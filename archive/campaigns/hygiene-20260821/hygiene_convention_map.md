# Item 6 — inertia-convention map, admissibility_dirac_kahler lane

Scope: `scripts/admissibility_dirac_kahler_*.py` only (66 files; 23 matched the
helper grep). Blocks 129–168 have runners on disk; the lane numbering runs
through 170 (169/170 have no runner file in this worktree — findings only).
NO file edits made.

## A. The two conventions (definitions read, ~15 lines each)

| helper | defining file | line | returns |
|---|---|---|---|
| `congruence_inertia` | `scripts/admissibility_dirac_kahler_massless_seam_verdict_2026_08_19.py` (b144, the root) | 336 | **(n_+, n_0, n_-)** — Sylvester congruence, WITH multiplicity |
| `real_symmetric_inertia` | `scripts/admissibility_dirac_kahler_scaling_probe_2026_08_21.py` (b165, the root) | 757 | **(n_+, n_-, n_0)** — Descartes-on-charpoly, WITH multiplicity |

Secondary/aux helpers, all order-checked:

| helper | file (block) | line | returns | note |
|---|---|---|---|---|
| `inertia` | carrier_reflection_blocker (b142) | 321 | (n_+, n_0, n_-) | same ORDER as congruence; `count_roots` counts DISTINCT roots → multiplicity-unsound, flagged by b144 itself |
| `inertia` | staggered_hermitian_pairing (b143) | 328 | (n_+, n_0, n_-) | same order; b144 flags it in the same sentence |
| `sturm_inertia` | validation_battery (b161) | 351 | (n_+, n_0, n_-) | independent route, ORDER-MATCHED to congruence, so the b161/b162/b163 cross-check is apples-to-apples; `(-1,-1,-1)` sentinel |
| `guarded_inertia` | site_reflection_channel (b163) 344 → zero_shear_region (b164) 350 | — | congruence, or `None` | `is_psd(i)` tests `i[2]==0 and i[0]>0`, i.e. n_- and n_+ under (n_+,n_0,n_-) — CORRECT for its convention |
| `inertia_from_leading_minors` / `inertia_from_nonzero_leading_minors` | positive_dressed_reflection 573 / global_dressing_involution_positivity 604 (both 2026-08-15, pre-b141) | — | (n_+, n_0, n_-) | outside the b141+ admissibility chain; no fence triples |

## B. Runner → helper → fence triples

Convention **C** = (n_+, n_0, n_-) [congruence]. Convention **D** = (n_+, n_-, n_0) [Descartes].

| block | runner | helper (source) | order | fence inertia triples (N5_FENCE) |
|---|---|---|---|---|
| 142 | carrier_reflection_blocker | own `inertia` (root-count) | C | (0,4,4) (2,0,6) (4,0,4) (6,0,2) (16,0,0) |
| 143 | staggered_hermitian_pairing | own `inertia` | C | (6,0,2) (8,0,0) |
| 144 | massless_seam_verdict | own `congruence_inertia` (ROOT) | C | (2,0,6) (6,0,2) (4,0,0)† |
| 145 | seam_dichotomy | `congruence_inertia` | C | (16,0,0) (6,0,2) (2,0,6) (4,0,4) |
| 147 | annealed_pairing_migration | → b144 | C | (4,0,4) |
| 148 | general_migration_theorem | → b144 | C | (4,4,0) (3,0,5) (8,0,0) (4,0,4) |
| 149 | shear_gauge_classification | own congruence | C | — (no triple in fence) |
| 153 | bare_character | → b144 | C | (4,0,4) (2,0,6) (6,0,2) (4,4,0) |
| 154 | unique_completion_price | congruence | C | (3,4,1) (5,2,1) … |
| 155 | discriminator_verdict | → b144 | C | (4,4,0) (2,4,2) (0,8,0) (0,4,4) |
| 156 | residue_transversality_gate | congruence | C | (4,4,0) (4,0,4) (2,4,2) |
| 158 | quotient_gate | congruence | C | (2,0,2) |
| 159 | link_curvature_scout | → b158 | C | (4,0,4) (4,4,0) (3,4,1) (2,4,2) |
| 160 | exchange_condition_contract | congruence | C | (6,0,2) (2,0,6) (4,4,0) (4,0,4) (0,4,4) (2,4,2) (0,8,0) |
| 161 | validation_battery | congruence + `sturm_inertia` | C | (4,4,0) (2,4,2) (6,0,2) (0,4,4) (2,0,2) (0,8,0) |
| 162 | mass_survival_stratum | → b161 | C | (6,0,2) (2,0,6) (4,0,4) (0,8,0) (2,4,2) (2,0,2) (1,6,1) |
| 163 | site_reflection_channel | → b162 → b144 | C | (4,4,0) ← "diag(1,1,1,1,0,0,0,0) at inertia (4,4,0)" = **PSD** |
| 164 | zero_shear_region | → b163 `guarded_inertia` | C | (4,4,0) ×2 ← the region normal form, **PSD**, 448 PSD cells |
| 165 | scaling_probe | own `real_symmetric_inertia` (ROOT) | **D** | — (fence carries NO inertia triple) |
| 166 | interpretation_discriminators | `inertia = b165.real_symmetric_inertia` (l.172) | **D** | (0,4,0) (4,4,0) (4,0,4) (5,3,0) (0,0,8) + the labeled collision pairs |
| 167 | null_model_corner_theorem | `inertia = b166.inertia` (l.162) → b165 | **D** | (0,4,0) (4,0,4) (5,3,0) (4,4,0) (4,0,0) (6,2,0) + collision banner |
| 168 | shim_zero_diagonal | `inertia = b165.real_symmetric_inertia` (l.204); also calls `b163.congruence_inertia` at l.693 to MEASURE the collision | **D** | (2,2,0) (4,0,0) (0,6,0) (4,4,0) + collision banner |

† b144's `(4,0,0)` is a QUOTATION of Block 142's helper output, explicitly
labeled "Block 142's inertia helper … is UNSOUND on this degenerate carrier,
reporting (4,0,0) for H_q" — a disclosed quotation of a *different tool*, same
tuple order, so no misread.

## C. Cross-block quotation audit (genuine quotations only)

Every triple below is a real quotation of another block's numeral, not a
coincidental numeral:

1. **b153 → b142**: "Block 142's THREE values {(2,0,6),(4,0,4),(6,0,2)}" and
   "Block 142's inertia census {(2,0,6),(4,0,4),(6,0,2)} → the UNIFORM {(4,0,4)}".
   Both blocks are convention **C**. SAFE.
2. **b144 → b142**: the `(4,0,0)` quotation above. Same order, disclosed as
   unsound. SAFE.
3. **b161 → b156**: "theta-prime's is (2,4,2) with live-live (2,0,2), so Block
   156's kill fires untouched". Both **C**. SAFE.
4. **b162 → b156**: "(0,8,0) … the Block 156 cone sign lock is evaded by
   ANNIHILATION". Both **C**. SAFE.
5. **b164 → b163**: "Block 163's 64 cells and its exact witness
   diag(1,1,1,1,0,0,0,0) reproduced" at (4,4,0). Both **C**. SAFE.
6. **b148/b153 → b148 escape witness** at (4,4,0). Both **C**. SAFE.
7. **b166, b167, b168 → b163/b164**: the ONLY cross-CONVENTION quotations in the
   lane, and all three are the *deliberate, measured* collision statement —
   "b163/b164's congruence_inertia returns (n_+, n_0, n_-) … so the region
   normal form reads (4,4,0) there and (4,0,4) here … THE LITERAL STRING
   (4,4,0) MEANS PSD IN BLOCK 164'S LANDED FENCE AND MEANS FULLY HYPERBOLIC
   HERE". b168 goes further and computes both readings on identical matrices
   (`b163.congruence_inertia` at l.693 vs `b165.real_symmetric_inertia`).
   Each of the three fences also gates the disclosure
   (`convention_collision_named` = both helper names present in the note).
   DISCLOSED — hazard named, not silently carried.

**No unlabeled cross-convention quotation was found anywhere in the lane.**
The direction that would be dangerous — a C-convention block quoting a D
numeral as if it were C — is structurally impossible here: b165 is the first
D block and every C block predates it, and b165's own fence carries no triple.

## D. Per-triple internal-consistency spot check

- b163 `diag(1,1,1,1,0,0,0,0)` → (4,4,0) under C = 4 pos, 4 zero, 0 neg = PSD. ✔
- b164 region normal form `m diag(D) ⊕ 0_4` → (4,4,0) under C = PSD, matches
  "448 PSD all at (4,4,0)". ✔
- b166/b167 `(4,0,4) PSD at s_t = 0` under D = 4 pos, 0 neg, 4 zero = PSD. ✔
- b167 `T*T = 1 at inertia (4,0,0) POSITIVE DEFINITE` under D = 4 pos, 0 neg,
  0 zero. ✔ (the same string under C would also be PD — a benign coincidence)
- b168 `(2,2,0) … on all 240 full-rank cells and indefinite` under D = 2 pos,
  2 neg = indefinite at rank 4. ✔
- b163 `is_psd(i) = i[2]==0 and i[0]>0` reads n_- under C. ✔
- b161 `sturm_inertia` is order-matched to congruence, so the b161/b162/b163
  "genuine cross-check" is not comparing different orders. ✔

## VERDICT

Each landed fence is internally consistent: every runner's fence triples are
produced by, and read against, the one helper that runner actually calls, and
the helper order is uniform within each of the two families (C for b142–b164
plus every aux route including the `sturm_inertia` cross-check; D for b165–b168).
The only cross-convention traffic in the lane is the b166/b167/b168 collision
disclosure, which names both helpers, states both readings on identical
matrices, and gates the disclosure in its own N5 fence — that is an audit, not
a defect. So there is **no live misread hazard inside the runners or their
fences**. The residual exposure is entirely *reader-side and corpus-side*: the
literal string `(4,4,0)` denotes PSD in the b163/b164 fences and fully
hyperbolic in the b166/b167/b168 fences, so any downstream document, ledger
entry, or successor block that compares the two families by tuple alone — which
b166 records its own tasking as having done — reads the exclusion backwards.
The mitigation already in place (convention carried inline on every numeral in
the D-family notes) is sufficient for the D family; the C-family fences
(b142–b164) carry their triples WITHOUT an inline convention marker, so the
one cheap, non-correcting improvement available to a follow-up pass is to add
the same inline "(n_+, n_0, n_-)" marker to the C-family notes' inertia
numerals — a documentation change only, with no verdict touched.
