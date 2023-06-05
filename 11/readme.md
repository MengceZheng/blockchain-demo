# 基于区块链浏览器测试节点通信功能

基于区块链浏览器和客户端，测试两节点的生成密钥对、生成签名、发送消息、哈希上链等功能。

首先为两节点，即 8080 节点和 8081 节点生成密钥对：

```console
python client.py -g --host localhost --port 8080

User Host  : localhost
User Port  : 8080
Address    : 1SRSdJL2FegT2IaKBqNIV5YIL+5M3FWgzPnuB49Ns6xwyvba4GhXgcS9NpSmfcuGUBtXxDsuJP24LNpKLurinw==
Private key: 8a1eda6323a2d4dbb12742032b684a435b25080b0dac1722b47f0e43700c0260

python client.py -g --host localhost --port 8081

User Host  : localhost
User Port  : 8081
Address    : 85Z2GeaYHKLKadDzQCWqKGpxAy4U6y9Kt6UQvSabWIaXVR3OV6KcBE1R/uN3ODj6OE8vZaYKgZgjOOy5kb+ciQ==
Private key: 2ce51862f5648c3c7f8d2b890bba1b30b6e00db25e8caaceff93ae105ae9b837

```

然后分别开启 8080 节点和 8081 节点的区块链浏览器：

```console
python blockchain.py -p 8080
python blockchain.py -p 8081
```

此时两节点都只有创世区块：

```json
[
  {
    "index": 0,
    "timestamp": "Sat, 01 Oct 1949 15:00:00 GMT",
    "data": "Genesis Block",
    "previous_hash": "0",
    "hash": "2c3776b2af0377c9c683852a16e6b1791523b919f48e2d2ac213f024a93693d9"
  }
]
```

现在由 8080 节点为 8081 节点上传一条消息：

```console
python client.py -s --host localhost --port 8081 -fa 1SRSdJL2FegT2IaKBqNIV5YIL+5M3FWgzPnuB49Ns6xwyvba4GhXgcS9NpSmfcuGUBtXxDsuJP24LNpKLurinw== -ta 85Z2GeaYHKLKadDzQCWqKGpxAy4U6y9Kt6UQvSabWIaXVR3OV6KcBE1R/uN3ODj6OE8vZaYKgZgjOOy5kb+ciQ== -k 8a1eda6323a2d4dbb12742032b684a435b25080b0dac1722b47f0e43700c0260 -m 8080to8081 -o first
```

成功上链后回显如下，且可在 8081 浏览器中查看：

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
    "timestamp": "Mon, 05 Jun 2023 12:25:16 GMT",
    "data": {
      "from_address": "1SRSdJL2FegT2IaKBqNIV5YIL+5M3FWgzPnuB49Ns6xwyvba4GhXgcS9NpSmfcuGUBtXxDsuJP24LNpKLurinw==",
      "to_address": "85Z2GeaYHKLKadDzQCWqKGpxAy4U6y9Kt6UQvSabWIaXVR3OV6KcBE1R/uN3ODj6OE8vZaYKgZgjOOy5kb+ciQ==",
      "hash_message": "8cc18ab4f8ad319821838ad48b0ccd2f2e13d831c9484c928cb1e4a6"
    },
    "previous_hash": "2c3776b2af0377c9c683852a16e6b1791523b919f48e2d2ac213f024a93693d9",
    "hash": "751bbbf6ea147a8117bf2f08ec33458e62dde90f07b48618543fc0fc8ba220b2"
  }
]
```

在 8080 节点浏览器中可通过添加节点和节点同步操作得到上述区块链：

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
    "timestamp": "Sun, 04 Jun 2023 17:03:35 GMT",
    "data": {
      "from_address": "1SRSdJL2FegT2IaKBqNIV5YIL+5M3FWgzPnuB49Ns6xwyvba4GhXgcS9NpSmfcuGUBtXxDsuJP24LNpKLurinw==",
      "to_address": "85Z2GeaYHKLKadDzQCWqKGpxAy4U6y9Kt6UQvSabWIaXVR3OV6KcBE1R/uN3ODj6OE8vZaYKgZgjOOy5kb+ciQ==",
      "hash_message": "8cc18ab4f8ad319821838ad48b0ccd2f2e13d831c9484c928cb1e4a6"
    },
    "previous_hash": "2c3776b2af0377c9c683852a16e6b1791523b919f48e2d2ac213f024a93693d9",
    "hash": "78963fd0bb71bcb9f151b42de186e1676446e4ae1f35501845bdcbdb86cb941b"
  }
]
```

现在由 8081 节点为 8080 节点上传一条消息：

```console
python client.py -s --host localhost --port 8080 -fa 1SRSdJL2FegT2IaKBqNIV5YIL+5M3FWgzPnuB49Ns6xwyvba4GhXgcS9NpSmfcuGUBtXxDsuJP24LNpKLurinw== -ta 85Z2GeaYHKLKadDzQCWqKGpxAy4U6y9Kt6UQvSabWIaXVR3OV6KcBE1R/uN3ODj6OE8vZaYKgZgjOOy5kb+ciQ== -k 8a1eda6323a2d4dbb12742032b684a435b25080b0dac1722b47f0e43700c0260 -m 8080to8081 -o first
```

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
    "timestamp": "Mon, 05 Jun 2023 12:25:16 GMT",
    "data": {
      "from_address": "1SRSdJL2FegT2IaKBqNIV5YIL+5M3FWgzPnuB49Ns6xwyvba4GhXgcS9NpSmfcuGUBtXxDsuJP24LNpKLurinw==",
      "to_address": "85Z2GeaYHKLKadDzQCWqKGpxAy4U6y9Kt6UQvSabWIaXVR3OV6KcBE1R/uN3ODj6OE8vZaYKgZgjOOy5kb+ciQ==",
      "hash_message": "8cc18ab4f8ad319821838ad48b0ccd2f2e13d831c9484c928cb1e4a6"
    },
    "previous_hash": "2c3776b2af0377c9c683852a16e6b1791523b919f48e2d2ac213f024a93693d9",
    "hash": "751bbbf6ea147a8117bf2f08ec33458e62dde90f07b48618543fc0fc8ba220b2"
  },
  {
    "index": 2,
    "timestamp": "Mon, 05 Jun 2023 12:26:25 GMT",
    "data": {
      "from_address": "85Z2GeaYHKLKadDzQCWqKGpxAy4U6y9Kt6UQvSabWIaXVR3OV6KcBE1R/uN3ODj6OE8vZaYKgZgjOOy5kb+ciQ==",
      "to_address": "1SRSdJL2FegT2IaKBqNIV5YIL+5M3FWgzPnuB49Ns6xwyvba4GhXgcS9NpSmfcuGUBtXxDsuJP24LNpKLurinw==",
      "hash_message": "8d9fe5e17cea6d3866b2206266e330c6e31826dc459fbc28a81ecf51"
    },
    "previous_hash": "751bbbf6ea147a8117bf2f08ec33458e62dde90f07b48618543fc0fc8ba220b2",
    "hash": "2ce92db9c41d6e32ec1115e57b3485a39d7282bcaaa7438dd33c27069623929c"
  }
]
```

类似的，在 8081 节点浏览器中可通过添加节点和节点同步操作得到上述区块链：

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
    "timestamp": "Mon, 05 Jun 2023 12:25:16 GMT",
    "data": {
      "from_address": "1SRSdJL2FegT2IaKBqNIV5YIL+5M3FWgzPnuB49Ns6xwyvba4GhXgcS9NpSmfcuGUBtXxDsuJP24LNpKLurinw==",
      "to_address": "85Z2GeaYHKLKadDzQCWqKGpxAy4U6y9Kt6UQvSabWIaXVR3OV6KcBE1R/uN3ODj6OE8vZaYKgZgjOOy5kb+ciQ==",
      "hash_message": "8cc18ab4f8ad319821838ad48b0ccd2f2e13d831c9484c928cb1e4a6"
    },
    "previous_hash": "2c3776b2af0377c9c683852a16e6b1791523b919f48e2d2ac213f024a93693d9",
    "hash": "751bbbf6ea147a8117bf2f08ec33458e62dde90f07b48618543fc0fc8ba220b2"
  },
  {
    "index": 2,
    "timestamp": "Mon, 05 Jun 2023 12:26:25 GMT",
    "data": {
      "from_address": "85Z2GeaYHKLKadDzQCWqKGpxAy4U6y9Kt6UQvSabWIaXVR3OV6KcBE1R/uN3ODj6OE8vZaYKgZgjOOy5kb+ciQ==",
      "to_address": "1SRSdJL2FegT2IaKBqNIV5YIL+5M3FWgzPnuB49Ns6xwyvba4GhXgcS9NpSmfcuGUBtXxDsuJP24LNpKLurinw==",
      "hash_message": "8d9fe5e17cea6d3866b2206266e330c6e31826dc459fbc28a81ecf51"
    },
    "previous_hash": "751bbbf6ea147a8117bf2f08ec33458e62dde90f07b48618543fc0fc8ba220b2",
    "hash": "2ce92db9c41d6e32ec1115e57b3485a39d7282bcaaa7438dd33c27069623929c"
  }
]
```

根据查询相关区块信息功能，见<http://localhost:8080/find>或<http://localhost:8081/find>，如输入地址`1SRSdJL2FegT2IaKBqNIV5YIL+5M3FWgzPnuB49Ns6xwyvba4GhXgcS9NpSmfcuGUBtXxDsuJP24LNpKLurinw==`后回显：

```json
{
  "sent": [
    {
      "index": 1,
      "timestamp": "Mon, 05 Jun 2023 12:25:16 GMT",
      "data": {
        "from_address": "1SRSdJL2FegT2IaKBqNIV5YIL+5M3FWgzPnuB49Ns6xwyvba4GhXgcS9NpSmfcuGUBtXxDsuJP24LNpKLurinw==",
        "to_address": "85Z2GeaYHKLKadDzQCWqKGpxAy4U6y9Kt6UQvSabWIaXVR3OV6KcBE1R/uN3ODj6OE8vZaYKgZgjOOy5kb+ciQ==",
        "hash_message": "8cc18ab4f8ad319821838ad48b0ccd2f2e13d831c9484c928cb1e4a6"
      },
      "previous_hash": "2c3776b2af0377c9c683852a16e6b1791523b919f48e2d2ac213f024a93693d9",
      "hash": "751bbbf6ea147a8117bf2f08ec33458e62dde90f07b48618543fc0fc8ba220b2"
    }
  ],
  "received": [
    {
      "index": 2,
      "timestamp": "Mon, 05 Jun 2023 12:26:25 GMT",
      "data": {
        "from_address": "85Z2GeaYHKLKadDzQCWqKGpxAy4U6y9Kt6UQvSabWIaXVR3OV6KcBE1R/uN3ODj6OE8vZaYKgZgjOOy5kb+ciQ==",
        "to_address": "1SRSdJL2FegT2IaKBqNIV5YIL+5M3FWgzPnuB49Ns6xwyvba4GhXgcS9NpSmfcuGUBtXxDsuJP24LNpKLurinw==",
        "hash_message": "8d9fe5e17cea6d3866b2206266e330c6e31826dc459fbc28a81ecf51"
      },
      "previous_hash": "751bbbf6ea147a8117bf2f08ec33458e62dde90f07b48618543fc0fc8ba220b2",
      "hash": "2ce92db9c41d6e32ec1115e57b3485a39d7282bcaaa7438dd33c27069623929c"
    }
  ]
}
```
