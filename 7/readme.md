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

测试时在8081节点区块链中加一条新信息，<http://127.0.0.1:8081/up/hello>：

```json
[
  {
    "index": 0,
    "timestamp": "Sat, 03 Jun 2023 17:07:57 GMT",
    "data": "Genesis Block",
    "previous_hash": "0",
    "hash": "fcbb7f9ac845fa075e7b3e80b8694d610583d94b1df9220295c94d2ad70a283c"
  },
  {
    "index": 1,
    "timestamp": "Sat, 03 Jun 2023 17:07:57 GMT",
    "data": "2020900103",
    "previous_hash": "fcbb7f9ac845fa075e7b3e80b8694d610583d94b1df9220295c94d2ad70a283c",
    "hash": "cbdc6bebbe4e5b3e8e98bc6aafb5baaef5a7691a24201c7a4e96430bba50ae7d"
  },
  {
    "index": 2,
    "timestamp": "Sat, 03 Jun 2023 17:07:57 GMT",
    "data": "郑梦策",
    "previous_hash": "cbdc6bebbe4e5b3e8e98bc6aafb5baaef5a7691a24201c7a4e96430bba50ae7d",
    "hash": "216b479184c2b0301d06d85bb2c07b7de482b1b1dd9dcd4681bbf50c233511b6"
  },
  {
    "index": 3,
    "timestamp": "Sat, 03 Jun 2023 17:07:57 GMT",
    "data": "Well done!",
    "previous_hash": "216b479184c2b0301d06d85bb2c07b7de482b1b1dd9dcd4681bbf50c233511b6",
    "hash": "e92619e98d95669c2877c4b5df05ebeaefb8442476a79df99539cb77b796534c"
  },
  {
    "index": 4,
    "timestamp": "Sat, 03 Jun 2023 17:18:22 GMT",
    "data": "hello",
    "previous_hash": "e92619e98d95669c2877c4b5df05ebeaefb8442476a79df99539cb77b796534c",
    "hash": "baef1372906ebc6c0b1fb37fde3a32ff907261c3978a7fb74ea9a8bb509c301f"
  }
]
```

然后在8080节点中同步数据，<http://localhost:8080/blocks/sync>：

```json
"Synchronized"
```
