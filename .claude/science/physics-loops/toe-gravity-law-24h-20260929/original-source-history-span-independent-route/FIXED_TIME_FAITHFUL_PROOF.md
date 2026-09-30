# Faithful actual source compression on a closed sparse winding tower

This refines the same actual-input problem. Inputs are the literal original
rotor operators and complete winding construction, frozen history proof
10eb8ccd, coherent quotient proof809a5838, and the no-four-cycle saturation
lemma in fixed-time proof5b57bb97 sections2-3. No new computation is used.
The conclusion remains a restricted physical-sector statement, not full
dark-module observability, phase-fiber faithfulness or source selection.

## 1. Exact physical signed-flux bands

Keep L divisible by4, L>=8, n=L^3/2 and4<=b<=n/4. Every link is oriented
A to B. Define the integer electric observable

    Jx(E)=sum_e d_x(e) E_e,                            (1)

where d_x(e) is +1 or-1 for an oriented nearest-neighbor edge in the
positive or negative x direction, and0 for a y or z edge. At periodic
seams use the nearest-neighbor displacement, not a coordinate subtraction
of size L-1. Jx is a self-adjoint diagonal operator on the physical rotor
space. Every primitive hop changes it by at most1; D is diagonal. Thus
the actual Q has Jx band at most4, R at most2, and L_j at most4, with the
unbounded diagonal part preserving every Jx eigenspace.

In the NB=0 sector all A charges are+. The exact landed scalar/plaquette
formula for Q_0 preserves Jx, since each elementary square has total
signed x displacement0. D_0 is diagonal and also preserves Jx. Finally
the complete original loss is exactly

    R_0=60 n I                                         (2)

on this sector. To check the normalization, a resolved marked edge has
five legal old outward destinations, since the marked B site must remain
empty before j. In F_a* j* j F_a every destination returns to the same
A site with the same field, so it contributes5I. There are6n edges and
two resolved signs. A coherent edge instead has twice the vacant-site
projector j* j, hence10I on each of6n edges. Both give (2), with no
coherent cross loss term because its two output charge words are orthogonal.

Consequently S_0(s), L_0 and all their allowed powers preserve Jx. In
particular the actual evolved vector S_0(s)Omega has exactly Jx=0 for
every s>=0. Its electric support is generally infinite; it is NOT replaced
by Omega or by a finite electric cutoff.

Let B=b_mu_b ... b_mu_1 be the complete fixed original preparation word.
All its marked edges point in y or z, including the special z birth, so
the j factors have Jx band0. Each old outward F factor has band1. Therefore
B has Jx band at most b, including every coherent alternative. The final
source T=-F_h j_mu F_h has band at most2, since its marked edge is in z.
The first-hop map A_h=F_h P_(h,3) has band at most1.

For the selected physical words already fixed in the preceding proofs,
directly summing their actual fields gives

    Jx(Xi_w)=-1-wL,       Jx(Theta_w)=-2-wL.             (3)

The first ordinary selected outward +x hop contributes-1. Each ring
circulation contributes-L. All other preparation edges are in y or z.
For Xi_w the final source's +x and-x outward hops contribute-1 and+1,
and cancel. For Theta_w only the +x hop is retained. This computes (3)
for these words, not for arbitrary paths inside a coherent history.

## 2. Derivatives of legal boundary histories at fixed total time

For fixed s>0 and0<=t<=s consider

    V_s^T(t)=T S_b(t) B S_0(s-t)Omega.                  (4)

This is a boundary history with all b-1 gaps between births set to zero.
It belongs to the closed span of ACTUAL histories at that same total
time s. Indeed, for0<t<s replace each intervening gap by epsilon>0 and
reduce the initial gap to s-t-(b-1)epsilon; all gaps are then strictly
positive for small epsilon and still sum to s. Strong continuity gives
(4). The endpoints follow by another strong limit. No isolated event time
is assigned positive probability.

Finite-field Omega is in every polynomial electric-weight domain. The
actual finite-band interaction-picture estimates in winding proof
section5 propagate each such domain under S_0(s). B preserves these
domains. Each L_j consumes only two electric weights. Thus every fixed
right derivative at t=0 of (4) exists strongly, with the ordinary finite
product rule:

 W_m^T(s)=sum_(k=0)^m binom(m,k)(-1)^(m-k)
                 T L_b^k B L_0^(m-k) S_0(s)Omega.       (5)

All factors in (5) act on their genuine domains. It follows also by
forward finite differences, with mt<s, that W_m^T(s) belongs to the
closed actual source-history span at fixed total time s. The same holds
for W_m^A(s), obtained by replacing T with A_h. No converse from formal
Taylor coefficients and no analytic-vector property is used.
At s=0, (5) below denotes its continuous electric-weight-domain limit,
not a history with a negative initial gap.

Because L_0^(m-k)S_0(s)Omega remains in Jx=0, the exact support bounds are

    W_m^T(s): |Jx|<=b+2+4m,
    W_m^A(s): |Jx|<=b+1+4m.                            (6)

These bounds concern Jx only, not the full electric l1 norm. They remain
valid for the unbounded electric support of S_0(s)Omega.

## 3. Sparse triangular rows at every time

Set

    D=floor((b+1)/L)+1,       w_j=Dj,       m_j=w_j L/4,
    X_D=closure span{Xi_(w_j):j>=1},
    Y_D=closure span{eta_(w_j):j>=1}.                   (7)

The eta family, its normalization c, and the actual range projection P_M
are exactly those of809a5838. Thus Y_D is a closed subspace of M_h. The
choice of D ensures DL>b+1. For l>j, equations(3),(6) give

    <Xi_(w_l),W_(m_j)^T(s)>=0,
    <Theta_(w_l),W_(m_j)^A(s)>=0                       (8)

for EVERY s>=0. The first inequality follows from
w_l L+1>w_j L+b+2; the second has an even smaller needed margin.
Since W_m^A(s) lies in M_h, replacing Theta_(w_l) with eta_(w_l) just
divides its pairing by c. Hence both projected derivative matrices are
lower triangular on these fixed closed orthonormal families.

No assertion that all marked paths have one fixed Jx value is hidden in
(8). Only the uniform bands in section1 enter. A sparse subsequence is
what makes those deliberately coarse bands sufficient.

## 4. Each diagonal is an actual bounded analytic matrix element

Define

    gamma_j^T(s)=<Xi_(w_j),W_(m_j)^T(s)>,
    gamma_j^A(s)=<eta_(w_j),W_(m_j)^A(s)>.              (9)

For any fixed j, move the finite generator powers in (5) to the test
vector. All original adjoint hops and every L_j* map finite-field vectors
to finite-field vectors. The test Xi is finite field, and eta is finite
field by the physical finite-block range-projection proof809a5838.
Thus there are actual finite-field vectors zeta_j^T,zeta_j^A in H_0 such
that

    gamma_j^Z(s)=<zeta_j^Z,S_0(s)Omega>,       Z=T,A.    (10)

Explicitly, for a test xi and output Z, the vector is the finite sum

 sum_(k=0)^m binom(m,k)(-1)^(m-k)
               (L_0*)^(m-k) B* (L_b*)^k Z* xi.        (11)

The domain transfers in (11) are justified by the same propagated
electric-weight domains used for (5), not by treating L_0 as bounded.
In particular (10) is a bounded test functional of S_0(s)Omega even
though (5) itself contains unbounded operators.

At s=0, every term of (5) with k<m_j contains an initial L_0 factor. Its
pairing with Xi_(w_j), or with Theta_(w_j), vanishes by the exact
no-four-cycle l1-saturation argument of5b57bb97 sections2-3: the target
field norm attains the full degree-m_j budget, while the first initial
factor must be scalar or a plaquette on a four-cycle absent from its
electric support. The only surviving term is k=m_j. Therefore the
complete coefficients are

    gamma_j^T(0)=-(i delta)^(m_j) a_j,        a_j>=2^(m_j),
    gamma_j^A(0)= c^(-1)(i delta)^(m_j) d_j, d_j>=2^(m_j). (12)

No unknown cancellation with the electric Hamiltonian, loss or coherent
birth branches remains in (12). Positivity and the common first-order
phase are those of the complete source coefficients, not selected paths
substituted for the actual history.

The bounded-functional representation (10) has the continuous
lower-half-plane extension established in frozen10eb8ccd. Each gamma
is nonzero at0 and hence is not identically zero. The bounded-quadrant
argument there proves that its positive-time zero set has Lebesgue
measure zero; continuity makes its nonzero set open dense. Intersecting
these sets for both Z and countably many j gives one dense-G_delta
full-measure set E_D subset(0,infinity) on which EVERY diagonal in (9)
is nonzero.

## 5. Closed-subspace faithfulness at those fixed times

Fix s in E_D. Project the actual derivative rows W_(m_j)^T(s) onto X_D.
By (8) the j-th projection is a finite linear combination of the first
j basis vectors, with nonzero diagonal (9). Finite triangular induction
therefore yields

    closure(P_XD span{actual source histories at total s})=X_D. (13)

Equivalently, if eta=sum_j c_j Xi_(w_j) is square summable and annihilates
all those histories, pairing with the first derivative row gives c_1=0;
the next gives c_2=0, and so on. Each row pairing is a finite sum. The
same argument applies to Y_D using W^A.

The positive original-history expansion of rho_b(s) now gives the precise
fixed-time operator conclusion:

 P_XD T rho_b(s)T* P_XD restricted to X_D is faithful,
 P_YD A_h rho_b(s)A_h* P_YD restricted to Y_D is faithful. (14)

Indeed a zero quadratic form means the complete scalar history pairing
vanishes almost everywhere on every original label simplex. Continuity
then makes it vanish everywhere in its interior and on its boundary;
the derivative test (13) applies. This proves (14) for ALL nonzero vectors
in the closed spaces at the same s, without an uncountable intersection
of individually exceptional time sets. The exact triangular rows, rather
than a mere dense countable set of positive scalar tests, are decisive.

Both compressions have infinite rank. Since Xi_(w_j) is dark, the first
is also the same compression of the actual dark-compressed source. For
4<=b<=L-2, D=1, so (14) covers the entire chosen positive winding family
X and Y. For larger permitted b the theorem concerns the explicit sparse
subsequence in (7), without claiming anything about its complement.

## 6. This still does not settle the full consumer

The spaces in (14) have one selected local matter profile and one signed
ring-winding direction, with the first-hop profile corrected by the actual
local range projection. They are not the full dark sector or M_h. An
annihilator outside these spaces can still combine other local profiles
and exterior electric directions. Nonzero projection of such a vector
onto X_D or Y_D does not itself rule out cancellation with its complement.

There is no uniform positive lower eigenvalue: the operators are trace
class on infinite-dimensional spaces. There is no weight, energy moment,
late-fast-time decay, mean residence, finite-spin or growing-volume bound.
The exceptional null set is not shown empty. Preparation remains the
actual bare Omega with the complete supplied dynamics and instrument;
this theorem neither selects that law physically nor identifies its
moving occupations with permanent framework Records. No formal review,
audit, retained-grade promotion or separate milestone is claimed.
