# All-state dilute lower bound and thermodynamic limits

This is current supporting proof owned by `NATIVE_DILUTE_THERMODYNAMICS_BOUNDED_THEOREM_NOTE_2026-09-30.md`,
under exactly its supplied full-qubit Hamiltonian and fixed positive mu,tau.
It has no separate claim classification or runner. The owner directly links
and binds it as a primary input. Its complete argument and interactions are
part of that one scientific unit. Equation numbers are local to each named
part below. Unsubscripted energy forms always use actual occupation amplitudes.

Inputs are the [landed local pin and all-density bound](NATIVE_QUBIT_PAIR_DENSITY_ONSET_BOUNDED_THEOREM_NOTE_2026-09-30.md),
the actual full threshold form in the [threshold source](NATIVE_FOUR_PARTICLE_THRESHOLD_BOUNDED_THEOREM_NOTE_2026-09-30.md), and
this unit's [physical boundary](NATIVE_DILUTE_PHYSICAL_BOUNDARY_PROOF_2026-09-30.md) and [cell-interaction](NATIVE_DILUTE_CELL_INTERACTION_PROOF_2026-09-30.md) proofs.
The exact uniform trial is proved in the canonical note. Every additional
counting, finite-mode and thermodynamic step is given here.

# Part I. Physical particle separation and internal variance

## 1. Global bad-particle estimate with its actual R-cubed growth

Let F_b count occupied x whose Chebyshev b-cube contains at least three
particles. For integer b>=10 and L>=10b, partition each coordinate circle
into intervals with lengths between b and2b, enlarge each product box B
by b to C and then by one to C+. For x in B its b-cube lies in C, so
F_b<=sum_B N_C 1_(N_C>=3). The expanded rectangles C+ have aspect ratio
at most two, volume at most125b^3 and incidence at most125 at each site
or selected free edge. In one dimension at most five intervals expanded
by b+1 can cover a point. The landed local spectator-pin bound

    <N_C 1_(N_C>=3)> <= <D_C>+896|C+| Egrad15_C+

therefore gives

    <F_b> <=125<D>+14000000 b^3 Egrad15.

Here D_C retains the actual full-torus neighbors; it is not a deleted-neighbor
polynomial. All restrictions are on actual annihilation outputs before
positive gradient sums are taken.

Let B_b count particles outside b-isolated graph dimers. A singleton has
D contribution one. Every vertex in a graph component of size at least
three has two other component vertices within at most two graph steps,
hence within Chebyshev distance four; it is counted by F_b. For an isolated
dimer rejected by the b-isolation condition, one endpoint sees its partner
and a third particle in its b-cube; charge its two particles to that F_b
endpoint. Different dimers have disjoint endpoints. Thus, pointwise,

    B_b <= D+2F_b.

Together with H>=mu D+a Egrad15 this proves the deliberately loose bound

    <B_b> <= (C_B b^3/a)<H>,       C_B=28000322.

Indeed D+2F_b<=251D+28000000b^3 Egrad15, and a<=mu and b>=1 make
28000251 a safe constant; the larger C_B preserves the stated common
normalization. The estimate holds for every state and particle sector.
It counts lost particles, not energy or a global no-defect projection.

## 2. Exact finite-five-mode sphere identity

For n particles in the auxiliary symmetric space Sym^n C^d, let gamma1 and
gamma2 be normalized reduced density matrices. With normalized sphere
measure dz, d_n=binom(n+d-1,d-1), the measure

    d_n <z^n,gamma_n z^n> dz

has total mass one. Its two-body moment is

    tilde gamma2=[n(n-1)gamma2
       +4n P_sym(gamma1 tensor I)P_sym+2P_sym]/[(n+d)(n+d+1)].

This identity can be derived directly from

    integral z^alpha conjugate(z)^beta dz
        =delta_(alpha,beta)(d-1)! alpha!/(|alpha|+d-1)!.

One derivation takes the normalized coherent resolution at n+2 and commutes
its two tested annihilators past the two creators:

    a(v)^2 a(v)^dagger^2
      =a(v)^dagger^2 a(v)^2+4a(v)^dagger a(v)+2

for ||v||=1. Testing every v tensor v and polynomial polarization fixes
all matrix entries on the symmetric square, including complex off-diagonal
entries. This is finite-dimensional auxiliary algebra, not a physical-pair
CCR. The auxiliary space is only used after the proved physical compression.

The extra terms are positive and have complementary trace1-p with
p=n(n-1)/[(n+d)(n+d+1)]. Thus
||gamma2-tilde gamma2||_1<=2(1-p). For d=5,n>=2,

    n(n-1)(1-p)<=12n+30<=27n.

For every positive full15-dimensional T and t_coh(T)=min_unit_z<T>_(z^2),

    <sum_(i<j)T^(ij)>
      >=t_coh(T)n(n-1)/2-27||T||n.

The harmless n=0,1 cases follow from positivity. The identity permits
arbitrary complex, mixed and fragmented internal states and independent
coherent measures in different cells. No claim about condensation is used.


# Part II. Particle tails and the all-state lower bound

## 1. An actual total-cell-count tail lemma

Let the physical torus have side L, fix disjoint vertex cubes Lambda_j of
side ell with L>=10ell, and write N_j for their actual particle numbers.
For an integer b>=10, let B_b count global particles outside b-isolated
actual graph dimers. Part I above gives the unchanged-law estimate

                         B_b <= (C_B b^3/a) H0,
 C_B=28000322,       a=min(tau,mu/12),       L>=10b.               (1)

Choose one endpoint as an anchor of each global b-isolated dimer. Distinct
anchors have Chebyshev separation greater than b. If a dimer has an endpoint
inside Lambda_j, its anchor is in its width-two enlargement. Grid boxes of
side b+1 therefore contain at most one such anchor. When b<=ell/8 and ell
is sufficiently large, at most8ell^3/b^3 grid boxes meet that enlargement.
The number of particles in Lambda_j belonging to globally b-isolated dimers
is consequently at most

                             16ell^3/b^3.                       (2)

This explicitly includes dimers crossing the cell face. Local coordinates
on the width-two enlargement are unambiguous since L>=10ell; periodic
seams do not alter the packing. The estimate uses actual occupation sets,
not a bosonic particle count.

Fix K>=2^18 and take

              b=ceil[(64ell^3/K)^(1/3)].                        (3)

For fixed K and sufficiently large ell, b>=10, b<=ell/8, and
b^3<=128ell^3/K. By(2), each cell has at most K/4 good particles. Thus on
every occupation, N_j>K implies that at least N_j/2 of its particles are
counted by B_b. Disjoint cells give the exact diagonal inequality

 sum_j N_j 1_(N_j>K) <=2 B_b.

For every quantum state, including coherent states and number fluctuations,

 sum_j <N_j 1_(N_j>K)>
            <= C_tail (ell^3/K) E,
 C_tail=256 C_B/a,       E=<H0>.                                (4)

The statement holds for every translation of the cell family. It controls
lost particles, not lost energy or a global no-defect norm. High-number
cell energies may be discarded only because the comparison cell operators
are positive. Boundary singleton sectors forbid silently replacing this
argument by a uniform N_j^2/ell^3 coercivity of H_plus.

## 2. The actual low-sector estimate

Put E_*=||T0|| and t0=min_(||z||=1)<z^2,T0 z^2>. Both are finite and positive
for the supplied model, with the full fifteen-channel physical normalization.
Fix0<eta<=1/2 and the finite K above. The actual cell-interaction proof implies that gamma>0 can be fixed sufficiently small and then
ell sufficiently large so that the actual positive cell operator obeys
for every physical particle number0<=M<=K,

 H_plus|_(N_j=M)
   >= [c_eta M^2-C_* M]/ell^3,
 c_eta=(1-eta)t0/8,       C_*=16 E_*.                            (5)

Here gamma may depend on eta,K but not ell or the state; assume gamma<=1.
The thresholds in ell can depend on all these fixed parameters. No estimate
uniform as K increases is presumed.

For precision, here is the derivation of(5) from that fixed-n cell theorem.
For even M=2n, finite5-mode sphere moments give for every internal n-pair
state, including fragmented and complex states,

 <sum_(i<j)T_eta^(ij)>
       >= [t_coh(T_eta)/2] n(n-1)-27 E_* n.

One may verify this without a dilute-gas theorem: the normalized two-body
coherent-mixture density is

 [n(n-1)gamma2+4n P_sym(gamma1 tensor I)P_sym+2P_sym]
                                      /[(n+5)(n+6)].

The positive added terms have the complementary trace. The resulting trace
norm bound gives the displayed27 E_* n error. Part I above proves this identity; the energy-minimizing state is not
assumed coherent.

Since (1-eta)T0<=T_eta<=T0, the right side is at least
c_eta M^2-14 E_* M. Choose gamma so that the cell Schur error is at
most E_* simultaneously for the FINITELY many n<=K/2. Its actual low-energy
spectral comparison has relative error tending to zero as ell grows; choose
ell large enough to price that too by E_*. For M>=1 these two absolute errors
are bounded by2E_* M. This yields(5). The M=0 vacuum is exact. For odd M,
the physical-cell gap c(eta,gamma)ell^-2 eventually exceeds the
right side of(5) for every fixed M<=K, so the same bound holds. Odd sectors
are not silently projected away.

All dependencies of(5) have now been proved in this unit: the actual
cell-interaction theorem, finite-mode identity, odd-sector gap and physical
boundary comparison. Only finitely many sectors are used for each fixed K.

## 3. Particle-number cutoff and all-state Jensen

Each H_plus preserves its own TOTAL physical particle number. Define the
commuting diagonal variable Y_j=N_j 1_(N_j<=K). Its high-number sector may
be dropped by positivity, and(5) gives the full-cell operator lower form

                 H_plus,j >= [c_eta Y_j^2-C_* Y_j]/ell^3.        (6)

No restriction on a state's support or probability of having defects is
made. The physical cell may be entangled with all other cells.

For any fixed tiling of J cells, state Cauchy and scalar Jensen give

 sum_j <Y_j^2> >=(sum_j <Y_j>)^2/J.

The same inequality holds after averaging translated tilings: apply Jensen
also to that average. For divisible tori J ell^3=L^3. For general L, use
J=floor(L/ell)^3 disjoint complete cubes and a translated remainder. The
covered fraction is at least1-3ell/L. Translation averaging therefore
loses at most3ell Nmean/L particles to the remainder. Safe diagonals optimize
all omitted neighbors, including this remainder, so the original positive
row comparison remains valid. No state is cut or replaced.

A site's probability of belonging to a retained cell boundary is at most
12/ell. Consequently the exact original-law penalty debit is still at most
12 gamma Nmean/ell^3. Since J ell^3<=L^3, the averaged Jensen lower term is
at least c_eta (Ymean/L^3)^2 L^3, where Ymean is the averaged retained count.
Equations(4),(6) imply for every state

 Ymean/L^3 >= (1-3ell/L)rho-C_tail(ell^3/K) E/L^3,
 E/L^3 >= c_eta (Ymean/L^3)^2
                              -(C_*+12gamma)rho/ell^3.          (7)

Use the positive part of the first lower bound when necessary. Here
rho=Nmean/L^3. These estimates apply to arbitrary particle-number mixtures,
not just canonical or translation-invariant states. The added boundary term
has been explicitly subtracted, not treated as part of the original law.

## 4. Dilute lower coefficient with all ordered limits

Take a fixed finite energy ceiling C_E>t0/8; states with E/L^3>C_E rho^2
already satisfy the desired asymptotic lower comparison. For the remaining
states suppose E/L^3<=C_E rho^2. Choose a fixed mesoscopic mean parameter
m>0 and, at each small density, an integer ell such that

                            rho ell^3 -> m.                     (8)

Choose K fixed, as large as desired compared with m, before letting rho
shrink. With eta fixed, choose gamma and the cell threshold as in section2.
Then rho->0 makes ell->infinity and eventually satisfies every fixed-K,
fixed-R0 and fixed-parameter cell hypothesis. Taking L->infinity first
removes the remainder fraction in(7). It follows that

 liminf_(rho->0) liminf_(L->infinity) E/(rho^2 L^3)
 >= c_eta [1-C_tail C_E m/K]_+^2 -(C_*+12gamma)/m.               (9)

This is uniform over the states under the stated energy ceiling. All limits
use the actual original H0. There is no hidden n~sqrt(log ell) or other
uniform growing-n assumption: for each chosen K there are only finitely
many particle sectors, and rho is taken small after their thresholds.

Finally choose m arbitrarily large, K/m arbitrarily large, and eta
arbitrarily small, in that order of parameter selection before the dilute
limit; gamma is chosen for the selected finite K,eta. Since0<gamma<=1,
its final debit is bounded by12/m. Equation(9) then yields the full-carrier dilute lower bound

             liminf E/(rho^2 L^3) >= t0/8.                      (10)

The coefficient is not assumed from a coherent ansatz: it arises from the
full15 pair form and the exact finite5-mode density-matrix identity, allowing
fragmentation and different cell states. This is a lower bound only. The upper construction and thermodynamic conclusions are proved separately
below and in the canonical note.


# Part III. Mean energy, grand energy and density slope

Use the canonical definitions e_L(rho),g_L(nu), t=t0, c=t/8,
c0=a/99090432 and h_*=182mu+240tau. The landed all-density coercivity is
H>=c0 N(N-2)/V, so every state satisfies

    <H>/V>=c0(rho^2-2rho/V).                              (5)

Dephasing in N preserves mean and energy. Thus e_L is the convex hull of
sector ground energies, continuous and convex on[0,1], with

    e_L(0)=0, 0<=e_L(rho)<=h_*rho,
    g_L(nu)=min_(0<=rho<=1)[e_L(rho)-nu rho].              (7)

The upper bound uses the vacuum/fully occupied mixture, not an equality
for the full-occupancy energy. Here and throughout, e_L constrains the
MEAN number. The fixed-sector energies are treated in Part IV.

## 1. Thermodynamic limits actually used

First prove the grand limit rather than assume it. Fix a bounded chemical-
potential interval |nu|<=nu_max. Tile a large torus by J=floor(L/ell)^3
complete cubes of side ell and a remainder. Replace H0-nu N by the sum of
J independent periodic ell-cube copies and zero on the remainder. Only
terms meeting block faces or the remainder change. A term centered farther
than two sites from a face is unchanged. The number of changed centers is
at most C[L^3/ell+ell L^2], and every changed local term has uniformly bounded
norm. Onsite chemical terms cost at most nu_max times the remainder volume.
Therefore the operator difference has norm at most

 C(h_*+nu_max)[L^3/ell+ell L^2].

The artificial periodic copies are used ONLY in this bounded-norm
thermodynamic comparison, not as physical lower cells in a dilute proof.
Their minimum energy adds because their Hilbert tensor factors are disjoint.
The variational principle gives a two-sided bound. Since |g_ell|<=h_*+nu_max
and Jell^3/L^3 differs from one by O(ell/L),

 sup_(|nu|<=nu_max)|g_L(nu)-g_ell(nu)|
             <=C(h_*+nu_max)[ell^-1+ell/L].                      (9)

For every fixed ell send L to infinity, then let ell grow. This makes g_L
uniformly Cauchy on the chosen interval. Hence a finite limit g(nu) exists
for every real nu, uniformly on compact nu intervals. It is concave and
1-Lipschitz because each g_L has those properties. The proof uses no
hypothesis on ground-state uniqueness or spatial order.

The mean-constrained limit near zero follows by elementary convex duality.
Nonnegativity, convexity and e_L(0)=0 imply e_L is nondecreasing. For
0<=rho<=1/2, its supporting slopes can be chosen in[0,2h_*]: every right
slope below1/2 is bounded by the secant to1, at most h_* /(1-rho).
The finite convex hull in(7) consequently has the exact representation

 e_L(rho)=sup_(0<=nu<=2h_*)[g_L(nu)+nu rho],       0<=rho<=1/2.

Uniform convergence in(9) implies uniform convergence of e_L on this
interval to

 e(rho)=sup_(0<=nu<=2h_*)[g(nu)+nu rho].                          (10)

This proves the claimed MEAN-constrained thermodynamic limit, not the
existence of an exact-N thermodynamic limit. The argument would extend to
any compact density interval below one with a larger bounded slope interval,
but that extension is unnecessary here. From(5), e(rho)>=c0 rho^2.

No thermodynamic rate in(9) is divided by a vanishing rho^2 or nu^2 at fixed
volume. Volume convergence occurs first throughout the dilute conclusions.

## 2. An upper at exactly the prescribed mean density

The exact unitary trial's density need not be monotone. Continuity
alone suffices. Fix epsilon, z and compact chi before all limits. Let
r_L(u)=<N>_(psi_L(u))/V. For a sufficiently small prescribed rho>0,

 r_L(0)=0,       r_L(sqrt rho)>=2rho-B_chi rho^2>=rho.

The intermediate value theorem supplies u_L in[0,sqrt rho] with
r_L(u_L)=rho exactly. Set s_L=u_L^2. The canonical note's uniform unitary bounds give, uniformly in L,

 |s_L-rho/2|<=B_chi rho^2/2,
 e_L(rho)<= (t_chi/8)rho^2+C_chi rho^3.                          (11)

For example the energy error follows from s_L<=rho and
|s_L^2-rho^2/4|<=3B_chi rho^3/4. No fixed particle-number projection is used;
the exact state still has its actual sector distribution. For fixed chi,
let L tend to infinity, then rho down to zero, and only then improve its
threshold accuracy. This proves

 limsup_(rho down0)e(rho)/rho^2<=t/8.

Part II's all-state lower has exactly that mean-density/volume order
and applies to every e_L-minimizing state. Its energy-ceiling alternative
causes no gap: the upper(11) supplies a fixed O(rho^2) ceiling for small rho,
and states above such a ceiling already satisfy the lower comparison.
It follows that

                         e(rho)=c rho^2+o(rho^2).                (12)

This matching statement concerns the precisely defined convex mean-number
problem defined in the canonical note. It does not assert equality of a canonical fixed-N quantity.

## 3. Confinement of grand minimizers before the dilute optimization

For any finite-volume ground state Gamma_nu,L of H0-nu N with nu>0,
comparison with the vacuum gives g_L(nu)<=0. Combining with(5) yields

                 rho_nu,L <= nu/c0+2/V.                         (13)

This ALL-density step excludes a remote positive-density minimizer from
invalidating the dilute optimization. A lower known only near rho=0 would
not justify(13). For fixed sufficiently small nu, all thermodynamic density
accumulation values lie in[0,nu/c0], a subset of[0,1/2].

For clarity, take any sequence of finite-volume grand ground states and a
subsequence on which rho_nu,L converges to r. Such a subsequence exists by
boundedness. Uniform mean-energy convergence in(10) gives

 g(nu)=e(r)-nu r.

At finite volume the ground state attains e_L at its own mean; otherwise
a state of the same mean with lower H0 energy would lower H0-nu N. Uniform
convergence and continuity justify passing the moving mean to r. Conversely
for any fixed small density s, variational comparison gives

                        g(nu)<=e(s)-nu s.                       (14)

Given delta in(0,c), equation(12) bounds e(r) between(c-delta)r^2 and
(c+delta)r^2 for every sufficiently small r. Confinement(13) puts every
minimizing accumulation r in that range when nu is small. Minimizing the
lower quadratic over all r>=0, and testing(14) at
s=nu/[2(c+delta)], gives

 -nu^2/[4(c-delta)] <= g(nu) <= -nu^2/[4(c+delta)].                (15)

Now send nu down to zero and then delta down to zero. This proves the grand
asymptotic in the canonical statement. It also recovers directly the older variational upper
coefficient -2/t, now matched by a full-carrier lower. For nu<0, H0>=0
makes the finite-volume vacuum the unique ground state and g(nu)=0. At
nu=0, the coercivity or exact kernel makes all thermodynamic ground-density
accumulation values zero.

## 4. Ground-density slope from concave secants

No differentiability of g is needed. For any finite-volume ground state at
nu, using it as a trial at nu+h and nu-h gives, for0<h<nu,

 [g_L(nu-h)-g_L(nu)]/h <=rho_nu,L
                      <=[g_L(nu)-g_L(nu+h)]/h.                 (16)

The signs follow from the actual perturbation -nu N. Equation(16) is valid
for every density matrix supported on the ground eigenspace, including
mixtures of degenerate particle sectors. Let L grow and take any density
accumulation value rho_gr(nu); convergence of g_L preserves both bounds.
Set h=theta nu with fixed0<theta<1 and use g(nu)=-kappa nu^2+o(nu^2),
kappa=2/t. Then

 kappa(2-theta)+o(1) <=rho_gr(nu)/nu
                                  <=kappa(2+theta)+o(1).

First send nu down to zero, then theta down to zero. The bounds do not depend
on the choice of ground state or accumulation subsequence, proving the canonical density ratio.
Equivalently all concave supergradient densities -partial g(nu) have that
same leading ratio wherever they are considered. No derivative of those
densities or second derivative of g follows.

The corresponding internal H0 energy per volume in such grand ground-state
accumulations is g(nu)+nu rho_gr(nu)=(2/t)nu^2+o(nu^2). This is a consequence
of the exact identity H0=(H0-nu N)+nu N and the proven density ratio; it does
not identify the state, its polarization, correlations or excitations.


# Part IV. Exact particle-number upper transfer

For any integer0<=N<=L^3 write E_L(N) for the lowest actual energy in
that sector. Fix a compact correction chi, t=t_chi,B=B_chi,D=D_chi and h*=h_*.
The canonical unitary bounds hold on every sufficiently large periodic
block; all such sectors exist in its actual qubit carrier. Fix rho in(0,1)
before every thermodynamic/block limit in this part.

## 1. Tune the actual finite-block mean by continuity

Fixchi and write B=Bchi,D=Dchi,t=tchi. Assume 0<rho<=min(1/2,1/B); the known B is positive. Let v=u². At v=rho/4 the upper density bound from the canonical uniform trial bounds is

 2v+Bv²=rho/2+B rho²/16<rho.

At v=rho the lower density bound is2rho-B rho²>=rho. The intermediate-value theorem therefore gives some actual u_ell with

 Tr tau_ell(u_ell)N/ell³=rho,   rho/4<=v_ell<=rho.             (5)

Neither uniqueness, monotonicity nor differentiability is used. The uniform remainder then implies

 |v_ell-rho/2|<=B rho²/2,
 v_ell²<=rho²/4+(B/2)rho³+(B²/4)rho4,
 v_ell³<=rho³.

Since B rho<=1, its energy e_ell obeys

 e_ell:=Tr tau_ell(u_ell)H0,ell/ell³
      <=t rho²/8+[D+3tB/8]rho³.                             (6)

Thus Cchi=Dchi+3tchi Bchi/8 suffices. This tuning occurs independently on each finite block size but with the SAME error constants. The proof does not project a variable-number trial onto a presumed typical number.

## 2. Number-sector block transfer lemma

Fix any ell>=5, put m=ell³, and let tau be any density matrix of the actual periodic block with exact MEAN particle number rho m,0<rho<1. Let e=Tr tau H0,ell/m. Then for EVERY sequence of integers N_L with N_L/L³->rho,

 limsup_L E_L(N_L)/L³ <= e+24h*/ell.                         (7)

Here is a constructive proof. Dephase tau in the block number sectors. Since N and H commute this changes neither mean nor energy. Write the dephased state as sum_(k=0)^m p_k tau_k, where tau_k is a normalized density in the exact k sector when p_k>0. For p_k=0 choose any density in that nonempty sector. Hence

 sum p_k k=rho m,   sum p_k E_k=m e,
 E_k=Tr tau_k H0,ell,   |E_k|<=h*m.                          (8)

Tile the large torus by B_L=floor(L/ell)³ disjoint contiguous ell-cubes and let R_L=V-mB_L be the unfilled sites. R_L/V->0 at fixedell. Reserve r_L complete cubes, leaving B'_L=B_L-r_L regular cubes. The precise vanishing reservation will be specified below.

For k<m set n_k=floor(B'_L p_k), and set n_m=B'_L-sum_(k<m)n_k. All n_k are nonnegative integers and sum to B'_L. Since each of the first m errors lies in(-1,0] and their opposite sum is the last error,

 sum_k |n_k-B'_L p_k|<=2m,
 |sum_k k n_k-B'_L rho m|<=2m²=:D_m,
 |sum_k n_k E_k-B'_L m e|<=2h*m².                            (9)

The inequalities deliberately overcount. In particular the last sector can be used for rounding even when p_m=0; no nonexistent conditional state is needed because tau_m was chosen above. Put exactly n_k of the regular cubes in state tau_k. Each product term is in one precise TOTAL number sector, despite possible mixing within each tau_k.

Let d_L=N_L-rho V, q=min(rho,1-rho)>0. For large L choose, for example,

 r_L=ceil((|d_L|+D_m+2)/(q m))+1.                            (10)

Then r_L/B_L->0 because d_L=o(V), while eventually r_L<B_L. Let U_L=R_L+r_L m be the number of reserved/unfilled sites. It satisfies q U_L>|d_L|+D_m+1. If N_reg=sum k n_k, equations(9)-(10) give

 0<=N_L-N_reg<=U_L.                                        (11)

Indeed N_L-N_reg=rho U_L+d_L-(N_reg-rho m B'_L), and both its lower bound and its distance from U_L are positive by the choice of q U_L. The difference is an integer. Fill exactly that many of the U_L free sites in a computational product state and leave the others empty. Every integer between0 and U_L is possible on actual M2 sites. The resulting full density matrix is supported in EXACT sector N_L, with no postselection, no normalization loss and no use of canonical pair commutation relations.

The construction may choose different reservations and block assignments for different N_L. This is a variational existence argument, not an efficient physical state preparation. At small fixedrho the constant reservation can be large; rho is held fixed while taking L->infinity, exactly as required.

## 3. All actual seams are priced

Compare the actual large-torus Hamiltonian with the tensor sum of periodic block Hamiltonians on all B_L cubes, acting by zero on the leftover sites. If a cube center is at least two coordinate steps from every cube face, its actual h_x equals the corresponding periodic-block h_x. At most

 ell³-(ell-4)³<=12ell²

centers per cube fail this condition. Every mismatched actual and block term has norm at most h*. Terms centered on R_L leftover sites contribute at most h*R_L. Consequently

 ||H0,L-sum_(all B_L cubes) H0,ell^(cube)||
                    <=24h* B_L ell²+h*R_L.                  (12)

This is a direct operator-norm comparison of the ORIGINAL finite-range terms. It includes actual physical edges across all seams, outer periodic wraparound and the internal periodic wraparound terms that were artificially introduced for block energies. It does not discard a positive interaction or assume a low-density boundary state.

The r_L reserved cube states have energy bounded above by h*m each. Combining(9),(12) for the exact-sector trial gives

 E_L(N_L)<=B'_L m e+2h*m²+h*r_L m
                          +24h*B_L ell²+h*R_L.             (13)

At fixedell,rho, the error2h*m²/V and reserved volume fraction vanish, B'_L m/V->1 and B_L ell²/V->1/ell. This proves(7), including arbitrary nondivisible L and either particle parity. No exchange of global and block limits occurred.

## 4. Remove block boundaries and take the dilute limit in order

Apply(7) to the tuned tau_ell from(5), using(6). For every fixedchi, fixed smallrho, every sufficiently largeell and every N_L/V->rho,

 limsup_L E_L(N_L)/V
       <=tchi rho²/8+Cchi rho³+24h*/ell.

The left side has no ell dependence. Taking ell->infinity AFTER the thermodynamic limsup proves the canonical upper statement. The trial parameter and state may depend on ell; the bound(6) does not. Then take rho down0 at fixedchi, obtaining a limsup coefficient at most tchi/8. Finally improve the compact threshold correction and coherent direction to t0. Divergent Bchi,Dchi with that improvement are harmless because their rho limit was already taken for each fixedchi.

For the lower side use Part II's actual all-state lower. Its finite-volume estimate applies to every density matrix. In an exact N_L sector its density is N_L/V and tends to rho. At each fixed mesoscopic choice its finite-volume remainder vanishes in the thermodynamic limit; replacing N_L/V by rho is ordinary continuity of that explicit polynomial bound. The subsequent fixed-m,large-K,small-eta parameter choices and final rho limit are precisely those of that source. Hence it gives the lower coefficient t0/8 for these same integer families. This combines with the upper to give the canonical dilute envelope statement.

This application does not infer the lower coefficient from the trial, does not use a periodic fixedN4 gap at finite density, and does not assume fragmented many-pair states are coherent. The lower theorem's finite-mode argument supplied that last minimization independently.
