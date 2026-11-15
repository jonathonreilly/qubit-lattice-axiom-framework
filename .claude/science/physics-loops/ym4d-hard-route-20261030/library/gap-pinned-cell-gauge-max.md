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
