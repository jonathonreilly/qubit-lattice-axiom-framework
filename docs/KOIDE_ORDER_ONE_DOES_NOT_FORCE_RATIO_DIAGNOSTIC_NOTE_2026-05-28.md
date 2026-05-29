# NCG Order-One Condition Does Not Force the Koide Ratio (Diagnostic)

**Date:** 2026-05-28
**Type:** bounded_theorem
**Status authority:** independent audit lane only.
**Status:** bounded NEGATIVE diagnostic — the NCG order-one condition, tested on
the Connes–Lott / product-grading spectral triple that a chiral Koide mass
operator would require, does **not** constrain the generation Yukawa ratio
`r = |b|²/a²` and so does **not** supply the `r = 1/2` (Koide `Q = 2/3`)
selector. This is a what-if test; it does **not** adopt the L/R-factor (`e₄`/P2)
import.
**Primary runner:** `scripts/frontier_koide_order_one_does_not_force_ratio.py` (PASS=9 FAIL=0)

## Context

The retained `koide_anticommuting_operator_derivation_theorem` shows charged-lepton
`Q = 2/3 ⟺` the mass operator is **chiral** (anticommutes with the Z₃ grading
`Γ_χ`), equivalently `r = |b|²/a² = 1/2` for the circulant generation Yukawa
`M = aI + bR + cR²`. Whether `r = 1/2` is **forced** has resisted six independent
lenses (kinematic, dynamical, quantum, chiral, records, and the
Connes–Lott/KO-dimension spectral-action route of `KOIDE_U_BAE_NCG_SPECTRAL_TRIPLE`
+ the KO-dim real-structure narrowing — both found the spectral action symmetric
in the three eigenvalues, never selecting `r = 1/2`).

A 2026-05-28 chirality-gate panel flagged **one untested fork**: the NCG
**order-one condition** `[[D, π(a)], π°(b)] = 0` (`π°(b) = J π(b)* J⁻¹`), which the
prior spectral-action probes never imposed. This note tests it.

## Result (runner-verified, two independent ways)

On the triple `H = (gen ℂ³) ⊗ (L/R ℂ²)`, `D = [[0, M],[M†, 0]]`, `M = aI + bR + cR²`:

1. **Circulant generation algebra ⇒ order-one is VACUOUS.** The natural algebra
   for the Z₃ generation symmetry is the circulant `⟨I, R, R²⟩`. Circulant
   matrices commute, so `[M, π(a)] = 0` and the inner commutator
   `[D, π(a)] = 0` **identically** — before `J` or the grading enter. Order-one
   then reads `0 = 0` for every `(a, b, c)`, imposing **no constraint** on `r`.
   (Symbolic, exact.)

2. **Explicit distinct-`r` witnesses.** For `r ∈ {0.05, 0.2, 0.5, 1.0, 2.0, 5.0}`
   the order-one residual is `0` (to machine precision) — a continuum of `r`
   values all satisfy order-zero + order-one. Order-one does not prefer `r = 1/2`.

3. **Full `M₃` algebra ⇒ moduli-free (corroboration).** Even enlarging the
   algebra to all of `M₃(ℂ)` (so the inner commutator is generically nonzero),
   the order-one solution space leaves Yukawa directions free (runner: a
   conservative `free_dim ≥ 1` in the `block_diag(a,a)` representation; the full
   chiral bimodule gives the 17-complex-dimensional family `D(m) = hm + mk`, i.e.
   the standard Cacic 2009 result — Yukawa values are free parameters of an
   order-one Dirac operator).

## Conclusion

The NCG order-one condition is a **bimodule/texture** condition: it constrains
*which* generation-pair entries of the Yukawa may be nonzero, never the *ratio*
of nonzero coefficients. It is therefore one more lens that does **not** force
`r = 1/2`. The order-one sub-route is closed; the charged-lepton chirality/`r`
gate (shared with generation-ID and the signed-gravity Origin obligation)
remains open, awaiting a genuinely new forcing principle — not order-one, not the
spectral action, not the six prior lenses.

A useful precision also surfaced: a circulant `M` at "`r = 1/2`" still commutes
with `R` (it is C₃-equivariant), so the genuine Koide point is the **chiral
non-circulant** operator `{H, Γ_χ} = 0`; "`r = 1/2`" as a bare circulant
coefficient ratio is not by itself the Koide condition. Order-one, being a
C₃-covariant bimodule condition, cannot select that chiral structure.

## Scope / boundary

- This is a **what-if** on the Connes–Lott / product triple, which itself would
  require the framework's `Z³→Z⁴`/`e₄` Wick-rotation (P2) import for the L/R
  factor. The note does **not** adopt that import; it shows that *even granting
  it*, order-one is not the missing selector.
- No new axiom, import, or retained bridge is introduced. Cacic 2009
  (arXiv:0902.2068) is cited as parallel literature for the moduli-freeness of
  order-one Dirac operators, not as a load-bearing retained authority.
- Standard NCG fact (parallel literature): the chirality grading, the L/R factor,
  the three-generation multiplicity, and the Yukawa couplings are all
  **postulated** inputs of the finite spectral triple; no standard NCG
  construction derives `Q = 2/3`.
