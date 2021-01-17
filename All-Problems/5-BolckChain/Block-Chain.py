import hashlib
import datetime
class Block:
    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()
        self.next = None
    def calc_hash(self):
        sha = hashlib.sha256()
        sha.update(self.data.encode('utf-8'))
        return sha.hexdigest()
    def __repr__(self):
        return str(self.timestamp) + str(" | ") + str(self.data) + str(" | ") + str(self.previous_hash) + str(" | ") + str(self.hash)
class BlockChain(object):
    def __init__(self):
        self.head = None
        self.tail = None
    def appendBlock(self, data):
        if data is None or data == "":
            return
        elif self.head is None:
            self.head = Block(datetime.datetime.utcnow(), data, 0)
            self.tail = self.head
        else:
            self.tail.next = Block(datetime.datetime.utcnow(), data, self.tail.hash)
            self.tail = self.tail.next
        return
    def toList(self):
        out = []
        block = self.head
        while block:
            out.append([block])
            block = block.next
        return out
def main():
    # Test Case 1
    bl = BlockChain()
    data1 = "First Blockchain block"
    data2 = "Second Blockchain block"
    data3 = "Third Blockchain block"
    bl.appendBlock(data1)
    bl.appendBlock(data2)
    bl.appendBlock(data3)
    print(bl.toList()) # prints block chain
    # Test Case 2
    bl1 = BlockChain()
    bl1.appendBlock("")
    bl1.appendBlock("")
    print(bl1.toList())  # prints empty block chain as there was no data passed
    #Test Case 3
    bl2 = BlockChain()
    bl2.appendBlock(None)
    bl2.appendBlock(None)
    print(bl2.toList())  # prints empty block chain as there was no data passed
if __name__ == "__main__":
    main()