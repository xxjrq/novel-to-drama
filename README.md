# 小说改短剧

把小说片段拆成可排练的短剧场次，输出场次目标、动作、对白、冲突和结尾钩子，并同时生成 Markdown 与 JSON。

## 能做什么

- 把叙述性文字拆成有目标、阻力和变化的短剧场次。
- 用动作和对白推进冲突，减少无法拍摄的旁白解释。
- 同时输出 Markdown 剧本和结构化 JSON。

## 使用

```bash
python3 scripts/self_test.py convert --input examples/success-input.md --output ./out
```

请提供有主线冲突的文本和改编范围；资料不足时会列出缺口，不会硬编剧情。
