# Assumptions and Imports (block 01, 2026-07-12)

Registry check performed against `docs/audit/data/axiom_premise_nodes.json`
(canonical nodes: minimal_axioms current path MINIMAL_AXIOMS_2026-06-29.md;
approved primitives incl. kinetic_isotropy_primitive, scale_reference_primitive,
realized_state_primitive).

## Accepted foundation consumed
- Lattice axiom: sites = Z^3, distinguished by supplied lattice structure only.
- Admissibility axiom (exact text): "There is one fixed nearest-neighbor
  admissibility rule, covariant under lattice translations and proper cubic
  rotations. For each site, the available possibilities are determined by,
  and vary with, the nearest-neighbor conditions."
- kinetic_isotropy_primitive: one-tick form CONTEXT only (as in the target
  note); supplies no action/dynamics/selector.

## Retained/authority inputs (cited at their scopes)
- lattice_nn_light_cone_note: R-locality machinery — R = self-edges + NN
  edges; C_0(S)=S, C_{t+1}(S)=C_t(S) ∪ {v: ∃u∈C_t(S),(u,v)∈R}; theorem:
  R-local updates propagate differences only inside C_t(S). Consumed for its
  DEFINITIONS and theorem, at its "finite graph reachability only" scope
  (its own header retires relativity/spacetime readings — we consume none).
- qubit_lattice_joint_presentation_tensor_substrate_bridge (P1a/P1b
  registered packet, PR #5133 in review): multi-site possibilities live in
  the commuting joint presentation. If cited, cite at bounded scope,
  premises included.

## Candidate named premise (to derive or register)
- (P-FUND-1TICK): a fundamental multi-link admissibility term is one-tick
  evaluable at each constituent link — i.e. its availability, registered at
  constituent l, is a function of tick-t data on l's dependency set C_1(l).
  Block 01's hard residual: close from Record axiom one-tick record
  semantics + Admissibility per-site clause, or register explicitly.

## Forbidden
- No new axioms/primitives. No observational values. No literature imports
  (combinatorial content is self-contained; --literature not requested).

## Counterfactual pass (implicit choices surfaced)
1. Geometry: Z^3 fixed by axiom — no alternative.
2. R includes self-edges (light-cone note def) — counterfactual (no
   self-edges) would shrink C_1 to NN-only, excluding endpoints from their
   own domains; absurd for availability (a link's own state determines it);
   direction: none open.
3. Link carrier = unordered site pair (a,b) with a↔b symmetry — counterf.:
   directed links would halve the stabilizer, doubling covariant subdomain
   count; enumeration must use UNDIRECTED (gauge terms are orientation-summed
   in the parent note's plaquette usage).
4. "Loop" domain = rooted simple closed, no backtracking, lengths 4/6 (the
   note's tested domain) — the derivation targets the LICENSE for arbitrary
   finite link sets; enumeration checks stay at the note's domain.
5. Quantifier fork in lifting the per-site clause: single-value-projection
   (intersection) vs joint-evaluation (union) vs permissive-bound (C_1) —
   resolved: the license is a PERMISSIVE BOUND (may-depend-only-on), and
   one-tick reachability makes C_1 the unique such bound; see
   ROUTE_PORTFOLIO R2 and NO_GO_LEDGER R1.
