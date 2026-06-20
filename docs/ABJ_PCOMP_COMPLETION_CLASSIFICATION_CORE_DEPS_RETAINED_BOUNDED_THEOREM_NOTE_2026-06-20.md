# ABJ P-COMP — Scale-Free RH Completion **Classification** Core From Retained Anchors — Decoupled From the ABJ Keystone (Bounded Theorem)

> **Key terms used in this doc** are indexed A–Z at
> [docs/KEY_TERMINOLOGY.md](KEY_TERMINOLOGY.md).

**Date:** 2026-06-20
**Type:** bounded_theorem
**Claim type:** bounded_theorem
**Status:** source note awaiting independent audit handling. Status authority is
the **independent audit lane only**; this note asserts no audit verdict and claims
no "retained"/"promoted" standing. **Audit-readiness purpose:** its load-bearing
dependencies are all retained-grade (deps-all-retained, "ready") and it does
**not** route through the unaudited keystone
`anomaly_forces_time_abj_inconsistency_accepted_premise_bridge_bounded_note_2026-05-26`
or its parent `anomaly_forces_time_theorem`.
**Primary runner:**
[`scripts/frontier_abj_pcomp_classification_bank_2026_06_20.py`](../scripts/frontier_abj_pcomp_classification_bank_2026_06_20.py)
(**TOTAL: PASS=40 FAIL=0**, exact `sympy` arithmetic + read-only ledger parse;
cache
[`logs/runner-cache/frontier_abj_pcomp_classification_bank_2026_06_20.txt`](../logs/runner-cache/frontier_abj_pcomp_classification_bank_2026_06_20.txt)).

## Why this note exists (audit-unblock, decoupling move)

This banks the **P-COMP arithmetic CLASSIFICATION core** — the RH-hypercharge
solving step consumed by step (B3) of the ABJ keystone — as an auditable,
keystone-decoupled, **conditional** bounded theorem. It is the same decoupling
move as the precedent
[`docs/SM_ANOMALY_CLOSURE_RETAINED_ANCHORS_DECOUPLED_BOUNDED_THEOREM_NOTE_2026-06-08.md`](SM_ANOMALY_CLOSURE_RETAINED_ANCHORS_DECOUPLED_BOUNDED_THEOREM_NOTE_2026-06-08.md)
(`effective_status=retained_pending_chain`, runner PASS=11): the load-bearing
**arithmetic** is reproven from retained anchors plus **explicit admissions**,
while the physical **existence/identification** stays a named admitted premise,
not imported from `anomaly_forces_time`.

The arithmetic is **only** bankable as a classification *given* the template; the
**existence / minimality** of the template is **not** bankable — block 02's
finite computation
([`docs/ANOMALY_FORCES_TIME_ABJ_EXERCISE_VERIFICATION_NOTE_2026-06-20.md`](ANOMALY_FORCES_TIME_ABJ_EXERCISE_VERIFICATION_NOTE_2026-06-20.md))
proved the only candidate native supplier (the complementary Hamming-odd sector
of the dim-8 Cl(3) carrier) is the SU(2)_weak fiber-flip image of the LH content
(**vectorlike**), not a native opposite-chirality SU(2)-singlet `3̄` template.

## Premises

- **(GIVEN — admitted premise, the template).** The opposite-chirality
  **SU(2)-singlet** RH completion adjoined to the LH surface:
  `u_R:(1,3)_x`, `d_R:(1,3)_y`, `e_R:(1,1)_z`, `n_R:(1,1)_n` — including the
  **neutral** singlet `n_R`. This is **not** derived here and **not** imported
  from the keystone/parent. Its existence/minimality is an open wall (Honest
  ledger H1; block 02 computed no-go).
- **(GIVEN — admitted, the LH surface, P-HY identification).** The LH content
  `Q_L:(2,3)_a`, `L_L:(2,1)_{-3a}` (color `n_color=3`, scale-free in `a≠0`), with
  the `+1 : −3` traceless abelian ratio. The "is-gauged" identification of this
  abelian direction with the anomaly-relevant `U(1)` is the P-HY admission, kept
  named (block 01).
- **(GIVEN — admitted branch convention).** `n=0` (the neutral branch).
  Load-bearing — see lemma B1.
- **(R-dep, retained).**
  `one_generation_anomaly_singlet_completion_narrow_theorem_note_2026-05-10`
  (`retained_bounded`, `chain_closes=True` — already banks the RH-Y closed form).
- **(R-dep, retained).**
  `cl3_complexification_split_narrow_theorem_note_2026-05-10`
  (`retained`, `chain_closes=True`).
- **(R-support, retained, corroborating — not bare).**
  `lh_traceless_eigenvalue_ratio_narrow_theorem_note_2026-05-10` (`retained_bounded`);
  `cl3_color_automorphism_theorem` (`retained_bounded`).
- **(External — comparator role).** Standard ABJ anomaly cancellation
  (Adler 1969; Bell–Jackiw 1969); `SU(3)` triplet Dynkin index `T(3)=1/2`; cubic
  index `A(3)=+1, A(3̄)=−1`. Named external mathematical content, reproven-in-runner
  where arithmetical.

## Statement and result

**Theorem (bounded, conditional).** **Given** the admitted template (an
opposite-chirality SU(2)-singlet RH completion `{u_R,d_R,e_R,n_R}`), the LH
surface, and the neutral branch `n=0`, anomaly cancellation
(`Tr[Y]=0`, `Tr[SU(3)²Y]=0`, `Tr[Y³]=0`, `Tr[SU(3)³]=0`) **FORCES** the RH
hypercharges

> **{x, y, z, n} = {4a, −2a, −6a, 0}**, **unique up to the `u_R ↔ d_R` triplet swap.**

At `a = 1/3` this is the keystone (B3) witness `(4/3, −2/3, −2, 0)`. The two
triplet values `4a, −2a` are the two roots of the single quadratic
`t² − 2a·t − 8a² = (t−4a)(t+2a)`; `z=−6a` and `n=0` are scalar-forced, so the
swap is the **only** ambiguity. Each anomaly is an exact `Fraction`-level equality
(verified at `a ∈ {1/3, 2/5, 7/4, −1/2}`).

This reproduces the arithmetic consumed by keystone step (B3) **without** routing
through `anomaly_forces_time` (block01 classification runner PASS=49, absorbed
below).

## Load-bearing NEGATIVE lemmas (verbatim, re-derived in-runner)

These show the result is **conditional and non-vacuous** — the admissions are
real, not cosmetic:

- **B1 (free `n_R` reopens a 1-parameter family).** With `n_R` free, the family
  `{x,y,z,n} = {4a+t, −2a−t, −6a−t, t}` cancels `Tr[Y]`, `Tr[SU(3)²Y]`, and
  `Tr[Y³]` for **every** `t`. The non-neutral witness `(0, 2a, −2a, −4a)` cancels
  the same anomalies with `n=−4a≠0`. Hence **`n=0` is a SELECTION (a load-bearing
  admitted branch), not an anomaly consequence.**
- **B2 (vectorlike pairs preserve zeros).** A vectorlike pair `(t, −t)` (colorless,
  or a color-triplet pair) adds `0` to `Tr[Y]`, `Tr[Y³]`, and `Tr[SU(3)²Y]`.
  Hence **the matter content is NOT anomaly-unique; uniqueness / minimality is not
  supplied by the anomaly algebra** (excluding vectorlike/mirror content is a
  separate chirality question).
- **B3 (global rescaling preserves zeros).** Each anomaly polynomial is homogeneous
  in `Y` (deg 1, deg 1, deg 3), so `Y → λY` preserves every zero. Hence **the
  absolute `Y`-scale (the value of `a`) is a CONVENTION; only the ratios
  (`+1:−3` LH; `4:−2:−6:0` RH) are content.**

## CRITICAL HONEST FLAGS

- **H1 (ARITHMETIC ONLY — existence/minimality is NOT banked).** The
  **existence/minimality** of the opposite-chirality SU(2)-singlet `3̄` template
  (incl. neutral `n_R`) is **not** bankable. Block 02's finite computation of the
  complementary chirality block proved the only candidate native supplier — the
  Hamming-odd sector `{|001⟩,|010⟩,|100⟩,|111⟩}` of the dim-8 Cl(3) carrier
  `Λ(C³)=(C²)^⊗3` — is the **SU(2)_weak fiber-flip image** of the LH content
  (color `3` not `3̄`; SU(2) doublet-half not singlet; no native `n=0` ray):
  i.e. **vectorlike**, not a native chiral RH template. The existence-side
  suppliers are all non-retained:
  `rh_completion_color_anti_fundamental_narrow_theorem_note_2026-05-17` (unaudited),
  `su3_anomaly_forced_3bar_completion_theorem_note_2026-05-02` (unaudited),
  `su3_dabc_symmetric_theorem_note_2026-05-02` (**audited_failed**). The template
  therefore **must be adjoined** and stays a **named admitted premise**.
- **H2 (circular-on-parent).** The SM witness consumed by keystone step (B3) is the
  conditional **output** of this classification, not an independent
  matter-existence supplier. Banking the arithmetic core does **not** resolve the
  circularity; **P-COMP remains circular-on-parent.**

## What this does and does not claim

- **Does:** given the admitted template + LH surface + `n=0` branch, the RH
  hypercharges are uniquely `{4a,−2a,−6a,0}` up to the `u_R↔d_R` swap; all four
  governed anomaly traces cancel — reproven from retained anchors, decoupled from
  the keystone/parent.
- **Does not** derive the template **existence/minimality** (H1), nor exclude
  vectorlike/mirror completions (B2), nor select the `n=0` branch (B1), nor fix
  the absolute `a`-scale (B3) — these are admissions/conventions.
- **Does not** resolve circular-on-parent (H2). Introduces **no** new
  axiom/primitive and changes **no** numerical prediction.

## Reprove-and-cite (source discipline)

- The classification arithmetic and the B1/B2/B3 negative lemmas are **recomputed
  in-tree** by the runner (`sympy`), not asserted by name. The dep ledger
  statuses are parsed **read-only** from `docs/audit/data/audit_ledger.json`.
- **Absorbed by path + PASS (cited, NOT rebuilt):**
  `scripts/frontier_abj_pcomp_block01_template_existence_2026_06_20.py`
  (**PASS=49**, block01 classification + three walled routes) and
  `scripts/frontier_abj_pcomp_hamming_odd_sector_2026_06_20.py`
  (**PASS=31**, block02 computed no-go of the candidate native supplier).
- **Context-only (NOT load-bearing markdown deps):** the keystone
  `anomaly_forces_time_abj_inconsistency_accepted_premise_bridge_bounded_note_2026-05-26`
  and parent `anomaly_forces_time_theorem` (both confirmed `unaudited`).
- Precedent: `SM_ANOMALY_CLOSURE_RETAINED_ANCHORS_DECOUPLED_BOUNDED_THEOREM_NOTE_2026-06-08`.
- Adler 1969; Bell–Jackiw 1969 — external comparator authorities.

## Forbidden-imports / firewall check

No PDG values, fitted selectors, or literature numerical comparators are used as
derivation inputs. The ABJ trace formulae and `SU(3)` indices are named external
mathematical content (comparator role), reproven-in-runner where arithmetical.
The absolute `Y`-scale (`a`) is treated as a convention (B3), not consumed as a
number. **No file under `docs/audit/`, `docs/publication/`, `AUDIT_LEDGER`/`QUEUE`,
`MISSING_DERIVATION_PROMPTS` was edited.** `docs/audit/data/` was parsed
READ-ONLY. No row/effective status set; no audit verdict asserted. Independent
audit required before any effective-retained movement.
