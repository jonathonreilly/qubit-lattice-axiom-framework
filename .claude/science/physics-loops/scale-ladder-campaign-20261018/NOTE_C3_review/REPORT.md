# Review of the C3 lane note (lattice relabelling no-go)

Provenance: a fresh-context reviewer of the same model family. Saved by the supervisor from the hand-back.

**Verdict:** needs changes. The mathematics holds: Theorems A, B (the arc lemma) and C are correct as stated, the proof sketch is complete, and the runner gives PASS=103 in 80.6 s.

## Independent checks (`rev_indep_checks.py`, `rev_r3_rand.py`): all pass

| Check | What it shows |
|---|---|
| R1 | B4 sufficiency by an affine-matrix realisation, L = 3–9 |
| R2 | Necessity by sympy.solve at L = 5 and 6 |
| R3 | A1's y ≠ 1 claim holds for every y ≠ 1 (gcd argument) |
| R4 | C3 in 2D |

## Findings

**F1 (must fix).** Theorem B forbids the continuum spectrum (Λ2 = 2Λ1), not closure. B4 shows that closing algebras with (P2) and (S) exist. Four sentences said otherwise.

**F2 (must fix).** "Every local or summable discretisation fails on Z" is too broad.
- A summable D with a band-limited product kernel satisfies Theorem C's condition. Counterexample: λ = λ′ = i g(k), with a supported in |k1|, |k2|, |k1+k2| < π/3.
- Theorem A for summable transports holds without the density premise (the reviewer's argument; not in the note).

**F3 (minor).**
- Tighten the B3_Q_L5 test.
- Note that the π–π symbol is −λ(−k).

## Tests that cannot fail

- S1 is tautological given S0.
- B4's Λ check matches its construction by design.

## Conventions

All are OK. The spin-½ companion is listed as a source but is only motivation.

All edits were sent to the note writer. The same F1 wording in the campaign's C3 FINDINGS and in the scale-ladder note was fixed by the supervisor.
