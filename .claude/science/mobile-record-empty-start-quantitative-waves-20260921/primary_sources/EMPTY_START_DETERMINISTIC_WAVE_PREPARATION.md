# A deterministic observation time for the process started empty

2026-09-21. Root conditional composition argument; independent check pending.

This note composes the proposed all-stage polynomial filling estimate with
the separately checked formed-state preparation and moving-geometry wave
results. It introduces no new microscopic transition. The geometric process
is autonomous, its records are permanent, and the fourteen pair colors have
the specified birth law. Rates, classical content recognition, paired births
and a physical clock remain supplied premises.

## 1. The explicit deterministic schedule

On an even cubic torus N>=8, set K=N^3/2 and take fixed beta,kappa>0,
k0>|gamma| and bounded fixed plaquette rate nu>=0. Start with every site
vacant. Let F be its first full-matching time. The proposed all-stage
estimate, if accepted, gives

    E F <= A_N := 2 K^3/beta + 2^27 K^26/kappa.

Fix any 0<eta<1. Define

    H_N = 2 A_N/eta,
    s_N = [8N(3N-1)/k0] [(K/2)log14 + log(1/eta)],
    t_N = H_N+s_N.                                      (1)

Both times are deterministic. Markov's inequality gives

    P(F>H_N) <= eta/2.                                   (2)

The formed-state preparation theorem with epsilon=eta/2 gives a conditional
total-variation error at most eta/2 after s_N units of post-formation color
evolution, uniformly in the completed arrangement and geometry history.
If completion occurs before H_N, evolution has at least s_N units to mix
before t_N. Longer evolution preserves the same contraction bound.

The event E={F<=H_N} is determined by the autonomous geometry. Conditional
on its entire history, the final color counts still have the multinomial
law with K trials and the specified full-support probability vector p.
Transport and rotations permute these immutable colors; they do not change
their counts. The uniform distribution within each count sector, mixed
with those multinomial probabilities, is exactly p^K.

Consequently, conditional on any geometry history in E, the color law at
t_N is within eta/2 of p^K. This statement uses the previously proved
contraction for an arbitrary prescribed sequence of geometry intervals and
record permutations. It does not assume that the actual entrance geometry
or its later history is stationary or uniform among matchings.

## 2. Construct the reference law and couple its future

For histories in E, use the actual full geometry at t_N as the reference
geometry. For histories outside E, substitute any one fixed full matching.
Sample reference colors from p^K independently of this reference geometry.
This defines a probability law on full colored matchings. The actual law
at t_N and that reference law differ in total variation by at most

    P(E^c)+eta/2 <= eta.                                 (3)

Here total variation is sup_A |mu(A)-rho(A)|, so the maximal-coupling
mismatch probability is that same distance. On E the bound follows by
mixing the conditional estimates. The entire E^c mass costs at most its
probability, whether the lattice has completed during (H_N,t_N] or remains
partially filled. No conditioning on successful formation is applied to
the law being claimed for the actual process.

Couple the initial states at t_N maximally, then use the same transition
randomness whenever they agree. Since the reference is already full, its
future has only the same color exchanges and autonomous plaquette motion;
there are no possible further births or vacant-site slides. Its generator
therefore agrees exactly with the actual full-state generator. Agreement
persists for the whole future path. The total-variation bound eta thus
holds for every finite future time interval, including an interval of
microscopic duration NT with fixed macroscopic T.

This reference construction is for the proof. No extra reset, conditional
rejection, color resampling or matching replacement is performed by the
physical process. The law of the reference geometry may be highly biased.
That is allowed by the uniform-in-matching wave theorem.

## 3. Transfer the quantitative wave bound

For definiteness define the fourteen-component pair field even before
completion. At each black site b let xi_b be the basis vector for the
color of its pair when it is covered, and zero when it is vacant. Put

    Y_N(Q,u) = K^(-1/2) sum_b exp(-i Q.b/N) (xi_b(u)-p).

On full states this is precisely the field in the routed wave theorem.
On every partial or full state its Euclidean norm is at most 2sqrt(K),
since ||xi_b-p||<=2. For fixed Q and 0<=t<=T the matrix propagator
U_Q(t)=exp[-i A(Q)t] has a finite norm bounded independently of N. Therefore

    ||Y_N(Q,t_N+Nt)-U_Q(t)Y_N(Q,t_N)||^2 <= C_(Q,T,p) K

holds deterministically for both processes. On their coupled agreement
event the two errors coincide. Using (3), the actual mean squared error
is at most the reference mean squared error plus C_(Q,T,p) K eta.

The proposed quantitative Euler result, if accepted at its stated premises,
bounds the reference error by C N^(-1/6), uniformly in the reference
geometry law and for fixed bounded nu. Take eta=N^(-4) in (1). Then

    sup_(0<=t<=T) E ||Y_N(Q,t_N+Nt)-U_Q(t)Y_N(Q,t_N)||^2
        <= C N^(-1/6) + C' N^(-1).                      (4)

This is a supremum of expectations. No expectation of a path supremum is
claimed. A fixed finite collection of modes and times transfers in the
same way. Its propagated Gaussian limit follows from the reference result
and the vanishing path-law total-variation difference. The two-physical-
endpoint field has the same conclusion with the previously established
sqrt(2) normalization and its O(N^(-2)) squared endpoint-displacement error.

For orbit-isotropic p the same conditional vector equations apply:

    partial_t X = (gamma rho_A/3) curl Y,
    partial_t Y = -gamma rho_B curl X,
    c = |gamma| sqrt(rho_A rho_B/3).

The scalar speed and four propagating modes require that isotropy condition,
as well as nonzero gamma and Q. The general matrix result uses the stated
full-support p and does not impose that mode count. The static longitudinal
color modes retain positive equilibrium variance. They are not identified
with the matching's geometric Gauss constraint.

## 4. Scope of the improvement

At fixed positive beta,kappa,k0, (1) with eta=N^(-4) is a polynomial
deterministic schedule; the leading displayed worst-case bound scales as
O(N^82/kappa). This exponent is only the consequence of the loose supplied
upper bounds. It is not an observed scaling law or useful numerical estimate.
The microscopic law is unchanged with N; only the time at which it is
observed grows with N. Uniform final-matching selection is unnecessary for
this result and is not asserted for fixed birth rate.

The logical gain is a single conditional statement from empty initialization
to an unconditioned wave-observation window. It removes an assumed formed
initial state, not the supplied microscopic law, colors, clock, recognition
or preparation time. The all-stage filling and quantitative Euler inputs
remain explicit provisional dependencies until their separate checks finish.
There is no quantum preparation, derived Born rule, geometric photon,
Lorentz symmetry, gravity or physical TOE claim here.
