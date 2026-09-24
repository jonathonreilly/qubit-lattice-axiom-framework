# PRE: microscopic electric-family robustness on the three-leaf star

Independent conditional reconstruction, 2026-09-24. This packet is sealed
before reading the withheld microscopic author calculation. It uses the
supplied local microscopic law and common initial state, with a new complete
physical-sector matrix construction. No campaign model builder is imported.
It is not an autonomous-source construction, a universal no-go, an audit,
or a retained-status claim.

## Source and hypothesis contract

`SOURCE_BINDINGS.json` binds the seven permitted scientific notes and their
full snapshots. The five operator/parent/compensation notes retain the hashes
used in the earlier independent work. The new electric-family note is
`LOCAL_ELECTRIC_COMPLETIONS_AND_POSTBIRTH_FIELD_PHASE.md`, SHA256
`a9db2a928a0cf16cb2e9dfbaafe36d3f775a42053d4f3074032b8d191e87a617`, read with
`ROOT_SCOPE_CORRECTION.md`, SHA256
`fd098fa5b571ea5af03766ecc2eef74f5bdefe2dd9df3e1f01ab046517c398fa`.
The current-main workflow at `5efa36e7c357ae2a62ee586a5407f90982f6ded9`
matches the previously read governing instructions. The checkout HEAD was
observed as `555b59209b773566ef8e172968fc224ee638aaaa`; scientific premises
are bound by their actual file hashes amid concurrent coordinator work.

The supplied graph has A={0}, B={1,2,3}, and oriented edges 0->b. Charges
are hard-core 0,+1,-1, links use normalized integer-spin shifts with S>=1,
and the physical equation is div E=q-1_A. Fix delta,K,kappa>0,
0<=lambda<=1, and epsilon>0 with

    C=S(S+1), epsilon^2 C=delta/K.

Write ell=lambda K and d=1+3epsilon^2. Let F be unsigned outward transport
from site 0 and let g have its sole plus record at 0 and every field zero.
The specified common input is

    psi_epsilon=(g+epsilon Fg)/sqrt(d).                 (1)

The state is supplied, not selected by a preparation theorem. It is not
assumed to be an eigenstate for lambda>0. The corrected common-density theorem
has P-supported initialization; (1) is not P-supported. All results here are
instead derived directly from the complete microscopic matrices, including
its nonzero W=1 component.

The physical jump channels remain exactly the original resolved j_(b,+),
j_(b,-), or the coherent j_(b,+)+j_(b,-), with Lindblad multiplier
sqrt(kappa)/epsilon. No energy filter, scalar replacement of H, number-energy
offset, changed jump normalization, or extra environmental law is inserted.

## Complete physical sector and microscopic Hamiltonian

The leaf Gauss equations fix

    E_(0,b)=-q_b.

The center equation then says total charge is one. Every charge word in
{0,+,-}^4 with total charge one is physical and has fields in {-1,0,1};
there are exactly sixteen such words, at every integer spin S>=1:

| sector | center occupied, W=0 | center empty, W=1 | total |
|---|---:|---:|---:|
| N=1 | 1 | 3 | 4 |
| N=3 | 9 | 3 | 12 |

There are no further physical number sectors. In particular full occupation
of all four sites is incompatible with total charge one; the electric-note
scope correction's parity condition is respected. A three-record state has
no legal further birth: either the center is occupied, or all leaves are.
It still has nontrivial number-preserving Hamiltonian motion.

Every actual legal hop or birth shifts its affected field between 0 and +1
or between 0 and -1. Therefore its exact normalized spin squared weight is

    1-E(E+k)/C=1.                                     (2)

The complete physical matrices are independent of S except through the
supplied coupling scale. This is a fixed-field example; no high-flux input
or moving spin-boundary approximation is involved.

For an active outward hop, its vacant leaf has q_b=E_b=0. Hence on this
entire sixteen-dimensional physical space,

    D_ext=0, E2=N_B=N-1+W.

The one-A occupancy gate is the empty product I. The spin and rotor diagonal
parts of F*F coincide, so the original compensation is exactly C_S=F*F.
Also T=-(F+F*). The actual supplied electric-family Hamiltonian reduces to

    H=Omega[W-epsilon(F+F*)+epsilon^2 F*F]+ell E2,
    Omega=delta epsilon^-4.                           (3)

This follows from delta epsilon^-2 lambda E2/C=lambda K E2. Thus the electric
family adds a bounded ell N_B term here, with 0<=E2<=3.

Let M=F*F and B=W-epsilon F. Since W is a projection and F maps W=0 into W=1,

    B*B=W-epsilon(F+F*)+epsilon^2 M,
    H=Omega B*B+ell E2 >=0.                            (4)

The matrix control constructs T independently from both local hop directions
and verifies (3)-(4), rather than assuming this factorization at input.

## Initial energy and the eigenstate issue

The three terms of Fg are orthogonal, so ||Fg||^2=3. Direct application gives

    B psi_epsilon=0,
    H psi_epsilon=ell epsilon Fg/sqrt(d).              (5)

Consequently

    E_initial=3ell epsilon^2/d,
    <H^2>_initial=3ell^2 epsilon^2/d,
    Var(H)_initial=3ell^2 epsilon^2/d^2.               (6)

At lambda=0 the common input is an exact zero-energy eigenstate of this
microscopic Hamiltonian. At lambda>0, H psi is not proportional to psi:
its g coefficient is zero while its Fg coefficient is nonzero. Its mean is
small but not zero, and its loss contribution below must not be discarded.
For every lambda in [0,1], the initial mean tends to zero in the joint limit.

## Actual marked first outputs and energy moments

Fix a birth edge (0,b). Only the two terms of Fg on leaves i!=b can undergo
that birth. Define

    v_(b,c)=j_(b,c) Fg,
    phi_(b,c)=v_(b,c)/sqrt(2), c=+1 or -1.

The exact microscopic output is

    L_(b,c) psi_epsilon=sqrt(kappa/d) v_(b,c).

Thus every resolved mark has initial intensity 2kappa/d. A coherent edge mark
has vector v_(b,+)+v_(b,-), squared norm four and intensity 4kappa/d. These
are actual outputs of the supplied jump, without intervening projections.
The total first intensity is 12kappa/d for either instrument.

On N=3, let w_b denote the W=1 state whose negative record is at leaf b.
The three vectors F*w_b have disjoint supports, each of squared norm three.
It follows that

    FF*=3I on the N=3 W=1 subspace,
    M^2=3M on the N=3 P subspace.                     (7)

For the plus-at-center resolved mark, both old destinations give the same
w_b after F acts, so Fv_(b,+)=2w_b. For the minus-at-center mark they give
the two other w_i, one each. The two images for opposite birth signs are
orthogonal. The normalized M moments are therefore

| mark | <M> | Var(M) |
|---|---:|---:|
| resolved c=+1 at center | 2 | 2 |
| resolved c=-1 at center | 1 | 2 |
| coherent edge | 3/2 | 9/4 |

Put a=delta epsilon^-2 and b_hop=delta epsilon^-3. Any one of these output
vectors phi lies in N=3, W=0 and has E2=2. Its full microscopic H image is

    H phi=(a M+2ell)phi-b_hop Fphi,

where the two displayed parts have orthogonal W sectors. Hence

    <H>_phi=a<M>+2ell,
    Var(H)_phi=a^2 Var(M)+b_hop^2<M>.                  (8)

Explicitly:

| mark | exact energy mean | exact energy variance |
|---|---|---|
| resolved + | 2delta/epsilon^2+2ell | 2delta^2/epsilon^6+2delta^2/epsilon^4 |
| resolved - | delta/epsilon^2+2ell | delta^2/epsilon^6+2delta^2/epsilon^4 |
| coherent edge | 3delta/(2epsilon^2)+2ell | 3delta^2/(2epsilon^6)+9delta^2/(4epsilon^4) |

Every variance is independent of lambda, exactly, not only at leading order.
The output lies initially in W=0, but H does not preserve that subspace; the
W=1 part of Hphi is essential to its second moment. Replacing H by its bare
P compression would miss the leading epsilon^-6 term. These are system-energy
moments in the output state, not statistics of energy transferred under an
unperformed two-energy-measurement protocol.

## Full initial energy derivative, including loss

On the N=1 W=1 subspace there is one old plus at a leaf and two vacant birth
leaves. Summing the two signs yields four unit loss contributions. Both
instruments therefore have

    Gamma=sum_j L_j*L_j=4kappa epsilon^-2 W

on N=1. Gamma is not scalar on psi_epsilon. The recycling energy gain is

    sum_j <L_j psi,H L_j psi>
       =kappa(18delta epsilon^-2+24ell)/d.

Using the full Hpsi from (5), the anticommutator loss is

    Re <Gamma psi,Hpsi>=12kappa ell/d.                 (9)

The Hamiltonian makes no contribution to its own energy derivative. Thus

    d<H>/dt at t=0
       =kappa(18delta epsilon^-2+12ell)/d.             (10)

This is positive for the stipulated positive delta,kappa, including lambda=0.
It diverges as 18kappa delta epsilon^-2. Extending the lambda=0 zero-energy
eigenstate property to lambda>0 would incorrectly omit (9); using total
rate times initial energy as the loss would also be incorrect.

## Exact finite-time number-sector energy relation

Let u=Fg/sqrt(3). Before the only possible formation the unnormalized state
has the form

    chi(t)=alpha(t)g+beta(t)u.

The Hamiltonian and loss preserve this two-dimensional subspace. In the
ordered basis (g,u), its no-event evolution is

    i d chi/dt = H_nh chi,
    H_nh = [[3Omega epsilon^2, -sqrt(3)Omega epsilon],
            [-sqrt(3)Omega epsilon,
                         Omega+ell-i 2kappa epsilon^-2]],
    (alpha(0),beta(0))=(1,sqrt(3)epsilon)/sqrt(d).       (11)

Write p_1(t)=||chi(t)||^2 and p_3(t)=1-p_1(t). The full density is block
diagonal in N, and its three-record block receives the birth recycling and
then evolves unitarily under H_3; there are no more births in that block.
At any birth time, the relative marked output vectors are the same as above,
because each j annihilates g and acts only on the single symmetric u amplitude.
The all-mark mean injection energy is therefore the constant

    c_epsilon=3delta/(2epsilon^2)+2ell.                (12)

Both instruments have this same value, despite their different marked states.
Unitary propagation inside N=3 preserves its H energy. Starting with p_3(0)=0,

    tr(Q_3 H rho(t))=c_epsilon p_3(t), all t>=0,
    <H>_t=E_1(t)+c_epsilon p_3(t),
    E_1(t)=<chi(t),H_1 chi(t)> >=0.                   (13)

This is an exact microscopic finite-time relation, at each finite S,epsilon.
It does not infer an energy moment from a density-approximation theorem.

The complete matrix control checks the injection operator identity on the
actual invariant span{g,u}, not just its initial expectation. It also checks
that this span is invariant and that every j annihilates N=3. Therefore the
identity integrates for all times. Its scope matters: dephasing the three
one-leaf components changes the all-mark injected mean to
delta/epsilon^2+2ell, so (12) is not claimed for arbitrary N=1 initialization.

For completeness the same argument and full-matrix identity give

    tr(Q_3 H^2 rho(t)) = p_3(t)[
         3delta^2/(2epsilon^6)+9delta^2/(2epsilon^4)
                       +6delta ell/epsilon^2+4ell^2]. (14)

Thus whenever p_3(t)>0, the conditional N=3 energy variance is
`3delta^2/(2epsilon^6)+9delta^2/(4epsilon^4)` for either instrument.
This number-sector moment statement does not identify their conditional
quantum densities or individual resolved marks.

## Controlled fixed-positive-time singular scaling

Here is a direct uniform estimate from (11). It avoids applying a P-initialized
effective theorem to the partly W=1 initial state. Put

    gamma=2kappa epsilon^-2, q=ell-i gamma,
    z(t)=beta(t)-sqrt(3)epsilon alpha(t),
    w=Omega d+q.

The exact equations and initial condition are

    i alpha'=-sqrt(3)Omega epsilon z,
    i z'=w z+sqrt(3)epsilon q alpha,
    z(0)=0.                                          (15)

No-event contractivity implies |alpha(t)|<=1. Duhamel followed by one
integration by parts in its scalar fast exponential yields, for any T,

    sup_(0<=t<=T)|z(t)| <= 2A_epsilon
                              +B_epsilon sup_(0<=t<=T)|z(t)|,
    A_epsilon=sqrt(3)epsilon |q|/|w|,
    B_epsilon=A_epsilon sqrt(3)Omega epsilon/gamma.    (16)

Indeed the integration-by-parts boundary terms are bounded by two, and the
remaining convolution of |alpha'| is bounded by its supremum divided by gamma.
Since ell belongs to [0,K], |w|>=Omega d, giving uniformly in lambda

    A_epsilon=O(epsilon^3), B_epsilon=O(epsilon^2).

For sufficiently small epsilon, B_epsilon<1, so (16) proves
`sup_t |z(t)|=O(epsilon^3)`, with constants independent of T. Also
beta=sqrt(3)epsilon alpha+O(epsilon^3)=O(epsilon). The positivity factorization
(4) now gives the actual no-event energy bound

    E_1(t)=Omega|z(t)|^2+ell|beta(t)|^2=O(epsilon^2).   (17)

This bound is stronger than trace-norm convergence and directly controls
the potentially large microscopic observable on the no-event part.

Survival obeys the exact relation

    p_1'=-4kappa epsilon^-2 |beta|^2.

Using p_1=d|alpha|^2+O(epsilon^4) and
|beta|^2=3epsilon^2|alpha|^2+O(epsilon^4), one gets

    p_1'=-(12kappa/d)p_1+O(epsilon^2), p_1(0)=1,
    p_1(t)=exp(-12kappa t)+O_T(epsilon^2)              (18)

on every fixed finite interval, uniformly in lambda in [0,1]. Equations
(13), (17) and (18) establish

    <H>_t=(3delta/(2epsilon^2))(1-exp(-12kappa t))+O_T(1),
    epsilon^2 <H>_t -> (3delta/2)(1-exp(-12kappa t)),
    <H>_t/[S(S+1)] -> (3K/2)(1-exp(-12kappa t)).        (19)

For every fixed positive t the last coefficient is strictly positive. The
initial mean from (6) tends to zero. The limits and error bounds are uniform
throughout the stipulated electric family; choosing lambda as a resource-
dependent value in [0,1] does not remove the leading divergence.

The underlying physical Hilbert space here remains sixteen-dimensional and
all fields remain in {-1,0,1}. The singular energy comes from the microscopic
couplings and the post-event state, not from a high-field input escaping a
spin box. Consequently an O(1) electric correction ell E2 cannot remove the
order-S(S+1) mean energy requirement or the leading marked variance.
A qualitative limiting density by itself would not have supplied (19).

## Necessary supply inequality under explicit environmental assumptions

No environment is included in the given Lindblad law. To state a necessary
resource condition, separately suppose a realization has this precise system
Hamiltonian H, an environment Hamiltonian H_env>=0, finite initial energy
expectations, and conservation of the additive system-plus-environment energy
in expectation. This can be formulated as an energy-preserving joint unitary;
it is an additional condition, not a demonstrated realization of these jumps.
Any work store must be counted in the environment. Under those assumptions,

    <H_env>_0 >= <H>_t-<H>_0
       >= [3delta/(2epsilon^2)+2ell] p_3(t)
                                    -3ell epsilon^2/d. (20)

The second inequality uses the exact nonnegative no-event energy in (13).
At a fixed positive time its right-hand side grows as
`(3K/2)S(S+1)(1-exp(-12kappa t))` up to lower-order terms.
This is the necessary energy-supply scaling for the stated input and law.
The electric family does not remove it.

If the conserved total Hamiltonian instead contains interaction V, the
appropriate inequality keeps its energy explicitly:

    <H_env>_0 +<V>_0-<V>_t >= <H>_t-<H>_0.            (21)

For example a uniform bound ||V||<=v allows the weaker necessary inequality
`<H_env>_0+2v >= <H>_t-<H>_0`. A resource-dependent interaction energy could
itself supply the large energy and must be counted. A driven or energy-
nonconserving model does not satisfy the hypotheses of (20) merely by being
a Lindblad model. Nothing here constructs a suitable autonomous environment,
excludes environments with growing energy resources, identifies heat, or
establishes a universal no-go.

## Controls, failures and recovery

`star_local_matrix_control.py` independently enumerates all physical words,
infers the tree fields, builds every actual local hop and birth, and records
all transitions with exact spin weights. It produces complete sparse operator
entries and symbolic checks in `EXACT_STAR_MATRIX_RESULTS.json`. The initial
state, its nonzero lambda-dependent residual, all marked moments, gain and
loss terms, and the full invariant-subspace source identities are computed
from those matrices. This is an independently written control, with no
import of a campaign builder or a withheld expected formula.

`star_finite_time_control.py` uses those own matrices to exponentiate the
full 256-dimensional Lindblad generator at six small-spin/instrument cases.
The largest observed number-sector energy residual was approximately
7.3e-13. Its stable exact two-by-two no-event propagator agrees with those
full evolutions. Moving-spin tables for S up to 512, three lambda values and
two positive times corroborate (17)-(19). Those floating tables are not the
proof of the singular limit; (15)-(19) supply it analytically. Complete data
and logs are retained, including the symbolic construction rerun during the
finite-time control's own-module import.

Sensitivity checks reject dephasing the supplied coherent initial leaf
amplitudes, treating the lambda>0 input as an exact eigenstate, and dropping
the W=1 contribution to marked energy variance. No failed execution or
mathematical assertion occurred while producing this PRE. Deliberate wrong
comparisons are identified as sensitivity checks, not suppressed failures.

No withheld microscopic author/checker directory, CHECKPOINT or external
personal calculation was read. No earlier high-flux artifact was changed.
The source snapshots, full control outputs, code and execution receipt are
bound by `PRE_SEAL.json` and its SHA256 file. The remaining action is a
source comparison with the coordinator's frozen author packet after this
seal. No independent audit status or landing authority is conferred.
