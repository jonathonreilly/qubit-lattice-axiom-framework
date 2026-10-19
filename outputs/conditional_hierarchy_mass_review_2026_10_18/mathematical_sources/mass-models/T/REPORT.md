# Complete exercise argument with controlling corrections

Original source: `.claude/science/exercises/mass-hierarchy-wall-20261018/T/REPORT.md`; exact SHA-256 `c752e06880dec42a0f5927bf7220fb5b71573a6919cd9fc7eff1599d88a12b02`.

**Controlling scope:** Shared residual constraints assume the actual specified invariant vacua and simple residual eigenspaces; degeneracies allow basis freedom. The finite coefficient grids, ranks and recalled-data fits are not all coefficient or all physical model conclusions.

**Source-use boundary:** The complete argument below is preserved for inspection, including its original qualifications and counterexamples. Its old verdict labels, claims of completed reviews, operational history and numerical outputs are historical provenance only. Terminal physical exclusions and claims stronger than the controlling scope are deferred, not active conclusions. The canonical conditional exercise note and its correction register control. This attachment is not a separately promoted scientific claim and is not a fresh replay of its exploratory computations.

---

**T-2AMP: 2AMP-FAIL on all three mass sets (MZ, GUT, MIX)**

**Refresher.** Before concluding I read `MINIMAL_AXIOMS_2026-06-29.md` in full, `PRIMITIVE_REGISTRY_CHECK.md` and `SCALE_REFERENCE_PRIMITIVE_NOTE.md`. I skimmed `derivation_obligations.json`: it has three entries (two charged-lepton readout gates, one theta gate) and no hierarchy entry. I also read WALL.md, TESTS.md, R1's report and scripts, and HIER-2's `H2/PREREG.md` for its three mass sets. I wrote PREREG.md at 21:55Z, before any run.

### Plain words
1. **A second symmetric breaking field does not help.** Both pairs leave a tetrahedral residual symmetry, which includes a 120° turn about the body diagonal. That turn keeps speeds the same in every direction, and it also kills quark mixing.
2. **Why mixing dies.** With axis labels (P) or corner labels (S), the turn gives each generation a different "charge", and up and down quarks share these charges. Both sectors then have the same three mass states, so the CKM matrix is a permutation: every entry is exactly 0 or 1. For pair (a) with corner labels the turn ties all three generations together, and the three masses come out exactly equal.
3. **Why the hierarchy dies, separately.** When every particle type carries the same label, a generation-blind Yukawa is allowed with no breaking at all. So all three generations get O(1) masses. Lightest over heaviest never drops below 1.5e-2 anywhere on the grid; the up sector needs 7e-6.
4. **The predicted failure is there but comes second.** R1 expected up and down to get the same ratios. They do, but the two failures above happen first.

### Result (40×40 grid in (ε₁, ε₂), 4 models, draws 1–3, free sector scales)

| Set | Best on all 12 numbers | Best on masses only (added after the run) | Reading |
|---|---|---|---|
| MZ | ×1.4e7 | ×114 | 2AMP-FAIL |
| GUT | ×1.4e7 | ×122 | 2AMP-FAIL |
| MIX | ×1.4e7 | ×88 | 2AMP-FAIL |

- The 12-number factor is set by the CKM zeros, so its size is a numerical floor. The real statement is that every |V| is 0 or 1, to within 1e-11 (1e-6 in a near-degenerate corner case).
- Random control: 0 of 300 spectra meet the pass rule, and none come within ×10.
- This matches my pre-registered prediction.

### Check-also items
- **Up and down ratios (checked).** Up and down get identical exponent structure, by construction. Across the grid and draws (1–99% range), the model's (m₁/m₃)_up / (m₁/m₃)_down lies between 0.18 and 8.7. The data need 1/136 (MZ), 1/176 (GUT) and 1/89 (MIX).
- **Isotropy, generation-blind part (proved; checked).** Speed anisotropy shared by all generations is zero at every order for both pairs. The proof: the residual symmetry's rotations form the tetrahedral group, and the 2-tensors that describe anisotropy have no tetrahedral-invariant component. The check: rank 0 at every order with k₁+k₂ ≤ 8.
- **Isotropy, per-generation part (checked by symmetry counting only).** Anisotropic speeds that differ between generations are not protected:
  - symmetry already allows them with no breaking (3 structures for P, 1 for S);
  - the pairs add more (P: 6; S: 2 for pair (a), 6 for pair (b)).
- **Residual groups (checked).** Pair (a) leaves 48 elements: the tetrahedral rotations plus the even translations. Pair (b) leaves the 12 tetrahedral rotations. The up and down mass matrices commute to about 2e-16 relative.

**General statement (proved, from R1's Lemma B plus Schur's lemma).** If the quark doublets carry P or S, these two vacua give either a permutation CKM or exactly degenerate masses. This holds for every placement of the right-handed fields, every coefficient choice and every order. The left-handed-only arm confirms it: the Yukawa has rank 1 (two generations massless), or for pair (a) with S it vanishes and all three are massless.

### Secondary arms (outside the reading)
These use R1's character labels, the only labels on which the residual symmetry acts by scalars, so CKM is unconstrained.

| Placement | Best fit | Random spectra fitting at least as well |
|---|---|---|
| Same label for all particle types | ×41–57 | 27–37% |
| Left-handed fields only | ×4.4 (MZ), ×4.7 (GUT), ×3.7 (MIX) | 11%, 13%, 5% |

The left-handed arm's random pass rate is 1.7%. Neither arm is within ×3, and neither counts as evidence. Pair (b) with the staggered-character labels does fix the exponents itself, at masses 1, ε₂³ and ε₁ε₂³ (the corner star cubed), but the fit still misses.

### Prior art (main)
- **The CKM kill is already on main.** It is the shared-C3 theorem in `THE_SMALL_MIXING_ANGLES_THETA_C_AND_THETA_13_ARE_C3_BREAKING_ORDER_PARAMETERS_UNIFICATION_NARROW_THEOREM_NOTE_2026-06-08.md` (a shared C3 makes V_CKM a permutation), plus R1's Lemma B, in lattice form. It is not new.
- **Distinct masses under C3** agree with `GENERATION_DEGENERACY_MINIMAL_SYMMETRY_BREAKING_NARROW_THEOREM_NOTE_2026-05-23.md`.
- **Pair (a)'s residual** (tetrahedral rotations plus even translations) is the symmetry `CORNER_FERMION_..._PSEUDOSCALAR_DIRAC_MASS_..._2026-10-17.md` records for its staggered pseudoscalar mass.
- **No two-amplitude flavour fit exists on main.** The grep found only the unrelated neutrino two-amplitude note.
- **New here** (same family, unrefereed): the fit numbers and the per-generation anisotropy counts.

### What this means for the wall (suggested)
For P and S labels, isotropy and CKM pull against each other. The tetrahedral residual that protects isotropy is the same C3 that forces a permutation CKM. Character labels escape this, but they fail ×3, and random spectra do about as well.

### Labels and limits
- **Inputs:** masses are HIER-2's recalled values (not fetched); CKM is fixed at 0.225 / 0.041 / 0.0037 for all three sets; coefficients are random O(1), not computed from a corner model.
- **Search setup:** free sector scales favour the hypothesis; the expansion stops at k₁+k₂ ≤ 8.
- **Status:** same family, unrefereed.
- **Run notes:** the first launch crashed on a print statement after the symmetry section and before any fit result; I fixed it and reran. Diagnostics added after the run are marked as such and do not enter the reading. Peak memory was 238 MB, and nothing is left running. I edited nothing outside T/.

### Files
All in `/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/masswall/T/`:
- `PREREG.md`
- `scripts/t2amp.py`
- `t2amp.out` (the pre-registered run)
- `t2amp_v2.out` (the same run plus the added diagnostics; the pre-registered part is identical)