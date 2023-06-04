# 拥有各项功能的区块链浏览器

现已制作拥有各项功能的区块链浏览器，客户端可生成密钥对、生成签名、发送消息等，见[`client.py`](./client.py)。

功能说明如下：

```console
Usage: client.py [OPTIONS]

Options:
  -g                        Generate ECDSA key pair
  -s                        Send message using signature
  --host TEXT               Server host
  --port INTEGER            Server port
  -m, --message TEXT        Message to transmit
  -fa, --from-address TEXT  From address
  -ta, --to-address TEXT    To address
  -k, --private-key TEXT    Private key
  -o, --memo TEXT           Memo for message
  --help                    Show this message and exit.
```

使用方式类似，此处略去。区块链浏览器中已集成相关功能，如消息上链功能，见<http://localhost:8080/post>，成功上链后回显：

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
    "timestamp": "Sun, 04 Jun 2023 15:10:52 GMT",
    "data": {
      "from_address": "CdCq+Mw1nrvf+NRHzurBAiDDh5XuOmcjhp7+hV3TjDYkvzE248cwHcUedDdb4B+0Nir7QOxQ3ZPdkULnlQlZZQ==",
      "to_address": "CdCq+Mw1nrvf+NRHzurBAiDDh5XuOmcjhp7+hV3TjDYkvzE248cwHcUedDdb4B+0Nir7QOxQ3ZPdkULnlQlZZQ==",
      "message": "测试",
      "signature": "A9noPVXIzOPcEB1Vid1sUg5Y+Ppaf/0PqwMd7792C07GCAnsQVUIGqVPtKlYRLMRXQUinTZ5jYGHXcYolKp73Q==",
      "memo": "浏览器"
    },
    "previous_hash": "2c3776b2af0377c9c683852a16e6b1791523b919f48e2d2ac213f024a93693d9",
    "hash": "b83dde8003206c8d8032bceb7a79ffb79466ec4c040691d2f2557f9f254c5948"
  }
]
```

根据查询相关区块信息功能，见<http://localhost:8080/find>，如输入地址`CdCq+Mw1nrvf+NRHzurBAiDDh5XuOmcjhp7+hV3TjDYkvzE248cwHcUedDdb4B+0Nir7QOxQ3ZPdkULnlQlZZQ==`后回显：

```json
{
  "sent": [
    {
      "index": 1,
      "timestamp": "Sun, 04 Jun 2023 15:10:52 GMT",
      "data": {
        "from_address": "CdCq+Mw1nrvf+NRHzurBAiDDh5XuOmcjhp7+hV3TjDYkvzE248cwHcUedDdb4B+0Nir7QOxQ3ZPdkULnlQlZZQ==",
        "to_address": "CdCq+Mw1nrvf+NRHzurBAiDDh5XuOmcjhp7+hV3TjDYkvzE248cwHcUedDdb4B+0Nir7QOxQ3ZPdkULnlQlZZQ==",
        "message": "测试",
        "signature": "A9noPVXIzOPcEB1Vid1sUg5Y+Ppaf/0PqwMd7792C07GCAnsQVUIGqVPtKlYRLMRXQUinTZ5jYGHXcYolKp73Q==",
        "memo": "浏览器"
      },
      "previous_hash": "2c3776b2af0377c9c683852a16e6b1791523b919f48e2d2ac213f024a93693d9",
      "hash": "b83dde8003206c8d8032bceb7a79ffb79466ec4c040691d2f2557f9f254c5948"
    }
  ],
  "received": [
    {
      "index": 1,
      "timestamp": "Sun, 04 Jun 2023 15:10:52 GMT",
      "data": {
        "from_address": "CdCq+Mw1nrvf+NRHzurBAiDDh5XuOmcjhp7+hV3TjDYkvzE248cwHcUedDdb4B+0Nir7QOxQ3ZPdkULnlQlZZQ==",
        "to_address": "CdCq+Mw1nrvf+NRHzurBAiDDh5XuOmcjhp7+hV3TjDYkvzE248cwHcUedDdb4B+0Nir7QOxQ3ZPdkULnlQlZZQ==",
        "message": "测试",
        "signature": "A9noPVXIzOPcEB1Vid1sUg5Y+Ppaf/0PqwMd7792C07GCAnsQVUIGqVPtKlYRLMRXQUinTZ5jYGHXcYolKp73Q==",
        "memo": "浏览器"
      },
      "previous_hash": "2c3776b2af0377c9c683852a16e6b1791523b919f48e2d2ac213f024a93693d9",
      "hash": "b83dde8003206c8d8032bceb7a79ffb79466ec4c040691d2f2557f9f254c5948"
    }
  ]
}
```

当然，浏览器首页也提供查询功能，如输入地址`CdCq+Mw1nrvf+NRHzurBAiDDh5XuOmcjhp7+hV3TjDYkvzE248cwHcUedDdb4B+0Nir7QOxQ3ZPdkULnlQlZZQ==`后回显：

```text
Sent 1 logs
Timestamp: 2023-06-04 15:10:52.921134
To Address: CdCq+Mw1nrvf+NRHzurBAiDDh5XuOmcjhp7+hV3TjDYkvzE248cwHcUedDdb4B+0Nir7QOxQ3ZPdkULnlQlZZQ==
Message Sent: 测试

Received 1 logs
Timestamp: 2023-06-04 15:10:52.921134
From Address: CdCq+Mw1nrvf+NRHzurBAiDDh5XuOmcjhp7+hV3TjDYkvzE248cwHcUedDdb4B+0Nir7QOxQ3ZPdkULnlQlZZQ==
Received Message: 测试
```
