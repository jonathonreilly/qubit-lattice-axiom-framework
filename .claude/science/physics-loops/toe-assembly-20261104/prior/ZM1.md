## **Searches run.**

- Read `ref/README.md` first. It identifies `main/docs/`, the consolidation PRs and `ym/`; each consolidation PR has a “*CONSOLIDATED* note.” (`ref/README.md:2–5`.)
- Searched `ref/main/docs`, `ref/pr*/`, `ref/ym/` and `repo/.claude/science/physics-loops/toe-assembly-20261104/`. Terms: `zoom`, `block map`, `coarse-grain`, `renormali`, `folded.mode`, `Balaban`, `wavelet`, `multiresolution`, `finite register`, `monodromy`, `tent kernel`, `transported averages`, `straight-link blocking`. Also searched the TOE `LIT_*.md` files for `block`, `zoom` and `renorm`.
- Used only the permitted file commands. No internet, git or edits.

Path abbreviations below:

- `TOE/` = `repo/.claude/science/physics-loops/toe-assembly-20261104/`.
- `YM/` = `ref/ym/.claude/science/physics-loops/ym4d-hard-route-20261030/`.
- `LOR` = `ref/pr10125/docs/LORENTZ_DISPERSION_CONSOLIDATED_BOUNDED_THEOREM_NOTE_2026-10-30.md`.
- `D4` = `ref/pr10130/docs/D4_ROUTE_CONSOLIDATED_BOUNDED_THEOREM_NOTE_2026-10-30.md`.
- `GAUGE` = `ref/pr10126/docs/GAUGE_MATTER_REGISTERS_CONSOLIDATED_BOUNDED_THEOREM_NOTE_2026-10-30.md`.
- `CHIRAL` = `ref/pr10131/docs/CHIRALITY_DOUBLERS_CONSOLIDATED_BOUNDED_THEOREM_NOTE_2026-10-30.md`.
- `MAIN/` = `ref/main/docs/`.

## **Already in the repo.**

- **Target and present standing.** ZM1 requires spatial correlation errors with explicit `p >= 2`, a controlled trajectory including interacting gauge fields, and compatible site content. The target says “every irrelevant term’s dimension and coefficient bounded.” The lane is frozen, but “ZM1-i and ZM1-I1 stay open”; its proofs “are not independent audit status.” (`TOE/TOE_ASSEMBLY.md:273–275`; `TOE/ZM1.md:5,7`.)

- **Finite-band perfection obstruction and pole persistence, #10092.** For analytic finite-band updates, the prior statement excludes an exactly relativistic band on an open momentum set. Positive propagator blocking retains physical poles. These are distinct restrictions on the image-tower target: “Block averaging keeps every physical pole” and “leaves the finest rung’s physical Lorentz violation unchanged.” The consolidation marks the result “Stands as written,” with radiative protection still conditional. (`LOR:434,438,474–489`.)

- **History-level free fixed point, #10092.** The prior construction uses image sums and reports relativistic dispersion, exponential locality and Ginsparg–Wilson diagnostics. Its scope is “complete only for free matter”; compatibility of its “infinite image tower of poles” with site content remains an owner question. This is history-level evidence, rather than a finite-content tick construction. (`LOR:426,434`.)

- **D4 refinement, positivity and background gauging.** The D4 fixed point has real positive poles, but “site positivity needs a one-slice buffer.” Its runners use “four supplied spinor components per event.” Finite-rung event kernels have a coefficient falling as `16^-n`; zooming an already chosen kernel only changes units. Gauged results use prescribed abelian backgrounds, “with no dynamical links and no loops.” These are author statements for review. (`D4:11,19–20,224–229,247`.)

- **Gauge-preserving split and level matching, #9928.** Child Gauss laws sum to the parent when parent face flux equals the four child fluxes. In the supplied `2+1D Z_3` toy, the passing is an isometry. A covariant level-matched polar map also exists. The consolidation explicitly limits this: “Toy sizes; no continuum limit of the register is computed.” (`GAUGE:287,308–313`.)

- **Native inputs on the live laws.** LW1 supplies finite gauge-invariant edge factorization. MT1 supplies the cell Clifford algebra, free cone and field count. ZM1 already quotes these inputs. In particular, MT1 states “20 two-component Weyl fields per cell,” while these contain “neither the SU(5) `10` nor a Spin(10) `16`.” GA2 supplies the finite-link coherence bounds used against c-number dressing. These are scoped assembly results, not independent audits. (`TOE/ZM1.md:32–38`; `TOE/MT1.md:73,96–101,137`; `TOE/GA2_Y2.md:88`.)

- **An actual dyadic algebra tower on a different model.** The supplied one-dimensional massive-chain note constructs parity-even embeddings preserving interval support. Its local inductive algebra “equals the intrinsic norm-Cauchy quotient.” It does not give exact compatibility of finite-scale states or flows. Current ledger status is `"effective_status": "unaudited"`. (`MAIN/DYADIC_EVEN_REFINEMENT_BOUNDED_THEOREM_NOTE_2026-10-12.md:5,49`; `MAIN/audit/data/ledger/dy/dyadic_even_refinement_bounded_theorem_note_2026-10-12.json:33`.)

- **Coarse-action control on supplied Wilson–staggered fibers.** Prior notes obtain uniform hidden-fiber mixing for `alpha(beta,m)<1/2`, an exponentially local raw-action Hessian, and an all-order complex-source/polymer region in a smaller high-mass wedge. The last theorem is “gauge body only”; it does not construct the retained gauge–Grassmann contraction or critical trajectory. All three current ledger rows say `"effective_status": "unaudited"`. (`MAIN/WILSON_STAGGERED_CONSTRAINED_FIBER_DOBRUSHIN_AND_RAW_RG_UNIT_DIRECTIONS_BOUNDED_THEOREM_NOTE_2026-07-12.md:39–56`; `MAIN/WILSON_STAGGERED_RAW_CONSTRAINED_ACTION_HESSIAN_DECAY_BOUNDED_THEOREM_NOTE_2026-07-12.md:60–63`; `MAIN/WILSON_STAGGERED_CONSTRAINED_FIBER_TWO_LAYER_KP_COMPLEX_SOURCE_POLYMER_BOUNDED_THEOREM_NOTE_2026-07-12.md:41–54,67–70`; corresponding ledger files under `MAIN/audit/data/ledger/wi/`: respectively lines `27`, `29`, `29`.)

- **YM block-RG machinery has conditional standing.** The Balaban reconstruction gives a “conditional proof” of critical-orbit, holomorphy and restriction statements. F0 remains a “cited-pending” operator package; pointed-core admission is additional and unproved. The branch status says “Existence is not proved.” Its registry “proves nothing and grants no scientific or audit status.” (`YM/library/a1-balaban.md:14–25`; `YM/FINISH.md:11`; `YM/library/open-registry.md:3`.)

## **Failed attempts on file.**

- **Keeping only low momenta in an exact local quasi-free zoom.** The failing step is explicitly named: “A local subspace invariant under `V^n` can keep only the low-momentum states.” Z1 instead requires equal retained rank across folded momenta. (`TOE/ZM1.md:137`.)

- **Minimal coupling of Z2’s linear block field.** Attack 1 fails at “`Psi_u` is a fermion field.” Z3 and Z3′ exclude its nonzero off-representative coefficients, including norm-convergent tails. (`TOE/ZM1.md:375`.)

- **Transferring the free estimate through coherent links.** Attack 2 fails at “the link operators act as c-numbers.” The coherence bound excludes its stated near-coherent criterion. The file expressly says this “does not rule out every state-dependent approximation.” (`TOE/ZM1.md:377`.)

- **Conserved-projection compression.** Attack 3 encounters boundary Gauss generators involving neighboring tiles. Its broader classification and rank inference remain unproved. It “is not an attack on ZM1-I1 as stated” and gives “No general conclusion on bounded content.” (`TOE/ZM1.md:379–381`.)

- **Extending the packet estimate to arbitrary spatial separation.** The missing step is deriving momentum support from separation: “physical separation `r` alone does not imply that support.” Composition into a tower also remains unshown. (`TOE/ZM1.md:268`.)

- **Using vacuum matching alone for gauge splitting.** The prior polar map sends excited levels outside the desired low-energy window. The note states “Carrying the vacuum is not enough”; level matching is the added construction. (`GAUGE:312–313`.)

- **Finite-range D4 perfection and positivity.** The tested truncations retain “a complex pair at every R = 1..4.” No finite tested rung is pair-free; unbuffered fixed-point site positivity also fails. These are finite diagnostics on the supplied kernel. (`D4:94–100`.)

- **Replacing an RG contraction by a scalar majorant.** The KMS bridge note identifies four failures: the majorant is “not an operator-norm contraction”; small-data admission is unverified; marginal eigenvalues are `O(1)`; and continuous flow is not the required discrete blocking map. Its current ledger status is unaudited. (`MAIN/HIERARCHY_BBS_STAGGERED_TASTE_BLOCKING_BRIDGE_KMS_SUBSTRATE_NARROW_NO_GO_NOTE_2026-05-15.md:33,48,63,86`; corresponding ledger under `MAIN/audit/data/ledger/hi/`:35.)

- **Using extra rungs to remove mirrors within bounded propagation.** The octree construction moves across `2^(j+2)` sites at rung `j`; bounded truncation restores the mirror. The bounded-speed ladder instead produces “one charged vector-like band per factor 2 in energy.” These are supplied-model results, not general exclusions of block maps. (`CHIRAL:215,349`.)

## **Overlap with this lane’s results.**

“NEW” below means no matching prior statement was found in the searched files.

- **Z0 — EXTENDS LW1’s gate factorization and Gauss conservation.** Z0 packages those inputs into exact regrouping, a coarse range bound and an explicit content count. Its distinguishing cost is that content “grows exponentially in `L^3`.” The prior input was a “finite product of even gates on individual edge triples.” (`TOE/ZM1.md:33,86–97`.)

- **Z1 and Z1.1 — NEW folded-rank theorem.** Z1 proves `d = L^3 r` under its translation, summability and exact-intertwining hypotheses. Prior #10092 excludes an “exactly relativistic lowest band”; it does not state this rank divisibility result for the live walk. Similar obstruction topics do not make them duplicates. (`TOE/ZM1.md:110,128–131`; `LOR:438`.)

- **Z2.0’s Clifford relations — DUPLICATES MT1 Theorem 4.** Both state that the six matrices are Hermitian involutions and “anticommute pairwise.” Z2.0 additionally gives the explicit walk and norm formulas. (`TOE/MT1.md:73`; `TOE/ZM1.md:147–150`.)

- **Z2.1–Z2.4, Z2 and its corollaries — EXTENDS MT1’s free-node expansion.** MT1 gives the leading Clifford cone. ZM1 adds the second-order basis rotation, normalized tent kernel, leakage control and explicit dynamics/sea comparison. The new estimate contains `2.66 κ² + 1.5 t κ³`; its spatial and tower limits remain explicit. The twenty-field content itself duplicates MT1’s count. (`TOE/MT1.md:96–101,137`; `TOE/ZM1.md:179–182,235–247,268,282`.)

- **Z4 — NEW Gauss-sum content bound.** The statement `D_u >= n_0 |S_u| + 1` concerns the dimension needed to embed a sum of fine Gauss generators. GA2’s earlier result instead excludes invertible operator links under bounded covariant generators. These are different conclusions. (`TOE/ZM1.md:304`; `TOE/GA2_Y2.md:44–48`.)

- **Z3 and Z3′ — NEW linear-field obstruction.** They force coefficients outside `S_u` to vanish in the stated finite and norm-closed linear classes. They do not classify nonlinear fields. The earlier GA2 obstruction concerns invertibility of a link matrix, rather than CAR block fields. (`TOE/ZM1.md:312–318,340,391`; `TOE/GA2_Y2.md:44`.)

## **Missed inputs.**

- **Dyadic refinement should inform the unresolved tower construction.** The prior note supplies actual compatible algebra embeddings and a Cauchy-section criterion. It also gives separate counterexamples to exact state and flow compatibility. Using it would make these separate obligations explicit; it supplies no three-dimensional interacting theorem. (`MAIN/DYADIC_EVEN_REFINEMENT_BOUNDED_THEOREM_NOTE_2026-10-12.md:5,553,570–579,793`: “no … interacting or higher-dimensional theorem is asserted.”)

- **The level-matched gauge split should be compared with any nonlinear interacting candidate.** It shows precisely why vacuum matching alone is insufficient. Its useful additional requirement is “each sector’s parent levels onto the children’s lowest levels.” This would add a low-energy-window test, conditional on a bridge from the toy to the live law. (`GAUGE:313,327`.)

- **The constrained-fiber series supplies concrete action-space obligations.** Raw integration has exact norm-one directions. Relevant-coordinate extraction, rescaling and an irrelevant-sector norm are named as necessary next objects. The later polymer theorem supplies a limited complex-source region. These could sharpen ZM1-i’s proposed trajectory contract; neither note supplies that trajectory. (`MAIN/WILSON_STAGGERED_CONSTRAINED_FIBER_DOBRUSHIN_AND_RAW_RG_UNIT_DIRECTIONS_BOUNDED_THEOREM_NOTE_2026-07-12.md:67–75`; `MAIN/WILSON_STAGGERED_CONSTRAINED_FIBER_TWO_LAYER_KP_COMPLEX_SOURCE_POLYMER_BOUNDED_THEOREM_NOTE_2026-07-12.md:67–70`.)

- **The observable-class follow-up is now a direct input.** The later draft gives five classes and warns that band-limited errors vanishing at zero momentum force exact zero-momentum spectral matching. It is “not yet distilled or refereed.” It would change the formulation of the next attack, after the owner chooses the class. (`TOE/ZM1_OBS_DRAFT.md:7,53`; `TOE/TOE_ASSEMBLY.md:227`: “the owner chooses after that.”)

- **The literature inventory preserves the remaining gauge bridge.** It says no verified source supplies T0-start or T0-rate for the fixed finite-register law. The needed object is a quantitative comparison with “the actual law, VC1 state, and ZM1 block map fixed.” This prevents replacing the missing comparison by large-register classicality or finitely many moments. (`TOE/LIT_QLM.md:3`.)

## **Consumers.**

- **LZ1.** The weakest relevant delivery is dynamical matching that transfers the light-band dispersion and bounds its leading correction. A common speed needs additional input: the target explicitly leaves “a mechanism that fixes one common `c` across species” open. (`TOE/TOE_ASSEMBLY.md:330–332`.)

- **MT1 and CH1.** MT1 needs the long-distance rotation action and physical excitation identification. CH1 needs a local gauged light sector with no extra light charged states and a reflection-positive measure. A free mode count alone supplies neither: MT1 asks for “local excitations” on the VC1 vacuum; CH1 requires “every doubler and every mirror gapped.” (`TOE/TOE_ASSEMBLY.md:364–366,409–411`.)

- **GA2 and the YM interface.** The weakest useful bridge is a specified block map with controlled gauge-invariant correlator comparison to an admitted reflection-positive measure, uniformly over the scales consumed. GA2 calls for “quantified errors.” The YM witness likewise says “a finite family at one scale is not enough.” These remain requested interfaces, rather than established branch inputs. (`TOE/GA2_Y2.md:169`; `YM/GOAL.md:34`.)

- **ST1.** It needs an effective vacuum-sector generator bounded below and a reflection-positive Euclidean continuation. Its explicit unresolved input is “reflection positivity for the chosen update with interactions.” (`TOE/TOE_ASSEMBLY.md:311–317`.)

- **GR1.** It needs controlled static long-distance matching for energy above the vacuum. Its target is the Poisson law with source `rho_E`, “the energy density above the vacuum.” (`TOE/TOE_ASSEMBLY.md:500–502`.)

- **GR2.** It needs a dynamical comparison retaining errors of order `(a/L)^2`, together with refinement compatible with collapse. The target separately leaves “refinement together with collapse” open. (`TOE/TOE_ASSEMBLY.md:517–519`.)