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
- 12:51Z-13:00Z: item chosen ((V9), Section 1); complete account CA-I, CA-II, CA-III fetched into a scratch folder.
- 13:00Z-13:10Z: Sections 2-4 written; every CA line anchor re-checked with grep -n -F (nine corrected in place).

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
(i) The loads that control the comparison (9.1:eq-centre-normalisation-d, III:12045-12058) are built from the
seminorms S^+_i[F] = sup_X e^(kappa_F d(X)) sup |F^B - F^A| over localisation domains X of each level (III:12016-12024),
plus boundary, coupling and shift differences. There is no load term for a run-dependent number that is not a sum of
domain-local slot values.
(ii) The stored array x^c, on which one run-independent assembly formula P_h acts (tau_h^c = P_h[x^c], III:11961-11975),
contains "the pieces that do not depend on z but depend on the run, namely the vacuum constants" (III:11973; also
III:59802 and III:18295-18296), and these are "counted in the total load" (III:18247-18249).

Next step (Section 3): decide what (i)-(ii) imply for the free constant, as a statement with proof.

## 3. The normalisation in which the account's chapter 9 comparison is proved, and (V9) (written 2026-11-20T13:07Z by date -u)

Notation. One torus T at a time; A_T = e^(E_+^# N_w^4), B_T = e^(C_low N_w^4) are the volume constants of the last
lattice (III:12140-12146; II:140907-140911, 140926-140933). For a run c of the 9.1 pair let Z~_0^c denote the
correlation theorem's own expansion, Z~_0^c(v) = sum_h tau_h^c(v)(V_w), and S^c := Z~_0^c(0). A "normalisation" of the
pair is a pair of constants lambda^A, lambda^B > 0, with representatives lambda^c Z~_0^c.

**3.1 Proposition N1 (rigidity of the free constants; PROVED, elementary).** Suppose the zero-source bound of
`9.1:cor-sourced-integrals`, |lambda^B S^B - lambda^A S^A| <= eps* A_T, holds for the pair (lambda^A, lambda^B) and
also for (lambda^A, mu lambda^B), and suppose lambda^B S^B >= 1/B_T (the window lower bound of II:140910). Then
|mu - 1| <= 2 eps* A_T B_T.

Proof. Subtract the two bounds: |mu - 1| lambda^B S^B <= 2 eps* A_T, and divide by lambda^B S^B >= 1/B_T. QED

So once 2 eps* A_T B_T < 1, the comparison fixes the ratio lambda^B / lambda^A up to the factor 1 +- 2 eps* A_T B_T.
The sentence "The normalisation admits exactly one free positive constant for each run and each centre" (III:18249-18250,
III:18301-18302) can therefore not mean two independent constants INSIDE the comparison; at most one common factor of
the pair is free there. (It is true of the three normalisation conditions alone, which is what the remark's proof
shows, III:18274-18302.)

**3.2 Lemma N2 (which normalisation Theorem 9.1 proves; the facts READ, the deduction ARGUED).** The printed proof of
`9.1:thm-last-lattice-comparison` compares the correlation theorem's own terms, with no per-run factor:
- the aligned-terms lemma (III:17381-17470) defines "tau_h[x; t^A] := P_h[x], the assembly formula of the label h
  applied to x at the ramps t^A" (III:17422-17423) and compares x^A with x^B along x^(lambda, eps) = x^A +
  lambda(x^B - x^A) + eps W^(z) (III:17429-17431); the integrand is "entire in the entries of the array" (III:17441);
- its modulus bound (9.1:eq-aligned-terms-3), sum_h |mu|^(m_a(h)) ||tau_h[x^(lambda,eps)]|| <= A^#, is "the proof of the
  upper member of the torus bound of the correlation theorem" with Balaban's bounds CMP 119 (2.43)-(2.49) and CMP 122b
  (1.68)-(1.69), (1.79) (III:17472-17480);
- the unpaired-labels lemma assumes "in each of the runs A and B: the torus bound of the correlation theorem, in its
  modulus form" (III:17798-17799);
- the array x^c holds the run-dependent source-free pieces "namely the vacuum constants" (III:11973) as stored units of
  localisation domains, and the loads that control the dial (9.1:eq-centre-normalisation-d, III:12045-12058) are the
  domain-wise seminorms S^+_i[F] = sup_X e^(kappa_F d(X)) sup |F^B - F^A| (III:12016-12024) plus boundary, coupling and
  shift differences; the envelope lemma bounds exactly these (III:17138-17230).

Deduction. No step divides a run's terms by a run-dependent number, and no load controls a run-dependent number that
is not a sum of domain-wise stored units. So the bounds of the theorem and of its corollary hold for lambda^A =
lambda^B = 1, that is for the correlation theorem's own representatives Z~_0^c, whose normalisation is the one in
which the torus bound is stated: by 8.22 (II:140916-140924), Z~(v) = e^(-E_m - Ecal(v)) Z(v) with E_m "Balaban's
normalisation constant of the bare density". By Proposition N1 the comparison then holds for no other relative
normalisation (up to 1 +- 2 eps* A_T B_T).

The alternative reading, that the 9.8 constant (Z~^c(0) = 1/B, III:53392-53400) is used inside 9.1 as a stored
"vacuum constant", would put the mark log(S^B / S^A) into the loads; no term of 9.1:eq-centre-normalisation-d and no
step of the envelope lemma bounds it. Under that reading the printed proof would be incomplete. Lemma N2's reading is
the only one under which it is complete. (ARGUED: this is a statement about the account's text, with the lines above.
The case of a constant carried as a stored unit is traced in the next paragraph.)

*A run-dependent global constant cannot be a dialled slot (ARGUED from III:17556-17580).* The first variation in the
aligned-terms proof is a Cauchy estimate: G_z is holomorphic in the dial eps of class z on |eps| <= Lambda_z =
E_1^z / [[delta]]_j, with modulus at most B_z = q_a^((k-j-1)_+) A^# there, so |V^(z)| <= B_z / Lambda_z
(III:17556-17580). Suppose a run-dependent constant c multiplied every term of a run by e^(-c) and were filed as stored
units of a level j. (a) Filed over the N_j domains of level j with mark delta c / N_j each: the load is of order
e^(kappa d) |delta c| / N_j, the dial radius moves c by about E_1^z N_j e^(-kappa d), and the modulus bound
(9.1:eq-aligned-terms-3) would need e^(E_1^z N_j e^(-kappa d)) <= A^# B_T, false once N_j (which grows like the fine
volume) is large, while A^# B_T depends on N_w only. (b) Filed as one unit of the whole torus of level j: the
modulus bound survives, but the class's contribution B_z / Lambda_z is of order A^# e^(kappa d(T)) |delta c| / E_1, so
the theorem needs |delta c| = |log(S^B / S^A)| small, a load that the envelope lemma (III:17138-17230) does not bound.
So in the printed proof the per-run constant is not dialled, the compared terms carry equal constants, and (b) is the
only alternative, with an incomplete proof.

**Corollary N2' (dichotomy; ARGUED from N1 and N2).** Either Theorem 9.1 is proved for the correlation theorem's own
representatives (lambda^A = lambda^B = 1), and then its corollary at the zero source is the comparison
|S^B - S^A| <= eps* A_T of the Balaban-normalised partition functions; or the printed proof uses another relative
normalisation, and then (Proposition N1) it needs a bound on the mark log(S^B / S^A), which is the same comparison and
which no load of 9.1 supplies. In both cases the zero-source comparison of Balaban-normalised partition functions is
part of what Theorem 9.1 provides once it is complete. So (V9) is not an input of the carry beyond 9.1 itself.

**3.3 Lemma N3 (the 9.8 normalisation is a downstream rescaling; PROVED).** Suppose |Z~_0^B(W^B(z)) -
Z~_0^A(W^A(z))| <= eps* A_T for all z in P_IR and at the zero source, and S^A, S^B lie in [1/B_T, A_T]. Put
zeta^c := Z~_0^c / (B_T S^c) (the 9.8 representatives, zeta^c(0) = 1/B_T). Then
|zeta^B(W^B(z)) - zeta^A(W^A(z))| <= eps* A_T (1 + A_T B_T).

Proof. B_T (zeta^B - zeta^A) = (Z~_0^B - Z~_0^A)/S^B + Z~_0^A (S^A - S^B)/(S^A S^B). The first term has modulus at most
eps* A_T B_T, the second at most A_T eps* A_T B_T^2. Divide by B_T. QED

So 9.8's closeness (9.8:eq-partition-closeness-a, with C_TC allowed to depend on N_w and g) follows from 9.1 in the
correlation theorem's normalisation, while its zero-source line is empty (both sides equal 1/B). This matches the
account's own conversion constant C_*(N_w) = 2 C*_TC Q_w (1 + Q_w), Q_w = A B, for the statements that apply the
corollary to increments (III:18223-18233). For the carry the consequence is: cite `9.1:cor-sourced-integrals` at the
zero source in the correlation theorem's normalisation, never the 9.8 Definition (check 1263 L107 is right that the 9.8
form carries no zero-source information).

**3.4 Proposition V9 (PROVED GIVEN the inputs listed, among them Lemma N2's reading).** Inputs: Lemma N2's reading (Theorem 9.1 proved for the correlation theorem's own representatives); Theorem `9.1:thm-last-lattice-comparison` with its
hypotheses (a)-(e) on every edge of the chain and on both seed tori (hypothesis (e) is the account's OUTSTANDING
`9.1:prop-blind-site-expansions`); 8.22's identification of the correlation theorem's normalised partition function
and its clause (b) (II:140873-140934); row 1233 Lemma 3.6 and row 1255 Lemma D0, Corollary D1, Proposition D2(b)
(HOLD in checks 1242 and 1263). Take as chapter 9 representatives on each torus the correlation theorem's own
expansions, S_9(d; T) := Z~_0(d; T)(0). Then:
(i) the representatives are consistent: S_9(d; T) is the run's own total at the zero source, sum_h tau_h(V_w) =
int rho_k dV_k at the stop (the expansion is exact, II:2935, and the corollary sums each run's own terms, III:18166-18175),
so it does not depend on the partner's ramps or labels (the B-terms formed with A's ramps enter only inside the proof,
III:17396-17399); the run itself, with its stop on the last lattice of T and the scaffold Theta_X read from X alone
(III:11934-11936), is the same on the two edges that contain it, so S_9(pi d; T) is one number on (d, pi d) and on
(pi d, pi^2 d);
(ii) on each edge of shorter length n and each torus, |log S_9(d; T) - log S_9(pi d; T)| <= eps*_n A_T B_T (from the
corollary, the window lower bound S >= 1/B_T, and |log x - log y| <= |x - y| / min(x, y)); hence row 1255's edge bound
holds with b_n := eps*_n (L^4 A_(T_s) B_(T_s) + A_(T_b) B_(T_b));
(iii) E9 = E_m, so by Proposition D2(b) D = 0 and (V9) holds with eta_9 <= eta_vac(m) + eta_det(m);
(iv) by Corollary D1, Phi(d) <= Phi(d_0) + sum_(n >= K_0) b_n + 2 (eta_vac(m) + eta_det(m)).

Proof. (i) from the definitions cited; (ii) as stated, using Lemma N2 for the normalisation; (iii) D2(b); (iv) D1 with
(ii)-(iii). Summability of b_n is that of eps*_n <= C*_TC(N_w; g) e_w, e_w = rho^(n-w) + Pi_n, as in row 1233 Lemma 3.5
(HOLDS in check 1242). QED

One point of reading stays: 9.1 stops at the level k = n - w, so the constant subtracted in Z~_0 at the stop is the sum
of the vacuum (and Gaussian) constants of the levels below the stop. The two-torus defect of any such partial sum is a
sum over wrapping domains with the decay of 8.22 (b), so Lemma 3.6's bound applies level by level; I did not re-derive
8.22's lemma for partial sums (ARGUED, low risk).

**3.5 If the identification of 3.2 were wrong (fallback; ARGUED).** If the correlation theorem's expansion carried a
bare constant E^c other than E_m^c, Lemma N2 still says that 9.1 is proved for that constant, the same on the two runs
of a pair. Then (V9) holds by Proposition D2(a) when E^c - E_m^c depends on the torus only, and by the wrapping argument
of 8.22 (not re-derived here) when E^c - E_m^c is a sum of domain-wise, translation-covariant pieces with the decay of
8.22 (b). A constant of neither kind would have to be chosen run by run; by Proposition N1, 9.1 would then fix its
edge-to-edge changes to within 2 eps* A_T B_T, and only the torus-only part could stay free.

## 4. State of the one-cutoff carry after this row, and what stays open (written 2026-11-20T13:09Z by date -u)

**4.1 The carry's input list.** Row 1233 Proposition 3.7, as corrected by checks 1242, 1263 and 1266 and by rows 1255,
1256, 1260 and 1267, reads the following. Status after this row:

| Input | Before this row | After this row |
|---|---|---|
| (V9), the physical normalisation bound (row 1255; open per checks 1263, 1266) | OPEN | PROVED GIVEN Lemma N2's reading (Proposition V9); by Corollary N2' not an input beyond Theorem 9.1 itself |
| Which normalisation the carry cites | 9.1 or 9.8 (unstated) | 9.1's corollary at zero source in the correlation theorem's normalisation; never the 9.8 Definition (Lemma N3) |
| Consistent representatives on both tori (row 1255 D1; check 1266 "single normalization per datum and torus") | required | met by the correlation theorem's own representatives (Proposition V9 (i)) |
| Hypotheses (a)-(e) of 9.1 on every edge and both tori; (e) = `9.1:prop-blind-site-expansions` | OPEN, (e) OUTSTANDING in the account | unchanged |
| (FI) / (FC) / (FC-T), the scaffold comparison (rows 1260, 1267) | OPEN | unchanged (not attacked here) |
| (DET)'s inputs for eta_det (rows 987-994 with checks) | as recorded | unchanged; Proposition V9 (iii) reads them through D2(b) |
| Summability of eps*_n (the power-law floor Pi_n) | row 1233 Lemma 3.5, HOLDS (check 1242) | unchanged |
| The infrared seed at the base datum, Phi(d_0) <= phi_* - sum b_n - 2(eta_vac + eta_det) | OPEN | OPEN, the crux |

**4.2 What this row does not do.** It does not prove the mass gap and proposes no engine for the band (Section 1). It
does not re-check Theorem 9.1 or its hypotheses; it reads which normalisation the printed proof uses. It did not trace
the account's first-variation statement for a constant spread over a fine level (3.2, last paragraph); that is the
step a checker should read first. No numeric run was made (the statements are about the account's text and
elementary inequalities). No other file was edited.

**4.3 For the lead (check request).** One cross-provider check of Section 3: (1) Proposition N1 and Lemma N3 (short,
elementary); (2) Lemma N2's reading against III:11857-11866, 11961-11975, 12016-12058, 17422-17447, 17472-17480,
17798-17799, 18223-18233, 18244-18302 and II:140873-140934, and Corollary N2' (the dichotomy); (3) Proposition V9
(i)-(iv) against row 1255 D0, D1, D2(b) and row 1233 Lemmas 3.5-3.6. Points most likely to fail: the "no run-dependent
factor" reading of N2 (a bare constant carried as a stored unit of a fine level), and V9 (i) (whether the run at a
datum is literally the same object on its two edges when the paired scaffolds are read).

**4.4 Credits.** Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text (complete account
CA-I to CA-III at 31a47c543775): the correlation theorem, chapter 9's comparison and normalisation, the 8.22 lemmas.
Tadeusz Balaban: the construction and normalisation constant those statements rest on (CMP 119, 122). The lane: row 1233
(Proposition 3.7, Lemmas 3.5-3.6), row 1255 (D0, D1, D2), checks 1242, 1263 (its L107 finding that the 9.8 form is
empty at zero source started this row's item), 1266; rows 1256, 1260, 1267 for the rest of the carry. The published
works read by row 1218 (six authors' A and B; Zeng) were weighed in Section 1 and supply no input here.

Status: complete at 2026-11-20T13:11Z (date -u). Author only; checked by no one; no numeric run; no subagent.

RESULT: Row 1275 (Claude Opus 5.5 max, Mac mini worker 1, 12:37Z-13:11Z by date -u; author only, checked by no one; no numeric run, no subagent). The Jaffe-Witten mass gap of four-dimensional SU(2) Yang-Mills is NOT proved and nothing on the chain is disproved; the infrared seed at the base datum stays OPEN with no engine for the band (Section 1: every mechanism screened is on file). Worked item: (V9), the physical normalisation bound of the one-cutoff carry (row 1255; OPEN per checks 1263, 1266), read in Sussman and Alpoge's complete account at 31a47c543775 (with Claude and Codex as authors of its text; after Balaban). PROVED (elementary): Proposition N1, the zero-source comparison of `9.1:cor-sourced-integrals` fixes the ratio of the two runs' free constants to within 1 +- 2 eps* A B, so the account's "one free positive constant for each run and each centre" (III:18249) cannot be two independent constants inside 9.1; Lemma N3, 9.8's normalisation Z~(0) = 1/B is a downstream rescaling whose closeness follows from 9.1 with the factor 1 + AB (matching the account's own C_* = 2 C*_TC Q_w (1 + Q_w), III:18229). ARGUED from the printed proof (III:17422-17441, 17472-17480, 17556-17580, 17798-17799): Lemma N2, Theorem 9.1 compares the correlation theorem's own terms P_h[x^c] with no per-run factor, which 8.22 normalises by Balaban's constant E_m (II:140916-140924); Corollary N2', either that holds or the printed proof needs an unbounded load on log(S^B/S^A), so (V9) is no input beyond 9.1 itself. PROVED GIVEN N2's reading, Theorem 9.1 with its hypotheses (a)-(e), 8.22 and rows 1233/1255 (Lemmas 3.5-3.6, D0, D1, D2(b)): Proposition V9, the correlation theorem's own representatives are consistent on both tori, the edge bound holds with b_n = eps*_n (L^4 A_s B_s + A_b B_b), D = 0 and eta_9 <= eta_vac + eta_det, so Phi(d) <= Phi(d_0) + sum b_n + 2(eta_vac + eta_det); the carry must cite 9.1's corollary at zero source, never the 9.8 Definition (empty there, as check 1263 found). OPEN: the infrared seed (the crux); 9.1's hypothesis (e) `9.1:prop-blind-site-expansions` (outstanding in the account); (FC-T) of row 1267; (DET)'s inputs; the account's premises. Output library/gap-mini-solve-am-opus.md.
