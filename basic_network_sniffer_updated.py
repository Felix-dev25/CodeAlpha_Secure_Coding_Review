""" Pylint is a static code analysis tool for Python that helps identify errors,
enforce coding standards, and improve code quality.
It adheres to the PEP8 style guide and assigns a score to your code based on its
quality."""
# Analyzing basic_network_sniffer_updated.py code using pylint
from scapy.layers.inet import IP, ICMP
from scapy.all import sniff, Raw, sr1


def summary_packet_callback(packet):
    """ Display a summary of all decoded packets """
    print(packet.summary())

sniff(prn=summary_packet_callback, count=20)

print ("*********************")

print (" Source and destination ")

def sd_packet_callback(packet):
    """ Display source and destination IPs """
    if IP in packet:
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        print(f"Source IP: {src_ip} → Destination IP: {dst_ip}")

sniff(prn=sd_packet_callback, count=10)

print ("*********************")

print ("UDP connections")

def udp_packet_callback(packet):
    """ Display UDP connections """
    if packet.haslayer("UDP"):
        print(packet.summary())

sniff(filter = "udp", prn=udp_packet_callback, count=10)

print ("*********************")

print ("TCP connections ")

def tcp_packet_callback(packet):
    """ Display TCP connections """
    if packet.haslayer("TCP"):
        print(packet.summary())

sniff(filter = "tcp", prn=tcp_packet_callback, count=10)

print ("*********************")

print ("Payload/ data")

def raw_packet_callback(packet):
    """ Display payload/ raw data """
    if Raw in packet:
        raw_data = packet[Raw].load
        print(f"Raw Data: {raw_data}")

sniff(prn=raw_packet_callback, count=10)

print ("*********************")

print ("Basic network sniffer")

print ("*********************")

print ("Tracert")

def tracert(dest, max_hops=30, timeout=2):
    """ Trace route for a particular domain/ website """
    print(f"Tracing route to {dest} over a maximum of {max_hops} hops:\n")
    for ttl in range(1, max_hops + 1):
        pkt = IP(dst=dest, ttl=ttl) / ICMP()
        reply = sr1(pkt, timeout=timeout, verbose=0)
        if reply is None:
            print(f"{ttl}\tRequest timed out.")
        elif reply.type == 0:
            print(f"{ttl}\t{reply.src} (Destination Reached)")
            break
        else:
            print(f"{ttl}\t{reply.src}")

# Prompt the user for input
user_input = input("Enter domain/ website to tracert. For example 'Google.com' : ")

# Display the input back to the user
print("You entered:", user_input)

# Tracert to domain entered
tracert(user_input)
print ("*********************")
