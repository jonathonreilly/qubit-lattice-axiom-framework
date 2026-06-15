# Spin-Statistics / FS: Cross-Site Fermion Sign Location and Open-Route Boundary (Exercise)

**Date:** 2026-06-06
**Claim type:** bounded_theorem (exercise location result + route-boundary portfolio)
**Status:** review-loop source proposal. Adds no axiom, no fitted input, no audit
verdict.
**Primary runner:**
[`scripts/frontier_exercise_spin_statistics_fs_admission_located_2026_06_06.py`](../scripts/frontier_exercise_spin_statistics_fs_admission_located_2026_06_06.py)
**Cached runner output:**
[`logs/runner-cache/frontier_exercise_spin_statistics_fs_admission_located_2026_06_06.txt`](../logs/runner-cache/frontier_exercise_spin_statistics_fs_admission_located_2026_06_06.txt)

---

## Role

Output of the repo's `/exercise` skill
([`docs/ai_methodology/skills/exercise/SKILL.md`](ai_methodology/skills/exercise/SKILL.md))
run as a full 5-subagent fan-out (assumptions ledger / Elon reduction / literature
/ mathematics-sector / reframing, each with a framework-refresher read) on the
spin-statistics / FS wall — the matter sector's highest-leverage residual
(it gates both FS and the chirality `ε`).

## Wall (neutral)

The per-site `Z₂` fermion-parity grading, Pauli exclusion, and the Berezin
determinant are **retained**; the **cross-site fermion exchange sign** (CAR / −1,
vs hard-core-boson CCR) is **not forced** from `{Lattice, Quantum, Record}`. A
hard-core boson has the same per-site dim 2 / `Z₂` grading / Pauli exclusion; only
the cross-site exchange sign differs. The standard spin-statistics theorem needs
Lorentz invariance + microcausality + positivity — the lattice lacks manifest
Lorentz (`axiom_first_spin_statistics_theorem` is unaudited).

## Verdict — checked location result, not global FS closure

The exact checked content is narrower than a global spin-statistics theorem. The
runner verifies the Cl(3) Pauli algebra obstruction and the elementary
`Hom(Z₂,U(1)) = {+1,-1}` sign dichotomy, and it guards that this note preserves
the multi-loop graded-net route as open. Literature and cross-note no-gos are
cited as comparators, not as independently rederived theorem steps by this
packet.

1. **Cl(3) does not supply the CAR grading** (verified). The per-site pseudoscalar
   `ω = σ₁σ₂σ₃ = i·I` has `ω² = −I` (*not* a `Z₂` involution), and the **only**
   operator anticommuting all three Paulis is `0` (the maximal-anticommuting /
   `d_s=3` fact). So the Cl(3) vector grade is *not* an inner `Z₂` grading on the
   qubit; the CAR grading is the **Fock parity** `F = (−1)^n = σ₃`, which requires
   choosing which basis state is "occupied" — a datum the Quantum axiom does not
   supply.
2. **Topology gives only the dichotomy, never the sign.** The 2-particle exchange
   class is order-2 (anyons excluded), but `Hom(Z₂, U(1)) = {+1, −1}` admits
   **both** boson and fermion; the first-quantized configuration-space route is
   **sign-blind** (Koszul vs ungraded boundary maps give identical `Z₂` torsion).
   Sharper `Z³` witness from the fan-out: the **3×3×2 box has
   `H₁(UD₂) = Z¹⁶ ⊕ Z₂`** — the smallest concrete `Z³` graph where the exchange
   `Z₂` appears (to be independently re-verified; the dichotomy itself is
   `retained_bounded` in the graph-braid notes).
3. **Precise location (the sharpest reframe).** The `Z₂` fermion-parity grading
   `F = (−1)^Q` is the retained central-sector datum from
   `fermion_parity_z2_grading_theorem`, identical in the boson and fermion
   frames. Record registers a supplied/derived central-sector label and
   explicitly "supplies no within-sector data." The exchange **sign** is
   within-sector data. So this packet locates the residual: Record is silent on
   the sign once the central grading is in place; it does not derive CAR. That is
   a location theorem/boundary, not a proof that every possible future FS route
   is globally closed.
4. **Literature no-go comparison.** Allen–Mondragon (quant-ph/0304088): "no
   spin-statistics connection in non-relativistic QM"; any derivation needs an
   extra premise ruling out spinless fermions. DHR superselection classifies
   (Bose/Fermi/para) but does not select the sign; Berry–Robbins is non-unique.

This is consistent with the four existing repo no-gos (`car_from_positivity`,
`staggered_dirac_substep1_statistics_agnostic`, `ring_monodromy_does_not_force_car`,
`FS_rotation_exchange_discrete_insufficiency`) but does not rederive those no-gos.

## 2026-06-12 audited scope narrowing

The load-bearing scope for re-audit is limited to the facts directly checked by
the runner:

1. the Cl(3) pseudoscalar is `i I`, squares to `-I`, and no nonzero `2 x 2`
   operator anticommutes with all three Pauli generators;
2. the exchange topology route supplies the order-two sign dichotomy
   `{+1, -1}` but does not select the sign;
3. the Record boundary used here is only that Record supplies no
   within-sector exchange-sign datum once the retained central fermion-parity
   label is in place.

The route portfolio below is not a closure theorem. In particular, the
multi-loop graded-net route is an open target, the continuum-migration route is
conditional on a future Lorentz/microcausality bridge, and the `3 x 3 x 2`
configuration-space witness remains a fan-out lead until independently
re-verified. Literature and existing repo no-gos are comparator/context
surfaces, not additional load-bearing proof steps in this note.

Thus this note is a bounded location certificate for the present FS admission.
It does not derive CAR, does not close spin-statistics, does not prove a
multi-loop no-go, and does not add a new axiom.

## Route portfolio

| Rank | Route | Outcome class | First artifact |
|---|---|---|---|
| 1 | **multi-loop graded-net cocycle consistency** (the one un-refuted opening) | possible forcing lemma | two linked Jordan-Wigner-string loops on a `Z³` patch — does a hard-core-boson framing survive *joint* single-valuedness, or does mutual consistency force −1? |
| 2 | **continuum migration** (emergent Lorentz → standard theorem applies) | migrate to the continuum frontier | complete the OS→Wightman reconstruction (rungs A–C) |
| 3 | **3×3×2 `Z³` box `H₁(UD₂)` witness** | sharpen the dichotomy | SNF on the actual `Z³` box (vs abstract `K₅`/`K₃,₃`) |
| — | graded-tensor / parity-superselection from `{L,Q,R}` | **infeasible** w/o new principle | (re-derives the admission) |

This exercise closes no route by itself. The multi-loop graded-net route remains
the live opening on the static baseline, and **no new axiom is invented** (the
protocol's forbidden outcome).

## Honest scope

This is a **location + route-boundary map**, not a closure. The retained
central-sector grading is not the within-sector exchange sign; Cl(3) does not
supply that sign; topology leaves a `+1/-1` dichotomy; and the multi-loop
graded-net consistency route remains un-refuted. The verified facts are exact;
the 3×3×2 `H₁` is from the fan-out and flagged for re-verification. No new axiom.

## Reprove-and-cite ledger

- **Reproven here** (runner): `ω = i·I`, `ω² = −I`, only `G=0` anticommutes all
  three Paulis; `Hom(Z₂,U(1)) = {±1}`; and the source-scope guards that keep the
  route portfolio non-closing.
- **Cited**: the four repo no-gos; `fermion_parity_z2_grading_theorem` (retained);
  the graph-braid dichotomy (retained_bounded); the Record axiom boundary
  (`MINIMAL_AXIOMS_2026-06-05`); literature (Allen–Mondragon, DHR, Berry–Robbins,
  Leinaas–Myrheim, Abrams/HKRS — comparators only).

## Audit dependency repair links

- [CAR_FROM_POSITIVITY_NEUTRALITY_NOTE_2026-06-02.md](CAR_FROM_POSITIVITY_NEUTRALITY_NOTE_2026-06-02.md)
- [AXIOM_FIRST_SPIN_STATISTICS_THEOREM_NOTE_2026-04-29.md](AXIOM_FIRST_SPIN_STATISTICS_THEOREM_NOTE_2026-04-29.md)
- [FERMION_PARITY_Z2_GRADING_THEOREM_NOTE_2026-05-02.md](FERMION_PARITY_Z2_GRADING_THEOREM_NOTE_2026-05-02.md)
- [GRAPH_BRAID_Z3_ANYON_EXCLUSION_DICHOTOMY_NARROW_THEOREM_NOTE_2026-05-29.md](GRAPH_BRAID_Z3_ANYON_EXCLUSION_DICHOTOMY_NARROW_THEOREM_NOTE_2026-05-29.md)
- [MINIMAL_AXIOMS_2026-06-05.md](MINIMAL_AXIOMS_2026-06-05.md)
