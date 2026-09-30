# Physical collision correctors and the many-pair Schur form

Author derivation in progress, September30. This is a new proposed theorem,
not a focused check or accepted downstream premise. The original supplied
qubit law, positive mu,tau, all physical occupation configurations and full
internal tensors are retained. Source-bound prior arguments are recorded in
SOURCE_AND_PRIOR.json. No physical-cell lower boundary law is supplied here.

## Target and candidate quantitative conclusion

Let V=L^3, fix the guard radius R0>=14, and let V_n:Sym^n C5 -> H_(N=2n)
be the actual polar isometry of the guarded constant-soft frame in the
checked periodic bridge. Write P_n=V_n V_n*, Q_n=1-P_n. That bridge gives

 H_N >= Delta_L Q_n,  Delta_L=a/[C_B R0^3+C_R0 L^2],
 a=min(tau,mu/12), C_B=28000322, C_R0=4+15C_B(R0+4)^3,       (1)

whenever its Gram loss delta=binom(n,2)(2R0+9)^3/V is below one.
The exact Schur matrix is

 S_n,L=V_n* H V_n - V_n* H Q_n(Q_n H Q_n)^(-1)Q_n H V_n.

The candidate conclusion is

 ||V S_n,L - sum_(i<j) T0^(ij)|| <= C_n L^(-1/4),           (2)

for fixed n and sufficiently large odd L, with C_n<=exp[C n log(n+2)].
Here T0 is the ACTUAL15-channel N4 threshold form, extended naturally to
each symmetric pair of the n internal factors. This is a full operator
comparison, not a coherent-direction energy comparison. If the stated
constant growth is established, it gives uniform convergence for
2<=n<=floor(sqrt(log L)), with error L^(-1/4+o(1)). It is not an EOS.

The critical new ingredients are proved below as candidate arguments:
adiabatically cut N4 correctors with a small ordinary l2 residual; exact
finite-degree hard-core source identities; a physical creation-operator
norm bound; and a connected-contraction estimate. Any gap in those steps
blocks(2), rather than becoming an assumed dilute-gas lemma.

## 1. Exact hard-core source identity

Let

 C_z*=sum_(x,alpha) z_alpha R_alpha(x)*,
 R=(Q_E1,Q_E2,Q_T12/sqrt2,Q_T13/sqrt2,Q_T23/sqrt2).

These are physical pair creators. They commute with one another because
all site creation operators commute, including their nilpotent same-site
products. On the torus, ||C_z*Omega||^2=V||z||^2 and H C_z*Omega=0.
Throughout this section C denotes C_z*, not an annihilator.

At site x write C=b_x* A_x+C_not_x, where A_x is a pure-creation polynomial
on other sites. The exact one-site algebra gives

 [b_x,C]=(1-2n_x)A_x,
 [[b_x,C],C]=-2b_x* A_x^2,
 ad_C^3(b_x)=0,  [n_x,C]=b_x*A_x,  ad_C^2(n_x)=0.          (3)

Use ad_C(O)=[O,C]. Every term of H is either n_x, a normal-ordered
pair word b_a*b_b* b_c b_d (allowing coincidences after normal ordering),
or a product of three number operators. The derivation rule and(3) imply

                         ad_C^5 H=0.                    (4)

The cubic occupation terms have budget three and a two-annihilator word
has budget four. This is an exact operator identity at every finite volume;
it does not replace hard-core operators by CCR. A nonzero commutator only
attaches creators at one of the original noncreation sites of its H term.
Thus its vacuum output is a finite-range, translation-covariant pure
creation polynomial. Let W_r*Omega=(ad_C^r H/r!)Omega. Since W0=W1=0,

 H exp(tC)Omega = exp(tC)[t^2 W2*+t^3 W3*+t^4 W4*]Omega.   (5)

All exponentials here are finite creation polynomials on a finite torus;
no state normalization or infinite-volume exponential is asserted.
W2*Omega=H C^2 Omega/2=F_(z tensor z)/sqrt2, where
Phi_A=(1/sqrt2)sum_ab A_ab C_a* C_b*Omega and F_A=H4 Phi_A.
The W3/W4 vectors are actual connected six/eight-particle sources.
They need not vanish. The frozen literal control exhibits nonzero examples.
Mixed internal sources follow by polarization, or by commuting the five
independent derivations. No internal coherence is assumed in that extension.

## 2. Actual N4 exterior and a sharper compact corrector

The checked threshold energy completion supplies a unique correction chi_A
with Riesz stationarity

 H4(Phi_A+chi_A)=0 against every finite physical occupation test,
 T0(A,B)=E_bare(A,B)+<chi_A,F_B>.                         (6)

It need not be l2. The map A->chi_A is linear and energy bounded on the
finite15-dimensional space. The full physical matching/nonmatching split
is P/Q. In N4, Q H4 Q>=mu Q. Coupling from Q into P has its P range in a
fixed collision core: two distant graph dimers remain matching after any
literal local pair move. This is a statement about actual configurations.

Outside that core, a matching configuration has a unique matching. Its
ordered amplitudes F_de(r), d,e in the nine forward bonds, obey
F_de(r)=F_ed(-r). The physical orbit norm is one-half their squared norm.
The exterior Hamiltonian is exactly the sum of the two true N2 edge
Hamiltonians. In Fourier variables its81-channel symbol is

 L(k)=K(k) tensor I9 + I9 tensor K(-k),                    (7)

with the corresponding index order; equivalently the second K acts on
the residual edge index with reversed relative translation. K is the
literal nine-bond S+W symbol already checked in the matrix-pin route.
In particular K(k)>=a l(k)I9, K(0) has kernel U C5, and K is a Hermitian
trigonometric polynomial. Thus L>=2a l I81 and its zero-momentum soft
space is P_s=(UU*) tensor(UU*), dimension25 before exchange symmetry.
The constant incoming tensor is sqrt2 U A U^T.

An exact isometry from physical matching amplitudes to ordered coordinates
uses division by sqrt(m(S)) where a core configuration has m matchings,
and the one-half ordered norm. All differences from the exterior coordinate
law, including forbidden overlaps and repeated matchings, are confined to
finitely many relative coordinates. Extend the finite missing core
coordinates by an arbitrary positive diagonal operator. The matching
block then differs from L by a finite-range finite-rank core operator.
The incoming physical Phi differs from its exterior constant by a compact
core vector. These are finite-dimensional bookkeeping changes only.

The Q correction solves a uniformly gapped equation with compact source.
For C=QHQ and M>=||C||, its inverse is
M^-1 sum_(j>=0)(I-C/M)^j, with norm ratio at most1-mu/M. Literal H moves
only a bounded number of sites by bounded distance at each step. The part
of a compact-source response outside configuration diameter r therefore
has l2 norm at most C exp(-c r). Polynomial configuration volume growth
also gives a uniform l1 bound for that tail. No all-N nonmatching gap is
inferred; this uses only the actual N4 Q block.

The ordered matching correction y, including its compact incoming-core
adjustment, solves L y=s with s supported in a fixed core. Its L-energy is
finite: outside the core it is the actual physical positive-row energy;
core differences are bounded by finitely many continuous physical point
functionals. The checked compact-source duality makes those functionals
continuous. The unique homogeneous-energy solution is the Fourier Green
solution L^-1 s. There is no additional decaying zero-energy homogeneous
solution, by positivity and the homogeneous Sobolev embedding.

Write y=(y_s,y_h) in the CONSTANT soft/high decomposition at k=0. The high
block L_hh is uniformly positive on the whole Brillouin torus: at zero it
has a fixed gap, and away from zero use L>=2a l. Its inverse has exponentially
decaying convolution coefficients, by analyticity in a complex strip.
The soft Schur symbol

 A(k)=L_ss-L_sh L_hh^-1 L_hs                              (8)

is analytic, nonnegative, has A(0)=0 and first derivative zero (positivity
at both signs of k), and is bounded below by2a l on the soft space.
Its convolution kernel has absolutely summable exponential moments,
zero zeroth moment and zero first moment. The block inverse and dyadic
Fourier integration by parts, exactly as in the checked one-pair matrix
Green proof, give uniformly in A with ||A||<=1

 |D^j y_s(r)|<=C_j(1+|r|)^(-1-j),
 |D^j y_h(r)|<=C_j(1+|r|)^(-2-j).                        (9)

Here finite differences are meant, and boundedly many core exceptions
are absorbed in the constants. The high decay gains one power because
L_hs(0)=0. The exchange symmetry is preserved by the soft/high split.

Choose a scalar smooth cutoff eta_R equal to one on |r|<=R and zero on
|r|>=2R. Cut only the soft field and reconstruct the high field by

 y_s^R=eta_R y_s,
 y_h^R=L_hh^-1[s_h-L_hs y_s^R].                         (10)

The high residual is then exactly zero before the final compact truncation.
The soft residual is [A,eta_R]y_s plus an exponentially small exterior
source. For its kernel a_h, write

 [A,eta]y_s(x)
 =y_s(x)sum_h a_h[eta(x-h)-eta(x)]
  +sum_h a_h[eta(x-h)-eta(x)][y_s(x-h)-y_s(x)].

The first sum is O(R^-2) by BOTH vanishing kernel moments, and the second
uses |D eta|<=C/R, |D y_s|<=C/R^2. On the annulus the full residual is
O(R^-3); away from it exponential kernel tails apply. Its squared l2 norm
is therefore O(R^-3), not O(R^-1). A naive cutoff of the full81-field can
produce an O(R^-2) high residual from L_hs, so that shortcut is invalid.

Outside3R the reconstructed high field is exponentially small, because
its sources are compact and its inverse is exponentially local. Truncate
there, impose the actual finite core constraints, and restore the exact
physical chi values throughout the fixed source core. Changes near that
core caused by(10) are exponentially small in R; they can be overwritten
with a smooth interior cutoff before the core projection. Truncate the Q
correction in configuration diameter as well. This produces a physical,
exchange-symmetric compact chi_R,A, linear in A, with support diameter<=C R:

 ||chi_R,A||_2^2 <= C R ||A||^2,
 ||chi_R,A||_1 <= C R^2 ||A||,
 ||H4(Phi_A+chi_R,A)||_2^2 <= C R^-3 ||A||^2,
 chi_R,A=chi_A on the fixed support of every F_B.         (11)

The l1 norm is in the physical translation-orbit basis. Matching fields
use(9); Q tails are exponentially summable. The map between physical core
and ordered coordinates has fixed finite dimension. The energy error is
O(1/R) as well, but the ordinary residual estimate in(11) is what the
many-pair argument below uses. This construction is not numerical knowledge
of chi; it is an existence argument from the actual threshold response.

## 3. A single compatible correction on each internal polynomial

Let D_R,z* be the pure four-site creator whose vacuum vector on a large
torus is the translated physical orbit vector chi_R,z^2/sqrt2. No independent
matching amplitudes are assigned. For a coherent internal vector z^n set

 B_n,L z^n = C_z^n Omega/(sqrt(n!) V^(n/2)),
 Psi_n,L,R z^n =sqrt(n!) V^(-n/2)
     [C_z^n/n! +D_R,z* C_z^(n-2)/(n-2)!]Omega.             (12)

The second term is zero at n<2. Both sides are homogeneous degree n in z,
so(12) defines unique linear maps on the ENTIRE Sym^n C5. At n=2 it is
exactly the physical incoming-plus-correction profile(Phi+chi_R)/V. The
binomial factor is fixed by this identity, not by a bosonic guess.
Every amplitude at every N is a single physical occupation coefficient.
Overlapping creation words vanish by hard-core nilpotence; alternative
matchings add with their actual phases.

For a k-particle vector f, define its pure creator A_f*. On a physical
m-particle sector,

 ||A_f*|| <=sqrt(binom(m+k,k)) ||f||.                     (13)

Proof: embed physical occupations isometrically into canonical SITE boson
Fock space, use the norm bound for symmetric tensor multiplication, and
project back to at most one boson per site. Because all factors are creation
operators, a forbidden duplicate can never become allowed again. The
compressed product is exactly the original hard-core product. This is a
norm comparison, not a pair CCR or identification of physical particles.

Using(11),(13), exact ||C_z Omega||^2=V, and finite-dimensional coherent
resolution/ordinary polynomial polarization gives

 ||Psi_n,L,R-B_n,L|| <= C_n sqrt(R/V).                   (14)

For the uncorrected map, projection onto mutually R0-isolated edges gives
exactly the checked unnormalized guarded frame T_n. The omitted auxiliary
anchor pairs have probability O(n^2/V); each physical occupation can have
at most(2n-1)!! matchings. Cauchy over those matchings therefore proves
||B_n,L-T_n||<=C_n/sqrt(V). The guarded Gram estimate then gives

 ||V_n* Psi_n,L,R-I|| <= C_n sqrt(R/V).                  (15)

No free translation action on arbitrary N=2n configurations is needed.
All contractions use literal physical torus occupations. Only individual
compact source words require L larger than their diameter.

## 4. Ordinary many-particle residual from connected sources

For this paragraph omit daggers on pure creators. Let

 K_r Omega=[ad_C^r H,D_R]Omega/r!,  0<=r<=3.

The fourth iterated commutator of H is pure creation, so K4=0. Multiplying
(5) by1+t^2D and commuting the remaining D gives the EXACT generating identity

 H e^(tC)(1+t^2D)Omega=e^(tC){
 t^2(W2+K0)+t^3(W3+K1)+t^4(W4+K2)+t^5 K3
                 +t^4D W2+t^5D W3+t^6D W4}Omega.       (16)

Its first source is the residual in(11), divided by sqrt2. The W3,W4
sources have fixed finite support and bounded orbit l2 norms. For r=1,2,3,
K_r is a bounded finite-degree local map from four-particle orbit amplitudes
to(4+2r)-particle orbit amplitudes, with norm independent of R. To see this,
expand H into local number/pair/triple words. Every nonzero commutator attaches
the D word at an original noncreation site of H, while C attachments have
bounded range there. Each input four-set has only boundedly many such local
attachments, and each output has only boundedly many input preimages; their
coefficients are bounded. The row/column Schur test proves the claim. Thus

 ||K_r Omega||^2 <= C V ||chi_R||^2 <= C V R.             (17)

Compact words embed with the usual exact V norm factor once C R<L/4;
nontrivial translation stabilizers cannot occur for one such compact word.
The disconnected D W_r products are not dropped: (13) bounds their norms
by C V sqrt(R). Extract degree n in(16), apply(13) to every remaining C,
and use polarization on the fixed five-dimensional internal space. This gives

 ||H_N Psi_n,L,R||^2 <=C_n[1/(V R^3)+R/V^2].             (18)

Here the norm is the operator norm from Sym^n C5. The first term is the
actual N4 residual. Connected degree>=3 sources and disconnected D W2
are both bounded by the second term. This explicitly prices collisions
with spectators; they are not assumed absent or independently attainable.

## 5. Leading energy and the required contraction count

Let F_z=H4 Phi_z and regard its translated creator as a fixed compact
four-site source. Expanding exact physical occupation contractions gives

 V B_n* H B_n =sum_(i<j) E_bare^(ij)+O(C_n/V),
 V (Psi_n-B_n)* H B_n
     =sum_(i<j) [chi_R*F]^(ij)+O(C_n R^2/V).             (19)

The second operator is not separately assumed Hermitian. The main term
is Hermitian because chi_R agrees with the Riesz correction on F's support.
For clarity, the coefficient count can be done on two arbitrary coherent
vectors w^n,z^n, then by polynomial polarization. The matched four-particle
component contributes

 binom(n,2) <chi_R,w^2,F_z^2> <w,z>^(n-2)/V.

This follows from the n2 normalization: D=chi/sqrt2, W2=F/sqrt2 and
n!/(n-2)!^2 times the(n-2)! permutations of distant spectator edges gives
n(n-1)/2. The same calculation gives E_bare in the first formula.

Here is the explicit error count behind(19), not an independent-fiber
ansatz. Make a bipartite overlap graph of the creation words in bra and
ket; identical physical sites join the words. Every site occurs once on
each side. Ordinary words have two sites; the special D and F words have
four. Leading graphs have one four-site component containing both D and F,
with those four physical sites equal, and n-2 two-site components. They
supply V^(n-1) before normalization. Every other graph, or an exclusion
between distinct leading components, has at most n-2 independently
translated components. A special four-site word may have long diameter R,
but its absolute weighted sum is at most||chi_R||_1<=C R^2. F and every
ordinary edge have fixed support; fixing a component anchor leaves only
boundedly many relative choices for all other local words. Summing those
choices gives at most C_n R^2 V^(n-2). The same argument without D gives
C_n V^(n-2) for the first formula. Graphs with no surviving hard-core
occupation contribute zero. This handles both repeated pairings and
nonmatching four-site source components.

Set deltaPsi=Psi-B. The exact identity

 Psi*H Psi=B*H B+Re(deltaPsi*H B)+Re(deltaPsi*H Psi)

uses Re X=(X+X*)/2. Equations(14),(18) bound the last term in norm by
C_n[1/(V R)+R/V^(3/2)]. Using(6),(19), therefore

 ||V Psi*H Psi-sum_(i<j)T0^(ij)||
  <= C_n[R^-1+R/sqrt(V)+R^2/V].                         (20)

This step uses the true compact response and full15 matrix, not a minimum
of coherent directions and not the new relaxed one-pair matrix pin.

## 6. Schur subtraction and scales

Put B=V_n*Psi and R_N=Q_n H Psi. Exact completion in the physical Q_n block is

 Psi*H Psi=B* S_n,L B+R_N*(Q_n H Q_n)^(-1)R_N.           (21)

This holds for any linear trial map, so does not assume it spans actual
eigenvectors. For large L, (15) makes B invertible. Use(1),(18) to bound the
second term after multiplication by V:

 V ||R_N*(QHQ)^(-1)R_N||
       <= C_n[L^2/R^3+R/L].                            (22)

The norm of sum T0^(ij) is at most binom(n,2)||T0||. Conjugation by B^-1
therefore changes the main matrix by O(C_n sqrt(R/V)). Combining(20)-(22)
and choosing R=floor(L^(3/4))/C_cut, where the fixed factor ensures that
all compact cutoff words fit before L/4 for sufficiently large L, gives(2).
The factor C_cut only changes constants, not either decisive exponent.

All n-dependence above comes from factorial/binomial creation bounds,
finite internal polarization and finitely many overlap graphs. Each graph
has at most O(n) words/sites, with choices bounded by(4n)! times C^n; its
local sums depend only on the fixed source and(11). Thus constants can be
bounded by exp[C n log(n+2)], with C independent of L,R. In particular
n<=sqrt(log L) makes C_n=L^o(1), the Gram loss and n2/L vanish, and all
estimates remain uniform. The checked Schur/eigenvalue comparison then
also identifies the actual low band up to the stated vanishing error;
the complementary levels have V lambda>=c L at fixed R0. This is a
periodic-cell result, not a physical large-system boundary replacement.

## Current proof-review boundary

The six/eight/fifth source control has passed on its literal fixtures.
The new analytic tail reconstruction, connected-contraction counting,
constant growth and complete argument above require a cold adversarial
read and a focused independent check before downstream use. In particular,
any unpriced long-range word contraction or invalid core-to-free embedding
would invalidate(11),(19) and the proposed many-pair conclusion. No such
step is supplied by the old fixed-N4 theorem alone.
