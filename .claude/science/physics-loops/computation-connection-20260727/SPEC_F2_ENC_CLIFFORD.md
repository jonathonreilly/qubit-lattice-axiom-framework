# Spec F2 — direct local encoded-input Clifford on the companion/center code

Runner: `scripts/frontier_cycle721_encoded_input_clifford_compiler_2026_07_28.py`
Cache:  `logs/runner-cache/frontier_cycle721_encoded_input_clifford_compiler_2026_07_28.txt`

## Claim being constructed (bounded, conditional on the Cycle-720 supplies)

A live even-CAR input presented on a dedicated input register bank at a
declared port cell is coupled into the companion/center code by a literal
bounded local Clifford word — no Bell measurement, no teleportation
corrections — such that:

1. the input bank carries the doubled image of one cell's even-CAR
   subalgebra in the same companion representation as the code (input-side
   M2 assignment is explicit and lives on the same site map, adjacent to
   the port cell);
2. an explicit Clifford intertwiner word V_port maps every input even-CAR
   generator (onsite parities, adjacent-Majorana pairs of the port cell)
   onto the corresponding encoded code generator, exactly, verified at
   tableau level for ALL generators (exhaustive) and on exact two-/
   three-mode sector matrices at machine residual;
3. V_port is compiled into one- and two-M2 primitives with nearest-neighbor
   routing and returned work; its total support is a fixed neighborhood of
   the port cell: support <= 2 cells, graph diameter <= 1 (same
   preregistered gate as F1) — the point of the route is that the companion
   representation removes any Jordan-Wigner cleanup growth, so measure and
   report the support census explicitly on every tested box;
4. after coupling, one application of the recurrent update word G acts on
   the encoded input exactly as the intended logical word (verify on the
   held small-box exact matrices; tableau-level on larger boxes);
5. sector discipline: the coupling preserves the fixed total-parity label
   and center signs; an unlawful odd input operator is refused/detected
   (control), not silently absorbed;
6. box ladder, covariance (24 x 576 x 8), deletion control (delete one
   primitive of V_port -> named nonzero residual/stabilizer mismatch),
   hostile-order control, and unchanged fixtures — all as in SPEC_F1.

## Honest boundary

- Same supplied inventory and prose boundaries as SPEC_F1 (no clock/time
  language; no matter/FTL/mass/charge transfer; state-level coupling only).
- The input bank's cleanliness and the port choice remain SUPPLIED; no
  autonomous input genesis is claimed.
- A PASS is an independent constructive escape of the raw-Bell diagnostic
  (Cycle-720 N1 route 4 moves UNTESTED/OPEN -> ATTEMPTED, constructive).
- A FAIL ships as a route-specific diagnostic (the exact compiled word and
  its measured support census) under N1-N8; it does not echo into any
  broader negative.

## Representation requirements

Same extraction sources and conventions as SPEC_F1. The intertwiner
construction should reuse the code's own encoding tableau (from the
mixed-gauge factorization V_s if exposed by the extracts) restricted to the
port cell, rather than inventing a new encoding.
