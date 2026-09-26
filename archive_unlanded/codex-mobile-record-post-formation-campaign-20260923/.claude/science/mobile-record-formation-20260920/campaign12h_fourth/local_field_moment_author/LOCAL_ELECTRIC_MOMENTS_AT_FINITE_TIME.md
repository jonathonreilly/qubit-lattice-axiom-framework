# Local electric moments at finite time

Root analytic candidate, September23,2026, before independent reconstruction
or new controls. Use the already checked compensated limiting rotor target
and its local volume dynamics. This is a bound on that supplied target,
not a microscopic approximation uniform in volume or a stationary energy
theorem. All statements distinguish local field tails from the error in
evolving a separately truncated Hamiltonian.

## 1. A local drift and quadratic-variation identity

Fix a link e of any finite induced bipartite graph of maximum degree z,
or of Z^d with z=2d. Let E=E_e be its signed integer field. The diagonal
electric Hamiltonian K D commutes strongly with E and E^2. Write the rest
of the Hamiltonian as V and the actual bounded jumps as L_mu, with their
own Lindblad loss. Define the bounded local operators

    C_mu=[E,L_mu],
    b_e=i[V,E]+(1/2)sum_mu(L_mu^* C_mu+C_mu^* L_mu),
    q_e=sum_mu C_mu^* C_mu.                           (1)

Only terms whose original supports contain e contribute. The generator
identities, initially on finite electric-support vectors, are

    L^*(E)=b_e,
    L^*(E^2)=E b_e+b_e E+q_e.                       (2)

The second follows by expanding each dissipator and the Hamiltonian
derivation. q_e is positive. No norm bound on K D, on E or on a total-volume
Hamiltonian appears in (1).

For completeness explicit conservative constants follow from the local
path form. Write the outward hopping operator F_a as the sum over its
neighbors, using the two orthogonal charge sectors in each term. Then
`||F_a||<=z`. A link has a unique A endpoint a_e; consequently
`||[E_e,F_a]||<=1` if a=a_e and is zero otherwise. For each retained pair
`S_ac=F_c F_a P`, at most one factor involves e. Thus

    ||[E,S_ac]||<=z,
    ||[E,-2 delta S_ac^*S_ac]||<=4 delta z^3.

There are at most z(z-1) retained pairs containing a_e, so their total
contribution is bounded by `4 delta z^4(z-1)`.

For a resolved birth on marked edge (a,b), `||L_mu||<=sqrt(kappa)(z-1)`.
Its E_e commutator is zero unless a=a_e. If the marked edge equals e, the
old hop cannot use that edge (birth requires its B endpoint empty), so
`[E_e,L_mu]=s_ab sigma L_mu`; its norm is at most sqrt(kappa)(z-1).
For the other z-1 marked edges at a_e, only the old hop can use e, and
the commutator norm is at most sqrt(kappa). Summing both signs gives

    ||b_e|| <= C =4 delta z^4(z-1)+4 kappa(z-1)^2,
    0<=q_e<=Q I,    Q=2 kappa z(z-1).                (3)

The two coherent newborn signs have orthogonal final A-charge ranges, as
do their E commutators. Their combined norms are bounded by sqrt(2) times
the one-sign bound. Using one coherent channel therefore gives exactly
the same conservative bounds (3). There is no coherent sum over different
marked edges. Constants are intentionally coarse; they are not signal
speeds, optimized heating rates or physical parameter measurements.

## 2. Moment bound without a global energy-domain assumption

Suppose the initial density has `m_e(0)=Tr(rho E_e^2)<infinity`, without
requiring moments on other links. Equations (1)-(2), Cauchy--Schwarz and
positivity imply the scalar upper inequality

    m_e'(t) <= 2 C sqrt(m_e(t))+Q.                    (4)

With `beta=C+Q/2`, a useful comparison is

    m_e(t) <= [sqrt(1+m_e(0))+beta t]^2-1 =: M_e(t). (5)

Indeed divide (4) by 2sqrt(1+m_e), which bounds the derivative of that
square root by C+Q/2. The bound is uniform in graph size, the electric
coupling K, boundary position and all unobserved initial field moments.
It does not claim uniformity for arbitrarily large added boundary terms;
the interaction bounds must remain those specified above.

Here is a domain-safe route to (5). At each fixed finite graph compress
every rotor to |E|<=R, using the compressed Hamiltonian and compressed
jumps with their own loss. On that finite Hilbert space, (2)-(5) hold
literally. The projections commute with E. Thus the commutators of the
compressed operators are the corresponding compressed commutators, and
the local estimates (3) are unchanged. Conditional initial compressions
have the observed second moment at most m_e(0) divided by their acceptance
probability, which tends to1. They require no moment on the other links.

For fixed graph remove R first. The diagonal free unitaries converge
strongly on a common rotor space, uniformly on compact times, since they
agree eventually on each finite-support vector. Bounded Hamiltonian
remainders and jumps converge strongly with their adjoints. The bounded
interaction-picture trace-class integral equation then gives strong
trace-class convergence of the finite-graph evolutions, uniformly on
compact times. This is not norm convergence of the unbounded generators.

For any fixed bounded spectral clipping min(E_e^2,M), pass the expectation
to that limit and then let M increase. Local normality and monotone
convergence yield (5). This argument proves the inequality even when the
original density is outside the full Hamiltonian generator domain. It
does not assert that (4) is an everywhere-defined derivative for every
such density; the cutoff comparison is the rigorous conclusion needed.

## 3. Infinite-volume local states and finite field windows

Take any locally normal initial state of the infinite target with finite
m_e(0) on the chosen link. Its restrictions supply finite induced-volume
initial densities with the same observed moment. Apply (5) uniformly in
volume. For each fixed clipping min(E_e^2,M), the checked local operator-
norm volume limit passes the expectation. Letting M increase gives (5)
for the locally normal evolved infinite state. Translation invariance and
initial spatial factorization are unnecessary. If m_e(0) has a common
bound over links, the same bound holds uniformly over links at finite time.

In particular, for R>0,

    omega_t(1_(|E_e|>R)) <= M_e(t)/R^2.              (6)

For a fixed finite region X with link set J, let P_R restrict every link
in J to |E|<=R. The commuting spectral projections give

    1-omega_t(P_R) <= sum_(e in J) M_e(t)/R^2.        (7)

If p=1-omega_t(P_R)<1, the normalized compressed local density differs
from the exact local density in trace norm by at most2sqrt(p). To prove
this, purify the local density and compare the original unit vector with
its normalized projected vector; their overlap is sqrt(1-p). Trace-norm
contraction under partial trace gives the stated bound. This is a finite-
time local tail and state-approximation guarantee. It does not bound the
difference between exact dynamics and dynamics run with a hard wall at R;
boundary feedback in that different evolution requires a separate estimate.

The quadratic growth in (5) does not give energy tightness uniformly for
all time. It therefore does not by itself make stationary cluster states
locally normal, restore norm time continuity on all bounded observables,
prove pointwise infinite-volume birth-rate decay or supply a global density
in a preferred infinite tensor-product representation.

## 4. Initial field diagnostic

For the all-A-plus, B-empty zero-field initial state, Hamiltonian evolution
has zero instantaneous E_e and E_e^2 expectation derivative. Choose the
orientation of e from its A endpoint to its B endpoint. Marked birth on
e shifts its field by either sign equally; old-record transfers on e
contribute a negative unit shift. Exact path counting predicts

    (d/dt)<E_e>|_0 = -2 kappa(z-1),
    (d/dt)<E_e^2>|_0 = 4 kappa(z-1).                 (8)

Reverse the first sign if the stored orientation is reversed. Each birth
changes two distinct link fields by one unit, consistent with the already
checked record-density growth. The two stipulated instrument conventions
give the same initial diagonal readouts, not identical output states.
These are proposed exact local controls, not finite-time moment solutions.

The decisive checks are the full commutator/carre-du-champ identity,
coherent-channel norm bookkeeping, legitimate cutoff removal and the
orientation-sensitive local diagnostic. Physical source selection,
microscopic-volume uniformity and long-time energy bounds remain open.
