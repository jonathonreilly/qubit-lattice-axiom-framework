# Compatible guarded cells: a full-channel reduction and its energy boundary

September 30, 2026. Author discovery, **conditional-support**, not formal
review or audit. Earlier packets remain unchanged. This result needs a
focused independent check before substantial downstream reuse.

The unchanged physical qubit law admits an exact bookkeeping representation
of selected isolated dimers **with all remaining particles retained in an
explicit environment**. It gives a controlled reduction of a specified
physical coarse quartic observable to all fifteen symmetric internal
channels, including arbitrary fragmentation and spatial variation. It does
not identify that observable with a lower bound on the microscopic energy.
An exact four-particle example shows why a simple energy intertwining fails.
A second result constructs the actual low band and a finite Feshbach operator
on a periodic dilute cell; it does not change the large-system boundary law.

Here is the main bounded result. Fix positive supplied mu,tau, a positive
Hermitian form T on Sym^2 C^5, and a fixed low-energy constant C_E. Put

 a=min(tau,mu/12), t_coh(T)=min_(||z||=1) <z tensor z,T z tensor z>.

For any physical torus state with mean density rho and energy E<=C_E rho^2 V,
there exist an integer R and a translated tiling by complete anchor cubes
such that the explicitly defined guarded, number-capped observable W_T in
(18) satisfies

 <W_T>/V >= t_coh(T) rho^2/8
              -C||T|| rho^2 [rho^(1/32)+ell/L].                 (1)

For sufficiently small rho use

 r=ceil(rho^(-1/16)), R in {r,...,2r},
 ell=floor(rho^(-3/8)), b=ceil(rho^(-31/96)),
 M=ceil(8ell^3/b^3), K=2M, L>=10ell.                            (2)

Constants in (1) may depend on C_E/a and the checked universal isolation
constant, but not on volume, the state or T. The density cutoff is only an
asymptotic one; the proof gives no useful finite-density numerical threshold.
The limits are volume first, then density. T may be the actual checked full
threshold form T0. Equation (1) then remains a statement about W_T0. The
additional comparison H0>=W_T0 up to an o(rho^2 V) expectation error is
**not proved**. In particular, no leading EOS or phase result is claimed.

## 1. Source authority and actual premises

CONTRACT.md was frozen before computation, SHA256
591214a27cfeb72caf1b2b0b5d431d540a8727b73804d3d976ab53a0a94f2666.
PRE_DERIVATION.md preserves the complete pre-control approach and its open
energy comparison. Main was refreshed to30a9461ee19a49b99fa6628fe942f08e504e8903;
selected procedure remains7146fe17a76de41badcaca3c3c7cac6d11eb2a00.
SOURCE_BINDINGS.json binds the actual landed native law and all reused proofs.
The complete preceding Neumann proof and its new independent check were read.
Open apparatus/gravity/ice units supply no premise. No historical priority
claim is made. This is neither a formal review of previous work nor an audit.

The carrier is one qubit per site, b_x=|0><1|, n_x=b_x^dagger b_x, with
commuting distinct-site operators. The supplied graph differences are
G={+/-2e_i,+/-e_i+/-e_j}. Define m_x=sum_(d in G)n_(x+d) and

 d_i(x)=b_(x+e_i)b_(x-e_i),
 v_ij^(s,t)(x)=st b_(x+s e_i)b_(x+t e_j),
 Q_E1=(d1-d2)/sqrt2, Q_E2=(d1+d2-2d3)/sqrt6,
 Q_Tij=(1/2)sum_(s,t) v_ij^(s,t).

The unchanged supplied Hamiltonian is

 H0=mu N-2mu sum PE-mu sum PT+V3+W,
 V3=mu sum_x n_x binom(m_x,2),
 W=tau sum_(x,j,A)|Q_A(x+e_j)-Q_A(x)|^2.

Its checked physical positive identity and bounds are

 H0=S+mu D+W,
 S=(2mu/3)sum|d1+d2+d3|^2
                 +(mu/4)sum_planes sum_(r<s)|v_r-v_s|^2,
 D=(1/2)sum_x n_x(m_x-1)(m_x-2)>=0,
 H0>=a Egrad15, <B_R><=C_B R^3 E/a, C_B=28000322.          (3)

B_R counts particles outside R-isolated actual graph dimers. Isolation means
no other occupied site is within Chebyshev distance R of either endpoint.
The last bound holds for R>=10 and L>=10R, on the full carrier and for mixed
states. It is an expectation/operator-form bound, not a claim that the
projection onto configurations with no bad particles has large probability.

Use the nine unique forward bonds B_d(x)=b_x b_(x+d), d=2e_i or e_i+/-e_j.
Their gradient sum Egrad9 is bounded by Egrad15: axial terms are center
translations and each plane bond occurs twice in the centered fifteen words.
Use plane order (e_i+e_j,e_i-e_j). The constant normalized soft matrix U has
axial rows (1/sqrt2,1/sqrt6),(-1/sqrt2,1/sqrt6),(0,-2/sqrt6), and for each
plane its own T column has rows (-1,+1)/sqrt2. All other entries vanish.
Thus U^dagger U=I5. The corresponding normalized collective modes are
(Q_E1,Q_E2,Q_T12/sqrt2,Q_T13/sqrt2,Q_T23/sqrt2).

T0 is the already checked physical N=4, total-momentum-zero compact-response
threshold quadratic form on Frobenius-normalized symmetric 5x5 tensors.
It is finite and positive. No numerical entries of T0, square-summable
zero-energy minimizer or positive-energy scattering interpretation is used.
The known lower bound T0>=2a/g I15 is not needed for the reduction proof.
The result below in fact applies to any supplied bounded positive T.

## 2. An exact map which keeps the bad environment

For an occupation S let A_R(S) be its set of R-isolated graph edges and let
E_R(S)=S minus their endpoints. Selected edges are disjoint and unique.
Define I_R on the physical occupation basis by

 I_R |S> = |A_R(S)>_Fock tensor |E_R(S)>_environment.       (4)

Fock space here is an auxiliary canonical bosonic Fock space over all unique
physical graph edges; |A_R(S)> has occupation zero or one at each such edge.
The environment is the ordinary finite site-occupation space. The image is
strongly constrained by exclusion, separation and consistency with the
retained environment. Recovering S by the union of the two records proves
that (4) is an isometry. It does not assert any physical bosonic commutator.

For a selected edge e, every other occupied site is farther than R from its
endpoints. Removing e therefore cannot alter any remaining edge's isolation,
nor can it make a new isolated edge inside the bad environment. Hence

 A_R(S minus e)=A_R(S) minus {e},
 E_R(S minus e)=E_R(S).                                  (5)

Define the actual guarded annihilator

 c_e^R=B_e product_(z not in e, dist(z,e)<=R)(1-n_z).

It annihilates precisely a selected edge, with coefficient one. On all
physical vectors, including superpositions of different particle numbers,

 I_R c_e^R=a_e I_R,
 I_R c_e1^R ... c_ek^R=a_e1 ... a_ek I_R.                  (6)

This is a genuine compatibility identity: different removals with the same
input occupation keep that one input coefficient and the same complete
environment. No removed-pair fiber is independently minimized.

Normal-ordered correlations therefore agree with the auxiliary ones.
Creation generally leaves the image, so compressing a creation operator
before taking products changes the result. In particular,
(I_R^dagger nsoft I_R)^2 need not equal I_R^dagger nsoft^2 I_R.
All factorial-number and Jensen operations below occur in the auxiliary
state I_R Gamma I_R^dagger. Only their normal-ordered conclusions are pulled
back by (6). The selected-pair count is diagonal and exactly equals
(N-B_R)/2; its cell restrictions do preserve the image.

## 3. A quantitative guard-gradient estimate

Let J=Egrad9+S/mu as a quadratic form on removal amplitudes; (3) implies
<J><=2E/a. In a fixed output occupation eta put
f_eta(e)=<eta|B_e psi>, extending it by zero when eta meets e. Guarding
multiplies this amplitude by q_R(e;eta)=1_{dist(eta,e)>R}. This formula includes
endpoints in the distance, harmlessly, because overlap amplitudes are zero.
A purifying index treats mixed states identically.

For each actual row sum_e l_e f(e), choose one edge e0. Since q is zero or
one and |q_e-q_0|^2=|q_e-q_0|,

 |sum l_e q_e f_e|^2 <=2|sum l_e f_e|^2
          +2||l||^2 sum_e |q_e-q_0| |f_e|^2.            (7)

All edges within a row have Hausdorff distance at most h=4 (the explicit
control finds the sharper value one). The distance of eta to them differs
by at most h. For integers R from r through2r, an unequal guard occurs for
at most h radii. In that case the input edge e is (r-h)-isolated and not
(2r+h)-isolated. Those edges are disjoint for r>=14.

The weighted incidence sum of ||l||^2 over rows containing any one forward
edge is at most15. Six gradient rows contribute12. The axial singlet row
contributes2; a plane edge occurs in two centered plane families, each with
three difference rows of squared row norm1/2, contributing3. Every selected
small-radius edge which is not large-radius isolated uses two particles of
B_(2r+h). Summing (7) and averaging the radius consequently gives

 average_R J_guard(R) <=4E/a+[60/r]<B_(2r+4)>
                    <=C_g r^2 E/a,
 C_g=4+1620 C_B.                                        (8)

Here (2r+4)^3<=27r^3 and (3) were used. At least one radius R has this bound.
Always <B_R><=<B_(2r)>. We require L>=10(2r+4); (2) guarantees this for small
rho. Equation (8) is a state-dependent radius choice, not a fixed-radius
operator inequality with that improved power.

## 4. Actual cell modes and an occupation cutoff

Tile floor(L/ell)^3 complete anchor cubes, allowing a translated remainder.
On each cube keep internal forward differences of all nine guarded fields
and S rows whose centers lie in its one-layer interior. Every such row is
selected at most once from J_guard. This is positive-row restriction, not a
change of D(m) or a deletion of physical neighbors.

For a nine-component field write f=m+q with mean q=0. The free-path Neumann
Poincare inequality is ||q||^2<=ell^2 Egrad9/4. The S symbol has norm<=2mu,
and on a constant m its interior rows equal
2mu(ell-2)^3||P_high m||^2, with P_high=I-UU^dagger. Extending q by zero,
using (ell-2)^3>=ell^3/27, and the squared triangle inequality gives

 ell^3||P_high m||^2<=27 S_inner(f)/mu+54||q||^2.

Thus the squared distance to the five constant U modes is at most
17ell^2(Egrad9+S_inner/mu), for ell>=3. In the auxiliary state, letting
Exc be the summed number outside these cell soft subspaces, (8) implies

 Exc<=17 C_g ell^2 r^2 E/a.                              (9)

The summed field norm is exactly the selected-pair number, so no comparison
of a composite physical Q with a canonical boson is hidden here.

A torus translation of the tiling loses in its remainder at most the fraction
3ell/L of the expected selected-anchor count. Choose such a translation.
This choice is compatible with (9), which holds for every tiling.

Choose a second isolation scale b>2r, b<=ell. The anchors of b-isolated
edges are separated by more than b. Packing translated integer cubes bounds
their number in each cell by M=ceil(8ell^3/b^3). Let n_j be the R-isolated
anchor count, n_j^(b) the b-isolated count, and Pi_j=1_{n_j<=K}, K=2M.
Pointwise, because A_b is a subset of A_R,

 sum_j n_j 1_(n_j>K)
       <=2 sum_j(n_j-n_j^(b)) <= B_b.                   (10)

Indeed n>2M and n^(b)<=M imply n<=2(n-n^(b)); each lost selected edge uses
two particles counted by B_b. This prices omitted particles only. It does
not require their energy to be o(rho^2 V).

Pi_j agrees with the auxiliary cell number cutoff and commutes with its
soft and nonsoft number operators. If
X=sum_j <Pi_j nsoft,j> in the auxiliary state, then

 X>=Nmean/2-<B_(2r)>/2-3ell Nmean/(2L)
                         -<B_b>-Exc.                   (11)

This argument allows fluctuating physical particle number and arbitrary
bad environments, including an extensive expected number of defects.

## 5. The full two-body variance estimate

On each capped auxiliary cell state Pi_j Gamma Pi_j let R2_j denote its
unnormalized ordered two-body density matrix, supported on the symmetric
square of the nine-component cell one-body space. Its trace is
<n_j(n_j-1)Pi_j>. Let P2_j be the symmetric square of the five-mode projection.
For any positive trace-class matrix R and orthogonal projection P,

 ||R-PRP||_1<=2 sqrt(Tr R * Tr((1-P)R)).                  (12)

A pure-state two-by-two computation followed by convexity and Cauchy proves
(12), so it does not assume commutativity of any channel matrices. Here

 Tr R2_j<=K<n_j Pi_j>,
 Tr((1-P2_j)R2_j)
  =<[n_j(n_j-1)-nsoft,j(nsoft,j-1)]Pi_j>
  <=2K<nexc,j Pi_j>.

Summing (12) and applying Cauchy over cells yields

 sum_j ||R2_j-P2_j R2_j P2_j||_1<=2K sqrt(Nmean*Exc).      (13)

Consequently replacing any uniformly bounded cell two-body kernel by its
soft compression, in a coarse energy normalized by1/(2ell^3), costs at most
||kernel|| K sqrt(Nmean*Exc)/ell^3. All noncommuting15-channel couplings are
covered. The scale1/ell^3 and the uniform kernel norm are essential. A bare
microscopic contact operator reexpressed in this normalization can have a
norm growing as ell^3, so (13) cannot itself replace that operator by T0.

## 6. Finite-dimensional coherent measures, without assuming condensation

For n bosons in C^d, let gamma1,gamma2 be normalized reduced density matrices.
The uniform complex-sphere measure weighted by
(dim Sym^n C^d)<z^n,gamma_n z^n> is a probability measure. Its second moment is

 tilde gamma2=[n(n-1)gamma2
       +4n P_sym(gamma1 tensor I)P_sym+2P_sym]
                      /[(n+d)(n+d+1)].                 (14)

For completeness the identity follows from the sphere moments
integral z^alpha conjugate(z)^beta
=delta_(alpha,beta)(d-1)! alpha!/(|alpha|+d-1)!.
Equivalently apply the coherent resolution at n+2 and use
 a(v)^2 a(v)^dagger^2=a(v)^dagger^2 a(v)^2+4a(v)^dagger a(v)+2.
Testing coherent vectors v tensor v and polynomial polarization determines
all entries on the symmetric square. This establishes (14) for general
mixed and complex states, not just occupation-diagonal tensors.

This finite-dimensional identity is standard prior art: Lewin, Nam and
Rougerie, *Remarks on the quantum de Finetti theorem for bosonic systems*,
[Theorem2.2 and its proof](https://arxiv.org/pdf/1310.2200), were read.
The k=2 formula was also reconstructed directly before that comparison and
is controlled here by exact sphere moments. No dilute-gas theorem is imported.

The extra terms in (14) are positive. Their total trace is1-p, where
p=n(n-1)/[(n+d)(n+d+1)], so
||gamma2-tilde gamma2||_1<=2(1-p). For d=5 and n>=2,

 n(n-1)(1-p)<=12n+30<=27n.

Therefore for every fixed positive15-dimensional T,

 (n(n-1)/2) Tr(T gamma2)
      >=(t_coh(T)/2)n(n-1)-27||T||n.                   (15)

The same lower bound is harmless for n=0,1. Apply it sectorwise after
tracing the nonsoft modes and the complete environment. A mixed coherent
measure is allowed; no extremal-polarization or unfragmented state assumption
occurs. More strongly, the summed soft two-body matrix divided by2ell^3 is
within trace norm27Nmean/(2ell^3) of a positive mixture of z tensor z tensors.
This retains arbitrary cell dependence of those measures.

## 7. The physical observable and all normalization factors

Define the actual guarded cell modes

 c_(j,alpha)=ell^(-3/2) sum_(x in cell j,d) conjugate(U_dalpha)c_(x,d)^R.

For a Frobenius orthonormal basis A^s of complex symmetric5x5 matrices let

 D_js=(1/sqrt2)sum_ab conjugate(A^s_ab)c_(j,a)c_(j,b).     (16)

On an auxiliary coherent n-pair vector z^n, the annihilation amplitude is
sqrt(n(n-1)/2)<A^s,z tensor z>. Thus these are the fifteen normalized
unordered-pair channels, not twice that number. The normal-ordered identity
(6) transfers this normalization exactly to the physical carrier.

With the physical selected-pair cutoff Pi_j, set

 W_T^(R,ell,K)=ell^(-3)sum_j Pi_j
                    [sum_st D_js^dagger T_st D_jt] Pi_j.       (18)

This is a well-defined positive finite-range observable for each finite
choice of scales, with guard radius R and cell size ell. It does not depend
on replacing the physical algebra by bosonic CCR. Auxiliarily it is precisely
the capped soft quartic governed by (15).

Set X_j=Pi_j nsoft,j in the auxiliary state. Since Pi_j commutes with nsoft,j,

 sum_j <Pi_j nsoft,j(nsoft,j-1)>
     =sum_j<X_j^2>-X >=X^2/ncells-X.                   (19)

The equality would be unsafe if one first compressed nsoft into the physical
image and then squared it; that operation is never made. Since
ncells ell^3<=V and X<=Nmean/2, equations (15),(18),(19) give

 <W_T>/V >= t_coh(T) X^2/(2V^2)
                -C||T|| rho/ell^3.                    (20)

The negative term also includes the -X contribution in (19), using
t_coh(T)<=||T||. Substituting (3),(9),(11), with X bounded below by the positive part of
its displayed lower estimate and (1-beta)_+^2>=1-2beta, proves (1). At (2),

 rho r^3=O(rho^(13/16)),
 Exc/Nmean=O(rho ell^2 r^2)=O(rho^(1/8)),
 rho b^3=O(rho^(1/32)),
 1/(rho ell^3)=O(rho^(1/8)).                            (21)

For the more general bounded-kernel compression in (13), also

 K/(rho ell^3)=O(rho^(-1/32)),
 [K/(rho ell^3)]sqrt(Exc/Nmean)=O(rho^(1/32)).            (22)

Every use of (3) is valid for small rho under L>=10ell. Taking volume first
makes ell/L vanish. Nothing here asserts a useful thermodynamic conclusion
for N=2 held fixed while V grows with incompatible mesoscopic scales.

## 8. A restricted physical cell frame can also be normalized

There is a useful norm statement, separate from all energy comparisons.
Embed Sym^n C^5 into the auxiliary cell Fock space by the five constant U
modes. Before any geometric projection, every ordered pair of anchors has
the uniform joint distribution ell^(-6), even when internal polarizations
are entangled: the spatial factor of each soft one-body mode is the same
constant vector. Let P_adm retain configurations whose edges are mutually
R-isolated. Every excluded pair has anchors within Chebyshev distance R+4;
use the harmless larger cube of size2R+9. A union bound gives, on this entire
finite-dimensional n-sector,

 W_n^dagger P_adm W_n
  >=[1-binom(n,2)(2R+9)^3/ell^3] I.                    (23)

Every retained edge set is exactly a physical occupation with those isolated
dimers and empty environment; it has no competing pairing. Thus the projected
frame maps into the actual2n-particle carrier. If the bracket is positive,
its polar normalization is an isometry of this *restricted local* soft
sector. For n<=K at (2), the lost Gram norm is O(rho). This is proved from
literal occupation geometry; it is not an assumed all-N global dimer map.

Equation (23) uses one cell with vacuum exterior and does not claim that
separately prepared neighboring cells have compatible boundary occupations.
A boundary buffer can impose that geometry, with additional norm loss of
order nR/ell, but norm loss alone does not bound its kinetic energy. Neither
(23) nor its polar normalization intertwines H0, and neither is used to
prove (1). This distinction matters for the attempted Temple/Feshbach route.

## 8b. An actual periodic-cell gap and many-pair Schur operator

The cold read produced a stronger finite-cell consequence. Its complete
proof is in [PERIODIC_CELL_BRIDGE.md](PERIODIC_CELL_BRIDGE.md); this is part
of the author packet and has not received an independent check. It concerns
the actual Hamiltonian on a periodic cell, not a proposed lower boundary law.

Fix R0>=14, Lc>=10(R0+4), Vc=Lc^3 and the physical N=2n sector. Define

 C_R0=4+15 C_B(R0+4)^3,
 Delta=a/[C_B R0^3+C_R0 Lc^2],
 delta=binom(n,2)(2R0+9)^3/Vc,
 s_R0=(2R0+9)^3-(2R0-7)^3,
 theta=60 max(mu,2tau)s_R0 n(n-1)/[Vc(1-delta)].         (23a)

When delta<1, the torus version of the projected frame in(23) has a polar
isometry V_n from Sym^n C^5 into the actual physical carrier. Let P be its
range projection and Q=I-P. The fixed-radius row estimate gives
J_guard<=C_R0 H0/a. On the periodic one-body space the gap estimate is
N_exc<=Lc^2 J_guard. The auxiliary complement of empty environment and all
pairs in constant soft modes is bounded by B_R0+N_exc. Pulling that statement
back through the exact map yields the full physical operator inequality

 H_N>=Delta Q.                                         (23b)

The near-isometry is used to identify the rank, not to infer this energy
bound. The rank is d_n=binom(n+4,4). On the entire internal n-pair frame,
D=0. Each actual annihilation output equals a guarded constant U vector.
A row vanishes unless its guard differs across that row. The shell has at
most2|eta|s_R0 anchors per orientation, weighted row incidence is at most15,
and the total squared residual amplitude is n. Thus

 V_n^dagger H_N V_n<=theta I.                          (23c)

This estimate covers entangled internal states, not only coherent vectors.
For theta<Delta, min-max proves exactly d_n eigenvalues below Delta, all at
most theta, and a gap of at least Delta to the complementary compression.
Their Q probability is at most theta/Delta. For fixed R0 and n<=K from(2),
putting Lc=ell gives delta=O(rho^(13/16)) and theta/Delta=O(rho^(1/16)).
This is an actual periodic-cell low-band statement. It does not assume a
relative gap above a thermodynamically extensive energy background.

The exact finite many-pair interaction on this internal space is

 S_(n,Lc)=V_n^dagger H_N V_n
   -V_n^dagger H_N Q(QH_NQ)^(-1)QH_N V_n.              (23d)

It is positive, bounded by theta, and gives an exact completion of the
physical quadratic form. The inverse is finite and bounded by1/Delta.
If s_j are its eigenvalues and lambda_j are the actual low-band eigenvalues,
the Schur complement at energy lambda proves

 lambda_j<=s_j<=[1+theta/(Delta-theta)]lambda_j.         (23e)

The companion proves all normalization, shell and Schur estimates. No
entries of this matrix or of T0 have been evaluated. Its convergence to
Vc^(-1)sum_(i<j)T0^(ij), uniformly over n<=K, is not proved. Nor is a lower
comparison of the original large torus with a sum of these periodic-cell
Hamiltonians. Those are separate remaining obligations, now with an actual
periodic-cell gap rather than a posited one.

## 9. A concrete energy-intertwining counterexample

Take the actual physical N=4 incoming E1 vector
Phi=(C_E1^dagger)^2 Omega/sqrt2 on a sufficiently large torus. For the residual
edge eta={0,2e1}, the removal amplitude of {x,x+2e1} is exactly1/sqrt2 when
these edges are far apart: the two creator orders give
2(1/sqrt2)^2/sqrt2. For R>=10, every guard transition lies in this far region.
The forbidden anchor set is precisely

 [-R-2,R+2] times [-R,R] times [-R,R].

Its forward nearest-neighbor edge boundary has

 2[(2R+1)^2+2(2R+5)(2R+1)]=24R^2+56R+22

members. This one residual/channel contributes12R^2+28R+11 to the guarded
nine-gradient sum. Translating the residual gives V distinct outputs. The
checked literal full-carrier incoming energy is

 <Phi,H0 Phi>=V(104mu+240tau).

Choose L large enough that neither the fixed interaction support nor this
box wraps. Hence

 J_guard(Phi)/<Phi,H0 Phi>
    >=(12R^2+28R+11)/(104mu+240tau).                    (24)

The normalization of Phi cancels in the ratio. There is no volume-uniform,
radius-independent bound J_guard<=C H0. In particular, exact removal
intertwining is not kinetic intertwining. This example is not a fixed-density
ground state and does not refute a correctly priced many-body replacement.
It explains the need for a guard cost such as (8), which is retained here.

## 10. The remaining actual lower-energy comparison

The precise unclosed comparison is, for the low-energy states and controlled
choices above (or a justified alternative with the same limiting properties),

 E_H >= <W_T0^(R,ell,K)>-epsilon(rho,L)rho^2 V,
 lim_(rho down0) limsup_(L to infinity) epsilon(rho,L)=0.         (25)

Equations (1) and (25) would give the full coherent-threshold lower coefficient
t_coh(T0)/8; the already checked physical dressed-pulse construction supplies
its separate upper variational context. Equation (25) has not been obtained.
The present proof closes the representation, occupation-tail, variance and
finite internal-mode reduction obligations, not the interaction replacement.

There are concrete reasons the remaining step cannot be silently inferred.
When physical dimers collide, they cease to be selected and enter the retained
bad environment. Their optimized actual four-particle relaxation is exactly
what T0 contains. The map (4) preserves that environment rather than solving
its energetic coupling to the selected sector. An absolute gap of a small
particle-number compression is not a relative gap above an extensive
many-body background. Small expected defect *fraction* is not small global
probability of any defect, and it does not justify deleting that coupling.

A proposed local Temple argument must first construct a lower finite-cell
physical form, with compatible shared-center rows, boundary treatment and
correct four-particle response. Keeping only complete S/W rows has extra
boundary zero modes, already exhibited in the preceding Neumann packet.
Deleting neighbors in D(m) can increase D when m changes from1to0 and is
not a lower comparison. Normalizing an arbitrary four-particle removal lift
also fails by the previously exact difference
(N-4)[V3/(N-2)-mu N/3], negative on separated dimers. None is repaired merely
by the near-isometry (23) or the many-mode inequality (13).

The scale arithmetic does not itself forbid a future compatible cell proof.
At the current cap K, K^2/ell=O(rho^(1/16)). Section8b establishes an actual
periodic-cell compression gap and a controlled finite effective operator
in this regime. What remains unproved is its uniform full-T0 pair expansion
and a lower Neumann/boundary comparison with the large physical system.
Ordinary localization of
physical pair wave functions incurs kinetic boundary energy; a small norm
error alone cannot price it. The next useful target is that specific physical
cell comparison or a direct positive-row scattering replacement proving
(25). No universal cluster theorem is assumed, and no restricted template
failure is presented as an exclusion of a phase or another route.

## 11. Actual controls, resources and limits

The new frozen check_compatible.py imports no earlier author runner and
uses only the standard library. It checked12288 literal occupation sets at
three radii, their injective complete-environment encodings,12288 selected
removal identities and the high-cell count inequality. Actual positive-row
geometry gives weighted incidences14 for each axial bond and15 for each
plane bond, and maximum row Hausdorff distance one. These finite checks
support the analytic bounds; they do not establish the all-state theorem.

It counted the guard boundary at R=2,3,5,10,20, obtaining respectively
230,406,902,2982,10742 edges. Using exact Gaussian rational arithmetic and
complex-sphere moments, it checked all625 ordered matrix entries of (14)
for each n=2,3,5, with nontrivial complex occupation superpositions. It also
checked the normalized15-channel unordered-pair count n(n-1)/2. Its initial
occupation fixtures did not activate the high-cell cutoff. A separate cold-
read control therefore used54 literal particles in27 radius-two isolated
dimers in one side40 cell. At b=40 the packing cap is K=16, no dimers are
b-isolated, and the active loss27 is bounded by B_b=54. The original control
and source were not changed or rerun.
No full many-body diagonalization, T0 evaluation, thermodynamic limit or
long-range-order observable was computed.

The primary managed run was priced at30 CPU seconds/150 MB, threads one,
and used5.539593 CPU seconds,5.543652 wall seconds and37,961,728 bytes peak
RSS. Deadline/STOP guards were checked. It passed with no failed assertion,
no repaired test and no failed run. CONTROL_FREEZE.json binds the script and
pre-control derivation; controls.json and control_execution.txt preserve the
actual output. The added active-cap control was separately frozen and priced
at3 CPU seconds/50 MB; it passed in0.015343 CPU seconds,0.015348 wall seconds
and18,726,912 bytes RSS.

A third separately frozen direct-position control evaluates only the N4
projected trial frame on an L=19 torus at R=4, mu=tau=1. It reconstructs the
actual S/W rows and all15 tensor directions. The Gram eigenvalues lie in
[0.8429800262,0.8477912233], obeying(23); the raw trial quadratic eigenvalues
lie in[0.1772205213,0.2910045197], below the deliberately coarse bound(B1).
These are Gram and trial-form matrices, not a full Hamiltonian spectrum,
threshold T0 or the Schur operator. It also checks81 literal complex ordered
creator amplitudes (maximum error1.37e-20), exact zero constant-soft rows,
and630 axial guard faces. Its price was30 CPU seconds/150 MB, threads one;
actual use was1.256365 CPU seconds,1.259569 wall seconds and130,252,800 bytes
RSS. No assertion failed and no script repair occurred.

This R=4 finite control does not satisfy the R>=14 isolation-bound hypotheses
of the band theorem; it tests the separate exact Gram/trial formulas only.
The all-N periodic band and Schur statements remain analytic. The existing
bare incoming energy used in(24) is a reused source-bound exact result, not
recomputed by these scripts.

The artifact is a compatible full-channel reduction and a concrete limit on
its energetic use. It is not the desired leading many-particle EOS. Its
nontrivial contribution is that neither fragmentation, cell occupation tails,
nor a missing literal selected-dimer representation need remain unspecified
premises of a future lower comparison. The still-open interaction step is
exactly (25), with physical boundary and relative-background control.

The periodic-cell extension supplies an actual finite many-pair effective
operator, but its full-T0 expansion and physical cell gluing remain open.
