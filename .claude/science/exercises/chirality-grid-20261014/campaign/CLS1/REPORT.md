# CLS-1 report: does class S (lattice-scale translation breaking to BCC) destroy X2's light generations?

**Reading: CLS-PRICE. Without tuning it is KILL-level at every f in the range.**

**Provenance.**
- **Worker:** Claude Opus 5.5 at xhigh. Same family as the supervisor and as X2 and OBS-1 to OBS-4; unrefereed.
- **Window:** 14:3x–15:19Z on 2026-10-15.
- **Saving:** the harness blocks subagents from writing REPORT.md. The supervisor saved this file from the worker's final message, lightly condensed; every number and file reference is the worker's.

**The finding.** Class S does not gap X2's three light generations at the bilinear level. But it mixes them with each other at the lattice scale.
- That gives the light quarks and leptons flavour-dependent energies and speeds, 10²²–10⁴² over the Lorentz bounds.
- Avoiding this needs one named symmetry, plus three new counterterm structures tuned to about 10⁻²⁷.
- PRICE rather than KILL follows registered rule R3: a tuning of stated size counts as PRICE, as for OBS-4's P2. This is the worker's reading under its own pre-registered rule, not yet refereed.

## Plain words

1. **Labels (this holds).**
   - Under the BCC translations, the hw1 corners share a label with hw3, and hw0 shares one with hw2.
   - The (1,1,1) translation is in BCC, and its sign on each corner equals that corner's handedness. So each sector holds a single handedness: 4 left-handed in one, 4 right-handed in the other, per Spin(10) component.
   - No ordinary mass term can pair anything.
2. **The real problem is light–light mixing, not light–hw3.**
   - A corner-changing Yukawa ψ_cψ_c′H₀S_K and a corner-changing hopping ψ_c†ψ_c′S_K carry the same translation charge (labels.out:9-11).
   - So the condensate that supplies CKM also lets the three light generations hop directly into each other, with no mirror involved.
   - **On-site form.** At the folded point, the light energies split into +2ε for the symmetric combination and −ε for the other two. That gives Fermi seas of size about ε, roughly 10¹⁸ GeV.
   - **Kinetic form.** The three light speeds become 1−η, 1 and 1+η.
   - No symmetry was found that forbids the kinetic form. Any symmetry that removed it would also remove the off-diagonal Yukawa.
3. **The mirror adds nothing here.** The hopping exactly as posed, hw1 to hw3 only, gives exactly zero hw3 admixture: the gapped mirror's propagator vanishes at zero energy. The admixture goes into the composite partner instead.
4. **OBS-3's one-loop zero does not survive class S.** Its premise, kinetic terms diagonal in the corners (OBS-3 REPORT:76), needs exact unit translations.

## Results

### (i) Labels (proved; checked by brute force)

**Residual translations.** BCC, with residues {(000), (111)} (labels.out:2).

**Sectors** (labels.out:3-6):

| Sector | Corners | Handedness | Index per component |
|---|---|---|---|
| even | hw0, hw2 | all R | +4 |
| odd | hw1, hw3 | all L | −4 |

Control: exact unit translations give 8 distinct labels (labels.out:7).

**What this forbids.**
- Dirac masses need opposite handedness in one sector, so they are impossible.
- Majorana-type pairings are excluded by Spin(10) (16⊗16 has no singlet), by Z₄^F and by B−L.
- This holds perturbatively. Non-perturbatively it holds only with a lattice CPT-type symmetry Θ: ψ(x) → ψ†(−x)ᵀ, antiunitary, with the partner field taking sign −1.
  - Θ forces every allowed one-body term to be odd in k, which pins both folded corner points at E = 0 for any strength (labels.out:14-33).
  - Without Θ, random BCC bilinears of strength ≥ 0.3 move the nodes out of a radius-0.6 sphere (index.out:2-4).
  - Whether nodes can annihilate globally was not tested.

**What protects the 3 light L modes.**
- At the bilinear level: the sector index.
- At the interacting level: nothing topological. By K1's absorption lemma (K1 KILL_REPORT:80-87, :147-153), the odd sector of 4×16 is anomaly-free, so an interaction could in principle gap all of it, light modes included.
- **Generalised X2-L2.** The number of exact zero modes at the folded point is 4 − rank Φ(P) per spin per component, where Φ(P) is the filter's 4×4 map from the four odd corners into the interacting field.
  - It is 3 only if the condensate leaves the filter unmodulated (κ = 0).
  - For κ ≠ 0 the rank is 4, so exact decoupling is lost (light.out:21-28).
  - Protection then becomes dynamical. It needs three things: the light channels' weight below the SMG threshold; Θ; and no gapless composite at the light corners.

### (ii) Coupling to the mirror interaction

**Method.** Free-fermion auxiliary-partner proxies in 3D, one-body level.

**Control (ε → 0).** X2-L2 is recovered exactly: hw3 weight about 10⁻³¹, |H·e_light| = 3×10⁻¹⁶ (light.out:1-4).

**Literal model (hw1↔hw3 hopping, static partner on hw3).**
- hw3 admixture is about 10⁻³¹, i.e. zero.
- The composite-partner admixture is θ_χ² = 3ε²/(3ε²+4Δ²), which matches direct diagonalisation exactly (theta.out:2-13).
- With one partner in the sector, exactly 3 L modes stay massless for every ε. That is a counting statement, not a protection.

**The Θ-imposed route (filter modulation κ).**
- θ² = 3κ²/4 + O(κ³). Three methods agree to 8 digits: SVD, direct diagonalisation of Model B, and real-space L = 4 diagonalisation of Model A (theta.out:16-20).
- The light modes enter the interaction at first order in κ, not θ. The channel weights are w = 2κ (symmetric) and κ (the other two). So the light modes feel about W(2κ)⁴, roughly 28× the θ⁴W estimate.
- The margin 1/w⁴ is 24.5 at κ = 0.33 and 1 at κ = 1 (light.out:26-28).
- The light nodes stay at P with linear dispersion (light.out:50-52).

**The two proxies disagree.**
- **Model A** (static partner; registered as primary) gaps the light modes at Δ·σ_light for every κ ≠ 0. The cause is that the free partner has unpaired zero modes at the light corners: the same vector-like modes X2's T5 reported.
- **Model B** (the registered threshold rule) keeps them gapless for κ ≲ 0.55 when W ≤ 10 W_c.
- Which proxy is right is decided by L_X2's no-gapless-composite clause.

### (iii) Observable changes

| Effect | Source | Size | Against bound |
|---|---|---|---|
| Dimension 3 (a-type): light energy split (1 new structure, count.out:1) | on-site density coupling to S | 3ε ≈ 1.2×10¹⁹ GeV at εa = 0.33, 1/a = M_Pl | ×4×10⁴² over IceCube 2.9×10⁻²⁴ GeV (bounds.out). Zero with Θ. |
| Dimension 4 (c-type): flavour speed spread (3 new structures, not removable by OBS-3's two counterterms, count.out:2) | modulated walker hop η | 2η (light.out:33-37) | ×1.7×10²⁷ over IceCube 3.9×10⁻²⁸ |
| The same, from the filter modulation | κ, through the hw3 admixture | ≈ κ²(1+O(κ)) (light.out:38-42) | ×2.8×10²⁶ |
| The same, regenerated at one loop when the tree terms are set to zero | toy on-site pairing Yukawa y(x) = y₀ + y₁Σcos(K·x) | coefficient 0.147·(y₀−y₁)y₁ (loop2.out:2-5); spread 2.3×10⁻⁵ at a B-gen-like phase of 0.07 rad (loop4.out) | ×6×10²² |
| Gauge couplings | — | unchanged: every mixing partner has the same G_SM charges, so the Ward identity fixes the charge (proved) | within bounds |
| Light four-fermion terms, including ΔB = 1 (16⁴ ∋ qqql) | W(2κ)⁴a² | — | proton decay safe by 5×10⁷ at M_Pl, by ×10² at 2×10¹⁶ GeV (suggested) |

## The price, with sizes

1. **A named structure, Θ** (a lattice CPT, with S even under it). By AX:169-171, K/CPT structure is downstream of the axioms, so this is extra structure, not axiom content. Without Θ, the dimension-3 coefficient must be tuned to about 2×10⁻⁴³ (at M_Pl) or 1.5×10⁻⁴⁰ (at 2×10¹⁶ GeV).
2. **Tuning.** Three new corner-off-diagonal c-type counterterm structures, probably needed per SM field (about 18; suggested). Each must be tuned to about 6×10⁻²⁸ of its tree-level natural size, or 2×10⁻²³–4×10⁻²⁶ of its one-loop size.
3. **Conditions from (ii).** κ ≲ 0.55, and no gapless composite at the light corners. If such a composite does exist, κ must be ≲ 8×10⁻²⁹.

**No part of the f range (fa ≥ 0.026) passes untuned** (bounds.out).

## Comparison with the supervisor's own thread (read after all results)

- **Agreed:** the BCC labels; single handedness per sector; the anomaly-free sector; unchanged gauge couplings.
- **Wrong in the supervisor's thread:**
  - Lemma S does not keep the zero. Cubic symmetry allows three corner-mixing structures that split the flavour speeds, and the loop regenerates them.
  - θ goes into the composite partner, not into hw3, and the light modes couple at first order in κ.
  - The supervisor predicted SAFE or a mild PRICE.

## Deviations (`PREREG_FOLLOWUP_2026-10-15.md`)

- The spin-density term P-b failed the cubic-symmetry check and was dropped.
- The first direct-diagonalisation θ mixed degenerate zero modes. It was replaced by a degeneracy-safe measurement.
- The count run hit the 0.4 GB cap because of a full SVD, and was rerun with an economy SVD. The killed log is kept.
- Added after the PREREG: the literal model, the structure count, the one-loop toys and the index check.
- The NT-3-style ED proxy was not run.

## Scope

- **Model:** 3D, continuous time, free-fermion one-body level per Spin(10) component.
- **Mirror gap:** a static auxiliary partner, either at every site (Model A) or only in channels above threshold (Model B).
- **Numerics:** folded-zone k-space, cross-checked against real-space tori with L = 4 and 6 to 3×10⁻¹⁴.
- **One-loop work** is a toy: real iσ_y pairing, free internal lines, BZ grids N = 48–96, m_H = 0.05–0.1. It drifts about 5% with N.
- **Not covered:** many-body SMG; extending Θ to the gauge links (suggested only); B-gen's actual vertex spin structure.
- **Bounds:** IceCube was fetched (arXiv:1709.03434, Table 1). The quark rows are OBS-3's as printed. The proton-decay and neutrino-mass scales were recalled.

## Files (`campaign/CLS1/`)

- `PREREG.md`
- `PREREG_FOLLOWUP_2026-10-15.md`
- `scripts/`:
  - `cls1_core`, `cls1_labels`, `cls1_light`, `cls1_theta`, `cls1_count`, `cls1_bounds`, `cls1_loop`, `cls1_loop2`, `cls1_loop3`, `cls1_loop4`, `cls1_index`, `cls1_archive` (`.py` and `.out`), including `count_run1_memcap.out`;
  - `cls1_archive.npz`, `cls1_light_archive.npz`, `cls1_theta_archive.npz`.
