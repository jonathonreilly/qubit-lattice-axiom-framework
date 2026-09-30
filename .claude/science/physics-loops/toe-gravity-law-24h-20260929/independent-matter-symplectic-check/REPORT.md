# Independent check of the regular mixed-Poisson route

This is a focused independent mathematical check, not a formal audit, review
PASS, source-status change, or proof of a framework no-go. No blocking error
was found in the frozen derivation under its specified hypotheses. The
necessary mixed equation already fails before Jacobi identities are imposed.
The separate fixed-energy/fixed-walk uniqueness argument is also correct.

The result concerns the massless two-component source, fixed linear gravity
seeds, fixed flat quadratic matter generators, a regular charge-equivariant
Poisson structure, and a strong mixed identity with a scalar lapse on the
right. It does not exclude arbitrary matter-gravity phase spaces or theories.

## Frozen inputs and actual source reconstruction

The checked author report is `matter-symplectic-route/REPORT.md`, SHA256
`44b490da0cdf86a021844b7a30e7d9a094e337fea35c370f1248ef85ca03eae8`;
its contract is SHA256
`bf33dda2dfc2f5372c9db880504006750af1bdbf47781083bd2523f6e296e6b6`.
The existing independent matter report is SHA256
`8ddaafb14195d4c90f8bae4892310e70fd5770718738711bff99e7e0dbcc99fe`.
Main was fetched again during this check and remained
`e75578f7136401d4bd750131671aed9212c06291`. The complete actual September 25
two-step symmetric-books source, including its prescribed-source and
nonzero-mode boundaries, was read. Its bytes have SHA256
`6623c7432bfe1548ac53724c85f9bb082d8060d4e937c851aa7816476cfc7795`.
The source inventory gives the full long path. No author computation or
assembly code was imported or executed.

With `(T_j psi)_x=psi_(x+e_j)`, the source defines

`S_j=(T_j-T_j^-1)/(2i)`, `C_j=(T_j+T_j^-1)/2`,
`H=sum_j sigma_j S_j`, and `P_j=S_j C_j`.

The averaged real energy density gives, by moving its self-adjoint averaging
operator onto the lapse,

`E_N=psi^dagger {f_N,H} psi/2`, `f_N=C_1 C_2 C_3 N`.

Every averaging factor preserves both constants and affine coordinate
functions. Thus `E_1=psi^dagger H psi` and
`E_(x_j)=psi^dagger (X_j H+H X_j) psi/2` exactly.

The carried momentum's average has total weight one, so its total is
`psi^dagger P_j psi`. Summing the source's coin-energy current gives the
operator `C_j {sigma_j,H}/2=C_j S_j=P_j`; its further body-diagonal average
also preserves the total. Consequently the total symmetric current
`(P''+Q)/2` is exactly `P_j`. This independently identifies the uniform
generator used below; it is not an assumption that the two local densities
coincide.

The chosen quadratic spatial generator is `J_j=-psi^dagger P_j psi`.
For the canonical matter bracket its action is `+iP_j psi`, with the positive
Lie smooth limit. This sign choice differs from the literal plus-current
branch of the source's displayed prescribed-source action. No exact lattice
Lie action or supplied canonical gauge completion is being attributed to
the source. With a different `Z`, even the generator's action changes.

## Complete matter-degree count at flat gravity

Let `g` collectively denote all neutral gravity coordinates and momenta, and
scale the compactly supported charged profile as `psi -> epsilon psi`.
Regularity here means the relevant Taylor jets exist; it does not include a
coefficient singular at zero matter. Equivariance alone gives:

| Poisson block at flat gravity | Lowest matter orders |
|---|---|
| neutral gravity/gravity | order 0, then order 2 |
| gravity/psi | order 1 |
| psi/psi | order 2 |
| psi/psi-star | `-iZ` at order 0, then order 2 |

These statements refer to charge, not to spatial locality. A monomial with
`a` charged and `b` conjugate factors has charge `a-b`; this immediately
gives the displayed minima. Complex conjugation and antisymmetry require
the constant convolution `Z` to be Hermitian, but not positive or invertible.

The fixed gravity seeds are `G1[xi]=P.Rxi` and `C1[N]=-K R1[N]`. For a constant
shift the entire differential of `G1` is zero. For a constant or affine lapse
the entire differential of `C1` is zero: every curvature component has zero
zeroth and first lapse moments. This statement includes shear components,
not just an axial diagonal restriction. Higher pure-gravity terms have zero
first derivative at `g=0`.

At `g=0`, a term linear in gravity and quadratic in matter has gravity
derivative of order `epsilon^2` and matter derivative zero. The flat `E,J`
have matter derivatives of order `epsilon`. Therefore a mixed Poisson block
can pair such a gravity derivative with a matter derivative only at order
`epsilon^2 * epsilon * epsilon = epsilon^4`. Pairing two gravity derivatives
through a gravity/gravity block also first contributes at order four.
Anomalous matter brackets, matter-dependent corrections to `Z`, and higher
pure-matter terms first contribute at order four as well.

This enumerates the possible first derivatives in the bracket; it does not
assume a direct-product symplectic form, a Darboux transformation, or a
canonical gravity/gravity block. In particular arbitrary gravity-linear
quadratic matter terms in BOTH constraints are included. Only the constant
Hermitian matter block remains in the flat matter-degree-two equation.

Regular neutral field-dependent scalar structure coefficients do not change
this conclusion on the stated pure `C[U]` right side: gravity corrections
vanish at flat gravity, matter corrections multiply the quadratic matter
constraint at degree four, and a linear gravity constraint is zero at the
flat point even if its smearing depends on matter. This does not silently
admit a new independent operator or constraint on the right side.

## Real Poisson normalization and operator order

Use `psi=(q+i p)/sqrt(2)`, with real `q,p`. Writing `Z=Z_R+i Z_I`, Hermiticity
means `Z_R` is real symmetric and `Z_I` real antisymmetric, including lattice
indices. The corresponding constant real Poisson matrix is

`J_real = [[Z_I,Z_R],[-Z_R,Z_I]]`.

It gives `{psi,psi-star}=-iZ` and `{psi,psi}=0`, with no missing factor two.
For Hermitian quadratic forms the exact bracket is

`{psi^dagger A psi,psi^dagger B psi}`
`= -i psi^dagger (A Z B-B Z A) psi`.

The position of `Z` between the two gradients is essential. It cannot
generally be moved outside a commutator. The independent exact control
verifies this identity for fully symbolic Hermitian `2x2` matrices by using
the real `4x4` Poisson matrix; a misplaced-`Z` mutation is nonzero.

For constant shift, however, `P_j` is a scalar translation convolution and
commutes with the full matrix convolution `Z`. Set `F=P_j Z`. The remaining
mixed bracket is therefore exactly `i[F,E_N]` at quadratic matter degree.

## Uniform and affine necessary equations

For a scalar translation-covariant field-independent lapse kernel, constant
shift yields constants `mu0,mu1` such that

`U(e_j,1)=mu0`, `U(e_j,x_j)=mu0*x_j+mu1`.

The required nonzero first lapse moment is `mu1 != 0`. Uniform lapse closure
gives

`i P_j [Z,H] = mu0 H`.

Multiply by `H` and trace. Cyclicity gives zero on the left, whereas
`tr(H^2)=2 omega^2`, with `omega^2=sum_l sin^2(k_l)`. Thus `mu0=0`.
Where `P_j != 0`, the equation then implies `[Z,H]=0`. This set is dense;
continuity extends the commutation to every momentum. Hence `[F,H]=0`.

In the source's shift convention, a convolution has symbol
`F(k)=sum_r F_r exp(i k.r)` and

`[F,X_j]=sum_r r_j F_r T^r=-i partial_j F`.

No sign reversal is needed. Using the already established commutation with
`H`, the affine bracket becomes

`i[F,(X_j H+H X_j)/2] = {partial_j F,H}/2 = mu1 H`.

In particular the derivative differentiates BOTH factors in `F=P_j Z`.
The independent code reconstructs this identity from the literal row/column
matrix elements `(a_j+b_j)H_(b-a)/2`; it does not differentiate a Fourier
expression to obtain the tested left side. A noncommuting control correctly
retains its position-dependent `x_j i[F,H]` term, which the uniform equation
is responsible for eliminating.

There is a shorter independent conclusion than decomposing `F` into Pauli
components. Fix, for example, `k_2=pi/2,k_3=0` when `j=1`. Then `H` is invertible
everywhere on the entire periodic `k_1` circle because `H^2=omega^2 I` and
`omega^2 >= 1`. Multiply the affine identity by `H^-1` and take the trace:

`tr(({F',H}/2) H^-1) = tr(F') = 2 mu1`.

This uses only trace cyclicity. Integrating the derivative of the periodic
function `tr F` gives `0=4 pi mu1`, a contradiction. Equivalently
`partial_j(tr F/2)=mu1`. No positivity, invertibility, scalar ansatz, or
diagonalization of `Z` was used. The author's `F=uI+vH` derivation is also
valid: the traceless and scalar parts give precisely the equations displayed
there. The trace proof avoids needing that parametrization.

For the literal `J=+P^B` orientation the bracket changes sign; the same
contradiction holds for nonzero `mu1`. It does not remove that branch's
separate earlier CC obstruction.

## Infinite-lattice and affine-domain justification

The proof is an infinite-lattice necessary identity tested on compact matter
profiles; it does not assign an affine coordinate to a periodic torus or use
a normalizable transverse plane wave.

For any fixed compact profile and fixed candidate kernels, replace the
constant shift and affine lapse by compact plateaux agreeing with them on a
sufficiently large neighborhood of the profile. Every relevant kernel other
than the constant matter block `Z` has finite support by the contract. In a
matter-degree-two term, any seed differential must consequently be within a
fixed distance of a matter factor. The plateau is constant/affine throughout
that whole neighborhood, so these seed contributions vanish exactly. Pure
gravity boundary terms at matter degree zero are irrelevant to this Taylor
coefficient. Flat quadratic gradients of `E` and `J` themselves have compact
support because their operators have finite range. The possibly infinite
range `Z` joins these gradients and introduces no new nonlocal seed term.

The declared bound `sum_r (1+|r|) ||Z_r|| < infinity` implies a bounded
convolution and a bounded commutator `[Z,X_j]`, with norm bounded by
`sum_r |r_j| ||Z_r||`. It also implies that `Z` preserves `Dom X_j`, since
`X_j Z psi=Z X_j psi+[X_j,Z]psi`. Multiplication by the finite-range `P_j`
preserves these properties for `F`. Thus the affine convolution operations
above are legitimate on compact profiles and extend to the natural weighted
domain. In momentum space the symbols and their first derivatives are
continuous and periodic. These are the regularity facts actually used;
finite range or exponential decay of `Z` is not required.

Equality of Hermitian quadratic forms on all compact profiles implies
operator equality by polarization. After the uniform equation has eliminated
the position-dependent affine part, the affine residual is bounded and
translation-invariant. Its continuous Fourier symbol therefore vanishes
everywhere, not merely almost everywhere. Restricting that symbol to a
transverse-gapped circle is then legal; it does not amount to imposing a
noncompact matter state. The proof as written concerns the infinite lattice
and a full momentum-zone identity, not a theorem about one isolated finite
torus with an arbitrarily different Poisson matrix.

## Independent fixed-law uniqueness check

If the unchanged total energy must generate the actual linear free walk,
Hamilton's equation at the same jet is

`dot psi = -i Z H psi`.

For the energy alone this follows immediately from its matter derivative.
If it is embedded in the full uniform-clock constraint, the extra mixed
contributions still vanish at linear matter order: `dC1[1]=0`, higher pure
gravity derivatives vanish at the flat point, and gravity-linear matter
derivatives times mixed blocks first give order three. Anomalous brackets and
matter dependence of the Hermitian block also enter only at order three.

Requiring the supplied walk `dot psi=-iH psi` for every compact initial
profile gives `ZH=H`. Since `H^2=omega^2 I`, `H` is invertible except at the
eight zero-energy points of the three-dimensional momentum torus. It follows
that `Z=I` on their dense complement, and continuity fixes the same value at
those points. This does not require the mixed closure result or Poisson
Jacobi. Freedom in a discontinuous/distributional object supported on those
points lies outside the stated regular convolution class.

This uniqueness is conditional on BOTH the energy functional and its exact
linear vector field being held fixed. It is not a uniqueness theorem for
all Hamiltonian representations after changing the energy or variables.

## Scope, attempted escapes, and execution

The following changes are not excluded: charged additional carriers;
charge-breaking or singular Poisson coefficients; altered flat energy or
current generators; a different constraint-valued/operator-valued right
side; weak equality only on a constraint surface; nonzero backgrounds;
restricted infrared identities; or a Poisson structure without the declared
regular affine domain. The present derivation is for the specified massless
two-component source and does not silently import the prior staggered-mass
extension into a new symplectic theorem.

An elementary reduced infrared escape confirms the full-zone hypothesis is
load-bearing. On an open interval in `k_j` about zero and strictly inside
`(-pi/2,pi/2)`, take `Z=[k_j/(sin k_j cos k_j)] I`, with its removable value at
zero. Then `F=k_j I`, the uniform reduced equation holds, and the affine
reduced equation has `mu1=1`. This does not extend to a regular periodic
symbol through the zeros at `+/-pi/2`, does not preserve the fixed free-walk
law, and is not a construction of the full lapse algebra or a nonlinear
Poisson completion. It is a direct reason not to call the result an
infrared no-go.

No source novelty search or full Jacobi/CC/GG construction was performed in
this check. The known `cos(2k_j)` canonical multiplier is prior art already
identified in the existing independent report. The additional checked scope
is the exclusion of the declared regular mixed-Poisson repair with the fixed
flat generators. The axioms and source admissibility statuses are unchanged.

One exact compute job was priced below ten seconds and 150 MB, with BLAS/OMP
threads capped at one. Actual runtime was **1.230 seconds**, peak RSS
**62,537,728 bytes**. It verifies the generic real-Poisson quadratic identity,
detects an ordering mutation, checks literal affine rows at `-7,0,11` for a
non-scalar commuting matrix convolution, checks a noncommuting control, and
verifies the generic trace identity and charge counts. Its symbol-slice
fixture has `sin(k_2)=3/5,sin(k_3)=4/5`, so it is genuinely gapped. It uses
unrestricted integer coordinates, with no finite-torus aliasing assumption.
These controls support the displayed analytic proof; finite examples are
not substituted for the universal argument.

The deadline remained open and the stop sentinel absent before computation.
Only this independent-check directory was written. `SOURCE_BINDINGS.json`,
`results.json`, the independent script, and `MANIFEST.json` bind the evidence.
