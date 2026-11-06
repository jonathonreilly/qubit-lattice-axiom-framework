lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-06T17:46Z

First failing step: (check in progress; this line is replaced at the end.)

# p6b-check: library/port/p6-correlation.md, second half (5.1:thm-correlation-theorem, 5.14:thm-one-loop-law)

Provenance: Claude Opus 5.5 (claude-opus-5-5), max effort, Mac mini worker, fresh session, started 2026-11-06T05:47Z. Repository commit d9d592ba8. One reading, not an audit, not human review. The port is Codex's. Credit: the theorems and proofs checked here are by Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text; Balaban's papers are cited inputs of their proofs.

(Work in progress. Sections are added as the check proceeds.)

## Quotation check (done)

Every fenced `latex` block of the port's second half was compared with CA-II by plain text comparison (script in my scratch folder; CA-II sha256 6a1f74b05f74...4b2b8f, 145,624 lines, same file as p6a-check). All 11 blocks are exact copies:

| Port lines | CA-II lines | Content |
|---|---|---|
| 465-639 | 2791-2966 | 5.1:thm-correlation-theorem statement |
| 686-725 | 27042-27082 | 5.14:thm-one-loop-law statement |
| 2677-2911 | 25243-25478 | joint hypothesis, pure step, frozen integral, frozen averaging, large-field step |
| 2920-3124 | 25480-25685 | 5.2:prf-induction-order and the deduction of clauses (i)-(ii) |
| 3141-3289 | 26531-26680 | 5.3:prf-flow-reference |
| 3331-3425 | 26682-26777 | 5.3:prf-local-averaging |
| 3436-3714 | 59645-59924 | 5.12:prf-torus-bound-proof |
| 3748-3908 | 59926-60087 | 5.12:prop-subsequential-limits and proof |
| 3927-4015 | 60089-60178 | 5.12:lem-limit-positivity and proof |
| 4040-4112 | 26967-27040 | 5.14 majorant definitions |
| 4124-4308 | 27120-27305 | proof of 5.14:thm-one-loop-law |

A text comparison checks quotation only. The mathematics was redone by hand, below.

## Working notes on B3 (filled in as the check proceeds)

- Flow arithmetic, redone. Pure step: |zeta_k| <= (4/3)|zeta| <= (8/3) r on D(0,2r). Frozen averaging: delta <= (1-4/L)/10 gives r(delta) = (1-10 delta)L/2 >= 2. Coupling increment: c_0 = 2 lambda puts the sum of (k+1-i) c_0 and the k+1-i defects in [lambda, 3 lambda](k+1-i); |s_i - s_{k+1}| <= 2c_2 widens it by 2c_2 per side. Correct. Cauchy on radius r' -> r about points of the closed disc D(0,r) gives |h_k'| <= 2 d_k(2r), so the total Lipschitz bound is 2/3. Schwarz gives |h_k'(0)| <= d_k(2r), and N_K - 1 = sum_{k<K} h_k'(0) is real, so N_K is in [2/3, 4/3]. Correct.
- Clause (ii)'s derivative bound (4/3) C_beta e_k on the closed half polydisc is 5.2:lem-polydisc-gradient (Moebius at |a_j| <= 1/2: sum (1-|a_j|^2)|d_j g| <= 1). The B3 passages do not invoke it at this place, but it is the lemma the driven-flow proof uses (checked in p6a-check). Correct.
- C-F2 (port 3299-3311), redone. For j <= k on a prefix with x_k > X: y_j > X - 4c_2 + lambda(k-j) >= X/2 + lambda(k-j), since X >= gamma°^{-2} = 8c_2 + 4. With e = 2E* tau + theta (CA-II 1946-1957): psi(y^{-1/2}) = y^{-1} e(y^{-1/2}) <= C y^{-3/2} (log y)^{p_0}, because p_0 >= 5r >= 10 is an integer (CA-I 1862-1864), so the exponential term is negligible. h(t) = t^{-3/2}(log t)^{p_0} decreases for log t > 2p_0/3. Integral comparison and t = A e^v give sum_u h(A + lambda u) <= C lambda^{-1} A^{-1/2} (log A)^{p_0}; for a = (kappa_0-4)/2 >= 3/2, sum_u (A + lambda u)^{-a} <= C lambda^{-1} A^{1-a} = C' lambda^{-1} g^{kappa_0-6}. This gives the theorem's bound on sum_{k<K} D_k(rho). Correct. The port's extra ceiling X/2 >= e^{2p_0} is needed and right: the source's step omega_k = C_beta e_k <= C_beta e(y_k^{-1/2}) (CA-II 26552-26553) uses monotonicity of e at the argument y_k^{-1/2} >= g_k, which can exceed gamma_J (up to sqrt 2 gamma_J); the monotonicity proof of 5.1:not-coupling-functions needs log of the inverse square of the argument >= 2p_0 there.
- D_k(rho) = phi'_k + phi''_k/rho (CA-II 2054-2060) decreases in rho. So clause (b) of (J_k), recorded only at rho = 2r, implies the bound at every rho in [r,2r] on D(0,rho). The proof's "the same bound obtained at the earlier steps" is therefore covered.
- Local averaging (5.3:eq-local-averaging-2), redone: |zeta_{k+1}(p)| <= sup|w| (1 + sum_{j<=k+1} d_{j-1}(2r)) <= (4/3) sup|w|, using 0 <= phi_j <= 1, h_y >= 0, sum_y h_y = 1. |b_j| <= |b_j(0)| + 2r d_{j-1}(2r) <= b_+ + 2r/3, since lambda - 2c_2 <= b_j(0) <= b_+. Correct.
- Torus bound (alpha), redone. For z in D, s -> h(s z) - 1 is holomorphic on |s| < 1, is 0 at 0 and is bounded by Q + 1, so Schwarz gives |h - 1| <= 1/2 on (2Q+2)^{-1} D, |Log h| <= log 2, and Cauchy on polyradii (1-u) r/((2Q+2) n ||f_i||) gives the log 2 (2Q+2)^n (n/r)^n prod ||f_i|| term. Correct (this reads D as the ball sum_i |z_i| ||f_i||_sharp < r; see the findings if that reading fails). (beta) and C-F5: for a_j = M t_j <= d/24, [d/(4a_j) - 3]_+ >= d/(8a_j) and e^{-kappa d/(32 a_j)} <= 5!(32/kappa)^5 (a_j/d)^5; the geometric sums give C(1 + d^{-4}); the other scales number at most 1 + log_L^+(24M/(d N_side)), each at most C(1 + (24/d)^4). With d <= 1 on the unit torus this is C d^{-4}(1 + log^+ d^{-1}). Correct.
