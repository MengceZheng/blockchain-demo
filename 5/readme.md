# 拥有查询功能的区块链

对代码进行以下修改和优化：

- 将 `blockchain` 对象的实例化和添加初始区块的操作移至 `if __name__ == '__main__':` 的条件下，确保在直接运行脚本时才执行代码。
- 优化获取区块链信息的方法，区块提供 `to_dict` 方法，返回字典形式的区块信息列表，以便在路由处理函数中进行 JSON 序列化。
- 修改路由处理函数的返回值，使用 `jsonify` 函数将数据转换为 JSON 格式进行返回输出。

三条信息上链后，访问全部区块时的地址为<http://localhost:8080/blocks/all>：

```json
[
  {
    "Index": 0,
    "Timestamp": "Tue, 06 Jun 2023 20:52:26 GMT",
    "Data": "Genesis Block",
    "PreHash": "0",
    "Hash": "5af830574cabab6ef14e01857783e3ac30e810379a26c16833e72fe2001ffbed"
  },
  {
    "Index": 1,
    "Timestamp": "Tue, 06 Jun 2023 20:52:48 GMT",
    "Data": "2020900103",
    "PreHash": "5af830574cabab6ef14e01857783e3ac30e810379a26c16833e72fe2001ffbed",
    "Hash": "bc0f6e96b35bfaf9bf638b7c2cab37e7fa6f5e5ad07aa7902237e6ce95d09e46"
  },
  {
    "Index": 2,
    "Timestamp": "Tue, 06 Jun 2023 20:52:54 GMT",
    "Data": "郑梦策",
    "PreHash": "bc0f6e96b35bfaf9bf638b7c2cab37e7fa6f5e5ad07aa7902237e6ce95d09e46",
    "Hash": "2eb14450b9d1c92bb023b92630e68758c79c40377d8d1a53571b76f6987a99f6"
  },
  {
    "Index": 3,
    "Timestamp": "Tue, 06 Jun 2023 20:53:14 GMT",
    "Data": "2023-06-06",
    "PreHash": "2eb14450b9d1c92bb023b92630e68758c79c40377d8d1a53571b76f6987a99f6",
    "Hash": "d687c3e2245a7c56ca1697e9c52a40a19e1d43a6487b8c0b623be457eb5f85ea"
  }
]
```

访问最新的区块时的地址为<http://localhost:8080/blocks/latest>：

```json
{
  "Index": 3,
  "Timestamp": "Tue, 06 Jun 2023 20:53:14 GMT",
  "Data": "2023-06-06",
  "PreHash": "2eb14450b9d1c92bb023b92630e68758c79c40377d8d1a53571b76f6987a99f6",
  "Hash": "d687c3e2245a7c56ca1697e9c52a40a19e1d43a6487b8c0b623be457eb5f85ea"
}
```

访问索引为从 1 至 3 的区块时的地址为<http://localhost:8080/blocks/1/3>：

```json
[
  {
    "Index": 1,
    "Timestamp": "Tue, 06 Jun 2023 20:52:48 GMT",
    "Data": "2020900103",
    "PreHash": "5af830574cabab6ef14e01857783e3ac30e810379a26c16833e72fe2001ffbed",
    "Hash": "bc0f6e96b35bfaf9bf638b7c2cab37e7fa6f5e5ad07aa7902237e6ce95d09e46"
  },
  {
    "Index": 2,
    "Timestamp": "Tue, 06 Jun 2023 20:52:54 GMT",
    "Data": "郑梦策",
    "PreHash": "bc0f6e96b35bfaf9bf638b7c2cab37e7fa6f5e5ad07aa7902237e6ce95d09e46",
    "Hash": "2eb14450b9d1c92bb023b92630e68758c79c40377d8d1a53571b76f6987a99f6"
  },
  {
    "Index": 3,
    "Timestamp": "Tue, 06 Jun 2023 20:53:14 GMT",
    "Data": "2023-06-06",
    "PreHash": "2eb14450b9d1c92bb023b92630e68758c79c40377d8d1a53571b76f6987a99f6",
    "Hash": "d687c3e2245a7c56ca1697e9c52a40a19e1d43a6487b8c0b623be457eb5f85ea"
  }
]
```

访问索引为从 2 的区块时的地址为<http://localhost:8080/blocks/2>：

```json
{
  "Index": 2,
  "Timestamp": "Tue, 06 Jun 2023 20:52:54 GMT",
  "Data": "郑梦策",
  "PreHash": "bc0f6e96b35bfaf9bf638b7c2cab37e7fa6f5e5ad07aa7902237e6ce95d09e46",
  "Hash": "2eb14450b9d1c92bb023b92630e68758c79c40377d8d1a53571b76f6987a99f6"
}
```
