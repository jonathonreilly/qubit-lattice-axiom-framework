**Provenance:** the worker's final message, saved verbatim by the supervisor.

**Reading: G-OUTSIDE.** Every candidate the framework has for the colour coupling where colour first exists lands outside the window, and far outside it. The only values that land inside are placed at a low scale by declaration, and that placement already contains the hierarchy. All four runs pass (R1 9/0, R2 8/0, R3 11/0, R4 4/0). Peak memory was 233 MB, one process at a time, nothing left running. This is a same-family result (Opus 5.5) and has not been refereed. The harness blocked me from writing REPORT.md, so this message is the only copy of the report.

## Plain summary

- **The window is narrow.** For the colour coupling to make a strong scale near v ≈ 2×10⁻¹⁷ M_Pl, g² at the cutoff (MSbar) must be:
  - 0.27–0.30 for SM-like colour (6 flavours);
  - 0.17–0.19 for pure SU(3);
  - 0.28–0.31 for X2′ with its mirrors one decade below the cutoff;
  - at most 0.36 anywhere, even if colour first lives on 35-site cells.

  On a pure-gauge Wilson lattice that is β ≈ 35–38. Moving one decade either way in scale corresponds to only about ±6% in g².
- **Every framework candidate has g² ≥ 1.** β = 6 and its tadpole-improved forms give 1.0–1.7, and all of them describe the same β = 6 lattice.
  - The repo's own β = 6 data give a string tension √σ = 0.23/a. On the Planck grid, colour therefore confines at about a quarter of the Planck mass. That is about 1 decade of hierarchy, not 16.7.
  - The most generous perturbative reading reaches 5.5 decades, still more than 10 decades short.
- **COL-1's cells fix no coupling.** Their Hamiltonian coefficients are free. As built, their one-flux link register caps the plaquette at 1/18, which is deep strong coupling.
- **Matching across rungs goes the wrong way.** Coarse-graining makes an asymptotically free coupling stronger, not weaker. Moving g² = 1 into the window would take a scale ratio of 3×10⁵ to 5×10⁸, which is the hierarchy itself.
- **If the convention g_bare = 1 is dropped**, the colour route needs two things supplied:
  - one number, g²(M_cut) ≈ 0.285 ± 0.017 (SM-like content, grid rung);
  - a mechanism tying the colour scale to v. With the observed QCD coupling, the colour scale sits 3.4 decades below v.

## 1. The window (task item 1)

Definitions were fixed in PREREG.md before any run. The cutoff is M_cut = M_Pl/b. The strong scale is the two-loop MSbar Λ; the four-loop Λ and the scale where α = 1 serve as robustness checks. The window is W_v: Λ/M_Pl ∈ [2×10⁻¹⁸, 2×10⁻¹⁶].

| Content | g² in W_v, b = 1 | g² in W_v, b = 35 | HIER-1 edge (10⁻¹⁵ of M_cut), b = 1 |
|---|---|---|---|
| Pure SU(3) | 0.168–0.189 (`r1.log:15`) | 0.184–0.209 (`:31`) | 0.198 |
| SM-like, n_f = 6 | 0.269–0.302 (`:35`) | 0.294–0.335 (`:51`) | 0.316 |
| X2′, mirrors at 0.1 M_cut | 0.278–0.314 (`:75`) | 0.305–0.349 (`:91`) | 0.329 |

- **(checked)** X2′ with its mirrors exactly at the cutoff is identical to the SM-like case (`r1.log:94`).
- **(checked)** Loop order and the choice of strong-scale definition move the edges by at most 1.8% (`:95-97`). Two-loop EW and top-Yukawa effects shift the scale by 0.012 decades (`:114`).
- **(checked)** The largest g² inside W_v anywhere is 0.361, i.e. α = 0.0287 (`:99`).
- **(checked; scheme ratios are comparators)** For pure gauge the window is β ∈ [34.6, 38.5] in the Wilson-bare scheme and β ∈ [34.1, 38.0] in the heat-kernel scheme (`:103-104`). These use Λ_MS/Λ_L = 28.81 and Λ_HK/Λ_W = 1.819 (PR #9702 `:206`).
- **(checked) Regressions** (`r1.log:2-8,111-112`). The runs reproduce:
  - the HIER-1 referee's one-loop edges, 0.208 and 0.403;
  - main's 42.8 and 52.4 (`HIERARCHY_VALUE_FRONTIER_PROBE_2026-06-05.md:161-165`);
  - main's 0.118233 (`ALPHA_S_DERIVED_NOTE.md:270`);
  - g₃(M_Pl) = 0.487, against main's 0.489 (`HIGGS_MASS_RETENTION_ANALYSIS_NOTE_2026-04-18.md:685`).
- **(checked)** The observed-QCD coupling at M_Pl, g² = 0.237, sits below the SM-like window. It gives Λ⁽⁶⁾ = 7.5×10⁻²¹ M_Pl, 3.4 decades too weak for v (`:113`). So "colour sets v" also needs a supplied technicolour- or composite-type link; SM-like content has none.
- **Prior art.** The one-loop version of this window is already on main (`VALUE_FRONTIER:72-96,159-171`). What is new here is two-loop running, thresholds, X2′ and the dependence on which rung colour first lives on.

## 2. Candidates (task item 2)

| # | Candidate | g² | Result | Label |
|---|---|---|---|---|
| C1 | g_bare = 1, β = 6 (a convention: `G_BARE_CANONICAL_CONVENTION…:27-28`; axioms `:188`) | 1.000 | best case 5.47 decades, 10.2 short (`r2.log:6`) | checked |
| C2 | the tadpole forms 1/u₀, 1/u₀², 1/⟨P⟩, −3 ln⟨P⟩ | 1.14, 1.30, 1.69, 1.57 | 3.5–4.9 decades, 10.8–12.2 short (`:7-14`) | checked |
| C3 | ⟨P⟩ = 0.5934, or the point estimate 0.59369 | feeds C2 | changes nothing (`:11-14`) | checked |
| C1–C3, non-perturbative | the repo's β = 6 certificate, r0/a = 5.006 | — | Λ_MS = 0.12 M_Pl, i.e. 0.92 decades and 14.8 short; still 13.2 short at b = 35 (`:23-33`) | checked; Λ·r0 = 0.602 is a comparator |
| C4 | COL-1 class-M cells | none | see below | proved / reading |
| C5 | rung 0→1 matching | — | one loop, pure gauge: g² = 1 becomes 1.29 at b = 5 and 1.98 at b = 35; bridging needs a Λ ratio of 3.4×10⁵ (pure) or 4.9×10⁸ (n_f = 6) (`:36-38`) | proved, one loop |
| C6 | α_s(v) placed at μ = v by declaration (B4, `ALPHA_S_DERIVED_NOTE.md:211-215`) | 0.237 at M_Pl | reproduces QCD (Λ⁽⁵⁾ = 0.215 GeV, 20.1 decades), so it is outside W_v; it also uses v as input | circular (`:41-44`) |
| C7 | the direct-Wilson-loop ruler r0 = 0.5 fm | — | a⁻¹ = 1.98 GeV, which makes the colour lattice 6.2×10¹⁸ grid spacings | circular (`:47-48`) |

"Best case" for C1–C3 is the most favourable perturbative reading: X2′ content, one loop, read as MSbar at μ = M_cut.

- **C1–C3 are one candidate (proved, by definition).** u₀, α_LM, α_s(v) and the plaquette coupling are all functions of ⟨P⟩ at β = 6 (`ALPHA_S_DERIVED_NOTE.md:233-239`). They are different estimates of one lattice theory, and that theory's scale ratio is measured.
- **C4, the cell coupling (proved at tree level).** Under the canonical normalisation the coupling belongs to each gauge point and plaquette. Cell size only lowers the cutoff to M_Pl/b, worth at most 1.54 decades for b ≤ 35. No value is derived: admissibility supplies no weights (axioms `:118-125`), and COL-1's spectrum used chosen coefficients (`COL1/REPORT.md:89`).
- **C4, what COL-1's register can hold.**
  - **(checked, exact)** On COL-1's link register {1, (3̄,3)}, ⟨Re Tr U_p⟩/3 ≤ 1/18 for every four-link state (`r3.log:8`). With both flux orientations the cap is 1/3 (`:9`).
  - **(reading, isolated plaquette)** Matching β = 6's plaquette of 0.5934 needs at least 10 qubits per link. Matching the window's plaquette of about 0.944 needs at least 22 (`:34-37`).

## 3. Decision (task item 3)

Every candidate that carries a value lands outside W_v in every reading: by at least 10.2 decades perturbatively and 13.2 decades non-perturbatively. C4 carries no value, and C6 and C7 are circular. By the pre-registered rule, the reading is **G-OUTSIDE**.

There is a stricter way to read the same facts. g_bare = 1 is a convention, and its "forced" form is conditional (`G_BARE_FORCED_BY_WARD…:41-66`). If only derived values count, the result is **G-UNFIXED**. The single primitive is then g²(M_cut) = 0.285 ± 0.017, to about 6%, plus the colour-to-v link.

**Supplied inputs** (all are comparators unless marked):
- M_Pl, which is B2;
- v, used only to define the target;
- α_s(M_Z) = 0.1180, α_em⁻¹ = 127.95, sin²θ_W = 0.23122, y_t(m_t) = 0.934 and m_t = 172.69, used only for the observed-QCD comparison;
- the four-loop β coefficients and the SM two-loop gauge matrix;
- Λ_MS/Λ_L = 28.81, Λ_MS·r0 = 0.602, and the plaquette coefficient 1.2208;
- the X2′ content (chirality `TESTS.md:652-720`).

## 4. Problems found on main (not edited)

1. **One β = 6 colour coupling is placed at four incompatible scales (checked, using only landed numbers):**
   - on the Planck grid, where it confines at about 0.23 M_Pl;
   - at μ = v, in the α_s lane;
   - at a = 0.1 fm (`ALPHA_S_SOMMER…:111-113`). `CONFINEMENT_STRING_TENSION_NOTE.md:123-128` flags this gap but not its size;
   - as α_LM at M_Pl (`YT_BOTTOM_YUKAWA…:543`, `BOUGEROL…:84`). Its Landau pole is already recorded at `YT_EW_COUPLING_BRIDGE_NOTE.md:156-158`.

   Observed QCD on the grid would need β ≈ 28 (`r4.log:7`).
2. **A scheme conversion has the wrong sign (checked).** `GAMMA_FULL_VS_GAMMA_CRIT_DECISIVE_NOGO_NOTE_2026-06-08.md:73-76` says β = 6's bare α of 0.08 corresponds to a smaller MSbar value, 0.019. In fact the conversion raises it, to 0.150 at one loop (`r4.log:1-2`). The β = 6 theory's own MSbar α at 1/a is 0.196–0.203 (`:3-6`). The 0.019 is a different theory point. That note's "false-escape guard" needs re-checking.

## 5. Open escapes

- **D-theory-type dimensional reduction (comparator).** There 1/g² grows with an integer extent, which swaps the coupling for a supplied integer.
- **Mirrors well below the cutoff**, giving a near-conformal stretch with 12 flavours.
- **HIER-1's escapes E1–E4.**
- **Non-perturbative N_f > 0 at g² = 1.** The repo has no data for this. For SU(3) with b₁ > 0, HIER-1's lemma caps it at 6 decades.

## Files

All in `.../scratchpad/hier/H3/`:
- `PREREG.md`, with two dated follow-ups;
- `rgcommon.py`;
- `r1_window.py`, `r2_candidates.py`, `r3_truncated_plaquette.py` and `r4_scheme_direction.py`, each with its log;
- `r1_v1.log` and `r4_v1.log`, from before a four-loop integrand rewrite that changed no numbers.

One line in `r2.log:41` is misleading. Its "inside band? True" compares C6 with the band pooled over all contents. On the pre-registered test, against C6's own content, it is outside (`:42-43`).