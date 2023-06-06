# 拥有信息上链功能的区块链

代码中定义一个新的路由处理函数`add_blockchain_msg`，它接收名为`msg`的 URL 参数。在该处理函数中调用`blockchain.add_block(msg)`将`msg`信息添加到区块链中，并使用`jsonify(blockchain.get_chain_json())`将更新后的区块链以 JSON 格式返回给客户端。现在，可以通过发送 GET 请求到`/up/<msg>`的 URL，其中`<msg>`是想要上链的信息，可将该信息添加到区块链中。返回的响应将包含更新后的区块链数据。

运行这段代码后，可以通过访问<http://localhost:8080/up/hello>在浏览器中查看*hello*上链后的区块链信息。

如果正常，可得到类似如下的返回：

```json
[
  {
    "Index": 0,
    "Timestamp": "2023-06-06 10:56:42.001169",
    "Data": "Genesis Block",
    "Previous Hash": "0",
    "Hash": "5b5ea6e89bcc97f651c53a24be2273ba605b1bff2c6b786b3c6900542889a0fe"
  },
  {
    "Index": 1,
    "Timestamp": "2023-06-06 11:01:48.990767",
    "Data": "hello",
    "Previous Hash": "5b5ea6e89bcc97f651c53a24be2273ba605b1bff2c6b786b3c6900542889a0fe",
    "Hash": "61f5bbd2705c260bd8214b00a5c2fd5f74befadd922dcdc090b40e1fca9202f1"
  }
]
```

再通过访问<http://localhost:8080/up/hello>在浏览器中再次查看*hello*上链后的区块链信息：

```json
[
  {
    "Index": 0,
    "Timestamp": "2023-06-06 10:56:42.001169",
    "Data": "Genesis Block",
    "Previous Hash": "0",
    "Hash": "5b5ea6e89bcc97f651c53a24be2273ba605b1bff2c6b786b3c6900542889a0fe"
  },
  {
    "Index": 1,
    "Timestamp": "2023-06-06 11:01:48.990767",
    "Data": "hello",
    "Previous Hash": "5b5ea6e89bcc97f651c53a24be2273ba605b1bff2c6b786b3c6900542889a0fe",
    "Hash": "61f5bbd2705c260bd8214b00a5c2fd5f74befadd922dcdc090b40e1fca9202f1"
  },
  {
    "Index": 2,
    "Timestamp": "2023-06-06 11:02:40.348882",
    "Data": "hello",
    "Previous Hash": "61f5bbd2705c260bd8214b00a5c2fd5f74befadd922dcdc090b40e1fca9202f1",
    "Hash": "009dcf07cce57b90d0a9c6a2d1f4f8f5891a14e6f3b606c80e2f36de1d7ccdfe"
  }
]
```
