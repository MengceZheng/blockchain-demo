# 拥有指定端口功能的区块链

现在可以在命令行中通过`-p`或`--port`参数来指定要监听的端口。例如，通过`python blockchain.py -p 12345`将会在`12345`端口上运行应用。如果没有指定端口，默认使用 8080 端口。

访问全部区块时的地址为<http://localhost:12345/blocks/all>：

```json
[
  {
    "index": 0,
    "timestamp": "Mon, 29 May 2023 20:39:43 GMT",
    "data": "Genesis Block",
    "previous_hash": "0",
    "hash": "fa8ef7324f4a02715bba306fb416539b220fc9a117d81117331aaefe98141045"
  },
  {
    "index": 1,
    "timestamp": "Mon, 29 May 2023 20:39:43 GMT",
    "data": "2020900103",
    "previous_hash": "fa8ef7324f4a02715bba306fb416539b220fc9a117d81117331aaefe98141045",
    "hash": "639feea55bb62d06cad3e8f9f9e3fc95f24c4c9e6f310056dd7153be2b07e636"
  },
  {
    "index": 2,
    "timestamp": "Mon, 29 May 2023 20:39:43 GMT",
    "data": "郑梦策",
    "previous_hash": "639feea55bb62d06cad3e8f9f9e3fc95f24c4c9e6f310056dd7153be2b07e636",
    "hash": "24b0f01445a55687845c0527605e0e95e0ff206a821fce82b38314168c1557d6"
  },
  {
    "index": 3,
    "timestamp": "Mon, 29 May 2023 20:39:43 GMT",
    "data": "Well done!",
    "previous_hash": "24b0f01445a55687845c0527605e0e95e0ff206a821fce82b38314168c1557d6",
    "hash": "117d4f4a8cf7cdbff8488650a1362b3c0f2831d1ef057f118d6dc7a148ef37d6"
  }
]
```
