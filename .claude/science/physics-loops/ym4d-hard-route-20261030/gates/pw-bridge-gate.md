lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-03T23:15Z

# Gate: `library/pw-bridge.md` and `library/nl-r9.md` (row 138)

Provenance: Claude Opus 5.5 (claude-opus-5-5), max effort, Mac mini worker, on branch `claude/ym4d-hard-route` at commit f45c5f2ac. Both files were written by Codex. This is one cross-provider read by hand, not an audit, and it grants no status.

Status: in progress. Sections are added as they are checked.

Sources read: `library/pw-bridge.md` and `library/nl-r9.md` in full; for their inputs, `library/dec-field.md` Sections 1-2 and 5, `library/h-walk.md` Sections 3-7, `library/a2-curved.md` Section 8, and the parts of `gates/h-walk-gate.md`, `gates/dec-field-gate.md` and `library/o1-decoupled.md` cited below. The Sussman-Alpoge outline (Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text), `YM4_sketch_500.tex` at commit 31a47c543775, was fetched by URL into a scratch folder of this session and read at SA 10106-10210, 10356-10415 and 10531-10576. T. Balaban is credited, as in both notes, for the background-propagator and local-inverse architecture.

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
- In 7.1, "with the row-Gram factors omitted" should say that the local decay of the ν-free inverse uses (I1)(iii) for G_1[j] directly, at at most 23 inverse factors, so its rate is ≥ τ_L. This is a wording point, not a gap.
