# Assumptions And Imports

| Item | Role in claim | Current class | Source surface | Load-bearing? | Needed for target status? | Retirement path | Disposition |
|---|---|---|---|---|---|---|---|
| Staggered kinetic exchange certificate `W M_KS W^T = M_KS` | Baseline symmetry that defeats axis-label selection | computed lattice input | `scripts/single_clock_axis_selection_check_2026_06_11.py` block [S] | yes | yes | already recomputed in packet | retained as native computed input |
| Scope-boundary N2/N4/N5 clauses | Defines the axis-label residual attacked by the note | retained support / no-go boundary | `SINGLE_CLOCK_UNIQUENESS_SCOPE_BOUNDARY_2026-06-06.md` | yes | yes | cited one hop | retained as governing boundary |
| Record axiom no-time-metric text | Shows records do not supply a lattice-axis metric | axiom text | `MINIMAL_AXIOMS_2026-06-05.md` | yes | yes | none needed | consumed narrowly |
| Record-formation no-go | Prevents "at least one record exists" from becoming an unconditional axis supplier | retained support / no-go boundary | record-formation no-go source | yes | yes | none needed | consumed narrowly |
| Clock/rate interface no-go | Shows record order lacks supplied `tau` and axis label | retained support / no-go boundary | clock/rate interface source | yes | yes | none needed | consumed narrowly |
| Finite-speed registration-cone route | Candidate axis supplier to be pruned | computed lattice input plus self-contained circularity statement | this note and runner block [RT-REC] | yes | yes | compute transport directly; do not cite external cone row | retired as external source import |
| Anomaly/chirality route | Candidate axis supplier to be pruned | computed lattice input plus self-contained count-not-label firewall | this note and runner block [RT-ANOM] | yes | yes | compute chirality invariance directly; do not cite the downstream anomaly row | retired as external source import |
| Boost-faith and cubic-anisotropy boundaries | Guardrails against importing boost/Lorentz/SO(4) content | retained support / no-go boundary | named boundary notes | no | no | cited as guardrails | non-closure context |
| Per-axis BC asymmetry or registration-direction bridge | Positive sharpened pin, sufficient if supplied | admitted normalization / open supplier shape | this note and runner block [PIN] | no for no-go; yes for future positive supplier | no for this no-go | future theorem or explicit admission needed | not derived here |

Result: the direct parent single-clock source, the external finite-speed cone
note, downstream anomaly row, and setup-convention example rows are no longer
load-bearing imports for this packet.
