# Block 158 — results (2026-09-26)

- **Runner.** `scripts/admissibility_rule_the_walker_on_the_members_lengths_needs_the_comparators_inversion_odd_curl_at_second_order_2026_09_26.py`: `TOTAL: PASS=16 FAIL=0` in about 25 s. Six mutations (four in families A–D, two in F), each failing in its own family only.
- **T1.** Through second order, with generic jets, for general and symmetric frames: comparator minus framed walk is `(1/8) ε·C` times the identity, with no vector part. For the lengths' frame, `ε·C` is 0 at first order and `2ε_abc η_ad ∂_b η_cd` at second.
- **T2.** On all 30 basis relabellings and all 1800 basis pairs:
  - at first order the moved walker is the new lengths' framed walk;
  - at order strain times relabelling it misses by `t = −(1/8)ε_abc(η_ad ∂_b S_cd + S_ad ∂_b η_cd)`, which equals the change of `(1/8)ε·C`;
  - `t` is nonzero on 48 basis pairs;
  - a stretched rod twisted about its axis gives `t = −λτ/4`.
- **T3.**
  - 7320 exact equations in 612 unknowns: rank 612, consistent. The unique solution is `B/8` times the identity.
  - A further coin rotation breaks the frame's symmetry, and a phase gives only a coin-vector term.
- **Reading.** Programme T's answer is the second outcome: consistency forces a connection-like term. That term is built from the lengths, needs no new field, is unique among one-derivative potentials, and is the comparator's. Together with block 157, the member's next order and the walker's second-order coupling are both the comparator's at leading order.
