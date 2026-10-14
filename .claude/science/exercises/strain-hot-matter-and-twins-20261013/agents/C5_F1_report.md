# C5 F1 report: the root's own SF-strained QED law and its hot-matter strain channel

- **Worker:** Claude Opus 5.5 probe (same model family as the supervisor and every C5 worker). Unrefereed. Run 2026-10-13, 12:11Z to 13:10Z. No repository file was edited. Nothing was downloaded. Every run used OMP_NUM_THREADS=2, ran one at a time, and took under 6 min. After the coordinator's memory note, every run stayed under 1.2 GB resident (k_z-slab chunking). No process of mine is still running.
- **Item:** `TESTS:9152-9186`. FIXED readings at `:9177-9181`; expectation at `:9182-9186`.
- **Paths.**
  - `P/` = `.claude/science/exercises/gravity-current-state-20261009/`; `AX` = `docs/MINIMAL_AXIOMS_2026-06-29.md`.
  - `rX` / `vX` = `P/agents/C5_X_report.md` / `..._referee_verdict.md`.
  - `S/` = `scratchpad/C5/F1/scripts/`. Unmodified archive copies are in `scratchpad/C5/F1/arch/`: `dirac.py`, `sublum.py`, `dfam.py` and `zz.py` (from `P/scripts/C5/R18-5`), and `r1934_lib.py` (from `P/scripts/C5/R19-34`).
  - `F2` = `scratchpad/C5/F2/F2_report.md`: the parallel worker, unrefereed, finished during this run.
- **Labels.** proved (a complete short argument, unrefereed) / checked (numerics run here) / suggested / reading / comparator. RECALLED means from memory.
- **Read.**
  - `AX` in full; `TESTS:9146-9207`.
  - `rR19-34` and `vR19-34` in full, with `r1934_lib.py`, `r1934_root.py/.out` and `r1934_sizes.py/.out`.
  - `rR19-31:1-110,245-265` and `vR19-31`.
  - `rR19-15:100-160` (Lemma H); `rR19-35` in full (Lemma R1 and the SF definitions, H4).
  - `rR16-13:1-140`; `rR9-2:215-232`; `rR18-9:30-90` and `vR18-9:1-12`; `rR18-5:1-130`.
  - `rR19-21:170-195,230-245`; `rR17-12` (VW, grep).
  - `PRICE_NOTE:1-30,600,655-690`.
  - Archived `dirac.py`, `sublum.py`, `lib9.py` and `dfam.py:1-40`.
  - `F2` in full.

## 0. Plain words, and the reading

**What was built (proved construction; checked).**
- The root's registered strain rule is SF: each band's momenta are moved by that band's own flow, Φ_t = the time-1 map of v = (t/2)·diag(1, −1, 0)·∇(E²/2) (`rR19-15:127-138`; `rR9-2:221-226`). Until now SF had been applied only to free-band energies.
- **The interacting law.**
  - The Dirac operator at strain t is D_t(k) = D(Φ^F_t(k)): the same matrix, evaluated at the flowed momentum. Its generator at t → 0 is UD (`rR18-5:53`).
  - The photon is Maxwell in frame components with flowed derivative symbols, d_{t,j}(q) = d(φ^γ_j(q_j)).
  - The coupling is minimal coupling of D_t with respect to the strained photon's gauge symmetry. It uses R19-34's divided-difference links along axis-ordered paths, averaged over the six orderings ("Psym").
  - Psym is the only choice in that family that is both cubic-covariant and hermitian (proved, §1). The Ward identity holds at every t, and the gauge parameter drops out of the P = 0 mass (proved; inputs checked to 1e-15).
  - The law is smooth on the torus (proved). At t = 0 it is exactly R19-34's law: δm = +0.041858390 e², all digits.
  - It reproduces the archived free shear rows. Dirac per field: −1.709406e-2 against −1.709412e-2. Photon per vector: +2.850877e-2 against +2.850892e-2.

**The result (checked; converged to about 1e-7).**
- On the R18-9 root, D1(0.909103708, 0.555604226) with Gph(2.9435), the additive-mass E_g strain Hessian under SF is:
  - **∂²_t δm = +2.42401e-2 e²** in SF units;
  - **+0.09696 e²** in R19-34's H-cov units (h = −t/2, ×4).
  - That is 2.4 times R19-34's magnitude, **with the opposite sign**. R19-34's H-cov value was −0.04047 e².
- **Every branch the root leaves open gives the same value.**

  | branch | Hessian (e², SF units) |
  |---|---|
  | Dirac flow at m = 0 instead of the rows' m = 0.01 | +2.42611e-2 |
  | single path orderings (non-hermitian; sensitivity probe only) | +2.42359e-2 to +2.42423e-2 |
  | the 0⁺ root | +2.45350e-2 |

- **There is no tuning knob inside SF.** The Wilson term is strained by the band's own flow, so R19-34's κ* placement zero has no counterpart in the registered law (proved, by construction).

**Why it is nonzero (structural account; proved and checked).**
- **Flowing alike gives an exact relabelling.** If the photon and the fermion were moved by one common separable flow, the strained loop integrand would be the unstrained one at relabelled momenta (proved). Then the Hessian reduces to a Jacobian (Liouville) term.
  - Checked: −2.26763e-3 from the finite difference against −2.26759e-3 from the Jacobian formula.
- **That term would vanish only for a volume-preserving flow.** No nontrivial separable E_g flow on the lattice torus preserves volume (proved). In the continuum, linear flows do preserve volume, and there the identity forces zero.
- **The root breaks the identity twice.**
  - The two flows differ. The photon is stretched like the continuum out to |q| = 2.94, but the Dirac flow bends beyond its box edge at 0.91, where the whole Wilson term lives. This is the dominant effect.
  - The Dirac flow is non-separable.
- **Decomposition:**
  - photon strained alone: +2.539e-2;
  - fermion strained alone: +1.256e-2;
  - cross term: −1.371e-2;
  - common photon flow: −2.27e-3; common fermion flow: +2.08e-3.
  - The tadpole carries +1.80e-2 of the total.

**Sizes (canonical reading, conditional; SM mapping an ESTIMATE, as R19-34).**
- **Sign.** With R19-34's sign convention (⟨ψ̄ψ⟩ > 0 relative to W), SF gives the **massive** sign, where H-cov gave the tachyonic one.
- **History:** m_g²/H² = +4.9e13 (150 GeV), +7.6e13 (100 GeV), +1.1e14 (50 GeV), +6.3e14 (10 GeV), +1.2e16 (1 GeV).
- **Today, |m_g| (nucleons):**
  - IGM: 1.0e-24 eV;
  - mean Sun: 1.8e-9 eV;
  - Earth: 3.6e-9 eV;
  - Sun core: 1.9e-8 eV.
- **Universal coefficient (F2's):** μ_ρ = 2.42e-21 eV² m³/kg.
- **Against F2's table:**
  - **Earth crossing (GW170817 from below the horizon): μ_ρ ≤ 1.5e-29, exceeded by 1.6e8.** This row is checked by F2, holds in either sign, and is the binding row.
  - Detector on the ground: about 2e8.
  - Binary pulsar: 1.2e22 (suggested).
  - PTA: about 3e2 (suggested, massive sign).
  - Galaxy+IGM LVK column: passes (9e-3).
  - Hot era: **no observational bound for the massive sign** (F2 row 10). In the other sign branch the tensor modes grow by about 3e9 e-folds, against a limit of 66-95 (F2 row 9).

**Subtractions (d).**
- **P-R19-34a, a strain-covariant critical mass** (named, not adopted: `PRICE_NOTE:679`; `rR19-34:177`).
  - It removes the channel exactly, by construction.
  - It also removes the matter-side rest-mass–shear coupling, about 0.0121 e²/a per unit t².
  - Neither is an observed effect, so nothing observed is removed (comparator).
- **P-R19-31b, ψ̄ψ as an (S_loc) background** (named, not adopted). It would stop the cross term from gravitating (suggested; count once with R19-31). It leaves the rest-mass–shear coupling in the law.
- **(S_loc) as registered** does not list ψ̄ψ (`rR19-21:45,178-179`).
- **(S\*), (Σ), (S) and P-Tad** are vacuum or lowest-state clauses. None touches a state-dependent ⟨ψ̄ψ⟩ channel (reading).

**Reading (worker): SF-HAZARD on the registered law; SF-COVERED with P-R19-34a.**
- The hazard rests on today's matter rows from F2 (Earth crossing), not on the hot era: for SF's computed sign, "|m_g| < H" is not an observational line.
- Dependencies:
  - F2 is unrefereed;
  - the canonical TT-pole bridge is conditional (`PRICE_NOTE:22`);
  - the SM mapping is an estimate;
  - two non-registered freedoms are named but not computed (§1, items 4-5).

## 1. Class, hypotheses, and every choice the root does not fix (stated before any title)

**Arena and conventions.**
- Z³ × ℝ, one loop, U(1), Euclidean, external P = 0.
- Critical mass fixed at t = 0 (as R19-34); the propagator mass is m = 0.
- Feynman gauge, with the gauge parameter handled in §3.1.
- Per e². E_g strain h = diag(1, −1, 0).
- SF units t: v = (t/2)h·p, and Φ_t is the time-1 map. These are exactly the archived rows' units (checked, §3.1).
- R19-34's H-cov h relates as t = −2h on soft modes (`rR19-31` §1), so Hess_h = 4·Hess_t.

**Edges.**
- Dirac: D1(b_f, r) (`P/scripts/C5/R18-5/dirac.py:24-49`):
  - R18-9 refined root (0.909103708, 0.555604226) (`vR18-9` item 2);
  - 0⁺ root (0.915438682, 0.568280847) (`rR19-11:167`).
- Photon: Gph(2.9435) = SymG(2.9435).h (`r1934_lib.py:113-119`).

**The registered law (`TESTS:9161-9165`) and how it is realized here.**
- **Dirac.**
  - D_t(k) = Σ_j iγ_j s([Φ^F_t k]_j) + m + Σ_j W([Φ^F_t k]_j), with the flow taken from p = ∇(E²/2) of the 4-component band.
  - Its spectrum is E∘Φ^F_t, which is SF's band energy at every order. Its t → 0 generator is UD (`rR18-5:53`).
  - The flow keeps k_z fixed, preserves the octant [0, π]³, the coordinate planes and the axes, and is odd and reflection-covariant (proved: p_j vanishes at k_j ∈ {0, π}).
- **Photon.**
  - Maxwell in frame components, with d_j → d_{t,j}(q) = d(φ^γ_j(q_j)) and p^γ_j = d d′. The flow is separable.
  - The Feynman propagator is δ_μν/(Q₀² + Σ_j d_{t,j}² + λ²), with λ = 0.
  - The first-order generator of d_{t,j}² is d_j²d′_j², which is VW's 𝔐₁ E_g weight w_jj = σ′(k_j)² (`rR17-12:158`) (suggested, by inspection).
- **Vertices.**
  - Generalized links with divided differences by d_{t,j}: the R8-5/R13-7/R19-34 convention (`r1934_lib.py:7`).
  - For a non-separable D_t, a hop needs a path. On axis-ordered paths the momentum-space vertex is a telescoping divided difference across cube edges. Psym averages the six orderings:
    - V_x(0, q) = [2Δ_x(0) + Δ_x(y) + Δ_x(z) + 2Δ_x(yz)]/(6 d_{t,x});
    - Δ_x(B) = D_t(B + q_x e_x) − D_t(B);
    - the y and z vertices are cyclic.
  - **Psym is unique (proved).** Proper cubic rotations act on the six orderings through all of S₃, simply transitively, so covariance forces uniform weights. A single ordering σ ≠ σ^rev breaks hermiticity, because a hop and its conjugate would carry different paths.
  - **The diagonal seagull at (q, −q) is path-independent (proved).** The starting phases cancel: T_jj = [D(q_je_j) + D(−q_je_j) − 2D(0)]/(2d_{t,j}²).

**Choices carried as branches.**
1. **The mass in the Dirac flow:** the rows' m = 0.01 (B1, main) or the critical m = 0 (B2).
2. **The path family:** Psym, the only admissible member. Single orderings are run as a non-hermitian sensitivity probe (B3).
3. **The root:** R18-9, or the 0⁺ root.
4. **The operator lift:** D∘Φ (U = 1). A k-dependent unitary conjugation U_t(k) = 1 + O(t²) keeps the SF spectrum and UD. **Not computed.** No registered text supplies one, and for a uniform symmetric strain the vielbein carries no rotation (reading).
5. **Path families other than axis-ordered** (staircase or straight-line Wilson lines). **Not computed.** They have no closed momentum form; the straight-line one is non-periodic.
6. **Controls, not branches:** photon unstrained; fermion unstrained; K1 (fermion on the photon's flow); K2 (photon on the fermion's flow).

**Formula (proved; checked against explicit 4×4 γ-matrices).**
- With V_j(0, q) = iγ·a_j + b_j and V_j(q, 0) = iγ·a′_j + b′_j:

  δm/e² = ⟨Σ_j W(φ^F_j(q_j))/d_{t,j}²/(2Ω)⟩ + ⟨[M + Σ_j((a_j·a′_j − b_jb′_j)M − b_j(a′_j·c) − b′_j(a_j·c))]/(2EΩ(E + Ω))⟩

  - c and M are D_t(q)'s components, E² = c² + M², and Ω² = Σ d_{t,j}².
  - Psym has a′ = a and b′ = b. At t = 0 the formula reduces to R19-34's (`r1934_lib.py:1-16`, docstring).
- **Quadrature:** R19-34's composite Gauss–Legendre on [0, π]³ (`r1934_lib.py:24-48`), with extra panels in the photon edge [2.9435, π]. The integrand is even in each q_j (proved).
- **Hessian:** dm(−t) = dm(t) exactly by C₂ about [110] (proved; checked to all digits, `f1_timing.out:1-2`). So Hess = 2[dm(d) − dm(0)]/d², Richardson over d and 2d.

**Excluded:** two loops; non-abelian vertices beyond C_F; Yukawa and W/Z loops; T₂g; the multiplicative (m-linear) channel under SF; a chiral SM edge (the "22.5 Dirac" convention is taken as given).

## 2. Prior art (counted once)

- **R19-34 + vR19-34.**
  - The H-cov law, its −0.04047 e², the κ* = 0.1884 placement zero, the sizes mapping and P-R19-34a.
  - vR19-34 item 4 (the referee's OPEN, because SF had not been built) is the reason for this item.
  - New here: the SF law itself and its value.
- **R19-31 + vR19-31:** the channel, the t = −2h normalization and P-R19-31b.
- **R19-15 Lemma H** (`rR19-15:127-138`): the SF flow and the Liouville form, reused for the free-row checks and for §3.2's Jacobian identity.
- **R19-35:** H4 and Lemma R1 (`rR19-35:19,40`). Its photon VW-versus-band remark (`:56`) does not enter, because the Feynman-gauge loop uses only the propagator.
- **R16-13 / R9-2:** the SF definition and the non-separable Dirac μ formulas (`rR16-13:93-96`, `dirac.py:12-14`).
- **R18-5:** UD as SF's generator (`rR18-5:53`).
- **R18-9 and R19-11:** the roots.
- **F2:** the bound table (worker, unrefereed).
- **Comparators (RECALLED):**
  - the continuum relabelling Ward identity;
  - Wilson additive mass renormalization;
  - the anisotropy dependence of the critical mass in lattice QCD;
  - local Lorentz invariance of matter (no anisotropic rest-mass shift).

## 3. Results

### 3.1 (a) Construction checks

| check | result | source |
|---|---|---|
| t = 0 equals R19-34's law | Psym and single orderings: +0.041858396 (n = 6) and +0.041858390 (n = 8), to all printed digits of `r1934_root.out:2-4` | `f1_validate.out:2-4`; `f1_root_conv.out:2-3` |
| Ward identity Σ_j d_{t,j}V_j(0, q) = D_t(q) − D_t(0) at t = 0.3, 2000 points | 4.4e-16 (scale 1.4) | `f1_validate.out:6` |
| D_t odd in c and even in M under q → −q | 8.9e-16 | `f1_validate.out:7` |
| non-separability present | the off-diagonal vertex reaches \|a_xy\| = 4.5e-3 at t = 0.3 | `f1_validate.out:8` |
| reduced formula against explicit 4×4 Euclidean γ-matrices, Q₀ by quadrature, general vertex | diff ≤ 1.4e-17 at 10 points, including off-diagonal vertices | `f1_validate.out:10-14`; `f1_validate2.out:2-6` |
| free Dirac row: e″(0) of −2⟨E∘Φ^F_t⟩, m = 0.01 | −1.7094063e-2 against the archived −1.709412e-2 (3e-6 relative) | `f1_validate.out:16` |
| free photon row: e″(0) of ⟨ω∘Φ^γ_t⟩, regulator 1e-3 | +2.850877e-2 at 690 nodes against +2.8508917e-2 (5e-6 relative). It converges slowly because the photon flow's Lipschitz constant is about 15 in its 0.198-wide edge, so d = 0.02 is outside the asymptotic regime | `f1_validate2.out:8-13` |
| evenness dm(−t) = dm(t) | identical to all 13 digits | `f1_timing.out:1-2` |

- **Gauge parameter (proved; inputs checked).**
  - In covariant gauge the ξ-dependent part of the P = 0 mass is (1 − ξ)∫[(d·V)S(d·V) − d_jd_kT_jk]/(Q²)².
  - The one-photon Ward identity gives (d·V)S(d·V) = S⁻¹(Q), because D_t(0) = 0 at the critical point (Φ_t(0) = 0).
  - For the two-photon term, the generalized links give d_j(q)d_k(−q)T_jk(0; q, −q) = ½[S⁻¹(Q) + S⁻¹(−Q)], whatever the path (proved: the phases cancel).
  - The mass parts are M_t(q) − ½[M_t(q) + M_t(−q)] = 0, because M_t is even.
  - Both inputs are checked to 1e-15 above.
- **Locality (proved; checked).**
  - D1's symbols and the Gph symbol are C^∞ (Gevrey sstep), and Φ_t is the flow of a C^∞ periodic field. So D_t and d_{t,j}² are C^∞ on the torus, and their hoppings decay faster than any power.
  - FFT tails on a 96³ grid (`f1_locality.out:1-4,6-9`): at t = 0.2, ten times the finite-difference steps, the tails are of the t = 0 size for D_t. The contracted photon axis's tail at |x| ≥ 31 grows from 1.2e-3 to 9.8e-3. That growth comes from its 0.198-wide edge being squeezed, and it is O(t).
  - **Side observation (checked; pre-existing, not from SF; outside F1).** The root photon's odd gauge symbol d jumps at the zone face (d(π) = 3.04), so its gauge-transformation kernel has a 1/|x| tail (`f1_locality.out:5`). Only d² enters at P = 0, as R19-34 noted (`r1934_lib.py:16`).

### 3.2 (b) The Hessian per branch, and the structural account

| branch / control (R18-9 root unless stated) | dm/e² | ∂²_tδm/e² (SF) | ×4 (H-cov units) | source |
|---|---|---|---|---|
| **B1 main**, 156 / 240 / 344 nodes, d = 0.003 | +0.041858390 | **+2.423855e-2 / +2.424027e-2 / +2.424013e-2** | +0.09696 | `f1_root_conv.out:2-3`; `f1_root_conv2.out:2` |
| B1, 344 nodes, d = 0.0015 | | +2.424011e-2 | | `f1_root_conv2.out:3` |
| B1 parts (240 nodes) | tadpole +0.018085, exchange +0.023773 | tadpole **+1.8022e-2**, exchange +6.219e-3 | | `f1_branches.out:3` |
| **B2** (Dirac flow at m = 0) | +0.041858390 | **+2.426109e-2** | +0.09704 | `f1_branches.out:4` |
| **B3** single orderings (156 nodes; Psym is +2.423855e-2 there) | +0.041858391 | **+2.42359e-2 to +2.42423e-2**; gradient ≤ 1e-11 | | `f1_orders.out:2-7` |
| **0⁺ root**, B1 | +0.042294398 | **+2.453499e-2** | +0.09814 | `f1_branches.out:5` |
| control: photon unstrained | | +1.25595e-2 | | `f1_controls.out:2` |
| control: fermion unstrained | | +2.53875e-2 | | `f1_controls.out:3` |
| control K1: both on the photon's flow (separable) | | −2.26763e-3 | | `f1_controls.out:4` |
| K1 from the Jacobian formula ⟨F₀ j″⟩ (unstrained integrand only) | | −2.26759e-3 | | `f1_controls.out:6` |
| control K2: both on the fermion's flow | | +2.07664e-3 | | `f1_controls.out:5` |
| comparator: R19-34's H-cov | | −1.0119e-2 | −0.04047 | `r1934_root.out:2-4` |

- **Convergence (checked).** The grid changes from 240 to 344 nodes and the step changes from 0.003 to 0.0015 move B1 by ≤ 1.6e-7.
- **Branches.** Every branch is ≥ 2.4e-2, about 24 times the 1e-3 threshold. They agree to 1.3% across the two roots and to 0.1% across B2. Psym and the single orderings differ by ≤ 4e-6.

**Lemma (relabelling; proved).**
- **Hypotheses:** a common flow that is separable (Φ_t(q)_j = φ_j(q_j), φ_j(0) = 0, odd), and the Psym vertex.
- **Then:**
  - every cube corner of q maps to the corresponding corner of Φ_t(q);
  - every divided-difference denominator d_j(φ_j(q_j)) is the unstrained one at Φ_t(q);
  - so F_t(q) = F₀(Φ_t q) pointwise.
- **Consequences:**
  - δm(t) = ⟨F₀ J_t⟩, where J_t is the transported density.
  - Per axis, j_t = 1 − tu′ + (t²/2)(u′² + uu″), with u = ±½p^γ.
  - δm″(0) = −⟨(div v)(v·∇F₀)⟩ (Lemma H's IBP).
- **Checked:** finite difference against the formula, 4e-8 apart (`f1_controls.out:4,6`).

**Lemma (no volume-preserving E_g flow; proved).**
- For separable v = (u(k_x), −u(k_y), 0), div v ≡ 0 forces u′ to be constant.
- A periodic u with constant u′ is u ≡ 0.
- So on the lattice, flowing alike never forces the Hessian to zero. In the continuum, with linear flows and a rotation-invariant regulator, the identity does force zero.

**What breaks the identity at the root (checked).**
1. **The Jacobian term** that every lattice E_g flow leaves: K1 = −2.3e-3, K2 = +2.1e-3, about 10% of B1.
2. **The mismatch between the photon and Dirac flows**, which is dominant.
   - The photon's p^γ = q is linear out to 2.9435, so the photon is stretched like the continuum almost everywhere.
   - The Dirac p = ss′ + MW′ is linear only inside the box |k_j| ≤ 0.909. All of W lives outside it.
   - Second-order split: H_FF = +1.256e-2, H_γγ = +2.539e-2, 2H_Fγ = −1.371e-2. The cross term cancels only 36% of the sum.
   - It shows up mainly in the tadpole, W(φ^F(q_j))/d(φ^γ(q_j))². Its numerator rides the slow Dirac flow and its denominator the near-linear photon flow.
3. **The non-separability of the Dirac flow:** cube corners are not mapped to corners. Measured through the ordering spread, it is small (≤ 4e-6).

**Against H-cov.** H-cov rescales every symbol alike, W/ℓ included. That is a "common flow" for the photon and the Dirac kinetic term, with only the Wilson placement κ free. SF instead drags W with the Dirac band's own flow. The SF value (+0.097 in h units) lies outside the whole κ family of R19-34 (+0.013 at κ = 0 down to −0.055) (comparison of checked numbers). So vR19-34's point that the strain law decides the result is confirmed, and the registered law gives a nonzero value with no tuning datum.

### 3.3 (c) Sizes (`f1_sizes.out`, `f1_envscale.out`; canonical reading conditional; SM mapping an ESTIMATE, copied from `r1934_sizes.py:1-14`)

**Mapping, as stated.**
- m_g²a² = 16π μ_SF (`PRICE_NOTE:22`, conditional).
- μ_SF = Σ_species ⟨ψ̄ψ⟩_state a³ × (coupling) × ∂²_tδm/e².
  - Quarks t, b, c: C_F g_s² with g_s² ≈ 0.3.
  - Electrons: e² ≈ 0.1.
  - Nucleons: σ-term weight of 13 light-quark units.
- In R19-34's notation this is c_h/4 with c_h = 4·Hess_t (`rR19-31` §1).
- Bound line |m_g| < H, as in R19-21/31/34. F2's table is used for the observational reading.

| | 150 GeV | 100 GeV | 50 GeV | 10 GeV | 1 GeV |
|---|---|---|---|---|---|
| m_g²/H², SF B1 (`f1_sizes.out:17-21`) | +4.90e13 | +7.55e13 | +1.11e14 | +6.26e14 | +1.15e16 |
| m_g²/H², H-cov control (`:2-6`) | −2.05e13 | −3.15e13 | −4.65e13 | −2.61e14 | −4.80e15 |

- **Down to 1 MeV (scaled arithmetic).** F2's extended H-cov history runs from −2.3e13 to −1.5e18 at 1 MeV (`F2:204`), partial below T_QCD. Multiplied by −2.396 it gives about +5.5e13 to +3.6e18.
- **Today** (`f1_sizes.out:22-29`):

  | environment | electrons | nucleons |
  |---|---|---|
  | IGM | 1.4e-25 eV | 1.0e-24 eV |
  | mean Sun | 2.5e-10 eV | 1.8e-9 eV |
  | Earth | 5.0e-10 eV | **3.6e-9 eV** |
  | Sun core | 2.6e-9 eV | 1.9e-8 eV |

- **Sign.** With R19-34's convention (m_f > 0 relative to W, so ⟨ψ̄ψ⟩ > 0), c_h > 0 gives **m_g² > 0, the massive sign**. The other sign branch is tachyonic, with the same magnitudes (count once with `rR19-34:151`).
- **Against F2's environment table** (`f1_envscale.out:1-7`; μ_ρ = 2.42e-21 eV² m³/kg, linear in |c_h| from F2's placeholder 1.012e-21):

  | F2 row | bound on μ_ρ | SF ratio | status of the row |
  |---|---|---|---|
  | 1, Earth crossing (GW170817 below the horizon at H1/L1) | 1.5e-29 | **1.6e8** | checked by F2; either sign |
  | 2, detector on the ground | ~1e-29 | 2.4e8 | checked by F2 |
  | 8, binary pulsar | 2e-43 | 1.2e22 | suggested |
  | 7, PTA | 8e-24 | 3e2 | suggested; massive sign |
  | 5, Galaxy+IGM LVK column | 2.7e-19 | 9e-3 | **passes** |
  | 10, hot era, massive sign | **no observational bound** | — | F2 reading |
  | 9, hot era, tachyonic sign branch | N_max = 66-95 e-folds | N ≈ 3.1e9 | checked arithmetic, scaled |

- **Tuning needed** to reach the lines: 8.7e-17 for the history line (not observational for the massive sign), and 1.3e-8 for the Earth against the 100 Hz energy (`f1_sizes.out:30`). F2 row 1 needs about 6e-9 in μ.

### 3.4 (d) Registered subtractions

| clause | covers the SF channel? | what it removes | removes anything observed? |
|---|---|---|---|
| **(S_loc) as registered** (P-R19-21a; `rR19-21:178-179,239`; `PRICE_NOTE:600`, named, OPEN) | **No, on its letter.** Its backgrounds are "local IR mean fields", e.g. ⟨φ²⟩, and the list is open ("…", `rR19-21:45`; `rR19-31:24`) | — | — |
| **P-R19-31b**: ⟨ψ̄ψ⟩ is an (S_loc) background (`rR19-31:256`; named, not adopted) | Yes, on the source side (suggested). The exact one-loop cancellation is R19-31's suggestion, not rederived here. The mechanism is independent of the strain law, so it applies to SF as to H-cov | The gravitating cross term ⟨ψ̄ψ⟩δm″ | Nothing observed (reading). It **leaves** the matter-side rest-mass–shear coupling ½δm″t² = 0.0121 e²/a per unit t² in the law. That is an LLI-type artifact, sized by the bridge only (not computed) |
| **P-R19-34a**: a strain-covariant critical mass (`rR19-34:177-180`; `PRICE_NOTE:679`; named, not adopted; "imposes rather than predicts", `vR19-34` item 6) | **Yes, exactly, by construction.** δm(t) ≡ δm(0) on every uniformly strained law, at all orders, for the P = 0 additive part | The channel, and the rest-mass–shear coupling | **No** (comparator: a traceless strain leaves a scalar rest mass unchanged; tests of local Lorentz invariance for matter see no anisotropic mass shift, RECALLED, no number quoted). It does not touch the multiplicative z″·m_f channel (not computed under SF) |
| (S\*), (Σ), (S), P-Tad (`rR19-35:67-70`) | No. They are lowest-state or vacuum clauses, and ⟨ψ̄ψ⟩_state is a state channel (reading; count once with `rR19-21` §3.3) | — | — |

## 4. Against the FIXED readings (`TESTS:9177-9181`), literal first

| reading | status |
|---|---|
| **SF-HAZARD** | **Met (worker).** (i) Nonzero, converged and ≥ 1e-3 in every branch the registered texts permit: B1, B2, the 0⁺ root, and the path sensitivity (§3.2). (ii) Beyond an observational bound per F2: the Earth-crossing row by 1.6e8 in μ_ρ (F2 checked, either sign); also the detector row, and the pulsar and PTA rows (suggested). (iii) No registered subtraction covers it: P-R19-34a, P-R19-31b and (S_loc) are all named, not adopted, and (S_loc)'s registered text does not list ψ̄ψ |
| **SF-COVERED** | **Met with P-R19-34a, if it is adopted.** It removes the channel exactly, and nothing observed. P-R19-31b covers only the source side (suggested) |
| SF-SAFE | Not met. Hessian 2.4e-2 ≫ 1e-10; the Earth row is exceeded by 1.6e8 |
| OPEN | Not met. The branches agree in reading, and the law was built from the registered texts. Two non-registered freedoms remain: §1 items 4 (a unitary operator dressing at O(t²)) and 5 (non-axis path families). Neither is supplied by any text |

**Worker reading: SF-HAZARD on the registered law, and SF-COVERED with P-R19-34a (an added rule).**
- Conditional on:
  - the canonical TT-pole mapping (`PRICE_NOTE:22`); under "μ is not a mass", only the rest-mass–shear coupling remains;
  - F2's table (worker, unrefereed);
  - the SM mapping estimate;
  - one loop.

## 5. Against the expectation (`TESTS:9182-9186`)

- **"The Hessian is nonzero":** borne out. It is +2.42e-2 e² (SF), i.e. +0.097 in H-cov units: **2.4 times larger than H-cov, with the opposite sign.**
- **"Photon and fermion flows differ, so no common change of variables exists":** borne out as the dominant mechanism (about 90%), with a correction. A common separable flow **does** give an exact change of variables (proved). It still leaves a nonzero lattice Jacobian term (−2.3e-3), because no E_g flow on the torus preserves volume (proved).
- **"The early-universe size is beyond |m_g| < H, as under H-cov":** numerically yes (+7.6e13 at 100 GeV). **But the sign is massive**, and for the massive sign F2 finds no hot-era observational bound (F2 row 10). The hot era conflicts only in the tachyonic sign branch. The binding observation is today's Earth crossing (GW170817), in either sign.
- **"P-R19-34a would cover it, as an added rule":** borne out, by construction.
- **"So SF-HAZARD on the registered law and SF-COVERED with P-R19-34a":** borne out. The hazard is carried by today's matter rows, not by the hot era.

## 6. Strong words

- **"Proved"** (short and unrefereed):
  - Psym's uniqueness in the axis-ordered family;
  - the path-independence of the diagonal seagull;
  - Ward at every t;
  - ξ-independence at P = 0 at the critical point;
  - evenness;
  - smoothness of D_t;
  - the relabelling lemma and the no-volume-preserving-flow lemma;
  - "no placement datum inside SF".
- **"Checked":** every number in §3, with the convergence stated. The free rows are reproduced to 3-5e-6. The γ-matrix reduction is exact to 1.4e-17.
- **"Every branch":** the registered-text branches only (§1 items 1-3), plus controls. Items 4-5 are named and not computed.
- **"Beyond an observational bound":** per F2, unrefereed. The Earth-crossing row is F2's checked 1D chord model, not a full 3D or TT-mixing calculation (`F2:78-81`).
- **Not claimed:**
  - two loops;
  - non-abelian or Yukawa terms;
  - T₂g;
  - the SF multiplicative channel;
  - the exact (S_loc) + ψ̄ψ cancellation;
  - VW = the frame-Maxwell generator beyond the q = 0 E_g weights (suggested);
  - any end state of the massive-medium screening.

## 7. Prices (named, not adopted)

- **P-R19-34a (counted once): strain-covariant critical mass.** It now covers the registered SF law as well. 0 numbers, 1 clause per edge per order (`rR19-34:177-180`). Gate `AX:114-130`.
- **P-R19-31b (counted once):** covers the source side only. Under it, the rest-mass–shear coupling (0.0121 e²/a per t²) needs its own disposition. That item is the same as R19-34 §3.4's "μ is not a mass" remainder.
- **No new price. No axiom text changes.**

## 8. Files (`S/` = `scratchpad/C5/F1/scripts/`)

- `f1_lib.py`: the SF-strained law (flows, Psym vertex, mass formula). It imports `../arch/` unmodified.
- `f1_validate.py/.out`: rerun after fixing a double division in the check script's own part (iii); the library was not affected. The pre-fix output is kept as `f1_validate_v0_buggycheck.out`. Its (iii) lines are invalid, and its other lines are identical to the rerun.
- `f1_validate2.py/.out`: the γ-matrix check, and photon-row convergence with small steps.
- `f1_timing.py/.out`: evenness.
- `f1_root.py` → `f1_root_conv.out`, `f1_root_conv2.out`: B1 convergence. The first run was stopped at 1.7 GB after two grids, and finished with chunking.
- `f1_branches.py` → `f1_branches.out` (B1, parts, B2, 0⁺), `f1_controls.out` (controls and the Jacobian check), `f1_orders.out` (B3).
- `f1_locality.py/.out`: FFT tails.
- `f1_sizes.py/.out`: history and today's matter.
- `f1_envscale.py/.out`: μ_ρ against F2's rows.
