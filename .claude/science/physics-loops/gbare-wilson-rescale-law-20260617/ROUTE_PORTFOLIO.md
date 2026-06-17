# Route Portfolio

| Route | Score | Outcome |
|---|---:|---|
| Narrow original row to Gram-only | 2 | Already present on `origin/main`; kept and clarified. |
| Derive fixed-component Wilson beta law under `T_a -> cT_a` | 3 | Implemented as Theorem A: `beta_new/beta_old = 1/c^2`. |
| Derive pure basis relabeling law | 2 | Implemented as Theorem B: beta unchanged. |
| Preserve old `c^2` law as WM coupling-coordinate identity | 3 | Implemented as Theorem C and wired into the beta arithmetic row. |
| Claim convention-free beta routing | 0 | Rejected; false without specifying what is held fixed. |

Selected route: convention-split theorem plus exact runner, because it directly
answers the audit blocker and prevents the old `c^2` statement from being read
as a fixed-component Wilson-action law.
