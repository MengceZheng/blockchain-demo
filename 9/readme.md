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
client.py -s -m ECDSA数字签名 -f 0HgX/z9doySYXRP7CB8DAI8nwnYGEgOjEHNoY7I71v+jXovuiIIMiAYPsrew+32mpb30h5AgpR40qV5w7v9BXw== -t 0HgX/z9doySYXRP7CB8DAI8nwnYGEgOjEHNoY7I71v+jXovuiIIMiAYPsrew+32mpb30h5AgpR40qV5w7v9BXw== -k 367d80eb91f4c2a07b984009f93bb7d9020dbb056e6463886b666dec13d3915d -o memo_test
```

回显如下：

```json
[
  {
    "index": 0,
    "timestamp": "Sat, 01 Oct 1949 15:00:00 GMT",
    "data": "Genesis Block",
    "previous_hash": "0",
    "hash": "2c3776b2af0377c9c683852a16e6b1791523b919f48e2d2ac213f024a93693d9"
  },
  {
    "index": 1,
    "timestamp": "Sat, 03 Jun 2023 20:59:16 GMT",
    "data": {
      "from_address": "0HgX/z9doySYXRP7CB8DAI8nwnYGEgOjEHNoY7I71v+jXovuiIIMiAYPsrew+32mpb30h5AgpR40qV5w7v9BXw==",
      "to_address": "0HgX/z9doySYXRP7CB8DAI8nwnYGEgOjEHNoY7I71v+jXovuiIIMiAYPsrew+32mpb30h5AgpR40qV5w7v9BXw==",
      "message": "ECDSA数字签名",
      "signature": "6flsF55K3CMiiIE0z/uLsvi/AnOSMb4SggrPjU213Puy2PN23fYrIxgyl12KGvTkqi55D/vkXY6t1q+V9UWB1A==",
      "memo": "memo_test"
    },
    "previous_hash": "2c3776b2af0377c9c683852a16e6b1791523b919f48e2d2ac213f024a93693d9",
    "hash": "fac16f5fed277cb07eb8bab6553730d1f06b2c89d8b83ffa60b129039279da49"
  }
]
```

也可在浏览器中查看，见<http://localhost:8080/blocks/all>：

```json
[
  {
    "index": 0,
    "timestamp": "Sat, 01 Oct 1949 15:00:00 GMT",
    "data": "Genesis Block",
    "previous_hash": "0",
    "hash": "2c3776b2af0377c9c683852a16e6b1791523b919f48e2d2ac213f024a93693d9"
  },
  {
    "index": 1,
    "timestamp": "Sat, 03 Jun 2023 20:59:16 GMT",
    "data": {
      "from_address": "0HgX/z9doySYXRP7CB8DAI8nwnYGEgOjEHNoY7I71v+jXovuiIIMiAYPsrew+32mpb30h5AgpR40qV5w7v9BXw==",
      "to_address": "0HgX/z9doySYXRP7CB8DAI8nwnYGEgOjEHNoY7I71v+jXovuiIIMiAYPsrew+32mpb30h5AgpR40qV5w7v9BXw==",
      "message": "ECDSA数字签名",
      "signature": "6flsF55K3CMiiIE0z/uLsvi/AnOSMb4SggrPjU213Puy2PN23fYrIxgyl12KGvTkqi55D/vkXY6t1q+V9UWB1A==",
      "memo": "memo_test"
    },
    "previous_hash": "2c3776b2af0377c9c683852a16e6b1791523b919f48e2d2ac213f024a93693d9",
    "hash": "fac16f5fed277cb07eb8bab6553730d1f06b2c89d8b83ffa60b129039279da49"
  }
]
```
