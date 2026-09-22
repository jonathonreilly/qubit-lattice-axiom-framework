# Independent reconstruction: hard-core records, ring exchange and live density

This report is sealed before access to any new author hard-core, live-density,
homogeneous-star or ramp argument, runner, result or seal. The neutral model is
recorded in `INPUT_SPEC.md`. No author computation is imported. The earlier
RK-adaptation correction acknowledgment is a separate completed task, not a
premise for the calculations here.

The supplied models admit a complete fourth-order ice-space Hamiltonian and a
finite-time bound on mean record/defect density uniform in volume. These are
different conclusions. A fixed-volume ring-dynamics limit can also be justified;
the density estimate alone does not establish that limit uniformly in volume.
At the controlled scale with a fixed positive birth rate, births remain enabled
at every finite parameter value, but their produced density tends to zero over
a fixed observation interval.

## 1. Definitions and necessary scope

Let V be the number of vertices of a periodic cubic d-dimensional lattice,
d>=1, with every side even and at least six. Its bipartition is A,B, each with
V/2 vertices. Positive-axis links are distinct, and each unoriented neighboring
pair has exactly one link. These conditions exclude two-link parallel cycles,
triangles, and length-four winding cycles. A geometrical plaquette is counted
once for each origin and unordered pair of positive axes.

The matter qutrit has states 0,+,-, charge q=0,+1,-1 and occupancy n=q^2.
Different sites have bosonic tensor-product operators; double occupation is
forbidden. E_e=+-1/2 and U_e=|+><-| have unit nonzero matrix element. The physical
constraint is

    div(E)_x + 1_A(x) - q_x = 0.                              (1)

The positive penalty Delta is assumed throughout the confinement/scaling
claims. The real hopping coefficient is denoted t; physical elapsed time is
tau, avoiding use of t for both. Put X_e=S_e+S_e^dag, where S_e moves an occupied
qutrit from A to B on that edge and makes the required unit gauge shift. The
Hamiltonians are

    H_s = Delta N_B - t sum_e X_e,
    H_f = (Delta/2) sum_x(div E_x)^2 - t sum_e X_e.            (2)

The second potential is homogeneous as an operator on links. The selected
background in (1) and the initial matter preparation still distinguish A and B.
Initially all A sites contain plus, all B sites are empty, and the field density
is arbitrary on the ice space div E=0. It can be mixed, coherent, and correlated.

For an oriented link from x to y, a q-record hop lowers E by q while moving q
from x to y. A birth V_e,q raises E by q and puts q,-q at x,y. Each update
therefore preserves (1), including at the operator level; a forbidden spin-half
shift has zero amplitude. The total signed charge is V/2.

For the two resolved jumps sqrt(beta)V_e,+ and sqrt(beta)V_e,-, or for one
coherent jump sqrt(beta)(V_e,+ +/- V_e,-),

    sum_mu J_e,mu^dag J_e,mu = beta P_e,
    P_e=(1-n_x)(1-n_y).                                     (3)

The two charge branches have orthogonal sources and ranges. There is one
allowed charge orientation for each vacant-edge electric basis state. If
**both** coherent signs are separate jumps with the displayed sqrt(beta)
coefficient, the total loss is 2 beta P_e; replace beta by that total rate in
the bounds below. A sum over both signs with no rate adjustment is not the
same clock normalization as the resolved instrument.

Equal loss does not imply equal CP maps or general histories. The independent
24-state physical-sector control below exhibits a nonzero coherent-versus-
resolved output difference. All density estimates below hold for either
specified instrument, without imposing equality of their densities as states.

## 2. Exact charge/count and potential identities

Let h_A be the number of vacant A sites, m_A and m_B the numbers of minus records
on A and B, and m=m_A+m_B. Summing (1) gives the operator identities, on the
fixed physical sector,

    N_B = h_A+2m,
    N_record = V/2+2m.                                      (4)

Hopping preserves each sign count. Every birth increases N_record by two and
m by one, and increases N_B by one. In particular, the only initially occupied
content being plus is essential to the low-space interpretation, while (4)
continues to hold after any number of births.

On this sector the homogeneous field penalty is exactly

    D_f := (1/2)sum_x(div E_x)^2
         = N_B+m_A-m_B
         = h_A+3m_A+m_B,
    N_B/2 <= D_f <= 3N_B/2.                                 (5)

With no births, m=0 for the stipulated initial preparation. Thus H_s and H_f
are **identical on the entire coherently accessible no-birth sector**, not just
to fourth order. This observation does not identify the two open dynamics after
births.

A birth on an A-B edge changes the potential energy by

| Born charge at A | Change of Delta N_B | Change of Delta D_f |
|---|---:|---:|
| plus | Delta | 0 |
| minus | Delta | 2 Delta |

This follows by changing the two divergences from (-1,0) to (0,-1) or (-2,1).
It also checks the sign of the supplied birth shift. The complete local star
and rectangle sectors realize both field-energy changes, so this distinction
cannot be removed by considering only a one-dimensional ring where the second
branch happens to be absent.

## 3. Fourth-order Hamiltonian, including folded normalization

This section concerns the coherent Hamiltonian on the initially accessible
fixed-number, no-minus sector. It is not a fourth-order expansion of the full
Lindblad generator at fixed Delta. Births leave that number sector; P J P=0.

Let P project onto all-plus A, vacant B and ice fields, let Q=I-P within the
fixed-number sector, and write A_hop=sum_e X_e so that H=H0-t A_hop. Let
R=Q H0^{-1} Q. The effective Hamiltonian on the orthonormally identified low
space through fourth order is

    H_eff^(2) = -t^2 B,
    B=P A_hop R A_hop P,
    A=P A_hop R^2 A_hop P,
    C=P A_hop R A_hop R A_hop R A_hop P,
    H_eff^(4) = t^4[-C+(AB+BA)/2].                           (6)

One direct derivation is to expand the finite Feshbach resolvent in hopping
and eigenvalue E. The equation for the P component has metric I+t^2 A and
right side -t^2 B-t^4 C. Conjugating by (I+t^2 A)^(-1/2) gives the anticommutator
in (6). Omitting this folded/normalization term would retain a spurious
volume-squared energy. Odd orders vanish by the parity of N_B.

For every ice configuration, precisely d links permit a plus hop out of each
A site. Equivalently, exactly d such links enter each B site. Consequently

    M=dV/2,
    B=(M/Delta)P,
    A=(M/Delta^2)P.                                         (7)

After the first hop, a second hop either returns to P along the same edge,
which is excluded by R, or puts a second plus on a different B site and leaves
a different A site vacant. Hard-core exclusion prohibits moving into any other
initially occupied A site. The latter excursions have successive denominators
Delta, 2Delta, Delta.

There are

    n_pair = choose(M,2) - V choose(d,2)                     (8)

unordered compatible pairs of initial hops. Distinct allowed edges may not
share an A or B endpoint; the two endpoint collision counts add, since the
lattice has no parallel links between a pair of sites. Returning both records
along their original edges gives two upward and two downward orders, hence
the diagonal contribution C_diag=2 n_pair/Delta^3.

The only different low-space endpoint after four hops comes from swapping
the two identical plus records around a geometrical square. For a flippable
electric loop there are two orders for its initially allowed A-to-B hops and
two orders for the final B-to-A hops: four paths, each of weight 1/(2Delta^3).
All have the same bosonic sign. The field operator is the unit plaquette flip
X_p=W_p+W_p^dag. No other loop of length four exists under the stated periods.

Combining these counts with the folded term gives the complete result

    H_eff = [-M t^2/Delta + M(2d-1)t^4/Delta^3] I
            - (2t^4/Delta^3) sum_p X_p
            + O_V(t^6/Delta^5).                             (9)

The remainder statement is for each fixed finite lattice and sufficiently
small |t|/Delta; its constant may depend on volume. There is **no fourth-order
flippability-dependent diagonal potential** in this model. In one dimension
the plaquette sum is empty. Distinguishable conserved particle identities would
require an additional permutation in the low operator, and fermionic
statistics would change the permutation sign; neither is the given bosonic
qutrit model.

The two independent checks are complementary. Complete small physical-sector
matrix calculations give, on a single cyclic square,

    H_eff^(2)/(t^2/Delta)=-2 I,
    H_eff^(4)/(t^4/Delta^3)=[[2,-2],[-2,2]].

On the six-cycle they give -3 I and +3 I, with no fourth-order winding flip.
Separately, exhaustive order-four hopping-path enumeration on actual side-six
tori gives:

| Geometry and ice word | M | Unfolded fourth diagonal | Folded diagonal | Total diagonal | Flippable squares |
|---|---:|---:|---:|---:|---:|
| 6x6, uniform links | 36 | -1188 | 1296 | 108 | 0 |
| 6x6, staggered links | 36 | -1188 | 1296 | 108 | 18 |
| 6x6x6, staggered links | 324 | -103356 | 104976 | 1620 | 324 |

Every nonzero ring matrix element is exactly -2 in fourth-order units. This
enumerates all contributing paths from each stated ice word, not the complete
many-body Hilbert space on those tori. Equations (7)–(8) supply the proof for
arbitrary ice fields.

## 4. Exact live-birth energy identity

Let S_vac=sum_e P_e. An edge can be vacant only if its A endpoint is vacant, so

    S_vac <= 2d h_A <= 2d N_B,
    d/dtau <N_record> = 2 beta <S_vac>,
    d/dtau <m> = beta <S_vac>.                              (10)

These are operator inequalities and exact expectations; they require no
product approximation. The total record number is nondecreasing in a jump
history, and the associated increments are always two.

The dissipator applied to hopping has a useful exact local reduction. If birth
edge e is disjoint from hopping edge f, its dual dissipator annihilates X_f.
If e=f it also annihilates X_f. If e and f share exactly one endpoint and z is
the other endpoint of e, then

    D_e^dag(X_f) = -(beta/2) q_z^vac X_f.                    (11)

Indeed J_e^dag X_f J_e=0: after birth both endpoints of e are occupied; any
allowed hop touching one endpoint leaves a vacancy there, so J_e^dag then
annihilates it. The remaining anticommutator uses
{q_x^vac,X_f}=X_f. This argument also removes all coherent charge-branch cross
terms; it is valid for both instruments in (3). It is not an assertion that
their full CP maps agree.

The potential drift is Delta beta S_vac for H_s. For H_f it is a positive
diagonal operator bounded by 2Delta beta S_vac. Equation (11), together with
these costs, is the full energy ledger used below. Dissipation need not
conserve H or simply add its potential cost: it also changes hopping energy.

## 5. Volume-uniform mean-density theorem

For either model put b(tau)=<N_B>/V and lambda=|t|/Delta. Each X_e changes its
B endpoint between occupied and vacant. Cauchy-Schwarz gives

    |<X_e>| <= 2 sqrt(<n_B(e)>),
    |<sum_e X_e>| <= C_d V sqrt(b),
    C_d=2 sqrt(2) d.                                        (12)

The same bound applies with a commuting vacancy projector at a third vertex.
Each hopping edge meets 4d-2 different birth edges at exactly one endpoint.
Define c_b=(2d-1)beta. From (10)–(12), writing
h(tau)=<H>/ (Delta V), the two models satisfy

    h >= alpha b - C_d lambda sqrt(b),
    h' <= 2 kappa_b d beta b + c_b C_d lambda sqrt(b),        (13)

with

| Model | alpha | kappa_b |
|---|---:|---:|
| H_s | 1 | 1 |
| H_f | 1/2 | 2 |

Here alpha is a lower bound on the dimensionless potential divided by N_B,
and kappa_b bounds the potential cost per birth in units Delta. The use of
both entries for H_f is necessary; substituting the H_s energy ledger after
births would be incorrect.

Young's inequality and the shifted energy

    y=h+C_d^2 lambda^2/(2alpha)

give y>=alpha b/2>=0 and

    y' <= a y + c_b C_d^2 lambda^2/(2alpha),
    a=4 kappa_b d beta/alpha+c_b.

Every prescribed initial ice density has h(0)=0. Integrating this scalar
inequality proves, for all finite tori and all tau>=0,

    b(tau) <= B_alpha(tau)
      := C_d^2 lambda^2/alpha^2
          [exp(a tau)+(c_b/a)(exp(a tau)-1)].                (14)

The bound may be clipped at 1/2. For beta=0 take the continuous limit of this
formula; the no-birth equality of the two Hamiltonians also yields the sharper
common estimate b<=C_d^2 lambda^2 directly from energy conservation. For beta>0,

    a_s=(6d-1)beta,       a_f=(18d-1)beta.

In particular B_alpha(tau)<=2 C_d^2 lambda^2 alpha^(-2) exp(a tau). All constants
in (14) are independent of volume, the chosen ice component, initial field
coherences and the retained or discarded charge mark. This is a bound on the
exact finite quantum dynamics, not a local-equilibrium closure or simulation
extrapolation.

Equation (4) and (5) then imply

    0 <= <N_record>/V-1/2 <= b,
    <h_A + m_A + N_B>/V <= 2b,
    <sum_x(div E_x)^2>/V <= 3b.                              (15)

The middle quantity counts sites whose occupation/content differs from the
initial A-plus/B-vacant pattern. The final quantity is deviation of charge
from the background, **not a Gauss-law violation**: (1) remains exact.
Markov's inequality also bounds the probability of a macroscopic defect
fraction in a specified measurement at a fixed time. Since total record
number only increases at births, its trajectory maximum through T is its
value at T. No analogous repeatedly measured or trajectory-supremum assertion
for N_B is inferred from (14).

The exponential in (14) is harmless on each fixed [0,T] with beta fixed. It
does not give uniform small density as T tends to infinity, nor control an
arbitrary simultaneous beta-to-infinity limit.

## 6. A finite ring scale with births still enabled

For d>=2 choose a fixed g>0 and

    t_Delta=(g Delta^3/2)^(1/4),
    2t_Delta^4/Delta^3=g,
    lambda^2=sqrt(g/(2Delta)).                              (16)

Keep beta>0 fixed. Equations (14)–(15) give uniform-in-volume mean excess-record,
matter-defect and squared-divergence densities O_(d,beta,T,g)(Delta^(-1/2))
for tau<=T. Each finite model still has genuine live formation. For example,
from any prescribed ice initial state, the small-time expansion is

    <N_record(tau)>/V
       = 1/2 + [beta d(2d-1)t^2/3] tau^3 + O(tau^4).        (17)

One hop creates a vacant A site with 2d-1 still vacant B neighbors; there are
M=dV/2 unit-amplitude allowed initial hops. Equation (17) is independently
checked by the exact third dual-generator derivative on the complete six-cycle
sector for both potentials and all three displayed instrument choices. This
short-time expansion is at fixed parameters; its remainder is not asserted
uniform in the scaling (16).

“Live” in this controlled limit cannot mean a nonzero limiting production
density over [0,T]. Monotonicity gives the exact identity

    E[number of births through T]/V
       = (<N_record(T)>/V-1/2)/2,

which tends to zero by (14). Choosing a growing beta to offset that suppression
requires another analysis; the present estimate does not prove it. Nonzero g
also means a nonzero coefficient in the effective operator, not motion of
every ice configuration. Frozen components can have all X_p=0; in d=1 there
are no elementary squares at all.

## 7. What is, and is not, justified for field dynamics

For each **fixed finite volume**, the scaled coherent Hamiltonian has a gap
Delta at zero hopping and finite operator dimension. Its low spectral block
and orthonormal identification are analytic in lambda for sufficiently small
lambda (with a volume-dependent neighborhood). The hopping-parity symmetry
makes its expansion even. Thus the omitted block term is O_V(Delta lambda^6),
and the near-identity identification differs from P by O_V(lambda). Under
(16), Delta lambda^6=O(Delta^(-1/2)). After dropping the scalar in (9), bare
low-space densities therefore converge on bounded time intervals to

    H_ring=-g sum_p X_p                                     (18)

at fixed volume. This conclusion follows from finite resolvent expansion and
Duhamel, not from the density estimate alone. It applies equally to H_s and
H_f before births by their exact sector equality.

Live formation at fixed beta does not invalidate that fixed-volume conclusion.
Let rho_U(tau) be the no-birth unitary density. For a positive density and the
edge loss in (3),

    ||D_e(rho_U)||_1 <= beta[p_e+sqrt(p_e)],
    p_e=Tr(P_e rho_U).

Unitary energy conservation yields b_U<=C_d^2 lambda^2; (10) and
Cauchy-Schwarz imply

    sum_e ||D_e(rho_U)||_1
      <= beta V[2d C_d^2 lambda^2 + sqrt(2)d C_d lambda].     (19)

Variation of constants and trace-norm contractivity of the exact finite
Lindblad semigroup bound its difference from rho_U by T times (19). Hence it
vanishes for fixed V,T. This argument includes no-event backaction; it does
not infer equality of quantum states just from a small probability of observed
births.

The factor V in (19) and the volume-dependent analytic constants are explicit.
They do **not** establish a uniform-volume field propagator, local field limit,
thermodynamic ground-state phase or photon dynamics. Such conclusions need
additional locality/perturbative estimates. Uniform density control survives
for simultaneous volume growth; the field-dynamics argument given here does
not automatically survive that order of limits. Higher-order winding processes
are likewise not a claim of geometric-sector ergodicity.

## 8. Complete finite checks and their limits

`finite_sector_check.py` builds physical sectors directly by electric-bit
enumeration and q=background+div(field change), with no imported author code.
It checks every allowed matrix element, all specified loss normalizations,
charge and number commutators, both potential identities, all birth-potential
changes and the exact local dissipative hopping identity (11).

The complete sectors have dimensions:

| Control | Full physical sector | No-minus sector | Low sector |
|---|---:|---:|---:|
| Four-cycle, cyclic link reference | 9 | 7 | 2 |
| Six-cycle, cyclic link reference | 27 | 18 | 2 |
| Four-leaf star, frozen external ice flow | 11 | 3 | 1 |
| 3x2 rectangle, frozen external ice flow | 24 | 12 | 1 |

The four-cycle, star and rectangle have selected active internal hopping edges
and fixed exterior reference flows. They are complete controls of those finite
physical sectors, not surrogates for the full period-at-least-six cubic model.
The six-cycle obeys the supplied geometry in d=1. On the rectangle, coherent
vacant-edge input superpositions at two selected edges give an exact squared
Hilbert-Schmidt CP-output difference 1/2 between coherent and charge-resolved
births at unit rate. Equal clocks must not be promoted to equal instruments.

The six-cycle additionally has full finite Liouvillian exponentials at
Delta=64, t=9/4, beta=3/10, elapsed times 0,0.2,0.5,1. All traces, Hermiticity,
positivity within numerical tolerance, density identities and bounds (14) pass.
For example at time one, excess record density is about 0.000679828 and
B-occupation density about 0.00149801. Those particular six-cycle runs agree
across the instruments and potentials because that physical sector does not
expose all their distinctions. The star/rectangle controls demonstrate the
missing branches; no general equality is inferred from the six-cycle screen.
Endpoint densities are preserved in `FINITE_DENSITIES.npz`.

`fourth_order_paths.py` is independently organized as occupation/field bit
paths, not a reduced-matrix implementation. It verifies (9) on the actual
side-six two- and three-dimensional examples, including the cancellation of
the volume-squared terms. `density_bound_check.py` checks the exact initial
record derivatives and the scalar comparison-function algebra in (14).

## 9. Failures, resources and unresolved obligations

The first complete-sector runner attempt failed before its operator checks:
SymPy interpreted a NumPy integer scalar passed to `diag` as a zero-dimensional
array. Original code, streams and receipt are preserved under
`failed_attempts/numpy_scalar_diag/`. Casting counts to ordinary integers was
the only repair. The original successful cycle/star packet is preserved under
`development/before_coherence_control/` before adding the rectangle control.

A later bookkeeping assertion incorrectly required replayed floating numerical
rows to be bitwise identical. The largest difference was 3.552714e-15. Its
submitted helper, full reproduced failure and receipt are preserved under
`failed_attempts/bitwise_float_replay/`. No scientific model, parameter,
assertion tolerance or result was changed in response. Exact fields remain
exactly checked; final evidence comparison uses an explicit 1e-12 tolerance
only for those already successful numerical replay rows.

All three final scientific runners complete successfully and have empty
stderr. The full result documents, full logs, command receipts, runtime
identities, failed attempts and source-read boundary are included in the PRE
seal. No newer author source or output was opened. No new external theorem is
imported; the finite perturbation, count and energy arguments are supplied in
this report.

The supplied jumps constitute an open-system formation mechanism. They do not
by themselves specify an autonomous energy-conserving reservoir. Adding an
occupied-record rest energy costs two such units per birth, in addition to the
potential/hopping ledger above; any fuel, coherent branch resource and exported
record memory must be supplied in an implementation. The field-only form of
H_f does not eliminate the staggered sector/preparation or those resources.

There is no assertion of finite-volume eventual full packing, thermodynamic
photons, a native-qubit compiler, an exact permanent-partner encoding, or a
uniform-volume field-dynamics theorem. Global charge and number parity alone
can preclude full occupation on some allowed finite graphs: for example a
six-cycle begins with three records and births add two. These restrictions do
not affect the finite-time mean-density statement proved here.
