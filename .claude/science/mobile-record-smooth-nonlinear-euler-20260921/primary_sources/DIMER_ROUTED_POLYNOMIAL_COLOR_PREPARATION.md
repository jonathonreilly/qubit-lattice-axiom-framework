# A finite preparation time for the routed record-color wave sector

2026-09-21. Root conditional theorem candidate, pending selective independent
reconstruction. This extends the fixed-geometry stationary result in
`DIMER_ROUTED_RECORD_TRANSPORT.md`. It supplies a conservative polynomial
post-completion color-preparation bound. It does not estimate the random
time to first complete the lattice, derive the rates, or identify the content
waves with the geometric Gauss field.

## 1. Claim and hypotheses

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

## 2. An elementary complete-transposition bound

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

## 3. Comparison to swaps on a connected graph

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

## 4. Apply the comparison to the actual routed chain

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

## 5. Formation, preparation and the joint wave limit

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

## 6. Decisive checks planned

Replay endpoint-transposition routes on immutable labels, test the finite
count-sector Dirichlet constants on connected small graphs, and separately
check the conditional-mean coupling and a nonreversible density contraction.
The deterministic proof above supplies the all-volume argument; numerical
spectral checks cannot establish its uniformity. Author controls and a
selective independent reconstruction remain pending at this source revision.
