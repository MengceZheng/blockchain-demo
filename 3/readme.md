# 基于Flask框架拥有Web界面的区块链

代码中将`/`路由指定为根路由，并将`HTTP`请求方法设置为`GET`。当访问根路由时，会调用`get_blockchain`函数来获取区块链的信息。在`get_blockchain`函数中，使用`jsonify`函数将区块链信息转换为 JSON 格式，并作为响应返回。

运行这段代码后，可以通过访问<http://localhost:8080>在浏览器中查看区块链的信息。

如果正常，可得到类似如下的返回：

```json
[
  {
    "Index": 0,
    "Timestamp": "2023-05-29 19:23:09.913664",
    "Data": "This is the genesis block",
    "Previous Hash": "0",
    "Hash": "7470fa6ac8b924c3393e8c78b1ac63948bcee76d3b580cf421f5ccee75432b55"
  },
  {
    "Index": 1,
    "Timestamp": "2023-05-29 19:23:09.913664",
    "Data": "This is block 1",
    "Previous Hash": "7470fa6ac8b924c3393e8c78b1ac63948bcee76d3b580cf421f5ccee75432b55",
    "Hash": "f00f5efb7936bb19813ee347e0fedd60be8e6b8a334c6ab99b7efc4a71256555"
  },
  {
    "Index": 2,
    "Timestamp": "2023-05-29 19:23:09.913664",
    "Data": "This is block 2",
    "Previous Hash": "f00f5efb7936bb19813ee347e0fedd60be8e6b8a334c6ab99b7efc4a71256555",
    "Hash": "7fa33f7f32adb10f060b59b893242bd80277f1f2ac58aced0f16c9bf7a5ce418"
  },
  {
    "Index": 3,
    "Timestamp": "2023-05-29 19:23:09.913664",
    "Data": "This is block 3",
    "Previous Hash": "7fa33f7f32adb10f060b59b893242bd80277f1f2ac58aced0f16c9bf7a5ce418",
    "Hash": "a0ad33b0842a7d6297f748210bfb1325b8553bc5eda10f81864edbe60fc84740"
  }
]
```
