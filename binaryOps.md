Tricks With Bits
----
`In python3, ~x (flip all bits in other languages) is achieved with (~x & 0xFFFFFFFF) (use repit1 lenght of HEXA as you wish)`

- `x & (x-1)` : clear the lowest set bit of x
- `x & ~(x-1)` extracts the lowest set bit of x (all others are clear). Pretty patterns when applied to a linear sequence.
- `x & (x + (1 << n))` : the _run_ of set bits (possibly length 0) starting at bit n cleared.
- `x & ~(x + (1 << n))` : the _run_ of set bits (possibly length 0) in x, starting at bit n.
- `x | (x + 1)` :  x with the lowest cleared bit set.
- `x | ~(x + 1)` : extracts the lowest cleared bit of x (all others are set), if ~ wrapping the expression, you have that cleared value.
- `x | (x - (1 << n))`: x With the run of cleared bits (possibly length 0) starting at bit n set.
- `x | ~(x - (1 << n))` : The lowest run of cleared bits (possibly length 0) in x, starting at bit n are the only clear bits.



1. By _**run**_ is intended the number formed by all consecutive 1's at the left of n-th bit, starting at n-th bit.
