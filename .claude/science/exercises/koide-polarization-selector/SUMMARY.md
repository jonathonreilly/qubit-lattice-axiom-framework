# Exercise: the Koide r=1/2 polarization-selector wall

**Date:** 2026-06-07 · **Type:** /exercise reframe + attack pass · **Output:** a sharpened, correctly-oriented
attack map (NOT a closure). **Runner:** `verify_exercise_facts.py` (sympy, 12/12 exact).
**Refresher surfaces read:** MINIMAL_AXIOMS_2026-06-05, KOIDE_BEREZIN_DETC_VS_DETR_FORK_MECHANISM_NOTE_2026-06-04,
FLAVOR_RECORD_READOUT_FORM_NOT_WEIGHT_2026-06-02, tier_a_admissions.json (AC_φλ), SKILL freshness check (fresh).

## Exercise Zero — the wall (neutral)

Charged-lepton Koide `r = |b|²/a² = 1/2` (`Q = 2/3`). The C₃ generation mass operator `M = aI + bC + b̄C²`
(K/CPT-real → Hermitian) has a singlet and a doublet block. The native additive readout `I = log|det H|` counts
the doublet by real dimension (twice) → `r = 1` (`Q = 1`, the live partial-falsification). `r = 1/2` needs the
doublet counted once (holomorphic). The open positive route (Berezin-fork note): *derive a native polarization
selector, OR show the readout factors through the doublet complex-slot quotient.* Progress = a forced selector or
a decisive no-go. Currently leaned on: the `log|det|` readout (a conditional surface, not an axiom), the AC_φλ
staggered realization (open Tier-A gate).

## The re-orientation (corrects the refuted #3138)

A prior block (#3138, retracted) claimed `det_C = Pfaffian = Majorana → r=1/2` and was REFUTED for **inverting**
the landed Berezin table. This exercise establishes the **correct** orientation, reproven:

- The C₃ doublet is **Frobenius-Schur COMPLEX type** (FS(ω)=FS(ω̄)=0; ω≠ω̄). [runner (1)]
- So **`r = 1/2` is the FS-faithful** (complex/holomorphic/Dirac, 1 complex slot) reading; **`r = 1` is the
  FS-mistype** — realifying a complex-type irrep as if it were real-type (FS=+1). [runner (2)]
- Majorana/real ↔ `r = 1` (NOT `r = 1/2`). The refuted block had this backwards.

This rules out the entire "reality-class foreclosure" family in the *wrong* orientation and points the lever the
right way: `r = 1/2` is what a faithful (complex-type, complex-carrier) reading gives.

## Assumptions ledger — the load-bearing one

| assumption | source | what if wrong |
|---|---|---|
| readout = `log|det|` (multiplicative/additive) | OBSERVABLE_PRINCIPLE (conditional, not axiom) | a different additive readout could count once |
| the det is over the **real** form (2 real slots) | **implicit / unforced** ← THE CRUX | complex/holomorphic form → 1 slot → r=1/2 |
| the doublet's two reals are independent modes | Hermitian spectrum m_μ≠m_τ | they are a conjugate pair of ONE complex char (ω,ω̄) |
| the selector is a **static** structure | assumed | if dynamical (kinetic metric), static no-gos don't bind |

The crux assumption is **real-vs-holomorphic polarization of the generation field** — exactly the open atom.

## The obstruction (why FS=0 is necessary-not-sufficient)

The native flavor complex structure `J_cs=(C−C²)/√3` **commutes with the entire K/CPT-real mass family**
(`[J_cs,H]=0`), so it is **measure-neutral / silent on r** — it cannot select det_C over det_R. [runner (3)]
FS=0 + the complex `M₂(ℂ)` carrier **exclude** the r=1 mistype but do **not force** the holomorphic readout. The
selector cannot be static; it must be **dynamical** (the kinetic metric / the action). Two adversarial reviewers
confirmed: "complex carrier → holomorphic readout" is a category step (operator algebra vs field-integration
measure) that must be *derived*, not asserted — the same trap that sank #3138 if taken as a static claim.

## The candidate selector (the genuine new lever)

The **Quantum axiom supplies a dynamical selector candidate**: the qubit (spin-1/2) coherent-state manifold is
`CP¹` with the **Fubini-Study Kähler** metric [runner (4a)], and the spin-coherent-state action's kinetic term is
**first-order** — the Berry/symplectic potential `A_z = −i z̄/(1+|z|²)` with `dA =` the Kähler form [runner (4b)],
**not** a second-order real `|ż|²`. First-order/holomorphic = "count once" = `r=1/2`; second-order modulus =
"count twice" = `r=1`. So the framework's own carrier dynamics is intrinsically first-order/holomorphic — the
`r=1/2` side of the fork — *if* the flavor sector inherits it.

## Honest status — NOT closed

The wall is **sharpened and correctly oriented**, not broken. The core obstruction is unmoved: the native
`log|det|` readout is the dimension count (`r=1`); the holomorphic count (`r=1/2`) needs the dynamical selector,
and whether the flavor `b`-field inherits the qubit coherent-state's first-order holomorphic dynamics is the
**AC_φλ realization gate** — now a concrete calculation, not vague. Do **not** ship a closure.
