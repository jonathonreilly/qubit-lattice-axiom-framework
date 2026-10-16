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
| b0 | (-1, 1, -1, 1) | unit ideal | unit ideal |
| b1 | (-1, 1, 0, 0) | unit ideal | unit ideal |
| b2 | (-1, 1, 1, -1) | unit ideal | unit ideal |
| b3 | (0, 0, -1, 1) | unit ideal | unit ideal |
| b4 | (0, 0, 0, 0) | dim 4; 2 unknowns vanish, 4 nilpotent | same |
| b5 | (0, 0, 1, -1) | unit ideal | unit ideal |
| b6 | (1, -1, -1, 1) | unit ideal | unit ideal |
| b7 | (1, -1, 0, 0) | unit ideal | unit ideal |
| b8 | (1, -1, 1, -1) | unit ideal | unit ideal |

In each `.out` file, `zzI power P` gives the smallest P <= 12 with
zzI^P in the ideal; P = 12 means none was found below 12 (not nilpotent at low order).

Evidence level: the branch list comes from a numerical linear-consistency
prefilter. The over-Q column is Singular's multi-prime modStd
(`bN_Q.out`, input `b0_Q.sing` pattern: `ring r=0`, `modStd`); for a unit
result modStd does not itself certify 1 in I. Together they
support "every U(0) = 1 twisted-pair cell walk is flat along the axes", but
do not prove it.

Rerun one branch with:
`Singular -q bN_p.sing` (Singular 4.x, any build with slimgb; modstd.lib for the Q input).
