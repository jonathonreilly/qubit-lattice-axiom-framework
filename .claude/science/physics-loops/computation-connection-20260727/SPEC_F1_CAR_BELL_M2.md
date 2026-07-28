# Spec F1 — literal M2 compilation of the even-CAR Bell input rows

Runner: `scripts/frontier_cycle721_car_bell_input_m2_compiler_2026_07_28.py`
Cache:  `logs/runner-cache/frontier_cycle721_car_bell_input_m2_compiler_2026_07_28.txt`

## Claim being constructed (bounded, conditional on the Cycle-720 supplies)

On the declared companion subsystem code, every row of the doubled even-CAR
Bell measurement family (onsite parities, onsite adjacent-Majorana pairs, one
oriented nearest-neighbor seam row per edge) is compiled into a literal
physical-M2 measurement word on the same site map as the prepared Choi
resource and the recurrent update, such that:

1. each compiled word = (route-in; ancilla-controlled character word;
   basis rotation; route-return), decomposed into one- and two-M2 primitives
   with nearest-neighbor routing and returned routing work;
2. the measurement outcome lands in a dedicated retained syndrome M2 —
   no reset, no postselection, no dissipative erasure;
3. the physical correction generators remain the Cycle-720 one-cell private
   duals: compiled correction support <= 2 cells and graph diameter <= 1
   (the preregistered gate), measured over EVERY row on every tested box;
4. measurement words that share support are scheduled in explicit conflict
   layers; report the layer count against the Cycle-720 counts
   (4 measurement layers, <= 11 correction layers) honestly;
5. exactness: on exact small sector matrices (two- and three-mode families,
   as in Cycle 720), the compiled word implements the intended character
   measurement instrument exactly (residual at machine scale); on full
   boxes, tableau-level verification over the whole doubled row family
   (exhaustive over rows — no sampling);
6. box ladder: 2x2x2 and 3x2x2 fully; held non-collinear 5x3x2; larger
   boxes only as reuse controls if runtime allows;
7. signed covariance: the compiled words, schedules, ancilla assignments,
   and routes transport under all 24 proper-cubic frames, 576 ordered
   products, and the eight coframe-origin sectors with zero
   tableau/stabilizer/schedule-key/returned-route failures;
8. controls: (a) deleting one private dual leaves unit sign residual;
   (b) hostile reordering of a conflict layer produces a nonzero named
   residual; (c) an unlawful odd character is detected and refused;
   (d) fixtures free/seam/reverse/contact/FSWAP/mass rerun unchanged.

## Honest boundary (print in the runner header and cache)

- All ordinals are circuit structure; nothing is a clock/time/rate/energy.
- Fixed parity/center sector, mixed gauge reference, coframe sector, finite
  box/root/router, clean ancilla banks, and one-time epoch remain SUPPLIED.
- This is state-level input coupling on the declared code; no matter/FTL/
  mass/charge transfer claim (harness-index HOLD honored).
- A PASS here is the "literal physical-M2 circuit for the input-side
  even-CAR Bell measurements" leg only; autonomy/genesis/sector-law remain
  open.

## Representation requirements (fill from EXTRACT_BELL_SURFACE.md and
EXTRACT_SITEMAP_RECURRENT.md; reuse conventions verbatim)

- fixture/site-map constructor, register indexing, companion representation;
- Pauli row encoding (integer bitmasks), symplectic form, sign bookkeeping;
- atlas key format and lookup; conflict-layer coloring function;
- routing word builder + route-return + distance census;
- covariance harness enumeration and comparison points;
- print/cache line conventions and receipt field production.

## Failure honesty

If any row on any tested box exceeds the support/diameter gate, the runner
prints the exact census (per-row support cells, diameter, box) and the
overall named check FAILS; the note then ships that leg as a route-specific
diagnostic under N1-N8 with the frozen route named. No silent narrowing.
