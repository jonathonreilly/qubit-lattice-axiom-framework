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
