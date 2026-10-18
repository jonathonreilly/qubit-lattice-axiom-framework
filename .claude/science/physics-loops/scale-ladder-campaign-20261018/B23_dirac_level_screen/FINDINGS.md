# B23 findings: Dirac-level screen of the remaining B20 families

Provenance: a worker of the same model family; not independently checked. Saved by the supervisor from the hand-back. The model is B20_check's `chklib.py` / `B18_check/chk_model.py`; b20lib, b18lib and walklib were not used. `run_all.sh` gives TOTAL: PASS=28 FAIL=0 (about 15 min on 4 cores).

**Result.** 0 of 8,302 D₊⊕D₋ 4-fold k* levels pass in the cliff2, π/6 and π/6-taste families.
- 7,554 fail the sign test.
- Each of the other 748 has a defective node exactly at E. These were confirmed 748/748 by one-sided finite differences, with the nodes at E to 7e−15.

Together with B20_check's 1,872, **all 10,174 D₊⊕D₋ levels in the parameter-free B20 families are screened, and none passes.**

| Family | Dirac levels | Sign fail | Survivors | Pass |
|---|---|---|---|---|
| cliff2 | 7,352 | 6,690 | 662 | 0 |
| π/6 | 726 | 672 | 54 | 0 |
| π/6-taste | 224 | 192 | 32 | 0 |

## Checks

- The k* node of every survivor is exactly D₊⊕D₋. There are no cross terms (4e−15), and each block is an untilted isotropic cone at v_D with chiralities (+1, −1). This confirms the check's Dirac lemma.
- At −k*: 4-fold isotropic at E in 490 survivors, 8-fold anisotropic in 78, and not at E in 180.

## Obstruction pattern (observed, not proved)

- **Defective nodes overall:** 32,652 anisotropic, 12,549 tilted, 7,425 flat, and 317 single bands at E. In 20 cliff2 survivors a missed Fermi crossing was found.
- **Closest cases:** S·o·R·o (H00, L022) and π/6 S·R·o (L0.6.6). Each has 4 defective nodes: three 4-fold cube doublers at [0.9, 1.2]·v_D, and −k* 8-fold anisotropic. That is B20's uniaxial-cube-doubler obstruction, now for Dirac levels.
- **Words without R_L:** at least 26 defective nodes each.
- **π/6-taste:** at least 40 generic-k nodes each.

## Still unscreened

- Higher-multiplicity k* levels mixing D and G3/2: 6-fold (24,128), 8-fold (4,020 + 5,458), 10-fold (3,144) and 12-fold (574).
- 65,244 G3/2 4-fold levels.

Both are outside L1. This is a numerical negative search, not a no-go.
