import hashlib
import json

class Block:
    def __init__(self, data, previous_hash):
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        sha = hashlib.sha256()
        sha.update(f"{self.data}{self.previous_hash}".encode("utf-8"))
        return sha.hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = []
        self.create_genesis_block()

    def create_genesis_block(self):
        data = "This is the genesis block"
        previous_hash = "0"
        self.chain.append(Block(data, previous_hash))

    def add_block(self, data):
        previous_block = self.chain[-1]
        previous_hash = previous_block.hash
        new_block = Block(data, previous_hash)
        self.chain.append(new_block)

    def get_chain_json(self):
        chain_json = []
        for block in self.chain:
            block_data = {
                "Data": block.data,
                "Previous Hash": block.previous_hash,
                "Hash": block.hash
            }
            chain_json.append(block_data)
        return json.dumps(chain_json, ensure_ascii=False, indent=4)

if __name__ == '__main__':
    # 创建一个区块链实例
    blockchain = Blockchain()

    # 添加一些区块
    blockchain.add_block("This is block 1")
    blockchain.add_block("This is block 2")
    blockchain.add_block("This is block 3")

    # 打印区块链信息
    print(blockchain.get_chain_json())
