---
claim_id: finite_energy_supply_for_marked_collision_dynamics_bounded_theorem_note_2026-09-24
claim_type: bounded_theorem
claim_scope: "Conditional mathematics of the explicitly supplied finite model and stated limits; numerical controls do not establish physical selection or extend the analytic quantifiers."
upstream_dependencies:
  - minimal_axioms
  - finite_time_star_energy_and_supply_bound_bounded_theorem_note_2026-09-24
  - star_energy_cost_across_the_electric_family_bounded_theorem_note_2026-09-24
runner: scripts/finite_energy_supply_for_marked_collision_dynamics_2026_09_24.py
---

**Type:** bounded_theorem
**Status:** conditional mathematical result; unaudited.

The complete source argument and its selected companion proofs follow, with the narrow corrections documented in the combined review. Dated author-status statements, seals and numerical observations are historical provenance, not audit authority. Quantum spaces, Hamiltonians, instruments, preparations and resource assumptions are supplied mathematical premises. Fresh controls corroborate the proofs within their scope.

# A finite energy supply for marked collision approximations

Personal conditional construction, 2026-09-24; independent reconstruction
pending. The earlier two-level fuel matched one actual output from one input.
Here a supplied, finite, positive-energy reference approximates a marked
operation uniformly on arbitrary inputs, including inputs entangled with an
untouched reference. Applying it to a collision approximation retains the
original microscopic Hamiltonian and jump operators in its generator limit.
The operations are scheduled. A native autonomous reservoir, its preparation,
and a physical selection of the supplied Hamiltonian are not derived.

The energy-translation lift is established machinery: see Aberg,
[arXiv:1304.1060, equation (1)](https://arxiv.org/pdf/1304.1060). That paper also
states its time-control qualification after equation (2). The finite ladder
boundaries, product reference, error bounds and application below are proved
directly; no catalytic or unlimited-reuse theorem is imported.

## 1. Exact finite, positive-energy construction

Let H be a finite-dimensional system Hamiltonian. Subtracting its lowest
eigenvalue for this construction leaves every energy change unchanged. Write

    H-E_min I = sum_(a=1)^r E_a P_a,  E_a>0,
    P_0 + sum_(a=1)^r P_a = I,

where P_a are its distinct energy projections. Degeneracies are allowed.
Introduce r ladders, each with number basis n=0,...,L+1, and set

    H_R = sum_(a=1)^r E_a N_a >=0.                     (1)

There is no assumption that the E_a are commensurate. Its dimension is
(L+2)^r. Each outcome flag has zero Hamiltonian; blank pure flags are explicit
additional resources. Let U be any unitary on system plus finitely many flags.
P_a below includes the identity on those flags. Set v_0=0 and v_a to the a-th
coordinate unit vector in Z^r.

Label a joint system/battery basis vector in system block a and battery
coordinate n by m=n+v_a. In every block with

    1<=m_a<=L+1 for every coordinate a,

all system energy blocks are available: their battery coordinates m-v_a lie
inside the finite cube 0,...,L+1. Identify this complete block with the entire
system-plus-flags space, and let V(U) act as U there. Let it be the identity
on every other, possibly incomplete, label block. This defines an exactly
unitary operator on the entire finite joint space. It conserves each total
label, hence

    [V(U), H+H_R]=0.                                  (2)

Extra degeneracies of H+H_R from rational energy relations cause no problem:
the chosen blocks can be smaller than a total-energy eigenspace. No shift
wraps the top of the battery into its ground state. No negative battery
energies or restrictions to a nonunitary truncated shift are used.

Prepare each ladder in the normalized sine profile supported strictly in the
buffered interval 1,...,L:

    b_L(n)=sqrt(2/(L+1)) sin(pi n/(L+1)),
    beta_L=b_L tensor ... tensor b_L.                 (3)

Every system input tensored with beta_L has support only on the complete
blocks just defined. On that support the action can be written, for analysis,
using bilateral coordinate translations T:

    V(U)=sum_(a,b) P_a U P_b tensor T^(v_b-v_a).       (4)

The implemented finite operator is the block unitary, not the bilateral
extension. All actual final battery coordinates stay in its finite cube.
The initial mean supply energy is exactly

    <H_R>_initial = (L+1)/2 sum_(a=1)^r E_a.           (5)

Equation (2) gives the exact balance of mean energy on every input and after
every conserving operation. Flags and their readout contribute zero free
energy in this supplied construction. This does not account for the physical
cost of producing blank flags or implementing the schedule.

## 2. Uniform channel bound and correlated sequences

The zero-extended one-ladder vector obeys

    <b_L,T b_L>=cos(pi/(L+1)),
    d_L=||T b_L-b_L||=2 sin(pi/(2(L+1))).             (6)

The overlap follows from the finite path adjacency eigenvector equation with
zero endpoint amplitudes. Shifting any single coordinate of beta_L therefore
has this same norm difference. Define controlled translations

    C_+ =sum_a P_a tensor T^(v_a), C_-=C_+*.

Equation (4) is C_- (U tensor I) C_+. Orthogonality of the P_a implies, for
any normalized input vector psi, including arbitrary extra reference factors,

    ||C_+(psi tensor beta_L)-psi tensor beta_L||<=d_L.

The analogous inequality holds for C_- on U psi tensor beta_L. A triangle
inequality and unitarity give a joint-vector difference at most 2d_L between
the lifted output and U psi tensor beta_L. Pure-state trace-norm distance is
at most twice the vector difference. Partial trace and flag readout contract
it. Thus the induced channels, including their classical outcome flags, obey

    ||Phi_L-Phi||_diamond <= eta_L,
    eta_L=min(2,8 sin(pi/(2(L+1))))
          <=min(2,4pi/(L+1)).                         (7)

This uses trace norm without the factor one-half. Purification supplies the
bound for mixed and reference-entangled inputs. The bound does not depend on
the dimensions or energy multiplicities; their resource cost remains in (1)
and (5). If H is scalar, r=0 and no energy reference is needed.

For a sequence U_1,...,U_n on the same system and distinct zero-energy flags,
use the SAME battery. Initial total-label blocks are complete and invariant
throughout. Within each such block,

    V(U_n)...V(U_1)=V(U_n...U_1).                      (8)

Consequently (7) applies to the complete joint flag history with the same
eta_L, without multiplying this error by n. This argument never resets the
battery and never assumes it remains uncorrelated with the system or flags.
Measurements of old flags can be deferred because later operations do not
act on them. The battery state generally changes and acquires correlations.
This is not an assertion of exact catalyst return or unlimited operations on
fresh systems: replacing the system by an ever-growing collection changes
the energy spectrum and the resource problem.

## 3. Marked collisions for the original generator

At fixed finite spin, keep the actual full physical Hamiltonian H and the
original Lj=sqrt(kappa)/epsilon j, for either stipulated instrument. Put

    Gamma=sum_j Lj*Lj, g=||Gamma||, h=||H||,
    A(rho)=-i[H,rho],
    D(rho)=sum_j Lj rho Lj* - (Gamma rho+rho Gamma)/2.

For tau g<=1/2, define the trace-preserving collision instrument before its
Hamiltonian evolution by

    K0=sqrt(I-tau Gamma), Kj=sqrt(tau) Lj.             (9)

Follow it by exp(-i tau H). A finite flag records 0 or the actual mark j.
The isometry psi ->sum_j exp(-i tau H) Kj psi tensor |j> has orthonormal
columns because sum_j Kj*Kj=I. Complete those columns to a unitary on system
and flag. This completion is independent of the input state. Apply sections
1-2 to that unitary. In particular the jump amplitudes in (9) use the original
j, without energy filtering, scalar substitution or incoherent resolution
of a mark originally specified as coherent.

Let Lambda_tau be (9) with its flag discarded, and let
E_tau=exp(tau A) Lambda_tau. It approximates the reduced GKLS channel; it is
not its exact finite-tau no-event operator. A useful explicit estimate is

    ||E_tau-exp(tau(A+D))||_diamond
                  <=tau²(7g²+4hg).                  (10)

For clarity, write sqrt(I-tau Gamma)=I-tau Gamma/2+R. The scalar identity for
the square-root remainder gives ||R||<=tau²g²/2. Both the square root and
I-tau Gamma/2 are contractions, whence

    ||Lambda_tau-(I+tau D)||_diamond <=5tau²g²/4.

Also ||D||_diamond<=2g, so its exponential remainder is at most
2tau²g² exp(2tau g). Combining these bounds costs less than 7tau²g².
Finally all three semigroups generated by A,D,A+D are trace-norm completely
contractive. The integral product formula bounds the splitting error by
tau²||[A,D]||_diamond/2 <=4tau²hg. This proves (10).

For n steps, T=n tau, telescoping completely positive trace-preserving maps
gives a reduced-system error at most T tau(7g²+4hg). Let Psi_(L,tau,T) denote
the actual finite-battery construction, after discarding all flags and the
battery. Equations (7)-(10) imply

    ||Psi_(L,tau,T)-exp(T(A+D))||_diamond
              <=eta_L+T tau(7g²+4hg) =: zeta.        (11)

For fixed finite model and T, increasing L and refining tau makes this error
arbitrarily small. The complete discrete marked instrument is approximated
by (7); (11) compares reduced continuous-time dynamics. No total-variation
comparison between discrete timestamps and an unbinned continuous event-time
path distribution is claimed. Conditioning on a rare flag can amplify an
absolute error, so no uniform normalized rare-output bound is inferred.

## 4. Microscopic energy accuracy and the star application

The finite spectral bound gives an additional, explicit moment estimate:

    |<H>_implemented-<H>_GKLS| <=h zeta.               (12)

This estimate, not qualitative density convergence alone, controls energy.
Combined with (2), it also bounds the error in the mean energy drawn from the
finite supply. Equation (12) applies to any input, including the dressed
star state previously used for its microscopic energy calculation.

There is a useful exact special case. If the system input is supported on one
energy block a, the full lifted output is
sum_b P_b U psi tensor T^(v_a-v_b) beta_L. Different b have orthogonal system
energies, and every translated battery vector has norm one. Thus all final
system energy probabilities, jointly with any zero-energy flag outcome,
coincide exactly with the target operation. The argument extends by mixing to
energy-stationary inputs and applies to the entire discrete history via (8).
Its energy moments agree even when coherences between different energies do
not. In particular the lambda=0 dressed star input has this property. This
does not remove the finite-tau error relative to the continuous GKLS model.

For the compensated degree-three star in the joint limit
epsilon² C=delta/K, C=S(S+1), the original lambda=0 energies are
0, delta epsilon^-4, and delta epsilon^-4(1+3epsilon²). The added electric
term is H_lambda-H0=Klambda E2, with 0<=E2<=3 and 0<=lambda<=1. Thus its
complete sixteen-state spectrum has at most fifteen distinct positive gaps,
h_lambda=O(C²) uniformly in lambda, and g=4kappa/epsilon²=O(C). No closed
formula or rationality assumption for the changed energy gaps is required
by (1)-(11).

For fixed T, one explicit sufficient sequence is L=O(C²), tau=O(C^-5), with
the constants chosen so each term in (11) is at most C^-2/2. This gives
zeta<=C^-2 and

    |<H_lambda>_implemented-<H_lambda>_GKLS|/C=O(C^-1).

The independently reconstructed microscopic star result can therefore be
carried by these engineered conserving operations at the level of its leading
mean energy:

    <H_lambda>_implemented/C
                 ->(3K/2)(1-exp(-12kappa T)).         (13)

Here the preparation is the same dressed star state for all lambda; its
initial H_lambda energy tends to zero. The battery's prepared mean energy in
this sufficient construction is O(C^4), because sum_a E_a=O(C²). Its dimension
can grow as (L+2)^15, and there are O(C^5) blank flags and scheduled operations.
These are loose upper bounds, not optimal requirements or an efficient design.
The actual order-C energy delivered is much smaller than this prepared reserve.

This route covers the entire finite electric family at this stated scope.
Energy conservation plus an arbitrarily engineered growing supply thus does
not, by itself, choose lambda. No general uniqueness or nonselection theorem
is inferred beyond this construction. A physical reservoir law could impose
additional restrictions absent here.

## 5. Remaining physical obligations

All reservoir Hamiltonians, coherent preparation, spectral couplings and blank
flags are supplied. Their implementation need not be spatially local. The
sequence assumes external scheduling; a physical clock, bounded interaction
strength and its energy, irreversible record storage, reset and replenishment
are not derived. A unitary's commutation with free energy does not establish
those properties. The finite collision instrument is exact as defined in (9),
but the original GKLS channel appears only in the controlled limit (11).

The generic construction is useful precisely as a checked alternative to an
universal energy-accounting prohibition. It is not evidence that these large
engineered resources occur in the intended physics. It neither adds an axiom
to the framework nor closes physical selection, the continuum/volume limit,
observed particle laws, gravity, or a TOE. Independent confirmation applies
only after reconstruction and source comparison of this packet.

## 6. Bound sources and executed controls

The exact microscopic star note and its complete matrix control supply H0,
the actual j and its three distinct energies. The electric-family bridge
supplies the positive bounded addition and the same common preparation. For
the uniform-in-lambda version of (13), the direct Duhamel mismatch estimate
in microscopic_electric_robustness_independent/PRE_RECONSTRUCTION.md is used;
that proof is attributed to its independent author. The root bridge stated
the weaker fixed-lambda version. AUTHOR_SEAL.json binds these exact sources.

finite_battery_control.py checks full finite-space unitarity, conservation
and the composition identity exactly for two different six-dimensional
unitaries and noncommensurate gaps sqrt(2),sqrt(3). Larger finite widths check
the isometry bound, a reference-entangled input and mean-energy balance.
A cyclic boundary wrap is explicitly detected as energy-nonconserving.
marked_collision_control.py reuses the pinned root star matrices in an
expendable copy. It checks complete-channel collision convergence in two
specified cases, then both actual marked isometries, their unitary completions,
the finite-supply all-input bound and exact stationary-input flag/energy
probabilities. The analytic argument supplies the general scope; the finite
samples do not establish it alone. Complete outputs are retained.


## Landing scope and No-Go Discipline Gate

- **N1 — Domain:** the specified graph, sector, input, observable and order of limits.
- **N2 — Alternatives:** other models, initial states, instruments and resource scalings remain possible.
- **N3 — Imports:** supplied quantum and probability structures are mathematical assumptions, not new repository axioms.
- **N4 — Dependencies:** companion results retain their hypotheses; no retained grade is imported.
- **N5 — Evidence:** exact finite controls and fresh numerical diagnostics corroborate the argument; floating computations are not interval enclosures.
- **N6 — Resolution:** density convergence, energy convergence, initial power, finite time and volume limits are distinct statements.
- **N7 — Remaining work:** native selection, physical implementation and empirical identification remain separate obligations.
- **N8 — Authority:** no audit verdict or retained-grade promotion is applied.

## Imports

- [minimal_axioms](MINIMAL_AXIOMS_2026-06-29.md): repository premise boundary; it does not derive the supplied model.
- [finite_time_star_energy_and_supply_bound_bounded_theorem_note_2026-09-24](FINITE_TIME_STAR_ENERGY_AND_SUPPLY_BOUND_BOUNDED_THEOREM_NOTE_2026-09-24.md): conditional companion source within its stated hypotheses.
- [star_energy_cost_across_the_electric_family_bounded_theorem_note_2026-09-24](STAR_ENERGY_COST_ACROSS_THE_ELECTRIC_FAMILY_BOUNDED_THEOREM_NOTE_2026-09-24.md): conditional companion source within its stated hypotheses.

## Source and verification

Source PR #8929, frozen head `413c01cc40fd085380125c8e1ec66a61f503eee3`. Original source dispositions and recovery branches are recorded in the combined receipt. Review uses the same primary session without subagents; no separate fix reviewer or formal audit is claimed.

```bash
python3 scripts/finite_energy_supply_for_marked_collision_dynamics_2026_09_24.py
```

Fresh controls execute in a temporary directory. Full scientific stdout and generated JSON are included in the authenticated result. Historical diagnostics and deferred source remain recoverable from the original branch.
