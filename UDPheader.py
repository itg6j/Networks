import socket
import struct
# 8byte header hex
header = "CB84000D001C001C"
src_ip = "192.168.1.1"
dest_ip = "192.168.1.2"
source = header[0:4]
destination = header[4:8]
total = header[8:12]
checkSum = header[12:16]
source1 = int(source, 16)
destination1 = int(destination, 16)
total1 = int(total, 16)
checkSum1 = int(checkSum, 16)
data = total1 - 8
def calculate_checksum(data_bytes):
    if len(data_bytes) % 2 != 0:
        data_bytes += b"\x00"
    total_sum = 0
    for i in range(0, len(data_bytes), 2):
        word = (data_bytes[i] << 8) + data_bytes[i + 1]
        total_sum += word
    while total_sum >> 16:
        total_sum = (total_sum & 0xFFFF) + (total_sum >> 16)
    return ~total_sum & 0xFFFF
src_ip_bytes = bytes([int(x) for x in src_ip.split(".")])
dest_ip_bytes = bytes([int(x) for x in dest_ip.split(".")])
pseudo_header = src_ip_bytes + dest_ip_bytes + struct.pack("!BBH", 0, 17, total1)
udp_header_zero_checksum = struct.pack("!HHH", source1, destination1, total1) + b"\x00\x00"
payload = b"A" * data
full_packet = pseudo_header + udp_header_zero_checksum + payload
calculated_checksum = calculate_checksum(full_packet)
print("source port : ", source1)
print("destination port : ", destination1)
print("total length data : ", total1)
print("check sum  : ", checkSum1)
print("legth data : ", data)
print("process name or protocol :", socket.getservbyport(destination1, "udp"))
print("calculated check sum :", calculated_checksum)
print("calculated check sum (hex) :", hex(calculated_checksum))
