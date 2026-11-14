lead: anthropic/claude-opus-5-5/high mac-mini-worker
lease_until: 2026-11-03T02:06Z

# lit-balaban: legal full texts of Balaban's series, and where they prove (1b) Theorem 2, (U), the nonlinear response and R

Pinned at 4129bb8ab. Status: finished 2026-11-02 (search record; no Balaban text reached).

Builds on `library/lit-large-field.md` (which could not reach any Balaban text:
bot check at Project Euclid, paywall at Springer) and `library/a3-response.md`
Section 8. The outline quoted is Sussman and Alpoge (with Claude and Codex as
authors of the text), `YM4_sketch_500.tex` at `31a47c543775`, read from a scratch
copy outside the repository. Everything here is a search record; nothing is
re-derived, and every Balaban statement below is `unchecked`.

## 0. What the next lane needs from Balaban (targets, from the outline)

- **(U) = outline Theorem 1** (l. 9660): for real eps_1-regular data V the
  regular critical configurations of C(B, V) form exactly one orbit, the
  background U_k(V), with |dU - 1| < C eps_1 eta^2 L(p)^-2. Its induction is
  closed (l. 9795, chain of (1b)) by "the global halving
  eps_0 -> max{C eps_1, eps_0/2}, following Proposition 8 [cited from
  Balaban; Package E] of CMP 102 (1985) 277-309". The outline's index
  (l. 32901-32904) separates "Balaban's Theorem 8, which he states without
  proof and which we must prove" from "Proposition 8 of CMP 102 (1985)
  277-309, which is cited".
- **(1b) Theorem 2 (local regularity)** (l. 9678): a critical regular U has
  eta^-2 L^2 |dU - 1|, L^3 |J(U)| <= C max_tau e^(-delta d_B(x,tau)) |dV(tau) - 1|,
  and (second half) any U regular on an enlarged cube has a local gauge
  e^(i eta A) with xi|A|, xi^2|nabla A|, ... <= C m eps. The outline (l. 9801)
  calls the second half "the counterpart for sequences" of **Proposition 6 of
  CMP 99 (1985) 75-102**, using its (1.135)-(1.136) and conditions (1.7)-(1.9).
- **Background propagators** (group (d) of (1c), l. 9797): Theorems 3.1 and
  3.3 of **CMP 99 (1985) 389-434**, p. 394 (auxiliary first member).
- **Linear minimiser decay**: CMP 95 (1984) 17-40, (1.103), Prop. 1.2, (1.110)
  (outline l. 26141); CMP 96 Lemma 2.1 (raw I l. 19391-19449).
- **R operation**: CMP 122 (1989) 175-202, (0.3)-(0.4) p. 176, pp. 177,
  181-183, Proposition 1 (minimiser in a box, outline Prop 2.4, l. 17656);
  CMP 122 (1989) 355-392, (1.73), (1.79), (1.102), pp. 384-387, Theorem 1;
  CMP 119 (1988) 243-285, Sect. 3, Theorem 1, Corollary 3, (3.40), (3.65),
  pp. 246, 278-279, 281 (outline l. 17290-17316, 17516, 17566, 22594, 22854).

## 1. Access, paper by paper (2026-11-02, from the Mac mini, curl and the web-fetch tool)

Method: DOIs from the outline's bibliography; OpenAlex (open API) for every
known location of each DOI; then one plain request per host. Stopped at every
bot check, as the rules say. No sign-in, no payment, no bypass.

Hosts:
- **Springer** (link.springer.com/content/pdf/...): "Client Challenge"
  JavaScript page. Stopped.
- **Project Euclid** (CMP 1965-1997 is free to read there; OpenAlex lists
  Euclid copies of CMP 89, 95, 96, 98, 99a, 99b, 102a, 102b, 119): Incapsula
  bot check to curl; empty page to the fetch tool. Stopped. Euclid IDs:
  euclid.cmp/1103922931 (89), 1103941451 (95), 1103941783 (96), 1103942283
  (98), 1103942611 (99a), 1103942769 (99b), 1104114382 (102a), 1104114383
  (102b), 1104162401 (119). 109 is at cmp/1104116842 (search result).
  OpenAlex lists no Euclid copy for 85, 86, 88, 109, 116, 122a, 122b.
- **Rutgers Esploro** (scholarship.libraries.rutgers.edu): has a record for
  every paper 85-122. The record of CMP 95 says "Open access", but its only
  file link is the Springer DOI (the record holds no PDF). So the Rutgers
  "open access" mark means the publisher copy, which is behind the challenge
  above. The records of the others carry no file either (as far as the
  JavaScript-free fetch shows).
- **Deep Blue, University of Michigan** (part of Springer's archive deposit
  there): **the only legal open repository copy found**, for CMP 102 (1985)
  255-275 (hdl 2027.42/46460) and **CMP 102 (1985) 277-309, the
  variational-problem paper that holds Proposition 8 (hdl 2027.42/46461,
  OpenAlex "green OA")**. Cloudflare "Just a moment" to curl, 403 to the fetch
  tool. Stopped.
- **CORE** (aggregator): lists both Deep Blue copies (download ids 3108475 for
  102a, 3108476 for 102b). core.ac.uk/download is behind Cloudflare; the
  public API's output download redirects to the Springer challenge. Stopped.
- **arXiv**: none of the series is there (1982-1989).

## 2. Readable secondary texts that follow CMP 102b (open, arXiv; read here)

Read from arXiv sources in a scratch directory outside the repository; nothing
committed.

- **A. Goswami, "The Variational Problem and Background Field in the
  Renormalization Group Method for Non-Linear Sigma Models", arXiv 2204.08252.**
  Follows Balaban CMP 102 (1985) 277-309 ("B_var") section by section for the
  O(N) sigma model in d = 2, and gives Balaban's equation and section numbers
  (unchecked against Balaban, since his text was not reachable):
  - the multiscale linear minimiser H, (1.103) of CMP 95 = (3.126) of CMP 99b,
    the form Delta (3.127), H_1 (3.129), decay bounds = (46), (103) of CMP 102b;
  - the "mapping transformation" (linearising the constraint around a
    reference U_0): CMP 99a (1.17), (1.29), (1.66), (1.80), Proposition 5,
    Lemma 1 (uniqueness of the gauge parameter lambda, u');
  - the linearising transformation of Q_k(A): **CMP 102b Sect. C**, the
    contraction condition below its (54), and (59)-(62);
  - the fixed point for the critical equation A_1 = -G J - G (dV/dA')(A_1 + H_1 B):
    **CMP 102b Sect. E** (Goswami's own Proposition 8 cites "See Sect. E in
    [B_var]"; whether Goswami's numbering matches Balaban's Proposition 8 is
    not known);
  - **the constant that keeps the induction closed: CMP 102b Sect. F, (162),
    (163)**: B_3 = O(1) B_0 sup sup sum_{y_2 in box'} e^(-kappa d(y_1,y_2)) (d+1),
    with the condition B_3 e^(-2 kappa M) <= 1/2. This is the mechanism the
    outline calls the "global halving eps_0 -> max{C eps_1, eps_0/2}" (outline
    l. 9795): the induction hands U_{k-1} to step k as a reference in
    U_k(B_3 eps_1) with B_3 independent of k, because the exponential decay
    beats the block size. My reading, not checked against Balaban.
  - critical point is a minimum: from (95)-(96) of Goswami, positivity of
    Delta_1; analyticity of the background: CMP 102b, (196)-(197).
  Limits: d = 2, sigma model, one reading per step, "See Sect. E" style
  citations rather than proofs for the fixed point and the halving.
- **W. Dybalski, A. Stottmeister, Y. Tanimoto, "The Balaban variational problem
  in the non-linear sigma model", arXiv 2403.09800.** One RG step only, O(4)
  sigma model, d = 2. Full proof by Banach contraction in L^infinity, with
  L^infinity bounds on G(Omega) and (Q G Q^*)^-1 from exponential decay. Says
  its solution is "quite different from Balaban's discussion ... in [CMP 102b]"
  and that "Balaban's papers on YM_4 are not easily accessible (cf. [MRS93,
  p. 326])". Useful inputs, both readable: Appendix (random walk) reproduces
  **Balaban-Jaffe, "Constructive gauge theory", NATO ASI B 141 (1986) 207-263,
  Section IV, Theorem 4.1**: a strictly positive operator on l^2(Z^d) whose
  kernel decays exponentially has an inverse whose kernel decays
  exponentially; and **Dybalski-Stottmeister-Tanimoto, "Lattice Green
  functions for pedestrians: exponential decay", Rev. Math. Phys. (2024)**.
  It also notes the YM_4 sup bound |A| <= c eps "follows quite easily using a
  gauge fixing condition which switches off the fields on many bonds in each
  box, cf. [CMP 99a, Lemma 1]".
- Both say the multiscale (k-step) problem is not done there: for k steps
  "the linearization of the constraint ... requires an additional application
  of the Banach contraction mapping theorem" and decay of "more complicated
  operators" (DST). So neither replaces CMP 102b for (U) uniform in depth.

## 3. Where Balaban states and proves what we need (through the Sussman-Alpoge raw accounts)

The raw Theorem 0 accounts of Sussman and Alpoge (with Claude and Codex as
authors of the text), `theorem_0_complete_account_raw_{I,II,III}.tex` at
`31a47c543775`, plainly had the papers: they quote Balaban "as printed" with
equation and page numbers (CMP 102b alone is cited about 700 times), and they
flag what Balaban prints **without proof**. That is the best map we can get
without the papers. Every item below is the raw account's reading, `unchecked`;
"raw I l. N" are lines of those files.

| Need | Balaban location (as the raw account reads it) | Proof in Balaban? ("not flagged" = the raw account does not mark it as printed without proof; nobody here has seen the proof) | Raw account |
|---|---|---|---|
| **(U)**, existence and uniqueness of the minimal orbit, uniform in depth | **CMP 102b, Theorem 1, (6)-(10), p. 279**: constants a_0, a_1, B_3 with B_3 a_1 <= a_0, "depending on d and L only". For V regular by (7) with eps_1 <= a_1, and B_3 eps_1 <= eps_0 <= a_0, the minimal gauge orbit exists, **is unique in the space (6) with parameter eps_0**, lies in U_k({Omega_j}, B_3 eps_1), and on the special cubes (side 2M'L^j eta, M' <= M(eps_1) = R_1 M_1 a_1/eps_1) has a gauge with \|A\| < B_3 M' eps_1 (L^j eta)^-1, \|nabla A\| < B_3 M' eps_1 (L^j eta)^-2 | not flagged; the raw account reads the proof in Sects. C, E, F, G (linearising map Sect. C, (40), (46)-(48), (54), (59)-(62), (71)-(80); fixed point Sect. E; induction constant Sect. F; second order and minimality Sect. G, (170)-(181)) | raw I l. 35144-35198; raw II l. 85845-85878; raw III l. 1065 |
| **The "halving"** that closes (U)'s induction (outline l. 9795: "Proposition 8 of CMP 102b") | **CMP 102b, Sect. F** ("the halving of [CMP102b, §F]"; cube side M'R_1M_1; Goswami: (162)-(163), B_3 e^(-2 kappa M) <= 1/2). Number "Proposition 8" not confirmed: the raw accounts cite Props 3, 5, 6, 9 of CMP 102b and never Prop 8 | not flagged; read as proved by the raw account and by Goswami | raw III l. 21280, 22162; Goswami Sect. 3.4 |
| **(1b) Theorem 2, first half** (curvature of a critical U bounded by an exponentially weighted profile of the data) | No such statement found. Closest: Theorem 1 (9)-(10) (uniform on cubes, not a profile); the Sect. F halving "applied locally on both kinds of two-level cube" (raw III l. 22162, an SA extension); and the data response (190) below | the profile form: **not in Balaban as far as the raw account shows** | raw III l. 22150-22170 |
| **(1b) Theorem 2, second half** (local gauge e^(i eta A) with bounds on a regular cube) | **CMP 99a (75-102), Proposition 6, (1.135)-(1.136)**, conditions (1.7)-(1.9); gauge uniqueness Prop. 5, Lemma 1, Theorem 2 with (1.39) | not flagged; but the Hölder variant after (1.147) is "stated without proof" | outline l. 9801; raw I l. 35201-; raw III l. 35320-35330 |
| **Nonlinear background response** (A3 curved part; analytic dependence of the minimiser on the data, decay of the derivative) | **CMP 102b, Proposition 9, (189)-(190), pp. 308-309**: U_k(V'V_0) U_k(V_0)^-1 in Landau gauge = exp(i eta H(B)), H analytic in B, with \|dH_mu(B,x)/dB_nu(y')\| <= O(1) (L^n eta)^-1 (L^{n'} eta)^-d e^(-delta_0 d(y,y')/8), and the gradient with (L^n eta)^-2; (189): second-variation bound O(1) eps_3 (L^j eta)^-3 e^(-delta_0 d/4) | **(189)-(190) printed without proof: Balaban writes "We do not perform these calculations here"**. Prop. 9 itself (analyticity) is not flagged | raw III l. 35577-35625, 75781; raw II l. 85845-85878 |
| Background propagators | CMP 99b (389-434), Theorems 3.1, 3.3, 3.4, 3.12, 3.13, (3.35) (printed without proof), (3.37)-(3.38), (3.41)-(3.45), (3.126)-(3.133), (3.187), p. 394, p. 396; "constants ... do not depend on the sequence {Omega_j}" | not flagged except (3.35) and the excluded cases ("It does not hold for G, G_1") | outline l. 9797; raw I l. 5690-5720; raw III l. 1055-1067 |
| Flat multiscale propagators (A3 flat part) | CMP 95, (1.103), Prop. 1.2, (1.110); CMP 96, Lemma 2.1, (2.59)-(2.61) | not flagged | outline l. 26141; raw III l. 75760- |
| Averages | CMP 98, Props 1, 2, 4, 5 | not flagged | raw III l. 75760- |
| **R operation** | CMP 122a: (0.3)-(0.4) p. 176, p. 177, pp. 181-183, Proposition 1 (minimiser in a box), (1.68)-(1.69), (1.90)-(1.100); CMP 122b: (1.33), (1.61)-(1.63), (1.68)-(1.73), (1.79), (1.89)-(1.100), (1.102), pp. 378, 384-387, 390, **Theorem 1** (UV stability, under the hypothesis g_0..g_K in (0, gamma]; Balaban says CMP 109 Theorem 2 would remove it and that its proof "has not been published", pp. 355-356); CMP 119, Sect. 3, Theorem 1, Corollary 3, (2.18), (2.50), (3.40), (3.65), pp. 246, 256, 276, 278-281 | **printed without proof: 122a pp. 178-179 (admissibility of the prepared large-field data), 122a (1.70) p. 192, 122b p. 375 (old terms beside a new region), 119 p. 276 (transfer of CMP 109 Sect. 3, Lemmas 5, 6 to the cover), 109 Theorem 2 and (0.31)**; the join sentence of 122b p. 387 (outline l. 17316) | raw I l. 4209-4240; raw III l. 75760-75815, 111296-111315, 53320-53330; outline l. 17288-17316, 17566, 17656, 17728, 22854-22917 |

## 4. What this changes for the next lanes

1. **(U), row 79 (`a1-orbit`).** The published statement is CMP 102b
   Theorem 1 (p. 279): existence and uniqueness of the minimal orbit in the
   space (6) at any eps_0 in [B_3 eps_1, a_0], constants depending on d and L
   only, so uniform in the number of scales; proof in Sects. C, E, F, G, with
   the Sect. F "halving" closing the induction. This is the proof to port for
   the outline's Theorem 1, not a new one. Before porting, check three
   differences, each of which could make the citation fail: (a) Balaban's
   average against the outline's M (the outline, l. 7063, says Balaban states
   his results hold "for every mean of this kind"; unchecked); (b) his
   generalized axial gauge (Sect. F; CMP 109 (3.26), p. 275) against the comb
   gauge and contour means; (c) his uniqueness class (6) at radius eps_0 <= a_0
   against the outline's "regular at a fixed small radius". **For the kill
   attempt of row 79** (two regular orbits, or constants growing with depth):
   inside Balaban's class (6), with his average, Theorem 1 already excludes
   both, if it holds. A counterexample has to live where (a)-(c) differ.
2. **Nonlinear A3, row 77, and stop (L) of `sa-2.8.md`.** The published
   nonlinear response, CMP 102b (190) (with (189)), is **printed without
   proof** ("We do not perform these calculations here", raw III l. 35622).
   So there is no Balaban proof to port for the curved nonlinear part, and
   `a3-response.md`'s route (Theorem CL plus (U) plus the chart bounds) is the
   one to finish. Its target form, to match what CMP 119 and the outline read:
   \|dH_mu(B,x)/dB_nu(y')\| <= C (L^n eta)^-1 (L^{n'} eta)^-d e^(-delta_0 d(y,y')/8)
   and the gradient with (L^n eta)^-2, in Landau gauge, analytic in B on a
   complex neighbourhood (Prop. 9). This agrees with the finding of
   `a3-response.md` Section 0 that Dimock 3.7 quotes Balaban at the same three
   places.
3. **(1b) Theorem 2.** The second half is CMP 99a Proposition 6 (port it).
   The first half, the exponentially weighted profile, has no Balaban
   statement in the raw account's reading; the outline proves it by a slowly
   varying maximum principle (l. 9867). It stays ours to prove.
4. **R operation (our rarity route and `route-compare`).** "Cite Balaban" does
   not close it: by the raw account, 122a pp. 178-179 and (1.70), 122b p. 375,
   119 p. 276 and 109 Theorem 2 are printed without proof, 122b Theorem 1
   assumes all g_j in (0, gamma], and the join step rests on the sentence of
   122b p. 387. `route-compare` should count each as an open step on the
   outline's side.

## 5. Not reached, and how one could reach them legally

Not read here: every Balaban paper (CMP 85, 86, 88, 89, 95, 96, 98, 99a, 99b,
102a, 102b, 109, 116, 119, 122a, 122b, and the N-vector series 167, 182, 196,
198), Balaban-Jaffe NATO ASI B 141 (1986), Balaban-Imbrie-Jaffe CMP 97 (1985).
Each stopped at a bot check (Springer, Project Euclid, Deep Blue, CORE,
scholar.archive.org) or had no open copy (Rutgers records carry only the DOI).
The Wayback Machine holds no PDF capture of the Deep Blue files (only
redirects and one 1.3 kB HTML page), and was then offline.

**The one legal open copy that exists:** CMP 102b (and 102a) at Deep Blue,
https://hdl.handle.net/2027.42/46461 (102b) and 2027.42/46460 (102a),
green open access per OpenAlex. A person with a browser can read it
legally; a machine session cannot pass the Cloudflare check, and must not try.
Project Euclid's CMP pages (IDs in Section 1) may also be free to read in a
browser; that is unconfirmed. For the lead: one browser read of CMP 102b
Theorem 1, Sects. E-F, Prop. 8-9 and p. 308 would confirm or correct rows 1-5
of the table in Section 3.

Checks of this record: none against Balaban. The raw-account readings were
cross-checked only against each other and against Goswami's independent
equation numbers ((46), (54), (59)-(62), (103), Sects. C, E, F, (162)-(163),
(196)-(197) of CMP 102b), which agree where both cite. No numerics (none
needed). Scratch files are in /tmp/lit-balaban-dl.6NQg and
/tmp/lit-balaban-arxiv.Bgza, outside the repository; nothing committed.

Credit: Balaban for every statement located here; Sussman and Alpoge, with
Claude and Codex as authors of their text, for the raw-account readings and
page citations of Section 3; A. Goswami and W. Dybalski, A. Stottmeister,
Y. Tanimoto for Section 2.

- **2026-11-08, availability.** CMP 122 (1989) 175-202 (122a) and 355-392 (122b) are now on disk, downloaded by the owner from Project Euclid (cmp/1104178393 and cmp/1104178467): Mini ~/ym4d-papers/cmp122a.txt, cmp122b.txt with the PDFs; laptop ~/ym4d-lead/papers/. Text layers extracted with PDFKit; check formulas against the PDFs. Never commit the PDFs or text.
