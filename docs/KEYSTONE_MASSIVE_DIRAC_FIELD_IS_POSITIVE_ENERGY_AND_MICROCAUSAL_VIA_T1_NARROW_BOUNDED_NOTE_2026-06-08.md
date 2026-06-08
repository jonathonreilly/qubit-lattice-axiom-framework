# The Massive Dirac Field Is Positive-Energy and Microcausal via T1 — the Keystone's Spectrum/Causality Piece Closes

**Date:** 2026-06-08
**Claim type:** bounded_theorem (a keystone residual-closure)
**Status authority:** independent audit lane only. This source note does not set, predict, or
estimate any audit verdict. Effective status is pipeline-derived after independent audit and
dependency closure.
**Primary runner:**
[`scripts/frontier_keystone_massive_dirac_t1_positive_energy_microcausal.py`](../scripts/frontier_keystone_massive_dirac_t1_positive_energy_microcausal.py)
**Cached log:**
[`logs/runner-cache/frontier_keystone_massive_dirac_t1_positive_energy_microcausal.txt`](../logs/runner-cache/frontier_keystone_massive_dirac_t1_positive_energy_microcausal.txt)
(TOTAL: PASS=8 FAIL=0)

## 0. What closes

The program's keystone — the emergent-time **massive Dirac field** that gates the chirality gate,
the `Q=2/3` chiral-mass mechanism, generation-ID, and the #1 `s3_time` gate — had two hard pieces
left after the chirality was supplied: **positive energy** and **microcausality**. This note closes
both. The retained-bounded
[`FLAVOR_CHIRALITY_GATE_NARROWS_TO_ONE_SPIN_STATISTICS_IMPORT_2026-05-31`](FLAVOR_CHIRALITY_GATE_NARROWS_TO_ONE_SPIN_STATISTICS_IMPORT_2026-05-31.md)
had already reduced the gate to a single engine — the spin-statistics forcing **T1**. With the
partner chirality now supplied (companion notes: the chiral grading is retained `Cl(3,1)`; the
`e_4` gamma is supplied by continuous emergent time, decoupled from the magnitude corner), **T1
fires**, and the massive Dirac field is positive-energy, microcausal, and boost-covariant. The
keystone's single remaining residual narrows to the **OS→Wightman field delivery**.

## 1. Inputs and live tiers (verified on `origin/main`, 2026-06-08)

| Input | Source | Live `effective_status` | Role |
|---|---|---|---|
| the chirality gate narrows to one spin-statistics import (T1) | [`FLAVOR_CHIRALITY_GATE_NARROWS_TO_ONE_SPIN_STATISTICS_IMPORT_2026-05-31`](FLAVOR_CHIRALITY_GATE_NARROWS_TO_ONE_SPIN_STATISTICS_IMPORT_2026-05-31.md) | `retained_bounded` | names the engine |
| the `{+E,+E,−E,−E}` particle/antiparticle `u`/`v` mode set | [`FREE_DIRAC_ANTIPARTICLE_MODE_ALGEBRA_BOUNDED_NOTE_2026-05-30`](FREE_DIRAC_ANTIPARTICLE_MODE_ALGEBRA_BOUNDED_NOTE_2026-05-30.md) | `retained_bounded` | the mode structure |
| emergent Lorentz / boost covariance | [`EMERGENT_LORENTZ_INVARIANCE_NOTE`](EMERGENT_LORENTZ_INVARIANCE_NOTE.md) | `retained_bounded` | boost-covariance surface |
| partner chirality supplied (the `e_4` gamma, decoupled from the corner) | companion `PARTNER_CHIRALITY_IS_THE_4TH_GAMMA…_2026-06-08` | (this session) | supplies T1's input |
| keystone reduction (algebra retained; field residual) | companion `CHIRALITY_GATE_AND_EMERGENT_TIME_GATE_ARE_ONE_KEYSTONE…_2026-06-08` | (this session) | the keystone framing |

No PDG value is load-bearing. No new axiom, import, or vocabulary.

## 2. T1 — the spin-statistics forcing (verified)

For the massive Dirac field `ψ = Σ_s [a_s u_s e^{-iEt} + b_s† v_s e^{+iEt}]`, the second-quantized
energy is `Ĥ = Σ E (a†a − b b†)`. Reordering `b b†` is governed by the **statistics**:

- **CAR** (`{b,b†}=1`): `b b† = 1 − b†b` ⟹ `Ĥ = Σ E (a†a + b†b) ≥ 0` — **positive energy**. The
  runner's single-mode Fock space gives eigenvalues `{0, E, E, 2E}`.
- **Bose** (`[b,b†]=1`): `b b† = 1 + b†b` ⟹ `Ĥ = Σ E (a†a − b†b)` — **unbounded below** (runner:
  min `−E·N → −∞`).

So CAR is the unique healthy quantization, and it yields positive energy. The sign-flip in the
reordering is the entire engine.

## 3. Microcausality and boost covariance (verified)

- **Microcausality.** The Dirac spinor completeness `Σ_s (u_s u_s† + v_s v_s†) = I_4` (verified)
  gives the **canonical** equal-time CAR anticommutator `{ψ_a, ψ_b†} = δ_{ab}` — the microcausal
  structure. The Bose combination `u u† − v v† ≠ I` is non-canonical (acausal). So the same
  statistics that fixes positivity fixes causality.
- **Boost covariance.** The mass term `m·I` is a **Lorentz scalar**: `S(η)^{-1}(mI)S(η) = mI`
  (verified). So the retained-bounded boost sector extends to the massive field — the mass does not
  break boost covariance.

## 4. The closure, and the narrowed residual

With the partner chirality supplied, the framework's massive Dirac field meets T1's hypothesis, and
T1 fires:

> the massive Dirac field is **positive-energy** (CAR `Ĥ ≥ 0`), **microcausal** (canonical CAR
> anticommutator), and **boost-covariant** (Lorentz-scalar mass).

This closes the keystone's spectrum/causality piece. The program's deepest object now has its
chirality DOF, positive energy, microcausality, and boost covariance all in hand; the **single
remaining residual** is the **OS→Wightman field delivery** — the reconstruction of the interacting
field on the emergent-time Hilbert space
([`FREE_FIELD_OS_WIGHTMAN_RECONSTRUCTION_CONDITIONAL_THEOREM_NOTE_2026-05-30`](FREE_FIELD_OS_WIGHTMAN_RECONSTRUCTION_CONDITIONAL_THEOREM_NOTE_2026-05-30.md),
the next target).

## 5. Scope — what this establishes and what remains

**Establishes (exact / finite):**
- T1's spin-statistics forcing for the framework's massive Dirac field: CAR ⟹ positive energy;
  Bose ⟹ unbounded below.
- Microcausality from spinor completeness (canonical CAR anticommutator).
- Boost covariance from the Lorentz-scalar mass term.
- Therefore, with the supplied chirality, the keystone's positive-energy / microcausality piece
  closes (bounded tier).

**Remains (the keystone's single narrowed residual):**
- The **OS→Wightman field delivery** — realizing the field on the reconstructed Hilbert space
  (currently conditional/unaudited). This note removes spectrum and causality from the residual; the
  reconstruction remains.
- Does **not** build the OS reconstruction; does **not** touch the firewalled `r=1/2`.

## 6. Honest verdict

The keystone's two hardest-sounding pieces — *does the massive field have positive energy, and is it
microcausal?* — are both **forced** once the chirality is supplied: the spin-statistics engine T1
makes CAR the unique healthy quantization (Bose is unbounded and acausal), and the Lorentz-scalar
mass keeps it boost-covariant. So the program's deepest object stands with chirality, positive
energy, microcausality, and boost covariance all in hand, resting on retained-bounded planks plus
the supplied chirality. The one remaining residual is the OS→Wightman field delivery — a
reconstruction problem, not a chirality, spectrum, or causality problem.

## 7. No-Go Discipline Gate

**Status:** PASS for this bounded closure. It does **not** claim the OS reconstruction is done; it
closes the spectrum/causality piece given the supplied chirality and the retained-bounded planks.

**N1 — Alternative-route enumeration.**

| Route | Marker | Result |
|---|---|---|
| Bose quantization of the Dirac modes | RULED OUT | `Ĥ` unbounded below; non-canonical (acausal) |
| CAR quantization | FORCED / HEALTHY | `Ĥ ≥ 0` (positive); canonical microcausal anticommutator |
| mass breaks boost covariance | RULED OUT | `m·I` is a Lorentz scalar |
| OS→Wightman field delivery | OPEN (narrowed residual) | the single remaining keystone piece |

**N2 — Wall-independence.** Spectrum/causality (this note) and the field delivery (OS
reconstruction) are distinct; closing the first narrows the keystone to the second.

**N3 — Hidden-wall scan.** Uses only the Dirac mode algebra, the CAR/Bose reordering, spinor
completeness, and the Lorentz-scalar mass — no hidden premise; the OS reconstruction is left open.

**N4 — Residual matching.** The remaining residual is exactly the OS→Wightman field delivery.

**N5 — Rhetoric audit.** The claim is a *forcing* (statistics fixes the sign) and a *closure of the
spectrum/causality piece*, not a construction of the interacting field.

**N6 — Partial-closure path scan.** The next step is the OS→Wightman reconstruction on the
emergent-time Hilbert space. No new axiom requested.

**N7 — Steelman.** A reviewer may hold that T1's forcing presupposes a fully relativistic field, so
emergent Lorentz must be unbounded first. The boost-covariance surface used here is retained-bounded
(`EMERGENT_LORENTZ_INVARIANCE`), and this note rests at that tier — it does not claim more than
retained-bounded for the relativistic structure; lifting to unbounded requires retiring that plank.

**N8 — Cross-cycle echo.** Consistent with the retained-bounded antiparticle mode algebra, the
retained-bounded emergent Lorentz, the retained-bounded chirality-narrows-to-spin-statistics import,
and the supplied chirality — assembling them without overruling any by prose.

## 8. Forbidden-imports check

- **No new axioms / imports / vocabulary.** Inputs are the cited retained-bounded rows plus the
  Dirac mode algebra and the CAR/Bose spin-statistics reordering.
- **No PDG/fitted load-bearing input; no new transcendental; no forcing of `r=1/2`.**

## 9. Command

```bash
python3 scripts/frontier_keystone_massive_dirac_t1_positive_energy_microcausal.py
```

Expected: `TOTAL: PASS=8 FAIL=0`. numpy + stdlib, deterministic, ≤16-dim (memory-safe). The runner
verifies the `±E` mode set, CAR positivity vs Bose unboundedness, the canonical microcausal CAR
anticommutator from spinor completeness, and the Lorentz-scalar mass.
