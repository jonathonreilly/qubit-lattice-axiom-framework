**Searches run.**

- Read `ref/README.md` first. Lines 2–5 identify main’s ledger, the consolidation PRs, and the YM corpus.
- Initial terms: `symmetric mass`, `Fidkowski`, `Kitaev`, `Majorana chain`, `mirror gap`, `mirror gapping`, `SMG`.
- Follow-up terms: `eight.Majorana`, `3450`, `Wang.Wen`, `Haldane`, `null.vector`, `chiral`, `fermion`, and relevant claim identifiers.
- Searched `ref/main/docs`, `ref/pr*/`, `ref/ym/`, and `repo/.claude/science/physics-loops/toe-assembly-20261104/`. Followed relevant hits into consolidations, ledger rows, TOE parts, drafts, referee reports, prior digests, and `LIT_SMG.md`.
- `briefs/SMG1.txt` was absent. No edits, internet searches, git commands, or proof checks were performed.

Path abbreviations used below:

| Label | Exact repository path |
|---|---|
| `T/` | `repo/.claude/science/physics-loops/toe-assembly-20261104/` |
| `M/` | `ref/main/docs/` |
| `A/` | `ref/main/docs/audit/data/ledger/` |
| `C` | `ref/pr10131/docs/CHIRALITY_DOUBLERS_CONSOLIDATED_BOUNDED_THEOREM_NOTE_2026-10-30.md` |
| `G` | `ref/pr10126/docs/GAUGE_MATTER_REGISTERS_CONSOLIDATED_BOUNDED_THEOREM_NOTE_2026-10-30.md` |
| `F` | `ref/pr10129/docs/FAMILIES_FLAVOUR_CONSOLIDATED_BOUNDED_THEOREM_NOTE_2026-10-30.md` |
| `S` | `ref/main/docs/SPIN10_SYMMETRIC_ATOMIC_GAPS_MIRROR_BOUNDARY_PROJECTION_AND_CURRENT_RESPONSE_BOUNDED_THEOREM_NOTE_2026-09-14.md` |

**Already in the repo.**

- **The full construction remains open.** The prior chirality synthesis says “**Answer: not obtained**” and limits its surviving results to “supplied-model, finite, 1+1D or Euclidean-only” (`C:17`). Its status is author-side: “These are author statements for review” (`C:11`). Frozen CH1 likewise “does not construct a chiral gauge theory, a mirror gap” (`T/CH1.md:5`).

- **The closest rung-1 precursor is #10078, logged.** It reports an exact eight-Majorana Cayley-cell spectrum: “−14 (1), 0 (8, odd), +2 (7, even).” Its supplied hopping chain has finite diagnostics through \(L=8\), with restricted coverage at that size. Its stated exclusions include “L > 8” and “gauge fields.” This is an exact local spectrum plus finite chain evidence, not the requested framework-tick theorem. The recorded source is `claude/toe-cayley-mirror-gap-20261021`, revision `d2b189516809` (`C:2341`).

- **A Spin(10) pair-square atom already exists as #9910, logged.** On a supplied 32-mode mirror cell it reports a “unique Spin(10)-singlet, spin-singlet, Z4-trivial ground state” and gap \(19.0715g\). It explicitly leaves “the lattice phase at finite hopping” unestablished. The recorded source revision is `839b6788c352` (`C:2316`).

- **Main contains a refined Spin(10) atom and boundary analysis.** The supplied CAR model has a “Unique Spin(10) singlet and exact atomic gap” (`S:28`). Its refined many-body gap remains \(\Delta\): “the orthogonal state … attains Delta” (`S:97`). Its source calls itself “conditional-support” (`S:7`). The ledger’s effective status is `"unaudited"` (`A/sp/spin10_symmetric_atomic_gaps_mirror_boundary_projection_and_current_response_bounded_theorem_note_2026-09-14.json:27`).

- **Exact local pairing algebra is available.** The supplied 32-complex-mode vertex fixes “kappa=(3/2,-1/2,0,0)” and “Q_QMC=Q_SIGN1/16” (`M/CHIRALITY_LOCAL_ENDPOINT_ALGEBRA_NOTE_2026-10-18.md:6`). Its boundary is explicit: “interacting gap and symmetric mass generation are not conclusions” (same file, line 10). Its ledger effective status is `"unaudited"` (`A/ch/chirality_local_endpoint_algebra_note_2026-10-18.json:27`).

- **The 3450 interaction lattice is already worked out.** Logged #10058 gives neutral six-fermion generators \(l_1=(1,-2,1,2)\), \(l_2=(2,1,-2,1)\): “it is K-null (a gapping lattice)” (`C:2334`). Kept #10060 reports a unique gapped three-site cell and cites Yarotsky stability “for the vector-like content only.” The stability theorem is supplied, with its constant uncomputed (`C:1690`; `C:1493`).

- **Lower-dimensional chiral constructions exist with different carriers.** Logged #9927 supplies a depth-three rotor disentangler and exact Gauss law, using “an angle per site and a winding integer per link.” Finite clocks retain only “Z_5,” not exact U(1) (`C:2318`). Logged #9939 supplies a chiral SU(2) × U(1) rotor construction, but “the flow to the locked phase is cited, not computed” (`C:2319`).

- **The block-local quartic has exact algebra and finite mirror-gap evidence.** Kept #9992 reports that the interaction alone has a “unique ground state with gap g.” Its hopping evidence is CT-INT on a supplied SU(4) Dirac-band toy: “The toy is not Spin(10)” and “L <= 6.” The same result records release of the light partners (`C:519`).

- **An anomaly-compatible 16-Weyl toy exists, without a persistent gap theorem.** Kept #10004 reports searched Z4-type symmetries with “Z16 index 0 mod 16.” Its thermodynamic conclusion is “no L-independent gap is shown” (`C:721`; `C:802`). Its Spin(10) content is “inherited … not forced by this term” (`C:725`).

- **Euclidean overlap results provide a separate partial route.** The consolidation reports “exact Ginsparg-Wilson chirality without doublers,” while stressing that the chiral content is “abelian, Euclidean and not a walk sector.” Its Standard Model background tests remain “diagnostics” (`C:21`).

- **The register obstruction predates SMG1.** The gauge synthesis reports vector-10 free cones and parity-odd fixed-site excitations “never the 16,” for site-bilinear Spin(10) (`G:23`). Its stated escapes are “a site-count change, deconfined spinons … or a Spin(10) not generated by site bilinears” (`G:27`). These are author statements, not audit verdicts (`G:11`).

- **Frozen TOE results sharpen that obstruction without closing the interacting question.** Theorem SC conserves the local centre-class pattern; “A spinor-class charge does not move” in that defined local-centre sense (`T/LW1_5.md:198`). Amendment 3 records the four frozen probes and their open alternatives (`T/LW1_5.md:11`). CG16S establishes free half-spin pairing under NN-a and condition E; its scope leaves open “gates violating E” and “a filled or entangled background” (`T/CG16S.md:140`).

- **L5-U already has candidate composite family content and interaction tensors.** CH1 constructs an anomaly-free one-site family exactly for \(2\le m\le8\), but labels this “operator content only” (`T/CH1.md:218`; `T/CH1.md:222`). Frozen CH1-5U proves covering, trace, SU(2), Z4, and quartic-phase results; full global-anomaly closure still uses an “unverified bordism computation” (`T/CH1_5U.md:7`; `T/CH1_5U.md:9`). The two mirror quartics leave exactly the gauged-centre phase image within the specified linear unitary class (`T/CH1_5U.md:143–145`).

- **RCS-P16 supplies longitudinal propagation, not the target particle.** Its frozen U(16)-rishon witness has \(V(K)=e^{iK_1}\), a node plane, and transverse flatness for the specified matter-activated class (`T/RCSP16.md:7`). It explicitly yields “No irreducible 16” and no “chiral Weyl particle” (`T/RCSP16.md:11`).

**Failed attempts on file.**

| Attempt | Recorded failing step |
|---|---|
| Free circuits, records, feedback, zoom and pumping | The synthesis reports zero winding for the stated circuit histories. Exact mode number and mirror reflection also obstruct removing only the mirror: “forbids gapping the mirror alone” (`C:19`; `C:151`). |
| Octree or bounded-speed rung escape | The octree route “needs unbounded range”; the bounded-speed ladder leaves “a charged tower or a charged mirror at a cut” (`C:19`). |
| Tetrahedral FK-type term | Logged #9909’s mirror map fixes the term, so “it gaps both light copies and cannot select one” (`C:2315`). |
| Strong cube-filtered quartic | The corrected sequence retains free Fermi lines in one toy and “pair order at g/t >= 8” in another. An apparent symmetric window also adjoins a quadratic touching, rather than a Dirac point (`C:2249–2250`). |
| Gapping the block mirror | The successful symmetric mirror gap “releases every light mode the mirror was pairing.” The surviving light spectrum is therefore not the desired chiral one (`C:519`). |
| Fine-scale momentum filter | It “keeps no Z4 inside U(1)_eps, only fermion parity,” losing the intended protecting symmetry (`C:742`). |
| One-taste filtered mirror | Its corrected obstruction is the mode-number Z4 anomaly: “index 16 = 0 with two tastes and 8 with one taste.” The former attribution to Z4_J was withdrawn (`C:2209–2211`). |
| Anomaly-free 16-Weyl filtered toy | The gap halves between the reported sizes; “Survival of the K gap as L -> infinity is not established: inconclusive” (`C:721`). |
| FREEZE light-partner removal | Schur forbids the stated light-light masses; the two-cell-label escape is blocked by light-sector winding (`C:19`). Its mirror-only quartic also “frees the X and M partners” (`C:2231`). |
| Strongly gapping a complete far layer | The mirror branch survives and “moves one layer in” (`C:1491`). Main’s atomic projection similarly “does not remove the topological interface” (`S:201`). |
| One-orbital Spin(10) quartic atom | The vector pairing channel is identically zero: “The suggested H … is zero.” Under the stated particle-hole symmetry, no interaction below degree 16 gives the desired unique site state (`C:1657–1663`). |
| Inferring a 3450 chain gap from \(L=12\) | The larger-size check gives persistence ratio \(0.358\); “persistence is not established.” The eight-Majorana proxy does not establish the slab or light-wall result (`C:2255`). |
| Using only atomic strong-coupling control | Main’s bound retains hopping-norm volume dependence. “This is not a volume-uniform expansion” (`S:235`; `S:239`). |
| Moving the unwanted content to quasienergy π | The Floquet sum rule forces π flow. The far-termination escape remains chosen boundary data, and “the far-wall gapping itself is not shown” (`C:19`; `C:2237`). |
| Smoothed far-wall gauging | The supplied four-dimensional slab develops “a cutoff-scale photon mass” (`C:19`). |
| Treating anomaly cancellation as a local measure | The admissible finite tests miss the proposed momentum criterion. The consolidation explicitly says this “does not show … non-local”; larger discriminating tests were unrun (`C:2221`). |
| Importing a Spin(10) flow directly into L5-U | The elementary quasi-free start lacks the required composite charge sectors. “The proposed gapping flow and a lattice realization … remain unproved” (`T/CH1_5U.md:155`). |
| Multiplicative overlap pullback | Nilpotent link entries evaluate to a matrix that is “zero and not unitary.” Operator-valued or approximate alternatives are not excluded (`T/CH1_5U.md:157`). |
| Excluding composite light fields by charge or elementary poles | Charge-dependent locality/spectral exclusions fail against a static zero mode (`T/CH1_5UQ.md:126`). An elementary pole theorem alone “does not establish a constraint on the composite family” (`T/CH1_5U.md:159`). |
| Turning the straight-string witness into a Weyl 16 | Its one-dimensional band cannot have a three-dimensional positive-speed Clifford cone (`T/RCSP16.md:86`). The specified frozen backgrounds force transverse flatness (`T/RCSP16.md:92`). |

**Overlap with this lane’s results.**

not run

**Missed inputs.**

These are prospective inputs for SMG1.

- **Start from #10078’s actual precursor.** Its exact Cayley spectrum and chain diagnostics would avoid rediscovering the cell calculation. The remaining rung-1 obligations include the native tick and a size-independent gap. Its recorded scope stops at “L > 8” (`C:2341`).

- **Use the existing FK rebuild map.** It identifies “four compatible quartic constraints” and calls for the Clifford identities, excited energy, and “antiunitary action.” It separately leaves “A weak-hopping stability theorem” to prove (`T/LIT_SMG.md:200–202`). This would make the first rung’s missing work explicit.

- **Use the atomic boundary and current discriminator.** Main shows that extra nodes survive particular atomic projections and that “Their actual charged-current response detects the additional modes” (`S:14–16`). This would add a light-sector test beyond uniqueness of the mirror cell.

- **Use the corrected pairing normalization.** The endpoint note fixes “Q_QMC=Q_SIGN1/16.” It also lists the kinetic, particle-hole, boundary, and factorization hypotheses needed for lattice positivity (`M/CHIRALITY_LOCAL_ENDPOINT_ALGEBRA_NOTE_2026-10-18.md:6`; same file, line 10). This would prevent importing an endpoint identity as a sign-free lattice theorem.

- **Use exact-group L5-U interactions.** The literature map supplies charge-balanced quartic channels and warns: “A mass at fixed nonzero Phi does not prove a gap after its orientation fluctuates” (`T/LIT_SMG.md:82`). Frozen CH1-5U supplies the more restricted quartic symmetry theorem (`T/CH1_5U.md:143`). This would replace an unspecified Spin(10) interaction import with explicit U(5) tensors.

- **Keep composite CAR and anomaly premises explicit.** The ten triple products “cannot be ten independent CAR modes” on the 32-dimensional site (`T/CH1.md:126`). Interacting AM and AM-5 are “not proved for these Floquet laws” (`T/CH1.md:28`). These inputs would separate representation arithmetic from a realizable many-body gapping construction.

- **Use the 3450 correction history before rung 2.** The null lattice is available, but the persistence claim was weakened (`C:2334`; `C:2255`). CH1 also excludes charges 4 and 0 as odd local fields of its specified one-mode charge law (`T/CH1.md:92`). This would force the carrier choice and bulk-included gap obligation to be stated.

- **Use the precise limits of the frozen obstructions.** CG16S leaves filled or entangled backgrounds open (`T/CG16S.md:140`). RCS-P16 leaves the Clifford form and VC1 identification open (`T/RCSP16.md:11`). These would identify which hypotheses a new construction changes, without treating a local-centre or free-band obstruction as universal.

**Consumers.**

| Consumer | Weakest useful statement |
|---|---|
| **SMG1’s next rung** | A native eight-Majorana 1+1D framework tick with a gap and symmetric unique ground state. This is the explicit first rung; mirror-selective chirality belongs to rung 2 (`T/TOE_ASSEMBLY.md:718`: “rung 1 … with a gap and a symmetric unique ground state”). |
| **CH1-i** | A mirror gap that preserves the desired light sector and introduces no extra light charged states. Its contract says “without releasing light partners.” The local gauged measure and reflection positivity remain separate (`T/TOE_ASSEMBLY.md:447`). |
| **CG1 and MT1-ii** | A dynamical light family carrying the required representation and charges. A spinor-class label or field count is insufficient: MT1 leaves “MT1-ii as a physical family claim” open (`T/MT1.md:29`). CG1 still requires physical charge identification and completion (`T/TOE_ASSEMBLY.md:462`). |
| **FL1 / #10022** | Symmetric mirror gapping with the required Spin(10), turn, and uniform-copy hypotheses. The prior implication gives only a necessary multiple-of-three condition: “Three families are not derived” (`F:19`). Frozen FL1 retains conditional matching premise V0 (`T/FL1.md:29`). |
| **FAM1** | At least W2’s rung-2 chiral mirror-decoupling statement. The assembly schedules “no lane until W2’s rung 2” (`T/TOE_ASSEMBLY.md:724`). |
| **GA2, matter bridge Y4** | A local gauged chiral measure suitable for the matter RG extension. “CH1-ii … is the entry point.” Pure-gauge T0 does not supply this extension (`T/TOE_ASSEMBLY.md:606`). |
| **Named YM-branch items** | none found. The explicit TOE interface says the chiral-matter extension is “outside T0’s statement” (`T/TOE_ASSEMBLY.md:606`). |