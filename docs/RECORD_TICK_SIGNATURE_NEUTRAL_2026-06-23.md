# The Record-Tick is Signature-Neutral: the Lorentzian Sign is a Separate Admission

> **Key terms used in this doc** are indexed A–Z at `docs/KEY_TERMINOLOGY.md`;
> each row points to the canonical source-of-truth doc.

**Date:** 2026-06-23
**Claim type:** bounded_theorem
**Type:** bounded_theorem
**Status authority:** independent audit lane only. This source note does not set
or predict an audit outcome. Any `audit_status` and `effective_status` fields
are pipeline-derived.

**Primary runner:**
[`scripts/record_tick_signature_neutral_2026_06_23.py`](../scripts/record_tick_signature_neutral_2026_06_23.py)
**Cached runner output:**
[`logs/runner-cache/record_tick_signature_neutral_2026_06_23.txt`](../logs/runner-cache/record_tick_signature_neutral_2026_06_23.txt)

## What this is

The emergent-time / chiral-carrier lane needs the Lorentzian signature
`eps = e_4^2 = -1` (the timelike Clifford generator squares to `-1`,
distinguishing `so(3,1)` from `so(4)`). A natural hope is that the record-tick —
emergent time as monotone, irreversible record accumulation — forces it. This
note checks that the record-tick is **signature-neutral** across the finite
algebraic channels below. It localizes where `eps = -1` would enter: the
multiplication-by-`i` of the Wick continuation `tau -> i t`, a separate
register-not-read input/admission if the lane uses Lorentzian signature.

This note does **not** amend, narrow, retire, or re-approve any registered
primitive, and adds no axiom or import. It localizes a missing sign input rather
than introducing that input.

## Runner-Checked Facts (`PASS=10 FAIL=0`, memory-trivial)

What the record-tick natively supplies — and that each lives at `eps = +1`
(Euclidean / `SO(4)`), hence is logically orthogonal to the metric sign:

1. **No on-site `e_4`.** The anticommutant of the Pauli triple in `M_2(C)` has
   dimension **exactly 0** — there is no on-site timelike generator squaring to
   `-1`. The sign is invisible to the one-qubit algebra.
2. **The same `H >= 0` feeds both branches.** From one positive Hermitian
   generator: the Euclidean semigroup `exp(-tau H)` has `|lambda| <= 1` (a
   contraction, `eps = +1`) and the Lorentzian group `exp(-i tau H)` has
   `|lambda| = 1` (unitary, `eps = -1`). Positivity / durability constrains only
   `|spec(T)|`, **never** the sign of `e_4^2`.
3. **Contraction `!=` unitary except at the Wick point.** `exp(-tau H)` is
   strictly non-unitary for `H > 0`, real `tau > 0`; it equals a unitary step
   only at `H = 0` (trivial) or `tau -> i t` (Wick). So the contraction→unitary
   identification requires the `eps = -1` input/admission (the factor `i`).
4. **The arrow coexists with a Euclidean substrate.** The record-norm
   `||T_E^n v||` is strictly monotone (an arrow) on the `eps = +1` heat-kernel.
   Irreversibility fixes **direction** (the already-admitted past hypothesis,
   `theta -> -theta`, available in both `SO(4)` and `SO(3,1)`), **not kind** (the
   metric sign).
5. **On-site `so(3,1)` is available but the sign is an unfixed label.**
   `{J_i = sigma_i/2, K_i = -i sigma_i/2}` closes `so(3,1)`
   (`[K_i, K_j] = -i eps_ijk J_k`, the `(1/2,0)` Weyl boosts), and the same Pauli
   span closes `so(4)` (`+i`). The `eps = e_4^2` sign is the
   anti-Hermitian-(boost)-vs-Hermitian-(rotation) choice, not selected by the
   on-site algebra.

## Consequence

`eps = e_4^2 = -1` remains a **separate, load-bearing binary input/admission**
not supplied by the checked record-tick channels. The record-tick gives an
**arrow** (direction), a **contraction** (the sign-neutral Euclidean heat-kernel),
**positive energy** (durability), and a **causal order** (metric-free) — all
native to a Euclidean `eps = +1` world. The Lorentzian sign is exactly the Wick
`i` (`tau = -i t`), orthogonal to all four. So **"time has an arrow, space does
not" is true but strictly weaker than "time differs from space in metric sign."**
If the lane uses `eps = -1`, that input belongs with the register-not-read import
class, alongside `r = 1/2` and the readout admissions; it is not an
emergent-time corollary of the checked channels.

## Honest boundary

- This is a **negative / localization** result: it does not derive `eps = -1`;
  it shows that the checked record-tick channels do not supply it, and pins where
  the sign enters (the Wick `i` / the contraction-to-unitary continuation).
- The checked cone / causal-order / durability / reflection-positivity channels
  are signature-neutral for this purpose. This note does not rule out every
  possible future route to Lorentzian signature.
- The remaining, strictly **different and harder** open route — not pursued here
  and likely needing owner-approved new framing — is to force a **non-compact
  (boost) symmetry** of the emergent record-causal cone (a non-compact stabilizer
  gives the indefinite form with no Wick fiat). On the bare action this is
  obstructed by the `single_clock` time↔space exchange certificate, so it would
  have to ride on the per-axis `Z_2` boundary datum (antiperiodic-`tau` BC) — and
  whether that datum is **sign-bearing** (vs merely axis-labeling) is the live
  question, currently behind the cited no-go
  [`SINGLE_CLOCK_KMS_APBC_AXIS_SUPPLIER_NO_GO_NOTE_2026-06-16.md`](SINGLE_CLOCK_KMS_APBC_AXIS_SUPPLIER_NO_GO_NOTE_2026-06-16.md).
- No new axioms / imports / comparators; uses only `M_2(C)`, a real-`tau`
  contraction, `H >= 0`, and a poset — all signature-agnostic. No primitive
  touched.

## Reproduce

```
python3 scripts/record_tick_signature_neutral_2026_06_23.py
# expect: TOTAL: PASS=10 FAIL=0   (memory-trivial, single process)
```
