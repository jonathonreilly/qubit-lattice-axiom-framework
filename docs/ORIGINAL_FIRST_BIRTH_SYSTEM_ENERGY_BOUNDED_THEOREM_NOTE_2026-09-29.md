---
claim_id: original_first_birth_system_energy_bounded_theorem_note_2026-09-29
claim_type: bounded_theorem
claim_scope: For the supplied full cubic integer-rotor common law on each even torus of side at least 24, the original first formation marks have strictly positive conditional system mean-energy increments at every finite actual first waiting time from the specified zero-field all-A-plus preparation. Exact local operator bounds and prebirth-sector adjoint-dissipator power are established for all positive K,delta,kappa. Physical work or heat, microscopic-limit energy, later-birth drift and an autonomous energy supplier are outside the theorem.
upstream_dependencies:
- local_compensation_common_field_record_limit_bounded_theorem_note_2026-09-24
- local_pair_form_and_general_graph_magnetic_dynamics_bounded_theorem_note_2026-09-24
runner: scripts/original_first_birth_energy_2026_09_29.py
---

**Type:** bounded_theorem
**Status:** conditional-support (supplied model; unaudited)

# Original first births increase the supplied system energy throughout the first wait

For the full supplied cubic rotor law, every original first mark from the
actual waiting state of the zero-field all-A-plus preparation increases the
conditional system mean energy. This statement holds at every finite first
waiting time and every positive electric-to-magnetic ratio. It keeps the full
postbirth Hamiltonian, the original five-branch or ten-branch mark, and its
interference. The energy is the model's common-law Hamiltonian; physical work,
heat, microscopic energy and a compensating reservoir remain separate questions.

```yaml
actual_current_surface_status: conditional-support
target_claim_type: bounded_theorem
trace_class: direct_blocker_closure
target_claim_id: null
target_blocker_text: "build an actual mixed-bracket or record-birth energy witness"
source_of_blocker_text: handoff
reachability_to_target: closes
artifact_role: theorem
next_trace_action: "Construct a supplier preserving the original instrument and account for its complementary energy and current."
conditional_surface_status: exact first-wait energy inequalities in the supplied model
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "An exact finite-domain inequality is proved for an explicitly supplied carrier, law, state and instrument."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

The trace target is the pre-existing campaign opportunity-queue discriminator
quoted above, restricted to its record-birth energy witness. This theorem
closes that calculation for the stated first-wait domain. The common-action
and autonomous-supplier obligations remain open. Exact queue provenance is
recorded in the milestone trace record.

## Supplied model and imports

The mathematical definitions are the
[local pair form](LOCAL_PAIR_FORM_AND_GENERAL_GRAPH_MAGNETIC_DYNAMICS_BOUNDED_THEOREM_NOTE_2026-09-24.md)
and [common field and record law](LOCAL_COMPENSATION_COMMON_FIELD_RECORD_LIMIT_BOUNDED_THEOREM_NOTE_2026-09-24.md).
Their explicit Hamiltonian and marks are supplied here as a model; the result
does not require reproving their microscopic limit. Every definition needed
for the calculation is restated below.

| Input | Role | Provenance | Physical identification still open |
|---|---|---|---|
| Hard-core charges 0,+1,-1 and integer edge rotors | Mathematical carrier | Two linked model definitions | Derivation of this carrier from the native qubit foundation |
| Full Hamiltonian and original formation marks | Evolution and event instrument | Two linked model definitions, restated below | Selection of the physical law and its energy supplier |
| Zero-field all-A-plus state | Actual initial preparation for this theorem | Explicit supplied state Ω below | Preparation mechanism |
| Positive K,delta,kappa and continuous time | Model coefficients and event clock | Supplied parameters | Calibration and physical clock selection |

Registered scale reference fixes units, kinetic isotropy has its registered
kinetic-form scope, and realized state supplies pointwise evaluation. None is
being used to select this Hamiltonian, state or formation instrument. No axiom
or primitive is added.

Take a finite periodic cubic lattice with even side L>=24. Its bipartition is
A,B, with N=|A|=L^3/2, and all edges are oriented A to B. Work in the sector P
where every A is occupied, with integer rotors satisfying div E=q-1_A.
Charges on different sites are tensor hard-core variables, with no exchange
sign. A hop F_a moves q_a to an empty neighboring B site b, empties a, and
shifts E_ab by -q_a. Its adjoint reverses the move. The original j_ab,sigma
fills two empty endpoints with sigma,-sigma and shifts E_ab by sigma.

Define

    D = sum_(a->b with q_b=0) E_ab(E_ab-q_a),
    S_ac = F_c F_a P,
    H4 = -2 sum_(unordered A pairs at graph distance2) S_ac* S_ac,
    h = K D + delta H4,
    B_ab,sigma = P j_ab,sigma F_a P,   B_ab,c = B_ab,+ + B_ab,-.

All three coefficients K,delta,kappa are positive. The resolved instrument
has the two signs per edge; the coherent instrument has the unchanged sum
per edge. Its rate coefficient remains kappa. The common generator is

    d rho/dt = -i[h,rho] + kappa sum_m
      (B_m rho B_m* - {B_m*B_m,rho}/2).

Ω has q_a=+1 on every A, empty B, and E=0. The normalized actual prebirth
state will be shown to be phi_s=exp(-i h_pre s)Ω. For each original mark set

    Q_m(s) = <B_m phi_s,h B_m phi_s>/n_m - <phi_s,h_pre phi_s>,
    n_-=n_+=5, n_c=10.

## Exact target and obligation graph

**Theorem.** For every stated finite torus, positive K,delta,kappa and finite
first waiting time s>=0, the three actual conditional increments obey

| Original mark | Q_m(0)/delta | Lower bound Q_m(s)/delta |
|---|---:|---:|
| Minus | 12172/5 | 8308/5 |
| Plus | 8452/5 | 860 |
| Coherent | 10312/5 | 6304/5 |

For either complete original instrument, its adjoint-dissipator system power
on this conditioned prebirth trajectory satisfies

    Power(s) = 60 kappa N Q_c(s) >= 75648 kappa delta N,
    Power(0) = 123744 kappa delta N.

The proof needs five intermediate statements: original-mark isometries and
actual waiting law; local full magnetic compression; exact electric compression;
prebirth symmetry and energy conservation; complete-instrument power. Each is
proved here. The exact magnetic coefficients are reconstructed by two distinct
finite algorithms. The supplied carrier and dynamics are explicit hypotheses,
not claims derived by this note. There is no open lemma inside the stated
finite-prebirth inequality.

## Original marks and the actual waiting state

For a fixed edge a->b, the original mark is

    B_ab,sigma phi = sum_(d~a,d!=b) |q_(sigma,d)>
                           U_ab^sigma U_ad^(-1) phi.

There are five orthogonal final matter words for each sign; opposite signs
also have orthogonal ranges. Therefore B_sigma*B_sigma=5I and B_c*B_c=10I
on the whole prebirth rotor space. There are 6N edges, so the loss is 60NI for
either instrument. The no-jump decay is a scalar, and normalization gives
precisely phi_s=exp(-ih_pre s)Ω. The no-birth probability is exp(-60kappa Ns).
No small-field or rare-event approximation is used.

The full Hamiltonian also has zero cross-sign compression. D is matter-diagonal.
In S_ac*S_ac both outward hops precede both returns. A B site already occupied
cannot receive an outward hop; a return may leave it occupied or remove its
charge, but cannot replace it by the opposite charge. The fixed b is occupied
with opposite signs in the two original outputs. Hence B_-*hB_+=B_+*hB_-=0
on the prebirth sector. Same-sign destination interference is retained.

## Exact full magnetic increment

On the prebirth rotor space let

    A_m = B_m*H4 B_m/n_m - H4_pre
        = a_m I + sum_(z!=0) c_(m,z) U^z.

Only pair stars meeting the root star can contribute to this difference.
The active A centers are the root and its 18 distance-two neighbors; there
are 264 unordered distance-two pairs with an endpoint in that set. For every
other pair, the local pair term commutes with the mark and its adjoint, and
B_m*B_m=n_m I cancels the entire operator contribution. This cancellation
includes nonconstant rotor shifts.

Two independent computations implement the literal source operations. One
applies outward hops, their adjoint returns, and the inverse original mark.
The other forms Gram matrices of complete two-hop outputs grouped by actual
matter word, keeping all rotor shifts. They agree on all 855 coefficients.
The results are:

| Mark | a_m | Sum of absolute nonconstant coefficients | Nonconstant words |
|---|---:|---:|---:|
| Minus | 12172/5 | 3624/5 | 284 |
| Plus | 8452/5 | 3912/5 | 284 |
| Coherent | 10312/5 | 3768/5 | 284 |

There are 285 words including the constant in each polynomial. Every shift is
an integer circulation, with the reverse shift carrying the same coefficient.
Their vertices lie in [-2,2]^3; the complete hop paths lie within a radius-five
coordinate patch. The stated L>=24 avoids all identifications in that patch.
The full coefficient output, not a field-angle sample, is preserved by the runner.

Since each rotor translation is unitary,

    A_- >= (8548/5)I,   A_+ >= 908I,   A_c >= (6544/5)I.

Also A_c=(A_-+A_+)/2 coefficient by coefficient. At Ω, all nonconstant
circulations have zero expectation, giving the initial constants in the theorem.
As an additional inspectable contraction, each sign block of the ten-vector
constant matrix has diagonal 2444 for the opposite foot and 2432 for each of
four transverse feet. Minus has zero off-diagonal entries; plus has -186 at
every distinct-foot entry; the sign-cross block is zero. Thus the minus
average is(2444+4*2432)/5 and the plus average is lower by 4*186.

## Electric compression and the finite waiting-time bound

For any divergence-free prebirth integer field E, one actual branch obeys

    Delta D_(sigma,d)(E)
      = -sum_(x in{b,d}) sum_(c~x) E_cx^2
        -(1-sigma)(E_ab+E_ad).

Both b,d become occupied, removing all electric terms ending there. The two
rotor shifts end at those occupied sites and contribute to no remaining D
term. For the minus mark the changed root charge adds twice the electric
sum over its other four edges. Input Gauss law converts that sum to
-2(E_ab+E_ad). Input Gauss at b,d removes the linear terms from their removed
edges. This proves the formula for every divergence-free input field;
310 nonzero-circulation branch checks test it directly.

In the prebirth sector D=sum_e E_e^2. There are six distance-two A partners
with one shared B and twelve with two. Literal two-hop return counts are35
and34 respectively. Counting each unordered pair once gives

    H4_pre = -618 N I + V,
    V = -2 sum_(6N elementary plaquettes p) (U_p+U_p*),
    ||V|| <= 24N.

The runner derives these counts from the hop rules. Each plaquette occurs
with its two orientations, so the coefficient and norm estimate include
both. No unmerged band or preparation lemma is needed.

The prebirth Hamiltonian and Ω are invariant under even-sublattice translations,
proper cubic rotations and the unitary field inversion |E> to |-E>. These
symmetries persist under evolution, giving <E_e>=0 and
<E_e^2>=<D>/(6N). Each branch removes twelve distinct edges, so

    <Delta D_m>_(phi_s) = -2<D>_(phi_s)/N

for all three marks. Energy conservation from Ω yields

    K<D> + delta<V> = 0,
    K<D>/N <= 24 delta,
    K<Delta D_m> >= -48 delta.

Adding this to the full magnetic lower bounds proves the three inequalities.
The argument is uniform in K/delta>0 and s finite; it uses the actual
prebirth evolution rather than substituting a zero-field state at later times.

## Complete-instrument power and domains

On a prebirth input, the adjoint-dissipator contribution of mark m is

    kappa(<B_m* h B_m> - <{B_m*B_m,h}>/2)
      = kappa n_m Q_m.

The loss term remains present. Symmetry equates translated and rotated edges,
and the zero cross-sign Hamiltonian compression gives Q_c=(Q_-+Q_+)/2.
Summing 6N edges proves Power=60kappa N Q_c and the displayed constants.
This is the instantaneous power evaluated on the conditioned prebirth state.
Its contribution to the full ensemble at time s carries the no-birth survival
factor. The theorem makes no claim about the sign after arbitrary later births.

On each fixed finite graph D_pre is self-adjoint and H4_pre is bounded. Ω
lies in Dom D_pre and its unitary evolution remains in that domain. Each
first mark is a finite sum of finite rotor shifts, and its output electric
operator is bounded in magnitude by a constant times 1+D_pre. Thus every
energy expectation above is well defined. Ω also has all electric moments;
finite rotor shifts preserve each polynomial electric graph norm under the
bounded-potential interaction-picture expansion. This provides the weighted
control needed to interpret the adjoint expression as ordinary instantaneous
system-energy drift. No trace-norm limit is substituted for an unbounded-energy
limit, and no infinite-volume first-event process is invoked.

## Boundary, evidence and review record

At s=0 the equalities are exact. K,delta,kappa=0 are outside the stated
strictly positive parameter domain; the displayed algebra may have separate
limits there, but strict positive power is not asserted at delta=0 or kappa=0.
Odd tori, later-birth inputs, a thermodynamic global first event, microscopic
energy convergence and a laboratory energy interpretation are outside scope.

The strongest next physical obligation is a supplier preserving these original
mark maps and their count statistics while accounting for complementary energy,
interaction energy and current. That construction is target-equivalent to an
autonomous event-energy ledger for this supplied model, not a lemma proved here.
The present positive inequality specifies a transfer it must account for.

Primary runner: `scripts/original_first_birth_energy_2026_09_29.py`; it directly
imports the distinct Gram-path implementation, so both code paths are in its
restricted packet. Its declared inputs bind this note, that implementation and
the two landed model definitions. No unmerged input or gitignored evidence is
needed. The paired cache is produced only by `scripts/runner_cache.py`.
Full coefficients, the first matrix and a result record are written to
`outputs/original-first-birth-energy-2026-09-29/`.

The research setup was compared with the provisional PR9345 at
`fe51bf1728b625dc0133256f43e7783afb11f7d8`. Its band, response and extreme-parameter
results are not dependencies: the mark normalization, prebirth geometry,
waiting law and energy estimate are derived here. The landed earlier note
`ACTUAL_INPUT_ENERGY_AND_ORIGINAL_MARK_POWER_BOUNDED_THEOREM_NOTE_2026-09-25.md`
uses a different charged preparation and selected mark; its broader physical
identifications are not imported. This note adds a separate theorem and
replaces no prior source.

Independent discovery checking reconstructed all 855 magnetic coefficients,
the complete first matrix, electric compression and prebirth geometry before
this source packaging. Formal source review and mutation checks are recorded
in the campaign's review pack when actually completed. No audit verdict or
effective retained status is supplied by this author note.
