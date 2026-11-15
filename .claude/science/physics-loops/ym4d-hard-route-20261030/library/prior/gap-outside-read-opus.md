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

