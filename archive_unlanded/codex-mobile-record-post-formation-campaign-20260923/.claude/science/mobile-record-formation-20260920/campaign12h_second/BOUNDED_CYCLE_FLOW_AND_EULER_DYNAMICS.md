# Bounded configuration cycles and the missing Gibbs-to-wave connection

2026-09-21. Second personal campaign. Author derivation; independent
reconstruction is pending. This is a quantitative statement about a specified
stationary classical Markov class. It supplies no axiom, physical dynamics,
universal exclusion theorem, or assertion that all record models are diffusive.

## 1. The question being tested

The first campaign constructed local permutations of immutable records that
preserve a supplied correlated Gibbs law. Their mean homogeneous transport
current vanishes. Could an unexamined collective effect nevertheless produce
the transverse Euler fluctuations found for the different context-exchange
generator? A vanishing mean current alone would not settle that question.

Here a stationary semigroup estimate addresses it without a hydrodynamic
closure. The relevant extra premise is a uniformly bounded length of cycles
in the **configuration graph**, not merely bounded range of each spatial
move. The product-invariant context exchanges are not asserted to have this
property. Ordinary directed motion on a ring illustrates the distinction.

## 2. Finite chain and a bounded cycle representation

Let a finite continuous-time Markov chain have rates r(eta,zeta), invariant
probability pi, and generator L acting on functions. Restrict to its support,
so pi is positive. Reducibility is allowed. Write the stationary edge flow

    Q(eta,zeta) = pi(eta) r(eta,zeta), eta != zeta.

Assume it has a positive directed-cycle decomposition

    Q = sum_C w_C 1_C,  w_C >= 0,  2 <= length(C) <= M.       (1)

Multiplicity may be counted for repeated edges; alternatively split into
simple cycles. Crucially M is uniform across the sequence of system sizes.
Every finite stationary flow admits some cycle decomposition; uniform M is
the additional, restrictive condition here.

Use the complex pi inner product and Dirichlet form

    D(f) = -Re <f,Lf>_pi
         = (1/2) sum_(eta,zeta) Q(eta,zeta)|f(zeta)-f(eta)|^2.

For one directed m-cycle, the form is w times the cycle difference operator.
On the nonconstant discrete Fourier modes its dissipative part has eigenvalues
1-cos(theta), theta=2pi j/m; the full difference eigenvalues are
exp(i theta)-1. Consequently the norm of the dissipative form's normalized
full operator is

    max_(j != 0) |exp(i theta)-1|/(1-cos(theta))
       = csc(pi/m).

Constants contribute zero. Applying this cycle inequality and then
Cauchy--Schwarz to the nonnegative weights in (1) gives the uniform strong
sector bound

    |<f,Lg>_pi| <= C_M sqrt[D(f)D(g)], C_M=csc(pi/M).        (2)

The antisymmetric part similarly has normalized norm at most cot(pi/M).
In particular, every generator eigenvalue lambda satisfies

    |Im lambda| <= cot(pi/M) [-Re lambda].                  (3)

For a zero dissipative eigenvalue the same inequality forces lambda=0.
This is a property of the finite Markov generator, not a proposed energy
operator. It precludes increasingly underdamped nonzero generator eigenmodes
within a family with fixed M; it does not classify general nonnormal
transients or projected-memory equations.

## 3. A stationary finite-time estimate, without a closure assumption

Let P_t=exp(tL), let f have zero pi mean, and put S=||f||_pi^2. Stationarity
and the Markov contraction imply

    integral_0^t D(P_s f) ds = [S-||P_t f||_pi^2]/2 <= S/2.

Apply (2) in

    <f,(I-P_t)f> = -integral_0^t <f,L P_s f> ds

and use Cauchy--Schwarz in time. For a stationary realization eta_t,

    E|f(eta_t)-f(eta_0)|^2
      = 2 Re <f,(I-P_t)f>
      <= C_M sqrt[2 t D(f) S].                            (4)

The left side is nonnegative; an absolute value on the intermediate scalar
integral justifies the upper bound even for complex f. When S=0 the result
is trivial. No differentiation of a limiting covariance and no interchange
of a thermodynamic and long-time limit is used.

## 4. Application to local immutable-record observables

Consider a cubic torus with V=N^3 sites, a fixed finite alphabet, and bounded
content observable a(eta_x). Each conservative event is supported in at most
s sites within Euclidean distance R of an event center, and preserves the
sum of a on that support. Suppose |a|<=A and the total exit rate of every
configuration is at most Lambda V, uniformly in N. Set

    F_N(k) = V^(-1/2) sum_x exp(-i k.x) a(eta_x),
    f_N(k) = F_N(k)-E_pi F_N(k), k=K/N,

where K is a fixed reciprocal-torus vector. The support has an unwrapped
embedding for sufficiently large N; periodic phases agree on that embedding.
For every allowed move, its zero total content increment gives

    |Delta F_N(k)|
      <= V^(-1/2) sum_x |exp[-i k.(x-c)]-1| |Delta a_x|
      <= 2 A s R |k| / sqrt(V).

Thus

    D(f_N(k)) <= 2 Lambda A^2 s^2 R^2 |k|^2 = B |k|^2.     (5)

If (1) holds with uniform M and the stationary structure factor
S_N(k)=Var_pi F_N(k) is uniformly bounded above, then for every fixed T,

    sup_(0<=t<=T) E|F_N(K/N,Nt)-F_N(K/N,0)|^2
      <= C_M sqrt[2 T B |K|^2 sup_N S_N(K/N) / N] -> 0.    (6)

The supremum is outside expectation. The same argument works for any
microscopic times t_N=o(N^2). It asserts frozen normalized modes on those
times, **not** existence of a nontrivial diffusive limit at time N^2.
For a vector of finitely many bounded content observables, sum the component
estimates. Any subsequential finite-mode stationary fluctuation limit is
constant in time on the Euler scale. A nontrivial Maxwell oscillation at
that normalization is therefore excluded in this stated class.

More generally, for S_N>0, (4) divided by S_N bounds the relative mean-square
change by C_M sqrt[2 t_N D(f_N)/S_N]. If S_N vanishes with N, that version
must be evaluated rather than silently using (6) at another normalization.
For example S_N proportional to |k| does not give the same vanishing bound
at Euler time after normalizing by sqrt(S_N). The spectral-sector statement
(3) remains valid, but a physical quantum-vacuum claim does not follow.

## 5. What this says about the existing Gibbs construction

In `../campaign12h/LOCAL_GIBBS_RECORD_CIRCULATIONS.md`, each plaquette
rotation has a stationary directed flow constant on its permutation orbit.
Those orbits have length at most four. Reverse rotations are reverse cycles,
and added Metropolis swaps are two-cycles. Hence M=4 and C_M=sqrt(2), for
any supplied bounded finite-range H and any closed count sector with positive
canonical probabilities. The rate bound and local content conservation hold.

If a chosen sequence of those stationary Gibbs laws has bounded structure
factors at the probed modes, (6) applies. A flat transverse classical
structure factor, if established, would satisfy that size requirement. Local
irreversibility by itself does not give the Euler waves missing from this
construction. The law need not be a product and no mixing estimate is used.

A local coupling of an E-loop reversal and a disjoint B-loop reversal into
a four-state directed cycle also has M=4. It preserves both microscopic
Gauss constraints and every record label, and can preserve nonuniform weights
by dividing a common orbit flow by those weights. It still belongs to the
class above. This is an explicit test of a tempting construction, rather
than an assertion that every E/B coupling has that form.

Births are not covered by this stationary conservative theorem. The earlier
vacancy budget shows why a positive-rate birth process is not stationary
with vacancies in finite volume. Its transient formation state, subsequent
nonstationary evolution, and mesoscopic initial layers require separate work.

## 6. Routes left open and a decisive countercontrol

For a single particle moving clockwise on an N-cycle at rate one, each move
has range one and the stationary position is uniform. The configuration
cycle has length N. Its Fourier observable f(x)=exp(2pi i x/N) satisfies

    Lf = [exp(2pi i/N)-1] f.

At time Nt its correlation tends to exp(2pi i t), with vanishing damping.
There is no size-independent cycle bound. This is a concrete counterexample
to replacing (1) by spatial locality alone.

The research decision is to examine mechanisms outside the bounded-cycle
class: stationary flows with long configuration cycles; a nonstationary
formation/preparation regime with a controlled wave window; additional
nonconserved microscopic variables; or a genuinely quantum amplitude
dynamics with its record bridge supplied separately. These are different
open routes, not reasons to infer a universal impossibility. The already
checked product-invariant wave process is another reason not to broaden
the present conclusion to all immutable-record motion.

## 7. Prior art and verification boundary

Bounded cycle representations and their sector estimates are established
Markov-chain machinery. Relevant primary sources are Pierre Mathieu,
[Carne--Varopoulos bounds for centered random walks](https://projecteuclid.org/journals/annals-of-probability/volume-34/issue-3/CarneVaropoulos-bounds-for-centered-random-walks/10.1214/009117906000000052.pdf),
and Deuschel--Koesters,
[The quenched invariance principle for random walks in random environments admitting a bounded cycle representation](https://www.numdam.org/item/AIHPB_2008__44_3_574_0/),
especially the latter's sector-condition Lemma 3.2. The finite-chain
inequalities and constants used here are derived above; their application
to the proposed record/Gibbs construction is the campaign's diagnostic.
No novelty is claimed for the general sector-condition method.

`bounded_cycle_flow_check.py` is the author's finite and numerical control.
It checks cycle constants, a nonuniform invariant law with overlapping
cycles, semigroup inequalities, immutable Gauss-loop histories, and the
long-cycle ballistic countercontrol. Finite checks do not replace the
uniform proof. Independent reconstruction and any required publication
negative-claim packet remain pending.
