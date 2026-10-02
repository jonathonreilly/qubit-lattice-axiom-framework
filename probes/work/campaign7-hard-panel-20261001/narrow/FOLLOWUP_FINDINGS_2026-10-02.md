# Corner-forcing narrowing: downstream follow-up findings (2026-10-02)

The narrowing repair drafted in `REPAIR_DRAFT.md` (this directory) has landed as open PRs:

- #9445: the corner-forcing note, plus an exact scope runner, `scripts/staggered_dirac_corner_label_symmetry_scope_check_2026_10_02.py` (44/44).
- #9446: wording of the old corner-label runner.
- #9447: the safe statement of the three-generation observable note (52/52).
- #9448–#9454: downstream narrowings.

The draft was written against `0485dc0738`. The blast radius re-derived on `e485eab6b0` (the only intervening change was an automated audit-state file) is identical:
- 41 direct dependents of the corner-forcing row and 93 of the observable row, 107 in the union;
- all 107 are `unaudited` or `meta`.

## (b) Load-bearing findings: NOT rewritten, owner decision needed

### F1. The pure-APBC off-diagonal curvature no-go rests on the false commutation premise

Where:
- `docs/STRUCTURAL_NO_GO_SURVEY_NOTE.md` (`no_go`, unaudited), the "Pure-APBC temporal refinement" proof (about lines 60–90). It says "Pure-APBC `D` commutes with each of the three lattice translations `T_x, T_y, T_z` … Hence `(D + J)^{−1}` commutes with each `T_k`", and concludes that "the pure-APBC temporal-refinement lane is permanently closed".
- `docs/CHARGED_LEPTON_MASS_HIERARCHY_REVIEW_NOTE_2026-04-17.md` §5.2 repeats it.
- `scripts/frontier_charged_lepton_curvature_apbc_extension.py` sets `b_value = sp.Integer(0)` "by construction" and computes no operator.

Why it is load-bearing: the conclusion `b = K_12 = 0` has no support other than the premise. The premise is false:
- main's own substep-4 narrowing note, 2026-06-10 repair record;
- the #9445 runner: in η⁰, `[2D, T_1]` and `[2D, T_2]` are nonzero.

Scratch evidence: float numerics, not landed (`k12_offdiag_curvature_probe.py`). The setup is 4D η⁰ with `η_t = (−1)^{x_1+x_2+x_3}`, `L_s = L_t = 4`, temporal APBC, masses 0.3/0.5/0.7 on the three hw=1 labels and 0.4 elsewhere, and `K_ij = −Re Tr[G P_i G P_j]`.

- **Spatially periodic, labels = exact corner plane waves:** every `K_ij` with `i ≠ j` is 0. The cause is not commutation. The spatial terms of D annihilate the corner plane waves, and η_t pairs `n ↔ n xor 111`, i.e. hw=1 with hw=2.
- **Spatially APBC, labels = nearest corner:** `K_{100,010} = K_{010,100} = 11.93 ≠ 0`, because the direction-3 term (`ζ_3 = 110`) maps label 100 to 010. The other off-diagonal pairs vanish in η⁰, and which pair couples depends on the representative.
- The runner's diagonal formula `c(L_t) = 3 + sin²ω` corresponds to spatial `sin² k = 1` in every direction (`k = ±π/2`). On such a block the corner labels are not separated at all.

Owner decision needed:
- either narrow §5.2 and the survey note to the spatially periodic realization with the corrected proof (corner annihilation plus η_t pairing);
- or withdraw "permanently closed", since in the spatially APBC reading the off-diagonal curvature is nonzero.

Either way the runner's `b_value = 0` stub should become a computation.

### F2. The chirality-boundary species claim rests on the withdrawn observable-sector reading

Where: `docs/THREE_GENERATION_CHIRALITY_BOUNDARY_NOTE.md` (`positive_theorem`, unaudited).
- Safe statement, bullet 2: "the `hw = 1` triplet is retained as physically distinct species structure on the accepted Hilbert surface".
- Claimed item 2: "exact observable separation plus no-proper-quotient closure already force the retained `hw=1` triplet to be physically distinct species structure".
- Paper-safe wording: "Exact translation observables therefore separate the triplet sectors as physically distinct species on the accepted Hilbert surface."

Why it is load-bearing: the conclusion is the species structure itself, and its two supports are gone.
- The observable note's "exact observable sectors of the Hamiltonian" is withdrawn by #9447. The plain translations whose characters separate the labels are not jointly symmetries of the staggered operator, so their characters are not conserved labels of the dynamics.
- `PHYSICAL_LATTICE_NECESSITY_NOTE.md`, which the note credits with closing "the narrower observable-species semantics step", states in its own narrowed scope that it does **not** load-bearingly claim physical-species semantics for the hw=1 triplet.

Owner decision needed:
- either narrow the safe statement, Claimed 2 and the paper-safe wording to the algebraic content (the no-proper-quotient label algebra; species reading open);
- or keep it explicitly as an open bridge.

## (a) Wording narrowings: done, with conclusions unchanged

| PR | Notes | Runner / cache |
|---|---|---|
| #9448 | A3 R2/R3/R5 reviews; routes 2, 3, 5 (representative for the C_3 Schur step; plain-translation label decorations; chirality complements corner labels) | 5 stale caches refreshed, no runner edits |
| #9449 | `SUBSTEP4_AC_LAMBDA_SEPARATE_CLOSURE` (AC_λ.struct by corner annihilation) | runner de-stubbed (literal-True commutation replaced by exact integer checks), 32/32 |
| #9450 | `AC_PHI_LAMBDA_PRESERVED_C3` §8.1; `KOIDE_S_SUBSTEP4_ACLAMBDA` K1 (K1's own falsifier was triggered by the KS operator; reason narrowed, conclusion kept) | koide_s runner wording, 38/38; ac_phi cache refreshed |
| #9451 | `KOIDE_BAE_PROBE_HW_SECTOR_IDENTIFICATION` probe 27 (hw=2 is also the gauge image of hw=1) | cache refreshed |
| #9452 | species-direct note; gate-closure synthesis (T4 re-synced, T5/T6 narrowed) | synthesis runner wording, 18/18 |
| #9453 | `GENERATION_LOCALIZATION_MOMENTUM_CORNER` (plain-translation label characters; label differences are gauge-invariant) | none |
| #9454 | (runner only) species-direct K13 | 15/15 |

Mixed rows (26): scanned for the specific overreach patterns, then read. None needs an edit beyond the synthesis sync.
- The labeling no-go's "commuting lattice translations" are the diagonal label operators on `V_3`, which is true as stated.
- The `p_flux` and `g_bare` rows use label characters only.

## Open: noticed, not done here

- **Runner prose not yet narrowed** (each needs an output trim to stay under 6000 characters):
  - `cl3_a3_r5_hostile_review_2026_05_08_r5hr.py` (8.9 KB; prints "kinetic + cubic isotropy + APBC" as the reason for `[H_KS, U_C3] = 0`);
  - `cl3_a3_route3_anomaly_inflow_2026_05_08_r3.py` (8.2 KB; prints "Index theorem chiral charge is (-1)^hw").
- **Five runners fail on current main, while their caches say exit 0:**
  - `audit_companion_quark_c3_oriented_ward_splitter_note_hash_drift_hygiene_2026_06_04`
  - `frontier_koide_q_reduced_carrier_physical_identification_obstruction_2026_06_12`
  - `frontier_physical_lattice_necessity` (missing `docs/publication/ci3_z3/USABLE_DERIVED_VALUES_INDEX.md`)
  - `frontier_quark_c3_oriented_ward_splitter_algebraic_core_split_2026_06_18` (its note is missing)
  - `frontier_quark_c3_oriented_ward_splitter_support`
- **Generation-localization runner:** `generation_localization_corner_protected_delta_runner.py` fails 2/12 on the live ledger, because it pins its upstream rows as `retained`/`retained_bounded` and they are now `unaudited`. Its cache, fresh by runner sha, still records 12/12.
- **Many stale caches:** rows carry `sha_mismatch` caches on main (runners gained "N5 execution certificate" sections without a cache refresh). Refreshed only where this follow-up touched a row.
- **koide_s yaml block:** `KOIDE_S…` `audit_review_points` (a) still says "translation-invariance of the propagator operator". It was left untouched because it is the audit-facing block.
