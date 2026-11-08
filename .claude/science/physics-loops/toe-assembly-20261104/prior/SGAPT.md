**Searches run.**

- Read `ref/README.md` first. It identifies “Ledger rows: main/docs/audit/data/ledger/” at line 2 and consolidation notes at line 3.
- Initial terms: `SGAPT`, `strong.coupling`, `spectral gap`, `analytic perturbation`. Searched `ref/main/docs`, `ref/pr*/`, `ref/ym/`, and `repo/.claude/science/physics-loops/toe-assembly-20261104/`.
- Follow-ups: `gap stability`, `charged gap`, `gapless remainder`, `Fröhlich`, `Frohlich`, `Yarotsky`, `G1′`, `SGAP`, and nonzero hopping. Read relevant parts, drafts, referee reports, `LIT_SMG.md`, consolidation entries, and ledger rows.
- `SGAPT_DRAFT.md` and `briefs/SGAPT.txt` were absent. No `SGAPT` entry was found in `TOE_ASSEMBLY.md`. The matching available target is tree node **S**, “S-GAP at nonzero hopping” (`T/SMG1_TREE.md:765`). Its identification with SGAPT is inferred.
- No internet search, git, edits, or proof judgments.

Paths below use these aliases:

| Alias | Path |
|---|---|
| `T/` | `repo/.claude/science/physics-loops/toe-assembly-20261104/` |
| `M/` | `ref/main/docs/` |
| `L/` | `ref/main/docs/audit/data/ledger/` |
| `C` | `ref/pr10131/docs/CHIRALITY_DOUBLERS_CONSOLIDATED_BOUNDED_THEOREM_NOTE_2026-10-30.md` |
| `F` | `M/GAUGE_WILSON_FINITE_PW_UNIFORM_STATIC_SOURCE_ENERGY_BOUNDS_BOUNDED_THEOREM_NOTE_2026-09-07.md` |
| `B` | `M/SPIN10_SYMMETRIC_ATOMIC_GAPS_MIRROR_BOUNDARY_PROJECTION_AND_CURRENT_RESPONSE_BOUNDED_THEOREM_NOTE_2026-09-14.md` |
| `K` | `M/WILSON_STAGGERED_RETAINED_GRASSMANN_TWO_LAYER_KP_POLYMER_NORM_BOUNDED_THEOREM_NOTE_2026-07-12.md` |
| `Q` | `M/KMS_FERMIONIC_BRYDGES_MAJORANT_EXTERNAL_NARROW_THEOREM_NOTE_2026-05-11.md` |

**Already in the repo.**

- **The nonzero-hop target is open.** It asks for a charged-sector gap uniform in ring length over `|t|,|ε|≤c₀τ`. The setting retains `L∈4N`, `L≥8`, canonical half filling, and zero electric coupling (`T/SGAP.md:21–23`: “`E_χ≥E_0+Δτ`”; `T/SMG1_TREE.md:789`: “`N=L/2`”; line 791: “Status: OPEN”). The tree is an unchecked sketch: “no node below is proved by this file” (`T/SMG1_TREE.md:1`).

- **The underlying TOE results have frozen author status.** SMG1, SMG15, SGAP, and SGAP0 each say “FROZEN” in their status blocks (`T/SMG1.md:3`; `T/SMG15.md:3`; `T/SGAP.md:3`; `T/SGAP0.md:3`). SGAP explicitly says “not an audit verdict” (`T/SGAP.md:3`).

- **The mirror atom and configuration algebra are available.** The atom has spectrum −14 once, zero eight times, and two seven times. Its ground vector is “`S`-fixed and even” (`T/SMG1.md:53`). Each character projector has rank one. Genuine intersite degree-four mixing is “off-diagonal in configurations” (`T/SMG15.md:32`). These are the frozen scoped inputs above.

- **The finite-ring Gauss reduction is exact.** Theorem 2 supplies “`J:F_even⊗C²→H_G`” and the wrap-bond holonomy action (`T/SMG15.md:40`). At zero electric coupling, holonomy “produces a wrap-bond sign” (`T/SMG15.md:46`). This preserves the ring’s two holonomy sectors.

- **The entire `ε=0` slice is solved, including moving light fermions.** For every real `t`, neutral energy is `E_L`, and every allowed nontrivial charge costs exactly `16τ` (`T/SGAP.md:36`: “`E_σ=E_L+16τ`”). Thus any S-GAP constant must satisfy `Δ≤16` (`T/SGAP.md:58`: “sharpens this to `Δ≤16`”).

- **Charge removal already reduces the question to a local perturbation.** Theorem 3 gives “`YH_εY=H_ε+B`” and identifies the charged block with a modified neutral block (`T/SGAP.md:48`). A positive comparison must cover “all seven” nontrivial even characters (`T/SGAP.md:58`).

- **The zero-hop reduction and charged gap are now proved.** At `t=0`, the model splits into `2^{L−1}` parity chains with “an on-site gap `14τ`” (`T/SGAP.md:64–68`). The later frozen amendment supersedes the older open labels: “S-GAP⁰ proved” (`T/SGAP.md:5`). SGAP0 gives `E_σ≥E_0+7τ` for `|ε|≤2·10⁻¹⁰τ`, uniformly over allowed rings (`T/SGAP0.md:150–152`: “`E_σ≥E_0+7τ`”).

- **SGAP0 supplies stronger intermediate bounds.** Its sector-complement gap is at least `3.3τ` for `|ε|≤τ/120000`, and at least `7τ` for `|ε|≤10⁻⁸τ` (`T/SGAP0.md:13,98–102`: “for every light number”). Its parity-pattern comparison gives “`e_p−e_{p_alt}≥|NW(p)| ε²/(6τ)`” (`T/SGAP0.md:124`). Thus the alternating patterns minimize energy in its stated range (`T/SGAP0.md:126`: “`e_{p_alt}=min_p e_p`”).

- **The zero-hop proof contains reusable cancellation machinery.** It rebuilds finite Dobrushin induction: “no published theorem is imported” (`T/SGAP0.md:78`). Its comparison “cancels activities away from non-wall bonds before estimating errors” (`T/SGAP0.md:162`). Its scope excludes the moving-bath conclusion: “do not prove the corresponding nonzero-hopping results” (same line).

- **An exact configuration-conserving benchmark already has moving light levels beside a charged gap.** Under `δ<7τ`, charged levels cost at least `14τ−2δ`. Below that threshold the spectrum is “exactly the free half-filled light spectrum” (`T/SMG15.md:66`). Its hypothesis is that `H_A` “preserves every configuration” (`T/SMG15.md:62`). It therefore does not establish stability under the off-diagonal mixing above.

- **Circuit dressing preserves spectra in a special family.** Theorem 6 gives sector spectra “exactly that of `H_A`” (`T/SMG15.md:114`). The source calls this “a fine-tuned example” (`T/SMG15.md:130`). Its dressed Hamiltonian is “not the R-GEN generator” of a certified NN-a decomposition (`T/SMG15.md:122`).

- **The induced light interaction is known at second order.** The atomic identity gives resolvent coefficient “`2/(7τ)`” (`T/SMG15.md:138`). For SGAP’s hopping factor, the formal correction contains repulsive density coefficient “`4ε²/(7τ)`” (`T/SMG15.md:140`). Higher orders and hopping corrections are “not bounded here”; the identity does not yield “volume-uniform decoupling” (`T/SMG15.md:144`).

- **A neutral low-energy state is available independently of the charged-gap proof.** The twist theorem gives an orthogonal state in the ground state’s own symmetry sector with “`⟨Φ,HΦ⟩≤E₀+C_h/L`” (`T/SMG15.md:98`). It supplies only “a second low state” and proves neither S1 nor uniqueness (`T/SMG15.md:108`).

- **Earlier Cayley-chain evidence is finite.** Logged #10078 records the same atomic spectrum and eight-Majorana proxy-chain diagnostics. Its exclusions include “gauge fields, L > 8” and the slab’s light wall (`C:2341`). Consolidation status is “author statements for review” (`C:11`).

- **A different model has an explicit vacuum-centered sector comparison.** The finite-PW SU(3) result proves a distance-dependent static-source lower bound uniform in cutoff and volume (`F:51`: “`E_xy,R-E_0,R >= (4/a)(1-kappa)d`”). It centers the calculation on its “OWN vacuum energy” (`F:27`). It retains an imported coordinate estimate and requires a “unique vacuum and gap at least1” (`F:57–61`). Source status is conditional-support (`F:17`); ledger status is `"effective_status": "unaudited"` (`L/ga/gauge_wilson_finite_pw_uniform_static_source_energy_bounds_bounded_theorem_note_2026-09-07.json:32`).

- **Existing fermionic polymer control has a massive scope.** The retained-Grassmann note proves an all-degree connected norm in an “explicit high-mass” region (`K:11–13`). Its ledger is unaudited (`L/wi/wilson_staggered_retained_grassmann_two_layer_kp_polymer_norm_bounded_theorem_note_2026-07-12.json:30`: `"effective_status": "unaudited"`). The repaired KMS note proves “only scalar ODE consequences” (`Q:14`); its ledger is also unaudited (`L/km/kms_fermionic_brydges_majorant_external_narrow_theorem_note_2026-05-11.json:27`).

**Failed attempts on file.**

- **Local Schrieffer–Wolff:** summing local remainder norms gives a bound “growing with `L`.” Weyl’s inequality then supplies no uniform sector gap (`T/SMG15.md:158`). A different Spin(10) Feshbach calculation has the same limitation: “the bound retains v’s volume dependence” (`B:235`). That note is conditional-support (`B:7`) and unaudited (`L/sp/spin10_symmetric_atomic_gaps_mirror_boundary_projection_and_current_response_bounded_theorem_note_2026-09-14.json:27`).

- **Absolute light-linked polymers:** a possible nonzero `|z|⁻²` contribution has an absolute space-time sum that “diverges logarithmically.” Complete weights and cancellations were not calculated; the failure does not exclude every polymer criterion (`T/SMG15.md:159`: “does not … exclude cancellations”).

- **Direct Fröhlich–Pizzo application:** the unsplit light mode leaves a “two-dimensional” on-site kernel. Adding the proposed penalty instead produces an “empty, rather than half-filled” reference chain (`T/SMG15.md:160`). The available open-segment theorem remains conditional and “cited, not rebuilt” (`T/SMG1.md:122`).

- **A4, summed charge removal:** the missing estimate is “`W_odd≤Kw` uniformly in `L` and `ε`.” Its bound counts odd fluctuations far from the selected charge (`T/SGAP.md:141`). Proposition 5.1 gives some parameters with “`W_odd≥Lε²/(200704τ²)`” (`T/SGAP.md:127`). The source explicitly says this “does not disprove that bound” (`T/SGAP.md:141`).

- **A5, unrestricted local windows:** the desired strict increase is false because “`λ_min(K+B)=λ_min(K)` exactly.” The failure holds for every `t`; it does not refute S-GAP (`T/SGAP.md:147`).

- **A6, per-parity half-filled comparison:** at `t=ε=0`, a specified parity block has equal neutral and charged minima of `28τ`, while the global ground energy is zero (`T/SGAP.md:74`: “both … minimum equal `28τ`”). SGAP0 later resolves the zero-hop problem through comparison across patterns, “rather than using its false per-sector half-filled claim” (`T/SGAP0.md:162`).

- **All-order cancellation from circuit equivalence:** projection onto the original mirror ground space need not commute with dressing. The corrected result is cancellation “through order `ε³`”; higher orders remain unsettled (`T/SMG15.md:130`).

- **Gaussian replacement of the interacting atom:** its four-point function “cannot follow by applying Wick’s rule” (`B:272`). A separate bare comparator produces a “nonzero attractive density interaction,” whose coefficient is “not imported unchanged” into the refined atom (`B:293,297`).

- **Earlier selective-gapping models:** #9992 “releases every light mode the mirror was pairing” (`C:519`). #10060’s far-wall branch “moves one layer in” (`C:1491`). #10004’s infinite-volume K-gap persistence is “not established: inconclusive” (`C:721`). These retain the consolidation’s author-review status (`C:11`).

- **SGAP0 bookkeeping, repaired:** the draft incorrectly excluded singleton contractible polymers. The correction records that their activities vanish and removes them from the gas (`T/SGAP0.md:58`: “Removing the zero-activity singletons leaves every partition function unchanged”).

**Overlap with this lane's results.**

not run

**Missed inputs.**

- **Use the latest amendment before reopening zero hopping.** `T/SGAP.md:5` says “S-GAP⁰ proved.” It supersedes the body’s older “S-GAP⁰ (OPEN)” at line 139. This changes the starting point from an unresolved zero-hop gap to the frozen SGAP0 theorem.

- **Transfer cancellation, not separate extensive energy estimates.** SGAP0 cancels unaffected activities (`T/SGAP0.md:162`: “before estimating errors”). The tree’s proposed moving-bath step is to retain “fermionic determinants” while cancelling neutral histories (`T/SMG1_TREE.md:797`). This identifies the additional estimate needed beyond the zero-hop proof.

- **Use the sector-preserving coordinate comparator as a method input.** The SU(3) calculation is centered on its “OWN vacuum energy” (`F:27`). It would guide a defect-relative comparison. Its unique-vacuum hypothesis remains a separate obstacle to transfer (`F:57`: “unique vacuum and gap at least1”).

- **Keep the induced interaction in the light theory.** The repulsive coefficient is already “`4ε²/(7τ)`” (`T/SMG15.md:140`). A weak-interaction treatment must control its higher kernels. It would prove a narrower result if it replaced the target square by a wedge: the tree says “Do not replace the full square” without naming the weaker theorem (`T/SMG1_TREE.md:1202`).

- **Do not treat the repaired KMS row as the missing fermionic estimate.** Future use must separately supply “the BBF/Polchinski inequality, its hypotheses, and the framework-substrate identification” (`Q:89–90`). This changes what remains load-bearing in a proposed RG argument.

- **Keep finite-ring, GNS, and tick conclusions separate.** SGAP0 says “Infinite-volume, GNS and tick statements are not established” (`T/SGAP0.md:164`). The adopted owner reading says “Tick stationarity remains a separate requirement” (`T/TOE_ASSEMBLY.md:261`). A successful ring theorem would still need these bridges.

**Consumers.**

| Consumer | Weakest statement needed |
|---|---|
| **SMG15 / R15-SPEC S1** | A uniform lower bound for every globally charged eigenvalue above the full canonical ground energy. S1 asks exactly for “every globally `S`-charged eigenvalue” (`T/SMG15.md:26`). Uniqueness is separate (`T/SMG15.md:154`: “A unique ground state is a separate question”). |
| **SMG15 twist corollary** | S1 plus separately established uniqueness. Under “S1 and S3,” the trivial-sector gap is at most `C_h/L` (`T/SMG15.md:104`). |
| **R1.5-D / tree node D** | A positive charged gap in the same coupled model and parameter wedge used for its effective light theory. D requires “a positive charged mirror gap in the same model” (`T/SMG1_TREE.md:821`). S-GAP alone does not supply its infrared correlations (`T/SMG15.md:162`: “controlled elimination … a `c=1` Luttinger scaling limit”). |
| **R2 and R3** | A transferable charged-cluster estimate, with each new carrier and dimension checked separately. R2 still needs “Mirror decoupling and a matching finite-register carrier” (`T/SMG1.md:135`). R3 proposes extending the estimate to “two spatial dimensions” (`T/SMG1_TREE.md:939`). |
| **W2 / CH1** | Eventually a selective mirror estimate for one three-dimensional construction with the required Weyl field. The immediate rung is “S with `tε≠0`, followed by D” (`T/SMG1_TREE.md:183`). The tree requires the final mirror estimates “uniformly in volume” (`T/SMG1_TREE.md:965`). |
| **YM branch** | No direct SGAPT consumer found. T0 is “pure gauge”; adding CH1’s chiral fermions is “outside T0’s statement” (`T/TOE_ASSEMBLY.md:637`). The YM tree explicitly says “No mass gap is requested or inferred” for its nontriviality witness (`ref/ym/.claude/science/physics-loops/ym4d-hard-route-20261030/library/t0-tree.md:252`). |