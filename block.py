from hashlib import sha256
import datetime


class Block:

    def __init__(self,privious_hash,data,timestamp):
        self.privious_hash=privious_hash
        self.data=data
        self.timestamp=timestamp
        self.hash = self.get_hash()

    def genesis_block():
        return Block(0,0,datetime.datetime.now())

    def get_hash(self):
        blockdata= (str(self.privious_hash)+str(self.data)+str(self.timestamp)).encode()
        hash1 = sha256(blockdata).hexdigest()
        #hash2 = sha256(hash1).hexdigest()
        return hash1
