# Derivation checkpoint before numerical controls

2026-09-30. Author discovery; not an independent check. The contract remains
unchanged. This is a durable checkpoint, not a release of a proved full EOS.
No new computation has run at this point.

## Exact bookkeeping, with the complete environment retained

For an occupation S let A_R(S) be its R-isolated graph dimers and let
E_R(S)=S minus their endpoints. Record S by the auxiliary bosonic occupation
vector of A_R(S), tensor the literal site-occupation vector of E_R(S).
These vectors are orthonormal and recover S, so this is an exact isometry
I_R into a constrained subspace of Fock(edge space) tensor environment.
It is emphatically not a representation of every particle as a free dimer.

Removing a selected edge e leaves every other occupied site farther than R
from its endpoints. Thus it can neither destroy nor create the isolation of
any remaining edge. Consequently A_R(S minus e)=A_R(S) minus e and the
bad environment is unchanged. For the actual guarded operator

 c_e=B_e product_(z outside e, dist(z,e)<=R)(1-n_z)

we have I_R c_e=a_e I_R and the same identity for products of annihilators.
Hence normal-ordered removal correlations agree exactly with the auxiliary
ones. Creation need not preserve the image. In particular, powers of the
physical compressed soft number are NOT the pullbacks of the corresponding
auxiliary powers. All number-sector/Jensen arguments below take place in
I_R Gamma I_R^dagger, and only normal-ordered conclusions are pulled back.
The physical diagonal selected-pair count itself is preserved exactly.

## Guard boundary and its necessary cost

Use the actual nine forward bonds and the actual positive S/mu rows. Set
J=Egrad9+S/mu<=2H0/a. On an output occupation eta, a row is sum l_e f_eta(e).
Guarding multiplies each amplitude by q_R(e;eta)=1_{dist(eta,e)>R}; overlap
amplitudes are zero. Choose one row edge e0. Splitting at q_R(e0) gives

 |sum l_e q_e f_e|^2 <=2|sum l_e f_e|^2
                   +2||l||^2 sum_e |q_e-q_0| |f_e|^2.

All edges within a row have Hausdorff distance at most h=4. For an integer
radius chosen uniformly from r,...,2r, the differing indicator is nonzero
for at most h radii. Such e is (r-h)-isolated but not (2r+h)-isolated.
Every nine bond belongs to six gradient rows of squared row norm two;
its S-row weighted incidence is at most three. The total is at most15.
Those selected edges are disjoint, and their endpoints belong to B_(2r+h).
For r>=14 and L>=10(2r+4), averaging therefore gives

 average_R J_guard(R) <=4E/a+(60/r)<B_(2r+4)>
                    <=C_g r^2 E/a,
 C_g=4+1620 C_B, C_B=28000322.

One radius has this bound. This is NOT an O(1) intertwining estimate.
Indeed take the actual N4 uniform E1 incoming vector C_E1^dagger^2 Omega/sqrt2.
Fix a residual axial edge {0,2e1} and remove {x,x+2e1}. Outside contact its
amplitude is 1/sqrt2. The guard kills precisely the anchor box
[-R-2,R+2] times [-R,R]^2. Its forward edge boundary contains
24R^2+56R+22 edges. Thus this one channel gives guarded gradient per residual
12R^2+28R+11. Summed over translations it is V times this quantity, whereas
the original known physical energy is V(104mu+240tau). The ratio diverges
quadratically. Normalizing the vector changes neither ratio. This does not
supply a positive-density ground-state counterexample.

## Cell soft modes, cutoff and compatible variance

On a complete anchor cube of side ell restrict Egrad9 to internal forward
rows and keep S rows with center at least one layer inside. Write f=m+q.
The Neumann variance bound and the actual S-row identity give

 ||q||^2<=ell^2 Egrad9/4,
 ell^3||P_high m||^2<=27 S_inner/mu+54||q||^2.

The kernel consists of the five constant normalized U columns. Hence the
squared distance to this space is at most17 ell^2 J_cell (ell>=3).
In the auxiliary state the total cell nonsoft number is therefore at most
17 C_g ell^2 r^2 E/a. No claim about closeness to a global isolated-dimer
projection occurs. A translated complete-cube tiling loses at most
3ell/L of the expected selected-pair number.

Introduce a larger isolation scale b, 2r<b<=ell. Every cell contains at
most M=ceil(8ell^3/b^3) b-isolated anchors, by disjoint-cube packing. Let
n_j be the R-isolated anchor count and Pi_j=1_{n_j<=K}, K=2M. Pointwise,

 sum_j n_j 1_{n_j>K} <=2 sum_j(n_j-n_j^(b)) <= B_b.

The first inequality also follows when cells contain additional bad
particles. It prices lost particles, not their energy. Pi_j is diagonal in
physical occupations and agrees with auxiliary cell number cutoff.
Let P_j be the five constant soft modes. The auxiliary soft number commutes
with Pi_j. Its retained expectation X obeys

 X >= Nmean/2 -<B_(2r)>/2 -3ell Nmean/(2L)
                    -<B_b> -17 C_g ell^2 r^2 E/a.

For a capped local ordered two-particle density matrix R2, with trace
<n(n-1)Pi>, compression to Sym^2 P obeys

 ||R2-P2 R2 P2||_1 <=2 sqrt(Tr R2 * Tr((1-P2)R2)),
 Tr R2<=K<n Pi>, Tr((1-P2)R2)<=2K<n_exc Pi>.

Cauchy over cells bounds the total error by 2K sqrt(Nmean*Exc).
This controls bounded coarse quartic kernels divided by ell^3, NOT the
unreplaced microscopic Hamiltonian. It preserves all15 symmetric channels.

## Finite five-mode reduction (standard identity, explicit here)

For n bosons in C^d, the coherent-state measure with density
(dim Sym^n) <z^n,gamma_n z^n> against uniform complex-sphere measure has
second moment

 tilde gamma2=[n(n-1)gamma2+4n P_sym(gamma1 tensor I)P_sym+2P_sym]
                      /[(n+d)(n+d+1)].

This follows from coherent resolution and the normally ordered identity
 a(v)^2 a(v)^dagger^2=a(v)^dagger^2 a(v)^2+4a(v)^dagger a(v)+2,
with polarization. It is the standard finite-dimensional de Finetti
identity (Lewin-Nam-Rougerie, arXiv1310.2200, Theorem2.2), not new prior art.
For d=5 and any positive Hermitian form T on Sym^2 C^5, put
 t_coh=min_||z||=1 <z^2,T z^2>.
The identity gives the local lower quartic value
 t_coh n(n-1)/2-C||T|| n, valid sectorwise including n=0,1.
No absence of fragmentation is assumed: the measure may be mixed.

Define physical normalized guarded cell modes
 c_(j,alpha)=ell^(-3/2) sum_(x in cell,d) conj(U_dalpha)c_(x,d).
For a Frobenius orthonormal symmetric matrix basis A^s define
 D_js=2^(-1/2) sum_ab conj(A^s_ab)c_ja c_jb and
 W_T=ell^(-3)sum_j Pi_j sum_st D_js^dagger T_st D_jt Pi_j.
Normal-ordered intertwining makes this exactly the corresponding auxiliary
quartic. The factor one half is the pair factorial, not a convention to fit.
Jensen applies to the auxiliary operators Pi_j nsoft,j; it gives
 sum <Pi nsoft(nsoft-1)> >= X^2/ncells-X.

For E<=C_E rho^2 V, choose
 r=ceil(rho^(-1/16)), ell=floor(rho^(-3/8)),
 b=ceil(rho^(-31/96)), K=2ceil(8ell^3/b^3).
The losses relative to Nmean are O(rho^(1/32)+ell/L). The bounded-kernel
projection error relative to rho^2 V is also O(rho^(1/32)), because
 Exc/N=O(rho^(1/8)), K/(rho ell^3)=O(rho^(-1/32)).
Thus the candidate completed lemma is

 <W_T>/V >= (t_coh/8)rho^2-C||T||rho^2(rho^(1/32)+ell/L).

It is a theorem about a defined physical guarded/coarse observable on
low-energy states. It is NOT a lower bound for H0 until the next comparison
has actually been proved. Constants may depend on C_E/a but not volume.

## Exact unclosed step

The desired compatible replacement is
 E_H >= <W_T0> -o(rho^2 V),
where T0 is the actual checked full15 compact-response threshold form.
Nothing above proves this. In particular, the bookkeeping isometry does
not intertwine H0; the guard counterexample explicitly forbids that simple
argument. Full contact configurations move from selected dimers into the
retained environment, so their optimal relaxation must be recovered by an
actual lower energy comparison. Independently minimizing incompatible
removed-pair fibers or invoking a scalar gas theorem would skip this step.
The remaining work is to verify the quantitative lemmas, test normalization
and determine whether positive-row allocation can close this comparison.
