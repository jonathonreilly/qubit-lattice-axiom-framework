# The Emergent (3,1) Lorentzian Signature from the Record I-Gradient (Ontological Route) — Narrow Theorem

**Date:** 2026-06-06
**Claim type:** bounded_theorem (an ontological assembly of the (3,1) signature, complementary to the retained Sylvester/DM topological route)
**Status:** unaudited candidate. Graph-visible only so the independent audit lane can decide.
**Primary runner:** [`scripts/lorentzian_signature_from_record_i_gradient_runner.py`](../scripts/lorentzian_signature_from_record_i_gradient_runner.py)
**Cached output:** [`logs/runner-cache/lorentzian_signature_from_record_i_gradient_runner.txt`](../logs/runner-cache/lorentzian_signature_from_record_i_gradient_runner.txt)

## Audit context

The staggered-Dirac realization (on which the flavor sector is conditional) admits a
**signature/time** carrier: a (3,1) Lorentzian spacetime with the right causal structure.
Its **time-direction** half is derived separately (the record-count `I`-gradient is the unique
emergent time axis). This note discharges the **signature** half by an **ontological** assembly —
the (3,1) split read directly off the record `I`-gradient — **independent** of the retained
**Sylvester/DM topological** route
[`dm_abcc_signature_forcing_theorem_note_2026-04-19`](DM_ABCC_SIGNATURE_FORCING_THEOREM_NOTE_2026-04-19.md)
(`retained_bounded`). Two independent routes converging on the same (3,1) split is the content.

## Safe statement

**Theorem (ontological signature assembly).** The emergent metric structure carries a **(1,3)
Lorentzian signature**, assembled from three structural facts:

1. **Three reversible spatial axes (the Z³ group).** The `LATTICE` translations `T_x, T_y, T_z`
   are a **reversible group**: unit-modulus, unitary, invertible (`max||eig|−1| ≈ 10⁻¹⁶`). Space is
   the direction one can traverse **both ways**.
2. **One monotone time axis (the record monoid).** The `RECORD` count `I` is **monotone** (a monoid
   with **no inverse** — one cannot un-register): it is the **unique** axis with `dI ≠ 0`, and its
   level sets are the **codim-1 constant-`I` spatial slices** (the emergent foliation). Time is the
   direction one can traverse **only one way**. So the dimension split is **1 (`dI ≠ 0`) + 3
   (`dI = 0`)**: the timelike axis is the `I`-gradient **normal**; the three spacelike axes are the
   slice **tangents**.
3. **A finite Lieb-Robinson cone.** The reconstructed dispersion
   `E(p) = arcsinh √(m² + Σ_μ sin² p_μ)` is real-analytic (`m > 0`), so the group velocity
   `v_LR = max|∇E|` is **finite** (`= 1/√2` at `m = 0.3`) and correlations decay outside the cone
   (rate `arcsinh(m) > 0`). This is the **light cone**: timelike inside, spacelike outside.

Together: **1 monotone timelike axis + 3 reversible spacelike axes + a finite causal cone = a (1,3)
Lorentzian signature.** This **agrees** with the retained Sylvester/DM topological route (its two
components `(1,0,2)`/`(2,0,1)` are the same 1-vs-3 split up to the overall sign convention).

**The physical content is the 1-vs-3 split and the causal cone**; the overall metric **sign** (which
triple is `+`) is convention — exactly the Sylvester two-component ambiguity.

## What this discharges

- The **signature** half of the staggered-Dirac **signature/time** carrier admission now has **two
  independent derivations**: the **topological** Sylvester/DM route (`retained_bounded`) and this
  **ontological** route (the (3,1) split read off the record `I`-gradient). The **time-direction**
  half is the separately-derived `I`-axis. So "why a (3,1) Lorentzian carrier" is grounded in the
  record ontology, not admitted.
- It **explains** the signature rather than only forcing it: *time is timelike because it is the
  monotone record axis; space is spacelike because Z³ is a reversible group; the cone is the
  Lieb-Robinson bound.* The metric's defining asymmetry (one direction unlike the other three) **is**
  the records' monotone-vs-reversible asymmetry.

## Boundary (honest)

- **A split + cone, not the metric tensor.** It delivers the (1,3) signature (the 1-vs-3 split and
  the Lorentzian causal cone), not a derivation of the full metric components or the overall sign
  (which is convention, matching Sylvester's two components).
- **Complementary, not a replacement.** The Sylvester/DM route remains the topological forcing; this
  is an independent ontological assembly that agrees with it.
- The monotone/reversible inputs are the emergent-time foliation and the Z³ group; the cone is the
  analytic-dispersion Lieb-Robinson bound — all reproduced self-contained in the runner.

## Forbidden imports check

No new axiom. A_min (LATTICE Z³ group; RECORD monotone `I`) + the reconstructed free dispersion
(reproduced in the runner). The Sylvester/DM comparison is to an existing `retained_bounded` note.
Exact finite-dimensional. No literature comparator imported (the Lieb-Robinson / Paley-Wiener facts
are reproduced numerically, not cited as authority).

## Runner check breakdown

Class A: (1) the 3 Z³ translations are reversible (unit-modulus, unitary, invertible); (2) the (3,1)
split = 1 monotone `dI≠0` axis + 3 reversible `dI=0` axes; (3) finite LR cone (`v_LR<∞`, decay rate
`>0`); (4) the (1,3) assembly agrees with the retained Sylvester/DM split + is Lorentzian (1 timelike
axis inside the finite cone). Expected `runner_check_breakdown = {A: 4, B: 0, C: 0, D: 0,
total_pass: 4}`.

## Honest auditor read

The three lattice translations are a reversible unitary group (`|eig|=1` to machine precision), the
record count is a strictly monotone non-invertible monoid whose level sets are the codim-1 spatial
slices, and the analytic free dispersion has finite group velocity with a positive spatial decay rate
— so the emergent structure has exactly one timelike (monotone, in-cone) axis and three spacelike
(reversible) axes: a (1,3) Lorentzian signature. This agrees with the retained Sylvester/DM
topological signature class up to the overall sign convention (its two components), giving a second,
ontological derivation of the staggered-Dirac signature carrier. The note is honest that it delivers
the 1-vs-3 split and causal cone, not the full metric tensor or the convention-fixed sign. Effective
status remains `unaudited`.

## Runner

```bash
PYTHONPATH=scripts python3 scripts/lorentzian_signature_from_record_i_gradient_runner.py
```
