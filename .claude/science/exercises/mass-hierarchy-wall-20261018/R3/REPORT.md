## R3 report: RG and strong dynamics on the mass wall

**What I read first.** I read `MINIMAL_AXIOMS_2026-06-29.md` in full, plus `PRIMITIVE_REGISTRY_CHECK.md` and `SCALE_REFERENCE_PRIMITIVE_NOTE.md`. In `derivation_obligations.json` there are no hierarchy entries, only three readout obligations (charged lepton and θ). I also read WALL.md, the HIER packet (SUMMARY, the H2 report and its referee record) and the PR #9702 note.

### The answer

**No.** The lattice's own content cannot fix the γ_i. Three things block it.
- The lattice symmetry forces equal exponents inside every generation multiplet.
- The only flavour breaking the lattice makes is irrelevant, so the RG flow cannot build it up into large factors, however long the window.
- The window length is not fixed anyway.

The lattice does fix one ordering of breaking insertions, and therefore of loops: the translation-charge grading. In three dimensions it has only two odd levels, orders 1 and 3. Infrared fixed points erase hierarchy rather than create it; at most they set m_t to about v. I did not count the rung span as a large log, because nothing fixes it: the rung 0→1 block is chosen by hand, the packet width is free, and v is not derived (HIER-1).

**Prior art.** These were already mapped, and I don't present them as new:
- the top quasi-fixed-point no-go (`QUARK_TOP_QFP_ATTRACTOR_ROUTE_NO_GO_NOTE_2026-05-10.md`: 205–219 GeV);
- the generation-blind radiative τ firewall (y_τ ≈ α_LM/4π);
- YT generation Outcome D, GEN-2 (Y = a·1 + b·J), and HIER-2's R2/R5;
- HIER-1's escape E2, the template for the bound below;
- three historic intakes (the mass-hierarchy honest assessment, the EWSB cascade, radiative CKM). These are mechanisms 1 and 2 as attempted before; their defects are listed below.

### Route 1: partial compositeness / conformal exponents

**Object.** Δγ_ij(μ), the generation-dependent part of the mass (or mixing-operator) anomalous dimension. The mass ratios are ln(m_i/m_j) = ∫Δγ_ij d ln μ.

**Lemmas.**
- **(a) Schur ceiling (proved; checked in `r3`).** Any lattice-symmetric generator of the RG flow commutes with the symmetry action on the generations. Projective scalar cocycles cancel in g·X·g⁻¹. Results by placement:
  - internal label X2′: 9 free real numbers, no constraint;
  - axis labels: 2 levels;
  - orientations T1: 1 level; with spin ½ under 2O: 2 levels (E1/2 + G3/2);
  - corners at momenta πe_i with translations: 1 level, so the three are exactly degenerate.
  - Only when the elements of O outside T are broken (for example by the chiral A2 term) are three levels allowed. They are then a complex circulant, with 3 free real numbers. That is main's Koide circulant route: the levels are allowed, not fixed.
- **(b) Irrelevance bound (proved; quadrature checked).** If Δγ = c(μ/Λ)^y with y > 0, the accumulated ln ratio is (c/y)(1 − e^(−yL)) ≤ c/y for every L.
  - Needed: ln(m_t/m_u) = 11.8 at M_Z. That requires y ≤ 0.085 at c = 1, and y ≤ 0.025 at c = 0.3.
  - Lattice-made splittings are irrelevant: dimension-3 splittings are forbidden (HIER-2 R1, PR #9702 item 4), and staggered taste breaking has y = 2 (comparator). With c = 1 that gives at most a factor e^0.5 ≈ 1.6.
- **(c) Comparator.** The built content's infrared fixed points are Gaussian (Weyl fermion, photon, linearised graviton; formation sits at the trivial fixed point, B3). So all dimensions are canonical. With L free, half-integer exponents are the same as FN integers, and HIER-2's control applies: 400 of 400 random spectra fit.

**The number it would fix.** The log-ratios R_s = ln(m3/m1)/ln(m3/m2), which do not depend on L. Observed values are 2.10 (up), 1.74 (down) and 2.89 (leptons). The left-doublet spacing ratio would be 0.47, not the equal-spacing value 1. With L = 38.4 (comparator only), the exponent differences would be 0.07–0.31 per unit L. None of this is supplied, by (a)–(c).

**Strongest objection.** Species with different velocities give a genuinely marginal splitting. The corner step's doublers have uniaxial cones (axial 0.25, transverse 0.58) against √2/3 at ±k*. However (suggested):
- the three doublers are permuted by C3, so the split is 1 + 3;
- the speeds converge logarithmically (main's velocity-attractor note);
- the size is about (α/4π)·L ≈ 0.4 in the log;
- constraint closure already rejects these cones (B17–B22).

**Kill condition.** The route dies unless the framework exhibits a flavour-splitting direction with y < 0.085 over a fixed window, with the generations not in one S3 orbit. There is none in the built content.

**Tests run.** `r1`, `r3` (as above) and `r2`, a one-loop SM Yukawa-matrix flow from M_Pl to M_Z with comparator gauge couplings.
- **Checked:** m1/m2 is unchanged to 1e-4 in all three sectors. m2/m3 moves by a factor 0.62–1.62, through y_t only.
- **Checked:** anarchic O(1) matrices become less hierarchical toward the IR. At s = 2 the up-sector median log10(m1/m3) goes from −0.75 to −0.61. The spread grew in at most 7% of samples, and by at most 0.06 decades, against 3–5 decades needed.
- So Pendleton–Ross focusing fixes at most one O(1) Yukawa per sector.

### Route 2: radiative loop ordering

**Object.** The Z2³ translation charge c of chirality-odd mass terms (always odd, HIER-2 R4a), and the set S of spurion harmonics.

**Lemmas.**
- **Loop order is insertion order (proved, Schur).** Symmetric loops renormalise only symmetric textures, so a whole irreducible representation switches on at once. "m_2 at one loop, m_1 at two loops" needs a spurion that separates them.
- **Charge grading (proved; exhaustive over all 127 harmonic sets in `r3`).**
  - Hamming weight mod 2 is additive, so with odd-weight harmonics the leading orders are odd. The minimal order is the Cayley distance d_S(c).
  - Every subset of a single weight class gives orders in {1, 3, ∞}, with at most 2 distinct finite values.
  - Every S3-invariant set gives at most 2.
  - Only 12 sets give 3 orders. All 12 are non-invariant and mix weight parities; for example {001, 011, 101} gives (1, 2, 2, 3). That is two supplied amplitudes, the free-pattern bin.
  - This explains HIER-2's numerical {1, 3} at the charge level. It does not prove the "at most 2 per spurion" bound beyond that level.

**The number it would fix.** The pattern (1³, 3), with a level ratio of (α_LM/4π)² = 5.2e−5. Not achievable: there are only two levels, the hw-1 triplet is degenerate, and the exponents are sector-blind.

**Kill (checked, `r1`).** QCD loops treat up and down quarks alike. But (m_d/m_b)/(m_u/m_t) is 136 at M_Z, 176 at the GUT scale and 89 in the mixed set, against at most 9 allowed by the ×3 tolerance.

**Objection.** Loop factors can carry logs, but L is not fixed.

### Defects found in historic intakes on main (not edited; for the audit lane)

1. **`HISTORIC_MASS_HIERARCHY_HONEST_ASSESSMENT` (archived original #1132).**
   - It runs an irrelevant, cutoff-scale taste splitting over the full window. By (b), Δγ = 0.173 at y = 2 gives a factor 1.09, not 851.
   - Its Wilson-mass tastes (2r·hw/a) are cutoff-scale states, not light generations.
   - Its own formula 3·e^(0.173·39)·39 equals 1.0e5, not the stated about 12,000 (log10 5.0, not 4.1).
2. **`HISTORIC_EWSB_GENERATION_CASCADE` (#448).** The residual y↔z C2, plus translations by e2 and e3, keeps the two colour-direction masses equal to all orders, for any sign dressing (`r4`, 4/4 trials). So the Jordan–Wigner (β_JW) split must vanish. The note's own splittings are fractional (1.10 : 1.003 : 1.003); the "1 : 0.0027 : 7.3e−6" row is not what the model gives.
3. **`HISTORIC_CKM_RADIATIVE` (#217).** The diagonal self-energy ratios (0:1:4) it assigns to three corners in one orbit contradict translations plus S3, which force equal diagonal entries. This is Outcome D's narrow lemma.

### Comparator and status

Partial compositeness and FN share the relation V_ub ≈ V_us·V_cb: 0.0094 against an observed 0.0037, a factor 2.55, inside ×3. It is not a framework result.

Same-family work, unrefereed. Peak memory was under 30 MB, and nothing is left running.

Files are in `/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/masswall/R3/`:
- PREREG.txt (written before the runs; all six predictions held)
- r1–r4 logs
- scripts/r1_window_and_data.py
- scripts/r2_sm_yukawa_flow.py
- scripts/r3_schur_and_grading.py
- scripts/r4_cascade_residual_z2.py