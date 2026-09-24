# Finite-window original record counts with background events permitted

Root candidate, 2026-09-24. This is a conditional composition of the sealed
local-background candidate and the separately checked prepared readout,
magnetic-window and microscopic-register arguments. Independent review of
the local bound and of this new count argument is pending. No retained
status, physical parameter selection or observational agreement is claimed.

## 1. The different statistic

Keep the complete supplied common rotor generator on a finite cubic torus,
h=KD+delta H4 and L_kappa=-i[h,.]+kappa sum_m D[B_m]. All original channels
and matter states are retained. Take the resolved local marks j,l of the
prepared plaquette readout, j != l. Let I be a fixed interval of length h_I>0,
b>0, and T exceed sup(I)+b. Define C_jl(I,b) to count every ordered pair of
recorded events with labels j then l, first time s in I, and lag 0<u<=b.
All other events are unrestricted. A history can contribute more than once.

The exact count mean is

    m_n=kappa^2 int_I ds int_0^b du
       Tr[M_l T_kappa(u)(B_j T_kappa(s)(rho_n) B_j^*)],
    M_l=B_l^* B_l.                                             (1)

Here n=0,1 indexes prepared vacuum and one-particle initial fields. There
is no no-event propagator or global survival factor in (1). These are actual
counts in the original labeled process; no outward destination is measured,
no first-birth matter coherence is removed, and no new instrument is imposed.

Set tau_*=a/c, K=g^2/(2tau_*), delta=1/(4tau_*g^2), and keep graph, tau_*,
I,T and packet fixed. Write H_I^0=int_I |chi_p(s)|^2 ds. The proposed result,
for 0<b<=r0 tau_*g^2 with r0 fixed, is

    m_1-m_0=-2 kappa^2 b g^2 exp(-g^2 v_p/2) H_I^0
        +kappa^2 b O(g^4+b/tau_*+kappa T(1+delta T)^3).         (2)

Constants can depend on the fixed graph and preparation. The disturbance
part inherited from the local bound is uniform in total volume; the separate
prepared-wave and magnetic-multiplier constants are not promoted to that
status. No graph/time/coupling limit is silently combined.

## 2. A two-insertion extension of the local disturbance bound

Write U_t(O)=exp(iht) O exp(-iht) and S_t=T_kappa^*(t). The tested effect is

    A_kappa(s,u)=S_s[B_j^* S_u(M_l) B_j],
    A_0(s,u)=U_s[B_j^* U_u(M_l) B_j].

Their difference first splits into

    S_s[B_j^*(S_u-U_u)(M_l)B_j]
            +(S_s-U_s)[B_j^*U_u(M_l)B_j].                     (3)

Contractivity and the local-background bound control the first term by
C kappa u(1+delta u)^3. The second input is not strictly local when u>0,
so the single-local-observable estimate cannot simply be applied to it.
The following is the additional argument required here.

For v>=0, Hamiltonian evolution is an automorphism, so

    U_v[B_j^*U_u(M_l)B_j]
                =U_v(B_j^*) U_(v+u)(M_l) U_v(B_j).            (4)

For every original mark B_m, expand its commutator with the three-factor
product by the Leibniz rule. Each term is a commutator with one evolved
local operator, times two uniformly bounded factors. The Hamiltonian
Lieb-Robinson estimate in the local-background candidate's section 2,
applied to B_j, B_j^* and M_l, gives an exponential tail from the fixed
union of the two mark supports, with propagation time at most v+u.
The trivial commutator norm bounds apply inside that neighborhood.

The same cubic shell sum as that candidate therefore gives

    sum_m ||D_m^* U_v[B_j^* U_u(M_l)B_j]||
                              <= C (1+delta(v+u))^3.         (5)

This uses its commutator-locality proof, not just the numerical statement
of a single observable norm estimate. The support and norm constants depend
only on these two fixed marks and the finite-range interaction geometry.
Apply dissipative Duhamel to the second term of (3) and use (5). Combining
the two contributions yields

    ||A_kappa(s,u)-A_0(s,u)||
                   <= C kappa (s+u)(1+delta(s+u))^3.          (6)

Initially prove (3)-(6) in the local electric boxes. The same common KD,
strong bounded-term convergence, trace-class Dyson expansion and duality
used for the local-background bound pass this estimate to rotors at each
fixed graph. No norm continuity of all unbounded-electric conjugations is
assumed, and no high-energy moment is required for this norm estimate.

Equation (6) permits arbitrary states and all background events. Its
comparison Hamiltonian is the full matter-field h. The reduction to the
prepared initial field Hamiltonian happens only for the pre-insertion
initial sector, where the parent actually proves that reduction.

## 3. Prepared contrast through a positive lag

The Hamiltonian comparison in (6) gives, for each initial prepared vector,

    Tr[A_0(s,u)rho_n]=||B_l exp(-ihu) B_j phi_n,g(s)||^2.

The magnetic-window argument applies to this expression with the loss term
absent from the *comparison Hamiltonian*, not from the actual process (1).
For clarity its required analytic steps are as follows.

The attributed prebirth graph estimate is ||Q_E phi_n,g(s)||<=C g^-2 and
||grad phi_n,g(s)||<=C g^-1. On all link angles the bounded H4 and original
mark maps are smooth finite matter-matrix multipliers. For u/(tau_*g^2)
in a bounded interval, V(u)=exp(-i delta u H4) has uniformly bounded first
and second angle derivatives. The product rule gives

    ||D V(v) B_j phi_n,g(s)||<=C g^-2, 0<=v<=u.

The actual word-dependent D is retained, including unconfined directions.
Graph-continuity and the diagonal domain justify Hamiltonian Duhamel, giving
||[exp(-ihu)-V(u)]B_j phi_n,g(s)||<=C u/tau_*. This controls the two individual
electric remainders without acting on the unweighted approximation error.

Compress B_j^* V(u)^* M_l V(u) B_j to the initial matter word and Haar-average
the harmonic translation fiber seen by the initial preparation. The scalar
effect minus its u=0 effect has C^2 norm O(u/(tau_*g^2)). The centered
vacuum/one-particle reference states and their O(g^2) vector approximation
give an actual expectation contrast at most C g^2 times that C^2 norm.
This averages the initial test, not the postbirth states or their winding.
Hence the Hamiltonian contrast differs from its boundary by O(u/tau_*).

The resolved boundary effect is 23I+W_p+W_p^*. Its prepared expectation
contrast is -2g^2 exp(-g^2 v_p/2)|chi_p(s)|^2+O_T(g^4). Combining these
facts with (6), for s+u<=T, proves (2) by integration. No factor
exp(-30 kappa V s) is reintroduced.

The separate baseline estimate is

    m_0=kappa^2 b [25 h_I
            +O(g^2+b/(tau_*g^2)+kappa T(1+delta T)^3)].        (7)

It follows from the boundary vacuum value and the individual magnetic
supremum-norm error, which is only O(u/(tau_*g^2)). Subtracting two estimates
of the form (7) would not prove (2); the centered contrast is essential.

One sufficient supplied joint family is

    kappa_g tau_*=o(g^8),       b_g=o(tau_*g^2), b_g>0.        (8)

Then (m_1-m_0)/(kappa_g^2 b_g g^2)->-2 H_I^0. If H_I^0>0, the actual count
contrast is negative for sufficiently small g. The error estimate is also
valid at fixed positive kappa; it need not resolve the signal there. The
small-rate family (8) is an explicit extra choice, not a physical rate
selection, a necessary condition, or permission to discard actual events.

## 4. Count variance cannot be borrowed from a Bernoulli event

Let beta_j=||B_j||^2 and beta_l=||B_l||^2, and r_j=kappa beta_j,
r_l=kappa beta_l. In every normalized conditional state the two marked
intensities are at most r_j and r_l. Bounded-intensity jump construction
allows their events to be thinned from independent Poisson proposal clocks
of those rates. Other labels and the state-dependent acceptance remain in
the actual process. The construction is only a coupling for a bound.

Every actual j,l pair is a proposal pair in the same window. Thus
0<=C_jl<=C_prop pathwise. Put mu=r_j r_l h_I b. For the independent Poisson
proposals the shared-point expansion gives

    E C_prop^2=mu^2+mu+r_j r_l^2 h_I b^2
                       +r_j^2 r_l int L(t)^2 dt,
    L(t)=length{I intersect (t-b,t)}.

Indeed two counted pairs can share both points, just their first point,
just their second point, or neither. Independent Poisson factorial moment
measures give the four displayed terms. Since 0<=L(t)<=b and
int L(t)dt=h_I b,

    Var(C_jl)<=E C_jl^2<=mu^2+mu[1+(r_j+r_l)b].              (9)

No Poisson assumption is made about the actual counts, and no independence
between actual marks is asserted. The finite total event cap also remains
valid; the proposal clocks may contain additional rejected events.

For N independent preparations of each arm, define the signal-to-standard-
deviation ratio for the difference of sample means using their actual
variances. Under (8), mu->0 and (r_j+r_l)b->0. Equations (2) and (9) imply
the conservative sufficient estimate

    SNR^2 >= [2/(beta_j beta_l)+o(1)]
                  N kappa_g^2 b_g g^4 (H_I^0)^2/h_I.         (10)

If both variances vanish the signal is deterministic and the bound is
interpreted accordingly. The resolved norm bound beta_j,beta_l<=25 permits
the numerical coefficient 2/625. This is a lower bound on statistical
signal-to-noise, not an exact variance formula or an optimal design.

For example, choosing kappa_g tau_*=g^(8+alpha) and
b_g=tau_*g^(2+zeta), alpha,zeta>0, makes a sufficient fixed-SNR repetition
order g^(-22-2alpha-zeta). This costly bound reflects the deliberately
conservative dynamics and variance estimates. It is not a lower bound on
what any detector must cost. Independent resets, sources and trials remain
supplied experimental operations; no apparatus implementing them is derived.

## 5. Fixed-parameter microscopic count moments

At each fixed graph,g,kappa,I,b, both the microscopic and target processes
have at most M=floor(|B|/2) original births. The microscopic-register argument
already constructs the finite classical word of original labels and time
bins, retains all physical matter and later events, and proves convergence
of its entire finite distribution at each fixed partition. Its channel and
domain hypotheses, bare P initialization and ordered spin/rotor limit remain
dependencies. We now specify the additional count observable.

For a partition of mesh eta, inspect every ordered pair of j,l entries in
the stored word. Define C_eta^- as the number of pairs whose bin information
forces membership in the requested window; define C_eta^+ as the number
whose bins permit it. Use the actual word order when entries share a bin.
Then pathwise C_eta^-<=C_jl(I,b)<=C_eta^+, and all three are bounded by
Q=M(M-1)/2. The bounds hold for both microscopic and target histories.

An ambiguous pair has first time within eta of an endpoint of I, or its
lag within 2eta of b. The known order makes the zero-lag boundary harmless
once b>eta. An enclosing region in (s,u) has area at most

                     4eta(h_I+b+4eta).

The target ordered factorial density is at most r_j r_l, by (1), positivity,
trace preservation and the two local operator norms. Therefore

    E_target(C_eta^+-C_eta^-)
                    <=4 r_j r_l eta(h_I+b+4eta).             (11)

Finite time-domain boundaries only reduce the region. Exact endpoint or
simultaneous pairs have zero target measure under the same density bound.
For second moments, (C_eta^+)^2-(C_eta^-)^2<=2Q(C_eta^+-C_eta^-).

Freeze the partition first. Both bounding counts and their squares are
bounded effects on the finite classical register, so their microscopic
expectations converge by the registered parent. Then let eta decrease to
zero and use (11). This proves, at fixed positive parameters and windows,

    E_micro C -> E_target C,
    E_micro C^2 -> E_target C^2,
    Var_micro C -> Var_target C.                            (12)

This does not require a uniform microscopic jump intensity, which scales
as epsilon^-2. It does not assert convergence of exact-time densities or
total variation of all continuous histories.

For a chosen sequence (8), select spin after freezing each row. Mean errors
can be made o(kappa_g^2 b_g g^2), and second-moment errors
o(kappa_g^2 b_g), for both arms. Finitely many convergence requirements can
be met by one sufficiently large spin in that row; enlarge it to make
epsilon->0 under epsilon^2 S(S+1)=1/(2g^4). Equations (2), (9) and their
count-level statistical consequence then transfer along this selected
microscopic diagonal. There is no rate, economical spin bound or guarantee
for a preassigned simultaneous schedule.

## 6. Observation status

The claimed mathematical connection concerns finite windows of the original
record process with background events present. It gives a controlled mean,
a conservative count-variance bound and an ordered microscopic comparison.
The original first-two-event probability is a different statistic and its
global survival restriction and Bernoulli variance cannot be copied here.

The observation bridge remains conditional on supplied compensated dynamics,
packet preparations, unit/time/spatial labels and rate choices. The admitted
weak-field regime has sparse local formation and shrinking lag windows;
the repetition estimate is expensive and not optimized. Stable photon
propagation at physically selected parameters, practical sources/detectors,
large-volume packet errors and empirical agreement remain open. This is
not a fit to observed photon data, a new physical axiom or TOE completion.

## 7. Separate deterministic controls

The personal control checks twelve Poisson proposal-rate/window combinations,
including windows on both sides of h_I=b. Three-point Gaussian quadrature on
each polynomial segment independently evaluates int L(t)^2 dt and agrees
with min(h_I,b)^2 max(h_I,b)-min(h_I,b)^3/3 to floating-point precision. All
second-moment upper bounds hold. Examples with mean greater than one make
the inapplicable Bernoulli variance expression negative, while the actual
proposal-count variance is positive.

The register control checks 848 ordered histories at each of four nested
meshes. The fixed six-label pattern includes two unrelated events and can
contribute two j,l pairs. Every exact finite-history count lies between its
bin bounds, every square gap satisfies the claimed deterministic bound,
and every refinement tightens or preserves both bounds. The aggregate count
bracket gaps decrease from 856 to 445, 251 and 218. Exact window-endpoint
examples remain in the test set; this discrete inventory is not a target
probability measure or a numerical proof of the density area estimate.

The complete personal run exited zero with empty stderr in
0.16588704194873571 seconds. The root read the complete source, all twelve
proposal rows and all four register summaries. These checks concern the
counting and proposal formulas only. They do not simulate the original
cubic dynamics, prove locality or microscopic convergence, or provide
independent confirmation or observational evidence.
