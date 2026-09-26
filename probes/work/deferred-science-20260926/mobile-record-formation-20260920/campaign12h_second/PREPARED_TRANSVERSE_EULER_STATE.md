# A prepared transverse state for the immutable-record Euler wave process

2026-09-21, root conditional derivation. The local process is the previously
checked fifteen-label context exchange; only its initial distribution changes.
This is a smooth-weight refinement of the first campaign's bounded-event
conditioning in ../campaign12h/MAXWELL_GAUSS_SECTOR_PREPARATION.md, not a new
solution of its preparation/propagation bridge. The additions are an explicit
finite-lambda Gaussian covariance and entropy, local-marginal estimates, and
a microscopic nonstationarity control. It does not derive preparation from local record
formation, impose microscopic Gauss, remove the other conserved fields,
implement qubit measurements, or identify a physical electromagnetic vacuum.

## Fixed microscopic input and normalization

Use the process in ../campaign12h/IMMUTABLE_TRANSVERSE_MAXWELL_CONSTRUCTION.md
(SHA256 1403c91ef041838347bc72c9a30a63d4db73619dcca7fd7775158cfaa2586d32),
with its independent transverse-exchange reconstruction. Its base proof is
../campaign12h/CONTEXT_EXCHANGE_FLUCTUATION_DERIVATION.md
(SHA256 0c0b3713caa0769a2a711c7a75480f6db59f01bea5088982fb97b1acf7edc85e).
These finite-mode inputs were checked in the first campaign; their frozen
notes retain their original historical status prose. No formal audit status
is imported or assigned here.

The local classical alphabet is vacancy, six A axis tags and eight B cube
tags. The fixed site observables are e=+/-e_i on A and zero otherwise, and
b=(+/-1,+/-1,+/-1) on B and zero otherwise. Whole-record nearest-neighbor
swaps have the bounded four-site context rates from that construction, with
a fixed positive floor. The product law nu_N has probabilities rho_A/6 on
each A label, rho_B/8 on each B label, and 1-rho_A-rho_B on vacancy, where
rho_A,rho_B>0 and rho_A+rho_B<1. Rates conserve all fourteen label counts.
There are no births in this result.

For V=N^3 and K in 2pi Z^3 define

    u_N(K)=V^(-1/2) sum_x exp(-iK.x/N) e(eta_x)/sqrt(rho_A/3),
    v_N(K)=V^(-1/2) sum_x exp(-iK.x/N) b(eta_x)/sqrt(rho_B),
    U_N(K)=(u_N(K),v_N(K)).

Both one-site means vanish. For finitely many fixed nonzero modes containing
one representative of each +/- pair, the product CLT gives independent
proper complex six-component Gaussians with covariance I_6. This applies
once N is large enough to avoid aliases and self-conjugate lattice modes.
The negative modes are complex conjugates, not additional independent modes.

Let C_K w=K cross w and let c=gamma sqrt(rho_A rho_B/3), retaining its sign.
The checked microscopic conclusion on Euler time is

    sup_(0<=t<=T) E_nu ||R_N(K,t)||^2 -> 0,
    R_N(K,t)=U_N(K,t)-exp(G_K t) U_N(K,0),
    G_K=i c [[0,C_K],[-C_K,0]].                             (1)

The supremum is outside expectation. This is a fixed-mode, finite-time
statement with no quantitative uniform rate or path-space convergence.
G_K is anti-Hermitian. Its longitudinal subspace is static; its four
transverse eigenvalues are +/-i |c||K| with multiplicity two each when c!=0.

## Explicit initial reweighting

Fix a finite set M of m nonzero modes as above and lambda>=0. Let
P_L(K)=KK^T/|K|^2 and P_T=I-P_L. Define

    Q_N=sum_(K in M) [||P_L u_N(K)||^2+||P_L v_N(K)||^2],
    g_N=exp(-lambda Q_N),  Z_N=E_nu g_N,
    d mu_N / d nu_N = g_N / Z_N.                           (2)

This is a measure on the same record configurations, with the same alphabet,
contents and generator. It has positive full support at each finite N.
It is translation-invariant. If M is closed under proper cubic rotations
up to the +/- representative convention, with a common lambda, it is also
proper-cubic-invariant. A general M would intentionally prepare selected
spatial directions; that symmetry must not be assumed for an arbitrary set.
The weight depends on global Fourier sums. It is not a finite-range birth
law, a local conditional specification, or an implemented preparation protocol.

Since each selected longitudinal complex Gaussian has variance one,

    Z_N -> Z_lambda=(1+lambda)^(-2m)>0.                    (3)

For fixed lambda and M the full microscopic **path** measure started at mu_N
has initial Radon--Nikodym weight g_N(eta_0)/Z_N relative to the same kernel
started at nu_N. It follows immediately from 0<g_N<=1 that

    sup_(t<=T) E_mu ||R_N(K,t)||^2
        <= Z_N^(-1) sup_(t<=T) E_nu ||R_N(K,t)||^2 ->0.     (4)

This transfers (1) without claiming microscopic stationarity of mu_N or
repeating the dynamical replacement proof under an unjustified new measure.
The constant is allowed to depend on fixed lambda and m. It cannot be treated
as uniform when either grows with N.

Weighted initial CLT, followed by (4), therefore gives the finite-mode,
finite-time limiting process

    U(K,t)=exp(G_K t) U_lambda(K,0),
    Cov U_lambda(K,0)=diag(Sigma_lambda,Sigma_lambda),
    Sigma_lambda=P_T+(1+lambda)^(-1)P_L.                    (5)

Different selected modes remain independent up to conjugacy. Product fourth
moments are uniformly bounded and the density in (2) is uniformly bounded
for fixed parameters; this also justifies convergence of the displayed
second moments, not only weak convergence. The limiting covariance commutes
with G_K, so this **limiting** Gaussian wave process is stationary. For example,

    E[u(K,t)u(K,s)^*]
       =(1+lambda)^(-1)P_L+cos(|c||K|(t-s))P_T.             (6)

The u/v cross covariance is i sin(c|K|(t-s)) C_K/|K|, with continuous zero
value at c=0. Its transverse form is unaffected by the longitudinal tilt.
One may first take N->infinity at fixed lambda,M and then lambda->infinity.
That ordered limit has covariance diag(P_T,P_T) and purely transverse
Maxwell-shaped propagation in the selected sector. This is not a claimed
joint large-N/large-lambda estimate or a growing-mode theorem.

## Microscopic stationarity and locality do not follow

The prepared microscopic law is generally not invariant. The positive swap
floor makes each fixed-content-count sector irreducible, with uniform
stationary law on its site arrangements. At K=(2pi,0,0), two identical +e_x
A records a distance one versus two apart have different |u_L(K)|^2 for
N>=4, so a nonzero lambda weight is not constant on that sector. For the
first-axis-shell choice of M the other axis modes
do not remove this difference. Thus the prepared conditional measure is
not that sector's invariant law. The stationarity in (5) is a limiting
statement on a fixed Euler observation window, not an exact finite-chain fact.

There is also no microscopic charge elimination. For any fixed finite set
of sites, its mu_N marginal tends to its nu product marginal. One direct
proof removes those sites from the finite vector of Fourier sums, making
the remaining sums independent of the local variables. Removal changes the
Fourier vector by O(V^-1/2). For fixed lambda the function exp(-lambda Q)
is globally Lipschitz, and Z_N stays bounded away from zero. The resulting
weighted expectations differ from the independent product expectations by
O(V^-1/2), with a constant depending on the selected local set and parameters.

At initial time, for the old centered-divergence readout

    D e(x)=(1/2)sum_j[e_j(x+e_j)-e_j(x-e_j)],

this gives

    E_mu |D e(x)|^2 -> rho_A/2,
    E_mu |D b(x)|^2 -> 3 rho_B/2,                           (7)

both positive. Six distinct neighboring sites contribute the stated product
variances. The microscopic means vanish by the global A/B sign symmetries.
A fixed-site Gauss constraint is therefore not obtained, even though selected
macroscopic longitudinal modes can be suppressed in the ordered limit.

The preparation has a finite relative entropy at fixed parameters:

    H(mu_N | nu_N) ->
       2m [log(1+lambda)-lambda/(1+lambda)].                 (8)

Indeed H=-log Z_N-lambda E_mu Q_N; weighted CLT gives
E_mu Q_N ->2m/(1+lambda), with the lambda=0 case immediate.
The entropy per site tends to zero. This small entropy cost does not make
the global Fourier preparation a local physical mechanism or select it
among many possible reweightings of macroscopic observables.

## What this closes, and what it leaves

Within one supplied local immutable-record generator, the earlier bounded
conditioning argument already connected a prepared state with a transverse
Euler wave sector. The smooth preparation here quantifies how finite-mode
suppression coexists with unchanged local limiting statistics and positive
microscopic charge fluctuations. The conclusion remains conditional on the
checked stationary propagator input and on the nonlocal measure (2).

The other eight conserved fluctuation fields have not disappeared. They
are Gaussian-independent of the two vectors at the isotropic product
linearization and remain spectator zero-current fields in this construction.
The preparation neither gives them a relaxation mechanism nor justifies
ignoring them in a physical theory. Nor does it choose the special cross
product rate tensor, establish a quantum vacuum/commutator/Born bridge,
supply finite-amplitude nonlinear Maxwell dynamics, or produce the required
state by nearest-neighbor formation from empty space. Those remain the
load-bearing TOE questions.
