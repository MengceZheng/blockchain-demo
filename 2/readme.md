# 附带索引和时间戳的区块链

在更新后的代码中，`Block`类添加`index`和`timestamp`字段。其中`index`表示区块的索引，`timestamp`表示区块的时间戳。`Blockchain`类中的方法也相应地进行修改，以在创建区块和添加区块时设置正确的`index`和`timestamp`值。

如果正常，可得到类似如下的返回：

```json
[
    {
        "Index": 0,
        "Timestamp": "2023-05-29 13:11:08.390695",
        "Data": "This is the genesis block",
        "Previous Hash": "0",
        "Hash": "cc25d15433256d6ff9b5497a43fc6f50fe124ec128beafe404fc299e3afef36d"
    },
    {
        "Index": 1,
        "Timestamp": "2023-05-29 13:11:08.391693",
        "Data": "This is block 1",
        "Previous Hash": "cc25d15433256d6ff9b5497a43fc6f50fe124ec128beafe404fc299e3afef36d",
        "Hash": "a2e85da154d5c4d8757a574d2aa5108e1bf5002067d3b57049b71be78f13dd54"
    },
    {
        "Index": 2,
        "Timestamp": "2023-05-29 13:11:08.391693",
        "Data": "This is block 2",
        "Previous Hash": "a2e85da154d5c4d8757a574d2aa5108e1bf5002067d3b57049b71be78f13dd54",
        "Hash": "1f819bf4ed7cbcee81e69d4cda5060d650797cea0f5c58b4343ace740cb30df0"
    },
    {
        "Index": 3,
        "Timestamp": "2023-05-29 13:11:08.391693",
        "Data": "This is block 3",
        "Previous Hash": "1f819bf4ed7cbcee81e69d4cda5060d650797cea0f5c58b4343ace740cb30df0",
        "Hash": "359f0389de0cb5d55743859bd7417e00eaae33c9bc1c67577d4e94e6bc9e99d7"
    }
]
```
