# Check of library/pi-native.md

Checked line by line by Claude (Opus 5.5), one reading. Not an audit.
Branch claude/ym4d-hard-route at 73ad79591.
Sources read: N (YM4_1400.tex) 26979-27028, 27666-27722, 28036-28066, 28220-28334,
31540-31669, 31940-32015, 32135-32290, 32598-32805, 32900-32922, 33215-33250,
33300-33372, 33528-33627, 40831, 40955-40975, 41020-41025;
CA-I 13580-13596, 13620-13666, 131568, 131628-131636, 131715-131746, 137556-137572;
122a text 655-700; out-pi.md 159-205, 1044-1106; pi-admit.md 185-215, 440-583;
gates/bz-122-check.md; bz-122.md 50-140.
Grep of N 26800-33700 for "outstanding", "assume", "hypothes", "sketch", "open", "remains".
Not read: SA 10505 and chunk-10.md; N 33528-33645 proof body; N 40831-40937 body.

## Verdict: ADVANCE

Every cited N range says what the note says. All are proved propositions or proofs,
not sketches. The kill test (1)-(4) and identities (5)-(6) are right.
Findings 13, 14 and 16 ask for small repairs. None blocks.

## Findings

### (1)-(2) The N ranges, and proved or assumed

1. **N 26979-27028.** Note 130. CONFIRMED.
   N 26994-26996: "All operators below act on the original graph of sites and bonds inner to Ω_0. The action still contains precisely its inner plaquettes."
   Measures η^4, ξ_y^4, ξ_c^4 and the own-pillar average q are at 27000-27005.
   Hypotheses here: regular branches of the actual means and the curvature ceiling on p ⊂ Ω_0 (27017-27022). The note lists both (149-150).
2. **N 27666-27716.** Note 131. CONFIRMED.
   Bare collar of width 2Hη; "Every bond read by v_b=θv is a bare determining row". The X norm "includes zero-extension boundary jumps".
   27717-27720: "nonbare boxes are inside by separation ... This convention never requires a flat extension across a hole."
   Conditions: K ≥ 64L^2(C_row+1), ρ ≥ CKL, ρ > 4H+C_L. These are separation thresholds.
3. **N 28236-28334.** Note 132. CONFIRMED. Proposition with full proof.
   28262: "This is a boundary estimate for the actual inner action."
   thm:npl-proper-gap: "The form uses the actual inner Wilson Hessian, projected gauge and nonlinear straightened-constraint curvature."
   Class: every depth, compatible volume, separated aligned geometry, ρ ≥ ρ_*, sup L(p)^2|F_U| ≤ κ_*, sup ξ^3|ω| ≤ γ_*. Real fields.
   The proof passes to a finite periodic cover; no global gauge or topology restriction (28333).
4. **N 31558-31669.** Note 133. CONFIRMED.
   A_F is "the full Feynman operator"; 𝒟_U is "the actual inner Wilson Hessian".
   Compression: "its contribution is its full row evaluated on the zero extension. It is not replaced by a renormalized partial average."
   "It also retains which original inner plaquettes are present."
5. **N 31944-32015.** Note 134, 145. CONFIRMED.
   31950-31958: bare-layer stencil force "bounded by C/m times the bare mass energy directly".
   31966-31973: "Missing exterior plaquettes are not filled in, and no local Coulomb gauge across that boundary has been assumed."
6. **N 32138-32261.** Note 135. CONFIRMED. Proposition lpw:positive-local-walks with proof.
   Exact walk series; coefficients holomorphic in local data; uniform weighted cell norm; real domain and small complex C^1 tubes.
   32262-32263 adds: equality with a separately prescribed signed or absolute-contour precision "requires that precision's gauge comparison". The note's section 5 keeps this distinction.
7. **N 32279-32286.** Note 50, 153. CONFIRMED.
   "Neither is silently identified with a prescribed history size M_h ... Admission of a separately fixed history geometry remains a comparison to be checked."
8. **N 32633-32715.** Note 136. CONFIRMED. Proposition with proof.
   Exact local carrier families for M^{-1}, Θ^{-1}; uniform in depth, volume, admitted geometry; common complex C^1 tube.
   Separation (cci:actual-separation-admission): ρ ≥ max{ρ_0, C_L L M_c, 64(log L)/s_*}. The spatial rate s_* is decreased explicitly (32624-32626).
9. **N 32717-32800.** Note 137, 146, 153. CONFIRMED. Corollary with proof.
   Applies to T_0^n = Ξ_Γ^2 a_f^{1/2} Q G_0 Q^♯ a_f^{1/2} Ξ_Γ^{-2}, with the Woodbury G_0. 32797: "The proof does not identify that tile with M_h."
10. **N 33223-33248.** Note 138. CONFIRMED.
    ncw:zero-current-Woodbury and ncw:G0-family. "There is no replacement of the actual projected precision by a periodic model."
11. **Other rows (33321-33360, 33528-33645, 40831, 40955).** Note 139-142. CONFIRMED where read.
    33604-33608 gives Ξ^3{(QG_iQ^♯)^{-1}-a_f}Ξ^{-1} = c_a(T_i^{-1}-1)c_a. This independently matches (5).
    40971: "No algebraic inverse identity is claimed for the decorated maps at s≠1." 41024: "no identification with a separately prescribed history partition."
12. **Proved, not sketched.** All ranges sit in section "Background fields and constrained inverses" (N 3543-46266).
    The grep found no "Proof outstanding" or sketch marker in N 26800-33700. Hits for "assume" are local proof steps or disclaimers (27017, 31973, 32829, 33373).
    pi-admit.md's "sketch" refers to N 16964-16977, not these ranges. Note 47 is right.

### (3) Kill test and identities

13. **(1)-(2).** Note 68-88. CONFIRMED.
    At U=1 with bare rows: Q=Q'=I, so PI's P = G'(G'^2)^{-1}G' = I and R=0 (out-pi 187-191). Δ_a = d_P^T d_P + η^{-2}I.
    Four edges per plaquette and six plaquettes per bond in 4D give d^Td ≤ 24η^{-2}. The normalization matches pi-admit (17).
    Small repair: line 117 writes (1-Cκ). N 28257 has (d_* - Cκ), d_* = inf ξ_c^2 a_f. It equals 1 only under a_f = m^{-2}. Say so there.
    N's estimate is for v supported in the bare outer collar. In the all-bare model every field is such, so the use is valid.
14. **(3)-(4).** Note 90-114. CONFIRMED.
    (I+ss^T)^{-1} = I - ss^T/(1+4). Spectrum of η^2Δ in [1,25] gives ‖E_0‖ ≤ 12/13.
    Entry bound: (η^2/13) Σ_{n≥r}(12/13)^n = η^2(12/13)^r. Correct.
    Neumann step: ‖Δ^{-1}‖ ≤ (4/3)η^2 and ‖Δ^{-1}E‖ ≤ 1/3 give 2η^2. Correct.
15. **(5)-(6).** Note 170-197. CONFIRMED.
    N 33323-33326: Q_n = Ξ_Γ^2 a_f^{1/2} Q, Q_n^♯ = Q^♯ a_f^{1/2} Ξ_Γ^{-2}, with Ξ_Γ b(c) = ξ_c b(c) (N 28476).
    With a_f = m^{-2}, Q_n = mQ and Q_n^♯ = Q^♯ m^{-3}. This is PI's K = mQ, K^T = Q^T m^{-3} (out-pi 172-173).
    Then QG_0Q^♯ = m^{-1}T_0m^3, so q_0 = m^{-3}T_0^{-1}m. Dividing the counting entry by m_{c'}^4 gives (6). Same as out-pi (8.1).
    N's a_f is c_y ξ^{-2} with c_* ≤ c_y ≤ c^*. PI's a = m^{-2} is the case c ≡ 1, inside N's class.
    UNCLEAR, minor: N calls ♯ the Hilbert adjoint at real points; PI uses bilinear transposes. They agree at real points. The holomorphic families force the bilinear continuation, but the note should say so.
    Raw datum: CA-I 13643 defines H_0 = G_0Q^*q_0 ℓ^{-1}. N 33366: H = GQ^♯S_J^{-1}. At J=0, H_0 = Hm^{-1}. CONFIRMED.
16. **(7).** Note 199-223. CONFIRMED with a repair.
    The algebra is right. But the ratio bound with factor L and rate (log L)/g is out-pi (8.2), proved in PI's contour metric.
    In N's layer metric use ncw:scale-reserve (N 32910-32912): ratio ≤ C_L e^{ε_g d}. Replace L by C_L and (log L)/g by ε_g, or prove (8.2) in N's metric.

### (4) The item-10 obligation

17. **Item 10 text.** Note 256, 292-297; CA-I 131568, 131725-131746. CONFIRMED, but incomplete.
    I 131568: "The following statements are used as inputs." Item 10 asks for:
    (i) the layer theorem at B_Z localised to Z, at γ_0^(k), "with the same constants";
    (ii) H_σ holomorphic on D_H(Y) ⊃ D♭_{n+1}(Y)|Y with the stated ambient condition (K_109 on X_a; G_1(B_τ) with its strata);
    (iii) H_σ = H_Z^(j) of 122a (1.58) at real points;
    (iv) |H_σ| ≤ H_max = L C_F B_♯ e^{4κ_1} K_f ᾱ^fat_k e^{-4R_k}, and |δ_{b'}| ≤ 2H_max/g_j.
    The final open-input paragraph names (ii) and (iii). Line 256 names H_max. Neither names the shift bound or "the same constants".
    Repair: list (i)-(iv) in the open-input paragraph.
18. **Constants.** Note 240-249. CONFIRMED.
    N's ρ_*, the enlarged tile M_c and the decreased rate s_* are N's own. The account's M_1 collar must meet them. The note says (8) is only a comparison.
    The bare outer band exists: bz-122.md 112-113 and (4) give grade 0 on D_0\D_1 with D_0 = X. Its width M_1ℓ_1 must cover N's 2Hη collar.
19. **Context omitted.** CA-I 131633 marks the consuming T-step layer lemma "Stated; proof incomplete at (∗)". I 137566-137567: B_Z "lies outside the geometry" of the input pair spaces.
    The note does not cite these. They do not change its claim. Add one line.

### (5) Consequence for C0-SUP / C0-ETA / BZ-CUT

20. **For item 10's inverse: yes, the whole-action line is not needed.** CONFIRMED with one proviso.
    pi-admit.md 196-198 restricts C0-SUP to entries that require whole-action PI. bz-122-check finding 10 shows item 10 is stated natively. BZ-CUT already stopped at (b).
    N supplies the native inverse and local expansion on its class. So C0-SUP and C0-ETA need not be closed for item 10.
    Proviso (UNCLEAR): item 10 fixes H_σ = H_Z^(j) of 122a (1.58). 122a text 681-686 says only that it is analytic in U restricted to Z, via "the formula corresponding to (1.41)".
    bz-122-check finding 11(b) notes that Balaban's Dirichlet compression keeps plaquettes through boundary bonds unless Ω_0 is inset.
    If H_Z^(j) is built that way, matching it to N's inner-action object needs pi-admit (18). That is a Schur complement with an outer inverse, which is a comparison estimate.
    So note 297's "not another native inverse estimate" is exact. The broader "not a new inverse estimate" holds only if H_Z^(j) is the inner-action object on N's graph.
21. **Not globally unnecessary.** Note 258. CONFIRMED.
    GW1 (out-gw1.md 31-77, per the note; not read here) and the other fresh settings in the digest's section 5 still use the whole-action PI graph. C0-SUP remains their supplier.
22. **Papers.** Note 164 says the paper directory was absent. /Users/jonreilly/ym4d-lead/papers holds cmp122a/b text and PDFs. Not load-bearing.
