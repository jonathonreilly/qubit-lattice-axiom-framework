# MATCHA — an opened mixed-history cell and its exact comparison budget

**PROVEN on the fixed positive sector specified below:** an actual opened
ancestral cell, paired numerator and bare all-cut comparator on identical
variables, and a nontrivial two-cell RM1 representation with
`eta_(sigma+1) <= 1/16`. Every main-action factor is retained before the
small tilt is tested. A joint fresh-gap budget is also evaluated at an
explicit sufficient coupling. **PROVEN failure of this same identity-mean
comparison on another positive sector of the same past history. OPEN:**
outer ancestral integration with local endpoint bounds, coverage of the
other sectors, a history-summed majorant, and regeneration.

This is a bounded **disintegration** of an actual history. The external
ancestral variables are still integration variables of the eventual RG
map; they are retained as parameters during this calculation. It is not
an all-history identification of `R_h/Z_A` with a probability expectation.
In particular, a small conditional remainder does not price the sector's
mass or the ratio of its two different main-action normalizers.

| Author-brief item | Result |
|---|---|
| Open a bounded mixed core and pair its integrals | **PROVEN**, MA1–MA8. Both levels of kernels, all their normalizers, the actual history, rho/b_1, original source labels and outer masses are explicit. |
| Absorb the main action and test RM2 in the fixed norm | **PROVEN** on the stated cap, MA9–MA17. The background budget is at most 1/16 at the extra support rate needed by RM12. The cap width, density-jet price and sufficient fresh-gap coupling are formulas, not fitted numbers. |
| Uniformity / history class that fails | **PROVEN** volume-uniformity for embeddings of this fixed core at fixed coupling and fixed exterior domains; **PROVEN** failed RM2 inequality MA23 for the specified rough sector; **OPEN** full-history and next-step regeneration. |

PROVEN labels the displayed mathematical statement, ARGUED a proposed
extension and OPEN an unproved obligation. None is audit status, a git
landing, a continuum construction or a mass-gap result. Source identities,
author checks and fresh review are recorded in [MATCHA_LOG.md](MATCHA_LOG.md).

Credit: Tadeusz Balaban's large-field organization and Jonathan Dimock's
[large-field exposition](https://arxiv.org/abs/1212.5562), together with
Fernandez–Procacci's [polymer methods](https://arxiv.org/abs/math-ph/0605041)
and Brydges–Slade's [normed algebras](https://arxiv.org/abs/1403.7244).
These are method attributions only; the first exposition concerns scalar
theory in d=3. No external theorem or memory-only [m] assertion carries
the argument. The local comparison and derivative estimates are rebuilt.

## 1. A fixed positive sector of an actual failed history — PROVEN

Use the supplied finite SU(2) model, L=3, kappa=1 and
`u_0=u_1=u_2=u>=1`. These equal couplings define a test family, not a
running-coupling theorem. Haar measures have mass one. Use exactly
MIXSMALL MS1's paired axial contours, with length at most
`ell=5L-4=11`, and `h_l=sqrt(2/u)` in REALRGA's derivative units.
Take compatible tori large enough for the finite supports below not to
wrap. For the later rough witness choose the level-one site side a multiple
of 9. No uniformity in L or N is claimed.

Use RD3 D1's actual history: two adjacent old blocks
`Y_0={q_0,q_0+e_1}` inside one level-one block v_0, cut 1 and size
threshold 1. Its inactive set is `H_1={-1,0,1}^4`, of size 81.
The current active set is its complement. Put -I on the interior
direction-one link at coordinates (1,1,1,1) in each of the two old
blocks, and I on every other old link. Denote this original field by G.
The incident plaquettes lie inside the respective block and equal -I;
all other plaquettes equal I. On the product of old link caps

    ||U_(0,b)-G_b||op < delta_0,       delta_0=1/16,       (MA1)

four-factor telescoping changes a plaquette by less than 1/4. Therefore
the bad set is exactly Y_0. Its size forces failure independently of U_1;
there is no other bad component. **All** history-absence factors equal
one on this sector, rather than being omitted. This proves
`Xi_h(U_0,U_1)=1` there for every real U_1. The sector has positive Haar
mass: a nonempty open group cap has positive mass, since finitely many
translates cover the compact group and Haar mass of the group is one.

Choose output links c=(v_0,direction 1), c'=(v_0,direction 2), inside
the inactive region. Its fields and kernels are still present in the
full transfer; inactivity removes specified cuts, not these variables.
The old marked blocks are in this selected contour's ancestry.
W=U_(2,c) will be integrated; all
other outputs V are retained, including V_c'. Choose four distinct original
plaquettes p_1,...,p_4 incident to the marked link in q_0. Their sources
are the **absolute original coefficients** J_i in

    S_0(J)=u sum_p s(U_(0,p)) + sum_(i=1)^4 J_i s(U_(0,p_i)),
    s(Q)=1-Re tr(Q)/2,
    |J_i|<1/16,                  r_i=1/16.              (MA2)

These weights and this source domain are fixed throughout. Every kernel,
coupling and cap is held fixed when a source is differentiated. No new
coarse source replaces p_i, and there is no 4! in a distinct-label jet.

Here are explicit finite coordinate sets; factor incidence, not a guessed
geometric collar, defines them.

1. X_1 is the union of every current link occurrence in the actual contours
   of c and c' and the four links of the 12 plaquette at within-block
   coordinates (1,1,1,1) of v_0.
2. X_0 is the union of every original link occurrence in the K_0 means whose
   output links belong to X_1, every interior link of Y_0, and all links
   of the four source plaquettes.
3. Write x=(U_(0,X_0),U_(1,X_1)), and y=(xi,eta,V), where xi and eta
   are **all** remaining original and current links. Let D_0 be every
   K_0 factor reading either part of x. Let D_1 be every K_1 factor other
   than c reading X_1. Include every Wilson plaquette reading x as well.
   Factors outside these lists are retained in explicit outside products.
4. H is a fixed connected hull of H_1, c, X_0, X_1, all original source
   labels and the complete readers of all the listed factors, including
   their normalizers and retained outputs. Choose the lexicographic
   coordinate-path hull in the unwrapped block graph. Original variable
   addresses remain attached when projected to that graph. Put M=|H|.

Each list is finite and independent of surrounding volume at this fixed
depth. Factors reading x can have y readers; those readers are in H and
are differentiated, not fixed to their central value. There is no
iterative deletion of ancestors and no claim that the outside products
are local. In particular M>=81, and all occurrences of M below mean this
complete support size, not one active block.

For the shared ancestry, take q_0 to be the old block at within-v_0
coordinates (0,0,0,0), and q_0+e_1 its neighbor. Some c contours read
the current direction-one link based at q_0. Its K_0 contour family
includes the straight leg through the marked original link, obtained
by taking transverse within-old-block coordinates (1,1,1).
This K_0 factor and those original Wilson/source factors belong to the
same retained ancestral cell. The rough component has not been placed
in a distant tensor factor merely to label the result mixed. No claim
that every mixed cumulant is nonzero is needed for the bounds.

Integrate x_0 in the fixed caps (MA1), denoted Omega_0. Integrate x_1
in fixed identity caps of radius delta, denoted Omega_1; delta is given
in MA15. Retained xi stays in the open old caps (MA1), and retained eta
stays in open identity caps of the same radius delta. One may take closed
half-radius evaluation sets in these open parameter domains. V is real.
Since delta<=1/16, every current plaquette is within 1/4 of I and every
current all-cut predicate is one. All sector boundaries are in integrated
coordinates and independent of y,J. Derivatives do not move these cuts.
The complements of these sectors are kept explicitly in section 2.

## 2. The paired integrals, on exactly the same variables — PROVEN

Let `m_0=int_(Omega_0) dx_0>0` and `q_0=1/m_0` on Omega_0.
The latter is an auxiliary **normalized** density used only to lift the
bare denominator into the same original variables. With y fixed, define

    R_fib(y,W;J) = int_(Omega_0 x Omega_1)
         exp(-S_0(J)) K_0(U_1,U_0) K_1(V,W;U_1) dx,
    Z_fib(y,W) = int_(Omega_0 x Omega_1)
         q_0 b_1(U_1) K_1(V,W;U_1) dx,
    b_1=exp(-u sum_p s(U_(1,p))).                       (MA3)

The history and current cuts are exactly one on these domains, as proved
above. They reappear in the complementary integrals. Integrating q_0
gives one, so Z_fib is precisely the current-sector bare all-cut fiber;
it has not acquired an artificial original-action factor.

To exhibit the inherited compensator rather than just rename it, put

    rho_fib(U_1;xi,J)=int_(Omega_0) exp(-S_0(J)) K_0 dx_0.
    R_fib=int_(Omega_1) b_1 (rho_fib/b_1) K_1 dx_1.    (MA4)

Integrating xi and summing the original-sector complement recovers the
actual rho_(1,h), with Xi_h in the complementary terms. The b_1 in MA4
cancels pointwise against its inverse; it is not an extra action reserve.
If the RD R6 local convention is used afterward, splitting b_1 into its
inside and outside plaquettes leaves RD3's exterior inverse a_B and its
O_(1,B) factor. MA3 uses the full-transfer convention, so that split and
its compensating factors have not been performed or discarded.

Allocate the factors exactly once as

    exp(-S_0(J)) K_0 K_(1,not c) = F_N(y) w_N(x;y,J),
    q_0 b_1 K_(1,not c)        = F_A(y) w_A(x;y),
    A_N=int_Omega w_N dx,      A_A=int_Omega w_A dx,
    n_N=w_N/A_N,              n_A=w_A/A_A.              (MA5)

Here w_N is the product of all original Wilson factors reading X_0,
all D_0 kernels and all D_1 kernels. All four sources belong to w_N.
w_A is q_0 times every current Wilson factor reading X_1 and every D_1
kernel. F_N,F_A are the products of **all remaining factors**. Thus
every cross-boundary action and every earlier/fixed-output kernel that
reads x is inside w, while every outside factor survives in F. The
densities are positive on the common fixed Omega=Omega_0 x Omega_1;
A_N,A_A>0. All Z_t(M) normalizers occur in their actual kernels.

Let `k_*=k_u(W;I)` and use the same residual function for both references:

    phi(x,W)=u h_(M_c(x_1)-I)(W)
                    -log Z_u(M_c(x_1))+log Z_u(I),
    1+a=exp(phi)=k_u(W;M_c(x_1))/k_*(W),
    dmu_alpha=n_alpha(x;y,J) dx k_*(W)dW,
    dnu_alpha=exp(phi)dmu_alpha,       alpha=N,A.        (MA6)

This is a product of **two cells**: one explicitly interacting ancestral
cell and one single-output cell. There is no assertion of independence
inside the ancestral cell. It contains the nonperturbative action, four
source couplings, past kernels and all other fixed-output kernels. Only
the selected kernel's change of mean is left as a tilt.

For every x, `int (1+a)k_* dW=1`. Consequently `int exp(phi)dmu_alpha=1`
for all y,J, with all its derivatives. This proves RM1 with Z=1, not an
approximation to its normalizer. The smallness check below nevertheless
uses pointwise pinned bounds; the vanishing integral of a is not used as
a substitute for them.

Write `p_alpha(W)=int n_alpha(x)k_u(W;M_c(x_1))dx`. Then

    R_fib=F_N A_N p_N(W),       Z_fib=F_A A_A p_A(W),
    R_fib/Z_fib=(F_N A_N)/(F_A A_A) times p_N(W)/p_A(W).
    int R_fib dW=F_N A_N,      int Z_fib dW=F_A A_A.   (MA7)

These are the two different endpoint masses. In particular the numerator
mass contains m_0 and its original action and source dependence; the
denominator's auxiliary m_0 cancels only through its specified q_0.
No estimate on the supported logarithm of `F_N A_N/(F_A A_A)` is asserted.

For complete outer bookkeeping let Omega_xi be the retained-original cap
sector, `m_xi=Haar(Omega_xi)>0`, and `q_xi=1/m_xi` on it. With eta in
its current cap sector, the actual sector integrals are

    R_sector(W)=int d eta int_(Omega_xi) R_fib d xi,
    Z_sector(W)=int d eta int_(Omega_xi) q_xi Z_fib d xi.
    R_h=R_sector+R_complement,
    Z_A=Z_sector+Z_complement,
    R_h/Z_A=(Z_sector/Z_A)(R_sector/Z_sector)
                                      +R_complement/Z_A.       (MA8)

The numerator complement uses the original Xi_h and every remaining
sector; the denominator complement uses its actual chi_A. Both are
nonnegative for real sources. Using q_xi also in the first integral
requires the multiplier m_xi. This may be extensive and is never erased.
The same formulas with current outcomes summed preserve their full
partition. The normalized density in MA6 is only the displayed fiber;
MA8 explains exactly what remains before it is an all-history result.

At the full terminal integration, write V_all=(V,W) and retain the
global endpoint masses as well:

    A_h(J)=int rho_(1,h)(U_1;J)dU_1,
    Zbar_A=int chi_A(U_1)b_1(U_1)dU_1,
    Z_0(J)=int exp(-S_0(J))dU_0,
    int R_h(V_all;J)dV_all=A_h(J),
    int Z_A(V_all)dV_all=Zbar_A,
    int (R_h/Z_A) Z_A dV_all/Zbar_A=A_h(J)/Zbar_A.   (MA8a)

This follows by integrating each now-unread terminal kernel to one.
If the history is normalized to R_h/A_h, its original mixture weight
is A_h/Z_0, exactly once; summing all past histories gives sum_h A_h=Z_0.
Every one of these source-dependent masses keeps its original jets.
MA8a does not replace an endpoint by a unit mass before that integration.

## 3. Complete real density jets, including the source labels — PROVEN

Use REALRGA RGA4 with total field order six and all subsets of [4]:

    T(F)=sum_(a+b<=6) sum_(B subset [4])
       r_B/(a! b!) sup |D_f^a D_c^b partial_B F|.       (MA9)

Fine directions include all still-retained xi,eta, with their original
max-link h_l weights. Coarse directions include every retained V, notably
V_c'. All weights are frozen. There is no derivative in x after x is
integrated, and pinning a cell does not introduce new derivatives in it.
Original source dependence has been absorbed in n_N, not set to zero.
No l1-to-max-link conversion or source-dependent transport is used.

Here is a fully finite, if conservative, computable price P(u). Let n_P
be the sum of the original and current Wilson factor counts in the two
w's, and let d_0,d_1 bound their respective K_0,K_1 counts. These are
the fixed incidence lists of section 1; counts may overestimate but may
not omit a reader. Set r=1/16, h=sqrt(2/u), lambda=12h. For m>=1 define

    M_m(t)=sum_(pi partition [m]) t^|pi|,       M_0=1,
    L_m(t)=sum_pi (|pi|-1)! product_(B in pi) M_|B|(t),
    B_m(u)=[n_P(u+1)+8r](1+4h)^m
                      +(d_0+d_1)lambda^m[u+L_m(u)],  1<=m<=10.
                                                               (MA10)

Every weighted ordered word of length m in log w_N or log w_A is bounded
by B_m. To check this: a plaquette word has at most 4^m choices of link
occurrences and cost h^m; its coefficient is at most u+1. A word with
one source position costs at most r times a plaquette derivative, or 2r
at field order zero; words with two source positions vanish in log w.
The 8r term is a common bound for four labels. A kernel numerator has
at most 12^m input/output choices. For its normalizer, differentiation
of exp(H) partitions the ordered positions, bounding |D^m Z|/Z by
lambda^m M_m(u). Differentiating log Z partitions again with coefficient
(-1)^(k-1)(k-1)!, giving lambda^m L_m(u). Normalizers have no original
source derivative. Products of fixed caps and q_0 have zero y,J jets.

For a nonnegative score array B define

    M_m(B)=sum_pi product_(C in pi) B_|C|,
    I_0(B)=1,
    I_m(B)=sum_(s=1)^m binom(m,s) M_s(B) I_(m-s)(B),
    C_m(B)=sum_(s=0)^m binom(m,s) M_s(B) I_(m-s)(B),
    P(u)=sum_(a+b<=6) sum_(c=0)^4
                 binom(4,c) C_(a+b+c)(B(u))/(a! b!).   (MA11)

M_0(B)=C_0(B)=1. Leibniz in `A A^-1=1` proves the inverse recurrence,
and Leibniz in `w A^-1` proves the last convolution. Division of an
integral derivative by its positive integral is expectation under its
own law. It introduces no inverse sector-mass bound. Therefore

    T(n_N)<=P(u)n_N,           T(n_A)<=P(u)n_A,
    T(k_*)=k_*,               P(u)>=1.                 (MA12)

This holds pointwise on every fixed cell support, uniformly over y,J
in the stated real domains. Compactness and finite positive kernels
justify the differentiation. Only factor counts local to H enter P;
outside factors are in F and have not been granted this bound.

For clarity the first fine/coarse derivatives are actually retained.
For a retained original fine direction A, its score in w_N contains

    -D_A S_(0,local)
    +sum_(d in D_0)[u Re tr(U_(1,d)^* D_A M_d)/2
                                        -D_A log Z_u(M_d)].

For `V_c'(s)=exp(s B)V_c'`, its coarse score is
`-u Re tr(V_c'^* B M_c')/2`. No denominator derivative is dropped.
For any fixed insertion F on the two cells,

    D E_(nu_alpha) F=E_(nu_alpha) D F
                     +Cov_(nu_alpha)(F,D log w_alpha),
    D log A_alpha=E_(n_alpha) D log w_alpha.             (MA13)

The score formula also applies with mu_alpha. Phi has no y derivative:
**every** link read by c was put in X_1, while the fine and coarse
directions in MA13 remain genuine exterior directions. If those input
links are retained instead of integrated, the missing kernel jets must
be paid and this particular bound cannot be used unchanged.

For each B subset [4], at arbitrary real J,
`partial_B A_N=(-1)^|B| A_N E_(n_N) product_(i in B)s_p_i`.
More generally the same formula holds for the unnormalized numerator
with F inserted. Its normalized coefficient is obtained by distributing
the labels between this numerator and A_N^-1, using MA11's exact inverse
recursion with signed derivatives. This specifies all fifteen nonempty
subsets, including the four-label coefficient. Differentiating these
identities in A or B retains all mixed field/source terms up to (6,[4]).
The derivatives of A_N in MA7 restore the unnormalized original moments;
averaging only normalized inner connected derivatives would lose them.

## 4. An evaluated RM2 and joint mixed-core budget — PROVEN

Telescoping each actual contour on Omega_1 gives
`||M_c(x_1)-I||<=ell delta`. Pointwise comparison of its positive
integrands gives
`|log Z_u(M)-log Z_u(I)|<=u||M-I||`. Thus

    |phi|<=2u ell delta,       T(a)=|a|<=s_delta,
    s_delta=exp(2u ell delta)-1,
    alpha=s_delta P(u).                                  (MA14)

The equality for T uses the declared external derivative variables, not
a value-to-derivative inference. Assign the full H to the background
atom, including the readers of n_alpha. To have output rate sigma>=0
and the extra reserve for RM12, **choose the integration cap once** as

    delta=min(1/16,
       log(1+exp[-(sigma+3)M]/[16P(u)])/(2u ell)).
    eta_(sigma+1)=exp[(sigma+3)M] s_delta P(u)<=1/16.    (MA15)

This is a strictly positive explicit radius at every finite u. The
source domain, its weights and the field derivative units have not
changed. The sector is deliberately narrow; its small mass is retained
in MA7–MA8 and is not claimed negligible or representative of the whole
history. Smallness is proved by a deterministic sector choice, not by a
numerical search or calibration.

Pinning either entire cell removes its integration-density cost; it
does not change MA12 or MA14. For any selected atoms, differentiation
under the integral and ordered Leibniz give
`T(int product f_i dmu)<=int product T(f_i) product T(n_c)`.
Unvisited normalized cells integrate to one before that estimate. A
visited ancestral cell costs at most P, a pinned one costs nothing,
and assigning P to each atom overcounts rather than undercounts it.
This proves RM5's common pinned majorant for **this two-cell alphabet**,
including pins of the ancestry cell, of W, of both or neither. It does
not assert internal subcell factorization. Another consumer wishing
to pin only some internal ancestry coordinates needs its own
disintegration; the corresponding reference marginal is not silently 1.

There is an actual mixed coefficient. Put E={W:s(W)>=1}; this is a fixed
positive-measure output event. For mean I its kernel gap is s(W).
A Haar ball of radius z about a maximizer has mass at least
`(1+8/z)^-8`: cover the eight real matrix-entry coordinates by cubes of
side z/4, choose occupied representatives, and translate group balls.
The Frobenius diameter is <z, so this is an operator-ball cover.
The function h_M is 1-Lipschitz. A ball of radius 1/u loses at most one
in the exponent. Factoring out the maximum from numerator and denominator
therefore gives

    p_E=int_E k_*dW <= exp[-q(u)],
    q(u)=u-1-8log(1+8u).                                (MA16)

Only use this exponential as a small price when q>=0. The cap in MA15
also has `2ell delta<=1/(16u)`, so on the actual mean the same fixed
E has gap at least `1-2ell delta>=15/16`. It is a fresh event, not a
mandatory event being charged again.

For each alpha=N,A the exact gap probability and its mixed correction are

    E_(nu_alpha) 1_E = p_E + int a 1_E dmu_alpha,
    T(int a 1_E dmu_alpha) <=s_delta P(u) exp[-q(u)].
    gamma=P(u) exp[-q(u)],
    d=exp[(sigma+3)M] gamma.                            (MA17)

These coefficients couple the actual small kernel remainder, a fresh
gap, and (in N) the rough inherited ancestor and four source labels.
The smooth atom a is the exact kernel-ratio remainder, not an invented
KR activity. It is not being asserted to exhaust KR's full output.
There is one owner of the one gap. The atom set {}, {a}, {1_E},
{a,1_E} has joint majorants 1, alpha, gamma, alpha*gamma:
the last assignment has an extra P>=1 and is conservative. These new-atom
bounds apply with W integrated, also if the ancestry cell is pinned.
If W is pinned, use P times its event indicator in place of gamma;
there is no pinned-event suppression. Only the background alpha is the
all-pin majorant required for RM5–RM7. Disconnected copies factor only
when their complete variable/factor cells are disjoint. No product of separately normalized
correlated groups is taken.

Here is an explicit sufficient coupling, rather than an unspecified
large-u statement. The lists are fixed as u varies. MA10 gives
`B_m(u)<=B_m(1)u^m` for u>=1: Wilson terms cost at most one power, and
every monomial of L_m has degree at most m. Each term of M_n(B), I_n(B)
and C_n(B) has weighted degree n when B_m has weight m. Consequently
`P(u)<=P(1)u^10`. Define the finite positive constant

    D=exp[(sigma+3)M+1] 9^8 P(1),
    U_*=max(1, 2log[16D(36/e)^18]).                   (MA18)

For u>=U_* we have

    d<=D u^18 exp(-u)
       <=D(36/e)^18 exp(-u/2)<=1/16.                  (MA19)

The middle bound follows by differentiating `v^18 exp(-v/2)`, whose
maximum on v>=0 is `(36/e)^18`. The logarithmic inequality
`1+8u<=9u` supplies the other eight powers. Thus the augmented budget
is <=1/8, strictly below 1/4. All constants are defined by finite factor
lists and finite partition sums; no numerical run is needed for this
inequality. If u<U_*, MA15 still proves RM2, but this sufficient
fresh-gap test has not been asserted to pass.

MA17 supplies the mixed bound with the ancestral density price P(u).
It is not the literal soft-kernel-only D_6(|S|) bill of REFMATCH RM9:
this ancestral cell has original-source and retained-coarse dependence.
The general pinned and complete-support decoration mechanisms
(RM5–RM8, RM11–RM12) apply with this P-priced core bound and the displayed
support reserve. The joint certificate instantiates RM13; its
marked-new-atom bound is at most `d/(1-4eta)<=1/12`.
The elementary one-core logarithm
can also be checked directly: its generating integral is
`1+z E_nu 1_E`, and the absolutely convergent log series controls all
the finite jets by the same joint majorants. The background integral
is exactly one. These facts establish neither an endpoint-mass log
budget nor a majorant common to the sum of different histories.

## 5. What is uniform, and an actual sector where this reference fails

**PROVEN bounded uniformity.** For embeddings of the specified finite
core, the factor counts, M, P(u), delta(u), source radius and the preceding
bounds do not depend on the surrounding volume. They are uniform in
the external real data on the stated domains. All outside products and
their eventual integrations remain present. This is a fixed-depth
fiber statement; its tiny cap can depend on u and its mass can depend
on the volume of the outer sector.

**PROVEN failed extension of this particular reference.** Keep the same
original cap (MA1), so the same past failure history has positive density
for **every** current U_1. On the current lattice set

    U_(1,1)(x)=diag(exp(i theta x_2),exp(-i theta x_2)),
    U_(1,2)=U_(1,3)=U_(1,4)=I,          theta=2pi/9.     (MA20)

Choose c in direction one with its block origin at x_2=0. The translated
paired axial paths have identical ordered steps and identical link values;
their diagonal matrices cancel. The straight leg contributes
`exp(2pi i r/3)` for the three offsets r. Thus the **actual** arithmetic
contour mean is

    M_c=diag(m,conj(m)),
    m=(1/3)sum_(r=0)^2 exp(2pi i r/3)=0.              (MA21)

Its 12 plaquettes have distance `2sin(pi/9)<1`; all others are I.
Therefore every current cut=1 passes, with a positive margin. This
is in the bare all-cut support as well as the inherited history's
support. A small fixed tube about MA20, together with MA1, has positive
measure under all the finite positive action/kernel factors. All other
terminal outputs can be any fixed real values. The point at its center
is an essential-supremum witness by continuity.

Repeat MA5–MA6 on that fixed rough tube, still absorbing the full
ancestral main action and still using the specified output reference
`k_*=k_u(W;I)`. At its center the actual selected kernel is Haar.
At W=-I the residual atom is exactly

    a=exp(u) Z_u(I)-1.                                (MA22)

Haar symmetry under W -> -W gives `int h_I(W)dW=0`, and
`exp(x)>=1+x` then gives Z_u(I)>=1. Hence every RM2 majorant for this
same residual atom and full support must satisfy

    eta_sigma >=exp[(sigma+2)M](exp(u)-1)>1/4,
                                      u>=1, sigma>=0. (MA23)

This is a **lower bound**, not a loose upper estimate that failed to
prove smallness. It already fails at order zero; fine/coarse and source
jets cannot repair it. The original/main action has been absorbed and
never re-expanded as the order-one Wilson atom of RD4 C10 or MIXSMALL
MS29. The failure is the remaining normalized output-kernel comparison.

Changing the output reference to Haar at this particular zero mean,
or to a nonperturbative reference adapted to the whole rough tube,
changes MA22 and is not excluded. Taking only a tiny tube about a
suitable sector-specific mean can again make a comparison small, but
covering all sectors, summing their masses/readers and controlling
moving sector maps are additional work. MA23 is not a no-go for RM1,
for a different reference, or for the RG map.

## 6. Regeneration, endpoint costs and the next construction — OPEN / ARGUED

The actual normalized soft kernel is strictly positive on every open
output set, including the complement of any small identity cap. The
new event E used above is itself outside that cap. Thus the current
cap is **not** an almost-surely invariant class of outputs. A future
selection can also make E mandatory; its previous probability must then
stay in the unnormalized endpoint mass and cannot be reused. This
proves failure of a proposed cap-only closed class, not failure of a
sector decomposition that retains its complement.

| Remaining obligation | Exact status / relation to this construction |
|---|---|
| Actual fixed-fiber RM1 | **PROVEN** in MA3–MA7, with a nonperturbative ancestral cell and a separately normalized output cell. The two paired references have different A and F factors. |
| Fixed-fiber RM2 and the needed extra support rate | **PROVEN**, MA15. Four original source derivatives and six field derivatives enter P, not an unchanged Haar density. |
| Joint mixed new-atom test | **PROVEN** for this one-gap core at u>=U_*, MA17–MA19. It does not instantiate every inherited activity or completion type. |
| Endpoint local logs | **OPEN** for `F_N A_N/(F_A A_A)` after the actual outer integrations. MA13 specifies their derivatives but supplies no small full-root log budget. |
| Outer ancestral integration | **OPEN** at local RG scope. MA8 is exact; freezing xi for the fiber proof does not make its later conditioned law product or discard its masses. |
| All sectors and histories | **OPEN**. MA23 rejects the unchanged identity-mean reference on a positive sector of the same h. A common summed majorant, including roots on tails, is still needed. |
| Regeneration | **OPEN**. One must produce the next cell/reference decomposition, fixed domains and reserve sigma+3 from the actual output, including the positive cap complement. Nothing in MA15 reproduces that input. |

**ARGUED next step.** Use a sector-specific nonperturbative output law on
the short-mean branch, keep its old mass, and estimate the paired
endpoint logs before summing sectors. The concrete target is a common
pinned joint majorant for those paired cells, together with the actual
outer integration; merely renaming that target as a matching assumption
would be target-equivalent, not a new reduction. Full KR, FR and TC
interfaces remain their coordinator lanes' inputs. No fixed source-radius,
finite-coupling kernel-remainder, or original-law coercivity/tail theorem
has been duplicated or claimed here.

## 7. No-Go Discipline Gate — scoped diagnostic, no exhaustion certificate

**N1.** Attempted: exact interacting-cell absorption and a frozen
identity-mean output comparison, producing both MA15 and MA23. An adapted
rough reference, joint cancellation before norms, and unnormalized
original-charge organization remain live. These are not five ruled-out
families; no packet PASS or exhaustion claim is available or asserted.

**N2.** Let J be a complete joint matching estimate including endpoint
and outer integration, and R its regeneration. R requires J on the next
states; one-step J does not establish R. A complete J would subsume the
separately listed endpoint and outer requirements. Remaining implication
relations are unresolved; no independent wall count is claimed.

**N3.** Explicit premises are the supplied finite model, one fixed
history, the displayed source/field units, fixed cap sectors, fixed-depth
reader lists, whole-cell pinning, and the exact u>=U_* condition for the
new-gap budget. The reference density and every remaining outside mass
are given by integrals. No invariant domain or complete-history bound
is hidden in the words cell, background or positive.

**N4.** RD4 C10/MIXSMALL MS29 concern unabsorbed Wilson atoms and are
only prior-route comparisons; they do not prove MA23. MIXSMALL MS11–MS14
and REFMATCH RM18 identify the same actual zero contour mean, rebuilt
in MA20–MA21; MA23 tests the distinct kernel-ratio atom, not their
individual normalizer-derivative claim. CHARGE C13 is an extensive
upper-majorant limit, not a lower bound used here.

**N5.** Per output element/cell: MA22–MA23 reject this one atom's
pointwise majorant. Per source and fine/coarse direction: MA10–MA13 retain
the finite jet orders. Per block: full M is paid in MA15. Per mode:
no spectral statement. Lattice-wide: only the disjoint sector identity
MA8, not uniform clustering or an all-history obstruction. No unrun
numerical diagnostic supplies any of these statements.

**N6.** Changing the reference, keeping old mass or refining the cell
organization are mathematical operations requiring no new physical axiom.
No approved primitive is called missing or used as an analytic estimate.

**N7.** A hostile counterargument to a broad negative conclusion is that
MA22 becomes zero at the center if the output reference is Haar. A
carefully matched rough-cell construction could control neighboring
means and use the original endpoint mass to pay a complete support sum.
REFMATCH's nonperturbative-cell alternative and CHARGE's once-only
accounting leave that route open. Its concrete unproved obligation is
the paired, differentiated, history-summed endpoint/reference estimate.

**N8.** The searched predecessors repaired repeated mandatory-event
prices, erased full readers and the use of an unabsorbed Wilson action.
This construction retains those repairs. It does not turn its chosen
sector's smallness or its other sector's failure into a universal result.
The narrow diagnostic is mathematically proved; a general negative-claim
packet remains unavailable under N1 and the live counter-route in N7.

The written derivations are the evidence. Numerical execution and fresh
review are recorded in the log and `checks/matcha_*`; their status does
not alter the displayed hypotheses or the OPEN obligations.
