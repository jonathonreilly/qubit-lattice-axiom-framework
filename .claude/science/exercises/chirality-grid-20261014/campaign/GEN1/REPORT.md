**Provenance:** the worker's final message, saved verbatim by the supervisor.

# GEN-1 report: where to put the three generations (X2′)

**Reading: GEN-CONE(n).** Items a1–a5 hold. Under the PREREG's literal rule n = 0. In the two-sided robustness variant n = 2; using the one-loop equality of coefficients the minimum is 1. Removing every one-loop flavour-pattern term in every field takes at most 8. Every count is ≤ 8, so the reading does not depend on which count is used. Panel E predicted n ≈ 7.

**Provenance.** Claude Opus 5.5 worker, the same model family as panel E and the OBS/CLS workers, so not independent; unrefereed. Ran 11:23–11:46Z on 10-17. PREREG written 11:37Z, before any run. Peak memory 252 MB, one process at a time. Nothing of mine is still running; the QMC `runner.py` processes belong to another agent.

## Plain words

1. **Putting all three generations at the one fully symmetric corner (k = 0, called Γ), as an internal label, removes the corner package's flavour problems.** Quark mixing (CKM) becomes unconstrained, exactly as in the Standard Model. There are no extra Higgs doublets, so no tree-level flavour-changing neutral currents beyond the SM's. No lattice-scale symmetry breaking is needed, and no first-order strain channel exists.
2. **The light-particle protection survives at Γ.** The interaction that gaps the mirrors still never touches the light modes. This is exact and checked.
3. **The 7-corner mirror has no extra anomaly once the 16th component (ν_R) is included.** The same short argument also closes X2's "cheapest open kill" for the 5-corner mirror. ν_R is still forced, as in X2.
4. **The price is one-loop Lorentz violation that no texture can avoid.** The u and d quarks get speed shifts that differ by 6e-8 to 9e-7, about 10¹⁴–10¹⁵ times the clean bounds.
   - If both signs of each quark-speed row are enforced, two extra counterterms built from the law's own Yukawa matrices remove it. They must be tuned to about 1e-16–1e-15.
   - Under the rows exactly as printed, which are one-sided, the per-field counterterms alone pass by making the d quark slightly slower than light (about 1e-6). I would not lean on that loophole (see b).
5. **Costs:** 96 modes per site; the "3" is put in by hand; and a lattice CPT-type symmetry becomes necessary to forbid flavour-dependent energy offsets (side finding 2).

## Results

Path prefixes: S = `campaign/GEN1/scripts/`, CH = the exercise packet.

**(a1) holds (proved; checked).** Exact translations give a Yukawa selection rule Γ + Γ + 0 = 0 for every generation pair, and the cubic rotations do not act on an internal label. So Y_u, Y_d and Y_e are arbitrary complex 3×3 matrices, i.e. the SM Yukawa sector. Rebuilding the OBS-3 PDG-2024 inputs reproduces masses to 2.9e-12, |V| to 1e-15 and J exactly (S/assembly.out:4, :40).

**(a2) holds.**
- **X2-L1 (proved).** The Γ sector holds 3 nodes per component, all of one chirality (index 3). No translation-invariant bilinear can gap it: Dirac pairing needs opposite chirality, and Majorana pairing is excluded because 16⊗16 has no singlet, and also by Z₄^F.
- **X2-L2 (proved; checked).**
  - f_Γ = (3 − Σcos p)/2 vanishes only at Γ; its minimum at |k| > 0.3 is 0.024 (S/symm.out:3).
  - It is a 7-site star, A1g and translation-covariant (≤ 9.9e-16; :5).
  - Fock check (L = 2): |[H, ψ(Γ)]| = 0.00, against 6.05 at the mirror corners and 0.155 for the unfiltered control (:6-7).

**(a3) holds.**
- **(i) Cyclic Z₁₆ gate (checked).** With d = 16 every g·i^F gives ν = 0. At d = 15 the 7-corner mirror gives ν = 3 or 11 (S/symm.out:11-12), so ν_R is forced, as in X2.
- **(ii) Mixed Z₂³ anomaly (proved, conditional on comparator).**
  - At each corner, a translation multiplies every field by the same sign (−1)^{g·c}, so Z₂³ acts through fermion parity.
  - A Z₂³ background therefore only twists the Spin-Z₄ (or Spin×_{Z₂}Spin(10)) structure. Each corner's anomaly is then the pullback of the pure anomaly of 16 × 3 Weyl fermions, which is zero because 48 ≡ 0 mod 16.
  - This rests on comparator bordism values: Ω₅^{Spin-Z₄} = Z₁₆, and the vanishing anomaly of the Spin(10) 16 (García-Etxebarria–Montero 2018, recalled, not fetched).
  - The Spin(10) instanton 't Hooft vertex is trivial (4 zero modes per 16; :17).
  - The same argument clears X2's 5-corner mirror (CH/combos/X2/COMBO_REPORT.md:252).

**(a4) holds (proved; checked).** Γ's little group is the full cubic group O. Neither End(C²) nor the pairing space contains the traceless-strain representation E + T₂: multiplicity 0, against 2 at an hw1 corner (S/symm.out:20-21). Flavour is internal, so this holds for any CKM. X2-L8's mechanism (COMBO_REPORT:126-136) needs the point group to act on generations, and here it does not.

**(a5) holds (proved; tree level).**
- With one doublet, the Higgs couplings are M/v: natural flavour conservation (Glashow–Weinberg). Walker and links are flavour-blind.
- Momentum conservation keeps every internal line of a tree diagram with light external legs near Γ. Mirror modes and lattice-scale Higgs modes therefore cannot appear at tree level.
- The 10-vector channel couples to light pairs only through f_Γ² ∝ (qa)⁴, so the first non-SM ΔF = 2 terms are dimension ≥ 14 (suggested size: negligible).
- Scope: assumes the mirror sector is gapped with no light composites (L_X2′, inherited).

**(b) One-loop Lorentz-violating residual.**
- **Kernel (checked).** OBS-2's model (`OBS2/scripts/yuk_lv.py`) evaluated at Γ, with the mirror proxy m0 + Δf_Γ.
  - κ_Γ = −0.01115 to −0.01164 per y² for on-site vertices, over N = 48/96, m0 = mH ∈ {0.1, 0.05, 0.025} and Δ ∈ {0, 0.5}. It drops to −0.0039 with a Γ-selective vertex (S/assembly.out:1). N drift is ≤ 1.4%.
  - Isotropic to ≤ 1e-14 (S/gk_*.out).
  - Control C1: at Δ = 0 it equals OBS-2's archived Γ table to 0.0 relative (S/ctl_N48_m0.1_D0.out). So panel E's use of the hw1 kernel was numerically right.
- **Structure (proved; symmetric phase, flavour-blind internal lines).** The speed matrices are Q: κ(H_u + H_d); u^c: 2κY_u†Y_u; d^c: 2κY_d†Y_d; L: κ(H_e + H_ν); e^c: 2κY_e†Y_e.
- **No structural escape (proved).** With any set of Yukawa vertex symbols, a kernel-independent zero needs H_u + H_d ∝ 1. That forces CKM to be a permutation. So OBS-3's texture-escape mechanism does not exist here. The residual is fixed by masses and CKM alone: it does not depend on the generation basis, to 1e-47 (C3).
- **Residual after per-field counterterms** (variant B: two-sided per component, defined at 11:40Z before the assembly run; :8, :19, :30, :44, :55, :66):

| | low-scale Yukawas | ×0.45 |
|---|---|---|
| d_L − u_L spread | 2.9e-7 – 8.7e-7 | 5.9e-8 – 1.8e-7 |
| worst clean-row ratio | 1.1e15 – 3.4e15 | 2.3e14 – 6.8e14 |

- **Counting n** (spurion basis, PREREG rule):
  - H_u alone leaves ×1e11–1e12, and H_d alone changes nothing (:10-11), so B needs **n = 2** on Q, which gives a residual of 1e-34.
  - With the one-loop equal coefficients, the single structure H_u + H_d suffices: n_min = 1.
  - **Tuning:** the H_u coefficient to 3e-16 – 4.4e-15 relative to κ; the H_d coefficient to 1e-12 – 1.5e-11 (:14, :72).
- **Literal PREREG rule (variant A):** zero residual with no flavour counterterms, so n = 0. It works only because c̊ is one-sided as printed: d̊ is set to 0 by matching right- to left-handed speeds, and c̊^d ≈ +(0.6–8.7)e-7 is subluminal (:7). I have not checked whether other data exclude subluminal quarks at that level.
- **n_all ≤ 8 (proved).** The 8 linear structures {H_u, H_d; Y_u†Y_u; Y_d†Y_d; H_e, H_ν; Y_e†Y_e; Y_ν†Y_ν} remove all one-loop dimension-4 terms exactly. No non-covariant or anisotropic structure is needed.
  - Heavy-flavour rows (mapping suggested; not evaluated against bounds) still carry, after per-field counterterms: t at −1e-2, b and c above their OBS-2 rows, and ν_τ–ν_μ speed splits of about 1e-7–1e-6 from H_e. Those need H_e on L.

## Compared with X2-corner (comparator: refereed records)

| | X2 corners | X2′ |
|---|---|---|
| CKM | needs hw2 carriers or translation breaking (CH/TESTS.md:471) | free (a1) |
| Tree ΔF = 2 | about 1.3–7.9e3 TeV needed untuned; KILL-level for X2 as written in the tested D3 benchmark (OBS-4 verdict); PRICE only via class S | SM-only (a5) |
| Class S | Θ plus about 1e-27 tuning (CLS-1) | not needed |
| First-order strain | forced; clock row ×0.09–2.5 | absent (a4) |
| One-loop LV | structural zero (B-gen), but only with the FCNC-priced carriers | ×1e14–1e15; n = 2 covariant counterterms, tuned to about 1e-16 |
| Matter per site | 32 modes | 96 modes |

## Side findings
1. **Two-loop (suggested).** Non-linear words (H_u², …) carry a spread of about κ²y_t⁴|V_td|² ≈ 1e-8. Each order needs its own counterterms.
2. **Flavour-dependent energy offsets (dimension 3).** An on-site term ψ_i†μ_ijψ_j is allowed by translations, cubic rotations and Spin(10) (proved). It is zero at one loop in this model by construction. Excluding it to all orders needs a Θ-type lattice CPT symmetry of the full law, which has not been checked. This is the named structure CLS-1 priced. In X2 corners the cubic symmetry of the law makes the leading such term flavour-universal.

## Deviations (PREREG_FOLLOWUP_2026-10-17.md)
- Variant B was added after the kernel runs and before the assembly run.
- The method for a3(ii) changed: the planned AHSS exponent bound needed unverified Ω₂ and Ω₃ values, so I used the twist argument.
- The identity-component part of control C2 holds by construction, so it was not run.
- Inputs (PDG masses and CKM, IceCube-type and heavy-row mappings, bordism values) were recalled, not fetched.

## Files (`…/chirality_ex/campaign/GEN1/`)
- `PREREG.md`, `PREREG_FOLLOWUP_2026-10-17.md`
- `scripts/gen1_kernel.py`, `scripts/run_kernel.sh`, `scripts/gk_N*_m*_D*.out` and `.json` (12 runs), `scripts/ctl_N48_m0.1_D0.out`
- `scripts/gen1_assembly.py`, `scripts/assembly.out`, `scripts/gen1_assembly_archive.npz`
- `scripts/gen1_symm.py`, `scripts/symm.out`
- `scripts/capped.sh`