lead: anthropic/claude-fable-5-2/max mac-mini-worker
lease_until: 2026-11-20T09:12Z

# gap-mini-free-fable: (W) by a free method, starting from the Jaffe-Witten target

Row 1181 of `FINISH.md`. Started 2026-11-19T21:12Z at commit 6a3a26b93. Research-stage working
state. It grants no status. Nothing here is a public claim. Every statement below carries one
of the labels PROVED, ARGUED, GUIDE, OPEN.

## Plan (written before any lane file was opened)

1. Read the statement of (W) only (row 720) and the Jaffe-Witten target as `GOAL.md` states
   it. Keep the lane files (`library/gap-solve*`, the council files, `parts/gap.md`) closed.
2. Write the target from the Jaffe-Witten side: what a mass gap is, which equivalent forms
   exist, and which inputs are specific to four dimensions and to a nonabelian group.
3. Choose routes that do not pass through the lane's reformulations. Attack one route per
   step. Each step ends with: statement, argument, the first step that fails, what is left.
4. Open the lane files and compare: `library/gap-council-synthesis.md`, `parts/gap.md`
   (methods 1-36 and the route registry), RESULT lines of rows 1143-1177. Mark each of my
   statements as new, known, or refuted there. Before attacking any open lemma, grep
   `library/open-core.md` and the FINISH rows for it.
5. Close: a proof, a disproof, or one precise obstruction statement per route tried. End
   with one RESULT line.

Rules in force: no computer-assisted step in a proof; a numeric run may only guide or refute;
credit Balaban, Sussman and Alpoge, Chatterjee and every other source by name; no
home-directory path in this file.

## Log

(steps are appended below, one per response)

Times (from `date -u`): the file was created at 2026-11-19T21:12Z; steps 1 to 4 were on disk
by 22:03Z. Per-step times were not recorded, so none is given in the headings.

### Step 1. The statement, and the target seen from the Jaffe-Witten side

**Read so far (statements only).** `GOAL.md`; `FINISH.md` L1-84, L299-356, rows 720 and
1174-1181; `parts/gap.md` L1-60 (the wording of (W)); `library/gap-phys-seed.md` L270-338
(definitions of S, D, Phi, z^-, D^+, Theorem ZD-c). No `gap-solve*` file, no council file and
no method list is open yet.

**(W), as on record (`parts/gap.md` L21-23).** Wilson SU(2) on four-dimensional tori, along
the trajectory (a_j, beta_j) of the account of Sussman and Alpoge after Balaban. P is a
dyadic set of physical sizes. D^+(L) is the upper limit of the Casimir free energy of the
symmetric torus of side L. z^-(L) is the lower limit of (side) x (gap of the transfer
operator of the periodic cube of side L). (W): there are (L_0, D_0) with D^+ <= D_0 from L_0
on, and one L >= 4 L_0 in P with z^-(L) > 256 D_0 + 30. By Theorem ZD-c of row 720, (W) is
equivalent to (PHYS-SEED), and Theorem S carries a seed to a gap on every larger cube.

**The Jaffe-Witten target.** A quantum Yang-Mills theory on R^4 for SU(2) with a Hamiltonian
H >= 0, a unique vacuum, and spectrum of H in {0} united with [Delta, infinity), Delta > 0.
In Euclidean form: exponential clustering of gauge-invariant local fields at a rate that is
positive in physical units. (W) is this statement at one finite physical volume of about 40
correlation lengths (GUIDE in row 720), together with flux energies that are not of order
1/L. So (W) is not a weak-coupling statement, and no small-volume expansion reaches it.

**What a proof must use (my own list, before any lane file).**

- U(1) in four dimensions at weak coupling has a massless photon (Guth; Froehlich and
  Spencer). A proof of (W) must use an input that is false for U(1).
- I know four inputs of this kind. (i) Asymptotic freedom: the sign of the one-loop
  coefficient, proportional to the adjoint Casimir. (ii) The Ricci curvature of the group
  manifold: positive for SU(2), zero for U(1); this is the same number as (i) in another
  role (Friedan's flow for sigma models; Singer's remarks on the orbit space). (iii) Twist
  eaters: SU(2) has flat connections with non-trivial 't Hooft flux (holonomies i sigma_1,
  i sigma_2), so a centre twist has zero classical cost; a U(1) flux has classical cost
  beta (2 pi)^2 / 2 times an aspect ratio. (iv) The dimension count N > 2 of the new
  two-dimensional proofs (below): SU(2) = S^3 has N = 4.

**Published work fetched (public, into a scratch folder; credited).** Jian Ding, Fenglin
Huang and Peng Yang, "Exponential decay for the two-dimensional Heisenberg model",
arXiv:2611.04908v1 (3 Nov 2026), 74 pages: exponential decay for the O(N) spin model on Z^2
for every real N > 2 and every beta. Their Remark 1.5 and Section 1 describe two mechanisms:
theirs (loop soup of intensity N/2 with fixed local time, Lupu's isomorphism, projection to
an XY model with random couplings, a Gaussian tail for the number of macroscopic loops, an
improved spin-wave argument on a "defective" region, then a coarse-graining step), and
OpenAI's of 6 Oct 2026 (non-commutativity of rotations of S^2 and a constructed family of
spin waves on S^2). Both are unchecked here. Both reach a finite-size criterion at a scale
exp(C beta) by a multi-scale argument that starts at the lattice scale and needs no control
of effective actions. That is the shape (W) needs, with one difference that matters:

**Remark 1.1 (ARGUED; rate versus trajectory).** A lattice result "gap at every fixed beta
with correlation length at most exp(C beta)" gives (W) only if C equals the exact exponent
1/(2 b_0) of the trajectory, with the right power of beta in front, or if it is applied to
the effective theory at the first-passage scale, uniformly over the effective actions that
the account produces there. With a constant C that is not sharp, the gap in physical units
tends to zero along the trajectory. So a port of a two-dimensional mechanism has two parts:
the mechanism at one cutoff, and its robustness under the block maps of the account.

**Routes I consider outside the reformulations (to be tested against the lane's list at the
compare step).**

- F1. Curvature route in Hamiltonian form: the Kogut-Susskind operator as a Dirichlet form
  on a product of 3-spheres, Bakry-Emery with Ric > 0, and what replaces log-concavity of
  the ground state.
- F2. Conditional sigma-model structure (Durhuus and Froehlich 1980): given the spatial
  links, the temporal links of one layer are an O(4) model in three dimensions in an SO(4)
  background. Random-walk form with holonomy weights (Kassel and Levy, covariant Symanzik
  identities). Question: does a mechanism of the Ding-Huang-Yang type survive holonomy
  signs?
- F3. Non-abelian spin waves for the twist: field-dependent, measure-preserving colour
  rotations, with the cost governed by a stiffness that non-commutativity reduces.

Nothing is proved in this step.

### Step 2. Compare: the three routes of step 1 are on the lane's map

Read in this step: `library/gap-council-synthesis.md` (whole); `parts/gap.md` (whole: the
formulation, methods 19-36, lead rules, obligations through row 1175, route registry, test
table, exact price); FINISH RESULT lines of rows 1174-1178 (rows 1143-1173 through their
digests at `parts/gap.md` L191-207).

**Verdict on my own list (statements about the record, checked against the lines named).**

| My route | On file as | Status there | Verdict |
|---|---|---|---|
| F1 curvature, Bakry-Emery | method 31 (rows 957, 968: averaged curvature, Polchinski flow, Piazza-Shen); Proposition G1 of row 1128 (one-link gain = Ricci/12 plus a group-blind part); method 24 | set aside | found again |
| F2 conditional O(4) layer | method 36 (row 1139, check 1140): background-uniform mixing fails at large b; normalized diamagnetic domination fails on 8 sites; BR-2 face rows 1077-1115 | blocked at (SING); "has to average over the actual Wilson backgrounds" | found again |
| F3 non-abelian spin waves for the twist | rows 1009-1050 (port of OpenAI's pinned-cell step; frames; route (ii)); row 1141 (field-built frames); C1, C2 of row 1013 | open with no mechanism | found again |

Two remarks I had written before the comparison are also on file: Remark 1.1 (a mechanism
at one cutoff plus a carry; `parts/gap.md` L24-26, method 23, row 1010), and the zero
classical cost of the centre twist (Lemma K4 of row 1051). The power beta^(-9/4) I had for
the one-plane twist ratio at fixed side is wrong against row 1143's checked
(3/2) log beta + log log beta; I had counted the toron integral naively and withdraw it.

So the independent start reproduced the map, as the three Fable seats of the council did
(synthesis 2a). This is the same model family; it is not an independent confirmation.

**What the record says a new route must be (from `parts/gap.md` L100, L190, L238-242 and
the synthesis).** (a) It must read the group at order-one response; (b) it must cancel
between supports before any bound (method 35); (c) it must read the whole state space, not
one factor (Lemma FAC, Lemma PT); (d) a worst case over pins, tilts, coupling fields or
backgrounds is false (Theorem D2, Lemma SHEET, method 36), so it must average over the
actual Wilson law; (e) the frame for the band "must come from blocked variables, not
microscopic transport" (lead reading under row 1141).

**Choice for the next steps.** I do not attack the two statements given to rows 1179 and
1180 (the Wilson branch selection; the one-cube neutral bound). I read the lane's digest
of OpenAI's pinned-cell step only as far as its mechanism, and then look for a route that
is not in the registry. Candidates will be grepped against `library/open-core.md` and the
FINISH rows before any attack.

### Step 3. What (W) adds to the Jaffe-Witten gap; second comparison

Read in this step: `library/prior/gap-o4-pinned-cell-read-opus.md` L57-200 (OpenAI's
pinned-cell step, as digested by row 1009); `library/gap-solve16-astra62.md` L1-70,
L236-281 (row 1175); `library/gap-solve9-astra62.md` L42-110 (row 1161, checked by row
1162); the Ding-Huang-Yang introduction (pp. 1-6).

**3.1 The question, from the Jaffe-Witten side.** The Jaffe-Witten gap is a statement
about local gauge-invariant fields. A local gauge-invariant observable commutes with the
centre flips of a periodic cube. So it acts inside each electric character sector, and
the vacuum lies in the neutral sector. (W) asks more: every electric flux energy of a
large periodic cube must be large. So I asked whether the flux clause is needed at all.

**3.2 My derivation (ARGUED here; then found on file, see 3.3).** Write Z[k, m] for the
64 twisted torus integrals, k the three temporal and m the three spatial twists, and
Z[k, m] = sum over e of (-1)^(k.e) Z_(e,m), with Z_(e,m) the trace of the transfer
operator on the sector of magnetic flux m and electric character e. Three sums are
symmetric under every exchange of axes and have a positive transfer operator in every
direction: the periodic one (m = 0, all e), the all-twist one (sum over k and m; it keeps
e = 0 and all m; this is the integral over SO(3) bundles), and the one with the sign
(-1)^(k.m) (it keeps e = m). Each contains the neutral periodic sector (e = 0, m = 0).
An engine of the type of Theorem S applied to any one of the three gives a gap on that
sector at every larger size. In a confining phase the first and third have one vacuum; in
a phase with a cheap electric flux and a costly centre vortex the second and third have
one vacuum. The third has one vacuum in both. So a seed for the third sum would give the
neutral gap with no choice of flux branch.

**3.3 This is on file.** Row 1161 (`gap-solve9-astra62.md` L85-105; check row 1162:
HOLDS) proves exactly this. Under a short-time neutral premise at one cube, one of two
alternatives holds (all twist ratios near 1, or all near 0), and in both the weighted
trace S_kappa = s + sum over m != 0 of X_(m,m) is at most 113 eta ("a flux-independent
seed for the local sector"); Theorem S-w then "gives the gap on its centre-blind local
observable space under the lane's limit hypotheses. This does not yet give the assigned
periodic wall in the second alternative." Row 1175 L270 adds that in either seed the
neutral gap is at least c_q/n_0 on all large cubes. Verdict: found again; not new.

**3.4 Consequence for the order of work (a reading of the record, for the lead).** By
rows 1161 and 1175 the two open statements have different consumers:

- the one-cube neutral premise (row 1180) is the only open input of the gap on local
  observables, which is what the Jaffe-Witten clause asks; it is also necessary for (W)
  (row 1161 L150);
- the branch selection (row 1179) is needed for the flux clause of (W) only, that is for
  the statement that the centre symmetry of the tori is unbroken.

The queue rows 1179-1181 name (W) as the target. If the owner's target is the
Jaffe-Witten gap, row 1179 is off its critical path. This is a reading of the record, not
a new result: row 731's RESULT already says "(GAP) does not need the flux sectors in its
limit half", and row 1161 supplies the kappa seed from the neutral premise in both
alternatives. I did not re-check Theorem S-w, Theorem EV-L or their limit hypotheses
(both are marked argued in row 731; row 1161 is checked by row 1162).

**3.5 OpenAI's step, and why I do not try a fourth port.** Row 1009's digest shows the
shape of the two-dimensional argument: stiffness = direct cost minus current variance
(3.4); after conditioning on cell boundaries, H_Q = v - Var J (3.19); a lower bound on
Var J from a Helffer-Sjostrand identity (3.21) and the Ward identity whose bracket term
rotates the current (3.7), (3.8), (3.28); the gain is twice a reciprocal-square frequency
sum, (log L)/pi (3.51). The step needs currents of a global non-abelian symmetry that
are themselves rotated by cheap moves. In a gauge theory every colour rotation of
integration variables is a gauge move (zero cost, and gauge-invariant currents do not
rotate), and the centre is the only non-gauge symmetry. Rows 1011-1050 and 1141 state
this in theorem form (Lemma CEN+, Lemma TWIST, Lemma WN, Lemma MASS, the adjoint
Laplacian gap of order 1/(1+b)). My own estimates in steps 1-3 gave the same numbers: a
lab-frame or microscopic covariant twist of total angle pi costs of order N^2, because
the adjoint transport is rough at the lattice scale; the cancellation that would remove
N^2 is the variance term, which no change of variables with unit Jacobian captures.
I add no port.

**3.6 Other routes considered in this step and not pursued (each ARGUED in two lines; no
theorem claimed).**

- Curvature of the orbit space as a mass term. The Ricci term of the product of
  3-spheres would give a gap of order g^2 per lattice unit. It is cancelled at the same
  order by the Hessian of the logarithm of the vacuum (the measure term against the
  tadpole), as gauge invariance forces. What is left is the running of the coupling.
  On file as method 31 and Proposition G1.
- A cone-contraction (Birkhoff) bound for the transfer operator. The projective diameter
  of the image of the positive cone grows like beta times the volume, so the bound is not
  uniform in the volume.
- Loop states with U-turn recombination. For n fundamental strands on one link the
  Casimir operator is n(n+2)/4 minus the sum over pairs of the cup-cap operators, so the
  electric heat kernel is a positive combination of U-turn diagrams. But Haar integrals
  of loop products have both signs (the integral of tr(U^2) is -1), so the positive cone
  of loop states has no positive pairing with the trace. This is the crosscap sign of
  method 35 in another basis.
- A Knabe-type criterion for the heat-bath dynamics (a sum of projections 1 - E_l with
  common kernel the constants). Its hypothesis is a local gap of a finite patch that is
  uniform over boundary pins and exceeds a threshold of order 1/n^2. It is a worst-pin
  statement at one cutoff, of the kind of (DS-W) (route registry), with no carry.
- A model of the class with first-passage data and no gap. A local action that is
  within the account's bounds of the Wilson form at first passage stays near the
  renormalized trajectory, so by universality (a belief) it has the Wilson infrared
  behaviour. Light matter changes the first-passage data. I have no counter-model; the
  test table point 5 stands.

Nothing is proved in this step.

### Step 4. One proved obstruction for the simplest twist move; guide sizes

**Addendum to 3.3.** The three axis-symmetric sector sums of 3.2 are row 731's "periodic,
full, kappa" (`library/gap-flux-exercise.md` L626; Theorem S-w at L507; "tr(F^2) observables
are centre-blind", C1 at L197). So 3.2 is found again in full.

**4.1 Setting.** Torus (Z/N)^4, N >= 3. Links l = (x, mu) run from x to x + e_mu. For a
plaquette p = (x; mu < nu) put U_p = U_(x,mu) U_(x+e_mu,nu) U_(x+e_nu,mu)^(-1) U_(x,nu)^(-1).
S(U) = -(beta/2) sum_p tr U_p, and S_eta(U) = -(beta/2) sum_p eta_p tr U_p, where eta_p = -1
on the stack (the N^2 plaquettes (x; 1,2) with x_1 = x_2 = N-1) and +1 elsewhere. Z and
Z_eta are the Haar integrals of exp(-S) and exp(-S_eta); mu is the Wilson measure;
u = E_mu[(1/2) tr U_p], which is the same for all p and is positive for beta > 0 (log Z is
convex in beta, its derivative is 6 N^4 u, and that derivative vanishes at beta = 0).
h(g) = (1/2) tr g for g in SU(2); h takes values in [-1, 1] and arccos h(g) is the round
distance from 1 to g on the 3-sphere, which is bi-invariant.

**4.2 Fact (PROVED; the Jensen bound through a fixed right translation).** For every field
Gamma of group elements on the links, independent of U,

  -log(Z_eta / Z) <= J(Gamma) := E_mu[ S_eta(U Gamma) - S(U) ],   (U Gamma)_l = U_l Gamma_l.

Proof. Haar measure is invariant under U_l -> U_l Gamma_l, so Z_eta is the integral of
exp(-S_eta(U Gamma)) and Z_eta / Z = E_mu[exp(-(S_eta(U Gamma) - S(U)))]. Apply Jensen. QED

**4.3 Lemma GA (PROVED; gauge averaging).** For every plaquette p = (x; mu < nu) and every
field Gamma,

  E_mu[ tr (U Gamma)_p ] = c_p(Gamma) E_mu[ tr U_p ],
  c_p(Gamma) = h(Gamma_(x,mu)) h(Gamma_(x+e_mu,nu) Gamma_(x+e_nu,mu)^(-1)) h(Gamma_(x,nu)).

Proof. (U Gamma)_p = U_1 A U_2 B U_3^(-1) C U_4^(-1), where U_1, ..., U_4 are the four links
of p in the order of 4.1, A = Gamma_(x,mu) sits at the vertex x + e_mu, B =
Gamma_(x+e_mu,nu) Gamma_(x+e_nu,mu)^(-1) at x + e_mu + e_nu, and C = Gamma_(x,nu)^(-1) at
x + e_nu. The measure mu is invariant under gauge transformations U_l -> g_x U_l g_y^(-1).
Take g equal to k at the vertex x + e_mu and 1 elsewhere. Then U_1 -> U_1 k^(-1) and
U_2 -> k U_2, so the expectation of tr(U_1 A U_2 B U_3^(-1) C U_4^(-1)) equals that of
tr(U_1 k^(-1) A k U_2 B U_3^(-1) C U_4^(-1)) for every k. Average over Haar k: the average
of k^(-1) A k is h(A) times the unit matrix (it commutes with SU(2) and has trace tr A).
Repeat at the two other vertices; they are distinct from each other and from x because
N >= 3. Last, h(C) = h(Gamma_(x,nu)). QED

So J(Gamma) = beta u sum_p (1 - eta_p c_p(Gamma)), and every term is at least 0.

**4.4 Proposition J (PROVED; area order for every fixed Gamma).** For every field Gamma,

  sum_p (1 - eta_p c_p(Gamma)) >= (1 - 1/sqrt 2) N^2,  so  J(Gamma) >= (1 - 1/sqrt 2) beta u N^2.

Gamma = 1 gives J = 2 beta u N^2 (the thin vortex). So no fixed right translation improves
the order N^2 of the thin-vortex bound. The same holds for a mixture over Gamma that is
independent of U, when Jensen is applied to the joint law of U and Gamma. A mixture kept
inside the logarithm is not covered; see 4.5.

Proof. Fix (x_3, x_4) and let Pi be the set of the N^2 plaquettes (x; 1,2) with these
coordinates. Exactly one plaquette p_0 of Pi is in the stack. Put kappa = 1 - 1/sqrt 2.
Suppose 1 - eta_p c_p < kappa for every p in Pi. Then c_p > 1/sqrt 2 for p != p_0 and
c_(p_0) < -1/sqrt 2. Each of the three factors of c_p has modulus at most 1, so each has
modulus above 1/sqrt 2. Every link of Pi is the first link (x,1) or the last link (x,2)
of exactly one plaquette of Pi. Hence abs(h(Gamma_l)) > 1/sqrt 2 for every link l of Pi.
Put s_l = sign h(Gamma_l) and g_l = s_l Gamma_l. Then h(g_l) > 1/sqrt 2, that is, g_l is
at distance less than pi/4 from 1. For two links a, b of Pi the distance from 1 to
g_a g_b^(-1) equals the distance from g_b to g_a, which is less than pi/2. So
h(g_a g_b^(-1)) > 0 and sign h(Gamma_a Gamma_b^(-1)) = s_a s_b. Therefore, for every p in
Pi, sign c_p is the product of s_l over the four links of p. Each link of Pi lies in
exactly two plaquettes of Pi, so the product of sign c_p over Pi is +1. But it is -1,
because c_p > 0 off p_0 and c_(p_0) < 0. This is a contradiction. So each of the N^2
planes Pi holds a term that is at least kappa, and all other terms are at least 0. For a
mixture over Gamma independent of U, apply Jensen to the joint law and average. QED

**4.5 What 4.4 does and does not say.** It is the finite, global form of row 1013's Lemma
WN for the centre twist, with a constant. It says that the zero classical cost of the
twist (Lemma K4 of row 1051) is invisible to every move that does not read U: gauge
averaging turns each inserted element into its half-trace. It does not cover maps
Gamma(U) that read the field (rows 1026-1050, 1141), nor bounds that keep the variance
term. With the frame averaged inside the logarithm, that is with
-log(Z_eta/Z) <= -E_mu[log of the Haar average over g of exp(-(S_eta(U Gamma^g) - S(U)))],
Gamma^g_l = g_y^(-1) Gamma_l g_y, the second-order terms cancel by the Ward identity
(ARGUED), and the cost that remains sits where Gamma is not small. A centre twist needs
such a place in every (1,2)-plane, for the reason used in the proof above. So this form is
of area order too (ARGUED, not proved). A bound below area order must use the freedom of
the core sheet to move, plane by plane; that is row 1179's open statement, and I do not
attack it.

**4.6 Guide sizes (GUIDE; hand estimates, one particle species of mass m, non-relativistic
gas, no flux term).** At time u on a cube of side L the neutral excited trace is about
L^3 (m/(2 pi u))^(3/2) exp(-m u). With u = L/K this is K^3 (x/(2 pi))^(3/2) exp(-x),
x = m L/K.

- Row 1161's neutral premise, K = 512, bound 1/2: x is about 21.3, so L is about
  1.1 x 10^4 / m.
- The kappa seed of rows 731 and 1161 at shape two, K = 2, bound 1/5041 (half of it for
  the neutral part): x is about 12.3, so L is about 25/m. The seven sectors with electric
  flux have weight below exp(-20) there if the string tension is m^2/14.3.

So the premise in the form of row 1161 sits about 440 times farther out than the seed it
feeds. This changes nothing in the logic. It may matter for any guide run on the premise.

**4.7 The Jensen gap is a relative entropy (PROVED; two identities).** Write
F_tw = -log(Z_eta/Z), mu_eta for the twisted measure, and mu_Gamma for the law of
U Gamma^(-1) when U has law mu_eta. Then

  J(Gamma) = F_tw + H(mu | mu_Gamma),

and, with A(Gamma) := -E_mu[ log of the Haar average over g of exp(-(S_eta(U Gamma^g) - S(U))) ]
(the bound of 4.5 with the frame averaged inside the logarithm),

  F_tw <= A(Gamma) = F_tw + H(mu restricted to gauge-invariant sets | mu_Gamma restricted) <= J(Gamma).

Proof. mu_Gamma has Haar density exp(-S_eta(U Gamma))/Z_eta, by right invariance. So
log(d mu / d mu_Gamma) = S_eta(U Gamma) - S(U) + log(Z_eta/Z), and its mu-mean is
J(Gamma) - F_tw. For the second line: S_eta(U Gamma^g) = S_eta(U^g Gamma) and
S(U) = S(U^g), because (U Gamma^g)_l = g_x^(-1) (U^g Gamma)_l g_y and S_eta is gauge
invariant. So the Haar average is R(U) := the average over g of rho(U^g), with
rho(U) = exp(-(S_eta(U Gamma) - S(U))) = (Z_eta/Z) d mu_Gamma / d mu. For a bounded
gauge-invariant f, E_mu[rho f] = E_mu[R f], since mu is gauge invariant. So R is the
conditional expectation of rho given the gauge-invariant sets, that is, (Z_eta/Z) times the
density of mu_Gamma with respect to mu on those sets. Take minus the mu-mean of log R.
The last inequality is the monotony of relative entropy under restriction. QED

Meaning. A bound on the twist cost through a change of variables is exact up to the
relative entropy between the Wilson measure and the transported twisted measure. With 4.4:
H(mu | mu_Gamma) >= (1 - 1/sqrt 2) beta u N^2 - F_tw for every fixed Gamma. A bound of
lower order needs a map, reading the field, that carries the twisted measure to within
that entropy of the Wilson measure on gauge-invariant sets. This is the frame with a
compensating Jacobian that the lane names as open under row 1141; the identity adds only
the exact size of what such a frame must achieve.

### Step 5. Third pass: further routes checked against the record before any attack

After step 4 I looked for a route that is not in the registry. Each candidate was grepped
in `library/`, `library/prior/` and `parts/` before any work (rule 0a). Counts are files
that name the key term.

| Candidate | What it would give | On file | Verdict |
|---|---|---|---|
| Thin torus with a 't Hooft twist (R^2 x small twisted T^2): all modes heavy at tree level, a dilute gas of fractional instantons gives the area law (Tanizaki and Unsal; Gonzalez-Arroyo), then continuity in the size of the small torus | a gapped, confining start at weak coupling | 20 files (Tanizaki), 8 (adiabatic continuity); "Route T", row 842, row 862 Theorem A (`gap-mine858-opus.md` L59: "The passage from thin n to n = a is missing. No seed holds in the thin box.") | found again; the continuity step needs a thermal sum at a time shorter than the side being enlarged (Lemma E'), which is not small in the thin box |
| Knabe-type local-gap criterion for heat-bath dynamics | a finite-size criterion with a threshold of order 1/n^2 | 23 files (Knabe), 25 (frustration-free) | found again; worst-pin hypothesis |
| Cone contraction (Birkhoff, Hilbert metric) | a gap from positivity | 21 files | found again; diameter grows with the volume |
| The neutral premise as an equation of state: neutral pressure at temperature T below 0.4 T^4 / K^3 in a box of side K/T | a thermodynamic form of row 1161's premise | route RB with row 934 ("THERMAL"); Proposition VIR | a restatement; covered by row 1180; not attacked |
| Transfer of the Ding-Huang-Yang mechanism (an XY model with defects from an extra loop-soup copy, improved spin wave on a reduced volume) | a second two-dimensional mechanism, with no non-abelian symmetry in it | rows 1099, 1117 use their Theorem 5.2 and their pins only | not ported, and I do not port it: see 5.1 |

**5.1 Why the Ding-Huang-Yang mechanism has no direct gauge form (ARGUED; reading of
their pp. 1-9 only, unchecked).** Their step needs three exact facts. (a) Given the third
coordinate, the first two form an XY model with couplings beta r_u r_v and nothing else,
because sigma_u . sigma_v = r_u r_v cos(theta_u - theta_v) + z_u z_v. (b) The model is a
conditioned Poisson soup of loops with non-negative weights, with the copies
exchangeable (Lupu's isomorphism). (c) A spin wave of the two XY coordinates costs a
gradient form, weighted by the couplings, so that a region with few XY loops is a region
of low stiffness. For Wilson SU(2), write a link as (u, v) with abs(u)^2 + abs(v)^2 = 1.
The map that shifts the phase of u and fixes v is U -> h U h, h = exp(i a sigma_3 / 2),
which preserves Haar measure. But tr U_p is twice the real part of a sum of eight
monomials, one for each choice of an even number of off-diagonal entries. One has the
gauge-invariant phase theta_1 + theta_2 - theta_3 - theta_4. Six carry the phases of two
links only, open strings that end on v-factors. One carries no theta. So (a) fails: given
the v-data the theta-field is a U(1) gauge field with charged sources on every plaquette.
And (c) fails with it: the cost of the shift is a mass form, not a curl form (Lemma 5.1a
below gives its mean exactly). (b)
fails because the action is quartic in the link quaternions; in the layer form of Durhuus
and Froehlich the temporal links of one layer are an O(4) model in an SO(4) background,
whose loop weights are traces of holonomies with both signs (Kassel and Levy), and
method 36 already shows that background-uniform statements are false there. I state no
theorem.

**Lemma 5.1a (PROVED; the phase shift of the diagonal entries has a mass form).** Let
a be a real field on the links and h_l = exp(i a_l sigma_3 / 2). The map U_l -> h_l U_l h_l
preserves Haar measure, multiplies the diagonal entry u_l by exp(i a_l) and fixes v_l. For
a plaquette p with links 1, 2, 3, 4 in the order of 4.1,

  E_mu[ tr (hUh)_p ] = E_mu[ tr U_p ] cos((a_1 - a_4)/2) cos((a_1 + a_2)/2) cos((a_2 - a_3)/2) cos((a_3 + a_4)/2).

So the mean action change is beta u sum_p (1 - product of the four cosines). It is zero for
the staggered field a_(x,mu) = (-1)^(x_1+x_2+x_3+x_4) alpha on a torus of even side, which
is the gauge transformation by g_x = exp(i (-1)^(|x|) alpha sigma_3 / 2). For a constant
field a it is 6 N^4 beta u sin^2(a), of volume order.

Proof. (hUh)_p = h_1 U_1 (h_1 h_2) U_2 (h_2 h_3^(-1)) U_3^(-1) (h_3^(-1) h_4^(-1)) U_4^(-1) h_4^(-1),
and under the trace the last factor joins the first: the four vertices of p carry the
insertions h_4^(-1) h_1, h_1 h_2, h_2 h_3^(-1), h_3^(-1) h_4^(-1). All are powers of
exp(i sigma_3 / 2), with half-traces the four cosines. Average over the gauge group at each
of the four vertices as in Lemma GA. For the staggered field every insertion angle
vanishes: a_1 - a_4 = 0 (both links start at x), a_1 + a_2 = 0 (they start at x and at
x + e_mu), a_2 - a_3 = 0 (they start at x + e_mu and x + e_nu, sites of equal parity),
a_3 + a_4 = 0. For a constant field the product is cos^2(a), and there are 6 N^4
plaquettes. QED

Contrast. In the O(3) model the constant rotation of the two XY coordinates is an exact
symmetry and a varying one changes the energy by a gradient form in every configuration.
Here the constant phase shift already has a mean cost of volume order. This is the precise
form of "(c) fails".

**5.3 A scan for method families with no file (GUIDE; a grep of key terms, counts of
files in `library/`, `library/prior/` and `parts/gap.md`).** Of 67 terms, 58 have at least
one file (for example bootstrap 98, Langevin 101, replica 49, Brascamp 33, Helffer 28,
Uhlenbeck 41, Gribov 21, Fradkin 23, Lee-Yang 18, loop equation 42; a count is a count of
a word, and some words also have other uses). Nine have none: Ricci
flow, Haagensen, holography, wavelet, Wetterich, Kugo, Haag-Ruelle, superselection,
Pirogov. A missing word does not show a missing idea (the curvature flow is method 31
under other words). Of the nine, one names an exact structure that is special to SU(2) in
three space dimensions: the gauge-invariant "metric" g_ij = E^a_i E^a_j of the electric
field (Lunev; Freedman, Haagensen, Johnson and Latorre; Bauer, Freedman and Haagensen;
recalled, not read in this run). It gives local gauge-invariant variables on a convex cone
with the linear potential (g^2/2) tr g. I did not attack it, for a stated reason (ARGUED):
in the electric representation the magnetic term is not a positivity-preserving
semigroup. On the lattice this is the sign of the 6j symbols in the spin-network basis,
which row 1081's check already records as the failure of squared-6j positivity. So the
cone has no Perron-Frobenius or Brascamp-Lieb structure to use. The other eight give no
inequality at order-one coupling that I know.

**5.2 What I did not do.** I did not read rows 879-956, the six council member files, or
any `gap-solve` file beyond the lines cited. I did not read the account of Sussman and
Alpoge in this run; I used only what the lane files quote from it. No numeric job was run
(none was needed; the numeric lock was not taken). I did not attack the Wilson branch
selection (row 1179) or the one-cube neutral bound (row 1180).

## Close

**Proved in this file (by hand, unchecked by another model).**

- Lemma GA (4.3): E_mu[tr (U Gamma)_p] = c_p(Gamma) E_mu[tr U_p], with c_p the product of
  three half-traces of the inserted elements.
- Proposition J (4.4): for every fixed link field Gamma on the N^4 torus, the Jensen
  bound for the centre twist through U -> U Gamma is at least (1 - 1/sqrt 2) beta u N^2;
  the thin vortex gives 2 beta u N^2.
- 4.7: J(Gamma) = F_tw + H(mu | mu_Gamma), and the bound with colour frames averaged
  inside the logarithm equals F_tw plus the same relative entropy on gauge-invariant sets.
- Lemma 5.1a: the mean cost of the phase shift U -> hUh of the diagonal entries is a mass
  form; it is of volume order for a constant shift.

These are obstructions to one family of moves. They are not selective and they do not move
(W). Lemma WN of row 1013 is the infinitesimal form of Proposition J; the constant, the
global statement and 4.7 are, as far as my greps show, not written elsewhere in the lane.

**Found again (no credit claimed).** F1 = method 31 and Proposition G1; F2 = method 36 and
BR-2; F3 = rows 1009-1050 and 1141; the three axis-symmetric sector sums and "the gap
does not need the flux sectors" = row 731; the neutral premise as the only open input of
the gap on local observables = rows 1161 and 1175; the thin twisted torus = Route T, rows
842 and 862; the zero classical cost of the twist = Lemma K4.

**Reading offered to the lead (ARGUED).** Section 3.4: for the Jaffe-Witten clause the
open input is the one-cube neutral premise alone; the branch selection serves the flux
clause of (W). Section 4.6 (GUIDE): that premise, in the form with K = 512, sits near
1.1 x 10^4 correlation lengths; the kappa seed it feeds sits near 25.

**Open, unchanged.** (W); the one-cube physical neutral upper bound; the Wilson branch
selection; a map reading the field that carries the twisted measure to within sub-area
relative entropy of the Wilson measure (4.7); any selective inequality at order-one
response. No route outside the lane's registry was found by this row.

RESULT: Row 1181 (Claude Fable 5.2 max, Mac mini worker; checked by no one). No proof and no disproof of (W). Starting from the Jaffe-Witten target with the lane files closed, the three routes I chose (curvature, the conditional O(4) layer, non-abelian spin waves for the twist) and the later candidates of step 5 are on the lane's map or stop at a stated reason, each already stopped at a stated obstruction there; the reading that the Jaffe-Witten gap needs only the one-cube neutral premise, with branch selection serving only the flux clause of (W), is also on file (rows 731, 1161). PROVED by hand, unchecked, not selective: Lemma GA, Proposition J (every fixed right translation gives a Jensen twist bound of area order, at least (1 - 1/sqrt 2) beta u N^2), the identities 4.7 (the Jensen gap equals a relative entropy, also after averaging colour frames) and Lemma 5.1a (the phase shift used by the Ding-Huang-Yang spin wave has a mass-form mean cost for Wilson SU(2)). GUIDE: the neutral premise at K = 512 sits near 1.1 x 10^4 correlation lengths. OPEN, unchanged: (W), the one-cube neutral bound (row 1180), the Wilson branch selection (row 1179), and any selective inequality at order-one response.
