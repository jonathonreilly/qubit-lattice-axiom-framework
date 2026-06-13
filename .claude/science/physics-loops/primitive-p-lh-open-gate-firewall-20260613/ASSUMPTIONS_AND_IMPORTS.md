# Assumptions And Imports

Current source surface:

- Existing physical Cl(3)/Z^3 baseline.
- Pauli-rep exact checks for P-LH-1, P-LH-2, and P-LH-3.
- Literature context from Connes/Chamseddine-style noncommutative geometry.

Open imports:

- Order-one condition is not derived from the framework.
- KO-dim-6 real structure is not derived from the framework.
- Finite algebra `C + Clplus(3) + M3(C)` is not derived from the framework.
- P-LH-2 remains circular because it encodes the SM LH/RH split directly.

This PR does not add axioms or approve primitives. It prevents downstream
consumers from using the design map as if those imports were retired.
