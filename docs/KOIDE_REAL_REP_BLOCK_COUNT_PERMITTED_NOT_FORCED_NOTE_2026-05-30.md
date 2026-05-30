# Koide Real-Rep Block-Count Route: Permitted-Not-Forced

**Date:** 2026-05-30
**Claim type:** bounded_theorem / route-diagnostic (negative)
**Status:** route diagnostic. Approves no axiom and no import; sets no audit
verdict. The audit lane sets status.
**Primary runner:**
`scripts/frontier_koide_real_rep_block_count_permitted_not_forced_2026_05_30.py`
with cache
`logs/runner-cache/frontier_koide_real_rep_block_count_permitted_not_forced_2026_05_30.txt`.

## Question

The charged-lepton Koide value reduces (retained
`koide_circulant_q_two_thirds_algebraic`, pure algebra) to one weighting of the
two `C_3` isotypes of the generation operator space `span{I, J-I}` (`I` =
trivial/singlet; `J-I` = doublet):

- BLOCK-COUNT `(1,1)` (each isotype-block weighted once) gives `3a^2 = 6|b|^2`,
  `r=|b|^2/a^2 = 1/2`, `Q = 2/3`.
- DIMENSION / Plancherel / trace `(1,2)` (weight by irrep dimension; this is what
  the Hilbert-Schmidt trace gives, `Tr(P_singlet)=1`, `Tr(P_doublet)=2`) gives
  `r=1`, `Q = 1`.

Two retained no-gos (`koide_frobenius_isotype_split_uniqueness`,
`action_normalization`) decline to rank these. The remaining structurally
motivated route to force `(1,1)` is the **real representation structure**: over
`R`, `C_3 = (trivial 1-dim) (+) (2-dim rotation)`, and a CPT / charge-conjugation
antilinear involution fuses the conjugate doublet characters `{w, wbar}` into the
single real-rotation block — which, with a `det_R` (signed / Brannen) readout,
*looks* like it should count the doublet once.

Does the **full** retained real structure (CPT antilinear `Theta` + signed/`det_R`
readout + real-rep `C_3` decomposition + reality of `D`) FORCE `(1,1)` — i.e.
make the `(1,2)` dimension weighting incompatible/forbidden?

## Result

No. The route is **permitted-not-forced**: `(1,2)` survives every retained
constraint. This is shown by an explicit witness plus the failure of each
candidate forcing mechanism, not by preference. The earlier linear `K=CPT`
test (`koide_z3_equivariant_anticommuting_no_go` lane) already found per-block
weighting permitted-not-forced; the fuller real structure does not change that.

Five computations (all reproduced by the runner):

1. **`C_3`-rotation invariance.** Solving `R^T G R = G` for the `2pi/3` rotation
   `R` on the real doublet plane `{B1 = C+C^2, B2 = i(C-C^2)}` forces the
   admissible weighting-Gram to `diag(g00, g11, g11)` — exactly the
   `koide_frobenius_isotype_split_uniqueness` 2-parameter cone, with the
   singlet:doublet ratio `g00:g11` FREE.

2. **Antilinear `Theta` (the new test beyond the prior linear commutator).** The
   CPT antilinear involution acts on the real coordinates as
   `Theta = diag(1, 1, -1)`, a `det = -1` reflection *within* the doublet plane.
   Imposed in full reality form — isometry `Theta^T G Theta = G` AND
   `G`-self-adjointness `(G Theta) = (G Theta)^T` — both residuals are
   identically zero on the entire cone. `Theta` imposes ZERO additional
   constraint: a reflection within a 2-dim block neither merges its two
   dimensions to one slot nor down-weights it.

3. **Hermitian doublet eigenvalues are two independent reals.** Retained
   Hermiticity (`H = iD`, `cpt_exact_real_anti_hermitian_d`) makes the two
   doublet eigenvalues `lam = a - b_re -/+ sqrt(3) b_im` — two INDEPENDENT real
   numbers, not a complex-conjugate `{e^{i phi}, e^{-i phi}}` pair. There is no
   rotation block and nothing for `det_R` to fuse; the fusion that motivated the
   route is inapplicable to the retained operator class. (A generic NON-Hermitian
   real circulant does give a conjugate pair — but Hermiticity removes exactly
   that pair.)

4. **The signed / Brannen readout is `(1,2)`-compatible.** `Q = (sum lam^2)/(sum
   lam)^2 = (3a^2 + 6|b|^2)/(9a^2) = (1+2r)/3`. The numerator counts each of the
   three eigenvalues once (dimension/`(1,2)` counting at the eigenvalue level);
   the denominator `sum lam = 3a` is a SUM, never a determinant/product. `Q`
   reaches `2/3` only at the externally supplied `r=1/2`, and equals `1` exactly
   at `r=1` with valid all-real Hermitian spectra. So the signed readout
   PRESUPPOSES `r=1/2`; it does not source `(1,1)`.

5. **The `det_R` adversary inverts; and a witness realizes `(1,2)`.** On the
   unreduced `3x3` real carrier, `det_R(alpha P_singlet + beta P_doublet) =
   alpha * beta^2` — a genuine real determinant carrying the `(1,2)` weighting
   (`beta^2` = the real rank-2 of the doublet projector). Both `(1,1) =
   alpha*beta` (the 2-slot-reduced determinant) and `(1,2) = alpha*beta^2` (the
   unreduced determinant) are real determinants; they differ only by whether the
   doublet is reduced to one slot before `det_R`. WITNESS: the Hilbert-Schmidt
   Gram `diag(3, 6, 6)` is retained, real, positive-definite, `C_3`-invariant
   AND `Theta`-invariant — it manifestly IS the `(1,2)` weighting and satisfies
   every retained constraint.

## The irreducible pin (named)

The `(1,1)`-vs-`(1,2)` choice is exactly: **is the doublet's real dimension 2
reduced to a single slot before the `det_R` / Koide readout?** That reduction is
the **continuous `SO(2)/U(1)_b` angular quotient on the doublet frame** (the
`B1`-`B2` rotation / the `arg(b)` = Brannen `delta` phase direction). It is not a
real-structure / CPT / signed-readout question — those leave it free. Forcing
`(1,1)` would require a retained operator acting as the complex structure `J`
(`det = +1`, `J^2 = -Id`) that performs this reduction, equivalently a retained
continuous `U(1)_b` symmetry whose quotient is the `SO(2)` collapse. Every
retained antilinear map (`K=CPT`, `T_alg`) is a `det=-1` reflection
(`b_im -> -b_im`); Hermitian conjugation is the identity on Hermitian circulants;
no product of discrete reflections generates the continuous `SO(2)`. The objects
that could supply the collapse are unaudited; the retained note examining the
angular kernel directly is a no-go (`angular_kernel_underdetermination`: the
weight `w(theta)` is not uniquely determined), and the `SO(2)` quotient is
carried on `koide_mru_weight_class_obstruction` as a definitional
(`audited_renaming`) step, not a derivation.

## Boundary

This closes the real-rep structure as a *forcing* route for `(1,1)`; it does not
close the broader search. The Koide-value pin is now localized to a single
continuous object — the `SO(2)/U(1)_b` doublet-frame quotient. The forward
handle (a distinct program, recorded as a review trigger, not claimed here):
whether `U(1)_b` is a derivable continuous symmetry of `A1+A2`, or whether the
`Q`-readout functional factorizes through the `SO(2)` quotient without `U(1)_b`
being an algebra symmetry. Per the no-imports policy, promoting the
`U(1)_b/SO(2)` quotient as background requires explicit user approval. (Note the
continuous `U(1)_b` rephasing `C -> e^{i alpha} C` is incompatible with the
retained order relation `C^3 = I`, which quantizes `alpha` to the discrete
`C_3`; so `U(1)_b` cannot be supplied as an algebra symmetry, leaving the
readout-functional-factorization question as the open handle.)

## Relation to Koide

The retained Koide surfaces continue to locate the observed value at the `C_3`
isotype split. This note adds that the real-representation structure — the last
structurally motivated route to force the equal-block weighting — does not force
it: the dimension weighting `(1,2)` is fully consistent with the retained real
structure. The value pin is the continuous `SO(2)/U(1)_b` doublet-frame quotient.
