# 最简单的区块链（改进版）

在改进后的版本中，区块的表示改为一个名为`Block`的类。该类包含`data`（区块的数据）、`previous_hash`（前一个区块的哈希值）和`hash`（当前区块的哈希值）属性。`Block`类还有一个`calculate_hash`方法，用于计算区块的哈希值。

另外，引入一个名为`Blockchain`的类来表示整个区块链。该类有一个`chain`列表用于存储区块链中的所有区块。`Blockchain`类提供`create_genesis_block`方法用于创建创世区块，`add_block`方法用于添加新的区块，以及`get_chain_json`方法用于输出区块链的信息。

其中，`get_chain_json`方法遍历区块链中的每个区块，将每个区块的数据、前一个哈希值和本区块哈希值存储在一个字典中，并将这些字典添加到一个列表中。最后，使用`json.dumps`将列表转换为 JSON 字符串并返回。现在通过调用`blockchain.get_chain_json()`，将获得以 JSON 形式表示的区块链信息。

运行方法：

```console
~$ python3 blockchain.py
```

如果正常，可得到类似如下的返回：

```json
[
    {
        "Data": "This is the genesis block",
        "Previous Hash": "0",
        "Hash": "53d466806088078bfc3a8c4aacc39c9218e8f1bc12434d964ca796267c5c1288"
    },
    {
        "Data": "This is block 1",
        "Previous Hash": "53d466806088078bfc3a8c4aacc39c9218e8f1bc12434d964ca796267c5c1288",
        "Hash": "de64351534cc31667fb17ef2c90a16a31cb49d4dff48efe64181b46af42d0db2"
    },
    {
        "Data": "This is block 2",
        "Previous Hash": "de64351534cc31667fb17ef2c90a16a31cb49d4dff48efe64181b46af42d0db2",
        "Hash": "bb1be90ddadb65d57bd580d6bd1a6e0b6573842d0b748abb0cbb3a66288be076"
    },
    {
        "Data": "This is block 3",
        "Previous Hash": "bb1be90ddadb65d57bd580d6bd1a6e0b6573842d0b748abb0cbb3a66288be076",
        "Hash": "ed30cf1020e42340c8b371a63fbbbd34871b9cea64840b271e9ec969e113e977"
    }
]
```
