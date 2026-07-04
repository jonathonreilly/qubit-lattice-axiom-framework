# Frontier Extension: Lane B Protects Lane A — Joint Composition Narrow Note

**Claim type:** bounded_theorem

**Date:** 2026-05-17
**Status:** narrow positive composition theorem; advances the
frontier-extension lane-opening note but does not close the lane
**Runner:** `scripts/frontier_extension_lane_b_protects_lane_a_joint_composition_narrow.py`
**Scope:** physical `Cl(3)` / `Z^3` framework-compatible composition of
already-landed Lane A (teleportation no-signaling) and Lane B (chronology
no-past-signaling) results inside one single-clock joint circuit

## What this note is

The lane-opening note
[FRONTIER_EXTENSION_LANE_OPENING_NOTE_2026-04-25.md](FRONTIER_EXTENSION_LANE_OPENING_NOTE_2026-04-25.md)
contains, in its "Priority Order" section, the claim:

> "Land the chronology boundary second. It protects the framework from
> sloppy implications of CPT, reversibility, and teleportation."

This is a derivation-shaped claim about the composition of Lane A and
Lane B that has not been individually closed. The two lanes have landed
their own first-gate theorems:

- Lane A: `docs/TELEPORTATION_NO_SIGNALING_AUDIT.md` and
  `scripts/frontier_teleportation_protocol.py`. The pre-message reduced
  state at Bob is input-independent on the encoded taste-qubit register.
- Lane B:
  `docs/CHRONOLOGY_PROTECTION_OPERATIONAL_NO_PAST_SIGNALING_THEOREM_NOTE_2026-04-25.md`
  and `scripts/frontier_chronology_operational_no_past_signaling.py`. On
  the retained single-clock framework surface, no later CPTP setting at
  `t_1` can alter the operational probability of an earlier durable
  record at `t_0 < t_1`.

Neither of those two notes states the *composition*: that a teleportation
protocol followed by an arbitrary chronology-respecting CPTP setting at
Bob's location cannot leak past-information about Alice's record.

This note closes that exact composition as a narrow positive theorem. It
does not close the lane, and does not promote the lane-opening note to a
manuscript-surface or retained claim. It also does not promote Lane C
(signed gravity) in any way.

Safe wording:

> Within the retained single-clock joint circuit, a successful native
> taste-qubit teleportation at `t_B` followed by an arbitrary CPTP setting
> at Bob's location at `t_C > t_B` cannot alter the operational marginal
> of Alice's earlier record at `t_A < t_B`. The pre-message Bob no-
> signaling is robust under every later chronology-respecting operation,
> with the standard postselection / final-boundary / directed-cycle
> exceptions explicitly excluded.

## Existing imports

This note uses only already-opened framework structure. It does not
introduce a new axiom, a new primitive, or a new framework surface. The
load-bearing inputs are:

- Hilbert/tensor-product surface from
  [SINGLE_AXIOM_HILBERT_NOTE.md](SINGLE_AXIOM_HILBERT_NOTE.md), used as
  the encoded taste-qubit register;
- Bell-inequality framework from
  [BELL_INEQUALITY_DERIVED_NOTE.md](BELL_INEQUALITY_DERIVED_NOTE.md), used
  as the source of the Bell pair `|Phi+>` resource;
- Teleportation no-signaling from
  [TELEPORTATION_NO_SIGNALING_AUDIT.md](TELEPORTATION_NO_SIGNALING_AUDIT.md);
- Chronology no-past-signaling from
  [CHRONOLOGY_PROTECTION_OPERATIONAL_NO_PAST_SIGNALING_THEOREM_NOTE_2026-04-25.md](CHRONOLOGY_PROTECTION_OPERATIONAL_NO_PAST_SIGNALING_THEOREM_NOTE_2026-04-25.md);
- The lane-opening framing from
  [FRONTIER_EXTENSION_LANE_OPENING_NOTE_2026-04-25.md](FRONTIER_EXTENSION_LANE_OPENING_NOTE_2026-04-25.md),
  which posits the protection effect as Lane B's role in the priority
  ordering.

## Formal model

Fix three clock times `t_A < t_B < t_C`.

1. At `t_A`, the joint state on three taste-qubit registers
   `H_A tensor H_R tensor H_B` is
   `rho_psi tensor |Phi+><Phi+|_RB`,
   where `rho_psi = |psi><psi|` and `|psi>` is an arbitrary unknown
   pure single-qubit input. The Bell resource `|Phi+>` is the standard
   `(|00>+|11>)/sqrt(2)`, taken to be the high-fidelity preparation
   delivered by the Lane A teleportation lane.

2. Alice performs a Bell measurement on `(A, R)`. The four projectors
   `P_a = |B_a><B_a|` for `a in {(0,0),(1,0),(0,1),(1,1)}` produce a
   classical record `a` of two bits. The branch state after outcome `a`
   is
   `branch_a = (P_a tensor I_B) (rho_psi tensor |Phi+><Phi+|) (P_a tensor I_B)`
   with `P(a) = Tr(branch_a)`.

3. At `t_B`, the post-correction teleportation channel
   `T(rho_psi) = sum_a C_a Tr_(A,R)(branch_a) C_a^dagger`
   delivers Bob's state. The pre-message Bob marginal at `t_B` (without
   using `a`) is
   `rho_B^pre = sum_a Tr_(A,R)(branch_a)`.

4. At `t_C > t_B`, an arbitrary CPTP setting `S_x` is applied to Bob's
   register. The setting can be a unitary, a dephasing channel, a memory
   reset, a Loschmidt-echo unitary chain, or a generic depolarizing
   channel. The composition with the joint circuit is the channel
   `(I_A tensor I_R tensor S_x)`.

An operational past signal is a dependence of the earlier record
distribution `P(a at t_A | x)` on the later freely chosen setting `x`,
without conditioning on a future outcome `b`.

As in the Lane B theorem, this definition intentionally permits
destructive future operations on Bob's memory at `t_C`. Such operations
are ordinary future causal actions on Bob's local register; they are not
edits of the event law at `t_A`.

## Theorem (Joint Protection)

For every admissible input `rho_psi`, every later setting `x`, every
CPTP later channel `S_x` on Bob's register, and every Alice Bell outcome
`a`,

```text
P(a at t_A | x) = P(a at t_A).
```

Equivalently, the *unconditioned* marginal of Alice's earlier record is
invariant under any later chronology-respecting setting at Bob, even
when the joint circuit contains a successful teleportation protocol.

### Proof sketch

1. (Lane A no-signaling, re-checked.) For every input `rho_psi`,
   `sum_a Tr_(A,R)(branch_a) = I/d` on `H_B`. The pre-message Bob
   marginal at `t_B` is independent of `rho_psi`. Equivalently, the
   marginal Bob state is `(1/d) I`, which is the maximally mixed state
   on Bob's encoded taste-qubit register.

2. (Lane B no-past-signaling, applied at `t_B -> t_C`.) Let
   `sigma_a = branch_a tensor (Bob's pre-message factor)`. Apply the
   later CPTP channel `S_x` to Bob's register only:
   `sigma_a^x = (I_(A,R) tensor S_x)(sigma_a)`. Because `S_x` is trace
   preserving, `Tr(sigma_a^x) = Tr(sigma_a) = P(a at t_A)`. Summing over
   the (unobserved) outcomes of any internal measurement inside `S_x`
   reduces to the same trace preservation.

3. (Composition.) Steps 1 and 2 are independent. Step 1 fixes the
   pre-message Bob marginal; step 2 fixes the invariance of the earlier
   record marginal under any later CPTP channel on Bob's register. The
   joint statement is the algebraic sum of the two.

This is the exact composition the lane-opening note posits in its
priority-order section as Lane B's protective effect on Lane A.
Stated in operational language: there is `no operational past-signaling channel from t_C to t_A` through Bob's register, even in the presence of a successful teleportation protocol at `t_B`.

## Joint runner properties (J1)-(J4)

The companion runner verifies four joint properties on an explicit
3-time circuit:

- (J1) Bob pre-message reduced state at `t_B` is `I/2` (Lane A
  no-signaling) for 14 input states (6 axis probes + 8 random).
- (J1b) The full teleportation channel `T(rho_psi)` delivers `rho_psi`
  exactly (fidelity 1) — i.e. the protocol is a real teleportation
  protocol, not a vacuous "Bob ignores everything" construction.
- (J2) Alice's record marginal `P(a at t_A)` is 1/4 uniform on the four
  Bell outcomes, and is invariant under each of six later settings at
  `t_C`: identity, Hadamard, dephasing, memory reset, Loschmidt echo,
  depolarizing.
- (J3) Bob's local state at `t_C` *does* respond to a choice of `x`
  (fairness control): applying `H` vs. `I` to the post-teleportation
  state `|+>` produces states with trace distance > 0.5, certifying
  that `S_x` is nontrivial and the no-signaling statement at `t_A` is
  not vacuous.
- (J4a) Conditional `P(a at t_A | x)` equals marginal `P(a at t_A)` for
  every input and every setting.
- (J4b) Positive control: a future postselection (project Bob onto
  `|0>` at `t_C` and condition on the projection) *does* bias the
  retrodicted record distribution; the bias exceeds the numerical
  threshold. This is the standard postselection / final-boundary
  exception explicitly excluded by Lane B's theorem; the bias is
  observed here to make explicit that the protection statement is
  doing real work, not a tautology of trace preservation.

## What this note does not close

This narrow composition theorem advances the Lane B protection claim
but **does not close the lane**. In particular:

- It does not close the lane-opening note. The note remains a
  planning/lane-opening record and is not promoted to a retained
  theorem-row or manuscript surface.
- It does not promote Lane C (signed gravity). The signed-gravity
  lane retains its prior verdict
  (`SIGNED_GRAVITY_ORIENTATION_LINE_NATURALLY_HOSTED_NOT_CANONICALLY_SELECTED`),
  unchanged.
- It does not derive Lane A's no-signaling result itself; it imports
  Lane A's existing no-signaling property as a hypothesis and verifies
  it on the joint circuit.
- It does not derive the retained single-clock surface itself; it
  imports the single-clock single-Hamiltonian framework property as a
  hypothesis.
- It does not address postselected, final-boundary, or directed-cycle
  theories. Those remain explicitly outside scope (the runner contains
  a positive-control showing that postselection can bias retrodictions,
  consistent with the Lane B theorem's stated exclusions).
- It does not address interacting CPT, advanced fields, or matter
  teleportation. Those remain broader framework work and are
  intentionally not load-bearing here.
- It does not change the package-level publication status or claim
  surface. There is **no main-surface promotion** of any retained
  theorem-row, prediction-row, or claim-row as a consequence of this
  note alone.

## Why this is a positive narrow theorem (not a definition)

- The lane-opening note posits the joint Lane B protective effect on
  Lane A as a priority-order rationale. It does not prove the
  composition.
- The two individual lane theorems (Lane A teleportation no-signaling,
  Lane B no-past-signaling) are each landed but were not composed in
  any single retained note prior to this block.
- The composition theorem is structurally clean (one-line algebraic
  composition of trace preservation), but the closure is positive in
  the sense that it makes the multi-time no-signaling envelope of the
  joint circuit explicit and runner-verified, including the
  nontriviality witness (J3) and the postselection control (J4b).

## Boundary phrases

The runner audits this note for the presence of the required boundary
statements listed in the "What this note does not close" section above
and for the absence of overclaim phrases (verbatim sensationalist
counterparts of the three lane names, and assertions promoting any of
the lanes by name). The forbidden phrases are not quoted here; their
exact strings are listed inline in the runner source.

## Distinct from prior blocks

This is block 18 of the 12-hour campaign and the first block on the
`frontier_extension` lane in the block series. Distinct from prior
blocks at the structural level (e.g. block 17 was a finite-box stripping
uniqueness lemma on the gauge-vacuum-plaquette parent; block 16 was a
factor-rigidity narrow theorem on `K_R`; blocks 14-15 were Ward / BC-
transfer narrow theorems). No prior block touched `frontier_extension`.

## Command

```bash
python3 -m py_compile scripts/frontier_extension_lane_b_protects_lane_a_joint_composition_narrow.py
python3 scripts/frontier_extension_lane_b_protects_lane_a_joint_composition_narrow.py
```

Both commands complete successfully with PASS > 0 and FAIL = 0.
