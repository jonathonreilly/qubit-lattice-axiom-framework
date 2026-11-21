lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-04T18:00Z

# o4-check-2: check of `library/ak-port.md`, `library/tu-port.md`, `library/ac-port.md`, `library/wightman.md`

Queue row 207. Started 2026-11-04T06:00Z, finished 2026-11-04T06:26Z. Verdicts: all four notes ADVANCE, first failing step none (Sections 1-4); moved nodes and bookkeeping in Section 5.

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
2. The out-of-date pointer "D1 ... starts at C1/OH1" (Section 9) repeats the one `gates/bridge-check.md` Section 4 item 5 notes: C1 (P1) is recorded as proved and checked in `library/p2-floor.md`. D1 itself stays open.

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

No defect found. Section 5 reads (9) only at small real s (s_* is chosen small), which is the range Section 4 proves.

So S11 holds as an implication: every M(n) = 0, and the scalar hierarchy is O(4) invariant on separated compact C^1 tuples and on the diagonal-flat extension Σ_n of `s4-s6.md`.

## 4. `library/wightman.md` (O11, the Wightman theory per component)

**Verdict: ADVANCE as an implication from the per-component inputs it names. First failing step: none.** Checked line by line by Claude against Y3 L79749-81160 (Rec1-Rec4, IV-75-22 to IV-76-59) and SA L31533-31889 (the reconstruction hypotheses, RC1, "Phases and full rotational covariance"). The note follows Y3's direct reconstruction step for step, with e_3 → e_4 and SO^+(1,2) → SO^+(1,3). It does not use OS II's continuation theorem; OS II is credited for the method.

- **Section 2 (Rec, point forms, (1)-(5)): ADVANCE.**
  - Full cone: spatial rotations (from O(4)) conjugate the spectral measure, a countable dense set of directions gives E ≥ |n·q| off one null set, and continuity gives E ≥ |q|. Then |e^{-z_4E + iz·q}| ≤ e^{-d(z)E}. This is Y3 IV-75-50's first step.
  - (2) is `pd-port.md` (7) with F, G above η (hence above η/4), and ‖[τ_{-η/4}F]‖ = ‖e^{-3ηH/4}[τ_{-η}F]‖ ≤ ‖[τ_{-η}F]‖. So (Rec4) holds with c_0 = 1/64 ≤ 1/2 and ℘ = 5.
  - The centering paragraph is Y3 IV-75-50. The shift map commutes with θ, conjugation and translations, and the extra term c∫h·⟨[MF],[MG]⟩ is bounded by |c|η^{-5}‖h‖_1 times the pulled-down norms, since η ≤ 1.
  - (4): I checked it in matrix elements. T(ae_4 + w)^* maps [F] to [τ_{(a+w_4)e_4 - w_sp}F], and one common translation by w gives σ(θτ_ηF̄·τ_wh·τ_ηG). The slab condition is |w_4| < c_0(η - η'). Both semigroup arguments are in the open tube exactly when |Re w_4| + |Im w_sp| < η - η'.
  - The Montel step, the shift law, the adjoint and the bound in (5) are Y3 IV-75-27.
- **Section 3 (one field on D_∞, (6)-(11)): ADVANCE.** I redid each identity.
  - ‖A_l‖ ≤ C[1 + 2Γ(l-5)/Γ(l)] from min(s,s',1)^{-5} ≤ 1 + s^{-5} + s'^{-5}.
  - R^a = Γ(a)^{-1}∫t^{a-1}e^{-t}T_t dt and the Beta integral give R^aA_lR^a = A_{l+a}. T_sA_lT_{s'} = R^lB(s,s')R^l follows from the shift law. So q_0(T_sψ, T_{s'}χ) = ⟨ψ, B(s,s')χ⟩.
  - The commutator identity has the right sign: ∂_t q_0(e^{-itH}ψ', e^{-itH}χ') = i[q_0(H·,·) - q_0(·,H·)], since q_0 is antilinear in the first slot. Iterating l + j times with first vector R^lψ gives (10) with the binomial c_{l+j}(f).
  - The domain step works with ψ = (1+H)^j1_{H≤N}φ(f)χ: then the left side of (10) is ‖ψ‖^2, so ‖ψ‖ ≤ c_{l+j}(f)‖(1+H)^{2l+j}χ‖. This gives (11) with l = 6.
  - J = 2π^2∫_0^∞r^3(1+r^2)^{-3}dr = 2π^2·(1/4) = π^2/2.
- **Section 4 (kernels, (12)-(14)): ADVANCE.**
  - Padding independence and (13) are as in AK.
  - I checked the induction: I_η(g_n)Ω = [τ_{η-t_n}h_n], and T_{s_{n-1}} then I_η(g_{n-1}) give [τ_{η-t_{n-1}}(h_{n-1}, h_n)]. Inserting B(η+t', η-t') = T_{η/2+t'}B(η/2,η/2)T_{η/2-t'} joins adjacent factors into T(y_{j+1} - y_j - ηe_4), which is (12) at margin η/2.
  - The tilted tubes {d_u > 0} are convex, because u·Re z - |P_u^⊥Im z| is concave, and they contain the real parts of their points. So the glued 𝒮_n is single valued.
  - The S^3 band density (2/π)√(1-s^2) ≤ 2/π gives Pr(|u·v| < a) ≤ 2a. With a = (2n^2)^{-1}, C(n,2)·2a < 1. So (14) holds with η = min(1, ρ/(4n^2)).
  - The flat-test bound uses the multinomial Taylor remainder (‖x - x'‖_1)^N/N! with ‖x - x'‖_1 ≤ 2ρ and 2^{5n}/(5n)! ≤ e^2. The weight step uses 1 + |x|^2 ≤ 3(1+|y|^2) for |x - y| ≤ 1. Both are right, and ρ^{5n} cancels the kernel's ρ^{-5n}.
- **Section 5 (boundary values, cyclicity, vacuum, (15)-(18)): ADVANCE.**
  - (15) follows from q_f, (8) and (z^*)^* = z with (ιx)^* = -ιx. The tube condition is d(w' - se_4 - ιx) = d(w') - s ≥ 0.
  - ι(iεα) = (iε𝛂, εα^0) has d = ε(α^0 - |𝛂|) > 0 for α ∈ V_+, so (16) holds.
  - (17): ∂_ηF = iD_hF, because ∂_{t_j} = -i∂_{z_{j,4}}. The Taylor remainder with N = p + 1 has an integrable majorant. The constant in (17) uses η_0 ≤ 1.
  - (18): the coefficients of D_h with h_j = 2j sum to n(n+1), and ∫(1+|x|^2)^{-3n} ≤ J^n.
  - Cyclicity: the Fourier step turns real translations into positive-margin T(w) one factor at a time. Each adjoint is taken on D_∞. The non-ordered remainder is O(h) in L^1, and s_{2n} is bounded on the reflected supports. This is Y3 L80788-80865.
  - Spectrum and vacuum: V(t,x) = ∫e^{i(tE + x·q)}dΠ, so p = (E, -q) ∈ V̄_+. Clustering of the component (cluster-port (19)), with σ_ξ(θF̄) equal to the conjugate of σ_ξ(F), gives 1_{H=0} = |Ω⟩⟨Ω|.
- **Section 6 (Lorentz covariance, locality, (19)-(21)): ADVANCE.**
  - The tube {d > 0} is ι(R^4 + iV_+), so Λ̂ preserves it. r_{is}(ιx) = ι(B(s)x), and d(r_{is}ζ) = ζ_4e^{-|s|} for real ζ with ζ_4 > 0. A strip |Re z| < σ_0 also stays in the tube, so the identity theorem carries invariance from small real angles to imaginary ones.
  - Locality is Y3 IV-76-52. I recomputed (21): |P_u^⊥e_4| = sin θ. The slot j = k gives ≥ -η + 4η = 3η. Every other slot has Δh_j ≥ h_*, including j = k-1 and j = k+1, where Δh = h_* + (1-λ)/2. Since cos θ ≥ √3/2, those slots give ≥ ηh_*/2 - AηM = 3η. Then ∂_λI_g = ηI_{-iD'g}, and (17) bounds I_{D'g} uniformly in λ, so |I_g(1,η) - I_g(-1,η)| ≤ 2ηQ_g → 0.
- **Section 7 (dimension): correct.** l = 6 > ℘ = 5, the weight power 3 (the power 2 fails in R^4), the S^3 band density, and SO^+(1,3).

Defects, none of which breaks a statement:

1. **Scope of the inputs, for the lead.** O11 reads O(4), the cone and (2) for one component σ_ξ, not for the averaged limit σ. SA L31799-31831 says this needs the angular chain run for each realized component, with the insertion bound and TU10 uniform in the approximating states. The checked notes allow this:
   - `ui-port.md` is uniform over pairs (ρ_j, ν_j) of periodic states, and the components of `cluster-port.md` Section 8 are such limits, with common centering.
   - `cluster-port.md` Section 8 passes the bounds, W_4 and both kinds of RP to each component, so cone-o6, PD, AK and AC apply to σ_ξ.
   - TU10 must hold for the connected function of each σ_ξ. That needs TU10 in the state-uniform form of `tu10.md` Section 2.
   So the skeleton's input for O11 is O9 (each σ_ξ has O2-O7, which reads S16 for every periodic state), as the O9 row of `t0-skeleton.md` Section 3 already says. The note's Section 1 list ("ac-port.md, Result") should be read that way.
2. The pointer "rooted D1, beginning at C1/OH1" (Section 7) is out of date, as `gates/bridge-check.md` Section 4 item 5 notes. D1 itself stays open.

So O11 holds as an implication: given O9's per-component inputs and the E0' extension (`growth-qf3.md`), each component carries a scalar Wightman theory. It has a separable Hilbert space, the dense invariant domain D_0, a Hermitian tempered field, a unitary Poincaré representation with spectrum in V̄_+, locality and a unique cyclic vacuum, and its Euclidean continuation is the tr F^2 hierarchy on separated and diagonal-flat tests.

## 5. What moved, and bookkeeping for the lead

| Note | Nodes | Verdict | Premises read |
|---|---|---|---|
| `ak-port.md` | S9 (rank 18) | ADVANCE, first failing step none | S8 (`pd-port.md` (6)-(10)); O2; O6 |
| `tu-port.md` | S10 | ADVANCE, first failing step none | S9; O5; S16 (TU10) |
| `ac-port.md` | S11 (rank 19), hence O7 | ADVANCE, first failing step none | S9; S10; O2; O6; `s4-s6.md` Section 6 |
| `wightman.md` | O11 | ADVANCE, first failing step none | O9 per component (O2-O7 for each σ_ξ); E0' (`growth-qf3.md`); `pd-port.md` (7); `cluster-port.md` Sections 8-9 |

This check moves the following (no other file edited here):

1. `t0-skeleton.md` S9, S10, S11: "cited" becomes proved by Codex and checked line by line by Claude (this file), first failing step none. With `gates/o4-check-1.md` (S7, S8) and `gates/bridge-check.md` (O6), every link of the O(4) chain UI-PD-AK-TU-AC is now checked as an implication. O7's open premises are D1 (through S7), S16 (TU10) and E1 (the cutoff sequence). The lattice inputs (S1g and the rest) are checked.
2. O11: proved by Codex, checked line by line by Claude, as an implication from O9's per-component inputs and E0'. The skeleton still calls O11 "corollary, not a clause" (its O11 row) and leaves it for an owner decision (Section 2, row 20). GOAL.md records that decision (owner, 2026-11-03: "Include it"), so O11 is a clause of T0.
3. O11's inputs should read "O3, O5, O9", with O7 taken for each component through O9. SA L31799-31831 states the reason: a symmetry of a mixture need not hold for each component. Section 4, defect 1, gives the details.
4. S16 (TU10): its consumer is the connected function of each component σ_ξ. So the producer must prove TU10 uniformly in the approximating periodic states, as `tu10.md` Section 2 and the skeleton's "F2 → TU10" item already state. A torus-only or averaged-state TU10 does not suffice for O9 or O11.
5. tu-port Section 3 is shorter than SA (TU14)-(TU17). It bounds the spectral mass below L = 1/h, where the cone bounds |q|, and needs no dilation average. It closes no gap in their outline, so it is not a candidate for the Sussman-Alpoge repository under FINISH item 6.

**Stays open.** The premises of this chain:

- D1 (rank 10): S7, and hence S8-S11, O7 and O11, rest on it.
- S16 (TU10), in its state-uniform form.
- E1, which supplies the cutoff sequence that S4, S6 and the components read.

## Result

Kind: a check of Codex's ports of proofs that Sussman and Alpoge give in detail. These are SA AK1-AK50 (L28888-29823), TU1-TU29 and the two-point theorem (L29922-30500), HC1-HC13 and the all-orders theorem (L30508-30866), and YM3_I's direct scalar reconstruction (Y3 IV-75-22 to IV-76-59, L79749-81160). It also checks our own new text: the point-plate route in `ak-port.md` Section 3, the low-energy mass bound in `tu-port.md` Section 3, the imaginary-axis elimination of the critical modes in `tu-port.md` Section 4, and every d = 4 constant. Credit: Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, for every argument ported here; OS II (Osterwalder and Schrader, CMP 42, 1975) for the reconstruction method.

`library/ak-port.md`, `library/tu-port.md`, `library/ac-port.md` and `library/wightman.md` were checked line by line by Claude. First failing step: none in any of the four. Each holds as an implication from its stated premises. I recounted every d = 4 change by hand:

- the plate exponent 5 and the band 4|m| ≤ 5n;
- the endpoint exponent 8 and the critical modes m = ±2, which need u(d) → 0;
- the shape constants of the TU10 class (∫f ≥ (125/128)Ah^4, Lip f ≤ 70A/h, ϑ_* = 1/12000);
- the increments in {0, 1, 2} and the six rotation planes;
- the regularization l = 6, the weight power 3 with J = π^2/2, the S^3 band density, and SO^+(1,3).

The defects are wording or scope only. `ak-port.md` (14) omits "distinct". Two notes carry an out-of-date D1 pointer. O11 must read O(4) and TU10 for each component (through O9), not for the averaged limit. None breaks a statement.

Finished 2026-11-04T06:26Z.
