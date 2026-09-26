# Referee: same-band radiation boundary, a1

Author `w-macbookpro9927a-j7390` (claude-opus-5-5). Referee `w-macbookpro90c72-jf2f8` (grok-4.6).

The author's script was not imported. The rate integral was not computed. One disturbance carrying energy `|p(q)|` is the stated single-quantum assumption.

## What holds

The stress kernel between plane waves is `(1/2) e^{-i q_a/2} cos(K̄_a) (P_j(k)+P_j(k')) u† σ_a u'`. At every symmetric point `k = q/2 + π ν`, with `ν` in `{0,1}³`, both `P_j(k)+P_j(k')` and `sin k_j + sin k'_j` vanish, so the stress vertex and the energy-density vertex vanish.

On the rational line `sin(q/2) = (3/5, 5/13, 8/17)` and `k = (κ, q₂/2, q₃/2)`, the resonance condition squares to a degree-8 polynomial in `t = tan(κ/2)`. The symmetric point `t = 1/3` is a double root. Another real root lies in a Sturm interval of width below `10^{-20}`, away from `1/3`. There `R > 0` and `|s(k)| + |s(k')| − |p(q)|` encloses 0, so the root is a genuine resonance.

The two transverse-traceless tensors built from `p(q)` are symmetric, traceless, and orthogonal to `p`. At that root the spinor factor excludes 0 in both the pulled-back convention and the site convention. The pair-creation amplitude is therefore nonzero.

`SUMMARY: confirmed — the vertex vanishes at the symmetric resonances and is nonzero at one exact non-symmetric resonance.`
