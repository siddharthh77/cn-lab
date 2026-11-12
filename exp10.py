import socket
import struct

# Create raw socket
sock = socket.socket(
    socket.AF_PACKET,
    socket.SOCK_RAW,
    socket.htons(3)
)

print("RAW SOCKET PACKET CAPTURE")
print("Press Ctrl+C to stop")

while True:

    packet, addr = sock.recvfrom(65536)

    print("\n----------------------------")
    print("Packet Length:", len(packet))

    # Ethernet Header
    eth_header = packet[:14]

    eth = struct.unpack("!6s6sH", eth_header)

    dest_mac = ':'.join(
        '%02X' % b for b in eth[0]
    )

    src_mac = ':'.join(
        '%02X' % b for b in eth[1]
    )

    protocol = eth[2]

    print("\nEthernet Header")

    print("Destination MAC:", dest_mac)
    print("Source MAC:", src_mac)
    print("Protocol:", hex(protocol))

    # IPv4 Packet
    if protocol == 0x0800:

        ip_header = packet[14:34]

        iph = struct.unpack(
            "!BBHHHBBH4s4s",
            ip_header
        )

        version_ihl = iph[0]

        ihl = (version_ihl & 15) * 4

        ttl = iph[5]

        proto = iph[6]

        src_ip = socket.inet_ntoa(iph[8])

        dst_ip = socket.inet_ntoa(iph[9])

        print("\nIP Header")

        print("Source IP:", src_ip)
        print("Destination IP:", dst_ip)
        print("TTL:", ttl)
        print("Protocol:", proto)

        transport_offset = 14 + ihl

        # TCP
        if proto == 6:

            tcp_header = packet[
                transport_offset:transport_offset + 4
            ]

            source_port, dest_port = struct.unpack(
                "!HH", tcp_header
            )

            print("\nTCP Header")

            print("Source Port:", source_port)
            print("Destination Port:", dest_port)

        # UDP
        elif proto == 17:

            udp_header = packet[
                transport_offset:transport_offset + 8
            ]

            source_port, dest_port, length, checksum = (
                struct.unpack("!HHHH", udp_header)
            )

            print("\nUDP Header")

            print("Source Port:", source_port)
            print("Destination Port:", dest_port)

        # ICMP
        elif proto == 1:

            icmp_header = packet[
                transport_offset:transport_offset + 2
            ]

            icmp_type, code = struct.unpack(
                "!BB", icmp_header
            )

            print("\nICMP Header")

            print("Type:", icmp_type)
            print("Code:", code)

        else:

            print("Other Protocol")
