# VERDICT: CONFIRMED WITH CORRECTIONS

The worker has proved a genuine **C-FAIL within the stated regular, local,
single-band scalar ansatz**.  The proof is the global-charge/Taylor-at-zero
obstruction, not the finite-rank numerics.  It does **not** prove the lane-level
FAIL: the fixed lane rule additionally requires a class that free matter cannot
avoid, whereas neither the axioms nor this packet forces one-band matter and
both multi-band/network and non-local routes remain outside the theorem
(`TESTS.md:1146-1151`, `MINIMAL_AXIOMS_2026-06-29.md:114-130`).

## 1. Lemma and global-charge sector

**Confirmed, with the regularity/domain assumptions made explicit.**  At the
flat gravity point, the matter-degree-two part of the order-λ⁰ brackets is
exactly the flat matter bracket plus the derivative of the order-λ correction
with respect to the gravity variable shifted by the leading gravity constraint:

- in `{D[ξ],H[N]}`, these are `T00^(1)[h=G^Tξ]` and
  `P^(1)[E=S^T N]`;
- in `{D[ξ],D[η]}`, only the two `h=G^T(smearing)` terms survive.

This is the bookkeeping stated at `C3_report.md:25-33`.  A regular structure
function depending on `h`, `E`, or matter cannot add a pure matter bilinear on
this flat submanifold: the gravity constraints have no background constant,
while the matter constraints already start at degree two.  Only the
field-independent Taylor coefficient can multiply `T00` or `P` at this degree.
Singular ratios/inverse fields would evade that count, but they are outside the
polynomial/regular ansatz and would not define the assumed algebra at the flat
point (`C3_report.md:145-151`).

The 09-14 stencil identities are exact.  From the displayed `G` row,
`G^Tξ=0` for a constant edge shift, and for
`ξ_j=A_jk(x_k+δ_jk/2)` its diagonal component is `-A_jj=0` and its
off-diagonal component is `-(A_ij+A_ji)=0`.  From the displayed `S` row, every
component of `S^T N` is a pure or mixed second difference and annihilates an
affine lapse (`LOCAL_FINITE_CLOCK_TENSOR_CONSTRAINTS_CUBIC_DISPERSION_AND_LINEAR_GRAVITY_BOUNDARIES_BOUNDED_THEOREM_NOTE_2026-09-14.md:95-102`).
The independent direct-adjoint check is at `C3_referee_independent.py:121-178`
and returns four exact zeros (`C3_referee_independent.out:1-5`).

The global sector is necessary.  On the infinite lattice one may use compactly
supported fields and cutoffs that agree with the affine smearing on the whole
interaction neighbourhood.  Equivalently, for a local/analytic closure
identity on periodic smearings, differentiating the trigonometric-polynomial
identity at smearing momentum zero is legitimate.  The continuum brackets
`{D[ξ],H[N]}=H[ξ·∇N]` and `{D[ξ],D[η]}=D[[ξ,η]]` then give the
boost and rotation subalgebra.  Thus failure of this subalgebra is sufficient
to rule out the full HDA within the same regular local ansatz.  This is not an
appeal to continuous rotations as a microscopic lattice symmetry; it is a
necessary Taylor coefficient of the proposed local HDA identity.

## 2. Assumptions, structure functions, improvements and `K`

**The assumptions are sufficient, but the headline at `C3_report.md:9` must be
read with A1-A5 and single-band scope, not as an unrestricted statement.**

- Field-dependent structure functions do not help at the selected flat,
  matter-bilinear coefficient for the degree-counting reason above.  C-number
  kernels may be arbitrary functions of the *smearing* momentum, but their
  Taylor coefficients at zero are still constants with respect to the internal
  matter momentum.  A matter-mode-dependent coefficient would be a new
  operator/field-dependent structure, not an ordinary structure function in
  this ansatz.
- Higher powers of `h` or `E` vanish at the flat point after one gravity
  derivative; the linear terms are killed by `G^Tξ=0` or `S^T N=0`.  A
  gravity-independent order-λ matter correction enters only at higher order
  in the λ expansion and cannot repair this order-λ⁰ coefficient.  The proof
  requires enough symbol regularity for the indicated Taylor coefficient
  (finite range is more than enough; `C^2` or an equivalent distributional
  formulation should replace the loose “summable first moment” wording at
  `C3_report.md:148`).
- A local energy-density improvement `T00 -> T00 + div B` preserves `H` and
  changes `K_b=Σx_b T00` by a translation-invariant total `-ΣB_b`.  For a
  real one-band quadratic scalar, `P_tot` phase-rotates the `k,-k` pair with an
  odd symbol, so every translation-invariant quadratic total commutes with
  `P_tot`; `{K_b,P_c}` is unchanged.  A momentum-density divergence/curl
  improvement leaves `P_tot` unchanged and alters `L_ab` only by an analogous
  translation-invariant internal term, again commuting with `P_tot`.  This is
  also why the L1 referee correctly cautioned that a curl improvement is not
  automatically a new complete symmetric stress (`RN_L1_referee.md:3`).
- An independently chosen `K` can evade only by ceasing to be `H[N=x_b]`.
  Within an HDA representation, `K` is the first moment of the scalar
  constraint; its allowed freedom is precisely the density-improvement freedom
  just discussed.  Choosing the exact quasimomentum `k` instead of the L1
  current `sin k` is the non-local SLAC escape, not a local improvement.

The seagull remains valid but irrelevant to this obstruction.  It repairs the
symmetric uniform-strain response (`RN_L1_referee.md:11-24`); it cannot change
the constant-shift/linear-lapse or antisymmetric-rotation brackets where the
gravity-dependent corrections vanish.

## 3. Boost and rotation theorems

**Both proofs are correct in their stated domain.**  Let
`u(k)=ω(k)^2/2` and `f=∇u`.  The total L1 current generates the
factorwise phase flow with symbol `f`.  The energy-type part of
`{K_b,P_c}` has coefficient `∂_b f_c=Hess(u)_bc`.  At the flat global
coefficient a deformed regular structure function may give a constant matrix
times `H`; a `P_j` term has the independent phase/mixed quadratic form and
cannot cancel the `ππ` coefficient.  Hence closure requires
`Hess(u)=constant`, not merely proportional to the identity.  Periodicity makes
that constant zero and then makes `∇u` and `u` constant.  This argument works
already in one dimension.  The remaining `u=constant` case has `P_tot=0` and
zero boost coefficient: it is the dispersionless Carroll contraction, not the
GR/Poincaré algebra (`C3_report.md:70-75`).

For rotations, small-`k` matching with `M=Hess(u)(0)>0` fixes the constant
structure coefficients and gives, for `f!=0`,

`f_a(H_bc-M_bc)-f_b(H_ac-M_ac)=0`.

Thus every column of `H-M` is parallel to `f`; symmetry gives
`H=M+μ f f^T`.  At a maximum of a nonconstant periodic `u`, take regular
points approaching the maximum and unit vectors perpendicular to `f`.  In
dimension `d>=2`, their quadratic Hessian value is the strictly positive
`v^T M v`, contradicting the negative-semidefinite Hessian at the limiting
maximum.  Analyticity guarantees regular points approach a maximum unless `u`
is constant.  The theorem requires `M>0`; it is not a theorem for a degenerate
or non-propagating band (`C3_report.md:76-79`).

## 4. Numerics and independent checks

**Reproduced, apart from one definite endpoint error and two presentation
qualifications.**

- Rerunning both worker scripts reproduces the stored outputs exactly:
  the dyadic real-space residuals are `0.0`, the sampled Fourier systems have
  `rank[A|b]=rank(A)+1` through `r=16`, and the continuum systems close at
  roughly `1e-14` (`c3_hblind_sector_exact.out:1-24`,
  `c3_fourier_system_and_dispersions.out:1-13`).
- A separate implementation using exact `Fraction` arithmetic reproduces zero
  for translation invariance, `{K,H}+P`, the boost closed form, the defect
  formula, and the rotation closed form
  (`C3_referee_independent.py:70-118`, `C3_referee_independent.out:6-11`).
  The worker script's dyadic-exactness explanation is sound for its field
  bounds, although its docstring says it asserts scaled integrality and the
  code contains no such assertion (`c3_hblind_sector_exact.py:15-17`).
- The decisive `p=0` certificate is exact and independent of `r`.  In the
  `ππ` component, the first `p` derivative of the lattice left side is
  `-i cos(q)/2`; the completion gate `1-cos(p)` and its first derivative vanish,
  the `P` columns have no `ππ` part, and the `H` column is the constant
  `1/2`.  At `q=0,π/2`, exact ranks are `1` and `2`; the continuum vector is
  constant and both ranks are `1` (`C3_referee_independent.py:181-193`,
  `C3_referee_independent.out:12-15`).  The sampled SVD rank test is therefore
  corroboration, not the proof for all `r`.
- The “IR residual” printed by the worker is the residual on IR rows **using
  the fit obtained from all rows**; `ir_only` is never used
  (`c3_fourier_system_and_dispersions.py:50-53,92-105`).  It should not be
  described as an independently minimized IR-only residual.  The exact Taylor
  certificate supplies the missing rigorous IR statement.
- The zone-average and IR powers are correct.  Exact differentiation gives
  `<u''-1>=-1` and leading anomalies
  `-k^2/2,-k^4/6,-k^6/20,-k^8/70,-k^10/252`
  (`C3_referee_independent.out:16-21`).
- The four random range-three cubic dispersions also rerun as reported: their
  grid-averaged Hessians vanish to roundoff and the best-constant relative
  non-constancy is `1.000` (`c3_fourier_system_and_dispersions.out:25-29`).
- **Correction:** the reported endpoint values `A(π)=-1.5,...,-2.532` are
  artifacts of applying `np.gradient` twice at an array endpoint
  (`c3_fourier_system_and_dispersions.py:133-142`).  The exact values for
  `r_m=1,...,5` are
  `-2,-8/3,-16/5,-128/35,-256/63`.  This strengthens rather than weakens the
  UV-anomaly statement, but `C3_report.md:82` is numerically wrong.

## 5. Interpretation and literature

**Central difference:** confirmed.  Directly from the L1 density,
`{phi,P_tot,c}=D_c phi` and `{pi,P_tot,c}=D_c pi`, with
`D_c=(T_c-T_c^{-1})/2` (`c3_hblind_sector_exact.py:50-69`).  A Hamiltonian
bracket is a derivation, so it applies `D_c` to each factor.  This is not the
finite difference of the composite product and is not the generator with
sawtooth symbol `k_c` of exact continuous translations.

**Kato-Sakamoto-So:** the link is correct as a structural interpretation, not
as a literal derivation of C3 from their theorem.  Their theorem excludes a
translation-invariant, local lattice difference/product pair satisfying
Leibniz and names infinite flavours or a matrix formulation as escapes
([Kato-Sakamoto-So, arXiv:0803.3121](https://arxiv.org/abs/0803.3121)).  C3 is
the first-moment manifestation for the fixed pointwise product and fixed L1
current; it additionally uses the HDA/global-charge identification.  The
report should therefore say “a moment-form instance/analogue,” not that KSS by
itself proves the C3 theorem (`C3_report.md:86-92`).

**Discrete-gravity prior art:** it supports plausibility and interpretation,
not the proof.  Bahr-Dittrich find exact symmetry absent for curved Regge
solutions and pseudo-constraints in the canonical theory
([arXiv:0905.1670](https://arxiv.org/abs/0905.1670)); perfect actions can recover
continuum dynamics and symmetry in examples
([arXiv:0907.4323](https://arxiv.org/abs/0907.4323)).  Dittrich-Höhn derive
local first-class constraints for linearized flat Regge calculus and
pseudo-constraints at quadratic order
([arXiv:0912.1817](https://arxiv.org/abs/0912.1817)).  These are analogies to
the L1/C3 order pattern, not results about this matter bracket.  Loll proves
closure of certain discretized spatial-diffeomorphism commutators in the
small-spacing limit
([arXiv:gr-qc/9708025](https://arxiv.org/abs/gr-qc/9708025)); that does not prove
the stronger phrase “anomaly-free only in the continuum,” does not cover the
full HDA, and does not establish C3 at finite spacing.  `C3_report.md:108-110`
must be narrowed accordingly.

**Non-locality:** the gravity-side singularity is a correct necessary scaling
inside the worker's factorization: the uncancelled Taylor coefficient is
`O(p)`, while `S^T N` supplies `O(p^2)`, so its coefficient must behave as
`1/p`; in three dimensions a representative is `∂Δ^{-1}`, with a
`1/|x|^2` tail.  It is not a universal theorem of *minimal* non-locality,
because non-local structure functions, altered generators, or extra fields
change the factorization.  On the matter side, the SLAC first derivative has a
`1/|x|` tail, while the scalar `k^2` Laplacian/dispersion kernel has a
`1/|x|^2` tail.  Infinite bands/matrix variables are possible escape classes,
not proved sufficient completions here.  Thus `C3_report.md:131-134` is a
well-motivated route list, not a uniqueness/minimality theorem.

## 6. Multi-band scope

The finite/multi-band failure is plausible but unproved.  If the conserved
charges are band-diagonal on isolated analytic bands, the scalar Hessian
argument applies band by band and periodicity remains obstructive.  But
interband charge matrices, degeneracies/crossings, Berry connections and
auxiliary constraints alter both `K` and the bracket; the scalar proof does not
exclude them.  Infinite-band/matrix constructions are specifically outside the
KSS hypothesis.  The worker correctly labels this only “SUGGESTED” at
`C3_report.md:153-156`.

The framework axioms do not force a Hamiltonian, transfer operator, scalar
carrier, or kinetic branch (`MINIMAL_AXIOMS_2026-06-29.md:114-130`).  A
nearest-neighbour law can propagate influence through repeated network steps,
and an effective description can have multiple or indefinitely many bands.
Therefore the one-band scalar class is not shown to be a class “that free
matter cannot avoid.”

## 7. Fixed-reading verdict and no-go discipline

The fixed C3 rule says C-FAIL exactly when impossibility is proved within the
ansatz (`TESTS.md:1141-1144`).  That condition is met after narrowing the claim
to: fixed 09-14 leading generators; fixed L1 one-band scalar `H,T00,P` up to
local improvements; regular structure functions; and local/analytic
gravity-dependent corrections polynomial in `h,E` and at least quadratic in
matter.  The exact zero-momentum Taylor coefficient proves that no such
completion closes the GR global-charge sector.  Hence **C3 = C-FAIL**.

The no-go stress test has a split result.  For the narrow theorem, the attack
routes—`h/E` completions, field-dependent regular structure functions,
improvements/redefinitions of `K`, deformed constant structure coefficients,
and the Carroll limit—are explicitly closed.  For a broader claim, non-local
gravity kernels, SLAC matter, finite/multi-band interband constructions,
infinite-band/matrix constructions, and abandoning the GR algebra are live
escapes.  The cited KSS/Regge/Loll results attack related but non-identical
residuals and cannot be counted as witnesses proving C3.  The earlier unitary
seagull is a structurally similar repaired wall, but it affects only symmetric
strain and leaves this h-blind sector untouched.  Thus the no-go gate passes
only for the narrow ansatz and fails for any “all free matter” or
“unavoidable class” extrapolation.

Explicit N1-N8 record:

- **N1:** six distinct routes were assessed: (1) local `h/E` completion
  (`ATTEMPTED`, annihilated by the adjoint stencils); (2) regular
  field-dependent structure functions (`ATTEMPTED`, excluded at the selected
  field degree); (3) local density improvements or an improved `K/L`
  (`ATTEMPTED`, their first moments differ by totals commuting with `P_tot`);
  (4) constant deformations/Carroll contraction (`ATTEMPTED`, constant-Hessian
  theorem, with only the non-GR degenerate case); (5) non-local gravity or SLAC
  matter (`ATTEMPTED AS STEELMAN`, a real escape outside locality); and (6)
  multi/infinite-band networks (`ATTEMPTED AS STEELMAN`, outside the scalar
  theorem and still open).
- **N2:** these are not six independent impossibility walls.  The proved wall
  is one conjunction defining the theorem's domain: fixed leading generators,
  one band, regularity and locality.  Dropping locality or one-bandness exits
  the domain rather than closing a second wall.
- **N3:** the hidden-condition scan exposes `C^2`/Taylor regularity and the
  ability to localize or Fourier-differentiate affine smearings.  Both are now
  explicit above; singular structure functions are not silently ruled out.
- **N4:** KSS, Regge and Loll do not attack this exact bracket residual.  They
  are interpretation/comparators only; the exact C3 certificate supplies the
  proof.
- **N5:** every negative statement is narrowed to the per-band L1 scalar and
  the flat global-charge coefficient.  No lattice-wide, all-matter or
  all-network negative is retained.
- **N6:** the escapes are changes of dynamics/representation, not evidence
  that a new framework axiom is required.  The existing axioms neither supply
  nor forbid those routes.
- **N7:** the strongest counterargument is an emergent multi-band network with
  interband charge matrices/Berry connection, or an infinite-depth effective
  SLAC kernel.  It is convincing against lane-level unavoidability but lies
  outside and therefore does not refute the narrow theorem.
- **N8:** the RN-L1 seagull is the closest prior retired wall.  Its unitary
  mechanism repairs symmetric uniform strain; exact Killing blindness proves
  that the same mechanism cannot enter the selected boost/rotation
  coefficient.

Consequently C3 alone does not meet the separate lane-FAIL clause at
`TESTS.md:1146-1151`.  Unless the independent C1-and-C2 route establishes its
own paired FAIL, the lane verdict remains **INCONCLUSIVE** from the evidence in
this packet.

## Strongest correct statement

For the fixed 09-14 constraint stencils and the L1 real, translation-invariant
single-band free scalar, with regular c-number structure coefficients on the
matter-bilinear flat sector and arbitrary local/analytic corrections polynomial
in `h,E` and at least quadratic in matter, the constant-shift/linear-lapse and
antisymmetric affine-shift sectors annihilate every gravity-dependent
completion exactly.  Closure would then require the periodic band function
`u=ω²/2` to have constant Hessian (and, independently in `d>=2`, to obey
the incompatible rotation equation `Hess u=M+μ∇u∇u^T`), leaving only the
dispersionless Carroll contraction rather than the GR algebra.  This proves
**C3 C-FAIL within that ansatz**; it does not exclude non-local SLAC-type
matter/gravity kernels, multi- or infinite-band/network realizations, singular
structure functions, altered leading generators, or a non-GR algebra, and so
it does not by itself establish the lane-level FAIL's “class free matter cannot
avoid” requirement.
