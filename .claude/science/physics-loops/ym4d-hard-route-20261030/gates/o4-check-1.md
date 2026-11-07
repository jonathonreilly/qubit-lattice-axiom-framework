lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-04T17:27Z

# o4-check-1: check of `library/am1-port.md`, `library/ui-port.md`, `library/pd-port.md`

Queue row 206. Started 2026-11-04T05:27Z, finished 05:52Z. Verdicts: all three notes ADVANCE, first failing step none (Sections 1-3); moved nodes and bookkeeping in Section 4.

Provenance: Claude Opus 5.5 (claude-opus-5-5), effort max, Mac mini worker, at branch commit `293adf31f`. One reading by one other model of three Codex notes. This is not an audit and grants no status.

Sources read for the comparison, fetched by URL into a scratch folder and not committed: the Sussman-Alpoge outline `YM4_sketch_500.tex` (sha1 `107abaef`) and `YM3/YM3_I.tex` (sha1 `ea67b3ce`), both at `31a47c543775`. Credit: every argument checked here rebuilds the work of Ethan Sussman and Levent Alpoge (with Claude and Codex as authors of their text). Section numbers of YM3_I are written Y3, lines of the outline SA L.

Kind of result (FINISH item 9): a check of Codex's ports of proofs that YM3_I and the outline give in detail, with the d = 4 changes redone by hand. Two parts are new text, in neither source: pd-port Section 5 and the polynomial argument of am1-port Section 6. I checked both as our own text.

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

So `am1-port.md` holds as written. Every periodic SU(2) Wilson DLR state at fixed spacing is invariant under aZ^4 ⋊ W_4. It is RP on the bounded Borel algebras of both closed halves at every coordinate site, coordinate bond and diagonal mirror. With this check, skeleton nodes S1c and S1g are proved by Codex and checked line by line by Claude, first failing step none. So is the bond-cut case of S1d, which `gates/bridge-check.md` item 2 left to this row. These nodes read no RG input.

## 2. `library/ui-port.md` (S7, rank 17)

**Verdict: ADVANCE as an implication from full rooted D1, S1g and S6. First failing step: none.** Checked line by line by Claude against Y3 L79070-79201 (IV-18-24, IV-55-9, IV-55-19), Y3 L79210-79443 (IV-55-32, IV-56-17), SA L28229-28521 (UI1-UI10), SA L23740-23870 ((ST4)-(ST9)) and SA L24042-24180 ((GS1)-(GS4)).

- **Section 2 (finite RP, chessboard, domination (3)-(5)): ADVANCE.**
  - The bond-splitting RP proof is a valid alternative to the gauge-averaged kernel of am1-port Section 3. Split a crossing bond as U = VW^{-1}, with V on the positive side. The crossing plaquette then has trace tr(AB^{-1}), where A = V_x^{-1}u_bV_y and B = W_x^{-1}u'_bW_y. So its weight is e^{-β}e^{βq(A)·q(B)}, and reflection exchanges V and W.
  - The run-doubling chessboard, the triangle inequality, p(zD) = |z|p(D) and p(D̄) = p(D) are correct.
  - I recounted the boundary cost in (4). Put n = ℓ/a. For one plaquette orientation (μ,ν), the plaquettes meeting the bonds anchored in the cube have base points in D ∪ (D - e_μ) ∪ (D - e_ν). That is n^4 + 2n^3 plaquettes. The interior has n^2(n-1)^2, and the torus has n^4. So the excess terms number 4n^3 - n^2 and 2n^3 - n^2. The interval length is at most 2(6n^3) per orientation. Six orientations give 72βn^3, as stated. Divided by N = (ℓ/l)^4, this gives 72βl^4a^{-3}ℓ^{-1}.
  - The steps log(1+tV) ≥ tV - t^2V^2 and log p(1+tV) ≤ tp(V), the order of limits, the phase choice and the coarsening are correct.
- **Section 3 (IV-55-9): ADVANCE.**
  - The identity θ_cθ_{c+l/2} = τ_{-le_4} holds as an identity of maps. It gives ⟨B,T_DA⟩_c = ⟨T_{D^♯}B,A⟩_c from translation invariance alone. K_D is formally self-adjoint because D^{♯♯} = D.
  - The two Cauchy-Schwarz pairs in (6) are right, and so is the log-convexity step to (7), including the cases s_0 = 0 and s_1 = 0.
  - I checked the coarse geometry for n ∈ dN. The 2n column factors fill coarse cells 0 to 2n'-1. The endpoints sit in cells -1 and 2n'. So no endpoint shares a coarse cell with a column factor.
  - Midpoint reflection preserves p. The global reflection at c + l/2 (a site mirror, since l/a is odd) maps the dissemination of D onto that of θ_{c+l/2}D, because θ_mid g_k = g_{-k}θ_mid for every board map g_k.
  - The order of limits (volume first, then n-th roots) is the outline's (UI3)-(UI5). The liminf form of q_D is stronger than the outline's limsup form, and it is valid by (ST3).
- **Section 4 (uniform middle-cell normaliser): ADVANCE.** This is the main d = 4 bookkeeping, and I redid all of it.
  - (10) is (ST5) with C_0 = C_+ + C_-. The bound ‖W^ch‖ ≤ 2|z|t_h is (ST7), using the l/4 face margin.
  - The rooted count (11) is (GS1). Every closed cube that meets a grid edge contains an endpoint of that edge (I checked this coordinate by coordinate). There are 16 corners and 2d = 8 walk directions, and each vertex lies in 16 cubes. So κ_D = 22 log 2 is a valid rate.
  - (12) is (GS2)-(GS3), with root cubes counted as C(1 + u/(Ma_s))^4 ≤ C(1 + u/a_s)^4.
  - The normaliser E_{h,ℓ} averages the retained terms over cells, so no covariance of D1's terms is needed. On odd cells, conj(g(z̄)) is holomorphic and has the same real part.
  - A discarded nonzero term has diam X^+ ≥ l/4 and diam X^+ ≤ Ca_s(m+1), so m ≥ cl/a_s - C.
  - The two costs in (13) are correct. Merging the outline's two finer ranges into one (a_s < l) is valid, since a negative lower bound on m is absorbed into C_2.
  - I checked B_0 term by term: Σ_{j≥0}L^{-4j}, then (1+L^j)^4 ≤ 16L^{4j}, then e^x ≥ x^6/6!, then Σ_{j≥1}L^{-2j} ≤ 1/(1-L^{-2}).
  - The Montel step is right. At fixed cutoff, |E_{h,ℓ}| is bounded by the point terms and Cl^4Σ_{s≤K}a_s^{-4}. The subsequence depends only on torus data.
  - The other mesh ratios are covered. For 3 ≤ l/a < 64 there are fewer than 64^4 barycentres per orientation in a cube of side l/2 < 32a, so ‖O_a(h)‖_∞ ≤ 12·64^4‖h‖_∞. For l/a = 1, every barycentre has two half-integer coordinates, so none lies in the middle cube of sup-radius a/4. For L ≥ 3 these ratios exhaust the powers of L.
- **Section 5 (IV-55-19): ADVANCE.** The holomorphy of Φ at fixed cutoff, the Cauchy estimate at radius → ϱ/t_h, the second state ν with A = B = 1, and the D = 1 case for the scalar term give (16) with 2Q/ϱ. The possibly divergent E'(0) cancels, as the note says.
- **Section 6 (IV-56-17): ADVANCE.**
  - With L ≥ 3, the radius is below l(1/8 + 1/18) = 13l/72 < l/4, and |y_{*,4}| + l/2 ≤ η(1/8 + 1/90 + 1/10) = 17η/72 < η/4. Y3 writes L ≥ 13 here only because that is its standing convention; L ≥ 3 suffices.
  - c is a bond mirror, and 2c and -l are lattice translations, once K_j ≥ i + 2.
  - The centering numbers of θ_cB_j match those of θF because ν_j is θ_c-invariant (S1g). So the lattice norm tuples are centered moments of fixed separated tuples.
  - The identification (18) is right, since τ_{-c}θ_c = θ_0τ_{-c}, and both semigroup times c + η/4 and η/4 - c - l are positive by (17).
- **Section 7 (d = 4 changes): correct and complete** for this small-ball form.

So rank 17 holds as an implication: c_I = 1/(40L) < 1/64, p = 0 and C_I = 2Q_0/r, where Q_0 = max(e^{B_0}, e^{12r·64^4}). The constant does not depend on the cutoff sequence, the states, the support position, or the number or coefficients of the surrounding fields. This matches Y3 IV-56-18 (p_I = 0), and it implies the outline's (UI10) with η^{-4}.

## 3. `library/pd-port.md` (S8; the RPM1 shortcut)

**Verdict: ADVANCE as an implication from S7 (UI with p = 0), O6 and local C^1 continuity of the separated moments. First failing step: none. Section 5 (the counterexample) is correct.** Checked line by line by Claude against SA L28530-28860 (PD1-PD19), Y3 L75696-75830 and L76220-76500 (IV-32-34, IV-32-38, IV-34-17, IV-34-30, IV-34-42), RPM1 L2430-2600 and QED3 L21660-21690. RPM1 and QED3 were fetched from the same commit (RPM1 sha1 `a11fffe0`).

- **Section 2 (bounded insertions, analytic translation): ADVANCE.**
  - (1) holds. I checked ⟨[A], [(τ_{η/4}h)·τ_{η/2}B]⟩ = b_{h,η}(A,B) by one time translation of σ, using τ_{-η/4}θ = θτ_{η/4}.
  - ‖T(z)‖ ≤ 1 holds because Σ_j|Im z_j||q_j| ≤ (Σ_j|Im z_j|)E on the cone.
  - In (2), the factor T(η/8 - x) moves Ψ to entries above η/8 - x_4 > 0. That is the region where B_{h,η/2} acts. The product of the three factors is θF̄·(τ_xh)·G after one time translation.
- **Section 3 (parametrix): ADVANCE.** I redid the d = 4 calculus.
  - With Δf = f'' + (3/r)f', Δ(r^2 log r) = 8 log r + 6 and Δ log r = 2r^{-2}. Away from zero Δr^{-2} = 0, and as distributions Δr^{-2} = -2|S^3|δ_0 = -4π^2δ_0.
  - So Δ^3G = -Δ(r^{-2})/(4π^2) = δ_0. The boundary errors O(ε^4|log ε|) and O(ε^2) are right.
  - Scaling: Δ^3[r^2n(x/r)] = r^{-4}[δ_0(x/r) - s(x/r)] = δ_0 - s_r, since δ_0(x/r) = r^4δ_0.
  - ‖n_r‖_♯ ≤ Cr uses G ∈ C^1 (∇G → 0 at 0), and ‖s_r‖_♯ ≤ Cr^{-5}.
- **Section 4 (density, plates, compatibility): ADVANCE.**
  - The polydisc: η/32 + 4·η/128 = η/16 < η/8.
  - The Cauchy factor is 6!(128/η)^6, and the coefficient sum of Δ^3 is 4^3.
  - (6): η^{-6}·εη + (εη)^{-5} = Cη^{-5}, so ℘ = p + 5.
  - In (7) the integration by parts is legitimate. The matrix element is real-analytic on the strip, k has compact support, and Δ^3 is even, so the sign is positive.
  - (9) follows from [τ_{-a}F] = e^{-(b-a)H}[τ_{-b}F] on a dense set.
  - I checked (10) by moving T((a-a'+t)e_4 + ue_1) to the left factor as its adjoint. The conditions a - a' > ±t are exactly positivity of the two semigroup times.
- **Section 5 (optimality, RPM1 threshold): ADVANCE.** This is new text, not in SA or Y3, so I checked every computation.
  - ∫λ^3e^{-λs}dλ = 6s^{-4}. The substitution v = |x|^2/(4s) gives C(x) = (6/16π^2)·4^5·4!·|x|^{-10}, which is positive.
  - In (12), the change λ = E^2 - |q|^2 at fixed q has dλ/(2ω) = dE. So the measure is (2π)^{-3}(E^2 - |q|^2)^3 dE d^3q on E > |q|.
  - The generalized free field is RP and O(4)-invariant. It satisfies O6 particle by particle.
  - I rederived the slab operator from the sharp-time picture as e^{-(a+t)H}φ_0e^{-(a-t)H}. The creation part is a^†(f_+)e^{-2aH} and the annihilation part is e^{-2aH}a(f_-), with the note's labels.
  - (13) needs a - |t| ≥ η/16 on the support of h. This holds because c_I = 1/(40L) ≤ 1/16. The weights are ∫_{|q|<E}(E^2 - |q|^2)^3d^3q = cE^9, so ‖f_±‖ ≤ Cη^{-1} and ‖E^{-1/2}f_±‖ ≤ Cη^{-1/2}.
  - The whole-space bound is correct. The creation part has ‖a^†(f)e^{-2aH}v‖^2 ≤ (‖E^{-1/2}f‖^2‖H^{1/2}e^{-2aH}‖^2 + ‖f‖^2)‖v‖^2, and the annihilation part is its adjoint. With ‖h‖_∞ ≤ c_Iη‖∇h‖_∞, UI holds with p = 0.
  - Lower bounds. On the region E ∈ [1/a, 2/a], |q_1| ≤ 1/(4a), q_⊥ in a ball of radius δ (or δ/a for the scaled label), with δ small: e^{-2aE} ≥ e^{-4} and (E^2 - |q|^2)^3 ≥ ca^{-6}. The region volume is ca^{-2} (or ca^{-4}). So ‖B_{φ;a}‖ ≥ ca^{-4} and ‖B_{φ_a;a}‖ ≥ ca^{-5}. (14) holds because BΩ = a^†(e^{-aE}φ̂)Ω, and the model's continuous density equals V_η by uniqueness.
  - The integer argument is right for ℘ < 4. The cut inequality with (a,b) = (k-1,k+1) makes the even terms convex. M_2 = 0, so every increment is 0 or at least 8. A positive increment contradicts M_{2K} ≤ 2℘K < 8K. Then b = 0 kills the odd terms.
  - M_n = 4n satisfies every hypothesis at ℘ ≥ 4. This matches RPM1's own Lemma `lem:integer`, which needs M_n ≤ 3n < 4n.
  - The QED3 remark is correct: QED3 L21665-21686 applies RPM1 Theorem A through the Gaussian bound E e^{F(f)} ≤ e^{‖f‖_2^2/2}.
- **Section 6 (dimension count): correct.** Y3 IV-34-30 costs (2r)^3·r^{-7}, giving ℘ = p_I + 4 in d = 3. In d = 4 the four-variable weight costs r^4·r^{-9} = r^{-5}. For IV-34-17 the label needs two partition directions, so r^2·r^{-5}·r^{-2} = r^{-5}.
  - The note's pointer "D1 ... beginning with C1/OH1" is out of date, as `gates/bridge-check.md` item 5 says for the other notes. D1 itself stays open.

So S8 holds as an implication: the analytic density (6)-(7), the L^1 bound, the plate bound (8) with ℘ = 5, and the compatibility identities (9)-(10). No bound sharper than ℘ = 5, uniform over L^1 labels, follows from UI and O6. Even fixed labels cannot reach ℘ < 4 from these inputs. So the RPM1 shortcut is closed on these inputs, and TU and AC stay on the route. The model shows this only for the plate-exponent shortcut. It is not a non-covariant example; the model is O(4)-invariant.

## 4. What moved, and bookkeeping for the lead

| Note | Nodes | Verdict | Premises read |
|---|---|---|---|
| `am1-port.md` | S1c, S1g (ranks 11, 12); also S1d (all three cut types), S1e, S1f, S1h (Lemma S) | ADVANCE, first failing step none | none (lattice only, fixed spacing, β ≥ 0) |
| `ui-port.md` | S7 (rank 17) | ADVANCE, first failing step none | full rooted D1; S1g; S6 |
| `pd-port.md` | S8; the RPM1 shortcut (rank 19's reversal) | ADVANCE, first failing step none; Section 5's counterexample correct | S7; O6; local C^1 continuity of separated moments |

This check moves the following (no other file edited here):

1. `t0-skeleton.md` S1c, S1g: "cited" becomes proved by Codex (`am1-port.md`) and checked line by line by Claude (this file). The result is stronger than SA AM1 (L2749) as stated: it covers β ≥ 0, not only β > 0.
2. S1d: all three cut types (coordinate site, coordinate bond, diagonal) are in `am1-port.md` Section 3. A second proof of the bond cut, by splitting each crossing bond, is in `ui-port.md` Section 2. S1e (the finite chessboard; `ui-port.md` Section 2) and S1f (the lower tangent and folding; `am1-port.md` Section 4) are rebuilt in d = 4 and checked here. The skeleton text "coordinate case written in upper-chain Lemma 1.1" can point to `am1-port.md` Section 3 instead.
3. S1h (Lemma S): checked by Codex in `am1-port.md` Section 1, and the steps are right. The skeleton's consequence "the limit is volume-first" overstates the lemma. The lemma rules out one torus adapted to both mirror families. It does not rule out every other construction. Suggested wording: "volume-first is the route chosen; Lemma S rules out the joint torus extraction".
4. S7: becomes "checked as an implication from D1 (rooted), S1g, S6", with c_I = 1/(40L), p = 0 and C_I = 2Q_0/r. Since S1g and S6 are now both checked (S6 in `gates/bridge-check.md`), the only open premise of S7 is D1.
5. S8: add "local C^1 continuity of separated moments (from S2/S3)" to its inputs, with state "checked as an implication". The exponent is ℘ = 5.
6. Skeleton Section 2, row 19, column "Reverses if: a plate density with ℘ < 4": `pd-port.md` Section 5 shows that UI and O6 cannot supply this. The generalized free field with Källén-Lehmann weight λ^3 (two-point function c|x|^{-10}) satisfies UI with p = 0 and O6. Its fixed-label point plates grow like a^{-4}, and its L^1-scaled plates like a^{-5}. A reversal would need an input beyond UI and O6. TU (with TU10, S16) and AC stay on the O(4) path.
7. O5 and O9 read S1g. Their lattice input is now checked.

**Stays open.** The premises of this chain:

- D1 (rank 10): open. S7, and hence S8, rest on it.
- S16 (TU10) and the rest of the rotation chain (S9-S11): not read here. `library/ak-port.md`, `tu-port.md`, `ac-port.md` go to row 207.
- E1 (the cutoff sequence), which the continuum statements read through S4 and S6.

## Result

Kind: a check of Codex's ports of proofs that Sussman and Alpoge give in detail: Y3 IV-14-20, IV-16-26, IV-16-31, IV-29-11 to IV-29-40, IV-54-9 to IV-54-17, IV-55-9, IV-55-19, IV-56-17; SA AM1 (L2749), UI1-UI10 (L28229-28521), PD1-PD18 (L28530-28860). It also checks our own new text: the polynomial replacement of Y3's character calculation (`am1-port.md` Section 6), the d = 4 constants of all three notes, and the counterexample in `pd-port.md` Section 5. Credit: Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, for every argument ported here.

`library/am1-port.md`, `library/ui-port.md` and `library/pd-port.md` were checked line by line by Claude. First failing step: none in any of the three. Each holds as an implication from its stated premises. Every d = 4 change was recounted by hand: 48β and (2r-1)^4 in the lower tangent, the diagonal transversal and its boundary bound 6/(iN) + 2/(ih), i^3 copies per height, the layer constants e^{-10β|S|} and e^{-12β|S|}, the boundary cost 72β(ℓ/a)^3, the rooted count with 8 directions and 16 corners, the scale sum B_0, the four-dimensional parametrix, and the exponent ℘ = p + 5. The defects are wording only: Section 5 of `am1-port.md` uses r without choosing it, Section 6 uses but does not state the gauge invariance of q_S (it follows in one line), and `pd-port.md` has an out-of-date D1 pointer. None breaks a statement.

Finished 2026-11-04T05:52Z.
