lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-03T23:15Z

# Gate: `library/pw-bridge.md` and `library/nl-r9.md` (row 138)

Provenance: Claude Opus 5.5 (claude-opus-5-5), max effort, Mac mini worker, on branch `claude/ym4d-hard-route` at commit f45c5f2ac. Both files were written by Codex. This is one cross-provider read by hand, not an audit, and it grants no status.

Status: finished. Verdicts are in Section F.

Sources read:
- In full: `library/pw-bridge.md` and `library/nl-r9.md`.
- For their inputs:
  - `library/dec-field.md` Sections 1-2, 4 (the Y_w norm) and 5;
  - `library/h-walk.md` Sections 3-7;
  - `gates/h-walk-gate.md` Sections 5-7;
  - `library/a2-curved.md` Section 8;
  - `library/a3-clauses.md` Section 3 Step 5 and Section 4 (B1);
  - `library/o1-decoupled.md` Definition D, (P), Lemma P and Theorems A-B;
  - `library/wf-room-2.md` Section 6.1.
- The Sussman-Alpoge outline (Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text), `YM4_sketch_500.tex` at commit 31a47c543775. It was fetched by URL into a scratch folder of this session and read at SA 5755-5800, 10125-10210, 10356-10420 and 10528-10580.
- Balaban's OCR texts in `~/ym4d-papers/`: CMP 102 pp. 289-291 ((74)-(89)) and CMP 99 (389-434) pp. 421-423. They were read, not copied.

T. Balaban is credited, as in both notes, for the background-propagator and local-inverse architecture and for the reduced nonlinear expression.

## A. pw-bridge Sections 3-4: the reduced equations and the lattice estimates

**(3.2)-(3.3): ADVANCE.** I redid the substitution in the eight rows of `h-walk.md` Section 4 (A-row q_AA A + q_Aλ λ - D h' + Q^T ν = f; Y-row h' + A_s λ' = g_h, q_λA A + q_λλ λ + A_s h' - Q'^T μ' = g_λ, -Q'λ' = g_μ; Z-row h + A_s λ - D^T A = g'_h, A_s h - Q'^T μ = g'_λ, -Q'λ = g'_μ; QA = f_ν). With the half-split blocks (3.1), the g'_h row gives ½DA_sλ = ½Dg'_h + ½DD^T A - ½Dh, and -Dh' = -Dp + ½DD^T A. This yields line 1 of (3.3) exactly, with f_∘ = f - ½Dg'_h. The other seven lines are immediate. The one-halves in (3.1) are right: the cross term <D^T A, A_s λ> of q is split symmetrically between the two blocks.

**(3.4)-(3.5): ADVANCE.** From SA's explicit current continuation (eq. ym4:explicit-current-continuation, SA 10171-10183) and h-walk's c_J(A, λ) = <i[λ,A] - i[A,λ^+] - i[λ,Dλ], J>_f:
- the λ-variation of the two A-brackets and of the Dλ-slot of the third bracket gives pointwise endpoint products J·A and J·Dλ (into F_λ);
- the variation in the Dλ' slot is D^T applied to a bracket of J and λ (into Z_λ, with the transpose kept outside);
- the A-variation gives endpoint products J·λ (into F_A).

The E-form contributes -E(A - Dλ) to the A-row and D^T E(A - Dλ) to the λ-row. Only |J| and transports enter, and no difference of J is taken. The absolute row sum of E is right. a2-curved (8.3) gives a leg sum of C_L ξ(η/ξ)^4 per row. Multiplying by ξ_c^4|j_c| ≤ γ_j ξ_c and dividing by η^4 for the kernel in the fine measure gives C_L γ_j ξ_c^{-2}. Boundedly many adjacent-level rows meet a bond (a2-curved, the paragraph after (8.10)). The Hölder/Schur step after (3.5) then gives ||Eu||_q ≤ C||u||_q for every q.

**Lemma CZ (4.1)-(4.3): ADVANCE.** Checked:
- the multiplier bound |(e^{it_i}-1)(e^{-it_j}-1)| ≤ Λ(t), so ||T||_{2→2} ≤ 1;
- the kernel bound (4.2) by the split at |t| = 1/R and k+3 integrations by parts, ∫_{1/R} r^{-5} r^3 dr ≤ CR, giving R^{-k-2};
- the rescaling G_η(x) = η^{-2}G_1(x/η), giving (|x|+η)^{-2-k};
- (4.3) by telescoping a path;
- the dyadic Calderón-Zygmund decomposition on ηZ^4: parent average ≤ t, so child average ≤ 16t; a one-site atom has zero bad part; the shell sum is C2^{-n}||b_Q||_1;
- Marcinkiewicz by hand: the two integrals give |v|^q/(q-1) and |v|^q/(2-q);
- duality above 2.

No constant depends on η. This is a correct, self-contained discrete CZ theorem.

**(4.4): ADVANCE** for the flat componentwise Laplacian. The truncated kernels of orders 2 and 3 are locally integrable, the second differences are (4.1), and the harmonic remainder is bounded by iterated Caccioppoli, the one-dimensional telescoping bound in each of the four coordinates and Cauchy-Schwarz (r^{|α|-4}·r^2·r^{-|α|} = r^{-2}). The bounded-r/η case is direct.

**(4.5): ADVANCE.** The exponents are right: a = 6/5, 24/19, 8/7 all lie below 4/3 and satisfy 1 + 1/q = 1/p + 1/a for (2,3), (3,8), (8,∞). |DG_η| ≤ C(|x|+η)^{-3} is uniformly in L^a on a fixed ball, including the innermost shell. The three-factor Hölder proof of Young's inequality is correct. W^{1,2} → L^3 and W^{1,3} → L^8 are strictly subcritical in d = 4 (critical exponents 4 and 12), and W^{1,8} → L^∞ is Morrey.

## B. pw-bridge Section 5: the source norm, Lemma R and Lemma C

**(5.1)-(5.4): ADVANCE.** The scalings (5.3)-(5.4) follow from (3.3) with [A] = m^{-1}, [λ] = 1, [h] = [p] = m^{-2}, [μ] = m^{-4}, [ν] = m^{-3}, a = a_0 ξ^{-2} on rows (SA 10187), and the transposes Q'^T, Q^T being order one in the physical pairings. ||F||_* ≤ C_L||F||_S holds: the represented divergence parts pair as <g'_h, D^T A>/2 and <z_λ, Dλ>, and both are controlled by the E- and graph-norm parts of 𝒳.

**Lemma R (5.5): ADVANCE, given its named inputs.** I redid the four bootstrap steps. Each uses only quantities controlled at the previous step:
1. λ, λ' ∈ W^{2,2} from the graph norm.
2. h, p ∈ W^{1,2} from the divergence form of the drift, which needs |∇B| bounded. Then h, A ∈ W^{2,2} from the nondivergence form.
3. Every field and controlled first difference lies in L^3. Then p ∈ W^{1,3}, and A, h, λ, λ' ∈ W^{2,3}.
4. Every first difference lies in L^8. Then p ∈ W^{1,8}, and A, h, λ, λ' ∈ W^{2,8}.

Two premises of (5.6) were checked against the outline:
- The bound |∇B| ≤ C needs bounded first differences of the potential, including the complex part. SA 10133 supplies both: a real gauge with ξ|A|, ξ²|∇A| ≤ α_0 on cubes of side O(M_1ξ_j), and ξ|A'|, ξ²|∇_U A'| < α_1. The class bounds the current J only in size, and Lemma R never differentiates a J-coefficient.
- At bare outputs (layer L_0, scale η, which contains every point near ∂Ω_0), m/η = 1 and point evaluation in 𝒳 suffices. The fine operators have the same lattice principal parts across seams, and only the bounded averaging terms change. So the interior estimate (4.4) applies on every nonbare pillar neighbourhood.

The input "Δ^W + DD^T = componentwise covariant Laplacian + bounded zeroth order" is the named [Coefficients] input (a3-clauses Step 5, (B1)). It is not re-proved here, and Lemma R reads it only in local units.

**Lemma C (5.7)-(5.11): ADVANCE.** I recomputed every entry of [𝕂,χ]Ψ.
- (5.9) is exact. The term ½DA_s's commutator splits as ½[D,χ]A_sλ + ½D[A_s,χ]λ, and the second part cancels against -½Dg'_h with g'_h = [A_s,χ]λ - [D^T,χ]A.
- (5.10) is the identity ½[A_sD^T,χ]A = ½A_s[D^T,χ]A + ½[A_s,χ]D^T A, then added to [A_s,χ]h'. Its second term is a divergence D^T(D w) with w = ½[D^T,χ]A plus a bounded mass term, and the flux uses two cutoff differences and one difference of A.
- (5.11) and p(χΨ) = χp + ½[D^T,χ]A are exact.

The current commutators gain only cutoff oscillations or cutoff differences, via the product identity applied to (3.4). No difference of J appears. The vertex bound (5.8) is the E-part alone with j_β, and its L^q bound is the row-sum argument of (3.5).

## C. pw-bridge Sections 6-7: walk and tree bounds, decoupling, the composed 𝔊

**The four named inputs: correctly scoped.**
- [Energy] is h-walk Lemma L as repaired in `gates/h-walk-gate.md` Section 5: Lemma D restricted to L² and energy spaces, two-difference pillar cutoffs, the graph part read from A_s G'g = g, and (I1) uniform on cut-downs.
- [Coefficients] includes the all-scale absolute second-jet premise that the same gate says must stay explicit. I also checked the Wilson part against `a3-clauses.md` Step 5 and (B1). There d^T d + DD^T = Δ_U + 𝒲_U with |𝒲_U f| ≤ C L² α_0 r^{-2}|f| pointwise. The PX114 remainder, ≤ C||P-1||η²|v|_p|w|_p, and the chart term η|J(U)| ≤ Cα_0ξ^{-2} are finite-stencil coefficients with pointwise bounds. So Δ^W + DD^T is the covariant Laplacian plus a zeroth-order operator bounded in every L^q, which is the form Lemma R needs (not only a form bound).
- [Walk geometry] and [Parameter geometry] are read only where the gates passed them: Theorem W's chaining, Lemma J (7.1), Theorem T with the C_*^{n+Σm_i} repair, Corollary T, and o1-decoupled Definition D, (P) and Lemma P. The failed (C5) locality and reflection assertions are not imported.

**Lemma W∞ (6.1): ADVANCE.** Lemma R is applied only at outputs inside κ^(5/2), where a cut-down is read through h̃_κ or [K, h̃_κ]. y^{++} has local diameter C_L ≪ M_1, so y^{++} ⊂ κ^(7/2). There, by (C2), the cut-down has the original layers, rows, coefficients and j^κ = j. The cut-down's artificial boundary lies outside κ^(7/2) and is never read. The original ∂Ω_0 lies in the bare layer, where point evaluation applies. Combined with h-walk (5.1), d_B^κ ≥ d_B (C3) and ||F||_* ≤ C_L||F||_S, this gives (6.1).

**(6.2)-(6.3): ADVANCE.** The chain alternates bounded operations:
- source multiplication (5.11);
- the local inverse (6.1);
- the commutator (5.7), at cost C_L/M_1;
- the tree vertex (5.8) with (7.1).

The exponent split and the backward pillar sums are those of h-walk Theorem W(b) and Theorem T(b) as gated. I checked the identity 3p_* - |ω| = 2(n - v) + 2Σ(m_i - 1) ≥ 0 directly from |ω| = n + Σm_i + v. The coefficient power C_L^{n+Σm_i} ≤ C_L^{|ω|} is kept, as the gate requires.

**Normalization, (6.4)-(6.7): ADVANCE.**
- The source eδ_c/ξ_c has S-norm C_L|e| and dual norm |e| (the ν-source norm Σ ξ_c²|f_c|²).
- The doubled-traversal count gives #P ≤ 16(1 + 8t/ℓ_P). Each thickened arc has diameter at most ℓ_P/4 + 2R_* < ℓ_P/2.
- With ℓ_P ≥ 2048κ̄/τ_L, the tags cost at most τ_L/16 of the rate. Walks (rate τ_L/2) and trees (rate τ_L/4) keep at least τ_L/8.
- Roots near y are boundedly many, and the counts ν_1^n or C_T^m are paid by M_1-powers. So (6.6) holds with a constant free of M_1.
- (6.7) is the Schur sum against a weight of rate ≤ τ_L/16 with K_{τ_L/16} < ∞ (τ_Lρ' ≥ 256 log L), with ||b||_{Y,w} = sup_c w(c)|b(c)| as defined in `dec-field.md` Section 4 (line 167).

**Section 7, (7.1)-(7.9): ADVANCE.**
- Deleting the ν row leaves T^{-1} = G_1[j] as the AA block (Lemma U(b)), with local decay from (I1)(iii).
- [K_1^{-1}]_{AA} = G_1 - H_1QG_1 = P_1 by Lemma U(c).
- [𝕏^{-1}]_{hh} = 1 - R by Lemma U(a), with at most five inverse factors, so the rate is ≥ τ_L.
- The scalar bootstrap (A_s h = s_λ + Q'^Tμ, A_s λ = s_h - h) gives h, λ ∈ W^{2,8} from L^8 sources, and its commutator sources are the three listed.
- (7.5) is exact: -G_1DRD^TG_1 = -G_1DD^TG_1 + G_1DP_scD^TG_1. This gives the SA 10205 operator G_1 - G_1DRD^TG_1 - H_1QG_1 with its sign and factor order.
- The scaling chain (7.6) is consistent with (5.3)-(5.4).
- In (7.7)-(7.8), the intermediate pillars range over a whole cell intersection, about M_1^4 pillars. They are summed by the retained e^{-(τ_L/16)d} factors, at cost K_{τ_L/16}, not counted. The note does this correctly.
- (7.9) is the same Schur sum.

One point of status. (7.4) is a supplied specification of 𝔊(s), not something read from the outline. This is admissible: SA 10356 and o1-decoupled Definition D say the decoupled operators are "defined the same way from their own expansions", and SA 10370 imposes no identity between undecoupled operators on decoupled sums. Each composite is tagged once on the union of its read hulls, so a term whose hull meets a cube with s_Δ = 0 vanishes. That gives the same splitting mechanism as H(s).

**No difference of J; uniformity: confirmed.** J enters only through multiplication, a shift, or an outer D^T, and Lemma C differentiates only cutoffs. Every constant depends on L, the fixed coefficient and energy constants, and e^{16κ̄}. None depends on η (CZ, the Sobolev steps, the bare-layer point evaluation), on depth or volume (local estimates and Schur sums), or on M_1 (the M_1-powers pay only counts, and the rates are free of M_1). ℓ_P must exceed 8C_L M_1, a constraint on the decoupling geometry that is already part of (P).

**Verdict on pw-bridge: ADVANCE as an implication from [Energy], [Coefficients], [Walk geometry] and [Parameter geometry]; first failing step none.** I found no defect that breaks a statement. Minor points, none breaking anything:
- Section 2 says the paper folder was absent. Literature coverage stays as the note states, and Section D below records what this gate added.
- In 7.1, "with the row-Gram factors omitted" should say that the local decay of the ν-free inverse uses (I1)(iii) for G_1[j] directly. Its inverse words are those of h-walk Lemma L with the W^{-1} factors deleted, so there are no more than Lemma L's 25 and the rate is ≥ τ_L. This is a wording point, not a gap.

## D. nl-r9: the reduced map (4.1)-(4.4) against the outline, and the [NL] bounds

**(4.1)-(4.4) against SA 10368-10389 and 10562-10576: AGREE, as far as the outline specifies; [RED] is an admissible adoption.**

What the outline fixes, and how (4.1)-(4.4) meet it:
- SA 10370-10372 and (j), SA 10562-10568: the reduced expression is formed "before the parameters are inserted", using the identities RD^T H = 0, QH = 1 and Δ_π H = Q^T[(QGQ^T)^{-1} - a] only at s ≡ 1 on shell. Its second-order term Δ_π H must be absent, and "this expression defines W_s for every s and every pair".
  - nl-r9 (4.5) is exactly that identity in raw rows. I checked the unit conversion: H^T f = 𝗆³ 𝖧^T_phys f, K^T = Q^T_phys 𝗆^{-3}, so K^T M = Q^T_phys(W_0^{-1} - a)𝗆^{-1} = EH, and H^T E H = (KH)^T M = M.
  - M is a symmetric matrix in counting measure, because W_0^{-1}𝗆^{-4} is symmetric.
  - (4.4) contains no E and no Δ^W.
- SA (j): "in the only term containing J, the factor r is supplied by the Schwarz lemma". In (4.4) the current enters through one term only, -d'_{3,s}(a)^T p_s. (5.6)-(5.7) replace the Schwarz lemma by an explicit telescoping of the four factors Z^T, Zh, 𝒞''(z), N^T. I redid that telescoping.
- SA (j): W_s "is a gradient only at s ≡ 1 and on shell". (4.4) is the gradient of (4.6) at s = 1. At decoupled s, M_s need not be symmetric, so (4.4) is then a continued expression, not a gradient. This is consistent with the outline.

Check against Balaban (credited; `~/ym4d-papers/cmp102.txt`, CMP 102 pp. 289-291, OCR read against the formula structure):
- At s = 1, (4.4) is the functional derivative of Balaban's V(A') = -<HD_3(A'), J> - <A', Δ_π HD(A')> + ½<HD(A'), Δ_π HD(A')> + V_0(A' - HD(A')), his (80). Here D_3 = D - C^(2) as in his (78).
- Term by term: -d_3'^T p is his (85); -K^T M d - d'^T M K a is his (88), obtained through his identity (87), which is nl-r9 (4.5); d'^T M d is his (89); Z^T N_0(z) is the derivative of his V_0 term.
- His quadratic part ½<A', Δ_π A'> - <HC^(2)(A'), J> (79) is nl-r9's ½<a,Ea> - <p, 𝒞_2(a)>. On the Landau slice it equals the outline's G_1 form.
- So (4.4) is the published form that SA (j) says it continues, with the decoupled H(s), M_s and p_s = H(s)^T 𝐉 inserted.

I also checked the derivation's supporting algebra. The BCH expansion of log(e^{itλ_-} e^{itηa} 𝐔 e^{-itλ_+} 𝐔^{-1})/(iη) gives t(a - Dλ) + ½t²(i[λ_-,a] - i[a,λ^+] - i[λ_-,Dλ]), using [λ_-, λ^+] = η[λ_-, Dλ]. Comparing t-orders of the gauge-invariant inner action then gives D^T J(U) = 0 and E = S^T Δ^W S, the SA 10188-10190 identity.

What the outline leaves open, and nl-r9 supplies:
- (i) The decoupling of M_s: its own -νν walk expansion at j = 0, with the diagonal -a_0 I untagged.
- (ii) The raw-row units.
- (iii) The Taylor subtraction on the unsandwiched 𝒞_2(a). This is forced by DW_s(0) = 0: (2.2)-(2.3) are correct, d_s''(0) = 𝒞''(0) independently of s, and the sandwiched 𝒞_2(Sa) leaves the linear operator S^T Δ^(2)[p] S - Δ^(2)[p].

All three leave the s = 1 on-shell values unchanged. SA 5775-5784 makes W_s "specified holomorphic maps ... [including] their walk coefficients and convergence domains". So adopting (4.1)-(4.4) is admissible as specification, of the same kind as o1-decoupled Definition D and pw-bridge (7.4). The untagged -a_0 I is diagonal, so it couples no wall-components. This matches SA (j)'s remark that "the member -a is diagonal and is carried by no proper set". The response-hypothesis clauses of SA 5786-5800 for this W_s (realness, covariance, restriction, transport) are not part of [NL], and this gate does not check them.

**Section 7 witness (7.1)-(7.3): CORRECT-NO-ADVANCE (scope as stated).**
- D^T J(U) = 0 follows from gauge invariance of the inner action.
- D^T 𝐉 = -(γ_0/η)(-1)^{x_1/η} T_1 for the staggered current.
- {{D^T 𝐉, a_1}, a_2} = (γ_0 t²/η)(-1)^{x_1/η} T_1, from {T_1,T_2} = -T_3 and {T_3,T_2} = T_1.

So a local cubic term that vanishes on the physical-current graph can destroy uniform [NL]. This shows that [RED] has to be stated. It is not a counterexample to (4.4).

**[NL] proof, Sections 3, 5, 6: ADVANCE as an implication from [RED], [Rows], [PW] (field member only), (O1) and the h-walk energy expansion.**
- (3.1)-(3.3): the one-step row and column sums L and L^{-3}, as in a2-curved (8.6). The v_n, p_n induction with Σt_n ≤ (L-1)^{-1}. Then |K_a(c,b)| ≤ C_L η^4 m_c^{-3} from the column sum C_L η L^{-3j}, Σ_b|K_a(c,b)| ≤ C_L m_c, and Cauchy circles of radius c/(m_c sup|h|). Transposes cost η^{-4}, which the density factor cancels.
- (3.4)-(3.7):
  - For traceless 2×2 matrices, tr(XYZ) = ½tr([X,Y]Z) is totally antisymmetric. This gives (3.4), and the quadratic-repeat terms vanish.
  - I recomputed the commutator sum (3.5) pair by pair.
  - Summation by parts puts the one difference on 2[v,w], giving |a||∇a| + η|∇a|².
  - ξ³ × (3.6) ≤ Cr² because η ≤ m. The missing-plaquette boundary lies in the bare layer.
- (5.1)-(5.7):
  - With R = 4r_0/B, 4C_*BR² ≤ R iff 16C_* r_0 ≤ 1, and the Lipschitz constant is 2C_*BR = 8C_* r_0 ≤ 1/4.
  - d' = NA, d''[h,k] = N𝒞''(z)[Zh,Zk], and the transposed identity (5.4) are correct.
  - The transpose bound (1 + H^T A^T)^{-1} on Y_w uses ||H(s)^T||_{F_w→Y_w}.
- (6.1)-(6.2): I differentiated (4.4) and got the same eight terms, including -(d''[h,·])^T H(s)^T N_0(z) from D(Z^T) = -(d''[h,·])^T H(s)^T. All eight bounds check, with B-powers CB²γ_0 r, CBr (×3), CBr² (×3), Cr. The sum is ≤ C_W B² r when γ_0 ≤ 1, B ≥ 1, r ≤ 1. That is SA's b̂² r.

**"[NL] uses [PW] only as stated": confirmed.**
- Only the field member ||H(s)||_{Y_w→X_w} ≤ B of [PW] is read.
- ||H(s)^T||_{F_w→Y_w} is the first sum of (O1). The note's displayed inequality reduces it to exactly sup_c w(c) η^4 Σ_b |H(s)(b,c)| ξ_b^{-3} w(b)^{-1}, which is o1-decoupled Theorem B(c), Codex-gated (row 129). That is an energy-level bound.
- ||M_s||_{Y_w→Y_w} comes from h-walk Theorem W (6.2) on the ν-output, whose 𝒳-norm contains ξ_c³|ν_c|, together with Lemma P's count.
- The H_1 and 𝔊 members of [PW] are not read by nl-r9. They are read by dec-field Proposition 5.1.
- The current enters only through ||p_s||_Y ≤ B||𝐉||_F (via (O1)), so no difference of 𝐉 is taken.
- r_0 (5.1) and C_W depend on fixed L-constants only, not on depth, mesh, volume or M_1.
- The weight ranges are compatible: (O1) holds for θ ≤ τ_L/8 and [PW] for θ ≤ τ_L/16. The ℓ_P floors of o1-decoupled (256κ̄/τ_L, 8r_1 + 1) and pw-bridge (2048κ̄/τ_L, 8R_*) are met together by taking the larger.

**Verdict on nl-r9: ADVANCE as an implication; first failing step none.** I found no defect that breaks a statement.

## E. Literature added by this gate (credited, not load-bearing)

Balaban, CMP 99 (1985) 389-434, pp. 421-422, after (3.130): to bound Δ'_π, "one of the three derivatives there has to be applied either to an expression on the right, or on the left, of Δ'_π". This gives his Theorem 3.3 for G "in all norms ... except the inequality involving the Laplace operator". That is at J = J(U), under his second-difference condition (3.36), (3.38).

pw-bridge (3.4) does the same thing for an independent current with only |J| bounded. It keeps D^T outside the bracket of J and λ, so the current block is a divergence-form source. The lattice CZ estimate then replaces Balaban's derivative transfer. The conclusion has the same shape: first-order supremum bounds, with only p ∈ W^{1,8} and no Laplacian bound. This independent-current version is ours (Codex), not Balaban's. Balaban CMP 109, p. 262, (1.10)-(1.14), cited at SA 10135 for pairs with an independent current, is not re-read here. dec-field-gate already checked that it bounds J only in size.

## F. Verdicts and what moves

| Statement | Verdict |
|---|---|
| pw-bridge (3.2)-(3.3) source combination and reduced equations | ADVANCE (exact) |
| pw-bridge (3.4)-(3.5) current and second-jet terms, no difference of J | ADVANCE |
| pw-bridge Lemma CZ (4.1)-(4.3), with its weak (1,1) and interpolation | ADVANCE |
| pw-bridge (4.4) interior estimates, (4.5) Sobolev steps 2 → 3 → 8 | ADVANCE |
| pw-bridge (5.1)-(5.4) norms and scalings | ADVANCE |
| pw-bridge Lemma R (5.5)-(5.6) bootstrap | ADVANCE, given [Coefficients] |
| pw-bridge Lemma C (5.7)-(5.11) commutator cancellations, vertex bound | ADVANCE (exact) |
| pw-bridge Lemma W∞ (6.1), walk and tree bounds (6.2)-(6.3), with the four named inputs | ADVANCE, as an implication |
| pw-bridge normalization, parameter count and column bounds (6.4)-(6.7) | ADVANCE |
| pw-bridge composed 𝔊 expansion (7.1)-(7.9), including (7.5) = SA 10205 | ADVANCE; (7.4) is a supplied specification, admissible |
| pw-bridge [PW] as stated in its Result | ADVANCE, as an implication from [Energy], [Coefficients], [Walk geometry], [Parameter geometry] |
| nl-r9 (2.1)-(2.3) tests | CORRECT-NO-ADVANCE (correct, scope as stated) |
| nl-r9 3.1-3.2: the constraint calculus (3.1)-(3.3) and the Wilson remainder (3.4)-(3.7) | ADVANCE |
| nl-r9 (4.1)-(4.4) against SA 10368-10389 and 10562-10576 | AGREE where the outline specifies; at s ≡ 1 on shell it equals the derivative of Balaban CMP 102 (80); [RED] is an admissible adoption under SA 5775-5784 |
| nl-r9 (4.2) linear bounds | ADVANCE: the H(s) field member from [PW]; H(s)^T from (O1); M_s from the h-walk energy expansion |
| nl-r9 (5.1)-(5.7), Theorem of Section 6, (6.1)-(6.2) | ADVANCE |
| nl-r9 Section 7 witness | CORRECT-NO-ADVANCE |
| nl-r9 [NL] as stated in its Result | ADVANCE, as an implication from [RED], [Rows], [PW], (O1) |

**First failing step: none, in either note.** I found no defect that breaks a statement. No step bounds a difference of the independent current. Every constant is uniform in mesh, depth, volume and M_1 above the fixed floors. The only M_1-dependence is the parameter-cube floor ℓ_P > 8C_L M_1, which belongs to (P).

**What moves.** Rows 135 and 139 count, as conditional implications. With `gates/dec-field-gate.md` (Proposition 5.1 ADVANCE from [PW] and [NL]), R9's unique small field, joint holomorphy and weighted first response on ||B'|| < cB^{-4} now follow as an implication from:
- [Energy] (h-walk Lemma L with (I1) uniform on cut-downs);
- [Coefficients] (a2-curved (8.3); a3-clauses Step 5 and (B1));
- [Walk geometry];
- [Parameter geometry] (o1-decoupled Definition D, (P));
- (O1) (o1-decoupled Theorem B);
- [Rows];
- the adopted specifications (7.4) for 𝔊(s) and (4.1)-(4.4) for W_s.

Each named input has its own cross-provider gate, as cited in the two notes.

**What stays open (not checked here):**
- The response-hypothesis clauses of SA 5786-5800 for the adopted W_s and 𝔊(s): realness, gauge covariance, restriction to wall-components, transport.
- The s ≡ 1 identification of R9's fixed point with the background response F'(𝐇) = K_𝐇^T λ (SA 10450-10458, outline mechanism (k)).
- The removed-system comparison, dec-field (6.3).
- Complex box localisation 6(c) and the Landau node-lift comparison.
- WF7 (rows 145-148).

The lead decides whether to record (4.1)-(4.4) and (7.4) as adopted data in `library/route-decisions.md` or the ledger. This gate shows only that the adoption is consistent with the outline's prescription and with Balaban's published formula.
