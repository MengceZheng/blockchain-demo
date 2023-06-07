# 拥有指定端口功能的区块链

现在可以在命令行中通过`-p`或`--port`参数来指定要监听的端口。例如，通过`python blockchain.py -p 12345`将会在`12345`端口上运行应用。如果没有指定端口，默认使用 8080 端口。

访问全部区块时的地址为<http://localhost:12345/blocks/all>：

```json
[
  {
    "Data": "Genesis Block",
    "Hash": "52ec2df3cee3af7d1896de9853e73672270c6852b8df10706ab84aa72f92e08a",
    "Index": 0,
    "PreHash": "0",
    "Timestamp": "Wed, 07 Jun 2023 08:53:36 GMT"
  }
]
```
