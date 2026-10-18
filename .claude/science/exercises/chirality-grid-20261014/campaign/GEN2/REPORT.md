**Provenance:** the worker's final message, saved verbatim by the supervisor.

**GEN-2 report: generations as the orientation of an extended fermion cell**

**Reading: DIR-PRICE.** Items c1, c2 and c5 hold. c3 holds: CKM forces a first-order strain channel. c4 exceeds GEN-1's n = 2 (proved at the level of which terms symmetry allows; their sizes are suggested). c6 fails only for even crystal periods, and an odd period or a floating cell law avoids it, so c6 also reads DIR-PRICE.

**Provenance.** One Claude Opus 5.5 worker, the same family as GEN-1, CLS-1 and OBS-1, so not independent. Unrefereed. Ran 21:09–21:16Z on 2026-10-17, which left only about 20 minutes, so this is a symmetry-level pass. PREREG was written at 21:11Z, before the run. One script, peak 23 MB, one process. Nothing of mine is still running; the `runner.py` process at about 430 MB belongs to QMC-1b.

## Plain words

1. **The label choice brings back the flavour problems that GEN-1 removed.** GEN-1's escape worked because rotations did not touch the generation label. Here they do: a rotation turns an x-rod into a y-rod.
2. **CKM needs the vacuum to pick out directions in space.** Under a cubic-symmetric law, the quark mass matrices can only take a "rotation-blind" form, and two such matrices can always be diagonalised together, so CKM is trivial (checked). Real CKM needs a piece that transforms like a traceless stretch of space, the Eg part.
3. **That forces a strain channel, and probably at tree level.** An Eg piece in the masses has the same symmetry as Eg strain, so stretching space shifts quark masses at first order (X2-L8's mechanism). In X2 that coupling was one-loop and gauge-suppressed. Here nothing forbids it at tree level, because the label is itself a direction.
4. **Speed problems grow.**
   - A rod can move at different speeds along its axis and across it. That is 3 extra rotation-allowed speed terms per field, each to be tuned at tree level.
   - The direction-picking vacuum can also give every field, the photon included, a direction-dependent speed at first order. Cancelling those needs counterterms that are not cubic-covariant: at least one per field, on top of GEN-1's 2.
5. **The anomaly checks and the protection of the light particles survive.** So do the tree-level flavour-changing limits (c5), given one Higgs doublet and a heavy direction-picking field.
6. **Crystals of cells (c6).** With an even period, all 8 corners fold onto Γ and the light sector loses its protection by handedness. With an odd period, or with cells that float, nothing folds onto Γ.

## Results

Path prefixes: S = `campaign/GEN2/scripts/`, G1 = `campaign/GEN1/REPORT.md`.

**(c1) holds (proved by inheritance; not re-run with rods).**
- **X2-L1.** Γ holds 3 nodes per component, one per orientation, all of one handedness, because proper rotations preserve chirality. GEN-1's argument (G1 a2) is unchanged: Dirac pairing needs opposite chirality, and Majorana pairing is excluded by 16⊗16 having no singlet and by Z₄^F.
- **X2-L2.** The filter f_Γ is A1g and translation-covariant, so it is unaffected by a label that translations do not act on.
- **Scope.** This needs floating cells; the crystal case is c6. COL-1's Z³ rod example has x-rods only and ignores cubic rotations (panelwork/COL1/REPORT.md:93), so a three-orientation cell law has not been built.

**(c2) holds (checked arithmetic; the crystalline-to-internal mapping is suggested).**
- **Generation charges.** C3 about (111) acts on generations with charges {0, 1, 2}. 16·Σq = 48 ≡ 0 (mod 3) and 16·Σq³ = 144 ≡ 0 (mod 9). The mixed Spin(10)²–Z₃ sum T(16)·Σq = 6 ≡ 0 (mod 3).
- **Transpositions** make one full 16-plet odd, giving ν = 16 ≡ 0 (mod 16) (S/symm.out:8).
- **Z₁₆ gate and mixed Z₂³ anomaly.** These are unchanged from GEN-1: 48 Weyl fermions, ν_R included (G1 a3).

**(c3) CKM forces a first-order Eg strain channel (proved, symmetry level; checked).**
- **Decomposition.** The generation rep is P = A1g + Eg (axes are unoriented). End(P) = 2A1 + A2 + 3E, with 2 cubic invariants (S/symm.out:1).
- **No E-part means circulant.** A matrix with zero E-projection is exactly a circulant (residual 2.4e-16).
- **Circulants give trivial CKM.** Two circulants commute ([Y_u, Y_d] ≈ 2e-16), and |V| is a permutation (S/symm.out:2-4). Every C3 maps onto the same two 3-cycles of the axes, so the conclusion does not depend on which C3 survives. Nontrivial CKM therefore needs an Eg component in Y.
- **First-order response.** A nondegenerate circulant has zero first-order eigenvalue shift under an Eg perturbation (≤ 5e-15), which reproduces OBS-1's circulant lemma. With an Eg component the shifts are O(1): 0.80, −2.66, 2.25 for a random instance (S/symm.out:5-6).
- **Why the coupling is not protected.** The flavour Eg and the spatial Eg are the same representation of the same group, so no symmetry can forbid the first-order coupling of strain to Y_E.
- **Clock row (suggested; the GEN-2 coefficient was not computed).**
  - X2 branch B gives 0.12–2.5 × the bound with one-loop coefficients of 7.2e-3 to 1.0e-2 per e² (panelwork/OBS1/REPORT.md:31-37, :49-58).
  - Rescaling linearly to a tree coefficient r, with e² ≈ 0.09, gives about (180–3800)·r × the bound.
  - That is more than 10× for every branch-B row only if r ≳ 0.06. At r = 1e-2 it is 1.8–38×, so my pre-registered rule (PREREG.md, decision rules) does not let c3 alone decide the reading. Branch A (aligned generations) would be far over.

**(c4) n exceeds GEN-1's (proved as a count of required structures; sizes suggested).**
- **Cubic-covariant per-field speed structures.** A1g multiplicity in End(P) ⊗ Sym²(R³) is 5 per field, against 1 in GEN-1 (S/symm.out:1). Two are isotropic (1 and J); 3 are anisotropic (S/symm.out:1, traceless part). These are tree-level, law-dependent rod anisotropies, v_∥ ≠ v_⊥. Each needs tuning to the clean-row level, about 1e-22 relative (inferred from G1's ratio of 1.1e15 at a 2.9e-7 spread).
- **Non-covariant counterterms (count toward n).** The Eg condensate needed by c3 couples at first order to every field's traceless speed tensor, Eg part, the photon's included. Removing it needs at least one counterterm per coupled field, aligned with the condensate. So n ≥ 2 + (number of coupled fields) ≥ 7, against GEN-1's n = 2.
- **Loop residual.** The one-loop flavour residual κ(H_u + H_d) of GEN-1 remains, and now has Eg parts.

**(c5) holds (tree level; proved given one doublet and a heavy flavon; flavon spectrum not computed).**
- With one Higgs doublet, Glashow–Weinberg natural flavour conservation holds as in GEN-1 (G1 a5).
- The Eg order breaks a discrete group, so there is no Goldstone mode. If the order is lattice-scale, its tree exchange is suppressed by about 1/M_lat².
- Side note (suggested): discrete breaking implies domain walls.

**(c6) Crystal of period c (proved for labels and index; checked c = 2..8).**
- **Even c.** All 8 corners fold onto Γ. The folded index per component is 3 − 3 = 0, so the protection by chirality index is lost (S/symm.out:9-15).
  - By CLS-1's computation, a bilinear light–mirror hopping gives zero mirror admixture at zero energy, because the gapped mirror's propagator vanishes there. The admixture goes into the composite partner (campaign/CLS1/REPORT.md, plain words item 3), so there is no bilinear gap (suggested, inherited).
  - The many-body fate is OPEN. Speed shifts of order (V_K/Δ)² are suggested.
- **Odd c.** Only Γ maps to Γ, the index stays 3, and c6 holds at the bilinear level.
- **Rule.** Odd c or a floating law avoids the even-c failure, so it reads DIR-PRICE, not DIR-FAIL.

## Compared with GEN-1 (refereed? no; same family)

| | GEN-1 (internal label) | GEN-2 (orientation) |
|---|---|---|
| CKM | free | needs an Eg vacuum order |
| First-order strain | absent | forced; tree-level allowed |
| Per-field covariant speed terms | 1 | 5 (3 anisotropic, tree level) |
| n beyond covariant | 2 | ≥ 7 |
| ΔF = 2 at tree level | SM only | SM only, if the flavon is heavy |

## Deviations

- No numerical tree coefficient for the strain channel or the rod anisotropy: no time. Recorded in the PREREG follow-up dated 21:13Z.
- c1 was not re-checked with an explicit three-orientation rod law, because none exists yet.
- OBS-1's branch rates were rescaled linearly, not recomputed.

## Files (`…/chirality_ex/campaign/GEN2/`)

- `PREREG.md` (with the 21:13Z follow-up)
- `scripts/gen2_symm.py`, `scripts/symm.out`, `scripts/gen2_archive.npz`, `scripts/archive.out`, `scripts/capped.sh`
- `TESTS_copy.md` (a read-only copy of the packet's TESTS.md)