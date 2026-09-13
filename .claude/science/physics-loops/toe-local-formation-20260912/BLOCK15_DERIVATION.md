# Uniform low-energy linearization of the nonlinear native star operator

Author derivation,2026-09-13. Written before its finite checks. The supplied
native model, Gaussian reference, all-parity defect gap and positive scalar
are those of PR8086 at7b03ad8d4b160c002f0a0c9bedeba10f8eab02c7. Independent
source review remains pending. The operator statement below is stronger than
a vacuum-vector spectral estimate, but it is still a local free-energy
statement, not control of an extensive interacting Hamiltonian or its phase.

## 1. The actual operator and quantified target

Use the same real Majoranas, nearest-neighbor pi-flux K of strength h>0,
pure Gaussian Fock vacuum Omega and H0=dGamma(omega)>=0. In the doubled
eight-site cell, omega(k)=2h sqrt(sum sin²(k_a/2)), four positive bands.
For every two-leg pair A, let g=gamma0, d_A,j=-K0j on those two neighbors,
B_A=i g gamma(d_A), D_A=H0+B_A>=h/4.

To separate spectral-parameter conventions from the positive shift used in
Block14, define for real zeta<h/4

    mathcal R_A(zeta)=-(D_A-zeta)^-1,
    O(zeta)=(1/8)sum_(A,C disjoint) mathcal R_C(zeta) g mathcal R_A(zeta).

Every one of the90 ordered terms is present. O(zeta) is bounded, Hermitian
and odd: adjunction exchanges A,C, and both resolvents are even. The original
vacuum energy is retained. At zeta=0, chi=O(0)Omega is exactly Block14's vector.
The third-star source derives -i O(zeta) beta_v as the returning singleton
part of the order-u³ energy-dependent Feshbach coefficient; other terms and
the convergence window of the full physical expansion remain separate.

Let P_E=1_(H0<=E). It includes all free particle numbers; no bound on N is
assumed. The new target is a bound on P_E[O(zeta)-alpha g]P_E, uniformly in
|zeta|<=E. Here7<h²alpha<330 is the same real positive scalar as before.
For dimensionless e=E/h, define

    v(E)=integral_(omega(k)<=E) d³k/(2pi)^3,
    t(E)=sqrt(v(E)),
    B=2,030,043,136,
    C=1,117,440,
    A=4C+47,520 pi.

The proposed bound, proved below, is

    ||P_E[O(zeta)-alpha g]P_E||
      <=h^-2 t(E) [A e+2B t(E)²]                         (1.1)

whenever0<e<=2^-21 and|zeta|<=E. In particular the right side is less
than(alpha/2)t(E). In fact(1.1) holds on a larger explicitly stated small
cutoff domain;2^-21 is chosen to make the relative bound immediate.

The compressed linear norm is exactly

    ||P_E alpha g P_E||=alpha t(E).                       (1.2)

Thus the full nonlinear operator approaches its linear part in operator norm
relative to its low-energy size, uniformly over every normalized state in
that free-energy subspace. The relative error is O(E/h). No Gaussianity or
fixed-particle-number condition is imposed on that state.

Both the input and output are projected by P_E. This is a theorem about the
low-energy-to-low-energy block; it does not bound excitation leakage into
the complement of P_E. In particular it does not claim the uncompressed
action [O(zeta)-alpha g]P_E is small.

## 2. A real spectral split and a surviving high-mode defect gap

Initially use a cutoff Lambda>=E. Let Pi_L project the real Majorana
one-particle space onto frequencies omega<=Lambda, Pi_H=1-Pi_L. It commutes
with the Gaussian complex structure. In the doubled cell its Fourier symbol
is simply1_(omega<=Lambda) I8. The graded Fock decomposition therefore has
H0=H_L+H_H and Omega=Omega_L tensor Omega_H, with both vacua even.

Write g=g_H+g_L and gamma(d_A)=d_H+d_L. Each physical site has

    ||gamma(Pi_L e_j)||=t=sqrt(v(Lambda)),
    v(Lambda)<=pi(Lambda/h)³/48.                          (2.1)

This is the real-field norm. It is not the four-band mode count4v. The bound
follows from the same enclosing ball used in Block14, divided by four.
Two selected neighbors give||d_L||<=2h t, while||d_H||<=sqrt2h and||g_H||<=1.

The scalar-in-cell cutoff has no matrix elements between origin internal
label0 and a nearest-neighbor internal label. Hence g_H anticommutes with
d_H, and g_L with d_L. All high fields anticommute with all low fields.
Consequently each term in

    B_A=B_H,A+W1,A+W2,A,
    B_H,A=i g_H d_H,
    W1,A=i(g_H d_L+g_L d_H),
    W2,A=i g_L d_L                                       (2.2)

is Hermitian, with

    ||W1,A||<=4h t,    ||W2,A||<=2h t².                   (2.3)

Take the low-vacuum expectation of the full quadratic-form inequality
D_A>=h/4. H_L and W1 have zero low-vacuum expectation. W2 contributes a
scalar of absolute value at most2h t². Thus on the entire high Fock space

    D_H,A:=H_H+B_H,A >=h/4-2h t².                         (2.4)

For domain precision, first use finite-particle high test vectors and the
low vacuum, then pass to the form closure of H_H; B_H is bounded. This
does not require a high impurity vacuum or positivity of B_H itself.
It avoids subtracting the larger O(t) mixed-term norm from the gap.

## 3. An analytic parity expansion on the whole low Fock space

Let rho=1/128, assume t<=rho/2 and|zeta|<=h/32, and use complex s. Define

    D_A(s,zeta)=D_H,A+H_L-zeta+s W1,A+s² W2,A,
    R_A(s,zeta)=-D_A(s,zeta)^-1,
    g(s)=g_H+s g_L,
    F(s,zeta)=E_H[(1/8)sum R_C(s,zeta) g(s) R_A(s,zeta)],   (3.1)

where E_H is high-vacuum partial expectation. Graded Fock factorization with
the even high vacuum makes E_H a norm-contractive map to low operators.
It is equivalent to compression to the high-vacuum subspace, followed by
the natural identification with the low Fock space.

The common unbounded part D_H+H_L is self-adjoint. By(2.4), for t<=rho
and|zeta|<=h/32 its lower bound after the shift is greater than h/5. On
|s|<=r=rho/t, the bounded perturbation has norm at most

    h(4rho+2rho²)<h/16.

The Neumann series then gives a norm-holomorphic inverse throughout a
neighborhood of that closed disk, with||R_A(s,zeta)||<=8/h. This argument
controls the entire unbounded H_L spectrum; it is not a low-number cutoff.
Consequently

    ||F(s,zeta)||<=720(1+rho)/h²<726/h².                  (3.2)

High parity changes W1 to-W1 and g_H to-g_H, while fixing W2 and g_L.
Its vacuum is invariant, so F(-s,zeta)=-F(s,zeta). The Taylor series of F
therefore has only odd powers. Cauchy's operator-valued coefficient bound
on |s|=r, followed by a convergent geometric sum at s=1, gives

    ||F(1,zeta)-F1(zeta)||
      <=(726/h²) r^-3/(1-r^-2)
      <=(4/3)*726*128³*t³/h²
      =B t³/h²=:T.                                      (3.3)

F1 denotes the coefficient of s. This bounds all powers3,5,... together,
and all input vectors in the low Fock space. The use of complex s is a
mathematical estimate; no complex physical Hamiltonian is proposed.

There is a second analytical check of this tail that does not use Cauchy's
formula. Expand both inverses in a norm-convergent Neumann series about
D_H+H_L-zeta. Assign8/h to each base inverse,4h t to W1 and2h t² to W2.
After taking the high-vacuum expectation, even powers vanish as above.
The remaining coefficient norms are bounded term by term by the positive
power series of

    M(x)=720(1+x)/(1-32x-16x²)².

Its linear coefficient is720*65x. The odd tail divided by x³ is a series
in x² with nonnegative coefficients. On0<=x<=1/256 it is therefore at most
its endpoint value

    [ (M(1/256)-M(-1/256))/2-720*65/256 ]/(1/256)³
      =1622982593539803709440/16028065902833
      <102,000,000<B.                                    (3.4)

This independently recovers the looser bound(3.3). Positivity of the scalar
series follows from expanding(1-32x-16x²)^-2; convergence holds on this
interval since32x+16x²<1. This scalar series is a coefficient majorant,
not a replacement Hamiltonian or an assumed sign of operator coefficients.

## 4. Removing total low energy from the linear coefficient

Put R_A^0(zeta)=-(D_H,A+H_L-zeta)^-1 and bar R_A=-D_H,A^-1.
Differentiation of the inverse gives the exact coefficient

    F1(zeta)=E_H[(1/8)sum_(A,C)[
       R_C^0 g_L R_A^0
      +R_C^0 W1,C R_C^0 g_H R_A^0
      +R_C^0 g_H R_A^0 W1,A R_A^0]].                     (4.1)

All resolvents in this display use the same zeta. Let Lbar be the identical
expression with every R_A^0 replaced by bar R_A. It is a Hermitian linear
low CAR field: each term contains exactly one low field, all remaining
factors belong to the high algebra, and the underlying real-s family is
Hermitian before taking its first derivative. The graded signs are retained
by the displayed operator order.

A low linear field with frequency support<=Lambda maps the H_L spectral
subspace<=E into that<=E+Lambda. This follows directly from its creation
and annihilation energy shifts; every term in(4.1) contains only one such
field. All high factors commute with H_L. On these intermediate subspaces,
the resolvent identity gives

    ||(R_A^0(zeta)-bar R_A)1_(H_L<=E+Lambda)||
        <=(E+Lambda+|zeta|)(8/h)².                       (4.2)

Telescoping the two or three inverses in each term of(4.1), using(2.3),
therefore proves

    ||[F1(zeta)-Lbar]1_(H_L<=E)||
      <=(90/8)t(E+Lambda+|zeta|)
                    [2(8/h)³+24h(8/h)^4]
      =C t(E+Lambda+|zeta|)/h³.                          (4.3)

Here2 comes from the two inverses around g_L;24 comes from two placements,
three inverses and the4h t bound on W1. There is no factor proportional to
the number of soft particles or system volume.

## 5. Calibration to the exact vacuum amplitude without assuming linearity

Let f_L=P_(N=1)1_(omega<=Lambda)chi be the actual low one-particle vector
of O(0)Omega. Define the Hermitian low field L_Lambda=a†(f_L)+a(f_L), with
the annihilation convention chosen so L_Lambda Omega_L=f_L. Its norm is
||f_L||. The map from a Hermitian linear field to its vacuum vector is an
isometry and is one-to-one; this follows from the CAR square
[a†(f)+a(f)]²=||f||²I. It is not an identity for general odd operators.

The one-particle projection of F(1,0)Omega_L is precisely f_L. Indeed the
high-vacuum compression removes all high excitations and leaves exactly
the low part of chi. Applying(3.3) and(4.3) at E=0,zeta=0 gives

    ||L_Lambda-Lbar||<=T+C t Lambda/h³.                   (5.1)

Because Lambda>=E, P_E has no occupied high mode: a single high frequency
is strictly greater than Lambda. Thus P_E O(zeta)P_E is exactly the
compression of F(1,zeta) to total low energy<=E. Combining(3.3),(4.3),(5.1),

    ||P_E[O(zeta)-L_Lambda]P_E||
      <=2T+C t(E+2Lambda+|zeta|)/h³.                      (5.2)

This is the step that upgrades a vacuum calibration to an operator estimate.
No equality O=L_Lambda on high-energy states has been used.

## 6. The positive native coefficient and explicit energy window

Block14's direct native node proof gives, for each k, a four-band amplitude
remainder from alpha gamma0 bounded by95,040|k|/h². The low sublevel set
has|k|<=pi Lambda/(2h). Its cell measure is v(Lambda)=t², hence the same
linear-field isometry yields

    ||L_Lambda-alpha g_L||<=47,520 pi*t Lambda/h³.         (6.1)

Set Lambda=E and assume|zeta|<=E. On P_E, g and g_L have identical
compression. Equations(5.2),(6.1) give exactly(1.1), with
A=4C+47,520pi and t²<=pi e³/48.

For0<e<=2^-21, the preliminary conditions t<=rho/2 and|zeta|<=h/32 hold.
Using pi<22/7, exact rational inequalities show

    A e+2B t²
      <=[4C+47,520(22/7)]e+[B(22/7)/24]e³ <7/2.          (6.2)

Since h²alpha>7, this proves the stated relative error below1/2.
The constants are coarse analytical bounds, not a fitted physical scale.
For the stronger zeta=0-only conclusion one may replace4C by3C; no such
optimization is needed for the uniform spectral-parameter theorem.

For(1.2), the upper bound is||g_L||=t. The normalized low one-particle
vector g_L Omega/t has free spectral support<=E. Together with the vacuum
it forms a two-dimensional invariant subspace of g_L on which g_L has
norm t, by its CAR square. Both vectors lie in Ran P_E. Therefore the
upper bound is attained after compression. It follows that

    (alpha/2)t(E)<||P_E O(zeta)P_E||<(3alpha/2)t(E),
    ||P_E O(zeta)P_E||/(alpha t(E))=1+O(E/h)               (6.3)

uniformly for|zeta|<=E as E→0. Since
v(E)=E³/(6pi²h³)+O(E^5) at fixed h,

    ||P_E O(zeta)P_E||
       =alpha E^(3/2)/(sqrt6 pi h^(3/2))+O(E^(5/2)).      (6.4)

The origin vacuum transition asymptotically attains the leading low-energy
operator size. Physical total parity can be preserved by including the
spectator Majorana in the even vertex-i O beta; the active odd operator
norm here allows both active parities as in the parent's gap theorem.

## 7. Boundaries and remaining interacting question

At E=0 the active spectral subspace is just the vacuum because omega>0
almost everywhere; both odd compressions vanish. No assertion about a
normalizable node state is required. The theorem is for h>0, the specified
Gaussian reference, the given defect family and the exact90-term O(zeta).
A different bath, state, cutoff or unbounded perturbation needs new bounds.

The full-operator L4 filled-state counterexample in the third-star source
remains valid: it lies outside this small free-energy domain. The present
proof does not replace O globally by a quadratic Majorana field. It bounds
one actual local vertex uniformly over low-energy states, including states
with arbitrarily many sufficiently soft particles.

The result does not bound the extensive sum over centers by its local
error, nor does it show that the interacting ground state lies in Ran P_E
of the original free reference. Both would be additional, substantial
arguments. Transitions out of this energy window must also be controlled
in a physical elimination or renormalization argument. Higher electric
coefficients, flux-sector stability at fixed
coupling, the full Feshbach energy dependence and the physical selection of
the Hamiltonian remain open. The simple two-channel hybridization spectrum
was already in the source and is not a consequence newly asserted here.

No axiom, primitive, occurrence law or physical clock is introduced. The
result is proposed conditional mathematical support for a joint treatment
of active and spectator degrees of freedom. It is neither an axiom wall
nor an interacting-phase theorem.

## Author verification status

The initial31 finite checks pass. A separately assembled seven-complex-mode
CAR comparator has three low and four high modes, an explicit positive
scalar defect shift, and orthonormal center/six-leg fields. It checks the
graded split, nonzero low-vacuum W2 scalar, parity of the analytic family,
the first coefficient against direct inverses, the complete soft-Fock tail,
linear-field reconstruction/isometry and the low-energy support margin.
Its operator comparison includes an input with three occupied low modes;
the unrestricted high-energy replacement still fails. It is not a native
finite-size estimate or a fit to the E^(5/2) power. The native constants are
checked separately with exact rational arithmetic. The uniform relative
error upper bound at the stated window is about0.314652, below1/2.

The subsequent exact Neumann-tail check in(3.4) supplies a different
analytical derivation of the cubic remainder estimate. Final checks and
the complete cold author review are recorded separately. All work is by
the same author; independent source review remains pending. No physical
phase or axiom conclusion is promoted by these finite checks.
