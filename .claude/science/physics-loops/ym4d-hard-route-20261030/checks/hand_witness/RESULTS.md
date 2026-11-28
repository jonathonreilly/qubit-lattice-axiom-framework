# Kill tests for `library/witness-by-hand.md`: results

Run 2026-11-01 at `f3aa2a8c5`, single thread, one job under `lab_ops.py numeric-lock`, memory free 61 percent before and after. Output: `kill_tests.log`, `kill_tests.json`. Criteria: `CRITERIA.md`, written before the first run.

All 18 checks pass.

| Check | Tests | Worst value |
|---|---|---|
| W1a | V_p = triple sum (V1) | 9.8e-15 |
| W1b | cyclic shift and reversal | 3.6e-14 |
| W1c | plane formula (V2) | 2.8e-14 |
| W1d | Lemma 3.6, d = 4 | 6.7e-15 |
| W1e | control: sum of k only 0 mod 2 pi must break the form | median relative difference 1.14 |
| W2a | trigonometric lines (V3), (V4), same-index sum | 3.1e-15 |
| W2b | Ward identity (V5) | 2.5e-14 |
| W2c | (3.4) by brute colour contraction | 2.2e-13 |
| W3a | formula (R5) on exponentials | 6.6e-16 |
| W3b | (R8) | 4.2e-16 |
| W3c | (R9) | 4.8e-16 |
| W3d | shift form (R6), contact term invisible | 5.7e-8 |
| W3e | sign of (R3): time domain against Fourier | 4.8e-12 |
| W3f | control: Hankel form of exp(-k^2) is indefinite | lowest -0.83, top 7.2 |
| W4a | E chi^8 and the clip bound (O2) | 951.7 against 945; Delta / bound at most 0.032 |
| W4b | weights of (B-1) | exact |
| W4c | P_(n,S)(x, x) from (B-3) | 0.4999, 0.1886, 0.1638 at n = 1, 3, 5; all at most 1 |
| W5 | b(L) and L_1 on grids of log L | 0 violations |

**Correction before the first run.** The first draft of W3d added and subtracted a term c_0 a exp(-a), which was wrong: at a > 0 the contact term gives c_0 (psi * psi)(-a) = 0. W3d was rewritten to integrate the full D before anything ran, which also makes it a genuine test that c_0 stays invisible in (R5) and (R6). No criterion changed.

**Limits.** These sample formulas at random points. A pass finds no error and proves no bound, and no step of the note rests on them. W4c is a sample of regulators; the bound is the written one, (P*) in section 3.3 of the note.
