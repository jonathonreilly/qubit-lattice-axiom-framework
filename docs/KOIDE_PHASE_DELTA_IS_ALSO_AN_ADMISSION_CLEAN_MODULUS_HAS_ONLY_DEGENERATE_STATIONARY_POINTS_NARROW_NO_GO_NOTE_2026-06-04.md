# The Koide Phase δ Is Also an Admission on the Clean-Modulus Surface: Only Degenerate Stationary Points (η→δ Residual Left Open)

**Date:** 2026-06-04
**Type:** no_go
**Claim type:** no_go (narrow, computable-side) — the clean determinant-modulus route in the η→δ
lead (#2624) does **not** derive the Koide phase `δ≈2/9`; on this surface `δ`, like the magnitude
`r`, remains an admission. The CP-odd η/θ-vacuum selector that could shift `δ` is **gated** and left
as the residual.
**Claim scope:** for the C3-circulant lepton Yukawa `M = aI + bC + b̄C²` (`b=|b|e^{iδ}`), the
determinant `det M = a³ − 3a|b|² + 2|b|³cos(3δ)` depends on `δ` only through `cos(3δ)`. So the fermion
**modulus** potential `V_mod = Σ log|λ_k| = log|det M|` is **even in δ** and stationary **only** at
`sin(3δ)=0`, i.e. `δ ∈ {0°, 60°, 120°, …}`. At **every** one of those stationary points the
√-mass spectrum is **degenerate** (two equal masses) — unphysical for the charged leptons. The
physical, non-degenerate `δ` (≈2/9 rad, three distinct masses) is **not** a stationary point; the
modulus gradient there is nonzero. Thus the modulus-only variational equation cannot pin the
physical `δ`; its stationary candidates are degenerate. This is parallel to the magnitude `r=1/2`
case (clean modulus → `r=1`), with the important caveat that the CP-odd η/θ residual remains open.
**Status:** review-loop source proposal. This note writes no audit verdict and supplies no direct
effective-status change.
**Runner:** [`scripts/audit_companion_koide_phase_delta_is_also_an_admission_exact.py`](./../scripts/audit_companion_koide_phase_delta_is_also_an_admission_exact.py)

## The attack and its result

The surviving Koide thread (#2624) was: the magnitude `r` comes from the determinant **modulus**
(`→ r=1`), but the **phase** `δ` might be selected by the chirality-graded **η-invariant**. This note
attacks that lead and finds it **fails on the computable side**:

1. `det M(δ) = a³ − 3a|b|² + 2|b|³ cos(3δ)` — a function of `cos(3δ)` only (verified numerically to 1e-12).
2. `d(det M)/dδ = −6|b|³ sin(3δ)` → the modulus is stationary **only** at `δ = k·60°`. It is **even
   in δ** (CP-blind on the selection).
3. At every modulus-stationary `δ` (`0°, 60°, 120°, …`) the √-mass spectrum is **degenerate**
   (e.g. `δ=0°` → `(a+2|b|, a−|b|, a−|b|)`).
4. The physical `δ≈2/9 rad` gives **three distinct** masses and is **not** a modulus stationary point
   (`sin(3·2/9) ≈ 0.62 ≠ 0`).
5. The modulus gradient at `δ=2/9` is nonzero → the modulus-only variational equation does not
   stationarize the physical value.
6. The only candidate to hold `δ` off degeneracy is the **CP-odd** η/θ-vacuum term — which is **odd
   in δ** (it vanishes at the modulus extrema) and is **gated** on the staggered-Dirac mass.

All seven checks pass exactly.

## Net: both Koide parameters are admissions

| Koide parameter | clean dynamics give | empirical | status |
|---|---|---|---|
| magnitude `r = |b|²/a²` | `r = 1` (modulus, #2624) | `r = 1/2` (Q=2/3) | admission |
| phase `δ = arg b` | `δ = 0°/60°` (degenerate) | `δ ≈ 2/9` (distinct masses) | **admission (this note)** |

The clean modulus surface gives the **trivial/degenerate** charged-lepton spectrum (`r=1`,
`δ=0/60°`); on the currently computed surface, **both** the magnitude and the phase that make the
leptons physical and Koide-special remain admissions. This note does not prove that every possible
selector fails: a CP-odd η/θ value-selector remains gated and is not computed here.

## No-Go Discipline Gate (N1-N8)

**N1 — Alternative route enumeration.** The closed claim here is narrow: the clean determinant-modulus
route does not select the physical `δ`. Routes checked or separated:

| route | attempt | status |
|---|---|---|
| determinant modulus | Stationarize `V_mod = log|det M|` over the C3-circulant phase. | ATTEMPTED here; stationary only at `δ=k·60°`, where the spectrum is degenerate. |
| determinant singularities | Let zeros/poles of `det M` act as hidden extrema. | ATTEMPTED here by using `d log|det M| = det'/det`; singular points are not stationary physical mass triples. |
| C3 eigenmode relabeling | Reorder the three circulant eigenvalues to make `2/9` look stationary. | RULED OUT by the symmetric determinant form: relabeling preserves dependence on `cos(3δ)`. |
| fitted mass inversion | Solve for `δ` from charged-lepton masses and declare that a derivation. | RULED OUT BY SCOPE; this note forbids PDG or fitted mass inputs as derivation inputs. |
| Berry/Plancherel/canonical-descent phase routes | Seek an independent phase mechanism that pins `2/9`. | RULED OUT AS WITNESS for this note; prior route attempts are not used as closure here. |
| CP-odd η/θ term | Add the odd selector that can hold `δ` away from modulus extrema. | OPEN RESIDUAL; explicitly not closed by this note. |

**N2 — Wall-independence audit.** Collapsed residual set: `(W_delta)` the CP-odd η/θ value selector is
not computed on the staggered-Dirac mass; `(W_r)` the magnitude `r=1/2` remains separate from the
phase. Closing `W_delta` would not close `W_r`; closing `W_r` would not compute the η/θ phase term.
They are independent if one wants a full charged-lepton mass-ratio derivation. This note only closes
the determinant-modulus route for `δ`.

**N3 — Hidden-wall scan.** Explicit load-bearing premises: C3-circulant lepton Yukawa form, positive
`a` and `|b|`, nonzero determinant away from singular mass triples, and modulus-only stationarity.
Hidden admissions made explicit: the η/θ selector and the empirical `δ≈2/9` value.
Baseline premise nodes are not used as bounded sources here.

**N4 — Residual matching.** The magnitude-modulus correction (#2624) matches only as an analogy:
modulus selects a trivial value (`r=1` there, degenerate `δ` here). Possible chirality/η structure
does not match the value-selector residual unless it computes a concrete non-degenerate stationary
point. Berry/Plancherel/canonical-descent notes are not treated as witnesses that the η residual is
closed.

**N5 — Rhetoric audit.** Broad phrase rejected: "the framework cannot derive `δ`." Narrow phrase used:
"the clean determinant-modulus route does not select the physical `δ`; its stationary points are
degenerate." The note does not claim the CP-odd η/θ term, a future controlled convention, or an
approved new value-selector cannot retire the admission.

**N6 — Partial-closure path scan.** A legitimate partial-closure path exists: explicitly compute the
CP-odd η/θ-vacuum contribution on the staggered-Dirac mass and test whether it pins a non-degenerate
`δ`. A fitted mass inversion or a labeling convention alone would not be a clean derivation. Approved
baseline premises chain-satisfy dependencies only; they are not bounded sources for `δ`.

**N7 — Steelman.** The strongest objection is that the CP-odd η/θ term is exactly the missing
odd-in-`δ` ingredient: once computed, it could add a non-degenerate stationary point and pin `δ≈2/9`
without contradicting the modulus calculation. This is valid, which is why this is a computable-side
no-go, not a universal no-go.

**N8 — Cross-cycle echo.** The closest echo is the magnitude route: clean modulus gave the trivial
value `r=1` while the empirical `r=1/2` remained an admission. This note finds the same shape for the
phase on the modulus surface. Unlike a retired convention wall, the η/θ residual is a real uncomputed
term, so the no-go is narrowed rather than declared universal.

**Gate status:** PASS for the narrowed claim. Failure conditions for a universal no-go are avoided by
leaving the η/θ residual open.

## What is / is not claimed

- Claims: the **modulus** does not select the physical `δ` (physical `δ` is not stationary, while the
  modulus stationary points are degenerate); `δ` remains an admission on the computable side,
  parallel to `r`.
- Does **not** claim the gated η/θ term cannot pin `δ` (it is the open residual), nor that `2/9` is
  definitely wrong (it is the empirical fit; possibly coincidental).
- Conditional on the C3-circulant lepton structure; no PDG values as derivation inputs.

## Trace gate

```yaml
trace_class: lead_closure
target_blocker_text: "the Koide phase delta=2/9 is an admission (radian-period / AC_phi_lambda)"
source_of_blocker_text: audit_ledger
reachability_to_target: closes the modulus route; residual = the gated CP-odd eta/theta term
artifact_role: no_go
next_trace_action: "the residual is gated: compute the CP-odd eta/theta-vacuum contribution on the staggered-Dirac mass and test whether it pins a non-degenerate delta. Magnitude r=1/2 remains a separate admission."
```

## Forbidden imports / reprove-and-cite

- `det M`, the triple-angle identity, the degeneracy at `δ=k·60°`, and the odd/even parity in `δ` are
  reproven from the circulant algebra. The η/δ connection is the cited #2624 lead; `2/9` and its
  coincidence status are comparator literature, not derivation inputs. No PDG values; no fitted parameters.

## Cross-references

- The #2624 frontier correction (magnitude `r=1` from the modulus; possible chiral/η structure would
  need a separate value-selector computation).
