**Searches run.**

- Read `ref/README.md` first. It identifies “Ledger rows: main/docs/audit/data/ledger/” (`ref/README.md:2`).
- Searched `ref/main/docs`, `ref/pr*/`, `ref/ym/`, and `repo/.claude/science/physics-loops/toe-assembly-20261104`. Included other parts, drafts, referee reports, prior digests, trees and `LIT_*.md`.
- Initial terms: `KINVE1`, `kinetic`, `inverse vielbein`, `kinematical`. Follow-ups: `KINV`, `K-INV-E`, `invariant-algebra`, `character filler`, `good-path`, `even refinement`, `Bratteli`, `ordered K`, `dimension group`, `AF algebra`, `multiplicity matrix`, `commuting square`, `boundary representation`, `boundary-crossing finite embedding`, `two adjacent chain cells`, `invariant recoupling`.
- No KINVE1 draft or brief was found. No KINVE1 entry was found in `TOE_ASSEMBLY.md`. The available E1 brief requests an “explicit unital injective map” at `m=m₁=2`, `L=2`, on “two adjacent chain cells,” with endpoint gauge actions, dilated translations, multiplicities and matrix units (`T/ZM1_TREE.md:930`). This digest uses that target.
- Path abbreviations: `T` = `repo/.claude/science/physics-loops/toe-assembly-20261104`; `M` = `ref/main/docs`; `G` = `ref/pr10126/docs/GAUGE_MATTER_REGISTERS_CONSOLIDATED_BOUNDED_THEOREM_NOTE_2026-10-30.md`; `Y` = `ref/ym/.claude/science/physics-loops/ym4d-hard-route-20261030/library`.

**Already in the repo.**

- **E1 is an open finite-patch target.** The tree requires an embedding across two adjacent coarse cells, with patch-stabilizer covariance (`T/ZM1_TREE.md:268`, “**Status: OPEN.**”; `:270`, “two adjacent coarse cells”). It requires explicit matrix units and symmetry intertwiners; “The integer conditions alone are insufficient” (`:284`). The tree itself is an unchecked sketch: “no node below is proved by this file” (`:1`).

- **The governing map definition is invariant-only.** The owner requires a “unital injective *-homomorphism,” cell covariance and exponential locality. It imposes “no map on charged fields or Gauss generators” (`T/TOE_ASSEMBLY.md:252`). Thus a full-algebra charge extension is additional structure.

- **Finite invariant algebras recover the quasi-local invariant algebra.** GB1Z2L5 Theorem 1 proves local invariant density and support-preserving averaging: “The union of A^G(R) is norm dense” (`T/GB1Z2L5.md:33`). Its status is frozen conditional mathematics, with “no retained or audit status” (`:5`).

- **Characters coexist with noncommutative corners.** Every named U-register invariant algebra and the O invariant algebra has a character (`T/GB1Z2L5.md:37`, “Each named-law invariant algebra has a character”). Nevertheless every U register admits a corner containing M₂: “a non-unital embedding of M₂” (`:89`). This is not an abelian-algebra classification. Status: frozen, without retained or audit status (`:5`).

- **Even-register character constraints are already proved.** KINV Theorem 3 forces every locked fine character to assign value one to the image of the balanced coarse-link projection (`T/KINV.md:45`, “`χ₀(Φ([p_{ℓ,X}=m₁/2]))=1`”). Theorem 7 supplies central site-freezing projections, with neighboring freezing projections incompatible: “`Π_XΠ_Y=0`” (`:95`). These are frozen results (`:5`, “FROZEN 2026-11-08”). They construct no faithful defect realization (`:99`, “No compatible fine defect pattern or faithful realization is constructed”).

- **Incompatible projections constrain placement.** ZM1INV R6 proves that approximation errors on disjoint fine regions satisfy “`δ₁+δ₂≥1/2`” (`T/ZM1INV.md:144`). It applies to injective invariant-algebra maps. It does not establish literal common support for exponential tails (`:146`, “does not establish literal common support”). ZM1INV is frozen author-side mathematics; its closures are “unrefereed” (`:5`).

- **A good-path building block exists, at a different register.** ZM1INV Theorem 3.4 works at `m=m₁=1`. Its interior-gauge commutant is the “full coarse link algebra on the first factor” (`T/ZM1INV.md:120`). It supplies neither the E1 register-2 construction nor a global extension: “Compatibility across local supports and defect sectors remains to be constructed” (`:126`). Status: frozen, with the qualifications above (`:5`).

- **Exact regrouping works with enlarged content.** ZM1 Z0 gives an exact regrouping of the base laws, preserving fine gauge transformations. Its content grows like “`exp(c L^3)`” (`T/ZM1.md:103`). This does not supply fixed five-mode R-form content. Status: the proofs are “not independent audit status” (`:18`).

- **A finite-group chain refinement supplies a geometric analogue.** RC-6 constructs a linkwise refinement that is “unital, injective, of finite range and translation covariant” (`T/ZM1I1A.md:134`). It has endpoint and midpoint gauge covariance but fails exact generator identification. Its scope is “a one-dimensional pure-gauge analogue” (`:144`). Status: a referee closure within a frozen author-side note (`:3`).

- **Coherent even refinement exists in a free chain.** The dyadic note constructs a “unital injective isometric *-map” and exact composition (`M/DYADIC_EVEN_REFINEMENT_BOUNDED_THEOREM_NOTE_2026-10-12.md:142,150`). Physical interval support is preserved (`:155`, “no physical interval enlargement occurs”). It asserts no “interacting or higher-dimensional theorem” (`:793`). Ledger: `"effective_status": "unaudited"` (`M/audit/data/ledger/dy/dyadic_even_refinement_bounded_theorem_note_2026-10-12.json:33`).

- **A gauge-register toy supplies a covariant isometry.** Consolidated #9928 records a level-matched polar map that is “gauge-, winding- and translation-covariant” (`G:295`). Its scope is “an isometry in a 2+1D Z_3 toy”; no register continuum limit is computed (`G:287`). Status: “author statements for review” (`G:11`). An isometry alone gives unit `VV*`, rather than the required global unit (`T/KINV.md:105`, “with unit `VV*`”).

- **Boundary sectors must remain present.** The finite-region Peter–Weyl approximation preserves “boundary representation sectors” and “does not project onto a boundary singlet” (`M/GAUGE_WILSON_LOCAL_OBSERVABLE_FINITE_REGION_PW_APPROXIMATION_BOUNDED_THEOREM_NOTE_2026-09-07.md:83`). It is a conditional approximation result, “not a free deterministic encoder” (`:73`). Ledger: `"effective_status": "unaudited"` (`M/audit/data/ledger/ga/gauge_wilson_local_observable_finite_region_pw_approximation_bounded_theorem_note_2026-09-07.json:30`).

**Failed attempts on file.**

- **Constant-character construction.** It meets covariance, locality and unital multiplicativity, “but not injective” (`T/KINV.md:53`). A nonzero complementary end-number projection lies in its kernel (`:55`, “is in the kernel”). This leaves the even-register question open.

- **Neutral full-matrix replacement.** Composing with a fine character would give a character of the matrix source. ZM1INV R5 therefore excludes characterless sources (`T/ZM1INV.md:98`, “no unital `*`-homomorphism”). This is not an obstruction to a source invariant algebra having its own characters (`:100`, “R5 gives no obstruction to K-INV”).

- **Representative-end path decimation.** Incompatible coarse end projections multiply to zero, while prescribed images on different fine links have nonzero product. The failing step is multiplicativity: “A homomorphism preserves products” (`T/ZM1INV.md:130`). The broader full-link end-equivariant route is also excluded under its specified endpoint actions (`:104`, “no unital link-algebra homomorphism”).

- **Good sector extended by zero or a character filler.** Zero extension “is not unital”; an infinite product of good-sector projections “is not a quasi-local projection” (`T/ZM1INV.md:126`). KINV additionally excludes a character filler on any nonzero invariant defect projection (`T/KINV.md:63`, “no character `χ` satisfies”). This does not exclude every defect mechanism (`:79`, “not all extensions”).

- **Charge-equivariant full-algebra decimation.** KINV Theorem 6 forces representative neighbors to remain fine neighbors, hence “no class J map exists for `L≥2`” (`T/KINV.md:83`). Its scope requires the full-algebra extension; it does not exclude invariant-only maps (`:91`, “without a full-algebra charge-equivariant extension”).

- **Draft commutation shortcut.** The draft asserted commutation of stars at distinct sites, although adjacent stars share a link. The frozen repair restricts the argument to “nonadjacent representatives, whose stars are disjoint” (`T/KINV.md:9`). This is a recorded repaired step, not a new assessment here.

- **Old exact Gauss-generator embedding.** The trace/adjacency route forces “`L=1`” under the old G1 and locality conditions (`T/ZM1I1A.md:44`). Those conditions were replaced; “Neither full-algebra obstruction … applies directly” to the owner’s invariant-only map (`T/TOE_ASSEMBLY.md:254`).

- **Refinement that matches only selected interfaces.** Fixed Haar refinement has an “exact scalar counterexample” to state compatibility and flows that “cannot intertwine for all t” (`M/DYADIC_EVEN_REFINEMENT_BOUNDED_THEOREM_NOTE_2026-10-12.md:553,577`). State-adapted refinement retains infinite support and “failure of exact energy-flow intertwining” (`M/STATE_ADAPTED_REFINEMENT_BOUNDED_THEOREM_NOTE_2026-10-12.md:46,48`). Energy-adapted refinement loses exponential coefficient decay and exact spatial translation intertwining (`M/ENERGY_ADAPTED_REFINEMENT_BOUNDED_THEOREM_NOTE_2026-10-12.md:320,336`, “rules out exponential”; “translations fail exact intertwining”). Both adapted-refinement ledger rows remain `"unaudited"` (`M/audit/data/ledger/st/state_adapted_refinement_bounded_theorem_note_2026-10-12.json:34`; `M/audit/data/ledger/en/energy_adapted_refinement_bounded_theorem_note_2026-10-12.json:34`).

- **Vacuum-only gauge isometry.** The nearest vacuum-carrying map sends excited levels outside the desired child window. “Carrying the vacuum is not enough” (`G:311`). Level matching repairs that finite toy interface, not E1.

**Overlap with this lane's results.**

not run

**Missed inputs.**

- **Use the complete finite commutants.** Local invariant density supplies the finite-region system (`T/GB1Z2L5.md:33`, “norm dense”). The E1 specification requires every target sector and explicit intertwiners (`T/ZM1_TREE.md:284,286`, “matrix units and symmetry intertwiners”; “No target sector may be discarded”). This changes a dimension-counting attempt into an explicit representation-and-inclusion problem.

- **Keep endpoint gauge actions and boundary sectors.** The E1 brief says “Include every endpoint gauge action” (`T/ZM1_TREE.md:930`). The Peter–Weyl result explains why singlet-only truncation loses valid physical states: it would discard one “with probability1” (`M/GAUGE_WILSON_LOCAL_OBSERVABLE_FINITE_REGION_PW_APPROXIMATION_BOUNDED_THEOREM_NOTE_2026-09-07.md:81`).

- **Separate centrality in the source from centrality in the target.** The tree states that a coarse central projection “need only commute with the image” (`T/ZM1_TREE.md:286`). Requiring global fine centrality would add a condition absent from E1.

- **Use path recoupling with its exact unresolved interface.** The good-path algebra is available, but compatibility with all defect sectors is not (`T/ZM1INV.md:126`, “remains to be constructed”). A register-2 recoupling must supply that missing action; the character-filler shortcut is already excluded for a global local embedding (`T/KINV.md:79`, “fails at Theorem 5”).

- **Treat AF and perturbation programmes as unverified leads.** The tree labels both L-AF and L-PERT “FROM MEMORY” (`T/ZM1_TREE.md:222,223`). KINV records “no classification or embedding test is verified here” (`T/KINV.md:101`). They provide no checked replacement for matrix units, prescribed symmetry or support estimates.

- **Keep finite-patch failure bounded.** The authorized outcomes include a proof, a bounded counterexample or a named compatibility lemma. “A failed collar does not refute unrestricted K-INV-E” (`T/ZM1_TREE.md:934`).

**Consumers.**

- **E2.** It needs explicit E1 embeddings whose restrictions can be compared on overlaps. Its first deliverable is to “extend an E1 construction across two overlapping plaquettes” and prove intersection agreement (`T/ZM1_TREE.md:938`). A multiplicity table alone is insufficient (`:284`, “integer conditions alone are insufficient”).

- **K-INV-E.** It needs compatible extensions with translation-uniform locality and injectivity. E2 must arrange “compatibility on every fixed local algebra” (`T/ZM1_TREE.md:316`) and remain “isometric on every local algebra” (`:324`). E1 alone supplies finite construction data.

- **Locked-state ZM1-I1[INV].** Its weakest sufficient handoff is a complete K-INV map for an allowed even coarse register. In the locked vacua the target “holds exactly when K-INV holds” (`T/ZM1INV.md:72`); character pairs make “both truncated functions vanish” (`:52`). This does not select the physical vacuum (`T/KINV.md:20`, “not a selected VC1 vacuum”).

- **Non-character ZM1, LZ1 and GA2.** They additionally need the actual state/update comparison and observable dictionary. “Class (a) alone does not establish a common speed” (`T/ZM1INV.md:179`). ZM1-G needs a controlled gauge-invariant correlator comparison “with quantified errors” (`T/GA2_Y2.md:178`).

- **YM H-BLOCK.** It needs a countable block-observable family whose convergent expectations supply a joint limiting state. This remains “a named input, not a consequence of curvature cumulant bounds” (`Y/port/p8b-limits.md:57`). Its registry row is “open” (`Y/open-registry.md:228`). A finite E1 map does not supply that limit.

- **R-CS, MT1-S and CG1’s charged 16.** They require a separate charged-sector bridge. The owner states that they “get no zoom from this map” (`T/TOE_ASSEMBLY.md:255`).