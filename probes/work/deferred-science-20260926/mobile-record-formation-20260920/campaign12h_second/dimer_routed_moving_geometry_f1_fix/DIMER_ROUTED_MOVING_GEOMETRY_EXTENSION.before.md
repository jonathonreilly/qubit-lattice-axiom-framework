# Record-color waves with continuing geometric motion

2026-09-21. Root conditional theorem candidate, not yet independently checked.
Dependencies are the corrected `DIMER_ROUTED_RECORD_TRANSPORT.md` and the
provisional `DIMER_ROUTED_POLYNOMIAL_COLOR_PREPARATION.md`. This note supplies
a complete extension argument, not an appeal to stationarity of an unproved
geometric equilibrium. It introduces no new record contents or primitive.
The additional plaquette-rotation channel is a supplied dynamics choice.

## 1. Dynamics and statement

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
initial finite-mode Gaussian law, covariance and transverse color-wave
speed are unchanged. For nonzero gamma, fixed nonzero Q and positive orbit
masses there are four propagating and nine static tangent modes. At gamma=0
all thirteen tangent modes remain static on this Euler scale.

The matching need not be at equilibrium, mix, or remain fixed during the
observation window. The proof needs its autonomy from the colors, uniform
stationarity of the color sectors under routed exchanges, and fixed bounded
nu. It does not apply to color-dependent geometric rates or arbitrary biased
plaquette rotations. No geometric photon or physical field identity follows.

## 2. Conditional color law along an entire geometric history

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

## 3. A time-inhomogeneous forward/backward energy estimate

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

## 4. The routed drift retains its uniform replacement proof

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

## 5. The extra plaquette color drift vanishes on the Euler scale

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

## 6. Explicit preparation still works while geometry moves

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

## 7. A precise boundary for the geometric Gauss field

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

## 8. Check scope

Finite controls should replay actual clockwise/counterclockwise immutable
record motion and its color projection, check the swap-form domination,
verify a switched finite-chain version of (2), and test the discrete-curl
Fourier increment. These will check load-bearing steps, not establish an
infinite-volume theorem by numerical extrapolation. The complete proof and
new controls require a selective independent reconstruction before shipping.
