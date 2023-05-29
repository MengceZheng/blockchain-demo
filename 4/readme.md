# 拥有信息上链功能的区块链

代码中定义一个新的路由处理函数`add_blockchain_msg`，它接收名为`msg`的 URL 参数。在该处理函数中调用`blockchain.add_block(msg)`将`msg`信息添加到区块链中，并使用`jsonify(blockchain.get_chain_json())`将更新后的区块链以 JSON 格式返回给客户端。现在，可以通过发送 GET 请求到`/up/<msg>`的 URL，其中`<msg>`是想要上链的信息，可将该信息添加到区块链中。返回的响应将包含更新后的区块链数据。

运行这段代码后，可以通过访问<http://localhost:8080/up/hello>在浏览器中查看*hello*上链后的区块链信息。

如果正常，可得到类似如下的返回：

```json
[
  {
    "Index": 0,
    "Timestamp": "2023-05-29 19:42:00.535673",
    "Data": "This is the genesis block",
    "Previous Hash": "0",
    "Hash": "9e22e392d65a215441b8d566e1b2de1c3cd51bf7cebee3b781b2f1a9d6134cf2"
  },
  {
    "Index": 1,
    "Timestamp": "2023-05-29 19:42:00.535673",
    "Data": "This is block 1",
    "Previous Hash": "9e22e392d65a215441b8d566e1b2de1c3cd51bf7cebee3b781b2f1a9d6134cf2",
    "Hash": "2b65633997678a1e7b179b4e1adada105f7b885532ea5b2d01d43a6fa98dfc79"
  },
  {
    "Index": 2,
    "Timestamp": "2023-05-29 19:42:00.535673",
    "Data": "This is block 2",
    "Previous Hash": "2b65633997678a1e7b179b4e1adada105f7b885532ea5b2d01d43a6fa98dfc79",
    "Hash": "788865acf8dc529e1a7f3cd7e9754ff8ed237ff0c2ef9124cc0aea57b72b624c"
  },
  {
    "Index": 3,
    "Timestamp": "2023-05-29 19:42:00.535673",
    "Data": "This is block 3",
    "Previous Hash": "788865acf8dc529e1a7f3cd7e9754ff8ed237ff0c2ef9124cc0aea57b72b624c",
    "Hash": "384ed86f29f16b508eaf7ece6a4dc1ca29e1158d0f93d2033a7cf01c30e70454"
  },
  {
    "Index": 4,
    "Timestamp": "2023-05-29 19:45:28.159443",
    "Data": "hello",
    "Previous Hash": "384ed86f29f16b508eaf7ece6a4dc1ca29e1158d0f93d2033a7cf01c30e70454",
    "Hash": "e0c30506ae5cfa0bd6ea9a8d4bc46c10e878582fafdf16cdf63389e00211cb95"
  }
]
```
