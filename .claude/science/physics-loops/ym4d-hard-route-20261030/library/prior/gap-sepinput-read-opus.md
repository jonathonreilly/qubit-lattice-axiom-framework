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

- 2026-11-15T06:08Z: Step 1 done.

## 2. Step 2: what the lane has already read (not repeated here)

Grep of `library/prior/*.md` for Bhanot, Creutz, adjoint, mixed action, endpoint (2026-11-15T06:12Z). Already read:

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

- 2026-11-15T06:14Z: Step 2 done.

## 3. Step 3: K7 in the published phase diagrams (location and nature of the endpoint)

Search path: arXiv API (export.arxiv.org) queries on "mixed action" + SU(2) + adjoint, "bulk" + adjoint + SU(2),
SO(3) + monopole (hep-lat), then the arXiv abstracts of the hits (scratch `/tmp/sep995/`, 2026-11-15T06:15-06:25Z).
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

- 2026-11-15T06:27Z: Step 3 done (abstract level; full texts not read; next: Step 4, Wilson axis numerics).
