## **Searches run.**

- Read `ref/README.md` first. It identifies “Ledger rows: main/docs/audit/data/ledger/” (line 2), consolidation notes (line 3), and the YM corpus (line 5).
- Searched `ref/main/docs`, `ref/pr*/`, `ref/ym/`, and `repo/.claude/science/physics-loops/toe-assembly-20261104/`.
- Initial terms: `SGAP`, `S-GAP`, `Schrieffer`, `polymer`, `mirror gap`, `density interaction`, `Fröhlich`, `Frohlich`, `strong-coupling gap`.
- Follow-ups: `gapless`, `gapless remainder`, `SMG1`, `mirror gapp`, `gapless sector`, `R1.5`, claim numbers, and ledger statuses. Read relevant parts, drafts, referee reports, prior digests and `LIT_SMG.md`.
- `briefs/SGAP.txt` was absent. No separate SGAP target was found in `TOE_ASSEMBLY.md`; the explicit stopping statement is in `SMG15.md:148–152`.
- Used only the permitted file commands. No edits, git, internet searches or proof judgments.

Path abbreviations:

| Label | Path |
|---|---|
| `T/` | `repo/.claude/science/physics-loops/toe-assembly-20261104/` |
| `M/` | `ref/main/docs/` |
| `C` | `ref/pr10131/docs/CHIRALITY_DOUBLERS_CONSOLIDATED_BOUNDED_THEOREM_NOTE_2026-10-30.md` |
| `S` | `ref/main/docs/SPIN10_SYMMETRIC_ATOMIC_GAPS_MIRROR_BOUNDARY_PROJECTION_AND_CURRENT_RESPONSE_BOUNDED_THEOREM_NOTE_2026-09-14.md` |
| `H` | `ref/main/docs/ADMISSIBILITY_RULE_THE_HARD_CORE_SEA_ON_A_RING_IS_ONE_TWISTED_BAND_HALF_FILLED_WITH_HALF_THE_FREE_SEAS_VOLUME_TERM_AND_CLOCK_STIFFNESS_BOUNDED_THEOREM_NOTE_2026-09-24.md` |

## **Already in the repo.**

- **SGAP’s precise target remains open.** It asks for an `L`-uniform charged-sector gap for the eight-Majorana atom, light hopping and the specified degree-four mixing, on half-filled gauged rings. The quantifiers include “`|t|,|ε|≤c₀τ`” (`T/SMG15.md:148`); the conclusion is “at least `Δτ` above its ground energy” (`T/SMG15.md:152`). That line explicitly says: “This includes `t=0`” and “A unique ground state is a separate question.”

- **The mirror atom is available.** SMG1’s Theorem 2.2 gives spectrum −14, 0, 2, with a unique “`S`-fixed and even” ground vector (`T/SMG1.md:53`). Lemma M classifies genuine symmetric mixing: “degree at least 4,” with degree four restricted to a same-flavour mirror pair times a number-conserving light pair (`T/SMG1.md:139`). SMG1 is “FROZEN” (`T/SMG1.md:3`); its results are “not an audit verdict” (`T/SMG1.md:7`).

- **Configuration algebra identifies why SGAP is outside the exact diagonal family.** SMG15’s Theorem 1 gives rank-one character projectors and states that genuine intersite degree-four mixing “is off-diagonal in configurations” (`T/SMG15.md:30`). Its status is frozen, conditional on SMG1’s atom (`T/SMG15.md:3`: “conditional on the atom”).

- **The gauged ring has an exact reduction.** Theorem 2 identifies the physical space through “`J:F_even⊗C²→H_G`” (`T/SMG15.md:38`). The residual holonomy gives a wrap-bond sign at zero electric coupling (`T/SMG15.md:44`: “produces a wrap-bond sign”). These are finite-ring identities, under the frozen status above.

- **An exact configuration-conserving family already has the desired charged gap beside light levels.** Under `δ<7τ`, all globally charged levels “cost at least `14τ−2δ`”; below that threshold the spectrum is “exactly the free half-filled light spectrum” (`T/SMG15.md:64`). The hypothesis is configuration conservation (`T/SMG15.md:60`: “preserves every configuration”). This does not cover SGAP’s off-diagonal degree-four perturbation.

- **A specially dressed family preserves sector spectra.** Theorem 6 says its spectrum in each global `S` sector is “exactly that of `H_A`” (`T/SMG15.md:112`). Its scope is restricted: for small nonzero dressing, it “is not the R-GEN generator of any certified NN-a decomposition” (`T/SMG15.md:120`). The source calls it “a fine-tuned example” (`T/SMG15.md:128`).

- **The atomic second-order identity directly matches SGAP’s mixing.** Theorem 7 gives “`PH_4P=0`” and resolvent coefficient “`2/(7τ)`” (`T/SMG15.md:136`). For the hopping light factor, the formal correction includes repulsive density coefficient “`4ε²/(7τ)`” (`T/SMG15.md:138`). Its limitation is explicit: higher orders are “not bounded here,” and it “does not yield volume-uniform decoupling” (`T/SMG15.md:142`).

- **The light-sector twist is already proved separately.** Theorem 5 supplies a same-sector orthogonal state with “`⟨Φ,HΦ⟩≤E₀+C_h/L`” (`T/SMG15.md:96`). Corollary 5.1 combines S1 and uniqueness to obtain a trivial-sector gap at most `C_h/L` (`T/SMG15.md:102`). It “neither proves S1 nor uniqueness” and gives only “a second low state” (`T/SMG15.md:106`).

- **Existing stability results concern different reference states.** SMG1’s zero-hop product contains an empty fifth mode, “`|0⟩_{5,x}`” (`T/SMG1.md:77`). Its hopping theorem is conditional and restricted to open segments: “uniformly in length” (`T/SMG1.md:118`). The imported theorem is “cited, not rebuilt”; rings and the infinite chain remain open (`T/SMG1.md:122`).

- **The eight-Majorana precursor supplies finite evidence only.** Logged #10078 reports the same Cayley atomic spectrum and proxy chains through eight sites. Its exclusions include “gauge fields, L > 8” and “the slab with bulk and light wall” (`C:2341`). Consolidation statements are “author statements for review” (`C:11`).

- **Main contains distinct mirror-elimination calculations.** A quadratic atom–bath coupling cancels to second order: “the induced term is a constant” (`S:256`). A bare comparator has a fourth-order “nonzero attractive density interaction” (`S:293`). Its coefficient is “not imported unchanged into the refined Spin(10) atom” (`S:297`). Source status is “conditional-support” (`S:7`); the ledger says `"effective_status": "unaudited"` (`M/audit/data/ledger/sp/spin10_symmetric_atomic_gaps_mirror_boundary_projection_and_current_response_bounded_theorem_note_2026-09-14.json:27`).

- **A separate half-filled ring comparator exists.** Its reduction is “one spinless band whose wrap bond carries `R`” (`H:90`). For uniform rings with four dividing their length, “the lowest state over all `N` is half filled” (`H:112`). It is “bounded-support” and “unaudited” (`H:23`), also recorded as unaudited in its ledger (`M/audit/data/ledger/ad/admissibility_rule_the_hard_core_sea_on_a_ring_is_one_twisted_band_half_filled_with_half_the_free_seas_volume_term_and_clock_stiffness_bounded_theorem_note_2026-09-24.json:31`).

- **Other polymer and gap machinery has narrower scope.** The retained-Grassmann polymer note controls an explicit “high-mass” region (`M/WILSON_STAGGERED_RETAINED_GRASSMANN_TWO_LAYER_KP_POLYMER_NORM_BOUNDED_THEOREM_NOTE_2026-07-12.md:12`); its ledger is unaudited (`M/audit/data/ledger/wi/wilson_staggered_retained_grassmann_two_layer_kp_polymer_norm_bounded_theorem_note_2026-07-12.json:30`). PR #10135’s gauge-gap theorem has a “full-space gap” (`ref/pr10135/docs/MDTN_TRUNCATED_GAUGE_STRONG_COUPLING_PHYSICAL_GAP_BOUNDED_THEOREM_NOTE_2026-10-31.md:150`), with the BHM rebuild still an “open obligation” (same file, line 31). Neither statement supplies the missing charged gap beside SGAP’s gapless remainder.

## **Failed attempts on file.**

- **Local Schrieffer–Wolff:** the remainder estimate becomes extensive. The referee records that the norm bound “grows with `L`,” so Weyl’s inequality gives no uniform sector gap. The proposed block-diagonal bound was also “plausible,” not proved (`T/SMG15_REFEREE.md:245`).

- **Absolute light-linked polymers:** the indicated absolute sum diverges logarithmically. The referee identifies nonzero “`|z|⁻²` tails,” while preserving the qualification that “other representations or resummations are not excluded” (`T/SMG15_REFEREE.md:246`).

- **Fröhlich–Pizzo applied to the half-filled reference:** hypothesis (1.4) “needs a one-dimensional on-site kernel.” The unsplit reference is degenerate; adding the fifth-mode splitting “empties the light chain” (`T/SMG15_REFEREE.md:247`).

- **Fixed-volume Feshbach control:** the error retains the hopping norm’s volume dependence. Main says “the bound retains v’s volume dependence” (`S:235`) and “not a volume-uniform expansion” (`S:239`).

- **Gaussian replacement of the interacting atom:** the failing step is reconstructing higher correlations from its propagator. The four-point function “cannot follow by applying Wick’s rule” (`S:272`).

- **All-order cancellation inferred from circuit equivalence:** the projection onto the original mirror ground space need not commute with dressing. The corrected result is “induced terms vanish through order `ε³`”; higher orders are unsettled (`T/SMG15.md:128`).

- **Earlier selective-gapping routes:** logged #9909 “gaps both light copies and cannot select one” (`C:2315`). Kept #9911 releases the one-dimensional partner “at p = pi” (`C:301`). Kept #9992 “releases every light mode the mirror was pairing,” within an SU(4) toy at `L≤6` (`C:519`). These are different models, under the consolidation’s author-review status (`C:11`).

- **Far-wall atomic freezing:** #10060’s gapped far layer leaves a branch that “moves one layer in” (`C:1491`). Its cited stability concerns “the doubled (vector-like) chain content,” not selective slab decoupling (same line).

- **Finite-size persistence:** #10004 says survival of its K gap at infinite volume “is not established: inconclusive” (`C:721`). The #10076 follow-up likewise says “persistence is not established” (`C:2255`).

## **Overlap with this lane's results.**

not run

## **Missed inputs.**

- **Use the configuration criterion before transferring an exact-family argument.** It would identify the precise new step: SGAP’s degree-four term is “off-diagonal in configurations” (`T/SMG15.md:30`), whereas the solved family “preserves every configuration” (`T/SMG15.md:60`).

- **Retain the full `t=0` quantifier.** SGAP “includes `t=0`” (`T/SMG15.md:152`). An argument assuming `ε²≪τ|t|` would therefore address a smaller target. The existing ratio is only a “useful proposed weak-interaction diagnostic” (`T/SMG15.md:142`).

- **Carry the induced interaction and higher cumulants.** The exact resolvent identity supplies the leading coefficient (`T/SMG15.md:136`: “`2/(7τ)`”). Main’s fourth-order comparator shows why a simple atomic propagator does not remove induced density interactions (`S:293`: “nonzero attractive density interaction”). This changes the effective light theory that must be controlled.

- **Use the repaired scope of prior RG tools.** The KMS-related note proves “only scalar ODE consequences” (`M/KMS_FERMIONIC_BRYDGES_MAJORANT_EXTERNAL_NARROW_THEOREM_NOTE_2026-05-11.md:14`). Any application must separately supply the “BBF/Polchinski inequality” and its hypotheses (same file, line 89). The existing retained-Grassmann bound is high mass, so its transfer to this gapless chain remains an additional obligation.

- **Keep finite-ring, GNS and tick conclusions distinct.** The exact family’s GNS spectral statement needs local vectors “to be a core” (`T/SMG15.md:74`). The owner’s adopted generator reading says “Tick stationarity remains a separate requirement” (`T/TOE_ASSEMBLY.md:261`). These inputs determine what a successful SGAP statement can pass downstream.

## **Consumers.**

| Consumer | Weakest form needed |
|---|---|
| **SMG15 / R1.5-D** | The stated uniform charged-sector gap for the specified degree-four model. Full decoupling still requires more: R1.5-D “contains S-GAP and R1.5-U” (`T/SMG15.md:160`). |
| **SMG15’s twist corollary** | S1 plus separately established uniqueness. The existing conclusion is conditional: “Under S1 and S3” the trivial-sector gap is at most `C_h/L` (`T/SMG15.md:102`). |
| **SMG1 R2** | A reusable mirror-gap and decoupling method, then an extension to chiral light content. R2 “Imports. R1.5 (decoupling)” (`T/SMG1_OUTLINE.md:190`) and assigns decoupling “with a chiral light sector” separately (`T/SMG1_OUTLINE.md:192`). |
| **SMG1 R3-D** | A method whose hypotheses can be re-established in two dimensions. R3 imports “R1, R1.5” (`T/SMG1_OUTLINE.md:200`); its two-dimensional decoupling statement remains open (`T/SMG1_OUTLINE.md:204`: “open: R3-D”). |
| **W2 / CH1, then family work** | Eventually a higher-dimensional selective mirror gap preserving the intended light sector. CH1 requires mirror removal “without releasing light partners” (`T/TOE_ASSEMBLY.md:457`). W2 targets “every mirror and doubler gapped” (`T/TOE_ASSEMBLY.md:728`). Family work waits until “W2’s rung 2” (`T/TOE_ASSEMBLY.md:734`). SGAP supplies only an earlier rung. |
| **YM branch** | No direct SGAP consumer found. The assembly’s explicit matter interface is later: “T0 is pure gauge,” and chiral matter lies “outside T0’s statement” (`T/TOE_ASSEMBLY.md:616`). |