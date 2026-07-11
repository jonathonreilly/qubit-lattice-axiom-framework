# Koide r=1/2 Polarization Selector: Tested Static-Readout No-Go

> **Key terms used in this doc** are indexed A-Z at
> [docs/KEY_TERMINOLOGY.md](KEY_TERMINOLOGY.md); each row points to the
> canonical source-of-truth doc.

**Date:** 2026-06-08
**Current premise authority (2026-07-11):** every Tier-A/admission/registry
reference below is superseded historical context. It supplies no premise and
makes no dependency ready; the scientific conditions remain conditional/open.
**Type:** named-obstruction no-go (tested static-selector class)
**Claim type:** no_go
**Status:** no-go proposal. Sharpens the standing Koide r=1/2 admission (`AC_φλ`):
the tested static holomorphic-vs-real polarization selectors do **not** choose
the `(1,1)` count. The remaining live opening is dynamical/first-order/index
readout; this note does not close that opening. Adds no axiom, no fitted/imported
value. Audit verdict set by the independent audit lane.
**Authority role:** no-go source proposal.
**Primary runner:**
[`scripts/koide_static_readout_no_go_2026_06_08.py`](../scripts/koide_static_readout_no_go_2026_06_08.py)
(aggregate: rank-2 sesquilinear-modulus wall, PASS=5; native complex structure
measure-neutrality, PASS=6).
**Cached runner output:**
[`logs/runner-cache/koide_static_readout_no_go_2026_06_08.txt`](../logs/runner-cache/koide_static_readout_no_go_2026_06_08.txt).
**Component runners:**
[`scripts/koide_polarization_wall_verification_2026_06_08.py`](../scripts/koide_polarization_wall_verification_2026_06_08.py) and
[`scripts/koide_jcs_measure_neutral_2026_06_08.py`](../scripts/koide_jcs_measure_neutral_2026_06_08.py).

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

An adversarial reframing of the **static** polarization selector class: 14
prior refuted/attempted routes mapped, then **8 selection-principle
lenses** were tested (framework-native complex structure `J_cs`; geometric quantization /
Kähler polarization; minimum-information / MDL record; equivariant holomorphic
index; KMS / modular; Grassmann / Pfaffian statistics; CPT / antiunitary; canonical
quantization uniqueness). **Result inside the tested class: 0 of 8 survived.**
This is not a universal theorem over every imaginable future static construction.

## Why the tested static routes fail (the three terminal walls)

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

Net: the tested holomorphic-count routes terminate in one of {rank-2
sesquilinear modulus → r=1; measure-neutral static structure; circularity}.
No tested *static* framework object — native i / `J_cs`, taste, ε, CPT, θ,
KO-dimension — supplies a measure/polarization selector. The Record axiom itself
supplies no weighting, normalization, or occupancy rule
([`MINIMAL_AXIOMS_2026-06-05.md`](MINIMAL_AXIOMS_2026-06-05.md)), so it cannot
force the holomorphic polarization either.

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

The tested static-selector class does not derive Koide `r=1/2`. The polarization
therefore remains an explicit unresolved sub-residual inside the `AC_φλ` Tier-A
target
(`docs/ADMITTED_INPUT_REGISTRY_TIER_A_NOTE_2026-05-23.md`);
it is not a new axiom and not a new primitive. `r=1/2` is **not forbidden** — it is
the un-forced one-complex-slot readout — but it is measure-neutral to every tested
static framework structure. This static-readout class does not derive Koide
`r=1/2`.

## What is and is not claimed

- **Is:** no tested *static* framework structure selects the holomorphic `(1,1)` count;
  the native `J_cs` is measure-neutral; the magnitude is the rank-2 sesquilinear
  modulus → r=1; the tested static-readout reframe class has no survivor.
- **Is not:** does **not** claim r=1/2 is impossible, nor that the dynamical
  staggered-Dirac gate is closed (its first-order construction is not yet done,
  though its index route is). Introduces no axiom and changes no prediction.

## Load-bearing inputs

- [`MINIMAL_AXIOMS_2026-06-05.md`](MINIMAL_AXIOMS_2026-06-05.md) — the C3 generation
  circulant structure and the Record "no weighting/occupancy rule" disclaimer; the
  C3/linear-algebra facts (J_cs, rank-2 modulus) are reproven in the two runners.
- [`KOIDE_RECORD_ORBIT_COUNT_DOES_NOT_SELECT_R_HALF_NO_GO_NOTE_2026-06-07.md`](KOIDE_RECORD_ORBIT_COUNT_DOES_NOT_SELECT_R_HALF_NO_GO_NOTE_2026-06-07.md) — prior Record-orbit count route-pruning no-go.
- [`KOIDE_FLUCTUATION_MODULUS_GIVES_R_ONE_CHIRALITY_IS_PHASE_ONLY_FRONTIER_CORRECTION_NOTE_2026-06-04.md`](KOIDE_FLUCTUATION_MODULUS_GIVES_R_ONE_CHIRALITY_IS_PHASE_ONLY_FRONTIER_CORRECTION_NOTE_2026-06-04.md) — prior modulus/chirality route correction.
- [`KOIDE_KAHLER_DIRAC_REALIZATION_GIVES_R_ONE_INDEX_ROUTE_CLOSED_BOUNDED_NO_GO_NOTE_2026-06-08.md`](KOIDE_KAHLER_DIRAC_REALIZATION_GIVES_R_ONE_INDEX_ROUTE_CLOSED_BOUNDED_NO_GO_NOTE_2026-06-08.md) — explicit Kähler-Dirac/index route boundary.
- [`KOIDE_DOUBLET_IS_FROBENIUS_SCHUR_COMPLEX_TYPE_ORIENTATION_BOUNDED_NOTE_2026-06-07.md`](KOIDE_DOUBLET_IS_FROBENIUS_SCHUR_COMPLEX_TYPE_ORIENTATION_BOUNDED_NOTE_2026-06-07.md) — complex-type/orientation support boundary.
- [`AC_ORBIT_OCCUPANCY_STATISTICAL_GRAIN_DERIVATION_OBLIGATION.md`](AC_ORBIT_OCCUPANCY_STATISTICAL_GRAIN_DERIVATION_OBLIGATION.md) — current zero-weight open dependency for the physical occupancy grain.
- `docs/ADMITTED_INPUT_REGISTRY_TIER_A_NOTE_2026-05-23.md` — historical provenance only.

Graveyard context (plain references — what this no-go confirms/sharpens, not
load-bearing deps): `KOIDE_R_HALF_INDEX_READOUT_NON_SUSY_STAGGERED_DIRAC_GATE_META_NOTE_2026-06-05`.

## Forbidden-imports check

No PDG / fitted / literature numerical comparator is consumed. The C3 circulant
spectrum, the `J_cs` complex structure and its SO(2)/measure-neutral flow, the
rank-2 modulus Hessian, and the weighting→r law are reproven in the runners.
Rivero-Gsponer and Seiberg are named as comparator/context, not derivation inputs.

## No-Go Discipline Gate

**Status:** PASS for the narrowed claim: the tested static-selector class does
not select `r=1/2`. This gate does **not** certify a universal negative against
dynamical, off-circulant, or future first-order/index constructions.

**N1 — Alternative route enumeration.**

| Route | Marker | Why it fails inside this scope |
|---|---|---|
| Sesquilinear modulus / CW magnitude | ATTEMPTED | The wall runner gives rank-2 Hessian over `(Re b, Im b)`, hence `(1,2) -> r=1`; matches [`KOIDE_FLUCTUATION_MODULUS_GIVES_R_ONE_CHIRALITY_IS_PHASE_ONLY_FRONTIER_CORRECTION_NOTE_2026-06-04.md`](KOIDE_FLUCTUATION_MODULUS_GIVES_R_ONE_CHIRALITY_IS_PHASE_ONLY_FRONTIER_CORRECTION_NOTE_2026-06-04.md). |
| Native complex structure `J_cs` | ATTEMPTED | The `J_cs` runner proves a measure-preserving `SO(2)` flow: it defines phase/holomorphy but does not select the magnitude count. |
| Record orbit count | RULED OUT BY PRIOR | Record names realized outcomes but supplies no weighting/occupancy rule; the orbit-count route is pruned in [`KOIDE_RECORD_ORBIT_COUNT_DOES_NOT_SELECT_R_HALF_NO_GO_NOTE_2026-06-07.md`](KOIDE_RECORD_ORBIT_COUNT_DOES_NOT_SELECT_R_HALF_NO_GO_NOTE_2026-06-07.md). |
| Kähler-Dirac/index count-once route | RULED OUT BY PRIOR for the explicit realization | The explicit realization gives `det D=|det M|^2 -> r=1`, not the first-order count, in [`KOIDE_KAHLER_DIRAC_REALIZATION_GIVES_R_ONE_INDEX_ROUTE_CLOSED_BOUNDED_NO_GO_NOTE_2026-06-08.md`](KOIDE_KAHLER_DIRAC_REALIZATION_GIVES_R_ONE_INDEX_ROUTE_CLOSED_BOUNDED_NO_GO_NOTE_2026-06-08.md). |
| Complex-type/orientation/Frobenius-Schur route | RULED OUT BY PRIOR as selector | The complex-type/orientation note supplies type information, not the asymmetric weighting rule; see [`KOIDE_DOUBLET_IS_FROBENIUS_SCHUR_COMPLEX_TYPE_ORIENTATION_BOUNDED_NOTE_2026-06-07.md`](KOIDE_DOUBLET_IS_FROBENIUS_SCHUR_COMPLEX_TYPE_ORIENTATION_BOUNDED_NOTE_2026-06-07.md). |
| Holomorphic phase/chirality route | RULED OUT BY PRIOR inside the tested modulus class | The phase/chirality route moves `arg(b)`/delta, not the magnitude weighting; see the fluctuation-modulus correction linked above. |

**N2 — Wall-independence audit.** Collapsed wall set:
`rank-2 modulus`, `measure-neutral static structure`, `Record/no weighting`,
and `explicit index route gives r=1`. Closing any one of these does not
automatically close the others; the claim is scoped to their intersection, not
inflated into independent Tier-A admissions.

**N3 — Hidden-wall scan.** "Standing admission" is resolved to the Tier-A
registry link above; "framework provides" is resolved to the minimal axiom memo;
"Record supplies" is explicitly negative and does not import a weighting rule;
"dynamical" is marked open, not silently closed.

**N4 — Residual matching.** The cited witnesses all attack the same residual:
whether a static/readout-side structure selects the asymmetric `(1,1)` doublet
count. The Kähler-Dirac/index witness is used only for the explicit built
realization; it is not used to close every possible future first-order route.

**N5 — Rhetoric audit.** The broad phrase "no static framework structure" has
been narrowed to "no tested static framework structure/class." Tested
resolutions: C3 circulant triplet, central/Record orbit count, native `J_cs`,
rank-2 real doublet modulus, and explicit Kähler-Dirac realization. Untested
resolutions remain outside scope.

**N6 — Partial-closure path scan.** The legitimate remaining path is an explicit
dynamical first-order/index readout that avoids the second-order modulus. A
convention or Record wording change alone does not supply the weighting rule,
because Record supplies no weighting/normalization/occupancy rule.

**N7 — Steelman.** A future off-circulant or first-order Pfaffian/index
construction could select a one-complex-slot readout before the second-order
modulus forms. That would break a universal negative, so this note does not claim
one; it only closes the tested static selector class.

**N8 — Cross-cycle echo.** Prior Koide re-walks retired several static routes
by sharpening the residual rather than adding axioms: Record orbit count,
modulus/chirality, and explicit Kähler-Dirac/index. The same mechanism applies
here: narrow the no-go to the tested static class and leave the dynamical
first-order/index route open.

## Current Dependency Routing (2026-07-11)

Historical decision records have zero premise weight. The unresolved content
used by this note is routed through the following current foundation or
zero-weight open obligation:

- [`AC_ORBIT_OCCUPANCY_STATISTICAL_GRAIN_DERIVATION_OBLIGATION.md`](AC_ORBIT_OCCUPANCY_STATISTICAL_GRAIN_DERIVATION_OBLIGATION.md)
