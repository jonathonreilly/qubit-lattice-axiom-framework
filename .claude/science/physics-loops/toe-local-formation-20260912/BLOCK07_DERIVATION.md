# Exact Regge reduction, source transport and static scalar readouts

Author derivation, 2026-09-13. Conditional on the supplied unit 4D path
triangulation and length Regge action. No independent review or physical
gravity claim. The corrected main spectrum and static-source notes are the
repository targets; their original finite diagnostics are preserved.

## 1. Object and prior art

The complex consists of all 24 ordered coordinate paths in each unit 4-cube.
Its action is S_R=sum_t A_t delta_t, with positive Euclidean simplex lengths.
At the flat background each nonempty coordinate subset A labels an edge of
length sqrt(|A|). Write q_A=delta(length_A squared); then
q_A=2sqrt(|A|)delta l_A at first order. All Hessians below are with respect to
q, and q(-k)^T Q(k)q(k) is the second variation, not the quadratic Taylor term
(which has an additional factor 1/2). No continuum limit is used in this identity.

The length-Regge reduction to ten metric coordinates, four body variables and
a decoupled hyperdiagonal is established prior art. The relevant primary
sections read are Bahr–Dittrich–He, [arXiv:1011.3667v2](https://arxiv.org/html/1011.3667v2),
section 6.1 and appendix A, and Dittrich,
[arXiv:2105.10808](https://arxiv.org/pdf/2105.10808), section IV.B.5.
The present derivation reconstructs the exact coefficients in this repository's
normalization and uses the resulting map to settle its static source/readout
questions. It does not claim discovery of linearized lattice gravity.

## 2. A rational local Hessian from geometry

In the reference simplex let X_j=e_1+...+e_j for j=0,...,4. The barycentric
normal vectors are

n_0=-e_1, n_1=e_1-e_2, n_2=e_2-e_3, n_3=e_3-e_4, n_4=e_4.

They sum to zero. Let h be its infinitesimal metric in this orthonormal
coordinate frame. For the hinge opposite vertices i,j set

a=n_i.n_i, b=n_i.n_j, c=n_j.n_j,
N=(n_i,n_j), P=I-N(N^T N)^(-1)N^T.

P projects onto the two-dimensional hinge plane. The flat simplex volume is
1/24, and its hinge area is A=sqrt(ac-b^2)/2. The interior angle obeys
cos(theta)=-b/sqrt(ac). Differentiating the inverse metric in this formula gives

A delta theta = -1/2 [n_i^T h n_j
             - b/2 (n_i^T h n_i/a+n_j^T h n_j/c)].                 (2.1)

Also delta A/A=tr(P h)/2. These are ordinary first derivatives at a nondegenerate
Euclidean simplex; no numerical angle derivative is used. Summing (2.1) over
all missing pairs gives zero: sum_(j != i)n_i.n_j=-a and sum_i n_i=0 cancel
the two terms. This is the needed Schlaefli identity directly in these variables.
It removes area-times-second-angle terms from the global flat second variation.
Consequently each simplex contributes

1/4 sum_(i<j) tr(P_ij h)
  [n_i^T h n_j - (b_ij/2)(n_i^T h n_i/a_i+n_j^T h n_j/a_j)].      (2.2)

For the ten squared-edge variations q_ij, with q_ii=0,

h_aa=q_(a-1,a),
h_ab=(q_(a,b-1)+q_(a-1,b)-q_(a,b)-q_(a-1,b-1))/2, a<b.         (2.3)

The local quadratic matrix in edge order
01,02,03,04,12,13,14,23,24,34 is exactly 1/48 times

```text
 0  0  0  0  0  3  0 -6  0  0
 0 -3  3  0  6 -6  0  3  0  0
 0  3 -2  0 -6  3  0  0  0  0
 0  0  0  0  0  0  0  0  0  0
 0  6 -6  0 -6  6  0  0  3 -6
 3 -6  3  0  6 -6  3  6 -6  3
 0  0  0  0  0  3 -2 -6  3  0
-6  3  0  0  0  6 -6 -6  6  0
 0  0  0  0  3 -6  3  6 -3  0
 0  0  0  0 -6  3  0  0  0  0
```

This table is obtained by substitution into (2.2), not by fitting the old
Hessian. Its zero 04 row also explains the hyperdiagonal zero before Fourier
transformation. For a permutation sigma, local edge ij maps to class
A={sigma_(i+1),...,sigma_j} at anchor {sigma_1,...,sigma_i}. Its Fourier
multiplier is z_anchor. Thus the global Q is the sum of 24 translated copies
of this displayed rational table. This is an explicit finite Laurent formula.

## 3. Exact body elimination and the correct metric coordinates

Put z_a=exp(i k_a), w_a=exp(i k_a/2), p_a=2sin(k_a/2), Delta=sum_a p_a^2.
For each triple A={a,b,c}, define

r_A=q_A - 1/2 sum_(ij subset A)(1+z_(A minus ij))q_ij
          + 1/2 sum_(i in A)(z_j+z_k)q_i.                       (3.1)

Let C be this four-row map. Define ten symmetric metric coordinates by

h_aa=q_a, h_ab=(q_ab-q_a-q_b)/2,
H_aa=h_aa, H_ab=h_ab/(w_a w_b), a!=b.                          (3.2)

The change from (q_axis,q_face,q_body,q_hyper) to (H,r,q_hyper) is invertible
for every finite complex k: the nonzero phases and the diagonal body coefficients
never require a Laplacian inverse. H is a discrete metric coordinate, not the
old line-integrated continuum metric field. The latter map is unchanged.

Collecting the 24 local tables gives

q(-k)^T Q(k)q(k) = -1/4 F_p(H(-k),H(k))
                         -1/2 sum_A r_A(-k)r_A(k),             (3.3)

where, for symmetric matrices U,V,

F_p(U,V)=Delta tr(U V)-2(Up).(Vp)
        +tr(U) p^T V p+tr(V) p^T U p-Delta tr(U)tr(V).          (3.4)

The p here belongs to k on both sides of (3.4); p(-k)=-p(k), while H(-k)
is the corresponding reversed-phase coordinate. For real k the minus-k field
is the complex conjugate field. For complex k use the bilinear analytic
continuation, not a Hermitian conjugate.

One compact coefficient verification of (3.3) is as follows. The body rows of
the table sum to -C/2, their four-by-four block is -I/2, and the hyperdiagonal
row is zero. After their Schur elimination and the phase change (3.2), the
remaining symmetric-component entries have these seven types. Distinct letters
below are distinct coordinate directions; the off-diagonal component has both
symmetric matrix entries equal to one, without a sqrt(2) normalization.

| Entries | Reduced coefficient |
|---|---|
| aa,aa | 0 |
| aa,bb | (Delta-p_a^2-p_b^2)/4 |
| aa,ab | 0 |
| aa,bc | -p_b p_c/2 |
| ab,ab | -(Delta-p_a^2-p_b^2)/2 |
| ab,ac | p_b p_c/2 |
| ab,cd | 0 |

Coordinate permutations and bilinear symmetry exhaust the ten-component matrix.
These are exactly the entries of -(3.4)/4. The local rational table and the
explicit anchor rule make each cancellation inspectable. The separate exact
checker expands all 225 Laurent entries and rejects any nonzero coefficient;
this verifies the stated algebra rather than extrapolating from sample momenta.

## 4. Gauge, rank and the continued dispersion

A vertex displacement xi changes q_A by

G_A xi=2(z_A-1)sum_(a in A)xi_a.

Substitution into (3.1) gives r_A=0. For each xi_a coefficient the two face
terms leave (1-z_a)(z_b+z_c), cancelled by the axis term. With u_a=w_a xi_a,
(3.2) gives H=i(p u^T+u p^T). Formula (3.4) annihilates this family directly.
The hyperdiagonal gives a fifth independent null direction at nonzero real k.

For Delta!=0, project transverse to p. Every symmetric H is a sum of a gauge
field and a transverse symmetric tensor. On the latter, the operator of F is
Delta(H-Pi tr H), Pi=I-pp^T/Delta. In four dimensions its five-dimensional
transverse traceless subspace has eigenvalue Delta and its transverse trace
has eigenvalue -2Delta. The remaining four modes are gauge. Hence the reduced
rank is six, the full rank is ten and the full nullity is five. For real k
this holds at every nonzero torus momentum, including Nyquist momenta.
At p=0 the reduced matrix vanishes, leaving full rank four and nullity eleven.

At a nonzero complex null vector p with Delta=0, the equation F(H)=0 is

H p=(tr H/2)p.                                                (4.1)

To derive it, the trace first gives p^T H p=0; the remaining dyadic equation
then forces (4.1). The map H -> H p-(tr H/2)p has rank four: choose a null q
with p.q=1 and two independent transverse vectors; q q^T, q e^T+e q^T, and I
produce four independent images. Its kernel is therefore six-dimensional.
It consists of the four gauge directions and two transverse traceless classes
in the two-dimensional transverse quotient. The full Q has rank eight and
nullity seven. This is an algebraic quotient count, not yet a reconstructed
physical Hilbert space or a positive graviton-residue theorem.

With real spatial k and k_t=i omega, omega real positive,

Delta=sum_i 4sin^2(k_i/2)-4sinh^2(omega/2).

Its derivative in omega is -2sinh(omega)<0. Therefore for every nonzero spatial
momentum modulo 2pi there is exactly one positive zero,

4sinh^2(omega/2)=sum_i 4sin^2(k_i/2).                          (4.2)

All other finite positive frequencies have nullity five, and that zero has
nullity seven. The invertible coordinate change and constant body block rule
out additional finite-frequency rank drops in this declared continuation.
At zero spatial momentum the zero is omega=0 and belongs to the different
rank-four origin. No claim is made about a nonlinear spectrum, transfer matrix,
OS reconstruction, physical time, or other actions/triangulations.

## 5. Transport a source through the same action

In the variables (H,r,q_hyper), choose a source which couples only to H, through
the same bilinear pairing. Its q-covector J is defined by
q(-k)^T J(k)=tr(H(-k)T(k)). In ten independent symmetric components,
J=E(-k)^T t, where E is (3.2), t_aa=T_aa and t_ab=2T_ab for a<b.
The off-diagonal factor is part of the Frobenius pairing. This is an explicit source lift; it is not selected by the axioms. At real
nonzero k, p^T T=0 is the gauge compatibility condition. The body equations give
r=0. The metric equation is the reduced equation from (3.4), and the source
has no hyperdiagonal component. Thus every such conserved source lies in the
range of the full Hessian. Its solution is unique modulo the complete kernel.

For transverse T a convenient representative is

H = -4/Delta [T-(1/2)Pi tr T].                               (5.1)

Adding a gauge tensor or an arbitrary hyperdiagonal leaves the sourced equation
unchanged. The inverse response of two compatible sources follows by contraction
with the same (5.1), so it is reciprocal with common normalization. A physical
matter action must still derive T and its conservation; a label called energy
or a supplied external potential alone does not do so.

## 6. Exact static endpoint-mean solution and genuine scalar readouts

Now k_t=0 and spatial Delta>0. Let the optional endpoint-mean ansatz of the
corrected main static note be expressed in squared edges:

q_A=(n_t(A)-n_s(A))(1+z_A)Phi.                               (6.1)

Substituting into every triple (3.1) gives r=0. For a purely spatial triple,
the single and pair monomials cancel separately, as do the constant and triple
monomials. For a triple with t, use z_t=1; the residual is
(1+z_i z_j)-(1+z_i)(1+z_j)+(z_i+z_j)=0.

Its H differs from diag(-2Phi,-2Phi,-2Phi,+2Phi) by the exact gauge tensor
i(pu^T+up^T), with u_i=-w_i Phi/2 and u_t=Phi/2. For example the off-diagonal
spatial entry is Phi(w_i/w_j+w_j/w_i-2w_i w_j)/2, precisely the corresponding
gauge entry; H_it=i p_i Phi/2. Therefore (3.4) gives the identity

Q_q q = -Delta Phi e_t,
Q_l delta l = -2Delta Phi e_t = 2 Delta_lat Phi e_t.          (6.2)

This proves the current main note's sampled source identity for every static
momentum, hence every finite periodic lattice where this path complex is well
defined. One may periodize the local stencil; usual simple-box geometry uses
periods at least three. At k=0 the equation is zero for every constant Phi.
A periodic source must have its constant mode removed, or an explicitly
specified compensating background; the proof does not bypass that requirement.

For Q_l delta l=8pi G P0 rho e_t, (6.2) gives
Phi=-4pi G (-Delta_lat)^(-1)P0 rho. The sign agrees with the corrected bridge.
No Newton constant or physical mass identification is derived.

Define readouts directly from the reduced coordinates,

Phi_inv=H_tt/2,
Psi_inv=-1/4 sum_(ij spatial)(delta_ij-p_i p_j/Delta)H_ij.     (6.3)

At static momentum every gauge tensor has zero tt component and zero projected
spatial trace. These readouts also ignore the independent hyperdiagonal, so
they are invariant under the COMPLETE kernel of Q. On (6.1) both equal Phi;
they therefore equal Phi on every solution of the same sourced equation,
including its pseudoinverse representative. They use (3.2), not pinv(M_AM),
and do not restore the old noninvariant readout routine.

Although half-phase coordinates change signs across a Brillouin-zone seam,
the scalar readouts are periodic: each p_i p_j H_ij is a Laurent expression
in z_i,z_j times q-components, and diagonal p_i^2 is periodic. Their inverse
Laplacian makes the scalar readout spatially nonlocal. No local Record readout
or physical metric/formation-rate interpretation follows automatically.

## 7. Exact exponent condition within the supplied scalar family

For the broader ansatz q_A=(n_t-nu n_s)(1+z_A)Phi, the body variables still
vanish. Its H is gauge-equivalent to diag(-2nu Phi,-2nu Phi,-2nu Phi,2Phi):
use u_i=-nu w_i Phi/2 and u_t=Phi/2. Applying (3.4) gives

T_tt=-nu Delta Phi,
T_ij=(1-nu)Phi(Delta delta_ij-p_i p_j)/2,
T_it=0.                                                       (7.1)

Since the spatial projector has rank two for every real static nonzero
momentum, absence of spatial stress at any mode with Phi nonzero forces nu=1.
Conversely nu=1 supplies zero spatial stress and (6.2). This holds on the
whole nonzero static domain, not just the four original tested momenta.
A constant field, a zero field or a supplied balancing spatial stress does not
select nu. The conditional theorem does not select a physical ruler law or
justify treating generic moving matter as a pressure-free source.

## 8. Checks and status

The analytical route and candidate formulas were recorded in BLOCK07_WORKING_PLAN
before the new comparison. The exact checker reconstructs the rational local
normal/area identity and all 24 anchored simplices. Every one of 225 Laurent
entry differences vanishes identically. It also checks Schlaefli, gauge,
constant body block, full body rows and the zero hyperdiagonal, and rejects
removed body terms, reversed action orientation and a missing metric phase.
The maximal global entry has four Laurent terms; this is a small fixed
coefficient identity, not a numerical search over momentum or lattice size.

A separate four-point floating comparison uses the existing area/angle
implementation, with maximum full residual below 7e-16. Its first separate
body-row comparison used a reversed row order and reported 1/2; the correctly
indexed full matrices already agreed. The first source/JSON are preserved;
aligning the body-row order gives residual below 3e-16 without changing the
mathematical candidate. This is a checker correction, not a discarded physical
counterexample.

The consequence checker passed 32 named exact checks in 23.98 seconds.
These include full Laurent exponent/source identities, scalar gauge and seam
invariance, five finite exact rank fixtures, a separately built symmetric-tensor
operator, inverse-source normalization and off-diagonal source multiplicity.
Its finite full ranks are 4 at the origin, 10 at two real static fixtures,
8 at an exact complex shell and 10 off shell. The complete symbolic static
identities have no momentum sampling. The first fixed run passed.

All new work is same-author. A separate cold proof pass and independent
review remain pending. Formal retention is not claimed. Physical source selection,
Record formation, a clock, Lorentzian positivity and nonlinear constraint
closure remain open. No axiom or primitive has been changed.
