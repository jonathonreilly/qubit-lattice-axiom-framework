# OBS-3 report: is X2's flavour-pattern Lorentz violation forced by CKM?

**Reading: TEXTURE-ESCAPE.** At one loop the observed CKM does not force X2's flavour-pattern Lorentz violation: the minimum residual over the family is exactly zero. The escape is structural, not tuned.

**Limits of the escape.**
- It fails if the up sector must be flat and the corner couplings carry the mass pattern. Then no structural zero exists, and a zero needs tuning to about 10⁻¹⁵.
- The forced version comes back at two loops (suggested).

**Provenance.**
- **Worker:** Claude Opus 5.5 at xhigh. Same family as the supervisor, X2, OBS-1 and OBS-2; unrefereed.
- **Window and resources:** 11:54–13:10Z on 2026-10-15. Peak memory 76 MB, one process at a time.
- **PREREG:** written 12:09Z, before any run. Dated follow-ups are in `PREREG_FOLLOWUP_2026-10-15.md`.
- **This file:** the harness blocks subagents from writing REPORT.md, so the supervisor saved it from the worker's final message, lightly condensed. Every number and file reference is the worker's.

## Plain words

1. **The d-quark result was a choice of texture.** OBS-2's d-quark Lorentz violation (2×10⁻⁸ against 10⁻²²) comes from its Yukawa texture, not from CKM.
   - At one loop, a corner's speed shift depends only on the moduli of the corner couplings.
   - Quark mixing and CP violation live in the phases.
2. **The main construction (checked).**
   - Corner-basis Yukawa matrices for both sectors, with three equal diagonal entries and all six off-diagonal moduli equal.
   - With free phases, they reproduce every quark mass ratio, every |V_ij| and |J| exactly.
   - Every corner then sees the same speed shift. After the allowed per-field counterterms every row is zero: c̊ and d̊ for u and d, the anisotropic c⁽⁴⁾₃₃ rows next to them in D44 part 3, the heavy-quark rows and the electron rows.
   - This holds for every regulator, placement, symbol range and carrier model.
3. **The origin of OBS-2's residual.** OBS-2 gave each corner its own Yukawa coefficient, which breaks the law's cubic symmetry explicitly (OBS-2 REPORT:67).
   - If the law's couplings respect the cubic symmetry and flavour breaking lives only in electroweak-scale vacuum values, the symmetric-phase loops never see the flavour pattern, at any order (proved).
   - What remains is suppressed by about (v·a)², roughly 10⁻³⁴ (suggested).
4. **What CKM does force.**
   - The up and down embeddings cannot both be unbiased to the corner basis unless CKM is a disguised circulant (proved). The observed CKM is not one, at 31σ.
   - Some product of the two sectors' Yukawa matrices must carry corner-dependent data (proved).
   - If such products enter the velocity at two loops, the violation would return at about 10¹³ times the u/d bound (suggested estimate).
   - If the up sector is held flat and the corner couplings carry the mass pattern, there is no structural escape (proved). The fixed rows then vanish only on a hypersurface tuned to about 10⁻¹⁵.

**Scope.**
- Physics: one loop; X2 walker on Z³ in continuous time; symmetric-phase nearest-neighbour Higgs; the family as built; no running from 1/a.
- Numerics: loop tables at N = 48 and 96; m0 = mH ∈ {0.1, 0.05, 0.025}; Δ ∈ {0, 0.5}.
- Variants covered: sym/int/ext placements; trace and selective splits; range-1 and range-2 symbols; carrier models M1 and M2; low-scale and ×0.45 Yukawas.

## Reading (FIXED, TESTS.md:393-410)

**TEXTURE-ESCAPE.**

**The minimising realisation, "B-gen"** (`univ.out:10-45`, `univ_B_gen.npz`).
- **Fit:** exact, with χ² = 7×10⁻²³, all pulls ≤ 10⁻¹¹ and |J| = 3.116×10⁻⁵.
- **Moduli:**
  - |Y_u|/y_t: diagonal 0.3331, off-diagonal 0.3334;
  - |Y_d|/y_b: diagonal 0.3311, off-diagonal 0.3346.
- **Phases:** the off-diagonal phases are about 0.04–0.10 rad and depend on orientation.
- **Rows checked:** the as-printed D44 part-3 rows (u at 3×10⁻²³, d at 10⁻²²; Schreck 2017*, `ref_OBS2/paper.tex:10426-10441`) and the electron rows.
- **Result:** with universal data every residual is zero by Lemma S (proved, §1). Numerically, max |residual|/|universal shift| ≤ 6.8×10⁻¹⁴ over the whole bracket, all carriers and both symbol ranges (`univ.out:45,117`, `r2check.out:2`). That is roundoff.

**Precision caveat.** The printed fixed-row "ratios" of 10²–10⁴ for these realisations are roundoff, not physics: double precision cannot resolve 10⁻²² against universal shifts of about 10⁻³. The zero is an identity.

**A second universal fit, "B-gen120"** (diagonal phases spaced 2π/3), also fits exactly (`univ.out:82-117`).

**The symmetric version fails** (checked over 400 starts; not proved impossible).
- Equal-modulus textures with symmetric off-diagonals, which is what on-site carriers give, cannot fit: the best χ² is 4.7×10³, with J only 1.2×10⁻⁷ and V_cb 0.010 (`univ.out:46-56`).
- This matches the USY literature: universal-strength textures fit the CKM moduli but not the size of CP violation (arXiv:1101.5808, abstract only).
- B-gen works because its phases depend on orientation. That needs orientation-selective τ_xσ_c carriers of range ≤ 2, which the family allows.

## 1. Structure: what enters

**S1 (proved).**
- Unit translations conserve the corner label, so the Lorentz-violating kinetic terms are corner-diagonal.
- The D2 subgroup fixing every hw1 corner makes each corner tensor diagonal.
- A mass eigenstate gets Σ_c |W_ci|² T(c,a) for left-handed fields, with |X_ci|² for right-handed ones.

**S2, the one-loop formula (proved; symmetric phase, no carrier mixing).**

T_L(c,a) = Σ_{s,s′} Re(η_s η̄_s′) I_{ss′}(c,a) + Σ_{c′≠c} w_{cc′} K(c,c′,a)

- The η are the Higgs symbol coefficients. They are fixed only by the corner-diagonal entries Y_cc and the symbol choice: on-site part, selective, range-2 split.
- The weights are w_{cc′} = Σ_A |λ^A_{cc′}|² ≥ |Y_{cc′}|², by Cauchy–Schwarz with Σ_A v_A² ≤ v².
- Q sums the u and d sectors; u^c and d^c use the transposes, times 2.
- **Only moduli and the diagonal Gram matrix enter. The phases of the off-diagonal entries never do. This is the escape route.**

**New exact identity (proved by q → q+Q plus σ_c spin conjugation; checked to 8.3×10⁻¹³ over N = 32–96 and the bracket, `structure2.out:1`).**
- For covariant on-site carriers, K(c,c′,a) = I₀₀(c′,a): the carrier loop equals the Higgs kernel of the internal corner.
- Hence T_L(c,a) = κ_⊥ (YY†)_cc + Δκ |Y_ca|².

**When only (W y² W†)_cc enters.** In the on-site carrier class: a constant diagonal from the on-site Higgs, plus on-site covariant carriers at hw2.
- The per-corner isotropic part is exactly κ̄ (W y² W†)_cc, summed over sectors for Q; for right-handed fields it is (X y² X†)_cc.
- The per-corner anisotropic part sees the individual |Y_ca|², weighted by Δκ.
  - Δκ is 0 at Δ = 0, by staggered reflection (`structure2.out:2,4,6`).
  - Δκ is 2.2–3.8×10⁻⁴ at Δ = 0.5 (`:3,5,7`).
- In OBS-2's M1, the off-diagonals are not in the loop, so only Y_cc enters. With corner-dependent diagonals (selective symbols), their own kernels I_{cc′} enter.

## 2. The cancellation condition and the conjecture

**Lemma S (proved).**
- If the data are S3-invariant (the diagonal Gram matrix is invariant and all off-diagonal weights are equal), cubic covariance of the loop makes T(c,a) = α + βδ_ac. The residual is then identically zero.
- In the on-site class this is also necessary (proved algebra; generic Δκ, κ̄ ≠ 0): zero residual if and only if |Y|∘² = oJ + (d−o)·1, i.e. one common diagonal value d and one common off-diagonal value o.

**Lemma F (proved).** After the speed counterterm, the isotropic row of eigenstate i is Σ_c (|W_ci|² − 1/3) ρ_c, where ρ_c is the per-corner isotropic residual and Σ_c ρ_c = 0. A flat column therefore has a zero isotropic row for any loop data.

**The conjecture is proved in both directions:** W_u and W_d are both flat if and only if V_CKM is equivalent, under rephasing and permutations, to a circulant.
- **The elementary 3×3 step:** in a dephased Hadamard matrix, 1 + a + b = 0 with |a| = |b| = 1 forces {a, b} = {ω, ω²} (`algebra.out:4-5`).
- **Classification:** Haagerup 1997 (in *Operator Algebras and QFT*, Rome 1996, International Press, pp. 296–322); catalogue in Tadej–Życzkowski, quant-ph/0512154.
- **Forward direction:** V = D P F†(monomial)F P′ D′, a circulant times a monomial matrix.
- **Converse:** W_u = F P₁†D₁† and W_d = F C P₂ D₂ realise any circulant-equivalent V.
- **Prior art on main:** `QUARK_C3_CIRCULANT_SOURCE_LAW_BOUNDARY_NOTE_2026-04-28` (as cited by `CKM_SMALL_VS_PMNS_LARGE…NOTE_2026-06-06`). It covers the special case in which two Hermitian circulants give a permutation CKM.

**The observed CKM is not circulant-equivalent (checked).** Such a matrix has a Latin-square moduli pattern. The PDG 2024 direct values (recalled) fail it:
- smallest entries of the rows: |V_ub| = 3.82(20)×10⁻³ against |V_cb| = 41.1(1.2)×10⁻³, a 30.6σ gap (`algebra.out:8`);
- middle entries: 152σ.

**But the conjecture is not a lower bound.**
- **Realisation E1** makes both first-generation columns flat with the observed CKM: |W_u1|² and |W_d1|² flat to 10⁻¹⁶ (`escape.out:2`).
- **Its cost (checked):**
  - the heavy columns are then ≥ 0.283 from flat (`escape.out:1-2`);
  - the anisotropic u/d coefficients come out at about 10⁻⁴, failing the c⁽⁴⁾₃₃ rows by 10¹²–10¹⁷;
  - the u DIS row is reached at up to 1.2×;
  - charm and top isotropic shifts are ±1–2×10⁻³ (`escape.out:20-49`).
- So E1 escapes only the fixed rows, while B-gen escapes everything.

## 3. Minimum over the family

**Full family: minimum = 0, structural (proved; checked).** Three independent routes reach it:
- **B-gen and B-gen120:** all rows, both carrier models, any kernel.
- **M1 diagonal equalisation:** free right-handed rotations make the corner-diagonal Yukawas constant for any W_u, so every row vanishes in M1 (`univ.out:2-7`). This includes OBS-2's own branch-B left embeddings, W_u = F and W_d = FV. **OBS-2's −2×10⁻⁸ is removed by a d^c rotation alone.**
- **E1 (flat light columns):** fixed rows only, at the costs listed in §2.

**Restricted to "up sector flat".**
- **Bounds (proved):** max_c ||W_d,c1|² − 1/3| ≥ 0.1206 (a scan gives 0.1221), and the b column is ≥ 0.0219 from flat (`algebra.out:18-20`, `upflat.out:1`). So the down-row sums are non-universal by at least 0.0219 y_b² (`structure2.out:8`).
- **M1:** minimum 0, structural (diagonal equalisation, `univ.out:2-3`).
- **M2** (the couplings carry the mass pattern): no S3-invariant realisation exists (proved), so there is no structural zero.
  - **On-site class.** The Q part of the d row is κ̄⟨δ^d, R^Q − R̄⟩, independent of the kernel. It changes sign over the generation phases (checked, `structure2.out:8`), so a zero needs tuning to about 2×10⁻¹⁵. The d^c part needs X_d1 to be flat together with a constant diagonal; that joint condition was not checked.
  - **Selective-symbol class.** Tuned zeros exist at single bracket points. Powell minima of the primary-point ratio are 0.04–4 (`upflat.out:8-13`).
  - **Best bracket-robust value found: 6.5×10⁹.** Powell is a local search, so this is an upper bound on the minimum, not a lower bound.
- **Conclusion:** within up-flat M2, the residual is CKM-forced unless tuned to about 10⁻¹⁵.

## 4. Mechanisms outside the family's literal textures

1. **A cubic-covariant law with flavour breaking only in vacuum values.** Proved for the symmetric-phase effective action at all orders.
   - Covariant couplings and propagators give U Σ(p) U† = Σ(Rp). So T is a cubic tensor field, and the residual is zero for any vev pattern.
   - This is consistent with X2-L8, which already puts the CKM-forced breaking in the vacuum.
   - Breaking enters only through vev insertions, at about y²(v·a)² ≈ 10⁻³⁴ for a = ℓ_P and about 10⁻²⁸ for a = 600 ℓ_P (suggested).
   - **Price, not computed:** the extra electroweak-doublet carriers at hw2 momenta have O(y_t) flavour-violating couplings, which raises a tree-level FCNC question (suggested).
2. **A Higgs degenerate at the corner-difference momenta.** By the K identity this is the same as the on-site carrier class. It produces the (W y² W†)_cc structure but is not an escape by itself.
3. **Main's velocity-RG attractor** (`EMERGENT_LORENTZ_INTERACTING_VELOCITY_RG_ATTRACTOR_NOTE_2026-06-06`, conditional). It gives only logarithmic suppression, not an escape.

## 5. What CKM forces (companions to X2-L8)

**L-words (proved).**
- If [H_u, H_d] ≠ 0, the unital *-algebra they generate is M₃ or M₂⊕C. Both contain a rank-1 projector onto a non-flat vector.
- So some word in H_u = Y_uY_u† and H_d has a corner-dependent diagonal.
- Any Lorentz-violating channel that resolves all such words with independent kernels is therefore forced to be non-universal by CKM.

**Two-loop size (suggested).** The spread across corners of the words in B-gen (`structure2.out:10-16`):

| Word | Spread across corners |
|---|---|
| H_u + H_d | 6×10⁻¹⁷ (zero) |
| H_u² | 1.6×10⁻⁵ |
| H_uH_d + H_dH_u | 4×10⁻⁷ |

A two-loop coefficient of about κ̄² ≈ 1.3×10⁻⁴, projected through δ^u ≈ 0.3, gives about 10⁻⁹–10⁻¹⁰. That is about 10¹³ over the u/d rows, unless the couplings are law-level and covariant (mechanism 1).

## Controls (all passed)

- **OBS-2 reproduced.** c_TT^d = −2.10666612×10⁻⁸ and d_TT^d = +7.0222204×10⁻⁹ at N = 24, m0 = 0.1, Δ = 0, matching OBS-2's digits. OBS-2's referee obtained −2.10666629×10⁻⁸, a relative difference of 8×10⁻⁸. Δ = 0.5 also matches (`ctl.out:1-4`).
- **Circulant inputs** give residual/universal ≤ 2.9×10⁻¹⁴ in both M1 and M2 (`ctl.out:7`).
  - Side note: non-Hermitian circulants are only C3-invariant. Their per-corner isotropic residual is 6×10⁻¹⁶, but in M2 a transverse residual of 3×10⁻⁴ relative remains (`ctl.out:8`).
- **Cubic covariance:**
  - archived tables to 1.3×10⁻¹⁴ (`ctl.out:5`);
  - flavon table to 3.5×10⁻¹⁵ (`:6`);
  - assembly under the corner 3-cycle to 3×10⁻¹⁵ (`:9`);
  - range-2 tables to 1.2×10⁻¹⁴, with entries shared with OBS-2's tables identical (`r2_ctl.out`).

## Deviations (all in PREREG_FOLLOWUP_2026-10-15.md)

- **The u row.** The as-printed u row is 3×10⁻²³. TESTS says "1e-22 as printed", and the printed value governs.
- **Placements.** For right-handed fields the int and ext placements are swapped, a refinement of OBS-2's convention. The sym placement is unchanged.
- **Added after the PREREG:**
  - the M1 diagonal equalisation;
  - the equal-modulus fits;
  - the kernel identity;
  - the two-loop word diagnostics.
- **Bugs.** The C3b and r2check bugs were fixed before any reading.
- **Inputs not fetched.** PDG 2024 masses and CKM values were recalled, not fetched. The USY literature was read at abstract level only (Branco–Silva-Marcos–Rebelo 1990; arXiv:1101.5808; Kalinowski–Olechowski).

## Files (`campaign/OBS3/`)

- `PREREG.md`, `PREREG_FOLLOWUP_2026-10-15.md`.
- In `scripts/`:
  - `obs3_core.py` (assembly);
  - `ctl`, `escape`, `upflat`, `univ`, `structure2`, `algebra`, `r2check` (`.py` / `.out`);
  - `yuk_lv3.py` with `run_r2.sh` (range-2 tables);
  - `tables/`: OBS-2's tables plus the new `yuk3_*`;
  - `escape_E1_Wu.npy`, `univ_A_M1.npz`, `univ_B_{gen,sym,gen120}.npz`, `upflat_results.npy`;
  - `obs3_archive.npz` (63 arrays).
