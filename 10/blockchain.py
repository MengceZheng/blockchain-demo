import hashlib
import json
import datetime
from flask import Flask, render_template, jsonify, request
from argparse import ArgumentParser
import requests
import base64
import ecdsa

# 定义节点列表
nodes = []

app = Flask(__name__)

def get_logs_by_address(address):
    out_logs = []
    in_logs = []
    blocks = blockchain.chain
    for i in range(1, len(blocks)):
        block = blocks[i]
        data = block["Data"]
        if isinstance(data, str):
            pass
        elif address == data.get("from_address"):
            out_logs.append(block)
        if isinstance(data, str):
            pass
        elif address == data.get("to_address"):
            in_logs.append(block)
    return out_logs, in_logs

@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        address = request.form.get('address')
        out_logs, in_logs = get_logs_by_address(address)
        return render_template('index.html', out_logs=out_logs, in_logs=in_logs)
    elif request.method == 'GET':
        return render_template('index.html')

@app.route('/find', methods=['POST', 'GET'])
def find():
    if request.method == 'POST':
        address = request.form.get('address')
        out_logs, in_logs = get_logs_by_address(address)
        return jsonify({"sent": out_logs, "received": in_logs})
    elif request.method == 'GET':
        return render_template('find.html')

# 签名消息
def sign_ECDSA_msg(private_key, message):
    bmessage = message.encode()
    sk = ecdsa.SigningKey.from_string(bytes.fromhex(private_key), curve=ecdsa.SECP256k1)
    signature = base64.b64encode(sk.sign(bmessage))
    return signature, message

# 验证签名
def validate_signature(public_key, signature, message):
    public_key = base64.b64decode(public_key).hex()
    signature = base64.b64decode(signature)
    vk = ecdsa.VerifyingKey.from_string(bytes.fromhex(public_key), curve=ecdsa.SECP256k1)
    try:
        return vk.verify(signature, message.encode())
    except:
        return False

@app.route('/post', methods=['POST', 'GET'])
def post():
    if request.method == 'POST':
        from_address = request.form.get('from_address')
        to_address = request.form.get('to_address')
        private_key = request.form.get('private_key')
        memo = request.form.get('memo')
        message = request.form.get('message')
        signature = request.form.get('signature')
        # if sig doesnot exist
        if signature is None:
            signature, message = sign_ECDSA_msg(private_key, message)
            signature = signature.decode('utf-8')
        if validate_signature(from_address, signature, message):
            block_data = {
                "from_address": from_address,
                "to_address": to_address,
                "message": message,
                "signature": signature,
                "memo": memo
            }
            blockchain.add_block(block_data)
            return jsonify(blockchain.chain)
        else:
            return jsonify({"error": "invalid signature"})
    elif request.method == 'GET':
        return render_template('post.html')

@app.route('/up/<string:msg>', methods=['GET'])
def up_block(msg):
    blockchain.add_block(msg)
    return jsonify(blockchain.chain)

@app.route('/blocks/latest', methods=['GET'])
def get_latest_block():
    latest_block = blockchain.chain[-1]
    return jsonify(latest_block)

@app.route('/blocks/<int:index>', methods=['GET'])
def get_block(index):
    if index < len(blockchain.chain):
        block = blockchain.chain[index]
        return jsonify(block)
    else:
        return jsonify({"error": "noindex"})

@app.route('/blocks/<int:from_index>/<int:to_index>', methods=['GET'])
def get_block_from_to(from_index, to_index):
    if from_index < len(blockchain.chain) and to_index < len(blockchain.chain) and to_index >= from_index:
        blocks = [block for block in blockchain.chain[from_index:to_index+1]]
        return jsonify(blocks)
    else:
        return jsonify({"error": "noindex"})

@app.route('/blocks/all', methods=['GET'])
def get_all_block():
    return jsonify(blockchain.chain)

@app.route('/blocks/height', methods=['GET'])
def get_block_height():
    height = len(blockchain.chain) - 1
    return jsonify(height)

@app.route('/nodes', methods=['GET'])
def get_nodes():
    return jsonify(nodes)

@app.route('/nodes/add/<string:ip>/<int:port>', methods=['GET'])
def add_node(ip, port):
    node = {"ip": ip, "port": port}
    if node not in nodes:
        nodes.append(node)
    return jsonify(nodes)

# 验证区块链
def validate(blocks):
    is_valid = True
    previous_index = 0
    previous_hash = 0
    for block in blocks:
        index = block["Index"]
        hash = block["Hash"]
        if index > 0:
            if previous_index == index - 1:
                pass
            else:
                is_valid = False
            if previous_hash == block["PreHash"]:
                pass
            else:
                is_valid = False
            if is_valid:
                previous_index = index
                previous_hash = hash
        if index == 0:
            previous_index = index
            previous_hash = hash
            pass
    return is_valid

@app.route('/validate',methods=['GET'])
def blocks_validate():
    blocks = blockchain.chain
    if validate(blocks):
        return jsonify("Validation Success")
    else:
        return jsonify("Validation Failure")

@app.route('/blocks/sync', methods=['GET'])
def blocks_sync():
    for node in nodes:
        ip = node["ip"]
        port = node["port"]
        url_height = f"http://{ip}:{port}/blocks/height"
        url_all = f"http://{ip}:{port}/blocks/all"
        try:
            r_height = requests.get(url_height)
            height = int(r_height.json())
            self_index = len(blockchain.chain) - 1
            if height > self_index:
                r_blocks_all = requests.get(url_all)
                blocks = r_blocks_all.json()
                if validate(blocks):
                    blockchain.chain = [block for block in blocks]
                    return jsonify("Synchronized")
                else:
                    return jsonify("Validation Failure")
            else:
                return jsonify("Unsynchronized")
        except:
            return jsonify("error")
    return jsonify("no nodes")


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

        def to_dict(self):
            return {
                "Index": self.index,
                "Timestamp": self.timestamp,
                "Data": self.data,
                "PreHash": self.previous_hash,
                "Hash": self.hash
            }

    class Blockchain:
        def __init__(self):
            self.chain = []
            self.create_genesis_block() #固定创世区块

        def create_genesis_block(self):
            index = 0
            timestamp = datetime.datetime(1949, 10, 1, 15, 0, 0)
            data = "Genesis Block"
            previous_hash = "0"
            self.chain.append(Block(index, timestamp, data, previous_hash).to_dict())

        def add_block(self, data):
            previous_block = self.chain[-1]
            index = previous_block["Index"] + 1
            timestamp = datetime.datetime.now()
            previous_hash = previous_block["Hash"]
            new_block = Block(index, timestamp, data, previous_hash).to_dict()
            self.chain.append(new_block)

    # 创建一个区块链实例
    blockchain = Blockchain()
    
    # 设置 JSON 输出选项
    app.config['JSON_AS_ASCII']=False
    app.config['JSON_SORT_KEYS']=False

    # 创建命令行参数解析器
    parser = ArgumentParser()
    parser.add_argument('-p', '--port', default=8080, type=int, help='port to listen on')
    args = parser.parse_args()
    port = args.port

    # 网页端显示信息
    app.run(debug=True, host='0.0.0.0', port=port)
