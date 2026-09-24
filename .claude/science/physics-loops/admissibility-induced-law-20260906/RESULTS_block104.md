# Block 104 — results (2026-09-23)

- **Runner.** `scripts/admissibility_rule_the_rules_own_clock_has_no_far_field_2026_09_23.py`: `TOTAL: PASS=12 FAIL=0` (~1 s). Seven mutations, each failing in its own family.
- **T1.** The sources of any field sum to zero on a torus. A clock set by the records within range R is ambient beyond R: no monopole and no tail. Block 53's clock gives n records the total source n log κ, which no such clock can.
- **T2.** The rule's clock, read as κ:
  - an isolated record has κ = 1;
  - one neighbour gives 12/17, 12/7 or 1; two give values from 1/2 to 3;
  - the averages are 382/357 (uniform) and 352/357 (pair law);
  - in the geometric form κ = π_x^(−5/6);
  - its field is u = −log π, confined to records that have neighbours.
- **T3.**
  - Equal pulls need log κ = −(γ/6)E_rec.
  - No on-site 2×2 term anticommutes with σ₁, σ₂, σ₃, so E_rec = 0 for a walker at rest.
  - γ is free.
- **Control** (`specs/`).
  - A 27-record clump under the rule's clock has a field only inside the clump and zero pull outside. Under block 53's clock it has a field across the box.
  - Block 39's law at densities 0.05 and 0.2: the mean source at records is −0.007 and −0.033, repaid at the empty sites; the total is zero.
