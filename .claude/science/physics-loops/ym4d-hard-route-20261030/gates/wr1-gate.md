First failing step: none

# WR1 gate (pass 3): `library/wr1.md`

Referee: Claude Opus 5.5, fresh session, 2026-11-05. One line-by-line reading of `library/wr1.md` (440 lines). I also read `ym4-assembly.md` §1 (T0 clause 4) and §5 WR1, `gates/o4-check-2.md` §4 whole, `ro1.md`, `ph1.md`, and `cl1.md` Lemmas 5, 8 and Theorem 9. SA = `scratchpad/sa/ym4.tex`. No computation was used.

## Findings

1. **Line 40 (H3) and line 403 (Theorem 11, "the cone and unique vacuum (CL1(4), PH1(5))").** Attribution, the same point as `ro1-gate.md` finding 1. For a component, the spatial unitaries and the coordinate cube cone are CL1 Theorem 9(3)–(4) applied with the component's realizing pure states as integrating states. CL1 allows that, but neither CL1 nor PH1 says it for components. Not fatal. Repair: one sentence in H3, or in PH1 clause 3.

2. **Lines 403–405 (scope of the Wightman list).** Remark, not a defect. Theorem 11 claims a unique vacuum. It does not claim the Wightman cluster property, and none of its lemmas proves it. T0 clause 4 (`ym4-assembly.md` §1) does not list that property either, so nothing is missing for T0. If AS1 later wants Wightman clustering, it is a separate step: unique vacuum plus the spectral condition, the classical argument.

## Each claimed Wightman property, and where it is derived

| Claim (Theorem 11) | Derived in | Check |
|---|---|---|
| Separable Hilbert space | H3 | imported from CL1 Lemma 5, applied to the component |
| Hermitian scalar field, tempered | Lemma 3, (12), (15) | yes |
| Dense invariant domain 𝒟_0 ⊂ 𝒟_∞ | Lemmas 3, 8 | yes |
| Tempered vacuum distributions, positivity | Lemma 7 | yes |
| Spectrum in V̄_+ | Lemmas 1, 8 | yes |
| Unique cyclic vacuum | Lemma 8 | yes, from the component's own clustering (6) |
| Poincaré unitary representation, covariance on 𝒟_0 | Lemma 9 | yes |
| Locality | Lemma 10 | yes |
| Euclidean continuation equals the given hierarchy | Lemmas 4, 5, 7 | yes, on separated C¹ tuples and on 𝒮_{Δ,n} |

The OS-type properties are imports H1–H5 for this one component. WR1 does not claim to derive them, and it uses each one only as stated.

## Steps checked (each holds as written)

**Lemma 1.**
- Rotations of the cube cone over a countable dense set of directions give E ≥ |n·q| for each n. Continuity then gives E ≥ |q|.
- [τ_{−η/4}F] = T_{3η/4}[τ_{−η}F], so (7) follows from (4) by contraction.
- Mean restoration bounds the extra term by |c_ξ|η^{−5}‖h‖_1, using η ≤ 1.
- |multiplier| ≤ e^{−d(z)E}, and E^me^{−dE} ≤ m!d^{−m}.

**Lemma 2.**
- Translating both sides by ηe_4 turns ⟨[G], I_η(h)[F]⟩ into σ(θ\overline{τ_ηG}·h·τ_ηF), with both tuples above η. Bound C_insη^{−5}‖h‖_1.
- (11) checked on classes: the shifts compose to τ_{ηe_4+w}h·τ_{2η}F.
- Slab: |t + w_4| < c_slη′ + c_sl(η − η′).
- Holomorphy domain |Re w_4| + |Im 𝐰| < η − η′.
- B(s,s′) = T_{s−η}b_η(0)T_{s′−η} is independent of η. Shift law, adjoint and bound (9).

**Lemma 3.**
- ‖A_l‖ ≤ C_ins[1 + 2Γ(l−5)/Γ(l)].
- R^aA_lR^a = A_{l+a} by the Beta integral; T_sA_lT_{s′} = R^lB(s,s′)R^l.
- The commutator sign: antilinear first slot gives q_f(Hψ,χ) − q_f(ψ,Hχ) = iq_{∂_tf}(ψ,χ).
- Binomial iteration. N = l + j gives the graph power 2l + j = 12 + j.
- Riesz and the domain criterion; Hermiticity and covariance.
- J = 2π²·(1/4) = π²/2, and (1 + Σ|x_i|²)^{−3n} ≤ Π(1 + |x_i|²)^{−3}.

**Lemma 4.**
- Margin independence. Induction (19): shift a_j + η − t_{j+1} = −t_j − η. Each intermediate tuple is positive time because t_{j+1} − t_j − η − c_slη > 0.
- b_η(u) = T(u + ηe_4/2)B_{η/2}T(−u + ηe_4/2). Consecutive factors give T(y_{j+1} − y_j − ηe_4).
- Tilted tubes are convex and contain their real parts.
- S³ projection density (2/π)√(1−s²). With a = (2n²)^{−1}, the bands have total measure < 1. η = min(1, ρ/(4n²)) gives (18).

**Lemma 5.**
- Midpoint displacement: Euclidean norm ≤ 1, ℓ¹ norm ≤ 2ρ.
- Multinomial remainder (2ρ)^{5n}/(5n)!, and 2^{5n}/(5n)! ≤ e².
- 1 + |y|² ≤ 3(1 + |y′|²).
- n^{10n} ≤ e^{10n}(n!)^{10}; C_flat as displayed. Identification with S_n by H1 density.

**Lemma 6.**
- d/dη F = iD_hF because ιx has fourth entry −it. Integration by parts gives I_{(−iD_h)^rg}.
- Taylor remainder sign (−1)^N/(N−1)!. Majorant s^{N−1−p} = 1. Each term bounded using η_0 ≤ 1.

**Lemma 7.**
- (25) in matrix elements: (w*)* = w and e_4* = e_4.
- Approach vectors: d(ι(iεα)) = ε(α⁰ − |𝛂|) > 0.
- (26): Σh_j = n(n+1), N = 5n + 1, ‖D_h^rg‖_1 ≤ [n(n+1)]^rJ^np_{r+6n}(g).
- Schwartz density of tensor sums; positivity.

**Lemma 8.**
- Successive replacement of V(a_j) by T(w_j): the vectors are well defined because T(w_1)* maps into 𝒟_∞. Fourier uniqueness of finite measures.
- Ordered classes are annihilated by (19). The unordered remainder has L¹ size C_Fh, and s_{2n} is bounded on the compact reflected set.
- p = (E, −𝐪) ∈ V̄_+.
- ⟨[F], P_0[G]⟩ = \overline{σ(F)}σ(G), from (6) and σ(θF̄) = \overline{σ(F)}. A translation-invariant vector has Hψ = 0.

**Lemma 9.**
- r_{is} = ιB(s)ι^{−1} checked by substitution, and d(r_{is}ζ) = ζ_4e^{−|s|}.
- Real-angle invariance for small angles, continued by the identity theorem.
- SO⁺(1,3) is generated by rotations and boosts. Isometry and well-definedness of (29); strong continuity; group law.

**Lemma 10.**
- (31) recomputed: Re z = (Δ𝐱_j, ηΔh_j), Im z = −Δt_je_4, and |P_u^⊥e_4| = sin θ = Aη.
- j = k: the term is ≥ −η + Aηδ = 3η.
- j = k ± 1: Δh = h_* + (1 ∓ λ)/2 ≥ h_*. Other j: Δh = h_*. Then the term is ≥ ηh_*/2 − AηM = 3η.
- ∂_λI_g = ηI_{−iD′g}. Lemma 6 bounds I_{D′g} uniformly in λ and η. At λ = ±1 the heights increase in the original and in the swapped order, and the approach vector is ∝ e_0 ∈ V_+.

**Componentwise scope.**
- H1–H5 all concern one fixed σ_ξ (lines 17, 65).
- H2 (O(4)) is RO1 Theorem 9 for that component. H4 is RO1(2) for that component. H5 is the component's own clustering, PH1 (19).
- The unique vacuum (Lemma 8) uses the component's (6), not the mixture.
- No averaged hierarchy enters. This retains `o4-check-2.md` §4, defect 1.

**Against the assembly entry.** Theorem 11 matches `ym4-assembly.md` WR1(a) word for word. Imports SR1, CL1, RO1 and PH1 match (b).

**SA readings confirmed.**
- SA L4622: "The reconstruction theorem itself remains external."
- SA L4625: "Here it is used as an imported theorem."
- SA L28569–28571: "The preceding insertion theorem supplies p = 4". With ℘ = p + 5 (L28789), SA's displayed exponent is 9, as Result item 4 says.
- SA L31143: the centering state is in 𝒢_j.
- SA L31799–31831: per-component scope.

## Verdict

WR1 is a correct conditional implication. For one component with imports H1–H5, every Wightman property listed in Theorem 11, and in T0 clause 4, is derived. The reconstructed theory's Euclidean continuation is the given tr F² hierarchy on separated and diagonal-flat tests. The two findings are an attribution and a scope remark. Neither breaks a statement.

Checked line by line by Claude (fresh session).
