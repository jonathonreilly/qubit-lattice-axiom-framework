# Assumptions And Imports

| Item | Role in claim | Current class | Source surface | Load-bearing? | Needed for target status? | Retirement path | Disposition |
|---|---|---|---|---|---|---|---|
| Finite `H_hw=1 = C^3` carrier | Carrier for the local Ward operator algebra | retained support | `THREE_GENERATION_OBSERVABLE_THEOREM_NOTE.md`; audit ledger `audited_clean` / effective `retained` on `origin/main` at branch start | yes | yes | already retained finite-dimensional parent | used as the only carrier input |
| Induced oriented `C3[111]` cycle | Order-three operator whose Hermitian commutant is classified | retained support | same parent theorem | yes | yes | already retained finite-dimensional parent | used |
| Hermitian finite matrix algebra | Algebraic category for Ward endomorphisms | zero-input structural on supplied `C^3` | elementary finite-dimensional linear algebra | yes | yes | proved directly by runner | not an external physics import |
| Reflection operator with `R C R = C^2` | Classifies orientation-odd splitter coefficient | supplied finite matrix comparison | explicit 3-by-3 matrix in runner | yes for orientation-odd statement | yes for splitter parity only | direct matrix check | used only for parity classification |
| Physical staggered-carrier provenance | Broader physical realization of the carrier | open physical bridge | historical staggered-Dirac program | no | no for this algebraic split | separate retained physical-carrier theorem if a future physical claim needs it | excluded from proof |
| Quark source/readout law for `a,b,c` | Needed for quark Yukawa closure | open | none in this block | no | no for local split; yes for Lane 3 mass closure | future theorem or no-go | explicitly left open |
| Observed quark masses, fitted Yukawas, CKM mass input | Comparator/fit data that would overclaim closure | forbidden import | not used | no | no | not admitted | excluded |
