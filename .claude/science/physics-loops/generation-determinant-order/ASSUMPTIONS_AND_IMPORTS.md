# ASSUMPTIONS_AND_IMPORTS — generation-determinant-order

## Import ledger (non-derivation role)
| item | role | status |
|---|---|---|
| C₃-circulant Yukawa M=aI+bC+b̄C² | derived structure (preserved-C₃) | retained-grade upstream |
| `Q=(1+2r)/3`, `r=|b|²/a²` | exact algebra (reproven) | exact |
| McKean-Singer (ind D = Str e^{−tD²}) | comparator (index is non-SUSY) | literature, comparator only |
| Berezin det_C/det_R fork | reproven on-repo (24/24) | exact |
| Coleman-Weinberg fermion V_eff=−Tr log(M†M) | comparator (energy→modulus) | literature, comparator only |
| Kähler-Dirac / staggered index theorems | comparator (non-SUSY index exists) | literature, comparator only |

## Counterfactual pass (implicit choices, "what if wrong?")
- **Polarization of the fermion measure (det_C holomorphic vs det_R real).** THE live selector. det_C→r=1/2,
  det_R→r=1. *What if the corner realization forces det_C?* → r=1/2 derived. *What if det_R?* → r=1.
- **Readout = energy (modulus) vs action (partition-function determinant).** Energy→r=1 robustly. Yukawa
  RATIOS are action data, not energy minima — but even the holomorphic det *extremized* → r=1 (massless); r=1/2
  is an equal-*channel* BALANCE, not an extremum. So "use the determinant" is necessary-not-sufficient.
- **An index is an INTEGER** — cannot output the continuous r=1/2. CORRECTION to #2743 "index→r=1/2": the
  operative object is the measure POLARIZATION, not a topological index.
- **Fermionic statistics frame (Grassmann/CAR vs hard-core boson).** Even det-valued readout rides an
  undetermined admission (FLAVOR_ZDET) — but charged leptons ARE Dirac fermions (forced, non-circular).
- **Continuous U(1)_b vs discrete C₃.** The U(1)_b that would force the channel collapse is incompatible with
  C³=I. *What if a DISCRETE (C₃-compatible) symplectic pairing suffices?* → cycle-2 stretch target.

## Hidden-admission scan
- "holomorphic polarization" — NOT supplied by {Lattice, Quantum, Record}; J_cs measure-neutral, ε phase-only,
  Record dimension-counting, native mass Berry-flat. The admission is the WITHIN-GENERATION real-antisymmetric
  bilinear in the corner-mass action.
