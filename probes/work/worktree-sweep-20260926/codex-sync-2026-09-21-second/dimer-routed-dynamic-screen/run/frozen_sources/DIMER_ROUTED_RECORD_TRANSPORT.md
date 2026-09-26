# Whole-pair transport and transverse waves on an arbitrary formed matching

2026-09-21. Root proposed construction and conditional finite-mode theorem.
Author controls and independent review are pending. The purpose is to put
formation, immutable records and a propagating content sector on one state
space. The geometric dimer Gauss field remains static in the full-state
transport below; it is not identified with the propagating content fields.

## 1. State and explicitly supplied choices

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

## 2. Six local routing permutations

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

## 3. Local rates and exact stationary laws

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

## 4. Product currents and geometric cancellation

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

## 5. Quenched stationary finite-mode propagation

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

## 6. The transverse sector and what it actually measures

At orbit-isotropic p_a=rho_A/6 on A and rho_B/8 on B, with positive
rho_A+rho_B=1, the full linear current on the probability tangent gives

    partial_t X=(gamma rho_A/3) curl Y,
    partial_t Y=-gamma rho_B curl X.                     (17)

It has speed |gamma|sqrt(rho_A rho_B/3), four propagating transverse modes,
two static longitudinal modes and seven further static color moments.
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

## 7. Continuous immutable contents and empty-start formation

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
