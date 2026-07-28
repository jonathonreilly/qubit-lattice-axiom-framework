# Wavefront DOWN/ACK action-request controller compiled to literal M2

Date: 2026-07-28

Authority: none

Audit: unset

Status: bounded conditional construction

Claim type: bounded_theorem

Primary runner:

- [`frontier_cycle726_wavefront_controller_m2_compiler_2026_07_28.py`](../scripts/frontier_cycle726_wavefront_controller_m2_compiler_2026_07_28.py)

Independent check:

- [`frontier_cycle726_wavefront_independent_check_2026_07_28.py`](../scripts/frontier_cycle726_wavefront_independent_check_2026_07_28.py)

Load-bearing landed surface:

- [physical-M2 spatial ACK and interval bridge](PHYSICAL_M2_SPATIAL_ACK_CYCLE612_INTERVAL_BRIDGE_CYCLE718_BOUNDED_THEOREM_NOTE_2026-07-26.md)
  supplies the existing physical commit, shield, decoded, shift, relay,
  handoff, return, and cleanup words reused here.

Constitutional effect: none. This package changes no axiom, foundation,
Qualification, primitive, registry, policy, queue, audit result, or audit
status.

All phases, stations, and application counts are circuit structure. None is
called physical time, duration, rate, or energy.

## Question

Given a supplied finite path, a supplied local transition table, clean
controller resources, and the landed physical macro words, can the table's
DOWN/ACK phase transfer and macro-request decisions be emitted as one fixed
literal reversible gate tuple rather than evaluated by runtime Python control
flow inside the request controller?

## Result

Yes, for the action-request controller alone.

The supplied convention uses two-bit IDLE/DOWN/ACK phase rails with one-hot
ownership, a 19-row priority table, source-DOWN genesis, boundary DOWN-to-ACK
conversion, and phase-gated local shift requests. The compiler emits a fixed
reversible word that evaluates those predicates, transfers the phase owner,
and toggles the declared macro-request ports:

- length 13: 27,695 literal controller gates and 271,071 expanded M2
  primitives;
- length 17: 36,883 literal controller gates and 361,123 expanded M2
  primitives;
- every declared table row has the expected request-port and phase-owner
  image on both fixtures; IDLE, local phase code `11`, and a nonmatching
  address remain fixed under the tested row stage;
- 19/19 rows are exercised, with four recorded hits per row across the two
  lawful-row and two identity fixtures;
- latch-compute, enable-Fredkin, and phase-update gate deletions are all
  detected;
- exactly one DOWN-or-ACK owner remains at every stage boundary on the
  declared full-path fixture, with no early cleanup request and no shift or
  commit request before the DOWN phase;
- the request word is exactly reversible on arbitrary bit assignments, and
  clean selectors, enable latches, and controller work return clean.

The emitted request word contains no runtime state executor, dynamic source
scan, state-dependent application loop, or runtime edge-order selection.
Python is used as a finite unrolling compiler for the supplied topology and
table.

## Separate gating lemmas

The runner also checks two reusable gadgets separately from the request word:

- X/CNOT/Toffoli macro words admit the extra-control lift used by the existing
  classical macro families;
- the H/T-bearing decoded word admits enable-latched Fredkin spectator
  rerouting. When enabled, the data experience the decoded word and the clean
  spectators return. When disabled, the data are unchanged while the decoded
  word acts on the supplied spectator bank, which returns to its clean state.
  No direct controlled-unitary decomposition is introduced.

The independent checker reads the primary source only as AST data. It
reconstructs the supplied table, replays all 19 transition rows, checks the
request sequence and one-hot ownership, verifies the latch sandwich, and
checks the Fredkin wrapper on 1,216 dense basis/operator cases. It also
confirms that the emitted request-controller path contains only static
unrolling logic.

## Integration boundary

This package does not yet connect the action-request ports to executions of
the physical shield, decoded, commit, relay, shift, return, or cleanup words.
The macro-control lifts and spectator wrapper are verified as separate
gadgets, and the existing landed words are rerun unchanged, but no single
controller-plus-macros executable word is constructed or routed here.

Accordingly, the separate component counts are inventories, not summands of a
composed gate word. End-to-end equivalence to a controller-driven physical
execution and removal of all runtime host selection remain open.

## Supplied / derived / open

### Supplied

- the phase encoding, priority table, genesis/boundary convention,
  phase-gated shift convention, spectator bank, and structural bank-index
  ROM;
- clean controller ancillas, latches, spectators, and DOWN/ACK rails;
- every supply declared by the linked landed spatial-ACK surface, including
  decoder/source words, law/admission bits, clean banks and link tubes, a
  one-hot allocator token, fixed edge order, and finite topology.

### Derived

- one fixed literal routed M2 action-request word for the supplied table;
- exact row-stage semantics, table coverage, active gate-deletion witnesses,
  ownership conservation, and exact inverse with clean controller work;
- absence of runtime semantic branching inside the emitted request word;
- separate classical extra-control and decoded-word spectator-rerouting
  gadgets;
- unchanged reruns of the landed spatial-ACK certificates and a standalone
  placement/routing/covariance check for the request-controller layout.

### Open

- wiring each request port to the corresponding gated physical macro and
  constructing one integrated executable word;
- end-to-end equivalence between that future integrated word and the intended
  supplied transition semantics;
- derivation of the transition law itself;
- autonomous preparation of the phase rails, latches, spectators, and
  wavefront genesis;
- renewal, fault repair, boundary-free geometry, and the inherited open items
  at their original scope;
- physical time or rate, permanent Record, Born, and source content.

## Negative-claim boundary

The only negative structural statement proved here is scoped to the emitted
request-controller tuple: it contains no runtime state branch, source scan,
state-dependent application loop, or edge-order selection. This does not
extend to the absent controller-driven macro composition. Deletion witnesses
are sensitivity checks, not no-go results.

## Verdict

The supplied DOWN/ACK table has a literal reversible M2 action-request
compiler with exact phase-transfer semantics and separately checked macro
gating gadgets. Full physical macro integration and end-to-end runtime-host
removal remain open.
