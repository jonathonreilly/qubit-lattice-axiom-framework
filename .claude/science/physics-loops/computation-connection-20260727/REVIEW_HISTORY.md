# Review history — block01 (Cycle 721)

## Supervisor review log

- Extraction pass: three worker extracts (Bell surface; site-map/recurrent;
  geometry/factorization) spot-verified against source line ranges before
  use (B:84-233 verified verbatim; adversary blocklist and cache mechanics
  read directly; landed even-CAR runner re-executed clean).
- F2 draft: two spec-level defects found by the worker's honest failures and
  fixed under supervisor edits + one sol-xhigh fix pass — (i) covariance
  must evaluate the transported port (lexicographic-minimum is a chart
  convention; demoted to an informational counter); (ii) the 3-CNOT-SWAP
  reversal control is palindromic (replaced by middle-CNOT flip +
  stray-primitive detection). Chart-family lesson: the 11-generator
  adjacent-pair basis is a JW path chart; covariant objects are dictionary
  families + fixture-derived seam orientation classes. Supervisor reviewed
  the full algebra core line-by-line (phase conventions re-derived
  independently) and the covariance rewrite. Final: 22/22 PASS, exit 0,
  supervisor-rerun verified.
- F1 draft: first draft honestly FAILED; diagnosed (i) dilation-direction
  spec error (H-CP-H fixes X_a, transports Z_a -> Z_a R — supervisor
  re-derived and corrected the spec), (ii) bare-JW input bank drags global
  strings (16 cells / diameter 7) — physics fix: companion-encoded bank,
  (iii) covariance chart-family objects, (iv) route-tuple semantics.
  Revision pass returned 9/10; the last failure (layer constancy) was a
  wrongly-posed check: supervisor re-posed it as the structural law
  measurement layers = 3 + maximum cell degree (Koenig bound) with interior
  saturation certified by adding the (4,4,4) box; correction layers
  constant at 11 from 3x2x2. Final: 10/10 PASS, exit 0, supervisor-rerun
  verified; core construction functions reviewed (consistency anchors:
  tag-rebuild equality + coarse-half/target binary equality).
- F3 + independent checker: see below when landed.

## Promotion Value Gate (V1-V5, written record)

The block proposes bounded_theorem status only (no retained-positive
movement), so the gate is answered for the PR record:

- V1 (specific obstruction closed): quoted from the Cycle-720 note's Open
  list — "a literal physical-M2 circuit for the input-side even-CAR Bell
  measurements; a collision-free composition of Choi preparation, Bell
  coupling, correction controller, and recurrent matter word on one literal
  site map" — and from its receipt boundary,
  `even_car_input_bell_measurement_physical_M2_compiled: false`. Routes 1
  and 3 retire exactly these two items at the bounded ceiling; Route 2
  moves N1 escape route 4 (direct encoded-input Clifford) from
  UNTESTED/OPEN to ATTEMPTED-constructive.
- V2 (new derivation + novelty search): the compiled dilation surface,
  the conflict-coloring law (3 + max cell degree with Koenig saturation),
  the port-local seam-coupling result, and the epoch liveness walk exist
  nowhere on origin/main. Prior-art sweep recorded in ROUTE_PORTFOLIO.md:
  commit 2f2f4878ca, searches S1-S8 with matched-hit classification — the
  only occurrences of "input-coupling circuit" / "encoded-input Clifford"
  on origin/main are the Cycle-720 note's own open/untested declarations.
- V3 (could the audit lane already do it from standard machinery?): no —
  the content is the literal construction on the companion code (site-map
  compilation, atlas one-hot duality, fixture-derived orientation classes),
  not a textbook identity; the audit lane has no compiled measurement
  surface for this code.
- V4 (non-trivial marginal content): yes — the compiled words flip a
  declared receipt flag under a preregistered support gate that the
  raw-mode route measurably fails (7 cells / diameter 4, Cycle 720), and
  the seam coupling collapsing to one cell is a structural discovery about
  the companion representation.
- V5 (one-step variant of a landed cycle?): no — closest prior work is
  Cycle 720 itself, which certified the Bell rows as CAR-domain operations
  but explicitly did not compile them ("naming the route is not an
  attempt"); Cycle 146/147's record machines compile Pauli measurement
  choices on a different code with no CAR/companion structure and no
  site-map composition (classified nonmatching in the sweep). origin/main
  re-checked at 2f2f4878ca.

## Review-loop disposition

Owner-operated lane (standing rule 2026-06-11): this block prepares the PR
and hands off; the review loop is not run from this session.
