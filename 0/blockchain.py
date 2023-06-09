#!/usr/bin/python
# -*- coding:utf-8 -*-
import hashlib
import json

blockchain = []


def hash_block(data, previous_hash):
    sha = hashlib.sha256()
    sha.update("{0}{1}".format(data, previous_hash).encode("utf8"))
    return sha.hexdigest()


def make_a_block(data, previous_hash):
    block = {"data": data, "previous_hash": previous_hash, "hash": hash_block(data, previous_hash)}
    return block


def add_a_block(data):
    last_block = blockchain[len(blockchain) - 1]
    previous_hash = last_block["hash"]
    blockchain.append(make_a_block(data, previous_hash))


def make_a_genesis_block():
    data = "this is the genesis block"
    previous_hash = 0
    blockchain.append(make_a_block(data, previous_hash))


if __name__ == '__main__':
    make_a_genesis_block()
    add_a_block("this is block 1")
    add_a_block("this is block 2")
    add_a_block("this is block 3")
    print(json.dumps(blockchain, ensure_ascii=False, indent=1))
