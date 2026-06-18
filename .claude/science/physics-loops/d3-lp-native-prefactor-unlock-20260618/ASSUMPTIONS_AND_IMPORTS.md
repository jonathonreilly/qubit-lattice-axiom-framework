# Assumptions And Imports

| Item | Role in claim | Current class | Source surface | Load-bearing? | Needed for target status? | Retirement path | Disposition |
|---|---|---|---|---|---|---|---|
| Cubic periodic `Z^3` nearest-neighbor Peierls Hamiltonian | D3 finite-torus reference | computed lattice input | `scripts/frontier_d3_orbital_response_decomposition_2026_06_13.py` | yes | yes | runner/log route | constructed directly and cached |
| Single-band interband term equals zero | D3 decomposition split | framework-derived within one-band model | D3 note/runner | yes | yes | exact algebraic route | fixed by one-band scope, not fitted |
| Landau-Peierls response prefactor `-1/12` | D3 Brillouin-zone integral normalization | framework-derived source companion, awaiting audit | `scripts/frontier_landau_peierls_prefactor_native_derivation_2026_06_13.py` | yes | yes | companion theorem plus audit route | D3 now consumes the derived rational instead of a raw scalar import |
| Magnetic Peierls/Moyal expansion surface | Companion symbolic derivation surface | literature theorem / mathematical bridge surface | `docs/LANDAU_PEIERLS_PREFACTOR_NATIVE_DERIVATION_BOUNDED_THEOREM_NOTE_2026-06-13.md` | yes for the companion | yes for companion acceptance | derive from finite Peierls algebra or grade as accepted bounded math surface | exposed; not hidden inside D3 |
| Exact finite Peierls diagonalization cross-check | Independent numerical check of derived scalar | computed lattice input | companion runner/cache | yes for companion support | yes | exact runner/log route | passes 8/0 |
| Audit acceptance of companion and D3 consumer | Authority status | independent audit judgment | audit lane, not this PR | yes | yes | reviewer/auditor process | not performed in this branch |
