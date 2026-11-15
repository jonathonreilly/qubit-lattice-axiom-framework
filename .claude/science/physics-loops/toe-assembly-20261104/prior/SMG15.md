**Searches run.**

- Read `ref/README.md` first. It identifies “Ledger rows: main/docs/audit/data/ledger/” (line 2), consolidation notes (line 3), and the YM corpus (line 5).
- Initial terms: `SMG15`, `symmetric mass generation`, `Fidkowski`, `mirror gapping`, `Spin(10)`.
- Follow-up terms: `R1.5`, `Luttinger`, `gapless sector`, `Schrieffer`, `light.mirror`, `Lieb.Schultz`, `gapless remainder`, `half.fill`. Followed claim identifiers and consumer references.
- Searched `ref/main/docs`, `ref/pr*/`, `ref/ym/`, and the TOE folder, including parts, outlines, drafts, referee reports, prior digests and `LIT_SMG.md`. Used only the permitted commands. No edits, git commands, internet searches or proof checks.
- `briefs/SMG15.txt` was absent. Refreshed the SMG1, CH1 and CG16S status blocks after concurrent freeze amendments appeared.

Path abbreviations:

| Label | Repository path |
|---|---|
| `T/` | `repo/.claude/science/physics-loops/toe-assembly-20261104/` |
| `M/` | `ref/main/docs/` |
| `C` | `ref/pr10131/docs/CHIRALITY_DOUBLERS_CONSOLIDATED_BOUNDED_THEOREM_NOTE_2026-10-30.md` |
| `S` | `ref/main/docs/SPIN10_SYMMETRIC_ATOMIC_GAPS_MIRROR_BOUNDARY_PROJECTION_AND_CURRENT_RESPONSE_BOUNDED_THEOREM_NOTE_2026-09-14.md` |
| `H` | `ref/main/docs/ADMISSIBILITY_RULE_THE_HARD_CORE_SEA_ON_A_RING_IS_ONE_TWISTED_BAND_HALF_FILLED_WITH_HALF_THE_FREE_SEAS_VOLUME_TERM_AND_CLOCK_STIFFNESS_BOUNDED_THEOREM_NOTE_2026-09-24.md` |

**Already in the repo.**

- **The SMG15 target remains open.** R1.5-D keeps the eight-Majorana mirror beside a half-filled fifth-mode chain. It asks for a “`c=1` Luttinger scaling limit” and exclusion of extra light fields. Mirror elimination with a gapless sector and control of induced couplings remain open (`T/SMG1.md:132`: “controlling the induced couplings are open”). The outline labels it “[O]” (`T/SMG1_OUTLINE.md:184`).

- **Rung 1 supplies the mirror atom and a gapped reference model.** The atom has a unique symmetric ground vector and spectrum −14, 0, 2 (`T/SMG1.md:51`: “`S`-fixed and even”). At zero hopping, the product ground state has a generator gap in finite and infinite volume (`T/SMG1.md:75`: “gap at least `Δ₀`”). Its fifth mode is empty, explicitly “`|0⟩_{5,x}`” (same line). SMG1 is now frozen, rather than independently audited (`T/SMG1.md:3`: “FROZEN 2026-11-07”; line 5: “not an audit verdict”).

- **The hopping stability input is conditional and narrower than SMG15.** Theorem 5.2 gives a uniform open-segment gap for sufficiently small mirror hopping (`T/SMG1.md:116`: “uniformly in length”). Its source theorem is “cited, not rebuilt”; native stability, rings and the infinite chain remain R1-H (`T/SMG1.md:120`). That line also states: “No stationarity for `U` at nonzero `θ` follows.”

- **The symmetry classification of mixing is already available.** Lemma M decomposes invariant local operators into mirror, light and link factors. Genuine mixing “has degree at least 4”; degree four requires a same-flavour mirror pair and a number-conserving light pair (`T/SMG1.md:137`). Higher terms are allowed: “`W_x n_{x,5}` has degree six” (`T/SMG1_REFEREE.md:249`). This is a referee closure; it establishes no Luttinger limit (`T/SMG1.md:132`: “No Luttinger limit follows from symmetry alone”).

- **Translation is an essential separate hypothesis.** Under global `S` and one-site translation, the specified quadratic mirror symbols vanish at “`k=0,π`” (`T/SMG1.md:61`). Symmetry alone allows same-flavour intersite bilinears. An invariant dimerized hop gaps a flavour (`T/SMG1.md:65`: “One-site translation is essential”).

- **The Cayley-chain precursor is logged finite evidence.** #10078 already reports the eight-Majorana atomic spectrum and proxy-chain diagnostics through eight sites. Its exclusions include “the slab with bulk and light wall, gauge fields, L > 8” (`C:2341`, status “logged”). The consolidation identifies its statements as “author statements for review” (`C:11`).

- **Main already contains mirror-elimination calculations.** The supplied Spin(10) atom gives exact second-order cancellation: “the induced term is a constant” (`S:256`). A separate bare-projector comparator generates a fourth-order “nonzero attractive density interaction” (`S:293`). Its coefficient is explicitly not transferred to the refined atom (`S:32`: “not imported into the refined atom”). Source status is “conditional-support” (`S:7`); ledger status is `"effective_status": "unaudited"` (`M/audit/data/ledger/sp/spin10_symmetric_atomic_gaps_mirror_boundary_projection_and_current_response_bounded_theorem_note_2026-09-14.json:27`).

- **The 3450 notes contain useful interaction algebra, with different content.** Logged #10058 gives a neutral lattice that “is K-null (a gapping lattice)” (`C:2334`). Kept #10060 supplies a unique three-site atom and cited hopping stability “for the vector-like content only” (`C:1693`). Its bosonization calculation makes both interactions relevant for “`x > 21/29`” in the specified equal-velocity Luttinger family (`C:1696`). These remain author-side consolidation results (`C:11`).

- **An exact half-filled one-dimensional comparator exists.** The supplied hard-core ring reduces to “one spinless band whose wrap bond carries `R`” (`H:93`). On uniform rings with four dividing their length, its minimum is half filled (`H:120`: “the lowest state over all `N` is half filled”). The source is “bounded-support” and “unaudited” (`H:23`); its ledger also says `"effective_status": "unaudited"` (`M/audit/data/ledger/ad/admissibility_rule_the_hard_core_sea_on_a_ring_is_one_twisted_band_half_filled_with_half_the_free_seas_volume_term_and_clock_stiffness_bounded_theorem_note_2026-09-24.json:31`). Its Luttinger reference is a “Comparator[], named only” (`H:62–64`).

- **Existing endpoint restrictions have explicit scope.** CH1’s K1 gives compensating pocket charge under its periodic-projector and charge-preservation hypotheses (`T/CH1.md:80`: “sum to zero in each block”). It applies “only at a quasi-free endpoint” (`T/CH1.md:84`). CG16S’s free-walk pairing leaves open “gates violating E” and “a filled or entangled background” (`T/CG16S.md:140`). CG16S is frozen conditional mathematics on proposed registers (`T/CG16S.md:5`: “It adopts no law, reading or axiom”).

**Failed attempts on file.**

- **Tetrahedral FK selection, logged #9909.** The mirror map fixes the interaction. The failing step is selectivity: “it gaps both light copies and cannot select one” (`C:2315`).

- **Copy-selective mirror freezing, kept #9911.** Exact protection of selected light zeros does not remove the other light nodes. The supplied one-dimensional chain also releases the partner at π (`C:301`: “A 1+1D chain shows the same release at p = pi”).

- **Block-local quartic, kept #9992.** Finite SU(4) diagnostics find a symmetric mirror gap, but it “releases every light mode the mirror was pairing” (`C:519`). The recorded scope is “L <= 6” and “The toy is not Spin(10)” (same line).

- **Strongly gapped far-wall cells, kept #10060.** The mirror survives outside the frozen layer: “moves one layer in” (`C:1491`). Main records the same boundary limit: an “atomic gap on a complete layer does not remove the topological interface” (`S:201`).

- **3450 finite-size persistence.** The larger-size follow-up weakens #10058. The persistence ratio is 0.358, and “persistence is not established” (`C:2255`). The eight-Majorana proxy does not settle the wall problem: “neither result concerns the bulk or the light wall” (same line).

- **Anomaly-compatible filtered 16-Weyl toy, kept #10004.** The thermodynamic mirror gap remains inconclusive: “Survival of the K gap as L -> infinity is not established” (`C:721`).

- **Atomic elimination as thermodynamic control.** The Feshbach bound retains hopping-norm volume dependence (`S:235`: “the bound retains v’s volume dependence”). The source explicitly says: “not a volume-uniform expansion” (`S:239`).

- **Gaussian replacement of the mirror.** The atom’s higher correlations obstruct reconstruction from its two-point function: the four-point function “cannot follow by applying Wick’s rule” (`S:272`).

**Overlap with this lane's results.**

not run

**Missed inputs.**

- **Start from Lemma M’s complete interaction class.** It would replace the outline’s leading-term shorthand with all allowed higher mixing terms. The referee explicitly directs the “R1.5 lane” to “Start from Lemma M’s form” (`T/SMG1_REFEREE.md:368`).

- **Use the existing induced-interaction calculation.** It would require retaining higher mirror cumulants after any second-order cancellation. Main already finds a “nonzero attractive density interaction” (`S:293`), while limiting that coefficient to its bare comparator (`S:32`: “not imported into the refined atom”).

- **Keep the stability and RG dependencies separate.** The assigned block diagonalization must work “relative to a gapless remainder”; the existing stability theorem “needs a global gap” (`T/SMG1_OUTLINE.md:182`). The proposed Luttinger technology was read only at “abstract” level (`T/SMG1_OUTLINE.md:103`, L34). Its full hypotheses and applicability remain work, as the assignment says: “after its theorems are read in full” (`T/SMG1_OUTLINE.md:182`).

- **Specify charged correlations before taking the light limit.** The outline already identifies the fifth-mode fermion as requiring “`Z_ℓ`-string dressing” on the parity-gauged carrier (`T/SMG1_OUTLINE.md:226`). The related frozen charged-field analysis reports “zero undressed two-point function at all times” under its stated gauge-law hypotheses (`T/CH1_5UQ.md:9`). This changes the observable or sector in which SMG15 must formulate its limit.

- **Repair the inherited exclusion criterion.** The existing rescaling criterion has an inconsistent universal reading and a vacuous existential reading (`T/SMG1.md:31`: “The existential reading … is vacuous”). The same line warns that π content can be “invisible rather than excluded.” SMG15 needs an explicit criterion for extra light fields.

- **Separate generator gaps from tick dynamics.** The assigned R-GEN ground state “does not imply stationarity under the tick” (`T/SMG1.md:21`). Lemma F has now had one check (`T/SMG1_LEMF_CHECK.md:29`: “VERDICT: Lemma F holds”). Its stated limitation matters: it “does not prove that 1 is non-isolated” (`T/SMG1_LEMF_CHECK.md:23`). This changes which gap and stationarity statements can be passed downstream.

**Consumers.**

| Consumer | Weakest useful statement |
|---|---|
| **SMG1 R2** | Controlled elimination of a gapped mirror beside a gapless sector, with its induced light interactions bounded. R2 explicitly “Imports … R1.5 (decoupling)” (`T/SMG1_OUTLINE.md:190`). Its chiral extension remains new work (`T/SMG1_OUTLINE.md:192`: “decoupling … with a chiral light sector”). |
| **SMG1 R3-D** | A precise one-dimensional decoupling theorem whose assumptions can be reconsidered in two dimensions. R3 imports “R1, R1.5” (`T/SMG1_OUTLINE.md:200`); the outline warns that “The 1D tools … do not apply” there (`T/SMG1_OUTLINE.md:236`). |
| **W2 / R4** | A reusable decoupling method with a defined light-field test. W2 imports “R3 (stability and decoupling in higher dimension)” (`T/SMG1_OUTLINE.md:210`). Its final assembly target remains “one Weyl 16 … with every mirror and doubler gapped” (`T/TOE_ASSEMBLY.md:718`). |
| **CH1-i** | Ultimately, selective mirror removal “without releasing light partners,” with “no extra light charged state” (`T/TOE_ASSEMBLY.md:447`). SMG15 supplies a lower-dimensional method toward that contract; CH1 already names the hardest step as “keeping a light sector gapless while its mirror is gapped” (`T/CH1.md:24`). |
| **GA2 matter bridge Y4; YM branch** | No direct SMG15 consumer found in the searched YM files. The explicit TOE interface requires the later chiral-matter extension: “T0 is pure gauge” and CH1’s matter RG lies “outside T0’s statement” (`T/TOE_ASSEMBLY.md:606`). |