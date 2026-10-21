# Historical submitted evidence and bibliographic assertions

Preserved for retrieval only; no fresh execution or independent theorem validation is implied. The corrected live argument is in the sibling mathematical file.

## 6. Runner evidence (finite Monte Carlo, not proof)

Command: `python3 runner_frequency_consistency.py` (seed 20261018). Log: `runner_full.log`. Result: **TOTAL PASS=17 FAIL=0** in 62 s. The simulation code is adapted, read-only, from the B3 runner, and the formation loop is rewritten to pass neighbour directions and record formation-time masks.

- **X.**
  - Exact repo counterexample numbers: 3/16 against 3/64, and non-summable covariance.
  - Rigorous χ ≤ 4069.
  - Theorem B parameters.
- **O. Chiral-pair order-blind rule**, 300 tori with L = 24. The expected constants come from the 2026-10-16 product formula and are computed separately from the simulation.
  - Class frequencies equal 1/12 within |z| ≤ 1.3.
  - Conditional frequencies given one or two neighbour Records match r(a|η) ∈ {1/8, 1/24, 1/12} within |z| ≤ 1.3.
  - n·Var of box means of h = X_{+x} + X_{−x} equals the exact 1/3 + (l−1)/(36l) for l = 1, 2, 4, 8, 11, within |z| ≤ 1.4. The replicas are exactly independent by 1-dependence.
  - Along a fixed scrambled sequence of distinct sites, chosen before any field was drawn, n·Var F_n matches the exact set-dependent prediction 1/3 + 2·#bonds/(72n) at n = 50, 500, 5000 and 13824.
- **F. Ferro (20,1,1)**, order-sensitive, 120 tori with L = 32.
  - Label frequency 1/6 (z = 0.17).
  - n·Var(F_l) rises from 0.139 to 1.40 by l = 12 and stays at or below χ̂ = 1.70. It matches Σ_z C(z)·(overlap weight). This is a same-data identity, a consistency check rather than an independent one.
  - Checks F3 and F4 as in §4(ii).
- **C. Copy-unanimous** (has zeros, order-sensitive): frequency 1/6 and the same two variance checks.
- **R. Rule mixture:** non-concentration, as in §5.3.

**Disclosure.** A plateau check (n·Var at the two largest l agreeing within 4 SE) was in the first version. It was removed after the quick run, before the full run, because it is not a valid test of O(1/n) scaling: finite-size growth toward χ is expected. The check counts above exclude it. No threshold was changed after the full run.

## 7. Prior art and contribution

**Standard.** The following are textbook results:

- Chebyshev's bound and the strong law for bounded variables with summable covariances (the subsequence argument);
- Hoeffding's inequality for dependency-graph sums (Janson, Random Structures Algorithms 24, 2004; recalled, not re-checked);
- the ergodic decomposition and the multidimensional ergodic theorem;
- for a factor of an iid process on an amenable group, Bernoullicity (Ornstein–Weiss); this is recalled and not used.

**New here (packaging).**

- The exact frequency obligation of the 2026-09-02 note is located, and its counterexample classified as non-ergodic and non-summable.
- The obligation is discharged for the B3 formation class, along arbitrary distinct-site sequences and with explicit Z³ constants.
- Separated sampling is shown to reproduce the IID variance.
- The limits are identified: rule weights for the order-blind class; not rule weights for order-sensitive rules given Record contexts (a witness is given); rule weights given the formation-time context.
- One-Record repetition is shown to be precisely the repo's counterexample.

## 8. No-Go discipline

Only one negative statement is made: that one-Record repetition and non-ergodic mixtures fail. It is shown by exact example, not by an impossibility theorem. Nothing is claimed about the framework outside the stated class. All premises are named in §2 and §5.3.
