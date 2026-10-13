# C5 R19-34 report: the Wilson ψ̄ψ strain channel on the root's actual edges

- **Worker:** Claude Opus 5.5 probe (same model family as the supervisor and every C5 worker). Unrefereed. Run 2026-10-13, 07:39Z to about 09:30Z. The report was finished after the 09:05Z hard return because Write-tool hook timeouts delayed saving it. No repository file was edited; nothing was downloaded.
- **Item:** `TESTS:8726-8745`. FIXED readings at `:8742-8744`; expectation at `:8745`.
- **Paths.** `P/` = `.claude/science/exercises/gravity-current-state-20261009/`; `AX` = `docs/MINIMAL_AXIOMS_2026-06-29.md`; `rX` / `vX` = `P/agents/C5_X_report.md` / `..._referee_verdict.md`; `S/` = `scratchpad/C5/R19-34/` (scripts and `.out` files in `S/scripts/`, unmodified runner copies in `S/arch/`).
- **Labels.** proved / checked / suggested / reading / comparator. RECALLED = from memory.
- **Read.** `AX` in full; `TESTS:8600-8745`; `rR19-31` in full, with `r1931_wilson_mass.py` and `r1931_sizes.py`; `rR16-1` and `vR16-1`; `rR19-5`; `vR19-24` and `rR19-24:1-80`; `vR19-21` and `rR19-21:1-60,170-250`; S26 (grep); `rR19-12:16-98`; `rR19-11:270-276`; `rR18-5:50-53,100-116`; archived `R18-5/dirac.py`, `sublum.py`, `R16-10/r1610_core.py`.

## 0. Reading: **PSI-HAZARD (worker)**, on R19-31's H-cov strain convention

**Plain words.**
- The root's fermion edge is D1, a box-exact Wilson-type law. Its doubler-removal term W multiplies β, the same matrix as the mass, so it breaks chiral symmetry, and one loop produces an additive mass.
- **Additive mass on the root's edges** (checked). On D1(0.909103708, 0.555604226) with the root photon Gph(2.9435):
  - δm = +0.04186 e²;
  - its uniform-E_g strain Hessian is **−0.04047 e²**, about 65% of R19-31's naive-Wilson value of −0.0622.
- **Size in R19-31's channel** (canonical reading, SM mapping an ESTIMATE):
  - m_g²/H² runs from −2.0e13 at 150 GeV to −4.8e15 at 1 GeV;
  - today, |m_g| ≈ 2.3e-9 eV inside the Earth.
- **What removes it.** Only one of these:
  - ⟨ψ̄ψ⟩ as an (S_loc) background (P-R19-31b);
  - twisted edges (P-R19-11c);
  - a strain-covariant critical mass (P-R19-34a, new);
  - leaving the root for chirally symmetric edges.

**Literal reading, clause by clause (`TESTS:8742-8744`):**
- **PSI-ZERO: not met.**
  - The Hessian is −0.0404747 e² on the R18-9 root and −0.0408127 e² on the R19-11 0⁺ root. Three quadratures agree to ≤ 1e-8.
  - An independent on-shell runner agrees after an O(m) extrapolation.
- **PSI-HAZARD: met** (checked).
  - The Hessian is nonzero.
  - m_g²/H² = −3.2e13 at 100 GeV, against the line |m_g| < H.
  - Earth: 2.3e-9 eV, against the 4.1e-13 eV energy of a 100 Hz gravitational wave.
- **The price named:** P-R19-31b on the root's D1 edges. ⟨ψ̄ψ⟩, per Wilson-type Dirac species, is among (S_loc)'s local IR mean-field backgrounds.

**Expectation (`:8745`).**
- **Wilson-type gives PSI-HAZARD: borne out.**
- **Twisted gives PSI-ZERO: borne out** (checked). The physical-mass Hessian is −0.0924 e²·μ, which tends to 0 with μ.
  - But twisted mass is not "a chirally symmetric kinetic term". Its untwisted additive mass keeps the same nonzero Hessian.
  - The zero comes from orthogonality: that shift enters the physical mass only quadratically (proved, §3.3).

**Scope.**
- One loop; U(1), Feynman gauge, Peierls divided-difference vertex (as in the refereed runners). QCD enters only through C_F (estimate).
- **H-cov E_g strain** (`rR19-31:56-59`): all per-axis hoppings, including the Wilson term, scale as 1/ℓ_j.
- **Not built:** the root's Dirac TT vertex UD generates a momentum-space strain flow (SF), not H-cov (`rR18-5:50-53`). A strained gauge law consistent with UD/SF was not built.
- **Sign and size depend on the Wilson term's strain placement** (§3.2), which has one tuned zero. Being nonzero does not depend on it.

## 1. (a) The root's edges (reading from cited files)

- **Dirac edge: Wilson-type, box-exact D1(b_f, r)**, R14-1's family.
  - h = Σ_j s(k_j)α_j + (m + Σ_j W(k_j))β, with s = k and W = 0 on |k_j| ≤ b_f (`P/scripts/C5/R18-5/dirac.py:4,25-38`; `rR16-1:56`).
  - Values:
    - R18-9 refined root: (0.909103708, 0.555604226) (`vR18-9:11`; `rR19-12:21,72`; `rR19-5:190`; `rR18-13:86`);
    - R19-11 0⁺ root: (0.915438682, 0.568280847) (`rR19-11:167`; `vR19-11:14`).
  - All 22.5 SM Dirac fields sit on this one edge (`S26:71`; `rR19-12:65`).
- **The mass is untwisted.** The twisted edge is the priced alternative P-R19-11c, "not the registered setting" (`rR19-11:276`).
- **Photon:** γG_w(2.9435) = Gph(2.9435), with d = q on |q| ≤ 2.9435 (`rR19-12:20,74`).
- **Vertices:** QED is Peierls, Feynman gauge (`rR19-12:65`); gravity is UD (`S26:119`).
- **Reading:** Wilson-type doubler removal. Not staggered, not twisted, not Ginsparg–Wilson.

## 2. Class and hypotheses

- **Arena.** Z³ × ℝ, one-loop U(1). The Euclidean P = 0 formula uses λ = 0; the on-shell checks use λ = 0.01.
- **Strain.** ℓ = (e^h, e^{−h}, 1) for E_g. Also run: (e^h, e^h, e^{−2h}), and isotropic e^h as a control.
- **Symbols.** s/ℓ_j and W/ℓ_j^κ, with κ = 1 for H-cov; κ is varied in §3.2 only. The photon is d/ℓ_j. Coupling: p_j → p_j + ℓ_j a_j.
- **Formula (proved; `r1934_lib.py` docstring).**
  - δm/e² = (1/V)⟨Σ_j ℓ_jW_j/d_j²/(2Ω)⟩ + (1/V)⟨[M + Σ_j((a_j² − b_j²)M − 2a_jb_js_j/ℓ_j)]/(2EΩ(E + Ω))⟩, with a_j = s/d and b_j = W/d.
  - This is R19-31's formula with the general divided-difference vertex. Only d² enters.
- **Quadrature.** Composite Gauss–Legendre on [0, π]³, with breaks at b_f, π − b_f and b_γ. Richardson Hessians with steps d = 0.02 and 0.04.
- **Counterterm.** Critical mass fixed at h = 0, as in R19-31. Per-site counterterms do not see traceless strain (count once).
- **Not computed:**
  - two loops;
  - non-abelian vertices beyond C_F;
  - Yukawa and W/Z loops;
  - a Wilson term for chiral SM fermions (the "22.5 Dirac" convention is taken as given);
  - a UD/SF-consistent strained gauge law;
  - T₂g.

## 3. Results

### 3.1 (b) Additive mass and strain Hessian, per edge (checked; `r1934_root.out`, `r1934_validate.out`)

**Validation.** The code reproduces R19-31's naive Wilson r = 1 values to every printed digit: +0.374347473 and −6.21578e-2. The Richardson value is −6.21822e-2. r = 0 gives 0. R19-31's own runner reruns identically, apart from the timing line.

| edge (H-cov E_g) | δm/e² | ∂²_hδm/e² | ratio |
|---|---|---|---|
| **R18-9 root D1(0.909103708, 0.555604226) + Gph(2.9435)** | **+0.041858390** | **−0.04047466** | −0.967 |
| **R19-11 0⁺ root D1(0.915438682, 0.568280847) + Gph** | +0.042294398 | −0.04081269 | −0.965 |
| R18-9 Dirac edge + naive photon | +0.070386231 | −0.06803199 | −0.967 |
| D1(1.4, 1/√3) + naive photon (R16-1 member) | +0.020436516 | −0.02057579 | −1.007 |
| naive Wilson r = 1 (R19-31) | +0.374347473 | −0.06218223 | −0.166 |
| naive Wilson r = 0.5556 | +0.250867400 | −0.10844240 | −0.432 |
| D1 shape at r = 0 (chiral control) | 0 | 0 | — |

- **Gradient.** ≤ 7e-16 everywhere.
- **Grid convergence.** n = 6/8 and hmax = 0.25/0.15 agree to ≤ 1e-8.
- **Cubic check.** The (h, h, −2h) Hessian is 2.999986 times the (h, −h, 0) one; the expected ratio is 3.
- **Dilation check.** d/dh = −δm and d²/dh² = +δm, as they should.
- **Parts.** Tadpole +0.018085; exchange +0.023773.
- **Independent formalism (checked; `r1934_onshell_check.out`).**
  - The refereed old-fashioned on-shell runner (`r1610_core.dirac_pt`, R13-7's), made per-axis. At ℓ = 1 it agrees with the unmodified function exactly (|diff| = 0 on 2000 points).
  - The differences δE(0) − δm and Hess(m) − Hess fall ∝ m for m = 1e-2, 3e-3 and 1e-3.
  - Extrapolated to m = 0: −0.040475, matching the Euclidean result to about 1e-6.
- **Gauge independence.** Suggested from the Ward identity (S⁻¹(0) = 0 on box laws). Not run.
- **Observation (suggested, empirical).** Across 45 D1 × photon combinations, the ratio ∂²δm/δm lies between −1.034 and −0.878. It is always negative and δm is always positive (`r1934_scan.out:2-46`). No member is near zero. I have no derivation of the near −1 ratio.

### 3.2 (c) Symmetry

- **Evenness (proved; checked ≤ 7e-16).** (x, y, z) → (y, x, −z), the C₂ rotation about [110], is proper. It maps the law at h to the law at −h and fixes P = 0, so the gradient vanishes.
- **One coefficient (proved).** On E_g, O_h has a single quadratic invariant, Σε². The ratio of 3 confirms it.
- **No symmetry forces zero on Wilson-type laws (r > 0).** W·β breaks chiral symmetry at every strain, and nothing else acts on β. A nonzero value is exhibited. Comparator (RECALLED): the critical mass depends on anisotropy in lattice QCD.
- **Chiral zeros (proved).**
  - At r = 0 the strained law keeps e^{iθγ5}, so δm(h) ≡ 0 to all orders (checked: 0). That brings back the π-doublers, which R9-1 excludes (`rR16-1:88`).
  - Staggered with any per-axis NN amplitudes: U(1)_ε holds at every strain, so δm ≡ 0. Not the root's edge.
  - Ginsparg–Wilson: the same (comparator, RECALLED).
- **Tuned zero (checked; `r1934_scan.out:47-54`).** With the Wilson strain placement W/ℓ^κ, the Hessian is:

  | κ | Hessian |
  |---|---|
  | 0 | +0.01309 |
  | 0.5 | −0.01860 |
  | 1 | −0.04047 |
  | 1.5 | −0.05253 |
  | 2 | −0.05477 |
  | 3 | −0.02980 |

  - It is zero at **κ\* = 0.188360** (residual 3e-14).
  - To meet the bounds, this needs about 2e-16 relative precision at every loop order.

### 3.3 Twisted comparator (proved at O(e²); checked; `r1934_twisted.out`)

- **Edge:** h = Σsα + (m₀ + ΣW)β + μ iβγ5 at maximal twist.
- **Proved:**
  - the vertex and seagull carry no iβγ5 part;
  - at rest, a = e₅, so the untwisted Σ does not enter at O(e²);
  - the residual ½δm″h² enters only at O(e⁴h⁴/μ).
- **Checked (5-direction rewrite of the refereed runner):**
  - with the twist off, the Wilson-type values are reproduced (+0.04420280 and −4.119110e-2);
  - twisted: Hess/μ = −0.0924 at μ = 1e-2, 3e-3 and 1e-3, so the Hessian → 0.
- **What remains: a multiplicative channel**, ⟨ψ̄ψ⟩_th·m_f·z″.
  - z″ = −0.0924 e² (twisted) or −0.0717 e² (Wilson root, m-linear slope).
  - m_g²/H² ≈ −5e-4 to −1.4e-3 between 150 and 1 GeV. That is below the line (estimate).
  - Staggered: not computed.

### 3.4 (d) Sizes (`r1934_sizes.out`; canonical reading conditional; SM mapping ESTIMATE, copied from `r1931_sizes.py:32-49`)

- **Control.** The naive-Wilson case reproduces R19-31's table exactly.
- **Root, early universe.** m_g²/H² = −2.0e13 (150 GeV), −3.2e13 (100 GeV), −4.7e13 (50 GeV), −2.6e14 (10 GeV), −4.8e15 (1 GeV). The 0⁺ root is within 1%.
- **Root, today:**
  - IGM: 6.5e-25 eV. This is below LVK's 1.92e-23 eV.
  - Earth: 2.3e-9 eV (nucleons) and 3.3e-10 eV (electrons). This is above 4.1e-13 eV. The conflict is suggested: it needs an environment-dependent propagation calculation (`vR19-21:26`).
- **Sign.** If m_f < 0 relative to W, the result is massive rather than tachyonic, with the same magnitudes (|m_g| ≈ 5.6e6 H at 100 GeV). It conflicts either way; count once with R19-21's sign branch.
- **Tuning needed.** The coefficient would have to shrink by a factor of 2.1e-16 for the history bound, or 3.1e-8 for the Earth.
- **Under "μ is not a mass"** (`PRICE_NOTE:22`). No tensor consequence. A rest-mass–shear coupling of 0.020 e²/a per unit h² remains.

## 4. Prior art (counted once)

- **R19-31** (worker; referee running): the channel, the cross term, the sizes code and P-R19-31b. Rechecked here (reproduced). New here: the root-edge coefficient, and the twisted case proved and checked.
- **R16-1 + vR16-1:** 𝒬_W and D1. R9-1 excludes r = 0.
- **R19-5:** edge identification.
- **R19-24 + vR19-24 item 4:** the D1∞ precedent, used for P-R19-34a.
- **R19-21 + vR19-21:** (S_loc) (`rR19-21:178-186`), the bounds, the matter channel.
- **R19-11:** P-R19-11c, the 0⁺ root.
- **Comparators (RECALLED):** staggered U(1)_ε, Ginsparg–Wilson, maximal twist, the anisotropic critical mass.

## 5. Strong words

- **"Proved":** the formula, evenness, the single coefficient, the chiral zeros, and the twisted O(e²) structure. All short and unrefereed.
- **"Checked":** every number in §3. Two independent formalisms agree to about 1e-6.
- **"Nonzero":** to 8 digits on two roots, under H-cov and at every sampled κ ≠ κ\*.
- **"No symmetry":** only within the strained Wilson-type law's own symmetries. The UD/SF strained law was not built.
- **Not claimed:** two loops; non-abelian or Yukawa terms; T₂g; staggered multiplicative terms; an exact (S_loc) + ψ̄ψ cancellation (R19-31's suggestion, not rederived here).

## 6. Prices (named, not adopted)

- **P-R19-31b, required on the root's edges.** ⟨ψ̄ψ⟩ is an (S_loc) background. 0 numbers, 1 clause. Gates: `AX:187`, `AX:94`.
- **P-R19-11c (counted once): twisted D1 at maximal twist.** Removes the additive channel at O(h²). Leaves about 1e-3 H² multiplicative. Still needs the h = 0 critical tuning.
- **P-R19-34a (new): strain-covariant critical mass.** The critical-mass counterterm is re-set on every uniformly strained law, i.e. a ψ̄ψ σ² counterterm fixed by a clause.
  - It is the mass analogue of D1∞ and P-R19-31c.
  - Number-free per vR19-24 item 4; 1 per edge per order in codimension.
  - Gate: `AX:114-130`.
- **P-R19-34b (new; not viable): tune the Wilson strain placement to κ\* = 0.18836.** Needs 2e-16 precision per order.
- **Chirally symmetric edges (staggered or GW).** These leave the root, so every row must be recomputed.
- **No axiom changes.**

## 7. Files (`S/scripts/`)

- `r1934_lib.py`
- `r1934_validate.py/.out`
- `recheck_r1931_wilson_mass.out`
- `r1934_root.py/.out`
- `r1934_onshell_check.py/.out`
- `r1934_scan.py/.out`
- `r1934_twisted.py/.out`
- `r1934_sizes.py/.out`
- `r1610_core.py` (unmodified copy)
- `S/arch/`: unmodified `dirac.py`, `sublum.py`, `r1610_core.py`, `r1931_*.py`
