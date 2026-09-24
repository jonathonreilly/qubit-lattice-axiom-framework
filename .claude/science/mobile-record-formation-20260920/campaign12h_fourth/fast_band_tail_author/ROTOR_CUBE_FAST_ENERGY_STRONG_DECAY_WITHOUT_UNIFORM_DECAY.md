# Rotor cube fast energy: strong decay without uniform decay

This is a conditional theorem in the supplied original compensated cube model.
It addresses the limit of the already derived fast-time semigroup as its time
parameter tends to infinity. It is not a fixed-positive-physical-time joint
spin/scale theorem. The finite-spin microscopic model, preparation, compensation
and original formation marks are unchanged. No physical bath, naturally selected
law, axiom, empirical prediction or audit status is supplied by this result.

## 1. Statement and the order of limits

Let A=(0,3,5,6), B=(1,2,4,7), with an A-to-B edge exactly when the two binary
cube vertices differ in one bit. Work in the rotor physical Gauss space with
total matter charge four and matter population N=6. Let Pi1 project onto one
empty A site. F is the original outward signed charge transport with unitary
integer-flux shifts, and j are the original resolved or coherent birth marks.
For positive delta and kappa set

    G = Pi1(FF* - F*F)Pi1,
    Gamma = Pi1 sum_j j*j Pi1,
    V(tau) = exp[tau(-i delta G - kappa Gamma/2)].

The two instruments have the same Gamma; their marked channels are not
identified. For every normalizable physical r in this N=6, W=1 sector,

    ||V(tau)r|| -> 0                 as tau -> infinity.                 (1)

Nevertheless, for every finite nonnegative tau,

    ||V(tau)|| = 1.                                                     (2)

Thus there is strong decay for each fixed vector, with no decay in operator
norm and no state-uniform rate tending to zero. A perfectly sharp flat Fourier
phase has a dark vector, but it is not a normalizable physical field state.

For the actual zero-field first-output high coefficient r_i=R_i/sqrt(b_i),
the preceding compact-fast-time theorem gives

    lim_joint epsilon^2 E_i(epsilon^2 tau)/delta
       = f_i(tau) = ||V(tau)r_i||^2.

Here the joint limit has epsilon^2 S(S+1)=delta/K, with tau fixed. Conditional
on that preceding theorem, (1) implies the sequential limit

    lim_(tau->infinity) lim_joint
       epsilon^2 E_i(epsilon^2 tau)/delta = 0.                           (3)

Equation (3) does not interchange the limits and does not permit tau=t/epsilon^2
inside the compact-time estimate. The fixed positive laboratory-time energy
and any finite-spin infinite-time limit remain separate open questions.

## 2. Complete physical charge and cycle representation

Population six and total charge four mean five positive and one negative matter
charges, with two vacancies. There are 168 charge words. Their W=0,1,2 counts
are respectively 36,96,36. In W=1 one vacancy lies in A and one in B. The birth
loss is two if these vacancies are adjacent and zero if they are opposite:

    Gamma = 2 P_bright,
    dim(charge bright) = 72,     dim(charge dark) = 24.                  (4)

Each allowed birth sign has unit rotor amplitude. On a fixed empty edge the
two signs have orthogonal output charges, so the coherent cross term vanishes
in j*j. Equation (4) therefore holds for both original instruments.

Use edge order

    01,02,04,31,32,37,51,54,57,62,64,67.

Choose spanning-tree edge indices (1,2,3,4,6,9,11), or
(02,04,31,32,51,62,67). The five chord indices are (0,5,7,8,10).
For each charge word q, the integer Gauss equations div(E)=q-1_A have a unique
tree-supported reference field E0(q). Removing one row from the incidence
matrix of the tree gives determinant of magnitude one. Consequently all
physical electric words have the unique form

    E = E0(q) + C_cycle n,       n in Z^5,                              (5)

where C_cycle has identity chord block and zero divergence. The exact runner
constructs the integer cycle matrix and checks (5) under every legal inward
and outward hop of every charge word. This is a coordinate representation of
the full physical field space, not a truncation or a Fourier-fiber state.

Taking the unitary Fourier transform of n identifies the W=1 physical Hilbert
space with L2(T^5; C^96), with normalized Haar measure. An outward charge-s
hop along a tree edge has phase one; along chord e it has phase z_e^(-s).
The adjoint inward hop has the conjugate phase. Thus G becomes a 96 by96
Hermitian Laurent-polynomial matrix G(z), and Gamma is the constant matrix (4).
The representation contains every legal Gauss word. Parseval gives

    ||r||^2 = integral_T5 ||r_hat(z)||^2 dz,
    ||V(tau)r||^2 = integral_T5 ||exp[tau L(z)]r_hat(z)||^2 dz,
    L(z) = -i delta G(z) - kappa Gamma/2.                               (6)

All operators are bounded: each elementary rotor shift has norm one and only
finitely many edges occur. Their finite fibers depend continuously on z.

## 3. Exact coupling out of the dark charge space

Write Q(z)=P_bright G(z)P_dark. Direct ordered two-hop paths yield

    P_dark G(z)P_dark = 0                                           (7)

identically as a Laurent polynomial. A path changing both vacancies uses
disjoint hops and cancels between FF* and F*F. A path changing only one vacancy
ends in the bright space. On a diagonal dark word the three possible returns
through W=0 and the three through W=2 cancel. All return amplitudes have modulus
one. The exact runner also checks (7) by collecting complete signed Laurent
monomials, before evaluating phases.

For completeness, an explicit exact rank witness uses z_01=-1 and all other
chord phases one. Enumerate occupied sets in lexicographic order, and within
each six-element occupied set enumerate the position of its negative charge.
Retain this ordering on the dark and bright sublists. At this phase Q is an
integer 72 by24 matrix. Its Gram determinant is exactly

    det(Q^T Q) = 4688333314034185078308864 > 0.                          (8)

An even smaller certificate takes all24 columns and bright rows

    0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,24,42.

The determinant of this 24 by24 minor is exactly -768. The full ordered charge
lists, every nonzero Laurent monomial, the witness matrix, Gram matrix and
minor row list are in EXACT_TAIL_RESULTS.json. The self-contained integer
runner constructs them from the original local charge hops. These are exact
finite algebra certificates, not floating singular-value thresholds.

The determinant of this minor is a nonzero Laurent polynomial p(z). Its zero
set on T^5 has Haar measure zero: multiply by a monomial to remove negative
powers; in one variable a nonzero polynomial has finitely many zeros; iterating
this statement with Fubini proves the multivariable claim, separating the
measure-zero set where all coefficients of the final variable vanish.
Therefore Q(z) has full column rank for almost every physical cycle phase.

## 4. Fiber stability and the strong limit

Each fiber semigroup is a contraction because

    d/dtau ||exp[tau L(z)]v||^2
       = -kappa <exp[tau L(z)]v,Gamma exp[tau L(z)]v> <= 0.             (9)

If L(z)v=i omega v for nonzero v, the real part of the eigenvalue identity
forces Gamma v=0. The bright component of the same equation is then
-i delta Q(z)v=0. Full column rank of Q(z), with delta>0, makes this impossible.
All eigenvalues have strictly negative real part for almost every z. In each
such finite fiber its matrix exponential tends to zero; Jordan blocks do not
change this conclusion.

For a normalizable physical input, the integrand in (6) tends to zero almost
everywhere and is bounded by the integrable function ||r_hat(z)||^2. Dominated
convergence proves (1). No spectral gap uniform in z and no exchange of limits
is used. Equation (4) also gives the useful finite-time lower bound

    exp(-2 kappa tau)||r||^2 <= ||V(tau)r||^2 <= ||r||^2.              (10)

The energy contribution remains strictly positive at every finite fast time
for nonzero r, while tending to zero as that fast time tends to infinity.

## 5. The exceptional flat phase and lack of uniform decay

At z=(1,1,1,1,1), exact rational elimination gives rank(Q)=23. The vector with
one on every dark charge word lies in its kernel. Let u be this vector divided
by sqrt(24), extended by zero on bright words. Equations (4) and (7) give

    G(1)u=Gamma u=L(1)u=L(1)*u=0.

The zero mode is one-dimensional. Any imaginary-axis eigenvector must lie in
the dark kernel, and (7) makes its eigenvalue zero. The orthogonal complement
is invariant and its finite matrix exponential decays. Thus for this one
fiber the long-time limit is the orthogonal projection onto u.

The actual first-mark high vectors at flat phase have limiting squared norms
1/12 for the resolved plus mark, 1/12 for the resolved minus mark, and1/6 for
the coherent mark. Their full initial norms squared are respectively2,1,3/2.
The exact runner reconstructs their physical charge/field path words and these
overlaps; it does not replace the physical initial state by the flat fiber.

For every fixed finite tau, continuity in z and exp[tau L(1)]u=u produce a
positive-measure neighborhood on which the fiber norm is arbitrarily close
to one. Equivalently, normalized physical Fourier wave packets concentrated
in these neighborhoods have norm ratios arbitrarily close to one. The
contraction upper bound then proves (2). These wave packets are legitimate
Gauss states via (5), but their neighborhood depends on the requested accuracy
and tau. They are not a single fixed nondecaying normalizable state.

The flat-phase witness therefore prevents a uniform rate over all inputs; its
measure-zero support does not invalidate strong decay of each fixed input.
No decay rate for the actual finite-word first output is derived here.

## 6. Limits, provenance and checks

The exact charge-sector, integer Gauss-coordinate, Laurent cancellation, rank
witness and exceptional flat-phase calculations are independent of epsilon
and finite-spin truncation. The compact-time microscopic interpretation is an
explicit prior dependency, whose separate independent comparison is pending
at this author seal. This note does not convert strong rotor decay into a
fixed-time finite-spin theorem, a field-only theory, or an energy-supply model.

The numerical exploratory ranks suggested the exact route but are not proof.
The first exact control failed before evaluating a determinant because Python
negative powers of -1 introduced floats, and a structural integer comparison
rejected them. Its source and raw logs are preserved. The corrected control
uses exact integer parity from the outset and requires integer entries. No
failed physical case, matrix entry or tolerance was removed or relaxed.

The present claim is a personal root candidate awaiting a separately sealed
independent PRE and released-source comparison. No author result was sent to
that checker before its PRE. No repository merge or audit verdict is made.
