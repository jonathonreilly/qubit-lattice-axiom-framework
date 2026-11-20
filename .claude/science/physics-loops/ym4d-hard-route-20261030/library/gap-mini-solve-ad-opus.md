lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-20T21:35Z

# gap-mini-solve-ad-opus (queue row 1251): four-dimensional SU(2) Yang-Mills mass gap, plain brief

Provenance: Claude Opus 5.5 (max reasoning), Mac mini worker 1, pinned at commit 6abdb75f2 on branch
`claude/ym4d-hard-route`. Started 2026-11-20T09:35Z (date -u). Labels: PROVED, ARGUED, GUIDE, OPEN, per the row.

## 0. Status log

- 09:35Z: file created (save protocol). Reading GOAL.md, the newest RESULT lines, `library/prior/gap-onebound-read-sol.md`.
- 09:52Z (date -u): reading done (GOAL.md; FINISH.md Joining, Working efficiently, Rules; row 1251 in full; RESULT lines of rows
  1222-1250; `parts/gap.md` L1-104; `library/prior/gap-onebound-read-sol.md` in full; row 1180 Steps 1-2; row 700
  Section 6; row 1244 (sibling, running) Step 1). Section 1 written.
- 10:09Z (date -u): Section 2 written (Zeng's Part II read in full; Lemmas Z1-Z3, Corollary Z2'). Next: Section 3.
- 10:14Z (date -u): Lemma Z4 (Remark B.15), Section 3 and the RESULT line written.

## 1. How best to attack it (judgement; ARGUED; every input cited)

**1.1 What a proof must contain (cited, not new).** Beside the existence chain T0, the gap clause of this lane reads
one lattice estimate, (N-phys) (row 1161 L146-148; restated in row 1180 Step 1, `gap-mini-neutral-fable.md` L44-48).
Row 1180 2.1 (L95-114) splits it into (a) a finite neutral seed at every fine coupling and (b) seed size O(1/a_j).
Row 1233 (`gap-mini-solve-u-opus.md` Proposition 3.7) pays (b) through the account's summable two-cutoff increments,
given the account's premises; row 1234 (`gap-mini-solve-v-opus.md`, check row 1250 HOLDS) shows (b) is a genuine
extra input in the comparison class. So, modulo the account, the infrared input is (a) at one coupling where the
running coupling is of order one: a seed for Wilson SU(2) at one coupling in the window beta = 2.3 to 2.6 (row 998
L133-136).

**1.2 Why every known kind of proof stops there (cited).**
- (K-one), a property with a number at one coupling in the band: the hand-proved edge is beta_std about 0.18
  (character ratio u = I_2/I_1 about 0.045; row 1229), against u = 0.48 to 0.52 in the band; A's own fixed-spacing
  results stop at beta_W <= 7/20 (row 1218 L116). GOAL.md forbids a computed certificate.
- (K-flow), a selective step carried through the band: needs an exact identity with a non-abelian sign at
  order-one response; none is on file (row 1243 Step 2.2; lead rule W2, `parts/gap.md` L97).
- A 4D port of the posted 2D O(N) proofs: no rigid non-abelian group acts on the integrated variables (Lemma CEN+,
  row 1016); boundary twists squeeze under tiling (row 1228); the neutral half needs association (row 1241).
- Published 4D proposals (row 1218): A's thermal seed (A-B*) is the lane's full periodic seed; B's cube criteria are
  open along the tuning, and B's weak-coupling Corollary 166 is the near-Haar property of long transports (row 1220,
  Lemma NULL); A's slab hypothesis (M) fails at beta 3-6 in GUIDE runs (row 1224).

**1.3 The one published weak-coupling mechanism not yet tested.** Zeng Chunping's Part II (Hexagon 2611.00543v1,
read by row 1218 L218-242 only; credited to its author) proposes a mechanism aimed at beta_N -> infinity: a
tunnelling package (COH), (TUN), (SPEC) from which Proposition 13.4 asserts an Eyring-Kramers law
rho_latt = Lambda exp(-c_K kappa_N B_*)(1 + O(kappa_N^(-1/2))) for a Dirichlet-form Poincare constant, and Theorem
14.1 adds (SPEC) and asserts the uniform transfer gap (C-MG2'') and the continuum gap. On file about it: row 1218
(reading; "constructs no Wilson TUN certificate"), row 1220 (SPEC fails as an identity at beta = 0), row 1234 ("TUN
must be read on a slice"; no claim made). Grep at this pin: no file tests (TUN) or (COH) against the Wilson action
(the lane's own (TUN) of rows 1158 and 1189 is a different statement: an overlap bound, `gap-paths-fable.md` L226).

**1.4 Choice for this row.** Rule 0 asks what changes. Zeng's package is the only published claim of a 4D
weak-coupling mechanism of (K-flow) kind (a selective step: tunnelling between two classical vacua, absent for the
free photon). Deciding whether (COH), (TUN), (SPEC) can hold for Wilson SU(2) either gives the lane a mechanism to
port (if they can) or closes the last published candidate (if they cannot). The question is decidable from the text
and the Wilson action. So this row: (i) reads Zeng's Part II definitions and the proof of Proposition 13.4 and
Theorem 14.1; (ii) tests each hypothesis against the Wilson action, by hand, with a PROVED verdict where possible;
(iii) runs a short GUIDE test only if a constant must be seen. Not attempted here: a new route to (N-phys); the
sibling rows 1244, 1248, 1249 (running) hold the (K-flow) stiffness questions.

## 2. Zeng's tunnelling package against the Wilson action (READ, ARGUED; written 09:58Z by date -u)

**2.0 Source.** Zeng Chunping, "From Four-Dimensional Wilson Lattice Gauge Theory to Quantum Yang-Mills Theory,
with a Conditional Mass-Gap Theorem", Hexagon 2611.00543v1 (17 November 2026), 57 pp., PDF fetched from
hexagonmath.org into a scratch folder outside the repository (not committed). Read in full: Part II, Sections 11-14,
pp. 45-50, and Appendix B.1, pp. 53-57 (Lemmas B.1-B.8, Proposition B.10, Corollary B.11, Remarks B.12-B.15).
Credit for everything quoted in this section: Zeng Chunping.

**2.1 What the package is (READ, with page).**
- Objects (p. 46): mu_p is "the Wilson measure on the time-slice configuration space", E_p "its Dirichlet form",
  rho_latt(p) the Poincare constant (11.3). The schedule is beta_N = beta_bar + 2 b_0 log(1/a_N) with b_0 = 22/(48 pi^2)
  (so beta_N = 1/g_N^2 at one loop), and kappa_N = beta_N kappa_*, kappa_* := 1/(2 b_0 c_K B_*) (11.1). Then
  exp(-c_K kappa_N B_*) = A a_N with A = exp(-beta_bar/(2 b_0)) (11.2). This is a definition of kappa_*, not a
  derived fact: kappa_* is chosen so that the barrier of (TUN) below produces exactly one power of a_N.
- (TUN) (pp. 46-47): two wells U^+-, a path gamma_p between them, and a foliation (s, y) in S^1 x Y_p of a
  neighbourhood of gamma_p with S(gamma_p(s, y)) = kappa_N Phi_p(s) + Psi_p(s, y); Phi_p has two nondegenerate
  minima (value 0) and two saddles, barrier Delta_p = c_K B_*, Morse curvatures uniformly bounded above and below;
  Psi_p and four y-derivatives bounded; Jacobian bi-Lipschitz. So along gamma_p the action barrier is
  beta_N/(2 b_0) + O(1): TUN asks the Wilson action to carry the one-loop number 1/(2 b_0) as a classical barrier.
- (SPEC) (p. 47) and Lemma B.1 (pp. 53-54): with E_p := E^tm_p(f, f) = <f, H_p f> (H_p = -log T_p on L^2(mu_p)),
  rho^tm_latt = -log(lambda_2/lambda_1) is a tautology. Zeng's own words (p. 54): "The substantive content of (SPEC) is
  then the identification of this temporal Dirichlet form with the spatial-bond Dirichlet form to which the
  semiclassical computation of Section 13 applies; that identification is part of the spectral side of the gap and
  is not proved here." This agrees with row 1220 (SPEC fails as an identity for the spatial form at beta = 0).
- (COH): Proposition B.10 proves only one-bond clauses (Lemmas B.2-B.8, defining representation); "the remaining
  clause of (COH) reduces to the design bound p >= p_0 > p_c ... and the multi-bond SU(2) transport extension;
  neither is supplied" (p. 56). The constants mu_harm "are numerical, obtained ... on three-dimensional
  bond-percolation resistor networks ... a model-level input ..., not a verbatim certificate for the Wilson
  transport measure" (Remark B.13, p. 56).
- Zeng's own status lines: Remark 11.2 (p. 47) "(TUN) is the spectral side of the mass gap itself"; Remark 14.3
  (p. 50) its construction "is the only step that cannot, even in principle, be certified a priori, since certifying
  it is equivalent to proving the gap"; Remark B.13 "The mass gap remains unproved."

**2.2 The proof of Proposition 13.4 (READ p. 49; ARGUED verdict).** Proposition 13.4 asserts the two-sided law
rho_latt(p) = Lambda(p) exp(-c_K kappa_N B_*)(1 + O(kappa_N^(-1/2))). Theorem 14.1 uses only its lower half. The proof
has three steps: (i) the coarea comparison (13.1) of E_p with the s-derivative form on the tube around gamma_p;
(ii) "conditioned on the transport coordinate s, the y-fibers contribute a gap bounded below by a kappa_N-independent
constant (Lemma 12.1, tensored over blocks with the uniform coherent-block control of (COH)), so the Rayleigh quotient
is minimized by functions of s alone"; (iii) the one-dimensional two-well Muckenhoupt law, Lemma 13.1 (correct as
stated, a Laplace computation). I find two steps that the hypotheses do not carry.
- Step (ii) tensorizes one-bond Poincare constants over blocks that interact. Tensorization holds for product
  measures; for an interacting Gibbs measure the joint constant can be smaller than every conditional one by a
  factor of the system size (a standard example, sketched, not used as a proof step: a ferromagnetic ring of n SU(2) spins at coupling kappa
  much larger than n; each
  one-site conditional law is a von Mises-Fisher law on S^3, whose Poincare constant is at least some c_0 > 0 for every
  concentration; the global rotation is an exact symmetry, so f = n^(-1) sum_i g(u_i) has variance close to Var_Haar(g),
  of order one, while its Dirichlet form is at most sup|grad g|^2/n; so the joint constant is O(1/n)). (TUN) bounds Psi_p and its
  y-derivatives, not the Poincare constants of the fibre measures dnu_s, so nothing in (TUN) or (COH) supplies step (ii).
- (TUN) describes a tube around one loop. The lower half of (13.4) is a statement about all of the configuration
  space Omega_p. A lower bound on a Poincare constant needs every bottleneck of mu_p, not one: a tube statement gives
  an upper bound (a test function in the tube), never a lower one. No hypothesis says that mu_p is carried by the tube.
- With E_p = E^tm_p, step (i) is the unproved identification that Zeng names on p. 54; with E_p the spatial-bond
  (gradient) form, (SPEC) is the unproved identification. Either reading leaves one identification of the size of
  the gap itself.

**2.3 The barrier normalization (ARGUED; one GUIDE remark).** In TUN the classical object S, evaluated at the saddle,
must equal beta_N/(2 b_0) + O(1) with a bounded residual. For a classical action of Wilson type, S = beta_N E(U) with E
independent of g, so the minimax barrier between two fixed wells is beta_N E_bar with E_bar a number fixed by the
geometry; (TUN) then forces E_bar = 1/(2 b_0) = 10.77 exactly in the limit (in the normalization S = beta_N E), a
coincidence between a classical lattice minimax and the one-loop coefficient. GUIDE (continuum values, not a lattice
proof): for tunnelling between topologically distinct vacua the natural barrier is the instanton action 8 pi^2/g^2,
and exp(-8 pi^2/g_N^2) = (a_N Lambda)^(22/3) for SU(2), so the physical rate behaves like a_N^(19/3) (Lemma Z3 below);
this is why kappa_* must be set by hand in (11.1). Zeng's Remark B.14 (p. 57) also withdraws the strong-coupling de-conditioning route.

**2.4 Verdict for the lane.** Part II of 2611.00543v1 contains two correct one-dimensional lemmas (Lemma 12.1, the
one-bond fibre reduction; Lemma 13.1, two-well Muckenhoupt asymptotics on S^1) and one-bond (COH) clauses. Its
mechanism step, the passage from a tube around one loop to the Poincare constant of the time-slice Wilson measure,
is not proved, and its hypothesis (TUN), by Zeng's own Remarks 11.2 and 14.3, is equivalent to the gap. So Part II
supplies no (K-flow) step and nothing to port: the last published 4D weak-coupling proposal of row 1218 is closed as a
mechanism. This does not refute Theorem 14.1 as an implication (no counterexample to (COH) + (TUN) => (13.4) for the
Wilson measure is constructed here; the two defects of 2.2 are gaps in its written proof). Novelty check: row 1218
(L218-242) and row 1220 read the package and its SPEC remark; no file on record reads Proposition 13.4's proof or
Lemma B.1 (grep `Lemma B.1`, `13.4`, `tensor` in files naming Zeng returns none of these points).

**2.5 Three lemmas that make 2.2 and 2.3 exact (PROVED by hand; written 10:08Z by date -u).**

**Lemma Z2 (Wilson Gibbs measures put almost no mass where the action is sub-extensive).** Let Lambda be a finite
lattice with link set E in which every link lies in at least 4 plaquettes, each plaquette containing it once (a
periodic cubic lattice of side n >= 3 in dimension 3 or 4 qualifies). For c > 0 and kappa > 0 let
S_kappa(U) = kappa c sum_p (1 - (1/2) tr U_p) on SU(2)^E and mu_kappa = Z(kappa)^(-1) exp(-S_kappa) dHaar. If
kappa c >= 3/16, then for every real t

    mu_kappa(S_kappa <= t) <= exp(t - |E|/16).

Proof. (i) One link. Fix kappa' with kappa' c >= 3/8 and a link l. For each plaquette p containing l,
(1/2) tr U_p = (1/2) tr(U_l A_p) with A_p in SU(2) built from the other links (cyclic order; if l enters inverted, use
U_p^(-1), which has the same real trace). Identify SU(2) with the unit quaternions; M_l = sum_p A_p is a quaternion,
M_l = r_l M_hat with 0 <= r_l <= q_l (q_l = number of plaquettes at l) and M_hat in SU(2). Then
sum_{p contains l} (1/2) tr U_p = r_l cos(phi_l), where cos(phi_l) = (1/2) tr(U_l M_hat). Given all other links, U_l M_hat
is distributed with density proportional to exp(x cos phi) against Haar, x = kappa' c r_l, and Haar puts density
(2/pi) sin^2 phi on the angle phi in [0, pi]. So, given the other links, phi_l has density proportional to
sin^2(phi) exp(x cos phi) on [0, pi]. Integrating d/dphi [sin^3(phi) exp(x cos phi)] over [0, pi] gives zero, so
3 E[cos phi] = x E[sin^2 phi] = x E[(1 - cos phi)(1 + cos phi)] <= 2 x (1 - E[cos phi]). With R = E[cos phi] this gives
R <= 2x/(3 + 2x), so x(1 - R) >= 3x/(3 + 2x) >= min(x/2, 1/2) (the last step: 3x/(3+2x) >= 1/2 iff x >= 3/4, and
3x/(3+2x) >= 2x/3 >= x/2 for x <= 3/4). The local energy l_l := c sum_{p contains l}(1 - (1/2) tr U_p) = c(q_l - r_l cos phi_l)
therefore satisfies, given the other links,
kappa' E[l_l | rest] = kappa' c (q_l - r_l) + x(1 - R) >= kappa' c (q_l - r_l) + min(x/2, 1/2).
If x >= 1 the right side is at least 1/2. If x < 1 then r_l < 1/(kappa' c), and kappa' c (q_l - r_l) >= 4 kappa' c - 1 >= 1/2.
So kappa' E[l_l] >= 1/2 for every link.
(ii) Extensive mean. Every plaquette has 4 links, so S_kappa' = (kappa'/4) sum_l l_l and E_kappa'[S_kappa'] >= |E|/8.
(iii) Tail. F(kappa) = log Z(kappa) is convex (F'' = Var(E_W) >= 0, E_W := S_kappa/kappa), so F'(t) = -E_t[E_W] is
non-decreasing and log(Z(2 kappa)/Z(kappa)) = -(integral from kappa to 2 kappa of E_t[E_W] dt) <= -kappa E_{2 kappa}[E_W]
= -(1/2) E_{2 kappa}[S_{2 kappa}] <= -|E|/16, by (ii) with kappa' = 2 kappa. Finally E_kappa[exp(-S_kappa)] = Z(2 kappa)/Z(kappa),
and Markov's inequality gives mu_kappa(S_kappa <= t) <= exp(t) Z(2 kappa)/Z(kappa) <= exp(t - |E|/16). QED

**Corollary Z2' (the tube of (TUN) has vanishing mass).** Read (TUN) with mu_p proportional to exp(-S) and S the
Wilson action of the time slice, S = kappa_N c sum_p (1 - (1/2) tr U_p) (the reading of Zeng's Section 12, whose bond cost
kappa_N(1 - Re(Q_b u*)) is the one-link conditional weight of this S; c is Zeng's normalization). Assume, as Proposition
13.4's uniform constants need (Lemma 13.1's O(1) depends on the C^4 norm), sup |Phi_p| <= M and sup |Psi_p| <= C_0 on the
tube N_p. On N_p, S = kappa_N Phi_p + Psi_p <= kappa_N M + C_0, so by Lemma Z2

    mu_p(N_p) <= exp(kappa_N M + C_0 - |E_p|/16).

Along the schedule kappa_N = beta_N kappa_* grows like log(1/a_N), while the periodic slice of physical side L has
|E_p| = 3 (L/a_N)^3 links. So mu_p(N_p) tends to zero faster than any power of a_N. The coarea identity (13.1) is a
statement about functions on N_p; a function supported off N_p has positive Dirichlet form and zero right side in
(13.1). Hence the written proof of Proposition 13.4 says nothing about a part of the configuration space that carries
all but exp(-c (L/a_N)^3) of the measure, and the lower half of (13.4), the half Theorem 14.1 uses, is not proved. Under
the other reading of Lemma B.1 (mu_p the ground-state measure Omega_p^2, S = -log Omega_p^2), the same conclusion needs
log max Omega_p^2 - E[log Omega_p^2] >= c |E_p|; this is ARGUED (each ultraviolet mode of the Gaussian picture contributes
about 1/2), not proved here.

**Lemma Z1 (a tube gives no lower bound; PROVED, elementary).** On the torus S^1 x S^1 let
mu_kappa proportional to exp(-kappa Phi(s) - kappa chi(t)) ds dt, with Phi, chi smooth, each with two nondegenerate zero
minima and two nondegenerate maxima, lower barriers Delta for Phi and Delta' > Delta for chi; Dirichlet form
integral of (f_s^2 + f_t^2). The tube {abs(t - t_0) < kappa^(-1/2)} around a minimum t_0 of chi, with coordinates (s, t),
satisfies the separation S = kappa Phi(s) + Psi with Psi = kappa chi(t) <= sup |chi''|/2 bounded there. The measure is a
product, so its Poincare constant is the smaller of the two one-dimensional ones, and by Lemma 13.1 for chi it is at
most C kappa exp(-kappa Delta') = o(kappa exp(-kappa Delta)). So an analysis on one tube can give an upper bound but not
the lower half of (13.4); a second bottleneck off the tube decides. (Correction, 10:09Z by date -u: in this toy (TUN)'s bounded
y-derivatives of Psi hold in the rescaled coordinate y = kappa^(1/2)(t - t_0), whose chart is not uniformly
bi-Lipschitz, and fail in the unscaled chart, where the second y-derivative of Psi is kappa chi''. The same tension sits
in Zeng's proof: its fibres concentrate at scale kappa^(-1/2) (Lemma 12.1 uses phi = y/sqrt(lambda), lambda = kappa_N r_b),
while (TUN) asks for bounded y-derivatives and a uniformly bi-Lipschitz chart at once. ARGUED: a tube on which both
clauses hold has fibre measures that are not concentrated in y, so it cannot carry a measure whose one-bond laws
concentrate; Corollary Z2' is the proved form of this point.)

**Lemma Z3 (fixed classical barriers give the wrong power of the cutoff; PROVED, algebra).** Let
beta_N = beta_bar + 2 b_0 log(1/a_N) and rho_N = C_N exp(-beta_N S_cl) with S_cl > 0 fixed and C_N in [C_-, C_+],
0 < C_- <= C_+. Then rho_N/a_N = C_N exp(-beta_bar S_cl) a_N^(2 b_0 S_cl - 1). So a lattice rate set by one fixed classical
barrier gives a physical rate that tends to 0 if 2 b_0 S_cl > 1, to infinity if 2 b_0 S_cl < 1, and stays bounded and
positive only if S_cl = 1/(2 b_0). For SU(2), b_0 = 11/(24 pi^2) and 1/(2 b_0) = 12 pi^2/11 = 10.77 (action in units of
beta_N = 1/g^2). The instanton (S_cl = 8 pi^2) gives a_N^(19/3), the fractional instanton of a twisted torus (S_cl = 4 pi^2)
gives a_N^(8/3). Zeng's (11.1) defines kappa_* so that the barrier is 12 pi^2/11 exactly. A tunnelling mechanism for the
gap therefore needs a barrier that runs with the scale (the coupling at the size of the tunnelling configuration), not a
fixed classical one. Prior record: the instanton weight exp(-8 pi^2/g^2(L)) with the 22/3 running is in row 1201
(`gap-mini-solve-j-fable.md` L132); the fixed-barrier filter in this form is not on file (grep `12 pi^2/11`,
`2 b_0 S`: no hits).

**Lemma Z4 (Zeng's "computable certificate for (MG)" certifies nothing; PROVED, elementary; written 10:14Z by
date -u).** Remark B.15 (p. 57, read from the rendered page) states, "for free (Gaussian) models", the equivalence
(exists eps_0 > 0: rho_p((0, eps_0)) = 0 for all p) iff (exists V_0, delta > 0: sup_p alpha_V^(p) <= 1 - delta for all
V >= V_0), with eps_0 = -log(1 - delta)/V_0 and alpha_V^(p) := (G_p(2V) - G_p(V)^2)/(1 - G_p(V)^2). The remark does not
define G_p; read it, as its left side suggests, as the normalized autocorrelation G_p(V) = integral of exp(-V lambda)
d rho_p(lambda) with rho_p a probability measure on [0, infinity). Any reading with 0 <= G_p(2V) <= G_p(V) <= 1 gives
the same conclusion.
(a) For every such G and V > 0 with G(V) < 1: 0 <= alpha_V <= G(V)/(1 + G(V)) <= 1/2. Proof: G(2V) >= G(V)^2 by
Cauchy-Schwarz, and G(2V) <= G(V) because exp(-2V lambda) <= exp(-V lambda); so G(2V) - G(V)^2 <= G(V)(1 - G(V)), and
1 - G(V)^2 = (1 - G(V))(1 + G(V)). QED
(b) So the right side of the equivalence holds with delta = 1/2 for every family, gapped or not, and the printed
eps_0 = log 2 / V_0 would then be a gap for every model and every V_0 > 0. Concretely, rho_p = delta_(1/p) (the
zero-momentum mode of a free field of mass 1/p on a fixed torus, a Gaussian model) has alpha_V^(p) = 0 for all V and p,
while no eps_0 > 0 has rho_p((0, eps_0)) = 0 for all p. The direction "<=" of Remark B.15 is false as printed; the
direction "=>" is true (alpha_V <= exp(-2 V eps_0)/(1 - exp(-2 V eps_0)) under a gap eps_0, plus the atom at 0). The
quantity alpha_V measures the departure of G from one exponential (it vanishes for a Markov semigroup with one rate),
not the size of the rate. Contrast: the lane's two-time form (Q) of row 1204 (as restated in row 1218 L59-72) reads the
mass through the relativistic dispersion (a spatial shift and a time step together), which is why it is a valid gap
criterion and alpha_V is not.

**2.6 Novelty and use (grep at this pin).** `grep -i -E "tensoriz|Muckenhoupt|Eyring" library/*.md` hits nine other
files (rows on LSI tensorization, Lemma CUT of `gap-oddgap-max.md`, the brainstorm lists); none of them names Zeng,
and no file reads Zeng's Proposition 13.4 or Lemma B.1. Prior work for Lemma Z2: **Lemma TYP** of
`library/explicit-region-two-step.md` L52-60 (hard-core lane; "discharged" there) proves the same kind of statement by
the same one-link heat-bath method (independent links of a plaquette-disjoint set; E[e_b | rest] >= 1/(8x); a Chebyshev
tail); it is the lane's "raw fine energy is extensive on typical fields" (FINISH L47). Lemma Z2 differs only in the
one-link identity 3 E[cos phi] = x E[sin^2 phi] (constant 1/2 instead of 1/8) and in the exponential tail from the
convexity of log Z (exp(t - |E|/16) instead of a Chebyshev bound). Its use against (TUN) is new. Use for the lane: any
future semiclassical row (wells, tubes, tunnelling) must say how its set carries the measure of a lattice with |E|
links; by Lemma Z2 a set on which the action is o(|E|) carries mass at most exp(-|E|/16 + o(|E|)).

## 3. Outcome of this row, and what stays open (written 10:14Z by date -u)

**3.1 Verdicts.**

| Statement | Label | Where |
|---|---|---|
| The crux, modulo the account, is a seed at one coupling in the band; no known kind of proof reaches it | ARGUED (cited) | Section 1 |
| Zeng's Part II gives no mechanism to port; its (TUN) is, by Zeng's Remarks 11.2 and 14.3, the gap itself | READ | 2.1, 2.4 |
| The written proof of Proposition 13.4 has two unsupported steps (tensorization over interacting blocks; global lower bound from one tube) | ARGUED | 2.2 |
| Lemma Z2: a Wilson SU(2) Gibbs measure puts mass at most exp(t - abs(E)/16) where the action is at most t (kappa c >= 3/16) | PROVED | 2.5 |
| Corollary Z2': under the Section 12 reading (mu_p proportional to exp(-S)), the tube of (TUN) has mass at most exp(kappa_N M + C_0 - abs(E_p)/16), so the lower half of (13.4) is not proved | PROVED given that reading | 2.5 |
| Lemma Z1: a one-tube analysis cannot give a lower bound on a Poincare constant | PROVED | 2.5 |
| Lemma Z3: a fixed classical barrier gives a physical rate a_N^(2 b_0 S_cl - 1); only S_cl = 12 pi^2/11 is finite; the instanton gives a_N^(19/3) | PROVED | 2.5 |
| Lemma Z4: alpha_V <= 1/2 for every spectral measure, so Zeng's Remark B.15 criterion ("<=" direction) is false as printed | PROVED | 2.5 |

**3.2 What this row did not do.** It did not attack (N-phys) or the one-coupling seed directly: Section 1 found no
route beyond the record, and the sibling rows 1244, 1248 and 1249 (running at this pin) hold the open (K-flow)
questions. It did not check Zeng's Part I, the C492 paper, or B's Theorem 45 hypothesis (B-D); for B-D I found no
quick refutation (with physical cube sides much larger than the correlation length the response to one exterior link
may stay local, so a supremum over exteriors need not fail; ARGUED, not written out). No numeric run was made (memory
56 percent free; none was needed). No subagent.

**3.3 What stays open.** (N-phys); the seed at one coupling in the band; (NS-gap) of row 700; the inputs of rows 1233
and 1241 ((EDGE), the 9.1 comparison's hypotheses, the (DET)-side items); the account's premises on the T0 chain; the
continuum datum. The mass gap of four-dimensional SU(2) Yang-Mills is not proved here, and nothing on the lane's chain
is disproved.

**3.4 For the lead.** (i) With Section 2, every published 4D proposal read by row 1218 (A, B, C) is now classed: A's
seed is the lane's seed; B's ascent is circular at weak coupling (row 1220) and B-BP is a hypothesis of the size of the
gap; C's mechanism is unproved and its certificate (Remark B.15) is vacuous (Lemma Z4). No published mechanism is left
to port. (ii) Lemma Z2 is a filter for any future semiclassical row: a set where the action is o(abs(E)) carries
mass exp(-abs(E)/16 + o(abs(E))); Lemma Z3 is a filter for any tunnelling row: a fixed barrier gives the wrong power of
the cutoff. (iii) A cross-provider check of Lemmas Z2, Z3, Z4 and Corollary Z2' is short (each proof is a few lines).

RESULT: Row 1251 (Claude Opus 5.5 max, Mac mini worker 1, 09:35Z-10:14Z by date -u; author only, checked by no one; no numeric run, no subagent): the mass gap of four-dimensional SU(2) Yang-Mills is NOT proved and nothing on the chain is disproved; (N-phys), the one-coupling seed and (NS-gap) stay OPEN. Worked item: Zeng's tunnelling package (Hexagon 2611.00543v1, Part II and Appendix B.1, read in full), the last published 4D weak-coupling mechanism not yet tested. READ: its hypothesis (TUN) is the gap by Zeng's own Remarks 11.2 and 14.3, and (SPEC) is a tautology for the log-generator form (Lemma B.1). PROVED by hand: Lemma Z2 (a Wilson SU(2) Gibbs measure gives mass at most exp(t - |E|/16) to {S <= t}, by a one-link identity and convexity of log Z; same method as the hard-core lane's Lemma TYP, with an exponential tail), hence Corollary Z2' (under the Section 12 reading the tube of (TUN) has mass at most exp(kappa_N M + C_0 - |E_p|/16), so the lower half of Proposition 13.4, which Theorem 14.1 uses, is not proved); Lemma Z1 (one tube gives no Poincare lower bound); Lemma Z3 (a fixed classical barrier gives a physical rate a^(2 b_0 S_cl - 1): finite only at S_cl = 12 pi^2/11, which Zeng's kappa_* imposes by definition; the instanton gives a^(19/3)); Lemma Z4 (alpha_V <= G(V)/(1 + G(V)) <= 1/2 for every spectral measure, so Zeng's Remark B.15 "computable certificate for (MG)" is false in its "<=" direction). ARGUED: the tensorization step of Proposition 13.4 is unsupported. So no published mechanism remains to port. OPEN: (N-phys), the seed at one coupling, (NS-gap), the account's premises. Output library/gap-mini-solve-ad-opus.md.
