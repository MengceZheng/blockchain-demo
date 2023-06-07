# 拥有节点同步功能的区块链

现已增加多个节点同步区块数据的功能，为方便同步数据，需增加一个对应接口，以获知目前区块链高度：<http://localhost:8080/blocks/height>，当目标节点区块链高度大于本地区块链高度时，执行同步功能。

添加节点接口为<http://localhost:8080/nodes/add/localhost/8081>

```json
[
  {
    "ip": "localhost",
    "port": 8081
  }
]
```

查看节点接口为<http://localhost:8080/nodes>：

```json
[
  {
    "ip": "localhost",
    "port": 8081
  }
]
```

测试时在8081节点区块链中加一条新信息，<http://localhost:8081/up/hello>：

```json
[
  {
    "Data": "Genesis Block",
    "Hash": "07cede23703424cfab54450d5de2c4d8d934b8ef3ef503d5831a9c8c1ac39196",
    "Index": 0,
    "PreHash": "0",
    "Timestamp": "Wed, 07 Jun 2023 09:05:21 GMT"
  },
  {
    "Data": "hello",
    "Hash": "d6130c2f1ecf97af9b4b1ae48f966bbf438caef4727c529d343cc36b13be585c",
    "Index": 1,
    "PreHash": "07cede23703424cfab54450d5de2c4d8d934b8ef3ef503d5831a9c8c1ac39196",
    "Timestamp": "Wed, 07 Jun 2023 09:05:40 GMT"
  }
]
```

然后在8080节点中同步数据，<http://localhost:8080/blocks/sync>：

```json
"Synchronized"
```
