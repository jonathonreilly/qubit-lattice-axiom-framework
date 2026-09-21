---
claim_id: mobile_records_moving_geometry_color_waves_bounded_theorem_note_2026-09-21
claim_type: bounded_theorem
claim_scope: "A supplied local classical process of permanent paired records on even cubic tori admits history-independent birth-color counts, arbitrary-full-matching product-invariant transport and a stationary finite-mode Euler color-wave limit uniform in matching geometry. Bounded autonomous plaquette motion preserves that limit. An explicit symmetric-gap comparison supplies a sufficient O(N^5) post-completion color preparation time. The geometric Gauss field is distinct and is Euler-static only under its stated stationary reversible law. No physical electromagnetic identification, quantum dynamics, fixed-rate total filling bound or TOE is established."
upstream_dependencies:
  - minimal_axioms
  - mobile_records_all_stage_formation_clock_bounded_theorem_note_2026-09-21
runner: scripts/mobile_records_moving_geometry_color_waves_2026_09_21.py
---

# Color waves carried by permanent records through moving geometry

**Date:** 2026-09-21
**Type:** bounded_theorem
**Status:** proposed_retained
**Author support:** conditional-support; no independent audit verdict.

This construction combines continuing record formation with a propagating
color sector after the lattice fills. Whole immutable record pairs exchange
between nearby matched sites. Their context-dependent rates preserve an iid
color law, and their large-scale fluctuation current has a curl form. The
matching can also move through bounded local plaquette rotations.

The process is not a derivation from the [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md).
Exact classical recognition, marked partnerships, paired births, the even
fourteen-color readout, context-dependent exchange rates and a physical clock
are supplied premises. Each pair exchange moves four existing records at
most two lattice steps; it is not restricted to one nearest-neighbor step.
Formation and slide rules depend on the explicitly provisional
[all-stage formation theorem](MOBILE_RECORDS_ALL_STAGE_FORMATION_CLOCK_BOUNDED_THEOREM_NOTE_2026-09-21.md).

For even N>=8, let K=N^3/2. Choose k0>|gamma| and fixed bounded plaquette
rotation rate nu>=0. The complete arguments below establish the following
conditional chain, with the original order of limits made explicit.

1. On every full nearest-neighbor matching, the routed color exchanges
   preserve each iid color law and are irreducible within every color-count
   sector. Their construction is covariant under proper cubic rotations
   and one-site translations. Before completion, the specified local birth
   density gives multinomial final color counts independently of the
   autonomous geometry, although the color arrangement at first completion
   need not be iid.
2. After that finite-volume random completion time, wait at least

       t_prep(N,epsilon) = [8N(3N-1)/k0]
                          [(K/2) log14 + log(1/(2epsilon))].

   Uniformly in the completion arrangement and geometry history, the color
   law then lies within epsilon in total variation of the iid reference
   law, independent of the current geometry. With epsilon=N^-4 this
   sufficient waiting time is O(N^5/k0). The random time to fill is
   additional; this result gives no volume-uniform bound on it at fixed
   positive birth rate.
3. Observe fixed Fourier modes Q=2pi m at microscopic times Nt after
   preparation. The normalized color field converges in mean square to
   its linear Euler propagator, uniformly over the initial full matching
   law, with the same conclusion while the autonomous geometry moves.
   Finite collections have the propagated Gaussian product-law limit.
4. For orbit-isotropic probabilities p_a=rho_A/6 on the six axis colors
   and p_a=rho_B/8 on the eight cube colors, the six vector moments obey

       partial_t X = (gamma rho_A/3) curl Y,
       partial_t Y = -gamma rho_B curl X,
       c = |gamma| sqrt(rho_A rho_B/3).

   At nonzero gamma and Q, four modes propagate, two vector-longitudinal
   modes are static, and seven other tangent color modes are static.
   At gamma=0 all thirteen tangent modes are static on this scale.
   Arbitrary full-support color probabilities retain the matrix
   propagation theorem; they need not have this speed or mode count.

The vector field formed from both physical endpoints has the same limit
with the stated factor sqrt(2) relative to the pair-normalized field.
Its longitudinal equilibrium variance remains positive. It is distinct
from the matching's exactly divergence-free geometric field. Under a
stationary reversible matching law the latter has vanishing Euler-time
increments; that conclusion is not asserted for arbitrary nonstationary
matching entrance laws. Thus this theorem supplies color waves alongside
a constraint, without identifying them as one electromagnetic field.

Four selective checks reconstructed these arguments in a separate context
before viewing their corresponding author calculations. They closed two
mode-count qualifications and found no remaining mathematical correction.
The original source arguments are reproduced in full below, with titles
removed and headings shifted. Historical pending-review and earlier
preparation wording remains as provenance: Part IV improves Part II's
O(N^7) bound, and Part III extends Part I's fixed-geometry result. The
source-bound packets record the final checked status and exact corrections.

## I. Routed immutable-pair transport and the color-wave limit

2026-09-21. Root proposed construction and conditional finite-mode theorem.
Author controls and independent review are pending. The purpose is to put
formation, immutable records and a propagating content sector on one state
space. The geometric dimer Gauss field remains static in the full-state
transport below; it is not identified with the propagating content fields.

### 1. State and explicitly supplied choices

Use an even cubic torus of side N>=8. Each present record is P_n in M_2(C),
with a unique antipodal partner P_(-n) at a nearest-neighbor site, as in
`GEOMETRIC_PARTNER_RECORD_FORMATION.md`. Recognition of exact contents and
the Bloch/spatial proper-rotation action remain supplied classical model
choices. Records retain their contents under every event.

At full packing let M be **any** nearest-neighbor perfect matching and
K=N^3/2. Temporarily choose one parity class as black. Label each pair by
its black site u and write its white site w_u=u+d_u, where d_u is a signed
unit vector. The final event family is independent of this parity choice.
Coordinates and dimer directions are position-derived, not record tags.

Each antipodal pair has a color a=chi(n)=chi(-n) in a fourteen-element
alphabet. The color is a specified function of its unchanged content;
there is no extra register. Define e(a),b(a) by six A colors with
e=+/-coordinate unit vectors,b=0 and eight B colors with e=0,b in
{+/-1}^3. Section 7 gives an explicit even proper-cubic color map on the
continuous qubit-projector sphere and a compatible formation density.

The clocks, color map and context tensor below are supplied choices. This
is not a claim that the axioms select them, or an operational unknown-qubit
measurement protocol. Pair exchanges move a record by at most two lattice
edges in one atomic event. This is bounded-range motion, **not** the earlier
one-nearest-neighbor-step slide channel. No new primitive is registered.

### 2. Six local routing permutations

For each signed unit vector delta, define q_delta on pairs by

    w_(q_delta u) = u+delta.                              (1)

Translation of the black sublattice by delta bijects it with the white
sublattice, and each white site belongs to one pair. Thus q_delta is a
permutation. Its inverse is just the pair whose black site is w_u-delta.
It is computable from a bounded neighborhood and the partner relation.
In black-site coordinates,

    q_delta u-u = delta-d_(q_delta u).                    (2)

A fixed point is exactly a pair with d_u=delta and is ignored. On a
nonfixed step, the scalar delta.(q_delta u-u)=1-delta.d_(q_delta u)
is either 1 or 2. Consequently every nontrivial cycle winds the torus in
the delta direction and has length at least N/2. For N>=8 it has at least
four distinct vertices. Four consecutive context positions below are
therefore distinct. Shorter tori are outside the theorem; their repeated
context variables must not be treated as independent samples.

For each nonfixed u->v=q_delta u, exchange the entire pair contents:
the black record at u goes to v and conversely; the white record at w_u
goes to w_v and conversely. This preserves the geometric matching and all
antipodal partnerships. The displacements are delta-d_v for black records
and delta-d_u for white records, so each has lattice path length two.
Intermediate positions are not states of this atomic event. This avoids
claiming that a sequential path through occupied intermediate sites was
provided. The two exchanged pairs are distinct and have four distinct sites.

The union of these pair edges is the graph obtained by contracting each
dimer of the connected cubic lattice. It is connected. Every original
nonmatching black-white edge occurs as one directed channel; channels with
the same unordered pair endpoints are retained with their multiplicity.

### 3. Local rates and exact stationary laws

Let gamma be real and choose a fixed k0>|gamma|. Put

    S_delta(a,b)=(gamma/2) delta.
                  [e(a) cross b(b)+e(b) cross b(a)].       (3)

For the four colors (l,a,b,r) on
q_delta^(-1)u,u,q_delta u,q_delta^2u define

    h_delta=S_delta(l,a)+S_delta(a,r)
                -S_delta(l,b)-S_delta(b,r),
    c_delta(u,eta)=(1/2)[k0+h_delta/2].                    (4)

The outer factor 1/2 compensates for using all six signed routing directions.
Since |S_delta|<=|gamma|/2, |h_delta|<=2|gamma| and the event rate is at
least (k0-|gamma|)/2. The footprint has four pairs, all within a fixed
lattice distance (at most five) of u. Reversing the pair exchange negates
h_delta. The symmetric part of the rate is exactly k0/2.

On each routing cycle, the sum of h_delta over its edges is zero: the
first and last nearest-position sums cancel, and the two distance-two sums
cancel after an index shift. Product weights are unchanged by exchanges.
The incoming-minus-outgoing rate sum is thus zero pointwise. It follows
that **every** homogeneous product law pi_p on pair colors is stationary,
as is the uniform law on every fixed color-count sector. Positive rates
on the connected contracted graph make each such sector irreducible.
This does not imply mixing of geometric matchings, which are fixed here.

Proper cubic rotations send delta and both color vectors by R; the cross
product in (3) is covariant. Under reversal of the temporary black/white
choice, the new routing in direction delta is the old q_(-delta)^(-1).
The ordered context reverses and S_delta=-S_(-delta); the two signs cancel
in h. Hence the event family, including its rates and contents exchanged,
is independent of parity choice. In particular, translations by one site
are symmetries, not just translations preserving the written black class.

### 4. Product currents and geometric cancellation

Write xi_u for the fourteen color indicators, X=sum_a p_a e(a),
Y=sum_a p_a b(a). Before the outer factor 1/2 in (4), the mean directed
color current is

    J_delta,a(p)=gamma p_a delta.
          [e(a) cross Y+X cross b(a)-2 X cross Y].         (5)

Indeed, condition on the two exchanged colors. Averaging the two context
colors gives E[h|a,b]=2[(S_delta p)_a-(S_delta p)_b]. Multiplication by
xi_a-xi_b and averaging gives 2p_a[(S_delta p)_a-p.S_delta p], which is
(5). Four distinct context positions and the product law are used here.
For fixed points the actual current is zero, and its spatial test-function
coefficient is also zero; formal use of (5) there contributes nothing.

Let J_i be (5) with delta=e_i and A_i its Jacobian at a fixed full-support
p, on the thirteen-dimensional probability tangent. Then
J_delta=sum_i delta_i J_i and A_delta=sum_i delta_i A_i. The identities

    sum_delta J_delta=0,       sum_delta delta J_delta=2 J,
    sum_delta A_delta=0,       sum_delta delta_i A_delta=2 A_i    (6)

will remove the dimer-direction dependence. Replacing a homogeneous
current by its physical displacement in (2), and summing over u using the
permutation q_delta, gives exactly the unwrapped total-current identity

    (1/2) sum_(delta,u) (delta-d_(q_delta u)) J_delta
                       = K J.                            (7)

The direction sum cancels for every matching, including one with nonzero
winding. Equation (7) alone is an expectation identity, not a fluctuation
theorem. The following block argument controls the fluctuating correction.

### 5. Quenched stationary finite-mode propagation

Take any sequence of perfect matchings M_N, with no regularity or
probability assumption on it. Start the pair colors in pi_p, independently
of this fixed geometry. For Q=2pi m, m a fixed nonzero integer vector, put

    Y_N(Q,t)=K^(-1/2) sum_(u black) exp(-i Q.u/N)
                                      [xi_u(Nt)-p].       (8)

The supplied microscopic clocks are accelerated by N. For every fixed
finite t, the claimed limit is

    E|Y_N(Q,t)-exp[-i A(Q)t]Y_N(Q,0)|^2 -> 0,
    A(Q)=sum_i Q_i A_i,                                  (9)

uniformly over the chosen M_N, and jointly for finitely many modes/times.
This is a stationary finite-dimensional limit. It is not a nonstationary
hydrodynamic theorem, quantitative mixing estimate, or formation-time limit.

Here are the load-bearing replacement details, adapting the finite-state
argument in `CONTEXT_EXCHANGE_FLUCTUATION_DERIVATION.md` to this graph.

**Finite-block mixing.** Let C_l(u) be the pairs with at least one endpoint
in the all-site cube of radius l about u. Their contracted internal graph
is connected, because it contains the image of every lattice edge inside
that connected cube. The four current pairs are included for l>=6.
There are Theta(l^3) pairs, uniformly in M_N. At most O(l^2) have black
site outside the cube. Given the colors outside C_l and its color counts,
pi_p is uniform on this finite sector. Internal pair transpositions connect
it, so a Poincare constant A_l<infinity exists. For fixed l there are only
finitely many local matching patterns and count sectors; their maximum
A_l is uniform in N and M_N. The actual symmetric Dirichlet form dominates
the internal unweighted swap form with a fixed positive constant.

For a bounded directed current j_delta=(k0+h_delta/2)(xi_u-xi_v), let
hat j=E[j_delta | the counts in C_l], and h=j_delta-hat j. Each h is
orthogonal to every global-count function. Conditional Poincare and
Cauchy-Schwarz, followed by the O(l^3) overlap bound for these blocks, give

    ||K^(-1/2)sum_u a_u h_u||_(-1,S)^2 <= C A_l l^3      (10)

for any bounded deterministic coefficients a_u; constants can depend on
p,gamma,k0,Q, but not the matching. The stationary forward/backward
martingale identity gives, for the N-accelerated process,

    E|integral_0^t K^(-1/2)sum_u a_u h_u(eta_(Ns))ds|^2
                         <= C t A_l l^3/N.               (11)

For completeness, solve -S f=F on the orthogonal complement of its kernel.
The forward and reversed stationary martingales add to 2 integral F;
each has second moment 2t <f,-Sf>. The square inequality gives
E|integral F|^2<=2t||F||_-1^2, and acceleration divides by N. This uses
no reversibility or unproved sector estimate for the nonsymmetric part.

**Canonical linearization.** With q_C the empirical color law of C_l,
sampling the four distinct positions without replacement differs from
independent q_C sampling by O(l^-3). The polynomial (5) has bounded second
derivatives. Therefore

    hat j=J_delta(p)+A_delta(q_C-p)+W,
    E W=0,                 E|W|^2<=C l^-6.               (12)

The centering follows from E hat j=J_delta(p) and E q_C=p, separately for
each fixed geometric footprint. Independence of disjoint blocks and their
O(l^3) overlaps bound the normalized sum of W in L2 squared by C l^-3.
Stationarity bounds its time integral by C t^2 l^-3.

Replace q_C by q_l, the average over black sites in the ordinary cube.
Its cardinality m_l is independent of u and M_N. The removed boundary and
normalization change have squared L2 error at most C l^-4 for one block:
O(l^2) coefficients have size O(l^-3), and O(l^3) interior coefficients
change by O(l^-4). The overlap bound thus gives C/l for the normalized
weighted sum. This step is necessary; the geometric blocks need not be
translates of one another. A shift of this black-site cube by any allowed
pair displacement of length at most two gives the same C/l bound.

**Removing the routing directions.** The exact conservation equation has
coefficients

    a_(delta,u)=N[phi(q_delta u)-phi(u)],
    phi(u)=exp(-i Q.u/N),                                (13)

and outer factor 1/2. They are bounded uniformly. Constant currents cancel
exactly because each q_delta is a permutation, sum_u a_(delta,u)=0.
At fixed l expand

    a_(delta,u)=-i phi(u) Q.(delta-d_(q_delta u))+O(N^-1). (14)

The centered linear remainder contributes a squared L2 error C_l/N^2.
The delta term in (14), summed with A_delta/2, is precisely -i A(Q)
times the black-cube average of (8), by (6). Its Fourier multiplier tends
to one as N->infinity at fixed l.

For the remaining direction term change variables v=q_delta u. Its
linear part is proportional to

    K^(-1/2) sum_v (Q.d_v) sum_delta A_delta
                      phi(q_delta^-1 v)[q_l(q_delta^-1 v)-p]. (15)

Subtract phi(v)[q_l(v)-p] inside the delta sum; its coefficient vanishes
by sum_delta A_delta=0. The phase difference is O(N^-1), with an L2 error
C_l/N^2. The shifted-block difference has squared L2 bound C/l just proved.
Thus (15) vanishes in the successive limits N->infinity, then l->infinity,
uniformly in the matching. This is the cancellation that an expectation
calculation alone would miss.

Combining (11)-(15), the integrated generator error relative to -i A(Q)Y_N
has squared L2 bound

    C_T [A_l l^3/N + 1/l + C_l/N^2].                    (16)

All coefficients are deterministic given M_N. A jump changes (8) by at
most C_Q/(N sqrt(K)); there are O(K) bounded channels. The martingale
bracket for accelerated time is at most C_Q T/N. Variation of constants
and integration by parts of the integrated drift error now prove (9),
as in the finite-state proof. This requires only a supremum of expectations
over t<=T, not an unproved expectation of a time supremum.

Finally, the independent bounded pair colors obey the elementary
triangular-array central limit theorem. Fourier orthogonality on the black
sublattice holds for any fixed finite set of modes when N is sufficiently
large, retaining conjugacy at opposite modes. Thus the limiting fields are
Gaussian with initial covariance C=diag(p)-p p^T, propagated by (9).
The statement is uniform in geometry, so it also applies after averaging
over any geometry distribution independent of these stationary colors.

### 6. The transverse sector and what it actually measures

At orbit-isotropic p_a=rho_A/6 on A and rho_B/8 on B, with positive
rho_A+rho_B=1, the full linear current on the probability tangent gives

    partial_t X=(gamma rho_A/3) curl Y,
    partial_t Y=-gamma rho_B curl X.                     (17)

For gamma!=0 and the stipulated nonzero Fourier mode, it has speed
|gamma|sqrt(rho_A rho_B/3), four propagating transverse modes, two static
longitudinal modes and seven further static color moments. For gamma=0
all thirteen tangent modes are static.
All thirteen tangent directions are retained. Equation (9) makes (17) a
long-wavelength dynamic correlation limit for this supplied process, not
merely an eigenvalue calculation. No reflection or physical time-reversal
assignment is inferred from the even projector color map below.

The site field that reads the same color from both antipodal records has
Fourier sum N^(-3/2)sum_sites phi(x)[xi(x)-p]. It differs from sqrt(2)Y_N
in L2 by O(N^-1), since the two endpoints are one edge apart and colors
of different pairs are independent. Its covariance is consequently 2C,
with the same propagation matrix. The mode normalization must not be
silently identified with one independent color per site.

The geometric dimer field B_geo,i(x)=sigma_x[n_i(x)-1/6] still obeys the
full-packing Gauss identity, but **does not change** during these events.
The wave fields in (17) have positive longitudinal variances under pi_p.
They are different functions of the records. A local curl readout would
remove their divergence while restoring the previously studied k^2
spectral suppression; that is not a solution of the common-field problem.
Coexistence of a static correlated geometry and these waves is the result.

### 7. Continuous immutable contents and empty-start formation

Here is an explicit even color code using only P_n. For generic n define

    f(n)=(n_y n_z(n_y^2-n_z^2),
          n_z n_x(n_z^2-n_x^2),
          n_x n_y(n_x^2-n_y^2)).                         (18)

It obeys f(-n)=f(n) and f(Rn)=R f(n) for every proper signed-coordinate
rotation. If max_i |f_i|>(9/10)|f|, assign the A color given by the sign
and index of this unique dominant component. Otherwise assign the B color
sign(f). Exclude the algebraic zero/tie sets of spherical measure zero.
The A and B regions both have positive measure: neighborhoods of (0,1,2)
and (1,2,3), after normalization and away from the exceptional sets, suffice.
The six A regions have equal spherical measure, as do the eight B regions.

Let mu be normalized spherical area and alpha_A,alpha_B their total masses.
Choose the even proper-cubic-invariant reference density g0 with value
rho_A/alpha_A on A and rho_B/alpha_B on B. Thus each color has mass p_a,
and integral_(color a) n g0(n)dmu=0. Continuous independent draws have
distinct antipodal keys almost surely; exceptional code points are also
avoided almost surely. This does not provide an operational finite-qubit
measurement of the chosen exact-content classes.

Replace the geometric model's vacant-edge birth density by

    beta g0(n)[1+epsilon n.delta] dmu(n),  0<|epsilon|<1, (19)

with the edge temporarily ordered x,x+delta. Reversing the order sends
n,delta to -n,-delta and leaves the law unchanged. The total edge clock
is beta, and the conditional probability of every color is exactly p_a,
independent of delta and of all prior history. At a vacant site x with
available vacant-neighbor directions D_x, its forming-record law is

    g0(n)[1+epsilon n.(sum_(delta in D_x)delta)/|D_x|]dmu. (20)

It is normalized, depends only on nearest-neighbor occupancies, and varies
with those conditions. At |D_x|=0 use the unused reference g0; no birth
occurs there. Thus the changing nearest-neighbor one-record distribution
and history-independent **even color** distribution are compatible.

A single local process can run these births, the earlier symmetric vacancy
slides, and pair transport at every density. At a partial matching, include
the exchange on a cross edge whenever its two pairs exist; use (4) when
all four distinct context pairs exist, and its floor k0/2 otherwise. This
condition and the fallback are bounded-neighborhood tests and are unchanged
by the exchanged colors. We do **not** assert product stationarity for the
partial routing paths, whose endpoint telescoping terms need not cancel.
No global test of saturation switches the rule.

These additional exchanges leave geometry unchanged. The geometric birth
and slide chain, its filling theorem and its slow-birth selection results
therefore stay autonomous and unchanged. Starting empty, the successive
new pair colors have conditional law p, so the final K color counts are
exactly multinomial(K,p), independent of the entire geometric trajectory.
Pair exchanges and slides conserve these counts. The finite-volume process
still fills almost surely in finite mean time.

After filling, the matching freezes, the routing permutations are complete,
and the color chain converges within each fixed-count sector to its uniform
law. Mixing the multinomial counts gives exactly pi_p, independently of
the selected final matching, in the limit of additional elapsed time
s->infinity at this fixed finite volume. Fine record-key/orientation memory
need not be erased for this color-marginal conclusion. There is no claim
that the colors are already independent at the first completion time.

Consequently, one may first form and then take this fixed-volume late-time
limit, and only then take N->infinity in the stationary wave statement.
If uniform geometric matching selection is wanted, beta->0 at fixed N
is another explicitly ordered limit. No simultaneous schedule or physical
preparation time follows from these statements. The microscopic field
identification, rate selection, other readable modes, common Gauss/wave
sector and coherent quantum bridge remain open.

## II. Finite preparation from the completed formation process

2026-09-21. Root conditional theorem candidate, pending selective independent
reconstruction. This extends the fixed-geometry stationary result in
`DIMER_ROUTED_RECORD_TRANSPORT.md`. It supplies a conservative polynomial
post-completion color-preparation bound. It does not estimate the random
time to first complete the lattice, derive the rates, or identify the content
waves with the geometric Gauss field.

### 1. Claim and hypotheses

Use the same even cubic torus, N>=8, K=N^3/2 record pairs, fixed gamma,
k0>|gamma|, supplied paired births and record slides. At full packing retain
the dimer-routed whole-pair exchanges of the preceding note; matching geometry
is frozen. The permanent pair color has fourteen values, with positive fixed
birth probabilities p, and never changes. The final color counts are exactly
multinomial(K,p) and independent of the complete geometric history, as proved
there. No independence of the color arrangement at first completion is used.

Let tau_fill be the almost-sure finite first-completion time. For any perfect
matching M and any fixed color counts, define

    g_N = k0 / [4(3N-1)(K-1)].                                (1)

Then, for every initial color arrangement in that count sector,

    ||Law(colors at t)-Uniform(count sector)||_TV
      <= (1/2) sqrt(|Omega_counts|-1) exp(-g_N t)
      <= (1/2) 14^(K/2) exp(-g_N t).                          (2)

The bound is uniform over all perfect matchings, including winding extrema,
and is for the actual nonreversible color generator. It concerns the finite
color projection, not all continuous record keys or their orientations.

Consequently, for 0<epsilon<1/2, the deterministic waiting time

    t_prep(N,epsilon)
      = [4(3N-1)(K-1)/k0]
        [ (K/2) log(14) + log(1/(2 epsilon)) ]                (3)

after tau_fill brings the joint geometry/color law within epsilon in total
variation of

    Law(M at tau_fill) times iid_pair_colors(p).              (4)

This closes the extra ordered infinite-time preparation step in the previous
note by an explicit sufficient schedule. The bound is intentionally coarse,
of order N^7/k0 at fixed epsilon. It is not a measured mixing exponent, a
lower bound, a practical estimate, or a bound on tau_fill itself.

### 2. An elementary complete-transposition bound

First work with K distinct labels on K positions, uniform law on permutations.
For an unordered pair e={i,j}, write T_e for swapping positions and put

    D_all(f) = (1/2) sum_(i<j) E[(f(T_ij sigma)-f(sigma))^2].

We prove the sufficient, nonsharp inequality

    Var(f) <= (2/K) D_all(f),    K>=2.                       (5)

This proof imports no spectral-gap theorem for the interchange process.
For K=2 it follows directly (the sharp factor is 1/2). Suppose the bound is
known for K-1. Fix a position i and condition on the label at i. The remaining
permutation is uniform, so

    E Var(f | sigma(i)) <= [2/(K-1)] D_internal,i(f),

where internal swaps avoid i. Let F_i(a)=E[f | sigma(i)=a]. Couple the
conditional law with label a at i to that with label b at i by swapping i
with the unique position carrying b. This is a bijection between the two
conditional permutation spaces. Jensen's inequality therefore gives

    Var(F_i(sigma(i)))
       = (1/(2K^2)) sum_(a,b) [F_i(a)-F_i(b)]^2
       <= (1/(2K)) E sum_(j!=i) [f(T_ij sigma)-f(sigma)]^2
       = D_cross,i(f)/K.                                    (6)

Average the conditional-variance identity over i. Each swap is internal for
K-2 positions and crosses two positions. Thus

    Var(f) <= [ 2(K-2)/(K(K-1)) + 2/K^2 ] D_all(f)
            <= (2/K) D_all(f).

For a color multiset, lift a function of colors to a function of the uniform
distinct-label permutation. The induced color law is uniform on its count
sector, with exactly the same variances and swap energies. Equation (5)
therefore applies to every color-count sector, including the trivial ones.

### 3. Comparison to swaps on a connected graph

Let H be any connected simple graph on these K positions, of diameter D>=1,
and let D_H use only its edges at unit rate. For every unordered pair x,y,
choose a simple path x=x_0,...,x_l=y, l<=D. The endpoint transposition is the
sequence of neighboring swaps

    (x_0 x_1),...,(x_(l-1) x_l),
    (x_(l-2) x_(l-1)),...,(x_0 x_1).

It has 2l-1 moves and restores every intermediate label; it swaps only the
two endpoint labels. At most two occurrences of any physical edge appear.
Cauchy--Schwarz and invariance of the uniform count law under each preceding
permutation give

    E[(f(T_xy sigma)-f(sigma))^2]
       <= (2D-1) sum_(steps on the chosen route) E[(Delta_e f)^2].

In the sum over all K(K-1)/2 endpoint pairs, a physical edge occurs at most
K(K-1) times. This deliberately crude count needs no congestion theorem or
special geometry. Hence

    D_all <= (2D-1) K(K-1) D_H,
    Var(f) <= 2(2D-1)(K-1) D_H(f).                           (7)

If a symmetric generator has at least rate r on every edge of H, its gap
on each nontrivial color sector is at least

    r / [2(2D-1)(K-1)].                                      (8)

All factors refer to the continuous-time convention D=-<f,Sf>; no lazy
discrete-time normalization is being imported.

### 4. Apply the comparison to the actual routed chain

For a perfect matching M, contract each dimer to one pair-position vertex.
Retain every nonmatching nearest-neighbor edge between distinct dimers and
then forget multiplicity. The resulting H is connected. A shortest physical
lattice path between any chosen representatives has length at most 3N/2;
contracting its matching edges cannot increase length. Thus D<=3N/2.

Every edge of H is represented by at least one nonfixed routed channel.
The preceding note's pointwise stationarity argument gives uniform law in
each color-count sector and symmetric rate k0/2 for every channel. Duplicate
physical channels add, so the actual symmetric part S=(L+L*)/2 dominates
(k0/2) times the unit-rate graph-swap form. Applying (8) gives exactly (1).
The antisymmetric drive does not worsen this L2 contraction bound.

For completeness, if h_t is the density of the evolving law with respect
to the uniform stationary sector measure, then

    d/dt ||h_t-1||_2^2
       = 2 <h_t-1, S(h_t-1)> <= -2g_N ||h_t-1||_2^2.

This uses the adjoint generator on densities; its symmetric part is the
same S. A point mass has squared centered norm |Omega_counts|-1. The
inequality ||law-pi||_TV <= (1/2)||h-1||_2 proves (2). Mixtures of point
masses obey the same bound. Since |Omega_counts|<=14^K, (3) follows.

### 5. Formation, preparation and the joint wave limit

Condition on the completed matching, the accumulated color counts and the
entire history up to tau_fill. The post-completion color law can start at
any arrangement in that sector, but (2) is uniform over all such starts and
all M. The strong Markov property makes the same estimate valid after the
random first-completion time. Average over that history. The counts have
multinomial(K,p) law independently of M, and the mixture of uniform count
sectors with those weights is exactly the iid product law pi_p. This proves
(4); neither geometric mixing after completion nor a fine-key mixing claim
is required.

Take epsilon_N=N^-4 in (3). Starting observations at

    tau_fill + t_prep(N,N^-4),

the joint law of any subsequent color trajectory and M differs from the
stationary reference trajectory law by at most N^-4, by contraction of total
variation under the common Markov path kernel. Bounded distributional tests
therefore inherit the previously proved, matching-uniform finite-mode Euler
wave limit at times Nt after preparation.

The same choice also transfers the stated mean-square approximation. Every
normalized color Fourier field is bounded by a fixed constant times sqrt(K).
At fixed wave times/modes/parameters the finite-dimensional propagator has
bounded norm, so the squared propagation residual is bounded by C K. Changing
trajectory law by total variation N^-4 changes its expectation by at most
C' K N^-4=O(N^-1). This tends to zero alongside the stationary theorem's
residual. The stationary Gaussian initial-field limit and its finite-time
propagation thus hold on this explicit joint preparation/volume schedule.

The geometric law in (4) is whatever the chosen finite-rate formation process
produces. Uniform geometric selection still needs its separate slow-birth
argument. The Gauss readout of that geometry remains static here; only the
record-color sector propagates. This is a controlled accessibility result
for one supplied process, not rate selection, a physical measurement scheme,
or evidence for a TOE.

### 6. Decisive checks planned

Replay endpoint-transposition routes on immutable labels, test the finite
count-sector Dirichlet constants on connected small graphs, and separately
check the conditional-mean coupling and a nonreversible density contraction.
The deterministic proof above supplies the all-volume argument; numerical
spectral checks cannot establish its uniformity. Author controls and a
selective independent reconstruction remain pending at this source revision.

## III. Extension to autonomous moving geometry

2026-09-21. Root conditional theorem candidate, not yet independently checked.
Dependencies are the corrected `DIMER_ROUTED_RECORD_TRANSPORT.md` and the
provisional `DIMER_ROUTED_POLYNOMIAL_COLOR_PREPARATION.md`. This note supplies
a complete extension argument, not an appeal to stationarity of an unproved
geometric equilibrium. It introduces no new record contents or primitive.
The additional plaquette-rotation channel is a supplied dynamics choice.

### 1. Dynamics and statement

On the same even cubic torus N>=8 at full matching density, add the following
to the routed pair exchanges. Whenever a nearest-neighbor square contains
two matching edges on opposite sides, rotate its four complete immutable
records clockwise at rate nu and counterclockwise at rate nu, with fixed
nu>=0. Each of its records moves one nearest-neighbor step. The resulting
two pairs occupy the other two sides of the square. All other records are
unchanged. Geometry has an autonomous plaquette-flip generator with rate
2nu per flippable square, independent of every color and fine key.

Use the temporary black sublattice to index a pair by its current black
endpoint. Since the color code is antipodally even, changing which record
of a pair is black does not change that pair's color. On a flippable square
one rotation sense swaps the two black-endpoint colors, while the other
leaves the black-endpoint colors in place. Which sense swaps depends on
the initial matching orientation; the equal rates fix the coefficient nu
in the color drift formula below.

Start with any law of the perfect matching M_0, and iid pair colors with a
fixed full-support p independent of M_0. Run the full joint process. For
each fixed finite list of Fourier modes and macroscopic times, the same
stationary-color finite-mode conclusion as the preceding routed theorem
holds, uniformly over the initial matching law:

    E |Y_N(t)-exp(-i A(Q)t)Y_N(0)|^2 -> 0,                  (1)

where the joint process is observed at microscopic time Nt and Y_N is the
K^(-1/2)-normalized color Fourier field on fixed physical black sites. Its
initial finite-mode Gaussian law, covariance and propagation matrix A(Q)
are unchanged. At orbit-isotropic p_a=rho_A/6 on A and p_a=rho_B/8 on B,
with positive rho_A+rho_B=1, its transverse color-wave speed is unchanged.
For nonzero gamma and fixed nonzero Q in this isotropic specialization there
are four propagating and nine static tangent modes. At gamma=0 all thirteen
tangent modes remain static on this Euler scale.

The matching need not be at equilibrium, mix, or remain fixed during the
observation window. The proof needs its autonomy from the colors, uniform
stationarity of the color sectors under routed exchanges, and fixed bounded
nu. It does not apply to color-dependent geometric rates or arbitrary biased
plaquette rotations. No geometric photon or physical field identity follows.

### 2. Conditional color law along an entire geometric history

Realize the autonomous geometry process with independent geometric clocks,
and attach its equally likely clockwise/counterclockwise marks. Its finite
history on a bounded time interval is independent of the initial colors and
the randomness used by the routed exchanges. Condition on that entire marked
history. There are then finitely many prescribed times at which the pair-color
configuration undergoes a specified permutation of black positions. Between
them, the color generator is the fixed routed generator L_M of the matching
on that interval.

Each L_M preserves every iid law pi_p and every uniform fixed-count law.
Every prescribed color permutation preserves the same measures. Thus the
conditional color law is exactly pi_p at every time, even though its
conditional trajectory is generally time inhomogeneous. The same statement
holds in each count sector. In particular, colors and the entire marked
geometric history are independent at any one specified time. Their joint
histories need not be independent.

This conditional stationarity is stronger than requiring an invariant law
for M. It is why arbitrary, possibly irregular initial geometric laws are
allowed in (1).

### 3. A time-inhomogeneous forward/backward energy estimate

The finite-state estimate used in the fixed-geometry proof extends to this
conditioned history. Let F_m be a centered color function on its m-th constant-
geometry interval, orthogonal to the global-count kernel, and let S_m be the
symmetric part of L_m. Solve -S_m f_m=F_m separately in each finite sector.
For that interval [a_m,b_m], the forward and stationary reversed martingale
increments are

    M_m^+ = f_m(eta_(b_m-))-f_m(eta_(a_m+))
             - integral_(a_m)^(b_m) L_m f_m(eta_s) ds,
    M_m^- = f_m(eta_(a_m+))-f_m(eta_(b_m-))
             - integral_(a_m)^(b_m) L_m^* f_m(eta_s) ds.

The reversed increment is a martingale increment with respect to the
reversed conditional path law: the color measure is the same stationary
measure at each endpoint, the interval semigroup reverses to its adjoint,
and each prescribed boundary permutation reverses to its inverse.
Their sum is exactly twice the integral of F_m on that interval.

Sum the forward increments in temporal order and the backward increments
in reversed order. Within either sum, the martingale increments are
orthogonal in L2, including across the intervening prescribed permutations.
Their endpoint functions can differ from interval to interval: cancellation
is made within each forward/backward interval pair, not by pretending that
one time-independent Poisson solution works across all matchings. Hence

    E[ |sum_m integral_(a_m)^(b_m) F_m(eta_s) ds|^2
          | marked geometry history ]
      <= 2 sum_m (b_m-a_m) ||F_m||_(-1,S_m)^2.              (2)

For complex functions use real and imaginary parts, with an inessential
fixed factor if their norms are recorded separately. No bound depends on the
number of geometric jumps. The torus is finite and rates are bounded, so
this number is almost surely finite at every finite N and time. Averaging
over the geometry history preserves the estimate.

### 4. The routed drift retains its uniform replacement proof

For each matching visited, use the contracted all-site cube C_l(u) and the
ordinary black cube B_l(u) of the original proof. The connected-block
Poincare constants A_l were uniform over all matching patterns. Equation (2)
therefore gives the same accelerated integrated-current bound

    C_T A_l l^3 / N

for the centered routed currents. The geometry-dependent Fourier gradient
weights remain bounded uniformly.

The canonical sampling, Taylor remainder, block boundary and shifted-block
estimates also remain valid. Conditioned on the entire geometric history,
the color configuration at each time is product-distributed. Disjoint block
color variables are therefore independent at that time. The relevant
O(l^3) overlap and O(l^2) boundary counts are deterministic and uniform in M.
Integrating the corresponding fixed-time L2 bounds uses Cauchy--Schwarz in
time; it does not assume temporal independence of colors or geometry.

The variable-direction cancellation is pointwise in the current matching:
q_delta remains a bounded-displacement permutation, and sum_delta A_delta=0.
After replacing C_l averages by ordinary B_l averages, the common Fourier
field is on fixed physical black sites. No derivative of a changing matching
coordinate system is introduced. Thus the routed part of the drift again
has integrated error bounded by

    C_T [ A_l l^3/N + 1/l + C_l/N^2 ].                       (3)

### 5. The extra plaquette color drift vanishes on the Euler scale

Let F be one normalized color Fourier component on black sites. The actual
plaquette contribution to its generator is

    (K_M F)(eta) = nu sum_(p flippable in M)
                       [F(T_(u_p,v_p) eta)-F(eta)],          (4)

where u_p,v_p are the opposite black vertices of square p. The other rotation
sense leaves F unchanged. Here K_M is an auxiliary color-only symmetric swap
operator at fixed M, used to compute this observable's actual joint drift;
it is not a replacement rule for the evolving matching.

Every swap edge in (4) is an edge of the dimer-contracted graph for M: one
nonmatching side of the flippable square connects the two occupied dimers.
For N>=8 a pair of opposite black vertices determines at most one such
elementary square. The routed symmetric part has at least rate k0/2 on each
of these edges. Therefore the two color Dirichlet forms obey

    D_KM(f) <= (2nu/k0) D_SM(f).                             (5)

Cauchy--Schwarz in D_KM and the variational definition of H-minus-one norm
give, for nu>0,

    ||K_M F||_(-1,S_M)^2 <= (2nu/k0) D_KM(F).                (6)

For nu=0 this drift is exactly zero. The Fourier phase difference across
opposite black square vertices is O(|Q|/N), the normalization is K^(-1/2),
the colors are bounded, and there are O(K) squares. Consequently

    D_KM(F) <= C nu |Q|^2/N^2,
    ||K_M F||_(-1,S_M)^2 <= C nu^2 |Q|^2/(k0 N^2),           (7)

uniformly in M. Apply (2) to this centered color function on microscopic
time [0,Nt]. It is centered in each count sector because K_M preserves that
uniform law. Equations (6)-(7) yield

    E | integral_0^(Nt) K_(M_s) F(eta_s) ds |^2
       <= C t nu^2 |Q|^2/(k0 N).                            (8)

This is the integral of the actual plaquette drift in the Fourier martingale
decomposition. It tends to zero. The decomposition itself is taken in the
unconditioned joint process; conditioning was used only to estimate its
drift integral. It does not replace random geometric event times by their
conditional deterministic values inside a generator formula.

Every joint jump changes F by O(1/(N sqrt(K))). There are O(K) bounded-rate
channels, so the full martingale bracket over microscopic time Nt is O(1/N).
Combine this with (3), (8), and variation of constants as in the original
proof. First take N->infinity at fixed l, then l->infinity. The same iid
initial Fourier CLT completes (1).

### 6. Explicit preparation still works while geometry moves

The comparison bound g_N in the provisional preparation note holds for every
M with the same constant. Condition on the marked geometric history after
first completion and start with any color arrangement in its count sector.
Between geometric events the centered density L2 norm contracts at least as
exp(-g_N times elapsed time). At a prescribed geometric event the color
permutation preserves that norm. Multiplying interval bounds gives the same
uniform total-variation estimate at the final elapsed time.

The birth-generated counts remain multinomial and independent of the
autonomous complete geometric history. Thus, after the same explicit
t_prep(N,epsilon), the color law is within epsilon of iid pi_p independently
of the geometric history. More precisely this is a bound on the joint law
of the observed color configuration and that history, whose geometry marginal
is unchanged. Subsequent evolution by the common joint Markov kernel cannot
increase total variation. Taking epsilon_N=N^-4 transfers (1) and its
mean-square conclusion from the stationary-color reference process, with the
same O(K epsilon_N) error bound.

This statement permits adding the color-independent plaquette channel during
formation as well. The autonomous geometric filling process and iid color
increments persist. The earlier finite filling proof still applies with the
extra finite-rate geometric moves. The first-completion time remains random;
no upper bound on it in the joint volume limit is supplied here.

### 7. A precise boundary for the geometric Gauss field

Microscopic geometric motion does not automatically make its Gauss field the
propagating color field. One rigorous comparison is available if geometry is
started in an invariant law of its own symmetric plaquette chain, for example
uniform measure in a communicating class or any mixture of these measures.
No connectivity of the complete perfect-matching space is assumed.

Let eta(x)=(-1)^(x_1+x_2+x_3) and

    B_i(x)=eta(x)[ 1_{ {x,x+e_i} in M } - 1/6 ].

Its exact lattice divergence vanishes by the matching constraint. For a fixed
nonzero long-wavelength mode k=Q/N, normalize its edge-midpoint Fourier sum
by N^(-3/2). A plaquette flip changes its four link terms by a discrete curl;
its Fourier increment is O(|Q|/(N sqrt(N^3))). Thus the geometric Dirichlet
energy of each such mode is at most C nu |Q|^2/N^2. Reversibility gives

    E |B_N(Nt)-B_N(0)|^2
       = 2 <B_N,(I-exp(Nt L_geo))B_N>
       <= 2Nt D_geo(B_N) <= C nu t |Q|^2/N -> 0.             (9)

Equation (9) uses stationary reversible geometry; it is not asserted for
arbitrary nonstationary initial geometry. It needs no geometric spectral gap
or phase assumption. The content waves of (1) and the geometric field of (9)
therefore have distinct Euler-scale behavior in this supplied model. Finding
one physical field with both the desired constraints and dynamics remains
open. The construction supplies no quantum preparation, Lorentz symmetry,
gravity or empirical prediction.

### 8. Check scope

Finite controls should replay actual clockwise/counterclockwise immutable
record motion and its color projection, check the swap-form domination,
verify a switched finite-chain version of (2), and test the discrete-curl
Fourier increment. These will check load-bearing steps, not establish an
infinite-volume theorem by numerical extrapolation. The complete proof and
new controls require a selective independent reconstruction before shipping.

## IV. Cubic-lattice comparison and the improved preparation time

2026-09-21. Root conditional proof candidate; independent check pending.
This strengthens the earlier polynomial preparation estimate by using the
geometry of the torus instead of the worst possible connected graph. The
earlier note and its sealed check remain unchanged and valid. No sharp
interchange-process theorem is imported.

### 1. Statement and unchanged premises

Let N>=8 be even, K=N^3/2, and let M be any perfect nearest-neighbor matching
of the cubic torus. Let H_M be the simple graph obtained by contracting each
matched pair. Use the same immutable pair exchanges with k0>|gamma|. The
uniform measure in each color-count sector is invariant, and its symmetric
generator S_M has rate at least k0/2 on every edge of H_M.

The following stronger uniform Poincare bound holds:

    Var_mu(f) <= [8 N(3N-1)/k0] D_SM(f),
    gap(S_M) >= g'_N := k0/[8 N(3N-1)].                    (1)

Singleton count sectors have zero variance and satisfy the inequality
trivially. This is a lower bound on the symmetric spectral gap, not a
diagonalization of the nonreversible generator or a sharp gap assertion.
It is uniform over the matching and conserved color counts.

The sufficient post-completion waiting time can therefore be replaced by

    t'_prep(N,epsilon) = (8 N(3N-1)/k0)
                         [ (K/2) log 14 + log(1/(2epsilon)) ].       (2)

For epsilon_N=N^-4 this is O(N^5/k0), with leading coefficient
6 log(14)/k0. It remains a deliberately conservative sufficient time, not
a measured relaxation time or a lower bound. The random completion time is
still additional and has no volume-uniform upper bound here.

### 2. Physical torus paths and their congestion

For every ordered pair of physical vertices (x,y), use this deterministic
nearest-neighbor path. Move coordinates 1, then 2, then 3. In each cyclic
coordinate use the shortest displacement; for the tie N/2 choose the
positive direction. The path has length at most 3N/2 and is translation
covariant. Every coordinate segment visits any undirected edge at most
once.

Fix an undirected physical edge e in coordinate direction i. The total
number of these ordered reference paths using e is exactly

    N^4/4.                                                (3)

To count it, in one cyclic coordinate the sum of the shortest distances
over all target displacements from a fixed start is

    2 sum_(r=1)^(N/2-1) r + N/2 = N^2/4.

Summing over N starts gives N^3/4 total one-dimensional edge traversals.
Translation covariance makes every one of the N undirected cyclic edges
carry N^2/4 paths. For an edge in the three-dimensional coordinate-i
segment, the other two coordinates each leave one freely chosen endpoint
coordinate; their multiplicity is N^2. This proves (3), including the tie
convention. Count actual path use, not just endpoint distance.

For each unordered pair of matched dimers, take their black endpoints u,v,
choose a fixed lexicographic order and use the corresponding physical path
u to v above. This is a subset of the ordered all-vertex path family, so
its load on each physical edge is at most (3).

Project each path to H_M by replacing a physical vertex by its matched pair,
discard consecutive repetitions and erase loops chronologically. The result
is a simple path between the specified dimers, still of length at most
3N/2. Every remaining contracted edge was traversed by the original physical
path; loop erasure adds no new edge.

Any two distinct matched dimers have at most two nonmatching physical
nearest-neighbor edges between them. Each dimer has one black and one white
endpoint, and a nearest-neighbor edge connects opposite parity. The only
candidates are black(u)-white(v) and black(v)-white(u). Therefore the number
of these projected reference paths using a fixed simple edge of H_M is at
most

    2 (N^4/4) = N^4/2.                                   (4)

This count remains valid for arbitrarily irregular M. It does not require a
periodic matching, a mixing law on matchings, or a favorable typical geometry.

### 3. Endpoint transpositions and the Dirichlet constant

Let D_all be the complete-graph unit-rate transposition Dirichlet form and
D_H the unit-rate simple-edge transposition form on H_M, both with the
convention D=(1/2) sum_edges E_mu[(Delta_e f)^2]. The earlier independently
checked elementary permutation argument gives

    Var_mu(f) <= (2/K) D_all(f).                          (5)

It applies to every color-count sector by equal-size distinct-label fibers.

An endpoint transposition along a simple path of length ell is realized by
the forward edge word followed by its reverse with the last edge omitted.
It has length 2ell-1<=3N-1, each path edge occurs at most twice, and every
intermediate immutable key returns to its original position. From (4), the
total word-use count of any H_M edge over all unordered reference pairs is
at most N^4. Telescoping, Cauchy--Schwarz and invariance of the uniform sector
under each preceding swap then give

    D_all <= (3N-1) N^4 D_H,
    Var_mu(f) <= (2/K)(3N-1) N^4 D_H
               = 4N(3N-1) D_H.                           (6)

The actual symmetric form dominates (k0/2)D_H. Substitution into (6) gives
(1). All channel multiplicities can only improve this lower bound; no
deduplication of the physical generator is performed.

### 4. Preparation and moving geometry

The earlier density-energy identity now yields

    TV(law_t, uniform count sector)
       <= (1/2) sqrt(|Omega_counts|-1) exp(-g'_N t)
       <= (1/2) 14^(K/2) exp(-g'_N t).                    (7)

Equation (2) makes the last expression epsilon. The argument uses the
symmetric form of the adjoint density generator and does not assume
reversible routed dynamics.

At first completion, the stated formation construction gives multinomial
counts independently of the autonomous geometry. The same strong-Markov,
count-mixture and total-variation arguments as in the earlier preparation
note apply with (2). The mean-square transfer error is still bounded by
C K epsilon_N = C/(2N) for epsilon_N=N^-4.

If the moving-geometry extension is accepted, its proof also applies with
g'_N. Conditioned on a complete marked autonomous geometry history, every
between-jump color semigroup contracts at this common rate, and each
prescribed boundary color permutation is an L2 isometry. Multiplying these
contractions gives (7) in elapsed time even while geometry moves. No
geometric equilibrium or clock freezing is used for this conclusion.

The moving-geometry statement retains that extension as an explicit open
dependency until its separate check is complete. The fixed-geometry
comparison (1)-(7) does not depend on the moving-geometry proof.

### 5. Limits and finite checks

Finite controls should count the ordered physical path loads, project the
black-endpoint paths for winding, columnar and irregular matchings, verify
loop erasure and immutable endpoint words, and check the constants on
independent finite color sectors. The proof above supplies all-volume
uniformity; a finite graph inventory does not supply that inference.

No logarithmic Sobolev theorem, sharp color mixing time, empty-start filling
estimate, physical time calibration, quantum preparation or TOE result is
asserted. This is a better explicit preparation schedule for the same
supplied local classical dynamics and its conditional color-wave theorem.

## Verification and remaining physics

[The evidence packet](../.claude/science/mobile-record-moving-geometry-waves-20260921/README.md) preserves all four primary arguments,
four complete author suites and four portable selective-review packets.
The runner executes thirteen mathematical control groups and one source
bookkeeping check in an isolated temporary directory. Exact finite path,
permutation, balance and Fourier controls test the proof's normalization
and mechanisms; finite matrices and numerical moment calculations have
their floating-point limits stated in the source results. Three deliberate
mutations test the current normalization, the physical plaquette motion
and restoration of intermediate immutable keys.

The all-volume conclusions come from the complete conditional proofs,
including the block replacement and time-dependent energy arguments.
Simulation trends do not establish those conclusions and are not used
as evidence in this theorem packet. No nonlinear hydrodynamic theorem,
optimal mixing time, quantum state preparation, Born rule, Lorentz
symmetry, gravity, empirical prediction or TOE follows from this result.

The highest-priority missing physics is a justified bridge between a
propagating field and the geometric constraint, with a microscopic law
and state-selection mechanism that do not simply supply the desired
continuum structure. This proposed theorem and its formation dependency
remain unaudited; formal retained status belongs to the repository's
independent audit path.
