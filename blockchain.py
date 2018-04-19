import block
from datetime import datetime
#print(block.Block.genesis_block().hash)
genesis=block.Block.genesis_block()
blockchain=[genesis]
data = input("enter multiple data and separate it using '-' :")
data_list=data.split("-")

for i in range (len(data_list)):
    #data=input("enter data:")
    priv_hash= blockchain[-1].hash
    #print(priv_hash)
    to_append = block.Block(priv_hash,data_list[i],datetime.now())
    blockchain.append(to_append)
    current_hash= to_append.hash
    #print(current_hash)
    print("data is {} , privious hash is---> {} , current hash is--->{}".format(data_list[i] , priv_hash , current_hash))
