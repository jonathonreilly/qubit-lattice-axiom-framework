lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-04T17:27Z

# o4-check-1: check of `library/am1-port.md`, `library/ui-port.md`, `library/pd-port.md`

Queue row 206. Started 2026-11-04T05:27Z. In progress; sections are written as they finish.

Provenance: Claude Opus 5.5 (claude-opus-5-5), effort max, Mac mini worker, at branch commit `293adf31f`. One reading by one other model of three Codex notes. This is not an audit and grants no status.

Sources read for the comparison, fetched by URL into a scratch folder and not committed: the Sussman-Alpoge outline `YM4_sketch_500.tex` (sha1 `107abaef`) and `YM3/YM3_I.tex` (sha1 `ea67b3ce`), both at `31a47c543775`. Credit: every argument checked here rebuilds the work of Ethan Sussman and Levent Alpoge (with Claude and Codex as authors of their text). Section numbers of YM3_I are written Y3, lines of the outline SA L.

Kind of result (FINISH item 9): a check of Codex's ports of proofs that YM3_I gives in detail, with the d = 4 changes redone by hand. pd-port Section 5 is new text (not in YM3_I); I checked it as our own text.

## 1. `library/am1-port.md` (S1c, S1g; ranks 11, 12)

**Verdict: ADVANCE. First failing step: none.** Checked line by line by Claude against Y3 L73340-73800 (IV-16-26, IV-14-20, IV-16-31), L78336-78688 (IV-29-11 to IV-29-36), L78688-78808 (IV-29-40) and L78850-79037 (IV-54-9 to IV-54-17). No premise outside the lattice is read.

- **Section 1 (Lemma S): ADVANCE.** Each of the six steps is correct. The projection steps use that adaptation is an orthogonal direct sum, so projection onto the normal line maps Γ onto its normal summand. I agree with the qualification: Lemma S rules out one torus adapted to both normals. It does not prove that every construction must take volume first.
- **Section 2 (setting, DLR, gauge invariance): ADVANCE.** In d = 4 each bond meets 2(d-1) = 6 plaquettes, so the DLR denominator is at least e^{-12β|B|}. A vertex has 8 incident bonds. The weak-limit DLR argument, the e^{±2δ} kernel comparison and the gauge averaging are dimension-free.
- **Section 3 (crossing kernels, split tori): ADVANCE.** I redid these steps.
  - The quaternion identity ½tr(gh^{-1}) = s(g)·s(h) holds, since Re(p q̄) = p·q.
  - The expansion (2) has 4^r terms of weight e^{-β}β^r/r! at order r, so its coefficient sum is e^{3β}. Every feature is bounded by one.
  - At n = e_1 + e_2, a plaquette has corner heights t, t+1, t+2, t+1 in the (1,2) plane. In the planes (1,ν) and (2,ν), ν = 3, 4, the heights are t, t+1, t+1, t. In the (3,4) plane all four are t. So only (1,2) plaquettes with t = c-1 cross. No bond crosses a diagonal mirror. The bonds lying in it point in directions 3 and 4.
  - At a bond cut, each tangential bond of the adjacent layer carries exactly one crossing plaquette. The weight is k(u_b, (w·u')_b) with (w·u')_b = w_x u'_b w_y^{-1}. The single gauge average equals the double average by Haar invariance, so the kernel stays a positive Gram kernel.
  - The fourth direction adds only tangential bonds and plaquettes, as the note says.
- **Section 4 (lower tangent (4), folding (5)): ADVANCE.** I recounted the d = 4 constants.
  - Four positive bonds start at a site. In each of the 6 coordinate planes, 3 plaquettes meet them: the one based at x and those based at x - e_μ and x - e_ν. So n_1 ≤ 18|∂_1D|. At most C(4,2) = 6 plaquettes are based at a site, so n_2 ≤ 6|∂_1D|.
  - The ratio of normalized densities costs 2β(n_1 + n_2) ≤ 48β|∂_1D|. Y3 has 2β(9 + 3) = 24β.
  - ∂_rD lies in (2r-1)^4 translates of ∂_1D.
  - The folding proof is the run-doubling argument of Y3 IV-16-31. I checked the relations τ_{(j-1)v_h} = w_j (j odd) and w_jϑ (j even). It has no dimension-dependent step.
- **Section 5 (IV-29-40 at a diagonal mirror): ADVANCE.** I redid the lattice bookkeeping for n = e_1 + e_2.
  - With generators N(e_1 - e_2), (h/2)(e_1 + e_2), Ne_3, Ne_4, the index is ι = N·h·N^2 = N^3h. Also Q ⊂ NZ^4 because h ∈ 2NN, [Q : Γ_i] = i^3·2i = 2i^4, and Γ_i ⊂ iZ^4.
  - The transversal (7) has |D_i| = ½(2iN)(2ih)(iN)^2 = 2i^4N^3h.
  - Each of the two diagonal coordinates has 4 boundary layers, each a fraction 1/(2iN) or 1/(2ih) of D_i. The coordinates x_3 and x_4 have 2 layers each, each a fraction 1/(iN). This gives (8): 6/(iN) + 2/(ih). The coordinate case gives 6/(iN) + 1/(ih).
  - The array Σ_{Q/Γ_i} τ_vA equals 𝔸^u with M = i. Jensen in the folded measure is used in the right direction. The error term → 0. The index action of Γ_i on Z × T has quotient 2i·i^3 terms, as stated.
  - One small omission: (9) uses an integer r with B_A in a cube x_0 + [0,r]^4, but Section 5 never chooses r. This is wording only (Y3 chooses the cube explicitly).
- **Section 6 (adjacent-layer exchange): ADVANCE.** The polynomial argument is new text in place of Y3's character calculation, so I checked every line.
  - The convolution form (Kf)(g) = ∫k(z,1)f(z^{-1}g)dz holds because k depends on the class of gh^{-1}. So K preserves P_r, and by symmetry it preserves W_r.
  - Strict positivity: ⟨f,Kf⟩ = Σ_I a_I|⟨s_I,f⟩|^2 with a_I > 0 for β > 0, and polynomials are dense.
  - The trace of K on W_r is Σ_I a_I‖Π_r s_I‖^2. Only features of degree at least r survive, so it is at most T_r ≤ β^r/r!.
  - O(4)-invariance of W_r with transitivity gives Σ_j|e_rj|^2 = dim W_r. Then each kernel block of K^{1/2} is at most √(max λ_rj)·dim W_r ≤ C(r+4,4)β^{r/2}/√(r!), a convergent series.
  - The note does not state, but uses, that q_S is invariant under simultaneous gauge maps (so Q commutes with P). This follows because K_S commutes with every unitary R_w, hence so does its positive root. It is a one-line gap, not a failing step.
  - The transfer formula (13), the trace-Hölder proof, the monotonicity Tr C^s ≤ Tr D^s, the exchange limit (0 ≥ i^4ν(φ_ε) - C_ε i^3, both signs of ε) and the skew operator with ⟨q_u, Dq_{u'}⟩ = Φ are all correct.
  - The d = 4 changes are i^2 → i^3 copies per selected height and |∂_1D| ≤ 8(iN)^3.
- **Section 7 (temporal gauge, two layers, common period): ADVANCE.** I recounted the constants.
  - A spatial bond meets 4 spatial plaquettes in three space dimensions, so V_S ≤ 8|S|. Hence Φ ≥ e^{-2β|S|}e^{-8β|S|} = e^{-10β|S|}, and N and the layer weight are at least e^{-12β|S|}.
  - The holonomy of the vertical plaquette is conjugate to ũ_t(b)ũ_{t+1}(b)^{-1}, so (16) holds.
  - The identity θU[ũ] = U[R_{2t_0+1}ũ] holds, and the two DLR states agree on gauge-invariant tests.
  - The determination step needs n-1 ≥ m, as the note says.
  - The bond reflections at 1/2 and 3/2 compose to translation by 2.
- **Section 8 (separation, Borel extension, W_4): ADVANCE.**
  - The translation 2kn lies in 2Z^4 for coordinate and diagonal n. The identity θτ_v = τ_{-v}θ holds for v ∥ n.
  - The L^2 Cauchy-Schwarz bound uses θ_*ν = ν, which is proved just before it.
  - There are 4 coordinate and 12 diagonal normals. Site mirrors, bond mirrors and x_μ = x_λ generate Z^4 ⋊ W_4.

So `am1-port.md` holds as written. Every periodic SU(2) Wilson DLR state at fixed spacing is invariant under aZ^4 ⋊ W_4. It is RP on the bounded Borel algebras of both closed halves at every coordinate site, coordinate bond and diagonal mirror. This closes skeleton nodes S1c and S1g, and the bond-cut case of S1d that `gates/bridge-check.md` item 2 left to this row.
