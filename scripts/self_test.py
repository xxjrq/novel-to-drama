#!/usr/bin/env python3
import argparse, json, re, sys
from pathlib import Path

def convert(text):
    body=" ".join(x.strip() for x in text.splitlines() if x.strip() and not x.startswith("#"))
    if len(body)<35 or not re.search(r"[。！？]",body): raise ValueError("needs_more_source: 请提供包含人物和冲突的故事")
    return {"title":"未命名短剧","episode":1,"gaps":[],"scenes":[{"scene_id":"E01-S01","slugline":"待确认","goal":"推进主冲突","characters":[],"actions":[body[:36]],"dialogue":[],"conflict":{"obstacle":"待从原文确认","escalation":"待确认","result":"待确认"},"turn":"待确认","props":[],"ending_hook":"留下一个可拍摄的未决动作"}]}

def write(data,out):
    out.mkdir(parents=True,exist_ok=True); (out/"drama-script.json").write_text(json.dumps(data,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    s=data["scenes"][0]; lines=[f"# {data['title']}","",f"## {s['scene_id']} {s['slugline']}","",f"场次目标：{s['goal']}","", "### 动作"]+[f"- {a}" for a in s["actions"]]+["", "### 冲突", f"- 阻力：{s['conflict']['obstacle']}", f"- 升级：{s['conflict']['escalation']}", "", f"### 结尾钩子\n{s['ending_hook']}"]
    (out/"drama-script.md").write_text("\n".join(lines)+"\n",encoding="utf-8")

def main():
    p=argparse.ArgumentParser(); sub=p.add_subparsers(dest="cmd",required=True); sub.add_parser("self-test"); c=sub.add_parser("convert"); c.add_argument("--input",required=True); c.add_argument("--output",required=True); a=p.parse_args()
    if a.cmd=="self-test":
        root=Path(__file__).parents[1]; assert convert((root/"examples/success-input.md").read_text(encoding="utf-8"))["scenes"]
        try: convert((root/"examples/failure-input.md").read_text(encoding="utf-8"))
        except ValueError as e: assert str(e).startswith("needs_more_source")
        else: raise AssertionError("failure sample was accepted")
        print("self-test: PASS (scene conversion + failure sample)"); return
    try: write(convert(Path(a.input).read_text(encoding="utf-8")),Path(a.output))
    except (OSError,ValueError) as e: print(e,file=sys.stderr); return 1
    print("wrote drama-script.md and drama-script.json")
if __name__=="__main__": sys.exit(main() or 0)
