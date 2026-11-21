Provenance: Claude Opus 5.5, the target lead, reading a proof written by OpenAI GPT-6 Astra at max effort. Different provider from the author. The lead wrote the prompt, so this read isn't independent of the framing. Not an audit, grants no status, no run used.

| Statement in `library/nt2-free-value-by-hand.md` | Verdict |
|---|---|
| (H1) to (H5), the near/far pair at (2d,2d,2d,d), (2d,2d,2d,2d) | ADVANCE |
| (H6) to (H12), the uniform bound on the fibre correction, C = 2^53, exponent L^-4 | ADVANCE |
| (H13) to (H17), the joint limit and the identification with the closed span | ADVANCE, read at the level of steps, less closely than the two rows above |
| (H18) to (H20), a_L >= a_0 > 0 | ADVANCE |
| (H21), the order of b and L | ADVANCE, as an implication from producer bounds |

Rechecked by hand: the moments in (H1); the Hessian of M and the constant 80 in (H2); the remainder (H3); mu, and the inequality 5*13^3 <= 6 d^2; the alias bound |a| <= u(m_mu)^2 prod u(m_nu); the shell sum 625*52 < 2^15; the normalization of h and G from (B-3), noting the projection doesn't depend on how coarse functionals are scaled; (H10); the arithmetic of (H12), (H18), (H19), and the a_L definition at line 76 of the criterion note.

Why the bound works: H_cl lies in H_all, and on H_all the Feynman covariance is diagonal, so the bound uses a space larger than the closed currents. Closed functionals are gauge invariant, so the Feynman inner product is only a device. The low-momentum count is |h|^2/G ~ (L^-2/|theta|)^2 theta^2 = L^-4, with no logarithm. The earlier trend at a block corner (2.59 to 3.17 at L = 9 to 33) doesn't contradict this.

Defects: none that break a step.
1. This covers only the explicit Gaussian map (B-1). The same bound isn't delivered for either attempt's map, and it doesn't identify the Gaussian fibre with the nonlinear chart in (FT).
2. L_0 is huge, since mu carries d^-4 with d >= 64. That's harmless to the logic, because every other part takes L large, but a fixed L elsewhere would conflict.
3. Corollary NT1-F's printed order of b and L at line 78 still needs (H21) applied to its text, under item `hand-witness`.

Not read: the remaining text of `parts/witness.md`, or the consumers of NT1-F beyond that corollary.
