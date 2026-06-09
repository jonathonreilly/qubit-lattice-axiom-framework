# A Rigorous Analyticity Floor for the SU(3) Bulk-Criticality Premise: Explicit β₀ With Enumerated Constants

**Date:** 2026-06-09
**Claim type:** bounded_theorem (an explicit-constant convergence floor) + a named open window
**Type:** bounded_theorem
**Status authority:** independent audit lane only. This source note does not set
or predict an audit outcome.
**Primary runner:**
[`scripts/frontier_su3_bulk_criticality_rigorous_floor_2026_06_09.py`](../scripts/frontier_su3_bulk_criticality_rigorous_floor_2026_06_09.py)
**Cached runner output:**
[`logs/runner-cache/frontier_su3_bulk_criticality_rigorous_floor_2026_06_09.txt`](../logs/runner-cache/frontier_su3_bulk_criticality_rigorous_floor_2026_06_09.txt)
(SCORECARD: PASS=15, FAIL=0)

> **Not claimed:** a solution of the mass-gap problem, an unconditional `β=6`
> gap, or a sharp convergence radius. **Claimed:** the β=6 reduction's premise
> interval `(0, 6]` is rigorously shrunk to `(β₀, 6]` with an **explicit,
> deliberately conservative** `β₀ = 0.0047`, every constant in the chain either
> enumerated on the actual `Z⁴` plaquette graph or bounded analytically, with
> Weyl-grid quadrature used only as calibration. The cleared fraction — **0.078%** of the interval — is stated
> plainly, together with the named route by which the floor rises.

---

## Role

The β=6 reduction note
(`SU3_BETA6_GAP_BULK_CRITICALITY_REDUCTION_BOUNDED_THEOREM_NOTE_2026-06-09.md`,
plain-text context reference; landed by review-loop from PR #3393) makes the SU(3)
lattice-units gap at `β=6` conditional on one premise:
*no second-order bulk critical point on the 4D SU(3) fundamental-Wilson axis in
`(0, 6]`*. That premise's lower end is provable: wherever the polymer/cluster
expansion converges, the free energy is **analytic in `β`** and truncated
correlations **cluster exponentially**, so no bulk criticality can occur there.
This note computes an explicit floor `β₀` for that convergence and thereby
converts the premise's lower edge from comparator-supported to **proven**.

## The chain (standard steps; explicit, conservative constants)

**(F1) Single-plaquette inputs: analytic bounds plus Weyl-grid calibration.** Write the Wilson plaquette factor
`w(U) = e^{(β/3)\,\mathrm{Re}\,χ_f(U)} = c(β)\,(1 + f(U))` with
`c(β) = ∫ w\,dU` (Haar), so `∫ f\,dU = 0` and every polymer activity obeys
`|z(X)| ≤ η^{|X|}` with `η(β) = \max_U |w/c - 1|`. Since `w/c - 1` is monotone in
`\mathrm{Re}\,χ_f` and `\mathrm{Re}\,χ_f ∈ [-3/2, 3]` for SU(3) (verified on the
class-angle grid; the endpoints are the identity and `Z₃`-center classes),
`η(β) = \max(e^{β}/c - 1,\; 1 - e^{-β/2}/c)`. The load-bearing proof uses
`c(β) ≥ 1` and `c(β) ≤ \exp(9β²/32)` (Jensen plus Hoeffding for
`X=\mathrm{Re}\,χ_f/3∈[-1/2,1]`, `E[X]=0`), giving a rigorous `η_bound(β)`.
The Weyl-grid quadrature is a calibration check only: `η(β)/β → 1` as `β → 0`
(verified to 0.5%).

**(F2) Combinatorial constants, enumerated.** On `Z⁴`, each plaquette shares a
link with exactly `Δ = 20` others — **enumerated** on a periodic `5⁴` block, not
assumed. The number of link-connected plaquette sets of size `n` containing a
fixed plaquette is bounded by `C_{\mathrm{anim}}^{\,n-1}` with the conservative
standard choice `C_{\mathrm{anim}} = e(Δ+1) ≈ 57.1`; the runner verifies the
bound directly at `n = 2` (count 20) and `n = 3` (**exact count 458** vs bound
3259 — a ~7× margin, showing how much slack the generic bound leaves).

**(F3) Kotecký–Preiss criterion.** With `a(X) = |X|`, absolute convergence of
the cluster expansion — hence analyticity in `β` and exponential clustering —
holds whenever
`(Δ+1) \sum_{n≥1} C_{\mathrm{anim}}^{\,n-1} (ηe)^n ≤ 1`, for which the
conservative closed form `η ≤ 1/((Δ+1)\,e\,(1+e)) = 0.004711` suffices (the
geometric-series validity `η e C_{\mathrm{anim}} < 1` is checked: ratio 0.73).

**(F4) The floor.** Bisection on the exact-quadrature `η(β)` gives

```text
    β₀ = 0.00470        (η_bound(β₀) = 0.004711)
```

For all `β ≤ β₀`: the free energy is analytic in `β`, truncated correlations
cluster exponentially with the quantitative polymer-tail bound
`m_{\mathrm{lat}}(β) ≥ \ln(η(β₀)/η(β))` (e.g. `≥ 0.694` at `β₀/2`), and therefore
**no bulk critical point exists in `(0, β₀]`**.

## Net

```text
premise interval:   (0, 6]  →  (β₀, 6]  =  (0.0047, 6]      [PROVEN shrink]
cleared fraction:   0.078%                                    [stated honestly]
```

Combined with the reduction note, the conditional structure of the `β=6` gap now
reads: *no second-order bulk point in `(0.0047, 6]`* ⟹ `m_lat(β=6) > 0` — the
first segment of the premise interval carries an explicit-constant proof rather
than Monte-Carlo support. The floor is **monotone machinery**: every improvement
of the animal/character constants raises `β₀` directly, with no new conceptual
input — the runner's own `n=3` enumeration already shows a ~7× slack in the
generic bound, and closed-surface counting (the character expansion's actual
combinatorics, Münster-class) is the named route. Closing the remaining
`(β₀, 6]` window unconditionally remains Balaban-class RG-constructive work.

## What this note does NOT claim

- **Not** a mass-gap solution, an unconditional `β=6` result, or any
  physical-units/Planck/`Λ_QCD`/spectrum claim (lattice units; pure-gauge SU(3)
  fundamental-Wilson at fixed spacing).
- **Not** a sharp convergence radius: `β₀` is a deliberately conservative
  sufficient bound; the true analyticity domain is expected to be far larger
  (that expectation is not used).
- **No** new axiom, primitive, vocabulary, or class tag; **no** PDG/fitted/MC
  input in the derivation (the floor's constants are enumerated or bounded
  analytically; Weyl-grid quadrature is calibration only).
- It does **not** set or change any audit status.

## Reprove-and-cite ledger

- **Reproven here** (runner): the `\mathrm{Re}\,χ_f ∈ [-3/2,3]` range; analytic
  `c(β)` bounds and `η_bound(β)` with a Weyl-grid small-`β` calibration; `Δ = 20` and the
  `n = 2, 3` animal counts by explicit enumeration on `Z⁴`; the validity of the
  closed-form KP sufficient condition; the bisection `β₀`; the polymer-tail gap
  bound below the floor; the cleared-fraction arithmetic.
- **Cited** (theorem-grade methodology, no numerical input): Kotecký–Preiss
  *CMP* 103 (1986) 491 (cluster-expansion convergence criterion); the standard
  connected-subgraph counting lemma (e.g. Friedli–Velenik, *Statistical Mechanics
  of Lattice Systems*, ch. 5); Osterwalder–Seiler *Ann. Phys.* 110 (1978) 440 and
  Seiler *LNP* 159 (1982) (polymer framework for lattice gauge theories);
  Münster (character-expansion combinatorics — the named improvement route);
  Balaban (the named constructive route for the remaining window).

## Dependencies

- `SU3_BETA6_GAP_BULK_CRITICALITY_REDUCTION_BOUNDED_THEOREM_NOTE_2026-06-09.md`
  (context, plain-text reference; landed by review-loop from PR #3393) — the
  reduction whose premise interval this note shrinks.
- [FIXED_LATTICE_GAUGE_EXISTENCE_STRONG_COUPLING_SCOPE_NOTE_2026-06-09.md](FIXED_LATTICE_GAUGE_EXISTENCE_STRONG_COUPLING_SCOPE_NOTE_2026-06-09.md)
  — the landed fixed-lattice scope this note inherits (lattice units, no
  continuum-limit claim).

**No-promotion statement:** this note does not promote, demote, or set the audit
status of any dependency. The independent audit lane is the only status authority.
