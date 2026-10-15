# OBS-4 PREREG follow-ups (dated; PREREG.md is not edited)

## 14:03Z (after runs C1, C2, C3, R1, R1b/R1c/R3/R4 numbers, R2 refits; before any reading is written)

- **Sign of J (rule 1 applied as registered).** B-gen as fitted by OBS-3 has J = -3.1157e-5 in the PDG definition
  (OBS-3 fitted |J|). Its complex conjugate (identical moduli, identical common diagonal, so the same escape) is used as
  primary. B-gen120 and the A-M1 realisations already have J > 0.
- **C3 partial deviation.** The UTfit-derived C4 rows reproduce Harnik-Kopp-Zupan Table 2 to 1% (pass). My own direct
  bag-parameter computation reproduces the HKZ rows within x0.43-1.6 except the K Re row, which is x2.8 looser than HKZ.
  Cause: my registered NP allowance for dm_K is 100% of dm_K^exp, while UTfit's fit is tighter. Registered threshold was
  "within a factor 2"; recorded as missed for that one row. The reading uses the INP rows (rule 5), not the direct ones.
- **Added after the PREREG (not registered):**
  - R1c: cancellation measure |sum_K|/sum_K|.| and a 1% vev-jitter test at the vev-optimised point (the vev-optimised
    M* turned out to be a fine-tuned cancellation);
  - R2b: FCNC-seeking refits of the exact B-gen family (soft log M* term, then an exact polish);
  - R1d (obs4_tuned.py): joint tuning of the exact-family parameters and the vevs, to see how low a tuned M* can go;
  - Crivellin-Kokulu-Greub arXiv:1303.5877 (2HDM type III, eqs. 28, 33-39) as the published 2HDM-III cross-check
    (abstract/text level via ar5iv).

## 14:12Z

- **Header time correction.** PREREG.md's header says "written 13:46Z"; I typed that without reading the clock. The file's
  modification time is 13:45:26Z and the first computation (r1.out) finished at 13:48:36Z, so the PREREG still preceded
  every run, but the typed time was about one minute ahead. Recorded here; PREREG.md is not edited.
- **R4b added (not registered): obs4_potential.py.** Differential-evolution search over the general renormalisable,
  CP-conserving, Z2xZ2-symmetric four-doublet potential (28 real quartics, |lambda| <= 4 pi or 8 pi), vevs with every
  carrier vev >= 16.2 GeV, local minimum required, boundedness from below not imposed. It replaces the registered
  analytic-only M_allowed with a checked number (0.77 TeV at 4 pi, 1.09 TeV at 8 pi for the lightest non-h state).
- **Reading rule unchanged.** Rule 10 is applied as registered.
