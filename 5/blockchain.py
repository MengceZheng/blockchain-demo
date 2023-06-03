import hashlib
import json
import datetime
from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/up/<string:msg>', methods=['GET'])
def add_block(msg):
    blockchain.add_block(msg)
    return jsonify(blockchain.get_chain_json())

@app.route('/blocks/latest', methods=['GET'])
def get_latest_block():
    latest_block = blockchain.chain[-1]
    return jsonify(latest_block.__dict__)

@app.route('/blocks/<int:index>', methods=['GET'])
def get_block(index):
    if index < len(blockchain.chain):
        block = blockchain.chain[index]
        return jsonify(block.__dict__)
    else:
        return jsonify({"error": "noindex"})

@app.route('/blocks/<int:from_index>/<int:to_index>', methods=['GET'])
def get_block_from_to(from_index, to_index):
    if from_index < len(blockchain.chain) and to_index < len(blockchain.chain) and to_index >= from_index:
        blocks = [block.__dict__ for block in blockchain.chain[from_index:to_index+1]]
        return jsonify(blocks)
    else:
        return jsonify({"error": "noindex"})

@app.route('/blocks/all', methods=['GET'])
def get_all_block():
    blocks = [block.__dict__ for block in blockchain.chain]
    return jsonify(blocks)

if __name__ == '__main__':

    class Block:
        def __init__(self, index, timestamp, data, previous_hash):
            self.index = index
            self.timestamp = timestamp
            self.data = data
            self.previous_hash = previous_hash
            self.hash = self.calculate_hash()

        def calculate_hash(self):
            sha = hashlib.sha256()
            sha.update(f"{self.index}{self.timestamp}{self.data}{self.previous_hash}".encode("utf-8"))
            return sha.hexdigest()

    class Blockchain:
        def __init__(self):
            self.chain = []
            self.create_genesis_block()

        def create_genesis_block(self):
            index = 0
            timestamp = datetime.datetime.now()
            data = "Genesis Block"
            previous_hash = "0"
            self.chain.append(Block(index, timestamp, data, previous_hash))

        def add_block(self, data):
            previous_block = self.chain[-1]
            index = previous_block.index + 1
            timestamp = datetime.datetime.now()
            previous_hash = previous_block.hash
            new_block = Block(index, timestamp, data, previous_hash)
            self.chain.append(new_block)

        def get_chain_json(self):
            chain_json = [block.__dict__ for block in self.chain]
            return chain_json

    # 创建一个区块链实例
    blockchain = Blockchain()

    # 添加一些区块
    blockchain.add_block("2020900103")
    blockchain.add_block("郑梦策")
    blockchain.add_block("Well done!")
    
    # 设置 JSON 输出选项
    app.config['JSON_AS_ASCII']=False
    app.config['JSON_SORT_KEYS']=False

    # 网页端显示信息
    app.run(debug=True, host='0.0.0.0', port=8080)
