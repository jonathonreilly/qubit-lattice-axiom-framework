# Arbitrary finite kinetic pairing: independently checked matrix-symbol obstruction

New route contract frozen before computation,2026-09-29. The argument and physical reduction have now been reconstructed independently
in `independent-axial-check/LATTICE_TRANSLATION_SYMBOL_CHECK.md`; this is not a
formal review or negative-packet PASS.
It expands the kinetic ansatz beyond block112 rather than silently changing
that source. No new axiom or primitive is proposed or adopted.

## Changed target and remaining fixed hypotheses

The affine point witness used the supplied ultralocal kinetic density. A
cross-site momentum pairing removes its stationarity: the original proof alone
does not exclude such a change. We now test *every* translation-covariant,
finite-range quadratic momentum density T2[N] with the same nondegenerate
long-wavelength TT kinetic normalization. Each candidate has finite total
support; there is no common radius bound across candidates.

Retain the source's canonical symmetric-tensor phase space, linear C1 and G1,
regular analytic jets, time reversal, and proper cubic covariance. Require the
strong mixed bracket with a finite-range bilinear U0 satisfying
U0(1,1)=0 and U0(1,x)=1, plus arbitrary regular same-order constraint mixing.
These normalizations express its supplied continuum action on a scalar lapse.
No cubic ADM normalization, fixed F0, CC or GG success is assumed in the proof.
The claim concerns a necessary mixed-bracket equation only.

## Axial transverse-traceless reduction

Take fields independent of y,z, with shift in x. Proper rotation by90 degrees
around x has eigenvalue-1 on the two canonical TT coordinates

    q=((h_yy-h_zz)/2, h_yz),   p=(P_yy-P_zz, P_yz).

The scalar sectors have eigenvalue+1 and the x-transverse vector sector has
eigenvalues+i,-i. Therefore any covariant quadratic kinetic form and the
constant-shift bilinear generator preserve the two-dimensional TT block.
Both TT components must be retained: proper cubic covariance alone does NOT
separate them into two one-dimensional sectors. General off-diagonal and
chiral matrix kernels are allowed in the following argument.

Use transverse zero Fourier modes with canonical normalization, or include the
transverse area in both reduced functionals and their symplectic form. The
common area cancels. Neither TT coordinate has a half-x stagger displacement.

On this block all linear momentum constraints vanish for arbitrary x profiles.
C1[1] and C1[x] vanish identically by their second differences; G1[1] vanishes
identically. At h=0 the mixed momentum-quadratic equation therefore reduces,
for uniform and affine lapses, to a statement about G2 and T2 alone. All
cubic generators and constraint-mixing terms disappear from these evaluations.
Compact smearings on a sufficiently large affine plateau give the same local
identities for any finite-support p and any proposed finite-range jet.

Write the constant-shift quadratic generator and kinetic forms as

    G2[1]=p^T D q,
    T2[1]=(1/2)p^T F p,
    T2[x]=(1/2)p^T B p.

Here D and F are real matrix convolution operators, F^sharp=F, with two by two
Laurent symbols in z; sharp sends z to1/z and transposes the matrix. The kinetic
normalization gives F(1)=(1/(4alpha))I for the source normalization, hence detF
is not the zero Laurent polynomial. Invert F over the rational-function field;
this step does not assume absence of isolated zeros at finite lattice momentum.

Any translation-covariant quadratic density linear in N has

    B=X F+A,

where X multiplies by the integer site coordinate and A is a matrix convolution.
Indeed, a density term N_x p_(x+i)^T t_ij p_(x+j) has N_x=y-i when its first
momentum coordinate is y. Its affine matrix differs from X times the uniform
matrix by the translation-invariant offset-i term. Symmetrizing the quadratic
matrix preserves this form. No midpoint-timing restriction is imposed on A.

## Matrix identity and contradiction

Canonical differentiation gives

    {p^T Dq, (1/2)p^T Fp}=(1/2)p^T(D F+F D^sharp)p.

The uniform-lapse equation therefore requires

    D F+F D^sharp=0.                                   (1)

The affine-lapse equation requires

    D B+B D^sharp=F.                                   (2)

Using B=XF+A and(1), the left side of(2) is

    [D,X]F+D A+A D^sharp
      = ([D,X]+[D,A F^(-1)])F.

For a convolution D(z)=sum_r D_r z^r, the exact commutator [D,X] has symbol
z*dD/dz. Thus(2) implies the rational matrix identity

    z*dD/dz + [D,A F^(-1)] = I_2.                       (3)

Taking the ordinary finite matrix trace removes the commutator:

    z*d(trD)/dz = 2.                                   (4)

The coefficient of z^0 on the left of(4) is zero for every finite Laurent
polynomial. The coefficient on the right is2. This is impossible.

Conditional conclusion: arbitrary finite kinetic pairing does not repair the
mixed bracket within this enlarged regular canonical, proper-cubic,
nondegenerate-TT and exact scalar-lapse-normalization class. This proof uses
finite matrix trace, not a scalar diagonalization or parity assumption.
The independent check separately verified the canonical reduction, proper C4
block isolation, arbitrary density centering, noncommuting matrix algebra and
a finite-position Hessian control. It also proved the extension with arbitrary
U0(1,1)=mu0 and U0(1,x)=mu0*x+mu1, provided mu1 is nonzero: the mu0 terms
cancel, and the trace equation becomes z*d(trD)/dz=2mu1.

## Scope, standard context and live alternatives

This is not a theorem against lattice gravity, finite-M2 dynamics, or all weak
constraint ideals. Its imports are the explicit canonical tensor carrier,
finite-support microscopic jets, supplied flat linear generators, regular
expansion, proper cubic covariance, generically invertible TT kinetic block and exact mixed
lapse normalization. An enlarged carrier may avoid the TT block reduction;
a singular constraint presentation, nonlocal generators or a weaker infrared
closure may avoid other steps. Each is a changed problem needing new analysis.

The appearance of a logarithmic derivative outside the Laurent class resembles
the standard lattice Leibniz obstruction of Kato,Sakamoto,So. Sections2–3 of
arXiv:0810.2360v1 were read: their theorem assumes a specified bilinear field
product, translation invariance, locality and an exact Leibniz rule, with an
infinite-flavor matrix escape. That theorem is context, not the proof of(1)–(4)
or a gravity impossibility input. Here the physical reduction and mixed
constraint identity are derived explicitly; no ordinary Leibniz premise is
silently imposed on shifted/cochain calculus.

A formal D(z)=log(z)I with F=I,A=0 solves(3) on a chosen logarithm branch,
but it is not a single-valued finite Laurent symbol. A central difference
D=(z-z^(-1))I/2 instead has residual(cos k-1)F at z=exp(ik) when F is scalar
and A commutes. This is a precise possible infrared weakening, not exact
closure. No physical source, interacting matter action or native encoding is
supplied by either formal control.

## Singular-symbol stress control

Generic invertibility is load-bearing. The independent exact example
F=diag(1,0), D=[[0,1],[0,0]], A=[[0,1/2],[1/2,0]] satisfies the two
uniform/affine equations with mu0=0,mu1=1. This A is realizable by a lapse-
difference mixed density. It does not have the supplied nondegenerate TT
continuum normalization or prove full arbitrary-lapse closure. It establishes
why replacing generic invertibility with merely nonzero F is invalid.
