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
    "Data": "Genesis Block",
    "Hash": "2c3776b2af0377c9c683852a16e6b1791523b919f48e2d2ac213f024a93693d9",
    "Index": 0,
    "PreHash": "0",
    "Timestamp": "Sat, 01 Oct 1949 15:00:00 GMT"
  },
  {
    "Data": {
      "from_address": "0HgX/z9doySYXRP7CB8DAI8nwnYGEgOjEHNoY7I71v+jXovuiIIMiAYPsrew+32mpb30h5AgpR40qV5w7v9BXw==",
      "memo": "browser",
      "message": "uploader",
      "signature": "b5pnQB55Z2sMytWN9F3NoptQjozXVkBK8AbAYQFSUGx0iPe6tIK+twmUtqR4xGJrvID2eEYAjF3y0xfiQIAFsw==",
      "to_address": "0HgX/z9doySYXRP7CB8DAI8nwnYGEgOjEHNoY7I71v+jXovuiIIMiAYPsrew+32mpb30h5AgpR40qV5w7v9BXw=="
    },
    "Hash": "74b7c334c9988c7374a992c56b1bd7eab2d830a24871ab9ec9251b400f5bd093",
    "Index": 1,
    "PreHash": "2c3776b2af0377c9c683852a16e6b1791523b919f48e2d2ac213f024a93693d9",
    "Timestamp": "Wed, 07 Jun 2023 10:12:02 GMT"
  }
]
```

根据查询相关区块信息功能，见<http://localhost:8080/find>，如输入地址`0HgX/z9doySYXRP7CB8DAI8nwnYGEgOjEHNoY7I71v+jXovuiIIMiAYPsrew+32mpb30h5AgpR40qV5w7v9BXw==`后回显：

```json
{
  "received": [
    {
      "Data": {
        "from_address": "0HgX/z9doySYXRP7CB8DAI8nwnYGEgOjEHNoY7I71v+jXovuiIIMiAYPsrew+32mpb30h5AgpR40qV5w7v9BXw==",
        "memo": "browser",
        "message": "uploader",
        "signature": "b5pnQB55Z2sMytWN9F3NoptQjozXVkBK8AbAYQFSUGx0iPe6tIK+twmUtqR4xGJrvID2eEYAjF3y0xfiQIAFsw==",
        "to_address": "0HgX/z9doySYXRP7CB8DAI8nwnYGEgOjEHNoY7I71v+jXovuiIIMiAYPsrew+32mpb30h5AgpR40qV5w7v9BXw=="
      },
      "Hash": "74b7c334c9988c7374a992c56b1bd7eab2d830a24871ab9ec9251b400f5bd093",
      "Index": 1,
      "PreHash": "2c3776b2af0377c9c683852a16e6b1791523b919f48e2d2ac213f024a93693d9",
      "Timestamp": "Wed, 07 Jun 2023 10:12:02 GMT"
    }
  ],
  "sent": [
    {
      "Data": {
        "from_address": "0HgX/z9doySYXRP7CB8DAI8nwnYGEgOjEHNoY7I71v+jXovuiIIMiAYPsrew+32mpb30h5AgpR40qV5w7v9BXw==",
        "memo": "browser",
        "message": "uploader",
        "signature": "b5pnQB55Z2sMytWN9F3NoptQjozXVkBK8AbAYQFSUGx0iPe6tIK+twmUtqR4xGJrvID2eEYAjF3y0xfiQIAFsw==",
        "to_address": "0HgX/z9doySYXRP7CB8DAI8nwnYGEgOjEHNoY7I71v+jXovuiIIMiAYPsrew+32mpb30h5AgpR40qV5w7v9BXw=="
      },
      "Hash": "74b7c334c9988c7374a992c56b1bd7eab2d830a24871ab9ec9251b400f5bd093",
      "Index": 1,
      "PreHash": "2c3776b2af0377c9c683852a16e6b1791523b919f48e2d2ac213f024a93693d9",
      "Timestamp": "Wed, 07 Jun 2023 10:12:02 GMT"
    }
  ]
}
```

当然，浏览器首页也提供查询功能，如输入地址`0HgX/z9doySYXRP7CB8DAI8nwnYGEgOjEHNoY7I71v+jXovuiIIMiAYPsrew+32mpb30h5AgpR40qV5w7v9BXw==`后回显：

```text
Sent 1 logs
Timestamp: 2023-06-07 10:16:12.303019
To Address: 0HgX/z9doySYXRP7CB8DAI8nwnYGEgOjEHNoY7I71v+jXovuiIIMiAYPsrew+32mpb30h5AgpR40qV5w7v9BXw==
Message Sent: uploader

Received 1 logs
Timestamp: 2023-06-07 10:16:12.303019
From Address: 0HgX/z9doySYXRP7CB8DAI8nwnYGEgOjEHNoY7I71v+jXovuiIIMiAYPsrew+32mpb30h5AgpR40qV5w7v9BXw==
Received Message: uploader
```
