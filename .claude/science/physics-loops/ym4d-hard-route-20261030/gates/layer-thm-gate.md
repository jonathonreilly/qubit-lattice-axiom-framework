lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-07T16:05Z

# Gate: line-by-line check of library/layer-thm.md and library/layer-r2.md

Queue row 418. Claude Opus 5.5, max effort, commit 9a6feac0c, Mac mini worker 2. One reading by one other model; not an audit.

**Verdicts.**

| Statement | Verdict | Section |
|---|---|---|
| layer-r2 sections 4-6: (S5) with a common analytic radius and (B4) are incompatible | ADVANCE | 1 |
| layer-r2 section 2: (G) from the operator bounds (3); (7a) | ADVANCE | 5 |
| layer-r2 section 3: tangent test (10)-(12) | ADVANCE | 1 |
| layer-thm Statement | REVISE: drop the Laplacian member on 𝕳; (b) becomes (N1) | 2 |
| Printed cutoff at U14 is impossible; repair (R5)-(R7) | ADVANCE, ADVANCE | 3 |
| U15 coverage | ADVANCE; needs only definitions, not (N1) | 4 |
| (G) as first unproved input | ADVANCE, refined: (G) follows from (3) | 5 |
| Three attacks on (B4) | correct as written; REVISE the framing, since (B4) is false under (G) | 6 |
| Clauses (a), (c), (e), (f), corollary, rider | ADVANCE | 7 |
| Clause (b) | REVISE | 2, 7 |
| Clause (d) | ADVANCE as implication; REVISE: cite K6 | 7 |
| Invocation table: U07, U16, U20 | REVISE (U07 proved here) | 8 |

No BLOCK.

Sources: the four pinned account files, fetched by URL from github.com/ethanwsussman/Yang--Mills-LLM-experiment at `31a47c543775` into a scratch folder; SHA-256 equal to the table in `library/layer-find.md`. I, II, III, SA as in those notes. Credit: Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text; Balaban for the chart and propagator constructions.

## 1. layer-r2.md, the (S5)-(B4) incompatibility (checked first)

**Verdict: ADVANCE.** The calculation of layer-r2 sections 4-6 is correct. I redid every step against the account's definitions. First failing step: none.

What I checked, in order:

- **Admission.** I 12935-13035: (S3) makes J a 𝔤^c-valued bond function with only `|J|_(-3) < a_γ`, and "no relation between J and U is required". So complex currents of the bidisc in 6.5 are admitted bases, with no derivative condition.
- **Definitions.** I 13719-13738 (Lemma `4.5:lem-free-current-operators`): `Θ'_J = k_JΛ + Λ^T j_J + Λ^T m_J Λ`, `G^J_π = Σ G_0(Θ'_J G_0)^n`, `H^J = G^J_π Q* q_J ℓ^{-1}`, `⟨A,Θ_J A⟩ = 2⟨H^J C^(2)(ℓA), J⟩`, `G̃^J = (I - G̃_0 Θ_J)^{-1} G̃_0`; `m_J(λ) = m_3 + D*_U m_4` with m_4 pointwise in `[λ,J]` (proof, I 13811-13823). So Θ_J depends on J only through the weight `w(J) = H^{J,T}J`, linearly, as r2 (31) uses. (J8) gives analyticity in (𝔞,J) on the whole class, so `Q_J(a)` is holomorphic on the bidisc at each mesh.
- **(15)-(16).** From `(Δ_a - Θ'_J)H^J = Q* q_J ℓ^{-1}` (J4) and `P_0 G_0 Q* = 0`, `P_0 H^J = H^J - H_0`: exact. The Neumann coefficients (16) follow because A_J is linear in J.
- **(13)-(14).** With d(t) = (-ta,0), (S5) gives `A'(t) = tT_J a + O(t²)` (V' has degree ≥ 2), and the inner map `X ↦ C(ℓA' - ℓH^J X)` (I 13996, Lemma `4.5:lem-nonlinear-correction` (a)) gives `X(t) = t² C_2(ℓT_J a, ℓT_J a) + O(t³)`, since DC(0) = 0. The Cauchy step on |t| = ε/2 gives (14). This needs holomorphy on a datum disc of mesh-free radius, which is exactly what (G) supplies.
- **Flat sector (20)-(22).** Qa = ⟨a⟩ on period-one fields; `B = P_0 G_0 = Δ^{-1}(I - Π_0)`, `ΔB = I - Π_0`, `Λ = Δ^{-1}D*`, `H_0 b = b`. These hold for any positive mass constant and any G' that inverts the site Laplacian on mean-zero fields; only `D*(constant) = 0`, `D_curl* D_curl + DD* = Δ` (flat) and `QH_0 = 1` are used.
- **(23)-(26).** The coarse-bond transport of e^{iηua} is the ordered product P_n(u) for every contour and for the composed k-step average (rows in other coordinates are identical), so x_0 = q_2(a). BCH: `[a(r),a(s)] = 2i A_*^{-2} sin(2π(s-r)/n) τ_3`; `Σ_{m=1}^{n-1}(n-m)z^m = nz/(1-z)`, Im = (n/2)cot(π/n). So c_n = -cot(π/n)/(2nA_*²) and |c_n| ≥ 1/(4πA_*²) for n ≥ 3. Correct.
- **(27)-(33).** I re-derived j_J from `⟨λ, j_J(A)⟩ = ⟨c^(1)(A,λ), J⟩` (I 13698-13708) and m_4 from the polarised c^(2). Every term of the full mixed coefficient (17): x_1 = x_2 = x_12 = 0 by (30)-(31); `A_2 H_0 x_0 = 0` (`[τ_3,τ_3] = 0`, `Λ(const) = 0`); `B A_1 H_0 x_0 = Dλ_1`; in `A_2 Dλ_1`, m_3 = 0 (`D_1 λ_1 = 0`), j_{J_2}(Dλ_1) = 0 (components 2 vs 1), k_{J_2}λ_1 has only component 1. So component 2 of `∂_s∂_t Q|_0` is exactly `D_2 Δ^{-1} D_1* m_4` with `m_4 = 2c_n d_1^{-4} f_n φ τ_1`. Signs and factors agree with (32)-(33).
- **(34)-(36).** D_1* and D_2 on the half-shifted sine modes, the eigenvalue `d_k² + d_r²`, `β_r ≥ 1/(4r)` for `2 ≤ r ≤ M-1`, `4k ≤ d_k ≤ 2πk`, and the dyadic-square count are all correct. The sine-sum bound `|S_M| ≤ 1+π` is correct (Abel summation). So the coefficient is at least `c_* q_n` with q_n → ∞ like log n.
- **(37)-(39).** Cauchy on |s| = |t| = r with r = γ_*/8 independent of n. The contradiction is valid.

**Mechanism, for the lead.** `Λ^T m_J Λ` contains `D Δ^{-1} D* m_4`, an order-zero operator applied to a product with the bounded current. Order-zero operators are not bounded on sup-norm data; the account says so itself: I 13599-13617 bounds `∇G_0∇*` only on Hölder data, and (J2) at I 13763-13764 says "The Laplacian member is not asserted for G^J_π". At an own-current pair `RD*H^J = 0` kills this term (layer-thm Attack 1), so the failure is specific to independent currents.

**What it establishes.** On any datum domain where the (S5) layers exist with a mesh-free radius and are holomorphic in the admitted independent current, (B4) has no mesh-free constant, and therefore (S9) fails: by (B3), (S9) implies (B4). Since layer-r2 section 2 derives (G) from the chart's own operator hypotheses (3), (B4) is false under the hypotheses the chain needs anyway. The stopping lemma R_Δ should not be attacked again on the independent-current domain.

**What it does not establish.** It does not refute (N1), the A' member or the four entries; it does not refute the block-only chart; it uses the field slot. I expect a block-only version with a coarse-scale varying block datum (then `C_2(ℓH_0 b, ℓH_0 b) ≠ 0` at J = 0 and the same `DΔ^{-1}D*m_4` term appears at second order in J), but I have not computed it; label: gap, not used below.

## 2. The Statement of layer-thm.md

**Verdict: REVISE.** It is precise and fixes no downstream target. But it asks for one member that no use I could find needs, and that member is the one section 1 refutes.

**Coverage.** At j = 0 and σ = 1, clauses (a), (c), (d), (f) are the account's chart theorem: K1 (I 14496-14560), K5 (`4.5:prf-chart-covariance`), K6 (`4.5:prf-diagonal-exactness`, I 15669-15701) and K10 (iii) (I 15333-15334). All are marked proved in the account, given cited Balaban inputs. The new content is the field slot j in (S5), the uniqueness domain and the rider. The field slot covers U01/U02 through the corollary's substitution of the field-datum lemma (I 72534), and only with the conversion layer-thm says each invocation must supply. Clause (e) has no located content (layer-find); the "proposed reading" adds nothing, which is honest.

**Smuggle check.**
- No downstream target fixed: passes. (S5)-(S6) are fixed by the chart equation I 14376-14420 and the switched form I 15311-15313.
- Not open-ended: passes. The norms, radii (S8) and uniqueness product are finite and specified.
- No structure its uses do not need: **fails**, at `‖δ𝕳‖^Δ_p` in (S9), and at the idle `|δX|_p`.

**Evidence for the failure.**
1. U16 itself says what it consumes. I 112603-112604: "These norms contain the four entries of 𝖭_y; the norm ‖X_1-X_2‖_p is idle." 𝖭_y (I 111405-111406) reads `N_y(δ𝕳)`, first order. The bound is then consumed as `𝖭_y(δ𝕳_p) ≤ η_p 𝖿 𝖴_L` (I 112646).
2. The other places that state `N^Δ_y(𝕳)` consume only its first-order or value part: I 117573-117577 (`N_y(χ_t𝕳) ≤ 2a N_y(𝕳)`), II 57663 (`ℓ|𝕳^w| ≤ N^Δ_y`), II 52440 (C^{1,β} sizes).
3. Every current formula reads Δ on A', not on 𝕳: the chart current I 14445-14448, (S10), and the partner lemma I 111397-111399.
4. The outline designs around the member. SA 10576: "When s≢1, bounds of first order on the operators do not yield a bound on Δ_U H independent of the level ... The reduced current takes its place ... only first-order norms occur."
5. Section 1: on a common analytic domain the member is false at s = 1 with independent currents.

**Repair (written out).** Replace (S9) by the four entries

  max{ ‖δA'‖^Δ_p, ‖δ𝕳‖_p, |P_1(σ)δA'|_{-3,p}, |m_H(σ)δX|_{-3,p} } ≤ B_𝕳 ‖δd‖_{dat,p},

which is exactly the admitted input (N1) (ca-f section 3; layer-thm (N1) transcribes it correctly). Drop `|δX|_p`, or keep it only as the fixed-kernel statement (B2). Replace "This is exactly the five-member reading in I 112588-112610" by "This is the four-entry content that I 112603-112604 says the five norms contain". Delete R_Δ (B4) from the Statement and from the stopping-lemma text. After the repair, clause (b) *is* CA-LAYER/(N1), owned by stage-claude; LAYER-THM has no separate obligation for (b).

## 3. U14: the printed cutoff and the repair (R5)-(R7)

**Impossibility (R4): ADVANCE.** I 111526-111527 asks for a C² ζ with ζ = 1 on [-1/3,1/3], ζ = 0 outside (-2/3,2/3), |ζ'|,|ζ''| ≤ 5. At 1/3, ζ = 1 and ζ' = 0, so ζ(2/3) ≥ 1 - 5·(1/3)²/2 = 13/18 > 0. No such ζ exists. (Any C² step of height 1 over length 1/3 with flat ends needs sup|ζ''| ≥ 36.)

**Repair (R5)-(R7): ADVANCE.** Rechecked: the trapezoid has integral 1/4 + 1/2 + 1/4; v_ε is supported in [1/200, 199/200]; the triangle kernel has integral 1, so supp v ⊂ [0,1]. v is C² because v'' is a finite sum of translates of the continuous k_ε. Sup bound 50/33, Lipschitz bound 45000/9801. Hence |ζ'| ≤ 3·50/33 = 50/11 < 5 and |ζ''| ≤ 9·45000/9801 < 42 (consistent with the lower bound 36). Mixed second partials are at most (50/11)² < 25. Then (R9): `5/(2L) + 42/(4L²) ≤ 2` for L ≥ 3, with equality at L = 3 for the rounded bounds and strict inequality for the exact ones. So `c_ζ = 2c_d` survives. The support of ζ is unchanged, so the vanishing argument of I 111630-111643 carries over.

**Coefficient count (R1)-(R3): ADVANCE.** I re-derived `[∇_α,χ] = f_α T_α`, `[∇*_μ,χ] = -g_μ T_μ^{-1}`, (R1), and both identities (R2). ∇* = (T^{-1} - I)/η is the bilinear transpose for complex links too, because the trace form is Ad-invariant. Totals per μ ≠ ν: derivatives (1+ϑ) + (1+3ϑ), values 1 + ϑ², all read on st(b). So `c_d = (2+4ϑ)(d-1)`, the printed constant. This supplies the step marked (∗) of `4.25:lem-cut-layer-partner`.

**Partner bounds (R11)-(R17): ADVANCE**, as an implication from (R13), which the note states as a premise. The note is right that the printed line I 111438 bounds `ℓ³|KδA'|` by `N_y(δ𝕳)`, which does not follow. The final bound by 𝖭_y holds through `N_y(δA') ≤ N^Δ_y(δA')`.

**Consequence.** U14 (`4.25:lem-cut-layer-partner`) now holds as an implication from the furnished triple, (R13), `N_y(χ𝕳) ≤ 1/40` and the collar geometry, with the cutoff replaced by (R5)-(R7). This is a correction of their text (the printed cutoff does not exist), with their constant unchanged.

## 4. U15 coverage

**Verdict: ADVANCE, and it needs less than claimed.** At I 112199-112213 the only layer-theorem content read is `N_y ≤ N^Δ_y` together with `𝕳 = A' - HX`. N^Δ_y contains the value and gradient entries by definition (I 94999: "ℓ|A'| ≤ N^Δ(A') by the definition of the norm"; I 95119-95120). The size bound comes from (e2), not from the layer theorem. So U15 is covered without (N1). layer-thm's "conditional on (N1)" is true but not needed.

## 5. (G) as the first unproved input

**Verdict: ADVANCE, refined by layer-r2 section 2.** In clause order, (a) is first and its uniform form needs (G). layer-r2 (3)-(9) proves (G) from the operator bounds (3). I checked the arithmetic:
- inner map: `2r + 8chr² ≤ 17r/8 < 3r < s_C`, value ≤ (9/2)cr² < 8cr², Lipschitz ≤ 3/64;
- room at N(A') ≤ 4r: argument ≤ 9r/2, value (81/8)cr² < 32cr², Lipschitz ≤ 9/128;
- forcing: N(Tj) ≤ (1+gθ)N(j), and (7) holds since a ≥ max{h_0, t, k};
- outer map: N(Ψ(z)) ≤ r/8 + (81/64)qr² ≤ 3r/16, and the Cauchy bound N(DF(A)u) ≤ 16qr²/(2r) ≤ 1/8.

(3) on the account's global class, at σ = 1 and switched σ, is the hypothesis set of `4.5:thm-chart-existence` and (K10). The account proves both (I 14518-14521: constants "uniform in k, in K, in the sequence of domains ... arbitrarily large X included") from two inputs it labels as unproved: q_0's walk expansion, "printed without proof" (I 15270-15273), and the analytic form of CMP98 Prop. 5, "stated ... without proof" (I 13982-13983). So the first unproved inputs under (G) are these two leaves, and (3) on the localised determining sets 𝔅^0, 𝔅^C, where no account statement was located (layer-find). The note's sentence "Calling (B4) the first unfinished step ... would be inaccurate" is correct.

## 6. The three failed attacks on (B4)

**Verdict: each attack is correct as written; the framing is REVISE.** Section 1 shows (B4) is false wherever (G) holds, so no fourth attack should be made. Replace "stopping lemma R_Δ, tested by three distinct attacks" (layer-thm lines 1338-1346 and the Result) by "R_Δ (B4) is false on any common analytic datum domain (layer-r2 section 6); after the repair of section 2 no use needs it".

- **Attack 1 (B5)-(B6).** I re-derived the curl identity `(D_1*D_1 + D_0D_0*)B = Δ_W B + K_W B` (the diagonal commutator vanishes; ∇* is the bilinear transpose), then `Δ_W = Δ_a + P_1 - Q*aQ - 𝒞_W - K_W` with `P_1 = D_0(I-R)D_0*` (I 13571-13572: P := I - R). With (J4) this gives (B6) exactly. The diagnosis (the term `Λ^T D_0* m_4(ΛH^J x)` needs regularity of J that K109 omits) is the term layer-r2 isolates. Correct.
- **Attack 2 (B7)-(B9).** The toy computation is exact: X = a² and `|Δv_n| = 4n` while `|v_n| = 1/n`, so `|ΔH_n(X(a)-X(0))| = 4na²`, while the four admitted entries hold with constant 2. It refutes an inference, not (B4), as the note says. (The toy H_n has `π_1 H_n = 0`, so it is not a lifting operator; the note does not claim it is.)
- **Attack 3 (B10).** The identity-theorem argument is right: `J - 𝒥(W)` vanishes on the own-current graph and not off it. SA 10462-10464 says the two systems "define separate functions" away from critical physical pairs.

## 7. Clause sections of layer-thm.md

| Clause or step | Verdict | Note |
|---|---|---|
| (a) finite-kernel contraction (A1), (A3)-(A4) | ADVANCE | Ball and Lipschitz arithmetic correct. |
| (A2) seven terms | ADVANCE | Matches I 14170-14181 term by term; each term has degree ≥ 2, so V'(0) = DV'(0) = 0. |
| (a) uniform | ADVANCE as implication | Uniform under (3) by layer-r2 section 2 (section 5 above). |
| (f) restriction, zero components | ADVANCE | Iterate-by-iterate induction is valid for component-preserving maps; basis is K10 (iii), I 15333-15334. Exempted families: substitution s = 1 keeps |s| ≤ e^{κ_1}. |
| (c) covariance, uniqueness domain, (C1) | ADVANCE | Transport identities hold for complex gauges because the bilinear trace form is Ad-invariant; (C1) is a correct sufficient margin. |
| (b) (B1)-(B2), HX corollary, (B3) | ADVANCE | Fixed-kernel statements; (B3) necessity and sufficiency both correct. |
| (b) uniform, (S9) | REVISE | See section 2: replace by the four entries = (N1). |
| (d) (D1)-(D4) | ADVANCE as implication; REVISE the citation | (D3) and the substitution giving (S4) are correct; (D4) is correct. (D2) is asserted ("a finite differentiation identity"), not derived. At j = 0, σ = 1 the whole clause is K6, `4.5:prf-diagonal-exactness` (I 15669-15701), proved in the account. Cite K6 per the port rule rather than re-deriving it. |
| (e) | ADVANCE | A specialisation with no content; correctly labelled. |
| Corollary, parameterised form (i) | ADVANCE | Substitution and Cauchy estimates on closed polydiscs inside the domain. |
| Rider (R1)-(R17) | ADVANCE | Section 3. The physical identity for (S10) is also correct. Off the diagonal, if m_H(1) is read as the chart's 𝒦_1 (I 14447), then (S10) at σ = 1, j = 0 is the account's chart current 𝔍(B) (I 14446) at every independent pair, since `Δ_a - Q*aQ - Δ' = Δ_W + K_W - P_1`. |

## 8. Corrections to the invocation table of layer-thm.md

1. **U07: "needs (B4)" is wrong; the bound holds by a direct proof.** U07 (I 94448-94540) bounds `sup_y N^Δ_y(T^L a)`, where T^L a is the derivative at datum zero. I prove it without (B4) or (N1).

   *Lemma U07'.* Let σ = 1, (W',J') ∈ 𝔎_109(𝔅^C; γ^♭), and assume on 𝔅^C the propagator bounds `N(H_0 a) ≤ B_0|a|`, `N^Δ_y(H_0 a) ≤ B_0^Δ|a|`, `N(G̃_0 f) ≤ B_0'|f|_(-3)`, `N^Δ_y(G̃_0 f) ≤ B_0'^Δ|f|_(-3)`, together with (J5) and `C_Θ γ^♭ B_0' ≤ 1/2`. Then `T^L a = T_J H_0 a` with `T_J = (I - G̃_0Θ_J)^{-1}`, and
   `sup_y N^Δ_y(T^L a) ≤ (B_0^Δ + 2C_Θ γ^♭ B_0'^Δ B_0)|a|_∞`.

   *Proof.* By (S5) at j = 0, `D_b z(0) = G̃^J Θ_J H_0`, since V' has degree ≥ 2. The inner solution has `|D^J(A')| ≤ 4C_2|A'|²` (I 13998), so `D_b X(0) = 0`. Hence `T^L a = D_b𝕳(0)a = (I + G̃^JΘ_J)H_0 a = T_J H_0 a`; this is (D4). Put u = T_J H_0 a. From `(I - G̃_0Θ_J)T_J = I` we get `u = H_0 a + G̃_0 Θ_J u`. Since `|Θ_J u|_(-3) ≤ C_Θ γ^♭ |u|_(-1) ≤ C_Θ γ^♭ N(u)`, we get `N(u) ≤ B_0|a| + N(u)/2`, so `N(u) ≤ 2B_0|a|`. Then `N^Δ_y(u) ≤ N^Δ_y(H_0 a) + N^Δ_y(G̃_0Θ_J u) ≤ B_0^Δ|a| + B_0'^Δ C_Θ γ^♭ · 2B_0|a|`. ∎

   The Laplacian member for G̃_0 follows from those for G_0 and H_0, because `G̃_0 = G_0 - H_0 ℓ Q G_0`; (J2) says the Laplacian member "is used for G_0 and H_0 only" (I 13763-13764). Label: implication from these propagator bounds on 𝔅^C. Those bounds are part of (3) on localised sets (section 5). The account's own route (I 94526-94540) passes through `N^Δ_y` of 𝕳 at finite t, which is the refuted member for the field slot; the direct route avoids it.
2. **U16:** after the repair, covered conditional on (N1). I 112603-112604 consumes the four entries only.
3. **U20:** reads only the constant B_𝕳 (I 125781-125785). After the repair this is the constant of (N1).
4. **U33:** stays not discharged, but the obstacle is the comparison across kernels and bases. That obstacle does not depend on (B4).

## 9. Defects, ranked by what each breaks

1. **(S9) asks for `‖δ𝕳‖^Δ_p`** (layer-thm lines 206-219). This breaks the Statement: by section 1 the member is false on any common analytic domain. Repair in section 2: use the four entries, which equal (N1).
2. **R_Δ (B4) is framed as an open stopping lemma** (layer-thm lines 577-598 and 1338-1346; layer-r2 Result keeps it as a target). This would send further lanes at a false statement. Repair: record it as refuted under (G), and not needed after defect 1.
3. **U07 marked "needs (B4)"** (layer-thm line 1278). This is wrong; Lemma U07' in section 8 proves the bound from the propagator bounds alone.
4. **Clause (d) asserts (D2) without deriving it.** It re-derives K6, which the account proves (I 15669-15701). Repair: cite K6 for j = 0, σ = 1.
5. **Their text, U14.** The cutoff of I 111526-111527 does not exist (R4). The repair (R5)-(R7) keeps `c_ζ = 2c_d`. The line I 111438 also bounds `ℓ³|KδA'|` by `N_y(δ𝕳)`; that step does not follow, but the conclusion holds through `N^Δ_y(δA')`. layer-thm cites the cutoff as I 111520-111525; the text is at I 111526-111527.
6. **Index, for the lead.** `library/sa-index/ca-full/index.tsv` reads `4.25:lem-cut-layer-partner` as PROVED, and `leaves.tsv` omits it. Its title says "the proof below is incomplete at the step marked (∗)" (I 111489-111490). With layer-thm (R1)-(R10), that step is now supplied as an implication.

**Pointers, not checked here.** (i) SA 10562-10576 builds the switched response with first-order norms only and replaces the current by a "reduced current" when s ≢ 1. The first entry of (N1), `N^Δ_y(δA')`, is a second-order norm read at all |σ| ≤ e^{κ_1}. Whether it holds at switched σ is a question for the CA-LAYER owner; compare the caution in `library/ca-f.md` on the field-datum norm. (ii) A block-only version of section 1 is expected but not computed (gap). It would show that the account's own `N^Δ_y(𝕳)` clauses (I 112595, I 94526-94531, I 131644, I 116658-116659, I 141784) fail at independent currents. Their consumers read only first-order parts, so the fix would be wording; that is low value as a contribution.

No numerical run was made; every check above is by hand. Memory was 55 percent free, but no job was needed.

## Result

**Moved.**
- R_Δ (B4) is killed: it is false wherever (G) holds (layer-r2 section 6, checked).
- With the repair of section 2, clause (b) of LAYER-THM becomes exactly CA-LAYER/(N1), so LAYER-THM has no separate (b) obligation.
- The step (∗) of `4.25:lem-cut-layer-partner`, an incomplete statement of the account, is supplied, with the printed cutoff replaced.
- (G) follows from (3) (layer-r2 section 2, checked).
- U15 is covered without (N1). U16 and U20 are covered conditional on (N1). U07's bound is proved here from propagator bounds.

**Still open.**
- (3) on the localised determining sets 𝔅^0 and 𝔅^C.
- The two printed-without-proof inputs under (3): the q_0 walk expansion (I 15270-15273) and the analytic CMP98 Prop. 5 (I 13982-13983). These are owned elsewhere.
- (N1) itself, owned by stage-claude.
- The conversion of each general-field invocation to the (S5) convention.
- Clause (e)'s content.
- U33's comparison across kernels and bases.

Checked line by line by Claude (Opus 5.5).
