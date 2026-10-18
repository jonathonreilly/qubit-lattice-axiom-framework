**VERDICT (same-family referee, Claude Opus 5.5; not independent): CONFIRMED WITH CORRECTIONS.** The reading is G-OUTSIDE, within contents A/B/C (κ ≥ 0.1, b ≤ 35). My independent script is `.../scratchpad/hier/ref_H3/chk.py`. It uses closed-form two-loop Λ, imports nothing from `rgcommon.py`, and peaked at 69 MB.

**1. Two-loop window: CONFIRMED.**
- I reproduced every edge to 4 digits:
  - pure SU(3), b=1: 0.1684–0.1890;
  - SM-like (n_f=6), b=1: 0.2690–0.3024, b=35: 0.2941–0.3346;
  - X2′ at κ=0.1, b=1: 0.2780–0.3139, b=35: 0.3050–0.3488.
- The scheme ranges match: Wilson β 34.6–38.5, heat-kernel 34.1–38.0.
- C1's best case of 5.47 decades (10.23 short) matches.
- The C5 numbers match: 1.289 and 1.981; ln ratios 12.73 and 20.00.

Corrections:
- **(a)** `TESTS.md:82`, "On the lattice this is β ≈ 35–38": this holds for pure gauge only. SM-like content needs a different β.
- **(b)** `REPORT.md:18`, "a scale ratio of 3×10⁵ to 5×10⁸, which is the hierarchy itself": wrong. That ratio is 5.5–8.7 decades *toward the UV*, finer than the grid. It is impossible on a coarsening ladder, and it is not the 16.7-decade hierarchy.
- **(c)** `REPORT.md:14`, "Every framework candidate has g² ≥ 1": C6 gives 0.237. The claim holds for value-carrying, non-circular candidates only.

**2. C1–C3 are one theory: CONFIRMED.**
- `ALPHA_S_DERIVED_NOTE.md:234-238` defines u₀, α_s(v) and α_LM as closed-form functions of ⟨P⟩ and α_bare = 1/(4π). −3 ln⟨P⟩ is trivially one too.
- They are therefore scheme estimates of the single β = 6 Wilson lattice, and its Λa is measured.
- The perturbative "best cases" are superseded by that measurement. The report says so.

**3. Non-perturbative β = 6: CONFIRMED, conditional.**
- Λ_MS·a = 0.602/(r0/a) = 0.120 using the repo's r0/a = 5.006, or 0.112 using the literature's 5.368.
- √σ·a = 0.233 from the certificate, or 0.219 from the literature.
- So colour sits at about 0.6–0.95 decades below M_Pl.

The conditions are not all stated in the report:
- The certificate is pure gauge (`r2.log:21`), so dynamical fermions are not included.
- a = 1/M_Pl is the B2 anchor. The axioms list "natural unit equals the Planck length" as open (`MINIMAL_AXIOMS_2026-06-29.md:189-190`).
- The data are for a Euclidean, isotropic action. A Hamiltonian or anisotropic action changes the result by O(1) factors.

**4. The 1/18 cap: CONFIRMED exactly (analytic).**
- On the register {1, D³}, the compressed Tr U_p is (1/9)Σ_{m,l}|u_ml⟩⟨w_ml|. Here u_ml has links 1,2 in flux and w_ml has links 3,4 in flux. The two families are orthonormal up to a norm of √3 and orthogonal to each other.
- So ‖T‖ = 1/3, and the maximum of Re Tr/3 = (T+T†)/6 is 1/18.
- No gauge-invariant plaquette loop fits in this register, because links 3 and 4 are traversed backward.
- I also confirmed by characters that the isolated ceiling is 1/3 when both orientations are allowed.
- The register is as described: `COL1/REPORT.md:74,107`.

Caveats:
- `COL1/REPORT.md:89` does not say the coefficients were chosen. The C4 "proved" part rests on axioms `:118-123` alone.
- "At least 10 qubits per link" uses the gauge-invariant isolated ceiling. For n ≥ 2 the cap over all four-link states was not computed, so that bound is a reading.

**5. Defects on main (nothing edited).**
- **Defect 2: CONFIRMED, reworded.**
  - `GAMMA_FULL_VS_GAMMA_CRIT_DECISIVE_NOGO_NOTE_2026-06-08.md:73-76` calls 0.019 "the MS-bar continuum value … smaller" than the β = 6 bare 0.08.
  - Converting the β = 6 bare coupling raises it instead: 0.1496 at one loop, 0.19–0.20 non-perturbatively.
  - The 0.019 is observed α_s run up to M_Pl (1/52.98). That is a different theory point, about β ≈ 28.
  - The note performs no explicit conversion. It misidentifies the coupling, so "wrong-sign conversion" should read "misidentification".
  - The guard needs re-checking. With β = 6 at M_Pl the no-go's weak-UV premise would be inapplicable, not "stronger".
- **Defect 1: CONFIRMED in substance, overcounted.**
  - The grid placement and the α_LM-at-M_Pl placement (`YT_BOTTOM_YUKAWA…:543`; `BOUGEROL_LACROIX_STAGGERED_BLOCKING_LYAPUNOV_BRIDGE_NO_GO_NOTE_2026-05-10.md:84`, the report's "BOUGEROL…:84" is ambiguous across four files) are the same scale read two ways.
  - The real incompatibility is the Planck placements against the QCD placements, which differ by 18.8 decades (C7).
  - Within the QCD placements, μ = v and 1/a ≈ 2 GeV still differ by about 2 decades.
  - Each placement is caveated on main individually: `ALPHA_S_DERIVED:211-215`, `ALPHA_S_SOMMER…:144-147`, `CONFINEMENT…:123-128`, `YT_EW…:156-158`. What is new is the size of the gap.
  - Main also carries two β = 6 values of r0/a that differ by 7%: 5.006 in the certificate and 5.37 at `CONFINEMENT…:107`.

**6. G-OUTSIDE vs G-UNFIXED: G-OUTSIDE is correct; G-UNFIXED is not the reading.**
- `TESTS.md:64` lists the g_bare = 1 convention as a candidate. It has no adjustable parameter, so it counts under the pre-registered definition (`PREREG.md:64-66`).
- C1 lands outside the window, and C6 also lands outside (3.4 decades on the weak side).
- G-UNFIXED requires that no candidate be derivable. That is false while C1 and the conditional Ward theorem stand.
- Correction to `REPORT.md:70`, "the single primitive … plus the colour-to-v link": that is two supplied items, not one. The 0.285 also cannot belong to observed QCD, which would then confine at about v. It needs a supplied extra confining sector.
- Prior art: the one-loop version is already on main (`HIERARCHY_VALUE_FRONTIER_PROBE_2026-06-05.md:161-171`).

**Strongest correct statement.**
- For SU(3) with pure, n_f = 6, or X2′ content (κ ≥ 0.1, b ≤ 35), colour transmutation reaches v·[0.1, 10] only for g²(M_cut) ∈ [0.168, 0.361] (two-loop MSbar, about ±6% in g² per decade).
- The framework's only non-circular coupling that carries a value is the single β = 6 Wilson lattice. Its tadpole forms are re-expressions of it.
- Given a = l_Pl (B2, open on main), the repo's own certificate puts Λ_MS ≈ 0.11–0.12 M_Pl and √σ ≈ 0.22–0.23 M_Pl. That is about 15 decades short of v and 19 decades above observed QCD.
- COL-1's register cannot represent ⟨P⟩ > 1/18.
- Reading: G-OUTSIDE.
- Dropping g_bare = 1 does not reduce the hierarchy to one number. It needs a supplied non-QCD confining sector with g² ≈ 0.285 ± 0.017, plus a supplied link to v.
- Escapes still open: mirrors below 0.1 M_cut (a supplied ratio), near-conformal walking, and non-perturbative N_f > 0.