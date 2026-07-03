# Lensing Slope: Centered Finite-Path Surrogate Negative Boundary

**Date:** 2026-04-07; 2026-06-08 negative-boundary narrow.
**Claim type:** no_go
**Status:** negative boundary packet submitted for independent audit; not an audit verdict.

This note no longer claims to explain the detector-centroid `kubo_true`
observable. Its live scope is narrower and negative:

1. The centered finite-path surrogate is not the literal static-mass
   detector-centroid reduction used by the harness.
2. The same surrogate's short-path regime-transition prediction is falsified by
   the `T_phys = 7.5`, `H = 0.25` Lane L++ measurement.
3. A layer-weighted analytical bridge from the literal harness geometry to
   `kubo_true` remains open and is not supplied here.

> **Issue 1 (parallel narrowing, bd14a30):** The "1.5% match" used a
> *centered* finite-path surrogate with `L = 10`. The literal harness
> geometry is NOT centered: the mass is at `x_src ≈ 5`, the beam
> traverses `x ∈ [0, 14.75]`, so the integration is asymmetric. When
> reduced to the actual geometry directly, the analytical surrogate
> gives slope ≈ −1.24 to −1.34 (depending on weighting), not −1.42.
> The "1.5% match" was sensitive to the centering convention.
>
> **Issue 2 (Lane L++ short-path test, this commit):** Even putting
> aside the centering issue, the surrogate makes a clean falsifiable
> regime-transition prediction: at T_phys = 7.5 (L_eff = 5) the slope
> should drop to ≈ −1.73; at T_phys = 45 (L_eff = 30) the slope
> should rise to ≈ −1.08. The Lane L++ short-path measurement at
> T_phys = 7.5 with H=0.25 fine refinement gives slope ≈ −1.44 —
> essentially **identical** to the T_phys=15 measurement of −1.43
> at the same H. The slope is approximately **L-independent** at
> H=0.25 in the tested range, which a ray-deflection formula cannot
> give. The regime-transition prediction is falsified.

The combined picture: the finite-path Fermat formula explains
neither (a) the literal-geometry version of the same observable
nor (b) the slope at a second T_phys value. The "1.5% analytical
match" at T_phys=15 with the centered surrogate was a coincidence
of two narrow choices (centering convention + the specific T value)
that landed on top of the actual measurement.

See `LENSING_LONG_PATH_TEST_NOTE.md`
for the Lane L++ falsifying data and the new "L-independent slope"
finding.

## 2026-06-08 Audit-Targeted Boundary Narrow

The current audit blocker says:

> "The arithmetic comparison and finite-path slope predictions are internally consistent, and the helper source computes the short-path Kubo measurement from the lattice/DAG propagator rather than merely printing the contested value. The chain still does not close as a first-principles explanation because the layer-weighted analytical bridge from the literal static-mass geometry to the detector-centroid kubo_true observable is explicitly missing."

This revision makes that missing bridge part of the negative boundary rather
than an unclosed positive premise. The row's repaired source claim is:

```text
The centered finite-path surrogate is ruled out as a first-principles
literal-harness detector-centroid explanation.
```

The packet still exposes the useful finite arithmetic and the long/short-path
measurement checks. It does not claim a positive explanation of the measured
`-1.4335` slope, and it does not close the separate layer-weighted analytical
bridge.

## No-Go Discipline Gate

**Status:** PASS for the centered finite-path surrogate negative boundary. The
claim is narrow: the centered surrogate is not a first-principles literal-harness
detector-centroid explanation.

- **N1 — Alternative routes.** Centered finite-path surrogate (attempted, not
  literal and short-path prediction falsified); literal full-path static-mass
  reductions (attempted, slopes too shallow); detector-shift proxy (attempted,
  still too shallow); signed adjoint-centroid/Kubo edge bridge (open); long-path
  numerical asymptotic test (open diagnostic, not a closure).
- **N2 — Wall independence.** The centering-convention failure and the
  short-path-regime falsifier are independent witnesses against the centered
  surrogate; either one blocks treating it as a closed literal derivation.
- **N3 — Hidden-wall scan.** The note names the surrogate geometry, literal
  harness geometry, `T_phys` values, and measured slopes explicitly; it does not
  assume a layer-weighted bridge.
- **N4 — Residual matching.** The residual matched is the centered finite-path
  surrogate's claim to explain the detector-centroid observable, not standard
  geometric lensing in another observable.
- **N5 — Rhetoric audit.** Negative language is limited to the centered
  surrogate as a literal detector-centroid explanation. The signed native
  centroid route remains open.
- **N6 — Partial-closure path scan.** The native layer-weighted/signed Kubo
  derivation is the partial-closure path and is not called a new axiom.
- **N7 — Steelman.** The centered formula may remain a useful heuristic because
  finite support effects are real. The note preserves that heuristic while
  rejecting theorem-grade literal derivation.
- **N8 — Cross-cycle echo.** This narrows the earlier lensing lane without
  discarding the later adjoint-centroid multipole route.

## Artifact chain

- [`scripts/lensing_analytical_finite_path.py`](../scripts/lensing_analytical_finite_path.py)
- [`logs/runner-cache/lensing_analytical_finite_path.txt`](../logs/runner-cache/lensing_analytical_finite_path.txt)
- [`logs/2026-04-07-lensing-analytical-finite-path.txt`](../logs/2026-04-07-lensing-analytical-finite-path.txt)
- `docs/LENSING_LONG_PATH_TEST_NOTE.md`
- [`scripts/lensing_long_path_test.py`](../scripts/lensing_long_path_test.py)
- [`logs/runner-cache/lensing_long_path_test.txt`](../logs/runner-cache/lensing_long_path_test.txt)
- [`logs/2026-04-07-lensing-long-path-test.txt`](../logs/2026-04-07-lensing-long-path-test.txt)
- [`scripts/lensing_finite_path_centroid_packet_manifest_2026_06_04.py`](../scripts/lensing_finite_path_centroid_packet_manifest_2026_06_04.py)
- [`logs/runner-cache/lensing_finite_path_centroid_packet_manifest_2026_06_04.txt`](../logs/runner-cache/lensing_finite_path_centroid_packet_manifest_2026_06_04.txt)
- [`outputs/lensing_finite_path_centroid_packet_manifest_2026_06_04.json`](../outputs/lensing_finite_path_centroid_packet_manifest_2026_06_04.json)

## 2026-06-04 Source Packet Re-audit Repair

This repair supplies the restricted-packet materials named by the previous
audit blocker. It does not promote this row or set an audit status;
independent audit owns any ledger/status movement. The 2026-06-08 repair above
narrows the row to the negative boundary supported by these materials.

The packet now exposes both load-bearing computations:

1. The finite-path analytical runner/cache for the centered surrogate,
   literal full-path static-mass reductions, regularized `r+0.1`
   reduction, and detector-shift proxy:
   [`scripts/lensing_analytical_finite_path.py`](../scripts/lensing_analytical_finite_path.py)
   and
   [`logs/runner-cache/lensing_analytical_finite_path.txt`](../logs/runner-cache/lensing_analytical_finite_path.txt).
2. The Lane L++ long/short-path runner/cache for the `T_phys=7.5`
   and `T_phys=45` tests:
   [`scripts/lensing_long_path_test.py`](../scripts/lensing_long_path_test.py)
   and
   [`logs/runner-cache/lensing_long_path_test.txt`](../logs/runner-cache/lensing_long_path_test.txt).

The new manifest runner
[`scripts/lensing_finite_path_centroid_packet_manifest_2026_06_04.py`](../scripts/lensing_finite_path_centroid_packet_manifest_2026_06_04.py)
checks that these source/cache paths are named here, that the cache
headers are SHA-fresh against the current runner sources, and that the
cache stdout contains the detector-centroid comparison facts:

- measured fine-lane slope `-1.4335`
- centered surrogate slope `-1.4188`
- literal regularized full-path slope `-1.2425`
- shift-weighted detector proxy slope `-1.3400`
- short-path `T_phys=7.5`, `H=0.25` measured slope `-1.4356`
- short-path finite-path formula prediction `-1.7336`

The primary analytical runner
[`scripts/lensing_analytical_finite_path.py`](../scripts/lensing_analytical_finite_path.py)
now also imports
[`scripts/lensing_long_path_test.py`](../scripts/lensing_long_path_test.py)
directly and prints a `LONG-PATH COMPANION PACKET` manifest. That makes the
audit helper-graph resolver include the long-path source in the restricted
packet, and it pins the long-path cache to the current source SHA while checking
the `T_phys=7.5` measured/predicted slope snippets named by the audit blocker.

That closes the packet-completeness part of the blocker: the long-path
runner/output and the detector-centroid proxy checks are now exposed in
one restricted packet. The remaining positive-science boundary is unchanged:
there is still no independently audited layer-weighted analytical derivation
from the literal harness geometry to the detector-centroid observable.

## Question

Lane L (H=0.35 only) headlined the sweep as "matches 1/b
gravitational lensing" with slope `−1.03`. Lane L+ (H=0.25 added)
downgraded that to "clean power law with exponent ≈ `−1.43`, not
standard 1/b lensing." The natural question was: **why isn't the
model giving the canonical 1/b law?**

The first attempt at an explanation used a centered finite-path
integral with `L = 10` and got an excellent numerical match. The
problem is that this is a **surrogate geometry**, not the literal
geometry used by the harness.

## Useful surrogate vs literal harness geometry

The propagator action `S = L(1−f)` is literally Fermat's principle
with refractive index `n = 1−f`. We impose `f = s/(r + ε)` where
**`r = √((x − x_src)² + (z − z_src)²)`** — this is the **2D**
distance in (x, z), the y coordinate is ignored in
[`imposed_field`](../scripts/kubo_continuum_limit.py).

If one models the observable as a beam passing a mass on a **centered
interaction segment** of length `L`, then the deflection-angle
integral gives the earlier surrogate formula:

```
α_centered(b, L) = s · L / (b · √((L/2)² + b²))
```

This surrogate has the expected three regimes:

1. **L ≫ b** (asymptotic, long-path): √((L/2)² + b²) ≈ L/2, so
   α ≈ s · L / (b · L/2) = **2s/b** → **canonical 1/b lensing**.
   This is the standard Newton/Einstein weak-field deflection.
2. **L ≪ b** (short-path): √((L/2)² + b²) ≈ b, so
   α ≈ s · L / b² → **1/b² falloff**, much steeper.
3. **L ≈ b** (transition regime): power somewhere between −1 and −2.

## What the harness actually does

The literal lensing sweep geometry is different:

- the mass is **static** at `x_src = round(NL/3) · H ≈ 5`
- the beam propagates over the **full** interval `x ∈ [0, (NL−1)H]`
- at `H = 0.25`, the detector is at `x_det = 14.75`
- the imposed field uses the **regularized** denominator `r + 0.1`
- the reported observable is **detector centroid shift** (`dM` / `kubo_true`), not outgoing angle

That means the earlier "`L_eff = 10` because the source is active for
the last 2/3 of the path" interpretation was incorrect for this lane.
`x_src` is the mass position, not an activation time.

## Comparison of surrogate and literal reductions

On the fine subset `b in {3, 4, 5, 6}`:

| Model | What it computes | slope | R² | `|Δ slope|` vs measured |
| --- | --- | ---: | ---: | ---: |
| **measured H=0.25** | `kubo_true(b)` | **−1.4335** | **0.9984** | — |
| centered `L=10` surrogate | earlier finite-path formula | **−1.4188** | **0.9988** | **0.0147** |
| actual full path, no regularizer | static mass over `x∈[0,14.75]` | −1.2793 | 0.9992 | 0.1543 |
| actual full path, `r+0.1` | same, literal denominator | −1.2425 | 0.9990 | 0.1910 |
| full path + lever-arm weight | crude detector-shift proxy | −1.3400 | 0.9987 | 0.0936 |

Two facts follow immediately:

1. The earlier `L=10` surrogate really does match the fine slope very well.
2. The **literal harness geometry does not reduce to that surrogate directly**.

So the earlier note was right to notice a finite-path-scale effect,
but too strong in calling it an exact first-principles derivation of
the measured observable.

## What still looks right

- A finite-path / finite-support effect is clearly relevant.
- The clean H=0.25 power law is real.
- The asymptotic `1/b` limit is still the natural long-path expectation
  for the surrogate angle model.

But what is **not** established yet is the exact reduction from the
beam/DAG detector-centroid observable to a 1D analytical formula.
The best current literal proxy is the lever-arm-weighted full-path
integral, and it is still noticeably shallower than the measured
`−1.4335`.

## What Would Close A Separate Positive Explanation Lane

There are two clean next moves:

1. **Layer-weighted analytical reduction.**
   Derive the first-order `kubo_true` contribution layer-by-layer from
   the actual free beam, instead of collapsing immediately to a uniform
   1D ray integral.
2. **Long-path numerical test.**
   Increase `T_phys` and check whether the measured slope moves toward
   `−1` as the surrogate model suggests. This is still useful, but it
   should be framed as a test of the heuristic finite-path story, not a
   verification of an already-derived formula.

Those moves are not needed for the negative boundary in this row. They are the
next route if the project wants a positive first-principles explanation of the
observed `kubo_true` slope.

## What this means for the lensing lane

### What survives

1. **Lane L+ still gives a clean gravity-side power law** at
   fine `H`.
2. **A finite-path surrogate can reproduce the slope numerically, but is
   falsified as the literal derivation.**
3. **The exact positive mechanism is not yet derived** from the literal harness
   geometry.

### The honest framing

The Lane L "`1/b` match" headline was wrong. The Lane L+ downgrade to
"clean non-standard power law" was numerically right. The attempted
finite-path rescue then went too far in the opposite direction: it
used a surrogate centered-segment formula that matches the fine slope,
but treated that surrogate as if it were the literal static-mass
harness geometry.

The honest source claim is now:

> "The fine lensing lane retains a clean gravity-side power law
> (`−1.4335`, `R² = 0.9984` on `b ∈ {3..6}` at `H=0.25`). A centered
> finite-path surrogate reproduces that slope closely, but the literal
> static-mass full-path geometry gives a shallower slope (`≈ −1.24` to
> `−1.34` in the tested reductions), and the `T_phys=7.5` measurement
> falsifies the surrogate's short-path prediction. Therefore the centered
> finite-path surrogate is not a closed detector-centroid explanation."

## Frontier map adjustment (revised)

| Row | Lane L+ (downgraded) | Revised read |
| --- | --- | --- |
| Strength against harshest critique | "downgrade — clean power law but non-standard exponent" | **partial recovery** — finite-path effects clearly matter, but the exact reduction is not derived yet |
| Compact underlying principle | "kubo_true(b) is a clean power law with non-standard exponent" | **better heuristic picture, not yet a closed derivation** |
| Experimental prediction | "partial — clean functional form but not matching known weak-field lensing" | **still partial** — long-path test remains useful, but current slope explanation is heuristic |
| Theory compression | "sharpened differently" | **sharpened, but still open** — literal beam-weighted reduction is the next target |

## Honest read

This is not the strong rescue it first looked like.

What is real:

- the fine H=0.25 power law is real
- the simple centered finite-path surrogate really does reproduce the slope
- finite-path / finite-support effects remain a serious heuristic clue

What is not yet real:

- an exact first-principles derivation of the measured `−1.4335` from
  the literal harness geometry
- a clean statement that the current setup is already explained by the
  static full-path 2D `1/r` integral

So this note stays valuable, but as a **diagnostic narrowing**, not as
the final explanation.

## Bottom line

> "The fine lensing lane measures a clean power law
> (`−1.4335`, `R² = 0.9984` on `b ∈ {3..6}` at `H=0.25`). A centered
> finite-path surrogate reproduces that slope almost exactly. But the literal
> static-mass full-path geometry gives a shallower slope (`≈ −1.24` to
> `−1.34` in the tested reductions), and the short-path Lane L++ measurement
> falsifies the surrogate's regime-transition prediction. The centered
> finite-path explanation is therefore a negative boundary. The right next
> positive-science move is a layer-weighted reduction of the actual
> detector-centroid observable."

## Audit Registration

```yaml
claim_id: lensing_finite_path_explanation_note
note_path: docs/LENSING_FINITE_PATH_EXPLANATION_NOTE.md
runner_path: scripts/lensing_analytical_finite_path.py
claim_type: no_go
claim_scope: >
  Negative boundary for the centered finite-path surrogate as a
  first-principles literal-harness detector-centroid explanation. The runner
  compares the measured H=0.25 kubo_true slope, the centered L=10 surrogate,
  literal full-path reductions, and the shift-weighted detector proxy, and it
  includes the long-path companion packet showing the T_phys=7.5 short-path
  prediction mismatch. Excludes any positive layer-weighted analytical bridge
  from literal static-mass geometry to kubo_true and any claim that the
  observed -1.4335 slope is already explained.
intrinsic_status: no_go
remaining_positive_bridge: layer_weighted_detector_centroid_reduction
audit_authority: independent audit lane
```

## Audit dependency repair links

This graph-bookkeeping section records explicit dependency links named by a prior conditional audit so the audit citation graph can track them. It does not promote this note or change the audited claim scope.

- `LENSING_LONG_PATH_TEST_NOTE.md` (downstream consumer; backticked to avoid length-2 cycle — citation graph direction is *downstream → upstream*)
- `lensing_long_path_test_note`
  (see-also cross-reference; backticked to break cycle-0009 in the citation
  graph. The long-path test note explicitly "Falsifies:" the present finite-
  path explanation as its own title-line scope ("Lensing Long-Path Test —
  Falsifies the Finite-Path Explanation"); the load-bearing citation
  direction is *lensing_long_path_test → this_finite_path_explanation*,
  not vice versa. This bookkeeping bullet duplicated the already-backticked
  entry above; left in see-also form for textual parity.)
