# Independent reconstruction before author-runner/results access

2026-09-21. The three supplied source notes were read completely. The author
runner and result constants remain unopened. This is a check of a specified
stationary Markov class, not new campaign theory or an audit decision.

## 1. Cycle form and exact constants

Let the complex inner product conjugate its first argument. On an oriented
m-cycle let T shift forward and G=T-I. In the ordinary uniform coordinate
inner product, the positive dissipative form is S=I-(T+T*)/2. Constants are
annihilated by both operators. Fourier mode j has eigenvalues

    G: exp(2pi i j/m)-1,     S: 1-cos(2pi j/m).

Hence on the nonconstant space

    ||S^(-1/2) G S^(-1/2)|| = csc(pi/m),
    ||S^(-1/2) (G-G*) S^(-1/2)/2|| = cot(pi/m).

These statements are for complex functions, and the constants are sharp.
Multiplying a cycle flow by w multiplies its form and dissipative form by
w; no invariant-probability uniformity on the ambient states is required.
If a directed walk repeats vertices, pull a state function back to the list
of visits and apply the same inequality. Alternatively split it into simple
cycles. These operations do not increase the maximum allowed length.

For Q=sum_C w_C 1_C, the ambient form is the sum of the pulled-back cycle
forms, and D(f)=sum_C w_C D_C(f). Taking absolute values and using weighted
Cauchy--Schwarz proves

    |<f,Lg>_pi| <= csc(pi/M) sqrt(D(f)D(g)).

Applying the same reasoning to the skew-adjoint part proves its cot(pi/M)
constant. For an eigenfunction Lf=lambda f this gives

    |Im lambda| <= cot(pi/M) (-Re lambda).

This includes zero dissipation. On positive support, D(f)=0 forces f to be
constant along every edge carrying positive stationary flow and thus Lf=0.
For a finite stationary chain the positive-probability support is closed;
zero-probability transient states must be removed. Reducibility thereafter
causes no problem and requires no spectral gap. Constants on different
closed components can differ and remain nonzero after global centering.

The independent finite check uses exact rational Loewner certificates:
C^2 S-B* S^(-1)B >=0 and (C^2-1)S-R* S^(-1)R >=0 after removing one
constant coordinate per component, where B=-diag(pi)L and R=(B-B*)/2.
All principal minors are checked. Pure cycles of lengths 2,3,4,6 saturate
the relevant constants. A separate seven-state rational example combines
2-,3-,4-cycles and has two closed components and a nonuniform pi.

## 2. Stationary semigroup inequality

For P_t=exp(tL), stationarity and the finite-dimensional derivative imply

    d ||P_t f||_pi^2/dt = -2 D(P_t f),
    integral_0^t D(P_s f) ds = (||f||^2-||P_t f||^2)/2.

Put S=||f||^2 and z=<f,(I-P_t)f>. The cycle-sector inequality and time
Cauchy--Schwarz yield |z| <= C_M sqrt(t D(f) S/2). For an actual stationary
trajectory, including complex f,

    E|f(eta_t)-f(eta_0)|^2 = 2 Re z
                          <= C_M sqrt(2t D(f) S).

Global centering makes S the stationary variance. It is not necessary to
center separately in each communicating class. The energy integral need
not approach S/2; a frozen class-dependent component survives. The result
uses neither normality nor decay to a unique equilibrium. The independent
semigroup check compares direct joint-transition expectations, complex
correlations, and numerical energy integrals on the reducible example.

## 3. Local conservative scaling

For k=K/N with K in 2pi Z^3, the phase is well defined under periodic
unwrapping. For each event subtract its center phase and use sum Delta a=0.
The support assumptions give

    |Delta F_N| <= (2 A s R |k|)/sqrt(V),
    D(F_N) <= (Lambda V/2) (2 A s R |k|/sqrt(V))^2
            = 2 Lambda A^2 s^2 R^2 |k|^2.

All constants and the configuration-cycle cap must be uniform in N. The
stationary structure factor must be bounded above at the selected modes.
Then microscopic time Nt with t<=T gives a mean-square bound O(N^(-1/2)).
The same argument permits t_N=o(N^2). K=0 is exactly conserved. Finitely
many fields and modes follow by summing estimates; this does not cover a
growing set of modes, establish tightness, or assert a diffusive limit.
The supremum is outside expectation. Any existing finite-dimensional
stationary subsequential fluctuation limit is time-constant at this
normalization; no pathwise maximal estimate was proved.

For S_N>0 the relative bound is C_M sqrt(2t_N D_N/S_N), which must be
reassessed if one renormalizes a mode with vanishing structure factor.
The note correctly declines to infer a quantum-vacuum statement from this.

## 4. Direct scope countercontrols

Spatially local motion does not imply bounded configuration-cycle length.
For one clockwise particle on a ring, lambda_N=exp(2pi i/N)-1 and
E[conj(f_0) f_(Nt)]=exp(Nt lambda_N) -> exp(2pi i t). The only directed
simple cycle has length N; its skew-sector constant cot(pi/N) diverges.
Using M=4 would violate the finite-time bound even at finite N.

Small structure factors genuinely change relative conclusions. Partition
an even torus into disjoint nearest-neighbor dimers along axis one, with
one occupied site per dimer and independent rate-one swaps. The stationary
orientation product is reversible, its configuration flow is a sum of
two-cycles, and each event conserves occupancy. For k=(2pi/N,0,0),

    S_N = (1/8)|1-exp(-ik1)|^2 = (1/2)sin^2(pi/N),
    L f_N = -2 f_N,     D_N=2 S_N,
    E|f_N(t)-f_N(0)|^2/S_N = 2(1-exp(-2t)).

The absolute fluctuations freeze trivially as S_N tends to zero, but
variance-normalized fluctuations do not. This dimer example does not claim
all cubic symmetries; none is a hypothesis of the finite-chain estimate.
A separately assembled four-state two-dimer generator checks the formula.

Stationarity cannot be discarded. For rate-one symmetric exchanges on a
cubic torus, occupation has the exact Fourier eigenidentity
L F_N=-4sin^2(pi/N)F_N. Start from the full-support inhomogeneous product
p_x=1/2+delta cos(2pi x1/N), 0<delta<1/2. Then

    E F_N(0)=delta N^(3/2)/2,
    E[F_N(NT)-F_N(0)]
      =(exp[-4NT sin^2(pi/N)]-1) delta N^(3/2)/2
      ~ -2 delta pi^2 T sqrt(N).

Thus its uncentered mean-square change is at least order N, although the
reference homogeneous stationary law has S_N=1/4 and M=2. Reusing that
stationary bound for this initial law would be false. Some nonstationary
laws could be handled with additional uniform density or energy control;
none is supplied by the theorem. Likewise no conclusion about a supremum
inside expectation follows merely from the displayed pointwise bound.

## 5. Application reconstruction

For a fixed plaquette R^4=id. With fixed exterior and local orbit-invariant
a_±, the Gibbs factors cancel exactly: pi(eta) r_±(eta) is constant on
that R orbit. Removing self transitions leaves cycles of lengths 2 or 4;
reverse rotations supply reverse cycles. A Metropolis channel contributes
a two-cycle of weight kappa min(pi(eta),pi(eta^xy)). Adding channels or
conditioning on a closed count sector preserves this decomposition. It is
a decomposition of full configuration-state flow, not of spatial bonds.

The finite-range interaction and fixed finite alphabet bound H_S uniformly;
there are O(V) event centers and each local multiplier is uniformly bounded.
Consequently the exit-rate and bounded-support hypotheses hold. Neither
canonical irreducibility nor a mixing estimate is needed. Bounded stationary
structure factors remain an explicit additional premise, not a proved
property of every Gibbs law. The independent 16-state plaquette construction
uses rational nonuniform Gibbs weights and checks every period-1/2/4 orbit
and every Metropolis channel against its exact cycle-flow decomposition.

For the separate thirteen-label loop example, reversing disjoint A and B
loops in order A,B,A,B gives a four-state configuration cycle. Every step
is a whole-record permutation, preserves both exact divergence fields and
capacity, and returns record identities after four steps. A common positive
orbit flow divided by orbit probabilities preserves arbitrary positive
weights on these four states. For a local Gibbs specification the exterior
factor cancels, or rates min_orbit(pi)/pi give bounded local rates. The
independent side-seven construction verifies all four states, eight immutable
identities and both zero divergences with nonuniform stationary weights.
This does not prove that the original full loop-translation generator has
new Gibbs invariance, or that every possible coupling is in this class.

Births, nonstationary formation laws, unbounded configuration cycles and
limits using another fluctuation normalization remain outside the stated
application. No material defect has been found before author comparison.
