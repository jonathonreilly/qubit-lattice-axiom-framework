# Assumptions And Imports

## Native Surface

- `Lattice`: finite site/exchange combinatorics.
- `Quantum`: one-qubit local algebra, compatible with hard-core-boson or
  Jordan-Wigner/CAR generator frames.
- `Record`: not used as a statistics source.

## Mathematical Infrastructure

- Type-A Coxeter presentation of adjacent exchanges.
- Exact finite enumeration of `Z_2` characters on exchange generators.

The runner reproves the finite enumeration; no literature value or observed
input is load-bearing.

## Open Imports

- `q=-1` as the global exchange-sign selector.
- Any graded-locality, spin-statistics reconstruction, microcausality,
  positive-energy, or superselection theorem that would choose `q=-1`.
- `{D,gamma5}=0` as the downstream staggered anticommutation filter.
