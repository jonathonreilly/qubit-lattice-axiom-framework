# A physical background-capacity lower comparison for the native pair model

Author discovery candidate, September 30, 2026. **Status: conditional-support**
for the supplied full tensor-product qubit Hamiltonian. This is not a formal
review, audit, native-law selection, dilute equation of state, or phase proof.
The new high-fanout inequalities require a focused independent check before
substantial downstream reuse.

The main result is an actual all-particle lower comparison, retaining the
occupation background and the low-frequency kinetic energy. Its error can be
made o(rho squared V) on states with energy O(rho squared V). The comparison
is to an explicitly defined positive physical capacity form, **not yet to the
full T0 many-pair functional**. A separate consequence is a quantitative lower
bound on the already defined fifteen-channel N4 threshold form. Explicit
low-energy states show why replacing the remaining background problem by a
small global defect projection, or discarding higher clusters from an energy
bound alone, is invalid.

## 1. Source and contract

`CONTRACT.md` was frozen before computation with SHA256
`c166b73c23b38bc9ecef64a252b5db14c7b069754d03b3442c202d1cdb3af940`.
Science authority was refreshed to main
`30a9461ee19a49b99fa6628fe942f08e504e8903`; selected procedure is
`7146fe17a76de41badcaca3c3c7cac6d11eb2a00`. The complete landed
`NATIVE_QUBIT_PAIR_DENSITY_ONSET_BOUNDED_THEOREM_NOTE_2026-09-30.md`
was read again, together with the complete dilute-structure and phase-method
reports and their focused checks. The threshold, strict-positivity and actual
upper-variational arguments were read completely in the preceding check.
Their exact identities are in `SOURCE_BINDINGS.json`.

The only open proposals at the refresh were supplied-record PR9397 and ice
covariance PR9008; neither is a mathematical input. A scoped current-main
search for native many-pair/lower/Dyson/matching arguments found no version
of the comparison below. No exhaustive or historical novelty claim is made.
No external theorem or numerical literature value is imported. The Fourier,
finite-dimensional variational and counting arguments needed here are given
below. Old campaign artifacts are unchanged.

## 2. Actual carrier and reused bounds

On each cubic torus L>=5, V=L cubed, use physical b_x=|0><1|, n_x=b_x* b_x,
and N=sum n_x. Different sites commute, and b_x squared=0. Let

    G={+/-2e_i, +/-e_i+/-e_j}, m_x=sum_(d in G)n_(x+d),
    d_i(x)=b_(x+e_i)b_(x-e_i),
    v_ij^(s,t)(x)=s t b_(x+s e_i)b_(x+t e_j),
    QE1=(d1-d2)/sqrt2, QE2=(d1+d2-2d3)/sqrt6,
    QTij=(1/2)sum_(s,t) v_ij^(s,t).

The unchanged Hamiltonian is

    H0=mu N-2mu sum PE-mu sum PT+V3+W,
    V3=mu sum_x n_x binom(m_x,2),
    W=tau sum_(x,j,A)(QA(x+e_j)-QA(x))* (QA(x+e_j)-QA(x)).

Both mu and tau are fixed and positive. The landed full-carrier identity is

    H0=S+mu D+W,
    D=(1/2)sum_x n_x(m_x-1)(m_x-2)>=0,
    S=(2mu/3)sum_x(d1+d2+d3)* (d1+d2+d3)
       +(mu/4)sum_(x,i<j,r<s)(v_r-v_s)* (v_r-v_s).

Put a=min(tau,mu/12). The fifteen actual bare pair fields satisfy
H0>=mu D+a Egrad as a quadratic form. The checked all-N pin result gives
V3<=24mu Egrad and H0>=a O/72, where O counts particles outside isolated
physical G-dimer components. These are full-carrier statements; they do not
assert a gap above an extensive background energy.

The landed point-pin estimate also supplies, for an inner rectangular box B
and its one-site enlargement C of aspect ratio at most two,

    <N_B 1_(N_B>=3)> <= <D_B>+896 |C| Egrad_C.             (1)

D_B uses actual full-torus neighbors. Restrictions on the residual occupation
word are made before summing positive gradient norms; no occupation projector
is commuted through an overlapping pair annihilator. This precise local
version, rather than only the final global coercivity constant, is reused.

## 3. Exact removal identity and a single-pair isometry

Let E be the set of unique unordered physical G edges. It has 9V members.
Let K be H0 restricted to the N=2 graph-edge subspace l2(E). Nonedge N=2
states decouple and have energy 2mu; no such state is added to E.

For an N-particle amplitude psi and each (N-2)-particle occupation set eta,
define

    f_eta(e)=(T_N psi)_eta(e)
             =psi(eta union e) if e is disjoint from eta, and 0 otherwise.

There is no selected matching. Each input configuration is repeated once
for each of its occupied physical graph edges. Consequently

    T_N* T_N=P_edges:=sum_(e={x,y} in E)n_x n_y,
    H_N=mu D_N+T_N* [direct_sum_eta K] T_N.                (2)

To prove the second identity, write each positive S or W term as L*L, where
L is a literal linear combination of the B_e=b_x b_y. Resolve the output
occupation eta in ||L psi|| squared. Its contribution is exactly the same
pair quadratic form as L*L on N=2, applied to f_eta. Summing L and eta proves
(2), with all shared plane centers intact. For N<2 the removal part is empty.

Configuration counting gives another exact identity,

    D=N-2P_edges+V3/mu.

Using the bounds in section 2 therefore yields operator inequalities

    N/2-H0/(2mu) <= T_N* T_N <= N/2+12H0/a.              (3)

Thus the extraction map has a useful uniform low-energy normalization. On
the fixed-N spectral subspace Q_epsilon=1_(H_N<=epsilon N), N>=2 and
0<=epsilon<mu,
let A=sqrt(2/N) T_N Q_epsilon, considered on that subspace. Then

    (1-epsilon/mu)I <= A* A <= (1+24epsilon/a)I.

Its polar normalization U=A(A* A)^(-1/2) is an actual isometry, and

    ||A-U|| <= max(1-sqrt(1-epsilon/mu),
                   sqrt(1+24epsilon/a)-1) <=12epsilon/a. (4)

This extracts **one** physical pair while retaining the complete residual
occupation carrier. It is not a many-boson isometry. Iterating O(N) estimates
of size O(epsilon) is not a controlled small-error argument at fixed density.
For a normalized state of energy E with E<mu N, its normalized removal vector
has mean free-pair energy at most 2E/[N(1-E/(mu N))].

## 4. The actual nine-component free symbol

A translation cell has three axial edges {x-e_i,x+e_i} and six plane edges
{x,x+e_i+r e_j}, i<j, r=+/-1. Use this nine-dimensional physical basis.
Writing ell(k)=4sum sin squared(k_j/2), the actual five-by-nine annihilation
matrix has the two E rows on its first three entries and plane entries

    q_ij,r(k)=-(r/2)[exp(-i r k_j)+exp(-i k_i)].

Its plane squared norm is 1+cos(k_i)cos(k_j). Hence K(k) has two E bands
 tau ell, four complementary bands 2mu, and the three bands

    mu[1-cos(k_i)cos(k_j)]
       +tau ell(k)[1+cos(k_i)cos(k_j)].                   (5)

This keeps the four high internal directions. In particular,

    a ell(k) I_9 <= K(k) <= b I_9, b=2mu+24tau,           (6)

and its only zero modes are the five uniform vectors. The lower inequality
also follows directly by applying the landed bare-gradient bound to N=2;
plane words count each physical plane edge twice, so their gradient norm
is no smaller than the physical-edge norm.

Let U0 be the real nine-by-five matrix of normalized uniform pair coefficients.
Its E columns are (1,-1,0)/sqrt2 and (1,1,-2)/sqrt6, and each plane has entries
(-1,1)/sqrt2 in its two physical orientations. Then U0*U0=I_5. It implements
R=(QE1,QE2,QT12/sqrt2,QT13/sqrt2,QT23/sqrt2), not unnormalized Q_T.

## 5. Exact background capacities without a relative many-body gap

Let E_eta restrict a physical edge vector to edges meeting the occupied
residual set eta. The hard-core identity is E_eta f_eta=0.
First consider a spectral projection P commuting with K, Q=1-P, and a positive
gap on Q. Define G=Q(QKQ)^(-1)Q. For p=P f, any lambda>0 gives

    <f,Kf> >= <p,Kp>
       +(E_eta p)*[lambda^(-1)I+E_eta G E_eta*]^(-1)(E_eta p). (7)

The inverse term is the minimum over q in Q of
<q,Kq>+lambda||E_eta p+E_eta q|| squared. The actual q=Q f has zero penalty.
This proves (7) by completing a positive quadratic form. At lambda=infinity
one must use the feasible-range inverse; finite lambda avoids a rank proviso.
The inverse is a **free-pair pin matrix**, not Q_iso(H0-E_N)Q_iso.

For the useful spatial comparison fix one smooth radial profile chi0, zero
on [0,1], one on [2,infinity), and between zero and one. Define
chi_kappa(k)=chi0(|k|/kappa). Thus all cutoff derivative constants come from
one fixed profile, not a kappa-dependent family of arbitrary transitions.
Take kappa<1/4; the cutoff is periodically smooth because its transition is
inside the Brillouin cube. It multiplies I_9. Set

    p_eta=(1-chi_kappa) f_eta,
    G_kappa(k)=chi_kappa(k) K(k)^(-1), G_kappa(0)=0.

The important power here is chi, not chi squared. The exact split is
K=(1-chi)K+chi K. For any selection F_eta of forbidden rows, let
M_eta=E_F G_kappa E_F*. If M_eta is invertible, then

    <f_eta,Kf_eta> >= <f_eta,(1-chi)K f_eta>
                            +r_eta* M_eta^(-1) r_eta,
    r_eta=E_F p_eta.                                     (8)

Indeed v=K^(1/2)sqrt(chi)f has norm squared equal to the used kinetic energy,
and E_F sqrt(chi)K^(-1/2)v=E_F chi f=-r. The minimum norm with that constraint
is r* M^(-1)r. The finite-lambda regularization works if needed. The untouched
low-frequency kinetic energy is retained in (8).

## 6. Uniform comparison to component pin matrices

For a physical dimer d, let F_d be its 35 incident graph edges: two sets of
18 incident edges, subtracting their common internal edge once. Define the
infinite-lattice matrix

    Gamma_d(e,e')= integral_BZ exp(ik.(x_e-x_e'))
                  [K(k)^(-1)]_(a_e,a_e') dk/(2pi)^3,
                     e,e' in F_d.                       (9)

The integral is finite in three dimensions by (6). There are nine dimer
orientations up to translation. Put

    g=integral_BZ 1/ell(k) dk/(2pi)^3 <=sqrt(3)pi/8.

The bound follows from ell>=4|k| squared/pi squared and enclosing the cube
in the ball of radius sqrt(3)pi. Parseval and (6) give explicit matrix bounds

    b^(-1) I_35 <= Gamma_d <=(35g/a) I_35.                (10)

For the lower bound apply K(k)^(-1)>=b^(-1)I almost everywhere to the
trigonometric polynomial of any finitely supported pin vector. The upper
bound uses the trace and each diagonal entry <=g/a. Thus no unproved
invertibility or positivity hypothesis is hidden in these local matrices.

Select in each eta all isolated physical dimers having no other occupied
site within Chebyshev distance R of either endpoint; R>=10. Their pin sets
are disjoint. Their centers are R-separated, up to harmless fixed endpoint
and cell offsets. No assumption on the unselected part of eta is made.

Here is the Green estimate used for the comparison. For any fixed integer
m>=4, the infinite-lattice Fourier coefficient of G_kappa obeys

    ||G_kappa(x)|| <= C_m (1+|x|)^(-1)(1+kappa|x|)^(-m).   (11)

The constants depend only on fixed mu,tau and the chosen smooth cutoff.
This estimate follows directly from the displayed symbol: near k=0 its
inverse and j-th derivatives are bounded by C_j |k|^(-2-j). The E projector
is constant. For a plane block, the inverse can be written

    (2mu)^(-1)I - [(-mu+tau ell)/(2mu epsilon_T)] q* q,

which is smooth even where q vanishes, and has the stated derivative bounds
at its only singularity k=0. Away from zero the inverse is periodically
smooth. Decompose into dyadic annuli of scale s>=kappa. After j integrations
by parts a shell coefficient is bounded by C_j s(1+s|x|)^(-j).
Summing shells with j>=m+2 proves (11), including |x|<=1. This gives a
finite definition of the constants through derivatives of the explicit
symbol; no unverified elliptic or positivity theorem is imported.

The coefficients in (11) are absolutely summable. The sampled finite-torus
kernel is therefore their periodization. For fixed pin blocks its diagonal
block differs from Gamma_d by at most

    C[kappa + 1/(L(kappa L)^4)]                         (12)

when kappa L>=2. The first term is the omitted integral over |k|<2kappa;
the second bounds nonzero period images using (11). This order of limits
avoids periodizing the uncut 1/|x| Green kernel.

For the off-diagonal blocks, packing R-separated dimer centers and using
(11) gives the uniform block-row estimate

    sum_(d'!=d) ||M_dd'||
                <= C[R^(-1)+1/(kappa squared R cubed)]. (13)

For completeness, shell nR contains at most C n squared centers, each block
has only 35 rows, and each coefficient is bounded by
C(nR)^(-1)(1+kappa nR)^(-4). The resulting sum is bounded by
C R^(-1)[1+(kappa R)^(-2)]. Periodic copies form the same separated packing,
so the estimate is independent of the number of selected dimers and V.
Take L>=10R. Fixed cell offsets only change C.

Let Gamma_block be the direct sum of (9) over selected dimers. Equations
(10)-(13), or the block Schur norm bound, imply

    ||Gamma_block^(-1/2)(M_eta-Gamma_block)
                       Gamma_block^(-1/2)|| <= epsilon,
    epsilon=C[kappa+R^(-1)+1/(kappa squared R cubed)
                         +1/(L(kappa L)^4)].             (14)

C is finite at each fixed mu,tau. For epsilon<1, M_eta is invertible and

    M_eta^(-1) >= (1+epsilon)^(-1) Gamma_block^(-1).       (15)

An empty selection contributes zero. This is uniform over every occupation
background eta. In particular it does
not require a small norm of its global nonmatching component.

Define the positive physical form

    V_(R,kappa)(psi)=sum_eta sum_(selected d in eta)
          (E_d p_eta)* Gamma_d^(-1)(E_d p_eta).

Combining (2), (8) and (15) proves the promised all-N lower comparison,

    <H0> >= mu<D> +sum_eta <f_eta,(1-chi)K f_eta>
                               +(1+epsilon)^(-1)V_(R,kappa). (16)

Every term is defined on the original occupation carrier. Equivalently, with
Btilde_e=sum_f(1-chi)_(ef)B_f and the diagonal residual projector Pi_(d,R)
onto occupation of d and emptiness of all other sites within distance R of it,

    V_(R,kappa)=sum_d sum_(e,e' in F_d)
          [Gamma_d^(-1)]_(e,e') Btilde_e* Pi_(d,R) Btilde_e'. (17)

The projector acts **after** annihilation. It is not commuted through Btilde.
Two-dimer collisions remain present: after one pair is removed the other is
an isolated dimer in the residual background. Only additional nearby residual
particles prevent selection. The comparison retains all nine physical bond
directions and all five soft channels.

## 7. Why the scales in the comparison are compatible with low energy

Let F_R count occupied x for which its Chebyshev R cube contains at least
three particles. Partition each coordinate circle into intervals of length
between R and 2R, with L>=10R and integer R>=2. Enlarge each product box B by
R to C, and by one more site to C+. For x in B its R cube lies in C, so

    F_R <=sum_B N_C 1_(N_C>=3).

The boxes C+ have aspect ratio at most two, volume <=125R cubed, and overlap
at most 125 at any site or selected free edge. Applying (1) to each C gives

    <F_R> <=125<D>+14,000,000 R cubed Egrad
           <=14,000,125 R cubed <H0>/a.                 (18)

The constant 14,000,000 is 896 times125 times125. The generous final constant
is valid without optimizing the simultaneous D/Egrad bound. In one dimension
an interval expanded by R+1 meets a point in at most five members of a
partition whose original intervals have length at least R, which proves the
stated overlap count.

Let B_R count particles outside the selected R-isolated dimers. A particle
outside an actual isolated dimer is counted by O. An isolated dimer rejected
by the R condition has at least one endpoint counted by F_R; charging both
endpoints to it gives

    B_R<=O+2F_R,
    <B_R> <= C_B R cubed <H0>/a, C_B=28,000,322.         (19)

This is a mesoscopic separation estimate, not merely the nearest-neighbor
O bound. It applies to arbitrary coherent or mixed states.

Removing an occupied graph edge cannot destroy any selected dimer except
by removing that whole dimer: its only graph neighbor is its partner.
Removing other particles cannot spoil its emptiness condition. Thus
B_R(S minus e)<=B_R(S), pointwise. Since P_edges<=9N in fixed N,

    sum_eta ||f_eta|| squared B_R(eta)
                           <=9N <B_R>.                 (20)

For N>2 and E<mu N, together with (3), the fraction of residual particles
outside selected dimers,
averaged in the normalized removal vector, is at most

    [18 N/(N-2)] [C_B R cubed E/(a N)]
                                      /[1-E/(mu N)].    (21)

This directly controls the actual removal background; no low-energy
assumption about a separately prepared (N-2)-particle state is needed.

The removed high-frequency mass also obeys

    sum_eta ||f_eta-p_eta|| squared
                       <=pi squared E/(4a kappa squared), (22)

because chi vanishes for |k|<=kappa and K>=4a|k| squared/pi squared there.
Consider canonical sequences N/V=rho, E<=C_E rho squared V with fixed C_E.
Choose, for example, R=floor(rho^(-1/4)) and kappa=rho^(1/3), with volume
sent large at each rho. Then the fraction in (21) is O(rho^(1/4)), the
relative squared mass error in (22) is O(rho^(1/3)), and epsilon in (14)
is O(rho^(1/12)). Moreover V_(R,kappa)<= (1+epsilon)E by (16), so replacing
its factor (1+epsilon)^(-1) by one changes the lower estimate by at most
O(epsilon E)=o(rho squared V). This is a controlled physical lower comparison
at the requested energy scale, with no claimed bosonic replacement.

It does not follow that every discarded background component carries only
o(rho squared V) energy, or that the remaining form equals T0 times density
squared. The following sections make both distinctions concrete.

## 8. Quantitative consequence for the full fifteen-channel threshold form

This consequence uses the existing definition of T0 as the infimum over
compact/l2 corrections to its constant N4 incoming profiles. It does not
require a zero-energy l2 minimizer or an evaluated threshold Green matrix.
Represent an incoming vector by a complex symmetric five-by-five matrix A,
with Hilbert-Schmidt norm giving its Sym^2 C5 norm. The normalization is
Phi_A=(1/sqrt2)sum_(alpha,beta) A_ab C_alpha* C_beta* Omega.
For coherent A=z z^T it is the previously checked Phi_z.

Write u_d for the row of U0 associated with a physical edge orientation.
For a fixed graph-edge residual eta=d and a far removed pair e, the incoming
removal amplitude is exactly

    sqrt2 u_e A u_d^T.

All other matching terms, hard-core exclusions, and any compact relative
correction alter this as a function of e on only a finite set. The low-pass
filter (1-chi_kappa) preserves the constant part and sends this compact
alteration to zero at the fixed pin rows as kappa decreases: its kernel
there is O(kappa cubed), after volume is sent large. A nonedge residual has
no far constant part and need not be used in a lower bound.

Apply (8) at N=4 using the one 35-row block for each graph-edge residual,
drop the other positive terms, divide by V, then send L to infinity and
kappa to zero for each fixed compact correction. The energy/V identification
uses the checked local compact-collision argument; it is not an isometry of
the entire finite-torus N4 fiber, whose distant orbits can have stabilizers.
Since Gamma_d is the limit,

    T0[A] >= T_static[A]
      :=2 sum_(nine orientations d)
            (A u_d^T)* C_d (A u_d^T),
    C_d=U_(F_d)* Gamma_d^(-1) U_(F_d).                  (23)

This lower bound holds for every compact correction, so also for their
infimum. The factor two is the squared sqrt2 in the actual identical-pair
incoming amplitude, not a fitted pair convention.

At one occupied site the sum of u_e* u_e over its 18 incident edges is
2I_5. The union of the pins of a graph-edge d therefore obeys

    U_(F_d)* U_(F_d)=4I_5-u_d* u_d.

The row squared norms are 2/3 on axial edges and 1/2 on plane edges. By (10),
C_d >=[2a/(21g)]I_5. Finally sum_d u_d* u_d=I_5, giving the explicit bound

    T0 >= [4a/(21g)] I_15
            >= [32a/(21sqrt3 pi)] I_15.                (24)

This is a quantitative bound on **all** fifteen incoming channels. It does
not assert that T_static=T0, that its coherent minimum is the many-body EOS,
or that any infinite-density state is selected. Unlike the earlier coherent
8c consequence, (24) comes from the N4 capacity argument and is not extended
from rank-one inputs by assertion. The matrix norm and normalization steps
above supply the full Sym^2 quantifier.

## 9. Exact low-energy counterfamily to two common shortcuts

The discarded-cluster issue cannot be settled by mean energy alone. Here is
an actual full-carrier family, which is not claimed to be a ground state.
Start with any fixed compact-correction unitary trial from the checked upper
bridge, and phase-average it if desired. Its uniform estimates are

    rho_base=2u squared+O_chi(u^4),
    e_base<=t_chi u^4/2+O_chi(u^6), t_chi=E(Phi+chi).

On tori with L divisible by12 choose disjoint reset cubes R=[-3,7]^3,
translated on the 12-grid, M=V/1728 in number. In each cube, independently,
with probability 1-p do nothing; with probability p/2 replace its state by
the occupation of the six sites +/-e_i and vacuum elsewhere in R; with
probability p/2 replace it by the two triangles
{0,2e1,e1+e2} and that set translated by4e3, with vacuum elsewhere in R.
A reset means partial trace over R followed by this fixed product state.
It is a valid completely positive trace-preserving map on the original sites.
Average the resulting state over the 12 cubed tiling offsets. It is translation
invariant; starting with the number-phase average also makes it U(1) invariant.

Every motif has six particles and all its graph neighbors lie inside the
reset cube. Thus no outside occupation can connect to it. The first motif is
a K6 graph with 15 perfect matchings, D=36, and actual diagonal energy
56mu+48tau. The second consists of two odd triangles, has no perfect matching,
D=0, and actual diagonal energy 22mu/3+20tau. Each successful reset produces
six particles outside isolated dimers.

The local Hamiltonian grouping has norm h=182mu+240tau and support contained
in the Chebyshev-two enlargement of its center. At most 15 cubed=3375 terms
meet a reset cube. Telescoping the channels and using unital norm contraction
therefore bounds the change of energy density by

    |e-e_base| <= (2*3375*h/1728)p,
    |rho-rho_base| <=(1331/1728)p.                       (25)

No independence of the initial quantum state is needed for these norm bounds.
The guard vacuum makes the component statements exact in each reset branch.
In particular,

    e>=18mu p/1728,
    <particles in connected components of size>=6>/V >=3p/1728,
    <P_isolated-dimers> <=(1-p)^M,
    <P_perfect-matching> <=(1-p/2)^M.                    (26)

The two projection estimates follow by conditioning on the independent reset
coins: any successful reset violates the first event, and any two-triangle
reset violates the second. They remain true after the two symmetry averages.

Take p=delta u^4 with any fixed delta>0 and small u. Then rho=2u squared+O(u^4)
and e=O(rho squared), but the higher-cluster density has a strictly positive
order-rho-squared lower coefficient. At every fixed u>0 both global
projections tend to zero exponentially in V. The energy ratio satisfies

    limsup e/rho squared <=t_chi/8 +3375*h*delta/(2*1728).

By first choosing chi near the checked coherent threshold upper coefficient
and then delta small, these examples lie within any fixed positive tolerance
above that coefficient. They are not certified near the *true* ground energy,
which could be lower. They refute the stated uniform deductions from low
energy alone; they do not refute a theorem using the ground-state equation,
a matching leading lower bound, or a pair phase. These counterexamples have
controlled mean density and are U(1)-invariant mixtures of number sectors;
a fixed-N reset counterexample is not claimed.

## 10. Matching normalization is a separate nonlocal issue

There is an exact isometry from perfectly matchable physical configurations
|S> to the normalized sum of their perfect matchings, m(S)^(-1/2)sum_M|M>.
The multiplicity factorizes over connected occupation components. However,
ordinary matching-edge annihilation on that image gives coefficient
sqrt[m(S minus e)/m(S)], whereas actual b_x b_y gives coefficient one when
the residual configuration is matchable.

An induced even axial rectangle cycle on the spacing-two square grid has
two perfect matchings. Removing a cycle edge leaves an even path with one.
Cut two far vertices of the original cycle and add a remote isolated dimer
to restore N; choose the cut parity so the same local edge belongs to the
unique matching. The coefficient has changed from 1/sqrt2 to one while the
occupation neighborhood of the tested edge is unchanged out to an arbitrarily
large prescribed radius. This proves that a bounded-neighborhood correction
cannot make this specific normalized-matching representation an exact local
pair annihilation law on all configurations. It excludes neither another
representation nor a ground-state dilute approximation. The removal map (2)
avoids this issue by retaining the occupation background and all matchings
implicitly, rather than choosing a matching fiber.

## 11. Actual controls, failures and remaining hard target

`check_removal_capacity.py` reconstructs literal hard-core occupation action
separately from the physical nine-edge Fourier symbol, fixed-N removal amplitudes,
and finite pin inverses. Its local action method reuses the reasoning of my
previous independent N4 check, not an author/helper import. Ten actual N2
columns agree with the Fourier operator to 8.88e-16; band errors are at most
5.33e-15. N=3,4,6 superposition controls verify (2) with errors at most7.11e-15,
including actual residual counts, masses and pin inequalities at three lambda
values. The exact graph controls count the two/one cycle matchings and verify
the two reset motifs and their rational diagonal energies. Two separated
dimer backgrounds at L=7,11,15,19 have 35+35 pin rows; the tested finite
regularized inverse comparison holds, with kappa from0.01803 to0.006717.
Those fixed-four-spectator examples are not a density-uniform extrapolation.
The uniform cutoff-kernel proof is the analytic argument in section6.

This run used4.482210 CPU seconds,4.512936 wall seconds and117,915,648 bytes
peak RSS, within its30CPU/150MB price. All thread limits were one.

A second small control addresses the new smooth-split ordering directly on
the actual K2 symbol. At L=9 with70 physical pin rows and50 transition modes,
the completed-square minimum and inverse formula both equal104.18544913598916
at floating precision; the pinned-vector retained-kinetic inequality also
holds. This used0.357244 CPU seconds,0.357610 wall seconds and44,466,176 bytes
RSS, within10CPU/100MB. Its first attempt stopped with a NumPy einsum
output-ellipsis ValueError before the mathematical assertions. The original
source, freeze and traceback are preserved under historical/filtered-attempt1;
only the scalar contraction syntax was repaired. No equation or expected value
was changed. No author numerical source was run. No full Fock torus, general
T0 matrix, many-particle ground state or long-range-order parameter was computed.

The lower EOS remains open for a concrete reason. Equation(16) is a controlled
physical form with a residual isolation projector and a low-pass annihilation
field. Turning it into the correct full T0 many-pair functional still requires
control of the compatibility among the f_eta, the effects of additional
nearby residual particles at leading energy order, and the multichannel
variational problem. Near-isometry for a single extraction is insufficient
for its repeated use. The reset family proves that a generic energy bound
alone cannot supply the stronger omitted-cluster estimate.

A separate local Dyson route was considered: replace pin capacities of
coherent local averages by shell-averaged squared amplitudes, retaining
kinetic energy to pay their variance. For the actual nine-bond system this
requires a quantitative finite-domain Neumann capacity/gap statement with
its shared-center boundary geometry, followed by a compatible many-pair
comparison. The existing448 pin bound alone does not identify that capacity
with T0. No universal cluster theorem or scalar Bose-gas lower theorem is
silently imported at this step. The smooth capacity comparison above is the
proved alternative intermediate result, not a claim that this remaining
Dyson step has been completed.

For a phase conclusion an extensive eigenvalue of the actual pair correlation
matrix remains necessary under the chosen criterion. Applied-source scaling,
finite-mode commutators, the new capacity matrices, and the selected low-energy
states do not establish it. No original-record process, tensor polarization,
common gravitational source, or current-axiom inconsistency follows.
