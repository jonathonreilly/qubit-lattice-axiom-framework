# P-HY ABJ Anomaly Trace Core From Retained Anchors — Decoupled From the `anomaly_forces_time` ABJ Bridge (Bounded Theorem)

**Date:** 2026-06-20
**Type:** bounded_theorem
**Claim type:** bounded_theorem
**Branch:** physics-loop/anomaly-abj-bridge-block03-20260620
**Status:** source note awaiting independent audit handling. Status authority is
the independent audit lane only; this note asserts no audit verdict and claims
no "retained"/"promoted" standing. **Audit-readiness purpose:** its load-bearing
dependencies are all retained-grade, so the row is deps-all-retained ("ready")
and does **not** route through the unaudited keystone
`anomaly_forces_time_abj_inconsistency_accepted_premise_bridge_bounded_note_2026-05-26`
(ledger=unaudited; fanout 1105) or its unaudited parent
`anomaly_forces_time_theorem`.
**Primary runner:**
[`scripts/frontier_abj_phy_core_bank_2026_06_20.py`](../scripts/frontier_abj_phy_core_bank_2026_06_20.py)
(**TOTAL: PASS=63 FAIL=0**, exact `fractions.Fraction` + explicit Gell-Mann /
Pauli matrices; cache
[`logs/runner-cache/frontier_abj_phy_core_bank_2026_06_20.txt`](../logs/runner-cache/frontier_abj_phy_core_bank_2026_06_20.txt)).

```yaml
Type: bounded_theorem
Claim type: bounded_theorem
deps_all_retained: true
keystone_decoupled: true
proposal_allowed: false
bare_retained_allowed: false
audit_required_before_effective_retained: true
independent_audit_lane_sole_authority: true
```

## Why this note exists (audit-unblock)

The P-HY edge of the ABJ accepted-premise bridge consumes a step-B1 left-handed
anomaly trace tuple. That tuple is correct, but as written it sits behind the
unaudited keystone bridge and its unaudited parent (both with documented circular
admissions), so the arithmetic is not separately auditable. This note reproves
the **load-bearing arithmetic** of that tuple from retained anchors plus
**explicit, named admissions**, so the result is auditable on its own. It is the
same decoupling move as
[`SM_ANOMALY_CLOSURE_RETAINED_ANCHORS_DECOUPLED_BOUNDED_THEOREM_NOTE_2026-06-08`](SM_ANOMALY_CLOSURE_RETAINED_ANCHORS_DECOUPLED_BOUNDED_THEOREM_NOTE_2026-06-08.md)
(deps-all-retained; ledger `effective_status=retained_pending_chain`,
`chain_closes=True`), applied to the P-HY edge: the physical hypercharge
identification stays a **named admitted premise**, and only the scale-free
arithmetic is banked.

## Premises

- **(R1, retained)** Native cubic `SU(2)` gauge structure and `N_c = 3` colour,
  with the `gl(3)+gl(1)` split and the LH hypercharge-like u(1) spectrum:
  [`GRAPH_FIRST_SU3_INTEGRATION_NOTE.md`](GRAPH_FIRST_SU3_INTEGRATION_NOTE.md)
  (`effective_status=retained`, `chain_closes=True`, `positive_theorem`).
- **(R2, decoration under R1)** The bounded LH abelian eigenvalue surface
  `{+1/3 ×6, −1 ×2}`:
  [`NATIVE_GAUGE_LEFT_HANDED_ABELIAN_SURFACE_BOUNDED_NOTE_2026-05-23.md`](NATIVE_GAUGE_LEFT_HANDED_ABELIAN_SURFACE_BOUNDED_NOTE_2026-05-23.md)
  (`effective_status=decoration_under_graph_first_su3_integration_note`,
  `chain_closes=True`).
- **(R3, decoration under R1)** The traceless `+1/3 : −1` (i.e. `1 : (−3)`)
  hypercharge ratio on the LH doublets:
  [`LH_DOUBLET_TRACELESS_ABELIAN_EIGENVALUE_RATIO_NARROW_THEOREM_NOTE_2026-05-02.md`](LH_DOUBLET_TRACELESS_ABELIAN_EIGENVALUE_RATIO_NARROW_THEOREM_NOTE_2026-05-02.md)
  (`effective_status=decoration_under_graph_first_su3_integration_note`,
  `chain_closes=True`).
- **(Axiom)** The `{Lattice, Quantum, Record}` baseline:
  [`MINIMAL_AXIOMS_2026-06-05.md`](MINIMAL_AXIOMS_2026-06-05.md) (ledger `meta`;
  chain-satisfies, listed separately, not a retained dep).
- **(P, admitted premise — stated, not imported)** the **is-gauged predicate**:
  that the canonical traceless u(1) direction supplied by (R1)–(R3) IS the
  gauged, anomaly-relevant U(1) entering the ABJ test. This is the single
  surviving P-HY identification admission (block01/02: the wall shrank to exactly
  this predicate); it is **not** derived here and **not** imported from the
  keystone bridge or `anomaly_forces_time_theorem`.
- **(External, comparator)** Standard ABJ anomaly trace bookkeeping (Adler 1969;
  Bell–Jackiw 1969), Dynkin indices `T(3)=T(2)=1/2`, `SU(3)` cubic normalization
  `A(3)=+1` (nonvanishing symmetric `d_abc`). These are named external
  mathematical facts, **reproven in-runner** (Part D) where arithmetical.

## Statement and result

**Theorem (bounded, conditional on (P)).** Under (R1)–(R3), the axiom baseline,
and the admitted is-gauged predicate (P): on the scale-free LH abelian surface

```
Y_a = a · (P_sym − 3 P_anti)     (P_sym mult 6 at +a ; P_anti mult 2 at −3a)
```

the left-handed ABJ anomaly traces are, exactly,

```
Tr[Y] = 0 ,   Tr[Y^3] = −48 a^3 ,   Tr[SU(3)^2 Y] = a ,
Tr[SU(2)^2 Y] = 0 ,   Tr[SU(3)^3]_LH = 2 ,
```

which specialize at the SM normalization `a = 1/3` to the keystone step-B1 tuple

```
{ Tr[Y]=0 ,  Tr[Y^3]=−16/9 ,  Tr[SU(3)^2 Y]=1/3 ,  Tr[SU(2)^2 Y]=0 ,
  Tr[SU(3)^3]_LH = 2 } .
```

The three nonzero traces (`Tr[Y^3]`, `Tr[SU(3)^2 Y]`, `Tr[SU(3)^3]_LH`) are
nonzero for **every** `a ≠ 0`; they are forced by the native `1 : (−3)` ratio
(R3) alone. This reproduces the step-B1 arithmetic of the keystone bridge
**without** its dependency on the unaudited keystone or
`anomaly_forces_time_theorem`. (Runner Parts A, B.)

## Honest forced / admitted / convention ledger

What is **forced** (given the surface and the is-gauged premise): the five trace
**values** above and their scale-free **shape**. What is **not** forced (verified
in the runner):

- **C1 (admission — is-gauged).** That the canonical traceless u(1) direction IS
  the *gauged* anomaly-relevant U(1) is an admitted dynamical predicate; A_min's
  `{Lattice, Quantum, Record}` withholds the gauge group / which-symmetry-is-gauged
  (block01/02 named wall). The **direction** is canonical (retained graph_first);
  only **gaugedness** is admitted. This is strictly narrower than the prior "full
  physical U(1)_Y identification" admission.
- **C2 (convention — the absolute scale α=1/3).** **NOT load-bearing.** Part C
  reproves the block01 **B2 homogeneity lemma**: every anomaly polynomial is
  homogeneous in `Y` (degree-1 traces scale by `λ`, the degree-3 `Tr[Y^3]` by
  `λ^3`, and `Tr[SU(3)^3]_LH` is scale-independent), so `{all anomalies = 0}` is
  invariant under `Y → λ Y` (verified `λ ∈ {2, −5, 1/7}`). Hence the absolute
  scale `a` (i.e. `α = 1/3`) is a free normalization **for the anomaly test**;
  only the `1 : (−3)` ratio is content. `hypercharge_identification_note` and
  `hypercharge_alpha_third_normalization_bridge_bounded_note_2026-05-25` are
  therefore kept **named, NOT in the load-bearing dep set**. (They are
  `retained_bounded`/`chain_closes=True`; they remain load-bearing only for the
  separate physical electric-charge value match, which is not banked here.)
- **C3 (convention — species naming).** The naming "colour-charged ≡ quark" is a
  definitional SM convention A_min does not supply; it is **not** load-bearing
  for the anomaly polynomial (only the rep content `3` vs `1` and the
  hypercharge values enter). The rep-content map `Sym²→3`, `Anti²→1` is the
  retained decoration content, not an admission.

## What this does and does not claim

- **Does:** given retained (R1)–(R3) and the admitted is-gauged predicate (P),
  the five LH anomaly traces take the stated scale-free values, specializing to
  the keystone B1 tuple at `a=1/3` — reproven from retained anchors, decoupled
  from `anomaly_forces_time`.
- **Does not** derive the is-gauged predicate (P), nor the matter **content** /
  chiral reps, nor the right-handed completion (that is the separate P-COMP
  edge), nor fix the absolute `Y`-scale (C2), nor name the species (C3).
- **Does not** assert the ABJ anomaly-to-inconsistency implication (the separate
  external P-ABJ admission, B2) — only the consumed LH trace **inputs** are
  banked here.
- Introduces **no** new axiom and **no** new primitive; changes **no** numerical
  prediction.

## Reprove-and-cite

- The trace arithmetic (five traces, scale-free shape, the C1–C3 caveats), the
  surface multiplicities `{+1/3 ×6, −1 ×2}`, the `1:(−3)` ratio, the homogeneity
  lemma, and the `su(3)`/`su(2)` index normalizations (`T(F)=1/2`, nonzero
  `d_abc`) are **reproven exactly in the runner** (Parts 0, A, B, C, D), not
  asserted by name.
- Prior packaging of the same arithmetic — cited as **context only**, NOT as
  load-bearing markdown deps, to keep this row deps-all-retained:
  block01 P-HY routes runner
  [`scripts/frontier_abj_phy_identification_routes_2026_06_20.py`](../scripts/frontier_abj_phy_identification_routes_2026_06_20.py)
  (**PASS=41**); block01 bankability runner
  [`scripts/frontier_abj_arithmetic_cores_bankability_2026_06_20.py`](../scripts/frontier_abj_arithmetic_cores_bankability_2026_06_20.py)
  (**PASS=55**); block02 synthesis verification
  [`scripts/frontier_abj_block02_synthesis_verification_2026_06_20.py`](../scripts/frontier_abj_block02_synthesis_verification_2026_06_20.py)
  (**PASS=29**). These are **absorbed by path + PASS**, not rebuilt; this note's
  primary runner re-derives the load-bearing arithmetic independently.
- Banking precedent:
  `SM_ANOMALY_CLOSURE_RETAINED_ANCHORS_DECOUPLED_BOUNDED_THEOREM_NOTE_2026-06-08`
  (`retained_pending_chain`).
- Adler 1969; Bell–Jackiw 1969 — external comparator authorities.

## Forbidden-imports check

No PDG values, fitted selectors, or literature numerical comparators are used as
derivation inputs. The ABJ trace bookkeeping, Dynkin indices, and `SU(3)` cubic
normalization are named external mathematical content (comparator role),
reproven-in-runner. The absolute `Y`-scale (`α=1/3`) is treated as a convention
(C2), not consumed as a number. No load-bearing fact routes through the unaudited
keystone bridge or `anomaly_forces_time_theorem`.

## Firewall / source-discipline attestation

New artifacts only: this note, the primary runner
`scripts/frontier_abj_phy_core_bank_2026_06_20.py`, and its cache
`logs/runner-cache/frontier_abj_phy_core_bank_2026_06_20.txt`. **No file under
`docs/audit/`, `docs/publication/`, AUDIT_LEDGER/QUEUE,
MISSING_DERIVATION_PROMPTS was edited.** `docs/audit/data/` was parsed READ-ONLY
(python) for `effective_status`/`chain_closes`. No row/effective status set; no
audit verdict asserted. **The independent audit lane is the sole authority**
before any effective-retained movement. No `git checkout/commit/push/fetch` was
run (orchestrator owns git).

---
*Block 03 of the anomaly_forces_time ABJ bridge attack: banks the block01 P-HY
arithmetic core as a standalone deps-all-retained, keystone-decoupled conditional
bounded theorem. Mirrors the `SM_ANOMALY_CLOSURE_RETAINED_ANCHORS_DECOUPLED`
precedent.*
