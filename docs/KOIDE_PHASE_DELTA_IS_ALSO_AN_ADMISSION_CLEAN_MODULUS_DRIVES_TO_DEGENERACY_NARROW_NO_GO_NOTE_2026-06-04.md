# The Koide Phase δ Is Also an Admission: the Clean Modulus Drives Toward Degenerate Spectra (η→δ Lead Closed on the Computable Side)

**Date:** 2026-06-04
**Type:** no_go
**Claim type:** no_go (narrow, computable-side) — the η→δ lead (#2624) does **not** derive the Koide
phase `δ≈2/9` from the framework's clean dynamics; `δ`, like the magnitude `r`, is an irreducible
admission. The CP-odd η/θ-vacuum selector that could shift `δ` is **gated** (the residual).
**Claim scope:** for the C3-circulant lepton Yukawa `M = aI + bC + b̄C²` (`b=|b|e^{iδ}`), the
determinant `det M = a³ − 3a|b|² + 2|b|³cos(3δ)` depends on `δ` only through `cos(3δ)`. So the fermion
**modulus** potential `V_mod = Σ log|λ_k| = log|det M|` is **even in δ** and stationary **only** at
`sin(3δ)=0`, i.e. `δ ∈ {0°, 60°, 120°, …}`. At **every** one of those stationary points the
√-mass spectrum is **degenerate** (two equal masses) — unphysical for the charged leptons. The
physical, non-degenerate `δ` (≈2/9 rad, three distinct masses) is **not** a stationary point; the
modulus gradient there is nonzero and **drives δ away, toward degeneracy**. So the clean dynamics
prefer degenerate leptons, and the physical `δ` is an irreducible admission — **exactly parallel to
the magnitude `r=1/2`** (clean modulus → `r=1`).
**actual_current_surface_status:** narrow no-go on the computable (modulus) side, 7/7 exact; the CP-odd
η/θ selector is gated. Not retained.
**bare_retained_allowed:** false
**Status:** independent audit required.
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
5. The modulus gradient at `δ=2/9` is nonzero → the clean dynamics **push δ toward the degenerate
   points**, not toward `2/9`.
6. The only candidate to hold `δ` off degeneracy is the **CP-odd** η/θ-vacuum term — which is **odd
   in δ** (it vanishes at the modulus extrema) and is **gated** on the staggered-Dirac mass.

All seven checks pass exactly.

## Net: both Koide parameters are admissions

| Koide parameter | clean dynamics give | empirical | status |
|---|---|---|---|
| magnitude `r = |b|²/a²` | `r = 1` (modulus, #2624) | `r = 1/2` (Q=2/3) | admission |
| phase `δ = arg b` | `δ = 0°/60°` (degenerate) | `δ ≈ 2/9` (distinct masses) | **admission (this note)** |

The framework's clean dynamics give the **trivial/degenerate** charged-lepton spectrum (`r=1`,
`δ=0`); **both** the magnitude and the phase that make the leptons physical and Koide-special are
irreducible admissions. **The framework does not derive the charged-lepton mass ratios.** Chirality
(`ε`) grounds the *structure* (parity violation, the existence of the η-phase — #2685) but selects
*neither* Koide value.

## NO-GO discipline (brief)

- **Routes for selecting δ:** (i) the determinant **modulus** → degenerate `δ=0/60°` [ruled out, this
  note]; (ii) the **CP-odd η/θ-vacuum** term → the only candidate, **odd in δ and GATED** on the
  staggered-Dirac mass [open residual]; (iii) a Berry-phase / Plancherel / canonical-descent route
  [prior framework attempts, not closed]. So this is **not** a universal no-go — it rules out the
  modulus route and locates the residual at the gated η/θ term.
- **Steelman:** the gated η/θ term, once computed, might pin `δ` at a non-degenerate value. Valid —
  hence "computable-side" no-go, not universal. But note even if it pins `δ`, the magnitude `r=1/2`
  stays a separate admission, and the literature flags `2/9` itself as a likely numerical coincidence.
- **Cross-cycle echo:** identical structure to the magnitude (#2624): clean modulus → trivial value;
  the chiral piece is real but doesn't move the selected value.

## What is / is not claimed

- Claims: the **modulus** does not select the physical `δ` (it drives toward degeneracy); `δ` is an
  admission on the computable side, parallel to `r`.
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
  reproven from the circulant primitive. The η/δ connection is the cited #2624 lead; `2/9` and its
  coincidence status are comparator literature, not derivation inputs. No PDG values; no fitted parameters.

## Cross-references

- The #2624 frontier correction (magnitude `r=1` from the modulus; chirality → phase, not magnitude).
- `ONE_CHIRALITY_GRADING_UNDERLIES_WEAK_PARITY_VIOLATION_AND_THE_FLAVOR_PHASE_NARROW_NOTE_2026-06-04.md`
  (#2685) — `ε` grounds the η-phase *structure*; this note shows it does not select the `δ` *value*.
