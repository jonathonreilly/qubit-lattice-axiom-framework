## **Searches run.**

- Read `ref/README.md` first. It locates “Ledger rows: main/docs/audit/data/ledger/” (line 2) and the consolidation notes (line 3).
- Initial terms: `SGAP0`, `S-GAP⁰`, `HF-alt`, `G1′`, `charged gap`, `Fröhlich`, `Frohlich`, `odd.weight`, `Koteck`. Searched `ref/main/docs`, `ref/pr*/`, `ref/ym/`, and the TOE folder.
- Follow-ups: `strong.coupling gap`, `parity.sector`, `Yarotsky`, `Lie.Schwinger`, `alternating.sector`, `sector comparison`. Read relevant notes, ledger rows, drafts, referee reports, prior digests and `LIT_SMG.md`.
- `briefs/SGAP0.txt` was absent. No `SGAP0` entry appeared in `TOE_ASSEMBLY.md`. The explicit subtarget is “**S-GAP⁰** is the same statement with `t=0`” (`T/SGAP.md:20`).
- Read only. No internet, git, edits or proof judgments.

Path abbreviations:

| Alias | Path |
|---|---|
| `T/` | `repo/.claude/science/physics-loops/toe-assembly-20261104/` |
| `M/` | `ref/main/docs/` |
| `C` | `ref/pr10131/docs/CHIRALITY_DOUBLERS_CONSOLIDATED_BOUNDED_THEOREM_NOTE_2026-10-30.md` |
| `E` | `M/THREE_STATE_CLOCK_ENDPOINT_REFLECTION_SECTOR_ENERGY_AND_GROUND_DEFECT_BOUND_BOUNDED_THEOREM_NOTE_2026-09-15.md` |
| `Y` | `M/GAUGE_WILSON_ELECTRIC_DOMINATED_VOLUME_UNIFORM_GAP_BOUNDED_THEOREM_NOTE_2026-09-07.md` |
| `S` | `M/SPIN10_SYMMETRIC_ATOMIC_GAPS_MIRROR_BOUNDARY_PROJECTION_AND_CURRENT_RESPONSE_BOUNDED_THEOREM_NOTE_2026-09-14.md` |
| `H` | `M/ADMISSIBILITY_RULE_THE_HARD_CORE_SEA_ON_A_RING_IS_ONE_TWISTED_BAND_HALF_FILLED_WITH_HALF_THE_FREE_SEAS_VOLUME_TERM_AND_CLOCK_STIFFNESS_BOUNDED_THEOREM_NOTE_2026-09-24.md` |

## **Already in the repo.**

- **The target is open.** S-GAP⁰ requires positive constants uniform over allowed rings and small `ε/τ`, with charged energies above the full half-filled ground energy. Its definition says “`E_χ≥E_0+Δτ`” and includes `ε=0` (`T/SGAP.md:20`). SGAP is frozen, but S-GAP⁰ remains “**OPEN**”; its results are conditional finite-ring statements and “not an audit verdict” (`T/SGAP.md:3`).

- **The atom and character algebra are available.** SMG1 Theorem 2.2 gives one copy of each character and spectrum “`−14` once, `0` eight times in odd parity, and `2` seven times in even parity” (`T/SMG1.md:53`). SMG15 gives rank-one projectors and the character-shift rule; genuine intersite degree-four mixing “is off-diagonal in configurations” (`T/SMG15.md:32`). These are frozen scoped results (`T/SMG1.md:3,7`; `T/SMG15.md:3`: “conditional on the atom”).

- **The gauge reduction is exact on the stated rings.** SMG15 Theorem 2 gives “`J:F_even⊗C²→H_G`” and sends parity-preserving matter operators to themselves tensored with the identity (`T/SMG15.md:40`: “maps to itself tensored with `1`”).

- **The unperturbed charged gap is already settled.** At `ε=0`, every nontrivial allowed charge has “`E_σ=E_L+16τ`” (`T/SGAP.md:34`). At `t=0`, this reads “`E_1=0` and `E_σ=16τ` directly” (`T/SGAP.md:36`). Thus any successful uniform constant must satisfy `Δ≤16` (`T/SGAP.md:56`: “sharpens this to `Δ≤16`”).

- **The complete `t=0` reduction is available.** Theorem 4 splits the Gauss space into “`2^{L−1}` sectors” (`T/SGAP.md:62`) with “`H_ε|K_p=H_p⊗1`” (`T/SGAP.md:64`). Each chain has 16-level sites, a unique product on-site zero vector, and “an on-site gap `14τ`” (`T/SGAP.md:66`). The product has `N=k(p)`, so it need not be half filled (same line: “has `N=k(p)`”).

- **Second order favours alternating parity patterns.** Proposition 4.2 gives the correction “`−2ε² walls(p)/(7τ)`”, minimized by the two alternating, half-filled patterns (`T/SGAP.md:80`). Its status stops there: “Higher orders are not bounded here” (same line). This is the restriction of SMG15’s exact atomic resolvent identity (`T/SGAP.md:82`: “already-proved”; `T/SMG15.md:138`: “`2/(7τ)`”).

- **A sufficient conditional route is already stated.** Uniform sector stability (G1) and the filling comparison (HF′) imply a charged gap `Δ_G−δ`, provided `δ<Δ_G` (`T/SGAP.md:89`: “S-GAP⁰ follows”). The weaker charged-only hypothesis (G1′) also suffices with (HF′), but is “unproved and not adopted” (`T/SGAP.md:93`). Under (G1), the alternating-sector comparison
  `e_{p_alt}−min_p e_p≤δτ`
  implies (HF′); HF-alt is also “unproved and not adopted” (`T/SGAP.md:95`).

- **Charge removal supplies another conditional route.** The local unitary obeys “`YH_εY=H_ε+B`” (`T/SGAP.md:46`). The removal bound gives
  “`E_σ−E_1≥16τ−4√2|ε|√(W_odd/w)`”
  when `w>0` (`T/SGAP.md:113`). The referee closure makes `W_odd≤Kw` sufficient for small coupling, with `K` independent of size (`T/SGAP.md:119`: “Then S-GAP holds”).

- **Two structural limits are proved.** At `t=0`, every half-filled charge-sector level has “even multiplicity”; the ground vector is therefore not unique at zero electric coupling (`T/SGAP.md:97`). Proposition 5.1 also supplies a paired trial bound and some `ε′∈(0,ε]` where every charged ground vector has “`W_odd≥Lε²/(200704τ²)`” (`T/SGAP.md:123,125`).

- **The solved exact families have narrower hypotheses.** The configuration-conserving family has charged cost at least “`14τ−2δ`” (`T/SMG15.md:66`), but “preserves every configuration” (`T/SMG15.md:62`). SGAP explicitly says it does “not cover the off-diagonal `H_4`” (`T/SGAP.md:38`). Circuit dressing preserves sector spectra (`T/SMG15.md:114`: “exactly that of `H_A`”), but is “a fine-tuned example” (`T/SMG15.md:130`).

- **Earlier stability applications are conditional comparators.** SMG1 gives a uniform open-segment gap conditional on Fröhlich–Pizzo (`T/SMG1.md:118`: “uniformly in length”); the theorem is “cited, not rebuilt”, with ring versions still open (`T/SMG1.md:122`). The 3450 cell construction cites a persistent-gap theorem for different, vector-like content (`C:1491`: “doubled (vector-like) chain content”; `C:1493`: “cited with its constant not computed”). These consolidation statements are “author statements for review” (`C:11`).

- **Main contains a different volume-uniform sector comparison.** The three-state clock note proves, within its supplied model, “`H_cons >= e0 I-c n1 >= e0 I-c N`” (`E:351`), with constants that “do not depend on L” (`E:356`). Its method uses reflection and charge-pattern dissemination (`E:271,282`: “chessboard inequality”). Its domain is dyadic three-dimensional tori; “arbitrary non-dyadic sizes are not claimed” (`E:311`). Ledger status is `"effective_status": "unaudited"` (`M/audit/data/ledger/th/three_state_clock_endpoint_reflection_sector_energy_and_ground_defect_bound_bounded_theorem_note_2026-09-15.json:27`).

- **Main also contains a carefully scoped Yarotsky application.** The compact SU(3) note obtains a small-coupling volume-uniform gap through an imported theorem (`Y:26`: “uniform in volume”). It explicitly says “We import the theorem” (`Y:38`) and distinguishes finite-volume boundary conventions (`Y:66`: “not identical”). Its surface is `conditional-support` (`Y:16`); its ledger is unaudited (`M/audit/data/ledger/ga/gauge_wilson_electric_dominated_volume_uniform_gap_bounded_theorem_note_2026-09-07.json:31`).

- **A free half-filling comparator exists.** On its distinct uniform ring model, “the lowest state over all `N` is half filled” (`H:112`). This is bounded-support and unaudited (`H:23`; `M/audit/data/ledger/ad/admissibility_rule_the_hard_core_sea_on_a_ring_is_one_twisted_band_half_filled_with_half_the_free_seas_volume_term_and_clock_stiffness_bounded_theorem_note_2026-09-24.json:31`: `"unaudited"`). The SGAP referee explicitly says it “does not transfer to the interacting `t=0` chains” (`T/SGAP_REFEREE.md:174`).

## **Failed attempts on file.**

- **A4, summed charge removal.** The missing step is “`W_odd≤Kw` uniformly in `L` and `ε`” (`T/SGAP.md:139`). The extensive odd-weight result does not disprove that bound, but the removal identity supplies no required lower bound on `w` (same line: “does not supply it”).

- **A5, unrestricted local windows.** The required strict energy increase fails because “`λ_min(K+B)=λ_min(K)` exactly” (`T/SGAP.md:145`). This refutes that shortcut, not S-GAP (same line: “does not refute S-GAP”).

- **A6, half-filled comparison within every parity sector.** Proposition 4.1 exhibits a sector whose neutral and charged minima both equal “`28τ`, while `E_0=0`” (`T/SGAP.md:72`). The remaining elementary estimates are extensive and “do not yield the needed `O(τ)` comparison” (`T/SGAP.md:147`).

- **Local Schrieffer–Wolff plus a global norm estimate.** The block-diagonal estimate is unproved; summing local remainder norms produces “a bound growing with `L`” (`T/SMG15.md:158`).

- **Naive absolute light-linked polymers.** The possible `|z|⁻²` contribution has a logarithmically divergent absolute sum. Complete weights and cancellations were not settled (`T/SMG15.md:159`: “does not … exclude cancellations”). This concerns moving light modes; the `t=0` sector reduction removes that particular obstacle (`T/SGAP.md:70`: “absent at `t=0`”).

- **Fröhlich–Pizzo on the unsplit reference.** Its on-site kernel is “two-dimensional”; splitting the fifth mode instead gives “an empty, rather than half-filled, reference chain” (`T/SMG15.md:160`).

- **Fixed-volume Feshbach control for a different atom.** The estimate “retains v’s volume dependence” (`S:235`) and is “not a volume-uniform expansion” (`S:239`). The same note rejects Gaussian replacement: the four-point function “cannot follow by applying Wick’s rule” (`S:272`). Its ledger is unaudited (`M/audit/data/ledger/sp/spin10_symmetric_atomic_gaps_mirror_boundary_projection_and_current_response_bounded_theorem_note_2026-09-14.json:27`: `"unaudited"`).

- **All-order cancellation inferred from circuit equivalence.** The original projection and dressing “need not commute”; only cancellation through order `ε³` is stated, with higher orders unsettled (`T/SMG15.md:130`).

## **Overlap with this lane's results.**

not run

## **Missed inputs.**

- **Start from the frozen parity chains.** They already have a unique on-site zero vector and gap `14τ` (`T/SGAP.md:66`: “unique product on-site zero vector”). This removes the unsplit-kernel obstacle. It leaves a native stability argument and the separate filling comparison (`T/SGAP_REFEREE.md:133`: “remain unproved hypotheses”).

- **Use the weakest sufficient comparison.** Exact alternating-sector minimization is stronger than required. HF-alt permits an error `δτ` (`T/SGAP.md:95`: “`e_{p_alt}−min_p e_p≤δτ`”), and the sufficient condition only needs `δ<Δ_G` (`T/SGAP.md:89`). This changes the comparison target from exact ordering to a controlled bounded error.

- **Test the clock note’s reflection method as an alternative input.** It compares sector energies without requiring every checkerboard energy to exceed the neutral one (`E:357`: “does not require proving e1>=e0”). A transfer would require establishing the corresponding reflection structure for SGAP’s chains. Its existing theorem is limited to its supplied model and dyadic topology (`E:469`: “specified model, dyadic periodic topology”).

- **Reuse the scope accounting in earlier stability applications.** The SU(3) note keeps the analytical import explicit (`Y:38`: “not a claimed complete independent reconstruction”). Its boundary convention is part of the theorem (`Y:64`: “whole-group rule”). These inputs identify hypotheses SGAP0 must establish for its periodic, parity-dependent chains.

- **Keep the second-order preference and exact comparison separate.** Alternating patterns minimize the formal term, but “Higher orders are not bounded here” (`T/SGAP.md:80`). A sector expansion with controlled local energy terms is already proposed, “not … an attempted construction” (`T/SGAP.md:147`).

- **Preserve the scope of a successful result.** S-GAP⁰ asks for finite-ring charged separation, “not GNS or tick statements” (`T/SGAP.md:20`). It cannot supply uniqueness at these parameters (`T/SGAP.md:97`: “not unique”).

## **Consumers.**

| Consumer | Weakest form needed |
|---|---|
| **SGAP / S-GAP⁰** | A uniform charged-sector lower bound plus a filling comparison whose error is smaller than the sector gap. The existing implication is “`E_σ≥E_0+(Δ_G−δ)τ`” (`T/SGAP.md:89,93`). |
| **SMG15 / R1.5-D** | The `t=0` charged-gap subcase. Generic decoupling still needs additional work: R1.5-D “contains S-GAP and R1.5-U” (`T/SMG15.md:162`). |
| **SMG1 R2 and R3-D** | A transferable stability-and-comparison method, with hypotheses re-established for chiral or two-dimensional light sectors. R2 imports “R1.5 (decoupling)” (`T/SMG1_OUTLINE.md:190`); R3 imports “R1, R1.5” (`T/SMG1_OUTLINE.md:200`). |
| **CH1 / W2** | Eventually, selective mirror removal “without releasing light partners” (`T/TOE_ASSEMBLY.md:457`). The higher-dimensional target requires “every mirror and doubler gapped” (`T/TOE_ASSEMBLY.md:732`). S-GAP⁰ supplies an earlier subcase only (`T/SGAP.md:151`: “Neither the finite-ring result nor the proposed reading establishes the higher-dimensional chirality target”). |
| **YM branch** | No direct SGAP0 consumer found. The explicit later interface is matter: “T0 is pure gauge”, and CH1’s chiral fermions are “outside T0’s statement” (`T/TOE_ASSEMBLY.md:620`). |