# Exact contraction test for the frozen fourteen-color preparation

Author research note, 2026-09-22. Status: exact author certificate; independent
check pending. This is a scoped incompatibility candidate for a specified code
and specified classical dynamics. It is not a theorem against mobile records,
the framework, other quantum codes, or a theory of everything. No formal audit
status is claimed. The no-go publication packet is not complete.

## Target and supplied premises

Let N be even, N >= 8, and take the periodic cubic lattice of side N. Let U be
its even sublattice, K=N^3/2, with the fixed matching white(u)=u+e1. A matched
pair carries one of fourteen labels: six A labels with e_a in {+/-ei} and b_a=0,
and eight B labels with e_a=0 and b_a in {+/-1}^3. These labels, the following
rates, and the quantum preparation are supplied model choices. They are not
derived from the repository's minimal axioms. The M2 site factor is respected
by the four-qubit encoding considered here, but its placement into four
physical sites per classical pair is a separate unprovided locality map. The
test gives each classical pair its own abstract sixteen-dimensional factor.
It already fails in this relaxed placement domain.

For delta in {+/-ei}, q_delta(u)=u+a_delta, a_delta=delta-e1. Omit the identity
route delta=+e1. On a routed edge (u,u+a), write the four labels at
(u-a,u,u+a,u+2a) as (l,c,d,r). Define the real symmetric color matrix

    S_delta(c,d) = (gamma/2) delta . (e_c cross b_d + e_d cross b_c).
    h(l,c,d,r) = S(l,c)+S(c,r)-S(l,d)-S(d,r).

The generator swaps c and d at rate k0/2+h/4. Use k0=11/10 and gamma=1.
Since each S entry has magnitude <= |gamma|/2, the rate is >= 1/20. The
definition is the frozen routed dynamics of the prior campaign, not a new
quantum law. All four stencil positions are distinct at the witness size.

Let rho_a be exactly the strictly positive sixteen-dimensional states of
`../campaign12h_second/DIMER_TWO_PAIR_FAITHFUL_COVARIANT_ENCODING.md`.
For reproducibility, construct the proper signed-permutation group G, put
U_R=1 direct-sum R and V_R=U_R tensor U_R, and use reference labels e1 and
(1,1,1). For i=0,...,15 let

    vA_i = (7 i^2 + 3 i + 5) mod 17 - 8,
    vB_i = (11 i^3 + 4 i + 1) mod 19 - 9.

For each reference label form S=I16+sum_(R fixes label) V_R vv^T V_R^T;
normalize by its trace (1168 and 2125 respectively), and transport by V_R.
Stabilizer invariance makes transport independent of the representative.
This positive covariant preparation is faithful to classical probabilities;
that earlier result does not assert operational label discrimination.

For a joint classical law mu set

    E(mu) = sum_config mu(config) tensor_(u in U) rho_(config_u).

The precise target is a differentiable family of CPTP maps Lambda_t, t>=0,
with Lambda_0 the identity, satisfying

    Lambda_t E(mu) = E(exp(t L_class) mu)

for every joint classical law mu, at least for sufficiently small t>=0.
The candidate obstruction allows arbitrary global quantum maps and generated
correlations. It does not require a separate CP realization of each classical
transition, a sum of local Lindblad terms, a semigroup assumption beyond the
specified classical side, detailed balance, or a particular Hamiltonian.

## Stationarity and the exact initial linearization

Every homogeneous product law p^tensor K is stationary. A swap preserves its
weight. Reverse-minus-forward rates equal -h/2 because h changes sign upon
swapping c,d. Summing h along a routed cycle gives zero: the terms involving
nearest routed neighbors cancel by index shift, while the two distance-two
terms cancel using symmetry of S. Each route is a permutation of U, so this
cycle proof covers its entire torus. Therefore the full generator leaves the
product law stationary. This assertion does not say the law remains a product
after an inhomogeneous perturbation.

Write p0_a=1/14. Then S_delta p0=0. If the initial site distributions are
p0+epsilon f_u, with sum_a f_u(a)=0, direct expectation of the four-color swap
current and extraction of its linear coefficient gives

    (Lf)_u = sum_delta { (k0/2)(f_(u-a)+f_(u+a)-2 f_u)
                + (1/28) S_delta
                  (f_(u-2a)+f_(u+a)-f_(u-a)-f_(u+2a)) }.

This is the exact initial marginal derivative in the product tangent. It is
not a closure assumption at positive times. One can recover it by linearizing
the exact product-current formula in the prior nonlinear-drift note, which is
also an input pinned by the runner.

Restrict to profiles depending on the first coordinate x and set

    f_x(a) = (e_a,2/2) X_x + (b_a,3/8) Y_x.

The delta=+e1 route is absent. Delta=-e1 shifts x by -2; the other four
routes shift x by -1 and their S matrices cancel in pairs. Direct color
sums give S_-e1 vY=-gamma vX and S_-e1 vX=-4 gamma vY. Hence exactly

    dot X = D X + A Y,       dot Y = D Y + 4 A X,
    D f_x = (k0/2)[f_(x-2)+f_(x+2)-2f_x
                         +4(f_(x-1)+f_(x+1)-2f_x)],
    A f_x = -(gamma/28)[f_(x+4)+f_(x-2)-f_(x+2)-f_(x-4)].

The runner checks this reduction against the full fourteen-color expression
at every coordinate of each reported witness, using integer arithmetic.

## Quantum contraction and reduction to one-factor marginals

For sigma>0 and Hermitian Delta define

    Q_sigma(Delta)=Tr[Delta sigma^-1 Delta].

For any CPTP Phi with Phi(sigma)>0,
Q_(Phi sigma)(Phi Delta) <= Q_sigma(Delta). Here is a short proof, without
importing an unchecked classification theorem. The block matrix with rows
(sigma,Delta) and (Delta,Delta sigma^-1 Delta) is positive by its Schur
complement. Apply id_2 tensor Phi and then take the Schur complement with
respect to Phi(sigma). This gives

    Phi(Delta sigma^-1 Delta) >= Phi(Delta)(Phi sigma)^-1 Phi(Delta).

Trace preservation proves the inequality. This is an instance of the
monotone quantum chi-squared metrics studied in Temme et al.,
https://arxiv.org/abs/1005.2358 (equation7 at alpha=0 or1, Theorem4).
The elementary argument above is the proof dependency used here.

Let tau=mean_a rho_a and Sigma=tau^tensor K. The claimed intertwining fixes
Sigma by classical stationarity. For a differentiable product preparation
with one-factor tangent d_x, its tangent at epsilon=0 is

    Delta = sum_x d_x tensor_(y != x) tau.

Because Tr(d_x)=0, cross-factor terms vanish and
Q_Sigma(Delta)=sum_x Tr[d_x tau^-1 d_x]. For its quantum generator G, even
if G Delta contains arbitrary higher correlations,

    d/dt Q_Sigma(Lambda_t Delta)|0
      = 2 Re sum_x Tr[d_x tau^-1 (partial_trace_(others) G Delta)].

Indeed Sigma^-1 Delta is a sum of single-factor operators tau^-1 d_x, so
only those marginals enter the trace. This identity does not neglect
generated correlations. Intertwining determines the marginals from the
exact classical linearization above.

Put Rx=sum_a(e_a,2/2)rho_a and Ry=sum_a(b_a,3/8)rho_a. Then d_x=Rx X_x+Ry Y_x.
Exact rational inversion of tau yields

    u = Tr[Rx tau^-1 Rx]
      = 2417748739555754821116820340799639977750
        /1317642545956945503834165709296483091641,
    v = Tr[Ry tau^-1 Ry]
      = 3294027190941045443247182637892226930624
        /5479433287981426997353428830244670390875,
    Tr[Rx tau^-1 Ry] = 0.

Thus u=1.83490488142962236... and v=0.601162021292631682.... In particular
u-4v is strictly negative. Covariance also explains the transverse zero
cross term, but the runner checks it directly.

## Finite rational certificate

Take N=2048, and the periodic integer triangle

    T_x=N/2-2|x-N/2|,             0 <= x < N,
    X_x=T_x/(N/2),    Y_x=T_((x-N/4) mod N)/(N/2).

These are actual finite profiles, with zero mean and absolute value <=1.
For example |epsilon|<1/7 gives positive one-site classical probabilities
p0+epsilon f_x, so the tangent arises from admissible initial preparations.
There are N^2/2 even sites at each x. The quantum quadratic-form derivative
per matched pair is exactly

    (2/N) sum_x [u X_x dot X_x + v Y_x dot Y_x]
       = -(734147/2348810240) u + (5085081/4697620480) v
       = 253943551350785258709380168798915548993408646371
         /3288323073641053210935625659843220349235316654080000
       > 0.

This contradicts stationary CPTP contraction. It therefore excludes the
specified exact intertwining at N=2048 for this frozen code and these rates,
subject to independent verification of the argument and certificate. The
system size here is a finite analytical witness, not a many-body simulation:
K=4294967296 abstract factors. The tensor factorization above avoids ever
constructing its enormous joint density matrix.

The runner reports all six tested triangles: both orientations at
N=512,1024,2048. Only the positive orientation at N=2048 has positive
derivative. A prior floating Fourier screen guided this choice; this is not
a preregistered numerical discovery. The Fourier test is not a premise of
the exact certificate. Its signs for named orientations are convention
dependent, so only the explicit discrete profile is used in this proof.

## Design implications and unresolved alternatives

The positive preparation map survives. It cannot by itself carry this exact
routed dynamics through a CPTP evolution. Enlarging the block, changing the
preparation, changing the rate law, using a correlated preparation, or matching
only selected observables are different targets and remain possible. A
classical orthogonal label code has u=7, v=7/4 at the uniform law and passes
this particular test. That observation is only a necessary-condition check;
a constructive quantum implementation needs its own proof.

At long wavelength the transverse drift has matrix
-d I - i g [[0,1],[4,0]], with
d=k0[(1-cos(2k))+4(1-cos k)] and
g=gamma[sin(4k)-sin(2k)]/14. For a diagonal local metric, stationarity and
contraction for arbitrarily large N force u=4v: otherwise the order-k
metric expansion has a positive direction that exceeds the order-k^2
damping. This observation motivates metric-compatible encoding searches;
it does not assert sufficiency or a no-go for every faithful code.

The currently selected no-go-discipline packet has not yet passed N1-N8.
In particular no five-family exhaustion or independent audit is represented
by this single contraction calculation. Keep this as raw research evidence
until the publication gate and an independent check are handled honestly.

## Reproduction and provenance

Run `python3 quantum_metric_exact_check.py` in this directory. The JSON result
pins the four prior source files and this runner, reports every exact rational
value, all 336 code covariance checks, and every full-color residual. The
raw stdout and stderr are preserved. Future note or code corrections must
preserve the earlier evidence and rerun affected checks.
