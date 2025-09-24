# Network Discovery and Subnetting Tool

📌 **Purpose**  

This tool is a Python-based network discovery and subnetting utility. It allows you to perform:

- ICMP ping sweeps using Nmap to identify live hosts
- Subnet calculations including network address, broadcast, usable hosts, and host IP range

It is designed to help network administrators, pentesters, and students quickly analyze a network.

---

🔧 **Requirements**

- Python 3.7+ installed
- Nmap installed on your system
- `python-nmap` Python package (`pip3 install python-nmap`)

---

⚙️ **How to Use**

1. Clone this repository and open it in VS Code or your preferred IDE.
2. Run the script with Python:

```bash
python3 rangefinder.py [flags] <TARGET>
