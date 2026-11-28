lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-05T00:52Z

# Check of `library/tc.md` §§3–4 and `library/b4-typed.md` §§3–4 (row 227)

Provenance: Anthropic Claude Opus 5.5 (`claude-opus-5-5`), effort max, Mac mini worker, fresh session. Branch `claude/ym4d-hard-route` pinned at `f4b915fb3`. `tc.md` (Codex, written at `79e6c7ba0`) and `b4-typed.md` (Codex, written at `6d367c519`) as they stand at the pin. Sussman–Alpoge outline `YM4_sketch_500.tex` at `31a47c543775`, fetched by URL into a private scratch folder (32992 lines, sha256 `d7f77d4d…4d6f`), cited as SA nnnn. One reading by the other model. Not an audit; it grants no status. No subagent. No numeric job: none was needed, and every step below is a written argument.

Credit: Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, for the midpoint tent and its quadrature (SA PH20–PH22, 13347–13395), the uniform tent Hessian bound (SA 13323–13345), the near-zero core inclusion (SA ER8, 6586–6600), the extraction bound (SA ER13, 6686–6742), the pointed window remainder (SA PW13–PW18, 13700–13850), the reserve and capacity lemmas (SA 5163–5316) and the direct Wilson channel (SA 5318–5344). OpenAI Codex for both notes under check. Claude for `b2-extract.md` (Theorem P, Proposition W) and `ur-gauge.md` (Lemma 2, Theorem UR), which this check reads.

Kind of result (FINISH item 9): a check of our own text, plus a reading of every outline passage that reads the tensor insertion. Read in full: `tc.md`, `b4-typed.md`, `b2-extract.md` §§2–3 and §7, `ur-gauge.md` Theorem UR and Lemma 2, and the cited SA lines. Not checked line by line: `tc.md` §§1–2 and `b4-typed.md` §§1–2, outside the row; I quote from them only where a reader question needs it.

## 1. Verdicts

Checked line by line by Claude. **First failing step: none.**

| Statement | Verdict |
|---|---|
| `tc.md` §3: the clover fields Q_u, the site tent w_z, R_{uv,z} (2); the families C⁰, C⁻ (3); filing on one cube | ADVANCE |
| `tc.md` §4: linearity, gauge invariance, holomorphy on the core | ADVANCE |
| `tc.md` §4 (4): the pointed affine jet; T(C⁰[c]) = T(C⁻[c]) = c | ADVANCE. It reads (AR) and the Landau bound only on plaquettes with h_z(p) > 0, and those are exactly the leaves it uses (Lemma S, §2) |
| `tc.md` §4 (5): ‖C⁰[c]‖ ≤ C‖c‖α_j², ‖R_{12,13,z}‖ ≤ C₁α_j² | ADVANCE |
| `tc.md` §4: Hessian kernel of R_{uv,z}, uniform moments; C⁻ has the same Hessians | ADVANCE |
| `tc.md` §4: C⁰ completes (TC) for an input E | ADVANCE, conditional on Theorem UR's inputs for E: (FG), (ER8u), (Cl), the Landau bound (5), (En) |
| `tc.md` §4 (6)–(8): C⁻ fails the uniform member bound | ADVANCE |
| `b4-typed.md` §3 with (TC) taken for C⁰: T(H_z) = 0, DH_z(0) = 0, (PW15) per domain, (2), window sum and tail, young ages, (3), the joint potential ball | ADVANCE, as an implication from 𝓘, Theorem UR's inputs for E, (TC) for C⁰, and SA (PW13)–(PW18), (WF4), (WF7), (WF13) as cited |
| `b4-typed.md` §4: its use of SA 5215–5316, and (7) | ADVANCE. It states the capacity criterion faithfully; I redid (7) |
| Reader SA 5060 | accepts C⁰ |
| Reader SA 5066–5082 | accepts C⁰, given `b4-typed.md` §3's inputs |
| Reader SA 6486–6526 | accepts C⁰, given (AR) |
| Reader SA 22879–22918 | does not read the tensor insertion. It reads only the scalar term b_{k+1}(ζ)A, and C⁰[b·1] is exactly SA's tent b·A_{j,z} |
| Further readers found by grep: SA 4020–4022, 5156, 5459, and the Ward route 7010–7014 | accept C⁰ as far as the outline states them. C⁰ meets the direct-channel bound and is dominated by the Wilson tent at real fields (Remark Z, §5); C⁻ meets neither uniformly in j |

So C⁰ can be adopted as our prescribed tensor insertion. No reader in the outline rejects it. What stays open is unchanged by this check: the inputs of Theorem UR for each typed E (above all (FG) and (ER8u) = (ER7)), the box package (BX), and the zone and joint inputs of `b4-typed.md` §4 (history reserve, the formation bound (5), the common capacity allocation).

## 2. `tc.md` §§3–4: what was redone

Notation of `tc.md`: η = L^{−j} = 1/N₀, a = α_j, chart U_b = e^{iηA_b}, ⟨X, Y⟩ = ½ Tr(XY), a(W) = 1 − ½ tr W. The core is SA's hereditary core (SA R4–R6, 5663–5730): |∂𝐔 − 1| < a₀η² on every plaquette, a₀ ≍ α_j, with a₀ ≤ ½.

**Lemma S (support identity; proved here by hand).** For each orientation u, the u-plaquettes with h_z(p) > 0 are exactly the leaves W_{u,r}(x) of the sites x with w_z(x) > 0.

*Proof.* (⊇) A leaf at x has barycentre p̄ = x + η(s_μe_μ + s_νe_ν)/2. In the two plane directions |p̄ − z| ≤ |x − z| + η/2 ≤ 1 − η/2. In the other two, p̄_r = x_r. (⊆) In a plane direction p̄_μ − z_μ = (k + ½)η with |k + ½| < N₀. The corner coordinate nearer to z has modulus |k + ½|η − η/2 < 1. In the other two directions the corner coordinates equal p̄_r. So the corner of p nearest z has w_z > 0, and p is one of its four leaves. ∎

So (AR) (`b2-extract.md` §2, stated "for each bare bond b in the support of h_z") and the Landau first-difference bound (SA 13325–13330, stated for h_z(p) > 0) cover every bond and plaquette that R_{uv,z} reads. The box of (7) also contains every plaquette of A_{j,z}. `tc.md` uses both facts without stating them; they hold.

**Jets, (4).** DW_p(1)[A] = iη ∂A(p), with ∂ the oriented sum. So DQ_u(x)[A] = ¼ Σ_r η ∂A(p_{u,r}(x)). By (AR) and Lemma S, Hℓ is a bare affine potential plus a bare gradient on these bonds. A positively oriented u-plaquette of side η then has ∂(Hℓ)(p) = ηF_u, and ∂(dψ) = 0. Hence DQ_u(x)[Hℓ] = η²F_u. Since Q = 0 at 1, D²(½ tr Q_uQ_v)(1)[A, A] = tr(DQ_u[A] DQ_v[A]). With the extended Hessian (decay clause of (AR)), ½ D²(R_{uv,z}∘P_j)(0)[ℓ, ℓ] = ½ Σ_x w_z(x) η⁴ tr(F_uF_v) = ⟨F_u, F_v⟩. The quadrature is N₀^{−1}[1 + 2 Σ_{r=1}^{N₀−1}(1 − r/N₀)] = N₀^{−1}[1 + (N₀ − 1)] = 1 in each direction. (PH22) gives ½⟨F_u, F_u⟩ for A_{u,z}. For symmetric c the sum is ½ Σ_{u,v} c_{uv}⟨F_u, F_v⟩. DR(1) = DA(1) = 0, so D²P_j does not enter. A_{j,z}R_{uv,z} vanishes to fourth order at 1, so C⁻ has the same first and second derivatives. (4) and T(C⁰[c]) = T(C⁻[c]) = c hold.

Two consistency checks pass. (i) The jet of any member with (D), (C), (G), (Mo) is a quadratic form in F alone: `b2-extract.md` Steps 1–6 use no hypercube. Step 5 removes the constant part of ℓ, and Step 6's two antisymmetries leave only F. Step 2 makes the colour factor δ_ab. So T_{j,z}(E) is a symmetric complex 6×6 matrix, 21 entries, and C⁰ is defined on all of them. (ii) A Euclidean member has jet (b_z/2) Σ⟨F, F⟩ (Theorem P (a)), so T = b_z·1, and C⁰[b·1] = Σ_u bA_{u,z} = bA_{j,z}. So C⁰ extends SA's scalar prescription exactly.

**Bounds, (5).** On the core ‖W_p − 1‖ < a₀η² ≤ ½, so ‖W^{−1}‖ ≤ 2 and ‖W − W^{−1}‖ ≤ 3a₀η². Then ‖Q_u‖ ≤ (3/2)a₀η². For 2×2 matrices ½|tr(XY)| ≤ ‖X‖‖Y‖, so |R_{uv,z}| ≤ (9/4)a₀². SA's |a(U)| ≤ ½‖U − 1‖² (SA 5320–5332) and (PH21) give |A_{u,z}| ≤ ½a₀². With one fixed filing cube X_z, ‖C⁰[c]‖_{j,κ} ≤ e^{κd_j(X_z)} (9/4) a₀² Σ_{u≤v}|c_{uv}|. This is (5), with C independent of j.

**Hessian kernel.** DQ_u(x)[Hδ_b] = η² L_u(b, x), with L_u as in `tc.md` and d_ηH(p) = η^{−1} Σ_{b'∈∂p} ±H(b') (SA 13323). This gives the displayed kernel. Only curls of the response enter. The contour and Landau responses differ by a bare gradient (`ur-gauge.md` Lemma 2), so their curls agree. This step needs no (FG): C⁰ is gauge invariant as a function of the bare field. With |d_ηHδ_b(p)| ≤ Ce^{−m_H|b−z|} on h_z(p) > 0 (all leaves, by Lemma S), the kernel is at most 2C²e^{−m_H(|b−z|+|b'−z|)}. Every moment with m < m_H is finite uniformly in j. SA 13323–13345 is the same estimate for A_{u,z}.

**Completion.** For a typed input E of norm g, Theorem UR (4.1) gives C_m(z) ≤ Cgα_j^{−2}. The second moments of K_z then give ‖T(E)‖ ≤ Cgα_j^{−2}; so does ER13. Hence ‖C⁰[T(E)]‖ ≤ C‖T(E)‖α_j² ≤ Cg, and the residual moments are at most Cgα_j^{−2} + C‖T(E)‖ ≤ Cgα_j^{−2}. The third clause of (1) is thus automatic. The content of (TC) for C⁰ is the jet identity and the member bound. The inputs are Theorem UR's, for E: (FG), (ER8u), (Cl), the Landau bound (5) and (En).

**The witness C⁻, (6)–(8).** P_j = (e^{iηA}, 0) with A = χ·t(x₁ − z₁)T, χ = 1 on a box that contains [z − 1, z + 1]⁴. Then ‖(A, 0)‖_{1,j} ≤ C₀t < r_*α_j, so P_j is in the core by (ER8u), and the real factor is flat. All values of A commute, A₁ = A₄ = 0, and on the box A₂ = A₃ depend on x₁ only. Each positively oriented 12- or 13-plaquette in the box has holonomy e^{itη²T}, whatever its base point. The other four planes have zero oriented sums. So Q₁₂ = Q₁₃ = sin(tη²)T and ½ tr(Q₁₂Q₁₃) = sin²(tη²). By the quadrature, R_{12,13,z}(P_j) = η^{−4} sin²(tη²). By (PH21) and Lemma S, A_{j,z}(P_j) = 2η^{−4}(1 − cos tη²). The two elementary inequalities of (7) are correct. All terms are positive, so C⁻[c_*](P_j) = R(1 + jα_j^{−2}A_{j,z}) ≥ jα_j^{−2}R² ≥ jε⁴α_j²/16. The member norm is at least this value, and ‖E_j‖ ≤ C₁α_j². This gives (8). C⁻ is linear, gauge invariant, holomorphic and filed on the same cube. So the member clause is the only clause of (TC) it fails. The map c ↦ C⁻[c] itself has norm at least cjα_j², so the failure lies in the family and not in the choice of E. The normalisation and the Hessian clause therefore do not fix the member clause.

**Covariance (not read by the listed readers; proved here by hand).** For a signed permutation w about z, C⁰_{j,z}[c]∘w = C⁰_{j,z}[w·c], with (w·c)_{w(u)w(v)} = ε_uε_v c_{uv} and ε_u = ±1 the orientation sign. Indeed w maps the positively oriented u-leaves at x onto the w(u)-leaves at w(x), each run with sign ε_u. W ↦ W^{ε_u}, so Q_u(x) ↦ ε_uQ_{w(u)}(wx). The tents w_z and h_z are invariant under signed permutations about z, and a(W^{−1}) = a(W). Unit translations act as C⁰_{j,z+e}[c]∘τ_e = C⁰_{j,z}[c]. C⁻ is covariant too, so covariance does not separate the two families.

## 3. `b4-typed.md` §3 with (TC) taken for C⁰

The section transposes Proposition W (`b2-extract.md` §7) from G̃ = G − b_jA_{j,z} to H_z = E_z − C⁰[T_{j,z}(E)] − (vacuum). I redid each step of that proof with this replacement.

- *Small domains, linear terms.* They vanish domain by domain, by constant colour invariance. For C⁰ this is direct: DC⁰(1) = 0. The commutator argument of `b4-typed.md` line 91 is correct.
- *Quadratic terms at ℓ_z.* (P20) is replaced by T(H_z) = 0, from linearity of T and (4). Then ½D²(H_z∘P_j)(0)[ℓ, ℓ] = ½ Σ T(H_z)_{uv}⟨F_u, F_v⟩ = 0 for every affine ℓ. This includes the complex affine part of the box pair (WF4), since both sides are polynomials in the coefficients of ℓ. C⁰[T(E)] lives on one fixed domain X_z, which enters this sum like any other domain. Its quadratic term is at most C‖T(E)‖|F|² ≤ Cgα_j^{−2}(α_kσ²)², the large-domain form.
- *Cross and error terms.* They read the moments of K_{H_z}. The third clause of (1) bounds these by Cgα_j^{−2}.
- *Cubic terms.* Cauchy on the ball of radius cα_j needs |C⁰[T(E)]| ≤ Cg there. The ball lies in the core by (ER8u), and (5) with ER13 bounds C⁰[T(E)] on the whole core.
- *Large domains and young ages.* (YA) for the counter-insertion is again the whole-core bound (5).
- *Sums, base points, ν-Cauchy, brackets.* These read norms only, not the form of the counterterm. They are unchanged.

The outline's own proof already covers this replacement. SA 13761–13762: "The same estimate holds after absorbing the member's own tent-action counterterm, with its own Hessian subtracted." Its proof uses only this, at SA 13798–13800: "Consequently its counterterm is another holomorphic family of size C𝗀, with bounded support. Apply the same proof to this family and subtract." C⁰[T(E)] is such a family. SA 13855–13856 allows a different member, with its own cancellation, at each site.

(2) is (PW17), plus "completing the tensor sum costs at most C𝗀ρ²σ⁴e^{−c/σ}" (SA 13816–13817), plus C𝗀e^{−c/σ} for far domains. The tail step is right: e^{c/σ} ≥ (c/σ)^m/m!, so (1 + ρ²σ⁴)e^{−c/σ} ≤ 2m!c^{−m}ρ²σ^{4+α_H} for m ≥ 4 + α_H, σ ≤ 1, ρ ≥ 1. With C_Mσ^{−4} bases, (PW18) gives 2Cgρ³σ^{α_H}. Then ρ² ≤ C(1 + k − j) gives ω_{k+1−j}, and (3) follows. The joint ball follows because V̇ is linear in the direction.

Verdict: ADVANCE. (3) is the typed potential test at ϰ_k = s_k, as an implication from 𝓘, Theorem UR's inputs for E, and (TC) for C⁰, which `tc.md` §4 proves. It is not a proof from 𝓘 alone. (BX), (ER8u) = (ER7) and (FG) for E stay open.

## 4. `b4-typed.md` §4 and SA 5215–5316

The section states the capacity criterion faithfully. I compared each clause.

| `b4-typed.md` §4 | SA 5215–5316 |
|---|---|
| Σ_z V_{ω,z} ≤ V_ω, Σ_z a_{ω,z,b} ≤ 1 | Σ_z W_{ω,z} ≤ W_ω, Σ_z a_{ω,z,b} ≤ 1 (5230–5234) |
| (5): \|L\| ≤ p(C_VV + Σ_b aS) | \|L_{ω,z,i}\| ≤ p_{z,i}(CW_{ω,z} + Σ_b a_{ω,z,b}S_{ω,b}) (5236–5244) |
| (6): r < min{c_V/(2C_V), c_S/2} | 0 < r < min{c/(2C), σ/2} (5256–5257) |
| domain Σ_i\|λ_{z,i}\|p_{z,i} < r | 𝒟_r, "for every z" (5260–5263) |
| "B_A … is not the product of separate survival bounds" | "they do not acquire a product of rarity factors from holomorphy alone" (5299–5301) |

*(7), redone.* At a point in both half-domains, put radii b/(2mq_r) on the differentiated t-coordinates. There are at most |α| ≤ m of them, so they add at most b/2 to Σ|t_r|q_r. The same holds for each use z in λ. So the closed polydisc lies in the domain, and Cauchy's formula gives (7). If q_r = 0, R_A is bounded and entire in t_r, hence constant in t_r. This matches SA 5296–5298 ("those derivatives are zero"). Verdict: ADVANCE. It applies the outline's conditional lemma and does not prove its majorant.

## 5. Does every reader of the tensor insertion accept C⁰?

Yes. I read every line of the three passages in the row. A grep for "counter-insertion" and "typed" found three more readers, treated last.

**SA 5060.** "It also explains why a typed extension must supply all of its prescribed tensor counter-insertions before claiming that the remaining part is irrelevant." The reader needs every tensor component removed. C⁰ is defined on all 21 components and has T(C⁰[c]) = c on each (§2). So E − C⁰[T(E)] has zero pointed jet in every component. *Accepts.*

**SA 5066–5082.** "Include its own scalar counterterm, or the complete tensor counter-insertions for a typed family" (5066). "The supremum in the potential norm must range over the complex pairs and decoupling parameters actually used inside the fluctuation integral, not just real backgrounds" (5072). "The additional typed claim requires the same cancellation at the complex pairs in the integrand, with the full tensor removed. A background extraction formula alone is insufficient for that extension" (5082). In §3 the cancellation is the polynomial identity T(H_z) = 0 at the complex affine part of the box pair (WF4). The member bound for C⁰ holds on the whole complex core. "A variable Wilson weight is a marginal slot" (5080): a C⁰[c] direction is a marginal slot of the same size, ‖C⁰[c]‖ ≤ C‖c‖α_j² against ‖bA_{j,z}‖ ≤ C|b|α_j². `b4-typed.md` line 126 claims no ω for it. *Accepts*, given §3's inputs.

**SA 6486–6526.** "For a Wilson family evaluated after the background map, the analogous normalization requires the linear-response identities in that map. Likewise T[𝖠[c]]=c for a constant allowed curvature tensor c is the prescribed counter-insertion normalization. Neither identity for pulled-back families is proved merely by the coordinate change below" (6521–6526). `tc.md` (4) proves the identity for C⁰∘P_j from (AR), which is the linear-response identity, and not from the coordinate change. *Accepts*, given (AR). One note on conventions: SA 6511–6512 defines T[E] by "second spatial moments" of the polarisation kernel. The pointed tensor fixes the relative moments, since Σ K(x̃, ỹ)(ỹ − x̃)_κ(ỹ − x̃)_λ = −(T_{μν,κλ} + T_{μν,λκ}) when the zeroth moments vanish (`b2-extract.md` Steps 5 and 8). This map kills exactly one direction, the alternating (F∧F) tensor. So under a relative-moment reading the identity is vacuous in that direction and holds in the other 20. C⁰ meets both readings.

**SA 22879–22918.** "When the source is constant, the step preserves the symmetries of (1e), so once b_{k+1}(ζ)A has been extracted only irrelevant terms remain" (22881). This is the only counterterm in the passage; it names no tensor and no insertion. C⁰[b·1] = bA_{j,z} is SA's own tent (PH20), and Σ_z A_{j,z} = A because Σ_z h_z(p) = 1 (SA 13365). *Does not read the tensor insertion*; adopting C⁰ changes nothing it reads. `b4-typed.md` §4 line 169 also cites this passage, for the drop-out fibres. That citation is correct: "The supremum is then taken over the evaluations at ξ … these evaluations form a set fibred over ξ (2c)" (22911).

**Further readers.** SA 4020–4022: "Joint marked derivatives and typed tensor counter-insertions must satisfy their corresponding estimates." This states the obligation; §3 supplies its potential part. SA 5156: "The index e records the entry, its counter-insertions, its carrier, and its particular occurrence. … The formed argument κ_{ω,e} must lie in that entry's original analytic domain." SA 5459: "The evaluation norm here is the norm after the specified unit change and counter-insertions." These zone readers need the counter-insertion's size at formed arguments. C⁰ is a polynomial in the entries of U and U^{−1} = adj U, so it adds no domain condition. Its size obeys the two bounds that SA proves for the Wilson weight:

**Remark Z (proved by Claude, not yet checked by the other model).**
- (Z1) If ‖U_p − 1‖ ≤ α_nη_n² ≤ ½ on its support, then |C⁰_{n,z}[c](U)| ≤ (9/4)‖c‖₁α_n², with ‖c‖₁ = Σ_{u≤v}|c_{uv}|. Over a zone of N_n unit cells this is SA's (zr-regular-weight) (5334–5341), with ‖δc‖_∞ replaced by ‖c‖₁.
- (Z2) If every link is in SU(2), then |C⁰_{j,z}[c](U)| ≤ ‖c‖_row A_{j,z}(U), with ‖c‖_row = max_u Σ_v|c_{uv}|. So the action reserve that SA 5346–5401 needs for the Wilson weight also pays for C⁰.

*Proof.* (Z1) is the proof of (5). For (Z2), write W = cos θ + i sin θ (n·σ). Then X = (W − W^{−1})/(2i) = sin θ (n·σ), and ‖X‖² = sin²θ ≤ 2(1 − cos θ) = 2a(W). By Cauchy–Schwarz, ‖Q_u(x)‖² ≤ ¼ Σ_r ‖X_{u,r}‖² ≤ ½ Σ_r a(W_{u,r}(x)). Hence |½ tr(Q_uQ_v)| ≤ ½(‖Q_u‖² + ‖Q_v‖²) ≤ ¼ Σ_r [a(W_{u,r}(x)) + a(W_{v,r}(x))]. Each u-plaquette is a leaf of its four corners, and a(W) depends neither on the base point nor on the orientation. If h_z(p) > 0, each shifted coordinate s of p̄ − z has |s| ≤ 1 − η/2. The tent is concave on [−1, 1], so τ(s − η/2) + τ(s + η/2) ≤ 2τ(s). Hence the corner sum of w_z is at most 4h_z(p). If h_z(p) = 0, the corner sum is zero, by Lemma S. So Σ_x w_z(x) Σ_r a(W_{u,r}(x)) ≤ 4A_{u,z}(U), and |R_{uv,z}| ≤ A_{u,z} + A_{v,z}. Summing with |c_{uv}|, and using symmetry of c, gives (Z2). ∎

C⁻ fails both bounds uniformly in j. At the real regular pair P_j of (7), C⁻[c_*](P_j) ≥ jε⁴α_j²/16 by (8). Also A_{j,z}(P_j) ≤ ε²α_j², since 2(1 − cos s) ≤ s². So the ratio to the tent is at least jε²/16. These readers therefore separate C⁰ from C⁻, and they accept C⁰ as far as the outline states them. The formation bound for actual histories (`b4-typed.md` (5)) stays open, as it does for the Wilson weight.

**The Ward route (SA 7010–7014).** "One marginal operator remains in 𝔘: a traceless diagonal anisotropy of Wilson's weight. … Put the weight 1+𝖾_{π(p)} on each a_p." On diagonal c, C⁰[c] = Σ_u c_{uu}A_{u,z} is exactly this plane-weighted tent. So this reader also accepts C⁰. The outline does not use this route for rotations: "Rotation invariance in Theorem 0' (1) is obtained along a different route, without any Ward identity (10b), and does not depend on c₁" (7014).

## 6. Defects

None breaks a statement. Three small notes for the owner of the notes:

1. `tc.md` §4 uses (AR) and the Landau bound on the clover leaves, while both inputs are stated on plaquettes with h_z(p) > 0. Lemma S (§2) shows the two sets are equal. The note should state it, since it is why the retained inputs suffice.
2. `tc.md` line 149 ("their responses differ by a gradient") should cite `ur-gauge.md` Lemma 2, which proves it.
3. If the lead adopts C⁰, the "first missing input: (TC)" of `b4-typed.md`'s Result and of row 219 becomes: (TC) holds for C⁰, given Theorem UR's inputs for each typed E.

## 7. Scope note for the lead (How we work, item 0)

The typed tests may not be on T0's path. This is a reading of the outline, not a proof; the lead should confirm it.

- Theorem 0 is subsequential: the correlations "have nontrivial volume-first subsequential continuum limits" (SA 67–69).
- "Weighted and matched-run comparisons and typed Ward estimates are required only for the stronger statements invoking them" (SA 3779–3780).
- The angular proof of G2, which our O7 follows, "assumes neither typed Ward counter-insertions nor vanishing distant-shell flux" (SA 4469–4470).
- "Subsequential separated-correlation compactness follows from its own cutoff- and volume-uniform source bounds … their volume-free proof can use undifferentiated age-resolved rarity without proving the differentiated zone estimates above. Similarly, tuning at one fixed cutoff can follow from its own holomorphic slope and target-crossing estimates" (SA 5115).
- The typed tests serve "the summable matched-cutoff comparison and the resulting whole-sequence tuned convergence" and "the typed tangent contractions, scale-uniform memory estimates, and differentiated anisotropy method for rotations" (SA 5119).

A grep of `library/` and `parts/` finds the typed potential, zone and joint tests only in the B4 notes, `tc.md` and `sa-ledger.md`. The skeleton lists B4 as an input of D1, E1 and C4. SA 5115 says their outline counterparts (source bounds, compactness, tuning at one cutoff) do not need the finer tests. If no T0 node reads the typed tests, then full B4's typed part (rows 219, 227, 228) belongs to the later extension, not to T0. In that case its open inputs ((FG) and (ER8u) for typed E, (BX), the zone formation bound, the capacity allocation) should not get T0 lanes.

## Result

Kind (FINISH item 9): check of our own text (`tc.md`, `b4-typed.md`, both by Codex), plus a reading of the outline's readers. No correction of the outline.

- **`tc.md` §§3–4: ADVANCE**, checked line by line by Claude, first failing step none. C⁰ is linear, gauge invariant, holomorphic on the whole core, filed on one cube, and covariant. It has T(C⁰[c]) = c on all 21 components, ‖C⁰[c]‖ ≤ C‖c‖α_j² and uniform Hessian moments. So it satisfies (TC) for every typed E that meets Theorem UR's inputs. C⁻ has the same jets and Hessians and fails the member bound by the factor j (8). So the normalisation does not fix the family; C⁰ is an explicit choice that works.
- **`b4-typed.md` §3 with (TC) taken for C⁰: ADVANCE** as an implication. It is Proposition W with the tensor counter-insertion in place of the scalar one, and SA's own proof of (PW15) covers that replacement. (3), the typed potential test at ϰ_k = s_k, holds from 𝓘, Theorem UR's inputs for E, and SA's cited window estimates.
- **`b4-typed.md` §4: ADVANCE.** It states SA 5215–5316 faithfully, and (7) is correct. It proves none of the zone or joint hypotheses.
- **Readers:** SA 5060, 5066–5082 and 6486–6526 accept C⁰ (the second given §3's inputs, the third given (AR)). SA 22879–22918 reads only the scalar term b_{k+1}(ζ)A, and C⁰[b·1] is SA's tent. The zone readers (SA 5156, 5459) and the Ward route (SA 7010–7012) accept C⁰ as far as the outline states them. By Remark Z (proved by Claude, not yet checked by the other model), C⁰ obeys SA's direct-channel bound and is dominated by the Wilson tent at real fields; C⁻ does neither uniformly in j.
- **Open, unchanged:** (FG) and (ER8u) = (ER7) for each typed E; (BX); the history reserve, the formation bound (5) and the capacity allocation of `b4-typed.md` §4. Full B4 is still not proved. §7 asks whether its typed part is on T0's path at all.
