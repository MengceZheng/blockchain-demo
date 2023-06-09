# 拥有节点同步验证功能的区块链

现已增加验证区块数据的功能，且增加一个对应接口，以获知目前区块链验证结果，见<http://localhost:8080/validate>：

```json
"Validation Success"
```

节点同步验证使用方式如下：

```console
~$ python blockchain.py -p 8080
~$ python blockchain.py -p 8081
```

添加节点，见<http://localhost:8080/nodes/add/localhost/8081>

```json
[
  {
    "ip": "localhost",
    "port": 8081
  }
]
```

在8081节点区块链中加一条新信息，见<http://localhost:8081/up/hello>：

```json
[
  {
    "Data": "Genesis Block",
    "Hash": "2c3776b2af0377c9c683852a16e6b1791523b919f48e2d2ac213f024a93693d9",
    "Index": 0,
    "PreHash": "0",
    "Timestamp": "Sat, 01 Oct 1949 15:00:00 GMT"
  },
  {
    "Data": "hello",
    "Hash": "55103f53d2cbfe1fdc4ead1a44e331177a403e3a4393d6bf0548d3879c856cac",
    "Index": 1,
    "PreHash": "2c3776b2af0377c9c683852a16e6b1791523b919f48e2d2ac213f024a93693d9",
    "Timestamp": "Wed, 07 Jun 2023 09:28:54 GMT"
  }
]
```

此时在浏览器打开地址<http://localhost:8080/blocks/all>，可见只有创世区块，并没有同步：

```json
[
  {
    "Data": "Genesis Block",
    "Hash": "2c3776b2af0377c9c683852a16e6b1791523b919f48e2d2ac213f024a93693d9",
    "Index": 0,
    "PreHash": "0",
    "Timestamp": "Sat, 01 Oct 1949 15:00:00 GMT"
  }
]
```

然后在8080节点中同步数据，<http://localhost:8080/blocks/sync>：

```json
"Synchronized"
```

可以在浏览器打开地址<http://localhost:8080/blocks/all>，说明8080节点的区块链已经验证8081节点的区块链，并且实现节点同步：

```json
[
  {
    "Data": "Genesis Block",
    "Hash": "2c3776b2af0377c9c683852a16e6b1791523b919f48e2d2ac213f024a93693d9",
    "Index": 0,
    "PreHash": "0",
    "Timestamp": "Sat, 01 Oct 1949 15:00:00 GMT"
  },
  {
    "Data": "hello",
    "Hash": "55103f53d2cbfe1fdc4ead1a44e331177a403e3a4393d6bf0548d3879c856cac",
    "Index": 1,
    "PreHash": "2c3776b2af0377c9c683852a16e6b1791523b919f48e2d2ac213f024a93693d9",
    "Timestamp": "Wed, 07 Jun 2023 09:28:54 GMT"
  }
]
```

注意：为使得初次节点同步总能成功，创世区块的时间戳已固定为某一时间（彩蛋）。
