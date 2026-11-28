lead: anthropic/claude-opus-5-5/high mac-mini-worker
lease_until: 2026-11-16T03:54Z

# gap-outside-read-opus: literature on frame changes for the gap (row 1005)

Queue row 1005, FINISH.md line 1086, pinned at commit 95fecd964. Companion of row 1004
(`gap-frame-change-exercise`). Literature reading only: no attack, no new claim.
Started 2026-11-15T15:54Z on Mac mini worker 3.

## Plan (at most eight steps; each step appends its result before the next)

1. Read FINISH.md (efficiency rules, build-on-published-work, row 1004/1005 context) and grep the lane
   (library/, library/prior/, FINISH rows) for each of the seven topics; list what the lane already holds.
2. Topic A: adiabatic continuity on R^3 x S^1 (Unsal, Yaffe, Poppitz, and later); Topic G: soft-broken
   SUSY YM and confinement. Search arXiv abstracts, grade each hit.
3. Topic B: rigorous 3D compact U(1) gap (Gopfert-Mack) and any 4D-to-3D reduction carrying it.
4. Topic C: YM on S^3 and hyperbolic space (van Baal, Hosotani, later): small-radius gap, continuity in radius.
5. Topic D: twisted boundary conditions and flux free energies with rigorous inequalities ('t Hooft,
   Tomboulis-Yaffe, Borgs-Seiler, Chatterjee and later).
6. Topic E: gap stability along paths of local Hamiltonians (Bravyi-Hastings-Michalakis, Michalakis-Zwolak,
   later) and use for lattice gauge theories; Topic F: gradient-flow and stochastic-quantisation monotones.
7. Synthesis table: statement, grade, group/dimension, separates gapped from massless-factor theory or not;
   which frame changes the literature supports as rigorous; credit to Sussman-Alpoge repository where used.
8. RESULT line.

## Step 1: lane inventory (grep of library/, library/prior/, FINISH rows; done 2026-11-15 ~16:05Z)

Grep keys and row hits are in this section. No numeric run is planned (reading item), so memory_pressure was not needed.
Labels below are the lane's own; I re-read only the lines quoted.

**A. Adiabatic continuity on R^3 x S^1, and the twisted thin torus (Route T).** Rows 669, 676, 678, 686-689,
744, 838, 842, 862, 880. The lane already holds:
- Route T: the twisted thin torus (Z/n)^2 x (Z/M)^2 with 't Hooft flux, crux (AC'-lat) (row 678, `library/gap-ac-lat.md`),
  the chart (CH) proved by hand (row 679, `gap-twist-chart.md` L262), Theorem S1 attempt with Theorem BAD and CH-D
  (row 842, `gap-s1-opus.md` L670: weak-coupling gap c/n on the thin torus; Lemma PE missing, row 862).
- `gap-skeleton-final.md` L249: "Tanizaki and Unsal, arXiv:2201.06166 ... The continuity (AC') is their conjecture."
- `gap-means-max.md` L50-51: (AC') is belief; other calculable deformations (Higgs, soft SUSY) need the same continuity.
- `prior/gap-kflow-read-opus.md` H18: Unsal-Yaffe 0803.0344, semiclassical, abstract only.
- `prior/gap-lit-xvol.md` L37: large-N volume independence (Kovtun-Unsal-Yaffe hep-th/0702021, Unsal-Yaffe 1006.2101), wrong N.
- `prior/gap-lit-rigid.md` L23, L83: Nguyen-Tanizaki-Unsal 2023 (temporal gauging), conditional on a gap.
- `gap-brainstorm-max.md` G7 (L482), L680 (recalled literature: Tanizaki-Unsal 2022, Hayashi-Tanizaki 2024, Unsal-Yaffe 2008).
- NOT in the lane: Poppitz's papers (Poppitz-Schafer-Unsal, Anber-Poppitz), the deformed-YM continuity papers read
  at primary-text level, Bergner et al. lattice checks of continuity, Cherman-Poppitz-Unsal-type bion results.

**B. 3D compact U(1) gap (Gopfert-Mack) and 4D-to-3D reductions.** Rows 656, 688, 735, 736, 782, 787, 992, 1002.
- `prior/gap-crux-lit-nonab.md` T5 (L135-152, L213): Gopfert-Mack CMP 82 (1981/82) 545-606, abstract page; mechanism
  "explicitly U(1), via exact duality"; Chatterjee arXiv:2602.00436 (3D, central U(1)), full HTML read.
- `prior/gap-lit-u1.md` L42: 3D Villain U(1) confines at all couplings; FS 4D U(1) no area law.
- `prior/gap-3dmix-read-opus.md` L48, L236: "YES, abelian only"; no 3D SU(2) mixing bound outside strong coupling.
- `prior/gap-kflow-read-opus.md` H17: THEOREM, 3D abelian, selective via 3D monopole Debye screening (fails in 4D).
- NOT in the lane: any rigorous 4D-to-3D reduction (high-temperature dimensional reduction, Polyakov's 3D
  argument for Georgi-Glashow, rigorous 3D Georgi-Glashow results), or a statement that carries Gopfert-Mack to R^3 x S^1.

**C. YM on S^3 and on hyperbolic space.** Rows 656, 661, 729, (others hit "hyperbolic" in other senses).
- `prior/gap-small-volume-lit.md` L101: van Baal review and de Divitiis et al. read in part (torus, not S^3).
- `prior/gap-lit-2.md` L21, L91: van Baal "QCD in a finite volume" not found; no small-torus gap proof found.
- `prior/gap-crux-lit-2.md` L170-172: Alonso Pichardo Zenodo preprints (2026) on S^3 x R, preprints, not refereed.
- `prior/gap-lit-grok-paths.md` L418: van Baal CMP 94 (1984) constant-field solutions on T^4.
- NOT in the lane: van Baal's S^3 papers (van Baal-van den Heuvel, Cutkosky), Hosotani, Rigorous YM on S^3 or on
  hyperbolic space, any continuity-in-radius statement. This topic is new to the lane.

**D. Twisted boundary conditions and flux free energies with rigorous inequalities.** Rows 661, 688, 690, 697, 702,
708, 734, 739, 742, 745, 749, 752, 765, 778, 787-800, 821, 831, 867, 878, 922, 928, 971, 995. Heavily covered:
- `prior/gap-lit-flux.md` L21-39: Kanazawa generalised TY inequality and twist-sum identity; Tomboulis-Yaffe (SU(2),
  high-temperature deconfinement, inequalities linking Wilson, 't Hooft, electric flux); Borgs-Seiler (chain of
  string-tension inequalities); Chatterjee centre symmetry; Tomboulis all-coupling claim and its criticism;
  Kovacs-Tomboulis (numerical vortex free energy).
- `gap-tomboulis-read.md` L879: Tomboulis 2007 claim fails at the global matching step (Appendix C, (C.8)-(C.10)).
- `prior/gap-lit-rigid.md` L51, L83: 't Hooft 1979 duality, Nguyen-Tanizaki-Unsal Appendix A (conditional).
- `prior/gap-twist-data.md` L40: Kovacs-Tomboulis numerical vortex free energy.
- This step will not re-search topic D; it only adds items not on file (step 5).

**E. Gap stability along paths of local Hamiltonians.** Rows 713, 745, 749 (and the MDTN note of `gap-prior.md`).
- `prior/gap-math-lit.md` L105-111: Hastings-Koma, Bravyi-Hastings-Michalakis Theorem 1 read; "Verdict for topic 7: no use".
- `prior/gap-lit-rigid.md` L61, `prior/gap-lit-casimir.md` L46-47: BHM, rigorous, weak perturbation only.
- `prior/gap-prior.md` L101, L209: a note in the repository imports BHM for truncated-link SU(2)/SU(3) at strong coupling.
- `gap-brainstorm-max.md` G15 (L498): "Gives a gap only for small magnetic perturbation: strong coupling. Not order one."
- NOT in the lane: Michalakis-Zwolak (frustration-free, local-gap condition), Nachtergaele-Sims-Young stability
  (2020-2022), Bachmann-Michalakis-Nachtergaele-Sims automorphic equivalence, gap-path results for lattice gauge
  (Kogut-Susskind) Hamiltonians, Cubitt-Perez-Garcia-Wolf undecidability as a negative result.

**F. Gradient flow and stochastic quantisation monotones.** Rows 688, 689, 713, 740, 747, 784-787, 812-845, 899-975.
- `prior/gap-math-lit.md` L49, L86-87: Shen-Zhu-Zhu 2204.12737 (strong coupling), Chandra-Chevyrev-Hairer-Shen 2D YM
  and 3D YMH; `prior/gap-crux-lit-cross.md` C8 (L63-67, L99, L132): Chevyrev-Shen 2D invariance, Piazza-Shen 2D all
  couplings LSI (arXiv:2610.35286); `prior/gap-lit-ineq.md` L53.
- `prior/gap-crux-lit-nonab.md` L23-35: Mondal 2301.06996 (orbit-space Bakry-Emery curvature, GUIDE weak).
- NOT in the lane: Luscher's Wilson flow as a monotone (flow time t, E(t)), its rigorous properties
  (Luscher-Weisz), gradient-flow coupling step scaling, Narayanan-Neuberger, rigorous YM heat flow on 4-manifolds
  (Rade, Struwe, Waldron) used as a monotone.

**G. Soft-broken supersymmetric YM and confinement.** Rows 1004, 1005 only.
- `gap-means-max.md` L51 and `gap-crux-exercise-astra.md` C19 (L384, L458): "Adding matter, supersymmetry ... and
  removing it preserves the gap: ... No lane theorem supplies this uniform bridge."
- `gap-brainstorm-max.md` L299 (Witten Laplacian, an unrelated use of "supersymmetric").
- NOT in the lane: Seiberg-Witten soft breaking (Douglas-Shenker; Alvarez-Gaume et al.), N=1 SYM with gaugino mass
  (Poppitz-Unsal-Schafer continuity), lattice N=1 SYM (DESY-Munster), any rigorous statement. New to the lane.

**Duplicate check.** This row is a reading item, not an attack: no open lemma is attacked here, so the
open-core grep rule (FINISH 0a) does not trigger. Row 1004 generates and tests frame changes; this row only
records literature. Row 1003 covers inputs inside the present frame (b_0, centre flux, instantons); topic D overlaps
it, so step 5 only records sources not on file.

## Step 2: topics A (adiabatic continuity on R^3 x S^1 and on R^2 x T^2) and G (soft-broken SUSY YM)

Source: arXiv API abstracts fetched 2026-11-15 into `/tmp/gor1005/a` (not committed). Abstract level unless
marked; primary-text reads are in Step 2b. Grades: LT = theorem on the lattice, CT = theorem in the continuum,
SC = semiclassical, NUM = numerical, BEL = belief or conjecture. "Selective" = would tell a gapped theory from one
with a massless factor (the lane's Lemma PT sense).

**A1. Unsal and Yaffe, "Center-stabilized Yang-Mills theory: confinement and large N volume independence",
PRD 78 (2008) 065035, arXiv:0803.0344.** Statement (abstract): a double-trace deformation of SU(N) YM on
R^3 x S^1; "if the theory is formulated on R^3 x S^1 with a sufficiently small compactification size L, then an
analytic treatment ... is possible. In this regime, we show that the deformed Yang-Mills theory has a mass gap and
exhibits linear confinement." Continuity: "there are no order parameters which distinguish the small and large
radius regimes." Grade: SC for the small-L gap (dilute monopole-instanton gas, Polyakov mechanism after
abelianisation); BEL for continuity in L (argued from the absence of an order parameter, which does not exclude a
transition). Group/dimension: SU(N), 4D with one small circle, deformed action (not Wilson YM). Selective: yes at
small L, in kind: the gap comes from monopole-instantons of the non-abelian theory; a product with a free photon keeps
a massless 3D photon. Continuity is not selective by itself: it is the statement that would need proof.

**A2. Shifman and Unsal, PRD 78 (2008) 065004, arXiv:0802.1232.** QCD-like theories with one massless fermion on
R^3 x S^1 with double-trace deformation; at small r(S^1) "confinement and chi SB" computed; "we argue that small and
large-r(S_1) physics are continuously connected." Grade SC (small r), BEL (continuity). SU(N), 4D. Selective at small r.

**A3. Unsal, PRL 100 (2008) 032005, arXiv:0708.1772.** SU(2) QCD(adj), several massless adjoint Weyl fermions on
small S^1 x R^3: "Confinement, the area law ... and the generation of the mass gap in the gluonic sector are shown
analytically" (center symmetry is stable without a deformation, by the fermions). Also notes a zero-temperature chiral
transition must occur somewhere (so continuity fails for the chiral order parameter). Grade SC. SU(2), 4D, with
adjoint matter. Selective at small L in the gluonic sector. Negative lesson: continuity in L is not automatic even
in this class; it fails for chiral data.

**A4. Poppitz, Schafer, Unsal, "Continuity, deconfinement, and (super) Yang-Mills theory", arXiv:1205.0290 (JHEP 10
(2012) 115 by memory, not checked).** SU(2) YM with one adjoint Weyl fermion of mass m on R^3 x S^1 (periodic
fermions). m -> infinity is thermal pure YM; m -> 0 is circle-compactified SYM. "In the m-L plane, there is a line of
center symmetry changing phase transitions"; near m = 0, L_c is semiclassical and the transition second order.
Grade SC (near m = 0); the link to pure YM is BEL. Key point for this lane: **for pure YM on R^3 x S^1 without a
deformation, continuity in L FAILS** (the thermal deconfinement transition at L_c = 1/T_c). The pure-YM side
needs a deformation or a twist. Selective: yes (the confined side is gapped by monopole-instantons and bions).

**A5. Poppitz, Schafer, Unsal, arXiv:1212.1238.** Same mechanism for all simple groups (perturbative potential,
monopole-instantons, neutral bions). Grade SC. For SU(N_c) and G_2. Same reading as A4.

**A6. Tanizaki and Unsal, PTEP (2022), arXiv:2201.06166 (on file, row 669/676).** 't Hooft flux through a small
T^2: semiclassical centre-vortex confinement on R^2 x small T^2. Quote: "We conjecture that the weak-coupling vacuum
structure on small T^2 x R^2 is adiabatically connected to the strong-coupling regime on R^4 without any phase
transitions." Grade SC (small T^2), BEL (continuity, stated as conjecture). SU(N), 4D, undeformed YM. Selective at
small T^2 (fractional-instanton centre vortices; U(1) has zero modes, as the lane's S1 note records).

**A7. Guvendik, Schaefer, Unsal, "The metamorphosis of semi-classical mechanisms of confinement",
arXiv:2405.13696.** "There are two distinct regimes ... where we can demonstrate confinement, the existence of a
mass gap, and fractional theta angle dependence using a reliable semi-classical calculation": (i) small S^1 with
double-trace deformation (monopoles), (ii) small T^2 with 't Hooft flux (centre vortices). On R^2 x S^1 x S^1 they
derive the vortex EFT from the monopole EFT; "This proves adiabatic continuity of the two confinement mechanisms
across dimensions." Grade SC: "proves" means within the semiclassical EFT; this is continuity between two weakly
coupled regimes, NOT continuity to R^4. SU(N), 4D. Selective in kind. Relevance: the closest published statement to
a continuity along a path of geometries, and it stays inside the weak-coupling window.

**A8. Dobozy and Poppitz, arXiv:2606.22078 (2026).** Numerical minimisation of the lattice action of trace-deformed
YM on twisted T^4, interpolating between R^{4-k} x T^k geometries; classical minimum-action configurations of
fractional charge. Grade NUM (classical saddles only, no quantum statement). SU(N). Not selective (classical).

**A9. Lattice tests of continuity in deformed YM.** Vairinhos, arXiv:1111.0303 (lattice center-stabilised YM on
R^3 x S^1: bulk transition and centre breaking); Bonati, Cardinali, D'Elia, PRD 98 (2018) 054508, arXiv:1807.06558
(trace-deformed SU(3), theta dependence agrees with the semiclassical prediction); Bonati, Cardinali, D'Elia,
Giordano, Mazziotti, PRD 103 (2021) 034506, arXiv:2012.13246: "the reconfinement phase transition is first-order"
(trace-deformed SU(3) on R^3 x S^1, as the deformation grows at fixed small L); Bonati et al., arXiv:2606.20270 and
PoS(LATTICE2026)242 (3D SU(2) trace-deformed flux tube deviates from Nambu-Goto deep in the reconfined phase).
Grade NUM. Reading for the lane: along the deformation parameter at fixed L there IS a first-order transition (SU(3));
continuity is claimed only inside the centre-symmetric region. No lattice paper found proves or measures a
continuity statement in a form a proof could consume.

**A10. Bergner and Piemonte, arXiv:1410.3668.** Lattice N = 1 SYM (SU(2)) on R^3 x S^1 with periodic fermions and a
soft gluino mass: "We find a deconfined region that shrinks when the fermion mass is lowered ... At the smallest
fermion masses we find no indication of a deconfinement transition." Grade NUM. Supports continuity in L only near
the SUSY point; at the pure-YM end (large mass) there is the thermal transition, as in A4.

**A11. Cossu and D'Elia, JHEP 0907:048 (2009), arXiv:0904.1353.** SU(3) with two adjoint Dirac flavours, one
compact spatial direction: "four different phases ... two center symmetric phases, for large or small values of Lc,
separated by two phases in which center symmetry is broken". Grade NUM. Negative evidence: **continuity in L fails**
for finite-mass adjoint QCD on the lattice at that mass; the small-L and large-L centre-symmetric regimes are
separated by transitions.

**A12. Poppitz, "Notes on confinement on R^3 x S^1", arXiv:2111.10423 (review).** SU(2) with massive or massless
adjoint fermions; "when available, present evidence for the absence of phase transitions as a function of the S^1
size"; notes "the necessity for analytic continuation of path integrals" (bion amplitudes need it). Grade SC review.
Reading for the lane: the bion contribution that stabilises the centre is defined by a prescription (BZJ, Lefschetz
thimbles), so the semiclassical gap at small L is itself not a theorem even at small L.

**Topic G, soft-broken SUSY.**

**G1. Douglas and Shenker, NPB 447 (1995) 271, arXiv:hep-th/9503163.** From the Seiberg-Witten solution, the
N = 2 theory broken to N = 1 by an adjoint mass "is confining and its effective Lagrangian is a spontaneously broken
U(1)^{N-1} abelian gauge theory". Grade: exact holomorphic data (Seiberg-Witten curve, itself not a theorem of a
constructed QFT) plus EFT; BEL as a statement about a QFT. SU(N), 4D, continuum, with matter. Selective at small
breaking (monopole condensation gaps the photons). Confinement only near the N = 2 point; the decoupling of the
adjoint (mass to infinity) to pure YM is not controlled.

**G2. Alvarez-Gaume, Distler, Kounnas, Marino, IJMPA 11 (1996) 4745, arXiv:hep-th/9604004.** Soft breaking of N = 2
via spurions "preserving the analyticity properties of the Seiberg-Witten solution"; exact effective potential for
small breaking; "If we extrapolate the results to the limit where supersymmetry decouples, we obtain hints".
Grade SC/EFT for small breaking, BEL for the pure-YM limit. SU(2) (and with flavours). Selective at small breaking.

**G3. Murayama, PRL 126 (2021) 251601, arXiv:2104.01179.** Anomaly-mediated SUSY breaking of SQCD; dynamics exact for
m << Lambda; "there may be a phase transition as m is increased beyond Lambda ... suggest that two limits m << Lambda
and m >> Lambda may be in the same universality class." Grade: exact within SUSY + AMSB perturbation theory in m/Lambda
(not a constructed QFT); BEL for m >> Lambda. Massless quarks (not pure YM); pure-YM analogue (SYM + AMSB gaugino mass)
is the same structure. Selective at small m.

**G4. Cordova and Dumitrescu, SciPost Phys. 16, 139 (2024), arXiv:1806.09592.** SU(2) adjoint QCD (two Weyl flavours)
from N = 2 SYM with a SUSY-breaking scalar mass M; small M gives "an exotic Coulomb phase without chiral symmetry
breaking". Grade SC/EFT. SU(2), 4D. Negative lesson for the lane: **a soft deformation of the gapped (confining)
N = 2 -> N = 1 picture can land in a phase with massless photons**; which phase the decoupling limit reaches is not
fixed by continuity. This is a direct case where the frame change gives a massless factor.

**G5. Bergner and Piemonte, arXiv:1410.3668 (A10) and Poppitz-Schafer-Unsal (A4).** Soft gluino mass in N = 1 SYM:
SC near m = 0, NUM on the lattice; the line of transitions in the (m, L) plane meets L = 1/T_c at m = infinity.

**Step 2 summary.** No rigorous (LT or CT) statement exists in topic A or G. The calculable ends are semiclassical:
small S^1 with a double-trace deformation or adjoint fermions (A1-A5, A12), small T^2 with 't Hooft flux (A6, A7), and
soft breaking near a SUSY point (G1-G4). Every one is selective at its calculable end, in kind. Every continuity
statement to undeformed 4D YM on R^4 is a belief or conjecture (A1, A2, A6 explicitly). Published negative evidence:
pure YM on R^3 x S^1 without deformation has the thermal transition (A4); trace deformation has a first-order
reconfinement line (A9); adjoint QCD at finite mass has intermediate centre-broken phases (A11); a soft deformation of
N = 2 can land in a Coulomb phase with massless photons (G4). So a proof that carries the gap along such a path
must exclude a transition, and nothing published even states a criterion for doing so beyond "no order parameter".
The undeformed twisted thin torus (A6) is the only path that changes the geometry alone, not the action; the lane
already attacks it (Route T, rows 678, 842, 862). Primary-text reads: Step 2b.

### Step 2b: primary text, Unsal-Yaffe arXiv:0803.0344v2 (29 pp., read in parts)

Read from the arXiv PDF in `/tmp/gor1005/uy` (not committed). Passages, short quotes:
- Introduction, item iii): "When N Lambda L << 1 limit, the deformed Yang-Mills theory is solvable in the same sense
  as the Polyakov model. The existence of a mass gap and linear confinement can be shown analytically." The same
  passage says the "Higgs" description "is a perturbative gauge dependent description with no well-defined invariant
  content."
- Item iv): "There exist no order parameters which can distinguish the N Lambda L << 1 'Higgs' regime from the
  N Lambda L >> 1 regime."
- Section 3.1 "Mass gap": the dual-photon potential from monopole-instantons gives
  m_gamma^2 = (2 pi)^2 g^{-2} L^{-1} zeta, of order m_W^2 (2 pi/(g^2 N))^3 e^{-Delta S} e^{-8 pi^2/(N g^2(m_W))} (eq. (3.31)).
  The monopole measure is adapted from SYM (footnote 19); determinants are Pauli-Villars regularised.
- Conclusion: "These two regimes are expected to be smoothly connected — no physical order parameter sharply
  distinguishes the two regimes."

Grade confirmed: SC for the gap at small L (dilute-gas computation, one-loop prefactors, no error bounds); BEL for
continuity ("expected"). The argument for continuity is the absence of an order parameter; this does not exclude a
first-order transition or a critical point without symmetry change (A9 shows a first-order line in the deformation).
Selective at small L: the photon mass is exponentially small but positive and comes from non-abelian monopoles
(the Wilson line as a compact adjoint Higgs). A theory times a free photon keeps a massless photon here.

## Step 3: topic B (3D compact U(1) gap of Gopfert-Mack, and 4D-to-3D reductions)

Sources: Springer landing page of CMP 82 (abstract; full text paywalled, stopped there per FINISH rules), arXiv API
abstracts in `/tmp/gor1005/b` (not committed).

**B1. Gopfert and Mack, "Proof of confinement of static quarks in 3-dimensional U(1) lattice gauge theory for all
values of the coupling constant", CMP 82 (1981/82) 545-606, DOI 10.1007/BF01961240.** Full abstract (new to the lane,
which had the title and a summary): Villain action, "related to the 3-dimensional Z-ferromagnet by an exact duality
transformation (and also to a Coulomb system). We show that its string tension alpha is nonzero for all values of the
coupling constant g^2, and obeys a bound alpha >= const m_D beta^{-1} for small a g^2, with beta = 4 pi^2/g^2 and
m_D^2 = (2 beta/a^3) e^{-beta v_Cb(0)/2}. A continuum limit a -> 0, m_D fixed, exists and represents a scalar free
field theory of mass m_D. The string tension alpha m^{-2} in physical units tends to infinity in this limit."
Grade LT (theorem on the lattice, all couplings), plus a continuum limit that is a FREE massive scalar. Group/dim:
U(1), d = 3, Villain. Selective: yes, and sharply: the 3D photon becomes massive through the monopole (Debye) gas.
Reading for the lane: (i) the mechanism is the exact abelian duality to an integer-valued field plus a Coulomb gas;
(ii) the continuum limit at fixed m_D is Gaussian, so the theorem does not by itself give an interacting theory;
(iii) the mechanism needs magnetic monopoles to be point-like instantons in d = 3; in d = 4 they are loops and the
same argument fails (4D U(1) has a Coulomb phase, Guth, Frohlich-Spencer, on file in `gap-lit-u1.md`).

**B2. Chatterjee, arXiv:2602.00436 (on file, `gap-crux-lit-nonab.md` L147).** 3D Wilson LGT with G contained in U(n)
and containing the scalar circle: |<W_l>| <= n exp{-c (1 + n beta)^{-1} T log(R + 1)} (logarithmic potential, via
Frohlich's comparison and Glimm-Jaffe). Grade LT. d = 3, groups with a central U(1) (so not SU(2)). Selective only
in the weak sense of a growing potential; no gap statement.

**B3. Garban and Sepulveda, arXiv:2107.04021 (new to the lane).** 4D U(1) Villain at low temperature:
|<W_gamma>| <= exp(-(C_GFF/(2 beta))(1 + C beta e^{-2 pi^2 beta})(|gamma| + o(|gamma|))), a perimeter law with the
monopole correction quantified. Grade LT. d = 4, U(1). It confirms the 4D Coulomb phase quantitatively; it shows the
GM mechanism does not carry to d = 4 in the bulk.

**B4. Chevyrev and Garban, "Villain action in lattice gauge theory", J. Stat. Phys. 192 (2025) 38, arXiv:2404.09928
(new to the lane).** Villain interaction is a limit of Wilson and Manton interactions on a larger "carpet graph",
"our proof also applies to non-Abelian lattice theories". Grade LT. Relevance: a rigorous bridge between Villain and
Wilson actions, so a GM-type Villain statement need not be lost when the action changes; it does not move the
mechanism to SU(2).

**B5. Athenodorou, Bonati, Soler Calero, arXiv:2608.27976 (2026, new).** 3D compact U(1): "its continuum limit is
pathological, since the ratio of the glueball masses to the square root of the string tension vanishes"; a monopole
fugacity term gives a line of constant physics. Grade NUM. Confirms B1 (ii).

**B6. 4D-to-3D reductions that would carry B1 to a 4D theory on R^3 x S^1.**
- The semiclassical carriers are A1, A3, A4, A12 of Step 2: at small L, SU(2) YM with a centre-stabilising deformation
  or adjoint fermions reduces to a 3D compact abelian theory (dual photon) with monopole-instantons; this is the
  continuum Polyakov mechanism that B1 makes rigorous in the Villain lattice model. Grade SC; nothing rigorous found.
- Dimensional reduction at high temperature (Laine, PLB 385 (1996) 249, hep-lat/9604011, SU(2)+Higgs): "the lack of a
  relation of the 4d lattice gauge coupling to continuum physics prevent rigorous conclusions." Grade NUM/perturbative.
- Rigorous treatment of the 3D Georgi-Glashow (SU(2) + adjoint Higgs) lattice model in the Polyakov regime: NONE
  FOUND in this search (arXiv API queries for "Polyakov ... monopole ... mass gap ... proof", "Georgi-Glashow AND
  rigorous" returned nothing). I recall none; this is a bounded search, not a non-existence claim.
- 3D SU(2) itself: no gap theorem outside strong coupling (on file, `gap-3dmix-read-opus.md` L282).
- Debye screening rigorous in other models (new, for completeness): D'Alimonte and Lammers, arXiv:2603.28734
  (2D lattice Coulomb gas, free-energy analyticity and Debye screening in the disordered regime). Grade LT, 2D.
  Chernodub, Ishiguro, Suzuki, PTP 112 (2004) 1033 (3D SU(2) abelian-projected monopole gas, NUM).

**Step 3 summary.** B1 is the one rigorous, all-coupling, selective gap theorem in this family, and it is abelian and
three-dimensional with a Gaussian continuum limit. No published rigorous step carries it to a 4D non-abelian theory:
the carrier (small-L abelianisation of deformed or adjoint-matter SU(2) on R^3 x S^1) is semiclassical, and even the
3D non-abelian Georgi-Glashow model has no rigorous Polyakov theorem that I found. In 4D bulk U(1) the mechanism
fails (B3). For the lane this matches row 1002 H17 and adds the exact abstract bound (m_D formula, free-field limit).

## Step 4: topic C (YM on S^3 and on hyperbolic space; small-radius gap and continuity in the radius)

Sources: arXiv abstracts in `/tmp/gor1005/c`; primary text of van Baal's review in `/tmp/gor1005/vb` (not committed).

**C1. van Baal, "QCD in a Finite Volume", hep-ph/0008206 (review, 79 pp.), Section 5 "Gauge Fields on the
three-Sphere" read in full (pp. 51-58 of the PDF) and Section 6 opening.** Statements:
- Purpose: "conformal equivalence of S3 x R to R4 gives a very simple and explicit construction for the instantons";
  theta dependence via boundary conditions on the fundamental domain.
- The free spectrum: the quadratic fluctuation operator in Coulomb gauge, M_ij = 2 L_1^2 delta_ij + 2 (L_1 + S)^2_ij,
  "has A(c, d) as its eigenspace for the (lowest) eigenvalue 4. These modes are consequently the equivalent of the
  zero-momentum modes on the torus, with the difference that their zero-point frequency does not vanish." So on a
  unit S^3 the free gluon already has frequency 2/R: the gap at small R is curvature, present in a free photon too.
- The method: an 18-dimensional (c, d) mode space, sphalerons, Gribov and fundamental-domain boundary identifications;
  effective Hamiltonian with variational solution. "Due to the curvature of the sphere, at large volumes the
  corrections to the glueball masses are in powers of the inverse radius, as opposed to an exponential approach for
  the torus."
- Section 6: SU(2) spectra "for the sphere and the torus, are compatible with m(2+)/m(0+) ~ 1.5 and
  m(0-)/m(0+) ~ 1.7" near the domain size; "The volume plays the role of the control parameter"; "large field
  fluctuations are essential".
Grade: perturbative + effective Hamiltonian on a finite mode space + variational numerics (SC/NUM); no theorem.
SU(2), S^3 x R. Selective: NO at small radius (every theory, including a free photon, has a gap of order 1/R on
S^3; for Maxwell on the unit S^3 the lowest coexact 1-form has omega = 2, the same value as the free gluon modes
above). The selective content would be a lower bound on the gap uniform in R, which is the original problem.
- References located in the review (abstract-level only, not read): Hosotani, PLB 147 (1984) 44; van Baal and
  Hari Dass, NPB 385 (1992) 185; van Baal and van den Heuvel, NPB 417 (1994) 215, hep-lat/9310005; Cutkosky,
  J. Math. Phys. 25 (1984) 939, and Cutkosky-Wang PRD 37 (1988) 3024; van Baal-Cutkosky hep-lat/9208027.

**C2. Aharony, Marsano, Minwalla, Papadodimas, Van Raamsdonk, ATMP 8 (2004) 603, hep-th/0310285.** "weakly coupled,
large N, d-dimensional SU(N) gauge theories on a class of compact spatial manifolds (including S^{d-1} x time)
undergo deconfinement phase transitions at temperatures proportional to the inverse length scale"; the analysis
reduces to a unitary-matrix integral over the thermal holonomy. Grade: exact at zero coupling and perturbative at
weak coupling, large N (a mathematical statement about the matrix integral is rigorous; the QFT reading is
perturbative). Selective: NO; the "confined" low-temperature phase at zero coupling comes from the Gauss law
(singlet constraint) on a compact space, which a free theory with the constraint also has. Lesson for the lane:
confinement-like behaviour on a compact space can be kinematic.

**C3. Hyperbolic space and AdS_4.**
- Aharony, Berkooz, Tong, Yankielowicz, "Confinement in Anti-de Sitter Space", JHEP 02 (2013) 076, arXiv:1210.5195:
  "Four dimensional gauge theories in anti-de Sitter space, including pure Yang-Mills theory, exhibit a quantum phase
  transition between a deconfined phase and a confined phase as the gauge coupling is varied." Grade SC/BEL.
- Ciccone, De Cesare, Di Pietro, Serone, arXiv:2407.06268: "The Dirichlet boundary condition cannot exist at
  arbitrarily large radius because it would give rise to colored asymptotic states in flat space. ... this implies a
  deconfinement-confinement transition as the radius is increased"; one-loop anomalous dimensions favour
  "merger and annihilation"; "For the Neumann boundary condition, the lightest scalar operator is found to have a
  positive anomalous dimension, in agreement with the idea that this boundary condition extrapolates smoothly to
  flat space." Grade: perturbative (one loop) plus an argument; BEL for the transition and for Neumann smoothness.
  SU(N), Euclidean AdS_4 = H^4. Selective: partly. In global AdS every field has a discrete spectrum of order 1/R,
  so a gap is NOT selective; what is selective is the boundary data (a conserved boundary current of colour under
  Dirichlet conditions, or the Neumann spectrum). Continuity in the radius is a stated belief for Neumann and is
  stated to FAIL for Dirichlet.
- Lawrie, Oh, Shahshahani, arXiv:1502.00697: classical equivariant SU(2) YM on 4D hyperbolic space (gap eigenvalues
  of a linearised operator for the wave equation). Grade CT, classical only, no quantum statement.
- Callan and Wilczek, "Infrared behavior at negative curvature", NPB 340 (1990) 366 (recalled, not fetched; not on
  arXiv): hyperbolic space as an infrared regulator. Status in this search: NOT READ.
- Spectral fact used above (recalled, standard, not rebuilt; label gap): on H^n the Hodge Laplacian on k-forms has
  essential spectrum starting at ((n-1)/2 - k)^2 for k < (n-1)/2, and L^2 harmonic forms exist only in middle degree
  k = n/2. For H^4 this gives L^2 harmonic 2-forms (abelian field strengths with zero action cost scale), so a free
  photon on H^4 is not gapped in any flat-space sense.

**C4. Rigorous constructions.** No rigorous construction of 4D YM on S^3 x R or on H^4 was found. On file: Alonso
Pichardo, Zenodo preprints 2026 (`gap-crux-lit-2.md` L170-172), not refereed. Rigorous Euclidean QFT on curved
backgrounds exists for scalar fields (Jaffe-Ritter, CMP 270 (2007), and Dimock, recalled, NOT READ in this run); none
for gauge fields in 4D.

**Step 4 summary.** The small-radius gap on S^3 (and on AdS_4/H^4) is curvature or kinematics and is NOT selective:
a free photon has it too. Continuity in the radius is the uniform-in-R lower bound, which is the original problem in
another geometry; the literature treats it by effective Hamiltonians and variational numerics (van Baal) or by
one-loop boundary data (AdS), and states a transition for Dirichlet conditions. Nothing rigorous. The AdS boundary
data (colour currents under Dirichlet conditions) is the only selective handle found in this topic; it is perturbative.

## Step 5: topic D (twisted boundary conditions and flux free energies), additions only

The lane already holds the core of this topic (Step 1, D): 't Hooft 1979, Tomboulis-Yaffe, Borgs-Seiler, Mack-Petkova
(31 files), Kanazawa (theorem and identity, arXiv:0805.2742), Chatterjee centre symmetry, Ito-Seiler and the
Tomboulis 2007 failure point (row 797), Kovacs-Tomboulis numerics, Nguyen-Tanizaki-Unsal Appendix A, de Forcrand-Jahn.
I did not re-search them. arXiv search (sorted by date) for new rigorous items found these, new to the lane:

**D1. Edwards and von Smekal, PLB 681 (2009) 484, arXiv:0908.4030; von Smekal, Edwards, Strodthoff, PoS
Lattice2010:292, arXiv:1012.0408.** 3D SU(2) (2+1 at finite temperature): the centre-vortex free energy at the
deconfinement point is matched to "the exactly known value of the interface free energy in the 2D Ising model at
criticality" to fix beta_c. Grade NUM, with an exact 2D Ising input via universality (the universality step is
BEL). 3D SU(2). Selective: the vortex free energy is a confinement order parameter, so yes in kind (it is the flux
quantity the lane already uses, Theorem ZD-c and (W)). Adds nothing rigorous.

**D2. Goller and Porta, arXiv:2501.10065, and Bachmann, Goller, Porta, arXiv:2508.21502.** 2D (2+1 Hamiltonian)
Z_2 gauge theory coupled to fermions: "Using reflection positivity, we prove that the ground state lies in the sector
of a uniform pi-flux per plaquette and that the monopoles are massive"; with a staggered fermion mass, "a fully gapped,
four-dimensional ground state space on large tori. It is topologically ordered." Proof by "reflection positivity and
chessboard estimates". Grade LT (Hamiltonian lattice theorem). Group Z_2, d = 2 + 1, with matter, at large hopping.
Selective: yes (gapped vs the semimetal they also prove without the mass). Relevance: the only recent rigorous use I
found of reflection positivity to fix the flux sector of a lattice gauge theory and then get a gap; the flux is
fixed by fermions at large hopping (Lieb's flux-phase theorem), not by pure gauge dynamics, and the group is finite.
It is a precedent for "RP fixes the flux sector", which the lane's twist work (rows 679, 842) already uses through
chessboard estimates (Theorem BAD).

**D3. Nothing new and rigorous on 4D SU(2) twist free energies.** Kanazawa's theorem (arXiv:0805.2742, on file:
"An equality is derived through" a blocking of vortex free energies across lattice sizes) remains the latest
rigorous all-coupling identity found. Tomboulis's 2007 claim (arXiv:0707.2179) is on file with its failure point.
SO(3)-type and vortex-model papers (Burgio et al. hep-th/0608075, hep-lat/0610097; Quandt-Reinhardt-Engelhardt
hep-lat/0412033) are NUM or models.

**Step 5 summary.** No new rigorous inequality on 4D SU(2) flux free energies since the lane's last search (row 739,
2026-11-11). The new rigorous items are Hamiltonian Z_2 + fermion theorems in 2 + 1 dimensions (D2) that use
reflection positivity to fix the flux sector; they are a technique precedent, not an input.

## Step 6a: topic E (gap stability along paths of local Hamiltonians, and its use for lattice gauge theories)

Sources: arXiv abstracts in `/tmp/gor1005/e` (not committed). Lane holdings: Step 1, E; Knabe and Gosset-Mozgunov
finite-size criteria are on file (16 and 11 files, e.g. `gap-crux-fp.md`, `prior/gap-math-lit.md`), Cubitt et al. too
(`gap-crux-exercise-astra.md`). New items are marked NEW.

**E1. Bravyi, Hastings, Michalakis, J. Math. Phys. 51 (2010) 093512, arXiv:1001.0344 (on file, re-read abstract).**
For H_0 a sum of "geometrically local commuting projectors on a D-dimensional lattice with certain topological order
conditions", "there exists a constant threshold epsilon > 0 such that for any perturbation V representable as a sum of
short-range bounded-norm interactions the perturbed Hamiltonian H = H_0 + epsilon V has well-defined spectral bands
... separated ... by a constant gap." Grade: theorem (quantum lattice, finite-dimensional sites). Selective: yes
(a gap is a gap), but only near a frustration-free commuting-projector point.

**E2. Michalakis and Pytel, CMP 322 (2013) 277, arXiv:1109.1588 (NEW to the lane; I take this to be the row's
"Michalakis and Zwolak": Justyna Pytel publishes later as Justyna P. Zwolak; the identification is mine, not
checked against a source).** "We prove stability of the spectral gap for gapped, frustration-free Hamiltonians under
general, quasi-local perturbations. We present a necessary and sufficient condition for stability, which we call
'Local Topological Quantum Order'". Grade: theorem. Needs: frustration-free H_0 with a uniform gap and LTQO;
perturbation small in norm. Finite-dimensional sites.

**E3. Nachtergaele, Sims, Young, arXiv:2102.07209 (NEW).** "uniformly small short-range perturbations do not close the
bulk gap above the ground state of frustration-free quantum spin systems that satisfy a standard local topological
quantum order condition. In contrast with earlier results, we do not require a positive lower bound for finite-system
Hamiltonians uniform in the system size." Grade: theorem (infinite-system GNS form). Same smallness and frustration-free
hypotheses.

**E4. Nachtergaele, Sims, Young, J. Math. Phys. 60 (2019) 061101, arXiv:1810.02428 (NEW).** Review/framework of
Lieb-Robinson bounds, quasi-local maps and spectral-flow automorphisms, including "systems with an infinite-dimensional
Hilbert space at each lattice site and Hamiltonians that may involve unbounded on-site contributions" (the Kogut-Susskind
electric term is such an on-site term). Grade: theorems. Relevance: the technical frame needed to even state E1-E3 for
a lattice gauge Hamiltonian with L^2(SU(2)) on each link exists in this generality for propagation bounds; the
stability theorems themselves are proved for finite-dimensional sites.

**E5. Bachmann, Michalakis, Nachtergaele, Sims, "Automorphic Equivalence within Gapped Phases", CMP 309 (2012) 835,
arXiv:1102.0842 (NEW).** If H(s), s in [0, 1], has finite-range interactions continuous in s and "a non-vanishing gap
above its ground state" for each s, then the ground states are related by a quasi-local automorphism (Hastings'
quasi-adiabatic flow). Grade: theorem. Direction: gap along the path => equivalence; it does NOT give a gap. Selective:
it presupposes the gap, so it cannot supply one.

**E6. Lemm and Mozgunov, arXiv:1801.08915 (NEW; Knabe and Gosset-Mozgunov on file).** Finite-size criterion for
frustration-free systems with boundary: "if the spectral gaps at linear system size n exceed an explicit threshold of
order n^{-3/2}, then the whole system is gapped" (1D and 2D, finite-range). Grade: theorem. Selective: yes. Needs
frustration-freeness; pure lattice YM (Kogut-Susskind) is not frustration-free.

**E7. Cubitt, Perez-Garcia, Wolf, Forum Math. Pi 10 (2022) e14, arXiv:1502.04573; Bausch, Cubitt, Lucia,
Perez-Garcia, PRX 10 (2020) 031038, arXiv:1810.01858 (on file).** The spectral gap problem is undecidable for
translation-invariant nearest-neighbour Hamiltonians in 2D (and 1D). Grade: theorem. It names the YM gap conjecture as
an instance of the general problem but does not bear on a specific Hamiltonian; it rules out a uniform algorithm, not a
proof for SU(2).

**E8. Use for lattice gauge theories.** The lane's own record (`prior/gap-prior.md` L101, L209): a note in this
repository imports E1 for link-truncated SU(2)/SU(3) Kogut-Susskind Hamiltonians at strong coupling (H(delta) =
sum n_l + delta sum O_P), i.e. a perturbation of the frustration-free electric term. arXiv search for "lattice gauge AND
spectral gap AND stability AND Hamiltonian" returned nothing; "Kogut-Susskind AND gap" returned only tensor-network and
MPS numerics (Tagliacozzo-Celi-Lewenstein PRX 4 (2014) 041024; Milsted PRD 93 (2016) 085012, NUM). Topic D2 above
(Goller-Porta; Bachmann-Goller-Porta) is the only recent rigorous gapped-phase result for a lattice gauge theory found,
and it uses reflection positivity, not E1-E3. Not found: any gap-stability theorem for a lattice gauge Hamiltonian away
from the strong-coupling (electric) point.

**Step 6a summary.** Every gap-stability theorem (E1-E3, E6) needs a frustration-free gapped reference point and a
perturbation small in norm (or a finite-size gap above an explicit threshold for frustration-free systems). For lattice
YM the only such point is strong coupling (the electric term), so the method reaches small magnetic perturbations only,
as `gap-brainstorm-max.md` G15 already says. E5 transports equivalence along a path that is already gapped and cannot
open a gap. Nothing here reaches order-one coupling.

## Step 6b: topic F (gradient flow and stochastic quantisation as monotones)

Sources: arXiv abstracts in `/tmp/gor1005/f` (not committed). On file (Step 1, F): Shen-Zhu-Zhu 2204.12737 and
2401.13299, Chandra-Chevyrev-Hairer-Shen 2D YM and 3D YMH, Chevyrev 2202.13359, Chevyrev-Shen, Piazza-Shen 2D,
Mondal; Luscher's Wilson flow appears in `gap-brainstorm-max.md`, `gap-skeleton-max.md`, `gap-vacsub-max.md` and
`prior/gap-lit-transport.md`. New items marked NEW.

**F1. Luscher, "Properties and uses of the Wilson flow in lattice QCD", JHEP 1008:071, arXiv:1006.4518.**
"the gauge field obtained at flow time t > 0 is a smooth renormalized field"; observables at flow time t "probe the
theory at length scales on the order of sqrt(t)"; topological sectors "rapidly separate" as the lattice spacing goes
to zero. Grade: the flow equation and its per-configuration monotonicity are exact (the Wilson action decreases along
its own gradient flow, d/dt S_W(V_t) = -|grad S_W(V_t)|^2 <= 0, recalled, elementary, not rebuilt; label gap until
written); the field-theory claims are perturbative and NUM. SU(3) (any group). Selective: the per-configuration
monotone is NOT selective (any gauge action decreases along its own gradient flow, the U(1) action included). The
derived coupling g_GF^2(t) proportional to t^2 <E(t)> is a running coupling; its growth with t is a (K-flow) quantity
of the type row 1002 already records (step scaling, H16 there).

**F2. Luscher and Weisz, JHEP 1102:051, arXiv:1101.0963 (NEW).** "For any matter multiplet and to all loop orders, we
show that the correlation functions are finite, i.e. do not require additional renormalization". Grade: theorem in
renormalised perturbation theory (all orders), not non-perturbative. 4D, any gauge group. Not selective.

**F3. Gradient flow as an RG (NEW).** Sonoda and Suzuki, PTEP (2019), arXiv:1901.05169: "a concrete correspondence
between a gradient flow and the renormalization group flow for a generic scalar field theory" with "a particular
choice of the cutoff function" (exact RG). Abe and Fukuma, PTEP (2018), arXiv:1805.12094: effective action along the
flow, local potential approximation. Carosso, Hasenfratz, Neil, PRL 121 (2018) 201601, arXiv:1806.01385: a continuous
real-space RG built on gradient flow, used numerically for SU(3) with N_f = 12. Grades: formal correspondence (scalar
theory, exact-RG level), approximation (LPA), NUM. Not selective; none states a monotone.

**F4. Waldron, "Long-time existence for Yang-Mills flow", Invent. Math. 217 (2019) 1069, arXiv:1610.03424 (NEW).**
"finite-time singularities do not occur in four-dimensional Yang-Mills flow, confirming the conjecture of Schlatter,
Struwe, and Tahvildar-Zadeh." Grade CT (classical PDE). 4D, compact group. Relevance: the classical YM heat flow is
globally defined in 4D (for smooth data), so a flow-time frame is well posed classically; it is a statement about the
classical flow, not about the measure, and it is not selective.

**F5. Stochastic quantisation (on file, re-read abstracts).** Shen, Zhu, Zhu, arXiv:2204.12737: Langevin dynamics,
"ergodicity, functional inequalities, large N limits, and mass gap" assuming |beta| < 1/(16(d - 1)) for SU(N) (strong
coupling, any d). Shen, Zhu, Zhu, arXiv:2401.13299: same for lattice Yang-Mills-Higgs in a strong-coupling region of
(beta, kappa). Chevyrev, J. Math. Phys. 63 (2022), arXiv:2202.13359: review of 2D and 3D stochastic YM heat flow,
renormalised to be "gauge covariant in law", with a state space of distributional 1-forms. Grades LT (strong coupling)
and CT (local-in-time solution theory in 2D/3D). Selective at strong coupling (a mass gap). Not in 4D; not at order-one
coupling. The Langevin generator's spectral gap at weak coupling is not known for any non-abelian lattice gauge theory
in d >= 3 (bounded search, consistent with `prior/gap-3dmix-read-opus.md` L282).

**F6. Monotones along the flow in the quantum theory.** No published monotone of a gradient-flow quantity in the
quantum measure (e.g. t^2 <E(t)> increasing in t) was found, rigorous or numerical-with-claim. Recalled, not rebuilt
(label gap): for a free massless photon, scale invariance makes t^2 <E(t)> independent of t at large t, so any
selective flow-time statement must be a growth statement about t^2 <E(t)>, the same kind of (K-flow) input that row
1002 found nowhere.

**Step 6b summary.** Gradient flow gives a well-posed classical frame (F4) and a renormalised probe (F1, F2), and
stochastic quantisation gives gaps at strong coupling (F5). The only monotone is per configuration and blind. Nothing
reaches order-one coupling in 4D or gives a selective monotone.

## Step 7: synthesis

### 7.1 Sussman-Alpoge account

Credit: Ethan Sussman and Levent Alpoge (text authored with Claude and Codex), `YM4_sketch_500.tex` at `31a47c543775`,
read through the lane's full-read index `library/sa-index/` (row 244). Grep of the index for every topic of this row:
adiabatic continuity, Unsal, centre-stabilised, S^3, hyperbolic space, supersymmetry, Gopfert-Mack, Polyakov,
Bravyi/Hastings/Michalakis: 0 hits. "Wilson flow": 1 hit (chunk-15 L78, an own-counterterm ledger that "transfers its
coefficient to Wilson flow", the bare action's flow, not the gradient flow). "twist": 15 hits in 7 chunks, all
background adjoint twists of the covariance (chunk-07 L29, L70, L147; chunk-08 L80; 4.12 refined minimiser), not 't
Hooft flux. So the account uses none of these frame changes; it states no mass gap (GOAL.md, T0). Row 992 already
read their 3D supplement (YM3_supplement Sketch C-361-3: a 3D finite-size criterion with an open seed). A direct read of
their repository tree through `gh api` was attempted in this run and the tool call was denied; I did not retry it.

### 7.2 Table (one row per source; Grade: LT lattice theorem, CT continuum theorem, PT perturbative theorem,
SC semiclassical, NUM numerical, BEL belief/conjecture; Sel = would tell a gapped theory from one with a massless
factor)

| # | Source | Statement (short) | Grade | Group, dim | Sel |
|---|---|---|---|---|---|
| A1 | Unsal-Yaffe 0803.0344 | deformed YM on R^3 x small S^1: gap, linear confinement; continuity "expected" | SC; BEL | SU(N), 4D deformed | yes at small L |
| A2 | Shifman-Unsal 0802.1232 | QCD-like, one fermion, double trace: confinement, chi SB at small r; continuity argued | SC; BEL | SU(N), 4D + matter | yes at small r |
| A3 | Unsal 0708.1772 | SU(2) QCD(adj) small S^1: gap, area law; a chiral transition must occur | SC | SU(2), 4D + adj | yes; continuity fails for chiral data |
| A4 | Poppitz-Schafer-Unsal 1205.0290 | (m, L) plane: line of centre transitions; pure YM end = thermal transition | SC; BEL | SU(2), 4D + adj Weyl | yes; undeformed continuity FAILS |
| A5 | PSU 1212.1238 | same mechanism all simple groups | SC | all simple | yes |
| A6 | Tanizaki-Unsal 2201.06166 | small T^2 with 't Hooft flux: centre-vortex confinement; continuity conjectured | SC; BEL | SU(N), 4D undeformed | yes at small T^2 |
| A7 | Guvendik-Schaefer-Unsal 2405.13696 | monopole regime and vortex regime connected inside the EFT | SC | SU(N), 4D | yes (weak coupling only) |
| A8 | Dobozy-Poppitz 2606.22078 | classical fractional-charge saddles across R^{4-k} x T^k | NUM (classical) | SU(N), 4D | no |
| A9 | Bonati et al. 1807.06558, 2012.13246; Vairinhos 1111.0303 | trace-deformed lattice YM; reconfinement first order | NUM | SU(3), SU(2) 3D | in kind; shows a transition |
| A10 | Bergner-Piemonte 1410.3668 | lattice SYM + soft mass: deconfined region shrinks to none at small mass | NUM | SU(2), 4D | in kind |
| A11 | Cossu-D'Elia 0904.1353 | adjoint QCD: four phases in L_c | NUM | SU(3), 4D + adj | continuity fails |
| A12 | Poppitz 2111.10423 | review; bions need analytic continuation | SC | SU(2) | yes at small L |
| B1 | Gopfert-Mack CMP 82 | string tension > 0 all g; alpha >= c m_D/beta; continuum = free scalar of mass m_D | LT | U(1) Villain, 3D | YES |
| B2 | Chatterjee 2602.00436 | log potential for G with central U(1) | LT | U(n)-type, 3D | weak |
| B3 | Garban-Sepulveda 2107.04021 | perimeter law with monopole correction | LT | U(1) Villain, 4D | shows 4D U(1) massless |
| B4 | Chevyrev-Garban 2404.09928 | Villain = limit of Wilson/Manton on carpet graph, non-abelian too | LT | any compact, any d | n/a (bridge) |
| B5 | Athenodorou-Bonati-Soler Calero 2608.27976 | 3D U(1) continuum limit pathological; monopole fugacity fix | NUM | U(1), 3D | in kind |
| B6 | Laine hep-lat/9604011 | 4D vs 3D reduced theory "prevent rigorous conclusions" | NUM | SU(2)+Higgs | n/a |
| C1 | van Baal hep-ph/0008206 Sec. 5-6 | S^3: lowest free mode eigenvalue 4 (omega = 2/R); effective Hamiltonian spectra | PT/SC/NUM | SU(2), S^3 x R | NO (curvature gap) |
| C2 | Aharony et al. hep-th/0310285 | weak-coupling large-N YM on S^3: Hagedorn/deconfinement transition | exact at g = 0; PT | SU(N), S^3 | NO (Gauss-law kinematics) |
| C3 | Aharony-Berkooz-Tong-Yankielowicz 1210.5195; Ciccone et al. 2407.06268 | AdS_4: Dirichlet b.c. must have a transition in the radius; Neumann believed smooth | PT (1 loop); BEL | SU(N), AdS_4 = H^4 | gap no; boundary data partly |
| C4 | Lawrie-Oh-Shahshahani 1502.00697 | classical equivariant YM on H^4 | CT classical | SU(2), H^4 | no |
| D1 | Edwards-von Smekal 0908.4030; 1012.0408 | vortex free energy matched to 2D Ising interface at T_c | NUM + BEL | SU(2), 3D | in kind |
| D2 | Goller-Porta 2501.10065; Bachmann-Goller-Porta 2508.21502 | RP + chessboard fix pi-flux; massive monopoles; gapped, topological | LT (Hamiltonian) | Z_2 + fermions, 2+1 | yes |
| E1 | Bravyi-Hastings-Michalakis 1001.0344 | gap stable under small local perturbations of commuting-projector TQO | theorem | spins, any D | yes, near FF point only |
| E2 | Michalakis-Pytel (Zwolak) 1109.1588 | same for frustration-free with LTQO | theorem | spins | yes, small perturbation |
| E3 | Nachtergaele-Sims-Young 2102.07209 | bulk-gap stability, no uniform finite-volume gap needed | theorem | spins | yes, small perturbation |
| E4 | NSY 1810.02428 | LR bounds and spectral flow incl. unbounded on-site terms | theorem | quantum lattice | n/a (frame) |
| E5 | Bachmann-Michalakis-Nachtergaele-Sims 1102.0842 | gapped path => automorphic equivalence | theorem | spins | presupposes gap |
| E6 | Lemm-Mozgunov 1801.08915 | finite-size gap > c n^{-3/2} => gapped (FF, boundary) | theorem | spins 1D/2D | yes, FF only |
| E7 | Cubitt-Perez-Garcia-Wolf 1502.04573 | gap problem undecidable (2D, 1D) | theorem | spins | n/a |
| F1 | Luscher 1006.4518 | Wilson flow: smooth renormalised field; per-config action decreases | exact (classical) + PT/NUM | any | no |
| F2 | Luscher-Weisz 1101.0963 | flowed correlators finite to all orders | PT | any, 4D | no |
| F3 | Sonoda-Suzuki 1901.05169; Abe-Fukuma 1805.12094; Carosso-Hasenfratz-Neil 1806.01385 | flow as RG | formal / LPA / NUM | scalar; SU(3) | no |
| F4 | Waldron 1610.03424 | 4D YM heat flow: no finite-time singularity | CT classical | compact G, 4D | no |
| F5 | Shen-Zhu-Zhu 2204.12737, 2401.13299; Chevyrev 2202.13359 | Langevin: ergodicity, LSI, mass gap at strong coupling; 2D/3D SQ solution theory | LT (strong); CT (local) | SU(N), any d; 2D/3D | yes at strong coupling |
| G1 | Douglas-Shenker hep-th/9503163 | N = 2 -> N = 1: confining, broken U(1)^{N-1} EFT | exact holomorphy + EFT; BEL | SU(N), 4D + adj | yes near N = 2 |
| G2 | Alvarez-Gaume et al. hep-th/9604004 | soft N = 2 breaking, exact potential for small breaking; pure YM "hints" | SC/EFT; BEL | SU(2) | yes near N = 2 |
| G3 | Murayama 2104.01179 | SQCD + AMSB exact for m << Lambda; possible transition at m ~ Lambda | SC/EFT; BEL | SU(N_c) + quarks | yes at small m |
| G4 | Cordova-Dumitrescu 1806.09592 | N = 2 SYM + SUSY-breaking scalar mass: small M gives a Coulomb phase (massless photons) | SC/EFT | SU(2), 4D + 2 adj | shows a massless end |

### 7.3 Reading for row 1004 (no new claim; what the literature supports)

1. **Rigorous and selective:** B1 (3D U(1), all couplings), D2 (Z_2 + fermions in 2+1, by RP and chessboard), E1-E3,
   E6 (spin systems near a frustration-free point), F5 (strong coupling). None is 4D non-abelian at order-one coupling.
   Each has a named structural input absent from 4D SU(2) at beta ~ 2.3: abelian duality with point monopoles (B1),
   a finite group and fermion-fixed flux (D2), frustration-freeness and small perturbation (E), strong coupling (F5).
   This matches row 1002's filter: each rigorous crossing names a low-dimensional or special-structure input.
2. **Selective but semiclassical:** every calculable end of a frame change (A1-A7, A12, G1-G3) is selective in kind.
   Every continuity from that end to undeformed 4D YM on R^4 is a belief, stated as such by the authors (A1 "expected",
   A2 "we argue", A6 "We conjecture", G2 "hints", G3 "may be in the same universality class").
3. **Published counter-evidence to continuity:** pure YM on R^3 x S^1 has the thermal transition (A4); the trace
   deformation has a first-order reconfinement line (A9); adjoint QCD has intermediate centre-broken phases in L (A11);
   chiral data must jump in QCD(adj) (A3); a soft deformation of N = 2 SYM can end in a Coulomb phase with massless
   photons (G4); YM in AdS_4 with Dirichlet conditions must have a transition in the radius (C3). So a frame change
   that carries a gap back must exclude transitions by an argument stronger than "no order parameter".
4. **Non-selective frame changes:** S^3 and AdS_4/H^4 (C1-C3): the gap at small radius is curvature or Gauss-law
   kinematics and a free photon has it; uniformity in R is the original problem. Gradient flow (F1-F4): blind
   per-configuration monotone. Automorphic equivalence (E5): presupposes the gap.
5. **Nearest to the lane's own work:** the undeformed twisted thin torus (A6, A7) is the one frame change that alters
   only the geometry and keeps the Wilson action; the lane already attacks it as Route T (rows 678, 679, 842, 862) and
   records (AC') as the authors' conjecture (`gap-skeleton-final.md` L249). D2 is a technique precedent for the RP and
   chessboard steps the lane uses there (Theorem BAD, row 842).

## Step 8: what was not done, and the result

Provenance: Claude Opus 5.5, high effort, Mac mini worker 3, pinned at 95fecd964, one session, no subagents, no
numeric run (reading item; memory_pressure not needed), 2026-11-15 15:54Z to 2026-11-15T16:05Z. Checked by no one.

Not done or not read (each is a gap in this reading, not a finding):
- Gopfert-Mack full text: Springer paywall; only the full abstract was read. Stopped there per FINISH rules.
- Primary text read only for Unsal-Yaffe 0803.0344 (Step 2b) and van Baal hep-ph/0008206 Sections 5-6 (Step 4).
  All other entries are abstract level.
- Not located or not read: Callan-Wilczek NPB 340 (1990); Hosotani PLB 147 (1984); Cutkosky J. Math. Phys. 25 (1984);
  van Baal-van den Heuvel hep-lat/9310005; Jaffe-Ritter CMP 270 (2007); Dimock on curved backgrounds; journal
  reference of A4 (given from memory, marked).
- The Michalakis-Zwolak = Michalakis-Pytel identification (E2) is mine and not checked against a source.
- Direct read of the Sussman-Alpoge repository tree through `gh api` was denied by the tool permission; the lane's
  full-read index of YM4_sketch_500.tex was used instead (7.1).
- Spectral facts on S^3 and H^n and the free-photon behaviour of t^2 <E(t)> are recalled, not rebuilt (label gap).

RESULT: Row 1005 (literature reading on frame changes for the gap, 7 topics, about 45 sources, 2 primary texts;
no attack, no new claim; checked by no one): no published rigorous result carries a gap from a changed frame
(R^3 x S^1, R^2 x T^2 with 't Hooft flux, S^3, AdS_4/H^4, a soft-broken SUSY parent, a Hamiltonian path, a flow
time) to 4D SU(2) at order-one coupling. The rigorous selective results (Gopfert-Mack 3D U(1); Goller-Porta Z_2 +
fermions by reflection positivity; Bravyi-Hastings-Michalakis, Michalakis-Pytel, Nachtergaele-Sims-Young, Lemm-Mozgunov
near frustration-free points; Shen-Zhu-Zhu at strong coupling) each rest on an input that 4D SU(2) at beta ~ 2.3
lacks. Every calculable end (small S^1 deformed or with adjoints, small T^2 with flux, near-SUSY soft breaking) is
semiclassical and selective, and every continuity to R^4 is the authors' stated belief or conjecture; published
counter-evidence shows transitions on several such paths (thermal and reconfinement lines, centre-broken phases in
adjoint QCD, a Coulomb end of soft-broken N = 2, Dirichlet AdS_4). S^3 and AdS_4 gaps and gradient-flow monotones are
not selective. Open: everything; (AC') of Route T remains the authors' conjecture, and the sources listed above as not
read.
