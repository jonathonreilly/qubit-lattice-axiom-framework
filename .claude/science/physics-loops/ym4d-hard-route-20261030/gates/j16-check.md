lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-06T19:41Z

# Check of library/t0-joins.md (J6 proof; J1 reduction)

Provenance: Claude Opus 5.5, max effort, Mac mini worker, fresh session, at commit 0893c31de. One line-by-line reading by one model. Not an audit, not human review. Kind of result: check of our own new text (Codex, row 358). No numeric job was run.

Sources read for this check: `library/t0-joins.md` whole (329 lines); `library/t0-tree.md` §5.4; `library/ph1.md` Theorem 1, Lemmas 8 and 10, Result and change log; `library/cl1.md` Definitions, Imports, Lemmas 4-6, Theorem 9, change log; `library/wr1.md` lines 10-70 and 398-448; `library/in1.md` lines 36-94, Lemma 4 (25)-(26), Theorem 12 and its proof. Outline SA (`YM4_sketch_500.tex`) and CA-I (`theorem_0_complete_account_raw_I.tex`) at `31a47c543775`, fetched once by URL into a scratch folder; SA 66-130 read. Credit: Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, for SA and CA.

Status: in progress. J1 sections are added below as the reading goes.

## J6 (t0-joins.md lines 175-252)

**First failing step: none.**

**Verdict: ADVANCE.** J6 is proved as an implication from PH1 Theorem 1(3)-(4) and Lemma 10 (with change-log item 2), CL1 Lemmas 4-6 for the component, and SR1's extension bound as PH1 Lemma 10 restates it.

Step by step:

1. Statement (lines 179-185). (J6.1) is word for word SA clause (v), SA 118-129: same Θ, same τ_(v,0), v in R^3, same test spaces S_+ (SA 74-78). CL1's E_+,n (support in closed positive time, flat on diagonals) is the same space as SA's S_+,n, since a smooth function that vanishes on an open set is flat on its closure.
2. (J6.2). The component Hilbert space with q(F,G) = σ_ξ(θF̄·G), antilinear in F, and U_x[G] = [τ_(x,0)G] with U_xΩ = Ω is CL1 Lemma 5 (16)-(17) at t = 0, with φ = σ_ξ, as PH1 change-log item 2 supplies it for each component. RP, reflection invariance, reality and translation invariance of σ_ξ are PH1 Lemma 8 (passed to every support point). Correct.
3. (J6.3) on D. The concatenation θF̄·τ_(v,0)G is separated for every spatial v, because the two groups lie in opposite open time half-spaces with compact supports. PH1 (19) holds for all sufficiently large real v in R^4, so it holds for v = (v,0). Then σ_ξ(θF̄) = conj σ_ξ(F) by reflection invariance and reality, and ⟨Ω,[F]⟩ = σ_ξ(F). The limit equals ⟨a,Ω⟩⟨Ω,b⟩. Correct.
4. D_v(a,b) = ⟨Qa,U(v)Qb⟩. Expanding a = Pa + Qa, and using U(v)Ω = Ω and U(v)* = U(-v), the cross terms vanish. Correct.
5. (J6.4). The difference is ⟨Q(a-a'),UQb⟩ + ⟨Qa',UQ(b-b')⟩; Cauchy-Schwarz, ‖Q‖ ≤ 1 and ‖U(v)‖ = 1 give the bound, with no dependence on v. Correct.
6. Density and the limit order (line 223). D (smooth entries) is dense in the C^1 completion by CL1 Lemma 6 and PH1 Lemma 10 (common slotwise mollification). limsup over v of |D_v(a,b)| is at most ‖a-a_r‖‖b‖ + ‖a_r‖‖b-b_r‖, which tends to 0. Correct.
7. (J6.5) mixed tensors are diagonal-flat (line 231). Correct: an internal diagonal is killed by the factor that owns it. At a cross coincidence with time t > 0, Θφ̄ is flat there, since θx has a negative time entry and φ is flat off the open positive-time region. At t < 0 the ψ factor is flat, and at t = 0 both are. A product with one flat factor is flat by Leibniz. This is CL1 Lemma 6, first paragraph.
8. The map j (lines 233-235). Density of strictly positive-time smooth separated tensors in Schwartz topology is CL1 Lemma 4, last two paragraphs. Continuity: |G_{p+q}(Θφ̄⊗ψ)| ≤ C_E^{p+q}((p+q)!)^{k+32} p_{20(p+q)}(φ) p_{20(p+q)}(ψ). This uses PH1 Lemma 10's per-component bound, the fact that reflection preserves p_s, and (20) of CL1 Lemma 6: p_s(f⊗h) ≤ p_s(f)p_s(h). So the sesquilinear form is jointly continuous, approximants are Cauchy in H_ξ, and j is well defined. Leibniz is not needed for a tensor in disjoint variables; the cited weight inequality alone proves (20). This is harmless.
9. (J6.6). A fixed spatial translation is continuous on Schwartz space and preserves positive time and diagonal flatness. It maps compact separated positive-time tensors to the same class, and U(v) is continuous, so j(τψ) = U(v)jψ. Also ⟨Ω,jφ⟩ = lim σ_ξ(φ_r) = G_m(φ). Degree zero follows from j(c) = cΩ. Correct.
10. Conclusion: the full-space form of (J6.3) at jφ, jψ gives (J6.1). The rate is claimed only on D; this is correct, as is the statement that no full-domain rate is asserted.

"Same hierarchy and reconstruction" (lines 246-252): the claims match their suppliers. WR1 Theorem 11 uses H3's Hilbert space of the same component and recovers the supplied extension on diagonal-flat tests (wr1.md 405-407). WR1 claims a unique vacuum, not a Wightman cluster property (wr1.md change log item 2). PH1 clause 3 gives the nonzero component mean c_ξ∫f. The NT1 remark is right: with ker H = CΩ, a nonzero vector in Ω^⊥ means H restricted to Ω^⊥ is not zero, because Ω^⊥ reduces H. These are remarks, and the J4/J5 premises stay open as the note says.

Scope note, not a defect: J6 proves SA clause (v) for PH1's component functionals G_n. It does not identify PH1's components with SA's "canonical components" G_ξ,n beyond PH1 Theorem 1(3). That identification belongs to PH1 and the final assembly, not to J6.
