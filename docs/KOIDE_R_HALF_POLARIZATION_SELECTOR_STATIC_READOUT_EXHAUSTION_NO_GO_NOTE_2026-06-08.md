# Koide r=1/2 Polarization Selector: Static-Readout Reframe Exhaustion — No-Go Note

> **Key terms used in this doc** are indexed A-Z at
> [docs/KEY_TERMINOLOGY.md](KEY_TERMINOLOGY.md); each row points to the
> canonical source-of-truth doc.

**Date:** 2026-06-08
**Type:** named-obstruction no-go (reframe-space exhaustion)
**Claim type:** no_go
**Status:** no-go proposal. Sharpens the standing Koide r=1/2 admission (`AC_φλ`):
the holomorphic-vs-real polarization selector is **not** chosen by any *static*
framework structure; the selection is intrinsically dynamical, and the clean
dynamics give r=1. Adds no axiom, no fitted/imported value. Audit verdict set by
the independent audit lane.
**Authority role:** no-go source proposal.
**Primary runners:**
[`scripts/koide_polarization_wall_verification_2026_06_08.py`](../scripts/koide_polarization_wall_verification_2026_06_08.py)
(the sesquilinear-modulus wall, PASS=5) and
[`scripts/koide_jcs_measure_neutral_2026_06_08.py`](../scripts/koide_jcs_measure_neutral_2026_06_08.py)
(the native complex structure is measure-neutral, PASS=6); exact sympy/numpy.

## The atom

On the C3 generation triplet the Yukawa fluctuation splits into a trivial isotype
(real singlet `a`, energy `E_s = 3a²`) and a conjugate-pair doublet (complex `b`,
energy `E_d = 6|b|²`). Koide `r = |b|²/a²`, `Q = 1/3 + (2/3)r`; `r=1/2 ⇔ Q=2/3`
(the observed charged-lepton value). The **whole admission** is one binary: does
the generation readout count the complex doublet `b` as **one holomorphic mode**
`(1,1) → r=1/2`, or **two real modes** `(Re b, Im b)`, `(1,2) → r=1`? Everything
else (carrier, `Q=1/3+(2/3)r`, the 2-sector split, the topological `2/9`, `r=1/2`
as the equipartition stationary point) is derived; only this polarization is open.

## What was done

An exhaustive adversarial reframing of the **static** polarization selector: 14
prior refuted/attempted routes mapped, then **8 genuinely-new selection-principle
lenses** (framework-native complex structure `J_cs`; geometric quantization /
Kähler polarization; minimum-information / MDL record; equivariant holomorphic
index; KMS / modular; Grassmann / Pfaffian statistics; CPT / antiunitary; canonical
quantization uniqueness). Each was attacked and put through independent adversarial
verification. **Result: 0 of 8 survived** (every carried frame refuted unanimously).

## Why every static route fails (the three terminal walls)

1. **The Koide magnitude is a sesquilinear energy, not a determinant or a
   mode-count — and its modulus is rank-2.** `E_d = Tr(M†M)|_doublet = 6|b|²`; its
   real Hessian over `(Re b, Im b)` is `diag(12,12)`, **rank 2** → two real modes →
   `(1,2) → r=1`. This is the `#2624` Coleman-Weinberg modulus wall, robust for any
   smooth modulus `f(|b|²)` (verified: the wall runner). The det_C-vs-det_R
   distinction is real but lives on `det(M)` (the operator), where `det_R=|det_C|²`;
   the Koide magnitude is **not** a determinant of `M`. Transferring an
   operator-symmetry onto "the energy counts `b` once" is a category slip and is
   **circular** (it assumes the asymmetric `(1,1)` split it claims to derive).
2. **The framework's native complex structure is measure-neutral.** The one native
   "i" on the generation space is `J_cs = (C − C²)/√3` (verified: real
   antisymmetric, spectrum `{0,±i}`, `J_cs² = −(I−P_triv)`). It commutes with every
   circulant `M` (`[J_cs, M]=0`) and generates an **SO(2)** flow (`det=+1`) on the
   doublet that **preserves** the eigenvalue magnitudes, `|det M|`, the `M†M`
   spectrum, `E_d`, and `r` for all θ (verified: the J_cs runner). A static complex
   structure that commutes with `M` and preserves every measure can **define** a
   holomorphic readout but provably cannot **select** it — both `(1,1)` and `(1,2)`
   are `J_cs`-invariant. `J_cs` rotates the doublet **phase** (the δ channel), never
   the **magnitude** (r).
3. **Holomorphy moves the phase, not the magnitude; and GQ gives additive, not
   multiplicative, shifts.** The only honestly-holomorphic doublet scalars are
   powers `bᵏ`; the lowest carries `arg(b²)=2·arg(b)=δ` (the phase channel,
   `KOIDE_FLUCTUATION_MODULUS...` η→δ), not r. Geometric quantization confirms it
   from the other side: a Kähler polarization yields only **additive** half-form /
   metaplectic / Riemann-Roch shifts, never the **multiplicative** ½ on the `|b|²`
   coefficient (`6→3`) that `r=1/2` requires.

Net: every holomorphic-count route terminates in one of {rank-2 sesquilinear
modulus → r=1; measure-neutral static structure; circularity}. No *static*
framework object — native i / `J_cs`, taste, ε, CPT, θ, KO-dimension — is a
measure/polarization selector. The Record axiom itself supplies no weighting,
normalization, or occupancy rule (`MINIMAL_AXIOMS_2026-06-05`), so it cannot force
the holomorphic polarization either.

## The one remaining opening (dynamical, currently leaning r=1)

A genuine count-once needs either a SUSY superpotential (chiral protection,
holomorphic by construction) — which the framework **lacks** (Seiberg) — or a
**dynamical first-order / index** realization of the readout (not the second-order
modulus). That is the only non-circular place `r=1/2` could live, and it is
*currently leaning r=1*: the landed
`KOIDE_KAHLER_DIRAC_REALIZATION_GIVES_R_ONE_INDEX_ROUTE_CLOSED_BOUNDED_NO_GO_NOTE_2026-06-08`
finds the explicit Cl(3)/Kähler-Dirac realization gives `det D = |det M|² → r=1`,
and the index gives a signed mode-count in `{±1,±3}`, not a ½-reweight. The decisive
open sub-question (the AC_φλ staggered-Dirac corner realization): does the actual
matter action deliver a *first-order* `det D` (Pfaffian/index, count-once) or the
*second-order* modulus (`det D†D`, rank-2, count-twice)?

## Verdict

The Koide r=1/2 polarization is an **irreducible admission**, structurally on par
with `AC_φλ` and `θ` (`ADMITTED_INPUT_REGISTRY_TIER_A`). `r=1/2` is **not forbidden**
— it is the un-forced one-complex-slot readout — but it is **measure-neutral to every
static framework structure**, so it is not derived. The static-readout reframe space
is exhausted (8 lenses, 0 survivors). The framework does **not** derive Koide r=1/2;
the 45-year problem (Rivero-Gsponer: `|b|/a=1/√2` "not from first principles") is not
solved here.

## What is and is not claimed

- **Is:** no *static* framework structure selects the holomorphic `(1,1)` count;
  the native `J_cs` is measure-neutral; the magnitude is the rank-2 sesquilinear
  modulus → r=1; the static-readout reframe space is exhausted (8 lenses).
- **Is not:** does **not** claim r=1/2 is impossible, nor that the dynamical
  staggered-Dirac gate is closed (its first-order construction is not yet done,
  though its index route is). Introduces no axiom and changes no prediction.

## Load-bearing inputs

- [`MINIMAL_AXIOMS_2026-06-05.md`](MINIMAL_AXIOMS_2026-06-05.md) — the C3 generation
  circulant structure and the Record "no weighting/occupancy rule" disclaimer; the
  C3/linear-algebra facts (J_cs, rank-2 modulus) are reproven in the two runners.

Graveyard context (plain references — what this no-go confirms/sharpens, not
load-bearing deps): `KOIDE_FLUCTUATION_MODULUS_GIVES_R_ONE_CHIRALITY_IS_PHASE_ONLY_FRONTIER_CORRECTION_NOTE_2026-06-04`,
`KOIDE_RECORD_ORBIT_COUNT_DOES_NOT_SELECT_R_HALF_NO_GO_NOTE_2026-06-07`,
`KOIDE_DOUBLET_IS_FROBENIUS_SCHUR_COMPLEX_TYPE_ORIENTATION_BOUNDED_NOTE_2026-06-07`,
`KOIDE_R_HALF_INDEX_READOUT_NON_SUSY_STAGGERED_DIRAC_GATE_META_NOTE_2026-06-05`,
`KOIDE_KAHLER_DIRAC_REALIZATION_GIVES_R_ONE_INDEX_ROUTE_CLOSED_BOUNDED_NO_GO_NOTE_2026-06-08`,
`ADMITTED_INPUT_REGISTRY_TIER_A_NOTE_2026-05-23`.

## Forbidden-imports check

No PDG / fitted / literature numerical comparator is consumed. The C3 circulant
spectrum, the `J_cs` complex structure and its SO(2)/measure-neutral flow, the
rank-2 modulus Hessian, and the weighting→r law are reproven in the runners.
Rivero-Gsponer and Seiberg are named as comparator/context, not derivation inputs.
