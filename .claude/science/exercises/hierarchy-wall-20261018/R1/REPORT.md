**R1 report: which BSM-naturalness tools can the qubit-lattice axioms realise natively?**

**Read before concluding.**
- `docs/MINIMAL_AXIOMS_2026-06-29.md` (in full), `PRIMITIVE_REGISTRY_CHECK.md` and `SCALE_REFERENCE_PRIMITIVE_NOTE.md`.
- `derivation_obligations.json`: it has three entries, none on the hierarchy.
- `WALL.md`, the PR #9783 summary, the HIER-1 report, and the header of main's meron no-go note.

**Plain answer.** None of the six tools works natively. Each one turns the hierarchy into one number the axioms do not fix:
- **A coupling at the cutoff**, for technicolour, for warping (read through its four-dimensional dual) and for SUSY breaking.
- **A distance**, for clockwork, domain walls and the relaxion's scan.
- **Registered state data**, for anthropic selection.

Two new lemmas settle the distance case:
- The lattice's own symmetry forbids clockwork in the bulk, in real space. In taste space it does too wherever the 16 corners are related by a symmetry.
- A localisation needs walls, and only records can supply them. So the wall spacing is history data, not something the law outputs.

| Tool | Number it needs | Native? |
|---|---|---|
| Technicolour | g²(M_cut) ≈ 0.29, or near-conformal content | Already mapped: HIER-1(b), HIER-3 G-OUTSIDE |
| Randall–Sundrum warping | k·r_c ≈ 12; its dual is a near-marginal coupling | No fifth dimension. The dual is HIER-1 escape E2 (open, mapped). The one-brane geometry is killed by Lemma B. |
| SUSY | the SUSY-breaking scale | A parameter-free nearest-neighbour exclusion supercharge exists (Fendley–Schoutens, used as a template). But the fermion grading has to be supplied, records cannot be removed, and SUSY protects an exact zero rather than producing a small number (suggested). |
| Clockwork | chain length N, gear ratio q | Forbidden in the bulk (Lemmas A and B); needs walls |
| Relaxion | slope or scan range | The scanner is native; the toy fails (T2) |
| Anthropic | a measure over states | The realized-state primitive rules out any measure or typicality. v becomes registered data (reading of the registry text). |

**Route 1: the localisation family (clockwork, one-brane warping, skin effect, domain walls, taste clockwork; HIER-1 escape E4)**

- **Object.** The light modes of any rule that is covariant under translations and proper cubic rotations, with the qubit as the internal space.
- **Lemma A, transitivity (proved).** Suppose the symmetry group acts transitively and unitarily on the "gears" (sites or taste corners). Then:
  - a non-degenerate mode has equal weight on every gear, because U_gψ = χ(g)ψ gives ‖ψ_gx‖ = ‖ψ_x‖;
  - a degenerate multiplet has equal summed weight on every gear (Schur's lemma).

  So a mode localised on one site needs a privileged site, and the Lattice axiom says "No site is privileged."
- **Lemma B, orientation (proved).** A C₂ rotation about an axis perpendicular to a bond, composed with a translation, reverses that bond.
  - The generator Σc_jQ_j of a protected, non-degenerate mode must then map to ±itself, so |c_j| is symmetric under reversal.
  - With translation-covariant links, c_{j+1}/c_j = q, this forces q² = 1.
  - So nothing can localise at one end: no clockwork q^−N, no single-brane warp, no Hatano–Nelson skin effect.
  - Two-ended structures remain allowed. A wall–antiwall pair splits as e^{−L/ξ}.
- **Consequence for main's candidate (proved).** α_LM^16 = 2.09e-17 has clockwork form q^−16 with q = 11.03. That reading is excluded:
  - The 2^4 block's 16 sites form one orbit of the block translations, so Lemma A applies.
  - 16 gears give at most 15 links in any case.

  So the 16 has to be a determinant degree (HIER-1 item 5).
- **Number it would fix.** v/M_Pl = e^{−L/ξ}.
- **Why that number is not supplied.**
  - L is the distance between two structures that break translations. By Lemma A, only the realized state (records) can supply such structures, so under the realized-state primitive L is registered data.
  - Fermion mass ratios would need a different L or ξ for each species, and HIER-2 found the exponents blind to sector.
- **Strongest objection.**
  - Records are not arbitrary: a formation law might fix the spacing of defects itself.
  - The record arrow of time is a native orientation that Lemma B does not cover.
- **Kill condition** for the claim "the distance is unavoidable": a native formation law whose stationary defect period is fixed by the law and is at least about 28 sites.
- **The time-arrow variant (suggested).** If v ∝ q^−N_t over ticks N_t, then d ln v/d ln t = −N_t ln q, which breaks the constancy of v required by Big Bang nucleosynthesis by an enormous margin. It survives only if it froze at N_t* = 38.4/ln q ticks, and that freeze-out time is history data.
- **Test (run; log `t1.log`; all pre-registered readings met; checked).**
  - **Lemma A:** the largest weight deviations were 1e-13 on the ring, 6e-14 on the 4³ torus with spin-½ cubic action, and 8e-13 on the 2^4 block with antiperiodic time.
  - **Lemma B, clockwork chain:**
    - The end ratio is 9.5e-7 = 2^−20.
    - Adding the bond-reversed partner with weight w lifts the zero mode to λ_min ≈ 2.25w.
    - Covariance forces w = 1, which gives λ_min = 1.79 and end ratio 1.
  - **Lemma B, skin effect:** the localisation rate is 0.2996 at asymmetry g = 0.3 and zero at g = 0.
  - **Two walls on the Wilson–Dirac qubit chain:**

    | Wall mass m₀ | Decay length ξ (sites) | Wall separation L* for 2e-17 (sites) |
    |---|---|---|
    | 0.25 | 3.47 | 131 |
    | 0.5 | 1.44 | 55 |
    | 0.75 | 0.72 | 28 |

    L* is the named number.
  - **Taste clockwork:** it needs a gear ratio q ≥ 13 over 15 links, or q ≥ 1.5e4 along the 4-link geodesic. Either one is a ratio of two supplied amplitudes (the "two amplitudes" escape).
- **Cheapest next test.** List the law-fixed defect periods of main's built formation laws and check whether any reaches about 28 sites. Two I know: the block 117 chessboard has period 2, and the block 132 walls sit antipodally, so their spacing is L/2 — again a size, not a law output.

**Route 2: relaxion on the record count (covers the uncovered "record count / history" item)**

- **Object.** Records are permanent, so the local record fraction s_i can only rise. That makes it a native monotone scanner (proved from the Record axiom).
- **Construction.**
  - The Higgs mass parameter is μ²_i = M²(1 − 2s_i).
  - Records form with probability p per tick while μ²_i > 0.
  - Formation stops where the vev turns on (backreaction).
- **Number it would fix.** v²/M_Pl² is the frozen floor F = ⟨|μ²|⟩; the target is about 4e-34.
- **Why that number is not supplied.** The axioms leave the formation rate open, and the averaging needs a scan region of some size.
- **Test (run on 48³; log `t2.log`; toy result, checked).**
  - The pre-registered reading NATIVE-RELAX-FAIL holds: at p = 1 with a nearest-neighbour box, F = 1.0.
  - For p ≤ 0.03 the floor is:

    | Scan box | 3³ | 5³ | 9³ | 17³ |
    |---|---|---|---|---|
    | Floor F | 0.19 | 0.11 | 0.056 | 0.027 |

  - **The floor does not depend on the rate** (d ln F/d ln p = 0.00 to −0.03). It falls only as V^−0.37 with scan volume V.
  - So the named number is the scan size, not the rate. My pre-registration guessed the rate; the data say volume.
  - Extrapolating, reaching 4e-34 needs a scan region about 10^29–10^33 sites across. No nearest-neighbour rule supplies that.
- **Strongest objection.** A real relaxion is one homogeneous field that averages globally. Reproducing that needs a massless mediator, and its scan range would then be the causal volume, which is history data.
- **Kill condition.** Met for the native local version.
- **Cheapest next test** (only if someone proposes a mediator). Rerun the toy with a global average and see whether the floor tracks 1/V or p.

**Prior art on main.**
- **No prior hits:** clockwork, relaxion, partial compositeness and Kaplan do not appear on main.
- **Already mapped, so not presented as new:**
  - the meron route e^{−4π²} (`HIERARCHY_MERON_SUBSTRATE_BRIDGE_SU2_SU3_MISMATCH_NARROW_NO_GO_NOTE_2026-05-16.md`);
  - domain-wall fermions, which appear only as a species-count regulator (`HIERARCHY_ALPHA_LM_EXPONENT_SPECIES_COUNT_BRIDGE_REGULATOR_DEPENDENCE_NO_GO_NOTE_2026-05-10.md:25,195`);
  - HIER-1's escapes E4 (clockwork and taste clockwork) and E2 (walking).
- **New here:** Lemmas A and B, the exclusion of α_LM^16 as a clockwork, and the T2 result that the floor tracks scan volume rather than rate.

**Not claimed.** I have not derived either hierarchy, and nothing here is a no-go beyond these six tools. No referee has checked this yet, and any referee would be from the same model family.

**Files** (in `/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/hierwall/R1/`):
- `PREREG.md`
- `t1_localisation.py`, `t1.log`
- `t2_relaxion_toy.py`, `t2.log`

Both tests ran under `capped.sh` (peak memory 80 MB), and no processes are left running.