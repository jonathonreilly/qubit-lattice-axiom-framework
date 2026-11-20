lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-21T02:59Z

# gap-mini-solve-aq-opus: four-dimensional SU(2) Yang-Mills mass gap (row 1284)

Started 2026-11-20T14:59Z (date -u) on the Mac mini, worktree pinned at commit 5b1df13cc
(branch claude/ym4d-hard-route). Labels: PROVED, ARGUED, GUIDE, OPEN, per the row brief.

## 0. Status log (updated in place)

- 14:59Z: file created; reading GOAL.md, FINISH.md rules, `parts/gap.md`, the RESULT lines of the
  earlier mini-solve rows, and `library/prior/gap-onebound-read-sol.md` (row 1218).

## Step 0. Record read (statements about the record, not evidence; written 2026-11-20T15:55Z by date -u)

Read: `GOAL.md` in full; `FINISH.md` L1-84 and L299-349; this item's row (L1365, row 1284); the RESULT lines of
rows 1189-1291 (the mini-solve series, the owner's tiling rows 1285-1287, rows 1281, 1283); `parts/gap.md` L1-104
and the route registry L223-267; `library/prior/gap-onebound-read-sol.md` (row 1218) in full;
`library/gap-crux-restate.md` L1-60; `library/gap-crux-exercise3-max.md` L100-160 (row 998's precise form of the
wall); Steps 0-3 of `library/gap-mini-solve-ap-opus.md` (row 1280) and Steps 1-2 of
`library/gap-mini-solve-ao-opus.md` (row 1278); CA-III L16540-16700 (`9.1:prop-blind-site-expansions`, fetched by
URL at Sussman-Alpoge commit 31a47c543775 into a scratch folder outside the repository).

What the record fixes (each item cites where it is proved or checked; none is re-derived here):

1. Modulo the ultraviolet carry, the gap clause reads one lattice input, (N-phys) of row 1161 (Theorem BP, row 1179,
   check 1183; rows 1225, 1233): at one physical side, uniformly in the cutoff, the periodic centre-neutral excited
   trace of the spatial cube at a time u <= n/K is at most 1/2. With K = 512 (row 1161) this needs a box of at
   least 512 log 2 times the inverse gap (check 1287). Equivalent forms: (W), (PHYS-SEED), (SEED) at one coupling
   with a carry, (SL) at one weak coupling (rows 998, 1258, 1277), and a lower bound of asymptotic-scaling type on
   the deconfinement coupling (rows 1180, 1184, check 1187).
2. In thermodynamic words (my paraphrase of item 1, GUIDE): log(1 + s) is the excess free energy of the thermal
   torus over the vacuum, so (N-phys) says the pressure at temperature 1/(u a) on a cube of side K u a is below
   log(3/2) / K^3 in units of T^4. That is a statement deep in the confined phase (at about a quarter of the
   deconfinement temperature, by Monte Carlo lore), not near any small parameter.
3. Every engine on file is blind, its seed sits in the band, and the one selective proved fact (asymptotic freedom at
   small coupling) has no carrier through the band (row 998 6b; `parts/gap.md` "Hardest open obligation").
   The all-coupling template (the posted 2D O(N) proofs) needs closure of a class uniform over pins and strengths;
   in 4D that class contains ordered members (Proposition CA-FAIL, rows 1072-1074: two pinned slices make a 3D O(4)
   magnet above beta about 1.01) and critical members (Lemma SHEET, row 996: K7 is an annealed Wilson model).
4. Row 1218's sources: A's ascent is conditional on its own seed (stronger than (N-phys)); B's Corollary 166 is
   non-selective (B's own Remark 155; row 1219); Zeng's routes are conditional.
5. Rows 1255-1280 worked the inputs of the one-cutoff carry. What remains there (row 1280 RESULT): (U-dom) or
   (P1)-(P4); (E0)-(E6), (E+) against Balaban's CMP 116 (not on this machine); `9.1:prop-blind-site-expansions`
   ("Proof outstanding" in the account, CA-III L16558-16560; its route repeats CMP 116 Section 2 with island-blind
   lengths, CA-III L16663-16700); (DET)'s inputs (rows 987-994); the account's premises.

## Step 1. How best to attack it (judgement, ARGUED; written 2026-11-20T16:10Z by date -u)

**The seed.** Modulo the carry, the problem is a lattice gap of Wilson SU(2) at one coupling, with a box of several
hundred correlation lengths (Step 0, items 1-2). I re-derived these routes before reading the tables, then grepped
each (rule 0a); every one has a match on file with its first failing step:
- continuity in beta from the strong-coupling seed, closed by a bound on how fast a level can fall: rows 708, 978,
  1281 ((LEV) is false as an operator inequality; it needs a "bounded excess" of the first level, which is the crux).
  My variant: the volume-robust thermal form d/dbeta log(1 + s) = (thermal action deficit) with a Gronwall bound
  "deficit <= K log(1 + s)" is equivalent to (LEV) with K proportional to u, so it adds nothing (checked by the
  one-level example: deficit / log(1 + s) = u |dm/dbeta|).
- a bootstrap through local excitations (Lieb-Robinson bounds for the Kogut-Susskind Hamiltonian, isolated
  one-particle band): rows 1113, 1213 and `library/gap-outside-box-max.md`; my estimate of what it gives is an excess
  bound of order m^(-4) in lattice units, so the gap would close at finite beta in the bootstrap; FAILS quantitatively.
- vortex and electric-flux free energies, twist eaters (Fact T): `library/gap-crux-restate.md` (TUBE'),
  `library/gap-cr-tomboulis-max.md` and its check (Tomboulis 2007 and the Ito-Seiler critique).
- Migdal-Kadanoff and hierarchical bounds: route RG, retired (row 998 7.4: "the departing step is the crux").
- B's ascent (H2)/(S) with C_B = 1 + O(g_k^2): the product over scales grows like a power of log(1/a) unless the
  O(g^2) term has a selective sign; this is a (K-flow) statement with no supplier (row 998 6b).
- Bakry-Emery for the Doob-transformed ground-state diffusion: needs the ground state; a coupling-uniform curvature
  would make the limit trivial (row 1237 Proposition UNI).
- gapless comparison models with asymptotic freedom (Georgi-Glashow, adjoint matter, products with a photon): on
  file (rows 1285, `library/gap-afield-b-max.md`, `library/gap-global-reform-max.md`).
- dimensional reduction to the posted 2D O(4) theorem, abelian projection, Gribov-Zwanziger, anomaly matching
  (theta = pi), Weinberg-Witten: on file or give no lower bound on the spectrum (anomalies and Weinberg-Witten allow a
  free Maxwell infrared and a trivially gapped one alike).
Verdict (ARGUED): I have no route to the seed that is off the record, and the record (row 998 9.5) says a further
screen is waste. I do not attack the seed in this row.

**What I do instead (the rule "only closures count").** The record leaves two kinds of items: the seed (no engine),
and inputs of the one-cutoff carry, most of which read Balaban's CMP 116 (not on this machine). Two carry inputs are
unowned at this pin and can be worked with sources on hand (rule 0a: grep of FINISH.md and `library/open-core.md` for
"(U-dom)", "H2'", "absolute core", "cross-admission": hits only in rows 1267, 1268, 1278, 1280, as OPEN or ARGUED):
- **Item A: (U-dom) of row 1280 (3.3),** ARGUED there; the input of Theorem U (row 1280 3.6) at the window levels.
  Sources: Balaban CMP 102 (Theorem 1 and (190)) and CMP 119 ((1.2), (3.2)-(3.13)), both in the owner's papers folder.
- **Item B: the connectedness clause of Lemma H2' (row 1278 2.3),** "connectedness and isometry-invariance of the
  absolute core (not found stated)". Source: YM4_EM at c7fef8b21b58 (fetched by URL to a scratch folder).

Moves: the one-cutoff carry on the pin route (row 1233 Proposition 3.7; rows 1267, 1268, 1278, 1280). Success on A:
(U) leaves the carry's list with only (E+) and the supplier readings left at the window levels. Success on B: Lemma
H2' becomes PROVED GIVEN readings with no geometric gap. Failure: the first step that does not close, named.
Neither item changes the seed; this is said plainly so that nobody counts it as progress on the crux.

**Plan.** Step 2: item B (short). Step 3: item A, reading CMP 102 Theorem 1, (190) and CMP 119 (3.6)-(3.9).
Step 4: labels, state, RESULT.

## Step 2. Items B and A examined (written 2026-11-20T16:55Z by date -u)

Sources read for this step: YM4_EM at c7fef8b21b58 L185-275 (cores, norm, block map, covariance), L495-520 (frames
and radii), L600-720 (the one-step inputs); Balaban CMP 119 OCR pp. 264-267 ((3.1)-(3.14)); CMP 102 OCR pp. 278-279
(Theorem 1) and pp. 305-308 (Section G, analyticity and the derivative bound). Credit: Sussman and Alpoge with Claude
and Codex as authors of EM; Balaban for CMP 102 and 119.

**2.1 Item B, the geometric clause of Lemma H2' (row 1278 2.3).**

*Lemma CC (covariance continues along paths; PROVED, elementary).* Let O be an open subset of a finite-dimensional
real space of data, D: O -> C real-analytic, and gamma: [0, 1] -> O continuous with D = 0 on a neighbourhood of
gamma(0). Then D = 0 on a neighbourhood of gamma(1).
*Proof.* Let T be the set of t in [0, 1] such that D vanishes on a neighbourhood of gamma(t). T is open by definition
and contains 0. If t_n in T increase to t*, every derivative of D vanishes at gamma(t_n), hence by continuity of the
derivatives at gamma(t*); D is real-analytic at gamma(t*), so its Taylor series there is 0 and D = 0 near gamma(t*).
So T is closed, T = [0, 1]. QED
Applied with D(W) = P_(rz)(G; rW) - P_z(G; W) (EM L258-262) on the real slice of the member's core (each torus is
finite-dimensional; D is real-analytic there because G is holomorphic on the core and the sum over X converges in the
norm of EM (2.x) by the stated entropy bound): covariance at a datum W of the phi-class follows once W is joined to
the psi-creation class by a path of real data inside the member's core. Row 1278 asked for connectedness of the whole
complex core; Lemma CC needs only such a path, so the clause is weaker than stated there.

*The path (OPEN here, with the reason).* On a box with l^2-small curvature, Lemma U (`library/lattice-uhlenbeck.md`,
checked 2026-11-02) gives a gauge with sup |a| <= C_U ||theta||, and the path t -> e^(i t a) keeps every plaquette
defect below C ||theta|| (first order t (da) plus O(t^2 |a|^2)). The covariance classes of EM are max-norm classes on
whole tori of side up to the compatible volumes. There the only gauge with |a| small that I can build has |a| of
order r N (r the max curvature, N the side), and the commutator term of the straight path is then of order (r N)^2,
which is not below the core radius once N exceeds r^(-1/2). I did not find a global path argument, so the clause is
reduced (to "every datum of the phi-class is joined to the psi-class by real data inside the core") and not closed.
Remark (ARGUED): the cleaner repair is in the account's own terms: covariance of a member is derived by the change of
variables of EM input 2 (orthogonal O_(r,W), transported cut and response) wherever the member's construction is
defined, so the creation radius can be stated as the member's whole real domain; that is a statement for the account
to make, not a lemma.

**2.2 Item A, (U-dom) of row 1280 (3.3).** CMP 119's cube reference is a minimal configuration on a finite data region
(U_(k+1, box') = U(B(box'~4), M(Q^(s*) V)), (1.2), (3.4)). (U-dom) compares the references of two nested cubes built
from one block field. That is a comparison of two minimisers with the SAME data on different DOMAINS (free boundary at
the smaller domain's edge). What CMP 102 supplies is a comparison in the DATA at a fixed domain: Section G proves that
U_k(V) is analytic in V and that dU_k/dB decays like the propagator (the derivative bound (190), p. 308, read by row
1280), and CMP 119 (3.6)-(3.7) uses exactly that form: the old and new cube references are written as one minimiser at
two data that differ by at most 4 delta_k in the bulk and O(eps_k) on a boundary layer. For two domains I found no way
to write the larger domain's minimiser as the smaller domain's minimiser at modified data: the larger problem has
action on plaquettes outside the smaller domain, so its restriction is not a minimiser of the smaller problem for any
data. A proof needs the linearised problem on the smaller domain with natural boundary conditions and an inverse with
exponential decay (Balaban's propagator theory with boundaries, CMP 99b), plus existence along an interpolation.
That is the same stop as row 1280 3.8. NOT closed here; (U-dom) stays ARGUED.

**2.3 What this step changes.** Item B: the clause of Lemma H2' is weakened from connectedness of the complex core
to the existence of real paths (Lemma CC, PROVED); the path on large tori is OPEN. Item A: no change. Both items are
inputs of the one-cutoff carry, not of the seed. Next (Step 3): a route to row 1280's parity envelope (Proposition
PE) that does not read the supplier's localised expansion, by applying row 1280's Lemma P to the global step integral
at the trivial datum, if EM's coefficient can be read from the global total.

## Step 3 (plan, written 2026-11-20T17:20Z by date -u): the parity envelope without the localised expansion

**What EM fixes (READ, EM L1170-1260, `em:prop-companion-coefficient`).** The coefficient b_j(E) is the second spatial
moment of the companion kernel, which the proof identifies with "the limit of the physical torus Hessian kernels" at
P_o, and b_j "is unchanged ... by changing coherent localizations of the same physical total". So the coefficient
f_(k+1) = b_(k+1)(F^u_(k+1)) is a function of the physical total of the unmarked interacting part alone, and the
unmarked total is formed from the all-small-field kernel (EM L544-547, read by row 1280 2.2).

**Idea (ARGUED; to be proved in Step 3).** Row 1280's Proposition PE needs (P4), the parity covariance of the
supplier's localised expansion (CMP 116, not on this machine). The Hessian kernel of the GLOBAL total at P_o can be
bounded without any localisation:
1. At data V near P_o the all-small-field step integral is I(V) = int dB rho(g B) chi_V(B) exp(Q(B; V)), and every
   factor depends on (g, B) only through g B, except the prefactor g^(-2) of the Wilson action. So the degree-n part
   of Q in B carries g^(n-2) (action) or g^n (Haar density, chart, inherited members): odd degree goes with odd power.
   The linear term of the action vanishes at the constrained minimiser for every V.
2. At V = 1 the Gaussian reference and the cut are symmetric under B -> -B (row 1280 4.3, from CMP 119 p. 249).
3. On the cut the measure nu_t proportional to rho chi exp(Q_2 + Q_even + t Q_odd) is log-concave for t in [0, 1]
   (Hessian at least the coercive constrained Hessian minus C delta, delta the cut radius in g B), so by the
   Helffer-Sjostrand representation with a Combes-Thomas bound (the tool of row 1237 Proposition UNI and row 1249
   Lemma CT) covariances of local functions decay exponentially, uniformly in the torus.
4. Then <O>_(nu_1) = int_0^1 Cov_(nu_t)(O, Q_odd) dt = O(g) for every local odd O, so each odd contribution to the
   Hessian kernel enters at order g^2; the even ones beyond the Gaussian are O(g^2) directly; the V-derivatives of the
   cut sit at the threshold and cost Gaussian tails. Hence the kernel's deviation from the one-loop kernel is
   O(g^2 polylog) with exponential decay, and its second moment gives |f_(k+1)| <= C theta_k^(-1) polylog + tails.
To be checked before it counts: whether every fluctuation variable is bounded by the cut (bonds b_0(c) excluded from
the tests, CMP 119 (1.9)), so that log-concavity holds on the whole fibre; the exact form of the chart and fibre
density at V near 1; and that the unmarked total is exactly log I(V) minus the Gaussian normaliser and the scalar.

## Step 3. The parity envelope without the supplier's localised expansion (written 2026-11-20T17:55Z by date -u)

Rule 0a: "parity envelope" is in row 1280 only (Proposition PE, ARGUED, inputs (P1)-(P4)); "half-loop" only there; the
convex Laplace theorem used below is `library/convex-laplace-tree-decay.md` (hard-core lane, "Status: proved here. Not
reviewed."; no FINISH row cites it, so it is UNCHECKED). Nothing below is a statement about the seed.

**3.0 The tool (CITED, unchecked).** Setting of `library/convex-laplace-tree-decay.md`: variables xi = (xi_c) on cells
c of a metric space X of uniform growth (G(kappa) := sup_x sum_y e^(-kappa d(x,y)) finite); cells K_c open convex
neighbourhoods of 0, independent of the parameters; convex barriers Psi_c (Psi_c = 0 and K_c the whole space allowed);
parameters p in an open set P of a product of spaces over points of X; S smooth on K x P with
(H1) D_xi^2 S >= gamma, (H2) |D_xi^alpha D_p^beta S| <= C_(a,b) e^(-mu tau(alpha, beta)) for a >= 2,
(H3) the same at xi = 0 for a <= 1 (gradient need not vanish), tau the tree length. **Theorem CL:** with
G(p) := -log int_K e^(-S - Psi), for |beta| = b >= 1, |D_p^beta G(p)| <= C'_b e^(-mu'_b tau(beta)), constants
depending only on gamma, mu, m, sup D_c, G(.), and the C_(a,c) with a + c <= b + 2; none on the size of X. Its
Remark 1: the cut must not depend on the parameters.

**3.1 Lemma OP (odd perturbations enter at second order). PROVED given Theorem CL.** Assume, besides the setting of
3.0 for the parameters p = (v, s) with v in an open set V and s in (0, lambda)^X (s_x located at x):
(a) every cell is symmetric, K_c = -K_c, and every Psi_c is even;
(b) S(xi; v, s) = S_e(xi; v) + sum_x s_x R_x(xi; v), with S_e(-xi; v) = S_e(xi; v) and R_x(-xi; v) = -R_x(xi; v) for
    every v and x;
(c) (H1)-(H3) hold for S on K x V x (0, lambda)^X with constants gamma, mu, C_(a,b) (lambda enters them only through
    (H1), which asks D_xi^2 S_e - lambda ||sum_x |D_xi^2 R_x| || >= gamma).
Put G_1(v) := G(v, lambda 1) (the full model) and G_0(v) := G(v, 0) (the even model). Then for |beta| = b >= 1,
    |D_v^beta G_1(v) - D_v^beta G_0(v)| <= (lambda^2 / 2) C'_(b+2) G(mu'_(b+2)/3)^2 e^(-mu'_(b+2) tau(beta)/3).
*Proof.* (1) At s = 0 the density e^(-S_e(.; v) - Psi) on K is even in xi for every v, by (a)-(b), and each R_x(.; v)
is odd, so D_(s_x) G(v, 0) = <R_x>_(v, 0) = 0 for every v in V. Hence every v-derivative of D_(s_x) G(., 0) is 0.
(2) Taylor's formula along s = t lambda 1, t in [0, 1], with integral remainder:
G(v, lambda 1) - G(v, 0) = lambda sum_x D_(s_x) G(v, 0) + lambda^2 int_0^1 (1 - t) sum_(x,y) D_(s_x) D_(s_y) G(v, t lambda 1) dt.
The first sum vanishes with all its v-derivatives by (1). (Differentiation under the integral and in v is allowed:
the sums over x, y converge absolutely with all v-derivatives by the bound below.)
(3) By Theorem CL with beta' = (beta, x, y), |D_v^beta D_(s_x) D_(s_y) G| <= C'_(b+2) e^(-mu'_(b+2) tau(beta, x, y)).
Fix a point z_0 of beta. The tree on beta and x, y contains a tree on beta and paths from z_0 to x and to y, so
tau(beta, x, y) >= max(tau(beta), d(z_0, x), d(z_0, y)) >= (tau(beta) + d(z_0, x) + d(z_0, y))/3. Summing,
sum_(x,y) e^(-mu' tau(beta, x, y)) <= e^(-mu' tau(beta)/3) G(mu'/3)^2. With int_0^1 (1 - t) dt = 1/2 this gives
the claim. QED
*Remark (what is not used).* No expansion of either measure is needed: the first-order cancellation is exact (step
(1)), the second-order term is a derivative of G and Theorem CL bounds it. This is the global form of row 1280's
Lemma P; it replaces that proposal's input (P4) (covariance of a localised expansion under b -> -b).

**3.2 Lemma MC (a moving cut costs only its wall). ARGUED, with the estimate stated.** Let the cut be a product of cells
K_c(v) = K_c(0) + h_c(v) (translates), and let nu_v be the probability measure proportional to e^(-S(.; v)) on the
frozen cut K(0). Put I(v) := int_(K(v)) e^(-S(xi; v)) d xi and I~(v) := int_(K(0)) e^(-S(xi; v)) d xi. Write
1_(K(v)) = prod_c (1_(K_c(0)) + w_c) with w_c := 1_(K_c(v)) - 1_(K_c(0)), supported in the shell of width |h_c(v)|
at the wall of K_c(0). Expanding the product gives I(v)/I~(v) = sum over sets Y of cells of an expectation of
prod_(c in Y) w_c, a polymer gas whose activities are wall masses. If the wall mass of every cell under nu_v (and under
its shells) is at most eta_w uniformly, and the covariances of nu_v decay as in Theorem CL (C), then log(I/I~) and
its v-derivatives are of size eta_w times the derivatives of the h_c, with tree decay. In the application below the
cells are balls of radius delta/g in the variables xi, the Gaussian reference has variance of order 1, so
eta_w <= exp(-c (delta/g)^2) = exp(-c (log theta)^(2 p_0)) up to polylog factors, and each v-derivative of h_c costs at
most a factor of order 1/g = theta^(1/2) (the shift is O(eps) in the variables g xi, CMP 119 (3.13)); so the wall
part of the coefficient is at most C theta^(b/2) exp(-c (log theta)^(2 p_0)), b = 2, which tends to 0 faster than any
power of theta when 2 p_0 > 1. Not proved here: the polymer-gas bound for the shells (a cluster expansion with
activities eta_w; standard in form, but it is a bound I state and do not write out). This is row 1280's (P3) made
quantitative; it is NOT the step that needed CMP 116.

**3.3 Proposition PE' (the parity envelope at the trivial datum). PROVED GIVEN Lemma OP, Lemma MC and the readings
(Par), (Sym), (Coord), (Conv), (EM-b) below.** Readings (each with its source and status):
- (Coord) The all-small-field step integral at data V near P_o is an integral over a FIXED set of real free variables
  xi (Balaban's linearised chart: CMP 119 (1.9)-(1.10) and p. 249, the bonds b_0(c) determined by the constraint, the
  rest free; EM L611-616, "a fixed Borel restriction in the real free variables"), with v := (1/i) log V entering
  through the chart, the background U(v) and the cube references. READ in part (row 1280 4.3; EM).
- (Par) In these variables S(xi; v) = -log(density) is g^(-2) A(U(v) e^(i g xi)) plus terms that depend on (g, xi) only
  through g xi (Haar density, chart Jacobian, soft gauge weight, fibre density, inherited members); its linear term in
  xi vanishes at every v (U(v) is the constrained minimiser). Hence its odd part in xi at each v is
  g R(xi; v), with R a sum of local terms of degree 3, 5, ... in xi, whose derivatives on the cut are bounded by powers
  of the cut radius delta/g = (log theta)^(p_0); and its even part is the Gaussian form (1/2)<xi, M(v) xi> plus terms of
  size g^2 times powers of delta/g. READ (CMP 119 p. 267: "exp(-1/2 <A, C* Delta^(k) C A> + P^(k)(g, U, A))", P^(k)
  a function of g A; row 1280 4.3), the locality of the terms ASSUMED as in EM's inputs.
- (Sym) At v = 0 the cut is a product of symmetric convex cells (balls |exp(i g xi_b) - 1| < 2 delta_k on the tested
  bonds, the cube tests on the block field are trivial, the soft axial truncation is even). READ (CMP 119 p. 249,
  row 1280 4.3).
- (Conv) (H1)-(H3) of 3.0 hold on K(0) for v near 0, with gamma a fixed fraction of the lower bound of Balaban's
  constrained fluctuation Hessian (CMP 99b, 109 propagator bounds) and C_(a,b) polynomial in (log theta); every free
  variable lies in a tested cell, so that the non-Gaussian Hessians are at most C delta on the cut. ASSUMED (the
  same kind of input as the hard-core lane's (H1)-(H3) "in the chart of Text 5.1", `parts/hard-core--mapped.md`
  L136, there for the lane's own kernel).
- (EM-b) f_(k+1) = b_(k+1)(F^u_(k+1)) is the second moment of the Hessian kernel at P_o of the physical total of the
  unmarked interacting part, which is -G(v) + log Z_ref(v) minus the Gaussian mismatch (scalar coefficient zero,
  EM L687-700) and a field-independent scalar; the inherited members are counterterm-subtracted (EM L538-541).
  READ (EM `em:prop-companion-coefficient`, L1172-1250: "unchanged ... by changing coherent localizations of the same
  physical total").
*Conclusion.* |f_(k+1)| <= C g_k^2 (log theta_k)^q + C theta_k exp(-c (log theta_k)^(2 p_0)), with C, c, q fixed by
the constants of the readings, uniformly in the torus and in the infinite-lattice companion.
*Proof.* (i) Lemma MC: the coefficient of -log I differs from that of -log I~ (frozen cut K(0)) by the wall term.
(ii) Lemma OP with lambda = g on -log I~: by (Sym), (Par), (Conv) its hypotheses (a)-(c) hold, R = sum_x R_x by
locality; so the Hessian kernel of -log I~ differs from that of the even model by at most C g^2 polylog e^(-mu'' |u|)
at separation u. (iii) The even model differs from the Gaussian model (1/2)<xi, M(v) xi> on K(0) by even terms of size
g^2 polylog: interpolate them with located parameters t_x in (0, 1) and apply Theorem CL to D_v^beta D_(t_x) G (first
order, no cancellation needed); the kernel changes by at most C g^2 polylog e^(-mu''|u|). (iv) The Gaussian model on
K(0) differs from the Gaussian model without cut by the Gaussian mass outside K(0), at most exp(-c (delta/g)^2) per
cell, with its v-derivatives (same estimate as Lemma MC). (v) The Gaussian model without cut is the reference
normaliser up to the mismatch family, whose coefficient is zero (EM L687-700). (vi) The second moment
sum_u u_mu u_nu (kernel difference)(u) is at most C sum_u |u|^2 e^(-mu''|u|) times the bounds of (ii)-(iv). QED

**3.4 Consequence for the carry (PROVED from 3.3 and row 1280's Proposition W2).** Row 1280 3.2: any window bound
eta_k <= kappa(theta_k) with sum_b D(2 Y_b) kappa(Y_b/2) finite closes the windows uniformly in n. With 3.3 the
per-level coefficient error is kappa(y) = C y^(-1) (log y)^q + tails, and even with the account's drift
D(y) = C_D y^(1/2) (log y)^(p_0), sum_b Y_b^(1/2) Y_b^(-1) polylog(Y_b) is finite because Y_b = exp(L^(b/r)) grows doubly
exponentially. So (U) of row 1268 closes by the parity route GIVEN Proposition PE' (that is, given the readings of
3.3 and Lemma MC), without (U-dom). Moreover the drift itself improves: summing |f| <= C theta^(-1) polylog along the
scaffold theta_r = X + c_0 r gives |x_k - theta_(n-k)| <= C (log theta)^(q+1), so the windows of row 1280's Lemma W
have polylog width (ARGUED: it needs the account's run to be driven by f alone, row 1260 2.1).
