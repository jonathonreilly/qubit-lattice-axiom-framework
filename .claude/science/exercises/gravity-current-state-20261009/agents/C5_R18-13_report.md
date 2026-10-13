# C5 R18-13 report: the off-axis graviton rows at the SM root — how many more conditions, and can shape or placement pay them?

**Author.** Claude Opus 5.5 probe (same model family as the supervisor and every C5 worker). Unrefereed. 2026-10-13, 03:38Z to 04:10Z. No repository file was edited. No downloads, no web lookups.

**Paths.**
- `P/` = `.claude/science/exercises/gravity-current-state-20261009/`.
- `S/` = `.../scratchpad/C5/R18-13/`. My scripts and `.out` files are in `S/scripts/`. `S/arch9/`, `S/arch18/`, `S/arch17_4/`, `S/arch17_12/` hold unmodified copies of `P/scripts/C5/{R18-9,R18-5,R17-4,R17-12}/`.
- Every run used `OMP_NUM_THREADS=2` and ran under 10 minutes (longest 393 s, `photface_N224.out`). Machine load was 3.3–8.5; I ran at most three of my jobs at once.

**Read.**
- `docs/MINIMAL_AXIOMS_2026-06-29.md`, in full (`AX`).
- `P/TESTS.md`: C5 method and readings (`:2302-2319`); round-17 rules (`:5688-5706`); round-18 rules (`:6395-6406`); R13-8 and verdict (`:4747-4760`, `:4803-4808`); R17-4 (`:5816-5845`, worker `:5940-5952`, verdict `:6171-6178`); R17-10 (`:6208-6230`, worker `:6384-6390`, verdict `:6586-6589`); R17-12 (`:6339-6362`, worker `:6601-6611`, verdict `:6795-6801`); R18-5 (`:6631-6653`, worker `:6779-6789`, verdict `:6964-6969`); R18-9 (`:6847-6869`, worker `:7044-7057`); my item `:7061-7091`.
- `P/agents/`: `C5_R18-9_report.md` (all); `C5_R17-4_report.md` (§§0–3.5) and `C5_R17-4_referee_verdict.md`; `C5_R17-12_report.md` (§ Survivors and Lemma I, `:200-230`, plus grep hits `:30,279,297`) and `C5_R17-12_referee_verdict.md` (`vR17-12`); `C5_R18-5_report.md` (grep hits on the midpoint, pair block and P-R18-5b/c, `:54,111,235,250,305-309`) and `C5_R18-5_referee_verdict.md` (`vR18-5`).
- **R18-9's referee:** `scratchpad/C5/ref_R18-9/REFEREE_VERDICT.md` (`vR18-9`) appeared at 04:09Z: **CONFIRMED WITH CORRECTIONS.**
  - FOUR-ROW-ZERO holds only in the O(q) convention (`vR18-9:76-85`).
  - The stored N = 224 point has converged-quadrature residuals of about 1e-6. An independently retuned root is at (b_s, b_f, r, a) = (2.526103698, 0.909103708, 0.555604226, −0.176095005) (`vR18-9:26-40`).
  - The honest knob count is **5 continuous law knobs**: 4 equality tunings plus 1 photon-window selection (`vR18-9:52-63`).
  - The UD face2 ≠ T₂g mismatch is confirmed at m = 0.3 and 0.1 but was "not resolved at the target m = 0.01" (`vR18-9:65-74`). It is resolved here (§3.3).
  - I folded these in below. Off-axis rows at the retuned root differ from the stored root by ≤ 7e-9 per field (`scal_offaxis_refroot.out`, `dface_refroot_m0.01.out`). That moves the face totals by ≤ 2e-7 and (w_d, w_o) by about 1e-7, which is negligible.

**Runners rechecked before use (checked).**
- R17-4's archived off-axis evaluator (`arch17_4/offaxis.py`, via R18-9's `scal_offaxis.py`) on the N = 224 root's scalar edge returns R18-9's scalar axis rows exactly (T₂g −6.277560e-4, E_g −3.621603e-4; `scal_offaxis_N224.out`, cf. `arch9/solve4k_N224.out`).
- My Dirac pointwise off-axis evaluator `dface.py` reproduces R18-9's brute-force `udface.py` (`arch9/udface_offaxis.out`) at m = 0.3 (face2 − T₂g −6.72e-5 vs −6.72e-5; face1 +6.0655e-4 vs +6.0649e-4 at N = 160) and at m = 0.1 (face2 − T₂g +7.210e-5 vs +7.06/7.15/7.18e-5 at N = 128/160/192, converging toward mine) (`dface_validate_m0.3.out`, `dface_validate_m0.1.out`). At the m = 0.01 root it reproduces R18-9's Dirac axis rows to 6e-9 per field (`dface_root_m0.01.out`).
- My photon off-axis evaluator `vwface.py` equals R17-12's archived `r1712_lib.xi(…, 'VWa')` on the axis to all printed digits (diff 0.0 at N = 32, 48; `vw_validate.out`), and at N = 224 it returns R18-9's per-vector axis rows exactly (T₂g −3.511808940e-3, E_g −1.270615292e-4; `photface_N224.out`, cf. `arch9/solve4k_N224.out`).

**Labels.** proved (complete argument under stated hypotheses; unrefereed) / checked (numerics here) / suggested / reading / comparator.

---

## 0. In plain words

1. **There are exactly two more conditions, face1 and face2. The body row follows (count proved from above, checked from below).**
   - R17-4's refereed rank-4 result (`vR17-4`, `TESTS:6171-6178`; `C5_R17-4_report.md:17,111`) leaves, once the two axis rows are zero, only the two face-diagonal rows. The body row is then fixed: body = (8 face1 + 4 face2 − 3 E_g)/9. That holds for any cubic-covariant vertex extension. I checked it per species: Dirac to 1e-17, scalars to 2e-19, photons to a finite-q residual that falls with N.
   - Both rows are nonzero at R18-9's root under the stated extensions, and they can be moved independently (Lemma O below). So they are two independent new conditions, not one.
   - Per species they are written as d1 := face1 − (3E_g + T₂g)/4 and d2 := face2 − T₂g. At R18-9's root the axis totals are zero, so the totals of d1 and d2 equal the face totals.
2. **At R18-9's root the off-axis rows are far from zero, and the vectors dominate (checked).** The VW photon needs an off-axis extension. I stated one ("VWa-geo": every half-integer offset in every direction uses the same two-offset stencil a as the axis). Per field at m = 0.01:

   | species | d1 | d2 | ×count: face1 / face2 contribution |
   |---|---|---|---|
   | real scalar, U, E1 (×4) | −2.909e-5 | 6e-13 (≡ 0, R17-4) | −1.83e-3 / −2.51e-3 |
   | Dirac, UD, midpoint (×22.5) | +5.283e-4 | +1.387e-4 | +0.0253 / +0.0478 |
   | vector, VWa-geo, a = −0.176095 (×12), N = 256 | +0.2194 | +0.1128 | +2.621 / +1.312 |
   | **total** | | | **face1 +2.645, face2 +1.357** |

   Against axis-row contributions of order 0.04, these are huge: an O(1) cubic anisotropy of the graviton cone. They come almost entirely from the vector vertex, through its off-axis placement and its large-box edge (§3.5, §3.6).
3. **Two placement data on the vector vertex pay both rows. That gives an explicit joint root (checked; it rests on R18-9's refereed axial root, `vR18-9:26-40`), so ALL-ROWS-ZERO is met on the letter in the O(q)-conservation scope.**
   - The data are two "own-direction" placement stencils:
     - each diagonal stress component T_ii is smeared along its own axis i, with weight u_d(q_i);
     - each off-diagonal component T_ij is smeared along its own two axes, with weight u_o(q_i)·u_o(q_j);
     - each u(s) = (1 − w) + w cos s.
   - They leave the q = 0 vertex (the forward test), the axis rows and both shear rows untouched (proved). On the face rows they act triangularly (Lemma O, proved): face2 depends only on w_o, and the Jacobian determinant E0·T0/16 is positive.
   - Solved and re-evaluated directly:

     | photon N | w_d | w_o | totals after the solve (face1, face2) |
     |---|---|---|---|
     | 160 | −1.13958 | −0.19108 | −5.9e-6, −1.4e-6 |
     | 192 | −1.16378 | −0.19458 | −3.0e-6, −7.1e-7 |
     | 224 | −1.17155 | −0.19542 | −1.7e-6, −4.0e-7 |
     | 256 (solve only) | −1.1729 | −0.1955 | — |

     The knobs converge. The residual totals are the w-quadratic grid artefact, about 1e-6 against contributions of 2.6.
   - The same data solve the m = 0.001 root, at (−1.1639, −0.1947) for N = 192.
4. **The scope is the whole story (proved, Lemma S).**
   - The off-axis anisotropies d1 and d2 are invariant under every identically conserved (superpotential) improvement of the vertex.
   - So the payment above works only because the campaign's "conserved" means the O(q) forward test (`vR18-5:18-20`; `vR17-12:15`). Own-direction smearing is not identically conserved; its W1 defect is O(q³).
   - If an exact W1 completion is ever required, these two tunings are not available. The off-axis rows would then be shape rows, or need non-shape knobs. In the sampled families, shape alone does not reach them: every sampled photon edge has d1, d2 > 0 (§3.5).
   - The off-axis values themselves also depend on how the axial stencil is extended off the axis:
     - with a = 0 as base plus a superpotential stencil, the photon's d1 and d2 drop to about 0.14 and 0.011 per vector (§3.6);
     - the totals stay nonzero, so the count is still two;
     - this is R17-4's P-TTV₂ again.
5. **Bill (reading; per-datum basis).**
   - The SM gravity block (four TT speed rows plus two shear rows) costs 6 equality tunings plus R18-9's photon-window selection. That is **7 continuous law knobs** in `vR18-9:52-63`'s convention:
     - 4 axial tunings from R18-9: b_s, b_f, r, a;
     - 2 off-axis placement data: w_d, w_o.
   - Still unpaid: the LV tadpole (P-Tad, or P-vac′ under (d-i)), the CC, and exact W1.
   - This matches the expectation's "~6 tunings", counting equality tunings. The difference is that a joint root was found, so the reading is ALL-ROWS-ZERO rather than OFF-AXIS-COUNTED.
   - The payment needs signed stencils: nonnegative own-direction stencils can only raise both rows, and both totals are positive (Corollary N).

---

## 1. Class, hypotheses, stipulations, exclusions (stated before any title)

**Setting (`TESTS:7074-7078`).**
- **Content.** R18-9's root at m = 0.01 (`arch9/root4k_N224.npy`; `C5_R18-9_report.md:212-231`):
  - 4 real scalars on G_w(2.5261508, w = 0.615442), U vertex;
  - 22.5 Dirac fields on D1(0.9091030, 0.5556037), UD vertex;
  - 12 vectors on γG_w(2.9435, 0.198093), VWa vertex with a = −0.1760950.
  - Second mass: R18-9's m = 0.001 root (`arch9/root4c_m001_N192.npy`).
- **Directions and rows.** Off-axis directions: face (110) and body (111). One loop. The four TT speed parameters are {E_g, T₂g, face1, face2} (R17-4's rank-4 basis), plus body as a check.
- **Normalizations.** Each evaluator keeps its own uniform normalization, as R18-9 did:
  - photon and scalar: e:e = 2 with a ½ in the amplitude;
  - Dirac: e:e = ½ (`dface.py` docstring).
  - The identities below are invariant under a uniform rescaling of e. The cross-species totals inherit R18-9's convention, which I checked by reproducing its per-species axis rows.
- **Excluded (`TESTS:7078`):** pairing; superluminal edges; the M vertex; V0.

**Hypotheses carried, not derived.**
- **W1 at O(q) only** (the forward test, Lemma F). No vertex here has an exact W1 completion (`vR18-5:20`; `vR17-12:15`).
- **The 𝔇 restriction behind UD** (P-R18-5b) and **UD's midpoint prescription** extended to every q direction (P-R18-5c; R18-9's `udface.py` convention).
- **SF** for the shear rows, used only through R18-9's root.
- **Signed stencils** are in setting (`vR18-5:16`).
- **R18-9's root itself.** Refereed CONFIRMED WITH CORRECTIONS (`vR18-9`), in the O(q) convention only.

**Off-axis extensions (stated before results; `vwface.py`, `dface.py` docstrings).**
- **VWa-geo (vectors).**
  - The base is R17-12's index-placed stress T_ij = c_ic_j[E_iE_j + B_iB_j − δ_ij(E² + B²)/2] in the rotated frame.
  - Each bilinear keeps the half-integer offsets of its two averaged fields. E_a sits at â/2. B_a sits at the two other half-axes. Averaging along an index moves a field to the site along that index only.
  - Every half-integer offset along axis l gets the axial stencil P(s_l) = (1 − a)cos(s_l/2) + a cos(3s_l/2). Integer offsets get no stencil.
  - Explicitly:
    - for i ≠ j: E_i(1)E_j(2) gets c₁ᵢc₂ⱼ, and B_i(1)B_j(2) gets c₁ⱼc₂ᵢP(s_k);
    - for i = j: E_i² gets +½c₁ᵢc₂ᵢ, and E_a² (a ≠ i) gets −½c₁ᵢc₂ᵢP(s_a);
    - B_i² gets +½c₁ᵢc₂ᵢP(s_j)P(s_k), and B_a² (a ≠ i) gets −½c₁ᵢc₂ᵢP(s_third(a,i)).
  - On q ∥ z this is R17-12's VWa term by term (checked, `vw_validate.out`).
  - **Torus continuity (proved by inspection).** Under a leg's wrap k_l → k_l − 2π:
    - the rotated-frame amplitude must transform as N → N·D with D = diag(−1 at l), which needs ME column l to flip and MB columns ≠ l to flip;
    - every term either carries P(s_l), which is antiperiodic, with the right sign, or carries a factor c(k_l) that vanishes at |k_l| = π (d′(π) = 0 for fw = 1).
    - So W is continuous across every wrap. I checked this term by term for the x-wrap; y and z follow by symmetry.
- **Own-direction placement data (new law data; the declared knobs).**
  - T_ii is multiplied by u_d(s_i), and T_ij (i ≠ j) by u_o(s_i)u_o(s_j), with u(s) = (1 − w) + w cos s.
  - These are finite-range (±1), symmetric and cubic-covariant, with u(0) = 1.
- **UD (Dirac).**
  - R18-5's UD vertex T_ij = ½(p_j∂_ih + p_i∂_jh) is evaluated at the pair midpoint k for pair (k − q/2, k + q/2), for any direction n.
  - The pointwise α formula of R18-5's `xiud.py` is a 1D Taylor expansion along q. I generalized it by replacing ∂_z with D = n·∇:
    - c = (S_x, S_y, S_z, M);
    - Dc = (n_xS′_x, n_yS′_y, n_zS′_z, Σn_lW′_l);
    - D²c = (n_x²S″_x, …, Σn_l²W″_l).
  - Quadrature: R16-13's composite Gauss–Legendre, which resolves m = 0.01.
- **Scalars.** U with R17-4's E1 extension (relative momentum only), evaluated by R17-4's archived evaluator.

**Round-18 head rules.**
- **v_max:** edges unchanged from R18-9 (`C5_R18-9_report.md:249-252`).
  - Dirac r < 1/√3, so v_max ≤ 1 (Lemma V1).
  - Photon: d′ ∈ [0, 1].
  - Scalar: 0.999997.
  - Graviton symbol: not touched.
- **Locality (`TESTS:6403`).**
  - VWa-geo keeps VW's face zero through c = d′(π) = 0, which multiplies every term at the face.
  - u_d and u_o do not remove that zero.
  - UD is spinor-covariant (Lemma M′, `vR18-5:5`).
- **Counterterm basis:** per datum (one stencil weight per symmetry type of one vertex family).
- **Certificates:** no CONFLICT is claimed.
- **Removed hypothesis:** axial q only.

## 2. Prior art (each counted once)

- **R17-4 + vR17-4.**
  - The off-axis formula; the rank-4 TT basis; the O_h relation (`C5_R17-4_report.md:17,111`).
  - The U identities face2 ≡ T₂g and face1 = (3E_g + T₂g)/4 − ⟨K₆/ε⁷⟩/128 (`:19-20,134-135`).
  - Off-axis values depend on the extension, E1 vs E2 (`:27`; P-TTV₂).
- **R13-8 + verdict.** TT ranks (2, 0, 4) with P and T (`TESTS:4805`).
- **R17-10 + verdict.** Theorem F concerns K₆ for one scalar edge, on the fast slice only (`TESTS:6586-6589`). Not used here: at the SM root the scalar K₆ term is −2.9e-5 per scalar and is paid together with everything else.
- **R17-12 + vR17-12.**
  - VW; Lemma I. Normalized symmetric stencils are W1-invisible on the axis through identically conserved superpotentials, "conditional on one exact completion existing" (`vR17-12:15`). VW is defined for q ∥ z only.
- **R18-5 + vR18-5.**
  - UD is unique only within 𝔇 (`vR18-5:7`).
  - Signed stencils are in setting; "conserved" means the O(q) forward convention (`vR18-5:16-20`).
- **R18-9 + vR18-9.**
  - The four-row root.
  - face2 ≢ T₂g for UD at m = 0.1–0.3 (`C5_R18-9_report.md:284-292`).
  - VW off-axis not computed (`:293`).
  - P-R18-9b (`:311-313`).
- **Grep.** I searched `P/agents/*.md` and `TESTS.md` for "own-direction", "superpotential", "off-axis" with "VW", "Lemma S", and "face1" with "photon". The only hits are R17-12's axial Lemma I and the R17-4/R18-9 items above. There is no prior off-axis photon value and no prior statement that off-axis anisotropies are invariant under improvements.

---

## 3. Results

### 3.1 Structure (proved)

Notation: q = s·n with n a unit vector, and Ξ(n, e) = ∂_{s²}Π_e(0, sn) + ∂_{ω²}Π_e(ω, 0), where Π_e = −⟨Σ_pol|Σ_ij e_ijV_ij|²/E⟩ + seagull. V_ij is the pair amplitude of the stress component T_ij, symmetrized as V_ij + V_ji for i ≠ j. Write E0 := −Π_{Eg}(q = 0) = ⟨W_Eg/E⟩ and T0 := −Π_{T2g}(q = 0) = ⟨W_T2g/E⟩. These are the q = 0 TT pair weights, each > 0 unless that amplitude vanishes almost everywhere.

**Lemma C (count).** Assume the vertex extension is cubic-covariant (proper rotations, `AX:37-41,57-58`). Then:
- the degree-2 TT rows span at most the four numbers {E_g, T₂g, face1, face2} (R17-4, refereed);
- body = (8 face1 + 4 face2 − 3E_g)/9;
- once E_g = T₂g = 0 (totals), the only further conditions are face1 = 0 and face2 = 0, equivalently d1_tot = d2_tot = 0.

So there are at most two extra conditions, in total and per species. ∎ (R17-4's basis result. The axioms supply only proper rotations, O. For the even-rank coefficient tensor of Π's O(q²) TT part, O-invariants and O_h-invariants coincide, because inversion acts trivially. So R17-4's O_h computation applies.)
- Checked per species: `dface_root_m0.01.out` gives a relation residual of 1.6e-17 per Dirac field; `scal_offaxis_N224.out` gives 2e-19 per scalar.
- For the photon the residual is a finite-q effect: −4.4e-4, −3.8e-4, −1.0e-4, −4.2e-5 at N = 48, 64, 96, 128 (`vwface_root_lowN.out`), and −6.0e-6, −3.8e-6, −2.4e-6 at N = 160, 192, 224 at the solved setting (`photface_N*.out`).

**Lemma O (own-direction placement).** Multiply T_ii by u_d(q_i) and T_ij (i ≠ j) by u_o(q_i)u_o(q_j), with u(s) = 1 − (w/2)s² + O(s⁴). Then for any species:
- (i) The q = 0 vertex is unchanged. So the forward (Lemma F) values, ∂_{ω²}Π, and every q = 0 quantity (μ_E, μ_T2, tadpole) are unchanged.
- (ii) The shift is exactly linear in (w_d, w_o): δΞ(n, e) = Σ e_ije_kl Re G_{ij,kl}(Λ_ij + Λ_kl).
  - Here G = ⟨VV*/E⟩ at q = 0, Λ_ii = (w_d/2)n_i², and Λ_ij = (w_o/2)(n_i² + n_j²).
  - Only the s² coefficient of u enters Ξ.
- (iii) On an axis, the TT components (xx, yy, xy) have Λ = 0, so δΞ_Eg = δΞ_T2g = 0.
- (iv) On the face (110):
  - δΞ_face2 = (w_o/2)·T0;
  - δΞ_face1 = (w_d/8)·E0 + (w_o/4)·T0.
- (v) The Jacobian of (face1, face2) in (w_d, w_o) is triangular with determinant E0·T0/16 > 0.

*Proof of (iv).*
- face2 = (ab + ba) with a = (x̂ − ŷ)/√2, b = ẑ, has only xz and yz components, each with Λ = w_o/4. So its amplitude acquires the factor 1 − (w_o/4)s² on every term. That gives δΠ = +(w_o/2)s²⟨W_face2/E⟩.
- By Schur at q = 0, Π_face2(0) = Π_T2g(0) (checked to 4e-16, `schur_check.out`).
- face1's amplitude is ½V_xx + ½V_yy − V_zz − ½V^S_xy, with Λ = (w_d/4, w_d/4, 0, w_o/2). Cubic symmetry removes the cross terms ⟨V_ii V^S_xy⟩. It leaves ⟨Re amp*(V_xx + V_yy)⟩ = A − B = E0/2 and ⟨Re amp*V^S_xy⟩ = −T0/2. ∎
- **Checked (photon, `pi0_check.out` vs `vwface_root_lowN.out`, N = 128).**

  | derivative | predicted | measured |
  |---|---|---|
  | d face2/d w_o | 0.578510 | 0.578450 |
  | d face1/d w_o | 0.289255 | 0.289186 |
  | d face1/d w_d | 0.139706 | 0.139659 |
  | axis-row derivatives | 0 | 0 exactly |

  The agreement is 1e-4 relative, which is the finite-q extrapolation error.

**Corollary N (signed stencils are needed for this route).**
- A nonnegative normalized symmetric integer stencil Σp_n cos(ns) has w = Σp_nn² ≥ 0.
- So with nonnegative own-direction stencils on any species, δface1 ≥ 0 and δface2 ≥ 0.
- Both totals are positive at R18-9's root (§3.3), so nonnegative own-direction data cannot zero them. ∎ This is scoped to the own-direction family. Other placement data, such as per-term half-integer weights, are not covered.

**Lemma S (improvements cannot move d1, d2).**
- Let δT_ij(q) = ε_ikm ε_jln q_kq_l Z_mn be an identically conserved (superpotential) improvement, where Z is any local, cubic-covariant, symmetric-tensor-valued pair amplitude at q = 0.
- Then for every unit n and every TT e ⊥ n: δΞ(n, e) = 2(b_E|P_E e|² + b_T|P_T e|²).
  - This is independent of n, with constants b_E and b_T.
  - Hence δface1 = (3δE_g + δT₂g)/4 and δface2 = δT₂g.
  - So δd1 = δd2 = 0.

*Proof.*
- Write A_im = ε_ikm q_k, the matrix of v ↦ q × v. Then e:δT = (AᵀeA):Z.
- For q = s n, A acts on the transverse plane as s times a 90° rotation and kills n.
- A helicity-±2 tensor rotated by 90° changes sign. So AᵀeA = −s²e, and e:δT = −s² e:Z.
- The O(s²) cross term in Π is therefore 2s²⟨Re(e:V)*(e:Z)/E⟩. This is an O-invariant bilinear form on Sym²(ℝ³) = A₁ ⊕ E ⊕ T₂, which is multiplicity-free with absolutely irreducible real irreps. By Schur it equals Σ_ρ b_ρ|P_ρe|².
- For face1, |P_E e|² = 3/2 and |P_T e|² = ½. For face2, |P_T e|² = 2. ∎
- **Temporal superpotentials.** Terms with time derivatives, such as δT_ij ∝ ω²Z_ij, shift ∂_{ω²}Π by the same kind of n-independent Schur form. Mixed ωq terms do not enter Ξ at this order. So the conclusion is unchanged (proved by the same argument).
- **Scope.** Leading order in q. Z is local, q-independent and cubic-covariant. On the lattice the q's become sin-type symbols, which is the same at O(q²). Improvements whose Z depends on q, or that vanish only on-shell, are not covered.
- **Consequence.** Every identically conserved improvement shifts the four TT rows only along the 2-dimensional subspace (β_E, β_T, ¾β_E + ¼β_T, β_T). That includes R17-12's Lemma I stencil freedom on the axis, once it is extended off the axis as a superpotential with q = 0 local Z. The off-axis anisotropies are fixed by the base vertex and the edge shapes. Paying them by placement needs placement data that are not identically conserved, such as the own-direction smearings. Those violate W1 at O(q³), which is allowed only under the registered O(q) convention.

### 3.2 (a) The extensions keep covariance and the forward test (checked)

- **Forward test.** At q = 0 every P(s_l) = 1 and u = 1. So VWa-geo with any (w_d, w_o) has R17-12's VW vertex at q = 0. VW passes Lemma F to 1.7e-16 (`vR18-5:3`). UD's midpoint G(k) is q-independent. Both are therefore unchanged (proved by inspection).
- **Off-axis covariance control** (`vw_cov_face_N64.out`). The face rows and both own-direction derivatives along (1,1,0), (0,1,1), (1,0,1) and (1,−1,0), with the polarizations rotated to match, agree to all 11 printed digits. These cubic images test the x, y and z wrap conventions, and the negative-shift wrap, of VWa-geo.
- **Covariance.** The C₄ control holds: xz with q ∥ ŷ equals T₂g with q ∥ ẑ.
  - photon: 1.6e-14, 7e-18, 0, 1.2e-13 at N = 48–128;
  - Dirac: ≤ 4e-19.
  - The O_h relation also holds (§3.1).
- **Axis reproduction.** VWa-geo equals R17-12's VWa exactly on the axis (`vw_validate.out`) and R18-9's per-vector rows at N = 224 (`photface_N224.out`).

### 3.3 (b) Off-axis rows at R18-9's root, per species and total (checked)

**Scalars** (`scal_offaxis_N224.out`, per real scalar):
- E_g −3.621603e-4, T₂g −6.277560e-4;
- face1 −4.576501e-4, face2 −6.277560e-4, body −5.650827e-4;
- d2 = 6.4e-13, so face2 ≡ T₂g holds;
- d1 = −⟨K₆/ε⁷⟩/128 = −2.909e-5.

**Dirac UD** (`dface_root_m0.01.out`, per field). GL(4,10)/(5,12)/(6,16) agree to ≤ 5e-9:
- E_g +1.321432e-4, T₂g +1.984560e-3;
- face1 +1.123535e-3, face2 +2.123236e-3, body +1.898311e-3;
- **d1 = +5.2829e-4, d2 = +1.3868e-4.**
- R18-9 saw d2 change sign between m = 0.3 (−) and m = 0.1 (+) (`C5_R18-9_report.md:288-289`). At m = 0.01, d2 stays positive and is about twice its m = 0.1 size (+7.2e-5, `dface_validate_m0.1.out`; slightly different law).

**Vectors VWa-geo, a = −0.1760950** (`vwface_root_lowN.out`, `photface_N{160,192,224}.out`, `photface_q_N256.out`, shifts (1,2)):

| N | face1 | face2 | (with T₂g, E_g at N = 224) d1 | d2 |
|---|---|---|---|---|
| 128 | +0.207057 | +0.103155 | | |
| 160 | +0.212488 | +0.106765 | | |
| 192 | +0.216907 | +0.108802 | | |
| 224 | +0.218247 | +0.109292 | +0.21922 | +0.11280 |
| 256 | +0.218454 | +0.109346 | +0.21943 | +0.11286 |

- **Convergence.** The successive N steps shrink: face1 changes by +5.4e-3, +4.4e-3, +1.3e-3 and +2.1e-4. The extrapolated value is +0.2185 ± 2e-4.
- **q-extrapolation** (`photface_q_N128.out`). Pairs (1,3) and (2,4) at N = 128 imply an O(q⁴) remainder of about −1.7e-3 at (1,2). It scales as N⁻⁴, so it is about 1e-4 at N = 256 (checked estimate).

**Totals at the root** (N = 224 photons; `photface_N224.out`):
- face1 = −0.00183 (scalars) + 0.02528 (Dirac) + 2.61897 (vectors) = **+2.6424**;
- face2 = −0.00251 + 0.04777 + 1.31150 = **+1.3568**;
- body total = (8 face1 + 4 face2)/9 = **+2.952** (by the relation, since the axis totals are zero).

### 3.4 (c) Count and solve (checked)

- **Count: two.** Lemma C gives at most two. Both totals are nonzero, and by Lemma O(v) the two rows are independently movable (a submersion), so they are independent conditions.
- **Per species:**
  - scalars on U carry one condition (d1) and zero d2 identically;
  - Dirac and vectors carry both.
- **Solve.** With the axis totals zero at R18-9's root and Lemma O(iii) protecting them, solving face1_tot = face2_tot = 0 for (w_d, w_o) of the 12 vectors is a 2 × 2 triangular linear problem (`photface_hi.py`):

| N | J = 12·∂(face1, face2)/∂(w_d, w_o) | det | (w_d, w_o) | direct re-evaluation: face1 / face2 / body totals |
|---|---|---|---|---|
| 160 | [[1.67618, 3.47075], [0, 6.94196]] | 11.636 | (−1.139576, −0.191076) | −5.9e-6 / −1.4e-6 / −6.5e-5 |
| 192 | [[1.67636, 3.47117], [0, 6.94259]] | 11.638 | (−1.163779, −0.194580) | −3.0e-6 / −7.1e-7 / −4.4e-5 |
| 224 | [[1.67645, 3.47136], [0, 6.94286]] | 11.639 | (−1.171554, −0.195418) | −1.7e-6 / −4.0e-7 / −3.1e-5 |
| 256 | N = 224 Jacobian (its N-dependence is 1e-4) | | (−1.172837, −0.195514) (solve from `photface_q_N256.out`) | — |

- The body residual equals 12 × the photon's finite-q O_h residual: −6.0e-6, −3.8e-6, −2.4e-6 per vector. It vanishes as q → 0 by Lemma C.
- At N = 224 the axis totals are −1.3e-7 and −1.6e-7. That is my Dirac quadrature against R18-9's: 6e-9 per field × 22.5.
- **Knob convergence:** w_o steps are −3.5e-3, −8.4e-4, −1.4e-4; w_d steps are −2.4e-2, −7.8e-3, −1.4e-3. These are geometric.
- **Sizes.** In λ units (u = 1 − λs²/2), λ_d ≈ −1.17 and λ_o ≈ −0.196.
  - As a ±1 stencil, u_d has weights 2.17 at 0 and −0.59 at ±1.
  - Equivalently, a ±2 stencil with a quarter of the weight gives the same λ.
- **Relation to R17-12's Lemma I** (`C5_R17-12_report.md:208-216`). Lemma I's axial superpotential Y^{xzyz} has a finite, local q → 0 limit. Its covariant completion is therefore of Lemma S's type. So R17-12's axial stencil freedom, extended covariantly as a superpotential, cannot pay face1 or face2 (proved under Lemma S's hypotheses).
- **m = 0.001** (`photface_m001_N192.out`; R18-9's separately tuned m = 0.001 root; Dirac `dface_root_m0.001.out`, scalars `scal_offaxis_m0.001.out`):
  - totals before the solve: face1 +2.6270, face2 +1.3518;
  - solved (w_d, w_o) = (−1.16391, −0.19470) at N = 192, against (−1.16378, −0.19458) at m = 0.01, N = 192.
  - Direct re-evaluation at the solved data (N = 192, `photface_m001_N192.out`) gives totals face1 −3.0e-6, face2 −7.1e-7 and body −4.8e-5. The body value is the finite-q O_h residual. The axis totals at this N are −9.4e-8 and +9.9e-8.
- **Knob count.**
  - Axial: 4 equality tunings (R18-9) plus the photon-window selection, i.e. 5 knobs (`vR18-9:52-63`).
  - Off-axis: 2 tunings, the vector own-direction weights.
  - Total: **6 equality tunings + 1 window selection = 7 continuous law knobs** for the SM gravity block.
  - Unused alternatives that could pay the same two rows:
    - UD's own-direction placement. Lemma O applies with the Dirac q = 0 weights ⟨t0/E⟩: T₂g 0.17295 and E_g 0.22525 per field (`dpi0.out`). In totals units it moves face2 by 1.95 per unit w_o, against 6.94 for the vectors, and face1 by 0.63 per unit w_d, against 1.68. So it needs a λ about 2.6–3.6× larger.
    - The scalars' own placement.
    - The Dirac pair block (P-R18-5b). It would also move the axis rows. Not tried.

### 3.5 Shape alone (sampled; suggested)

**Photon d1 and d2 across edges** at the root's a = −0.176095, VWa-geo, N = 96 (`photd_shape_N96.out`), per vector:

| edge | d1 | d2 |
|---|---|---|
| R18-5's γG_w(1.271, 0.260) | +0.101 | +0.013 |
| γG_w(2.0, fw 1) | +0.051 | +0.005 |
| γG_w(2.6, fw 1) | +0.093 | +0.027 |
| root edge γG_w(2.9435, fw 1) | +0.214 | +0.108 |
| γG_w(3.0, fw 0.5) | +0.282 | +0.142 |

- Every sampled edge has d1, d2 > 0. The scalars' d1 is −3e-5 per field and the Dirac's is +5e-4.
- So with these families and this a, no sampled shape change brings Σd1 or Σd2 near zero. The large-box photons that R18-9's window requires (b_γ ≈ 2.94) have the largest anisotropies.
- Within VWa-geo, d1 = 0 at the root edge would need a ≈ +0.32 (§3.6, linear in a), which conflicts with the axial a = −0.176.
- **Reading (suggested, sampled, not an enclosure).** In the stated families the off-axis rows are not shape-payable alongside the four axial rows. They need placement data (the route here) or non-shape knobs.

### 3.6 Extension dependence of the off-axis values (checked; this is why the count, not the value, is the robust result)

- **Within VWa-geo, the photon's d1 and d2 depend on the axial stencil a** (`photd_a_N96.out`, N = 96, per vector):

  | a | d1 | d2 |
  |---|---|---|
  | 0 | +0.1383 | +0.0062 |
  | −0.176095 | +0.2140 | +0.1082 |
  | −0.5 | +0.3531 | +0.2958 |

  By Lemma S an identically conserved extension of the stencil could not do this. So VWa-geo extends R17-12's axial superpotential freedom (Lemma I) off the axis by placement that is not identically conserved.
- **The superpotential-compatible alternative.** Take VW0-geo (a = 0) as the base and extend the axial stencil change as an identically conserved superpotential. Lemma S then makes the photon's d1 and d2 equal their a = 0 values whatever a is (proved under Lemma S's hypotheses; I did not construct the explicit Z of R17-12's axial superpotential) (`photd_a0_N{160,224}.out`). The a = 0 values are:

  | N | d1(0) | d2(0) |
  |---|---|---|
  | 96 | +0.1383 | +0.0062 |
  | 160 | +0.13792 | +0.00840 |
  | 224 | +0.14367 | +0.01092 |

  These are **not converged** (single-setting runs; d2(0) is small and still rising). Treat them as about ±5% (d1) and ±30% (d2) (checked sequence, suggested error).
- **Under that alternative**, the root's off-axis totals are Σd1 = 12·d1(0) + 0.01177 ≈ +1.74 and Σd2 = 12·d2(0) + 0.00312 ≈ +0.134 (N = 224). Here 0.01177 and 0.00312 are the scalar-plus-Dirac d totals. They are still nonzero and still photon-dominated, so the count stays two. The own-direction payment works the same way (Lemma O is base-independent), with different data: w_o ≈ −0.134/6.943 ≈ −0.019 and w_d ≈ −(1.74 − 3.471·0.019)/1.676 ≈ −1.00 (suggested, from the N = 224 Jacobian; not re-evaluated directly).
- **Reading.** "Which off-axis extension is the photon's" is a law datum (R17-4's P-TTV₂, now for vectors). The count of two and the existence of a two-datum payment are extension-independent in the O(q) scope. The numbers are not.

### 3.7 (d) Prices and the bill (named, not adopted)

- **Used, not new:** P-R17-12b with signed weights (the axial a); P-R18-5b (𝔇); P-R18-5c (midpoint, extended to all q); SF; P-R17-13a; P-R18-9a (photon window).
- **P-R18-13a (new): own-direction stress placement.**
  - The vector stress components carry own-axis smearings u_d and u_o, with signed weights (λ_d ≈ −1.17, λ_o ≈ −0.196).
  - These are two law data fixed to the precision of the cone rows.
  - They conserve only at O(q): they are not superpotentials (Lemma S).
  - Gates: source/action `AX:187`; dynamics downstream `AX:114-130`; qualification `AX:85-90`.
- **P-R18-13b (new): the off-axis extension of the vector vertex** (VWa-geo, i.e. the axial weight reused in every half-integer direction). It is a P-TTV₂-type datum. Its alternative (§3.6) gives different off-axis values.
- **P-R18-13c (conditional): exact W1.** If an exactly conserved stress is required, Lemma S removes the placement route. The two off-axis rows then need shape data (not sufficient in the sampled families, §3.5) or non-shape knobs, and the gravity-block count stays at least 6 but with different payers.
- **Bill (reading, per-datum basis; on R18-9's root, refereed with corrections in the O(q) convention).**

  | row | payer |
  |---|---|
  | E_g, T₂g, μ_E, μ_T2 | b_s, b_f, r, a (R18-9) plus the photon window |
  | face1, face2 | w_d, w_o (here) |
  | body | follows (Lemma C) |

  - That is **6 equality tunings + 1 window selection (7 continuous law knobs) for the SM gravity block.**
  - Unpaid: LV tadpole (P-Tad, or P-vac′ under (d-i)); CC; exact W1; the charge block (outside this item).
- **No axiom text changes.**

---

## 4. Against the FIXED readings (`TESTS:7087-7090`)

**ALL-ROWS-ZERO: worker reading MET on the letter, in the registered O(q)-conservation scope (checked), with the knob count.**

| clause | status |
|---|---|
| explicit SM-count law | R18-9's root content (4 + 22.5 + 12), plus (w_d, w_o) = (−1.1716, −0.1954) at N = 224 (−1.1729, −0.1955 at N = 256) on the VWa-geo vectors |
| conserved | O(q) forward test (Lemma F) unchanged, since the q = 0 vertex is unchanged. **Not exactly conserved:** own-direction data violate W1 at O(q³), and no vertex here has an exact completion (`vR18-5:20`) |
| covariant, local | cubic-covariant by construction (C₄ control, O_h relation); finite-range symmetric stencils; VW face zero kept |
| all subluminal | edges unchanged from R18-9 (Dirac r < 1/√3; photon d′ ∈ [0, 1]; scalar 0.999997) |
| axial rows zero | R18-9's four rows (refereed in the O(q) convention, `vR18-9:76-85`; retuned root `vR18-9:33-36`). Untouched by the new data (Lemma O(i),(iii)); re-evaluated at N = 224: −1.3e-7, −1.6e-7 (Dirac-quadrature difference) |
| off-axis rows zero | face1 and face2 totals −1.7e-6 and −4.0e-7 (N = 224, direct); body −3.1e-5, which equals the finite-q O_h residual and falls with N |
| common light mass | m = 0.01; also m = 0.001 with separately tuned knobs (R18-9's root, as there) |
| knob count | **7 continuous law knobs: 6 equality tunings (b_s, b_f, r, a, w_d, w_o) + 1 window selection (b_γ)** |

**OFF-AXIS-COUNTED** is superseded on the letter, because a joint root is found. Its first clause holds: the count is established, two conditions (Lemma C upper bound proved; independence checked via Lemma O).

**If "conserved" is read as exact (identically conserved) W1:** the payment route used here is excluded by Lemma S. The record would then be OFF-AXIS-COUNTED: two conditions, payable only by shape or non-shape data, with no joint root shown. Without the own-direction data, independence of the two rows still holds by shape: across the five sampled photon edges the ratio d1/d2 runs from 3 to 16, so d1 and d2 move non-proportionally (checked, sampled; `photd_shape_N96.out`).

**Expectation (`TESTS:7091`).**
- "OFF-AXIS-COUNTED with two extra conditions (face1 and face2), payable by off-axis stencil data; ~6 tunings": the count, the payers and the bill match.
- The reading is stronger, because a joint root was found.
- The off-axis rows are photon-dominated and O(1): about 0.22 and 0.11 per vector. They are not small Dirac residues like R18-9's 22.5 × 7e-5 estimate (`C5_R18-9_report.md:296`).

**Removed hypothesis (axial q only):** removed. Off-axis directions add exactly two rows.

## 5. Strong-word check

- **"Proved"** is used for:
  - Lemma C, which is R17-4's refereed basis applied to totals;
  - Lemma O;
  - Corollary N;
  - Lemma S;
  - the torus continuity of VWa-geo;
  - the forward-test invariance.

  Each is a short argument from stated definitions under stated hypotheses: cubic covariance, local q = 0 Z for Lemma S, and leading order in q.
- **"Checked"** means numerics here at the stated resolutions.
- **"Converged"** means successive-N steps falling geometrically. The photon off-axis rows are uncertain at about 2e-4 per vector (0.1%), and the knobs to about 2e-3 in w_d and 1e-4 in w_o.
- **"Exactly two"** covers: an upper bound (proved); nonzero values at this root under the stated extensions (checked); independence (Lemma O). It does not say the rows are nonzero under every possible extension (§3.6).
- **"Huge" / "O(1)"** means 2.64 and 1.36 in Ξ totals, against 0.04 axial contributions. I quote no a = ℓ_P sizes.
- **Not claimed:**
  - exact W1;
  - SF derived;
  - uniqueness of the extension;
  - shape-only payment excluded (only sampled, §3.5);
  - one law serving both masses;
  - anything about R18-9's root beyond its referee's O(q)-convention scope;
  - anything at two loops.

## 6. For the referee

1. **Lemma S.** Check the helicity-2 sign AᵀeA = −s²e and the Schur step. It is the reason the payment is scope-dependent.
2. **Lemma O(iv)** and the photon check (`pi0_check.out`).
3. **VWa-geo's term placement** and the torus-continuity argument. The large photon off-axis values should be checked with an independent off-axis photon evaluator at N ≥ 224, including the q-extrapolation.
4. **The Dirac pointwise generalization** (`dface.py`), validated against R18-9's brute grid at m = 0.3 and 0.1.
5. **Whether VWa-geo or the superpotential-compatible extension** (§3.6) should be the registered off-axis vector vertex. The count is the same; the numbers differ.

## 7. Files (`S/scripts/`)

- **Evaluators:**
  - `dface.py` (UD Dirac, any direction, GL quadrature);
  - `vwface.py` (VWa-geo photon plus own-direction data, any lattice direction).
- **Validation:**
  - `dface_validate_m0.3.out`, `dface_validate_m0.1.out`;
  - `vw_validate.{py,out}`;
  - `vw_cov_face.{py}` → `vw_cov_face_N64.out`;
  - `photd_shape.py` → `photd_shape_N96.out`;
  - `pi0_check.{py,out}`;
  - `schur_check.{py,out}`.
- **Root rows:**
  - `scal_offaxis_N224.out`, `scal_offaxis_m0.001.out`, `scal_offaxis_refroot.out` (R18-9's `scal_offaxis.py`, unmodified, in `S/arch9/`; `root_refR18-9.npy` holds vR18-9's retuned root);
  - `dface_refroot_m0.01.out`;
  - `dface_root_m0.01.out`, `dface_root_m0.001.out`;
  - `dpi0.{py,out}`.
- **Photon rows and solves:**
  - `vwface_root_lowN.out` (N = 48–128);
  - `photface_hi.py` → `photface_N160.out`, `photface_N192.out`, `photface_N224.out`;
  - `photface_hi_m001.py` → `photface_m001_N192.out`;
  - `photface_q.py` → `photface_q_N128.out`, `photface_q_N256.out`.
- **Extension dependence:** `photd_a.py` → `photd_a_N96.out`, `photd_a0_N160.out`, `photd_a0_N224.out`.
