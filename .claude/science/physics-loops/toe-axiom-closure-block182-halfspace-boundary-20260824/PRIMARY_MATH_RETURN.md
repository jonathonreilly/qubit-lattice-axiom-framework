# Block 182 primary mathematics return

## Dispatcher correction after independent refutation

Every negative “positive transfer/realization” statement below is restricted
to an **H-self-adjoint OS transfer whose fixed readout is the H-adjoint of the
fixed source**. Positivity alone is not obstructed. With `u=(1,1,1)^T`,
`Pi=I-uu^T/3`, and

\[
 H_c=(cu^T+uc^T)/3-(u^Tc)uu^T/9+\Pi,
\]

the same three-pole response has `H_c u=c`, `H_c>0`, and
`H_c-T^T H_cT>0`; the minimum eigenvalues are respectively `0.1094414` and
`0.1021778`. But `||H_cT-T^TH_c||=0.1085594`, so the escape is a positive
non-self-adjoint contraction, not an OS/self-adjoint transfer. This correction
is load-bearing and narrows the worker's original wording wherever needed.

## Decision and exact scope

At the supplied action, `mu=1/1024`, spatial momentum
`k=(pi/2,0,0)`, odd `y/z` reflection sector, and the supplied local TT-plus
source/readout, separating the polynomial endpoint chains does **not** produce
a source-faithful positive H-self-adjoint one-step or two-step half-space transfer for the
exact TT response.  The obstruction is finite-dimensional: the minimal stable
TT response has three simple, source-visible states, and the Hermitian metric
equations have a unique solution with one negative eigenvalue.  Squaring the
transfer removes the negative eigenvalue of the transfer matrix but does not
remove the negative residue.

This decides only that exact response/action/source/readout tuple at this one
spatial momentum and at one- and two-tick cadence.  It is not a result about
gravity, other actions, other momenta, another half-space Weyl function, a
different boundary state, or a different source/observable map.

## 1. The bordered polynomial and a strong descriptor linearization

Let `U` be the supplied orthonormal six-column `y/z`-odd edge basis, let `V`
be the supplied one-column odd gauge basis, and put

\[
 g=\binom{U^T o_{\rm TT+}}{0}=\sqrt2\,e_1\in\mathbb C^7.
\]

On `z=e^{iq_t}` define the analytic continuation of the sampled border by

\[
 \mathcal B(z)=
 \begin{bmatrix}
 -U^TQ_\mu(k,z)U & U^TG(-k,z^{-1})V\\
 (U^TG(k,z)V)^T&0
 \end{bmatrix}
 =\sum_{r=-2}^{2}B_rz^r .                                      \tag{1}
\]

The coefficient definition used independently in the scratch calculation was

\[
 B_r={1\over64}\sum_{\ell=0}^{63}
 \mathcal B(e^{2\pi i\ell/64})e^{-2\pi i r\ell/64},             \tag{2}
\]

whose out-of-support matrix leakage was `4.143e-17`.  It obeys
`B_{-r}=B_r^dagger` to roundoff.  Clear the two negative powers:

\[
 P(z)=z^2\mathcal B(z)=P_0+zP_1+z^2P_2+z^3P_3+z^4P_4,
 \qquad P_j=B_{j-2}.                                           \tag{3}
\]

The numerical coefficient ranks are

\[
 (\operatorname{rank}P_0,\ldots,\operatorname{rank}P_4)
 =(2,7,7,7,2),\qquad P_{4-j}=P_j^\dagger.                       \tag{4}
\]

The endpoint matrices are particularly simple.  In the supplied odd basis,
with `mu=1/1024`,

\[
 P_0=i\mu
 \begin{bmatrix}
 0&\sqrt2&0&-\sqrt3&0&0&0\\
 0&0&0&0&0&0&0\\
 0&0&0&0&0&0&0\\
 0&0&0&0&0&0&0\\
 \sqrt2&0&0&0&0&0&0\\
 -\sqrt3&0&0&0&0&0&0\\
 0&0&0&0&0&0&0
 \end{bmatrix},\qquad P_4=P_0^\dagger.                         \tag{5}
\]

Thus the two nonzero endpoint singular values are both
`2.18366013e-3`; the remaining five are at the `1.1e-16` absolute
coefficient-reconstruction level.

For `x in C^7`, set

\[
 X(z)=\begin{bmatrix}z^3x\\z^2x\\zx\\x\end{bmatrix}.
\]

An explicit 28-by-28 first Frobenius strong linearization is

\[
 \mathcal L(z)=zE-A,                                           \tag{6}
\]

\[
 E=\begin{bmatrix}
 P_4&0&0&0\\0&I_7&0&0\\0&0&I_7&0\\0&0&0&I_7
 \end{bmatrix},\qquad
 A=\begin{bmatrix}
 -P_3&-P_2&-P_1&-P_0\\
 I_7&0&0&0\\0&I_7&0&0\\0&0&I_7&0
 \end{bmatrix}.                                               \tag{7}
\]

Indeed, the first block row of `L(z)X(z)` is `P(z)x`, and the other
three block rows vanish.  Standard block elimination gives unimodular
equivalence to `diag(P(z),I_21)`; applying the same elimination to the
reversal makes (6) a strong linearization, including infinity.  Numerically,
`rank(A)=rank(E)=23`, consistent with five geometric endpoint chains at each
end.

## 2. Zero, punctured-plane, and infinite eigenvalue counts

### 2.1 Determinant degree

An implementation independent of the supplied permutation expansion sampled
`det B(e^{it})` at 128 points and Fourier transformed the scalar determinant.
The relative leakage outside `r=-7,...,7` was `2.302e-16`.  After averaging
reciprocal-paired roundoff, the real Laurent coefficients
`(d_-7,...,d_7)` are

```text
(-1.54618e-9, -5.76613329e-5, +2.17280781e-1, -3.473767144,
 +2.626241651e1, -8.348609979e1, +1.411405590e2, -2.470681964e2,
 +1.411405590e2, -8.348609979e1, +2.626241651e1, -3.473767144,
 +2.17280781e-1, -5.76613329e-5, -1.54618e-9).
```

The endpoint determinant coefficient is `6.258e-12` of the largest
coefficient, still about `2.7e4` times the measured Fourier leakage.  Hence,
for the reconstructed pencil,

\[
 \det P(z)=z^{14}\det\mathcal B(z)
 =z^7q_{14}(z),\qquad
 q_{14}(z)=\sum_{m=0}^{14}d_{m-7}z^m,                            \tag{8}
\]

with `q_14(0) != 0` and a nonzero degree-14 leading coefficient.

### 2.2 Endpoint rank staircases

For the zero endpoint define the lower block-Toeplitz chain matrix

\[
 \mathcal T_k^{(0)}=
 \begin{bmatrix}
 P_0&0&\cdots&0\\
 P_1&P_0&\ddots&\vdots\\
 \vdots&\ddots&\ddots&0\\
 P_{k-1}&\cdots&P_1&P_0
 \end{bmatrix},                                                \tag{9}
\]

where coefficients above `P_4` are zero.  For infinity use the same matrix
with `(P_0,...,P_4)` reversed.  After zeroing coefficient noise below
`1e-12`, both endpoints gave

| `k` | matrix size | rank | nullity `kappa_k` | last retained / first dropped singular value, normalized |
|---:|---:|---:|---:|---:|
| 1 | 7 | 2 | 5 | `1.000e0 / 6.28e-17` |
| 2 | 14 | 8 | 6 | `9.566e-7 / 1.08e-17` |
| 3 | 21 | 14 | 7 | `3.741e-9 / 1.35e-17` |
| 4 | 28 | 21 | 7 | `3.943e-15 / 6.63e-18` |

The infinity figures agree at the displayed precision.  Since
`kappa_k-kappa_{k-1}` counts chains of length at least `k`, the increments
`(5,1,1,0)` give the endpoint partial multiplicities

\[
 (3,1,1,1,1)                                                   \tag{10}
\]

at zero and again at infinity.  Their sum is seven at each endpoint.
Equation (8) independently caps the zero sum at seven and the grade-four
reversal caps the infinity sum at seven; this is important because the
`k=4` retained singular value is small.

Consequently the 28 generalized eigenvalues of (6), with algebraic
multiplicity, split as

\[
 \boxed{N_0=7,\qquad N_{\mathbb C^\times}=14,\qquad N_\infty=7.} \tag{11}
\]

There are seven punctured-plane roots inside the unit circle and seven
reciprocal roots outside it.  A raw, unbalanced double-precision QZ call on
the undeflated 28-pencil reported `4/20/4`: it split the length-three endpoint
chains into three false roots of order `1e-5` and three false reciprocal roots
of order `1e6`.  That output was rejected.  The `epsilon^(1/3)` scale is
exactly why the determinant support and rank staircase, rather than a bare QZ
count, are load-bearing.

### 2.3 What is and is not finite dynamics

For every `z != 0`, `ker P(z)=ker B(z)`.  At `z=0` multiplication by `z^2`
is not invertible, and infinity enters through the chosen grade-four
polynomial reversal.  Thus the ten chains in (10), carrying fourteen endpoint
eigenvalue multiplicities, are descriptor endpoint/denominator-clearing data,
not extra punctured-plane poles.  They
still encode the singular outer temporal stencil and must not be silently
called physical constraints; their physical boundary interpretation remains
open.

For the actual TT scalar response the separation is stronger.  With

\[
 F(z)=g^T\mathcal B(z)^{-1}g={N(z)\over D(z)},
 \quad D(z)=\det\mathcal B(z),
 \quad N(z)=g^T\operatorname{adj}(\mathcal B(z))g,               \tag{12}
\]

the independent scalar Fourier calculation found `supp D=[-7,7]` but
`supp N=[-6,6]`, with endpoint numerator coefficients
`-7.57441e-9`.  Hence `F(z)=O(z)` at zero and `F(z)=O(z^-1)` at infinity.
Neither endpoint contributes a pole to the nonnegative-time TT moments.

## 3. Finite stable TT boundary state

For a simple finite root choose analytic right and left null vectors

\[
 \mathcal B(z_i)x_i=0,\qquad y_i^T\mathcal B(z_i)=0.
\]

Its scalar residue and moment weight are

\[
 \rho_i={ (g^Tx_i)(y_i^Tg)\over y_i^T\mathcal B'(z_i)x_i},
 \qquad a_i={\rho_i\over z_i}.                                 \tag{13}
\]

A simple pole is removable from this TT response exactly when

\[
 (g^Tx_i)(y_i^Tg)=0,                                           \tag{14}
\]

i.e. the mode is unobservable on the readout side or uncontrollable from the
source side.  A nonzero denominator and two nonzero factors make it
source-visible; choosing a desired root by its location alone is not allowed.
For nonnegative time the stable contour therefore gives

\[
 C_n={1\over2\pi i}\oint_{|z|=1}z^{n-1}F(z)\,dz
 =\sum_{|z_i|<1}a_i z_i^n,
\]

with no zero-endpoint term because `F(z)=O(z)` there.

The seven stable roots are

| root | TT status |
|---:|---|
| `-2.45439e-5` | two-sided, source-visible |
| `+2.911690e-4` | two-sided, source-visible |
| `0.093342994 - 0.088067940 i` | one-sided dark |
| `0.093342994 + 0.088067940 i` | one-sided dark |
| `+0.266171726916` | two-sided, source-visible |
| `0.055544754 + 0.547714173 i` | one-sided dark |
| `0.055544754 - 0.547714173 i` | one-sided dark |

The supplied machinery and the disjoint reconstruction gave the following
three nonzero weights.  Small imaginary parts are numerical residuals; the
table records their real parts.

| `i` | supplied `z_i` | supplied `a_i` | left/right coupling | border / full-edge / multiplier residual | simplicity ratio |
|---:|---:|---:|---:|---:|---:|
| 1 | `-2.45439070e-5` | `+1.51761043e-4` | `4.946e-5 / 4.946e-5` | `3.17e-17 / 3.82e-15 / 3.37e-15` | `3.144e-12` |
| 2 | `+2.911690247e-4` | `-2.174507276e-4` | `7.023e-4 / 7.023e-4` | `2.04e-16 / 3.73e-15 / 2.66e-15` | `6.154e-8` |
| 3 | `+0.266171726916` | `+0.581884811601` | `0.4280 / 0.4280` | `3.49e-17 / 6.12e-17 / 1.11e-15` | `5.454e-2` |

The independent route used a 64-point matrix DFT, a 128-point direct
determinant DFT rather than the supplied Laurent permutation expansion,
direct null-vector residues, and a 32768-point contour quadrature.  Its three
root differences from the supplied route were at most `9.5e-11` absolute,
its real-weight differences were at most `2.1e-10` absolute (imaginary
roundoff stayed below `8e-10`), and its first-nine
moment reconstruction error was `9.65e-10` relative.  The supplied route's
corresponding moment error was `6.81e-10`.  This is a calculation cross-check,
not an independent audit verdict.

After the four stable zero-residue cancellations, a finite stable realization
of the exact nonnegative-time TT response is

\[
 T=\operatorname{diag}(-2.45439070\!\times\!10^{-5},
                         2.911690247\!\times\!10^{-4},
                         0.266171726916),                         \tag{15}
\]

\[
 b=\begin{bmatrix}1\\1\\1\end{bmatrix},\qquad
 c=\begin{bmatrix}
 1.51761043\!\times\!10^{-4}\\
 -2.174507276\!\times\!10^{-4}\\
 5.81884811601\!\times\!10^{-1}
 \end{bmatrix},\qquad
 C_n=c^TT^nb.                                                    \tag{16}
\]

The controllability and observability matrices have rank three:

\[
 \det[b,Tb,T^2b]=2.23450\times10^{-5},\qquad
 \det\begin{bmatrix}c^T\\c^TT\\c^TT^2\end{bmatrix}
 =-4.29081\times10^{-13}.                                      \tag{17}
\]

Thus (15)-(16) is minimal despite the small first two residues.  The direct
moments used for the check were

```text
C[0:9] = (5.81819122e-1, 1.54881218e-1, 4.12250191e-2,
          1.09729345e-2, 2.92068494e-3, 7.77403753e-4,
          2.06922899e-4, 5.50770255e-5, 1.46599470e-5).
```

## 4. Positive-metric feasibility, without branch selection

The same-source/readout condition is not a sign choice.  In the realization
(15)-(16), a Hermitian state metric must make the readout the Riesz dual of
the source:

\[
 H=H^\dagger,\qquad Hb=c.                                      \tag{18}
\]

For a stable positive one-step transfer the finite feasibility problem is

\[
 \begin{array}{ll}
 \text{find}&H=H^\dagger\\
 \text{such that}&H\succ0,\quad T^\dagger H=HT,\quad Hb=c,\\
                 &HT\succeq0,\quad H-T^\dagger HT\succeq0.
 \end{array}                                                    \tag{19}
\]

The last inequality is the contraction condition; dropping it does not alter
the negative result.  For the two-step transfer use the same `b,c` and

\[
 S=T^2=\operatorname{diag}(6.02403\times10^{-10},
                            8.47794\times10^{-8},
                            7.08473882\times10^{-2})             \tag{20}
\]

and replace `T` by `S` in (19).

All three `z_i` are distinct and real, so

\[
 (T^\dagger H-HT)_{ij}=(z_i-z_j)H_{ij}=0
\]

forces `H` diagonal.  Equation (18) then fixes it rather than allowing a
desired branch to be selected:

\[
 H=\operatorname{diag}(a_1,a_2,a_3).                            \tag{21}
\]

The three squared roots in (20) are also distinct, so the two-step equality
problem has exactly the same unique solution.  Numerically,

| test | equality residuals `||Riesz||, ||selfadjoint||` | `lambda_min(H)` | `lambda_min(H transfer)` | result |
|---|---:|---:|---:|---|
| one step `T` | `0, 0` | `-2.1745073e-4` | `-6.33149e-8` | infeasible |
| two step `S=T^2` | `0, 0` | `-2.1745073e-4` | `-1.84353e-11` | infeasible |

There are two independent one-step sign failures.  The first branch has
`a_1>0` but `z_1<0`, giving `(HT)_11=-3.72481e-9`; the second has
`z_2>0` but `a_2<0`, so `H` itself is indefinite.  Squaring closes only the
first sign problem.  It leaves `(HS)_22=-1.84353e-11`.

This conclusion is not an artifact of using a three-state realization.  Any
positive H-self-adjoint Hilbert-space transfer with the same source and readout would make
the relevant Hankel matrices Gram matrices.  The direct moments give

\[
 \lambda_{\min}
 \begin{bmatrix}C_1&C_2\\C_2&C_3\end{bmatrix}
 =-4.42624335\times10^{-9},                                    \tag{22}
\]

for one step, and

\[
 \lambda_{\min}
 \begin{bmatrix}
 C_0&C_2&C_4\\C_2&C_4&C_6\\C_4&C_6&C_8
 \end{bmatrix}
 =-3.29747671\times10^{-7}                                    \tag{23}
\]

for the even subsequence.  A nonminimal positive self-adjoint dilation or the addition of
source-dark states cannot change these scalar Gram matrices or the nonzero
partial-fraction residues.

## 5. Minimum object that must change

The invariant obstruction is the exact scalar TT response, specifically the
pair `z_1<0,a_1>0` at one step and `z_2>0,a_2<0` at both cadences.  Merely
changing descriptor coordinates, retaining or deleting the zero/infinite
chains, applying a similarity transformation, or adding source-dark boundary
states cannot help.

Therefore the minimum algebraic object that must change is the **exact TT
response** (its finite pole set or residues), unless the OS/self-adjoint
transfer requirement itself changes. With the bulk action held fixed,
that could come from a physically derived boundary state/Weyl prescription
whose Green function is not (12).  Alternatively the source/readout map could
be changed so that a hostile pole satisfies (14), but that is no longer the
same source-faithful TT question.  Changing the action is sufficient in
principle but is not logically forced by this one-momentum certificate.  A
boundary-state change that leaves (12) unchanged is insufficient.

## 6. Algebra proved, numerical evidence, and open interpretation

**Proved algebra, conditional on the reconstructed coefficient data.**  The
linearization (6)-(7) is strong; (8)-(11) imply the `7/14/7` generalized-
eigenvalue split; (13)-(17) give the minimal response realization; and
(18)-(23) prove infeasibility for every exact same-source/readout positive
H-self-adjoint one- or two-step realization, including nonminimal ones.

**Numerical evidence.**  The coefficient support, endpoint ranks, determinant
endpoint coefficients, fourteen finite roots, three nonzero residues, signs,
and Hankel eigenvalues are conditioned double-precision results.  The weakest
simple-root ratio is `3.144e-12`, so only the displayed stable digits should be
used.  The independent determinant/quadrature route and the supplied
machinery agree at the residuals stated above.  This is not a symbolic
completeness proof for the unthresholded action.

**Open physical interpretation.**  The endpoint chains have been separated
algebraically, not identified with a physical Dirac constraint surface.  The
minimal axioms do not select an action, time metric, transfer, boundary state,
or source/observable dictionary.  The positive multislice SU(3)-staggered
half-space construction in the supplied RP note demonstrates that a positive
crossing-kernel construction can exist in a different model; it supplies no
intertwiner to this reflected-curvature pencil.  A derived half-space Weyl
function, longer blocking, another action, or another source/readout remains
open.

## 7. Proposed primary runner certificate

Each mutation below should be applied to an isolated copy of the formula
input, must exit nonzero, and must not alter the expected constant used by its
own check.

| check family | load-bearing checks | one source-level mutation |
|---|---|---|
| `symbol-source-binding` | odd dimensions `6+1`, exact `g=sqrt(2)e1`, support `-2..2`, reciprocity, DFT leakage | add `1e-3 exp(3 i q_t) I_6` to the odd action sample (`laurent_support`) |
| `descriptor-endpoint-staircase` | construct (3), verify (6)-(7) on random `z,x`, ranks `23/23`, Toeplitz nullities `(5,6,7,7)`, determinant degrees `7..21`, counts `7/14/7` | move `P_0` from the fourth to the third top-row companion block (`companion_p0_slot`) |
| `punctured-root-residue-visibility` | 14 simple nonzero roots, 7 inside, reciprocal pairing, three two-sided TT residues, endpoint numerator support `-6..6` | replace the derivative factor `r` by `r+1` in `B'(z)` (`residue_derivative`) |
| `minimal-state-direct-moments` | matrices (15)-(16), controllability/observability rank three, 32768-point direct contour, first nine moments | reconstruct with `a_i z_i^(n+1)` (`moment_exponent`) |
| `one-step-metric` | solve all real parameters of Hermitian `H`, enforce original `Hb=c`, selfadjointness, `H>0`, `HT>=0`, and shifted Hankel control | feed `abs(c)` to the solver while retaining original `c` in the Riesz residual (`metric_abs_weight`) |
| `two-step-same-interface` | form `S=T^2` mechanically, retain identical `b,c`, solve the full metric equations, and check the even Hankel matrix | delete the negative-weight state before squaring (`even_drop_branch`) |
| `scope-and-no-go-boundary` | one momentum/action/source only; distinguish algebra, numerics, and physical interpretation; N1-N8 text present; no gravity/axiom/audit claim | replace `one supplied momentum` by `all gravity momenta` (`scope_broadening`) |

Normal execution should end with seven passing aggregates and
`TOTAL: PASS=7 FAIL=0`; stdout should include substantive `per_element`,
`per_site`, `per_mode`, `per_block`, and `lattice_wide` lines and stay below
6000 characters.

## 8. No-Go Discipline Gate

The gated statement is only: *the exact scalar response (12), with the same
TT source/readout, has no positive H-self-adjoint one-step or two-step
realization at the declared momentum*.  No route is marked `RULED OUT BY PRIOR`; the supplied
parents are bounded/unaudited inputs, and the evidence below is recomputed.

### N1 — normalized alternative routes

| family `(object; invariant; terminal obligation)` | result | marker |
|---|---|---|
| descriptor endpoint deflation; Smith-chain multiplicities; remove nonfinite chains before testing positivity | succeeds in separating `7+7` endpoint eigenvalues, but leaves all three finite TT residues unchanged | `ATTEMPTED` |
| minimal-realization similarity; pole/residue invariance; find a positive self-adjoint metric in another coordinate basis | (18)-(21) are similarity invariant and give one negative metric eigenvalue | `ATTEMPTED` |
| pole cancellation; numerator/source-observable factors; make hostile finite poles removable with the same `g` | both factors in (13) are nonzero for all three hostile/target poles | `ATTEMPTED` |
| one-step transfer; positivity of `HT` and shifted moments; realize all `C_n` | the negative root and negative weight independently violate (19) and (22) | `ATTEMPTED` |
| even-step transfer; positivity of `HS` and even moments; realize all `C_2n` | squaring removes the negative root sign but preserves the negative weight, violating (23) | `ATTEMPTED` |
| nonminimal positive self-adjoint dilation; positivity of the scalar spectral measure; preserve the exact rational response | extra source-dark states cannot alter a nonzero residue or the negative Hankel eigenvalues | `ATTEMPTED` |

These families differ in primary object, invariant, and terminal obligation;
they are not multiple phrasings of one diagonal-metric calculation.

### N2 — collapsed walls

| walls | closing first closes second? | closing second closes first? | independent? |
|---|---|---|---|
| `W1`: negative one-step spectral point / `W2`: negative source-visible weight | no; squaring closes `W1` but not `W2` | no; changing the weight does not change the negative root | yes |

There are two one-step walls and one surviving two-step wall; endpoint
separation is a completed reduction, not an additional wall.

### N3 — hidden-condition scan

The load-bearing conditions are all explicit: supplied action and `mu`, one
spatial momentum, one odd basis, the supplied local TT-plus `g`, the stable
unit-disk contour, simple roots, the exact response (12), and identical source
and readout.  “Strong” and “minimal” are linear-systems properties proved by
(6) and (17), not physical-canonical claims.  No background, standard-QFT,
framework-provided dynamics, or unregistered physical inner product is used.

### N4 — residual matching

| supplied citation | cited residual | residual here | match/use |
|---|---|---|---|
| Block-181 note, lines 129-138 and 231-246 | same three roots/weights and one/two-step moment signs | metric realization of that same scalar TT response | exact match; recomputed, not inherited |
| Block-74 script, lines 591-631 | necessary one-step and hostile two-step TT Hankel positivity | equations (22)-(23) for its TT-plus moments at `k=pi/2` | exact for TT-plus; cross observable not claimed here |
| RP multislice note, lines 155-190 and 304-305 | positive half-space Gram for a different SU(3)-staggered crossing kernel | reflected-curvature TT pencil | no match; retained only as a live counterexample to broad rhetoric |
| minimal axioms, lines 116-123 and 173-188 | no selected transfer/action/source-observable law | premise boundary | not numerical evidence and not used as a no-go witness |

### N5 — rhetoric and resolution

- `per_element`: all five 7-by-7 coefficients, the TT row, and both border
  sides enter the reconstruction.
- `per_site`: only the translation-invariant reflected unit cell is executed;
  an inhomogeneous carrier is not tested.
- `per_mode`: every generalized temporal root at one spatial momentum is
  resolved; no other spatial momentum is tested.
- `per_block`: endpoint chains, finite residues, one-step metric, and two-step
  metric/Hankel blocks are executed.
- `lattice_wide`: not executed; no Brillouin-zone, nonlinear, continuum, or
  all-action statement is made.

### N6 — partial-closure paths left live

A boundary Weyl/Feshbach function may change (12) while keeping the bulk
action; a different source/readout may make a hostile pole dark; a changed
action may move roots/residues; longer-than-two blocking may define another
moment problem; and an independently factorized positive crossing kernel may
define another half-space theory.  None is called failed.  No new-axiom claim
is made, so convention/primitive retirement is not being foreclosed.

### N7 — strongest steelman

> A constrained half-space theory need not use the full-circle inverse (12)
> as its Weyl function.  A derived Dirac boundary relation could pair the
> length-three endpoint chain with auxiliary boundary data and yield a new
> source-faithful boundary Green function in which the two small hostile poles
> are absent or have positive measure, just as a positive crossing kernel
> controls the distinct RP multislice construction.  The terminal obligation
> is to derive that boundary form from this action and show its source/readout
> pullback and exact moments; it has not been attempted here.

This steelman defeats any gravity or all-boundary-state no-go.  It does not
defeat the exact-response statement because its proposed Weyl function changes
(12).

### N8 — cross-cycle echo and trigger flag

Within the dispatch-permitted five-file surface, Block 74 found the Hankel
sign, Block 181 localized it to finite residues, and the RP note shows that a
different single-crossing kernel can be positive.  A repo-wide echo search was
forbidden by the five-file reading boundary, so no repo-wide/cross-campaign
negative is eligible to ship.  Any claim about gravity, all actions, all
momenta, all boundary states, or axiom insufficiency therefore **triggers a
fresh full N1-N8 gate and is not made here**.

**Gate disposition:** pass for the self-contained finite-dimensional
infeasibility statement above; fail/not attempted for every broader no-go.

## Raw summary

```text
verdict=exact same-TT one-step and two-step positive H-self-adjoint realization infeasible at supplied k/action
descriptor_counts=zero:7 finite_nonzero:14 infinity:7
endpoint_partial_multiplicities=zero:(3,1,1,1,1) infinity:(3,1,1,1,1)
minimal_TT_state=3 roots; weights=(+1.51761e-4,-2.17451e-4,+5.81885e-1)
metric_solution=unique H=diag(weights); lambda_min(H)=-2.17451e-4
even_step=negative weight survives; lambda_min(even_Hankel)=-3.29748e-7
scratch_01=python3 .block182_probe.py
scratch_02=python3 .block182_probe.py
scratch_03=python3 .block182_probe.py | rg 'clean staircase|QZ counts|P coefficient ranks|companion ranks|Toeplitz kernel dims|rank gaps'
scratch_04=python3 .block182_probe.py | rg -A4 'TT numerator|Hankel one|Hankel even|moment max|coupled roots|coupled weights|metric residuals'
scratch_05=python3 .block182_probe.py | rg -A5 'supplied machinery'
scratch_06=python3 .block182_probe.py | rg -A10 'determinant roots|stable residue rows|coupled roots|supplied machinery'
scratch_07=python3 .block182_probe.py | rg 'clean endpoint gaps|clean staircase 1e-16|determinant reciprocal error'
scratch_08=python3 .block182_probe.py | rg -A4 'supplied machinery coupled'
scratch_09=python3 .block182_probe.py | rg 'T diagonal|T2 diagonal|H one transfer|H even transfer'
scratch_processes_left_running=none
claim_scope=one momentum, supplied action, supplied TT source/readout, one/two step only
broader_physics_interpretation=open
```
