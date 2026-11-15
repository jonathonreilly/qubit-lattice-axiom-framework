lead: anthropic/claude-opus-5-5/high mac-mini-worker
lease_until: 2026-11-15T18:02Z

# Row 995: literature reading for the separating input (Wilson SU(2) axis vs the K7 endpoint family)

Queue row 995 (`gap-sepinput-read-opus`), FINISH.md line 1074, pinned at 805e7c67d. Feeds row 996 (`gap-sepinput-max`).
Started 2026-11-15T06:02Z on the Mac mini worker. Literature reading only; no numeric run planned.

## Plan (at most eight steps; one step per response, appended here before the next)

1. Read the K7 definition (`library/gap-constraints-max.md` L73) and row 708 Proposition V (`library/gap-mid-max.md`,
   and its source file); state K7 exactly in Section 1.
2. Grep the lane's earlier literature files (`library/prior/gap-lit-*.md`, `gap-crux-lit-*`) for the mixed / adjoint /
   fundamental-adjoint phase diagram and Wilson-axis facts already recorded, so that this row does not repeat them.
3. Phase diagram: locate K7 in the published fundamental-adjoint (Bhanot-Creutz, Greensite-Lautrup, Halliday-Schwimmer,
   Caneschi-Halliday-Schwimmer) and related diagrams; nature of the endpoint and the bulk line.
4. Wilson axis itself, numerics: absence of a bulk transition on the fundamental axis, crossover location, monotonicity
   of plaquette in beta, center vortex and monopole densities at beta 2.3-2.6.
5. Wilson axis, rigorous: correlation inequalities (Ginibre / Griffiths type for SU(2) fundamental, reflection
   positivity, character-expansion positivity of the one-plaquette weight, Osterwalder-Seiler), and which of them
   fail for the K7 actions.
6. Center / Z_2 and monopole literature that separates the two (Mack-Petkova, Tomboulis, Kovacs-Tomboulis, vortex
   free-energy, Alexandru-Haymaker etc.), with coupling ranges.
7. Sussman-Alpoge repository: grep the index for statements about the one-plaquette action, positivity, mixed actions.
8. Table of hits (statement, theorem or numerical, coupling range, source with short quote) and the RESULT line.

## Status log

- 2026-11-15T06:02Z: file created with plan.

## 1. Step 1: what K7 is (read from the lane's own files)

**K7 (row 708, `library/gap-mid-max.md` L48, L207, L357; cited by `library/gap-constraints-max.md` L73).** The
fundamental-adjoint one-plaquette weight

    w_K7(U_p) = exp( beta_F x + beta_A (4 x^2 - 1)/3 ),   x = (1/2) tr U_p,

taken on its first-order line in the (beta_F, beta_A) plane, which ends near (beta_F, beta_A) = (1.5, 0.9)
(row 708: RECALLED from Bhanot and Creutz, GUIDE values; row 712, `library/gap-crux-fp.md` 3b.3 L282, uses
(1.48, 0.90)). Note 4x^2 - 1 = |tr U|^2 - 1 = tr_adj U, so this is the standard Bhanot-Creutz normalisation
S = sum_p [beta_F (1 - (1/2) tr_F U_p) + beta_A (1 - (1/3) tr_A U_p)] up to a constant. On the line two phases
coexist, so (row 708) every thermal sum of a periodic box is at least 1 - o(1): no seed at any size. Row 708's
list of what K7 shares with Wilson: group, centre, zero-cost twists, reflection positivity, positive character
coefficients, Ricci curvature, one-loop coefficient (`gap-mid-max.md` L48). Row 708's one named difference: Wilson
is log-linear in x (log-convex in x once beta_A > 0).

**Proposition V (row 712, `library/gap-crux-fp.md` L356-363; check `library/gap-crux-fp-check.md` L84-104).** The
theorem-backed relative of K7: w_p(U) = exp(beta ((1 + x)/2)^p), p large, has a first-order point beta_t (van Enter
and Shlosman, cond-mat/0306362, Commun. Math. Phys. 255 (2005) 21-32, Theorem 2, in a reading with normalised trace;
proof sketched only for U(1) in d = 3), and then S(a; (2a)^3; beta_t) >= 1/5041 for every a >= 3 (1/1650 with the
check's one-line repair). w_p has ONE well (increasing in x), unlike K7, whose weight has a second local maximum at
U = -1 when beta_A > 3 beta_F/8 (0.90 > 0.555 at the endpoint). Row 712's reading: the separating property is a NUMBER
(how far log w is from linear in x), not a qualitative property; K7 needs beta_A/beta_F above about 0.6.

**What row 995 must find, restated.** Published results (theorem or numerical) that (A) place K7 and its endpoint in
the fundamental-adjoint phase diagram and say what the endpoint is; (B) say something about the Wilson axis
beta_A = 0 itself at beta = 2.3-2.6 (no bulk transition, crossover, monotonicity, correlation inequalities, Z_2 vortex
and monopole densities); (C) name exact properties of the one-plaquette fundamental weight that fail for
beta_A > 0 (or for w_p, p > 1).

- Step 1 done (before 06:10Z by `date -u`).

## 2. Step 2: what the lane has already read (not repeated here)

Grep of `library/prior/*.md` for Bhanot, Creutz, adjoint, mixed action, endpoint. Already read:

| Source | Where in the lane | What it gave |
|---|---|---|
| Bhanot-Creutz, PRD 24 (1981) 3212 | `prior/gap-tests-lit.md` L49-55 (full scan read); `prior/gap-vir-lit.md` L39; `prior/gap-fullread-1.md` L25 (no copy) | MC: triple point (0.55, 2.34), critical endpoint (1.48 +- 0.05, 0.90 +- 0.03); SU(2) specific-heat peak is a "shadow"; weight monotone in x iff beta_A <= 3 beta_F/8 |
| Rinaldi, Lacagnina, Lucini, Patella, Rago, arXiv:1212.0635 | `prior/gap-tests-lit.md` L57-61; `prior/gap-vir-lit.md` L41; `prior/gap-fullread-1.md` L33-37 | MC: Wilson axis is a crossover near beta_F = 2.30; first-order line weakens as beta_adj decreases; endpoint near beta_adj <~ 1.25 (their normalisation), nature "controversial" |
| Kanazawa, arXiv:0808.3442 (Tomboulis-Yaffe for SU(N), any one-plaquette action) | `prior/gap-vir-lit.md` L52, `prior/gap-crux-lit-2.md` L261 | theorem, not Wilson-specific |
| Kazakov-Zheng loop equations, arXiv:2404.16925 | `prior/gap-vir-lit.md` L50, `prior/gap-crux-lit-nonab.md` L164 | exact, survive the adjoint term in changed form |
| SU(2) character positivity for beta_F, beta_A >= 0 | `prior/gap-vir-lit.md` L51 | elementary; holds for K7 too |
| van Enter-Shlosman cond-mat/0306362 | `gap-crux-fp-check.md` L96-100; row 717 (`gap-ves-read`) | theorem (sketched for U(1), d = 3) for ((1+x)/2)^p |
| Osterwalder-Seiler, Luscher transfer matrix | `prior/gap-lit-channel.md` L17-19, `prior/gap-lit-grok-paths.md` L144-151 | hold for every positive-character one-plaquette weight |
| Creutz 5D, SU(5), SU(6); Knechtli-Luz-Rago 5D | `prior/gap-tests-lit.md` L17-45 | other tests, not K7 |

Earlier verdict (`prior/gap-vir-lit.md` L54): "No verified example was found of a proof that depends on a property
destroyed by the adjoint plaquette term." So the new path of this row is: (i) the LATER mixed-action literature on
the endpoint's location and nature (Gavai-Grady-Mathur, Mathur-Gavai, Heller for SU(3), de Forcrand-Jahn and
Burgio et al. for SO(3), Migdal-Kadanoff studies of the mixed plane); (ii) Z_2 monopole and vortex literature on the
Wilson axis (Mack-Petkova, Brower-Kessler-Levine, Halliday-Schwimmer, Kovacs-Tomboulis, Langfeld-Reinhardt-Tennert);
(iii) exact one-plaquette facts specific to exp(beta x): character-coefficient ratios I_{2j+1}/I_1 (monotone and
log-concave in j; used in Migdal-Kadanoff bounds by Ito and by Tomboulis), the vMF one-link law; and Tomboulis's
"confinement for all beta" claim with the Ito-Seiler critique, which is the one published argument that claims to
use the Wilson weight's coefficients.

- Step 2 done (before 06:10Z).

## 3. Step 3: K7 in the published phase diagrams (location and nature of the endpoint)

Search path: arXiv API (export.arxiv.org) queries on "mixed action" + SU(2) + adjoint, "bulk" + adjoint + SU(2),
SO(3) + monopole (hep-lat), then the arXiv abstracts of the hits (scratch `/tmp/sep995/`, 2026-11-15, before 06:10Z).
All hits in this section are NUMERICAL (Monte Carlo, or mean-field / strong-coupling series), none is a theorem.
Normalisation of all SU(2) papers below: Bhanot-Creutz, S_p = beta(1 - tr U/2) + beta_A(1 - tr_A U/3), i.e. the K7
weight of Section 1 with beta = beta_F, unless said otherwise. Quotes are from the arXiv abstracts unless a page is given.

**3.1 Where the endpoint is: it moved UP in beta_A after 1981.**

- R. V. Gavai, "A study of the bulk phase transitions of the SU(2) lattice gauge theory with mixed action",
  hep-lat/9603003, Nucl. Phys. B474 (1996) 446. NUMERICAL, N^4 with N = 6-16, at beta_A = 1.25: "Our simulations ...
  show an absence of a first order bulk phase transition. We find the discontinuity in the average plaquette to decrease
  approximately linearly with N." So the Bhanot-Creutz endpoint (1.48, 0.90), measured on small lattices, is NOT the
  endpoint of a bulk first-order line; at beta_A = 1.25 there is still none on 16^4.
- M. Mathur and R. V. Gavai, "Universality and the deconfinement phase transition in SU(2) lattice gauge theory",
  hep-lat/9410004, Nucl. Phys. B448 (1995) 399. NUMERICAL, 8^3 x 2, 8^3 x 4, 16^3 x 8, beta_A = 1.1: "we find no evidence
  of any transition at the location of a previously known bulk phase transition around beta = 1.33 ... suggest that the
  previously claimed bulk transition around beta = 1.33 is, in fact, the first order deconfinement transition." Also:
  the deconfinement transition "is of first order for beta_A >= 1.1, thus implying a change of universality class from
  that of the Wilson action at beta_A = 0".
- E. Rinaldi et al., arXiv:1212.0635 (already read by the lane, Section 2): separation of the two plaquette branches
  vanishes near beta_adj <~ 1.25, endpoint neighbourhood near beta_fund ~ 1.2; nature "controversial".
- S. Datta and R. V. Gavai, "Stability of the bulk phase diagram of the SU(2) lattice gauge theory with
  fundamental-adjoint action", hep-lat/9610022, Phys. Lett. B392 (1997) 172. Improved mean field + strong coupling:
  "the qualitative features of the bulk phase diagram are robust ... the location of the endpoint of the line of bulk
  phase transitions, seem to be strongly dependent on the higher terms of the strong coupling expansion."

**Consequence for K7 (my reading, ARGUED).** Row 708's K7 sits "on the first-order line ending near (1.5, 0.9)". The later
finite-size studies say that the segment 0.9 <= beta_A <= about 1.25 of that line is not a bulk coexistence line on
large periodic L^4 (it is a finite-temperature transition of small N_t lattices, or nothing). So K7's "no seed at any
size" (thermal sum >= 1 - o(1) from two coexisting phases on a periodic box) is supported by the literature only on the
segment beta_A >~ 1.3-1.5 (towards the triple point (0.55, 2.34)), and the endpoint itself is at beta_A about 1.25 or
above, beta_F about 1.2 or below. The arithmetic of row 712 (3b.3: oscillation 3.14, Lipschitz constant 3.88, second
local maximum at U = -1 since beta_A > 3 beta_F/8) holds a fortiori there: at (1.2, 1.25), 3 beta_F/8 = 0.45 < 1.25,
Lipschitz constant beta_F + 8 beta_A/3 = 4.53, oscillation of log w on [-1,1]: max 1.2 + 1.25 = 2.45 at x = 1; min at
x = -3(1.2)/(8(1.25)) = -0.36, value -0.432 - 1.25/3 + 1.25(4(0.13))/3 ... = -0.633 (hand arithmetic: 1.2(-0.36) =
-0.432; (4(0.1296) - 1)/3 = -0.1605, times 1.25 = -0.2006; sum -0.633); oscillation 3.08, Wilson-equivalent beta 1.54.

**3.2 What the endpoint is: three published readings.**

- Ordinary critical point with a scalar (phi^4 / Ising-like) continuum and ONLY the 0++ channel critical. U. M. Heller,
  "SU(3) lattice gauge theory in the fundamental-adjoint plane and scaling along the Wilson axis", hep-lat/9508009,
  Phys. Lett. B362 (1995) 123 (SU(3), NUMERICAL): "the mass of the 0++ glueball decreases as the endpoint of the bulk
  transition line is approached, while the other glueball masses appear unchanged ... the bulk transition line ends in a
  critical endpoint, with the continuum limit there being a phi^4 theory with a diverging correlation length only in
  the 0++ channel", and sqrt(sigma)/T_c "remains approximately constant". For SU(2): B. Lucini, A. Patella, A. Rago,
  "Infrared conformality and bulk critical points: SU(2) with heavy adjoint quarks", arXiv:1309.1614, JHEP 1311 (2013)
  106 (NUMERICAL; heavy-mass limit of Nf = 2 adjoint fermions, which induces an adjoint plaquette term): "showing the
  presence of a critical point ending a line of first order bulk phase transition ... the effective theory at
  criticality is a scalar theory in the universality class of the four-dimensional Gaussian model."
- Tricritical point, the transition continues as a SECOND-ORDER BULK line to and beyond the Wilson axis. M. Grady,
  "Critical or tricritical point in mixed-action SU(2) lattice gauge theory?", hep-lat/0404015, Nucl. Phys. B713 (2005)
  204 (NUMERICAL, scaling along the first-order line): "strongly supports the first-order endpoint being a tricritical
  point ... If tricritical, the transition must continue from the endpoint further into the phase diagram as a
  second-order bulk transition and extend to and beyond the Wilson axis." This is a minority reading; see 3.3.
- Deconfinement line joins the endpoint. R. V. Gavai, M. Grady, M. Mathur, hep-lat/9403001, Nucl. Phys. B423 (1994) 123
  (NUMERICAL, finite temperature): "the finite temperature deconfinement phase transition line joins the first order bulk
  phase transition line at its endpoint ... across the bulk transition line, the Polyakov loop undergoes a discontinuous
  jump implying the existence of both confining and deconfining phases on its two sides." And Gavai-Mathur,
  hep-lat/9512015: the tricritical point of the DECONFINEMENT line "first moves down towards the Wilson axis and then
  moves slowly upwards, if at all, as the lattice spacing is reduced".

**3.3 The dissenting Wilson-axis claim (must be on record).** M. Grady claims a transition ON the Wilson axis:
"Direct evidence for a Coulombic phase in monopole-suppressed SU(2) lattice gauge theory", arXiv:1306.6921, Nucl.
Phys. B876 (2013) 794 (NUMERICAL, Wilson action and a monopole-suppressed action): "gauge-invariant SO(3)-Z2 monopoles
... undergo a percolation transition exactly at the phase transition previously seen using Coulomb-gauge methods, with
an infinite lattice critical point near beta = 3.2"; and, for the action with Z2 vortices and monopoles and SO(3)-Z2
monopoles eliminated, at beta = 0 on up to 60^4, "The monopole restriction appears to prevent the transition to a
confining phase at any beta". Earlier: hep-lat/9806024 (preprint): with SO(3)-Z2 monopoles eliminated "the theory
deconfines for all beta on 12^4 and 20^4 lattices even in the strong coupling limit, despite a rather strong average
plaquette of around 0.64. This corresponds to an effective Wilson beta of 2.45". Status: Grady's Wilson-axis transition
at beta ~ 3.2 is not the accepted reading (the standard large-beta scaling studies, e.g. Teper's glueball and string
tension data up to beta = 2.7-2.85 and step-scaling studies, see no transition); it is outside the arena 2.3-2.6 in any
case. The SECOND claim is relevant as a K7-type test, not about Wilson: a constrained action (monopole-suppressed) with
plaquette 0.64, i.e. Wilson-like at beta_eff 2.45, is reported NON-confining at every beta. So "plaquette value of the
arena" plus all Wilson symmetries does not decide confinement; the Z_2 / SO(3) monopole content does.

**3.4 Monopole and vortex suppression in the mixed plane.** S. Datta, R. V. Gavai, hep-lat/9905030 (Phys. Lett. B458
(1999) 331) and hep-lat/9909139 (Phys. Rev. D62 (2000) 054512), NUMERICAL plus an exact duality remark: "In the limit of
complete suppression of the Z2 monopoles, the mixed action for the SU(2) theory in its Villain form is shown to be
self-dual under the exchange of the fundamental and adjoint couplings. By further suppressing the Z2 vortices we show
that the extended model reduces to the Wilson action with a modified coupling." And "In the limit of large lambda and
gamma [monopole and vortex chemical potentials], we obtain only lines of second order deconfinement phase transitions".
Reading (ARGUED): in the Villain mixed form, the whole adjoint direction is carried by Z_2 monopoles and vortices; with
both suppressed, the mixed plane collapses to the Wilson axis. This makes the Z_2-monopole density the published
order parameter that tells the K7 line from the Wilson axis (Section 6 collects its values).

- Step 3 done (abstract level; full texts not read; next: Step 4, Wilson axis numerics).

## 4. Step 4: the Wilson axis itself, numerical results in and near beta 2.3-2.6

All NUMERICAL. Sources fetched into `/tmp/sep995/dl/` (not committed), read with PyMuPDF / sed.

**4.1 The scalar glueball dips towards strong coupling, the tensor does not (the endpoint's "shadow" on the axis).**
M. Teper, "Glueball masses and other physical properties of SU(N) gauge theories in D = 3+1: a review of lattice
results for theorists", hep-th/9812187, Appendix A, Table 10 (p. 12 of the arXiv PDF; Wilson plaquette action: "All
these calculations use the standard Wilson plaquette action"). Rows read (beta, lattice, a sqrt(sigma), a m_0++, a m_2++):
2.2 (8^3 10): 0.467(10), 1.44(8), 2.76(45); 2.3 (10^4): 0.3687(22), 1.216(23), 1.94(8); 2.4 (14^4): 0.2686(21), 0.959(20),
1.487(33); 2.4 (16^4): 0.2660(21), 0.936(23), 1.520(30); 2.5 (16^4): 0.1834(26), 0.660(22), 1.028(27); 2.5 (20^4):
0.1881(28), 0.723(23), 1.051(26); 2.5 (32^4): 0.187(12), 0.70(4), 0.99(4); 2.6 (20^4): 0.1326(30), 0.51(3), 0.73(4);
2.7 (32^4): 0.1005(20), 0.39(3), 0.55(3); 2.85: 0.0636(12), 0.229(12), 0.353(16).
My ratios (hand arithmetic from these rows; errors not propagated):

| beta | m_0++/sqrt(sigma) | m_2++/sqrt(sigma) |
|---|---|---|
| 2.2 | 3.08 | 5.9 |
| 2.3 | 3.30 | 5.26 |
| 2.4 | 3.57 (14^4), 3.52 (16^4) | 5.54, 5.71 |
| 2.5 | 3.60 / 3.84 / 3.74 (16^4 / 20^4 / 32^4) | 5.61 / 5.59 / 5.29 |
| 2.6 | 3.85 | 5.50 |
| 2.7 | 3.88 | 5.47 |

Continuum (Teper, Table 8 and Table 12 for improved actions): m_0++/sqrt(sigma) about 3.7-4.0, m_2++/sqrt(sigma)
about 5.5-5.9. So on the Wilson axis the 0++ ratio falls by about 15-20 percent between beta 2.6 and 2.2 while the
2++ ratio stays flat: the same pattern Heller reports for SU(3) along the axis towards its endpoint (Section 3.2).
In the arena the 0++ mass in lattice units stays large: a m_0++ >= 0.51 at beta <= 2.6, = 1.22 at 2.3, i.e. a
correlation length below 2 lattice units in the most critical channel. This is the published quantitative statement
that the arena is OFF the critical endpoint: at the endpoint a m_0++ -> 0 (Heller SU(3); Lucini-Patella-Rago SU(2)
with heavy adjoint quarks, Gaussian scalar), while sqrt(sigma)/T_c and the other glueballs do not move.

**4.2 The lattice beta function: a 25 percent dip, not a zero.** J. Engels, F. Karsch, K. Redlich, "Scaling properties of
the energy density in SU(2) lattice gauge theory", hep-lat/9408009 (Nucl. Phys. B435 (1995) 295), Table "nonpert"
(TeX lines 520-575): non-perturbative a dg^(-2)/da (beta = 4/g^2), from a spline fit to the measured deconfinement
couplings g_c^2 at N_t = 2, 3, 4, 5, 6, 8, 16, checked against MCRG Delta beta data. Values: -0.1379 (2.15), -0.1174
(2.20), -0.0848 (2.30), -0.0754 (2.38-2.39, the minimum of |.|), -0.0779 (2.50), -0.0812 (2.60), -0.0848 (2.80),
-0.0929 (beta -> infinity, the one-loop value -2 b_0). Quote (TeX L367-369): "physical quantities such as the critical
temperature or the string tension are violating asymptotic scaling in the range of coupling constants considered so
far ... Nevertheless the scaling of dimensionless ratios of observables works remarkably well". Reading: on [2.3, 2.6]
|a dbeta/da| = 4 |a dg^(-2)/da| lies in [0.30, 0.34], smooth, against 0.37 (one loop) and about 0.40 (two loop at
beta 2.4, my arithmetic with b_0 = 22/(48 pi^2), b_1 = 136/(3 (16 pi^2)^2)). A bulk critical point on the axis would
make it vanish; the dip is the endpoint's shadow at finite distance. NUMERICAL, a fit, not a bound.

**4.3 Step scaling (abstract only).** M. Luscher, P. Weisz, R. Sommer, U. Wolff, "Computation of the running coupling
in the SU(2) Yang-Mills theory", hep-lat/9207010, Nucl. Phys. B389 (1993) 247 (NUMERICAL, finite-size scaling, Wilson
action): "already at rather low q, the evolution of alpha(q) is well described by the 2-loop approximation to the
Callan-Symanzik beta-function". The bare couplings used were NOT READ here; whether its steps pass through 2.3-2.6 is
not checked.

**4.4 What on the Wilson axis is monotone in beta, exactly (my own one-line remark, PROVED, and it does NOT separate).**
d<sum_p x_p>/dbeta = Var(sum_p x_p) >= 0 on every finite torus, for every weight exp(beta F) and in particular along any
line through the K7 plane (with F the directional derivative of the action). So plaquette monotonicity in beta holds
for K7 too and cannot separate. What separates numerically is the SIZE of the specific heat: no growth with volume on
the axis (Bhanot-Creutz "shadow", already read) against a volume-proportional peak (first order) or a divergence
(endpoint) in K7.

- Step 4 done. Next: Step 5 (rigorous correlation inequalities and exact one-plaquette facts).

## 5. Step 5: rigorous statements on the Wilson axis, and exact one-plaquette facts that fail for K7

**5.1 Tomboulis's all-coupling argument is blind to K7 (THEOREM-LEVEL CLAIM, disputed; hypothesis read).**
E. T. Tomboulis, "Confinement for all values of the coupling in four-dimensional SU(2) gauge theory", arXiv:0707.2179
(TeX `confI.tex`, read L286-349, L670-690). The action enters only through its normalised character coefficients:
"We start with some appropriate plaquette action A_p ... which, for definiteness, is taken to be the Wilson action"
(L290-292), and the property used is (L343-345) "F_j(beta) >= 0, hence 1 >= c_j(beta) >= 0 all j, which implies that the
measure ... satisfies reflection positivity". After one decimation step the effective action "will generally contain
all representations ... among the effective couplings beta_j(m) negative ones will occur" (L676-679). K7 (beta_F,
beta_A >= 0) and w_p have 1 >= c_j >= 0 (lane: `prior/gap-vir-lit.md` L51; check of row 712 L86). So by row 712's
Proposition T3 the argument, if repaired, could not use anything that separates Wilson from K7; it is consistent with K7
only because both K7 bulk phases confine (Section 3.2, Gavai-Grady-Mathur). The Ito-Seiler critique (arXiv:0711.4930,
0803.3019, 0901.4246, PoS Confinement8:034) is already in the lane (`prior/gap-lit-2.md` L45-49,
`prior/gap-crux-lit-nonab.md` L246). Verdict for row 996: confinement-type inputs do not separate; the mass gap does.

**5.2 An exact one-plaquette property of the Wilson weight that K7 and w_p violate: log-concave character coefficients
(adjoint subordination).** Sources: the Wilson coefficients F_j(beta) = (2/beta) I_{d_j}(beta), d_j = 2j + 1 (Tomboulis
L316-318), so the normalised coefficients are c_j(beta) = I_{2j+1}(beta)/I_1(beta). The Turan inequality for modified
Bessel functions, "I_{nu-1}(u) I_{nu+1}(u) - [I_nu(u)]^2 < 0 ... where nu > -1 and u > 0 ... was proved first in 1951 by
Thiruvenkatachar and Nanjundiah and later in 1974 by Amos ... In 1991 Joshi and Bissu ... in 1994 Lorch" (quoted from
A. Baricz, S. Ponnusamy, "On Turan type inequalities for modified Bessel functions", arXiv:1010.3346, Proc. AMS 141
(2013) 523, Section 1). THEOREM (cited).

Consequence (PROVED here, two lines, from the cited theorem). For the Wilson weight at every beta > 0 the sequence
n -> c_{n/2}(beta) (n = 0, 1, 2, ...; c_0 = 1) is strictly log-concave: c_{n/2}^2 > c_{(n-1)/2} c_{(n+1)/2} (Turan at
nu = n + 1 >= 1). Hence the ratios r_n = c_{n/2}/c_{(n-1)/2} strictly decrease, r_1 = c_{1/2}, and
c_{n/2} < c_{1/2}^n for n >= 2; in particular c_1 < c_{1/2}^2 ("adjoint subordination": every higher representation is
weaker than the matching power of the fundamental). The same holds for the heat-kernel weight, c_j = exp(-t j(j+1)),
whose logarithm is concave in j (my arithmetic: c_1 = e^(-2t) < c_{1/2}^2 = e^(-3t/2)).

Fails for K7 and for w_p (GUIDE numbers, plus a small-coupling argument). 1D quadrature (`/tmp/sep995/scripts/chars.py`,
200,001-point trapezoid on [0, pi] with Haar weight (2/pi) sin^2; control: Wilson at 2.3 reproduces I_{n+1}/I_1 =
0.4793, 0.1665, 0.0450 to 4 digits; run under the numeric lock, 2026-11-15T06:09Z, memory 70 percent free, < 2 s):

| weight | c_{1/2} | c_1 | c_1 - c_{1/2}^2 |
|---|---|---|---|
| Wilson beta 2.3 | 0.4793 | 0.1665 | -0.0632 |
| Wilson beta 2.6 | 0.5203 | 0.1995 | -0.0713 |
| K7 (1.48, 0.90), Bhanot-Creutz endpoint | 0.4326 | 0.2106 | +0.0235 |
| K7 (1.2, 1.25), later endpoint estimate | 0.4012 | 0.2358 | +0.0749 |
| K7 (1.0, 1.5) | 0.3682 | 0.2559 | +0.1204 |
| K7 (0.8, 1.8) | 0.3278 | 0.2862 | +0.1787 |
| K7 (0.55, 2.34), triple point | 0.2655 | 0.3537 | +0.2832 (and c_1 > c_{1/2}) |
| w_p, p = 10, beta 6 | 0.6701 | 0.5762 | +0.1272 |
| w_p, p = 50, beta 10 | 0.8415 | 0.8288 | +0.1206 |
| w_p, p = 200, beta 14 | 0.9541 | 0.9519 | +0.0416 |

(The w_p couplings are arbitrary test points: the van Enter-Shlosman beta_t(p) is not known numerically.) Small
coupling (my arithmetic, ARGUED to second order): with Haar E[x^2] = 1/4 and orthonormal characters, c_{1/2} = beta_F/4
+ O(beta^3) and c_1 = beta_F^2/24 + beta_A/9 + O(beta^2 beta_A, beta^3), so c_1 - c_{1/2}^2 = beta_A/9 - beta_F^2/48 +
..., positive as soon as beta_A > 3 beta_F^2/16 at small couplings; for w_p, p >= 2, ((1 + x)/2)^p has a chi_1 component
with positive coefficient, so c_1 is linear in beta while c_{1/2}^2 is quadratic, and the inequality fails at small beta.
So log-concavity is NOT a qualitative property of "no adjoint term": it fails for every K7 point tested and for w_p, and it
is a quantitative statement of row 712's "how far log w is from linear in x" (Section 1). Caveat (from Tomboulis L676-679):
decimation does not preserve it (effective actions acquire all representations, some with negative couplings), so it is a
property of the BARE weight at one scale only. I found no lattice-gauge paper that uses the Turan inequality or
log-concavity of c_j; NOT FOUND in this search, not a nonexistence claim.

**5.3 Correlation inequalities for SU(2): negative search result.** arXiv API queries ("correlation inequalities" AND
gauge in math-ph / math.PR / hep-lat; "Wilson loop" AND monotone in math.PR / math-ph) returned no SU(2) Griffiths- or
Ginibre-type inequality. Hits: Kovacs-Tomboulis hep-lat/9607068 (Nucl. Phys. Proc. Suppl. 53 (1997) 509): "A sufficient
condition for confinement was previously translated into Z(2) monopole correlation inequalities in a related SO(3) gauge
theory ... present some Monte Carlo evidence" (a condition with numerical support, not a theorem; Section 6); Mota-Sa
Barreto arXiv:2402.12277 (Z_3 only). Griffiths (Z_2) and Ginibre (U(1)) inequalities and their irrelevance as the
separating mechanism are row 708's (`gap-mid-max.md` L46). Plaquette monotonicity is universal (Section 4.4).

- 2026-11-15T06:10Z (`date -u`): Step 5 done. Earlier times I had written in this log were estimates and are removed. Next: Step 6 (centre vortex / Z_2 monopole densities and vortex free energy on the axis).
