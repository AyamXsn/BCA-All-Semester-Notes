# IP Addressing and Subnetting

## 1. IP address
An IP address identifies an interface in an IP network. IPv4 uses 32 bits, commonly written as four decimal octets. IPv6 uses 128 bits and hexadecimal notation.

## 2. Network prefix
A prefix length indicates how many leading bits identify the network. For example, `/24` means 24 network bits and 8 remaining host bits in IPv4.

## 3. Basic subnet example
For `192.168.10.0/24`, the mask is `255.255.255.0`. The block contains 256 addresses. In a traditional subnet, `.0` is the network address and `.255` the broadcast address; usable host conventions depend on the subnet and special cases.

## 4. Subnet calculation
For IPv4 prefix `/p`, host bits = 32 − p. Address count = 2^(32−p). For conventional subnets with at least two host bits, usable host count is commonly address count minus network and broadcast addresses.

## 5. Private IPv4 ranges
- 10.0.0.0/8
- 172.16.0.0/12
- 192.168.0.0/16

Private addresses are not globally routed on the public internet by default.

## 6. Exercises
Find the network address, broadcast address, and address count for `192.168.4.64/26`. Compare IPv4 and IPv6 notation.
