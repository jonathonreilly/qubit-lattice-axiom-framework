# C5 R17-9 report: SM content on one graviton cone — do the gauge-boson loops offset the Dirac birefringence?

**Author.** Claude Opus 5.5 probe (same model family as the supervisor and every C5 worker). Unrefereed. 2026-10-13, 00:53Z to 01:37Z. No repository file was edited. No downloads, no web lookups.

**Paths.** `P/` = `.claude/science/exercises/gravity-current-state-20261009/`. `S/` = `.../scratchpad/C5/R17-9/`. Scripts and `.out` files are in `S/scripts/`. Every run used `OMP_NUM_THREADS=2`; the longest single run took 8.5 min (`verify_VM.out`, 508 s). Machine load was 3–8 from other jobs.

**Read.**
- `docs/MINIMAL_AXIOMS_2026-06-29.md`, in full (`AX`).
- `P/TESTS.md`: C5 method and readings (`:2302-2320`); round-16/17 rules (`:5039`, `:5688-5713`); the entries for R9-9 (`:3862-3873`, `:3939-3950`), R13-5 (`:4668-4680`, `:4707-4713`), R14-3 (`:4830-4844`, `:4915-4922`), R16-3 (`:5087-5106`, `:5359-5371`, `:5427-5432`), R16-9 (`:5373-5397`, `:5550-5560`, `:5668-5684`), R16-13 (`:5595-5613`; worker `:6088-6108`), R17-4 (`:5816-5845`); my item (`:6110-6128`). The driver appended the R16-13 and R17-4 verdicts while I ran (`:6146-6157`, `:6171-6178`).
- `agents/C5_R16-13_report.md` (all) and its verdict (`scratchpad/C5/ref_R16-13/REFEREE_VERDICT.md`, `vR16-13`): **NOT CONFIRMED, OPEN**.
- `agents/C5_R17-4_report.md` (all) and its verdict (`scratchpad/C5/ref_R17-4/REFEREE_VERDICT.md`, `vR17-4`): **CONFIRMED WITH CORRECTIONS, COUNTED-ROWS for U+E1**.
- `C5_R16-9_report.md` and verdict; `C5_R16-3_report.md` and verdict; `C5_R10-5_report.md` and verdict (`vR10-5`); `C5_R9-9_report.md:20,36-48,100-101`; `C5_R16-10_report.md:28-74,160`.
- Archived runners `P/scripts/C5/R16-13/{zz,dfam,dirac,sublum,content3,content4,r161_laws}.py`, copied unmodified into `S/scripts/`.

**Labels.** proved (complete argument under stated hypotheses; unrefereed) / checked (numerics here) / suggested / reading / comparator.

---

## 0. In plain words

1. **A vector TT vertex was built (stipulated; checked).** The lattice photon is R8-5's generalized forward difference, D_j = iσ(k_j)e^{ik_j/2}, with a subluminal symbol d = |σ| (d′ ∈ [0, 1], R16-10's 𝒞_sub). The TT vertex is the canonical Maxwell stress T_ij = Ē_iĒ_j + B̄_iB̄_j of site-averaged fields, with averaging symbol e^{−ik/2}d′(|k|) (plain link averaging, cos(k/2), for the NN photon). Placed at R9-9's 09-14 points (h_xx at sites, h_xy at plaquette centres, `C5_R9-9_report.md:100`), this is vertex **VU**. It is local, and at q = 0 in the continuum it reduces to the helicity-2 pair amplitude (checked to 5e-14).
2. **The Maxwell vector pushes the graviton cone out, like Dirac, not like a scalar (checked).** Under VU, every subluminal photon law I tested with box b_γ ≥ 0.15 has Ξ_T2g > 0 and Ξ_Eg > 0 per vector. That is 54 laws, including R8-5's own photon, the NN photon and the R14-1-type G(1.4) photon:

   | photon law | Ξ_T2g (VU) | Ξ_Eg (VU) | μ_E (SF) |
   |---|---|---|---|
   | γG(1.4) (R14-1 shape) | +9.79e-2 | +1.20e-1 | +8.68e-3 |
   | R8-5's own photon R85(1, 2, 1) | +4.77e-2 | +6.13e-2 | +5.23e-3 |
   | NN (cos(k/2) averaging) | +1.44e-2 | +1.72e-2 | +5.39e-3 |
   | smallest (b_γ ≥ 0.15): γGw(0.15, 0.25) | +3.3e-4 | +3.1e-4 | — |

   The decomposition shows why. The electric part alone is boson-like (negative). The magnetic part and the E–B interference are positive and dominate (§3.3).
   - The expectation ("vector sign likely boson-like", `TESTS:6128`) fails for the Maxwell stress.
   - A "two scalars per vector" comparator (VS) does have the boson sign. So the sign comes from the vector's E–B structure, not from its statistics.
3. **At SM counts the vectors therefore add to the Dirac side (checked; search, not a proof).** The content is 4 scalars on one edge, 22.5 Dirac on D1 and 12 vectors. Two needs then clash under VU:
   - The T₂g row needs a photon with Ξ_γ,T2g ≤ 6.0e-4.
   - The Dirac birefringence (≥ +2.43e-3 per field over 60 D1 laws) must be paid by the vectors: Ξ_γ,Eg − Ξ_γ,T2g ≥ +4.5e-3.

   No sampled VU photon meets both. A 6-knob local solve under VU stopped at its cap with a T₂g residual of +1.65e-2 (§3.4).
4. **Under a second local placement (VM), an explicit SM-count zero exists (checked).** VM moves the B-part half a cell in z, off R9-9's h_xy (plaquette) position. Under VM, small-box photons have Ξ_γ,T2g < 0. The root at m = 0.01, re-solved at photon grid N = 96, is:
   - 4 real scalars on one edge, G_w(2.5943, 0.3276), U vertex;
   - 22.5 Dirac fields on D1(0.38483, r = 0.55963);
   - 12 vectors on γGw(0.25133, 1.0195).

   Results:
   - **Residuals.** Ξ_T2g = Ξ_Eg = μ_E = 0 to ≤ 3e-11. The same knobs at N = 128 leave 2.9e-5, against a per-content scale of 3e-2. Re-solving at N = 128 gives ≤ 6e-12, with knob shifts of 2e-6 (b_γ), 2.4e-4 (b_f) and 4.8e-3 (b_s).
   - **Count.** 3 continuous edge tunings (b_γ, b_f, b_s), one per spin edge; the Jacobian has rank 3.
   - **Light mass.** Re-solved at m = 0.001.
   - **Subluminal on every edge.** v_max: scalar 0.999998; Dirac ≤ 1 (Lemma V1); photon 1, attained in the box.
   - **μ_T2 = +0.106 is not zero.** It comes only from the 22.5 Wilson-Dirac fields. A 4-row solve did not find a zero.
5. **What decides it is a vertex datum.** VU and VM are both local Maxwell stresses. They differ only in where the magnetic part sits relative to the graviton's h_xy. VU is the placement R9-9's graviton uses; VM needs h_xy half a cell away (a different graviton placement, or a non-local half-shift of h). So the SM question on one cone turns on an O(q²) placement datum. This is R17-4's P-TTV₂, now for vectors.

**Against the FIXED readings (`TESTS:6124-6127`): worker reading OPEN.**
- **SM-LIFTED:** not met in the registered setting (VU, R9-9's placement); no root found. It is met on the letter only under VM. VM departs from the item's imported R13-5/R9-9 prescription, which is the ground on which the R16-13 referee read OPEN (`vR16-13:25`).
- **SM-CONFLICT:** not met. The VU obstruction is sampled (54 photon, 60 Dirac and 40 scalar laws plus one local solve), not a demonstration over the families. At b_γ = 0.1 the photon's sign is unresolved and Dirac's T₂g row turns negative (§3.3, §3.4).

---

## 1. Class, hypotheses, stipulations, exclusions (stated before any title)

**Content (`TESTS:6114`).** SM counts in the free-field limit:
- 12 massless vectors, 2 polarizations each, sharing one photon edge (gluons as 8 free copies; W and Z treated as massless at m ≤ 0.01);
- 22.5 four-component Dirac fields on one D1(b_f, r) edge;
- 4 real scalars on one edge family, G_w(b_s, w_s) (R14-3's family, which contains G(b)).

The common matter mass is m = 0.01, with a re-solve at 0.001. The vectors are massless.

**Scalar vertex: U** (R9-9's τ_ij = f_if_j, f = σσ′). M is excluded as non-local by Lemma M, refereed (`C5_R17-4_report.md:114-127`; `vR17-4:7`; `TESTS:6178`). This follows the item: "use the U-type or a local vertex" (`TESTS:6116`).

**Dirac vertex: V0** (R16-13's vielbein vertex, `C5_R16-13_report.md:84-88`), with the Wilson mass not coupled. It is local on D1 because s is continuous with s(π) = 0. It is confirmed conditionally with an ultralocal seagull (`vR16-13:5`).

**Photon law (stated).**
- R8-5/R9-9's generalized forward difference: D_j(k) = iσ(k_j)e^{ik_j/2}, σ(k) = sgn(k)·d(|k|).
- d is even, smooth and periodic, with d = |k| on the box |k| ≤ b_γ and d′ ∈ [0, 1]. This is R16-10's subclass 𝒞_sub (`C5_R16-10_report.md:66-67`); R16-10's superluminal stiffening is excluded (`TESTS:6116`).
- ω² = Σ_j d(k_j)². Gauss's law is σ·Ẽ = 0 in the half-shifted frame Ã_j = e^{−ik_j/2}A_j. That frame is continuum Maxwell with momentum vector σ(k). Its fields are antiperiodic, but the pair weights are invariant (proved, §3.2).

**Photon families.**
- γG(b): R14-1's G(b) as the photon. This is my reading of "the R14-1 subluminal photon edge"; R14-1 itself built no photon.
- γGw(b, w).
- R8-5's own photon R85(1, 2, G = 1).
- NN (d = 2|sin(k/2)|).
- Plateau laws with d′ = 1 → λ → 0.

**Vector TT vertex (stipulated; probe (a)).**
- **Form.** δH = ½h_ij(Ē_iĒ_j + B̄_iB̄_j). This is the canonical Maxwell stress, derived from √−g F² at linear order in a traceless h: both terms carry the same sign, and E_i means the conjugate momentum.
- **Averaging.** Site-averaged fields use the symbol a(k) = e^{−ik/2}c(k) with **c = d′(|k|)**. This is the NN link average cos(k/2) for the NN photon. c equals 1 in the box, c(π) = 0, and c is antiperiodic, so the stress kernel is local.
- **VU (registered placement).** T_xx at sites and T_xy at xy-plaquette centres, R9-9's "09-14 placement" (`C5_R9-9_report.md:100`). For axial q this gives:
  - E-part form factors c_xc_y;
  - B-part form factors c_xc_y·c_z(k₁)c_z(k₂).
- **VM (comparison; off R9-9's placement).**
  - T₂g: E_xE_y at the site (c_xc_y), and B_x averaged in y and B_y in x, so the B-product sits at the z-link midpoint.
  - E_g: E_x², E_y² on their own links, and B_x², B_y² at their plaquette centres.
  - Every B-product therefore sits at height z + ½. It carries the relative phase exp(i(k₁z + k₂z)/2), using representatives, which keeps the amplitude periodic.
  - Coupling it to R9-9's h_xy, which sits at height z, with that pure phase needs a non-local half-shift of h, or a graviton placed differently from R9-9's.
- **Not used.** c ≡ 1 (no averaging) is a half-lattice shift, the photon analogue of Lemma M, and is not local. The E1-type variant (form factors at the relative momentum) is not well-defined on the torus for the z factor; its numbers in `scan_photon_N48.out` are kept only as a record.

**Ward, seagull and placement.**
- **Ward requirement:** standard first-order W1 is assumed and not built for vectors, as for scalars and Dirac (`vR16-3`, `C5_R16-13_report.md:89`). No W2, standard or deformed.
- **Seagull:** ultralocal, so q- and ω-independent (`vR16-13:5`).
- **Gauge:** temporal/Coulomb (physical transverse modes); no Peierls charge coupling enters a free TT loop.

**Shear (SF, stipulated).** R9-2's universal strain flow, as in R16-13 (`C5_R16-13_report.md:90-97`):
- scalar: +ε/2 per mode;
- Dirac: −(N_c/2)E;
- vector: +ω/2 per polarization, so μ^γ = 2μ^s[ω]. This is polarization-blind, a stipulation.

ω is separable, so μ_T2^γ = 0 (proved: H_xy ≡ 0). The photon μ_E uses a regulator m_γ = 1e-3; it is unchanged at 1e-4 to all printed digits.

**Meaning of Ξ.** The bare-cone shift with q ∥ z, Ξ = ∂_{q²}Π + ∂_{ω²}Π. It is not the dressed split (`vR9-9`). Normalization is R9-9's for one real scalar: Π = −⟨Σ|amp|²E/(E² − ω²)⟩, with the same pair-creation convention for every species.

**Vacuum.** Supplied zero-point vacuum or filled sea, one loop. In the empty Fock vacuum every quantity here is 0.

**Round-16/17 rules (`TESTS:5039`, `:5695-5711`).**
- **Whole-zone v_max for every law, gauge fields included.** For any separable ω, |∇ω|² = Σ(σ_iσ′_i)²/Σσ_j² ≤ max σ′² (proved).
  - Every photon used: v_max = max d′ = 1, attained in the massless box (`gsym_vmax.out`).
  - R9-9's graviton symbol d(q) (c₁ = 1, c₂ = 2.5): d′ ∈ [2e-6, 1], so v_max = 1 (checked).
  - Matter edges: §3.5.
- **Frame-tied kernels:** none introduced.
- **Ward:** standard W1, assumed.
- **Counting basis:** per (spin, edge) class (§3.6).
- **Λ:** none proposed.
- **Control:** the continuum control is the same observable (the TT pair amplitude, and Ξ = 0 by covariance), §3.2.
- **Forks:** VU/VM are two examples, not exhaustive (VC, a cube-centre placement, is untested).
- **Changed hypothesis:** "scalar and Dirac loops only" is removed (`TESTS:6117`).

**Excluded:**
- the M scalar vertex;
- superluminal photons (R16-10's 7.35);
- pairing, including a photino partner;
- q off-axis;
- W2;
- two loops;
- non-free (interacting) gauge fields;
- massive W/Z longitudinal modes;
- dressed poles;
- the charged-matter cone rows (R16-2/R16-10), which the photon edge also enters.

## 2. Prior art (each counted once)

- **R16-13** (`vR16-13`: NOT CONFIRMED, OPEN). Theorem DT, the D1 signs and Lemma V1 are confirmed conditionally. The joint zero used the non-local M scalar. With one Higgs edge and SM counts the solves stalled on Dirac birefringence (`C5_R16-13_report.md:58-59,200`). Photon and gluon loops were not built (`:108`, `:280`).
- **R17-4** (`vR17-4`). Lemma M confirmed, so U or another local vertex is required; P-TTV₂ (the vertex extension is a datum); the bill is 8 + CC per class / 12 + CC per species for U+E1 (`vR17-4:13`).
- **R16-9** (OPEN, `TESTS:5668-5684`). The block split holds only for the truncated scalar-loop prescription.
- **R16-3** (REFUTED via U, `TESTS:6178`). The axis IBP identity.
- **R13-5.** The W1 pair stress and the stipulated vertex; its numbers are W1- and prescription-scoped (`TESTS:5447`).
- **R10-5 Lemma PD** (refereed, `vR10-5` item 3). In the SUSY-QM class 𝒮 a doubler-free box photon cannot be paired with a photino. So the "photino control" route to cancelling vector TT loops by pairing is closed in 𝒮.
- **R8-5 / R9-9 photon and graviton symbols.** D = d e^{iq/2}, with the 09-14 placement (`C5_R9-9_report.md:38,100`).
- **R16-10** (`TESTS:5890`). A stiffened photon is superluminal (v_max 7.35) and excluded here. On 𝒞_sub the photon symbol acts on the charge cones like a q²-correlated counterterm (`C5_R16-10_report.md:46`).
- **Grep.** I searched `agents/` and TESTS for "Maxwell stress", "vector TT", "photon TT", "gluon loop" and "E–B interference". The only hits are the open items naming the gap (R16-9's P-R16-9b, R16-13's `:280`). No vector TT vertex exists in the chain.

---

## 3. Results

### 3.1 Rechecks of archived runners (checked; `recheck.out`)

- **zz.py (R16-3) on G(1.4), m = 0.01.**
  - Ξ_M,T2g = −1.6892e-3, Ξ_M,Eg = −8.4891e-4, μ_E = +4.3384e-3. These equal R16-13 §3.1 and the referee (`vR16-13:13`).
  - The U values are −4.6291e-4 and −2.5354e-4.
- **NN at m = 1.** U,T2g −2.289166113e-4, U,Eg −6.883236561e-5, M,T2g −1.903007307e-3 and M,Eg −8.301856729e-4. All 10 digits equal R17-4 §3.1.
- **R16-13 root at the printed knobs.** Totals ≤ 1.4e-13, against 6e-14 reported; the difference is 10-digit knob rounding. The fermion part (+5.511e-3, +2.801e-3, −2.690e-2, μ_T2 −3.538e-5) equals the report.
- **D1(1.4, 0.3), m = 0.01.** (+5.4602e-3, +2.8292e-3, −2.9192e-2), equal to the referee's (+5.4601e-3, +2.8291e-3, −2.9185e-2) (`vR16-13:9`).
- **R16-13's two scalar edges under U** (the local vertex): G(b₁) (−6.33e-4, −3.66e-4) and G_w (−4.52e-4, −3.17e-4), against M's (−9.45e-4, −5.48e-4) and (−1.81e-3, −8.53e-4). The local vertex makes the scalar side weaker.

### 3.2 (a) The vector TT vertex: identity status and continuum checks

- **Continuum q = 0 amplitude (proved; checked).** Take σ = k and c = 1, with polarizations ε₁, ε₂ ⊥ k̂.
  - The pair matrix N = ½[ω e + X e X/ω] (X = [σ]_×) gives ε₁ᵀNε₂ = (ω/2)[e(ε₁, ε₂) − e(k̂×ε₁, k̂×ε₂)]. This is the helicity-2 (opposite-helicity) projection.
  - Equal-helicity pairs vanish, as the trace-free free-Maxwell stress requires.
  - Checked against the transverse-plane formula on 2000 random k: worst relative deviation 5.1e-14 (`calib.out`).
- **Continuum zero (proved, by covariance).** With a Lorentz-invariant regulator, Π_TT depends on q² − ω² only, so (∂_{q²} + ∂_{ω²})Π = 0. The lattice Ξ below is therefore measured against zero.
- **Representative invariance (proved).** Shifting one leg's k_z by 2π flips σ_z, c_z and the half-shifted field together. The pair matrix then goes N → NS_z, and Σ|amp|² = tr(P₁NP₂Nᵀ) is invariant. So VU is periodic, hence local. VM keeps periodicity through its representative phase.
- **No closed IBP identity was obtained (OPEN).** Unlike the scalar and Dirac cases (R16-3; DT), the vector vertex depends on k_z through the polarization projectors P(σ(k₁)), P(σ(k₂)) and the leg form factors c_z(k₁)c_z(k₂). The single-IBP route of Theorem T/DT does not close. Instead, α = ∂_{q²}Π is evaluated by R10-5's exact grid shifts with Richardson extrapolation, and β = −⟨Σ|amp|²/E³⟩ exactly.
- **Validation of the method (checked).**
  - On a real U scalar the same pipeline reproduces the closed form. G(1.4) at m = 0.3, N = 256 gives −4.51136e-4 against −4.51136e-4. At m = 0.1 it gives −4.61591e-4 against −4.61590e-4 (`calib.out`).
  - For the photon, an independent quadrature agrees with the grid shift: a symmetric pair (k ± q/2) with off-grid interpolation, q = 0.08 and 0.16. NN T₂g gives +1.44337e-2 (symmetric) against +1.44293e-2 (shift, N = 96). γG(1.4) gives +9.792e-2 against +9.791e-2 (T₂g) and +0.12022 against +0.12021 (E_g) (`symcheck.out`).
  - Convergence on γG(1.4) T₂g: +9.757e-2, +9.783e-2, +9.788e-2, +9.791e-2 at N = 32, 48, 64, 96.

### 3.3 (b) Signs and sizes per vector field (checked; `scan_photon2.out`, `scan_small.out`, `vm_check.out`, `vm_conv.out`)

**Decomposition** (γG(1.4), N = 64, symmetric pair; `symcheck.out`):

| part | Ξ_T2g | Ξ_Eg |
|---|---|---|
| E only | −1.19e-3 | −3.86e-3 |
| B only | +3.10e-2 | +3.42e-2 |
| full (with E–B interference) | +9.79e-2 | +1.20e-1 |

- The electric part alone is boson-like, the same sign as a G scalar. The E–B interference, which is what makes the continuum pair helicity-2, is positive and dominant.
- **Reading.** At the lattice edge, the B-part's extra form factors c_z(k₁)c_z(k₂) and the saturating σ_z unbalance the E/B cancellation that Lorentz invariance enforces in the continuum.

**VU sign scan (54 subluminal photon laws).**
- 38 laws: NN, R85(1, 2, 1), γG(b) for b from 0.1 to 3.1, γGw(b, w) for b ≥ 0.3 at N = 96, and plateau laws.
- 16 small-box laws: γGw(b, w), b ∈ {0.1, 0.15, 0.2, 0.3}, at N = 96.

Results:
- **Every law with b_γ ≥ 0.15 has Ξ_T2g > 0 and Ξ_Eg > 0.** The smallest is γGw(0.15, 0.25) (+3.3e-4, +3.1e-4). Over the 38-law scan the smallest is +3.31e-3 / +1.15e-2, both at γGw(0.3, 0.5).
- **Values grow with the box:** γG(2.8) gives +1.27 and γG(3.1) gives +4.69.
- **At b_γ = 0.1** (1.5 grid spacings at N = 96, unresolved), γGw(0.1, 0.25) gives (−2.8e-5, −2.7e-3) and γGw(0.1, 0.5) gives (+1.4e-4, −1.6e-3).

**VM.**
- Positive on every G-type, NN and R85 law.
- Negative T₂g on G_w laws with a small box or a narrow turn (b = 0.3 for every w; b = 0.8 at w = 0.25) and on the b = 0.5 plateau laws. The extreme case is γGw(0.3, 0.5): Ξ_T2g = −3.447e-3 / −3.455e-3 (N = 128, shifts (1,2) / (2,4)) and Ξ_Eg = −2.68e-2.
- The γGw(0.3, 1.0) values converge as −2.432e-3, −2.421e-3, −2.414e-3, −2.412e-3 at N = 48, 64, 96, 128.

**Shear (SF).**
- μ_E^γ ∈ [−8.1e-4, +3.17e-2] per vector over the 38 laws. It is positive on G-type photons and slightly negative for narrow early-flattening G_w.
- μ_T2^γ = 0.

**Comparator VS** (2 × U scalar on ω, not a Maxwell stress): −5.4e-4 to −1.4e-3 (T₂g), negative on every law. This is the boson-like sign the expectation assumed.

**Matter ranges at m = 0.01** (checked; `scan_dirac_scalar.out`, `scan_small.out`).
- **D1(b_f, r), 60 laws** (b_f ∈ [0.1, 1.55], r ∈ [0.02, 1/√3]):
  - Ξ_T2g ∈ [−2.0e-4, +5.70e-3]. It is negative only at b_f = 0.1 with r = 0.577; it is ≥ +1.0e-4 for b_f ≥ 0.15.
  - Ξ_Eg ∈ [−6.4e-3, +3.3e-3].
  - **Birefringence Ξ_T2g − Ξ_Eg ≥ +2.43e-3 in all 60.**
  - μ_E ∈ [−3.2e-2, +1.44e-2]; μ_T2 ∈ [−1.2e-4, +1.6e-2].
- **Scalars G_w(b, w), U vertex, 40 laws:**
  - Ξ_T2g ∈ [−6.80e-4, −8.2e-5];
  - Ξ_Eg ∈ [−4.05e-4, −1.39e-4];
  - Ξ_T2g − Ξ_Eg ≥ −2.9e-4;
  - μ_E ∈ [−4.8e-4, +1.38e-2].

### 3.4 (c) The SM-count solve

**VU (registered placement): no zero found (checked; search).**
- **The two necessary inequalities** (sampled ranges of §3.3):
  - **T₂g row.** 12Ξ_γ,T2g = −22.5Ξ_F,T2g − 4Ξ_s,T2g ≤ 22.5(2.0e-4) + 4(6.8e-4), so Ξ_γ,T2g ≤ 6.0e-4.
  - **Birefringence row** (T₂g − E_g). 12(Ξ_γ,Eg − Ξ_γ,T2g) = 22.5B_F + 4B_s ≥ 22.5(2.43e-3) − 4(2.9e-4), so Ξ_γ,Eg − Ξ_γ,T2g ≥ 4.46e-3.
- **No VU photon in §3.3 satisfies both.** Those with Ξ_T2g ≤ 6e-4 (b_γ ≤ 0.15, narrow w) have Ξ_Eg − Ξ_T2g ≤ 2.7e-4 or negative.
- **6-knob local solve.** `smsolve.py VU 64` (b_γ, w_γ, b_f, r, b_s, w_s), from (0.2, 1.0, 0.3, 0.55, 2.6, 0.33). It stopped at the nfev cap (18), not converged (`smsolve_VU_N64.out`).
  - End point: b_f at its lower bound 0.15; the photon turn shrunk to w_γ = 0.18, under-resolved at N = 64.
  - Totals: (Ξ_T2g, Ξ_Eg, μ_E) = (+1.65e-2, −2.4e-3, +4.4e-4), with the vectors' +1.53e-2 dominating T₂g.
- **Reading.** Under the registered placement the vectors deepen R16-13's Dirac-birefringence stall instead of offsetting it.
- **Scope.** Not a demonstration. The ranges are samples, the bounds are not enclosures, and the families are not exhausted. At b_γ = 0.1 the photon sign is unresolved and D1's T₂g row turns negative.

**VM (comparison placement): an explicit SM-count zero (checked; `smsolve_VM_N48.out`, `verify_VM.out`).**

| item | value |
|---|---|
| content | 4 real scalars, G_w(b_s, w_s), U; 22.5 Dirac, D1(b_f, r), V0; 12 vectors, γGw(b_γ, w_γ), VM; SF; m = 0.01 |
| 6-knob search (N = 48) | no knob at a bound; totals ≤ 1.3e-11 |
| root after 3-knob re-solve at N = 96 (w_γ, r, w_s frozen) | b_γ = 0.25133, w_γ = 1.01946, b_f = 0.38483, r = 0.55963, b_s = 2.59435, w_s = 0.32758 |
| totals at N = 96 | Ξ_T2g −5.3e-14, Ξ_Eg −1.7e-13, μ_E +2.9e-11 |
| totals at N = 128 (same knobs) | +2.9e-5, +2.9e-5, +2.9e-11 (photon grid; per-content scale 3e-2) |
| re-solved at N = 128 (`resolve128.out`) | b_γ = 0.251323, b_f = 0.384592, b_s = 2.589508 (shifts −2e-6, −2.4e-4, −4.8e-3 from N = 96); totals (+6.2e-12, +3.3e-12, −5.0e-12); μ_T2 +0.1062 |
| contributions (6-knob point) | 4 scalars (−2.49e-3, −1.53e-3, +3.78e-2); 22.5 Dirac (+3.50e-2, −3.40e-2, −3.59e-2); 12 vectors (−3.25e-2, +3.55e-2, −1.89e-3) |
| Jacobian (N = 64), 3×6 | singular values 2.40, 1.99, 0.108 (rank 3); det(b_γ, b_f, b_s) = −6.66e-3 |
| light mass | re-solved at m = 0.001: b_γ 0.25174, b_f 0.37834, b_s 2.56103, residual ≤ 1.2e-13 |
| **μ_T2 total** | **+0.106**, entirely Wilson-Dirac (scalars and separable photons give exactly 0) |
| 4-row solve (adding μ_T2 = 0), one start | ended at bounds (b_γ = b_f = 0.15, b_s = 3.0); residuals (−2.7e-2, +1.9e-3, −2.5e-2, +3.7e-2); **not found** (`smsolve4_VM_N48.out`) |

- **Mechanism (reading).**
  - The small-box VM photon carries negative T₂g and positive E_g. This cancels the Dirac birefringence.
  - The Higgs edge's large μ_E (+9.4e-3 per scalar, a wide box with a narrow turn) cancels the Dirac sea's μ_E.
- **Count.** 3 continuous edge tunings, one per spin edge, each held to the GW precision (~1e-13 relative, R16-3's comparator).

### 3.5 Whole-zone v_max at the VM root (checked; `verify_VM.out`, `gsym_vmax.out`)

- **Scalar G_w(2.594, 0.328):** max|σ′| = 1.000000000, no valley, v_max = 0.999998 at m = 0.01.
- **Dirac D1(0.3848, 0.5596):** r < 1/√3 (3.1% below), so v_max ≤ 1 by Lemma V1. Sampled v_max is 0.999967 (81³).
- **Photon γGw(0.2513, 1.0195):** d′ ∈ [0, 1], so v_max = 1, attained in the box. Note that the photon is box-exact only for |k_i| ≤ 0.25.
- **Graviton symbol:** v_max = 1.
- **Tails:** not computed.

### 3.6 (d) The bill update (reading; conditional bookkeeping)

- **The block split ends.** With vector and Dirac TT loops, the axial gravity rows depend on all three edges. The photon edge also sets the charged-matter cones (R16-10: the photon symbol acts as a q²-correlated counterterm, `C5_R16-10_report.md:46`). The Dirac edge sets the electron rows (R16-1/R16-2). So the gravity and charge blocks share knobs. R16-9's split held only for the truncated scalar prescription (`TESTS:5681`).
- **Counting basis:** per (spin, edge) class. One edge parameter is shared by every species on that edge.

| row (R13-8/R17-4 basis) | R17-4 (U+E1, refereed arithmetic) | this probe | status |
|---|---|---|---|
| charged-matter speeds | 3 / 7 | 3 / 7 | unchanged; now coupled to the gravity rows through the photon and Dirac edges |
| axis TT (E_g, T₂g) + μ_E | 2 shape + 1 non-shape | **VU:** still needs ≥ 1 non-shape knob (no shape zero found). **VM:** 3 shape tunings across the three edges, no non-shape knob | count unchanged (3 conditions) |
| off-axis TT | 1 (K₆; face2 ≡ T₂g holds for U scalars) | 1, or 2 if the face2 identity fails for vector/Dirac contributions (not computed; suggested) | vector and Dirac off-axis rows not computed |
| μ_T2 | 0 (V3 coupling) | **1**: 22.5 Wilson-Dirac fields give +0.106 at the VM root; only the Dirac edge (or Clifford-flat fermions, P-R16-13b) can fix it | new at SM counts |
| LV tadpole | 1 (never shape-zeroable for scalars) | 1; with Dirac seas (ρ < 0) shape-zeroing is no longer excluded by R17-4's positivity (not computed; suggested) | |
| CC | 1 | 1 | |
| **total** | 8 + CC / 12 + CC | **9 + CC per class / 13 + CC per species** (10/14 if the face2 identity fails) | conditional |

### 3.7 (e) Prices (named, not adopted)

- **P-R17-9a (vector vertex, stipulated).** The site-averaged Maxwell stress with c = d′, at the 09-14 placement (VU); an ultralocal seagull; standard W1 assumed and not built for vectors; SF for the vector shear (polarization-blind). Law data: source/action gate `AX:187`, dynamics downstream `AX:114-130`.
- **P-R17-9b (vector placement datum).** Where the B-part of T_ij sits relative to h_ij is an O(q²) vertex datum. It flips the small-box vector sign and decides between "no zero" (VU) and "SM zero" (VM). This extends R17-4's P-TTV₂ to vectors. Choosing VM means a graviton whose h_xy is not at R9-9's plaquette centres, or a non-local half-shift of h.
- **P-R17-9c (the VM root's bill).**
  - 3 edge tunings at ~1e-13;
  - a photon box of 0.25/a, a lattice-modified photon for |k| > 0.25/a, whose shape also re-enters the charge cones (not re-solved here);
  - a Dirac box of 0.38 with r 3.1% below the cap;
  - μ_T2 = +0.106 left unfixed: +1 Dirac-edge condition (not found in one search) or P-R16-13b.
- **P-R17-9d (the in-setting route).** Under VU at SM counts, the axial cone plus the shear needs a non-shape knob (counterterm, R16-9's P-R16-9a), pairing (P46), or the empty Fock vacuum. For vectors, photino pairing is closed in 𝒮 by R10-5 Lemma PD (`C5_R10-5_referee_verdict.md:7`).
- **No axiom text changes.** No sizes at a = ℓ_P are quoted (`AX:189-190`).

---

## 4. Against the FIXED readings (`TESTS:6124-6127`)

**Worker reading: OPEN.**
- **SM-LIFTED: not met in the registered setting.**
  - The item imports R13-5's prescription, and with it R9-9's vertex placement (`TESTS:6113`; `C5_R9-9_report.md:100`). Under that placement (VU) no SM-count zero was found.
  - Under VM there is an explicit content meeting the clause's letter: SM counts, one Higgs edge, every edge subluminal, E_g = T₂g = μ_E = 0 at m = 0.01 (and 0.001), checked, count 3.
  - But VM's B-part is off R9-9's h_xy position. By the precedent of `vR16-13:25` (a root outside the imported local-stress prescription does not lift), I do not read it as SM-LIFTED. The referee should rule on whether VM is in-setting.
  - If the referee rules VM in-setting, the reading becomes SM-LIFTED with the caveats μ_T2 ≠ 0 and the vertex-placement price.
- **SM-CONFLICT: not met.** The VU obstruction (§3.4) rests on sampled ranges over 54 + 60 + 40 laws and one local solve. It is not an enclosure over the stated families, and the b_γ ≈ 0.1 corner is unresolved.
- **Expectation** ("OPEN; vector sign likely boson-like … could offset the Dirac birefringence", `TESTS:6128`):
  - OPEN: met.
  - The sign premise is false for the Maxwell stress under both local placements on G-type, NN and R8-5 photons. Only the electric part, or the VS comparator, is boson-like.
  - The offset of the Dirac birefringence does happen, but only via small-box photons under VM, through negative T₂g with positive E_g. It does not come from a boson sign.
- **Removed hypothesis** ("scalar and Dirac loops only"). It matters, but in the opposite direction from the expectation: under the registered placement the vectors add to the Dirac side.

## 5. Strong-word check

- **"Proved"** is used only for:
  - the continuum helicity-2 reduction;
  - the covariance argument Ξ = 0 in the continuum;
  - representative invariance (locality) of VU;
  - μ_T2^γ = 0 for separable ω;
  - |∇ω| ≤ max d′.
- **"Checked"** is used for every number. Sources: grid shift with Richardson (N = 32–128); an independent symmetric-pair quadrature; calibration of the pipeline to the scalar closed form; GL quadrature for Dirac; Laplace moments for scalars; re-solves at N = 96 and m = 0.001.
- **"Every / all".** "Every law with b_γ ≥ 0.15" (VU sign) and "all 60" (Dirac birefringence) are statements about my sampled laws, not theorems.
- **"No zero found"** means local least squares from the stated starts plus the sampled-range inequality. No global search and no certified bound.
- **Not claimed:**
  - a vector IBP identity;
  - any W2;
  - off-axis rows for vectors or Dirac;
  - the tadpole with fermions;
  - interacting gauge fields;
  - W/Z longitudinal modes;
  - the joint charge-cone rows;
  - uniqueness of the VM root;
  - SM-CONFLICT.

## 6. For the referee

1. **The vector vertex.** The canonical-quantization pair amplitude N = ½[√(ω₁ω₂)C₁eC₂ + X₁ᵀC̃₁eC̃₂X₂/√(ω₁ω₂)] (both terms with the same sign), the site-averaging symbol c = d′, and representative invariance. Is VU the right reading of "Peierls/Maxwell stress plus R13-5's prescription"?
2. **Whether VM is in-setting.** VM is a local stress, but its B-part sits at z + ½, off R9-9's h_xy plaquette position. This decides SM-LIFTED against OPEN.
3. **The photon α.** The E–B interference dominates (§3.3). I checked α against the scalar closed form through the same pipeline, and against an independent symmetric-pair quadrature, but not against an analytic identity.
4. **The VM root.** Rerun it independently, especially the photon at N ≥ 128. My N = 128 re-solve converged (≤ 6e-12), but only N = 48/64/96/128 grids of one method were used for the root.
5. **The VU inequality argument (§3.4).** Whether an enclosure of min Ξ_γ,T2g and max(Ξ_γ,Eg − Ξ_γ,T2g) over the photon family is reachable; this would make it a CONFLICT for VU. Also the b_γ → 0 corner.

## 7. Files (`S/scripts/`)

- **Copied unmodified** (from `P/scripts/C5/R16-13/`): `zz.py`, `dfam.py`, `dirac.py`, `sublum.py`, `content3.py`, `content4.py`, `r161_laws.py`.
- `recheck.{py,out}`: archived-runner rechecks.
- `photon.py`: photon laws, the VU and VM pair weights, grid-shift Ξ, the scalar-pipeline twin, and the continuum check.
- `calib.{py,out}`: continuum amplitude, scalar-pipeline calibration, photon convergence.
- `symcheck.{py,out}`: independent symmetric-pair quadrature, and the E/B decomposition.
- `scan_photon.py` → `scan_photon_N48.out`: first scan, including the discarded E1 variant.
- `scan_photon2.{py,out}`: 38-law VU/VM/VS/μ_E scan.
- `scan_small.{py,out}`: small-box photons and D1 corners.
- `vm_check.{py,out}`, `vm_conv.out`: VM values and convergence.
- `scan_dirac_scalar.{py,out}`, `scan_D1.npy`, `scan_GwU.npy`: matter ranges.
- `smsolve.py` → `smsolve_VM_N48.out`, `smroot_VM_N48.npy`; `smsolve_VU_N64.out`, `smroot_VU_N64.npy` (VU end point, not a root).
- `resolve128.{py,out}`, `verified_VM_N128.npy`: the VM root re-solved at photon grid N = 128.
- `smsolve4.py` → `smsolve4_VM_N48.out`.
- `smsolve_lib.py`; `verify_root.py` → `verify_VM.out`, `verified_VM.npy`.
- `gsym_vmax.{py,out}`: gauge-symbol v_max.
