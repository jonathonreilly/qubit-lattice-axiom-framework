## **Searches run.**

Paths below are relative to `~/toe-worker`. Abbreviations:

- `T/` = `repo/.claude/science/physics-loops/toe-assembly-20261104/`.
- `G` = `ref/pr10126/docs/GAUGE_MATTER_REGISTERS_CONSOLIDATED_BOUNDED_THEOREM_NOTE_2026-10-30.md`.
- `F` = `ref/pr10129/docs/FAMILIES_FLAVOUR_CONSOLIDATED_BOUNDED_THEOREM_NOTE_2026-10-30.md`.

Read `ref/README.md` first. It identifies the status source: “Ledger rows: main/docs/audit/data/ledger/” (`ref/README.md:2`).

Ran case-insensitive filename searches over `ref/main/docs`, `ref/pr*/`, `ref/ym/`, and `T/`. Initial terms: **cell frame**, **split register**, **mode image**, **site phases**, **commutant**, **inter-cluster**. Follow-ups: **CAR automorphism**, **homogeneous unitary**, **gate-compatible**, **cube-local**, **cube tick**, **cell-local commutant**, **B5B**, **B5(b)**, **#9882**, **#10010**, **#10014**. Also searched `T/LIT_*.md` for **frame**, **cube**, and **compensat**.

Read relevant hits by line. The brief is `briefs/b5bref.txt:1`: “for the item B5(b) of part LW1.” The assembly connects the target to GA1-i: “the group that the chosen content gives” (`T/TOE_ASSEMBLY.md:389`).

## **Already in the repo.**

- **One-site CAR classification and gauge compensation.** LW1 B3 gives phase or particle-hole transformations: “These transformations form \(U(1)\rtimes\mathbb Z_2\)” (`T/LW1.md:237`). B5(a) already establishes an abelian image for number-preserving site-local actions (`T/LW1.md:249`: “a subgroup of a product of \(U(1)\)'s”). B4 supplies the phase-compensation construction: “Every dressed edge term, dressed cube gate and electric gate commutes with every \(\mathcal G_x\)” (`T/LW1.md:241`).

- **Block covariance does not select a non-abelian gauge group.** #9882 finds plain \(U(1)^4\), a twisted copy \(U(2)\), and coin breaking to \(U(1)\times U(1)\). Its scope is supplied block covariance, not compensated local-frame invariance (`G:53`: “plain covariance leaves a U(1)^4 one-body commutant”). Its many-body commutants “act on n-particle states, not as one-body transformations of the modes” ([source:42](/Users/jonBridger/toe-worker/ref/pr10126/docs/BLOCK_COVARIANCE_GIVES_ABELIAN_OR_COPY_U2_AND_NO_REGISTER_SELECTS_THE_GAUGE_GROUP_BOUNDED_THEOREM_NOTE_2026-10-21.md:42)). Status: consolidation entries are “author statements for review” (`G:11`).

- **The free cube tick has no exact corner \(su(4)\).** #10010 finds the one-layer commutant scalar and the two-layer internal algebra \(so(4)\). The precise corner statement is “the only corner-label operator … that commutes with the tick is X = 1” ([source:69](/Users/jonBridger/toe-worker/ref/pr10126/docs/TWO_LAYER_CUBE_TICK_HAS_EXACT_SO4_AND_NO_CORNER_SU4_BOUNDED_THEOREM_NOTE_2026-10-22.md:69)). Scope: “Supplied model; finite diagnostic” ([source:12](/Users/jonBridger/toe-worker/ref/pr10126/docs/TWO_LAYER_CUBE_TICK_HAS_EXACT_SO4_AND_NO_CORNER_SU4_BOUNDED_THEOREM_NOTE_2026-10-22.md:12)). The consolidation explicitly calls it “not a replacement of” #9882 (`G:460`).

- **The full free two-tiling family commutant is scalar.** #10044 corrects an earlier dimension-eight result. The consolidated statement is “the cell-local commutant over all k is 1-dimensional (scalars only)” (`F:212`). It concerns momentum-independent one-body operators of a supplied free tick, with specified copy terms (`F:204`: “Supplied model”). Status: “author statements for review” (`F:11`).

- **Local conservation and composite-cluster obstructions were already logged.** #10024 supplies a Gaussian criterion: a local constant of motion exists iff the one-mode map has an invariant subspace inside its support. Its scope explicitly excludes links: “flat-edge cube tick without links” (`G:1198`, status “logged”). #10026 finds a cluster algebra “abelian once generic C4v-covariant matter-end pieces are added” (`G:1199`, status “logged”). Neither row classifies B5B’s compensated frames.

- **Finite registers can support exact supplied Gauss laws.** #9926 gives exact \(U(1)\), and supplied three-colour rishons give \(SU(3)\). The consolidation limits the latter to a hop that “does not read which rishon mode carries which colour” (`G:246`). Its corrected scope says the result is “not that the lattice supplies a colour label” (`G:1140`). This is a construction under supplied roles and hops, not a group selector.

- **The five-mode fallback has an earlier cluster obstruction.** #10014 records that nearest-neighbour inter-cluster exactness forces the tiling lattice to be all of \(\mathbb Z^3\): “which means L = Z^3 and N = 1” ([source:147](/Users/jonBridger/toe-worker/ref/pr10126/docs/FIVE_MODES_PER_SITE_ARE_THE_SMALLEST_ANOMALY_FREE_PROTECTED_SPIN2N_CONTENT_BOUNDED_THEOREM_NOTE_2026-10-22.md:147)). Its conclusion is “Spin(10) on a spread cluster can be at most emergent” ([source:150](/Users/jonBridger/toe-worker/ref/pr10126/docs/FIVE_MODES_PER_SITE_ARE_THE_SMALLEST_ANOMALY_FREE_PROTECTED_SPIN2N_CONTENT_BOUNDED_THEOREM_NOTE_2026-10-22.md:150)). The consolidation narrows its protected-content claim to “Fock content only” (`G:1132`).

- **Existing Pauli and taste algebras have narrower meanings.** The per-site theorem proves the canonical Pauli \(j=\tfrac12\) module, while disclaiming identification with physical excitation spin ([source:10](/Users/jonBridger/toe-worker/ref/main/docs/PER_SITE_SU2_SPIN_HALF_THEOREM_NOTE_2026-05-02.md:10): “It does not, by itself, identify this”). Native gauge closure calls its inputs “nonabelian structural facts” ([source:136](/Users/jonBridger/toe-worker/ref/main/docs/NATIVE_GAUGE_CLOSURE_NOTE.md:136)). Current ledger statuses are both “unaudited” ([Pauli ledger:30](/Users/jonBridger/toe-worker/ref/main/docs/audit/data/ledger/pe/per_site_su2_spin_half_theorem_note_2026-05-02.json:30); [native ledger:30](/Users/jonBridger/toe-worker/ref/main/docs/audit/data/ledger/na/native_gauge_closure_note.json:30)). These are not prior classifications of exact frames of `L_cube`.

## **Failed attempts on file.**

- **Scalar \(U(1)\) per cell.** LW1’s draft claimed “the mode image is scalar \(U(1)\) per cell” (`T/LW1.md:253`). The recorded failing steps are the one-body factorization and the assumption of no internal links: “contrary to the specified twelve internal links” (`T/LW1.md:255`). The same line gives the counterexample: eight compensated site phases “are not scalar on the cell.”

- **Copy \(SU(2)\) from block covariance.** The failing step is survival under the update. #9882 concludes: “The copy SU(2) is not a symmetry of the tick” ([source:30](/Users/jonBridger/toe-worker/ref/pr10126/docs/BLOCK_COVARIANCE_GIVES_ABELIAN_OR_COPY_U2_AND_NO_REGISTER_SELECTS_THE_GAUGE_GROUP_BOUNDED_THEOREM_NOTE_2026-10-21.md:30)).

- **Corner \(su(4)\) on the two-layer tick.** The proposed corner algebra fails the exact commutant test: “Its corner labels carry no internal generator” ([source:109](/Users/jonBridger/toe-worker/ref/pr10126/docs/TWO_LAYER_CUBE_TICK_HAS_EXACT_SO4_AND_NO_CORNER_SU4_BOUNDED_THEOREM_NOTE_2026-10-22.md:109)). The apparent larger first-order algebra does not survive the lattice corrections (`G:21`: “with no corner su(4)”).

- **Dimension-eight full-tick symmetry.** The failing step was insufficient momentum sampling. The consolidation says it “was computed at only three momenta” and “The runner’s pass … is withdrawn” (`F:374`).

- **Unrestricted even-layer mode image.** B5B’s pass-1 example did not establish mode linearity. The frozen correction says: “no mode-linear image is established for it” (`T/B5B.md:118`). The even-layer classification remains open.

- **Unsplit whole-tick extension.** The recorded split-support step fails: “an unsplit \(L\) also invalidates the step placing \(M_eLM_e^*\) wholly outside \(A\)” (`T/B5B.md:163`). The same paragraph says the base-tick result does not cover an unspecified plaquette layer.

## **Overlap with this lane’s results.**

B5B ran and is “FROZEN 2026-11-05 after pass 3.” Its status expressly says “conditional mathematical results” and “not … an audit verdict” (`T/B5B.md:5`).

- **Theorem 3.1 — EXTENDS LW1 B5(a); DUPLICATES its own draft Theorem B5b.** B5(a) assumes “number-preserving one-body transformations” (`T/LW1.md:249`). B5B permits frames that “may entangle matter with internal links” (`T/B5B.md:17`) and obtains every compensated phase tuple (`T/B5B.md:80`: “every tuple in \(U(1)^8\) occurs”). The draft already states the phase-and-register form (`T/B5B_DRAFT.md:140`: “phases … and a unitary W”).

- **Scalar-cell conclusion — CONTRADICTS the original LW1 draft claim.** Earlier: “scalar \(U(1)\) per cell” (`T/LW1.md:253`). B5B: “the image of the full compatible set is \(U(1)^8\)” (`T/B5B.md:80`).

- **Corollary 3.2 — EXTENDS LW1 B3; DUPLICATES draft Corollary B5b.1.** B3 allows \(c_x\mapsto v c_x^\dagger\) (`T/LW1.md:237`). B5B says that branch “is excluded without assuming number preservation” (`T/B5B.md:90`). The draft already says “gate compatibility removes it” (`T/B5B_DRAFT.md:173`).

- **Theorem 3.3 — NEW relative to the located independent prior work; DUPLICATES draft B5b-T.** The earlier free commutant is “scalars only” (`F:212`). B5B instead assumes a split compensating register change (`T/B5B.md:25`: “Hypothesis T requires a split register change”). Its whole-base-tick classification holds for “all real \(a_e,\tau_E\)” and \(a_o\ne0\) (`T/B5B.md:96`). The same parameter coverage appears in draft B5b-T (`T/B5B_DRAFT.md:266`: “every \(a_e\) … every \(\tau_E\) and every spin S”).

- **Proposition 3.4 — DUPLICATES draft Proposition 7.2’s odd-half-step result, with a narrower even-layer conclusion.** Frozen: “the same phase conclusion holds” (`T/B5B.md:114`). Draft: “commuting with \(\gamma_o\circ\gamma_E\)” implies the phase-and-register form (`T/B5B_DRAFT.md:342`). The unsupported mode-image claim is explicitly corrected at `T/B5B.md:118`.

- **Theorem 4.1 — DUPLICATES draft Theorem 5.1, with the joint-action hypothesis explicit.** Both give “\(U(1)^8\rtimes\mathbb Z_2\)” (`T/B5B.md:122`; `T/B5B_DRAFT.md:205`). The frozen statement requires outside compensations “to preserve parity” (`T/B5B.md:122`).

- **Theorem 4.2 and Lemma 4.3 — DUPLICATE draft Theorem 7.3 and Lemma 7.4.** The draft already classifies commuting internal-link phases (`T/B5B_DRAFT.md:355`: “pairwise commuting Hermitian \(h_x\)”). It also states the internal-register commutant conclusion: “then O is a scalar” (`T/B5B_DRAFT.md:369`). The frozen versions are at `T/B5B.md:132` and `159`.

- **RC5 — NEW proof relative to the draft.** The referee explicitly says the draft’s non-closure assertion was “without proof” and “RC5 proves it” (`T/B5B_REFEREE.md:161`). The frozen proposition gives two compatible frames whose “composite … is not” compatible (`T/B5B.md:150`).

## **Missed inputs.**

- **Use #10044’s corrected full-tick commutant in the prior-work framing.** It replaces the dimension-eight claim with “scalars, dimension 1” (`F:376`). It would sharpen the comparison with whole-tick Theorem 3.3. It supplies no compensated-frame classification; its stated object remains the “cell-local commutant” (`F:212`).

- **Use #10010’s special-angle qualification when discussing exceptional angles.** At \(\varepsilon=\pi/2\), “eps joins the one-layer commutant” ([source:94](/Users/jonBridger/toe-worker/ref/pr10126/docs/TWO_LAYER_CUBE_TICK_HAS_EXACT_SO4_AND_NO_CORNER_SU4_BOUNDED_THEOREM_NOTE_2026-10-22.md:94)). This supplies a prior free-model example of angle-sensitive symmetry. B5B separately leaves “Exceptional gate angles and their full compensation groups” open (`T/B5B.md:7`).

- **Carry the #10014 cluster obstruction into fallback discussions.** Its exactness failure supports changing intrinsic site content rather than simply regrouping one-mode sites ([source:150](/Users/jonBridger/toe-worker/ref/pr10126/docs/FIVE_MODES_PER_SITE_ARE_THE_SMALLEST_ANOMALY_FREE_PROTECTED_SPIN2N_CONTENT_BOUNDED_THEOREM_NOTE_2026-10-22.md:150): “at most emergent”). The assembly already cites this input in the five-mode transition (`T/TOE_ASSEMBLY.md:208`: “no nearest-neighbour inter-cluster coupling keeps Spin(2N>2) exact”).

## **Consumers.**

- **LW1 B5(b).** Needs the abelian upper bound under its cube-local gate interpretation. Exact realization of every phase tuple strengthens that answer. LW1’s amendment records: “B5(b) is settled under split register changes” (`T/LW1.md:19`).

- **GA1-i and the PS-6 correction.** Need exclusion of non-abelian mode mixing under the stated frame and compensation hypotheses. The assembly now says “the SU(2) gauge group of T0 does not come from site or cell frames of L_cube” (`T/TOE_ASSEMBLY.md:137`).

- **LW1-5, MT1, CG1 and CH1.** Need the bounded obstruction to the exact one-mode-cell route, rather than a universal exclusion of emergent or nonlocal alternatives. The assembly identifies these consumers as “parts that need the gauge group” (`T/TOE_ASSEMBLY.md:208`). CH1 preserves the scope limit: “a failure claim for every possible reading is not established” (`T/CH1.md:91`). LW1-5 also reuses the frame definition (`T/LW1_5.md:33`: “B5B Definition F”).

- **B5b-E′ and GA1-P.** Need Lemma 4.3 and the precise failed support step as inputs. They still require new statements for the even gate, unsplit whole tick and plaquette layer (`T/B5B.md:163`: “Both obligations remain B5b-E′”).

- **GA2 and the YM branch.** No direct YM-branch consumer was found. The weakest relevant handoff is the exact-group identification for selecting the correct interface. For `L_cube`, the repository says “not T0,” but GA2’s abelian Coulomb-phase clause (`T/GA2_Y2_DRAFT.md:167`). The YM target itself starts with “SU(2) lattice Yang-Mills with the Wilson action” (`ref/ym/.claude/science/physics-loops/ym4d-hard-route-20261030/GOAL.md:26`).