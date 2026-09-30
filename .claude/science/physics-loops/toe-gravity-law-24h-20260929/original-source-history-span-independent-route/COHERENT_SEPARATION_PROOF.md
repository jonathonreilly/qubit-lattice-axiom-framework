# Actual coherent winding separation and a first-hop range subspace

This analytic supplement uses the frozen actual-history proof10eb8ccd,
the complete winding proof633126b7 and its focused receiptc9d99fc4. It
does not edit them. The result is more than diagonal support, but remains
a restricted separation result. No scientific computation was performed.

## 1. One fixed physical construction throughout

Fix the same even periodic cubic lattice, L divisible by4, L>=8, and
n=L^3/2. Fix4<=b<=n/4. Use exactly the dark preparation variant in winding
proof section2: the first birth at a0=(0,0,0), the two specified y-grid
births, the specified z birth and any allowed fixed remaining grid births.
Their original label string is fixed. It is either resolved with the stated
signs, or the original unnormalized coherent edge instrument. Let

    Phi_b=b_mu_b ... b_mu_1 Omega.                         (1)

This is the COMPLETE original word, not its selected physical component.
It has nonnegative coefficients and finite electric support ||E||_1<=2b.
The checked selected word chi_b has coefficient at least1 in it. All
subsequent products below also retain complete operators and all signs
inside the original coherent labels.

Write L_b=-iKD_b+i delta Q_b-(kappa/2)R_b for the actual no-event generator
on the fixed H_b sector. This avoids confusing it with the first-hop map.
Q has electric l1 displacement at most4 and nonnegative real matrix
entries; R has displacement at most2 and nonnegative entries; D is
diagonal. These are the actual full operators, not selected words. Let
S_b(t)=exp(tL_b).

The closed actual input history span is C_b from frozen proof section2.
Taking all preliminary gaps to zero strongly shows Phi_b in C_b. Its
positive final-gap orbit S_b(t)Phi_b is in C_b as well. The finite-field
vector Phi_b lies in every fixed generator-power domain. In particular,
the weighted-domain estimates in winding proof section5 justify every
fixed derivative at t=0. Therefore, for any bounded output map Z,

    Z L_b^m Phi_b in closure(Z C_b),       m=0,1,... .       (2)

Indeed the m-th forward finite difference of ZS_b(t)Phi_b is in the
closed span on the right, and converges strongly to that derivative.
Only membership (2) is used; no claim that Taylor words span the whole
semigroup orbit, and no convergence of an infinite Taylor series, is made.

## 2. The complete source matrix is triangular

Fix h=c0=(4,2,0), the original source edge h->h+e_z with the same resolved
sign or complete coherent label, and T=-F_h j_mu F_h P_(W=0). The checked
physical source words Xi_w=Xi_(b,w), w>=1, have one fixed matter word,
the actual h vacancy, all six neighboring B sites occupied, and

    E(Xi_w)=E_prep+w C_x+E_source,
    ||E(Xi_w)||_1=2b+3+wL.                              (3)

They are normalized mutually orthogonal physical words. Every Xi_w is in
the actual fast-loss kernel because its whole star is occupied. This is
not a statement that its fast Hamiltonian orbit stays there.

Let m_j=jL/4 and v_j=T L_b^(m_j)Phi_b. Each is a finite-field vector and
belongs to closure(T C_b) by (2). Field bandwidth bounds the support of
v_j by2b+3+4m_j. Consequently

    <Xi_w,v_j>=0                       whenever w>j.       (4)

At w=j, attaining the maximum in (3) forces every generator factor to
be i delta Q. Any R factor loses at least two electric-band units; any
D factor loses four. Hence the COMPLETE coefficient is exactly

    <Xi_j,v_j>=-(i delta)^(m_j) a_j,
    a_j=<Xi_j,F_h j_mu F_h Q_b^(m_j)Phi_b> >= 2^(m_j).    (5)

The inequality uses the checked legal sequence of m_j four-hop Q terms,
each with coefficient2, followed by the actual three-hop source path.
All other contributions to a_j are nonnegative, including all original
coherent branches. Thus (5) is an equality for the full first possible
coefficient followed by a lower bound on its positive real factor, not
an inference of a full amplitude from an isolated path.

Put X=closure span{Xi_w:w>=1}, with orthogonal projection P_X. Equations
(4)-(5) imply that P_X v_j is a linear combination of Xi_1,...,Xi_j with
nonzero coefficient of Xi_j. Induction in this finite triangular system
therefore gives

    span{P_X v_1,...,P_X v_j}=span{Xi_1,...,Xi_j},
    closure(P_X T C_b)=X.                               (6)

Equivalently, no nonzero eta in X annihilates all actual source histories.
This includes every square-summable superposition eta=sum_w c_w Xi_w,
not merely basis tests: pairing first with v_1 gives c_1=0, pairing with
v_2 then gives c_2=0, and so on. At each step the sum is finite by (4).
No exchange of an infinite coefficient sum and an infinite derivative
series occurs.

## 3. Positive integrated operator and exact limits

For any nonempty bounded open I subset(0,infinity), let

    Sigma_T(I)=int_I T rho_b(s)T* ds,
    K_X(I)=P_X Sigma_T(I)P_X restricted to X.             (7)

The actual complete-history expansion and the time-window support theorem
in frozen proof sections2-4 give closure Ran Sigma_T(I)=closure(T C_b).
Alternatively its positive quadratic form vanishes exactly on the
annihilator of those histories. Combining with (6) proves

    <eta,K_X(I)eta> > 0 for every nonzero eta in X.        (8)

Thus K_X(I) is faithful on X and has infinite rank. Sigma_T(I), and also
its actual dark compression, have infinite rank. For the latter, Xi_w is
dark and P_X D_dark=P_X, so its compression to X is exactly (7).

These are TIME-INTEGRATED rank statements. They do not assert infinite
rank or faithfulness at every or almost every individual source time.
For each fixed nonzero eta in X separately, the frozen scalar alternative
does imply <eta,T rho_b(s)T*eta> >0 for almost every s; that exceptional
set can depend on eta. No uncountable intersection is taken. Trace class
also implies that (8) cannot be replaced by a uniform c I_X lower bound
with c>0 on this infinite-dimensional X. No useful quantitative weight,
field moment, tail decay or residence bound is obtained.

## 4. A genuine subspace of the first-hop range

There is a related result inside the precise quotient consumer of frozen
proof section7. Fix the input sector H_b and define

    A_h=(F_h P_(h,3))|H_b,
    M_h=closure Ran A_h,        P_M=projection onto M_h.   (9)

Do not assume that an individual physical output basis vector belongs to
M_h. The first-hop incidence operator can have coherent kernels.

Starting from the same chi_b after w ring circulations, retain only the
first selected outward hop h->h+e_x. Denote the resulting physical word
by Theta_w, now in W1 with NB=2b+1. It has four occupied B sites around h,
not six, and

    E(Theta_w)=E_prep+wC_x+E_first,
    ||E(Theta_w)||_1=2b+1+wL.                           (10)

The selected input has precisely three occupied B neighbors of h, so
P_(h,3) acts as identity on it. Its other three neighbors are empty and
h has charge+. Consequently A_h applied to that input has exactly three
distinct unit-amplitude outputs, one of which is Theta_w. Its norm is
sqrt(3). This proves

    ||P_M Theta_w|| >= 1/sqrt(3).                       (11)

For completeness, projection P_M is local in the required precise sense.
The domain and codomain split as orthogonal sums over all charge/electric
data outside h's star. A_h preserves those exterior data. In each fixed
physical exterior block, the six B Gauss equations determine the six
star fields from the finitely many star charges. Thus each relevant local
domain and range block is finite dimensional. The range closure and its
orthogonal projection split over those same exterior blocks. This is not
a tensor-product claim that ignores Gauss constraints.

The unit circulation shift U along the x ring is a physical unitary,
preserves the fixed number sectors, and has support disjoint from h's
star. It commutes with A_h as a map between its domain and codomain and
therefore with P_M on the output. Also Theta_w=U^w Theta_0. Hence the
number c=||P_M Theta_w|| is independent of w and satisfies

    1/sqrt(3) <= c <= 1.

Different w have different exterior ring fields. P_M preserves those
fields, so the finite-field vectors

    eta_w=c^(-1)P_M Theta_w,       w>=1,                  (12)

are orthonormal. Let Y=closure span{eta_w}. It is an actual closed
infinite-dimensional subspace of M_h, unlike a presumed basis-word range.

Set u_j=A_h L_b^(m_j)Phi_b. Complete-operator bandwidth again gives
<Theta_w,u_j>=0 for w>j. At w=j the only possible terms are all-Q and the
legal first-hop path supplies the nonzero positive coefficient:

    <Theta_j,u_j>=(i delta)^(m_j) d_j,    d_j>=2^(m_j).   (13)

Since u_j is in M_h, <eta_w,u_j>=c^(-1)<Theta_w,u_j>.
Thus the same finite triangular induction, now wholly inside the genuine
first-hop range, proves

    closure(P_Y A_h C_b)=Y,
    Y intersection (A_h C_b)^perp = {0}.                (14)

For every nonempty bounded open I, the compression to Y of the actual
operator int_I A_h rho_b(s)A_h* ds is faithful and has infinite rank.
The proof uses complete original histories from Omega, not an arbitrarily
chosen physical input as the process preparation. The selected chi_b and
Theta_w only establish full-coefficient noncancellation in (13).

## 5. Precisely what remains missing

Equation (14) is a restricted first-hop separation theorem, not
closure(A_h C_b)=M_h. Projection density onto Y does not imply
Y subset closure(A_h C_b), nor density on Y's orthogonal complement in
M_h. A putative source-invisible vector can involve other local matter
profiles and electric directions whose amplitudes cancel against this
family. Even knowing that its projection onto X or Y is nonzero would
not rule that out: its complementary part can contribute to the same
history pairing. The theorem excludes annihilators LYING wholly in the
stated subspace, rather than arbitrary annihilators with nonzero projection.

Likewise X uses one fixed mixed full-star matter word and one direction
of physical noncontractible circulation, not a complete local phase
fiber, arbitrary winding sectors or all charge masks. The two results
are not a proof that every fast invariant dark module meets an actual
source. They do give actual coherent, infinite-dimensional separation
and faithful integrated compressions on explicitly identified subspaces.

The remaining exact global consumer is still absence of a nonzero eta in
M_h annihilating all bounded-resolvent words (18) of frozen proof, or the
smaller relevant source-adjoint separation condition stated there. The
current argument establishes that necessity on Y but does not close it
on all of M_h. The next algebraic step would have to control coupled
local-profile/exterior-field blocks, not substitute population support
for coherent separation.

All statements keep one finite graph, fixed b and fixed original labels.
No spin-cutoff transfer, volume-uniform time, fast long-age estimate,
energy uniform integrability, permanent-record realization, physical
law/clock selection, formal review, audit or retained grade is inferred.
