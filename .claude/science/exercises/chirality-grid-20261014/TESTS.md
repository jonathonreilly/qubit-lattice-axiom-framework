# Step 8 tests: index

Every test was pre-registered in its folder's `PREREG.md` before it ran. Results are as reported; referee status is noted.

| Test | Folder | Reading | Referee |
|---|---|---|---|
| F1 C1 (mod-16 table), C2 (GS reduced locator) | routes/F1 | COUNT-16 met; signatures located | — |
| F2 T1, T3b/c, T4b, T5b | routes/F2 | PASS (T4 FAIL: mis-built) | codex: confirmed (T3 defect norm ~2×) |
| F3 R1 / R1-F1 / R1-F2 / R2 | routes/F3 | R1 FAIL (tolerance); R1-F1, R1-F2, R2 PASS | — |
| F4 T-F4-1..4b | routes/F4 | lemma-consistent; price-prohibitive; T-F4-3 PASS (free); inverse-L | — |
| F5 T1, T2/T2b, T3a, T3′ | routes/F5 | T1/T3a not met; T2 PASS; T3′ FAIL | — |
| F6 tA–tD | routes/F6 | all PASS | — |
| X1 DI-Z8 | combos/X1 | CHAIN-CONSISTENT (instrument) | — |
| X2 T1–T5 | combos/X2 | PASS (structural) | — |
| X3 T-X3, T-X3b–f | combos/X3 | T-X3 PASS; gauged tests inconclusive | via K2 |
| K1 A1–A4, A3′, B1–B4 | kills/K1 | anomaly kill failed (all classes vanish); GPR mean-field upheld | — |
| K2 T1 (+V1–V6), T3 | kills/K2 | free X3-A survives; Fejér-measure open-time RP FAIL | codex: confirmed with corrections (Fejér scope; hard measure positive) |
| K2b T1, T2, V1–V5 | kills/K2b | torus PASS-at-power (Fejér); PV-DWF and Shamir negative (Fejér) | — (scope as K2) |
| K3 T1, T1F | kills/K3 | KILL-(b)-READING; NET-GAIN | — |
| K2c (hard-support RP) | kills/K2c | **running** | — |

**Update (18:36Z).** K2c finished. Under X3's hard measure, the as-registered searches are PASS-at-power, which turned out to be masking. The V2 W-matched follow-up gives a **FAIL on open time and the torus** (same-family; codex referee running).

**K2c referee (20:40Z):** CONFIRMED WITH CORRECTIONS. Non-RP of the hard-support overlap measure holds in the finite 2D U(1) proxy, including the tori. Wording correction: "certified" becomes "quadrature-converged".

## Next set of tests (pre-registered 2026-10-14 ~20:48Z, at Jon's request: "run the next set of tests")

Memory: ≤ 0.4 GB per run for NT-1 and NT-2, ≤ 1 GB for NT-3, one process at a time per agent. Each agent writes its detailed PREREG.md before running. The readings below are fixed now.

**NT-1. Chiral-measure RP (route 1, set B).** Does gauged reflection positivity also fail for a genuinely chiral, anomaly-free 2D U(1) overlap measure? Use Weyl projections with a charge set such as 3-4-5-0, or 1⁴(−1)⁴ with Kikukawa-type mirror vertices if needed, and a gauge-invariant measure (Lüscher-type measure term or its 2D abelian construction), with W-matched witnesses as in K2c.
- **CHI-RP-FAIL:** a quadrature-converged negative RP eigenvalue (< −10× the error estimate) on W-matched gauge-invariant witnesses.
- **CHI-RP-PASS-at-power:** PSD within error, with the vector-like K2c witness as the power reference.
- **OPEN:** otherwise, including "a gauge-invariant chiral measure could not be built in budget". State which.

**NT-2. Is the hard plaquette bound RP in 3D (pure gauge)?** This is X3's price P-X3d, owed by K2c. Use a 3D slice with a 2×2-plaquette crossing structure, the hard indicator |arg U_p| < δ, link reflection, and W-matched pools.
- **PG3-NEG:** a converged negative eigenvalue (the bound itself is not RP in 3D).
- **PG3-PSD:** PSD on searched pools at power.
- **OPEN:** otherwise.

**NT-3. T-G1 (route 2, X2).** Does the filter overlap destroy the unique symmetric gapped strong-coupling phase? Exact diagonalisation of a filtered "star" quartic, with an SU(4) (or Spin(6)) toy symmetry on 4–6-site rings or clusters, compared with the onsite quartic.
- **TG1-SYMMETRIC:** at strong coupling, the filtered model has a unique, symmetric, gapped ground state with no order-parameter growth with size.
- **TG1-BROKEN:** degeneracy or order that grows with size (an SSB precursor), or a gapless sector.
- **OPEN:** otherwise.
