# Twisted pair E1/2 + E5/2: line-branch ideals (B7 note, item 4)

Pipeline:
1. `../../exact_extensions/spinj_exact.py E12+E52` builds the U(0) = 1 cell
   walks and the line-lemma branches. The E5/2 half is E1/2 with the sign
   on the C4 generators.
2. `build_branches.py` writes one pickle per branch.
3. `../../exact_extensions/tosing_branch.py` converts each pickle; these
   runs use the version fixed at 21:35Z.
4. The mod-p files swap `modStd` for `slimgb` in characteristic 32003. Each branch has 32 free unknowns and 336
real equations.

Each branch is labelled by its J_x-eigenline exponents along the x axis:

| file | axis exponents (m_1..m_4) | mod 32003 (slimgb) | over Q (modStd) |
|---|---|---|---|
| b0 | (-1, 1, -1, 1) | unit ideal | unit ideal (`b0_Q.out`) |
| b1 | (-1, 1, 0, 0) | unit ideal | not run |
| b2 | (-1, 1, 1, -1) | unit ideal | not run |
| b3 | (0, 0, -1, 1) | unit ideal | not run |
| b4 | (0, 0, 0, 0) | dim 4; 2 unknowns vanish, 4 nilpotent | not finished in window |
| b5 | (0, 0, 1, -1) | unit ideal | not run |
| b6 | (1, -1, -1, 1) | unit ideal | not run |
| b7 | (1, -1, 0, 0) | unit ideal | not run |
| b8 | (1, -1, 1, -1) | unit ideal | not run |

In each `.out` file, `zzI power P` gives the smallest P <= 12 with
zzI^P in the ideal. P = 12 means none was found up to 12.

Evidence level: the branch list comes from a numerical linear-consistency
prefilter, and the unit ideals are mod p except for b0. Together they
support "every U(0) = 1 twisted-pair cell walk is flat along the axes", but
do not prove it.

Rerun one branch with:
`Singular -q bN_p.sing` (Singular 4.x, any build with slimgb; modstd.lib for the Q input).
