# Network Data
class IPPacket:
    def __init__(self, src_ip, dst_ip, payload=None):
        self.src_ip = src_ip
        self.dst_ip = dst_ip
        self.payload = payload

    def route(self):
        print(f"[IP] Routing packet {self.src_ip} -> {self.dst_ip}")


class EthernetFrame:
    def __init__(self, src_mac, dst_mac):
        self.src_mac = src_mac
        self.dst_mac = dst_mac
        self.payload = None

    def encapsulate(self, packet: IPPacket):
        self.payload = packet
        print("Encapsulated IP packet inside Ethernet frame")


# Information System
class InformationSystem:
    def __init__(self, mac):
        self.mac = mac

    def send_data(self, dst_mac, packet) -> EthernetFrame:
        frame = EthernetFrame(self.mac, dst_mac)
        frame.encapsulate(packet)
        return frame

    def receive_data(self, frame):
        print(f"Frame received from {frame.src_mac}")


# Switch
class Switch:
    def __init__(self, name):
        self.name = name


# L2 Switch
class L2Switch(Switch):
    def __init__(self, name):
        super().__init__(name)
        self.mac_table = {}   # MAC -> port
        self.vlan_table = {}  # port -> VLAN

    def manage_vlan(self, port, vlan_id):
        self.vlan_table[port] = vlan_id
        print(f"Port {port} assigned to VLAN {vlan_id}")

    def forward_frame(self, frame, in_port):
        if frame is None:
            return
        self.mac_table[frame.src_mac] = in_port
        out_port = self.mac_table.get(frame.dst_mac)
        if out_port:
            print(f"Forward frame to port {out_port}")
        else:
            print("Unknown MAC -> Flooding frame")


# L3 Switch
class L3Switch(L2Switch):
    def __init__(self, name):
        super().__init__(name)
        self.routing_table = {}  # network -> next hop

    def add_route(self, network, next_hop):
        self.routing_table[network] = next_hop

    def route_packet(self, frame):
        if isinstance(frame.payload, IPPacket):
            packet = frame.payload
            packet.route()
            print(f"Routing decision for destination {packet.dst_ip}")
        else:
            print("No IP packet found in frame")


# Example usage
if __name__ == "__main__":
    host = InformationSystem(mac="AA:BB:CC:DD:EE:01")

    ip = IPPacket("192.168.1.10", "192.168.2.20")
    frame = host.send_data("AA:BB:CC:DD:EE:FF", ip)

    l2 = L2Switch("SW-L2")
    l2.manage_vlan("Fa0/1", 10)
    l2.forward_frame(frame, "Fa0/1")

    l3 = L3Switch("SW-L3")
    l3.route_packet(frame)