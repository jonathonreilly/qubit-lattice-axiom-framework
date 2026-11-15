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
