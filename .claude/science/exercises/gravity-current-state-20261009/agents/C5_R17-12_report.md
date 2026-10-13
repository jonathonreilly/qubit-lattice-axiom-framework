# C5 R17-12 report: which vector-vertex placement does consistency force, VU or VM?

**Author.** Claude Opus 5.5 probe (same model family as the supervisor and every C5 worker). Unrefereed. 2026-10-13, 01:37Z to 02:16Z. No repository file was edited. No downloads, no web lookups.

**Paths.** `P/` = `.claude/science/exercises/gravity-current-state-20261009/`. `S/` = `.../scratchpad/C5/R17-12/`. Scripts and `.out` files are in `S/scripts/`. Every run used `OMP_NUM_THREADS=2`; the longest single run took 7 min (`smsolve_VWa_N48.out`, 412 s). Machine load was about 5–6 from other jobs.

**Read.**
- `docs/MINIMAL_AXIOMS_2026-06-29.md`, in full (`AX`).
- `P/TESTS.md`: C5 method and readings (`:2302-2319`); R9-9 entry and verdict (`:3862-3872`, `:3939-3950`); R13-5 entry and verdict (`:4668-4678`, `:4707-4714`); R16-13 entry, worker line and verdict (`:5595-5613`, `:6088-6104`, `:6146-6156`); R17-4 entry and verdict (`:5816-5845`, `:5940-5952`, `:6171-6178`); R17-9 entry and worker line (`:6110-6128`, `:6267-6279`); my item (`:6339-6363`).
- `P/agents/C5_R17-9_report.md` (all, `R179`), and its referee verdict, which appeared while I ran (`scratchpad/C5/ref_R17-9/REFEREE_VERDICT.md`, `vR17-9`): **CONFIRMED WITH CORRECTIONS; OPEN with the imported placement, SM-LIFTED only if VM is admitted as an extra stipulation** (`vR17-9:9,13`).
- `P/agents/C5_R9-9_report.md` (all, `R99`) and verdict (`vR9-9`); `C5_R13-5_report.md:1-220` (`R135`) and verdict (`vR13-5`); `C5_R17-4_report.md:15-50,114-128,270-280` and verdict (`vR17-4`); `vR16-13:5` (the V0 stipulation).
- Runners: `P/scripts/C5/R17-9/{photon,vm_check,smsolve,smsolve_lib}.py` read; `photon.py, sublum.py, content3.py, content4.py, zz.py, dfam.py, dirac.py, r161_laws.py` copied unmodified into `S/scripts/`. The R9-9 and R13-5 runners were not rerun; their results enter only through refereed statements (`vR9-9:5-7`, `vR13-5:3-5`).

**Labels.** proved (complete argument under stated hypotheses; unrefereed) / checked (numerics here) / suggested / reading / comparator.

---

## 0. In plain words

1. **Neither VU nor VM survives the four requirements (proved; checked).**
   - **VU fails the vector Ward identity W1 already at first order in q, in the stated Maxwell family 𝔐.** W1 at O(q), with a symmetric stress whose energy density integrates to H, fixes the *forward* stress of every photon: T_ij(k, k) = ω v_i v_j, the same for both polarizations. VU's B-part carries an extra z-average on each leg (c_z(k)², `R179:88`). Outside the photon's z-box this makes the forward T_xy mix the two polarizations, which W1 forbids. The size is O(1): 0.25–0.87 against a required scale of 0.01–0.06 (`forward_w1.out`). This is the same "extra form factor c_z(k₁)c_z(k₂)" that R17-9 itself names as what unbalances E against B (`R179:188`).
   - **VM, as R17-9 built it, is not covariant about R9-9's graviton.** Its B-product sits at z + ½ on one side of h_xy (phase e^{is/2}). The C₂ rotations through h_xy's plaquette centre flip z, so they send this coupling to the mirror one at z − ½. The covariance defect is 15–29% at q = 0.3 and zero at q = 0 (`cov_check.out`). VM is local (a finite one-sided stencil), so this corrects R17-9's "non-local half-shift" wording (`R179:93`): its defect is covariance, not locality.
   - **VM's E_g row also fails W1 at O(q).** It has no averaging, so its forward E_g stress is wrong off the transverse box (`forward_w1.out`, "any Eg" rows).
2. **What does survive is a third family, VW, the vector analogue of R9-9's scalar U vertex (proved; checked).** U was defined by its W1 forward value (`R99:46`); VW is defined the same way.
   - Each stress component T_ij carries per-leg averaging σ′(k_i)σ′(k_j), in the directions of its own indices only.
   - Every product of fields sitting at half-integer height (E_z², B_x², B_y², B_xB_y) is placed symmetrically about h.
   - VW passes forward-W1 (residual ≤ 6e-16), C₂/C₄ covariance (≤ 4e-16), gauge invariance and co-location with R9-9's h.
   - Within 𝔐, its T₂g vertex at q = 0 is **unique** (Lemma X), and it equals VM's T₂g at q = 0.
3. **The placement freedom that remains is FREE at O(q²) inside VW (proved).** It consists of one symmetric z-stencil per half-integer-height product type: one for T₂g, two for E_g.
   - Any two stencils differ by an identically conserved superpotential term (Lemma I), so W1 cannot fix them at any order. An exact W1 completion is not built for any member. This confirms the expectation (`TESTS:6363`), but only *inside* VW.
   - Ξ is exactly affine in the stencil's second moment λ. The slopes are positive on every sampled law: +1.3e-2 to +0.26 for T₂g and +4.4e-2 to +0.36 for E_g per unit λ per vector (`stencil_sens.out`). So the stencil is a live law datum that moves both TT rows.
4. **R17-9's sign, recomputed for the survivors (checked; search).**
   - **The T₂g sign survives, weaker.** Under the nearest symmetric placement (VW0, λ = ¼), small-box photons still have Ξ_T2g < 0, but weaker than VM: −1.05e-3 against −2.70e-3 at R17-9's root photon.
   - **The E_g row changes completely.** At R17-9's root photon it goes from +2.95e-3 (VM) to −3.4e-4 (VW0).
   - **R17-9's VM root is not a root under VW0.** The totals there are (+1.97e-2, −3.95e-2, μ_E 1.3e-11) (`recheck_root.out:3`).
   - **No VW0 photon in a 40-law grid meets R17-9's two sampled necessary inequalities.** The closest misses are γGw(0.15, 1.5) at (+7.2e-4, +3.95e-3) and γGw(0.7, 0.25) at (+6.3e-4, +4.19e-3) (`vw0_scan.out`).
   - **The VW0 solves found no root.** Two 6-knob solves both stopped at the same bound point, with T₂g residual +1.2e-2.
   - **Opening the stencil as a 7th knob found no root either.** With weights ≥ 0, i.e. λ ≥ ¼, two continued solves ran toward under-resolved narrow-turn photons and the Dirac lower bound. The apparent residual of (+3e-4, −5e-5, +8e-6) is a grid artifact: the vector T₂g term shifts by +1.7e-3 between N = 48 and N = 96 (§3.5).
5. **Against the FIXED readings: worker reading OPEN, with a registration note.**
   - Each FORCED clause has an "or excludes" disjunct. Here VM is excluded (covariance; E_g W1) and VU is excluded (W1 at O(q)). So the letters of FORCED-VU and FORCED-VM would both be met at once, which shows the readings presumed one of the two survives.
   - Neither is refereed, and FREE (both pass) fails.
   - Substantively, the reading is **NEITHER**. Consistency forces the VW family, and inside it the placement is FREE at O(q²).

---

## 1. Class, hypotheses, stipulations, exclusions (stated before any title)

**Setting (`TESTS:6346-6351`).**
- The photon is R8-5/R17-9's generalized forward difference, D_j = iσ(k_j)e^{ik_j/2}, σ = sgn(k)·d(|k|), in R16-10's subluminal class d′ ∈ [0, 1], with ω² = Σσ_j² (`R179:71-74`).
- Families: NN, γG(b) (the R14-1 shape) and γGw(b, w).
- The field theory is non-compact U(1). At one loop in the free limit the compact theory gives the same bilinears.
- R9-9's graviton: h_xy at xy-plaquette centres, divergence symbol D^g_j(q) = d_g(q_j)e^{iq_j/2}, d_g(q) = q for |q| ≤ 1 (`R99:38,100`).
- One loop, axial q = qẑ, the R17-9 pipeline (Ξ = ∂_{q²}Π + ∂_{ω²}Π, grid shifts plus Richardson, β exact; `R179:108,171`).
- Excluded: superluminal photons and pairing.

**The family 𝔐 ("Maxwell stress with E and B products placed at any half-integer offsets").**
- T_ij is a sum of products of lattice E (links) and B (plaquettes), with the Maxwell index structure E_iE_j + B_iB_j − ½δ_ij(E² + B²).
- Each product has its own per-leg averaging and its own product placement.
- At axial q each TT component is described by matrices M_E(κ₁, κ₂) and M_B(κ₁, κ₂) on field components (S/scripts/r1712_lib.py:24-65):
  - per-leg symbols c(k) = d′(|k|) (R17-9's averaging symbol, `R179:85`);
  - a product-placement factor P(s), s = k₁z + k₂z with representatives, which the half-integer-height products carry.
- Sub-family 𝔐₁ ("one weight per component"): every product in T_ii carries the same weight. This is the natural reading of "Maxwell stress", and VW lies in it.

**Members tested.**
- VU (`photon.py:66-79`) and VM = VMone (`photon.py:130-156`): R17-9's two vertices, rerun unmodified in my own implementation.
- VMsym: VM with the B-product placed symmetrically at z ± ½, P = cos(s/2).
- VW(n): forward-correct and symmetric, with offsets z ± (n + ½), P = cos((n + ½)s).
- VWa: P = (1 − a)cos(s/2) + a·cos(3s/2), second moment λ = ¼ + 2a.

**W1 hypotheses (imported from R13-5, `R135:85-88`).**
- (W1-s) Scattering channel: (ω(k+q) − ω(k))F^{0ν}_{λλ′}(k+q, k) = Σ_j D^g_j(q)F^{jν}_{λλ′}(k+q, k), with a kernel that is C¹ near the diagonal.
- (H-sym) T^{μν} is symmetric.
- (H-E) Universal forward energy: F^{00}_{λλ′}(k, k) = ω δ_{λλ′}, i.e. ∫T⁰⁰ = H.
- The two photon polarizations are degenerate bands.

**Order of exactness.** The W1 tests here are at O(q) (forward values), which is necessary. An exact W1 completion is not constructed for any member (it stays OPEN; `vR17-9:3`).

**Locality and covariance.**
- Locality: a finite-stencil or absolutely summable kernel; continuity on the torus is checked via the representative twist.
- Covariance: under the proper cubic rotations (`AX:37-38`) about R9-9's h_xy site. Lemma M uses the same hypothesis (`R17-4:116`; `AX:57-58`).

**Excluded:**
- general (non-Maxwell) E/B bilinears, which lie outside 𝔐 (§3.1, scope note);
- off-axis q;
- the dressed matter side;
- W2;
- interacting gauge fields;
- the Dirac V0 and scalar U vertices (inherited unchanged from R17-9).

## 2. Prior art (each counted once)

- **R17-9 and its referee.** VU and VM; VM gives a rank-3 SM-count zero with μ_T2 = 0.106 (`vR17-9:7,13`). The VU W1 completion is "assumed" (`vR17-9:3`). Under the strict R9-9 placement VM is out of setting (`vR17-9:9`). P-R17-9b (`R179:282`).
- **R9-9.** Placement: T^{jl} at (e_j + e_l)/2, and the Ward identity via midpoint phases (`R99:100-101`). The U vertex is defined by its W1 forward value εv_iv_j (`R99:46`). The tree-level identities are algebraic (`R99:83`; `vR9-9:5`).
- **R13-5.**
  - Lemma P1/C3: in the pair channel W1 is no constraint for m > 0 (`R135:143-182`; `vR13-5:3`).
  - Lemma W0: the axial TT blocks are invisible to the two-point Ward identity (`R135:184-207`), narrowed by `vR13-5:5`.
  - "Only the q → 0 values are tied to constrained components" (`R135:200`). Lemma F below makes this concrete for the photon.
- **R17-4.** Lemma M: C₂ᵧ covariance plus continuity force T₂g to vanish at K_x = π (`R17-4:114-127`; `vR17-4:7`). P-TTV₂ (`R17-4:274`).
- **R16-13.** V0 is a stipulation, not derived from one Belinfante action (`vR16-13:5`).
- **Lattice Maxwell stress literature (RECALLED, not checked).** The standard statement is that a lattice gauge theory has no exactly conserved local symmetric stress tensor without improvement and point-splitting choices. Improvement terms ∂∂Y are the standard ambiguity. Lemma I uses only the elementary identity, not the literature.

---

## 3. Results

### 3.1 (a) The vector W1 identity at O(q): the forward-value lemma

**Lemma F (proved).** Under (W1-s), (H-sym) and (H-E):

  **F^{ij}_{λλ′}(k, k) = ω(k)·v_i(k)·v_j(k)·δ_{λλ′},  v = ∇ω, v_i = σ_iσ_i′/ω.**

*Proof.*
1. D^g_j(q) = q_j + O(q²), and ω(k+q) − ω(k) = q·v + O(q²).
2. Divide (W1-s) by |q| and let q → 0 along any direction n. This gives (n·v)F^{0ν}(k, k) = n_jF^{jν}(k, k) for all n, hence F^{jν} = v_jF^{0ν}.
3. For ν = 0, with (H-E): F^{j0} = ωv_jδ. (H-sym) then gives F^{0j} = ωv_jδ.
4. For ν = i: F^{ji} = v_jωv_iδ. ∎

This is R9-9's U normalization, "forward values ε(1, v)(1, v)ᵀ" (`R99:105`), now required for the vector.

**Forward amplitude of a family member (proved).** For a†_k a_k (legs (−k, k), s = 0):

  S_{λλ′} = ½[ω ε_λᵀM_Eε_{λ′} + ω (σ̂×ε_λ)ᵀM_B(σ̂×ε_{λ′})].

It is required to equal −(ω/2)e:(vv)δ_{λλ′} (R17-9's sign convention, T = EE + BB − …).

**Corollary F1: VU is excluded (proved; checked).** For T₂g, M_E = κ_E e and M_B = κ_B e, with κ_E = c_xc_y and κ_B = c_xc_yc_z² at (−k, k) (`photon.py:67-77`). Using σ̂×ε₁ = ε₂ and σ̂×ε₂ = −ε₁:

  S₁₂ = ½ω(κ_E − κ_B)e(ε₁, ε₂) = ½ω c_xc_y(1 − c(k_z)²)(ε₁ₓε₂ᵧ + ε₁ᵧε₂ₓ).

This is nonzero wherever |k_z| > b_γ, c_xc_y ≠ 0, and the polarization factor is nonzero (generic). Lemma F requires it to vanish. So no symmetric stress with ∫T⁰⁰ = H that obeys W1 even to O(q) has VU's T_xy.

Checked (`forward_w1.out`; 400 random k per region):

| photon | VU, k_z off the box: max\|S − S_req\| (scale) T₂g / E_g | VMone T₂g | VMone E_g (whole zone) | VW0, VW1 (all) |
|---|---|---|---|---|
| NN | 0.76 (0.024) / 0.75 (0.011) | 3.6e-16 | 0.93 (0.29) | ≤ 5.5e-16 |
| γG(1.4) | 0.87 (0.020) / 0.86 (0.012) | 6.7e-16 | 1.13 (0.78) | ≤ 6.1e-16 |
| γGw(0.2513, 1.0195) (R17-9 root photon) | 0.35 (0.045) / 0.32 (0.024) | 1.8e-16 | 0.35 (0.12) | ≤ 2.3e-16 |
| γGw(0.3, 0.5) | 0.27 (0.059) / 0.25 (0.033) | 1.2e-16 | 0.28 (0.11) | ≤ 1.4e-16 |

- **Closed form, checked.** Corollary F1's S₁₂ matches the direct computation to 3.3e-16 over 900 points (`f1_closed.out`).
- **Weaker test.** I also tested only rank-one-ness: F^{e}(k, k) = e:(vv)·Λ with *any* common polarization matrix Λ for both TT components. VU fails it (relative mismatch 15–816) and VMone fails it (27–475); VW0 passes to ≤ 1.2e-13.
- **Box.** For the NN photon (no exact box), VU fails at O(k²) even near k = 0 (1.3e-3), while VW is exact.

**Corollary F2: VM's E_g is excluded; VM's T₂g passes (proved; checked).**
- VMone E_g has M_E = M_B = diag(1, −1, 0). Its forward value is −(ω/2)(σ̂ₓ² − σ̂ᵧ²), against the required −(1/2ω)(σₓ²cₓ² − σᵧ²cᵧ²). These are equal only if σₓ²(1 − cₓ²) = σᵧ²(1 − cᵧ²), which fails off the transverse box.
- VMone T₂g has κ_E = κ_B = c_xc_y at (−k, k), because B_x is averaged along y and B_y along x (`photon.py:145`). It passes to rounding.

**Lemma X: the T₂g pair vertex at q = 0 is fixed in 𝔐 (proved).**
1. Pair at q = 0 and forward scattering are both read from the same position-space operator at leg arguments (κ, −κ): c is even and s = 0.
2. In 𝔐, T₂g has two unknown scalars at q = 0, κ_E(k) and κ_B(k).
3. Lemma F gives two independent conditions:
   - the λ ≠ λ′ element forces κ_E = κ_B;
   - the trace forces κ_E + κ_B = 2σ′(k_x)σ′(k_y).
4. So κ_E = κ_B = σ′ₓσ′ᵧ, and the q = 0 pair matrix N = ½[ωM_E + X M_B X/ω], with X = [σ(k)]× (`photon.py:10-12`; X₂ = −X₁ and X₁ᵀ = −X₁ at q = 0), is fixed.
5. With c = d′ this is VM's T₂g at q = 0. ∎

For E_g in 𝔐 there are six per-product weights against three conditions, so the q = 0 E_g vertex is fixed only in 𝔐₁. There w_xx = σ′(k_x)² and w_yy = σ′(k_y)², which is VW's E_g:

  M_E = diag(½(cₓ² + cᵧ²), −½(cₓ² + cᵧ²), −½(cₓ² − cᵧ²)P),  M_B = diag(½(cₓ² + cᵧ²)P, −½(cₓ² + cᵧ²)P, −½(cₓ² − cᵧ²)).

- R17-9's E_g rows dropped the δ-part. With unequal xx/yy weights on the lattice it does not cancel.

**Scope note (proved; reading).** Lemma X uses 𝔐's tie between the pair and scattering kernels.
- For a general E/B bilinear (arbitrary 3×3 kernels), S fixes only (M_E − M_B)^⊥_tl and the trace. The pair helicity-2 part (M_E + M_B)^⊥_tl stays free.
- That is R13-5's C3 ("the pair stress is a law datum", `R135:182`), now for vectors.
- Outside 𝔐, a scattering-only correction supported off the box (where ω > 0, so it is quasi-local) could repair VU's forward values while keeping its pair vertex. So VU is excluded *in 𝔐*, which is the registered family, not among all local stresses.

**W1 at axial q itself.** The two-point Ward identity does not reach the B₁ and B₂ blocks at axial q (`R135:186-198`, narrowed by `vR13-5:5`). Every constraint above enters through the q → 0 limit. This makes `R135:200` concrete: the forward values are what W1 fixes.

### 3.2 (b) Gauge invariance, covariance, locality

- **(ii) Gauge invariance (proved; trivial).** Every member of 𝔐 is a bilinear in E and B, which are invariant under A → A + Dφ (and under compact link gauge transformations, at one loop in the free limit). So (ii) separates nothing. All the pair amplitudes are transverse (projectors P₁, P₂, `r1712_lib.py:83-85`).
- **Lemma C (proved; checked).**
  - The stabilizer of h_xy's site in the proper cubic space group contains C₂ about the x-parallel and y-parallel lines through (½, ½, 0). These map z → −z.
  - VMone couples h_xy(r) to T^B_xy(r + ½ẑ). Under those C₂ it maps to h_xy(r)·T^B_xy(r − ½ẑ), a different operator.
  - Covariance therefore requires a z-symmetric product stencil, P(s) = Σ_n w_n cos((n + ½)s). VMone's e^{is/2} is not of that form.
  - Checked (`cov_check.out`, N(Rk₁, Rk₂) against s_e R N Rᵀ, 300 pairs):
    - VMone: C₂ₓ and C₂ᵧ defects of 15–29% at q = 0.3 for both rows (`cov_check.out:6,14,22`), and 0 at q = 0;
    - VU, VMsym and VW0: ≤ 3.5e-16 for all of C₂ₓ, C₂ᵧ and C₄z.
- **Locality (proved).**
  - Under a leg's k_z → k_z − 2π, the rotated-frame components that sit at half-integer z (E_z, B_x, B_y) flip sign (`R179:74`, `R179:170`).
  - VW's P(s) flips exactly on the entries that carry those components (T₂g: B_xB_y; E_g: E_z², B_x², B_y²; not B_z² or E_x², E_y²). So every VW pair amplitude is continuous on the torus, and its finite stencils give a finite-range position kernel.
  - VMone is also a finite stencil, so it is local; it is non-covariant only.
  - VU is continuous because c(π) = 0 (`vR17-9:3`).
- **Lemma M-type face test (proved).** VW's T₂g amplitude carries σ′(k_x)σ′(k_y). It vanishes on K_x = π as Lemma M requires (`R17-4:116-121`), for every photon with d′(π) = 0 (all laws used).

### 3.3 (iii) R9-9's placement and its identities

- **What R9-9's identities require (proved).**
  - The tree-level identities (R symmetric, R(d⊗ξ + ξ⊗d) = 0, Bianchi, {G, S} = 0) are algebraic in the graviton's own symbols (`R99:83`). They constrain nothing on the matter side.
  - The matter coupling enters the gauge algebra only through the variation of Σh*T, which the lapse and shift absorb iff W1 holds with D^g (`R99:100-101`).
  - So (iii) = (i) plus co-location: T^{jl} centred at (e_j + e_l)/2, i.e. covariant under the stabilizer of h's site, which is Lemma C.
- **Result.**
  - VU is co-located but fails (i).
  - VMone is not co-located: centring its B-product on R9-9's h needs P symmetric. The alternative is a graviton whose h_xy sits at height z + ½, which is not R9-9's (`R179:93`).
  - VW is co-located and passes (i) at O(q).

### 3.4 (c) Survivors, the residual freedom, and R17-9's sign

**Survivors.**
- The stated requirements tested here — W1 at O(q), gauge invariance, covariance about R9-9's h, and locality — select the family VW: for T₂g within 𝔐, and for E_g within 𝔐₁.
- Its free data at axial q are the symmetric z-stencils:
  - P_T for B_xB_y (T₂g);
  - P_E^E for E_z² and P_E^B for B_x², B_y² (E_g).
  - These are in different irreps or different fields, so cubic covariance does not tie them.

**Lemma I: the residual freedom is invisible to W1 at every order (proved).**
1. For n ≥ 1, cos((n + ½)s) − cos(s/2) = −2 sin²(s/2)·U_n(cos(s/2))·U_{n−1}(cos(s/2)) (Chebyshev U). The product U_nU_{n−1} is itself an antiperiodic symmetric stencil, and sin²(s/2) = sin²(q/2).
2. Hence for any two members, ΔT^{xy} = (P − P′)T_B = D^g_z(q)²·Y. Here Y = e^{−iq}[4 sin²(q/2)/d_g(q)²]·(finite-stencil B-product), and the bracket is smooth, periodic and nonvanishing, because d_g has a single simple zero.
3. Set Y^{xzyz} = Y^{zxzy} = −Y^{zxyz} = −Y^{xzzy} = Y (Riemann symmetries).
4. Then ΔT^{ij} = D_kD_lY^{ikjl} and ΔT^{0ν} = 0 satisfy D_iΔT^{iν} ≡ 0 identically, because D_iD_k is symmetric while Y is antisymmetric in (i, k). The axial-q TT component of ΔT is exactly (P − P′)T_B. The same works for E_g via Y^{xzxz} − Y^{yzyz}. ∎

**Consequence.** If any VW member has an exact W1 completion, all do, and W1 does not select among them (other Ward identities, e.g. W2, are not examined). The placement is FREE inside VW. That existence is not proved: the exact W1 completion is OPEN for every member (`vR17-9:3`).

**Sensitivity (proved; checked).**
- The stencil enters α only through its O(q²) coefficient −λ/2. So Ξ(λ) = Ξ(¼) + (λ − ¼)G with G = ⟨Re⟨N, N_B⟩_P/E⟩ at q = 0; β does not depend on λ.
- For non-negative weights, λ = Σw_n(n + ½)² ≥ ¼. So VW0 minimizes both rows wherever G > 0.
- Checked (`stencil_sens.out`): affine to 6e-7 over a ∈ [−0.3, 0.2].

| photon | dΞ_T2g/dλ | dΞ_Eg/dλ |
|---|---|---|
| γGw(0.2513, 1.0195) | +1.25e-2 | +4.40e-2 |
| γGw(0.3, 1.0) | +1.47e-2 | +4.94e-2 |
| γG(1.4) | +0.263 | +0.359 |

**Per-vector Ξ at N = 48 (N = 64 in parentheses), selected rows (`xi_scan_N48.out`, `xi_scan_N64.out`).**

| photon | VU (T₂g, E_g) | VMone | VW0 = VMsym for T₂g; VW0 E_g | VW1 |
|---|---|---|---|---|
| NN | +1.441e-2, +1.720e-2 | +1.944e-2, +7.333e-2 | +3.722e-2, +5.505e-2 | +0.298, +0.457 |
| γG(1.4) | +9.783e-2, +0.1201 | +4.746e-2, +9.597e-2 | +8.410e-2, +0.1111 | +0.611, +0.830 |
| γGw(0.15, 0.25) | +3.8e-4, +7.9e-4 (+2.0e-4, −4.9e-4) | −2.79e-3, −0.126 | −2.69e-3 (−2.50e-3), −1.60e-2 (−1.48e-2) | −1.19e-3, −2.69e-3 |
| γGw(0.2513, 1.0195) | +3.715e-3, +8.961e-3 | −2.705e-3, +2.953e-3 | −1.063e-3 (−1.053e-3), −3.36e-4 (−3.27e-4) | +2.40e-2, +8.77e-2 |
| γGw(0.3, 1.0) | +4.81e-3, +1.174e-2 | −2.43e-3, +7.99e-3 | −5.00e-4, +1.444e-3 | +2.89e-2, +0.100 |
| γGw(0.5, 0.5) | +1.06e-2, +3.16e-2 | −2.69e-3, +5.33e-3 | −8.73e-4, +3.79e-4 | +2.67e-2, +9.63e-2 |

- **Recheck of R17-9's numbers.** VU and VMone reproduce `vm_check.out` and `R179:26-28,201` to every printed digit: NN VM N = 48 +1.94395e-2 / +7.33269e-2; γG(1.4) VU +9.783e-2. They also match the referee's (−2.68, +2.96)e-3 for VM at the root photon (`vR17-9:5`).
- **R17-9's root, rechecked.** R17-9's archived N = 48 root reproduces with my VMone code to 1e-12 (`recheck_root.out:1`). The referee's tighter-quadrature retune (`vR17-9:7`) was not repeated.
- **Readings.**
  - The T₂g sign mechanism of R17-9 (small-box photons give Ξ_T2g < 0) survives under the covariant, W1-correct VW0, but weaker: 21–96% of the VM value on the sampled small-box laws, and 39% at R17-9's root photon.
  - VM's large positive E_g on small-box photons does not survive. It was a product of the missing δ-part and the missing c² weights.

**The SM-count question under the survivors (checked; search, not a proof).** Content, matter vertices and knobs are as in R17-9 (`smsolve.py`); m = 0.01.
- At R17-9's VM root, VW0 gives totals (+1.97e-2, −3.95e-2, μ_E 1.3e-11), and VMsym gives (+1.97e-2, +0.321, …) (`recheck_root.out:2-3`). The root does not carry over.
- R17-9's sampled necessary inequalities (Ξ_γ,T2g ≤ 6.0e-4 and Ξ_γ,Eg − Ξ_γ,T2g ≥ 4.46e-3; `R179:226-227`) are met by **no** VW0 law on a 40-law (b, w) grid (`vw0_scan.out`). The boundary is close:
  - γGw(0.15, 1.5): (+7.2e-4, +3.95e-3);
  - γGw(0.7, 0.25): (+6.3e-4, +4.19e-3).
- **VW0, 6 knobs, two starts** (`smsolve_VW0_A.out`, `_B.out`). Both stopped at the same point: w_γ = 0.118 at its lower bound (under-resolved at N = 48), b_f = 0.15 at its lower bound. Totals (+1.21e-2, −5.57e-3, +6.4e-4). No root.
- **VWa, 7 knobs (stencil a ∈ [0, 0.5], weights ≥ 0)** (`smsolve_VWa_N48.out`). Stopped at the nfev cap: a = 0.49994 (bound), b_f = 0.15 (bound), w_γ = 0.18. Totals (+1.41e-3, −3.24e-4, +4.8e-5). No root.
- **VWa continuation with a ∈ [0, 1]:** stopped at an under-resolved point; not a root (§3.5).
- **Reading.** With the forced, covariant vertex and nonnegative placements, the R17-9 VM zero is not reproduced, and the searches stall at the Dirac lower bound, as R17-9's VU solve did (`R179:229-231`). This is a search, not a demonstration. Signed stencils (λ < ¼) and independent per-irrep stencils were not searched; with them, the placement data are two to three free knobs on the axis rows.

### 3.5 VWa continuation (a ∈ [0, 1])

**Run.** `smsolve_vwa1.py`, started from the VWa end point, with a ∈ [0, 1] so both weights stay ≥ 0. The solve stopped at the nfev cap, status 0 (`smsolve_VWa1_N48.out`).

**End point.**
- Knobs: a = 0.578 (λ = 1.41); b_γ = 0.3527 with w_γ = 0.139 (fw_γ at its lower bound 0.05); b_f = 0.15 at its lower bound; r = 0.481; b_s = 2.183, w_s = 0.0197.
- Totals: (+3.07e-4, −5.3e-5, +8.5e-6) against a content scale of 7e-2. μ_T2 = +9.2e-2.

**Not a root (checked).**
- The end-point photon's turn width is 0.139, about one grid step at N = 48 (2π/48 = 0.131).
- Its 12-vector T₂g contribution moves from −7.45e-4 (N = 48) to +6.5e-5 (N = 64) to +9.56e-4 (N = 96) (`endpoint_res.out`). That shift of +1.7e-3 is about five times the N = 48 residual.
- At N = 96 the T₂g total would be about +2.0e-3, not 0.
- The search is being driven into under-resolved narrow-turn photons and the Dirac lower bound.

**Reading.** No resolved SM-count root was found with VW-type vectors under nonnegative placements (λ ≥ ¼). This is a search, not a demonstration. Not searched:
- signed stencils (λ < ¼, which lowers both rows);
- independent stencils per irrep (P_T, P_E^E, P_E^B);
- photons outside γGw;
- Dirac boxes below b_f = 0.15.

With independent per-irrep stencils the two axis rows have two extra linear knobs (§3.4, sensitivity). A zero would then be a placement-datum tuning (P-R17-12b), not a shape zero.

### 3.6 (d) Prices (named, not adopted)

- **P-R17-12a (correction, no new price).** The vector stress must have W1-correct forward values: T_ij(k, k) = ωv_iv_j, per-leg averaging σ′ in the directions of its own indices only, and the δ-part with weights c_i². This uses only R13-5's imported W1 hypotheses (`R135:85-88`). It removes VU and VM's E_g as non-conserved. R17-9's VU numbers, and VM's E_g numbers, are integrals of vertices that are not TT parts of any symmetric, O(q)-conserved stress with ∫T⁰⁰ = H in 𝔐.
- **P-R17-12b (refines P-R17-9b and P-TTV₂).** Three symmetric z-placement stencils (P_T, P_E^E, P_E^B) are law data. They are W1-invisible at all orders (Lemma I) and each moves its TT row linearly (G ~ 1e-2 to 0.4 per unit λ per vector). Fixing them needs a principle beyond the stated requirements, e.g. derivation from one lattice action √g F² with a stated metric placement, which was not attempted. Source/action gate: `AX:187`; dynamics downstream: `AX:114-130`.
- **P-R17-12c (covariance).** Keeping VM's one-sided placement costs either a graviton with h_xy at z + ½ (not R9-9's) or a non-covariant coupling (against `AX:57-58` as used by Lemma M).
- **Bill (reading, conditional).** The VM-route count of R17-9 (3 tunings) is void under the forced vertex. With VW0 no shape root was found, so the axis-row status reverts to R17-9's VU line: the axis cone plus shear needs a non-shape knob (`R179:288`). The P-R17-12b stencils are exactly such non-shape knobs, at ~1e-13 each, if adopted as tunable law data.
- **No axiom text changes.** No sizes at a = ℓ_P are quoted (`AX:189-190`).

---

## 4. Against the FIXED readings (`TESTS:6358-6362`)

**Worker reading: OPEN, with a registration note.**
- **FORCED-VU (selects VU or excludes VM, refereed): not met.** VM is excluded here by Lemma C (proved; checked) and by Corollary F2 for its E_g row (proved; checked). But VU does not survive either (Corollary F1), so consistency does not "select VU". The proof is unrefereed.
- **FORCED-VM (selects VM or excludes VU, refereed): not met.** VU is excluded (Corollary F1, proved in 𝔐; checked). But VM does not survive (Lemma C; F2), so consistency does not "select VM". The proof is unrefereed.
- **Registration note.** Read literally, the "or excludes" disjuncts of both FORCED clauses are met simultaneously. The readings presumed that one of VU and VM survives. The referee should rule on whether this is OPEN, or a FORCED reading for the third family.
- **FREE (both satisfy every stated requirement, checked): not met.** Neither VU nor VM does.
- **OPEN: met (otherwise).**
- **Substantive reading: NEITHER.**
  - Consistency (W1 at O(q) plus covariance about R9-9's h) forces the VW family, the vector analogue of U.
  - Its T₂g vertex at q = 0 is unique and equals VM's T₂g at q = 0.
  - The z-placement is FREE at O(q²) *within* VW (Lemma I), as the expectation said, but it is not the VU/VM fork.
- **Recomputed sign (probe (c)).** The negative small-box T₂g survives, at 21–96% of VM's size (39% at R17-9's root photon). R17-9's VM SM-count zero does not carry over; no VW0 root was found.

**Expectation ("FREE at O(q). W1 constrains only the divergence, and the placement is an O(q²) datum", `TESTS:6363`): partly refuted.**
- W1 at O(q) is *not* silent. Through the forward values it fixes the per-leg form factors, which is what separates VU from VM; that difference is O(1) at q = 0, not O(q²).
- The O(q²) part of the expectation holds for the residual symmetric stencils.

## 5. Strong-word check

- **"Proved"** is used for:
  - Lemma F; Corollaries F1 and F2 (algebraic forward amplitudes);
  - Lemma X (two unknowns, two conditions);
  - Lemma C; locality and continuity via the sign-flip bookkeeping;
  - Lemma I (Chebyshev factorization plus superpotential);
  - the affine dependence on λ; λ ≥ ¼ for nonnegative stencils.
- **"Checked"** is used for every number.
- **"Excluded"** for VU means: in 𝔐, under (W1-s, O(q)) + (H-sym) + (H-E). It is not excluded among general local stresses (§3.1 scope note).
- **"Excluded"** for VM means: as a coupling to R9-9's h_xy under cubic covariance, plus its E_g row by W1.
- **"No root"** means local least squares from stated starts, ending at bounds. It is not a conflict claim.
- **Not claimed:**
  - an exact W1 completion of any member;
  - uniqueness of VW's E_g vertex outside 𝔐₁;
  - off-axis rows;
  - Dirac/V0 or scalar-U forward tests (U passes by its definition, `R99:46`; V0 is untested here);
  - SM-CONFLICT;
  - μ_T2.

## 6. For the referee

1. **Lemma F.** Whether (H-E) and (H-sym) are in-setting for the vector W1 (I import them from `R135:85-88`). If (H-E) is dropped, the weaker rank-one test still excludes VU and VMone (§3.1).
2. **The forward amplitude formula** S = ½[ωεM_Eε′ + ω(σ̂×ε)M_B(σ̂×ε′)] and Corollary F1's closed form ½ωc_xc_y(1 − c_z²)e(ε₁, ε₂).
3. **Whether 𝔐 is the registered family** ("E and B products placed at any half-integer offsets"), and whether per-leg averaging (as in VU) belongs to it. Outside 𝔐 the pair vertex is free (scope note).
4. **Lemma C:** whether covariance of the coupling about h's site is a stated requirement (item (iv), "Lemma M-type covariance").
5. **Lemma I's superpotential bookkeeping** with the graviton's D^g, including the representative sign of P(s).
6. **The registration conflict** (§4).
7. **Suggested follow-up, not done.** Apply Lemma F to R16-13's Dirac V0, which has the Wilson mass uncoupled while the Wilson term shapes ω (`vR16-13:5`). If V0 fails the forward test, the Dirac Ξ and μ_T2 numbers (R17-13's input) belong to a non-conserved vertex too.

## 7. Files (`S/scripts/`)

- `r1712_lib.py`: vertex family (VU, VMone, VMsym, VW(n), VWa), pair weights, Ξ pipeline, forward amplitude.
- `forward_w1.{py,out}`: Lemma F tests (exact and rank-one).
- `cov_check.{py,out}`: C₂ₓ, C₂ᵧ and C₄z covariance.
- `f1_closed.{py,out}`: Corollary F1's closed form.
- `xi_scan.py` → `xi_scan_N48.out`, `xi_scan_N64.out`: per-vector Ξ for 12 photon laws × 5 vertices.
- `vw0_scan.{py,out}`: VW0 against R17-9's inequalities.
- `stencil_sens.{py,out}`: λ-sensitivity.
- `recheck_root.{py,out}`: R17-9's archived root under each vertex.
- `smsolve_vw.py` → `smsolve_VW0_A.out`, `smsolve_VW0_B.out`; `smsolve_vwa.py` → `smsolve_VWa_N48.out`, `smroot_VWa_N48.npy`; `smsolve_vwa1.py` → `smsolve_VWa1_N48.out`, `smroot_VWa1_N48.npy`; `endpoint_res.{py,out}`: grid check of that end point.
- Copied unmodified from `P/scripts/C5/R17-9/`: `photon.py`, `sublum.py`, `content3.py`, `content4.py`, `zz.py`, `dfam.py`, `dirac.py`, `r161_laws.py`, `smsolve_lib.py`, `smroot_VM_N48.npy`.
