# Formation balance and unsaturated stationary states

Root analytic candidate, September 23, 2026. This studies the supplied
compensated rotor target. Its infinite-volume portion provisionally depends
on the current local-volume theorem, whose independent source comparison is
still pending. The finite-graph identities and explicit stationary product
states do not require a uniform microscopic-volume approximation.

The question is whether continued motion and reuse of individual sites can
sustain a nonzero homogeneous formation rate indefinitely on this fixed
hard-capacity lattice. The relevant accounting is total record number,
not whether a particular site can become vacant more than once.

## 1. Exact finite-graph balance

Use the checked effective local spaces: A is always occupied with charge
+1 or -1, B has charges 0,+1,-1, and links are integer rotors. Write

    N_G = |A_G| I + sum_(b in B_G) n_b,
    h_G = K D_G -2 delta sum_(a<c sharing B) S_ac^* S_ac,
    S_ac=F_c F_a P,
    L_mu=sqrt(kappa) P j_mu F_a P.                       (1)

The alternative coherent sum of the two signs on one edge is allowed, with
the stipulated normalization. Each of its summands has the same number
change. The electric term and every magnetic pair term conserve N_G. Every
L_mu raises N_G by exactly two:

    [N_G,h_G]=0,   [N_G,L_mu]=2 L_mu,
    L_G^*(N_G)=2 sum_mu L_mu^* L_mu.                    (2)

These are identities on the full effective space, not just zero field.
The first commutator is understood strongly for the unbounded diagonal:
its spectral projections commute with the bounded N_G. For the dissipator,
[N_G,L_mu^*L_mu]=0 and L_mu^* N_G L_mu=L_mu^*L_mu N_G+2L_mu^*L_mu.
The mild evolution and boundedness of the right side therefore give, for
every density without an electric moment assumption,

    <N_G>_t-<N_G>_0
      =2 int_0^t sum_mu <L_mu^*L_mu>_s ds.             (3)

Consequently the expected integrated event intensity is at most
`(|V_G|-<N_G>_0)/2`. With an initial definite N0 sector, a count-register
unravelling has at most `floor((|V_G|-N0)/2)` births on every allowed history:
the Hamiltonian stays in a number sector and each birth raises it by two.
This last path statement is finite-volume only. No global first clock or
finite total count is introduced in infinite volume.

## 2. Spatial mean balance on the infinite target

Let T_t be the proposed local infinite-volume semigroup on Z^d, d>=2,
with K>0 and fixed delta,kappa>=0. Take a locally normal initial state
invariant under all translations preserving the A/B bipartition. The
evolved state omega_t=omega_0 composed with T_t has the same invariance.
No decay of correlations, product form or uniform field moment is assumed.

For any A site 0 and any B site b define

    rho(t) = [1+omega_t(n_b)]/2,
    r(t) = (1/2) sum_(e=(0,c),mu on e) omega_t(L_mu^*L_mu). (4)

The sum uses two sign channels in the resolved convention or one coherent
channel in the coherent convention. The factor 1/2 is the density of A
anchors. Thus r is event intensity per lattice vertex, and rho is mean
record number per vertex. Both are expectations of fixed bounded local
operators, not a samplewise spatial concentration claim. Local normality
and the volume theorem imply their continuity in t.

Here is a derivation that does not manipulate an infinite total N. Let
Lambda_R be a large vertex box and N_(Lambda_R)=sum_(x in Lambda_R) n_x.
Since it commutes with every electric term, its generator image is a
bounded local observable. A Hamiltonian term wholly inside Lambda_R
contributes zero to the sum. A jump wholly inside contributes 2L_mu^*L_mu.
Terms outside contribute zero. All remaining terms lie in a fixed-width
boundary strip. Uniform local norms and bounded support give

 L^*(N_(Lambda_R)) =2 sum_(mu wholly inside Lambda_R) L_mu^*L_mu
                         + E_(boundary,R),
 ||E_(boundary,R)|| <= C |boundary_strip(Lambda_R)|.    (5)

The constant depends only on degree and the fixed bounded couplings, not
electric amplitudes. The bound follows termwise from (1): commutator norms
are at most 2||h_Z|| times the number of observed sites in Z, and dissipator
norms at most 2||L_Z||^2 times that number. Electric terms give exactly zero.

For each fixed R, the weak integral identity for N_(Lambda_R) passes from
finite graphs to T_t by local norm convergence, applied both to this observable
and its bounded local generator image. Divide the identity by |Lambda_R|
and let R increase. Translation invariance identifies the bulk expectations
with (4), uniformly on compact time intervals; the boundary ratio tends to
zero. This use of van Hove boxes is an additional mean-density step, separate
from the local-volume theorem, which needs no boundary/volume ratio.
It proves

    rho(t)-rho(s)=2 int_s^t r(u) du,
    rho'(t)=2 r(t)>=0.                                (6)

Since rho<=1, rho has a limit and

    int_0^infinity r(t)dt <= [1-rho(0)]/2,
    (1/T) int_0^T r(t)dt <= [1-rho(0)]/(2T).           (7)

For the all-A-plus, B-empty initial state rho(0)=1/2, so the right capacity
is 1/4 expected events per vertex integrated over all time. Its previously
checked initial intensity `kappa z(z-1)` and density derivative
`2 kappa z(z-1)`, z=2d, agree with (6).

Equation (7) excludes a positive asymptotic time-averaged homogeneous
formation rate in this fixed-capacity, birth-only target. It does not by
itself prove r(t)->0 pointwise: a continuous integrable nonnegative function
can have narrowing spikes. Uniform time continuity of the relevant rate
observables over the entire evolving state family has not been established
for these unbounded electric fields. No pointwise relaxation theorem is
claimed. Nor is an infinite total number of events on an infinite lattice
excluded by a finite integrated intensity per vertex.

## 3. Stationarity and time-averaged limits

Any translation-invariant locally normal stationary state satisfies r=0
by (6). Since the channel losses are positive, it annihilates each
L_mu^*L_mu. In its GNS representation,

    L_mu Omega=0                                     (8)

for every local channel: it is dark to this formation instrument. This
does not yet assert full occupation, uniqueness or accessibility from the
specified initial state.

One can also form the time-averaged states
`bar_omega_T(A)=T^-1 int_0^T omega_t(A)dt`. Continuity of local expectations,
contractivity and density extend the scalar integral to the quasi-local
algebra. They are states. The state space is weak-star compact, so they have
cluster subnets. For any fixed s>=0,

    ||bar_omega_T composed with T_s - bar_omega_T|| <=2s/T. (9)

This follows by shifting the time integral. Every cluster state is invariant
under each T_s, and (7) makes its expectation of the local positive rate
zero. Translation and Gauss constraints also pass as bounded local identities.
These cluster states need not be locally normal: no uniform energy tightness
has been proved. We do not infer the conclusion for arbitrary singular
stationary states by differentiating a nonexistent normal generator equation.
Equation (8) for these particular clusters follows directly from their zero
rate, not from an illicit exchange of that generator with a singular state.

## 4. Explicit physical stationary states with vacancies

Full occupation is not necessary. Let the vacant B sites have mutual
ordinary lattice distance greater than 4. Every jump requires two distinct
vacant B neighbors of one A, hence vanishes. A nonzero S_ac requires two
distinct vacant B destinations, one adjacent to a and one to c. The retained
pairs have distance(a,c)=2, so those destinations have distance at most 4.
Thus S_ac also vanishes on every matter/electric basis word with this
vacancy pattern. All bounded Hamiltonian terms and jumps annihilate it.
Its remaining Hamiltonian is diagonal, so its basis density is stationary.

There are periodic, Gauss-legal examples with a positive vacancy density.
Use period 6 in every direction and vacancies

    (1,0,0,...,0), (4,3,0,...,0) modulo 6.             (10)

Both are B sites. Distinct vacancies, including periodic copies of the same
type, have lattice distance at least 6. The period cell has 6^d/2 B sites,
of which 6^d/2-2 are occupied; this is even. Put all A charges at +1 and
assign half the occupied B charges +1 and half -1. Total charge minus the
given A background is zero in the cell. The connected periodic lattice has
an integer flow with any such zero-sum divergence: choose a spanning tree,
send each subtree's charge to its parent, and set non-tree flows to zero.
Periodic extension gives a finite-valued integer electric word satisfying
every local Gauss equation. This is a locally normal product basis state,
with finite local electric moments and finite mean electric energy.

The annihilation argument applies to every finite induced target as well:
removing boundary edges cannot supply missing destinations. Its diagonal
evolution leaves the local basis density unchanged. The volume limit is
therefore stationary. Averaging over the finitely many bipartition-preserving
translations modulo 6 gives an invariant locally normal physical stationary
state of density

    rho_dark =1-2/6^d.                               (11)

For d=2 this is 17/18; for d=3 it is 107/108. The vacancies persist even
when K,delta,kappa are all strictly positive. This is an explicit family,
not a classification of stationary states or a proof that the all-A-plus,
B-empty state relaxes into it. Accessibility of its charge/field words by
actual formation histories is a separate question.

## 5. Physical implications and open checks

Records moving away can allow a site to form again, but transport conserves
total record number. In a homogeneous fixed-capacity phase, it cannot supply
an endless positive density of new records. Formation adds two records
per event and has no reverse channel in this model. Unbounded capacity,
annihilation/recycling, nonstationary lattice growth or inhomogeneous escape
are different physical premises; none is ruled out by (7). Even the current
target can have an infinite global event count with vanishing mean intensity.

The next checks should reconstruct the number-change identities, the infinite
mean balance with the correct topology, and the periodic dark configuration's
support and integer Gauss flow. They must distinguish time averages from
pointwise relaxation, and locally normal stationary states from arbitrary
singular limits. The volume premise remains provisional until its pending
comparison is completed. No microscopic-volume theorem, resource derivation,
empirical prediction or TOE closure is claimed.
