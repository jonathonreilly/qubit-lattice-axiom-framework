# Block 105 — results (2026-09-23)

- **Runner.** `scripts/admissibility_rule_in_discrete_ticks_a_local_clock_is_exact_only_for_walks_that_do_not_move_2026_09_23.py`: `TOTAL: PASS=11 FAIL=0` (~1.4 s). Six mutations, each failing in its own family.
- **T1.** The partial-swap walk:
  - is unitary with range 2 for every clock field;
  - equals two coined ticks at θ = π/2 − ε, so U = V² with V of range 1;
  - has block 54's walk as its first order.
- **T2.**
  - sin(ω/2) = sin ε |cos k|.
  - ω = 2ε|cos k|(1 − (ε²/6)sin²k): a clock to relative ε².
  - The rays obey block 54's law plus O(ε⁴), with Ψ in closed form.
- **T3.** tr U(2ε)/2 − cos 2ω(ε) = 2 sin⁴ε sin²2k. U[w]² reaches four sites; U[2w] reaches two.
- **T4 (flat-band theorem).**
  - Finite-range powers, or exact clock scaling, force flat bands and no transport.
  - A local, covariant, continuous tick rule that keeps the discrete clock identity has flat bands.
  - The theorem is sharp: cos c − i sin c H.
- **Control.** A packet moves 326.59 sites in 400 ticks. The discrete rays give 326.80 (off 0.21); block 54's law gives 324.47 (off 2.12).
