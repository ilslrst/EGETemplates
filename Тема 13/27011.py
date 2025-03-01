from ipaddress import ip_network

s = 0
for s in range(33):
    net1 = ip_network(f"84.77.95.123/{s}", False)
    net2 = ip_network(f"84.77.96.123/{s}", False)

    if net1 == net2:
        print(s)
