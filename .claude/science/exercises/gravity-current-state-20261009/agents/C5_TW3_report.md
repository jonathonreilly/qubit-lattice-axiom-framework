# C5 TW-3 report: symmetric mass generation toy — can interactions gap the mirror twins without breaking the protecting symmetry, keeping the strain zero?

- **Worker:** Claude Opus 5.5 probe, same model family as the supervisor and every C5 worker. Unrefereed. Run 2026-10-14, 12:56Z to about 13:21Z.
- **Hygiene:** no repository file was edited. Nothing was downloaded; web search was used for citations only (no files fetched). Every run used OMP_NUM_THREADS=2, one process at a time. Peak resident memory was ≤ 462 MB for every run (`scripts/*.err`); the largest was the 4-site plaquette at 2^16 states. No process of mine is still running.
- **Item:** `TESTS:9647-9658` (shared setting `:9611-9617`; FIXED readings `:9654-9657`; expectation `:9658`).
- **Paths:** `P/` = `.claude/science/exercises/gravity-current-state-20261009/`; `AX` = `docs/MINIMAL_AXIOMS_2026-06-29.md`; `rX`/`vX` = `P/agents/C5_X_report.md` / `..._referee_verdict.md`; `pF/` = `P/agents/panel_F/`; `M:` = file on `origin/main` (8143841bf7); `S/` = `scratchpad/C5/TW3/scripts/`.
- **Read:** `AX` in full; `TESTS:9146-9658`; rNF1 in full and vNF1; rE1 in full; `pF/SYNTHESIS.md` and `pF/condmat_statement.md` in full; the coordinator's prior-art list (below, §2).
- **Labels:** proved (complete short argument, unrefereed) / checked (numerics run here) / suggested / reading / comparator (literature, cited). RECALLED = from memory.

---

## 0. Plain words, and the reading

1. **The 8-Majorana cluster works exactly as advertised (checked).** Eight Majorana modes with the Spin(7)-invariant (Cayley-form) four-body interaction have one ground state, a gap of 14W, and no allowed two-body mass term. Both Spin(7) and the time-reversal-type symmetry forbid every bilinear on their own. Fewer than 8 modes (2, 4, 6) cannot be gapped this way; 8 can. This is Fidkowski–Kitaev's Z8 (comparator).

2. **On small lattices of such clusters, strain never makes a mass (proved; checked).** I strained the hopping (x-bonds × (1+u), y-bonds × (1−u)) on a 2-site, an L-shaped 3-site and a 4-site cluster (up to 2^16 states).
   - The ground state stays unique and symmetric at every strain and coupling tested.
   - Every "mass" entry of the zero-frequency propagator stays at zero (≤ 1e-14), while a deliberately symmetry-breaking control makes it nonzero in proportion to the breaking.
   - **A light sector survives exactly:** adding two light modes per site that do not take part in the gapping, coupled to the gapped sector in every symmetry-allowed way, their zero-energy pair stays exactly degenerate (≤ 3e-12) at every strain. Strain gives the light sector no mass.
   - The reason is one exact symmetry, the sublattice time reversal Θ (the staggered edge's own Θ of NF-1). Strain only changes the strength of hops between the two sublattices, which Θ allows; every mass term sits within one sublattice, which Θ forbids. Spin(7) is not needed: a random Θ-symmetric four-body term does the same.

3. **How the gap itself responds to strain depends on how strong the interaction is (checked).**
   - **Weak interaction on protected zero modes:** the gap is the interaction times a wavefunction overlap, and strain changes only the overlap. The response is exactly proportional to the gap (multiplicative): d²ln Δ/du² → 8, as predicted.
   - **Strong interaction:** the gap is 14W minus the hopping bandwidth. Strain changes the bandwidth, so the gap moves by an amount set by the hopping, the same at every W: d²Δ/du² → −√2·t. That is an additive, fine-scale shift. It is small relative to a large gap, but it is not proportional to the gap.
   - On a real 3D lattice there are no protected zero modes; four-fermion gapping needs a finite coupling. Near that threshold the gap is "tuned" and strain moves it at the fine scale, like E1's Ising case (suggested; comparator).

4. **That additive piece is in the heavy mirror gap, not in the light sector.** The light (observed) fermions keep exactly zero additive mass. The mirror's fine-scale strain response can matter only through the vacuum's strain stiffness (heavy states are not in the Earth), which is the kind of term (Σ)/(S\*) already absorb. Not computed here.

5. **The count (proved by counting; comparators agree).**
   - 3+1D symmetric gapping needs 16 Weyl fermions; one SM generation with ν_R is exactly 16 (15 without).
   - On the staggered edge, Θ acts site by site, so onsite symmetric gapping needs 8 Majoranas per site = **4 staggered fields** = 8 Dirac tastes = 16 Weyl. This matches Catterall–Pradhan's anomaly count for Hamiltonian staggered fermions (multiples of four).
   - With one staggered field per component of the 16: 64 Weyl per generation, of which 16 are wanted and 48 = 3 × 16 must be gapped. The counting works with ν_R.

6. **But onsite gapping cannot pick out the twins (proved).** Any onsite interaction that is the same on every site is invariant under the staggered shift, which swaps the two tastes. So it gaps the wanted taste and its twin together. Gapping only the twins needs interactions spread over the 2×2×2 cube that break the shift. Θ and P_stag do not forbid that, but whether such a law exists, leaves a chiral light sector, and does not bring the doublers back at strong coupling is the open chirality problem. The repo's own Spin(10) note found that the strong-coupling endpoint restores 8 Weyl corners on a Wilson slab.

**Worker reading: OPEN** (literal), with the split named.
- SMG-PROTECTS clauses 1 and 2 (symmetric gap; bilinear forbidden under strain) are checked.
- Clause 3 (multiplicative gap response) holds only in the weak-coupling zero-mode regime. At strong coupling the toy's gap response is additive at the hopping scale (checked).
- SMG-LEAKS is not met: no additive mass appears in the light sector (proved; checked). The additive piece is in the gapped mirror sector.

---

## 1. Setting, hypotheses and choices (stated before any title)

- **Arena.** Finite Majorana clusters with continuous time (Hamiltonians), exact diagonalization. Each "site" carries 8 mirror Majoranas γ_a(x) (a Spin(7) spinor) and optionally n_L = 2 light Majoranas λ_l(x) (Spin(7) singlets). Jordan–Wigner, matrix-free (`S/tw3_lib.py`, `S/tw3_lattice.py`).
- **Interaction.**
  - The FK cluster term W·Ω(x), with Ω the 14-term Cayley 4-form (`S/tw3_lib.py:cayley_terms`, sign fixed by the Spin(7) commutant test, `tw3_fk.out:3-6`).
  - Branch: a random real combination of all 70 four-Majorana strings (Θ-even, Spin(7)-broken; `tw3_lat_L3_randT.out`).
- **Hopping and strain.** Bipartite i t_b Σ_a γ_a(x)γ_a(y), x ∈ A, y ∈ B, flavour-diagonal (SO(8)-invariant).
  - "Strain" = traceless anisotropic hopping, t_x = t(1+u), t_y = t(1−u), t = 1. This is the panel's reading of strain as a change of bond strengths (`pF/SYNTHESIS.md:15-16`).
  - The registered SF flow is not built for these toys. It acts on band symbols; on a 2–4 site cluster only the bond strengths exist.
- **Clusters.**
  - dimer (2 sites, one x-bond, 2^8);
  - L3 (A site at the origin, B sites at +x and +y, 2^12; the chiral index |B|−|A| = 1 gives one exact zero mode per flavour);
  - π-flux plaquette (4 sites, 2^16; no zero modes).
  - The zero-flux plaquette was not run (memory headroom).
- **Θ.** Antiunitary, γ(x) → ε_x γ(x), λ(x) → ε_x λ(x). This is the Majorana form of NF-1's Θ: χ_x → ε_x χ_x†, with K (`rNF1:130-133`). It is built explicitly and checked on H (`S/tw3_lattice.py:find_theta`).
- **Light–mirror couplings** (all Θ-, Spin(7)- and O(2)_L-invariant):
  - V1·(iΣλλ)(iΣγγ) on bonds;
  - V2·Ω(x)(iΣλλ) on bonds;
  - light hop t_L = 0.5 × the same strain.
  - Choice: V1 and V2 are not strained. How interaction bond terms strain is a branch the registered texts do not fix (see §3b-4).
- **Diagnostics.**
  - (i) Ground degeneracy and gaps per fermion-parity sector. Δ_odd is the single-fermion gap; Δ_even is the lowest same-parity excitation.
  - (ii) The "mass channel": all same-sublattice entries (including onsite a≠b) of the Majorana Green function at zero frequency, G_ab(x,y; iω=0) = Σ_n (⟨0|γ_b|n⟩⟨n|γ_a|0⟩ − ⟨0|γ_a|n⟩⟨n|γ_b|0⟩)/(E_n−E_0), computed by CG solves. A bilinear mass is exactly a nonzero same-sublattice block (its inverse is then not block-off-diagonal).
  - (iii) Strain response: ∂²_u at u = 0 by symmetric differences, h = 0.02.

---

## 2. Prior art (counted once)

**Repo, main (`git show origin/main:…`):**
- `M:docs/SPIN10_SYMMETRIC_ATOMIC_GAPS_MIRROR_BOUNDARY_PROJECTION_AND_CURRENT_RESPONSE_BOUNDED_THEOREM_NOTE_2026-09-14.md`. This is the direct prior symmetric-gapping attempt. Conditional-support, not independently reviewed.
  - An exact Spin(10) atom with a unique singlet and gap (`:50-59`);
  - atomic propagator zeros (`:131-166`);
  - freezing the mirror slots of a Wilson slab at strong coupling restores eight Weyl corners (`:203-223`);
  - the Feshbach endpoint bound (`:225-243`);
  - second-order Schrieffer–Wolff gives a constant, not a mirror mass (`:245-257`);
  - Golterman–Shamir endpoint warning (`:371-397`).
  - TW-3's 8-Majorana cluster is the Z8 analogue of that atom. Its §4 warning carries over to any strong-coupling twin removal (§3d).
- `M:docs/AXIOM_FIRST_SM_ANOMALY_CANCELLATION_COMPLETE_THEOREM_NOTE_2026-05-03.md:13-37`: the four perturbative traces plus Witten's Z2 vanish on SM + ν_R. It does not include the mod-16 (Dai–Freed/Z16) condition. Its `:230-250` lists what it does not claim.
- `M:docs/CHIRALITY_GATE_IS_TWO_INDEPENDENT_GATES_DIRAC_VS_GENERATION_SCOPING_NOTE_2026-06-08.md:42-47,91-102`: Dirac/spinor chirality and generation chirality are independent gates. TW-3 concerns only the first: the L/R content of the staggered edge (reading).
- `M:docs/A3_ROUTE3_ANOMALY_INFLOW_BOUNDED_OBSTRUCTION_NOTE_2026-05-08_r3.md:162` (E6: staggered chirality complements hw=1 ↔ hw=2 corner labels) and `:512-523` (current scope: an equal-diagonal identity only).
- `M:docs/THE_GENERATION_COUNT_IS_THE_SPATIAL_DIMENSION_ON_THE_K1_BRANCH_AND_IS_UNDEFINED_ON_K0_THE_WILSON_OPERATOR_IS_THE_K0_OPERATOR_BOUNDED_THEOREM_NOTE_2026-09-03.md:39-50,57-66,174-182`. The hw=1 corner triplet appears only for λ > 0 in H_K1 + λM_W. §3d-4 below checks that M_W breaks both Θ and P_stag.
- Also hit by the grep: `M:docs/EMERGENT_LORENTZ_INVARIANCE_AT_THE_DIRAC_POINT_AND_THE_TASTE_CENSUS_BOUNDED_THEOREM_NOTE_2026-09-03.md:167` (local census 8 = spin 2 × chirality 2 × flavour 2, so N_f = 2, consistent with NF-1); `M:docs/A_RECORD_NATIVE_STAGGERED_MASS_GAP_…_2026-09-03.md:247-248` (no four-fermion term, no chiral sector).
- No other symmetric-mass-generation or Fidkowski–Kitaev attempt was found on main. The grep's other hits are four-fermion terms in unrelated contexts: Yukawa/Ward, NJL, RP, PRs 8056 and 8081.

**C5 exercise:**
- NF-1 and its verdict: Θ and P_stag force all 64 entries of Σ(0,0) = 0 (`vNF1:7,19`; `rNF1:129-143`); the dictionary Γ_ε ≅ β⊗1 (`rNF1:81-84`); taste splitting breaks Θ and is untested (`vNF1:13`).
- E1: tuned gaps open with a fine-scale coefficient, p = 0 (`rE1:151,72`); a transmuted scale shifts multiplicatively (`rE1:172-177`); protection is a property of a phase with an O(1) margin (`rE1:190-196`).
- Panel F condensed-matter lens: the three-way choice (`pF/condmat_statement.md:273-279`); mirror SMG wants 16 Weyl per generation (`:83`).
- R2-4 §A7: mirror SMG is an open interacting escape; Golterman–Shamir objections (`rR2-4:257-264`).
- `TESTS:908` (lane RS, S1): staggered contact four-fermion terms, tested for momentum only.

**Comparators (literature; cited, not reproduced):**
- Fidkowski & Kitaev, PRB 81, 134509 (2010), arXiv:0904.2197; PRB 83, 075103 (2011), arXiv:1008.4138. Z → Z8 for the time-reversal-symmetric Majorana chain.
- Slagle, You & Xu, PRB 91, 115121 (2015), arXiv:1409.7401. QMC on a bilayer honeycomb: a direct transition from gapless Dirac to a symmetric gapped phase at finite coupling, tied to Z16.
- Tong, JHEP 07 (2022) 001, arXiv:2104.03997. SMG through gauge dynamics in 2d and 4d, including SM fermions.
- García-Etxebarria & Montero, JHEP 08 (2019) 003, arXiv:1808.00009. Dai–Freed anomalies: the SM with ν_R is anomaly free for a Z4, and its fermion count is a multiple of 16. Summarized from search results, not verified from the full text.
- Catterall & Pradhan (v3+ with Samlodia), "Symmetries and anomalies of Hamiltonian staggered fermions", arXiv:2501.10862. A mixed shift/time-reversal anomaly cancels for multiples of four staggered fields; the minimal anomaly-free model looks like Pati–Salam. Catterall, arXiv:2209.03828 (4D Euclidean: multiples of two).
- Butt, Catterall & Hasenfratz, PRL 134, 031602 (2025), arXiv:2409.02062. One staggered SU(2)-fundamental fermion: an SMG phase at strong gauge coupling, transition suggested continuous.
- Golterman & Shamir, arXiv:2311.12790 (propagator zeros act as ghost-like states when gauged; journal reference not verified) and arXiv:2505.20436 (constraints on SMG for lattice chiral gauge theories).
- Wen, arXiv:1305.1045; Wang & Wen, arXiv:1809.11171 (cited via the repo note `M:…SPIN10…:474-478`).

---

## 3. Results

### 3(a) The 8-Majorana cluster (checked; one proof)

| check | result | source |
|---|---|---|
| Cayley form, 14 terms; Hermitian | residual 0 | `tw3_fk.out:1-3` |
| commutant of Ω in so(8) | dimension **21** (Spin(7)); Lie closure 2.7e-14 | `:3,5-6` |
| Spin(7)-invariant bilinears | dimension **0** (smallest singular value 13.66) | `:7` |
| T (antiunitary, γ_a → γ_a): T² = +1, TPT⁻¹ = +P; H T-invariant | residual 0 | `:8-9` |
| every bilinear iγ_aγ_b is T-odd | residual 0 (proved: T i T⁻¹ = −i) | `:10` |
| spectrum of H = WΩ | −14W (×1, even), 0 (×8, odd), +2W (×7, even) | `:11` |
| ground state | unique, gap 14W (single-fermion gap 14W), Spin(7) Casimir 0, max \|⟨iγ_aγ_b⟩\| = 2.2e-17 | `:12-16` |
| mass channel G_ab(iω=0), all 64 | 0 | `:17` |
| G_00(iω=1e-3) | −1.02e-5 i = −2iω/Δ²: a propagator **zero** at ω = 0, not a mass pole (comparator: `M:…SPIN10…:139-144`) | `:18` |
| control: +0.1·iγ₀γ₁ (T- and Spin(7)-breaking) | ⟨iγ₀γ₁⟩ = −1.25e-2 | `:19` |

**Z8 count (checked; comparator FK 2010/2011).** Over 200 random T-symmetric even Hamiltonians each (`tw3_fk.out:21-25`):

| ν | T² | T P T⁻¹ | minimum ground degeneracy |
|---|---|---|---|
| 2 | +1 | −P | 2 |
| 4 | −1 | +P (Kramers) | 2 |
| 6 | −1 | −P | 2 |
| 8 | +1 | +P | **1** |

A random T-symmetric quartic at ν = 8 already gives a unique ground state, so **Spin(7) is not needed**. T alone suffices for the count and for forbidding bilinears.

### 3(b) Small lattices under strain (proved + checked)

**b-1. The symmetry argument (proved).**
- Under Θ, a bond term i t γ_a(x)γ_b(y) maps to −i t ε_xε_y γ_a(x)γ_b(y).
- For x, y on opposite sublattices (ε_xε_y = −1) it is invariant for every real t. For the same sublattice, including onsite a ≠ b, it is odd.
- Uniform strain changes only the real A–B hop magnitudes, and onsite quartics are Θ-even (ε⁴ = 1). So H(u) is Θ-invariant at every u.
- When the ground state is unique, every same-sublattice bilinear expectation and every same-sublattice entry of G(iω=0) vanishes, at every strain and coupling.
- This is the Majorana image of NF-1's Θ statement (`rNF1:130-133`), counted once.

**b-2. Mirror sector (checked).** 84 (W, u) points in all: W ∈ {0.01, …, 10}, u ∈ {0, ±0.02, 0.05}, on the dimer, L3 and the π-plaquette.

| cluster | ground state | Θ residual (W = 0.1, 10; u = 0.05) | same-sublattice max \|G(0)\| | A–B max \|G(0)\| (the test has power) | onsite \|⟨iγγ⟩\| | control m = 1e-3 / 1e-2 |
|---|---|---|---|---|---|---|
| dimer | unique at all points | 0 | ≤ 5.7e-16 | 2.3e-7 – 0.96 | ≤ 1e-15 | 2.84e-5 / 2.84e-4 |
| L3 | unique at all points | 0 | ≤ 1.1e-14 | 2.3e-7 – 0.57 | ≤ 5e-15 | 2.87e-5 / 2.87e-4 |
| π-plaquette | unique at all points | 0 | ≤ 9.2e-16 | 2.3e-7 – 0.52 | ≤ 6e-15 | 2.87e-5 / 2.87e-4 |

Sources: `tw3_lat_dimer.out:6-57`, `tw3_lat_L3.out:6-57`, `tw3_lat_plaqpi.out:6-57`. The control (a Θ- and Spin(7)-breaking onsite bilinear) makes the same-sublattice channel nonzero in proportion to m.

**b-3. Spin(7)-broken branch (checked).** With a random Θ-even onsite quartic, L3: unique ground state at W = 0.01–10; same-sublattice max |G(0)| ≤ 2.2e-11 against A–B entries 1.5e-5 to 0.5; Θ residual 0 (`tw3_lat_L3_randT.out`). So the protection rests on Θ, not on Spin(7).

**b-4. Light sector (checked; proved).** L3 with 2 light Majoranas per site (2^15 states).
- The chiral index gives one light zero mode per light flavour, i.e. ν = 2 light zero-mode Majoranas.
- By the ν = 2 row of §3(a), T anticommutes with parity there. So no Θ-symmetric operator can split them (proved).
- Checked: the lowest odd − lowest even splitting is ≤ 2.7e-12, against |E₀| ~ 420. That holds for W ∈ {0.1, 1, 10}, (V1, V2) ∈ {(0, 0), (0.3, 0), (0.3, 0.2)}, and u ∈ {0, 0.05, 0.2}. The Θ residual is 0 (`tw3_lat_L3_light.out:7-33`).
- **Control:** a Θ-odd light bilinear m·iλ₀(1)λ₁(1) splits the pair by 1.006m, 1.018m and 1.054m at u = 0, 0.05 and 0.2 (`:35-41`). Once Θ is broken, the light mass is strain dependent, in proportion to the breaking.
- **Side finding (suggested; checked numbers):** the control's u-trend is opposite to the bare-hopping zero-mode weight (predicted 1.000m, 0.900m, 0.615m).
  - It agrees to ≤ 3% with an effective light hop t_L(1±u) + V2⟨Ω⟩, where ⟨Ω⟩ ≈ −14, as an unstrained interaction term.
  - So a symmetric light–mirror coupling can change, even reverse, the anisotropy the light species feels. That is a per-species metric (light-cone) effect, not a mass.
  - It is the toy image of E1's per-species metric (`rE1:134-137`) and panel F's C3 (`pF/SYNTHESIS.md:78`), counted once. It depends on how interaction bond terms are strained, which is not registered.

### 3(c) What sets the gap's strain dependence (proved at leading order; checked)

**c-1. Weak coupling on protected zero modes: multiplicative.**
- *Proved, first-order degenerate perturbation theory:* on L3 the 8 mirror zero modes Γ_a = Σ_x ψ₀(x)γ_a(x), with ψ₀ = (0, t_y, −t_x)/√(t_x²+t_y²), carry the projected interaction W(Σ_x ψ₀(x)⁴)Ω(Γ).
- Mixed terms with two non-zero-mode operators reduce to ⟨γ_cγ_d⟩_free ∝ δ_cd, which Ω contracts to zero, so no induced bilinear appears. Hence Δ = 14W·(t_x⁴+t_y⁴)/(t_x²+t_y²)² + O(W²/t), and ∂²_u ln Δ = 8 exactly. The response is ∝ Δ.
- *Checked:*
  - W = 0.01: Δ = 0.070747, against 14·0.01·½ = 0.07; ∂²_u ln Δ = 8.06 (odd) and 8.06 (even) (`tw3_lat_L3.out:6,37`).
  - Random Θ-even quartic: 8.12 at W = 0.01 (`tw3_lat_L3_randT.out`).

**c-2. Strong coupling: additive at the hopping scale.**
- *Proved, first order in t/W:* a single excitation γ_a(x)|S⟩ hops with the free amplitude, because ⟨S|γ_aγ_b|S⟩ = δ_ab. So Δ_f(u) = 14W − max_k ε_u(k) + O(t²/W), where ε_u(k) are the free one-flavour levels.
- *Checked at W = 10* (`tw3_lat_*.out:30-43`):

| cluster | 14W − Δ_odd | predicted max ε | ∂²_u Δ_odd | predicted −∂²_u max ε |
|---|---|---|---|---|
| dimer | 1.014 | 1 | −0.021 | 0 (gap linear in u) |
| L3 | 1.433 | √2 = 1.414 | −1.507 | −1.414 |
| π-plaquette | 1.442 | √2 = 1.414 | −1.450 | −1.414 |

The O(t²/W) remainders are 0.01–0.09. The shift does not depend on W; relative to the gap it is O(t/W): ∂²_u ln Δ = −1.1e-2 at W = 10.

**c-3. The π-plaquette at small W has no symmetric-gapping regime.** Its gap is the finite-size kinetic gap 2√2, with ∂²_u ln Δ = 1.000 = ∂²_u ln √(t_x²+t_y²) (`tw3_lat_plaqpi.out:37`). This is kinetic, not interaction-generated.

**c-4. Extrapolation to a 3D lattice (suggested; comparator).**
- A free staggered band has Dirac points, not zero modes, so weak four-fermion terms are irrelevant. A symmetric gap needs W above a finite threshold W_c (comparators: Slagle–You–Xu 2015; Butt–Catterall–Hasenfratz 2025).
- Leading order gives W_c ≈ max_k ε_u(k)/14, and strain moves it at O(u²) with a hopping-scale coefficient. For the 3D staggered band under E_g strain, ∂²_u √(Σt_j²)/t = 2/√3 (`tw3_count.out`, last block).
- Near W_c, δΔ stays W-independent while Δ → 0: E1's tuned class, p = 0 (`rE1:151`).
- A multiplicative response needs the gap to be generated perturbatively on a protected zero-mode manifold (c-1, 0+1D), or tied to a transmuted scale. Examples: E1 b-5, counted once (`rE1:172-177`); gauge-driven SMG (Tong 2022; Butt–Catterall–Hasenfratz 2025) by that reasoning (reading).

### 3(d) The count, and the staggered edge (proved by counting; comparators)

**d-1. Weyl count.**
- SM: 15 Weyl per generation (45 for three, ≡ 13 mod 16). With ν_R: 16 per generation (48 ≡ 0) (`tw3_count.out:1-3`).
- So **one SM generation with ν_R matches the required multiple of 16** (comparator: García-Etxebarria–Montero 2019; Tong 2022). Without ν_R it does not.
- The repo's anomaly closure covers the perturbative and Witten conditions only (`M:…ANOMALY…:13-37`), not this mod-16 condition.

**d-2. Onsite count on the staggered edge.**
- Θ acts site by site as T (A sites) or as T with a sign (B sites). A site with n one-component staggered fields holds 2n Majoranas, so by the Z8 table an onsite Θ-symmetric unique gapped state needs **2n ≡ 0 mod 8**, i.e. n = 4.
- That is 4 staggered fields = 8 Dirac tastes = 16 Weyl (`tw3_count.out:5-13`).
- This agrees with Catterall–Pradhan(–Samlodia)'s anomaly count for Hamiltonian staggered fermions in 3+1D: multiples of four (arXiv:2501.10862). The toy's Z8 is the onsite image of that lattice anomaly (reading).

**d-3. Per generation** (one staggered field per component of the 16; `tw3_count.out:15-19`):
- 2 tastes × (16 ⊕ 16̄) = 64 Weyl. Keep 16; gap 48 = 3 × 16.
- 32 Majoranas per site = 4 × 8.
- NF-1's T1 assignment with ν_R: the twins are 24 Dirac = 48 Weyl = 3 × 16.
- The count is compatible with ν_R and incompatible without it, as with NF-1's 11.25 (`rNF1:207`).

**d-4. Selectivity (proved, short).**
- A translation-invariant onsite interaction is even at every site, so the shift's sign factors ζ_μ(x) cancel and it is shift invariant.
- Shifts exchange the two tastes. So onsite symmetric gapping removes the wanted taste and its twin together, and leaves no light sector.
- To gap only the twins (or only the 16̄ mirrors), the interaction must break the shift and act through cube-spread taste projectors.
- Θ and P_stag do not forbid this: in NF-1's dictionary both act trivially on taste (Γ_ε ≅ β⊗1, `rNF1:81-83`).
- Also proved: a symmetric-gapping pole Σ(ω) ≈ Δ²M/(iω) is allowed by Θ and P_stag whenever [M, ε] = 0. Θ requires εΣ(ω)ε = −Σ(−ω), and the pole satisfies it when M commutes with ε. That is how symmetric gapping evades the bilinear ban.
- So the symmetry does not block taste-selective symmetric gapping. Whether such a law exists open:
  - it must leave a chiral light sector;
  - the strong-coupling endpoint can restore doublers (`M:…SPIN10…:203-223`; Golterman–Shamir 2505.20436);
  - the mirror's propagator zeros, once gauged, act as ghost-like states (Golterman–Shamir 2311.12790; comparator).
- This goes to the chirality exercise, as the expectation said.

**d-5. Cross-lane (checked).**
- The generation lane's hw=1 triplet needs λ > 0 in H_K1 + λM_W (`M:…GENERATION_COUNT…:39-50,57-66`).
- On the 4³ torus (`tw3_gen.out`):
  - H_K1 keeps Θ and P_stag (residuals 0, 0);
  - H_K0 keeps Θ but breaks P_stag (residual 2);
  - the onsite part dI breaks Θ;
  - M_W breaks both (6, 1).
- So the λ > 0 generation branch lies outside NF-1's protected class. The strain-zero route and the hw=1 generation reading are on different branches (reading).

**Light-sector protection in the real case (reading).** The toy's light pair (ν = 2) is anomalous, so it cannot be gapped at all; that over-protects. SM + ν_R is anomaly-free, so nothing symmetric stops its own symmetric gapping. The light sector stays light because it is in the weak-coupling phase, with an O(1) margin (as in E1 c-2, `rE1:190-196`). A strain of ~1e-21 cannot cross a finite threshold. Bilinear masses stay forbidden by Θ and P_stag at every strain.

---

## 4. Against the FIXED readings (`TESTS:9654-9657`), literal first

| reading | clause | status |
|---|---|---|
| **SMG-PROTECTS** | the gap opens symmetrically | **checked** in the toy: unique Θ-symmetric (and Spin(7)-singlet) ground states on all clusters at all (W, u). Finite clusters only; a thermodynamic 3D symmetric phase is comparator only |
| | the bilinear stays forbidden under strain | **proved + checked**: same-sublattice G(0) ≤ 1.1e-14 (controls ∝ m); the light zero pair stays degenerate ≤ 2.7e-12 |
| | the gap's strain response is multiplicative | **only in part.** Weak coupling on zero modes: ∂²_u ln Δ → 8 (proved; checked 8.06). Strong coupling: ∂²_u Δ → −√2·t, independent of W, i.e. additive at the hopping scale (proved at leading order; checked on three clusters). On a 3D lattice the near-threshold gap is expected to be tuned-class (suggested) |
| | all checked | **not met** (clause 3) |
| **SMG-LEAKS** | strain induces a symmetry-allowed additive mass in the light sector | **not met.** Θ forbids it (proved); none appears (checked). The additive response is in the gapped **mirror** gap, which is not light |
| **OPEN** | otherwise | **met** |

**Worker reading: OPEN.**
- SMG-PROTECTS fails only on its multiplicative clause, and only for the mirror gap at strong or near-threshold coupling.
- No light-sector leak exists, so SMG-LEAKS also fails.
- The strongest positive statement: in the toy, **the light sector's strain zero is exact (Θ alone), and a symmetric gap exists. Its own strain response is multiplicative only where the gap is generated on protected zero modes. Elsewhere it is set by the hopping (fine) scale.**

## 5. Against the expectation (`TESTS:9658`)

- **"SMG-PROTECTS in the toy":** borne out on the protection, not on the multiplicative clause.
  - The bilinear ban and the symmetric gap hold, and the light sector is exact.
  - The mirror gap's response is multiplicative only at weak coupling on zero modes. At strong coupling it is additive at the hopping scale.
- **"The open part is whether the 3+1D staggered mirror content admits it":** confirmed and sharpened.
  - The count admits it with ν_R (4 staggered fields per onsite block; 48 = 3 × 16 per generation).
  - Onsite gapping provably cannot be twin-selective. A shift-breaking, cube-spread law is needed, and its existence is the chirality exercise.
- **Not anticipated:**
  - Spin(7) is unnecessary; Θ alone protects.
  - Symmetric light–mirror couplings change the light species' strain anisotropy (a metric/light-cone effect, §3b-4).
  - The generation lane's λ > 0 branch breaks both Θ and P_stag (§3d-5).

## 6. Prices (named, not adopted; no axiom text changes)

- **P-TW3a: a twin-selective symmetric four-fermion law.**
  - It breaks the shift, keeps Θ and P_stag, is cube-local, and acts on 48 Weyl per generation, with ν_R added (content).
  - It is supplied dynamics; dynamics is downstream of the axioms (`AX:116-130`). The staggered realization itself is an open gate (`AX:178`).
  - Its existence with a chiral light sector is open (chirality exercise).
- **P-TW3b: the mirror sector's strain-dependent zero-point energy.** It is a lattice-scale vacuum strain term, because the mirror gap's response is fine-scale (§3c-2). It can only be absorbed by (Σ)/(S\*) (count once with F5's knock-on, `TESTS:9390`). Not computed.
- **P-TW3c (a branch):** how interaction bond terms are strained. It sets the light species' effective metric (§3b-4). Count once with panel F's light-cone clause C3.

## 7. Not computed / scope

- **Not computed:**
  - a 3D lattice, or any thermodynamic limit (sizes ≤ 2^16; c-4 is suggested);
  - the registered SF flow on these toys (bond strain only);
  - gauge fields and the propagator zeros when gauged (comparator only);
  - the zero-flux plaquette;
  - near-threshold numerics;
  - two-point functions beyond iω = 0;
  - the mirror vacuum stiffness (P-TW3b);
  - any taste-selective interaction (P-TW3a).
- **"Proved"** means short arguments, unrefereed: the Θ symmetry statement, the first-order formulas in c-1 and c-2, d-2 and d-4. "Every strain" means uniform bond strain on the clusters stated.
- The FK cluster and the lattices are supplied model data. Nothing here derives a fermion from a qubit (`AX:178`).

## 8. Files (`scratchpad/C5/TW3/scripts/`, each with `.out` and `.err` / peak RSS)

- `tw3_lib.py`: Jordan–Wigner Majoranas and the Cayley form.
- `tw3_fk.py` → `tw3_fk.out`: probe (a) and the Z8 table. 59 MB.
- `tw3_lattice.py <cluster> [nL] [mode]` → `tw3_lat_dimer.out` (61 MB), `tw3_lat_L3.out` (82 MB), `tw3_lat_plaqpi.out` (462 MB), `tw3_lat_L3_light.out` (`L3 2 light`, 206 MB), `tw3_lat_L3_randT.out` (`L3 0 randT`, 85 MB).
- `tw3_count.py` → `tw3_count.out`: probe (d) arithmetic and the 3D strain coefficient. 27 MB.
- `tw3_gen.py` → `tw3_gen.out`: cross-lane Θ/P_stag check of M_W. 28 MB.
