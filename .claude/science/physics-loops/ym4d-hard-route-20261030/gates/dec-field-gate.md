lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-03T22:14Z

# Gate: `library/dec-field.md` (queue row 134)

Provenance: Claude Opus 5.5 (`claude-opus-5-5`), effort max, Mac mini worker, fresh session. Branch `claude/ym4d-hard-route` at `d16a72623`. Gated text: `library/dec-field.md`, Codex (GPT-6), its own source pin `109d75dfb`. Sussman-Alpoge outline `YM4_sketch_500.tex` fetched by URL at `31a47c543775f3f74013d06dd5d85962358f3b9e` into my own scratch folder (sha256 prefix `d7f77d4da3eb2303`); `SA n` means a line of that file. Balaban read from the OCR layers in `~/ym4d-papers/` (CMP 109 pp. 261-263; CMP 99b pp. 396-397, 417-423). One cross-provider reader, by hand. Not an audit, and it grants no status. No numerics, no subagents.

Credit: Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, for the regular-pair class, the explicit current continuation, R9 and its norms; T. Balaban for the independent-current spaces (CMP 109) and the derivative-transfer treatment of the current form (CMP 99b); Codex for the gated note.

## Verdicts

| Statement | Verdict | First failing step |
|---|---|---|
| Proposition 2.1 and its scope paragraph | ADVANCE | none. Minor wording in the optional constraint aside, see 1.4 |
| Lemma 3.1, (3.3), (3.4) | ADVANCE | none |
| Lemma 3.2, kernel bound (3.7) | ADVANCE | none |
| Lemma 4.1, Theorem 4.2 | ADVANCE as an implication from its named inputs | none |
| Energy example and (4.3) | ADVANCE | none |
| Proposition 5.1 | ADVANCE as an implication from [PW], [NL] | none |
| (5.3) remark on the composed block of 𝔊 | ADVANCE | none |
| Section 6: (6.2) | ADVANCE as an implication | the input attribution "for H, this is o1-decoupled Lemma C1" is WRONG (C1 is one-way), see 6 |
| Section 6: (6.3)-(6.4) | ADVANCE | none |
| Result and "where rank 4 stops" | CORRECT-NO-ADVANCE | accurate at its pin; superseded by rows 135 and 139, see 8 |

The two questions of the row. **[PW] is exactly** the operator content of SA 10383-10384 for the three operators that R9 applies outside W_s, with three precisions (Section 4). **[NL] is not proved** by `library/a3-clauses.md` Section 4: its C member follows from `a3-derivative.md` (11), which that section re-reads at complex pairs, but its W_s member needs its own lane, which row 139 opened (Section 5).

## 1. Proposition 2.1: the counterexample holds

**1.1 Admissibility.** SA 10129-10135 bounds the independent current only by |J| < γ_0 ξ_j^{-3} on L_j, with no difference bound. With every Ω_j equal to the torus, the only layer is L_k with ξ_k = 1 and η = L^{-k}, so the staggered J_1 = (γ_0/2)(-1)^{x_1/η} J_0 has ξ^3|J| = γ_0/2 < γ_0 everywhere. U = **U** = 1, A' = 0 and the real gauge A = 0 meet every other clause, and separation is vacuous when Ω_j^c is empty. Balaban's space has the same feature: CMP 109 p. 262, (1.14), bounds the independent J only by |J| < γ_0.

**1.2 The form.** h-walk §4's c_J is the diagonal of SA's continuation (SA 10168-10190) with λ in place of λ_A, and (3.2) is that formula with (λ_A, λ_C) → (λ, μ). At A = 0 the current form is -⟨i[λ, Dλ], J⟩_f. I rederived (2.3) with the outline's base-point convention (λ evaluated at b_-): for v = W 1_{x}, only the two direction-1 bonds at x contribute, and η^{-4} dc_J(0,λ)[0,v] = η^{-1}⟨i[Z,W], J_1(x) - J_1(x - η e_1)⟩ = (2ab_0/η)(-1)^{x_1/η}, as printed.

**1.3 The slot and the test.** In h-walk's K, the Y-row is Π^T q_λA A + Π^T q_λλ Π Y + X Z, so q_λλ λ sits in the λ-slot, whose principal part is A_s h' acting on the adjoint unknown h'. The current enters the h'-equation as a coupling to λ. Lemma 6.1' (a3-clauses, line 132) needs |(Eu)_μ| ≤ a(r^{-2}|u_ν| + r^{-1}|∇u_ν|) near x; here |λ| = 1 and Dλ = 0 near x, so the right side is a r^{-2}, against a|b_0|/η. At A = 0 and j = 0, nothing else in K_J - K_0 reaches that slot. A fixed rescaling of components changes only powers of r and m, so it cannot remove η^{-1}. The test is valid in the common interior of a cut-down, and p82-curved Proposition 6.2 does consume its E-terms pointwise, component by component, so the refuted step is the one row 130 proposed.

**1.4 Scope and aside.** The scope paragraph is accurate. What fails is absorbing c_J as a pointwise E-term; the field bounds are not refuted. The outline flags the divergence-admitting source itself (SA 10546). In the optional aside (lines 62-68), "two translated bumps with equal discrete sums" gives Q'λ = 0 only if both bumps lie in the same top block, or if the sums are the Q'-weighted means of each block. Choosing the second bump inside the block of x with matching weighted mean repairs it. Proposition 2.1 does not use the aside.

**1.5 Agreement with Balaban.** Balaban never treats the current form as a pointwise perturbation. CMP 99b p. 396, (3.36), bounds only the size of D*∂A, and p. 419 uses it only to make J = D*η^{-2} Im ∂U small. At p. 421, after (3.130), he writes that one must be careful with the third term of Δ'_π (3.120): "one of the three derivatives there has to be applied either to an expression on the right, or on the left, of Δ'_π", and on p. 422 he applies D* to A_1 in (3.131). At p. 423, after (3.138), the derivatives "have to be applied either to the operator on the right, or on the left, because kernels of the operators defining Δ'_π + Δ^(2) are not regular enough". This is the published form of Proposition 2.1's diagnosis. The bodies of (3.131) and (3.138) are garbled in the OCR layer, and the PDF could not be rendered on this machine, so the prose is quoted and the displays are not.

## 2. Lemmas 3.1 and 3.2: hold

**Lemma 3.1.** I re-expanded the polarisation (3.2) and bounded each of its six terms with |J| ≤ γ_0 m^{-3}. The four mixed terms give γ_0 ‖m^{-2}λ‖ ‖m^{-1}C‖ (and the same with the roles swapped). The two difference terms give γ_0 ‖m^{-2}λ‖ ‖m^{-1}Dμ‖. Every factor is in the energy or graph norm. Transports cost e^{cα_1} at most, since η|A'| < α_1 η/ξ ≤ α_1. No difference of J and no M_1 enters. (3.3) is the exact weak identity with |f_0| ≤ C|J||Dλ| and |f_1| ≤ C|J||λ|. In (3.4), the base point of χ D λ is b_-; the commutator bound C_L γ_0 /M_1 follows from |Dχ| ≤ C_L/(M_1 m), as stated.

**Lemma 3.2.** In (3.7), on the Brillouin torus the multiplier λ(p)^{-1} times q difference symbols is O(|p|^{q-2}). The ball |p| < 1/R contributes R^{-q-2}. Outside it, q+3 integrations by parts in a coordinate with |x_μ| = R leave ∫_{1/R} p^{-5} p^3 dp ≤ R. Cutoff derivatives scale the same way, so the result is C R^{-q-2}. Restoring the mesh gives (|x|+η)^{-2-q}. Dyadic shells give r|g| + r²|F| for the value and (1 + log(r/η))|g| + r|F| for the gradient. The harmonic remainder needs telescoping in four directions and Cauchy-Schwarz (r²), then nested Caccioppoli steps (r^{-|α|}), which gives r^{-2}‖h‖_2; with r ≥ 16η there is room for the five nestings needed. (3.5)-(3.6) follow. The closing paragraph's η^{-ε} Hölder size of the staggered flux is right, and it is correctly labelled "not an impossibility result".

## 3. Theorem 4.2: an implication from the named inputs

**Inputs, as read.** h-walk Lemma L and Theorem W(b), (6.2), are ADVANCE after the graph-norm repair (`gates/h-walk-gate.md` §§5-6), conditional on (I1) holding uniformly on every cut-down. Theorem T(b) needs the branch-constant repair (gate §7: retain C_*^{n+Σm_i}, absorbed into C_T), and the count (c) holds as repaired. The second-jet coefficient premise is kept explicit (gate item 5), as dec-field does. Hypothesis (P) was pending at dec-field's pin. It now has a gate: `gates/o1-decoupled-gate.md` §2.1 ADVANCE, satisfiable uniformly in depth for a grid of side ≥ ℓ_P ξ_max/2 with room for three cubes per direction. The cross-sequence clause (C5) is not read, which is correct, since Theorem 4.2 compares no two sequences.

**Arithmetic, redone.** Lemma 4.1: an Euler tour has length 2t, so there are ⌈8t/ℓ_P⌉ arcs of length ≤ ℓ_P/4. Their R_*-neighbourhoods have diameter < ℓ_P/2 once ℓ_P > 8R_*, so each meets ≤ 16 cubes, which gives (4.1). With ℓ_P ≥ 1024κ̄/τ_L, 128κ̄t/ℓ_P ≤ τ_L t/8, leaving e^{-(3τ_L/8)t} for W terms and e^{-(τ_L/8)t} for T terms. The unit ν-source has norm ξ_c, cancelled by H = 𝖧m^{-1}. The roots meeting an output pillar are boundedly many (bounded overlap, independent of M_1). The floors give the two geometric series ≤ 2. The weight ratio is ≤ e^{(τ_L/16)d}, so the row sum is ≤ C_L K_{τ_L/16}, which is finite because τ_L ρ' ≥ 256 log L (h-walk §5). Holomorphy follows from normal convergence. The constants are C(L)e^{16κ̄}, with M_1 entering only through the floors and ℓ_P > 8C_L M_1.

**Specification note, not a defect.** Theorem 4.2's H_1(s) is Σ_ω s^ω [T^(1)_ω]_{Aν}, with tags over the full decorated hull and with K^(0) (hence j^(0)) left untagged inside the local operators. That is consistent with SA mechanism (g), "the part of walk length zero stays in the local operators", and with o1-decoupled Definition D's "defined the same way". Every reader of H_1(s) must use this same assignment.

The energy example below (4.2) and (4.3) are correct and correctly scoped: ‖A‖_E² = 8 + η², with sup|A| = η^{-1} and sup|∇A| = η^{-2}.
