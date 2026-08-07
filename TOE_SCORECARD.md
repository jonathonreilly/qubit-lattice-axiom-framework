# TOE closure scorecard

LIVE distance-to-goal map for positive TOE closure: the remaining walls between
the four axioms (+3 approved primitives) and full derivation, as a root-first
DAG plus the bounded->positive restatement lever. Session-memory mirror:
`project_toe_closure_scorecard.md` — update both when a line moves.

**Last verified: 2026-08-07 @ origin/main `fb5e056ddf`** (Cycle 872; axioms doc
last changed 2026-08-05). STALE the moment
`git rev-parse --short origin/main` differs — re-verify the lines you rely on
(protocol at bottom) before planning.

**Premise authority (policy header, 2026-07-11):** foundation = four axioms +
three approved primitives, NOTHING else; everything else is conditional/open at
zero premise weight; "Tier-A/admission" is historical vocabulary — keep it out
of notes/PRs. theta RETIRED 2026-07-05, retained-grade basis — do NOT re-attack
(`docs/THETA_RETIREMENT_BASIS_REMATCH_2026-07-04.md` on origin/main). Owner
goal (2026-07-01): derive ALL lanes without bounding — every line ends as a
retained derivation or an honest no-go, never a new premise.

**Shape: a DAG, not a checklist — two roots carry half the lines; attack roots
first.** Root A = register/readout price (lines 1,5,10). Root B = chirality
grading (line 3); line 7 is mostly downstream of A+B. A positive (not bounded)
endstate ALSO needs line 11 — wall retirement alone flips ~0 bounded rows.

1. **Root A — readout/register family**: Born FORM (values), R-η/h-unit,
   (M)/det h-class (orientation {0,π}→{0} discharged #4779; residual =
   determinant-channel identification), occupancy/W_occurrence, plus lines 5
   and 10. NEW RESOURCE 2026-08-05: the NN distribution's EXISTENCE is now
   law-level — live attack = uniqueness of the FORM (weight/Born functional)
   from NN-determination + Record consistency, as native new theorems (no
   imports). δ=2/9 instance: cos6δ weight (two-harmonic V_eff, SSB vacuum).
   `feedback_readout_import_is_register_not_read_price.md`
2. **Staggered-Dirac realization gate** (former `AC_phi_lambda`, last
   admission-era target — now conditional/open like everything else):
   substantially closed; substep 4 bounded, promotion route open
   (`project_staggered_dirac_gate_substantially_closed.md`).
3. **Root B — chirality gate**: generation count (why 3 — the prize), δ=2/9
   chain, Koide Q=2/3, color-bar discharge, and the signed-gravity origin
   cross-term ALL reduce to it; K/CPT ×2 = do-not-re-attack. Enabler: the
   no-go is NARROW — only the hybrid γ_CL=Γ_χ identification is forbidden.
   `project_chirality_nogo_narrow_dirac_vs_generation_2026_06_08.md`
4. **Action/bridge-gap**: Wilson action = admitted import (the deepest one);
   HK = Casimir-native candidate; 3-part decomposition
   (`project_bridge_gap_resolution_c_locked.md`). Feeds the line-11 keystones.
5. **c=1 identity-unit** (Root A member; clock/normalization dial; #4762
   proves axioms+primitives alone don't derive readout selection).
   `project_defect_identity_unit_rescale_obstruction_2026_07_01.md`
6. **Hypercharge** (fanout 1035): waits on OWNER decision — not
   science-attackable; `hypercharge_identification_note` audited_conditional
   (ledger-verified 2026-08-07).
7. **r=1/2 / δ pins**: settings not forced (lane-scoped forcing PERMITTED
   never REQUIRED; universal falsified). Positive closure here = Root A weight
   (δ) + Root B boundary (r) — don't attack standalone.
   `feedback_r_half_stable_setting_not_forced.md`
8. **ν/DM lane**: y_nu^eff = g²/64 on 3 named conditional inputs.
   `project_neutrino_dm_leptogenesis_program_entry_2026_06_07.md`
9. **Gravity lane (active, self-driving)**: G→1/(4πr) DERIVED; cell-cutting
   charge-space program at c736 (PR #6016 open), main loop Cycle 872 —
   PR-side science is grep-invisible on main.
   `project_gravity_cell_cutting_charge_space_cycle736_2026_08_05.md`
10. **Hierarchy (4π)⁻¹⁶**: residual = I1 readout import → Root A.
11. **Bounded→positive RESTATEMENT (the positive-endstate lever)**:
    retained_bounded rows are bounded by reason "self" ⇒ wall retirement flips
    0 rows mechanically; endstate ≈1800 bounded unless keystones are RESTATED
    as positive theorems. Fanout ranking (2026-07-01 snapshot — re-rank via
    the ledger shards before dispatch): kawamoto_smit 1296, alpha_third 1120,
    abj 1114, three_generation 1094, SME 1088, kinetic_class 1070, plaquette
    1024, spin_statistics 1005.
12. **Open lanes named in the theta-retirement record**:
    W_anomaly_covariant_assembly; Q-structure — emergent-Q nonvacuous
    weighting, OS0-surface 4D carrier, defect closure, SU(3) abelianization.
    Open physics; absence from lines 1-11 ≠ done.

**Refresh protocol (cheap, per line):** premise surface →
`git show origin/main:docs/audit/AXIOM_MINIMALITY_POLICY.md | head -6`;
axioms →
`git log -1 --format='%h %cs' origin/main -- docs/MINIMAL_AXIOMS_2026-06-29.md`;
grades → grep the tracked ledger shards extracted from origin/main
(`docs/audit/data/ledger/` + `ledger_meta.json`), NEVER memory or note
headers; open lanes → `gh pr list --state open --limit 15`; in-flight
science → session-memory Active programs index.
