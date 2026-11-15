lead: anthropic/claude-opus-5-5/high mac-mini-worker
lease_until: 2026-11-16T05:43Z

# Literature read: gauge-field stiffness and the 4D analogue of the pinned-cell iteration

Queue row 1012 (`gap-gauge-stiffness-read-opus`), FINISH.md at commit c216eeef9. Companion of row 1011.
Reading only. No attack, no new claim. Every grade below says what the cited source states; nothing here is checked by a second derivation.

## Plan (at most eight steps)

1. Read FINISH.md (rules, row 1012, rows 1009-1011 for context) and grep the lane for: Schrodinger functional, background field, stiffness / helicity modulus, Ward identity, McBryan-Spencer / Mermin-Wagner / complex translation, Balaban background-field and boundary-uniform bounds, pinned cell. List what the lane holds per topic.
2. Literature: Schrodinger-functional coupling (Luscher-Narayanan-Weisz-Wolff 1992, Luscher-Sommer-Weisz-Wolff, Sint), the classical background minimum, its stability theorem, and what is rigorous vs perturbative vs numerical.
3. Literature: rigorous Ward identities, stiffness / helicity-modulus / free-energy-of-twist bounds for lattice gauge fields ('t Hooft twist, Tomboulis, Kovacs-Tomboulis, Munster, Borgs-Seiler, Mack-Petkova).
4. Literature: gauge analogues of McBryan-Spencer / Mermin-Wagner / Frohlich-Spencer (complex translations of link variables; Frohlich-Spencer U(1) massless phase, Guth, Ito, Tomboulis, Gopfert-Mack, Driver, Chatterjee).
5. Literature: Balaban background-field and small-field results that bound effective couplings uniformly in boundary data; Balaban-O'Carroll-Schor; Dimock's expositions; uniform-in-boundary bounds for gauge fields in a box (King, Seiler, Brydges-Frohlich-Seiler, Federbush).
6. openai/math and yang-mills-group releases: list by title, check for any pinned-cell or stiffness argument for gauge fields.
7. Table: per hit, exact statement, grade, group and dimension, whether it would tell a gapped theory from one with a massless factor.
8. Synthesis and RESULT line.

## Step log

(Each step appends below when it finishes.)

### Step 1. Lane grep, per topic (2026-11-15T17:50Z)

Searched `library/`, `library/prior/`, `parts/` and FINISH rows with `grep -rlE` from the folder. Counts are files that match.

| Topic | Files | What the lane already holds (file:line) |
|---|---|---|
| Schrodinger functional (SF) coupling | 21 | LNWW 1992 (hep-lat/9207009) read in main text and App. A: `prior/gap-fullread-1.md` Section 8 (Theorem 1 of Section 5.2, the lattice stability of the abelian background, `TL/a^2 > (N-1) pi^2 max{1, N/16}`; coupling defined by a derivative of the effective action in the background parameter; one-loop only, no two-volume inequality). Abstract-level: `prior/gap-vir-lit.md` Section 6 (LNWW; LWSW hep-lat/9207010 numerical running); `prior/gap-seed-lit.md` L59 (Sint-Vilaseca 1211.0411, lattice artefacts). Lane use: `gap-phys-seed.md` Q6 L202, L226 (SF coupling holds "the flux half at most"; fails at a point with two confining phases, GUIDE); `gap-constraints-max.md` L133 (Dirichlet walls KNOWN; row 903 chose Neumann walls). Row 1009, `prior/gap-o4-pinned-cell-read-opus.md` table rows 2, 3, 10 (L405-420): SF coupling is the nearest 4D object to OpenAI's stiffness H_Q, RECALLED, "monotone decrease at the one-loop rate is a belief". |
| Stiffness / helicity modulus | 32 (stiffness) / 0 (helicity) | No helicity-modulus result on file. "Stiffness" appears as the 2D pinned-cell stiffness (rows 1007, 1009, 1010) and as twist free energies (Theorem D (e)). |
| McBryan-Spencer, Mermin-Wagner, complex translation | 18 | Recalled only: `gap-crux-exercise4-max.md` L157, L742 (2D plane rotator, Frohlich-Spencer 1981, McBryan-Spencer 1977, not re-read). The gauge Mermin-Wagner twist idea is ARGUED to fail for SU(2): `gap-brainstorm2-max.md` L161, L216 (seam multiplication by a non-central constant costs order beta per plaquette on a rough field), L507; `gap-crux-skeleton-max.md` L236 (axis must be covariantly constant), `gap-crux-restate.md` L158 (Way 3 fails); checked as ARGUED only, `gap-crux-skeleton-check-astra.md` L304, L338. No complex translation of link variables on file. |
| Frohlich-Spencer, Guth (U(1) Coulomb phase) | 31 | `prior/gap-lit-u1.md` RESULT L42: FS large-beta 4D U(1) no-area-law (Villain, extended to Wilson cosine), Guth's Villain Wilson-loop bound (abstract), 3D Villain confinement at all beta (Gopfert-Mack). |
| Tomboulis, Ito, Kovacs-Tomboulis, Ito-Seiler, Kanazawa | 64 / 50 | `gap-tomboulis-read.md` and its check `gap-tomboulis-check-opus.md` (Tomboulis 0707.2179, Kanazawa 0805.2742, Ito-Seiler 0803.3019, read at pages listed there); `prior/gap-lit-flux.md`, `gap-lit-ineq.md` RESULT L61 (no parameter-monotone inequality for 4D SU(2)). |
| Balaban background field, bounds uniform in background / boundary | 168 / 88 | The whole hard core: A3 "uniform nonabelian multiscale background response" (FINISH Current order), CMP 96 flat linear part, CMP 102 Thm 1 (row 81), CMP 122 Prop 1 (`library/ref-chart.md`). On the gap lane: `gap-ds-gauge.md` L24, L189 (strong mixing of one boundary link, uniform in boundary values, for cubes, implies (W): a sufficient condition, open); `gap-crux-fp.md` L386 Proposition TW (twist ratios uniform in background for beta < 1/6); `prior/gap-lit-tiltcov.md` RESULT L360 (tilt-uniform covariance only at strong coupling). |
| Ward identities | 90 | Hard-core gauge Ward identities for the background (c0-loc, b99w); row 1009 table row 4: a local rotation profile of links is a gauge transformation, so no bracket term on gauge-invariant data. |
| Pinned cell | 6 | Only rows 1007, 1009, 1010, 1011 and `parts/gap.md`. |
| Commutator averaging | 1 file | `prior/gap-lit-commutator.md` RESULT L273: no publication uses random-commutator averaging for a vortex or centre-odd bound in 3D/4D. |

Net: the lane has read LNWW's main text, has abstracts of the SF numerics, has the U(1) Coulomb phase and the Tomboulis-type flux literature. It has no reading of: rigorous helicity-modulus or stiffness bounds for non-abelian lattice gauge fields; gauge spin-wave (McBryan-Spencer type) upper bounds; Balaban's results stated as uniform in Dirichlet boundary data on a box; the later SF literature (Sint's boundary counterterms, Narayanan-Neuberger, gradient-flow SF). Steps 2-6 go to those gaps and do not redo LNWW Section 5.2.

### Step 2. Schrodinger functional (SF) coupling (2026-11-15T18:05Z)

Sources. Primary text downloaded into its own folder under /tmp, text extracted with PyMuPDF from a separate tool folder, read with grep and sed: LNWW. Others through arXiv/ar5iv HTML pages fetched with a summariser (marked FETCH; quotes there are the summariser's and are not checked against the PDF).

**S1. M. Luscher, R. Narayanan, P. Weisz, U. Wolff, Nucl. Phys. B384 (1992) 168, hep-lat/9207009. READ pp. 1-2, 12-13, 22-24, 31-34 (text).**
- Definition (Sect. 4, p. 22): "A non-perturbatively meaningful definition of the Schrodinger functional can be given in the framework of lattice gauge theories." Lattice SF: integral over SU(N) link fields on a box of time extent T, spatially periodic with period L, with prescribed spatial links W at x0 = 0 and W' at x0 = T (4.2). So it is a pinned-slab partition function: Dirichlet on two faces, periodic on the others.
- Coupling (Sect. 2.6, p. 12): for a background B(eta), Gamma' = d Gamma / d eta "is a renormalization group invariant"; gbar^2 = Gamma'_0[B] / Gamma'[B] (2.43), where Gamma = -log Z and Gamma'_0 is the classical value, so gbar^2 = g_0^2 at leading order.
- Theorem 1 (Sect. 5.2, p. 32; proof App. B, "elementary ... quite involved"): for spatially constant diagonal abelian boundary data with angle vectors Phi_k, Phi'_k in the fundamental domain (phi_1 < ... < phi_N, |phi_a - phi_b| < 2 pi, sum = 0), and TL/a^2 > (N-1) pi^2 max{1, N/16}, the abelian field V of (5.6) minimises the Wilson action among all lattice fields with the same boundary values, uniquely up to gauge. Grade: lattice theorem, classical (no measure). Group SU(N), D = 4 (the appendix reduces to D = 2). It covers one abelian family of boundary data, not all Dirichlet data.
- Status words: "A rigorous proof of this conjecture [renormalisability] to all orders of perturbation theory is beyond the scope of this paper" (p. ~11, L520 of the text); one-loop finiteness only (Sect. 3.5).
- Monotone or bound on gbar^2 beyond perturbation theory: none in the text.

**S2. M. Luscher, P. Weisz, R. Sommer, U. Wolff, Nucl. Phys. B389 (1993) 247, hep-lat/9207010 (SU(2) running coupling). FETCH (ar5iv).**
- The coupling is an expectation: gbar^2(L) = k <dS/d eta>^(-1) (3.0); dS/d eta is a sum over the plaquettes touching the two Dirichlet faces of the tau_3 colour-electric field (3.1)-(3.2). No positivity of <dS/d eta> is claimed.
- Sect. 2.5 (heuristic): "gbar^2(L) proportional to e^(mu L) at large L" for a theory with mass mu. The step-scaling function sigma(2, u) and the running are Monte Carlo with continuum extrapolation. Grade: numerical, plus a heuristic large-L law.
- Gapped versus massless factor: the heuristic says yes in principle (gapped: 1/gbar^2 decays like e^(-mu L); a free massless abelian factor gives a box-size-independent response, RECALLED from the classical abelian SF action, not from a theorem), but no rigorous inequality is attached.

**S3. Luscher, Sommer, Weisz, Wolff, Nucl. Phys. B413 (1994) 481, hep-lat/9309005 (SU(3)).** ABSTRACT: finite-size scaling, numerical. Same grade as S2.

**S4. Later SF literature. ABSTRACT or FETCH only.** Sint-Sommer (QCD SF, one loop, "a rigorous definition of the QCD Schrodinger functional exists on a space-time lattice": a definition, not a bound); Sint 1008.4857 (chirally rotated SF; boundary O(a) counterterms "determined perturbatively to two loops"); 1105.0110 (O(a) modified SF set-up, tree-level boundary counterterm); Sommer hep-lat/9705026 (review of O(a) improvement); Fritzsch-Ramos 1301.4388 (gradient-flow coupling in the SF, g^2_GF = N^(-1) t^2 <E(t)>, perturbative normalisation; numerical step scaling); Sint-Vilaseca 1211.0411 (already in `gap-seed-lit.md` L59); a 2026 preprint (arXiv:2603.29841, twisted boundary conditions, gradient-flow step scaling, preliminary numerics). Grade: perturbative or numerical. None states an inequality for gbar^2 at any coupling, or between two box sizes.

**S5. M. Luscher, Commun. Math. Phys. 54 (1977) 283, "Construction of a selfadjoint, strictly positive transfer matrix for Euclidean lattice gauge theories". ABSTRACT (bibliographic records only; text not opened).** Lattice theorem: the Wilson-action transfer matrix is selfadjoint and strictly positive. RECALLED consequence, not read here: the lattice SF is a kernel of a power of this positive operator (LNWW (2.9)-(2.10) give the continuum form Z[C', C] = <C'| e^(-HT) P |C> and Sect. 4.2 says a spectral representation "may be obtained, for all values of the lattice spacing").

**Step 2 findings.**
1. The SF is exactly a pinned-slab partition function of lattice gauge theory (Dirichlet links on two faces). Its coupling is the response of -log Z to a one-parameter family of boundary data, and equals the expectation of a boundary electric field. This is the gauge object nearest to OpenAI's stiffness H_Q (row 1009, table row 2), as row 1009 said.
2. The only rigorous statement in the SF literature found is classical: LNWW Theorem 1 (unique minimiser for one abelian boundary family, all lattice spacings with TL/a^2 above a constant). Everything about gbar^2 itself is perturbative (one or two loops) or numerical.
3. No published bound of the form gbar^2 <= g_0^2 (the analogue of H_Q <= b), no monotonicity in L, no uniformity over boundary data, and no positivity of <dS/d eta> was found.
4. Tells gapped from massless factor: only heuristically (S2 Sect. 2.5).

### Step 3. Ward identities, stiffness and helicity-modulus bounds for non-abelian lattice gauge fields (2026-11-15T18:20Z)

The twist and flux inequalities (Tomboulis-Yaffe, Kanazawa's SU(N) extension, Borgs-Seiler, Mack-Petkova, Kovacs-Tomboulis, 't Hooft duality, Tomboulis 2007 and its critiques) are on file in `prior/gap-lit-flux.md` L17-42 and `gap-tomboulis-read.md` with its check. Not redone. New items only.

**W1. M. Vettorazzo, P. de Forcrand, "The helicity modulus in gauge field theories", hep-lat/0311007 (Lattice 2003 talk). ABSTRACT.** "we consider the helicity modulus (h.m.) for this theory [4D compact U(1), Wilson], and show that it is an order parameter for the confinement deconfinement phase transition. We extend the definition of the h.m. to an Abelian projected Yang-Mills theory, and discuss its behavior in SU(2)." Grade: numerical (lattice talk; no theorem claimed). Group U(1), and SU(2) only after abelian projection (gauge fixed). Gapped vs massless factor: for U(1) the h.m. is the photon's stiffness, non-zero in the Coulomb phase, zero in the confined phase; so it separates a massless abelian factor from a gapped phase, numerically. For SU(2) the definition is gauge-dependent.

**W2. Kovacs, Tomboulis, "SO(3) vortices as a mechanism for generating a mass gap in the 2d SU(2) principal chiral model", hep-lat/9603022. ABSTRACT + search excerpts.** A sufficient condition for a mass gap: the expectation of an external Z(2) twist tends to 1 exponentially in the box size. The reduction to one condition (bounded free energy of a vortex pair joined by a string) uses "a vortex correlation inequality" that the authors do not prove. Grade: conditional theorem plus an unproved inequality; 2D, SU(2). On file in conditional form as `gap-lit-flux.md` L36.

**W3. Rigorous lattice Ward / Schwinger-Dyson identities.** RECALLED, not re-read in this row: Chatterjee's master loop equation for lattice SO(N) (CMP 2019) and Jafarov's SU(N) version are exact lattice identities by Haar integration by parts (Stein's identity on the group), with splitting and merging terms that come from the Lie bracket. Search hit, ABSTRACT only: arXiv:2608.05415 ("Exact Lattice Identities and Continuum-Limit Dyson-Schwinger Equations for Yang-Mills Theory"; authors listed by the search as Chatterjee, Frasca, Ghoshal, Groote; not verified): lattice Dyson-Schwinger identities for SU(N) from left invariance of Haar measure, then a continuum limit for one- and two-point functions. Grade: exact lattice identities (theorem level for the identities); the continuum step is not stated as rigorous in the abstract. None of these gives a stiffness inequality.

**W4. Gauge invariance as a Ward identity.** Row 1009 table row 4 (on file): a local SU(2) rotation profile acting on link variables is a gauge transformation, so on gauge-invariant data the Ward identity is exact invariance, with no contact term and no bracket term. The SF coupling (Step 2) avoids this because its parameter moves the Dirichlet boundary data, not a bulk symmetry: d Gamma/d eta = <dS/d eta>, a boundary electric field. No published rigorous identity or inequality for the second derivative d^2 Gamma / d eta^2 (the SF "stiffness") was found.

**Step 3 findings.** No rigorous helicity-modulus or stiffness bound for a non-abelian lattice gauge field was found. The nearest rigorous inequalities are the reflection-positivity twist inequalities already on file; they bound Wilson loops by twist free energies and do not give a stiffness that decreases with scale. The helicity modulus in gauge theory is a numerical U(1) order parameter, and its SU(2) form needs abelian projection.

### Step 4. Gauge analogues of McBryan-Spencer, Mermin-Wagner and Frohlich-Spencer (2026-11-15T18:25Z)

**M1. S. Chatterjee, "A short proof of confinement in three-dimensional lattice gauge theories with a central U(1)", arXiv:2602.00436v2. READ pp. 1-7 (text; also on file in `gap-form-exercise.md` L89, `prior/gap-crux-lit-nonab.md` L147).**
- Theorem 3.1 (p. 3): G a compact Lie subgroup of U(n) with zI in G for all |z| = 1; Lambda a finite subset of Z^3; free boundary; Wilson action at any beta > 0. For a rectangular loop with sides R <= T: |<W_l>| <= n exp(-C (1 + n beta)^(-1) T log(R + 1)), C universal.
- Mechanism (p. 3): "The proof of Theorem 3.1 adapts the Mermin-Wagner 'complex rotation' mechanism for the two-dimensional XY model. The central U(1) allows us to introduce auxiliary U(1) edge variables and to decompose the Wilson loop into a U(1) phase factor and a bounded G-matrix factor; we then condition on the latter." Lemma 4.3 (pp. 6-7): a 2D XY-type model with arbitrary complex edge weights w_e has |E(phi_x phi_y)| <= exp(-C L^(-1) log(R + 1)), L = 1 + max |w_e|, by a change of variables tau along l-infinity shells.
- History (p. 3): Glimm-Jaffe (3D U(1), logarithmic potential, "using ideas originating in the McBryan-Spencer approach to the Mermin-Wagner theorem") plus Frohlich's comparison "U(n) lattice gauge theory confines whenever the corresponding U(1) theory does" (via Messager-Miracle-Sole-Pfister) give Theorem 3.1 as Corollary 2 of Frohlich.
- Grade: lattice theorem. d = 3. Groups with a central U(1) (U(n)); not SU(2), whose centre is Z_2.
- Gapped vs massless factor: no. It gives a logarithmic potential, which holds also in a 3D theory with a massless photon (the 3D Coulomb potential is logarithmic). It is a spin-wave upper bound on order, not a gap.
- Use for the pinned-cell question: this is the published gauge form of the McBryan-Spencer spin wave. It works because the central U(1) phase of the links behaves as a 2D XY spin after conditioning on slices; it uses the abelian centre, not a bracket. In d = 4 the same conditioning gives 3D XY-type slices, where the spin wave gives no decay (RECALLED: 3D XY orders); so it has no 4D form, as expected from the 4D U(1) Coulomb phase (M2).

**M2. J. Frohlich, T. Spencer, "Massless phases and symmetry restoration in abelian gauge theories and spin systems", Commun. Math. Phys. 83 (1982) 411. ABSTRACT** (IHES preprint P/81/40; record on file in `prior/gap-lit-u1.md` L42): "a new, elementary proof for the existence of a deconfining transition to a massless (QED) phase in the four-dimensional U(1) lattice gauge theory". Grade: lattice theorem; 4D U(1), large beta (Villain; Wilson cosine extension on file as incomplete in print). Gapped vs massless factor: this is the theorem that a massless factor exists in 4D U(1), i.e. the abelian control case. Complex translations: the 2017 exposition (arXiv:1711.04720, ABSTRACT) says the complex-translation method comes from McBryan-Spencer and is applied to terms of the spin-wave step; in FS it acts on abelian (Coulomb-gas) variables. Not read here.

**M3. A. Guth, Phys. Rev. D 21 (1980) 2291 (4D Villain U(1) Wilson-loop bound).** On file, ABSTRACT (`prior/gap-lit-u1.md`). Grade: lattice theorem, 4D U(1). Massless factor: yes, it proves one (perimeter-type behaviour).

**M4. Gopfert-Mack (3D U(1) Villain, area law at all beta).** On file (`prior/gap-lit-u1.md` L23). Uses complex translations (sine-Gordon representation) on abelian variables. 3D only.

**M5. McBryan-Spencer, Commun. Math. Phys. 53 (1977) 299 (cited by M1 as ref. [4]).** RECALLED, not re-read: in 2D SO(n)-symmetric models, correlations decay at least like a power, by a complex translation of the angle field along a harmonic-like profile. 2D spin models only.

**M6. Searches with no hit.** No paper was found that applies a complex translation to non-abelian (non-central) link variables, or proves a Mermin-Wagner or McBryan-Spencer type bound for SU(2) lattice gauge fields in any dimension. The search for "Ito" and "Tomboulis" with complex translation found nothing beyond the flux literature on file. Searches run: "Mermin-Wagner theorem non-abelian lattice gauge theory rigorous spin wave ..."; "complex translation link variables lattice gauge theory rigorous bound Frohlich Spencer ...". A search that finds nothing does not show that no such paper exists.

**Step 4 findings.** Every published gauge spin-wave bound found acts on an abelian degree of freedom: U(1) itself (Glimm-Jaffe, Gopfert-Mack, Frohlich-Spencer, Guth) or a central U(1) inside U(n) (Frohlich's comparison; Chatterjee M1). SU(2) has no central U(1), and the lane's own ARGUED notes (`gap-brainstorm2-max.md` L216, `gap-crux-skeleton-max.md` L236) say a non-central seam rotation costs order beta per plaquette on a rough field. None of these uses a bracket; all are blind in the sense of `parts/gap.md` (they hold equally where a massless abelian factor exists, or are upper bounds on order).
