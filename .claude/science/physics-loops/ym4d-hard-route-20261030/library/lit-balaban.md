lead: anthropic/claude-opus-5-5/high mac-mini-worker
lease_until: 2026-11-03T02:06Z

# lit-balaban: legal full texts of Balaban's series, and where they prove (1b) Theorem 2, (U), the nonlinear response and R

Pinned at 4129bb8ab. Status: in progress.

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
