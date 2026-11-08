---
claim_id: su2_neighborhood_propagation_record_readout_bounded_theorem_note_2026_11_08
claim_type: bounded_theorem
claim_scope: A covariant conditional permanent-record copy law relays a supplied record along arbitrary finite adjacent paths. Under separately supplied tensor quantum kinematics, preparation, driven gates and a Born instrument, a five-site circuit measures the electric Casimir of the five-state SU(2) link using 19 adjacent pair gates and seven onsite gates. The active link code and Gauss constraints are preserved by the completed instrument, including external entanglement. Fresh output records enlarge the original fixed-spectator code. Neither an autonomous homogeneous joint law nor plaquette evolution is derived.
upstream_dependencies: []
runner: scripts/gb1_cf_neighborhood_record_readout_exact_2026_11_08.py
actual_current_surface_status: conditional-support
target_claim_type: bounded_theorem
trace_class: upstream_support
reachability_to_target: partially_closes
artifact_role: theorem
next_trace_action: Construct a specified homogeneous joint live-state and record process, with fresh output allocation, and test plaquette evolution.
audit_required_before_effective_retained: true
bare_retained_allowed: false
---

# Neighborhood propagation and electric-value records in the native code

**Type:** bounded_theorem
**Status:** conditional author construction; independent audit pending.

The user clarified that neighborhood influence can propagate through neighbors.
The results below use successive adjacent-site operations. An instantaneous
in-code nearest-neighbor generator is a different target and is not imposed.
The construction was checked against the axiom wording at main `f5af11cd`.
The owner subsequently approved the two governing substitutions of
"neighborhood" for "nearest-neighbor", landed separately in
[PR #10143](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/pull/10143).
The [current axioms](MINIMAL_AXIOMS_2026-06-29.md) include that wording; it does
not supply the quantum preparations, gates or probability values used below.

## 1. A permanent-record relay

For this candidate, support record content on rank-one projectors in the
one-site M2 algebra. Let N_R(x) be the recorded sites adjacent to a forming
site x. Supply the fixed conditional distribution

    mu_x = (1/k) sum_{y in N_R(x)} delta_{P_y},  k=|N_R(x)|>0,

and, for k=0, use normalized area measure on the Bloch sphere of rank-one
projectors. Append the sampled content at x and never modify an old record.
The law is normalized, varies with the neighbor condition, and is covariant
under all native translations and proper cubic rotations: these permute the
neighbors without changing the average. Unitary conjugation of every record
also conjugates the distribution. This is a chosen law, not a derivation
that the axioms select it or select rank-one record contents.

Supply one initial record P and a finite self-avoiding adjacent path starting
there, with no other initial records. Supply formation along the path in
order. At each step every already recorded neighbor has content P, including
any additional neighbors caused by a path approaching itself. Induction gives
mu_x=delta_P at every new site. A straight path therefore relays P to arbitrary
finite graph distance while preserving every old record.

This closes a genuine conditional record-propagation example. Its formation
order is supplied; no clock, rate or autonomous scheduler follows. It carries
an existing record value, not an unknown quantum state. It demonstrates why
elementary locality must not be mistaken for a one-step bound on total influence.

## 2. The gauge register and the exact quantum target

Use the [previous native code](SU2_HOMOGENEOUS_NATIVE_QUBIT_CODE_BOUNDED_THEOREM_NOTE_2026-11-08.md)
on four consecutive sites numbered 1,2,3,4, with e_i the one-excitation words:

    J0=(e1+e4)/sqrt(2), J1=(e1-e4)/sqrt(2),
    J2=(e2-e3)/sqrt(2), J3=(1100-0011)/sqrt(2),
    J4=(e2+e3)/sqrt(2).

The five columns are orthonormal. Put a fresh unrecorded output at site
0 immediately before site 1, prepared in |0>. Under the spacing-five
placement, site 0 is a coarse vertex and hence an available spectator in
a fixed grid-origin sector. Supply ordinary tensor quantum states, the
specified gates, the schedule, a final Z-basis Born instrument and the
interpretation of its outcome as a permanent record. These are mathematical
conditions, not consequences of a one-site M2 presentation.

Write P0=|0><0| and P1=sum_{mu=1}^4 |mu><mu| on the five-state link.
Its electric Casimir is E²=(3/4)P1. The target is the instrument

    rho -> P_b rho P_b,  probability Tr(P_b rho),  readout 3b/4,

including on states entangled with other links. This is an electric-value
measurement, not a construction of Hamiltonian evolution.

## 3. A five-site circuit with no work qubits

Gate lists are chronological. S is full SWAP, CX has its first argument as
control, and H is Hadamard. Decode the data by

    W: S(3,4), S(2,3), CX(1,2), H(1), CX(3,4).

The two swaps send abcd to adbc. The endpoint Bell phases give

    WJ0=0100,  WJ1=-1100.

Every word contributing to J2,J3,J4 has exactly one old middle bit equal
to one. Those bits move to sites 3,4, remain unaffected by the endpoint
decoding, and their parity is written into site 4 by the last CX.
Consequently the decoded flag table is:

| Input | Site 1 | Site 4 | Energy bit |
|---|---|---|---|
| J0 | 0 | 0 | 0 |
| J1 | 1 | 0 | 1 |
| J2,J3,J4 | arbitrary coherent value | 1 | 1 |

For P=|0><0|_1 tensor I_2 tensor I_3 tensor |0><0|_4 this proves

    W† P W J = J P0,   W†(I-P)W J = J P1.

P has rank four on the full native data space; its restriction through J
is the rank-one logical vacuum projector. No equality off the code is claimed.

To copy the flag, first apply X(1),X(4), then S(3,4),S(2,3).
The two controls are now at sites 1,2. Define
V=(I+X)/2 + i(I-X)/2, so V²=X. On consecutive sites 0,1,2 the list

    CV(1,0), CX(2,1), CV†(1,0), CX(2,1),
    S(2,1), CV(1,0), S(2,1)

is Toffoli with controls 1,2 and target 0. The last three gates equal
CV(2,0) by tensor-factor permutation. On basis control bits u,v the target
exponent of V is v-(v XOR u)+u=2uv, and the controls are restored.
Linearity proves the identity for arbitrary entangled inputs, with no
phase discarded.

After this Toffoli, undo the route with S(2,3),S(3,4), undo the negative
controls with X(1),X(4), and apply X(0). The output holds the OR of the
two original decoded flag bits. Finally apply W†:

    CX(3,4), H(1), CX(1,2), S(2,3), S(3,4).

There are 4+11+4=19 adjacent pair gates and 1+5+1=7 onsite gates, followed
by one output instrument. No work qubits, reset or discarded data are used.
The data may leave the code during the sequence; the completed instrument
returns it to the code.

For any external system A and arbitrary vectors r_mu, the complete unitary
takes a fresh output and sum_mu J|mu> tensor r_mu to

    |0>_out J|0> r_0 + |1>_out sum_{mu=1}^4 J|mu> r_mu.

This proves the target instrument, preservation of coherence inside the
four-dimensional occupied sector, and validity for arbitrary external
entanglement and mixed inputs.

## 4. Gauge gluing and the output-space change

The supplied endpoint representation is (0,0) direct-sum (1/2,1/2).
P0 and P1 project onto these invariant summands and commute with both
endpoint gauge actions. With trivial gauge action assigned to the output,
the completed instrument, tensored with identity on other links, preserves
the Gauss-invariant subspace, including the glued finite patches. This
does not make each intermediate native gate gauge invariant.

The active data code is preserved, but the original global code C_p fixes
every spectator to |0>. A recorded output 1 therefore lies outside C_p.
The required finite readout space is the active code tensor a two-state
output, with the other spectators still fixed. No local site dimension
has increased, but the allowed encoded subspace has changed. The output
cannot be reused after recording; permanence here is imposed by never
acting on it again.

This experiment is specified in one fixed grid-origin sector. Translating
or rotating the whole apparatus gives another valid experiment. It is not
one autonomous covariant program on the coherent sum of all 125 origins.
Neither indefinite fresh-output supply nor a global phase-compatible record
allocation has been constructed.

## 5. A discriminating phase and record-first comparison

The code family psi_phi=(e1+exp(i phi)e4)/sqrt(2) has identical computational
populations for every phi. Its actual electric readout probabilities are

    Pr(E²=0)=(1+cos(phi))/2,
    Pr(E²=3/4)=(1-cos(phi))/2.

Thus J0 and J1 give opposite certain electric values. If the four data
sites are first recorded in the computational basis, their outcome-labelled
ensembles agree for both states: e1 and e4 each occur with probability 1/2.
This specific instrument loses the distinguishing phase. Formally applying
the quantum circuit to that dephased ensemble gives equal output odds;
operating on already permanent data records is not itself permitted by
the schedule used here.

A second exact example is J3. Computational dephasing gives the equal
mixture of 1100 and 0011. Its overlap with Q=JJ† is 1/2, since the symmetric
partner (1100+0011)/sqrt(2) is outside the code. Four permanent basis records
therefore cannot simply be substituted for this live register.

These are instrument-specific counterexamples. They do not exclude a
different record instrument, fresh outputs, preparation records, or a
law whose quantum state is reconstructed from its record history.

## 6. What is closed and what still needs a law

Closed: a conditional record relay; an exact adjacent-gate electric
instrument on the full active link code; compatibility of its completed
action with finite Gauss gluing; and an explicit change to the output
subspace needed by records. This construction adds no axiom or primitive.

The missing object is a specified joint law for live encoded data and permanent
records, with preparation, local propagation, formation and fresh-site
allocation. A pair of distinct live preparations with identical current record
configurations is not automatically a pair of distinct framework states:
the qualification says a state is a configuration of records. A realization
must connect those preparations to distinguishing record/history conditions
or propose a broader state description. This work does not prove that an
axiom change is necessary. The particular probability weights and driven
gates here remain supplied, and magnetic plaquette evolution remains untested.

## Evidence and method credits

The [exact runner](../scripts/gb1_cf_neighborhood_record_readout_exact_2026_11_08.py)
uses Gaussian-rational state vectors and tests all five code columns with
both pointer inputs. It separately checks a different seven-site electric
instrument with two returned work qubits on every clean-work basis input.
The two native extensions agree on the code and differ off it. A 74-pair-gate
controlled-reversal experiment supplies another phase-sensitive test;
orientation reversal is not asserted to be gauge invariant at fixed endpoints.
Finite relay checks supplement the induction proof.

The [cache](../logs/runner-cache/gb1_cf_neighborhood_record_readout_exact_2026_11_08.txt)
and [research handoff](../.claude/science/physics-loops/gb1-cf-boundary-gluing-20261107/native_law/HANDOFF.md)
record actual execution, independent derivations and source identities.
The [scope check](SU2_NEIGHBORHOOD_PROPAGATION_RECORD_READOUT_SCOPE_CHECK_2026-11-08.md)
keeps the record-first witnesses separate from any general no-go.

The controlled-square-root method is due to Barenco and colleagues,
[Elementary gates for quantum computation](https://arxiv.org/abs/quant-ph/9503016),
Lemma 6.1; the concrete identity is proved above. Returned SWAP routing is also
used in the repo's
[finite local clock/memory note](FINITE_LOCAL_CLOCK_MEMORY_RESOURCES_BOUNDED_THEOREM_NOTE_2026-10-15.md),
section 4; only that elementary permutation identity is reused. No claim
about its clock, thermal model or retained standing is imported. The
[record-sufficiency note](LIVE_M2_RECORD_SUFFICIENT_JOINT_LAW_STATE_ONTOLOGY_FORK_BOUNDED_THEOREM_NOTE_2026-08-14.md),
sections 4 and 8, motivates keeping current-record, history-conditioned and
live-state realizations distinct; its numerical results are not used.
