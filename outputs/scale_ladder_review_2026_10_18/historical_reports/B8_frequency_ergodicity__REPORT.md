# B8 report: frequency consistency from formation mixing (draft, unreviewed)

Provenance: a worker of the same model family. Saved by the supervisor from the hand-back. The runner gives PASS=17 FAIL=0 (runner_full.log). This rests on the B3 draft, which was independently checked with corrections (B3_check).

## The repo's obligation

Source: the 09-02 FINITE_ACTION_FUNCTIONAL... note, §8.

- **The frequency:** F_m over m trials sharing the same neighbour condition, preparation, instrument and cadence.
- **Why it is open:** the note's six premises do not force consistent frequencies.
- **The counterexample:** X_i = B for all i, with B ~ Bernoulli(1/4).
  - It is stationary but **not ergodic**: a mixture of two ergodic laws, with covariances that are not summable.
  - The note concedes that ergodicity would suffice.

## Theorems

Setting: B3 class, empty start, covariant rule, Z³.

- **Lemma 0.** χ = Σ|Cov| is finite. The rigorous bound is ≤ 4069 for a single site; measured values are 0.14–1.7.
- **Theorem A.** For any deterministic sequence of distinct sites, E F_n = p and Var F_n ≤ χ/n.
  - With pairwise separation s, the bound becomes (p(1−p) + τ(s))/n, with τ(s) decaying factorially.
  - F_n → p almost surely.
- **Theorem B.** P(|F_n − p| ≥ ε) ≤ 3exp(−nε²/(8k_m)), using an m-local truncation and Janson's inequality.
- **Theorem C.** Conditional frequencies given a context of positive probability converge to P(E|C), almost surely and in L^r.

## The limits

- **Order-blind positive rules:** the limits equal the rule weights r(a|η).
- **Order-sensitive rules:** the limits are generally not the rule weights. For ferro, freq = 0.5125 against the weight 0.8. The weights are recovered given the formation-time context (0.804), which Records alone do not reveal.

## Not obtained

- Born weights.
- Repeated readouts of one Record.
- Independence: it is moved onto the supplied clocks, marks, empty start and a single rule, not removed. A rule drawn once at random gives a non-ergodic mixture (runner check R1).
- Adaptive selection of the sampled sites.

## Disclosure

One weak check was removed after the quick run and before the full run.
