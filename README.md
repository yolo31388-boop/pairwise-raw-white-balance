# pairwise-raw-white-balance

## 领域

游戏、图形与多媒体

## 主题

RAW 自动白平衡

## 说明

分区估计、高光裁剪与逐帧增益限制。

初始状态下 `imaging/raw_white_balance.py` 中所有函数抛出 `NotImplementedError`，测试全部失败。
修复实现后运行：

```bash
python -m pytest -q
```

期望全部通过。
