# 拥有数字签名功能的区块链

现已增加数字签名消息内容上链的功能，使用客户端可生成密钥对、发送消息等，见[`client.py`](./client.py)。

功能说明如下：

```console
Usage: client.py [OPTIONS]

Options:
  -g       Generate ECDSA key pair
  -s       Send message using signature
  -m TEXT  Message to transmit
  -f TEXT  From address
  -t TEXT  To address
  -k TEXT  Private key
  -o TEXT  Memo for message
  --help   Show this message and exit.
```

生成地址和私钥使用方式如下：

```console
python client.py -g

Address    : 0HgX/z9doySYXRP7CB8DAI8nwnYGEgOjEHNoY7I71v+jXovuiIIMiAYPsrew+32mpb30h5AgpR40qV5w7v9BXw==
Private key: 367d80eb91f4c2a07b984009f93bb7d9020dbb056e6463886b666dec13d3915d
```

签名消息上链使用方式如下：

```console
python client.py -s -m ECDSA数字签名 -f 0HgX/z9doySYXRP7CB8DAI8nwnYGEgOjEHNoY7I71v+jXovuiIIMiAYPsrew+32mpb30h5AgpR40qV5w7v9BXw== -t 0HgX/z9doySYXRP7CB8DAI8nwnYGEgOjEHNoY7I71v+jXovuiIIMiAYPsrew+32mpb30h5AgpR40qV5w7v9BXw== -k 367d80eb91f4c2a07b984009f93bb7d9020dbb056e6463886b666dec13d3915d -o memo_test
```

回显如下：

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
    "Data": {
      "from_address": "0HgX/z9doySYXRP7CB8DAI8nwnYGEgOjEHNoY7I71v+jXovuiIIMiAYPsrew+32mpb30h5AgpR40qV5w7v9BXw==",
      "memo": "memo_test",
      "message": "ECDSA\u6570\u5b57\u7b7e\u540d",
      "signature": "/F9OoWMIEYK5fY2wwsrxWhlBrhVEUgu8ekgDxNepeTgQPVfeAYAOfODtChDrhYwGIJM8NxBOy44LgwZEzuVreg==",
      "to_address": "0HgX/z9doySYXRP7CB8DAI8nwnYGEgOjEHNoY7I71v+jXovuiIIMiAYPsrew+32mpb30h5AgpR40qV5w7v9BXw=="
    },
    "Hash": "b312330db54b13c980ff83b948f3c1bfa24a8f25c06fdaff0294ec051fd13d8a",
    "Index": 1,
    "PreHash": "2c3776b2af0377c9c683852a16e6b1791523b919f48e2d2ac213f024a93693d9",
    "Timestamp": "Wed, 07 Jun 2023 10:00:08 GMT"
  }
]
```

也可在浏览器中查看，见<http://localhost:8080/blocks/all>：

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
    "Data": {
      "from_address": "0HgX/z9doySYXRP7CB8DAI8nwnYGEgOjEHNoY7I71v+jXovuiIIMiAYPsrew+32mpb30h5AgpR40qV5w7v9BXw==",
      "memo": "memo_test",
      "message": "ECDSA\u6570\u5b57\u7b7e\u540d",
      "signature": "/F9OoWMIEYK5fY2wwsrxWhlBrhVEUgu8ekgDxNepeTgQPVfeAYAOfODtChDrhYwGIJM8NxBOy44LgwZEzuVreg==",
      "to_address": "0HgX/z9doySYXRP7CB8DAI8nwnYGEgOjEHNoY7I71v+jXovuiIIMiAYPsrew+32mpb30h5AgpR40qV5w7v9BXw=="
    },
    "Hash": "b312330db54b13c980ff83b948f3c1bfa24a8f25c06fdaff0294ec051fd13d8a",
    "Index": 1,
    "PreHash": "2c3776b2af0377c9c683852a16e6b1791523b919f48e2d2ac213f024a93693d9",
    "Timestamp": "Wed, 07 Jun 2023 10:00:08 GMT"
  }
]
```
