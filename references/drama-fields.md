# 短剧场次字段

根对象使用 `title`、`episode`、`scenes` 和 `gaps`。场次字段为 `scene_id`、`slugline`、`goal`、`characters`、`actions`、`dialogue`、`conflict`、`turn`、`props` 和 `ending_hook`。

`dialogue` 是 `{speaker, line}` 数组；`conflict` 至少包含 `obstacle`、`escalation`、`result`。结尾钩子要能拍出来，例如“门锁转动，屏幕显示失踪者来电”，避免抽象评价。
