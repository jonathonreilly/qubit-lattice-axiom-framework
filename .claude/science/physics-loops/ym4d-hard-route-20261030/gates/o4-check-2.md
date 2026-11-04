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

## 2. `library/tu-port.md` (S10)

**Verdict: ADVANCE as an implication from AK (`ak-port.md`), O5 and TU10 (S16). First failing step: none.** Checked line by line by Claude against SA L29922-30500 (TU1-TU29 and the two-point theorem). Sections 2, 5 and 6 follow the outline. Sections 3 and 4 take a shorter route than the outline, and I checked both as our own text.

- **Section 2 (axis measure, (1)-(3)): ADVANCE.** The vacuum projection commutes with H and P_1, so ζ_{φ,b} = e^{-(b-a)H}ζ_{φ,a} survives the centering. Then G = K_2 - K_1(φ)K_1(ψ), and (1) holds because AK's (7) at n = 1 gives σ(α⊗φ) = K_1(φ)∫α. The partition into pieces of diameter below d/4 works: two points at distance at least d differ by at least d/√2 in one coordinate, and d/√2 - d/2 > 0. (2) uses a quarter turn and Γ nonincreasing. In (3) the pair (θ(ᾱ⊗φ), α⊗φ) has disjoint planar supports, and the Fubini bound ‖α‖_1^2Γ(2δ) is right.
- **Section 3 (endpoint bound, (4)-(8)): ADVANCE.** This differs from the outline. SA (TU14)-(TU17) averages over dilations λ to get past the zeros of the spline transform. The note instead bounds only the spectral mass m_μ(L) below L = 1/h, where the cone gives |q| ≤ 1/h, and then integrates by Tonelli. I redid every constant.
  - ∫a = 5/8 and ‖a'‖ = 12. b(s) = (1-|s|)^2(1+2|s|) is C^1, nonnegative, ∫b = 1, ‖b'‖ = 3/2. Also b(s) + b(1-s) = 1 on [0,1], so the integer translates of b sum to one. ∫ρ = 5/2 and ‖ρ'‖ = 3.
  - N ≤ (2R/h + 3)^2 ≤ 25R^2h^{-2}, since h ≤ 1 ≤ R.
  - The support of f_i^± has half-widths 3h/8, h/4, 3h/2, 3h/2. The squared sum is 301h^2/64 < 5h^2 < d^2 with d = 5h/2. The distance from the time reflection is 17h/4, which lies in [d, 6d].
  - ∫f_i^± ≥ (5/8)(1/4)(25/4)Ah^4 = (125/128)Ah^4. Since ‖f‖_∞ ≤ 3A, this equals (1/120)·3A·d^4 exactly, so the integral condition holds at ϑ_* = 1/12000.
  - The Lipschitz bound is 3A(12 + 6)/h + (12 + 3 + 1)A/h = 70A/h ≤ 4800A/h ≤ ‖f‖_∞/(ϑ_*d).
  - (6): ‖[f_i^±]‖^2 = S_2(θf_i^±, f_i^±) ≤ 9A^2u(5h/2), and there are 2N terms.
  - (7): for E ≤ 1/h and t ≤ 23h/8, the time transform is at least (5h/8)e^{-23/8} ≥ (h/2)e^{-3}. On |x| ≤ h/4 and |q| ≤ 1/h, cos(xq) ≥ cos(1/4) > 1/2, and the odd part vanishes because b is even. So the spatial transform is at least h/8. This gives (e^{-6}/256)h^4m_μ(1/h) ≤ (6NA)^2u(5h/2) and the stated C_φ.
  - (8): Γ(t) = t∫_0^∞e^{-tL}m_μ(L)dL by Tonelli, and t^8Γ(t) ≤ t^9L_εm_μ(L_ε) + 8!ε.
- **Section 4 (critical frequency, (9)-(11)): ADVANCE.** This also differs from the outline, which proves the uniform strip bound (TU20). The note instead uses AK's finite band |m| ≤ 2 and the bound on the imaginary axis only. That suffices, because a finite sum Σ_{|m|≤2}a_me^{-4ms} that is o(e^{8|s|}) has a_{±2} = 0. R_{is}(r,0) = (r cosh s, ir sinh s) lies in the tube, and E cosh s + q sinh s ≥ Ee^{-|s|} on the cone. Reality gives a_{-m} = ā_m, and x ↦ -x maps R_t(r,0) to R_{-t}(r,0), so a_{-m} = a_m.
- **Section 5 (diagonal measure, (12)-(13)): ADVANCE.** θ_DR_{π/4} = R_{π/4}θ, so the mollified diagonal RP gives (12) in the limit. Centered positivity is ‖v‖_D^2 - |⟨Ω_D, v⟩_D|^2 ≥ 0. |D(t,x)| ≤ Γ(t/√2), so the orbits are bounded by Γ(√2 min t_i)^{1/2}Σ|c_i|. The contraction by iteration, positivity T_s = T_{s/2}^2, injectivity of T_1, H_D = -log T_1 and Stone's theorem for P_D are all correct. This is SA (TU22)-(TU24).
- **Section 6 (fourth frequency, (14)-(16)): ADVANCE.** I redid the identities.
  - The spectral multiplier at R_{is}(t,x) is e^{-tE_s + ixq_s}.
  - The three-term identity holds: for e^{±4iθ} the coefficient is -(C-1) + e^4 + e^{-4} = C + 1.
  - Integrating (15) against w_s, with ∫w_s dμ_{±1} = c_0 + 2c_1cosh(4s ± 4) and cosh(4s+4) + cosh(4s-4) = 2C cosh 4s, gives ∫w_s dν = c_0 - 2c_1cosh 4s. Hence c_1 = 0.
  - Polarization uses G_{φ,ψ}(y) = G_{ψ,φ}(-y) = G_{ψ,φ}(y). The half turn of the (x_4, x_1) plane is in W_4 and fixes the labels.
- **Section 7 (dimension): correct.** Two transverse cell directions give (h^{-2})^2, and the two planar integrations give h^{-4}, so the exponent is exactly 8. Y3 IV-33-53 (Y3 L76117-76150) needs A = 4 + a_Γ < 8, which a bounded u gives in d = 3. In d = 4, u(d) → 0 is needed for the critical modes m = ±2. The note says this correctly.

No defect breaks a statement. TU10 is the outline's (TU9)-(TU10) with the same class and ϑ_*, for the connected S_2^T of `library/tu10.md` Section 2. It stays an open premise.

So S10 holds as an implication: for every pair of real labels the two-plate kernel G_{φ,ψ} is radial, so M(2) = 0 in AK's notation.

## 3. `library/ac-port.md` (S11, the last link of O7)

**Verdict: ADVANCE as an implication from S9 (`ak-port.md` (12)-(16)), S10 (`tu-port.md`), O2, O6 and the diagonal-flat extension of `s4-s6.md` Section 6. First failing step: none.** Checked line by line by Claude against SA L30508-30866 (HC1-HC13 and the all-orders theorem) and Y3 IV-37-27 (Y3 L76854-76912).

- **Section 1 (interface, (1)-(3)): ADVANCE.** (1) is AK (11)-(13), (2) is AK (16) with S10's b_2 = 0, and (3) is AK (15). Labels in C_c^∞ give the same b_n as AK's C_c^1 or L^1 labels, by AK Section 9.
- **Section 2 (polygon divisibility, (4)-(6)): ADVANCE.** I redid the reduction.
  - (4): rotation through π/k permutes equally labelled vertices, and the phase is e^{-4πib_{2k}/k}. This differs from one exactly when k does not divide 2b_{2k}.
  - (5): the diagonal configuration (θ_ℓX, X) with X = Q ∪ A is a distinct completion of S, so it is zero. Then (3) kills the row. The free points (θ_ℓA and B) vary over a nonempty open subset of a connected domain, so real analyticity of c̃ releases both positions and labels.
  - The reflection i ↦ c - i (mod 2k) with c odd fixes no vertex, and its axis is an edge bisector. For j even (c = j - 1) and j odd (c = j, vertex j added), Q = {0, ..., ⌈j/2⌉ - 1} lies strictly on one side. I checked the angles: the arc spans at most π, including j = k for odd k, where vertex k is antipodal to vertex 0. Vertex j need not be in S, because it receives its label from the reflection.
  - Iteration j → ⌈j/2⌉ reaches one point. Translation and the arbitrary choice of φ then give H ≡ 0, which contradicts b_{2k} > 0.
- **Section 3 (discrete convexity, (7)-(8)): ADVANCE.** The increments d_k are nondecreasing integers in {0, 1, 2}, because a_k ≤ 5k/2. So eventually a_k = dk - D. Divisibility gives k | 2D for all large k, so D = 0 and a_k = kb_2. The empty-tuple cut gives 2b_n ≤ b_{2n} = nb_2. This is SA (HC7)-(HC9). Y3 IV-37-27 instead bounds odd n by the split a = ⌊n/2⌋; both are correct.
- **Section 4 (local translations, (9)-(10)): ADVANCE.** θ_jτ_{-ae_j}θ_j = τ_{ae_j}, so ⟨Φ, e^{-tH_j}U_wΨ⟩ = σ(F_-·τ_{(t-d)e_j + w}F_+). That is (9) with t = d + z_j. The modulus of the spectral multiplier is e^{-(d + v_jRe s)E - Im s(v_∥·p)} ≤ e^{-ηE}, by the cube cone in the coordinate-j picture (O6 transported by O2). The derivative bound L^q q! ε^{-q} gives norm convergence of the power series for L|h| < ε.
- **Section 5 (exceptional support, (11)-(12)): ADVANCE.** I checked each step of the induction.
  - Base case: on product boxes that keep both strict time orders, the plates are represented by AK (7). The kernel there is c̃_0, which is invariant under every real rotation once b_n = 0. Fourier tensor approximation converges in every C^r, since the shell sum Σ j^{D+r-1-N} is finite for N > D + r.
  - Every tied pair is separated by a cut in a coordinate μ ≠ 4. This holds because each cut keeps its partition in both frames.
  - Translating the A side by se_4 has slope ±1 in the original frame and ±cos u in the rotated frame, with cos u > 1/2 for |u| < π/3. So cross ties disappear for small s ≠ 0, and internal ties of nearby x are among those of the base point. Hence q ≤ q_0 - 1 on V × I.
  - Holomorphy in s: the first term uses v = e_4, tangential to the cut, with η = d - |Im s|. The second uses v = R_ue_4 = (cos u)e_4 + (sin u)e_1. If μ = 1 it has normal part s sin u, which is harmless for small |s|. The note's "shrink the segment if needed" covers this. The identity theorem then carries zero from I to s = 0.
  - Termination: q ≤ n(n-1).
- **Section 6 (all angles, O(4), diagonal-flat): ADVANCE.** The angle-stepping by a finite cover is correct. Givens elimination with positive pivots leaves an upper triangular orthogonal matrix with diagonal (1, 1, 1, det) = I, so the plane rotations generate SO(4). Rotations act continuously on S_{Δ,n} and preserve flatness. With the density in `s4-s6.md` Section 6, invariance passes to the unique extension Σ_n. Restoring the mean c∫f commutes with rotations.
- **Section 7 (dimension): correct.** The polygon and convexity steps are planar. The band constant 5 enters only through boundedness of the increments. The cone sum in (10) has three tangential coordinates, and the cut induction uses all four coordinates.

No defect breaks a statement. One remark on wording only: Section 4 says "for small real z", but Section 5 uses (9) at every real tangential z = se_4. That is valid, because a tangential translation keeps both groups on their sides of the cut, as in SA (HC10).

So S11 holds as an implication: every M(n) = 0, and the scalar hierarchy is O(4) invariant on separated compact C^1 tuples and on the diagonal-flat extension Σ_n of `s4-s6.md`.
