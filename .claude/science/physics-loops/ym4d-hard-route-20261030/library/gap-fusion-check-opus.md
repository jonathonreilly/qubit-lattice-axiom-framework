# Check of gap-fusion-astra.md, Sections 1 to 6

- Checker: Claude Opus 5.5 (one session, no subagents). Date: 2026-11-12.
- Author checked: Codex gpt-6-astra max, FINISH row 765, source `39b2391804e2`.
- File checked (read-only, read in full, lines 1-629):
  `ym4d-lead/clone/.claude/science/physics-loops/ym4d-hard-route-20261030/library/gap-fusion-astra.md`.
- Inputs read (same folder unless stated):
  - `gap-es1-opus.md` Sections 0-3, 5, 6 (Theorem V, Theorem LB, (FUSE_K), FUSE-suff).
  - `gap-es1-opus-check.md` verdict table, Section 6 and the RESULT line.
  - `gap-loop-eq-opus.md` Sections 6 and 7 (Lemma 6.2, Corollary 6.3, (LOC)).
  - `gap-loop-eq-check.md` Section 5 (the corrected form (1) and the kernel counterexample).
  - `gap-sc-box.md` Sections 1-4 (Lemmas 3.1-3.5, Proposition 3.6, the Schwarz step).
  - `gap-seed-sc.md` Sections 1-2 (the torus port (P), Lemma 3.3(a) on tori).
  - `gap-means-max.md` 4.1 (the input (TM-tw): Z^{e+m}(t,B) = Tr(T_{B,m}^t C^e), the 1/8 Fourier sum).
  - `gap-transfer.md` Notation, Section 1, Section 9 (9.3 the eight electric sectors).
  - `gap-crux-fp.md` 3b.3 (Propositions T1-T3).
  - The soft-route witness `MASS_GAP_LOCAL_BLOCK_ASTRA.md` Sections 0-2, read with
    `git show f76f6c649cff:.claude/science/toe-ruleset-20261021/agents/ym4d-proof/MASS_GAP_LOCAL_BLOCK_ASTRA.md`
    from my own worktree (not from the checked folder).
- Not read: `gap-flux-exercise.md` 8.2-8.4 in full (only through `gap-means-max.md` 4.1, which
  restates and cites them); `gap-es1-astra.md`; the Sussman-Alpoge files.
- Method: by hand. One pure-Python guide run (`python3 -I`, a few kB) evaluated the
  constants and I_2/I_1; it decided nothing.

## Verdict table

| # | Statement (lines) | Verdict | Finding |
|---|---|---|---|
| 1a | Definition of B, S, p, crossed set, L_mag (43-55) | HOLDS | Matches `gap-es1-opus.md` Section 1 |
| 1b | Inputs p>=0, p<=1, sum p=4 (57-63) | HOLDS | Lemma R1(b), R2(a) via (TM-tw) |
| 1c | Exact (F-h) target (65-68) | HOLDS | Same as (FUSE_K) (F-h); "K polynomial in a" is the consumer's wish, not part of FUSE-suff |
| 1d | LOC and estimate (1) (70-91) | HOLDS | Identical to the corrected Corollary 6.3 in `gap-loop-eq-check.md` Section 5 |
| 2a | Witness (3) and eta in (2) (95-127) | HOLDS (remark) | Source (11) has p_B=13; 16 is a valid upper bound; algebra gives eta exactly. Rectangular sides >=3: see remark |
| 2b | eta <= r_ev, S >= eta^t (129-135) | HOLDS | |
| 2c | (4): sqrt(eta) >= beta^2/160 on (0,R] (137-150) | HOLDS | r >= beta/(4e^beta) checked by odd-moment expansion |
| 3a | Signed-activity port, (6) (165-183) | HOLDS | eta_p U_p is in SU(2); Lemma 3.1, 3.2, 3.3 and (P) unchanged |
| 3b | Winding-area cancellation (185-210) | HOLDS | Mod-2 projection argument checked step by step |
| 3c | Zero of order A_min, Schwarz step, (5) (212-219) | HOLDS | (64/3)*6 = 128, 128R = 1/100 |
| 3d | (7) on the consumer shapes (221-227) | HOLDS | V <= 4a^4, A_min = a^2 |
| 4a | Finite comparison (8) at any beta (232-257) | HOLDS | Uses only (TM-tw), positivity and sum of characters = 0 |
| 4b | Theorem SC-F, (9)-(11), K=1, all a>=3 (259-303) | HOLDS | Every constant re-derived: 5/16, 80/81, 405/2048, 2/25 |
| 4c | Corollary SC-large, (12) (305-329) | HOLDS AFTER CORRECTION (wording) | At beta=0 all twelve heavy weights vanish, not only the electric ones |
| 4d | ARGUED interpretation (331-336) | Not a proof claim | Consistent with the proof |
| 5a | Sufficient test (13) and identification of L_mag for D<1/4 (340-351) | HOLDS | |
| 5b | (14) suffices at order one with K=1, thresholds (353-371) | HOLDS (wording remark) | Concavity of both exponents gives the "every larger a" step |
| 5c | (14) is stronger than (F-h) (373-377) | HOLDS AFTER CORRECTION (precision) | True as: (14) implies (F-h) with K=1 for all large a; (F-h) does not imply (14). Not at every fixed a |
| 5d | 5.1 limitation statements, (15) (379-413) | HOLDS | (15) is the exact derivative; constants of Step 3 quoted correctly |
| 5e | 5.2 seam comparison, (16) (415-441) | HOLDS | 6 stacks x 4a^2 plaquettes x 2beta |
| 5f | 5.3 variance half, (17) (443-489) | HOLDS (remark) | Density e^{-12k beta} matches source (4) with p_B <= 4k, b = k |
| 5g | (18) (491-505) | HOLDS | |
| 5h | (19) finite-beta repair (507-532) | HOLDS | |
| 6a | U(1) logic (536-553) | HOLDS | Consistent with T1, T2 of `gap-crux-fp.md` 3b.3 |
| 6b | Cutoff-scope statements (555-572) | HOLDS | eta ~ e^{-80 beta}/20 -> 0; c_2 grows like e^{12k beta} |

No statement FAILS. Checked line by line by Claude Opus 5.5; the corrections are wording
and precision, not mathematics.

## 1. Section 1: the target and its relation to LOC

Confirmed (credit Codex gpt-6-astra). The definitions match `gap-es1-opus.md` Section 1:
the sixteen crossed sectors x = (chi;m) with chi_2 = m_2 = 0, the box A = (a,c,d) at time a,
p_z = Z_z(a;A)/Z_0(a;A), S = eps_cd = S_ev(a;A). L_mag = {chi = 0} has four members.
The twelve others have chi != 0 and include the dyonic ones (chi != 0, m != 0).

The inputs p >= 0, p <= 1, sum_X p = 4 are Lemma R1(b) and R2(a) as quoted in
`gap-es1-opus.md` Section 1; they rest on (TM-tw) of `gap-means-max.md` 4.1.

The stated target is exactly (F-h) of (FUSE_K). The phrase "K at most polynomial in a" is
not a hypothesis of FUSE-suff. It is the consumer's requirement, because FUSE-suff needs the
six even sums below 10^{-16}/(144 K_*^2). The note's (F-h) with K = 1 meets it trivially.

Estimate (1) and the LOC hypotheses are, symbol for symbol, the corrected Corollary 6.3 of
`gap-loop-eq-check.md` Section 5: Dir(f) <= c_1(1-r_chi)||f||^2,
||f||_inf^2 ||f||^2 <= c_2 Var(f^2), c = 4 c_1 c_2, and
p_chi <= Theta_chi [S^{1/(4c)} + e^{-a/(4c)}]. The note correctly says that (1) gives no pure
power alone (the check's kernel K_eta), and that LOC does not compare magnetic operators
(`gap-loop-eq-opus.md` 6, item 3). HOLDS.

## 2. Section 2: the lower bound S >= eta^t

**Source match.** Soft-route note (11): C_F(a) >= v_N^2 exp[-4 beta(p_B+b)]/(1+v_N/r_f^b),
with F = W_C - integral W_C psi^2, v_2 = 1/4, r_f = I_2/I_1 for SU(2). For an elementary
plaquette b = 4 and the source states p_B = 13. The note uses p_C <= 16 (four links, four
spatial plaquettes each). The bound is decreasing in p_C, so the replacement is valid and
conservative. Algebra: (1/16)/(1 + 1/(4r^4)) = r^4/(4 + 16 r^4), and
exp(-4 beta(16+4)) = e^{-80 beta}. So eta in (2) is exactly (3) with p_C = 16. HOLDS.

**Domain.** The source assumes a cubic periodic lattice of side at least four. Its Sections 1-2
use: distinct loop edges; each link in at most four spatial plaquettes; the kernel ratio (2);
the Perron equation with psi > 0. On a rectangular box with sides at least three, a plaquette
has four distinct edges and every spatial link lies in exactly four distinct spatial plaquettes
(sides >= 3), so p_B = 13 still. The kernel comparison (2) is pointwise. *Remark (no change
of result):* the positivity of psi and the simple top eigenvalue on rectangular boxes come
from the positive-kernel argument of `gap-transfer.md` Sections 1-4 and (TM-tw), which the
note cites in Section 1. They do not come from the soft note's inherited cubic construction.
The note's "checking these geometric hypotheses" should name this input too. The transfer
operators agree: the soft note's kernel exp[beta w(UV^dag)] and `gap-transfer.md`'s
c(g) = exp[-beta(1 - w)] differ by the constant e^{-beta |E|}, which cancels in T/lambda_0.

**eta <= r_ev and S >= eta^t.** W is gauge invariant and invariant under the centre flips
(a plaquette meets a flip slice in zero or two links). So F Omega lies in the even sector,
and <Omega, F Omega> = E_pi F = 0. T restricted to the even complement of Omega is positive
with top r_ev lambda_0, so eta <= <F Omega, (T/lambda_0) F Omega> <= r_ev ||F Omega||^2 <= r_ev,
since ||F Omega||^2 = Var_pi(W) <= 1. All eigenvalue ratios are nonnegative, so
S_ev(t;B) >= r_ev^t >= eta^t for every t >= 1. HOLDS.

**(4).** r <= 1: Markov contraction. Lower bound: with s = tr V/2, the fundamental coefficient
is c_f = E[e^{beta s} 2s] = 2 sum over odd n of beta^n E s^{n+1}/n! >= 2 beta E s^2 = beta/2,
since odd moments vanish and even moments are nonnegative; c_0 <= e^beta. So
r = c_f/(2c_0) >= beta/(4 e^beta). Then eta >= e^{-84 beta} beta^4/(256 * 20).
sqrt(5120) = 71.55 < 80 and e^{-42 beta} >= 1/2 for beta <= 1/84. So
sqrt(eta) >= beta^2/143.1 >= beta^2/160. HOLDS. (Guide run: I_2/I_1 >= beta/(4e^beta) at
seven values of beta in [1e-6, 3]; sqrt(eta)/(beta^2/160) is about 5 at beta = R.)

## 3. Section 3: the uniform bound on the twisted partition functions

**Signed-activity port.** exp[-beta(1 - eta_p s_p)] = e^{-beta} exp[(beta/2) tr(eta_p U_p)]
= e^{-beta} c_0 (1 + g(eta_p U_p)), because -1 is central and eta_p U_p is in SU(2).
`gap-sc-box.md` Lemma 3.1 bounds |g(V)| <= 4|beta| for every V in SU(2), |beta| <= 1/4.
Lemma 3.2 needs only that components use disjoint links. Lemma 3.3 and Proposition 3.6 then
run unchanged; `gap-seed-sc.md` (P) states them on every torus with sides >= 3 and
N = 6V. The activities are real for real beta. So (6) holds for every k on |beta| <= R,
with log Xi_k(0) = 0. HOLDS (credit Codex gpt-6-astra for the port).

**Winding-area cancellation.** Z^k = e^{-beta N} E exp(beta sum_p eta_p s_p). A monomial with
multiplicities h_p carries sign prod_p eta_p^{h_p} = prod over b of eta_p, b = {h_p odd}.
The flip U_l -> -U_l preserves Haar measure and multiplies the integrand by
(-1)^{sum over p containing l of h_p}; a nonzero integral forces b closed. Then the sign is
(-1)^{<k,[b]>}. With the canonical stacks, a negative sign forces an odd intersection
with one activated mu-nu stack. I checked the projection: summing the closedness equation of
a mu-link at (x_mu, x_nu) over (x_rho, x_sigma), each mu-rho and mu-sigma plaquette appears
twice (at x and x - e_rho, summed over all x_rho), so it cancels mod 2. What remains is
c(x_mu, x_nu) + c(x_mu, x_nu - 1) = 0 mod 2. The nu-link equation gives the other
direction. So c = 1 on all n_mu n_nu cells, |b| >= n_mu n_nu >= A_min, and j >= |b|. HOLDS.

**Zero order and Schwarz.** Below degree A_min every contributing monomial has sign +, so
the Taylor coefficients of Z^k and Z^0 agree; both have constant term 1, so their logs agree
below A_min. The branch of (6) is the branch vanishing at 0, so D_k = log Xi_k - log Xi_0
(the terms -beta N + N Log c_0 cancel exactly) has a zero of order >= A_min, and
|D_k| <= (64/3)|beta| N < (64/3) R N on the disc. Maximum principle on |beta| = r < R and
r -> R gives |D_k| <= (64/3) R N q^{A_min} = 128 R V q^{A_min} = (V/100) q^{A_min}.
This is the same step as `gap-sc-box.md` Section 4. HOLDS.

**(7).** On (a,a,c,d) with c,d in {a,2a}: V = a^2 c d <= 4a^4 and A_min = a^2.
So D <= (4a^4/100) q^{a^2} = (a^4/25) q^{a^2}. HOLDS.

## 4. Section 4: Fourier cancellation and (F-h) with K = 1

**(8).** By (TM-tw), Z_{chi,m} = (1/8) sum over e in Z_2^3 of (-1)^{chi.e} Z^{e+m}, and every
Z^k > 0 (positive integrand). For chi != 0 the character sum vanishes, so
Z_{chi,m} = (Z^0/8) sum_e (-1)^{chi.e}(e^{d_{e,m}} - 1); |e^d - 1| <= e^D - 1 for |d| <= D.
Z_{0,0} = (1/8) sum_e Z^e >= Z^0 e^{-D}. So p_{chi,m} <= e^D(e^D - 1) <= D e^{2D}.
Z_{0,m} >= Z^0 e^{-D} and Z_{0,0} <= Z^0 e^D give p_{0,m} >= e^{-2D}. Nonnegativity is
Tr(T_{B,m}^a P_chi) >= 0. The "order-two centre" enters only through the 8-element group
of temporal flips and the vanishing of a nontrivial character sum; no eigenvector of one
magnetic sector is compared with another. HOLDS (credit Codex gpt-6-astra).

**Theorem SC-F.** q = 12800 beta <= 12800 beta_* = R^2/512 < 1/2 (numerically 1.19e-11).
a^4 2^{-a^2}: ratio ((a+1)/a)^4 2^{-(2a+1)} <= (4/3)^4/128 = 0.0247; value 81/512 at a = 3.
So D <= D_a < 1/25 and e^{2D} < 2. By (8), (7), (2), (4):
p_z/sqrt(S) <= D e^{2D}/eta^{a/2} <= 2 D_a (160/beta^2)^a.
Split q^{a^2} = q^{3a} q^{a(a-3)}; q^3 * 160/beta^2 = 160 beta/R^3 <= 160 beta_*/R^3 = 160/512 = 5/16;
q^{a(a-3)} <= 1. So p_z/sqrt(S) <= (2a^4/25)(5/16)^a, with ratio <= (4/3)^4 (5/16) = 80/81
and value (2*81/25)(125/4096) = 405/2048 = 0.198 at a = 3. Heavy p <= D e^{2D} < 2/25;
magnetic p >= e^{-2D} >= 1 - 2D > 23/25. So L_mag is exactly the set {p > 1/2} and (10) holds
for all twelve heavy sectors, all a >= 3, all three shapes, with K = 1. HOLDS.
This is a fixed-bare-coupling result at beta <= 9.3e-16, as the note says.

**Corollary SC-large.** q = e^{-sigma}. a >= 8/sigma gives 4 log a <= 4a <= sigma a^2/2, so
D_a <= e^{-sigma a^2/2}/25 < 1/25. a >= M/sigma gives M a/2 <= sigma a^2/2. Then
4 log a - sigma a^2 + M a/2 <= 0 and p_z/sqrt(S) <= 2/25. M > 0 since eta < 1/16. HOLDS.
*Correction (wording):* at beta = 0 all Z^k equal 1, so Z_{chi,m} = 0 for every chi != 0 and
every m. All twelve heavy weights vanish, the dyonic ones included, not only "the heavy
electric weights". The conclusion at beta = 0 is unchanged.

## 5. Section 5: the test (13) and the supplier (14)

**(13).** p_z <= D e^{2D} <= K eta^{a/2} <= K sqrt(S) by (8) and (2). For D < 1/4:
magnetic p >= e^{-2D} > e^{-1/2} = 0.607 and heavy p <= D e^{2D} < e^{1/2}/4 = 0.412. HOLDS.

**(14) suffices with K = 1.** eta(beta) is continuous and positive on (0, infinity), so
eta_* > 0 on the compact I. If C a^p e^{-sigma a^2} <= 1/4 then D <= 1/4, e^{2D} < 2 and
D e^{2D} <= 2C a^p e^{-sigma a^2} <= e^{-M_* a/2} = eta_*^{a/2} <= eta(beta)^{a/2} under the
second condition. Both exponents, log C + p log a - sigma a^2 and
log(2C) + p log a - sigma a^2 + M_* a/2, are concave in a and tend to -infinity. *Remark
(wording):* the threshold is any a_0 >= 3 at which both conditions hold and both derivatives
are negative; concavity then keeps both for every a >= a_0. That is what the note's last
sentence means. HOLDS.

**"(14) is stronger than (F-h)."** *Correction (precision):* the valid statement is that
(14) implies (F-h) with K = 1 and L = L_mag for all sufficiently large a, and that (F-h)
does not imply (14). At a fixed small a, (14) with a large C need not imply (F-h).
(F-h) does not imply (14) for two reasons: (F-h) with L_mag gives only
|log(Z^k/Z^0)| of order K sqrt(S), and S >= eta^a allows sqrt(S) as large as e^{-Ma/2},
not e^{-sigma a^2}; and (F-h) is compatible with an electric light set, where magnetic twists
are suppressed and |log(Z^m/Z^0)| is large. (An illustration of the second reason,
ARGUED, not needed: deconfined Z_2 at large beta.) With this reading the note's sentence and
"excludes other light-group choices" HOLD.

**5.1.** (15): d/d beta log Z^k = sum_p (eta_p <s_p>_k - 1); subtract the k = 0 case. The quoted
Step 3 ratio 400 (4|beta|) e^{0.06} and the domain |beta| <= 1/4 of Lemma 3.1 are those of
`gap-sc-box.md`. The note states correctly that this is a limit of the estimate, not of the
expansion. HOLDS.

**5.2.** The integrands differ on at most 6 * max(n_rho n_sigma) <= 24 a^2 plaquettes, and
there the ratio lies in [e^{-2 beta}, e^{2 beta}]. So D <= 48 beta a^2. HOLDS. The RP remark
matches `gap-es1-opus.md` Section 6, item 3.

**5.3.** f = prod of tr H_j over loops in k distinct directions is real, bounded by 2^k, gauge
invariant, and in the chi sector (each flip slice meets a loop in its direction once). Given the
exterior, the chosen edges make the holonomies independent Haar. The source's (4) gives a
log-density oscillation <= 2 beta p_B + 4 beta b with p_B <= 4k, b = k, so the conditional
density is >= e^{-12k beta}. E(tr H)^2 = 1, E(tr H)^4 = 2 (chi^2 = 1 + chi_1). So
E_Haar(f^2 - m_2)^2 = 2^k - 2 m_2 + m_2^2 = (2^k - 1) + (1 - m_2)^2, and (17) follows with
||f||_inf^2 ||f||_2^2 <= 16^k. HOLDS. *Remark:* the letter k is used for both the twist and
the number of bits; cosmetic.

**(18).** Ptilde on the chi sector has spectrum in [0, r_chi]. HOLDS.

**(19).** S >= e^{-Ma} gives e^{-a/(4c)} <= S^{1/(4cM)}. For S <= 1 both powers in (1) are
<= S^gamma with gamma = 1/(4c max(1,M)). So p_chi <= 2 Theta_chi S^gamma. The kernel K_eta of
the check has S = eta^a with eta -> 0, so M is unbounded there and no contradiction arises.
HOLDS.

## 6. Section 6: U(1) and cutoff scope

**U(1) logic.** Proposition T1 (`gap-crux-fp.md` 3b.3) refutes a tool only by a model in its
class where its hypothesis holds and the seed fails; T2 shows that "it also works for U(1)"
is no refutation. The note's statements (8), (19) and the spectral comparison are fusion
comparisons. FUSE-suff still needs small even sums and (F-l), which fail in the U(1) Coulomb
phase. So their U(1) extension contradicts nothing. The Z_2 subgroup {+1,-1} of U(1) gives the
same flip argument; no pseudoreality is used; the U(1) moments (E(Re U)^2 = 1/2) and
convolution coefficient differ, so the constants must be recomputed, as the note says. HOLDS.

**Cutoff scope.** eta(beta) = e^{-80 beta} r^4/(4 + 16 r^4) -> 0 as beta -> infinity (r -> 1);
c_2 in (17) contains e^{12k beta}. Theorem SC-F holds only at beta <= 9.3e-16. The bounds are
uniform in the number of sites at fixed bare coupling and give nothing along the ultraviolet
trajectory. The open extension is stated correctly. HOLDS.

## Summary

Checked line by line by Claude Opus 5.5: every mathematical statement of Sections 1-6 of
Codex gpt-6-astra's note holds. Credit Codex gpt-6-astra for the signed port, the winding-area
cancellation without surface enumeration, the Fourier comparison (8), Theorem SC-F with
K = 1, Corollary SC-large, the test (13), the variance bound (17) and the repair (19).
The local witness (2)-(3) is Codex's earlier soft-route result; the polymer bounds are
Opus's `gap-sc-box.md` with Fable's port (P). Three precision or wording corrections:
(i) name the rectangular-box Perron input in Section 2; (ii) at beta = 0 all twelve heavy
weights vanish; (iii) "(14) stronger than (F-h)" holds as "implies (F-h) with K = 1 for all
large a, and is not implied by it". Not checked: `gap-flux-exercise.md` 8.2-8.4 directly,
and the soft-route proof (7)-(10) beyond matching its statement (11) and its density bound (4).

RESULT: Sections 1-6 of gap-fusion-astra.md HOLD (Claude Opus 5.5, line by line): (F-h) with K=1 for all a>=3 at 0<beta<=1/(512*12800^3) and for large a at each beta<1/12800, all twelve heavy crossed sectors, constants re-derived; (13), (17), (19) hold; three wording/precision corrections (Section 2 Perron input on rectangular boxes, beta=0 remark, "(14) stronger than (F-h)" only asymptotically in a); nothing FAILS; no order-one or cutoff-uniform result is claimed or granted.
