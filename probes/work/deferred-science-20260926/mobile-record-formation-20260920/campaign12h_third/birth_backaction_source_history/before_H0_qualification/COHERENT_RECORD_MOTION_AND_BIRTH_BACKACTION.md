# Coherent record motion and birth backaction in supplied occupation models

Date: 2026-09-22. Status: author derivations and exact finite checks;
independent checking pending. This is private campaign research, not retained
science or a completed no-go packet.

## Question and premises

Can a site form another permanent record after its earlier record moves away
when movement is coherent quantum dynamics? A completely positive model can
implement that behavior, but its formation clock is affected by the movement.
This note isolates the interaction before claiming a large-scale field theory.

Every model below supplies its Hamiltonian, formation instrument, clock, and
vacancy/occupation distinction. These are not consequences of the repository's
minimal axioms. A local space C|0> direct-sum K represents vacancy and occupied
record content. The separately constructed six-qubit pointer code can carry
such a space with dim K = 14 at the block level. It has not been compiled into
one native M2 site per independently readable record. A one-color occupation
model has local dimension two but supplies its distinguished basis.

Hopping preserves existing record content and number. Birth increases number.
The paired model in section 4 does not impose the previous classical model's
requirement that permanent partners remain nearest neighbors after moving.
Consequently the results below cannot be imported into that model unchanged.

## 1. An exact two-block renewal clock

Let A = |a,0>, B = |0,a>, and F = |b,a>. A record initially occupies the
source, can move to its neighbor, and then permits a new record at the source.
Set, with kappa,beta > 0,

    H = kappa (|A><B| + |B><A|),
    J = sqrt(beta) |F><B|.

F is absorbing in this three-state model. The original record a is neither
destroyed nor overwritten. Different birth colors can be separate orthogonal
absorbing states F_b; only the sum beta of their rates enters the waiting time.

Before the first birth the unnormalized amplitude evolves under

    A_nojump = [[0, -i kappa], [-i kappa, -beta/2]].

All its eigenvalues have negative real part: an imaginary-axis eigenvector
would have zero B amplitude, and hopping would then force its A amplitude to
vanish. Thus the survival integral exists. The exact solution of
A_nojump^dagger X + X A_nojump = -I is

    X = [[2/beta + beta/(4 kappa^2), -i/(2 kappa)],
         [i/(2 kappa),             2/beta]].

X is the time integral of exp(A_nojump^dagger t) exp(A_nojump t). Starting in A,

    E[tau_birth] = 2/beta + beta/(4 kappa^2).

The optimum is beta = 2 sqrt(2) kappa, at mean sqrt(2)/kappa. Increasing the
birth rate without bound therefore slows renewal: the prospective birth
continuously distinguishes whether the source has emptied, inhibiting coherent
transfer. This is a finite-model instance of quantum-Zeno backaction, not a
claim to have discovered that mechanism.

A classical reversible A <-> B hop with rate k and B -> F birth with rate beta
instead gives 1/k + 2/beta by two first-step equations. Quantum kappa and
classical k have different interpretations; this comparison does not fix a
physical calibration between them.

`quantum_birth_backaction_check.py` verifies the symbolic Lyapunov equation and
optimum. It separately evolves the full three-state Lindblad equation at four
birth rates and five times, verifies trace and positivity to 1e-12, and compares
its birth probability to the no-jump solution. These numerical points are
controls; the all-positive-parameter formula follows from the exact equation.

## 2. One vacancy: a precise dark-subspace criterion

Take a finite graph's one-vacancy Hilbert space, any Hermitian hopping H, and
single-vacancy birth sources with loss matrix

    Gamma = sum_{s in sources} beta_s |s><s|,  beta_s > 0.

After a birth the vacancy is gone. Before birth, A = -iH - Gamma/2. Define D as
the largest H-invariant subspace contained in ker Gamma. Equivalently, D is
the span of H eigenvectors whose amplitudes vanish at every source.

For Av = lambda v, taking the real part of <v|Av> gives
Re lambda ||v||^2 = -<v|Gamma|v>/2. An imaginary-axis eigenvector therefore
lies in ker Gamma and is an H eigenvector. Conversely each such eigenvector
survives indefinitely. H is Hermitian, so D and its orthogonal complement
reduce H; positivity of Gamma and Gamma D = 0 make them reduce Gamma too.
All eigenvalues of A restricted to D-perp have strictly negative real part.
The finite-dimensional exponential on D-perp decays even if A has Jordan
blocks. Hence, for initial vacancy density rho,

    Pr(eventual birth) = 1 - Tr(P_D rho).

Writing P_S for the coordinate restriction to source sites, full completion
for every initial state is equivalent to full column rank of

    O = [P_S; P_S H; ...; P_S H^(V-1)].

Cayley-Hamilton makes ker O H-invariant; it is exactly D. No stochastic
independence or population-only closure is used.

Exact controls: a four-cycle with one source at vertex 0 has dark vector
(0,1,0,-1), so a vacancy initially at vertex 1 has eventual birth probability
1/2. On the eight-vertex cube with one corner source, O has rank 4 and the
maximally mixed vacancy state has eventual birth probability 1/2. These are
finite supplied models; neither number is a thermodynamic prediction.

## 3. Contact pair formation with two vacancies

Now put a one-color record/vacancy space at each vertex. On a graph G use

    H = kappa sum_{<x,y>} (sigma_x^+ sigma_y^- + sigma_x^- sigma_y^+),
    J_{xy} = sqrt(beta) sigma_x^+ sigma_y^+,

where sigma^+ changes vacancy to occupied record. Pair births act only on
adjacent vacancies. H preserves the vacancy number; every J reduces it by two.
Vacancy parity is therefore conserved. The fully occupied configuration is
absorbing. This model allows records to move off their birth sites without
requiring their original partners to move with them.

For the periodic 4 by 4 by 4 cubic graph, use unordered two-vacancy basis
|{x,y}>. Define the real unnormalized amplitude

    psi({x,y}) = sin(pi (y_1-x_1)/2) sin(pi (y_2-x_2)/2).

It is invariant under x <-> y and periodic with period four. It vanishes for
coincident or nearest-neighbor vacancies. To compute H psi, first extend psi
to coincident pairs by zero. Each coordinate hop of either vacancy shifts the
relative displacement. In axes 1 and 2 the two opposite shifts sum to zero;
in axis 3 they sum to twice the original amplitude for each moving vacancy.
Thus H psi = 4 kappa psi. Removing the forbidden coincident transitions makes
no change because their extended amplitudes are zero. Every birth jump and
every birth loss operator annihilates psi. This is an exact permanent
two-vacancy dark state for any beta > 0.

The integer runner enumerates all 2016 unordered pairs, checks H psi = 4 psi
at kappa = 1 without floating-point arithmetic, and checks zero amplitude on
all 192 adjacent pairs. Its squared norm is 512. The localized vacancy pair
{(0,0,0),(1,1,1)} has amplitude one, hence overlap squared 1/512 with this
normalized dark state. From that initial configuration, the probability of
never completing is at least 1/512; additional dark vectors may increase it.

## 4. Reachability from the completely vacant torus

An existing dark state alone does not establish trapping from the intended
initial condition. Here the empty-start reachability can also be established,
although the argument gives no useful macroscopic lower bound on its weight.

Start with x-oriented dimers (0,y,z)-(1,y,z) and (2,y,z)-(3,y,z). Along the path

    000 - 100 - 110 - 010 - 011 - 111

remove its three matching edges and insert the two intervening edges. The
result is a 31-edge nearest-neighbor matching covering exactly the 62 vertices
other than 000 and 111. The runner verifies every edge and all vertex counts.

Choose any ordering of these 31 distinct birth channels. The unnormalized
quantum-trajectory amplitude for those jumps and no intervening jumps is a
product of birth operators and finite-dimensional no-jump exponentials. At
zero intervening waiting times its limiting value is a nonzero scalar times
the localized vacancy pair just described. Its projection onto normalized
psi is therefore nonzero. Matrix exponentials depend continuously on every
waiting time, so an open region of sufficiently small strictly positive
waiting times retains a nonzero projected norm. That region has positive
trajectory probability density and positive measure. After the last jump,
the projected component cannot be removed by H or by any birth channel.
Integrating these trajectories gives strictly positive failure probability
from the completely vacant torus for finite kappa,beta > 0.

This continuity argument is analytic. No full 2^64 density matrix was evolved,
and the small path probability has not been estimated. It does not establish
a finite-density vacancy phase or an appreciable trapping fraction at large N.

A useful countercontrol is the four-cycle: its two-vacancy dark vector is
(|{0,2}> - |{1,3}>)/sqrt(2), but a first pair birth from the fully vacant cycle
leaves adjacent vacancies with zero dark overlap. Its subsequent no-jump
evolution cannot create that overlap. The only dark direction in the
two-vacancy sector is this opposite-pair difference, so that empty-start
four-cycle still completes for finite positive kappa and beta. Initial-state
reachability must be checked, not inferred from dark-space dimension.

## 5. What is and is not established

These models demonstrate genuine quantum compatibility of movement and renewed
birth, a formation-induced transport slowdown, and a separate possibility of
interference trapping. The companion `OCCUPATION_MONITORING_AND_PAIR_BIRTH_COMPLETION.md`
gives a constructive sufficient condition for removing the trapping on every
finite connected graph, with explicitly added local occupation monitoring.

No statement here excludes all coherent formation rules, all nonorthogonal
record encodings, or all native implementations. The negative examples have
not passed the repository's N1-N8 publication gate. No Lorentz symmetry,
quantum field phase, gravity, continuum limit, or theory of everything follows
from these calculations.

Known noise-assisted transport and dark-state mechanisms provide context:
Plenio and Huelga, arXiv:0807.4902v1; Rebentrost et al., arXiv:0807.0929v2;
and Thiel et al., arXiv:1906.08112. Only their abstracts were consulted during
this derivation; no theorem from them is used in the proofs above. The last
paper treats repeated detection, whereas the present models use continuous
Lindblad dynamics. Exact formulas and scope in this note are independently
checkable from the stated finite models.

