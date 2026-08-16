import socket
#8byte header hex
header = "CB84000D001C001C"
source = header[0:4]
destination = header[4:8]
total = header[8:12]
checkSum = header[12:16]
source1 = int(source, 16)
destination1 = int(destination, 16)
total1 = int(total, 16)
checkSum1 = int(checkSum, 16)
data = total1-8 
print("source port : ",source1)
print("destination port : ",destination1)
print("total length data : ",total1)
print("check sum  : ",checkSum1)
print("legth data : ",data)
print("process name or protocol :",socket.getservbyport(destination1, 'udp'))