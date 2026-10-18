# Review history — toe-scale-ladder-20261018

| Block | Author run | Independent check | Findings | Disposition |
|---|---|---|---|---|
| C2 | PASS=49 FAIL=0 | different derivation (Coulomb gauge, exact angular integrals), PASS=35 FAIL=0 | 10 non-blocking (scope/wording; T_tie proper-rotation invariant count) | all applied; reviewer confirmed: ready |
| C3 | PASS=59 FAIL=0 | forward-time simulation + exact enumeration, PASS=75 FAIL=0 | F1 wording false (tie-exchangeable counterexample W-tie), F2-F8 wording/scope; 3 editorial nits at confirmation | all applied; reviewer confirmed: ready; nits applied |
| C6 | PASS=21 FAIL=0 | own GF(2)/Pauli code, PASS=16 FAIL=0 | BHM wording recalled (no network); TQO-2 implication wording; uniform-in-L scope; no-go scope (tori, J0, qubit-local); R5 distance unverified; new general-L FF theorem (F1-F4) confirmed | all applied; reviewer: ready for F1-F4, F5 conditional |
| C7 | PASS=107 FAIL=0 | own sympy series + numpy/mpmath walk build, PASS=55 FAIL=0 | Lemma V TRIM condition; Theorem C C3/κ0/item-5 wording; parent runner 8/45->4/45 defect confirmed | corrections + parent repair in progress |
| C4 | all logs TOTAL lines (3 intentional FAIL = falsified predictions) | independent F2 + Pauli brute-force code, all FAIL=0; NOT blind to headline counts (orchestrator prompt leaked them) — independence of implementation only | Theorem 2(d) general-H glider exclusion (minor); subgroup/twist/58-hom sweep not re-checked; sign-action phase-valid spreading count 84->14 | all applied; reviewer: ready |
