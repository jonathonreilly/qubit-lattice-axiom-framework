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

**Status block.** Step 1 inputs: done (Section 1). Step 2 mechanism list: done (Section 2). Step 3 lattice
statements: done (Section 3; Propositions A, W). Step 5 first piece: done (Section 4; it FAILS for SU(2), with
proofs and one passing numeric control). Step 4 tests: done (Section 6). Step 6 one-step gain: no statement exists
(Section 7). Compare with earlier work: Sections 5 and 8. Report and RESULT: Section 9. The sections are in work
order; read 9.1-9.2 first, then 4.7.

**What this run did not cover.** OpenAI's O(4) paper was re-read at p. 13 only; everything else of both OpenAI
papers is used through rows 1009 and 1010 (readings, unchecked). The part of the 2D proof after small stiffness
(coarse orientations, association) was not examined. No published literature was searched (companion row 1012);
Luscher, Narayanan, Weisz, Wolff and Durhuus, Frohlich are RECALLED or cited through lane files. PRs #10133,
#10134, #10141, #10144 were not searched. No typical-pin form was formalised or tested.

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
- 2026-11-15T18:41Z: GUIDE control of Proposition SEAG run (PASS at three points, 4.8); Sections 5 (compare) and 6 (tests) written.
- 2026-11-15T18:43Z: Section 7 written: Task 4 has no statement (fails at the twist); Lemma FR; the missing objects (N1)-(N3).
- 2026-11-15T18:45Z: Sections 8 (cross-branch search) and 9 (report, work items, registry, RESULT) written. Run ended after the anchor check.

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

Reading (ARGUED for the constants). For a potential theta of a constant field strength f on a cube of side S, a
boundary square of side r has |sum of theta around it| = |f| r^2, so the sum of theta^2 over its 4 r links is at least
f^2 r^3/4 (Cauchy-Schwarz). Nested squares in the slices of the boundary faces give sum of theta^2 over boundary links of
order f^2 S^5 for EVERY choice of the potential. So the class supremum of the response is at least of order
b f^2 S^5, against the classical b f^2 S^4: the best constant h in "H_c <= h times the classical action, uniformly on
the class" is at least of order b S. It grows with the scale; it does not start at b and decrease. For closed theta
no constant works. For U(1) the bound holds with h = b at every scale (3.2). With a homogeneous interior strength b
the same conclusion is ARGUED only (a rough pure-gauge pin turns a theta into a rough field at the trivial pin; at
large b its cost is of order b per link by the classical action; not proved here for all b).

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

### 4.8 GUIDE control of Proposition SEAG (run 2026-11-15 18:40Z; it decides nothing)

Script `/tmp/row1011-scripts/seag.py` (plain numpy, quaternion links, checkerboard heat bath, periodic lattice;
outputs in `/tmp/row1011-out/`; numeric lock held as `row1011-fable` and released; memory 69 percent free).
Reading written before the run: PASS if E[X^2], -E[D_B^2 A] and 36 b E[t_p] agree pairwise within 3 standard
errors, for B = a d(indicator of z), averaged over the sites z. FAIL would mean an algebra error in 3.2, 3.3 or 4.4.

| lattice, b | E[X^2] | -E[D_B^2 A] | 36 b E[t_p] | largest pairwise difference |
|---|---|---|---|---|
| 4^4, 1.0 | 8.732(28) | 8.773(17) | 8.768(17) | 1.1 s.e. |
| 4^4, 2.3 | 50.45(28) | 50.43(10) | 50.41(9) | 0.5 s.e. |
| 6^4, 2.6 | 62.77(16) | 62.84(5) | 62.77(3) | 1.95 s.e. |

Result: PASS at the three points (7 to 8 seconds each). The mean plaquettes 0.2436, 0.6088 (a 4^4 box), 0.6706
are in the known range, so the sampler is sane. The run supports the algebra; the proof is the text of 4.4.

## 5. Compare with the earlier work (exercise step 5; searched: `library/gap-*.md`, `library/prior/gap-*.md`,
## `parts/gap.md`, `library/open-core.md`, the FINISH rows, by the words listed in Section 1 and Durhuus, chiral
## model, Schwinger-Dyson, Makeenko, Dirichlet-to-Neumann, one-form symmetry, abelian projection, vortex free energy)

| Item of this row | Already in the lane? | Where | Credit |
|---|---|---|---|
| Lemma CEN (only central link symmetries) | partly: stated as a GUIDE remark, not proved | `gap-crux-fp.md` L88 ("The centre of SU(2) is finite ... SU(2) has no other continuous symmetry") | row 712 |
| Lemma EMB (the layer of one link direction is a chiral model in a background) | yes for the layer model with two-sided background; the exact match with OpenAI's local class (pins, signs, right twists, half weights) on the box {0,1,2} x {0,1} x Q(S) is not on file | `gap-crux-fp.md` L369-373 (layer model I(u, v)); `gap-arealaw-opus.md` Lemma S (row 825); `gap-tiltproof-max.md` L240 (D2's O(4) sheets) | Durhuus and Frohlich 1980 (idea; the lane records their paper as read by row 831); rows 712, 825, 977 |
| "The flat background is not the worst": equal rough slices break the slab symmetry to Z_2 and the slab can order | yes (ARGUED there) | `gap-brainstorm2-max.md` L263 (G8) | row 876 |
| Proposition W (second-order Schwinger-Dyson for the action) | partly: the lane has the first-order Ward form for Wilson loops | `gap-loop-eq-opus.md` Lemma 1.1, 1.2 (row 754) | row 754 |
| Proposition A (iii), the Neumann datum | partly: the first-step electric field as a score | `gap-sgstep-opus.md` Section 2 (row 944, Lemma TG / EF, per the lane index) | row 944 |
| Proposition B, B' (covariance of the pin supremum; no curl bound) | not found (no hit for a pin supremum, a covariance of the supremum, or a Schrodinger-functional bound uniform in boundary data) | scope as in the heading | - |
| Proposition SEAG | not found | same scope | - |
| The gauge "twist" has no continuous form on gauge-invariant data | yes, at reading level | row 1007 B(5), `prior/gap-2don-proofs-read-opus.md` L159-161; row 1009 Step 7 rows 2-4 | rows 1007, 1009 |

What the fresh pass added: Propositions A, W as exact lattice statements, Propositions B, B', SEAG, and the exact
form of Lemma EMB. What it only found again: CEN's content, the layer model, the G8 warning.

Two reading-level remarks of row 1009 are corrected by Section 4 (ARGUED until checked):
- Row 1009 Step 7, row 3 (L406): a Schrodinger-functional form of H <= b "would follow the same way by dropping a
  variance". It does not: by Proposition SEAG the direct term is not classical, at any pin.
- Row 1009 Step 6 note (i) (L387-390): "an UPPER bound on a response ... is the direction a supremum over pins can
  keep". For SU(2) the supremum over pins of the response to a fixed-colour field is not bounded by the classical
  action (Proposition B'). The binding fact is gauge covariance, not Theorem D2.

## 6. Step 4 (Task 2): the tests

"Candidate" below means the class-supremum iteration of Section 3 with constant link twists. After Section 4 it
has no start, so most tests are answered by what they say about the surviving pieces.

| Test | What it was run on | Result |
|---|---|---|
| Compact U(1): the gain must be zero | Propositions A, W with all fields in one axis | PASS, and it locates the failure. For U(1): kappa = 0, every bracket in Proposition W vanishes, the twist is the one-form symmetry, H_c <= b on the whole class, and no step lowers it. For SU(2): the brackets are there and the symmetric twist is not (Lemma CEN). The 2D O(N) models have both at once; the two gauge models have one each. |
| Lemma PT (product with a massless factor), `gap-crux-exercise3-max.md` L690 | a gain statement for SU(2) x Villain U(1) | Not reached: no gain statement exists. On the sheets of Lemma EMB the answer is row 1009's (the step reads one factor). |
| Proposition NP, `gap-crux-exercise4-max.md` L383 | the candidate | Passes trivially: no value of D is read. |
| Theorem D2, `gap-tiltproof-max.md` L240 | the supremum over boundary pins | D2 does not bind a class of cubes with boundary pins: its sheets need links pinned in the interior. It binds every class that contains thin boxes or interior pins, through Lemma EMB, as a constraint and not a refutation: by D2 5.4 the sheet structure factor is at least A (1/4 - G_S/b) with G_S about (1/(2 pi)) log S + 0.0488, positive while log S < (pi/2) b - 0.31. So a statement of mixing uniform on such a class has a length of at least order e^((pi/2) b) (ARGUED from D2 5.4: mixing with length X bounds the sheet structure factor by a constant times X^2; D2 itself is PROVED GIVEN its two ported inputs, rebuilt in row 1000). What binds the cube class is Proposition B' (gauge covariance). |
| Lemma SHEET at fixed b, `gap-sepinput-max.md` L358 | strengths in [0, b] | Does not bind: its proof needs the coupling on the tube to tend to infinity. At fixed b the frozen structures come from pins, not strengths: Lemma EMB. |
| The G8 warning, `gap-brainstorm2-max.md` L263 (added test) | classes with thin boxes | A thin box with equal curved faces is a 2D model whose continuous symmetry is broken to Z_2 by the background; the lane ARGUES it can order like an Ising model. If so, NO statement of mixing holds uniformly on a class with thin boxes at large b. OpenAI's class avoids this because its twists are one-sided. Not rebuilt here. |
| Frozen Q_8 and 2T, `parts/gap.md` L199 | Sections 3-4 | The derivatives of Propositions A, W do not exist for a finite group. Lemma CEN holds with the same centre Z_2. So whatever survives Section 4 for SU(2) (the central twists) holds verbatim for Q_8 and 2T, which have degenerate flat states at large coupling. A gauge gain must therefore use the Lie algebra, that is exactly the part with no class. PASS as a constraint; it leaves nothing to test. |
| Five dimensions, `gap-crux-fp.md` L76, L266 | Sections 3-4 | Everything in Sections 3 and 4 is dimension free except 3.4: the sum of the inverse fourth powers is a logarithm only in d = 4, and the classical action of a constant-field twist is scale invariant only in d = 4. Proposition B' fails the candidate in every dimension. Lemma EMB's sheets exist in every d >= 3 and are 2D models, so a gapped sheet says nothing about the bulk (in 5D the bulk is believed massless at weak coupling). |
| Instantons and refilling, row 1010 L136, L201 | the pinned class | On the lattice a pure-gauge pin of any winding is exactly gauge trivial (3.1), so C_b has no sectors and the test does not bind the class. It binds any repair by smooth frames (Remark HOPF) and the carry across cutoffs (row 1010), which this row does not reach. |
| Row 1010's exponent condition (L202, unchecked): mixing exponent below 3/2 of one loop | the sheets | ARGUED arithmetic. With beta = 4/g^2 and b_0 = 11/(24 pi^2), one loop gives log(xi) = (3 pi^2/11) b = 2.69 b for 4D SU(2); the 2D O(4) sheet has log(xi) = pi b (OpenAI, O(4) mass paper). The ratio is 11/(3 pi) = 1.17, inside 3/2. So one-sided sheets alone would not break the 4D exponent condition; two-sided ones (G8) are another matter. |

## 7. Step 6 (Task 4): the one-step gain has no statement in the class; what a 4D form would need

### 7.1 The exact step that fails

The 2D induction hypothesis is "H_c(A, A) <= h |A|^2 for constant twists A, uniformly on the class". A gauge form
needs, for every cell of a tiling and every ring configuration, a boundary field that (i) is the restriction of
one field on the ring links and (ii) is "constant" in a sense in which its direct cost is the classical action.
Proposition B says the supremum over pins forgets the colour coherence of the field. Proposition B' says the
classical normalisation is then false at every scale. Lemma CEN says no exact symmetry restores it. Proposition
SEAG says the start bound is not "drop the covariance" even at the trivial pin. So the one-step gain cannot be
written as a statement on C_b: it FAILS at (M2), before any constant. Task 4 has no statement to give.

### 7.2 The three seeds of the row

- Seed 1 (scale invariance; waves on frequency shells): true as arithmetic. The classical action of a
  constant-field twist is scale invariant in d = 4, and the shell sum of |k|^(-4) is (1/(8 pi^2)) log (3.4). It has
  no class to act on: along a fixed-colour wave the Hessian of the ring action is mass-like, not k^2-like (4.4).
- Seed 2 (the bracket of the field strength): true as an identity, Proposition W. The same non-commutativity that
  gives the bracket removes the symmetric twist (Lemma CEN). In the 2D model the two are separate: the symmetry is
  exact and the bracket only rotates the current.
- Seed 3 (a Schrodinger-functional stiffness uniform over all Dirichlet data): FAILS (Proposition B').

### 7.3 Lemma FR (a colour frame costs at least the non-abelian part of the pin; PROVED)

For a unit-vector field n on the sites put D_l n = n_tail(l) - Ad(omega_l) n_head(l) (the covariant difference; it is
gauge covariant). For every plaquette p with base x,

  2 |s_p(omega) x n_x| = |(1 - Ad(omega_p)) n_x| <= |D_(l_1) n| + |D_(l_2) n| + |D_(l_3) n| + |D_(l_4) n|.

Hence, with lambda_x(omega) = min over unit n of the sum over plaquettes p based at x of |s_p x n|^2 and
NA(omega) = sum over sites of lambda_x(omega): every frame has sum over links of |D_l n|^2 >= NA(omega)/6.

Proof. Telescope n_x - Ad(omega_p) n_x along the four links; each term is a rotated D_l n. Ad(omega_p) is the rotation
about s_p by twice the class angle, so |(1 - Ad(omega_p)) n| = 2 |sin phi_p| |n_perp| = 2 |s_p x n|. Square and use
(a_1 + ... + a_4)^2 <= 4 sum a_i^2: |s_p x n_x|^2 <= sum over the links of p of |D_l n|^2. Sum over p; a link lies in at
most 6 plaquettes. QED

Use. The exact relation between a frame twist and a gauge transformation is theta n = d lambda n with
(d lambda)_l n_tail = [gauge direction of - lambda n]_l + lambda_head D_l n (direct computation from 3.1: the gauge
direction of mu n is mu_tail n_tail - mu_head Ad(omega_l) n_head). So the Ward identity of
the U(1) about n fails exactly by the frame defect D n, and the direct term along theta n has a mass-like part of
order b theta^2 |D n|^2. NA(omega) is zero only when all plaquette axes at each site are parallel (an abelian pin).
ARGUED size: for a typical configuration at coupling b, |s_p|^2 is of order 1/b with independent directions, so
NA is of order (number of sites)/b and the mass-like part is of order theta^2 per plaquette, with no factor b. For
the potential of a constant field this exceeds the classical b f^2 S^4 once S^2 is above order b. So no choice of
frame removes the term on typical link-level pins beyond log S = (1/2) log b; only a cancellation against the
current variance can, and Proposition W gives that cancellation only for exact symmetries.

### 7.4 What a replacement would have to supply (each is OPEN; none is attacked here)

- (N1) **A frame on typical ring configurations.** A gauge-covariant, ring-measurable frame whose defect is small
  on the cells of the tiling, with the rare cells where it is not small controlled (Remark HOPF: it cannot exist
  on all pins). This is a small-field / large-field statement about typical fields. It is the account's kind of
  object, not a class supremum.
- (N2) **The cancellation of the mass-like term.** An exact or controlled Ward identity for the U(1) about the
  frame, with the defect term of 7.3 bounded. In the continuum this is background gauge invariance.
- (N3) **The gain.** Then the bracket of Proposition W and the shell sum (1/(8 pi^2)) log would enter as in the 2D
  proof. The orbital (diamagnetic) part of the one-loop response has the sign that RAISES the stiffness; the
  spin (bracket) part lowers it and is larger (RECALLED: the split 11/3 = 4 - 1/3 of the one-loop coefficient).
  A variance lower bound would have to capture the bracket part while (N2) controls the other. Not derived here.
- Kind under lead rule W2: (N1)-(N3) read typical fields of the Wilson measure at small effective coupling. That
  is the (K-flow) kind with first-passage data. The frame exists only while the non-abelian part of the
  block-scale field is small, that is above the band. So this repair does not cross the band by itself (reading).
  The 2D engine crosses its band because its twist is defined on every configuration at every coupling.

### 7.5 A reading of the right uniform object (reading; one identity PROVED)

By Proposition A (iii) the Hessian of the pinned free energy is a boundary term minus the covariance of the
Neumann data N_l. For two boundary fields with supports that share no plaquette, the mixed second derivative is
exactly - Cov(N(B), N(B')). So the class-uniform, gauge-covariant object that the gauge theory does have is the
boundary-to-boundary covariance of the Neumann data across a cell, a mixing statement between parts of the
boundary, uniform over pins. In the 2D model the global symmetry gives a sum rule that turns this into a
stiffness with a classical normalisation; the gauge class has no sum rule (Lemma CEN). A uniform bound on that
covariance is a finite-size mixing condition of Dobrushin-Shlosman type. On classes with thin boxes it is
constrained by Theorem D2 and threatened by the G8 warning (Section 6). No attack here.

## 8. Repo search across branches (rule "Repo first"; finished 2026-11-15T18:44Z by the file time of its output)

Bare blob-less depth-1 fetch of `main` and of PR #10114 into `/tmp/row1011-git` (nothing in the checkout touched).
Searched for Schrodinger functional, pinned cell, stiffness, helicity modulus, background field: on main in the 67
`.md` files with ym4d in the path; on PR #10114 in 44 files of `agents/ym4d-proof/` picked by name (mass gap,
coupling, flux, twist, background, sigma, RTARGET). Hits: main, 7 files of `research/ym4d/library/` for "background
field" only (the existence chain's Balaban backgrounds); PR #10114, `FINITE_COUPLING_KERNEL_ASTRA.md` and
`UNIFORM_ONE_LOOP_COUPLING_ASTRA.md` use "stiffness" for the kernel constant of the soft-kernel route, and
`RTARGET.md`, `BARE_DETERMINANT_COUPLING_ASTRA.md` have "background field" only. No pinned-cell argument, no
Schrodinger-functional coupling and no gauge twist stiffness on either branch. PRs #10133, #10134, #10141, #10144
were not searched (10134 is an older copy of this folder; the others hold existence-chain files, per the lane's
notes). The search by names is bounded: it is "not found in the files searched", not "absent".

## 9. Report (exercise step 9)

Every statement below carries the mark of the section it comes from. Nothing is checked by another model.

**9.1 The wall, in plain words.** OpenAI's two-dimensional proof takes a block of a magnet with its edge held fixed
and twists it slowly. A slow twist is cheap on every arrangement of the spins, because turning all spins together
costs nothing. The proof shows that the block resists the twist less at each larger size; the reason is that
rotations about different axes do not commute. Once the block is soft, order is lost and a mass gap follows. The
row asked whether the same step-by-step argument can be written for the four-dimensional gauge field. What
happens instead: the gauge field has no operation that plays the part of "turn all spins together", except
multiplying by -1. The evidence covers the argument in its uniform form, over every boundary condition. It does
not cover forms that hold only for typical fields. Getting past it needs a twist that is cheap on every block.

**9.2 What the exercise found.**
1. The pieces that are identities exist on the lattice and are proved here: the class of pinned cells, the exact
   formula for the response to a link rotation (Proposition A), the Ward identity with a bracket term
   (Proposition W), and the 4D log sum (1/(8 pi^2)) log (3.4). PROVED, unchecked.
2. The piece that carries the 2D proof does not exist for SU(2): a twist whose direct cost is the classical action
   on every pin. The supremum over pins is blind to the colour coherence of the twist (Proposition B); the best
   uniform constant grows like b S instead of starting at b (Proposition B'); the only link symmetries are central
   (Lemma CEN); the start bound is not "drop the covariance" even at the trivial pin (Proposition SEAG, with a
   passing numeric control, 4.8). PROVED, unchecked; the scaling constants are ARGUED.
3. Compact U(1) has the twist and the start bound, and zero gain. SU(2) has the bracket and no twist. The 2D
   models have both. This is the structural reason in one line (PROVED as the sum of 3.2, 3.3, 4.3).
4. The 2D class sits inside the gauge class exactly, on thin boxes with one flat face (Lemma EMB; the layer idea
   is Durhuus and Frohlich's and is on file in rows 712, 825, 977). It says nothing about the bulk.
5. A repair needs a colour frame, which costs at least the non-abelian part of the pin (Lemma FR, PROVED). Such
   a frame can exist only on typical small-field configurations, that is above the band (reading). So the row's
   question "does the iteration itself have a 4D gauge form" has the answer: not as a class-supremum induction;
   a typical-field form would be of the first-passage kind and would not cross the band by this mechanism.

This run did not pass the wall. It produced a located failure with proofs, and no new route with a consumer.

**9.3 Filters corrected.** Two reading-level remarks of row 1009 (Section 5, end): a Schrodinger-functional start
bound does not follow by dropping a variance; and an upper bound on a response is not kept by a supremum over
pins for SU(2). One test reading: Theorem D2 does not bind a class of cubes with boundary pins; Proposition B'
does (Section 6). No lead rule of `parts/gap.md` changes.

**9.4 Routes worth doing.** One, and it is a check: W1 below. No attack route is proposed from this mechanism.

**9.5 What not to do next.**
- Another transfer of the pinned-cell iteration with constant link twists, or with a Schrodinger-functional
  coupling taken uniformly over boundary data: refuted in that form (4.2).
- A frame by gauge fixing on all pins: Lemma FR and Remark HOPF.
- An argument from the sheets of Lemma EMB to the bulk: the sheets are 2D models in every dimension d >= 3.
- A class of boxes of all shapes with uniform mixing as hypothesis: Theorem D2 constrains it and the G8 warning
  (ARGUED in row 876) says it is false at large b.

**9.6 The exact price.** Not found. What is located: the 2D engine uses an exact continuous symmetry that acts on
every configuration, and SU(2) lattice gauge theory has none beyond the centre (Lemma CEN). This is a necessary
condition for this engine, not an equivalence for the wall (W).

**9.7 Work items.**

W1 (check; a model that did not write this file; Claude Opus 5.5 high or gpt-6-astra). Read
`library/gap-pinned-cell-gauge-max.md` Sections 3 and 4 and 7.3 at the commit that holds it. Redo by hand, in this
order: (i) Proposition A (i): the expansion of t_p(e^(eps B) U) to second order, with the quaternion rules of 3.1;
(ii) Proposition W: the mixed coefficient and its same-link part; (iii) Proposition B and B': the covariance rule
with the tail convention, the value H_c(1; B) for the boundary strength field, the two lower bounds; (iv)
Proposition SEAG: the four corner cases, the gauge-averaging step, the count 6 + 18; (v) Lemma CEN; (vi) Lemma EMB
against p. 13 of OpenAI's O(4) paper (github.com/openai/math commit 4eaee87548250b2682affda7d05d947c05554bae,
`preprints/Sharp-mass-bounds-for-the-two-dimensional-O4-model-September-23-2026/paper.pdf`, fetch into a new empty
/tmp folder); (vii) Lemma FR. Test first: (a) in 4.2, is the strength field (b on boundary plaquettes, 0 inside)
inside the class the row means; (b) in 4.4, does the base corner vanish identically; (c) the sign in 7.3 "Use".
Verdict per statement: ADVANCE, CORRECT-NO-ADVANCE or WRONG with the failing line. Also judge the two corrections
of row 1009 in Section 5. Stop rule: stop at the first WRONG that breaks 4.7 and report it. Output
`library/gap-pinned-cell-gauge-check-<model>.md`. No new attack.

Not proposed, with reasons:
- An attack on (N1)-(N3) of 7.4: it is a typical-field statement at small effective coupling; the lane's record
  says no input carries such a statement across the band (`parts/gap.md` L41-43), and this row adds none.
- A proof of the G8 warning (a Peierls argument for a thin box with equal curved faces): it would close the
  uniform-class door for thin boxes by proof, but no route on the path of (W) consumes it.
- A 3D corollary (area law for 3D SU(2) from the 2D O(4) results through the layer comparison): off the 4D
  path, and the layer model there has two-sided backgrounds, which OpenAI's theorems do not cover.
- The Schrodinger-functional bound at the trivial pin, H_c(1; a theta) <= b times the classical action (4.4): OPEN,
  no consumer in the lane.
- A numeric measurement of the Hessian on typical pins in a smooth gauge: guide only; no decision of the lane
  moves on it.

**9.8 Approach registry (proof-search governance).**

| Family | Object | Mechanism | Terminal obligation | Strength vs (W) | Status | Evidence | Reopen condition |
|---|---|---|---|---|---|---|---|
| G1 class supremum, constant link twists | Hessian of the pinned free energy on C_b | 2D iteration transcribed | a twist with classical direct cost on every pin | stronger (it would give uniform mixing) | retired | Propositions B, B', SEAG, Lemma CEN | an exact continuous symmetry of a reformulated model |
| G2 typical pins with a colour frame | the same Hessian along theta n | background-field Ward identity plus bracket | (N1)-(N3) of 7.4 | unknown; reads first passage | blocked-local | Lemma FR, Remark HOPF | a frame and a controlled Ward identity on typical fields that persist into the band |
| G3 abelian pins | F_c on one maximal torus | exact U(1) Ward identity | closure under conditioning | weaker (one family of pins) | blocked-local | 4.7 (ii) | a conditioning that keeps the pins abelian |
| G4 sheets | thin boxes with a flat face | the 2D theorem itself | none (it is OpenAI's theorem) | weaker (no statement on the bulk) | candidate-complete as a 2D statement, GIVEN OpenAI's proof | Lemma EMB | a comparison from sheets to the bulk |
| G5 boundary Neumann covariance | mixed Hessian across a cell | Dobrushin-Shlosman type condition | uniform-in-pin decay at one scale | stronger | unexplored | 7.5 | a mechanism for decay uniform in pins |

Assumptions most likely to be wrong in this row: that a class of cubes is the only natural class (a class of
typical pins was not formalised); the ARGUED sizes in 7.3. Most expensive if wrong: Proposition B' (it carries the
verdict). Literature worth translating: none found by this row; row 1012 reads the published record.

RESULT: Row 1011, exercise on transferring OpenAI's 2D pinned-cell stiffness iteration to 4D SU(2); checked by no one. PROVED by hand (unchecked): the lattice pieces that are identities exist (the pinned class; Proposition A, the exact response to a link rotation; Proposition W, the Ward identity with its bracket term; the 4D shell sum (1/(8 pi^2)) log). PROVED (unchecked): the piece that carries the 2D proof FAILS for SU(2) in the class of all pins and strengths in [0, b]: the supremum over pins is invariant under site-wise colour rotation of the twist (Proposition B), so no bound by the classical action holds and the best uniform constant grows like b S (Proposition B'; constants ARGUED); the only link symmetries are central (Lemma CEN); the start bound is not "drop the covariance" even at the trivial pin (Proposition SEAG; a numeric control of its identity passed at three points, guide only); a colour frame costs at least the non-abelian part of the pin (Lemma FR). Compact U(1) has the twist with zero gain, SU(2) has the bracket with no twist. The 2D class embeds exactly on thin boxes with a flat face (Lemma EMB; idea of Durhuus and Frohlich, on file in rows 712, 825, 977) and says nothing on the bulk. Tests: U(1) passes with zero gain; Theorem D2 and Lemma SHEET do not bind a class of cubes (Proposition B' does); Q_8, 2T, five dimensions and instantons constrain only a repair. Corrected: two reading-level remarks of row 1009. The one-step gain has no statement, so Task 4 gives no constants. OPEN: a typical-field form with a colour frame ((N1)-(N3) of 7.4), which would read first-passage data and not cross the band by this mechanism; the Schrodinger-functional bound at the trivial pin; the wall (W) is not moved.
