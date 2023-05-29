# 拥有查询功能的区块链

对代码进行以下修改和优化：

- 将`blockchain`对象的实例化和添加初始区块的操作移至`if __name__ == '__main__':`的条件下，确保在直接运行脚本时才执行代码。
- 优化获取区块链信息的方法，将`get_chain_json()`方法改为返回字典形式的区块信息列表，以便在路由处理函数中进行 JSON 序列化。
- 在路由处理函数中，使用`block.__dict__`将区块对象转换为字典形式，以便进行 JSON 序列化。
- 修改路由处理函数的返回值，使用`jsonify`函数将数据转换为 JSON 格式进行返回输出。

访问全部区块时的地址为<http://localhost:8080/blocks/all>：

```json
[
  {
    "index": 0,
    "timestamp": "Mon, 29 May 2023 20:18:02 GMT",
    "data": "Genesis Block",
    "previous_hash": "0",
    "hash": "20591d8361f460eaef11a0396d3eef1be5f674e8573ff7069dc1c88a6c4e6c37"
  },
  {
    "index": 1,
    "timestamp": "Mon, 29 May 2023 20:18:02 GMT",
    "data": "2020900103",
    "previous_hash": "20591d8361f460eaef11a0396d3eef1be5f674e8573ff7069dc1c88a6c4e6c37",
    "hash": "17c841a355e8f238dce0de891a4ef40803eb0a1b5547d4e6d42490a233b94fa0"
  },
  {
    "index": 2,
    "timestamp": "Mon, 29 May 2023 20:18:02 GMT",
    "data": "郑梦策",
    "previous_hash": "17c841a355e8f238dce0de891a4ef40803eb0a1b5547d4e6d42490a233b94fa0",
    "hash": "62b7e86713c23067b97af17fb60b09bf5afc67d00fd459a12045d39dc9830362"
  },
  {
    "index": 3,
    "timestamp": "Mon, 29 May 2023 20:18:02 GMT",
    "data": "Well done!",
    "previous_hash": "62b7e86713c23067b97af17fb60b09bf5afc67d00fd459a12045d39dc9830362",
    "hash": "400845377f61d2e86210a4f96f326c00fb4d925061953cde6cc774caf443c40a"
  }
]
```

访问最新的区块时的地址为<http://localhost:8080/blocks/latest>：

```json
{
  "index": 3,
  "timestamp": "Mon, 29 May 2023 20:18:02 GMT",
  "data": "Well done!",
  "previous_hash": "62b7e86713c23067b97af17fb60b09bf5afc67d00fd459a12045d39dc9830362",
  "hash": "400845377f61d2e86210a4f96f326c00fb4d925061953cde6cc774caf443c40a"
}
```

访问索引为从 1 至 3 的区块时的地址为<http://localhost:8080/blocks/1/3>：

```json
[
  {
    "index": 1,
    "timestamp": "Mon, 29 May 2023 20:18:02 GMT",
    "data": "2020900103",
    "previous_hash": "20591d8361f460eaef11a0396d3eef1be5f674e8573ff7069dc1c88a6c4e6c37",
    "hash": "17c841a355e8f238dce0de891a4ef40803eb0a1b5547d4e6d42490a233b94fa0"
  },
  {
    "index": 2,
    "timestamp": "Mon, 29 May 2023 20:18:02 GMT",
    "data": "郑梦策",
    "previous_hash": "17c841a355e8f238dce0de891a4ef40803eb0a1b5547d4e6d42490a233b94fa0",
    "hash": "62b7e86713c23067b97af17fb60b09bf5afc67d00fd459a12045d39dc9830362"
  },
  {
    "index": 3,
    "timestamp": "Mon, 29 May 2023 20:18:02 GMT",
    "data": "Well done!",
    "previous_hash": "62b7e86713c23067b97af17fb60b09bf5afc67d00fd459a12045d39dc9830362",
    "hash": "400845377f61d2e86210a4f96f326c00fb4d925061953cde6cc774caf443c40a"
  }
]
```

访问索引为从 2 的区块时的地址为<http://localhost:8080/blocks/2>：

```json
{
  "index": 2,
  "timestamp": "Mon, 29 May 2023 20:18:02 GMT",
  "data": "郑梦策",
  "previous_hash": "17c841a355e8f238dce0de891a4ef40803eb0a1b5547d4e6d42490a233b94fa0",
  "hash": "62b7e86713c23067b97af17fb60b09bf5afc67d00fd459a12045d39dc9830362"
}
```
