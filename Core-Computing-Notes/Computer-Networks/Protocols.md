# Transport and Application Protocols

## 1. TCP
Transmission Control Protocol is connection-oriented and provides a reliable, ordered byte stream. It uses sequence numbers, acknowledgements, retransmission, and flow/congestion control.

## 2. UDP
User Datagram Protocol provides datagrams without TCP's built-in reliable ordered delivery. Applications may choose it when low overhead or application-controlled recovery is useful.

## 3. Ports
Transport ports identify application endpoints on a host. A socket endpoint is commonly described using an IP address, transport protocol, and port.

## 4. Application protocols
- HTTP/HTTPS: web request/response; HTTPS protects HTTP using TLS.
- DNS: resolves names to records such as IP addresses.
- SMTP: sending email between systems.
- IMAP/POP3: accessing mailboxes.
- SSH: secure remote login and command execution.
- DHCP: automatic network configuration.

## 5. Client-server model
A client initiates a request; a server listens and responds. Some systems use peer-to-peer or hybrid models.

## 6. Exercises
Explain TCP's three-way handshake at a high level. Compare TCP and UDP for file transfer, live voice, and DNS query use cases.
