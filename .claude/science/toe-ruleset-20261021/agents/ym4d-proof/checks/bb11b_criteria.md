# checks/bb11b_criteria.md — pre-registered criteria for check bb11b (BFT_B session 11)

Written after `checks/bb11.out` was read (bb11: **NOT ALL PASS**, A5 FAILED) and **before** `checks/bb11b_*.py` existed.
**`checks/bb11_criteria.md`, `checks/bb11_bgd.py`, `checks/bb11.out` and `checks/bb11.time` are not altered**; bb11's A5
FAIL stands as the record. No bb11 criterion is retuned. The model, the backgrounds and the entire operator construction
are copied from `checks/bb11_bgd.py` unaltered; only the tests below are new.

**What bb11's A5 FAIL means (the diagnosis, stated before the new tests are written).** bb11's A5 tested the covariant
form of §16.1 (a)'s gauge shift for an **arbitrary** level-0 gauge function `mu`:
`lam_X^{E,Z}(x + d_Z mu) = lam_X^{E,Z}(x) - mu + mu(c_X)`. Its proof at the trivial background substitutes
`nu := lam + mu - mu(c_X)` and uses `d(mu(c_X)) = 0`, i.e. **"d of a constant is 0"**. At a nontrivial background
`(d_Z c)(b) = (Ad_{Z(b)} - 1)c`, which is **not** zero. So the step is a Tier-B step (an exactness/constancy relation),
not a Tier-A step, and §38.2's Theorem N1-alg is wrong in the generality in which this session pre-stated it. bb11's A5
is therefore a **correct FAIL of a wrong statement**, not a script defect.

## New tests (pre-registered here)

| id | statement tested | PASS iff | FAIL iff |
|---|---|---|---|
| **A5p** | the gauge shift restricted to the class the consumers use: for every level-0 `mu` with `mu(c_X) = 0`, `lam_X^{E,Z}(x + d_Z mu) = lam_X^{E,Z}(x) - mu` exactly, on the curved nonabelian background (4 pseudo-random `x`, 4 pseudo-random `mu` pinned at `c_X`) | exact equality in `Q` on every instance | any instance differs |
| **A5g** | the general-`mu` identity in its corrected form: `lam_X^{E,Z}(x + d_Z mu) = lam_X^{E,Z}(x + d_Z kappa) - mu + mu(c_X)` with `kappa` the **constant** function `mu(c_X)`, exactly, for 4 pseudo-random `x` and 4 pseudo-random unpinned `mu` | exact equality in `Q` on every instance | any instance differs |
| **A5n** | non-vacuity of the correction: `d_Z kappa` is **exactly nonzero** for the `kappa` used (so A5g is not A5p in disguise, and bb11's A5 could not have passed) | `d_Z kappa != 0` for at least one instance, and `lam_X^{E,Z}(x + d_Z kappa) != lam_X^{E,Z}(x)` for at least one | either is identically zero |
| **A5a** | the same `mu`s on the **abelian** background: bb11's original A5 identity holds there exactly (so the failure is caused by the curvature of the background and by nothing else in the construction) | exact equality in `Q` on every instance | any instance differs |
| **A6q** | the consequence for the gauge group: at a curved background the constant functions are **not** in the kernel of `d_Z` on the box, so `Lambda_0` cannot be taken modulo constants. Tested as: `d_Z c != 0` for a nonzero constant `c`, exactly, on the curved background; and `d_Z c = 0` exactly on the abelian one | both hold | either fails |

## Verdict rule (pre-registered)

- **ALL PASS** iff A5p, A5g, A5n, A5a and A6q all pass.
- A failure is reported as a FAIL, output and script kept unaltered, any rerun under a new id with this file untouched.
- **Scope limitation, to be reported whatever the outcome:** the same as bb11's (`d = 2`, `k = 2`, SU(2) adjoint, a thin
  family of rational-rotation backgrounds, a reduced `5 x 5` box). These tests settle the **quantifier** on the gauge
  shift and nothing else; they say nothing about Tier C, about §38.4, or about `d = 4`.
- **No constant derived in session 11 appears above.** The only constants used are the model parameters `d = 2`, `L = 3`,
  `k = 2` and the rational rotation entries `3/5, 4/5`, all fixed in `checks/bb11_criteria.md` before any script existed.
