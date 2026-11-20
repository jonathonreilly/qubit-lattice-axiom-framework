lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-21T00:37Z

# gap-mini-solve-am-opus (FINISH row 1275): plain brief, the four-dimensional SU(2) mass gap

Worker: Claude Opus 5.5 (max reasoning), Mac mini worker 1, branch `claude/ym4d-hard-route` pinned at b013734a1.
No commit, no push (a relay copies this file). Labels: PROVED, ARGUED, GUIDE, OPEN.

## 0. Status log

- 2026-11-20T12:37Z (date -u): file created; reading the row, `parts/gap.md`, the newest RESULT lines and row 1218's reading
  (`library/prior/gap-onebound-read-sol.md`) before choosing the item.
- 2026-11-20T12:39Z (date -u): read FINISH.md rule sections (L1-84, L299-360), GOAL.md, `parts/gap.md` L1-104, the RESULT lines of rows
  1250-1276, and row 1218's reading `library/prior/gap-onebound-read-sol.md` (sections A, B, comparison, outcome). Branch tip
  (88b2846ae, 12:38Z) holds no file yet for the concurrent rows 1268-1272.

## 1. How best to attack it (judgement, ARGUED; written 2026-11-20T12:54Z by date -u)

**What the record fixes (cited, not re-derived).** The Jaffe-Witten gap clause of the lane reads one infrared input,
(N-phys) (rows 1161, 1179; check 1232), equivalently a seed at one coupling modulo the ultraviolet carry (rows 916-917
(ONE-K), 1233 Proposition 3.7 with check 1242, rows 1255, 1256, 1260, 1267). Row 1258 (Lemma WS, Proposition RR) turned
the two one-scale mixing forms (W) and (SL)/(RR) into PROVED sufficient inputs at ONE coupling; row 1259 (Lemma CD) priced
the count half. The published work of row 1218 adds no weak-coupling infrared input: six authors' thermal criterion A-B*
is the lane's full periodic seed with a shape window (row 1218, "the same thermal-purity mechanism"); B's Corollary 166 is
the near-Haar property of long straight transports (row 1220, Lemma NULL), a perimeter-law ultraviolet effect; Zeng's
(TUN) is the gap itself (row 1251). No engine for the band is on file (about 45 route families with a named failing
step; `parts/gap.md` methods 19-36; rows 1188-1267).

**Registry screen run for this row (grep counts of files in `library/gap-*.md`, `library/prior/gap-*.md`,
`parts/gap.md`).** Every mechanism I could name for the band is already on file: spectral independence 7, Gribov 28,
abelian projection 11, Chatterjee 90, Adhikari 30, Sheffield / surface sums 37 / 19, tensorization 11, disagreement
percolation 20, OSSS 6, random current 11, Mack-Petkova 26, Lieb-Robinson 5, Kotecky 21, Witten Laplacian 14, Helffer 24,
Singer 26, O'Neill 16, orbit space 31, Bakry 99, Brascamp-Lieb 19, Holley-Stroock 17, Zegarlinski 24, Kogut-Susskind 22,
Peter-Weyl 36, Hagedorn 5, Bachas 11, glueball 74, string tension 83, Polyakov loop 30, Svetitsky 5, centre symmetry 38,
Knabe 31, Mozgunov 20, Martinelli 35, Theorem 66 (B's BP consumer) 9. A blind screen is waste here, as rows 1188-1267
recorded.

**Judgement.** I do not have an engine for the band, and I do not offer one. The best use of one session is to close an
input that any future proof of the base datum must pass through, with a statement that can be checked. Two siblings are
running on the carry at this pin ((FC-1)/(FC-T) of row 1267 is the natural next item of Mac mini worker 2, row 1268;
H-C items of the account are worker 3's line, rows 1264, 1276). The carry input named OPEN by the newest cross-provider
check and owned by no row is **(V9), the physical normalisation bound** (check 1263 on row 1255: "reading (R) FAILS to
establish the physical normalization"; check 1266: "OPEN: ... the physical normalization bound (V9)").

**Item.** (V9) of row 1255: with consistent chapter 9 representatives on both tori, a uniform bound
sup_d |Delta E9(d)| <= eta_9 on the two-torus defect of the representatives' own bare constants. Row 1255 Proposition D2
(HOLDS, check 1263) gives (V9) with eta_9 <= eta_vac(m) + eta_det(m) when E9 = E_m (the energy constant of CA-I Lemma
4.36(a)), and D = 0 when E9 - E_m depends on the torus only. So (V9) reduces to one question about the account's text:
**for which normalisations of the chapter 9 representatives does the account's zero-source comparison
(`9.1:cor-sourced-integrals`) hold, and does that set contain E_m or a torus-only shift of it?** If the comparison holds for
every value of the free positive constant (III:18249-18250, 18301-18302), (V9) follows from D2(b). If it holds only for
one constant fixed by the proof, (V9) must be proved for that constant.

Moves: the carry's input list (Proposition 3.7 of row 1233 as corrected by checks 1242, 1263, 1266) loses (V9) or gains a
precise replacement. If it fails, the carry needs a normalisation-matching lemma before any base datum can be carried,
and the lead should know that now. Rule 0a: `library/open-core.md` has no gap-lane entry for (V9) (grep below, Section 2);
FINISH rows name (V9) only in rows 1255 (author), 1263 and 1266 (checks); no queued row owns it.

**Plan.** Section 2: fetch the account (CA-I, CA-III at 31a47c543775) into a scratch folder and quote the 9.1 comparison,
the representatives' definition and the free constant. Section 3: the lemma (constant invariance, or the precise failure).
Section 4: state of the carry after this row and the RESULT line.

## 2. What the account says about the chapter 9 normalisation (READ; written 2026-11-20T13:01Z by date -u)

Source: Sussman and Alpoge's complete account at 31a47c543775 (CA-I, CA-II, CA-III; with Claude and Codex as authors
of its text; after Balaban), fetched by raw URL into a scratch folder outside the repository. Line numbers below are
`grep -n` anchors in those files.

**2.1 The bare constant is free in three places, fixed in a fourth.**
- CA-I 1.1:def-wilson-action (I:447-480): rho_0(U) = exp[-g_0^(-2) A(U)], no constant (I:479).
- CA-II correlation-theorem setting (II:730-741): rho_0^w = exp[-A(x_0 - w, U) - E], "E a constant, independent of U and
  of z, entering the exponent of the bare density additively"; clause (iii) (II:2930-2935): int rho_k^w dV_k =
  int rho_0^w dU at every level.
- CA-II 8.22 (II:140873-140934): Z~_m(v) = e^(-E_m - Ecal_m(v)) Z_m(v), E_m = sum_(j<K) E^(j)_vac(T_m, T_m) is "Balaban's
  normalisation constant of the bare density rho_0 = exp[-x_0 A(U) - E_m]", and clause (b) gives
  e^(-C_low (2L^m)^4) <= Z~_m(0), |Z~_m(v)| <= e^(E_+^# (2L^m)^4).
- CA-III 9.1 (Notation 9.1:not-centre-normalisation, III:11804-11870; Remark 9.1:rem-centre-normalisation-b,
  III:18244-18302): Z^c(c^c; v) = e^(Ecal^c(v)) Z~^c(v) with Ecal^c(0) = 0, "each Z~^c is the representation given by the
  correlation theorem at the run's own real centre", and "The normalisation admits exactly one free positive constant
  for each run and each centre" (III:18249-18250; again III:18301-18302).
- CA-III 9.8 Definition 9.8:def-partition-closeness (III:53385-53442): "The normalisation fixed for each run and each
  centre is the one in which the value of Z~^c at the zero source is Z~^c(0) = 1/B", and h^c := Z~^c / Z~^c(0) = B Z~^c.

**2.2 What the comparison bounds.** Theorem 9.1:thm-last-lattice-comparison (III:17913-17990) bounds, in "the
normalisation (9.1:eq-centre-normalisation-a)", sum_(h aligned) ||tau_h^B - tau_h^A|| + (unpaired terms) <= eps_n A^#,
eps_n <= C_TC(g, N_w) e_w, e_w = rho^(n-w) + Pi_n; Corollary 9.1:cor-sourced-integrals (III:18136-18221) sums the terms:
|Z~^B(W^B(z)) - Z~^A(W^A(z))| <= eps*_n A, "and the same bound holds at the zero residual source".

**2.3 Check 1263's point, re-read.** Under the 9.8 choice Z~^c(0) = 1/B the zero-source comparison is 0 <= eps*_n A,
true and empty, and Lemma D0 of row 1255 gives E9(d; T) = log Z_T(d) + log B, so Delta E9(d) = Phi(d) + Delta log B:
(V9) is then the seed itself (`library/gap-opus-batch5-check-astra.md` L107). So the carry has physical content only
if the 9.1 comparison holds in a normalisation whose constant has a small two-torus defect, for example Balaban's E_m
(Proposition D2(b) of row 1255, HOLDS in check 1263).

**2.4 Two structural facts of the 9.1 proof (READ).**
(i) The loads that control the comparison (9.1:eq-centre-normalisation-d, III:12063-12075) are built from the
seminorms S^+_i[F] = sup_X e^(kappa_F d(X)) sup |F^B - F^A| over localisation domains X of each level (III:12025-12030),
plus boundary, coupling and shift differences. There is no load term for a run-dependent number that is not a sum of
domain-local slot values.
(ii) The stored array x^c, on which one run-independent assembly formula P_h acts (tau_h^c = P_h[x^c], III:11960-11975),
contains "the pieces that do not depend on z but depend on the run, namely the vacuum constants" (III:11973; also
III:59802 and III:18295-18296), and these are "counted in the total load" (III:18247-18249).

Next step (Section 3): decide what (i)-(ii) imply for the free constant, as a statement with proof.
