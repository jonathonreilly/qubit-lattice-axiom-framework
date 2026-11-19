# minimal-toe-b: an information-minimisation ruleset (2026-10-22)

Designer: independent (no coordination). Runner: `runner.py`, output in `out.txt` (16 PASS / 0 FAIL).
Steer applied: keep the lattice, but re-read it as the information-minimal structure, not as spacetime.

## Principle IM (meta-rule)
**The law carries the least information consistent with consistency.** Concretely, it fixes nothing that
a constraint does not fix: maximum entropy over everything else (Jaynes). This is the axioms' "a law privileges
no states" turned into a selection rule. It is also the anti-smuggling gate stated as physics.

## The five rules

**R1 Unit.** The possibility unit is the smallest system that has continuous reversible dynamics *and* can
interact (entangle) with a copy of itself. Literature: within the d-ball state spaces, only d = 3 (the
qubit, complex QM) has entangled states, so interaction is impossible for every other d (Masanes, Mueller,
Perez-Garcia, Augusiak, JMP 55 122203 (2014)). This **derives the Qubit axiom**. Bends: none.

**R2 Relation = the unit's own axes.** Units are adjacent along one commuting generator per independent unit
observable, so there are three generators, one per Bloch axis. Commuting generators are the minimal description:
polynomial growth, with an address costing about 3 log L bits. Free (non-commuting) generators give exponential
address cost. Gromov's theorem says polynomial growth is virtually nilpotent; abelian is the minimal case. The
result is Z^3 with nearest neighbours, and each site owns 3 forward links. A related literature route ties space
dimension to the qubit's Bloch dimension: "direction information carried by the qubit" forces d = 3 (Mueller and
Masanes, NJP 15 053040 (2013)). **Reading:** the lattice is the adjacency graph of information units, not
spacetime. The metric is a derived response, as in the existing CL-3 response clause. Bends: the Lattice axiom
becomes derived rather than supplied, with the same content.

**R3 Records = irreversible, exclusive bits.** A record is a bit copied out redundantly and never erased.
Erasure costs (Landauer), so IM forbids it, which gives permanence. There is at most one record per mode, so
local matter modes are exclusive (fermionic, Grassmann). Born weights come from IM via noncontextual additivity
(Gleason/Busch) or envariance (Zurek). The record count only grows, and that growth is the arrow of time. Bends:
Record gains exclusion per *mode* (the axiom says per *site*). This is the main interpretive bend.

**R4 Unread frames are free.** The one-excitation modes of a site are its 2 qubit levels plus its 3 owned links:
C^5 = C^2 (+) C^3. Exclusion makes the site's matter space Lambda(C^5), which has 32 states. Only records are
read, so local frames are unobservable. Neighbours are compared by the frame changes that preserve the split and
the site volume form: **S(U(2) x U(3))**. Bends: Admissibility gets link transports with values in that group.
Literature: S(U(2)xU(3)) is isomorphic to (SU3xSU2xU1)/Z6, and Lambda C^5 restricted to it is one generation plus
its conjugate (Baez and Huerta, Bull. AMS 2010, arXiv:0904.1556). The new step is that 3 = owned links and
2 = qubit levels, with both counts derived from R1 and R2 rather than chosen.

**R5 Count and spread.** The dynamics is maximum entropy at fixed constraints:
- (a) One record is one unit of 4-volume. Lambda is conjugate to the record count (unimodular), so it fluctuates
  as N^(-1/2) ("everpresent Lambda", Sorkin; Ahmed, Dodelson, Greene and Sorkin 2004).
- (b) Vacuum entanglement is at a maximum in small regions at fixed volume. That gives the Einstein equations
  (Jacobson PRL 116 201101 (2016)), with the area coefficient (G) set by the vacuum entanglement density.
- (c) No family is privileged. The same matter appears once per choice of the record (quantisation) axis among
  the 3 Bloch/lattice axes, so there are **3 families**. Cubic rotations permute them as S3_L x S3_R.

## Calculation 1 (done, exact, runner.py)
- **A1–A3.** For d = 3 the traceless U(1) that commutes with SU(3)xSU(2) has charges diag(-1/3 x3, +1/2 x2). The
  even-occupation half of Lambda(C^5) is exactly Q(3,2)_{1/6}, u^c(3b)_{-2/3}, d^c(3b)_{1/3}, L(2)_{-1/2},
  e^c_{1}, nu^c_{0}: 16 states with exact SM hypercharges. Colour singlets carry integer charge and coloured
  states carry thirds.
- **B.** All perturbative anomalies vanish: Y^3, Y-grav, SU3^3, SU3^2 Y, SU2^2 Y. There are 4 doublets (Witten
  OK) and 16 Weyl states per family (Z16 OK; that check is a tautology here).
- **C.** (w 1_3, -1_2, e^{2 pi i Y}) acts trivially on all 32 states, so the global form (SU3xSU2xU1)/Z6 comes
  out derived.
- **D.** The even half is chiral iff d is odd. For d = 1 it is anomalous (Y^3 = 3/4). For d = 5 it is consistent
  but gives SU(5)xSU(2)xU(1). Given R1 (d = 3), **the SM group and hypercharges follow from space being 3D plus
  the qubit being 2-level**. None of SU(3), SU(2), Y or the particle list is written in.
- **E.** S3_L x S3_R invariance forces a democratic, rank-1 mass matrix: one heavy family per sector. Equal
  up/down alignment gives |V_33| = 1, so CKM is about 1 at leading order.
- **F.** The counting estimate is Lambda l_P^2 ~ N^(-1/2) = 1.4e-122, against 2.85e-122 measured: ratio 2.1. The
  O(1) coefficient is not derived.

## Gate (anti-smuggling)
| Rule | (1) no fitted number | (2) no named structure | (3) unbuilt prediction | (4) axiom bent |
|---|---|---|---|---|
| R1 | pass | pass | d = 3 Bloch = d = 3 space | none (derives Qubit) |
| R2 | pass | pass | Lorentz violation at the lattice scale (the repo's photon-decay window) | Lattice becomes derived |
| R3 | pass | pass | arrow = record growth | Record: exclusion per mode |
| R4 | pass | **borderline**: the 2(+)3 one-excitation mode choice is a structural choice; it names no group | nu_R exists; no gauge-mediated proton decay (only S(U2xU3) is gauged); Z6 global form gives no free fractional charge and a minimal-monopole lattice | Admissibility: group-valued links |
| R5 | (a) coefficient ~O(1), **FITTED** if tuned (ADGS need ~0.01–0.02 for BBN/CMB) | pass | evolving w != -1 (DESI-type), 3 families only, democratic hierarchy | Record count = volume |

**Smuggling review.** What is forced: d = 3 (given R1's interaction requirement), the group and hypercharges
(given R4's mode split), anomaly freedom, Z6, and 16 per family. What is supplied: the mode set "qubit levels (+)
owned links" (load-bearing; why a direct sum?), exclusion per mode, the family = record-axis identification, and
the Lambda coefficient. There is also a **double use** of the qubit SU(2). It is the rotation/direction unit in
R1 and R2, and weak isospin in R4. Either a graviweak split is derived (self-dual Lorentz SU(2) vs SU(2)_L;
Nesti and Percacci 2010) or spin must come from somewhere else (e.g. the 2^3 cell / Kahler–Dirac). Until then
this is an open identification, not a theorem.

## Scorecard against measurement
| Item | Status | Note / missing step |
|---|---|---|
| QM, complex Hilbert space | **derived** (literature) | R1, Masanes et al. |
| Born rule | plausible | needs noncontextual additivity of record odds (Gleason in dim ≥ 3; Busch POVM in dim 2) |
| Arrow of time | **derived** | R3: permanent records, monotone count |
| 3 spatial dimensions | **derived** (literature, under R1's assumptions) | |
| Lorentz invariance | plausible | emergent at long distance; tiny violation at the lattice scale is a prediction (needs the repo's light-cone results) |
| Gravity / Einstein eqs | plausible | R5b holds if the vacuum entanglement area law + local equilibrium hold; G not computed |
| Gauge group (SU3xSU2xU1)/Z6 | **derived given R4 split** | Calc 1 A–D |
| Hypercharges, charge quantisation | **derived given R4 split** | Calc 1 A, C |
| Chirality | plausible | internal: occupation parity = handedness (Calc 1 D). Spacetime Weyl fermions on Z^3 still face Nielsen–Ninomiya: the dynamics must gap the odd (mirror) half. This is the repo's live chirality wall, not removed |
| 3 families | plausible | R5c: show the three record-axis sectors are identical dynamical copies |
| Mass hierarchy | plausible (qualitative) | democratic rank 1: one heavy family per sector (t, b, tau). S3-breaking (from the actual record axis) not derived, so no numbers |
| CKM small / PMNS large | plausible (qualitative) | CKM about 1 at leading order (Calc 1 E). Large PMNS needs non-democratic nu (Majorana nu^c); theta_13 needs corrections |
| Higgs | missing | the bidoublet is in link/qubit content in principle; no derived light scalar; the hierarchy (v << 1/a) is unsolved |
| Neutrinos | plausible | nu^c forced (16th state), so nu mass exists; Majorana scale not derived |
| Strong CP | missing | needs a rule making arg det M = 0 (e.g. exact P/CP of R4 broken only spontaneously); not shown |
| Lambda | plausible | size to a factor of 2 by counting (Calc 1 F); coefficient FITTED-level; predicts w != -1 |
| Inflation / seeds | missing | no clock. Everpresent-Lambda fluctuations are not adiabatic seeds |
| Dark matter | missing | candidates: a heavy/sterile nu^c, or odd-half (mirror) states if gapped symmetrically; no law |
| Coupling values (alpha_s, alpha, sin^2 theta_W) | missing | the R4 group is not simple, so no SU(5)-style 3/8 is forced; a counting law for the couplings is needed |

Inserted = failure: **none** by name. **Borderline:** the R4 mode split and the Lambda coefficient.

## Cheapest decisive calculations (next)
1. **(DONE)** The S(U2xU3) frame group on Lambda(C^2+C^3) gives the SM group, hypercharges, anomalies and Z6.
   This is d-dependent and holds only for d = 3.
2. **Mode-split forcing.** Show that IM picks one-excitation space = C^2 (+) C^3 over C^2 (x) C^3 (6 modes, 64
   states) and over oriented links C^2 (+) C^6. Count description bits and check chirality and anomalies for each
   alternative, using the same runner pattern. Under 1 minute.
3. **Spin vs isospin.** Build the 2^3 cell (8 corners) in d = 3 with the qubit, and check whether a Lorentz SU(2)
   commuting with the R4 SU(2) exists, so that spin-1/2 is not the qubit SU(2). This is a finite matrix check on
   C^8 (x) C^2 (16-dim). If it fails, R4 must take isospin elsewhere and the ruleset is in trouble.

Repo context: hypercharge trace notes on main (`HYPERCHARGE_SQUARED_TRACE_CATALOG_THEOREM_NOTE_2026-04-25.md`,
`FULL_Y_SQUARED_TRACE_SU5_GUT_NOTE_2026-05-02.md`) take the SM content as given. This ruleset instead *derives*
the content from the site's mode count. No main note found deriving S(U2xU3) from owned links + qubit levels.
