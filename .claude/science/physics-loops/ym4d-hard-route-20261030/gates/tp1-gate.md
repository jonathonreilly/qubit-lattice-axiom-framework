First failing step: none.

# TP1 pass-3 referee report

Text: `library/tp1.md` (636 lines), the Codex distillation of `library/tp1-draft.md`.
Sources read in bounded ranges: SA = `scratchpad/sa/ym4.tex`, `ca_III.tex`, `ca_I.tex`, `YM3_I.tex`; `library/ag1-draft2.md` (§1, §8, §9), `ag1-draft.md` (Lemma 2.3), `ag1-tt-draft.md` (§3, §8), `pan-draft.md` (§0), `ref-73.md` (§2), `c4-order.md`, `in1-draft.md`, `t0-skeleton.md`, `GOAL.md` (NT1). Every statement was checked once, step by step.

## Findings

All findings can be repaired. None is fatal. None changes a constant, an exponent or a conclusion.

**1. Lines 122–128, used at 443–449 (Lemma 5.4, (5.10)). REG does not give the Gaussian energies the properties the proof uses.** REG gives source locality (independence of a source that misses \(X^+\)) and holomorphy on the discs (2.8) only for \(e_j\). For \(e_j^G\) it says only "on the same family, bounded by the same estimate". It also does not say on which \(z\)-domain the comparison in (2.9) holds. The proof of (5.10) needs three things:
- (a) the restriction of \(\sum_{j,X}\partial_{12}(e_j-e_j^G)\) to the domains that meet both supports. This needs \(\partial_{12}e^G_j(X;0)=0\) when \(X^+\) misses a support. Without it, the remaining domains contribute a number of terms that grows with the volume.
- (b) holomorphy of \(e_j^G\) on the bidisc of radii \(r_{\rm cx}x_j/(2t_i)\).
- (c) the first inequality of (2.9) on that bidisc, so that Cauchy's formula applies to the difference.

*Repair:* add to REG that \(e_j^G(X;\cdot)\) has the same holomorphy domain (2.8), is independent of a source whose support misses \(X^+\), and that the first inequality of (2.9) holds on (2.8). These are statements about a strengthened hypothesis (§9 item 6). With them, (5.9)–(5.10) hold as written.

**2. Line 48. The definition of \(\Lambda\) is ambiguous.** "Such a component" points back to "a live component of lineage age at least \(b\)", with \(b\) unspecified. The intended event is that some live component at level \(k_1\), of any lineage age, meets the neighbourhood. That is \(b=0\), and \(A\ge0\) is then the largest contacting age. Lemma 5.3 holds under this reading. *Repair:* write "a live component (of any lineage age)".

**3. Lines 148–154 and 187. The AG import: its ceiling, and the form in which it is cited.**
- (a) \(\gamma_{\rm AG}\) (line 187) is not defined in the text. By `ag1-tt-draft.md` L419, the updated Theorem AG holds only at levels with \(x_k\ge\max(X_F,X_{TT})\). So \(\gamma_{\rm AG}\) must enforce \(g^{-2}\ge\max(X_F,X_{TT})\). Then every \(j\le K\) qualifies, because \(x_j>g^{-2}\).
- (b) `ag1-draft2.md` (8.1) states the bound first with \(\varpi_k=\delta\mathsf nM\check R_k/512\). Its one-line proof then derives \(\varpi_k\ge c_0(\log x_k)^2\) from "\(\check R_k\ge(\log x_k)^r\)". That step does not follow from the running-minimum definition, because \(\min_{i\le k}x_i\le x_k\). TP1 does not rely on that step. Its own reduction (lines 154 and 419–420) uses \(\min_{i\le j}x_i\ge x_j-2c_2\ge x_j/2\) from (4.1), and it is correct. Line 153 should therefore say that (2.11) is obtained from the \(\check R\)-form of ag1-draft2 (8.1) by Lemma 4.1 (the step at line 420). It should not present the \((\log x)^2\) form as that draft's direct output.
- (c) The upstream draft should correct its own step in the same way.

**4. Line 154. The description of (P-an)(d) is out of date.** The text describes (P-an)(d) as "a zero-free tube for healed-region factors". That follows `ag1-tt-draft.md` §3.3. `pan-draft.md` §0 (pass 1, no gate) recasts (d): no factor is kept for a healed component, and (d) becomes a uniform Kotecký–Preiss statement (its Theorem D1). That draft proves (d) as an implication and names (L), the walk-interpolated presentation, as the first input on the path that no owner has stated. *Repair:* update the Outstanding note to cite `pan-draft.md` and its open input (L). The implication is unaffected, because AG is a hypothesis.

**5. Lines 165–166, used at 543–548. LIMIT should state what a "realization" includes.** For each component, Lemma 7.1 uses convergence of the centred first and second moments along that component's own realizing sequence of periodic Gibbs states. LIMIT states moment convergence only "along the specified volume-first limits". It states the component realization separately. Also, \(\langle\Omega,[O(f)]\rangle=\sigma(O(f))\) is written for the uncentred field, which has no continuum limit. *Repair:*
- State that a realization includes convergence of centred first and second moments on separated tuples.
- Write the OS vectors with centred fields \(O(f)-c_f\). Then \(v_f\) is unchanged and \(\|v_f\|^2=S_2^T[\sigma](f,\vartheta f)\) as imported.

**6. Lines 336 and 526 (cosmetic).**
- Line 336: "\(x_i\ge x/3\) throughout the run" holds only for \(i\le k_1\). That is the only range used.
- Line 526: the bound \(x\ge(c_*/2)\log(1/d)\) needs one more reduction of \(d_0(g)\), from the uniform limit in (4.2). Say so.

**7. Line 600 (cosmetic).** "SA 17325": the display for \(\Omega_t^c\) and \(Z^{[0]}\) is SA 17320–17322, and \(Z_t\) is defined at 17325. Cite 17320–17325.

## Steps checked with no defect

- **Constants.** \(C_G=\frac{N^2-1}2\cdot\frac6{\pi^4}\) (SA 26008 gives the same arithmetic). \(c_*=11N^2/(12\pi^2)\) agrees with SA 26083 in SA's convention \(\beta=g_0^{-2}\). \(v_4=\pi^2/2\). \(\mathrm{tr}\,\mathbb K^2=6\pi^{-4}|u|^{-8}\), because \(\Lambda^2(I-2\hat u\hat u^T)\) is orthogonal. \(\int\phi=2\pi^2/24=\pi^2/12\), and \(\operatorname{Lip}\phi\le8/(3\sqrt3)<4\).
- **F3 telescoping (Lemma 4.1).**
  - First passage keeps \(x_j>g^{-2}\) with no sign assumption.
  - (4.1) follows from \(|A^0_k-A^0_i-c_0(k-i)|\le2c_2\) and the per-step ceiling.
  - (4.2): minimality of \(s\) gives \(C_W(s)\le D<LC_W(s)\). With \(c_0s=c_*(\log(1/d)+\log D)\) this gives \(x/(c_*\log(1/d))\to1\), uniformly in \((K,\beta)\).
  - (4.5) by dyadic splitting.
  - (4.3) keeps both slope terms, matching SA 26084 (\(g^3\) and \(g^{\kappa_0-6}\)) and SA 22880.
  - The sign \(\zeta_k=-x_k'(0)\) is consistent with SA's running shift (SA 22863).
- **Lemma 4.2.** Cross-distances lie in \([d,10d]\). Tent sup, support and count bounds hold. (4.8) holds.
- **Lemma 5.1.** Exact covariance-plus-mean identity, and the pointed mixed derivative is zero.
- **Lemma 5.2.**
  - (5.3), with factor \(\tfrac14\cdot2=\tfrac12\) and \(C_{>\max(j,l)}\).
  - The separation \(3d/4\ge d/2\) after \(C_hM/D\le1/8\).
  - The early-slice tail \(D^4e^{-cD}\).
  - (5.4), including the terminal \(R_{k_1}\) with \(r/a_{k_1}\le11DL^{-n}\).
  - The profile recombination to \(\zeta f^0\).
  - The support-count bound (5.5).
  - The Riemann sum (5.6), with the conditions of (2.4) met because \(d<1/10\) and \(\ell\ge10\).
- **Lemma 5.3.**
  - The weighted contact bound.
  - The contact count is generous but harmless: SA 26166 says \(O(1)\) history cells touch the supports.
  - \(x/2\le x_{k_1}\le2x\).
  - \(\check R_{k_1}\le L(\log 2x)^r\).
- **Lemma 5.4.** The entropy sum (5.9), with \(d/a_j=DL^{k_0-j}\). Cauchy bidisc bounds. The \(\Lambda/\Lambda^c\) split. Item 1 above is the only gap.
- **Lemma 5.5.** \(L^2\) bounds, Cauchy–Schwarz, and the relative error. The relative error uses \(\zeta\ge2/3\) and \(\mathcal K\ge10^{-8}\theta^2t_ft_h\).
- **Transfer to all periodic states (Lemmas 6.1–6.2).**
  - The Schwarz bound \(|h-1|\le1/2\) on radii \(r_0/(4(Q_0+1)u_i)\), and the constant \(32\log2(Q_0+1)^2r_0^{-2}\). Both match SA ET5–ET7 (26778–26820).
  - The packing by lattice translates, \(v\in[40d,41d]\) for \(a\le d/40\).
  - The Lipschitz bound by exit and entrance points, and the sign average \(J\Delta(f,h)\).
  - The torus law passes to \(\nu_*\) through a closed interval that does not depend on the volume.
  - The relative transfer error \(C_\theta d^2[\log(1/d)]^2\).
  - The monotone envelope.
- **Lemma 7.1.**
  - TU10 constant \(\frac32\cdot\frac{16}9\).
  - \(\eta_g=a_g+(1+a_g)\varepsilon_g\).
  - Connected covariances are invariant under centring.
  - The closed bounds do not depend on the datum, because the continuum normalization replaces \(x\).
- **Non-triviality (Lemma 7.2).**
  - \((f,\vartheta f)\in\mathfrak T(d;\theta)\): gap \(d\), mass \(\pi^2d^4/12\), \(4/d\le1/(\theta d)\).
  - \(\|v_f\|^2>0\) from (3.3) and (4.6), for each realized component separately. No mixture argument is used, which is what NT1 of GOAL.md requires.
  - \((1+H)^{-1}\) is injective, maps into \(\operatorname{Dom}H\) and preserves \(\Omega^\perp\).
  - \(\ker H=\mathbb C\Omega\) then gives \(Hw\ne0\).
- **Quotations.** All SA, CA-III, CA-I and YM3-I readings in §8 were checked against the cited lines and are accurate. This covers the order (2.12) and the cycle cut (SA 19469–19485), D3, F1–F3 and TU10 (SA 4165–4415), \(a_p\approx\frac12a^4|F|^2\) (6852), the waiting rule (23265), the propagated \(\widehat Y^{\sim8}\) (17320), \(\check R\) by running minimum (17334), the formats of Propositions 4.3, 4.4 and 4.6, live bounds with \(L^{C\check R}\) and label age \(\le\) lineage age (26113–26118), the decomposition \(C^{\rm free}=C^{\rm bg}+C^{\rm fl}\) (26010–26016), GCB52 (28195–28226), the CA-III outstanding lists, Corollary IV-68-44 on the small torus with its volume-dependent tail, and Lemma IV-69-33 on dimension \(\ge2\). \(\kappa_0>8\) appears in IN1 (`in1-draft.md` L347) and at SA 20748. Lemma 8.1 agrees with AG1 Lemma 2.3 (`ag1-draft.md` L115, `ag1-draft2.md` L122).
- **Use of hypotheses.**
  - FLOW: Lemma 4.1.
  - FREE: Lemma 5.2.
  - PRES: Lemma 5.1, and the law in Lemma 5.3.
  - REG and G-ID: Lemma 5.4.
  - AMP: Lemmas 5.4–5.5.
  - AG: Lemma 5.3.
  - STATE: Lemmas 6.1–6.2.
  - LIMIT: Lemmas 7.1–7.2.
  - The order (2.12) is used only in fixing constants. The text correctly uses the early envelope \(\bar B\) in place of the returned \(B_\sharp\). `ag1-draft2.md` §9 has \(C_L\) depending on \(B_\sharp\).

## Note on the imports

F/gates contains no gate for `ag1-draft.md`, `ag1-draft2.md`, `ag1-tt-draft.md` or `pan-draft.md`. The AG hypothesis therefore rests on drafts that no referee has checked. This does not affect the conditional implication. It does affect what the implication delivers.

## Verdict

Yes. The implication holds as stated, conditional on its imports. The imports are FLOW, FREE, PRES, REG with G-ID, AMP, AG-k1*, STATE and LIMIT in the IN1 order. They give, for the torus and for every periodic Gibbs state:
- the uniform two-point law F2 (3.1);
- the running normalization F3 (3.2) by telescoping;
- TU10;
- the continuum law (3.3) for every limit and every realized component;
- \(H|_{\Omega^\perp}\ne0\) on each realized component.

The repairs needed are to the wording of hypotheses: REG must carry the locality, holomorphy and comparison domain of \(e^G\) (item 1), and LIMIT must state what a realization includes (item 5). The remaining items are wording and citation fixes.

Checked line by line by Claude (fresh session).
