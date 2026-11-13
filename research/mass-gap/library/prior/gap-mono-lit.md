# Mean-plaquette literature guide

**Author:** OpenAI Codex, gpt-6-luna high (this session). **Purpose:** reading guide only; no proof step or status follows. **Sources read in full:** Engels and Scheideler, full text and captions of the 10-page preprint (plots not digitized). All other papers below were read only in the cited sections/pages. The Sussman–Alpoge raw files were fetched and searched, not read in full. Anything not read on its cited page is marked NOT READ.

## Repo search

- The lead's `library/prior/repo-search-2026-11-08.md` is absent in this checkout, and FINISH row 728 contains no “Repo prior work” block. Therefore there is no recorded lead search to report.
- This checkout is pinned at `a867197306ac4eab32466e4ab6fe86e92e9ad89c` and uses sparse checkout. I searched the lane’s `library/sa-index`, `library/open-registry.md`, `library/gap-phys-seed.md`, and FINISH row 728 plus rows 705, 708, and 727; the only exact target result was the queued reading task in `gap-phys-seed.md` lines 445-446. No prior literature note or other owner row for `gap-mono-lit` appeared.
- I fetched `origin/main` and the open YM4D PR heads #10114, #10133, #10134, #10141, and #10144, then searched them for `MONO-Delta`, “mean plaquette”, “interaction measure”, and `eps-3p`. No target-specific note was found. Broad archived references to plaquette observables are unrelated to four-dimensional Wilson SU(2) finite-volume Monte Carlo values or SU(2) thermodynamics.
- The target’s nearest scientific context is `gap-phys-seed.md` Section 3.2 and its Ising comparison; it motivates this literature guide but does not supply SU(2) data. `gap-seed-shape.md` reports a finite-volume free-energy derivative in terms of a plaquette difference, but it is not a data table for the requested lattice sizes.

## Source retrieval and reading log

- **Sussman–Alpoge:** fetched each requested raw source once to `/tmp/sa_ym4.tex` and `/tmp/sa_ca_I.tex`; searched target terms and checked indexed ranges only. The outline and CA-I account were not read in full. Credit Ethan Sussman and Levent Alpoge, with Claude and Codex as the authors of their text.
- **Engels–Scheideler (1996):** full preprint text and captions read from the open arXiv PDF; saved at `~/ym4d-papers/gap-mono-lit-engels-9610019/source.pdf`. Figures were not digitized.
- **Giudice–Piemonte (2017):** selected thermodynamics sections/pages read from the open arXiv PDF; saved at `~/ym4d-papers/gap-mono-lit-giudice-piemonte-1708.01216/source.pdf`. Rest of paper **NOT READ**.
- **Leme–Oliveira–Krein (2018):** Sections 5 and 6.1 read from the open arXiv PDF; saved at `~/ym4d-papers/gap-mono-lit-approx-dual-1703.07335/source.pdf`. Rest of paper **NOT READ**.
- **Nauenberg–Schalk–Brower (1981):** APS page refused access with “Authorization Required”; stopped there. Paper **NOT READ** and no values used.

## Index and target cross-check

The Sussman–Alpoge outline index has no entry for `MONO-Delta`, mean plaquette finite-size data, or the interaction measure. Its nearby indexed entries define the Wilson action and plaquette (outline chunk 02, 2094–2110; chunk 30, 32530–32538), but they are theoretical definitions rather than simulation tables. The account index for CA-I 4.12–4.19 also has no mean-plaquette or thermodynamics data. These sources do not cover this reading target. The two raw Sussman–Alpoge files were each fetched once as instructed; they were searched for these terms, not read in full. Credit Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, for the indexed outline and account. No material from them is used as an empirical value.

The target source says the four-dimensional Wilson SU(2) action is `S = β Σ_p (1 − ½ Tr U_p)` in `gap-phys-seed.md` lines 367–370 and asks for this literature guide in lines 445–446. Its Ising counterexample is a different model and cannot answer the SU(2) numerical question (lines 371–373). The open registry has no row for `MONO-Delta`, `gap-mono-lit`, mean plaquette data, or interaction-measure sign.

## Open Monte Carlo source checked

**J. Engels and T. Scheideler**, “The Pseudo Specific Heat in SU(2) Gauge Theory: Finite Size Dependence and Finite Temperature Effects,” arXiv:hep-lat/9610019 (1996), 10 pages. Open PDF saved at `~/ym4d-papers/gap-mono-lit-engels-9610019/source.pdf`. I read the full text (including all pages’ text and captions; plots were not digitized).

- Section 2, p. 2, Eqs. (2.1)–(2.3), defines the standard Wilson action and the average plaquette action `P = 1 − ½ Tr U_p` on periodic symmetric `N^4` lattices, with `N_P = 6N^4` plaquettes. This matches the target normalization.
- Section 2, p. 2, Eq. (2.4) defines the pseudo-specific heat as `−β² d⟨P⟩/dβ`. The paper reports that the mean plaquette was measured over β, but the text does not tabulate those means and errors.
- Section 3, pp. 5–6, Figure 3 and its caption compare `C_V` for `N = 4, 6, 8, 12, 16`. The figure reports the specific heat, not the requested `⟨P⟩ ± error`; no plaquette values with uncertainties for the requested common β grid are printed there. The stated reported peak values at β≈2.23 concern `C_V`, not the mean action.

This source therefore confirms a relevant Wilson SU(2) study at the requested volumes, but it does **not** supply the requested data table. I have not inferred plaquette values from the plotted derivative or treated a curve without reported errors as a data point.

## SU(2) thermodynamics source checked

**P. Giudice and S. Piemonte**, “Improved thermodynamics of SU(2) gauge theory,” arXiv:1708.01216v3 (2017), *Eur. Phys. J. C* 77, 821. Open PDF saved at `~/ym4d-papers/gap-mono-lit-giudice-piemonte-1708.01216/source.pdf`. I read the relevant parts, not the full paper: Section 3, pp. 10–14, Eqs. (19), (23), (25)–(29), and Figure 14 on p. 24; Section 4, pp. 14–15.

Equation (23) defines `Δ = ε − 3p`; Eq. (29) gives `Δ = 0` in the Stefan–Boltzmann limit. Figure 14 plots the SU(2) trace anomaly normalized by the Stefan–Boltzmann pressure limit over the studied temperature range, and its finite-temperature data are positive throughout that displayed range. Thus the literature sign reported here is **positive** at the temperatures measured, tending toward zero in the high-temperature ideal-gas limit. This is an empirical-literature statement, not a theorem for every temperature. The paper uses a Symanzik-improved action, so it supports the thermodynamics sign statement but is not a Wilson-action plaquette dataset. **NOT READ / not established by this source:** a claim for temperatures beyond its finite plotted/simulation range.

## Additional Wilson SU(2) finite-volume source checked

**R. Leme, O. Oliveira, and G. Krein**, “Approximate dual representation for Yang–Mills SU(2) gauge theory,” arXiv:1703.07335v2 (2018), 17 pages. Open PDF saved at `~/ym4d-papers/gap-mono-lit-approx-dual-1703.07335/source.pdf`. I read Section 5, p. 9, Eqs. (47)–(50), and Section 6.1, pp. 10–11, Figs. 6–7 and surrounding text; **NOT READ:** the rest of the paper. Section 2, p. 2, Eq. (1) identifies the standard Wilson action. Section 6.1 reports the plaquette mean for `6^4` and `12^4` over varying β; it compares its 12⁴ result against a separate 10⁴ heat-bath Wilson simulation. Its Fig. 6 is a plot without a printed table of central values and uncertainties. The authors describe the finite-volume effect as “no or only a mild dependence” (Sec. 6.1, p. 11). This is useful qualitative coverage, but it supplies neither the five requested sizes nor the per-coupling error table. Its dual algorithm is explicitly approximate and the paper reports deviations from heat-bath estimates, so I do not substitute its plotted curve for the requested standard Wilson data.

## Requested comparison table: published values found

I did not find in the open sources read a publication that prints mean-plaquette central values with errors, at a common set of β values in [1.5, 3.0], for every requested symmetric periodic size. The table below records the source coverage rather than substituting unaudited visual estimates.

| β in [1.5, 3.0] | 4⁴ | 6⁴ | 8⁴ | 12⁴ | 16⁴ | Largest-lattice value at same β | Is smaller-lattice action larger outside errors? |
|---|---|---|---|---|---|---|---|
| Common published β grid with printed `⟨1 − ½ Tr U_p⟩ ± error` | NOT FOUND in the open source read | NOT FOUND | NOT FOUND | NOT FOUND | NOT FOUND | NOT FOUND | NOT ASSESSABLE from the values read |

The Engels–Scheideler paper covers the five lattice sizes but does not report the required plaquette means and errors in its text or tables. Leme–Oliveira–Krein add only `6^4` and `12^4` means in a figure and describe the volume effect qualitatively; they do not give the uncertainty comparison required here. It would be unsound to infer an outside-errors result from either paper’s plots. Therefore this reading does **not** establish whether a smaller Wilson SU(2) lattice has a larger mean plaquette action than a larger one at any coupling.

## Other source access

Nauenberg, Schalk, and Brower, “Finite-size scaling and asymptotic freedom of the SU(2) lattice gauge model,” *Phys. Rev. D* 24, 548(R) (1981), DOI 10.1103/PhysRevD.24.548, appeared relevant from its abstract because it studies the lattice-size dependence of plaquette energy for `L=4` to `10`. The APS page displayed “Authorization Required” and requested credentials. Per the reader rule, I stopped at that refusal. The paper is **NOT READ** and contributes no values here.

## Status and limits

- Sources-level result: the open Wilson SU(2) papers checked confirm the requested observable and include relevant lattice sizes, but do not provide the central-value/error table needed for the requested five-size comparison.
- Thermodynamics guide: Giudice and Piemonte’s SU(2) thermodynamics figure shows positive interaction measure over its plotted finite-temperature range; Eq. (29) gives zero in the Stefan–Boltzmann limit. It does not justify a universal all-temperature theorem.
- **Unresolved:** the requested five-size, common-coupling plaquette table and the outside-error comparison. No numerical claim has been added to any proof or scientific status.
