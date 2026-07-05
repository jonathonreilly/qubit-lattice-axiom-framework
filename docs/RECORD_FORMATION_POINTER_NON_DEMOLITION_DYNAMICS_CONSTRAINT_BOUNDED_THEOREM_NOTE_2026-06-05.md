# Record-Formation Pointer-Conservation and Controlled-Copy Constraint (Bounded Theorem)

> **Key terms used in this doc** are indexed A-Z at
> [docs/KEY_TERMINOLOGY.md](KEY_TERMINOLOGY.md); each row points to the
> canonical source-of-truth doc.

**Date:** 2026-06-05
**Type:** bounded theorem
**Claim type:** bounded_theorem
**Status:** source note awaiting independent audit handling.
**Primary runner:**
[`scripts/frontier_record_formation_dynamics_constraint_2026_06_05.py`](../scripts/frontier_record_formation_dynamics_constraint_2026_06_05.py)
**Cached log:**
[`logs/runner-cache/frontier_record_formation_dynamics_constraint_2026_06_05.txt`](../logs/runner-cache/frontier_record_formation_dynamics_constraint_2026_06_05.txt)

This is the **temporal/formation** companion to the timeless gauge-structure
boundary in
[`TWO_ENDPOINT_GAUSS_LAW_INVARIANCE_PROFILE_BOUNDED_THEOREM_NOTE_2026-06-05.md`](TWO_ENDPOINT_GAUSS_LAW_INVARIANCE_PROFILE_BOUNDED_THEOREM_NOTE_2026-06-05.md):
that note characterizes the gauge-invariant *algebra* at a fixed time; this
note characterizes the pointer-conservation condition and the additional
controlled-copy hypotheses under which a finite time step `U` forms a record.

## Claim

Condition on the following explicit finite model:

- a system qubit `S` (site 0) with pointer observable `Pi_S = sigma_z(S)`;
- `n` environment qubits `E_1..E_n` (the local neighbourhood of `S`), each
  initialized in `|0>`; the system initialized in a generic off-axis Bloch
  state (nonzero `x`, `y`, `z` components, so the pointer entropy `H(Pi_S)` is
  a nontrivial record and a pointer-rotating coupling genuinely scrambles it);
- a local interaction Hamiltonian `H_int` and the step `U = exp(-i H_int t)`;
- the quantum-Darwinism reading of a *record*: a record of `S` in a fragment
  `F` is the recoverable `Pi_S`-information of `S` from `F`, computed as the
  system<->fragment mutual information after dephasing `S` in the pointer
  basis (the Holevo content of the pointer ensemble). The record is **additive**
  over disjoint fragments (Record axiom), **redundant/objective** when many
  disjoint fragments each certify the same pointer value (Darwinism plateau /
  redundancy `R_delta`), and **persistent** when stable under further `U` steps.

In that model the following hold.

1. **Pointer conservation is exact.** By the Heisenberg equation for
   the pointer populations `P_k` (the spectral projectors of `Pi_S`),
   `d<P_k>/dt|_{t=0} = i <[H_int, P_k]>`, the pointer populations are frozen for
   **all** states and **all** times **iff** `[H_int, Pi_S] = 0`. This is a
   statement about the *commutation property*, not the specific
   `sigma_z(S) (x) sum sigma_x(E_k)` operator: the runner certifies both
   directions over random Hamiltonians (60/60 sufficiency for pointer
   conservation, 60/60 necessity for pointer-motion witnesses). This is not a
   record-formation theorem: a commuting Hamiltonian can preserve the pointer
   while writing no fragment.

2. **A nonzero local controlled-copy coupling is sufficient for record
   formation.** For the explicit finite local Hamiltonian
   `H_int = g sigma_z(S) (x) sum_k sigma_x(E_k)` with `g > 0`, the recording
   time `t = pi/(4g)` gives each fragment the full pointer record `H_S`,
   redundancy `R_delta = n`, a flat classical plateau at `H_S`, and objective
   fragment agreement. In the fresh-fragment measurement-chain version, a
   finished idle fragment keeps its record while later fragments record.

   The converse is **not** claimed. `[H_int, Pi_S] = 0` alone preserves pointer
   populations, but it does not imply that any fragment is written: `H_int = 0`,
   an environment-blind commuting Hamiltonian, or a nonzero commuting
   `sigma_z(S) sigma_z(E_1)` interaction with `E_1` initialized in a
   `sigma_z` eigenstate is pointer-non-demolishing and forms no redundant
   record. A coherent controlled-copy kick also is not persistent if the same
   completed fragment is re-used: the runner shows that a second identical
   kick can erase the record. The sufficiency result therefore includes the
   nonzero controlled-copy form, the recording time, and the fresh-fragment,
   idle-completed-fragment, or decoupling hypotheses.

3. **Demolition and locality controls.** A pointer-demolition control with
   handle `sigma_x(S)` fails to carry the `Pi_S` record, collapses redundancy,
   makes the pointer populations oscillate, and reaches no objective pointer
   consensus. Local finite-range controlled-copy couplings give conditionally
   independent redundant fragments; a pointer-preserving but **non-local**
   env-env coupling injects excess pairwise correlation
   `I(E_a:E_b) > H_S` and destroys the independent-copy structure.

4. **Transfer-class consequence.** Any downstream transfer step that has been
   independently established to possess a conserved charge/pointer, for
   example a number-conserving reflection-positive OS transfer `T = exp(-H)`
   with `[T, Q] = 0`, lies in the pointer-conserving class. This row verifies
   the finite algebraic membership condition in the runner; it does not cite or
   prove that a physical framework OS transfer has the nontrivial
   fragment-imprinting channel needed to form redundant records.

This is **bounded** because the quantum-Darwinism identification of a *record*
(a redundant, objective, persistent imprint of a system observable) is a model
convention in this note. The Lattice, Quantum, and Record axioms supply the
qubits, the locality, and the *additivity* of the readout, but they do not by
themselves assert that a record is such an imprint or that every
pointer-conserving Hamiltonian writes fragments. The constraint is forced
**given** that bridge and the explicit controlled-copy hypotheses.

## Load-Bearing Inputs

- [`MINIMAL_AXIOMS_2026-06-05.md`](MINIMAL_AXIOMS_2026-06-05.md) supplies the
  repo baseline Lattice + Quantum + Record language. The axiom baseline
  chain-satisfies as an approved premise; it is not a source of bounded status.
- The quantum-Darwinism reading of a *record* (recoverable pointer information,
  redundancy `R_delta`, classical plateau, persistence) and the choice of the
  explicit `S + E_1..E_n` carrier are explicit bounded inputs for this note.
- The Heisenberg-equation pointer-conservation argument (item 1) is an
  elementary reproven-in-runner fact, not an import.
- The nonzero controlled-copy interaction, the recording time
  `t = pi/(4g)`, and the fresh-fragment, idle-completed-fragment, or
  decoupling persistence condition are explicit sufficient-construction
  hypotheses, not consequences of `[H_int, Pi_S] = 0` alone.

## What This Does Not Claim

- It does not derive a dynamics, an action, gauge bosons, coupling values, beta
  functions, electroweak symmetry breaking, or color SU(3). It constrains only
  a structural FORM of `U` / `T` (conserved pointer + nontrivial fragment
  imprinting + locality).
- It does not pin the coupling strength or the transfer-matrix magnitude: any
  `g > 0` forms an equally good record at the rescaled time `t = pi/(4g)`. In
  particular it says **nothing** about `beta = 6`.
- It does not derive the quantum-Darwinism bridge (record = redundant objective
  imprint of a system observable) from Lattice + Quantum + Record; that bridge
  is the supplied bounded model input.
- It does not claim that arbitrary pointer-non-demolition dynamics form
  records. Pointer non-demolition is necessary for all-state pointer
  persistence, but record formation also needs a nonzero record channel and the
  stated fragment/persistence hypotheses.
- It does not claim the pointer `Pi_S` is a second free input: einselection runs
  the other way (given `H_int`, the pointer is the observable `H_int`
  conserves), so the transfer-class constraint is self-consistency, not an
  extra supplied premise. But it does not derive *which* physical observable
  becomes the pointer from the axioms either.
- It does not claim that `[H_int, Pi_S] = 0` alone forms a redundant record.
  Nontrivial fragment imprinting and the fresh/idle fragment persistence
  condition are part of the sufficient construction.
- It does not use OS-transfer membership as a record-formation proof. A
  conserved-charge OS transfer is only in the pointer-conserving class; a
  physical record channel still has to be supplied or proved separately.
- It does not establish the lattice/continuum or interacting-field
  generalization; the theorem is on the explicit finite model.
- It does not identify the gauge-invariant algebra of the companion timeless
  note with physical observables, nor does it enlarge that result.

The safe downstream use is only the bounded finite-model statement: under the
stated quantum-Darwinism record conventions, persistent objective pointer
record formation requires pointer-non-demolition `[H_int, Pi_S] = 0`, while
the displayed local controlled-record coupling with fresh/idle fragments is a
sufficient finite construction. A conserved pointer/charge is therefore a
necessary transfer-step feature, but a physical fragment-imprinting channel
remains an additional bounded model requirement.

## Beyond the Timeless Gauge-Structure Boundary

The companion timeless note fixes which *algebra* is observable
(gauge-invariant) at a fixed time. This note adds a *temporal/formation* layer:
it fixes a *feature of the time step* `U` / `T` that builds the record -- the
existence of a conserved pointer, a nontrivial fragment imprint, and locality.
It is the dynamical sibling of the structural corollary, obtained from the same
Record axiom by passing from the timeless additivity to its quantum-Darwinism
(redundant-imprint) realization.

## Runner Certificate

The runner verifies, on the explicit `S + E_1..E_4` model (numpy, exact dense
operators, peak RSS ~36 MB):

1. the explicit nonzero local controlled-copy coupling has
   `[H_int, Pi_S] = 0`, forms a full per-fragment record `H_S`, preserves the
   pointer populations, gives redundancy `R_delta = n` with a flat plateau, and
   persists in the fresh-fragment/idle-finished-fragment chain while
   same-fragment coherent re-use can erase the record;
2. the Record-axiom additivity holds and is *consistent* (the recovered pointer
   information saturates at `H_S`, no super-additivity) with all fragments
   objectively agreeing on one value;
3. the demolition control `[H_int, Pi_S] != 0` records the wrong observable,
   collapses the redundancy, oscillates the recorded value, and reaches no
   objective consensus;
4. the interpolation sweep: objective-record quality is maximal and perfect
   only at the zero-commutator point and decreases monotonically as
   `||[H_int, Pi_S]||` grows;
5. pointer-population preservation and necessity over random Hamiltonians via
   the Heisenberg equation (60/60 each), plus explicit commuting non-recording
   counterexamples (`H_int = 0`, system-only phase, and a nonzero
   `sigma_z(S) sigma_z(E_1)` interaction with `E_1` in an eigenstate) showing
   QND alone is not record-sufficient;
6. the forced class: `[U, Pi_S] = 0` for non-demolition (not for the control),
   a nontrivial fragment-imprinting channel for sufficiency, and locality for
   independent redundant copies; a non-local env-env coupling injects excess
   pairwise correlation `I(E_a:E_b) > H_S`; a supplied positive
   number-conserving OS-style transfer block `T = exp(-H)` commutes with the
   conserved charge, which is a transfer-class membership check rather than a
   record-formation proof;
7. the coupling/magnitude/`beta` are not pinned (any `g > 0` works);
8. this source note keeps the dynamics, action, coupling, and `beta=6` claims
   out of scope.

Run:

```text
python3 scripts/frontier_record_formation_dynamics_constraint_2026_06_05.py
```

Expected result:

```text
SUMMARY: PASS=46 FAIL=0
```
