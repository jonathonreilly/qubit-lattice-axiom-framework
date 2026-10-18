# B17 findings: closure rejects anisotropic cones, and therefore the eight-node step's doublers

Provenance: written by the supervisor. Checked by a fresh-context same-family agent (`../B17_check/REPORT.md`): all four claims hold, and its corrections are applied below. Runner: `aniso_weyl_bracket.py`, exact sympy, PASS=4 FAIL=0 (2 s). It reads one symbol component, and its check 4 compares hard-coded numbers. The full-matrix, general-triad and improvement-term support is `../B17_check/chk1_bracket.py` (PASS=12). The computed cone support is `chk2_step_cones.py`.

## Computation

For h_N = ½ Σ_j v_j {N, σ^j(−i∂_j)}:
- The derivative part of [h_N, h_M] is −Σ_j v_j² w_j ∂_j, with w = N∇M − M∇N. The shift vector is direction-weighted.
- In the isotropic case the full bracket is −v² L_w, with the Kosmann spin term. This reproduces B15 C2.
- Closure against gravity requires a relabelling along κw with a single κ: B14 E2, B15 C6, B16. That forces v_j² = κ for every j. So an anisotropic (here uniaxial) Weyl cone cannot close.

This is the standard Hojman–Kuchař–Teitelboim statement: closure requires every species' cone metric to equal the structure function. The computation just makes it explicit for a uniaxial Weyl node.

## Consequence for the corner step (conditional)

- **The step's nodes.** The eight-node step S·R_L·U_H·U_L has:
  - at ±k*, isotropic Weyl nodes of speed √2/3, where O forces isotropy;
  - at the six D4 cube points, uniaxial doublers with speeds 0.2467 axial and 0.5837 transverse (ratio 1 − 1/√3, unexplained). A second, symmetry-forced eight-node set at −π/2 has identical cones.
  All eight nodes sit at the node quasi-energy (B1 cube scans).
- **What closure would require.** Suppose its long-wavelength theory couples to the curvature-member constraints like the B15 Weyl field. Closure would then need all eight cones to equal √κ isotropically. **The step fails.**
- **General form, heuristic.**
  - The doubling corollary forces the node quasi-energy to be reached away from ±k*, for gapped steps and odd-filling Hamiltonians that carry the anticommuting axis-C2 lifts.
  - At those momenta the little group is smaller than O (D4 at the cube points), so isotropy there is not symmetry-forced. A closing matter sector therefore needs either an isotropic cone at speed √κ that is accidental (codimension ≥ 2, a genericity heuristic only), or a symmetry relating the doubler orbits to ±k*, as the naive walk's taste symmetry does. The corner step has no such symmetry: k → k + π(1,1,1) exchanges only orbits of the same type.
  - Or it needs the corollary's hypotheses to fail: gapless in quasi-energy, or broken axis C2s.
- **What this means.** Gravity closure and the lattice doubling statement together act as a cross-rung selection rule on step rules. That is the scale-ladder mechanism "an upper rung constrains a lower one" in concrete form.

## Not established

- **No local Floquet Hamiltonian.** The step is gapless away from ±π/2, so every branch cut passes through the other node set. The argument needs only a band-projected theory near E.

- **A QCA is not a Hamiltonian.** Coupling a unitary step to a lapse means local step timing, or multi-fingered time. Whether such a step's local-timing algebra reduces to B15's bracket at leading order is assumed, not shown.
- **Doublers at other momenta.** The corollary does not say they are Weyl cones. They could be nodal lines or surfaces, which closure also rejects, since they are not cones.
- **κ in step units.** It would be (√2/3)² = 2/9 only if the ±k* species were the sole matter. With doublers present there is no consistent κ.
