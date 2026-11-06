lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-06T16:30Z

# P9 witness ports: one line-by-line check (row 341)

Started 2026-11-06T04:30Z. Pinned at commit 50b8bafeb. Work in progress: sections are added as the check runs.

Scope: `library/port/p9-witness.md` (C9 8.18:thm-torus-witness, C10 8.22:thm-volume-transfer, C11 8.1:thm-two-point-witness, with 8.22:cor-transfer-depth-floor and cor-reference-torus-kernel) and `library/port/p9b-extraction.md` (C5 8.2:prop-gaussian-extraction). Both ports were written by Codex. Sources: the Sussman-Alpoge complete account at 31a47c543775 (CA-III), fetched by URL into a scratch folder.

## 0. Sources and statement blocks

- CA-I, CA-II, CA-III and the outline were fetched at 31a47c543775 into a scratch folder. Their SHA-256 values equal the table at p9-witness.md lines 13-18.
- The anchors hold: 8.1:thm-two-point-witness at II:71279, 8.2:prop-gaussian-extraction at II:77279, 8.22:thm-volume-transfer at II:141540, 8.22:cor-transfer-depth-floor at II:142317, 8.22:cor-reference-torus-kernel at II:142607, 8.18:thm-torus-witness at II:144922.
- Each of the nine `latex` blocks in p9-witness.md was compared with CA-II, character for character. All nine are verbatim: C9 = II:144922-145029, C10 = II:141540-141583, C11 = II:71279-71367, the four excerpts at II:73250-73333, cor-transfer-depth-floor = II:142316-142371, cor-reference-torus-kernel = II:142607-142632.

## 1. C10 (8.22:thm-volume-transfer), p9-witness.md lines 359-443

Source proof: II:141585-141852, read in full.

Result: **first failing step none.** The port follows the source step for step: placement, the reflected source W_z and its two mirror conditions, the chessboard bound (VT1), four applications of the trace lemma with k = L^(m-m') odd, the stability and zero-source bounds (VT2), the one counterterm E'' formed on T_m', the bounds |h_m|, |h_m'| <= Q_star, and the Schwarz-Cauchy step.

Filled steps, each redone by hand:

- F10.1 (line 420). For finite K the lattice is finite and O(w_z) = z_1 O(F_1) + z_2 O(F_2) is bounded in U on compact z-sets. So Z_v(w_z) is entire, and h_v is holomorphic on D because E'' is (per-ball bound, part (i), inside H-VT(c)). Correct.
- F10.2 (lines 422-433). Fix z in D with N(z) = |z_1|a_1 + |z_2|a_2 > 0 and put phi(t) = (h_v(tAz/N(z)) - 1)/(Q+1) on |t| < 1. Then |phi| <= 1 and phi(0) = 0, so Schwarz gives |h_v(z) - 1| <= (Q+1)N(z)/A. On the closed polydisc |z_i| <= b_i = A/[2a_i(2Q+2)] we get N(z) <= A/(2Q+2) < A, so |h_v - 1| <= 1/2 and |Log h_v| <= sum 2^-n/n = log 2. Cauchy: |d1 d2 Log h_v(0)| <= log 2/(b_1 b_2) = log 2 (2Q+2)^2 (2r/rho)^2 a_1 a_2. Two volumes give the factor 2 log 2 of C_VT. Correct. The case a_i = 0 is also correct: then F_i = 0, and neither w_z nor E'' depends on z_i.
- F10.3 (line 441). d1 d2 log Z = Z_12/Z - Z_1 Z_2/Z^2 at z = 0 is the connected two-point function. Correct.

Minor wording, not failures:

- Line 363: "the least power of L above 16(R+1)". The source (II:141587) has ">=". Nothing depends on this.
- Line 363: the port credits the invariance of the sharp norms to `1.1:lem-invariance`. The source (II:141598-141600) uses the translation invariance of the sup norm and the Lipschitz constant. The fact is true either way.
- Lines 387-391: the port does not repeat that, for r = 2, the upper stability bound is applied to the real system of four functions at (z, conj z) on the polydisc of radius rho/2 (II:141700-141702). Line 371 records it. Nothing is lost.

Standing: C10 is a proved implication from H-VT (a)-(f), as the account states. The port adds no unproved step.
