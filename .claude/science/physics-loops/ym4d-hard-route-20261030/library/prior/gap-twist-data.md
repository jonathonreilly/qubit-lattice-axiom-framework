# Twisted partition functions and electric-flux data

Reading note for FINISH row 734 (2026-11-11). Research literature only; all measurements, fitted quantities, and conversions below are **GUIDE**. This is not a proof, an audit, or a status change. No computation was used to discharge a claim.

## Repo search

The lead's `library/prior/repo-search-2026-11-08.md` is a digest for a different lane item; it reports a search of `origin/main` and PRs #10114, #10133, #10134, #10141, and #10144, but not a twist-data search for this row. FINISH row 734 itself contains no separate “Repo prior work” lines; it points to work item 3 of row 731. The closest topical repo search I found is `library/prior/gap-crux-prior-repo.md`, §2E (lines 868–883, 897): it records twist/flux-adjacent candidates, but says those do not give the SU(2) Wilson twisted-torus bound being sought there. Its closest hits are conditional supplied Hamiltonians and non-transferable flux notes. `library/prior/gap-seed-lit.md` lines 80–85, 90, 114–115 likewise treats twist bounds as conditional and not a bound on the untwisted torus seed. These are adjacent to the present reading task; none contains the requested published numerical table.

I checked the current checkout at `d56f924eefc64e80e85fda70a3b6b90771686cb6`, the named prior files, and `library/open-registry.md`. There is no existing `library/prior/gap-twist-data.md`, and no registry owner for this literature read. `library/gap-flux-exercise.md` already defines the twist classes and sector sums (Sections 3.0 and 8.4); this note adds no proof to them.

The task packet's `library/sa-index/README.md` directs a tag/name search across the full-read outline index followed by reading the cited lines. I searched the chunks and obligations for twisted partition functions, electric-flux free energies, one-plane/two-plane twists, and Pfaffian-one twists. The hits are background-field or RG covariance twists, not the finite-volume twist ratios in this task. I fetched the outline and CA-I once each at the specified `31a47c543775` commit (`/tmp/sa_ym4.tex`, `/tmp/sa_ca_I.tex`; 32,992 and 166,711 lines). No source passage from them is used here. Credit Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, for any later use of their outline or account.

## What the requested differences require

Use the definitions in `library/gap-flux-exercise.md` §3.0 and §8.4. For time length (a=L/2), spatial box (B=L^3), and (r_k=Z^k(a;B)/Z^0(a;B)),

\[
S_{\rm per}-S_{\rm ev}
=(1+S_{\rm per})\left(1-\frac{1}{8}\sum_{e\in E_1}r_e\right)
=\frac{1+S_{\rm per}}{8}\sum_{e\in E_1\setminus\{0\}}(1-r_e).
\]

With cubic symmetry, if (r_1,r_2,r_3) denote the ratios for one, two, and three temporal-plane twists, this is
\[
S_{\rm per}-S_{\rm ev}
=\frac{1+S_{\rm per}}8\bigl(3(1-r_1)+3(1-r_2)+(1-r_3)\bigr).
\]

For the kappa sum, (W_\kappa/Z^0=\frac18\sum_{k\in K}(-1)^{\operatorname{Pf}(k)}r_k), while (Z_{\rm ev}/Z^0=\frac18\sum_{e\in E_1}r_e). Thus
\[
S_\kappa-S_{\rm ev}
=(1+S_{\rm per})\left(\frac18\sum_{k\in K}(-1)^{\operatorname{Pf}(k)}r_k-\frac18\sum_{e\in E_1}r_e\right).
\]
These are identities from the exercise's definitions, not measured numerical values. A one-plane ratio and one Pfaffian-one two-plane ratio alone do not determine either difference: the first needs all electric twists, and the second needs the full Pfaffian-weighted 64-twist sum (as well as (S_{\rm per}) or the normalization by the leading eigenvalue).

A terminology trap matters here. In de Forcrand–von Smekal's finite-temperature paper, (Z_k(1)), (Z_k(2)), (Z_k(3)) count one, two, and three **temporal** twists. Any pair of temporal planes shares the time direction, so their four-dimensional Pfaffian is 0. The requested Pfaffian-one two-plane twist is a complementary pair, one temporal and one spatial plane. Their (Z_k(2)) data is therefore not the requested class.

## Open literature read

1. **T. G. Kovács and E. T. Tomboulis, “Computation of the Vortex Free Energy in SU(2) Gauge Theory,”** arXiv:hep-lat/0002004v2; *Phys. Rev. Lett.* 85 (2000), 704. Open arXiv PDF, pp. 5–7, especially p. 7, Fig. 3. It defines the vortex free-energy ratio (Z_\Lambda(\tau)/Z_\Lambda) and plots its measured “probability” against physical lattice size for symmetric lattices at \(\beta=2.3,2.4,2.5\) (the accompanying text gives (a=0.165,0.119,0.085\) fm). **GUIDE:** the plotted one-plane ratio rises toward 1 by about 1.5 fm. The article reports no table of point values, no correlation length for converting those points to (L/\xi), and no Pfaffian-one two-plane data. I cannot identify a plotted point in the requested (10\le L/\xi\le40) interval from this source.

2. **P. de Forcrand and L. von Smekal, “‘t Hooft Loops, Electric Flux Sectors and Confinement in SU(2) Yang-Mills Theory,”** arXiv:hep-lat/0107018v2; *Phys. Rev. D* 66 (2002), 011504(R). Open arXiv PDF, pp. 2–4, Eqs. (10)–(13), Figs. 2–5. The simulations use (N_t=4) and (N_l=6,8,10,12,16,20), i.e. (1/T\times L^3) finite-temperature tori. The plotted finite-size variable is (x=\pm L T_c |t|^\nu\propto L/\xi_\pm) (Eq. 18, p. 3). **GUIDE:** their below-critical fit gives (1/(\xi_-^{(0)}T_c)\simeq3.66) from the universal-amplitude estimate and (3.58\pm0.5) from the electric-flux slope (p. 4, discussion of Fig. 4); Fig. 4 reaches (-x\) of about 6, corresponding to roughly (L/\xi_-\lesssim22) under the reported fit conversion. Thus this source does show data in part of the requested (10)–(40) correlation-length window, but only for the finite-temperature geometry and through figures/fits, not a tabulation. Figs. 2 and 5 concern one and two/three mutually orthogonal **temporal** twists; they do not supply the Pfaffian-one complementary-plane ratio. The article's electric-flux ratios are Fourier transforms of twist ratios, not the requested symmetric four-torus table.

3. **L. von Smekal, with P. de Forcrand and O. Jahn, “More on Electric and Magnetic Fluxes in SU(2),”** arXiv:hep-lat/0212019v1, proceedings note. Open arXiv PDF, pp. 2–3, Figs. 1–4. It discusses (Z_k(\vec k,\vec m)) and (Z_e(\vec e,\vec m)), including parallel and orthogonal electric/magnetic fluxes, and shows data on (4^4), (6^3\times4), and (8^3\times4) lattices. Figs. 3–4 give electric-flux curves for mixed fluxes; Fig. 2 gives a magnetic-twist curve. **GUIDE:** these figures establish qualitative finite-size behavior and the sensitivity to whether fluxes are parallel, but the note provides no numerical table and does not give the (L/\xi) values needed to select (10\)–(40) points. I did not read an extractable Pfaffian-one (Z^k/Z) value from it.

The de Forcrand–von Smekal data satisfy the task's stop threshold in the limited sense that a plotted finite-temperature dataset extends past (5\xi) (to about (22\xi_-), as above). I therefore did not stop at the threshold. That does **not** supply the requested Pfaffian-one finite-volume numbers or make the finite-temperature geometry an equal-sided four-torus.

## Numerical answer and limitation

No opened source supplies tabulated values for both the one-plane and Pfaffian-one two-plane ratios at an identified equal-sided 4D torus with (10\le L/\xi\le40). The nearest quantitative source has figures rather than tables and gives temporal-plane classes only; the mixed-flux proceedings note also has figures rather than tables and does not specify (L/\xi). Accordingly I do not assign numerical entries to (Z^k/Z), (S_{\rm per}-S_{\rm ev}), or (S_\kappa-S_{\rm ev}). The ratios cannot be reconstructed uniquely from the published figures in this read set without digitizing/reading additional data, and the requested page-and-table citations do not exist in these copies. All reported literature fit numbers above are GUIDE, not inputs to a proof.

RESULT: GUIDE literature read; the open sources show one-temporal-twist behavior beyond (5\xi) in finite-temperature scaling plots, but no source read provides the requested tabulated Pfaffian-one two-plane ratio or numerical (S_{\rm per}-S_{\rm ev}) and (S_\kappa-S_{\rm ev}) for an identified (10\le L/\xi\le40) four-torus.
