# Frozen fixed-time comparison

Predeclared before inspecting any fixed-time propagation output.

- Initial vector: the actual resolved first-mark output in #8831, `q=(1,-1,1,0,1,1)`, `E=(1,0,0,0,0,1)`.
- Observable: the bounded projector onto a vacancy at B site 3, `O=1[q_3=0]` (operator norm 1).
- Physical parameters: `K=1`, `delta=1`; retain both in the exact effective operator. The spin sequence is `S=2,3,4,6,8` (extend only if the matrix and cutoff checks remain controlled), so `C=S(S+1)` and `epsilon=C^(-1/2)` obey the declared simultaneous scaling.
- Times: `tau=1/4, 1/2, 1` in fixed laboratory units; no time shrinks with `S`.
- Exact finite-spin target: `C H2,S + H4,S`, with `H2,S=-P T_S Pi1 T_S P` and `H4,S=(A_S^dagger A_S)^2-(1/2)Z_S^dagger Z_S` reconstructed from the bounded finite-spin hop graph.
- Proposed comparison: `C H2,infinity + D + H4,infinity` on the full rotor path. Simulate increasing independent path cutoffs and report cutoff sensitivity; never substitute agreement of truncated matrices for a domain or electric-tail proof.
- Outcome rule: a certified observable gap would reject this generator/preparation only. Stable floating-point gaps without rigorous error bounds are numerical warnings. Agreement at a few spins is inconclusive. Core coefficient agreement alone is not a fixed-time result.

Secondary tail diagnostic, declared before its evaluation: for each `S`, let `I_S` be the exact connected path interval on which every physical link flux satisfies `|E_e|<=S`; use the bounded rotor projector `O_tail,S=1[n not in I_S]`. Its exact finite-spin expectation is zero. The rotor candidate expectation will be reported against increasing path cutoffs. This can expose missing tail control but remains numerical unless the infinite-cutoff tail is bounded.
