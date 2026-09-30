# Physical collision correctors and the many-pair Schur form

Cold-checked author theorem candidate, September30. Independent focused
checking remains pending; this is neither a formal review nor an accepted
downstream premise. The initial derivation remains immutable separately. The original supplied
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

The proposed conclusion, conditional on the precisely bound prior
physical gap and threshold-completion lemmas below, is

 ||V S_n,L - sum_(i<j) T0^(ij)|| <= C_n L^(-1/4),           (2)

for fixed n and sufficiently large odd L, with C_n<=exp[C n log(n+2)].
Here T0 is the ACTUAL15-channel N4 threshold form, extended naturally to
each symmetric pair of the n internal factors. This is a full operator
comparison, not a coherent-direction energy comparison. The constant growth proved in section6 gives uniform convergence for
2<=n<=floor(sqrt(log L)), with error L^(-1/4+o(1)). It is not an EOS.

The new proof consists of the following linked arguments:
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

Choose a scalar smooth even cutoff eta_R equal to one on |r|<=R and zero on
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
All contractions use literal physical torus occupations. Individual compact source words and connected labeled contraction graphs
are kept below the torus scale: impose C R+C n<L/4. Disconnected words
are estimated directly in the full physical torus Hilbert space.

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

## Source boundary and exact result obtained

All source identities and the actual open-proposal refresh are in
SOURCE_AND_PRIOR.json. Main was fetched and resolved to
30a9461ee19a49b99fa6628fe942f08e504e8903; selected methodology is
7146fe17a76de41badcaca3c3c7cac6d11eb2a00. The contract was frozen before
any new control. The following are mathematical inputs, with their exact
proof scopes retained:

* The landed native density note defines H0=S+mu Ddiag+W on the full qubit
  occupation space, including every spectator. It supplies the joint
  positive rows and isolated-dimer estimate used by the prior gap proof.
* The checked native-compatible-threshold REPORT04e13444 and periodic
  bridge b99af6fa supply the polar frame, all-N gap(1), trial bound and exact
  Schur comparison. Their focused check is25b3f255. Their auxiliary map
  intertwines guarded annihilation; it is not a global pair Fock isometry.
* Reviewed conditional PR9401 at ea3d4f6236160233f6f9e183b4b6eb5ba3252607
  supplies the full actual N4 energy completion, compact-source duality,
  threshold form and strict positivity. Its fixed-N4 limit alone does not
  imply this result. The threshold response used here is that physical
  completion's response, not a scalar or independently minimized fiber.
* The actual nine-bond symbol and its elementary matrix Green argument are
  reconstructed in the checked root matrix-pin proof56920870, with focused
  check fde7a525. The relaxed pin capacity value is not an input to the new
  leading interaction. Only the actual K symbol and its lower bound are used.

The proposed new conclusion is the complete operator comparison(2), for
fixed n and uniformly for2<=n<=floor(sqrt(log L)), at fixed mu,tau>0 and fixed
R0. It applies to the actual periodic qubit N=2n low band and all internal
vectors in Sym^n C5, including noncoherent vectors. In particular, it is a
compatible many-particle collision-correction construction, followed by a
lower comparison from an ordinary residual and the physical Q_n gap.
It does not identify a thermodynamic EOS, canonical fixed-density limit,
physical Neumann-cell boundary replacement, condensate or phase. The allowed
n grows extremely slowly while n/V tends to zero. No approximation by a
scalar gas and no all-N nonmatching gap have been used.

No historical novelty is asserted. Previous uniform-pulse quartics and
coherent upper threshold constructions remain prior work. The changed step
here is the full internal operator residual/Schur estimate with an actual
physical compatible correction and a quantitatively cut threshold response.

## Actual controls and author-check status

The two scripts were written for this route without importing prior runner
assembly. They are author controls, not independent mathematical reviews.
No large Hilbert-space enumeration, numerical fit, imported theorem or
floating threshold minimization was executed.

`check_connected.py` uses exact integer12H occupation rows at mu=tau=1.
All nine one-pair zero equations and26 selected literal Hermiticity entries
passed. The connected six- and eight-particle source coefficients at its
explicit configurations are respectively-12 and-64; the ten-particle
coefficient is0. The last check supports the operator identity ad_C^5 H=0
on one nontrivial fixture, not on every configuration. Actual execution:
exit0,1.200619 CPU seconds,1.234866 wall seconds,21,364,736 peak RSS bytes.

`check_overlap.py` computes exact Gaussian-integer physical N=6 contractions
with all hard-core exclusions. For the explicit four-site rectangle D,
line F, and two axial soft weight choices, at both L=17 and19 it finds

 ||D C_E1 Omega||^2/V=2V-8,
 ||D C_complex Omega||^2/V=4V-24,
 <D C_E1,D C_complex>/V=(1-i)(V-4),
 <D C_E1,F C_E1>/V=4.

These confirm the leading volume factor and nonzero bounded reconnection
errors in those fixtures. The last cross term has distinct D/F orbit shapes
and no leading volume term. All translation stabilizers are computed;
a separate six-point L=18 orbit has stabilizer6. Actual execution: exit0,
7.380396 CPU seconds,7.610648 wall seconds,57,163,776 peak RSS bytes.
The script does not use H, so it is a contraction/normalization control only.

Both controls had frozen30 CPU/90 wall/150 MiB/thread1 envelopes, checked
the original campaign deadline/STOP sentinel through their managed launch,
and completed within them. No failed mathematical assertion or repaired
fixture occurred in these two controls. Their full sources, stdout, stderr,
pre-execution freezes and actual execution receipts are preserved.

The initial complete DERIVATION.md was frozen at10:51:56 UTC before the
second control. This final report expands its cold-checked details; the
initial source remains unchanged. Parent independently froze a preliminary
reconstruction before opening the proof, with target/mechanism exposure
explicitly disclosed. That focused check has not yet been received. The
claim above is therefore an author proof candidate, not a review PASS,
retained result, audit outcome or permission for downstream scientific reuse.

## A. Physical exterior, completion and cutoff details

The physical graph has the18 offsets +/-2e_i and +/-e_i+/-e_j. In a four-set,
two distinct perfect matchings force all four vertices into one bounded
graph cluster. Thus the set of such translation classes is finite. The
same is true of any two-dimer configuration admitting a literal H move that
uses one site from each dimer. Choose a fixed core containing all of those
classes and their neighbors under H. Outside it, the two dimers are unique,
and every H term acts on one dimer or on neither. The particle term and
pair terms give exactly K on each; Ddiag and the triple penalty vanish.

For an ordered forward-edge pair, represent its first anchor by zero and
its second by r. At a matching four-set S with m(S) perfect matchings, put
its physical amplitude divided by sqrt(m(S)) in each of its2m(S) ordered
representations. With one-half the ordered counting measure this map J is
an isometry. Its range constraints, the forbidden shared-site coordinates,
and all differences between J P H P J* and the exterior free operator are
supported in finitely many relative coordinates. Add a positive operator
on that finite range complement. The resulting full ordered-space
operator differs from L only in a finite core block. The exterior isometry
has multiplicity one in unordered and two in ordered coordinates, so no
factor of two in L or its Dirichlet form is changed by this extension.

The actual K, in a forward-anchor Fourier convention, is as follows. Put
ell=4 sum_j sin^2(k_j/2), v_i=exp(-ik_i), P_v=v* v/3. The axial block is
2mu P_v+tau ell(I-P_v). For plane ij and eta=+/-1 put
q_eta=-eta[exp(-i eta k_j)+exp(-ik_i)]/2. Its block is
2mu I2+(tau ell-mu)q* q. The normalized constant U has two axial columns
(1,-1,0)/sqrt2 and(1,1,-2)/sqrt6 and one(-1,+1)/sqrt2 per plane. These
literal formulas give K(0)U=0, its four-dimensional high complement gapped,
and a ell I<=K<=(2mu+24tau)I. Reversing the relative-coordinate convention
interchanges k and-k in(7); all statements retain the actual index action.

For the physical N4 energy completion, Q is controlled in l2 by H>=mu Q;
this follows from the diagonal Ddiag>=1 on every nonmatching four-set.
The Q component of the stationary correction solves a gapped equation
whose right-hand side is supported in the fixed collision core. Indeed
Q H P only connects to P-core configurations, and H is finite range.
Its resolvent Neumann series therefore has an exponential tail in diameter.
The number of translation classes of diameter at most r is O((1+r)^9),
so summing l2 tails over unit shells gives the asserted l1 tail as well.

For compact physical test vectors, the free L energy of their J images is
bounded by their physical energy plus a finite sum of squared core values.
All these values are continuous in the physical energy norm by the checked
compact-source duality. Consequently J extends continuously into the free
homogeneous energy completion. Include the compact difference between J Phi
and the free constant incoming tensor. Its sum with J chi is the y used in
section2. It satisfies L y=s off the core with s=0 there, hence with a compact
source s everywhere. The finite core values are bounded linear functionals
of A, so all source bounds are uniform on the unit15-dimensional sphere.
The free homogeneous completion is embedded in l6 by L>=2a Delta. Testing a
homogeneous zero solution by its energy approximants forces zero energy;
the l6 representative is then zero. This proves that y is the Green
response, excluding an additional unpriced homogeneous part.

For completeness, the decay estimates used in(9) follow directly from
Fourier integration. On a dyadic shell |k|~s, the inverse soft Schur symbol
and its m-th derivatives are O(s^(-2-m)). The compact-source Fourier
polynomial and the analytic high inverse have bounded derivatives. A j-th
lattice difference adds j factors O(s); M integrations by parts on a smooth
shell give a contribution bounded by

 C s^(1+j) min(1,(s|r|)^(-M)).

Sum shells below and above s=|r|^-1, choosing M>j+2. This gives
C(1+|r|)^(-1-j). Away from zero the smooth symbol has faster decay. Since
L_hs(0)=0, the high response carries an extra factor s and has the second
bound in(9). Analyticity of the high inverse on a complex strip follows
from compactness of the real torus and its uniform positive gap; it implies
absolute exponential summability of its convolution coefficients. This
argument uses a matrix inverse throughout and does not diagonalize the
soft channels or assume commuting symbols.

In the cutoff commutator split, restrict first to |h|<=R/4 and
R/2<=|x|<=3R. Taylor's formula for eta, the two exact kernel moments and
the difference bound on y_s give O(R^-3) pointwise. The omitted |h|>R/4
kernel sum is exponentially small times a fixed polynomial in R. Inside
R/2 and outside3R every nonzero cutoff difference similarly uses an
exponentially long convolution step, except for the exponentially decaying
effective source b=s_s-L_sh L_hh^-1 s_h. Thus the total squared residual
is bounded by C R^3 R^-6 plus exponential errors. This is a global l2
bound, not merely a shell calculation.

Choose the scalar cutoff even under r->-r. All blocks and inverses commute
with the ordered-edge exchange involution, so the reconstructed field has
the correct symmetry. The new high field differs from the old one at every
fixed core coordinate by O(exp(-cR)); the soft field agrees there exactly.
Overwrite a fixed slightly enlarged core with the true physical correction,
using a fixed finite-dimensional map. This restores every repeated-matching
and forbidden-overlap constraint and changes the residual exponentially.
Cut the high field beyond3R and the nonmatching field at diameter3R; both
changes and their H images are exponentially small. H is bounded on N4,
uniformly in volume. These operations establish all four statements(11)
on physical amplitudes. No arbitrary ordered field is treated as physical.

## B. Labeled contraction proof and uniform constants

Here is a counting formulation that avoids translation-orbit assumptions
at many-particle N. Expand every creation product as a sum over labeled
word slots. An ordinary slot has two distinct sites joined by a graph edge;
its offset is one of nine forward choices and its coefficient is uniformly
bounded for ||z||=1. A W_r slot has2r sites in one of a fixed finite list of
compact shapes. A D slot has four sites; choose one representative and one
anchor per translation class, with absolute coefficient sum O(R^2). Each
slot is a pure site-creation monomial. Within each bra or ket, coincident
sites make the term zero; otherwise the physical scalar product is one
exactly when the two sets of2n sites agree. No bosonic pair identification
is used in this expansion.

For a surviving term, join its bra and ket slots by their common sites.
The resulting bipartite graph has no isolated vertex. A component carries
an equal number of bra and ket sites; write this number2m. The sum of m
over all components is n. Components made only of ordinary words have
m>=1, and m=1 means identical graph edges. A component containing a
four-site D or F word has m>=2. A component with a W_r word has m>=r.

For <D C^(n-2),F C^(n-2)>, the largest possible component count is n-1.
It is attained only by a single m=2 component containing both D and F
and n-2 identical-edge components. If D and F are in separate components,
they each require m>=2 and the count is at most n-2. If they lie together
with additional slots, that component has m>=3, again losing one count.
The sole n-1 family has exactly equal D/F four-sets. Choose its common
anchor, sum the physical four-set coefficient, and match the n-2 labeled
ordinary slots in(n-2)! ways. In the unrestricted count their summed
contribution is V^(n-1)<D,F>_orbit <w,z>^(n-2). Intersections between
different components are excluded in the physical state; each intersection
identifies at least one pair of component anchors and so loses one V.
For each fixed collection of shapes there are only O(n^2) possible such
site identifications. Crucially this is a count of the actual sites of D,
not every site in the diameter-R region; no R^3 volume factor is inserted.

Once a component anchor and its D shape, if any, are fixed, any adjacent
ordinary or compact special word has at least one fixed site. It then has
only boundedly many possible anchor/orientation choices. Traverse a
spanning tree of the component to bound all relative choices. A nonleading
graph therefore costs at most C^n V^(n-2), multiplied by the absolute D
shape sum C R^2. The number of labeled incidence patterns is at most
(2n)! times C^n times a fixed polynomial in n. Thus the second error in(19)
is bounded as stated, uniformly over w,z on the unit sphere. The same
argument for bra C^n and ket W2 C^(n-2) has one m=2 component with two bra
ordinary slots. The binomial choice of those slots, followed by(n-2)!
spectator permutations, gives binom(n,2) E_bare. A W3 or W4 ket slot has
m>=3 and contributes only an O(C_n/V) error after the V normalization.
This proves the first line of(19) including its other connected sources.

For precision on the coefficient in the second line, both normalized maps
have the factor sqrt(n!)/(n-2)!, and D=chi/sqrt2, W2=F/sqrt2. The common
component and its spectators therefore yield

 [n!/(n-2)!^2] [(n-2)!/2]
 <chi_w^2,F_z^2> <w,z>^(n-2)/V
 =binom(n,2)<chi_w^2,F_z^2><w,z>^(n-2)/V.

The tensor with this coherent kernel is precisely sum_(i<j)T^(ij) on the
symmetrized n-fold space, for any operator T on Sym^2 C5. This argument
does not minimize T on coherent directions.

The finite-volume estimates can be taken in the regime C R+C n<L/4.
Then every connected labeled graph using one D slot can be unwrapped
without a winding ambiguity. Alternatively its spanning-tree bound holds
directly on the torus. Graphs with independent components need not have a
free common translation orbit: their anchor sums occur as labeled site
sums, with all stabilizer multiplicities already included in the original
physical contraction. The explicit stabilizer control tests this distinction.

To pass from coherent bounds to full operator norms without ill-conditioned
coefficient extraction, use normalized unit-sphere measure on C5. On
Sym^n C5, with d_n=binom(n+4,4),

 d_n integral |z^n><z^n| dz=I.

This identity follows by unitary invariance on the symmetric power and
tracing. If a linear map M obeys ||M z^n||<=m on the sphere, then
||M||^2<=tr(M*M)<=d_n m^2. If an operator E has coherent kernels bounded by
e for all w,z, the two resolutions of the identity give the safe bound
||E||<=d_n^2 e. These polynomial factors are absorbed into C_n.

For the residual source maps K_r, r<=3, each input four-set has a bounded
number of touched sites and hence a bounded number of local H/C attachment
choices. An output has at most ten sites; choosing which ones came from
the input and recovering any removed input sites uses only the same fixed
local neighborhoods. Both row and column sums are therefore bounded
independently of R. This supplies the two sides of the Schur test used
in(17), including corrections whose two constituent pairs are far apart.
Disconnected D W_r terms use only the genuine creation bound(13).

Finally, repeated application of(13) uses at most2n factorials and bounded
source orders; the graph counts use at most(2n)! incidence choices and
C^n local choices; frame comparison uses at most(2n-1)!! matching choices.
Coherent resolution adds only powers of d_n. Increasing a fixed constant
C depending on mu,tau,R0 and the fixed core therefore bounds every constant
in(14)-(22), and the harmless final conjugation, by exp[C n log(n+2)].
For n<=sqrt(log L), this is L^o(1), while C R+C n<L/4 for R~L^(3/4).
The polar-frame Gram loss and trial-to-gap ratio tend uniformly to zero.

For the last spectral statement, the prior trial estimate is
theta<=60 max(mu,2tau) s_R0 n(n-1)/[V(1-delta)], with
s_R0=(2R0+9)^3-(2R0-7)^3. Thus theta/Delta=O(n^2/L), uniformly in this
range. If lambda_j is the actual j-th level and s_j the Schur eigenvalue,
lambda_j<=s_j<=[1+theta/(Delta-theta)]lambda_j for j<=d_n. Combining with
(2) gives the same o(1) comparison of V lambda_j with the eigenvalues of
sum T0^(ij). All other levels are at least Delta, so their V-scaled lower
bound grows linearly in L. These are periodic-sector statements only.
