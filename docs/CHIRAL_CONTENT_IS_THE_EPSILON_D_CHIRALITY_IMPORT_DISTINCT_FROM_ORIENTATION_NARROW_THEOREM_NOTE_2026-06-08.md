# The Chiral-Content Admission Is the `{ε,D}=0` Staggered Chirality Import — a Distinct Recurring Import, Not the Gauge/Flavor Orientation `Z₂` (Narrow Theorem + Synthesis Correction)

> **Key terms used in this doc** are indexed A-Z at
> [docs/KEY_TERMINOLOGY.md](KEY_TERMINOLOGY.md); each row points to the
> canonical source-of-truth doc.

**Date:** 2026-06-08
**Type:** narrow finite-algebra theorem (distinctness) + correction to the unification narrative
**Claim type:** bounded_theorem
**Status:** proposal. Places the chiral-content admission (why `su(2)_L` gauges `P_L` =
parity violation) in the framework's admission floor, and **corrects** a loose
over-unification: the chiral content's `{ε,D}=0` gate is a **distinct** recurring import,
**not** the same `Z₂` as the gauge/flavor "orientation" objects. Adds no axiom, no fitted
value. Audit verdict set by the independent audit lane.
**Primary runner:**
[`scripts/chiral_content_distinct_recurring_import_2026_06_08.py`](../scripts/chiral_content_distinct_recurring_import_2026_06_08.py)
(exact numpy, PASS=5).

## Context

The chiral-content admission is already **consolidated**: the chirality grading, the
half-integer matter-carrier state-law, `r=1/2`'s chirality pin, and generation-identification
all reduce to **one** recurring gate, `{ε,D}=0` with `ε(x)=(−1)^{x+y+z}`
([`CARRIER_ATTACHMENT_CONSOLIDATES_TO_RECURRING_CHIRALITY_GATE_SHARPENING_NOTE_2026-06-06`](CARRIER_ATTACHMENT_CONSOLIDATES_TO_RECURRING_CHIRALITY_GATE_SHARPENING_NOTE_2026-06-06.md));
and Record is a **consumer** of chiral labels, never a chirality source
([`CHIRALITY_RECORD_TYPING_INTERFACE_2026-06-05`](CHIRALITY_RECORD_TYPING_INTERFACE_2026-06-05.md)).
This note answers a precise open question: does that chirality gate **unify** with the
"orientation `Z₂`" the session tied to the `δ`-sign and `θ`-sign? **It does not** — and
verifying that corrects a loose conflation.

## Result — three distinct objects, not one `Z₂`

The candidate "orientation/chirality" structures are **three different objects in three
sectors with different `K`-parity** (verified, finite numpy):

| object | sector | `K`-parity | role |
|---|---|---|---|
| `ε(x)=(−1)^{x+y+z}` (staggered) | **spatial** `Z³` site-grading | **even** (real) | the chirality grading; `{ε,D}=0` for the NN Dirac `D` |
| `ω=σ₁σ₂σ₃=i·I` (Cl(3) pseudoscalar) | **qubit** operator | **odd** (`Kω=−ω`) | the gauge/`F̃F` spacetime orientation |
| `sign(Vandermonde)` | **generation** handedness | **even** (real) | the generation/`δ`-sign orientation |

Because `ω` is `K`-**odd** while `ε` and the Vandermonde are `K`-**even**, and all three live
in different sectors, **they cannot be the same `Z₂`**. So:

- **The chiral-content gate is `{ε,D}=0`** — the staggered, K-even, *spatial* chirality grading.
- The chiral **gauging** (chiral-vs-vector, i.e. the `r` chiral-vs-vector binary) is an import
  `ε` is **blind** to: `[ε, T^a]=0` and the dressed connection (`D·T^a`, `D·T^a·P_L`,
  `D·T^a·P_R`) all anticommute with `ε` identically — `ε` fixes the grading, not the coupling.
  Record (a consumer) cannot supply it.

## Synthesis correction

Earlier session prose (the strong-CP parity note and the admission-floor synthesis) loosely
wrote the gauge orientation as "`ω = sign(Vandermonde) = one orientation `Z₂`." That is an
**over-unification**: the gauge `F̃F` is sourced by the `K`-odd spatial/qubit pseudoscalar `ω`,
the generation/`δ`-sign rides the `K`-even Vandermonde, and the chiral content rides the
`K`-even staggered `ε` — **three distinct recurring imports**. The honest unified picture is
therefore **not** literally a single `Z₂`; it is a **small set of distinct dynamical-structure
imports** —

> `{ the {ε,D}=0 staggered chirality gate (matter carrier),  the CP-odd/coupling sector
>   (gauge θ + flavor δ),  the scalar i,  the scale,  the arrow }`

— unified only by the single **theme**: *Record forces the action **form/structure**, not its
**couplings/gradings***. The companion PRs are being corrected to use this accurate framing.

## What is and is not claimed

- **Is:** the chiral content reduces to the `{ε,D}=0` staggered chirality import (already
  consolidated), which Record cannot supply; that gate is a **distinct** object from the K-odd
  qubit pseudoscalar `ω` and the K-even generation Vandermonde (different K-parity and sector),
  so it does **not** collapse into a single "orientation `Z₂`"; the chiral-vs-vector gauging is
  the un-derived import `ε` is blind to.
- **Is not:** does **not** derive the chiral grading or the chiral gauging (both remain
  imports); does **not** claim chirality is impossible to derive (the staggered/Kawamoto-Smit
  forcing is the live open route); does **not** force `r=1/2`; adds no axiom or fitted value.

## Load-bearing inputs

- [`MINIMAL_AXIOMS_2026-06-05.md`](MINIMAL_AXIOMS_2026-06-05.md) — the `Z³` lattice (staggered
  `ε`), the qubit `Cl(3,0)` (`ω`), and the C₃ generation circulant (Vandermonde); the
  `{ε,D}=0` anticommutation, the K-parities, and the `ε`-blindness of the coupling are reproven
  in the runner.

Companion + context (plain references, not load-bearing deps):
`CARRIER_ATTACHMENT_CONSOLIDATES_TO_RECURRING_CHIRALITY_GATE_SHARPENING_NOTE_2026-06-06`,
`CHIRALITY_RECORD_TYPING_INTERFACE_2026-06-05`,
`I_IDENTITY_AUTOMORPHISM_GATE_SCALAR_I_ONE_OBJECT_REAL_STRUCTURE_INDEPENDENT_NARROW_THEOREM_NOTE_2026-06-08`,
`KOIDE_R_REDUCES_TO_CHIRAL_VS_VECTOR_YUKAWA_BINARY_NARROW_THEOREM_NOTE_2026-06-04`.

## Forbidden-imports check

No PDG / fitted / literature value is consumed. The staggered `{ε,D}=0` anticommutation, the
`K`-parities of `ε`/`ω`/Vandermonde, and the `[ε, T^a]=0` coupling-blindness are reproven in
the runner from the lattice and qubit primitives.
