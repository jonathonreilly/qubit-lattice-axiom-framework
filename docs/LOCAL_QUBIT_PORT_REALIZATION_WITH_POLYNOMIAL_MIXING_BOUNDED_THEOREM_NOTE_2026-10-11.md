---
claim_id: local_qubit_port_realization_with_polynomial_mixing_bounded_theorem_note_2026-10-11
claim_type: bounded_theorem
claim_scope: "For a supplied finite local GKSL law on an explicit periodic one-qubit-per-site carrier, nearest-neighbor compartment swaps and streaming ports plus four-site collision plaquettes approximate the specified transport-collision count process in classical path total variation. Capacity and fast-mixing errors, polynomial mixing estimates, full spatial embedding, and finite epsilon resource choices are explicit. Under the supplied nonlinear particle theorem, a stopped capacity comparison and exact finite quantum count readout identity yield a conditional nonlinear-fluid corollary with explicit polynomial resources; physical dynamics and Record interpretation remain supplied/open."
upstream_dependencies:
  - spatial_quantum_collision_realization_bounded_theorem_note_2026-10-09
  - spatial_particle_to_nonlinear_fluid_limit_bounded_theorem_note_2026-10-11
runner: scripts/local_qubit_port_realization_polynomial_mixing_2026_10_11.py
---

# Local qubit ports with polynomial mixing and a controlled count-path limit

**Date:** 2026-10-11

**Type:** bounded_theorem

**Status:** proposed_retained

Current surface status: conditional-support. Independent retained-status audit has not occurred.

**Source baseline:** frozen main `a13caa4885f547c8d206265b031ba7649e539fd9`;
provisional transport parent `73a76d2141d30d75c6aebfb2f2f9baa6e0a025bf`.

**Runner:** [self-contained finite controls](../scripts/local_qubit_port_realization_polynomial_mixing_2026_10_11.py).

**Evidence cache:** `logs/runner-cache/local_qubit_port_realization_polynomial_mixing_2026_10_11.txt`.

This note replaces the labelled particle registers and same-cell all-pairs
addressing of the [spatial quantum parent](SPATIAL_QUANTUM_COLLISION_REALIZATION_BOUNDED_THEOREM_NOTE_2026-10-09.md)
by an explicit periodic array of one-qubit spatial sites. Particles are live
occupations spread over connected velocity compartments. Fast local swaps
bring them to fixed streaming bonds and four-qubit collision plaquettes.
Exact fiber averages give exclusion-corrected rates; finite capacity and
finite-rate mixing produce a quantitative classical count-path error.
An elementary polynomial integrated-mixing bound makes finite resource
choices explicit. The parent SHA-256 is
`f02fe7fae147bf5aedac035334ab8a34ac89deb3220c9381918e58e30711fff2`;
it is a branch dependency absent from the stated frozen-main baseline.

The joint tensor carrier, computational basis, role pattern, separately
marked local GKSL law, rates, clock, and preparation are supplied. A
four-site plaquette has Manhattan diameter two and is not a two-site jump.
The construction gives literal site support for the chosen operators; it
does not derive the framework's selected Admissibility law, bath, or native
permanent-Record readout. Its live occupations are mathematical observables
whose interpretation remains separate. No new physical primitive is adopted.

## 1. Target process and mathematical carrier

Fix the normalized spatial conventions:

\[
 X=(\mathbb Z/m\mathbb Z)^3,\quad m\ge3,\quad M=m^3,
 \quad\ell=2\pi/m,\quad w=m^{-3},\quad\Omega=Nw,
 \quad V=\{-1,0,1\}^3,
\]

with integer `N>=1`, positive `b,c`, and the 288 conservative distinct pair
exchanges `r:{i,j}<->{k,l}`. Let `K_Sigma=sum_r kappa_r`, with the same positive
coefficient `kappa_r` in both directions. Every nontrivial reaction has four distinct species:
a shared input/output cancels by momentum; a repeated input has strictly
larger output energy unless the reaction is trivial.

The target count generator G has hop update
`n -> n-e_(x,v)+e_(x+s e_d,v)`, where `s=sign(v_d)`, and rate

\[
 q_{v,d}n_{x,v},\qquad q_{v,d}=b|v_d|/\ell,
\]

and collision update `n -> n-e_(x,i)-e_(x,j)+e_(x,k)+e_(x,l)` with rate `c kappa_r n_xi n_xj/Omega` in the forward direction,
with the reversed update and analogous reverse product. Its diagonal entry
is minus the sum of outgoing rates; these rules completely define G. Density is `F=n/Omega`; normalized total
mass is `w sum F=1`. No expectation factorization is assumed.

Supply an actual tensor factor `C^2` at every site of the microscopic cubic
torus `(Z/(mS)Z)^3`. Divide it into cubes of side S, one per coarse cell.
The explicit construction below assigns disjoint connected sets
`C_(x,v)` of exactly K active qubits to each `(x,v)`, with `K>=N`.
Other sites retain their full qubit factors but are inert. At active site a,
write `b_a=|0><1|`, `n_a=b_a^dagger b_a` and

\[
 n_{x,v}=\sum_{a\in C_{x,v}}n_a,
 \quad\mathsf N=\sum_{x,v}n_{x,v},\quad
 \mathsf P=\sum_{x,v}v\,n_{x,v},\quad
 \mathsf E=\sum_{x,v}|v|^2n_{x,v}.
\]

These are supplied live occupation observables and assigned kinetic charges.
They are not asserted to be the framework's physical energy, momentum, or
Record readout. The theorem applies to every initial density matrix supported
on `mathsf N=N`, including arbitrary coherences and correlations. Here support means `(Pi_N active tensor I_inert)rho(Pi_N active tensor I_inert)=rho`.
Inert spectators may have arbitrary occupations and be correlated with the
active system; the number condition does not count their qubits. A readout rule for an unrecorded site
is not inferred from using a diagonal mathematical observable.

## 2. Complete periodic site geometry

Index the 27 velocities by `v=0,...,26` in lexicographic order. Enumerate the
288 reactions deterministically by equal total momentum and squared speed,
as the helper does; give reaction r an ordered tuple `(i,j,k,l)`. For any
integer `S>=1152`, put its four ports at

\[
 (4r+2,2,0),\ (4r+3,2,0),\ (4r+3,3,0),\ (4r+2,3,0),
 \qquad r=0,\ldots,287.
\]

They are the corners of one elementary plaquette, with Manhattan diameter 2.
Assign those corners respectively to i,j,k,l. At every port `(x,y,0)` of
velocity v, add the vertical column to height `h_v=v+1`. In the plane
`z=h_v`, connect a `y=2` port through `y=1` to `y=0`; connect a `y=3` port
through `y=4` to `y=5`. In each velocity plane add both full x-backbones
`(x,0,h_v),(x,5,h_v)`, `0<=x<S`, and the full y-stem
`(0,y,h_v)`, `0<=y<S`.

Choose one of v's reaction columns and extend it to `z=S-1`. Call its fixed
horizontal coordinates `(x_v,y_v)`. Each velocity occurs in the reaction
list; the helper checks the actual choice. These full columns lie at `y=2`
or 3. They cannot meet another velocity's backbone or stem, and at a
reaction-column coordinate only its assigned velocity has a horizontal
connector. Thus compartments are disjoint even after these extensions.
Their other possible intersections occur in distinct `z=h_v` planes.

If `d_v` is the number of reaction ports of velocity v, its unpadded size is

\[
 K_v^0=4S+C_v,\qquad C_v=d_v(v+3)-v-4.                 \tag{G1}
\]

Indeed the two backbones plus stem have `3S-2` sites, each port adds
`h_v+2`, and the selected full column adds `S-h_v-1`. The exact census gives
`min C_v=104`, `max C_v=1259`.

To equalize the sizes at K, add the first `K-K_v^0` sites from the list

\[
 (1+(j\bmod(S-1)),\ 6+\lfloor j/(S-1)\rfloor,\ h_v),
 \qquad 0\le j<(S-6)(S-1).                           \tag{G2}
\]

Every nonempty row meets the y-stem, and every filled prefix is connected.
This region has `y>=6`, so it meets no reaction or full vertical column.
Different velocities again have different heights. Consequently the
construction is valid for every integer

\[
 4S+1259\le K\le 4S+104+(S-6)(S-1).                  \tag{G3}
\]

For example `K=floor(S^2/2)` satisfies (G3) at every `S>=1152`. This gives an
explicit family with K tending to infinity. On each connected compartment
choose a breadth-first spanning tree rooted at `(0,0,h_v)`. Its K−1
edges are actual nearest-neighbor cubic bonds.

The streaming ports of velocity v are the pairs

\[
\begin{array}{c|cc}
 d&\text{lower face}&\text{upper face}\\\hline
 1&(0,0,h_v)&(S-1,0,h_v)\\
 2&(0,0,h_v)&(0,S-1,h_v)\\
 3&(x_v,y_v,0)&(x_v,y_v,S-1).
\end{array}                                                    \tag{G4}
\]

They all belong to that compartment. For `v_d>0`, use the upper port in x
and the lower port in `x+e_d`; reverse the direction when `v_d<0`.
Subtracting their microscopic coordinates, after translation by `sign(v_d) S e_d`,
gives exactly `sign(v_d)e_d`. Thus each streaming edge is a native
nearest-neighbor bond. The same proof works across the periodic seam.
Different marks may share a port, which causes no problem for a sum of local
generators and is not an independence assertion about simultaneous events.

The executed smallest-S fixture uses

\[
 S=1152,\quad K=5867,\quad 27K=158409,\quad
 S^3=1528823808.                                      \tag{G5}
\]

The primary constructs all 288 plaquettes and 54 boundary-port matches,
checks disjointness/connectivity and reconstructs every BFS distance in this
fixture. It builds the coordinates in memory with no coordinate-file input
or output. No vector in the full many-body Hilbert space is allocated.

For the padded family `K=floor(S^2/2)`, active sites are `27MK`, total physical
sites are `MS^3=O(M K^(3/2))`, and maximum jump arity remains four. No resource
optimality is asserted. In normalized torus coordinates the microscopic
spacing is `ell/S`. If the physical lattice spacing is instead held fixed
by a dimensionful reference, this family increases the physical box size;
it is not a claim to vary the physical ruler at fixed laboratory volume.

The static role pattern, basis and orientation are supplied. The law repeats
under translations by a coarse cell; full one-site translation/proper-cubic
covariance of the actual Admissibility rule has not been derived. Translating
or rotating the entire supplied pattern gives a family of constructions,
not selection of one pattern by the axioms.

## 3. Local quantum jumps and exact averaged rates

Fix `nu>0`. For every edge `{a,b}` of a compartment tree use the rate-nu jump

\[
 J_{ab}^{\rm fast}=b_b^\dagger b_a+b_a^\dagger b_b.
\]

It exchanges 10 and 01 and annihilates 00 and 11. For each directed streaming
bond `(a,b)` from (G4), use

\[
 J^{\rm hop}=b_b^\dagger b_a,
 \qquad\Gamma_{v,d}=Kq_{v,d}.
\]

At the four ports a,b,c,d of reaction r in a cell use

\[
 J^{\rm col}=b_c^\dagger b_d^\dagger b_a b_b
                  +b_a^\dagger b_b^\dagger b_c b_d,
 \qquad\Gamma_r=K^2c\kappa_r/\Omega.                 \tag{J}
\]

The reaction is the partial swap `1100 <-> 0011`. There is one plaquette
mark per reversible reaction per cell, not four labelled-particle marks;
there is no input-orientation or output-arrangement multiplicity. Equation
(J)'s K squared compensates two occupied-port sampling probabilities.
The forward/reverse directions of a given microscopic partial swap have the
same rate. All these operators commute with the full assigned
`mathsf N,mathsf P,mathsf E`. They have norm one.

Supply the time-homogeneous finite GKSL generator with no Hamiltonian,

\[
 \mathcal L_{K,\nu}=\nu\sum_{\rm tree\ edges}\mathcal D[J^{\rm fast}]
           +\sum_{\rm streaming}\Gamma_{v,d}\mathcal D[J^{\rm hop}]
           +\sum_{\rm collision}\Gamma_r\mathcal D[J^{\rm col}]. \tag{L}
\]

Here `D[J](rho)=J rho J^dagger-(J^dagger J rho+rho J^dagger J)/2`.
Every jump is a partial permutation of the complete occupation-bit basis.
For any diagonal `D_f`, its adjoint dissipator is the diagonal function
`1_(eta in dom sigma)[f(sigma eta)-f(eta)]`. This follows because the partial map is
injective and `J^dagger J` is diagonal. Therefore populations of (L) obey the
classical bit process for arbitrary initial coherences. The claim concerns
populations and their count marginal, not full dephasing or a quantum
channel identification with the old labelled-register channel.

Write its classical generator as `nu A+B`. A is independent nearest-neighbor
simple exclusion inside each compartment. Every count fiber is connected:
adjacent swaps on a connected tree can move any arrangement of n occupied
vertices to any other. Its generator is symmetric, so its unique stationary
law on that fiber is uniform. Different compartments are independent under A.
Let Pi average a function uniformly in each count fiber. Then
`Pi A=A Pi=0` and `Pi^2=Pi`.

Under the uniform fiber law, one named port has occupancy probability n/K.
The two hop ports belong to distinct compartments, as do the four reaction
ports. Averaging B therefore gives the exact count generator `G_K` with rates

\[
\begin{split}
 a^{K}_{\rm hop}(n)&=q_{v,d}n_{x,v}(1-n_{x+s e_d,v}/K),\\
 a^{K}_{r,+}(n)&=\frac{c\kappa_r}{\Omega}n_{x,i}n_{x,j}
                 (1-n_{x,k}/K)(1-n_{x,l}/K),\\
 a^{K}_{r,-}(n)&=\frac{c\kappa_r}{\Omega}n_{x,k}n_{x,l}
                 (1-n_{x,i}/K)(1-n_{x,j}/K).
\end{split}                                                    \tag{R}
\]

The factorization here is a proved product of uniform **fast fibers**, not
a molecular-chaos hypothesis for the actual evolving population. The actual
finite-nu count process generally is not Markov. Its full classical count-path
approximation is proved below without instantaneous mixing or initial uniformity.

## 4. Polynomial fast-fiber mixing

Within each K-site compartment, the fast generator A_T is the sum over its
chosen tree edges of `f(eta^e)-f(eta)`, at unit rate per undirected edge.
For the uniform n-particle fiber pi, define

    E_T(f,f)=-<f,A_T f>_pi
             =(1/2) sum_(e in T) E_pi[(f(eta^e)-f(eta))^2].

The graph and fiber are connected. Empty/full fibers are singletons with
zero mixing distance. We first prove a bound uniform in every K>=2 and
n=0,...,K, then apply it to D=27M product compartments. All clocks in this
section use unit edge rate; the full supplied fast generator is nu A.

### Complete-graph variance comparison

Let A_C use every unordered pair of the K vertices at rate one, and let E_C
be its Dirichlet form in the same convention. We prove the deliberately
nonoptimal but useful inequality

    Var_pi f <= (2/K) E_C(f,f).                         (M1)

For K=2 the nontrivial fiber has two states. If their f values differ by d,
Var f=d^2/4 and E_C=d^2/2, which implies (M1). Singleton fibers are trivial.

Suppose (M1) holds on K-1 sites and consider a nontrivial K-site fiber. Fix a
coordinate i and condition on eta_i. The law on the remaining sites is the
uniform (n-eta_i)-particle fiber. Conditional variance decomposition gives

    Var f = E[Var(f | eta_i)] + Var(E[f | eta_i]).

Let E_int,i sum pairs not containing i and E_cross,i sum pairs containing i,
with both Dirichlet forms evaluated under the full pi law. Induction yields

    E[Var(f | eta_i)] <= 2 E_int,i/(K-1).              (M2)

For the second term, put p=n/K and let mu_1,mu_0 be the conditional means.
Draw a uniform configuration with eta_i=1, then uniformly choose one of its
K-n vacant other sites j, and swap i,j. The output is uniform conditional
on eta_i=0: each such output has exactly n equally likely predecessors.
This can also be verified by

    binom(K-1,n-1)(K-n) = binom(K-1,n) n.

Detailed balance between the two orientations of these swaps gives

    E_cross,i = p(K-n) E[(f(output)-f(input))^2]
              >= K p(1-p) (mu_0-mu_1)^2.

The last step is Jensen's inequality. Consequently

    Var(E[f | eta_i]) <= E_cross,i/K.                 (M3)

Average (M2)+(M3) over all K choices of i. Each complete-graph edge belongs
to K-2 internal sums and to two cross sums, so

    Var f <= [2(K-2)/(K(K-1)) + 2/K^2] E_C
           = (2/K)[1 - 1/(K(K-1))] E_C
           <= (2/K) E_C.

This proves (M1) for every K,n and every real f. In particular no occupation-
density restriction, molecular-chaos condition or large-K limit is used.
The exact complete-graph gap is not needed; asserting its optimal value
would add no premise benefit here.

### Tree routing and a uniform Poincare constant

For an unordered pair u,v, write its unique tree path as
v_0=u,v_1,...,v_d=v. Apply the adjacent transpositions in the order

    (v_0,v_1), (v_1,v_2), ..., (v_(d-1),v_d),
    (v_(d-2),v_(d-1)), ..., (v_0,v_1).                (M4)

This word has L=2d-1 transpositions. It exchanges the two endpoint labels
and restores every interior label. Therefore it implements eta -> eta^{uv}
on every bit configuration, including configurations with repeated bits.
The reverse portion is essential; a single pass transports interior labels.

Telescope f along (M4), apply Cauchy-Schwarz, then average under pi. Every
partial word is a permutation of the coordinates and preserves uniform pi.
If m_e(u,v) is the number (at most two) of occurrences of edge e in (M4),

    E_pi[(f(eta^{uv})-f(eta))^2]
       <= (2d-1) sum_{e on path(u,v)} m_e(u,v)
                       E_pi[(f(eta^e)-f(eta))^2].     (M5)

Delete a tree edge e. Its two component sizes are a_e and K-a_e, so exactly
a_e(K-a_e) unordered pairs have paths through it. Since d<=K-1,

    sum_{u<v} (2d(u,v)-1) m_e(u,v)
       <= 2(2K-3) a_e(K-a_e)
       <= 2(2K-3) floor(K^2/4).

Summing (M5), with the same 1/2 Dirichlet convention on each side, yields

    E_C <= 2(2K-3) floor(K^2/4) E_T.                  (M6)

Combining (M1) and (M6) proves

    Var_pi f <= C_K E_T(f,f),
    C_K = 4(2K-3) floor(K^2/4)/K
        <= K(2K-3) =: c_K.                           (M7)

Thus every nontrivial exclusion fiber has gap at least 1/c_K. This is a
bound for all occupations on every connected K-vertex tree, derived without
an interchange-process spectral-gap identity. Adding other unit-rate edges
only increases the Dirichlet form and preserves this lower bound. With a
common edge rate r>0, divide c_K by r. If rates vary, a uniform positive
lower bound r_min gives the same replacement; no bound independent of
vanishing edge rates is asserted.

The comparison deliberately loses constants. It gives the diffusive K^-2
order of the worst-tree gap as a lower bound, but makes no optimal-constant
or sharp worst-tree characterization claim.

### Integrated worst-case distance

Fix a starting state eta in a nontrivial fiber of size Q=binom(K,n).
The density relative to uniform is h_0=Q 1_eta, with
||h_0-1||_(L2(pi))^2=Q-1. Reversibility and (M7) imply

    d/dt ||exp(t A_T)(h_0-1)||_2^2
       = -2 E_T(exp(t A_T)(h_0-1), exp(t A_T)(h_0-1))
       <= -(2/c_K) ||exp(t A_T)(h_0-1)||_2^2.

Integrating this elementary differential inequality and using
||g||_1<=||g||_2 gives

    TV(exp(t A_T)(eta,.),pi)
       <= (1/2) sqrt(Q-1) exp(-t/c_K).                (M8)

Use zero for a singleton fiber. Equation (M8) holds uniformly in eta. Its
amplitude matters: merely knowing the spectral gap does not justify
replacing the right side by exp(-t/c_K) in an arbitrary state space.

Now let A be the sum of the D independent compartment generators. A fixed
count vector n=(n_1,...,n_D) has product uniform measure pi_n. Its transition
law from a bit configuration is the product of the D compartment laws.
Coupling the components independently, or telescoping their product measures,
gives the elementary total-variation inequality

    TV(product_i mu_i, product_i pi_i) <= sum_i TV(mu_i,pi_i).

Set

    Q_K = binom(K,floor(K/2)),
    H_(K,D) = (D/2) sqrt(Q_K-1).

For the supremum over every fiber and every initial bit configuration,

    d_(K,D)(t) <= min{1, H_(K,D) exp(-t/c_K)}.         (M9)

For H>=0 define g(H)=H when 0<=H<=1, and g(H)=1+log H when H>=1.
Direct integration of the two pieces of (M9) yields

    tau_(K,D) := integral_0^infty d_(K,D)(t) dt
       <= c_K g(H_(K,D))
       <= c_K [1 + log D + (K/2) log 2].              (M10)

For the last inequality, if H<=1 then g(H)<=1; otherwise use Q_K<=2^K
and omit the favorable -log 2. This is a polynomial integrated bound,
O(K^3 + K^2 log D), even though the full state space is exponentially large.
It is not an estimate obtained by taking a norm after integration.

The potential operator R=integral_0^infty(exp(tA)-Pi)dt satisfies
||R||_(infty->infty)<=2 tau_(K,D), by integrating the distance bound.
The reverse inference from ||R|| to tau is not made.

### Sharpening for the fixed-total-N sector

In the spatial construction K>=N>=1. At most D_N=min(D,N) compartments
are nonempty and nonfull. Every such count has

    binom(K,n_i) <= binom(K,n_*),
    n_* = min(N,floor(K/2)).

Replace H in (M9) by H_N=(D_N/2)sqrt(binom(K,n_*)-1). The same proof gives

    tau_(K,D,N) <= c_K g(H_N)
       <= c_K [1 + log D_N + (n_*/2) log(eK/n_*)].    (M11)

Here binom(K,n_*) <= (eK/n_*)^n_*, which follows from
n_*! >= (n_*/e)^n_*. The latter follows by summing log j and comparing with
its integral. All logarithms have positive arguments because n_*>=1.
For fixed total N and large K this is O(K^2 log K), with explicit N factors.
Global fixed total number does not destroy the fiber-product argument:
conditioning on the entire count vector leaves a Cartesian product of
independent uniform within-compartment arrangements. Arbitrary initial laws
are mixtures of initial configurations, so the same uniform bounds apply.

### Optional sharpening for the actual cubic-compartment trees

The preceding proof works for arbitrary trees. If a tree has diameter d_T,
replace 2K-3 in (M6) by 2d_T-1. Thus its Poincare constant is at most
K(2d_T-1). This offers an additional improvement for the actual coordinate
construction, not a new carrier assumption.

In a cube of side S, the coordinate construction chooses a breadth-first tree rooted
at (0,0,h_v). Every stem/backbone/connector site has a route to that root
of length at most S+6. A port column reaches its root through the assigned
connector, using at most S+6+|z-h_v| <= 2S+4 steps, because
1<=h_v<=27, 0<=z<S, S>=1152 imply |z-h_v|<=S-2. A padding site (x,y,h_v)
connects along its filled row to the stem and then to the root in x+y<=2S-2
steps. These paths remain in the assigned compartment. Therefore every
BFS tree has radius at most 2S+5 and diameter at most 4S+10. Consequently
all occurrences of c_K in (M8)–(M11) may be replaced by

    c_(K,S) = min{K(2K-3), K(8S+19)}.                 (M11a)

The primary reconstructs these coordinate graphs and independently checks
that the chosen tree distances equal graph distances. In the S=1152,K=5867
fixture the maximum radius is 1345 and maximum diameter is 2505. These are
finite controls; the displayed route argument proves the family bound.

For K=floor(S^2/2), (M11a) is O(K^(3/2)). The integrated bound is then
O(K^(5/2)+K^(3/2)log D) over all fibers and O(K^(3/2)log K) at fixed total N.
No lower bound or optimality claim is intended.

## 5. Finite-rate classical path comparison

Let d(t) be the supremum, over every initial bit configuration eta in the
fixed-total-N sector, of the total-variation distance from exp(tA)(eta,.) to
the uniform law on eta's count fiber. Choose tau to be any upper bound from
(M10), (M11), optionally with (M11a). Thus integral_0^infty d(t)dt<=tau.
This is an integrated mixing-distance bound. A norm bound on the potential
operator R alone cannot be substituted for it.

The sum of slow mark rates bounds every slow exit rate:

    B_K=54MK b/ell + M K^2 c K_Sigma/Omega
       =54Kb/(w ell) + cK^2 K_Sigma/(N w^2).           (B)

A reversible collision mark contributes once: at a microstate only one of
its two directions is enabled. Uniformize B using a state-independent
Poisson proposal clock of rate B_K and kernel P_B=I+B/B_K. Between proposals
run the fast chain at speed nu. This gives exactly the microchain nu A+B.

Construct a reference chain on the same proposal times. Before each proposal,
redraw a uniform microstate of its current count fiber, then apply P_B.
Its count proposal kernel is I+G_K/B_K, so its counts form exactly the CTMC
with the averaged rates (R). Start the two processes with the same counts.

If counts still agree after the preceding proposal and the next waiting gap
is u, maximally couple the actual fast endpoint to that reference uniform
redraw. Given the entire joint past and u, the mismatch probability is at
most d(nu u). On success apply the same P_B transition to both endpoints;
on failure use any coupling with the correct marginals. Fast motions do
not change counts. This constructs both required process marginals and
makes their complete count paths equal until a failed endpoint coupling.
It works from each initial microstate, without initial equilibration; a
mixture follows by conditioning on its starting state.

Let E_j be successive exponential proposal gaps and t_j the proposal times.
A union bound and the Poisson renewal identity give

    P(any mismatch through T)
      <= E sum_(j:t_j<=T) d(nu E_j)
       = integral_0^T B_K exp(-B_K u)[1+B_K(T-u)]d(nu u)du
      <= tau B_K(1+T B_K)/nu.                         (C)

The first gap contributes the 1 term. Every later gap starts at a Poisson
point of mean intensity B_K; integrating its possible start over [0,T-u]
gives the second term. The first unequilibrated interval has therefore not
been discarded. This proves a total-variation bound for the full associated
classical count paths, not only their one-time marginals.

These paths are the classical population process associated with (L).
No unique quantum trajectory, physical outcome-selection law or permanent
Record history is inferred from that mathematical association. Quantum
coherences require no extra initial restriction for one-time populations,
by Section 3. There is no diamond-norm equality of full quantum channels.

## 6. Capacity coupling and the complete finite-resource theorem

For K>=N, every target count state has a nonempty qubit fiber. Every rate in
(R) is the corresponding target rate times a number in [0,1]. Couple G_K
and G using their common transitions until a target-only transition occurs.
At a common count state the divergence rate is bounded by the sum of their
rate deficits.

For streaming, m>=3 ensures that a directed cycle edge occurs at most once
as an unordered pair. Thus sum_x n_(x,v)n_(x+s e_d,v)<=N_v^2/2. There are
at most three nonzero velocity coordinates, and sum_v N_v^2<=N^2, giving
streaming deficit at most 3bN^2/(2ell K).

For one reaction in a cell, write a,b,c,d for its four counts and N_x for
the total count in that cell. The sum of forward and reverse product deficits
before multiplication by the common coefficient obeys

    ab[1-(1-c/K)(1-d/K)] + cd[1-(1-a/K)(1-b/K)]
       <= [ab(c+d)+cd(a+b)]/K <= N_x^3/(16K).

Indeed if U=a+b and W=c+d, the numerator is at most
U^2 W/4+W^2 U/4=UW(U+W)/4<=(U+W)^3/16<=N_x^3/16.
Sum over cells, using sum_x N_x^3<=N^3, and over reaction coefficients:

    Delta_K=3bN^2/(2ell K) + c K_Sigma N^3/(16Omega K),
    TV(path law G_K, path law G) <= T Delta_K.         (D)

Combining this coupling with (C) proves the theorem. For every initial
microdistribution, or for the populations of every initial density matrix
specified in Section 1, the associated classical count paths satisfy

    TV(Law((n_t)_(0<=t<=T)), Law((nbar_t)_(0<=t<=T)))
       <= tau B_K(1+T B_K)/nu + T Delta_K,             (E)

where nbar has generator G and the same initial count distribution. Equality
in the successful couplings is literal at every time, since common event
clocks are used. Any bounded measurable path test or stopping-event indicator
therefore inherits the comparison. The mathematical path-space statement
remains distinct from a physical Record law.

For positive epsilon and finite N,m,b,c,T, define

    C_cap=3bN^2/(2ell) + c K_Sigma N^3/(16Omega),
    K_req=max{N,2,ceil(2T C_cap/epsilon)},
    S=max{1152,ceil(sqrt(2(K_req+1)))},
    K=floor(S^2/2),
    nu >= 2 tau B_K(1+T B_K)/epsilon.                  (F)

The geometry accepts these integer S,K, K>=K_req, and each term in (E) is
at most epsilon/2. Multiplication of the unit-rate fast generator by nu
divides the integrated mixing distance by nu. B_K and nu are rates and T
is time, so (E) is dimensionless with the stated normalization.

At b=delta^-1,c=delta^-2 the constants become

    B_K=54K/(delta w ell) + K^2 K_Sigma/(delta^2 N w^2),
    C_cap=3N^2/(2delta ell) + K_Sigma N^2/(16delta^2 w).

Total physical sites, including inert qubit factors, are MS^3=O(MK^(3/2));
active sites are 27MK. There are 27M(K-1) fast marks, 54M streaming marks,
and 288M collision marks. With the actual BFS bound and fixed total N,
tau=O(K^(3/2)log K); at fixed other parameters and positive T, (F) gives
a sufficient nu=O(K^(11/2)log K). General all-fiber bounds retain the
explicit D factors in (M10). These sufficient polynomial choices do not
assert optimality, bounded strength, fixed physical volume, or an autonomous
apparatus. A separate supplied fluid composition follows below.

## 7. Conditional nonlinear-fluid corollary and finite count readouts

Use the complete model, smooth-lifetime and preparation hypotheses of the
[nonlinear particle theorem](SPATIAL_PARTICLE_TO_NONLINEAR_FLUID_LIMIT_BOUNDED_THEOREM_NOTE_2026-10-11.md).
That provisional branch dependency has SHA-256
`ab42c1e6377e360739d01ac9f37f56f98b087997649ebec45be59ea07e23fc90`.
In particular, let `M_v=(2/3)^(3-|v|^2)(1/6)^|v|^2`, `m_*=1/216`, and
use its nine axial rates `alpha_*=(-4579+3 sqrt(7614177))/1072`; the other
279 rates are 1. The axial reactions are
`{s e_c-e_a,s e_c+e_a}<->{s e_c-e_b,s e_c+e_b}`, where c is one coordinate,
a,b the other two, and `s=-1,0,1`. These rates are a supplied choice.

The parent supplies a smooth solution on `[0,L]` of

    div j=0,
    partial_t j+j dot grad j+grad pi=(67/361) Delta j,
    partial_t rho+(2/5)j dot grad rho=(4/49) Delta rho,
    U_v=rho(5-3|v|^2)/2+3j dot v.

It assumes mean-zero rho and mean-zero pressure, with rho,j in
`C H^8 intersect C^1 H^6 intersect C^2 H^4`, and specifies correctors,
constants `C_d,R_0,C_path,C_prob` depending on this lifetime and solution
but not delta. Its smallness requirements include
`delta C_d<=1/2` and `delta(R_0+1)<=1/2`; retain every parent hypothesis.
This corollary uses that checked conditional particle estimate rather than
claiming a new fluid existence theorem or re-proving the fluid equations.

For `0<delta<=1` choose

    m=the least odd integer >= max(3,2 pi delta^-2),
    ell=2 pi/m, w=m^-3, N=max(2,ceil(delta^-19)),
    b=delta^-1, c=delta^-2.                           (H1)

Let `P_m` be the parent's principal Fourier cutoff and `S_m` its sampling
at cell centers `x_z=ell z`. The initial target counts have the multinomial
law from N independent draws with exact probabilities

    p_zv=w M_v[1+delta (S_m P_m U(0))_zv].            (H2)

The retained parent smallness and zero-mode conditions give `p>=0` and
`sum p=1`. Choose any initial density matrix with active-number support
`mathsf N=N` whose count law is (H2). Every such count vector is realizable
when `K>=N`; a diagonal mixture of one chosen bit configuration per fiber
is an existence witness. Coherences and correlated inert qubits are allowed.
No initial fast-fiber equilibrium is imposed.

The parent proves a stopping time `tau_*` for the target G process with

    F_zv=n_zv/(Nw)<=2M_v strictly before tau_*,
    P(tau_*<=L)<=min(1,C_prob delta^2),
    tau_*>L => sup_(t<=L)||I_m h(t)-U(t)||_(L^2_M)<=C_path delta, (H3)

where `h_zv=n_zv/(Nw delta M_v)-1/delta` and `I_m` is the piecewise-constant
cell reconstruction. The parent includes initially excessive error,
continuous exit and the full stopping-jump overshoot. We use the bound
only in the pre-stop state, without assuming this event has probability one.

### Stopped finite-capacity comparison

Put `p_r=M_iM_j=M_kM_l` and define the finite model constant

    T_4=sum_r kappa_r p_r(M_i+M_j+M_k+M_l).          (H4)

Couple G_K and G using common transitions at the smaller G_K rates until
the first discrepancy. Before that time their counts agree. Strictly
before the target stopping time, the hopping-rate deficit is at most

    sum_(z,v,d) b|v_d| n_zv n_(z+sign(v_d)e_d),v/(ell K)
      <=4bN^2 w/(ell K) sum_(v,d)|v_d|M_v^2
       =bN^2 w/(6ell K).                            (H5)

Here the one-dimensional identities are `sum M_1D^2=1/2` and
`sum |v|M_1D^2=1/18`, so the three-dimensional sum is `1/24`.
For each reaction in a given cell, both directional deficits together are
bounded by

    c kappa_r/(NwK) [n_i n_j(n_k+n_l)+n_k n_l(n_i+n_j)]
      <=8c kappa_r N^2 w^2 p_r(M_i+M_j+M_k+M_l)/K.  (H6)

This uses `1-(1-x)(1-y)<=x+y` for `0<=x,y<=1`; K>=N ensures that range.
Summing over `1/w` cells gives the uniform pre-stop defect

    Delta_local=C_local/K,
    C_local=N^2 w[b/(6ell)+8cT_4].                   (H7)

The stopped compensator bounds the probability of a discrepancy through
`L wedge tau_*` by `L Delta_local`. On no discrepancy and `tau_*>L`, the
paths agree for the whole interval and the target implication (H3) applies.
The global fast-averaging estimate (C) still uses the global B_K and tau;
it is not restricted to a favorable state region. Gluing these path
couplings therefore gives

    P(actual associated count path violates the error bound in H3)
      <= C_prob delta^2+L C_local/K+tau B_K(1+LB_K)/nu. (H8)

There is one target-exit term. This stopped argument is an event transfer,
not a global `delta^2` total-variation comparison with G on all target paths.

For the BFS compartments choose the following finite resources:

    K_req=max(N,2,ceil(2L C_local/delta^2)),
    S=max(1152,ceil(sqrt(2(K_req+1)))), K=floor(S^2/2),
    D=27m^3, D_N=min(D,N), n_*=min(N,floor(K/2)),
    c_KS=min(K(2K-3),K(8S+19)),
    tau=c_KS[1+log D_N+(n_*/2)log(eK/n_*)],
    B_K=54K/(delta w ell)+K^2 K_Sigma/(delta^2 Nw^2),
    nu=2tau B_K(1+LB_K)/delta^2.                     (H9)

The geometry's integer admissibility interval holds, K>=K_req, and (H8)
is at most `(C_prob+1)delta^2`. Thus

    P(sup_(t<=L)||I_m h(t)-U(t)||_(L^2_M)<=C_path delta)
      >=1-min(1,(C_prob+1)delta^2).                  (H10)

Probability here refers to the associated classical population count law
of the supplied quantum dynamics. Finite-nu projected counts need not be
Markov. The full microscopic process and the path couplings are defined.

### Actual finite quantum count measurements

Supply the ideal selective count instrument `rho -> Pi_n rho Pi_n`, whose
branch probability is its trace. This is a mathematical observation premise;
an apparatus realizing it is not constructed here.
Let `Pi_n` project onto a count fiber, tensor the identity on inert sites,
and let `Diag_act` denote the active computational diagonal after tracing
out inert factors. Let Q be the forward population generator, the transpose
of the backward generator `nu A+B`. The partial-permutation calculation in
Section 3 gives, for every matrix rho,

    Diag_act(exp(t L_GKSL)rho)=exp(t Q)Diag_act(rho),
    Diag_act(Pi_n rho Pi_n)=1_(count=n)Diag_act(rho). (H11)

Apply these identities successively to the unnormalized selective states
at any fixed finite ordered list of count-measurement times in `[0,L]`.
At each step the diagonal is precisely the classical microscopic
distribution restricted to the observed count fiber. Its trace is the
joint probability. Induction proves equality of the quantum joint law
and the associated classical count law at those times, even for coherent
initial states and correlated inert factors. It does not replace a
post-measurement fiber by its uniform distribution. Consequently all such
readouts satisfy the corresponding simultaneous sampled-time version of
(H10), with a failure bound independent of the finite number of readings.
No continuous physical record, ontological quantum path, arbitrary quantum
observable, or permanent-Record interpretation is supplied by this identity.

### Explicit polynomial ceilings

Set `c_m=2pi+2`, `c_ell=2pi/c_m`. Then
`m<c_m delta^-2`, `ell>c_ell delta^2`,
`w<=(2pi)^-3 delta^6`, and `delta^-19<=N<=2delta^-19`.
Separating the hopping and collision terms of (H7) gives powers -35 and
-34, respectively, and

    C_local<=C_local0 delta^-35,
    C_local0=4(2pi)^-3[1/(6c_ell)+8T_4].             (H12)

All the following constants are independent of delta:

    C_req=max(2,2L C_local0+1),
    C_S=max(1152,sqrt(2(C_req+1))+1), C_K=C_S^2/2,
    D0=27c_m^3, c0=C_K(8C_S+19),
    B0=54C_K c_m^3/c_ell+K_Sigma C_K^2 c_m^6,
    T0=c0 max(2+log D0+log C_K,43),
    V0=2T0 B0(1+LB0).                               (H13)

The ceiling/floor inequalities in (H9) imply

    K_req<=C_req delta^-37, S<=C_S delta^(-37/2),
    K<=C_K delta^-37,
    m^3S^3<=c_m^3 C_S^3 delta^(-123/2).              (H14)

The two terms of B_K have powers -46 and -69, whence
`B_K<=B0 delta^-69`. The BFS comparison gives
`c_KS<=c0 delta^(-111/2)`. Since `D_N<=D0 delta^-6`,
`n_*<=2delta^-19` and `1<=n_*<=K`,

    tau<=c0 delta^(-149/2)
             [2+log D0+log C_K+43log(1/delta)]
       <=T0 delta^(-149/2)[1+log(1/delta)],
    nu<=V0 delta^(-429/2)[1+log(1/delta)].            (H15)

For the first line, bound `log(eK/n_*)<=1+log C_K+37log(1/delta)`
and enlarge the remaining `1+log D_N` term by `delta^-19`.
For the second line use `1+LB_K<=(1+LB0)delta^-69`.
Active sites and fast marks are `O(delta^-43)`; the individual hopping
and collision rates are `O(delta^-40)` and `O(delta^-63)`. These are
sufficient constructive ceilings, with no claim of optimality. Volume,
preparation, rate strengths and the supplied dissipative law vary with
accuracy; no fixed-volume, fixed-strength microscopic fluid theorem follows.


## 8. Scope, prior art and evidence

The [finite encoded-channel note](QUTRIT_FREE_WAIT_COARSE_GRAINING_AND_ENCODED_CHANNELS_BOUNDED_THEOREM_NOTE_2026-10-08.md)
already provides conditional finite channel intertwiners. The present
additional result is the explicit periodic site geometry, fixed local ports,
capacity correction, and controlled fast-mixing path comparison; generic
block encoding alone is not claimed as the contribution. The classical
variance, path-comparison and averaging methods are established mathematical
machinery, proved at the exact hypotheses used here. Frozen-main top-level
source searches and reading identities are preserved in the campaign pack;
no exhaustive literature novelty claim is made.

The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) and registered scale,
kinetic-isotropy and realized-state primitives do not select the displayed
GKSL law, computational basis, role pattern or observation procedure. The
operators' assigned number, momentum and kinetic energy are conserved by
the mathematical model. They do not account for an external dissipative
apparatus's physical energy or identify native physical observables.

| Proof obligation | Evidence and limitation |
|---|---|
| Every streaming port and collision patch is literally spatial | Explicit coordinates, disjoint compartments and periodic seam proof; complete finite tile reconstruction |
| Collision support and conservation | Four-site partial swaps; reactionwise assigned-charge identities |
| Arbitrary-coherence population closure | Full partial-permutation argument and every local matrix unit |
| Correct averaged rates and multiplicities | Exact fast-fiber product law; all finite K=2 port fibers |
| Finite-rate count process | Full common-proposal-clock coupling, including the initial gap; finite generator and two-time controls |
| Polynomial integrated mixing | Complete-graph induction, tree routing, L2 decay, product TV envelope and actual BFS radius proof |
| Capacity and epsilon resources | Uniform deficit coupling, exact small-count controls and explicit (F) |
| Native law, bath, clock and permanent Record readout | Supplied or open physical interfaces; no additional primitive adopted |
| Nonlinear-fluid composition and finite count readouts | Linked conditional particle theorem, pre-stop capacity coupling, active diagonal/instrument induction and explicit resources; no native outcome or permanent-Record law |

The primary is deterministic, declares a 180-second timeout, and uses Python,
NumPy, SciPy and SymPy. It has no runtime input files, repository imports or
output artifacts. Its audit-input metadata names this note and the spatial
quantum and nonlinear particle parents for provenance. It rebuilds all coordinates, tests the full
288 local matrix units, 256 collision microstates/81 fibers, and 16 hop
microstates/nine fibers. The exact N=3 eight-qubit generator has 56 states
and 16 count states; the runner checks its uniform fast fibers, averaged
rates and failure of exact finite-rate count lumping. Two-observation
comparisons use floating matrix exponentials and are labeled as finite
controls, not an all-path proof.

The variance comparison is checked by exact rational LDL forms on all
zero-mean functions in 21 complete-graph fibers through K=7. Every labelled
tree through K=6 (1,441 trees) and every endpoint route is reconstructed;
larger path/star/binary fibers through K=9 have floating spectral and TV
controls. A two-component mixing integral is calculated from actual 2x2
semigroups and their tensor product. The disconnected-graph example is a
finite check of the stated connectivity hypothesis, not a physical no-go.
The native BFS distances and exact epsilon allocations are also checked.
New composition controls reconstruct the fixed equilibrium weights and nine
axial reactions, test every reaction on an exact 81-point pre-stop box, and
derive the resource exponents from the displayed formulas. Rational bounds
check finite stopped-capacity choices. Actual quantum superoperators and
selective count instruments on four active qubits at number two plus a
correlated inert qubit give a floating three-readout check of all 27 joint
outcomes. Those finite controls support, but do not replace, the analytic
stopping and measurement-induction proofs.

Actual source-mutant copies and full failure logs are retained in the
campaign evidence pack. They change the relevant matrix, rate, projection,
first-gap factor, routing, geometry or resource formula; syntax failures are
not counted as scientific discrimination. These are author controls, not
independent audit verdicts. Original broader negative research probes remain
separate and are not imported as general no-go claims here.

```yaml
actual_current_surface_status: conditional-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "Replace labelled spatial registers and nonlocal pair addressing with an explicit local spatial-qubit construction."
source_of_blocker_text: user_goal
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "Independently check the complete source-bound positive unit and its provisional nonlinear particle dependency; investigate the supplied dynamics, preparation and permanent-Record interfaces."
conditional_surface_status: conditional-support
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "Explicit conditional local qubit-port realization with polynomial mixing and a finite-resource classical count-path approximation."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```
