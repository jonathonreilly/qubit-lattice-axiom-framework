lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-06T11:42Z

First failing step: none.

# Gate: `library/b102.md`, first half (H1–H14, through Lemma O), row 354 `b102-gate-a`

Provenance: Claude Opus 5.5 (claude-opus-5-5), max effort, Mac mini worker, fresh session, statement pinned at commit 799a4acd0 on `claude/ym4d-hard-route`. Text by Codex (rounds 1–2). One line-by-line reading by the other model. It is not an audit and grants no status. I did not write the text.

Scope read: `library/b102.md` lines 1–1990 (§§1–7 and both preserved round results), with every proof step of H1–H14 and of Lemma O redone by hand. Imports were checked only for being used as stated: FP1 Lemma 8 (`fp1.md` 254–314, frozen), `flat-port.md` §§4, 5 ((5.1), (5.2), (5.6)) and 8 ((8.1)–(8.5)) (gate: first failing step none), P82 Lemmas 5 and 8 (`p82.md` 376–421, 542–600, frozen), `a1-balaban.md` §3.8 (568–724, gate: ADVANCE conditional on F0, which flat-port supplies) and §7.6 ((7.10)–(7.16)). Balaban's text was read on the printed pages, rendered locally from `~/ym4d-papers` (nothing copied into the repository): CMP 99b pp. 392–399, 408–409; CMP 96 pp. 224, 231–232; CMP 98 pp. 22–23, 28, 31, 36 ((42), (61)–(63), (89)–(92), (121)–(126)); CMP 102 pp. 284, 290, 297–298, 308 ((36)–(42), (77)–(84), (125)–(137), (185)–(190)). Credit: T. Balaban for every operator, average and estimate checked here; Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, for the account arguments that H1–H8 port.

Not checked here, by assignment: the §1 target statement (T1)–(T7), H15–H25 and the Result (row 355, `b102-gate-b`). The SA and CA line ranges cited as sources were not fetched. Every argument ported from them is written out in full in b102 and was checked on its own, so those citations are credit, not premises.

## Verdicts

| Statement | Verdict | Note |
|---|---|---|
| H1 constrained inverse, minimum, (H1.3) | ADVANCE | Redone: C > 0, QH = I, P² = P, 𝒢 = PG = GP*, K𝒢 = P*, Q𝒢 = 0; both directions of the stationarity equivalence. The remark QH = ℓ⁻¹ matches CMP 102 (129). |
| H2 analytic flattening | ADVANCE | Self-map 4C₂r² ≤ r/B₀; Cauchy bound 9C₂r on radius 3r < c₄; contraction 1/2; (H2.4) by shrinking s; range r/4 and (H2.5). The sign A = A′ − HD matches CMP 102 (80). |
| H3 weighted transfer, Neumann, (H3.4) | ADVANCE | Weight ratio e^{κd} (triangle inequality), scale ratio L^A e^{δd/4}, sum S; both derivative identities re-derived. |
| H4 fixed point | ADVANCE | Image B₀\|J\| + 4B₀C₄r² < r; Cauchy on \|t\| = 2r/N(v) gives 8C₄r; Lipschitz 1/4; (H4.3); Taylor minimum λ‖a‖²/4. |
| H5 halving iteration | ADVANCE | Wording note W1 below. |
| H6 local action bounds, (H6.4)–(H6.9) | ADVANCE (conditional on (H6.7), as stated) | Cubic coefficient (H6.1) re-derived from the BCH and trace terms; it is the leading term of printed CMP 102 (39). The word bound, Cauchy steps and (H6.2) hold. (H6.4) is printed (80) with K = Δ_π. All five terms of (H6.5) and all eight of (H6.6) re-derived, and each of the eight bounds checks. (H6.9) is printed (189) at rate δ₀/4. |
| H7 data response | ADVANCE (conditional, as stated) | (H7.2) equals printed (188) after adding H₀v; Θ = Δ⁽²⁾. Rate δ₀/8 as in (190). |
| H8 Gram bound, Schur inverse | ADVANCE | Both Gram inequalities; Schur sum tM; entry bound (2/m)e^{−td}. |
| §4 Attacks 1–3 | CORRECT-NO-ADVANCE | Attack 1's flat field (da = 0, RD*a = 0, D*a = f) and Attack 2's seam field (every plaquette is 1, holonomy h) are right; neither is used later. |
| Lemma O statement | — | K_U is printed CMP 99b (3.26) at a = 1, with the compression Ω₀Δ_aΩ₀ of (3.27). (O2) is the first two members of (3.42) for G(U), which Theorem 3.3 asserts (p. 399). Theorems 3.1/3.3 assume only (3.35); O also assumes (3.36), which only weakens O. |
| H9 normalization, rows, local flat input | ADVANCE | (H9.1) is printed (3.16) at d = 4, a = 1 in the physical row pairing. (H9.2): CMP 98 (89) has endpoint factors that cancel the contour terms at the identity, and (125) is the straight main term, so Q_j(1) is the n⁻⁵ block-and-path mean. The bond convention "sets formed before differences" is printed CMP 96 p. 224, (2.3). Telescoping gives Q⁰D ker Q′⁰ = 0. (H9.3) is FP1 Lemma 8 (14) with a_c = 1, including arbitrary marked shape and h = 1. (H9.5) is immediate. |
| H10 comb rows | ADVANCE | CMP 98 (42) has the same form as the outline's mean: straight centre path times the averaged loop logarithms. So (H10.3)'s first line holds with v_r and no gradient term. The second line: pure gauge gives coarse plaquette I, the linear part has ℓ¹ weight L², and the remainder is C_L(u+v)v. The bootstrap closes (Σ t_r < 1/(L−1)). (H10.5) follows by submultiplicativity and telescoping, (H10.7) by Schur. The port matches a1-balaban (7.10)–(7.16). |
| H11 scalar elimination, massive local system | ADVANCE | Q′Q′* = I in the top pairing; P is the orthogonal projection onto ran(SQ′*), so R = proj onto D*D ker Q′ for any positive scalar mass (this is printed (3.25)). (H11.5) and (H11.6) were re-derived by elimination. (H11.4) is flat-port (8.1) with Q*aQ = B*B at a = 1. |
| H12 assembly, Wilson Hessian | ADVANCE | (H12.1): forward and backward shifts give drift O(α/s) and value O(α/s²). (H12.2) holds through the quadratic forms. (H12.3): the second variation in the chart e^{iηa}U is 𝔡*𝔡 plus at most 16 insertion terms, each carrying P_p − I, so the error is εs⁻², consistent with printed (3.10). (H12.4) re-derived. (H12.5) by bounded overlap and dual-norm localisation. The Schur complement gives ≥ c_L J_E, so 𝓛_U ≥ (c_L/2)J_E. |
| H13 decay and (O2) | ADVANCE | The distance is printed CMP 96 (2.46): weighted length per layer, with the triangle inequality and the collar cost of (2.48). Each factor of (H12.6) propagates at most C_L M_P, which gives (H13.1). (H13.2) by Cauchy–Schwarz. (H13.4) is exactly P82 Lemma 5 (value, gradient, E term, r ≥ 16η, small gauge on the doubled cube). Its hypotheses hold with r = c_L s_y and a = C_Lα. The E terms are range-two and zero-order with coefficient Cαs⁻²; I re-derived 𝔡a − d_U a = η⁻¹(I − Ad P_p)(Ad U_ν a_μ(x+ν) + a_ν(x)). (H13.3), (H13.6), (H13.7) and (H13.8) all hold, with δ = δ_w/2. |
| H14 admission | ADVANCE | (3.35) gives s\|A\|, s²\|∇A\| < c𝔐α₀ on cubes of the class. Printed p. 409 takes c = 12 and p. 408 takes 𝔐 = KR₀M₀. Read boxes fit, including cubes of index j−1 at an adjacent layer. The second half is P82 Lemma 8 without I6. a1-balaban §3.8 at reference I reads only flat inverses (its gate says so), and (3.36) is not used. |

## Findings (none breaks a statement)

**S1 (scope, for `b102-gate-b`).** Lemma O is the first-order part of CMP 99b Theorem 3.3. Printed CMP 102 (128) reads Theorem 3.3 "and especially the bounds (3.42) for the second order operator". (130)–(137) also read (3.49), (3.69), (3.126), (3.133) and (3.137). Round 3's H17 (b102 2375–2381) derives the component-Laplacian member from (H13.5) in the way I would: every term is at most Cℓ_y⁻³Z_y. Gate-b should confirm that H15–H25 read no further member of Theorems 3.1–3.3 (G∇*_U, the Hölder bounds (3.43)–(3.45)) beyond what H15–H17 prove. Nothing in H1–H14 claims more than (O1)–(O2).

**W1 (wording, line 611).** H5's conclusion omits the premise U ∈ 𝔘_k(t₀); the proof uses it. Repair: add "and U ∈ 𝔘_k(t₀)".

The row-337 questions are answered on the way. P82 Theorem P is not used as a black box; b102 §7 says so, and that is correct. Only P82 Lemma 5 is cited directly, as stated, and the proof architecture of its Lemma 4 is re-run for the four-variable system. Lemma O is exactly the operator CMP 102 (128) inverts, at the strength of the first two members of (3.42).

## Verdict

H1–H14 hold as written. H6 and H7 are implications from their stated operator premises ((H6.7) and the H7 operator bounds). These premises are still open in this half.

Lemma O, positivity of K_U and (O2), is proved as an implication from FP1 Lemma 8; flat-port §§4, 5 and 8; P82 Lemma 5 with its imports I3 and I8; and a1-balaban §3.8 conditional on F0, which flat-port supplies. All of these are frozen or gated with first failing step none. The constants are uniform in depth, mesh, volume and admissible nest, chosen in the order of §7, with the background ceiling last.

No fabricated step was found. Every cited library location and printed equation listed above says what b102 says it says.

Checked line by line by Claude (Mini worker).
