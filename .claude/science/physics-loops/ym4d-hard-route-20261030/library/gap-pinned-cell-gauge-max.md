lead: anthropic/claude-fable-5-2/max mac-mini-worker
lease_until: 2026-11-16T05:44Z

# Row 1011, gap-pinned-cell-gauge-max: does the 2D pinned-cell stiffness iteration have a 4D SU(2) gauge form?

Worker: Claude Fable 5.2, max effort, Mac mini worker 1. Pinned at commit c216eeef9. Started 2026-11-15T17:44Z.
Research-stage working state. Nothing here is a claim of the mass gap or of any part of T0. Marks used: PROVED (written
by hand here, not yet checked by another model), ARGUED, OPEN, FAILS. A numeric run, if any, only refutes or guides.

Credit. The pinned-cell stiffness iteration is OpenAI's (posted, unrefereed preprints, github.com/openai/math commit
4eaee87548250b2682affda7d05d947c05554bae: "Sharp mass bounds for the two-dimensional O(4) model", Section 3; "The
canonical massive continuum limit of the two-dimensional O(3) model", Sections 2 and 8). The readings this row starts
from are rows 1007, 1009, 1010 of this lane. The Schrodinger-functional coupling is Luscher, Narayanan, Weisz, Wolff
(1992). Sussman and Alpoge (with Claude and Codex as authors of their text) are credited where their account is read.

## 0. Plan (save protocol; at most eight steps, one step per response, result appended before the next)

1. Read the inputs: `parts/gap.md`, rows 1009, 1010, 1007 in full, the exercise skill at main 8b11ae2bb9. Note what
   each gives. Then the registry grep (open-core, FINISH rows, idea digests) for every object the row names.
2. Read the primary text of the O(4) paper Section 3 at the points the transfer needs (class, stiffness, Ward
   identity, bracket gain, shell family), and state the 2D mechanism in one page as a list of steps with the
   property each step uses.
3. Task 1: state each piece on the 4D lattice: the class, the stiffness, the Ward identity with its bracket term,
   the family, the one-step gain.
4. Task 2: run the tests first (Lemma PT, Proposition NP, Theorem D2, Lemma SHEET at fixed b, compact U(1), frozen
   Q_8 and 2T, the five-dimensional test, the instanton and refilling obstruction).
5. Task 3: for the first piece that survives, prove it by hand or build the counterexample.
6. Task 4: if the one-step gain survives, its statement with constants, the remaining lemma to the 4D mixing bound
   and the exponent condition. If it does not, the exact step that fails and why.
7. Exercise-skill report: set-aside table, blockage sentence, what the next row should be (a complete brief).
8. Print every cited anchor, fix drift, write the RESULT line.

## Status log

- 2026-11-15T17:44Z: file created, plan written. Nothing read beyond GOAL.md, the FINISH head and the queue row.
- 2026-11-15T18:08Z: Step 1 done (inputs read, record located). See Section 1.
- 2026-11-15T18:32Z: Steps 2-3 written (Sections 2, 3): mechanism list; lattice class, Proposition A, Proposition W, log sum.
- 2026-11-15T18:35Z: Section 4 written: Propositions B, B', SEAG, Lemmas CEN, EMB; the first piece (twist with classical cost, start bound) FAILS for SU(2) in the class.

## 1. Step 1: inputs read, and where the lane's record sits (exercise step 0)

Model and provenance: Anthropic, Claude Fable 5.2, max effort, one session, no subagents. Nothing in this file is
checked by another model. The target is a standalone proof target, so the contract of `GOAL.md` (no
computer-assisted step, Lean-formalizable proofs) replaces the framework refresher read of the exercise skill.
The skill was fetched at main 8b11ae2bb9 with its reference `proof-search-governance.md` (both read in full).

Read in full: `parts/gap.md` (the state file), row 1009 (`library/prior/gap-o4-pinned-cell-read-opus.md`),
row 1010 (`library/prior/gap-o3-continuum-rg-read-opus.md`). Read in part: row 1007
(`library/prior/gap-2don-proofs-read-opus.md`, A(5) L84-100 and Step 6 L112-176).

What the inputs give (all OpenAI's mathematics, as restated by rows 1009 and 1010; unchecked):

- The 2D engine is a statement about one class C_b: every pinned square, every boundary pin, every strength field
  with |b_e| <= b (O(4): also signs and right twists). Monotone: the twist stiffness H_Q = direct cost minus
  current covariance (row 1009 L84). Start H <= b (L85). Step: H_c <= h on the class at side R gives H <= h - delta
  at side l R, delta >= (log l)/pi - C log B (O(4), L141-147) or (log l)/(4 pi) (O(3), L272).
- Why the step closes: (i) conditioning a square on cell rings gives cells of the same class, and the ring action's
  Hessian is the sum of cell stiffnesses, exactly (3.16) (L102-103); (ii) Gaussian augmentation turns "stiffness at
  most v" into "variance of the augmented current at least the gain" (3.19) (L107); (iii) a Brascamp-Lieb /
  Helffer-Sjostrand identity (3.21) and Cauchy-Schwarz give Var J(A) >= (signal)^2 / (cost) (3.50) (L139-140);
  (iv) the signal is the bracket term of the Ward identity: the derivative of the current J(A) along a rotation
  u_i about a perpendicular axis is 2 J(u_i A') with A' = -a x A (3.28)-(3.29) (L115-117); (v) the test directions
  are u_i = chi phi_i/|k_i| over a frequency annulus M <= |k| <= K_1, and the sum of |k|^(-2) over a 2D annulus is
  (1/(2 pi)) log(K_1/M) (3.37) (L127).
- After small stiffness: local rotations are cheap, coarse orientations, disagreement percolation, then abelian
  decompositions with association give mixing for all observables (L158-187). The seed follows by the coupling
  integral (3.70), which is the lane's Theorem D (f) (L190-195, L419).
- Row 1010: the band is crossed only by that mixing bound at one bare coupling; the RG only carries a box number
  across cutoffs under the exponent condition (8.3); its 4D transcription asks for a mixing exponent below 3/2
  times one loop (L202, unchecked).
- Row 1007 B(5) (L159-161): a constant gauge rotation of a pinned boundary layer is undone inside (SU(2) is
  connected); a local gauge change of variables gives no inequality on gauge-invariant data.

Where the lane's own record on the row's objects sits (located, NOT read yet; closed until the compare step):
Schrodinger functional: `gap-constraints-max.md`, `gap-crux-exercise-astra.md`, `gap-flux-exercise.md`,
`gap-form-exercise.md`, `gap-phys-seed.md`, `gap-skeleton-final.md`, `prior/gap-kflow-read-opus.md`,
`prior/gap-small-volume-lit.md`, `prior/gap-fullread-1.md`, `prior/gap-seed-lit.md`, `prior/gap-vir-lit.md`.
Stiffness: 20 gap files (among them `gap-sc-max.md`, `gap-fc-max.md`, `gap-hcphys-max.md`, `gap-tiltproof-max.md`,
`gap-direction2-max.md`, `gap-brainstorm-max.md`). "gauge wave": no file. `library/open-core.md` has no hit for
pinned, stiffness, Schrodinger, background field, helicity or step scaling.

Companion row 1012 (`gap-gauge-stiffness-read-opus`, queued at the same time, reading only) searches the published
literature on SF coupling rigour, gauge Ward identities and stiffness bounds, and gauge McBryan-Spencer bounds.
This row does not repeat that search; it uses the lane's files and the primary OpenAI text.

## 2. Step 2: the 2D mechanism as a list of properties (what a transfer must reproduce)

Source: OpenAI, O(4) paper Section 3 (p. 13 re-read in this row from the PDF at commit 4eaee8754; the rest through
row 1009's reading, lines cited in Section 1). The 2D engine uses exactly these properties.

- (M1) **A closed class.** Pinned squares, every pin, signed strengths |b_e| <= b, a fixed unit quaternion U_e on
  each bond (bond quaternion t_e + s_e = q_y U_e q_x^(-1)). Conditioning a square on its cell rings gives cells of
  the class.
- (M2) **A twist that is locally a symmetry.** The rotation q_x -> e^(a f_x) q_x changes the bond energy only through
  f_y - f_x (p. 13, (3.6)). A constant f costs nothing on EVERY configuration. So the twist is defined for every
  pin, and its direct cost is classical: D_f^2 A = sum_e w_e t_e (f_y - f_x)^2.
- (M3) **The start bound is free.** H_Q = direct cost minus current covariance, and |t_e| <= 1, so H_Q <= b I by
  dropping the covariance (3.5). In d = 2 this bound is scale invariant.
- (M4) **Exact Hessian of the ring action** = sum of cell stiffnesses at the local gradient (3.16).
- (M5) **A variance identity.** With Gaussian augmentation, stiffness = v |A|^2 - Var J(A) (3.19); a lower bound on
  a variance lowers the stiffness bound.
- (M6) **The bracket.** The derivative of the current J(A) along a rotation about a perpendicular axis is 2 J(u A'),
  A' = -a x A (3.28)-(3.29). For one axis there is no such term.
- (M7) **The log sum.** sum of |k|^(-2) over a 2D annulus = (1/(2 pi)) log (3.37).
- (M8) **From small stiffness to mixing.** Cheap local rotations, coarse orientations, disagreement percolation,
  abelian decompositions with association (not examined in this row: the transfer stops before it).

(M2) and (M3) carry everything that follows: they give a quadratic form on a fixed finite-dimensional space of
twists (constant 3 x 2 matrices), bounded uniformly over the class at the start.

## 3. Step 3 (Task 1): the pieces on the 4D lattice

Marks: DEF, PROVED (by hand here, checked by no one), ARGUED, OPEN, FAILS.

### 3.1 Conventions and the class (DEF)

G = SU(2) = unit quaternions; su(2) = Im H = R^3 with u.v and u x v; [u, v] = 2 u x v; for g in G write
t(g) = Re g = (1/2) tr g and s(g) = Im g. A link l = (x -> y) has tail x and head y; a gauge transformation acts by
U_l -> g_x U_l g_y^(-1). The plaquette p = (x; mu, nu) has links l_1 = (x -> x + mu), l_2 = (x + mu -> x + mu + nu),
l_3 = (x + nu -> x + mu + nu), l_4 = (x -> x + nu) and holonomy U_p = U_1 U_2 U_3^(-1) U_4^(-1), based at x.

**Cell.** A box c = product of intervals {0, ..., S_mu} in Z^4 (a cube when all S_mu = S). A link is a boundary link
if it lies in a boundary 3-face; a plaquette is a boundary plaquette if its four links are boundary links. A pin is
omega in G^(boundary links). Interior links carry Haar measure. Weight w_p = 1 / (number of cells of the tiling that
contain p), so 1, 1/2 or 1/4; adjacent cell actions then add to the action of the union (the 2D half weight).
Strengths |beta_p| <= b (signed), or beta_p in [0, b]. Action, partition function, free energy:

  A_c(U) = sum_p beta_p w_p t_p(U),   Z_c(omega) = int exp(A_c) dU_int,   F_c(omega) = - log Z_c(omega).

**The class C_b.** All (c, omega, beta). It is closed under conditioning on the links of the cell boundaries of a
tiling (Markov property: given those links the cell interiors are independent, each with a law of the class).
This is (M1); it holds for every gauge group. Signed strengths are the Z_2 two-form background (a centre twist of
the plaquette); a continuous non-central plaquette twist would break gauge invariance, so the class has no analogue
of the fixed quaternions U_e.

**Gauge covariance (PROVED, one line).** For g: sites of c -> G, Z_c(omega^g) = Z_c(omega): change variables
U -> U^g on the interior links; Haar measure and every t_p are invariant.

### 3.2 Link rotations, the current, the stiffness (Proposition A, PROVED)

A link field is B in su(2)^(links of c). It acts by (e^B U)_l = e^(B_l) U_l (B_l sits in the frame of the tail). For a
plaquette put

  c_1 = B_1,  c_2 = Ad(U_1) B_2,  c_3 = Ad(U_1 U_2 U_3^(-1)) B_3,  c_4 = Ad(U_p) B_4,   (a_1, ..., a_4) = (c_1, c_2, -c_3, -c_4),
  delta_p(B) = a_1 + a_2 + a_3 + a_4   (the covariant curl of B at p),      kappa_p(B) = sum over i < j of [a_i, a_j].

**Proposition A.** (i) U_p(e^(eps B) U) = E(eps) U_p with E(eps) = e^(eps a_1) e^(eps a_2) e^(eps a_3) e^(eps a_4), and
  t_p(e^(eps B) U) = t_p - eps delta_p . s_p - (eps^2/2) (|delta_p|^2 t_p + kappa_p . s_p) + O(eps^3).
(ii) Let B_bd be a field on the boundary links and B any extension to all links. Then
  F_c(e^(eps B_bd) omega) = - log int exp(A_c(e^(eps B) U)) dU_int,
and the second derivative at eps = 0 is
  H_c(omega; B_bd) = E sum_p beta_p w_p (t_p |delta_p|^2 + kappa_p . s_p) - Var(X_c(B)),    X_c(B) = - sum_p beta_p w_p delta_p . s_p.
It does not depend on the extension. (iii) With the extension by zero, X_c(B) = - sum over boundary links l of
B_l . N_l, where N_l = sum over plaquettes p containing l of (+ or -) beta_p w_p (s_p transported to the tail of l) is
the derivative of the action in the boundary link (a lattice Neumann datum). So the Hessian of the pinned free
energy is a boundary term minus the covariance of the Neumann data.

Proof. (i) Move each exponential to the left: e^(eps B_1) U_1 e^(eps B_2) = e^(eps c_1) e^(eps c_2) U_1, and so on; this gives
E(eps). In quaternions a_i a_j = - a_i . a_j + a_i x a_j, so E = 1 + eps delta + (eps^2/2)(- |delta|^2 + kappa) + O(eps^3),
and Re(u (t + s)) = - u . s for imaginary u. (ii) e^(eps B_l) is a fixed left translation on each interior link, so Haar
measure is invariant; F'' = - E[A''] - Var(A'). Two extensions differ by a field that vanishes on the boundary,
which is a change of variables. (iii) Collect the terms of X_c by boundary link. QED

For U(1) (all fields in one axis a): delta_p = a (d theta)_p, kappa_p = 0, and (ii) reads
H_c(omega; theta) = E sum_p beta_p w_p t_p (d theta)_p^2 - Var. So H_c <= b sum_p w_p (d theta)_p^2 for EVERY pin: (M2) and
(M3) hold for compact U(1), with the closed link shifts (the one-form symmetry) as the local symmetry.

### 3.3 The Ward identity with its bracket term (Proposition W, PROVED)

Let B vanish on the boundary links and let B' be any link field. For a plaquette, order the eight factors as
[c_1][c'_1][c_2][c'_2][-c'_3][-c_3][-c'_4][-c_4] and put kappa_p(B, B') = sum of [earlier, later] over the pairs with one
entry from B and one from B'. Then, in the law of (c, omega, beta),

  E[X_c(B) X_c(B')] = E sum_p beta_p w_p t_p delta_p(B) . delta_p(B')  +  (1/2) E sum_p beta_p w_p kappa_p(B, B') . s_p.

The first term is the contact term. The second is the bracket term. Its same-link part is
(1/2) sum_p beta_p w_p delta_p([B, B']) . s_p = - (1/2) X_c([B, B']) with [B, B']_l = [B_l, B'_l]: a current in the
commutator colour, as in (3.8) of the O(4) paper. For U(1) every bracket vanishes.

Proof. N(d, e) = int exp(A_c(e^(d B) e^(e B') U)) dU_int does not depend on d (left translation on interior links).
Take the mixed derivative at 0: E[D_d D_e A] + E[(D_B A)(D_B' A)] = 0. The d e coefficient of the plaquette word is the sum of
(earlier)(later) over mixed pairs; its real part against U_p gives - delta(B) . delta(B') t_p - (1/2) kappa(B, B') . s_p. QED

These are the Schwinger-Dyson (loop) equations at second order. They are exact for every pin and every group.

### 3.4 The family and the log sum (arithmetic, PROVED as a statement about sums)

For a lattice shell M <= |k| <= K in (2 pi/N) Z^d: (2 pi/N)^d sum |k|^(-d) = |S^(d-1)| log(K/M) + O(1/M) relative error.
d = 2: (2 pi)^(-2) 2 pi = 1/(2 pi), the O(4) paper's (3.37). d = 4: (2 pi)^(-4) 2 pi^2 = 1/(8 pi^2). So the 4D sum of
|k|^(-4) over a frequency shell is (1/(8 pi^2)) log(K/M) per unit volume. In d = 5 the same sum grows like K: no log.
The power 4 is what a second-order bracket gives: two fluctuating fields, each with variance of order 1/(h |k|^2),
against h^2 from the cubic term of the action. This is the place of the row's first seed. It is arithmetic only.

### 3.5 What is missing after 3.1-3.4

The class (M1), the exact formulas (M4 is the chain rule applied to a sum of cell free energies), the identity with
a bracket (3.3) and the log sum (3.4) all exist on the lattice. What 3.2 does not give is (M2)-(M3): for SU(2) the
direct term t_p |delta_p|^2 + kappa_p . s_p depends on the configuration through the adjoint transports, and it is not
the classical curl energy of B. Section 4 proves that this cannot be repaired inside the class C_b.

## 4. Step 5 (Task 3): the first piece, (M2)-(M3), fails in the class C_b for SU(2). Proofs

All statements here are PROVED by hand in this row and checked by no one, unless marked otherwise.

### 4.1 Proposition B (covariance of the pin supremum)

For g: sites -> G put (Ad_g B)_l = Ad(g_tail(l)) B_l. Then for every cell, pin, strength field and boundary field B:

  H_c(omega; B) = H_c(omega^g; Ad_g B),   so   sup over pins of H_c(omega; B) = sup over pins of H_c(omega; Ad_g B).

Proof. (e^(eps B) omega)^g = e^(eps Ad_g B) omega^g link by link, and F_c is gauge invariant (3.1). QED

So the supremum over pins sees B only up to an independent rotation of its colour at every site. For U(1) the
rotation is trivial. For SU(2) the orbit of a fixed-colour field a theta is the set of all fields theta_l n_tail(l) with
n: sites -> S^2 arbitrary. A uniform bound cannot use the colour coherence of B. The curl energy of a theta uses
exactly that coherence.

### 4.2 Proposition B' (no pin-uniform curl bound; the class supremum is mass-like)

Let c be any box with at least one boundary plaquette, b > 0, G = SU(2). There is NO constant K such that
H_c(omega; a theta) <= K inf over extensions of sum_p w_p (d theta~)_p^2 for all pins, all strength fields in [0, b] and all
real boundary fields theta. More precisely, for the strength field beta = b on the boundary plaquettes and 0 inside:

  sup over pins of H_c(omega; a theta) >= b sup over n of sum over boundary plaquettes of w_p |d(theta n)_p|^2,

and the right side is positive for some closed theta (curl energy 0), and is at least
b sum over boundary plaquettes of w_p (theta_2(p)^2 + theta_3(p)^2 + (theta_1(p) - theta_4(p))^2) (average over independent signs).

Proof. With that strength field the interior integral is trivial, so F_c(omega) = - b sum over boundary plaquettes of
w_p t_p(omega), and by Proposition A (i) at omega = 1 (t_p = 1, s_p = 0): H_c(1; B) = b sum w_p |B_1 + B_2 - B_3 - B_4|^2
for every su(2)-valued boundary field B. By Proposition B, sup over pins of H_c(omega; a theta) >= H_c(1; theta n) for
every n. For theta = d lambda with lambda the indicator of one boundary site z, and a plaquette with x + mu = z:
d(theta n)_p = n_x - n_z, which is not zero when n_x differs from n_z. For the second bound take n_x = eps_x a with
independent signs eps_x: the tails of l_1, ..., l_4 are x, x + mu, x + nu, x, so d(theta n)_p = a [eps_x (theta_1 - theta_4) +
eps_(x+mu) theta_2 - eps_(x+nu) theta_3], and the mean of its square is the stated sum. QED

Reading. For the potential of a constant field strength f on a cube of side S, theta is of order f S on most
boundary links. So the class supremum of the response is at least of order b f^2 S^5, against the classical
b f^2 S^4. The hypothesis "H_c <= h on constant twists, uniformly over the class", normalised by the classical
action, is false for SU(2) at every scale and every h, already at the start. For U(1) it is true with h = b (3.2).
With a homogeneous interior strength b the same conclusion is ARGUED only (a rough pure-gauge pin turns a theta into
a rough field at the trivial pin; its cost is of order b per link at large b by the classical action; not proved
here for all b).

### 4.3 Lemma CEN (the only link symmetries are central)

Let h be a configuration-independent field of group elements on the links of one plaquette, with
t_p(h U) = t_p(U) for all U. Then every h_l is +1 or -1 and h_1 h_2 h_3 h_4 = 1.

Proof. Re(X U) = Re(X' U) for all U in SU(2) forces X = X' (the unit quaternions span H). Varying U_1 gives
h_2 U_2 U_3^(-1) h_3^(-1) U_4^(-1) h_4^(-1) h_1 = U_2 U_3^(-1) U_4^(-1) for all U_2, U_3, U_4. With U_3 = U_4 = 1 and U_2 = 1:
h_2 h_3^(-1) h_4^(-1) h_1 = 1; then h_2 U_2 h_2^(-1) = U_2 for all U_2, so h_2 is central. The other links are the same. QED

So (M2) has no SU(2) form with constant link rotations: the "locally a symmetry" twists of the class are the
closed Z_2 link fields. Their twists are the signed strengths with d sigma = 0, that is the flux insertions the lane
already uses (Theorem D (e), flux sectors). On a cube with pinned boundary every closed Z_2 two-cochain is exact
relative to a change of pin, so a cube has no topological twist at all. A discrete twist has no Hessian, so (M5)
and (M6) have nothing to act on.

### 4.4 Proposition SEAG (the direct term is not classical, even at the trivial pin)

Let z be an interior site of c all of whose neighbours are interior sites, lambda the indicator of z, and
B = a d lambda (so B is curl free, B_l = +a on links with head z, -a on links with tail z, 0 elsewhere; it vanishes on
the boundary). Then, in the law of any (c, omega, beta),

  E sum_p beta_p w_p (t_p |delta_p(B)|^2 + kappa_p(B) . s_p) = Var X_c(B) = 2 sum over p containing z with base(p) != z of beta_p w_p E[t_p].

In a homogeneous interior this is 36 b E[t_p], not 0.

Proof. The first equality is Proposition W with B' = B (kappa_p(B, B) = 2 kappa_p(B), and H_c = 0 for a field that
vanishes on the boundary). For the value, sort the 24 plaquettes at z by the corner where z sits. Base at z: l_1
and l_4 have tail z, the deformation is the gauge transformation e^(-eps a) at z on this plaquette, and the term
vanishes identically (direct check: with U_p = cos phi + s^ sin phi, t |a - Ad(U_p) a|^2 = 4 sin^2 phi cos phi |a_perp|^2 and
kappa . s = - 4 sin^2 phi cos phi |a_perp|^2). At the other three corners the two links at z have transported colours
that differ by Ad of a link variable ending at an interior site; averaging over the gauge transformation at that
site (which leaves t_p, s_p and the law invariant) kills the cross terms and kappa, and leaves t_p (1 + 1). QED

Meaning. In the 2D model the start bound H <= b is "drop the covariance". For SU(2) gauge fields the direct term
of a fixed-colour field contains a term of order b times the L^2 norm of theta (interior links are Haar distributed
by gauge invariance, so a fixed colour is a random colour). An upper bound on the stiffness then needs a LOWER
bound on the current variance that cancels this term exactly. The only exact tool for that is Proposition W, and
it gives the cancellation only for fields that vanish on the pins. The statement "H_c(1; a theta) <= b times the
classical action of the harmonic extension" (a Schrodinger-functional coupling at least the bare one, at the
trivial pin) is OPEN; it is not a one-line bound.

### 4.5 Lemma EMB (where the 2D class sits inside the gauge class)

Let c = {0,1,2} x {0,1} x {0,...,S}^2 with coordinates (x_0, x_1, y), y in {0,...,S}^2. Its only interior links are the
direction-1 links q_y := U_1(1, 0, y) with y in the open square, and the direction-1 links at x_0 = 1 with y on the
boundary of the square are pinned. Put strength 0 on the plaquettes of the (0,1) planes and take the trivial pin
on the face x_1 = 0. Then the law of (q_y) is exactly a member of OpenAI's local class of Section 3.1 on Q(S):
bond quaternion q_y' U_e q_y^(-1) with U_e = (the pinned link of the face x_1 = 1 over the bond)^(-1), strengths
beta_p (signed if allowed), half weight on tangent boundary bonds. Every member of that class arises this way.

Proof. Each link in direction 0, 2 or 3 has x_1 in {0, 1} and lies in a face x_1 = const; direction-1 links with
x_0 in {0, 2} or y on the boundary lie in a face. For the plaquette ((1, 0, y); 1, k), k = 2, 3:
t_p = Re(q_y u_k(1,1,y) q_(y+k)^(-1) u_k(1,0,y)^(-1)) = Re(q_(y+k) u_k(1,1,y)^(-1) q_y^(-1)) when u_k(1,0,y) = 1. The plaquette
lies in a boundary face exactly when the bond is tangent to the boundary of the square, where w_p = 1/2. QED

Consequences. (a) On these members the fixed-colour field B = a f(y) on the direction-1 links is the O(4) left
rotation. The flat face x_1 = 0 supplies the global colour frame that a general pin does not have. So the 2D
engine runs inside the gauge class on such sheets, as the 2D engine and at the 2D rate. (b) With a pure-gauge pin
on x_1 = 0 the same holds after q -> h^(-1) q. With a curved pin on x_1 = 0 the bond is L q R q'^(-1) with two-sided
twists, the left symmetry is broken, and the member is outside OpenAI's class. (c) A class that contains thin
boxes contains the 2D O(4) class at coupling b. Any length X(b) for which a statement holds uniformly on such a
class is at least the 2D O(4) length. (d) These sheets are the objects of Theorem D2 (row 977,
`library/gap-tiltproof-max.md` L240: the tilt that pins directions 2, 3 "leaves exactly O(4)-symmetric sheets").
Cubes with boundary pins only do not contain them.

### 4.6 Remark HOPF (ARGUED; standard topology, not rebuilt)

For a smooth boundary gauge function g: S^3 -> SU(2) of degree k, the frame n = Ad(g) a: S^3 -> S^2 has Hopf
invariant k. If k != 0 it has no extension to the ball without zeros (pi_3(S^2) = Z). On the lattice the pin 1^g
is exactly gauge equivalent to the trivial pin, so C_b has no topological sectors. The remark says that a "smooth
colour frame adapted to the pin", the object that would replace the missing global frame, cannot exist for all
pins even among pure-gauge ones. This is the place where pi_3(SU(2)) = Z meets the stiffness, beside the refilling
step of row 1010.

### 4.7 Verdict on the first piece

- The class (M1): exists (3.1). The exact Hessian (M4): exists (chain rule). The identity with a bracket: exists
  (Proposition W). The log sum: exists in d = 4 (3.4).
- The twist with a classical direct cost, (M2), and the free start bound, (M3): **FAIL for SU(2) in C_b**
  (Propositions B, B', Lemma CEN, Proposition SEAG). They hold for compact U(1), where the gain is zero.
- What survives: (i) the sheets of Lemma EMB, which are the 2D model; (ii) the abelian pins (omega in one maximal
  torus), where a theta is a symmetry direction of the PIN family and F_c depends on d theta only. The abelian pins
  are not closed under conditioning: the ring links of a tiling are non-abelian and rough, and for them 4.2 applies.
- So the pinned-cell iteration, as a class-supremum induction, has no 4D gauge form with constant link twists.
  The row's third seed (a Schrodinger-functional stiffness uniform over all Dirichlet data) is refuted in this
  form. The first and second seeds (log sum, bracket) are true as identities and have no class to act on.
