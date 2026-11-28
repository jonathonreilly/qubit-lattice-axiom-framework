# Gate: upper chain and the UV-CT interface, at 41489e4876

Checker: claude-opus-5-5 at high effort, a fresh context under lead session b3f5c21a. Author: claude-opus-5-5 at max effort. This is a same-model check, not an independent review. It grants no status.

Scope: `parts/upper-chain.md`, lines cited at that commit. Theorems 6, 8, 9 and 10 were read but not checked line by line, and the file's own numerics were not re-run. Check script: `checks/gate_upper-chain_41489e4876.py`.

## Verdict: ADVANCE, conditional on UV-CT, which stays open. No item is WRONG.

| Item | Verdict | Result |
|---|---|---|
| Lemmas 1.1, 1.2, Theorem 1 | CORRECT-NO-ADVANCE | Known method; weights, conjugate pattern and the Corollary 1.3 Hessian check |
| Theorem 3, Corollary 3.2 | ADVANCE | Parity set, conditional variance, constants and second difference check |
| Theorem 4 | ADVANCE | (a)-(c) and the K_1 limit are right; the Reading must be narrowed (D1) |
| Proposition 5 | ADVANCE | Works; caveat in D4 |
| Lemma 7.2 | ADVANCE | Transfer-operator positivity plus Tr A^2 <= (Tr A)^2 |
| Theorem 7.4 | ADVANCE | Exponents, 16 images, translation choice, mixed derivatives, polydisc and Bell bound check |
| UV-CT | CORRECT-NO-ADVANCE | Unproved, not refuted |

## Findings

**Bounded fields do not escape Theorem 4 at finite tolerance.** Take eps = b clip(phi, +-K), with b = sqrt(c) m and K = C rho sqrt(c)/m, so sup|eps| = C rho c uniformly in a. Reflection positivity holds and the pressure stays c t^2/2 on |t| <= rho, up to about exp(-kappa/m^2) per site. Comparing m = m_* a with m = a^(1/2) gives separated correlators of about c a^-4 against exponentially small ones, with data indistinguishable at any C L^4 tolerance. Exact 1D transfer matrix at m = 0.2, 0.1, 0.05 matches c t^2/2 to 10 digits. The 4D upper bound is only sketched, by a variational argument.

**Interface tests.**
- 2D torus: with additive E, |G| exp(-Re E) is within 3e-4 of 1 at |w| = 1, tau = 0.5, 0.1, n = 400 to 40000. CT3 holds with tau = 0, and CT4 reduces to a finite log Theta(tau).
- 4D Gaussian: E = log G gives c = 0, and the cross term is cutoff-free.
- The a^-2 gradient term has range about a and cancels on separated supports, so CT3 is consistent with it.
- CT4 for all L is equivalent to p_P(beta) - p_infinity(beta) <= c_F (a/a_*)^4. It has no simple failure.

## Defects

- **D1 (medium), lines 6, 155.** "No argument" is overbroad. Theorem 4(b) has exact Z of order 2, while bounded fields give exponential type, so no bounded member matches exactly. Yang-Mills-shaped data cannot split exactly either. The barrier is a statement at tolerance on bounded t, for arguments that use Z generically. A proof exploiting the specific Yang-Mills h is not formally excluded. Restate it that way, and replace "believed" at line 364 with the clipped family.
- **D2 (medium), line 367.** The CT4 check covers only log T at fixed beta. By mode count (derived, not checked), 9T^4 - 3 fluctuating modes give +(3/2) log beta, and the moduli integral adds log log beta. So naive Gaussian CT4 fails at beta(a) by log log(1/a), and only two-loop running of the zero-mode factor can rescue it. CT4 cannot be verified at Gaussian order.
- **D3 (medium), lines 9, 248.** "Infrared safe" and "natural" are unproved. CT4 fixes p_infinity to accuracy a^4 relative to p_P, and the a^-3 surface terms must cancel exactly.
- **D4 (low), line 163.** "Hence on a half-line" needs rho >= half the trajectory step, about 0.13 for SU(2).
- **D5 (low), line 94.** "> 0 automatically" should be >= 0. Unused.
- **D6 (low), line 373.** Replace the plane statement with the torus statement above.

**Risk, not a defect.** CT1 at complex w^pat is the least tested clause: it needs phase cancellation to O(1) in an exponent of order a^-4.

## Gate questions

1. Right? Yes for the items checked, subject to D1.
2. Strictly smaller? In volume, position and zero-freeness, yes. In the cutoff, no. In the Theorem 4 family, CT1, CT2 and CT4 hold with c = c_F = 0 and only CT3 fails, so CT3 carries all the separated content. E is not a free counterterm: Jensen applied to Ztilde gives at most log A/log 2 zeros in |t| <= 1/2 and forces E to be close to log G in L^1. The UV core is essentially UV-LOC-C on one torus, without non-vanishing, plus CT4.
3. Which consumer? (SM) for Theorems 8 and 9, through Corollary 7.5. It delivers neither E0', O(4) nor Wightman functions, and it gives the witness no lower bound.
