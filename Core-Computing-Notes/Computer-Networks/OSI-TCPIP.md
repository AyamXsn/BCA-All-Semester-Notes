# OSI and TCP/IP Models

## 1. OSI reference model
| Layer | Main role | Example |
|---|---|---|
| 7 Application | Network services for applications | HTTP, DNS |
| 6 Presentation | Representation, encoding, encryption concepts | Data formats |
| 5 Session | Session coordination concepts | Session control |
| 4 Transport | End-to-end process communication | TCP, UDP |
| 3 Network | Logical addressing and routing | IP |
| 2 Data Link | Local link framing and media access | Ethernet |
| 1 Physical | Signals and bits over a medium | Copper/fibre radio |

The OSI model is a conceptual reference; real protocols do not always map neatly one-to-one.

## 2. TCP/IP model
A common four-layer view is application, transport, internet, and link/network access. Some texts split link into data-link and physical.

## 3. Encapsulation
As data moves down a protocol stack, each layer adds control information. At the receiver, corresponding layers remove and interpret that information.

## 4. Why models matter
Layering separates responsibilities, supports interoperability, and helps diagnose problems systematically.
