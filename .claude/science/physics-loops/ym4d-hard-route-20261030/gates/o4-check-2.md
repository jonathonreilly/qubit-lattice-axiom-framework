lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-04T18:00Z

# o4-check-2: check of `library/ak-port.md`, `library/tu-port.md`, `library/ac-port.md`, `library/wightman.md`

Queue row 207. Started 2026-11-04T06:00Z. Sections are written as the check proceeds.

Provenance: Claude Opus 5.5 (claude-opus-5-5), effort max, Mac mini worker, at branch commit `e3e771590`. One reading by one other model of four Codex notes. This is not an audit and grants no status.

Sources read for the comparison, fetched by URL into a scratch folder and not committed: the Sussman-Alpoge outline `YM4_sketch_500.tex` (sha1 `107abaef`) and `YM3/YM3_I.tex` (sha1 `ea67b3ce`), both at `31a47c543775`. Credit: every argument checked here rebuilds the work of Ethan Sussman and Levent Alpoge (with Claude and Codex as authors of their text). Lines of the outline are written SA L, lines of YM3_I are written Y3 L.

Kind of result (FINISH item 9): a check of Codex's ports of proofs that the outline gives in detail (AK, TU, AC, the reconstruction), with the d = 4 changes redone by hand.

## 1. `library/ak-port.md` (S9, rank 18)

**Verdict: ADVANCE as an implication from PD (`pd-port.md` (6)-(10)), O2 and O6. First failing step: none.** Checked line by line by Claude against SA L28888-29823 (AK1-AK50). The note follows the outline's AK step for step. It differs in one place: it builds the kernels from PD's point plates B_{φ;a} = V_{φ,4a}(0,0), a norm limit, where the outline takes a normal-families limit of smoothed kernels (SA L29196-29300). Both routes give the same K_n, by the density formula (7).

- **Section 1 (inputs, (1)): ADVANCE.** (1) is `pd-port.md` (9) with p = 5. Self-adjointness for real labels holds. Conjugate ⟨[G], B[F]⟩ (reality), reflect about the plate time a and translate (reflection invariance), and permute (symmetry). A real radial bump is fixed by the reflection, so the smoothed operator is self-adjoint. Its norm limit B_{φ;a} is too. This is SA (AK8) with ᾱ∘θ = α.
- **Section 2 (tube, products, (2)-(5)): ADVANCE.** I redid each identity.
  - T(v)^* = T(v^*), since the conjugate multiplier is e^{-v̄^0E - iv̄^1q}. T(v)Ω = Ω uses HΩ = P_1Ω = 0. The Taylor coefficient bound r^{-j-k} follows from x^je^{-x}/j! ≤ 1 with x = rE_∓.
  - Padding independence: T((b-a)e_0)T(v-2be_0)T((b-a)e_0) = T(v-2ae_0), and T((b-a)e_0)^*Ω = Ω. So (3) and (4) do not depend on the padding.
  - For real x with x_1^0 ≥ a and gaps ≥ 2a, B_{φ;a}[A] = [(plate at time a)·τ_{2a}A] (from `pd-port.md` (1) and (7) with η = 4a). Induction from the right puts plate i at x_i, as SA (AK18) does.
  - (5): with a = δ/4, 2a = δ/2 < min_i r(v_i) and a ≤ 1/4, so ‖B_{φ;a}‖ ≤ C4^pδ^{-p}‖φ‖_1 per plate and every T is a contraction.
- **Section 3 (removing the smoothing, (6)-(7)): ADVANCE.**
  - For ε < a/16 the bump lies in |t| < a/16 = η/64 with η = 4a. That is the strip of `pd-port.md` (7), and V_{φ,4a} is norm holomorphic on |Re t| + |Im u| < a/8. So (6) holds, and the norm continuity of V gives the limit.
  - The identity B_a[β_ε,φ][G] = [τ_a(β_ε⊗φ)·τ_{2a}G] follows by pairing with [A'] and one translation by a. Both sides are positive-time classes with disjoint supports.
  - (7): the Riemann-sum step, local C^1 continuity and the locally uniform norm limit of the product vectors are correct. The profiles must be C^1 for the left side to be defined. This is implicit in the note.
- **Section 4 (gluing the frames, (8)): ADVANCE.** U_{π,ρ} = U_{0,ρ^rev}, so the four frames give the time charts and the spatial charts. Every time chart meets every spatial chart, since a real configuration can carry any strict time order and any strict spatial order. So the union is connected. Overlaps are convex and contain the real parts of their points. Equality of the two densities on a real overlap follows from symmetry of σ and shrinking bumps. Then the identity theorem gives equality on the overlap. Quarter-turn invariance of the glued function holds by construction, because U_{ν+π/2,ρ} = R_{π/2}U_{ν,ρ} and R_{2π} = 1.
- **Section 5 (Gram kernel, (9)-(10)): ADVANCE.** (x - ae_0)^* = x^* - ae_0, so the adjoint of (4) joins with (4) to give (3) at J(x,y). Every entry of J is in V, since the star preserves V and V is a convex cone. (R_{is}v)^* = R_{is}v^* gives J(R_{is}x, R_{is}y) = R_{is}J(x,y).
- **Section 6 (finite band, (11)-(12)): ADVANCE.** I redid each step.
  - Re(R_{z-ν}v_i)_± = |v_i|e^{∓s}cos(α_i + t - ν), with |α_i + t - ν| < 3π/8. So every rotated pencil lies in a chart, and a_y is entire.
  - π/2-periodicity is the quarter-turn invariance of the glued kernel. The bound e^{pn|s|} comes from (5) with δ ≥ min(1, r_0cos(3π/8))e^{-|s|}.
  - The contour shift gives |c_m| ≤ Ae^{4ms + pn|s|}, so c_m = 0 for 4|m| > pn = 5n.
  - On the coefficients: d/dt f(R_tz) at t = 0 is Lf. So P(L)K_n = 0 on pencils, and then on the connected U_n. The identities Σ_m p_m = 1 and (X - 4im)p_m = const·P give (12). d/ds c_m(R_{is}z) = i(Lc_m)(R_{is}z) = -4mc_m(R_{is}z). Conjugating the coefficients of p_m gives p_{-m}, so c_{-m} = c̄_m on real points.
- **Section 7 (global coefficients, positivity, (13)-(15)): ADVANCE.**
  - The set with no perpendicular pair of nonzero differences is open and dense. Every rotation of it stays ordinary. A time tie and a spatial tie would give two perpendicular nonzero differences, including when the two pairs share a point.
  - At sorted times, J(x,y) is the list of consecutive differences of (θx_k, ..., θx_1, y_1, ..., y_l), because v^* = -θv for real v. So (14) is the Gram matrix of (10).
  - Rotating the half-plane: R_{-ν}θ_ℓ = θR_{-ν}, and the phase law gives the factor e^{4iM(2k)ν}. Hence (15).
- **Section 8 (cut inequality, (16)): ADVANCE.** The left side of the Cauchy-Schwarz inequality has leading term e^{4M(k+l)s}c_{-M(k+l)} as s → +∞, with nonzero coefficient. Each right factor is O(e^{4M(2k)s}) or O(e^{4M(2l)s}). The empty case uses ‖Ω‖ = 1 and M(0) = 0. This is SA (AK50).
- **Section 9 (L^1 labels, d = 4): correct.** Norm convergence of the plates follows from (1), and the derivatives in (12) converge by Cauchy's formula. AK reads only H ≥ |P_1|, so the extra spatial generator does not enter. The only d = 4 change is the plate exponent p + 5 = 5 (Y3 has p_I + 4) and the label space R^2.

Defects, none of which breaks a statement:

1. (14) and the text after it say "arbitrary real positive-half-plane configurations". The coefficients c̃_m are defined only at distinct points. So each configuration in a Gram family must have distinct points. The combined configuration (θx, y) is then distinct, because its two groups lie on opposite sides of the mirror. SA L29717 says "distinct points".
2. The out-of-date pointer "D1 ... starts at C1/OH1" (Section 9) repeats the one `gates/bridge-check.md` item 5 notes. D1 itself stays open.

So S9 holds as an implication: holomorphic product kernels (3)-(5), norm removal of the smoothing (6)-(7), one glued kernel on U_n (8), the Gram representation (9)-(10), the band 4|m| ≤ 5n (11)-(12), boost positivity and the top kernel (14)-(15), and the cut inequality (16) with the empty tuple.
