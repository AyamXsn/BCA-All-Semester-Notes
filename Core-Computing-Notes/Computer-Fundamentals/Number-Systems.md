# Number Systems and Data Representation

## 1. Positional notation
A base-\(b\) number uses digits from 0 to \(b-1\). Each position has a weight that is a power of the base.

For example, \((1011)_2 = 1×2^3 + 0×2^2 + 1×2^1 + 1×2^0 = (11)_{10}\).

## 2. Common bases
| System | Base | Digits |
|---|---:|---|
| Binary | 2 | 0, 1 |
| Octal | 8 | 0–7 |
| Decimal | 10 | 0–9 |
| Hexadecimal | 16 | 0–9, A–F |

## 3. Conversion methods
- Binary to decimal: add the powers of two represented by 1 bits.
- Decimal integer to binary: repeatedly divide by 2 and read remainders upward.
- Binary to hexadecimal: group bits into sets of four from the right.
- Hexadecimal to binary: replace each hex digit with its four-bit representation.

Example: \((2D)_{16} = 2×16 + 13 = 45_{10}\).

## 4. Binary arithmetic
Addition rules include 0+0=0, 0+1=1, 1+0=1, and 1+1=10 (write 0 and carry 1). Subtraction and multiplication follow positional arithmetic with base 2.

## 5. Signed representation
Common representations include sign-magnitude, one's complement, and two's complement. In an \(n\)-bit two's-complement representation, the range is \(-2^{n-1}\) through \(2^{n-1}-1\). Two's complement supports convenient binary addition/subtraction.

## 6. Character and media encoding
Text can be represented using character encodings such as Unicode encodings (UTF-8/UTF-16). Images use pixels and colour values; audio can be sampled and quantized; video combines timed image frames and audio.

## 7. Units
A bit is a binary digit. A byte is commonly 8 bits. Be careful to distinguish decimal prefixes (kB = 1000 bytes) from binary prefixes (KiB = 1024 bytes).

## 8. Practice
1. Convert \(110101_2\) to decimal.
2. Convert \(73_{10}\) to binary.
3. Convert \(AF_{16}\) to decimal.
4. State the range of an 8-bit two's-complement integer.

## 9. Summary
Number systems express values using different bases. Binary is central to digital systems, while octal and hexadecimal provide compact ways to read binary patterns.
