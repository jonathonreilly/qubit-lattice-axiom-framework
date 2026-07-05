# The Parity-Averaged Flux Response Also Has No Uniform Sign: Exact Analytic Derivatives Show N-Alternation With Decay at the Particle-Hole Point — the Screening Sign Lives Off Symmetry (Bounded)

**Date:** 2026-06-12
**Type:** bounded_theorem (ST3 continuation: the named parity-averaged follow-on of the no-uniform-sign note)
**Claim type:** bounded_theorem
**Script:** `scripts/frontier_grand_canonical_flux_response_alternation_2026_06_12.py`
**Cache:** `logs/runner-cache/frontier_grand_canonical_flux_response_alternation_2026_06_12.txt`
**Status:** source proposal; the audit lane grades. Runner `PASS=7 FAIL=0` — **exact
analytic second derivatives** (Hellmann–Feynman + sum-over-states with degenerate-
subspace handling; no finite differencing in any claim), validated against finite
differences where those are resolvable (`3.6×10⁻⁷` relative).

## Two hypotheses died; what survived is the theorem

The no-uniform-sign note
([`MATTER_LOOP_FLUX_RESPONSE_NO_UNIFORM_SIGN_SHELL_NMOD4_RESOLVED_BOUNDED_THEOREM_NOTE_2026-06-11.md`](MATTER_LOOP_FLUX_RESPONSE_NO_UNIFORM_SIGN_SHELL_NMOD4_RESOLVED_BOUNDED_THEOREM_NOTE_2026-06-11.md))
ended with the named follow-on: pose the screening-sign question on the
**parity-averaged** object. The natural candidate —
the grand-canonical potential `Ω(φ,T)` at the particle-hole point (`μ_ch = 0`),
which is filling-free and smooth at `T > 0` — was probed with two successive
hypotheses, both refuted by exact data: (i) a *uniform sign* does not emerge; (ii)
the response does not *cancel exactly* either (max `|Ω″(0)| = 2.1×10⁻⁴`, at
`N = 8, m = 0, T = 1.0` — a double-precision analytic-derivative model datum).
Both were the author's working hypotheses, not landed claims. What the exact
derivatives show:

## The findings (runner `PASS=7`)

**(G1) Strict N-alternation with decay.** At `T = 0.3`, `m = 0.4` the exact
`Ω″(0)` alternates in sign strictly across `N = 8,10,12,14,16`
(`−2.5×10⁻², +8.7×10⁻³, −3.3×10⁻³, +1.2×10⁻³, −4.6×10⁻⁴`) — the `N mod 4`
structure of the linked filling-resolved note **survives the parity averaging**,
with successive magnitude ratios
`2.83, 2.62, 2.70, 2.67` (~`2.7×` decay per `ΔN = 2`).

**(G2) No net sign at the particle-hole point — on the tested grid.** The
alternating, decaying sequence means the matter loop contributes **no uniform
orbital screening sign** at `μ_ch = 0` on the tested sizes (`N ≤ 16`) — the
response's envelope shrinks rather than selecting a direction. No `N → ∞`
asymptotic is claimed. **The natural place a sign could live is off particle-hole
symmetry** (`μ_ch ≠ 0`) — the named next follow-on, an inference target, not a
result.

**(G3) Exactness and controls.** The analytic derivative is validated against
resolvable finite differences; gauge invariance is exact; the `T = 50` response
dies; the `m = 0` point is analytic at `T > 0` (no cusp — finite temperature
regularizes the level crossing). All values are exact-arithmetic-grade, free of the
finite-difference floor that limited the filling-resolved note's smallest entries.

## Scope

Abelian `U(1)` flux, free rings, grand-canonical `μ_ch = 0`, finite `T`; the
alternation-with-decay table **is** the datum. **Not claimed**: the `b₃` coefficient
or any β-function number; non-abelian antiscreening; the gauge self-energy (named
gap); the `μ_ch ≠ 0` behavior (named follow-on); `N → ∞` asymptotics beyond the
tested grid; `d = 3`. The Peskin–Schroeder formula `(X3)` is used nowhere. Standard
math (method only): grand-canonical traces; first/second-order perturbation theory;
degenerate-subspace diagonalization.

No new axiom, primitive, measure, or weight; `r` untouched; discrete throughout.
The audit lane grades.
