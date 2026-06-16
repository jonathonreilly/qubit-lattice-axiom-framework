# Record-Formation Pointer-Non-Demolition Dynamics Constraint (Bounded Theorem)

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
note characterizes a *feature of the time step* `U` / transfer matrix `T` that
forms a record.

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

1. **Corrected theorem boundary.** Additive + redundant + persistent +
   objective record formation forces pointer-non-demolition, but
   pointer-non-demolition alone is not sufficient to form a record. The closed
   finite theorem is:
   - if the dynamics forms a persistent objective record of the pointer for all
     allowed initial pointer populations, then `[H_int, Pi_S] = 0` is necessary;
   - the explicit local controlled-record coupling
     `H_int = g sigma_z(S) (x) sum_k sigma_x(E_k)` with `g > 0`, fresh
     fragments, and idle completed fragments is sufficient for a full redundant
     pointer record: every fragment carries `H_S`, redundancy is
     `R_delta = n`, the classical plateau is flat at `H_S`, all fragments agree
     on one pointer value, and completed fragments persist;
   - `[H_int, Pi_S] = 0` without a nontrivial system-to-fragment imprint is not
     record-sufficient: `H_int = 0` and system-only pointer rotations commute
     with `Pi_S` but write no environment record;
   - `[H_int, Pi_S] != 0` (control: handle `sigma_x(S)`) records the *wrong*
     (non-pointer) observable, collapses redundancy, makes the recorded value
     oscillate in time, and fails objective pointer consensus;
   - the interpolation
     `cos(theta) sigma_z(S) + sin(theta) sigma_x(S)` shows this particular
     controlled-record route degrades monotonically as `||[H_int, Pi_S]||`
     grows from zero, with a perfect record only at the zero-commutator
     endpoint.

2. **Necessity is exact, not just illustrative.** By the Heisenberg equation for
   the pointer populations `P_k` (the spectral projectors of `Pi_S`),
   `d<P_k>/dt|_{t=0} = i <[H_int, P_k]>`, the pointer populations are frozen for
   **all** states and **all** times **iff** `[H_int, Pi_S] = 0`. This is a
   statement about the *commutation property*, not the specific
   `sigma_z(S) (x) sum sigma_x(E_k)` operator: the runner certifies both
   directions over random Hamiltonians (60/60 preservation, 60/60 necessity).

3. **Forced dynamics class.** Record formation forces a transfer step `U` / `T`
   that (a) possesses a **conserved pointer/charge** `[U, Pi_S] = 0` (a preferred
   basis), (b) includes a **nontrivial record-forming imprint** from the pointer
   to fragments, and (c) is **local** in the sense that locality is what makes
   the fragments conditionally independent given the pointer (clean independent
   redundant copies). A pointer-preserving but **non-local** env-env coupling
   injects excess pairwise correlation `I(E_a:E_b) > H_S` and destroys the
   independent-copy structure. The framework's **number-conserving,
   reflection-positive OS transfer** `T = exp(-H)` with `[T, Q] = 0` (e.g. the
   gauge-invariant meson OS transfer) has the conserved-charge part of this
   class; this row does not claim that it has already derived a physical
   fragment-imprinting record channel.

This is **bounded** because the quantum-Darwinism identification of a *record*
(a redundant, objective, persistent imprint of a system observable) is a model
convention in this note. The Lattice, Quantum, and Record axioms supply the
qubits, the locality, and the *additivity* of the readout, but they do not by
themselves assert that a record is such an imprint. The constraint is forced
**given** that bridge.

## Load-Bearing Inputs

- [`MINIMAL_AXIOMS_2026-06-05.md`](MINIMAL_AXIOMS_2026-06-05.md) supplies the
  repo baseline Lattice + Quantum + Record language. The axiom baseline
  chain-satisfies as an approved premise; it is not a source of bounded status.
- The quantum-Darwinism reading of a *record* (recoverable pointer information,
  redundancy `R_delta`, classical plateau, persistence) and the choice of the
  explicit `S + E_1..E_n` carrier are explicit bounded inputs for this note.
- The Heisenberg-equation necessity argument (item 2) is an elementary,
  reproven-in-runner fact, not an import.

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
- It does not claim the pointer `Pi_S` is a second free input: einselection runs
  the other way (given `H_int`, the pointer is the observable `H_int`
  conserves), so item (3a) is self-consistency, not an extra supplied premise. But it
  does not derive *which* physical observable becomes the pointer from the
  axioms either.
- It does not claim that `[H_int, Pi_S] = 0` alone forms a redundant record.
  Nontrivial fragment imprinting and the fresh/idle fragment persistence
  condition are part of the sufficient construction.
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

1. the non-demolition coupling has `[H_int, Pi_S] = 0`, forms a full
   per-fragment record `H_S`, preserves the pointer populations, gives
   redundancy `R_delta = n` with a flat plateau, and persists (pointer frozen
   for all times; an idle finished fragment keeps its bit while later fragments
   record);
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
   counterexamples showing QND alone is not record-sufficient;
6. the forced class: `[U, Pi_S] = 0` for non-demolition (not for the control),
   a nontrivial fragment-imprinting channel for sufficiency, and locality for
   independent redundant copies; a non-local env-env coupling injects excess
   pairwise correlation `I(E_a:E_b) > H_S`; the framework's positive
   number-conserving OS transfer `T = exp(-H)` commutes with the conserved
   charge;
7. the coupling/magnitude/`beta` are not pinned (any `g > 0` works);
8. this source note keeps the dynamics, action, coupling, and `beta=6` claims
   out of scope.

Run:

```text
python3 scripts/frontier_record_formation_dynamics_constraint_2026_06_05.py
```

Expected result:

```text
SUMMARY: PASS=43 FAIL=0
```
