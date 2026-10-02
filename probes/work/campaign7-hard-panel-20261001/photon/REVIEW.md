**Hostile review of c7/hard/photon/REPORT.md (Lane D, pure ring model)**

Method: derivation only, no code run. I checked the landed definitions on origin/main: `u = Σ⟨R_p⟩/(3N) = −E0/(3N)`, `s² = 2−2cos k`, `m1 = 2us²`, `χ = 2m₋₁`, from the RING_MODEL_ENERGY_ONLY_BOUNDS…2026-09-25 note. I also checked the arXiv abstracts. Labels follow the brief.

## Verdicts

| Claim | Verdict |
|---|---|
| D3 tiling covers every link exactly once | HOLDS |
| D3 three tiles per corner, so every circulation pattern is ice | HOLDS |
| D3 product state normalised, in the Gauss sector, ⟨H⟩ = −3Ng/4, u ≥ 1/4 | HOLDS WITH NARROWED SCOPE (holds in the flip component containing the tiling, not necessarily the seed component) |
| D3 second order 3/128 | HOLDS |
| D3 third order = 0 | HOLDS (and stronger: every odd order vanishes) |
| D3 "total 35/128; a crystal needs ≥ 0.013 from fourth order and beyond" | GAP. The arithmetic is right, but I count the fourth order at about +0.0064, roughly half the gap. |
| D2 gauge map W, seams, (−1)^{L_z} anticommutation | HOLDS (EXACT) |
| D2 Oshikawa–Hastings adiabatic step | HOLDS WITH NARROWED SCOPE (ARGUED, as the report labels it) |
| Cl₃ algebra of π-flux magnetic translations | HOLDS (as algebra); the plaquette Bragg assignment is ARGUED |
| D1 Ω(z) ≥ ω_min, monotone in z, Ω(∞) = landed bound | HOLDS. The diagnostic consequences are ARGUED, not EXACT. |
| O2 gap Δ implies χ ≤ 4us²/Δ² | HOLDS, but it restates the landed bound ω_min ≤ 2s√(u/χ); it is not new |
| D4 conservation of Δh, Fourier/monopole identity, cube 6-cycle | HOLDS |
| Literature | All arXiv IDs are real and match. One quoted word is misattributed (Wiese); nothing looks invented. |

## D3 in detail (the key check)

**Coverage [EXACT, reviewer].** The tiles are: xy at (x,y) both even; xz at x odd, z even; yz at y odd, z odd.
- x-link at (x,y,z): if x is even, exactly one of xy(x,y) or xy(x,y−1) has even base y, and no xz tile applies. If x is odd, exactly one of xz(x,·,z) or xz(x,·,z−1) has even base z, and no xy tile applies. One tile either way.
- y-links and z-links work the same way, split by the parity of y and of z.

So the 3N/4 tiles cover the 3N links exactly once. Each vertex has 6 links, so it meets exactly 3 tiles. A circulating tile is 1-in, 1-out at each of its corners, so every one of the 2^{3N/4} patterns is ice and has zero section fluxes.

**⟨H⟩.** The link space factorises over tiles, so the product state is normalised and lies in the Gauss sector. Each tile has ⟨U+U†⟩ = 1. A non-chosen q shares at most one link with any tile, so U_q pushes 4 tiles out of circulation, giving ⟨U_q⟩ = 0. Hence ⟨H⟩ = −3Ng/4, u = 1/4. This needs L even, and L ≥ 4 so that no two plaquettes share 2 links (which happens on L = 2).

**Second order [EXACT].** H0 is the tile terms: S at −g, A at +g, non-circulating states at 0. The four tiles touched by q are distinct; q is flippable with probability 2/16 = 1/8; the flip takes 4 tiles from −g to 0, so the cost is exactly 4g. Images from different q are orthogonal, because q⊕q′ meets every tile in at most 2 links. So E2 = −(9N/4)(g/32) = −9Ng/128, i.e. **3/128 per plaquette ✓.**

**Third order [EXACT].** The report's inequality n_nc ≥ n_c holds, but the report gives no proof. Proof: on a closed mod-2 surface every edge carries an even number (≥ 2) of surface faces, and at most one of them is a tile. So each edge has at least as many non-chosen faces as chosen ones; summing over edges gives n_nc ≥ n_c.

A stronger result also holds. Every cube has n_nc ∈ {4, 6}, so every contractible closed surface has even n_nc. A flip sequence of odd length leaves an odd mod-2 set of non-chosen faces, so it cannot close. **All odd orders vanish**, and E(λ) is a series in λ². For L ≡ 0 mod 4 this is also a global Z₂ gauge-sign map V → −V. (Cube classes: 6/8 have one opposite chosen pair, 2/8 have none ✓.)

**Fourth order (not done in the report) [ARGUED: reviewer's hand linked-cluster count, not CHECKED].** Contributions to u per plaquette:

| Cluster | Contribution to u |
|---|---|
| single q, −11g/8192 each (RSPT and Brillouin–Wigner agree) | +0.00101 |
| cube rings, −g/96 per ring cube (48 paths of weight 1/64) | +0.00260 |
| pairs sharing 1 tile, no shared link (25.5N) | +0.00059 |
| pairs sharing 1 tile through a shared link (6N, blocking) | −0.00041 |
| ring-opposite sides (1.5N) and corner pairs (3N), η = +1 | +0.00065 and +0.00130 |
| ring-adjacent sides (3N) | +0.00065 |
| **Total** | **≈ +0.0064** |

So u through fourth order ≈ **0.2798**. The coefficients run 1/4, 0.0234, 0, 0.0064: about 0.27 per λ² order. A geometric tail suggests roughly 0.282, i.e. about 0.005 short of 0.287. That is not decisive:
- convergence at λ = 1 is unknown;
- a phase transition along H0 + λH1 cannot be seen by perturbation theory;
- this is one crystal ansatz, not "a crystal".

D3 therefore does not disfavour a crystal on energetics.

**Landed scans are more relevant than the report says.** The landed runner measures the orientation-summed flippability structure factor at (π,π,0), with base-vertex positions. The tiling crystal has a non-cancelling (π,π,0) amplitude of about 7/32 per site from its xy tiles. Its (π,0,0) amplitudes cancel between orientations. So the landed "no growth at (π,π,0)" already bears on this crystal, within the limits of a mixed estimator and small tori.

## D2 and Cl₃

- **Curl λ [EXACT].** Bulk: λ_x(y+1) − λ_x(y) = B. y-seam: −2π(L_y−1)/(L_xL_y) + 2π/L_x = B. Corner seam gives B − 2π. xz and yz plaquettes give 0. So curl λ = B mod 2π ✓.
- **Translation [EXACT].** T_x shifts λ_y by −2π/L_x + 2πδ_{x,0}. A 2π shift on a half-integer link gives −1, so the factor is (−1)^{L_z} e^{±2πiΦ_y/L_x} ✓. Sanity checks pass: the all-plus state cancels the phase, and no T_x-invariant ice configuration has Φ_y = 0 when L_z is odd.
- **Gauge structure.** H(θ) keeps Gauss's law, stays Hermitian and stays translation-invariant, so the KSKR-style setup is legitimate.
- **Strengthening available [EXACT, finite size].** Perron–Frobenius gives P_x = 0 at θ = 0; at θ = B the ground state is W†ψ₀ with P_x = π. So the P_x = 0 and P_x = π levels must cross for some θ in (0, B), on every such torus.
- **Still ARGUED.** Turning that crossing into "no gap at θ = 0" needs the gap to survive a uniform O(1/(L_xL_y)) field whose total norm is O(L_z). Norm bounds do not give this.
- **Required scope.** The flip component must be T_x-invariant (or use the full Gauss sector), with Φ_y = 0 and L_z odd. The trichotomy must add "other gapless (for example z = 2 or critical)" to Coulomb, crystal, and topological order.
- **Cl₃ [EXACT as algebra].** Three pairwise-anticommuting unitaries; the T_a² are central, and after fixing them the irreps are 2-dimensional ✓. Mapping n_b onto b-normal plaquettes at Q_b is ARGUED.
- **Landed-scan criticism needs narrowing.** (π,π,0) is Q_z itself, one of the predicted momenta, and the cubic-symmetric runs see it diluted. "Skipped (π,0,π), (0,π,π)" is literally true but weak; the real gaps are orientation resolution and the mixed estimator.

## D1 and O2

- **D1 [EXACT].** Ω² = ∫dν/∫(dν/w) is a harmonic mean, so Ω² ≥ w_min. d/dz of E_ν[1/w] equals −Cov(1/w, 1/(w+z)) ≤ 0, so Ω is non-decreasing. Ω(∞)² = 2m1/χ = 4us²/χ ✓. Evenness in ω_m needs a real H (✓, stoquastic).
- **D1 caveats.**
  - At T > 0, G(0) carries a static (Curie) term that appears at ω_m = 0 only.
  - "Coulomb ⇒ Ω·L → const" is not implied, because Ω bounds ω_min from above only. The exact direction is the one-sided "Ω → 0 excludes a transverse gap".
  - The landed note already has the tighter structure-factor bound m₀/m₋₁. D1's small-z member, √(m₋₁/m₋₃), is tighter still. The report should say so.
- **O2.** Δ = 0.265 g ✓ (s = 2 sin(π/24)). It is the landed bound read backwards.

## D4

- Δh is a closed integer dual 1-cochain; bubbles and single-plaquette resampling conserve it ✓.
- The Fourier identity, an average over static fractional monopoles with background flux θ_c, is correct ✓. The T/6 bias estimate (equipartition) is ARGUED, and breaks down if monopoles are condensed.
- **6-cycle traced link by link ✓.** Bottom, y=0, x=1, y=1, x=0, top are each circulating when flipped. The final state equals the start. Every face goes cw→ccw relative to its outward normal, so Δh = +1 per face, i.e. δ of the cube indicator.

## Literature

- 1105.1322 (Sikora et al., diamond, μ_c = 0.75): the report's correction is right. The abstract does not say the R state extends down to μ = 0.
- 1105.4196 (Shannon et al.) ✓. The −0.5 figure is confirmed only via a secondary source, the Gingras–McClarty review (1311.1817).
- cond-mat/0305401 ✓, 1805.05367 ✓, 2009.04499 ✓, 2201.07171 ✓, PRB 73, 134402 ✓ ("Ordering in a frustrated pyrochlore antiferromagnet proximate to a spin liquid").
- 1305.1602: Wiese writes "perhaps even for S=1/2". The word "plausible" appears in a later D-theory review, so the quote is misattributed.

## Required corrections

1. Report 35/128 as a third-order partial sum, not a value or bound. Add the fourth-order estimate (about +0.0064, to be CHECKED) and drop the "crystal needs ≥ 0.013" framing. Rescope to this tiling, L ≡ 0 mod 4 or L ≥ 4 even, and the component containing the tiling.
2. Add the odd-order vanishing and the edge-count proof of n_nc ≥ n_c.
3. D2: state the T_x-invariant-component and Φ_y = 0 assumptions, add the exact finite-size level-crossing statement, and include "other gapless" among the outcomes.
4. D1: label the diagnostic consequences ARGUED, add the static-term caveat, and credit the landed m₀/m₋₁ bound.
5. O2: credit it as the landed bound.
6. O3: comparing the 74× bias with the flux gap ignores that biases can cancel in energy differences; keep it ARGUED.
7. Narrow the landed-scan criticism as above. Fix the Wiese quote. "Useful … only as a cross-check" uses a banned word.

## Bottom line

The EXACT cores of D1, D2, Cl₃, D4 and D3 through third order are correct, and the D4 6-cycle checks out. The weak point is the D3 inference. The fourth order the report skipped appears to be large, about half the 0.013 gap, so the tiling crystal is energetically inconclusive, not disfavoured. The decisive follow-up is the report's own R3 test: an exact fourth- and sixth-order linked-cluster count on 4³, by a small combinatorial program. It should reproduce −11g/8192 per plaquette and −g/96 per ring cube before anything else.