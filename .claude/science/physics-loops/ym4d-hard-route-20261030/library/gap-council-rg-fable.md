# Gap council, RG seat (FINISH row 1128)

Status: done (steps 1 to 5 written; RESULT line at the end). This file was written in stages.
Literature: every citation in this file is recalled from memory. No paper was opened in this run. Treat each
citation as RECALLED until it is read.

Seat: constructive quantum field theory and the multiscale renormalization group.
Worker: Claude Fable 5.2, max effort, laptop subagent. One worker, one run. No second reader has checked this file.

## Plan (five steps)

1. Read `library/gap-council-brief.md` in full. State the obstacle of its Section 3 in the terms of constructive field theory: the object, the nearest known theorem, the line where that theorem stops.
2. Propose at most three attacks, ranked. Give for each: mechanism, exact first statement with quantifiers, the failing line for the three controls of Section 4, the nearest item of Section 5, the cheapest decisive test.
3. Attempt the first statement of the top attack. End at a proof, a counterexample, or a named failing line.
4. Read `parts/gap.md` (crux section, route registry, test table, methods set aside 1 to 34) and the FINISH RESULT lines it cites. Mark each attack new or already tried, with its row.
5. Write one RESULT line.

Labels used below: PROVED, ARGUED, GUIDE, OPEN. No statement in this file is a mass-gap claim.

## Step 1. The obstacle in the terms of constructive field theory

Source read: `library/gap-council-brief.md`, all seven sections. No other lane file was read before step 4.

### 1.1 The object

The object is one renormalization group trajectory, read in two ways.

- Read as a flow of measures. Balaban's block averaging gives effective densities rho_k on unit lattices, with a
  running coupling g_k. For g_k at most a small constant gamma_0 the account gives rho_k as a sum over large-field
  regions of exp(-A/g_k^2 + E_k) times small factors, with polymer bounds on E_k. (Balaban; the account.)
- Read on the torus. The wall (W), or (CAS), is a statement about the same flow: it is a bound on the doubling
  defect Phi_4(n) = 16 F(n^4) - F((2n)^4).

Identity R2 (PROVED here, elementary; input is (TM) in the form Z(X x n) = Tr T_X^n with T_X positive and trace
class; checked by this worker only). For a cross-section X let
S_2(n; X) = 2 log Tr T_X^n - log Tr T_X^{2n}. Then S_2 is at least 0, and

    Phi_4(n) = 8 S_2(n; n^3) + 4 S_2(n; 2n.n^2) + 2 S_2(n; (2n)^2.n) + S_2(n; (2n)^3).

Proof. Double one direction at a time: 16 F(n^4) - F((2n)^4) =
8 [2F(n^4) - F(2n.n^3)] + 4 [2F(2n.n^3) - F((2n)^2.n^2)] + 2 [2F((2n)^2.n^2) - F((2n)^3.n)] + [2F((2n)^3.n) - F((2n)^4)].
In each bracket take the doubled direction as time. The bracket is 2 log Tr T^n - log Tr T^{2n} for one fixed
operator T. It is at least 0 because Tr(A^2) is at most (Tr A)^2 for a positive trace-class A. End of proof.

S_2(n; X) is the Renyi-2 entropy of the state T_X^n / Tr T_X^n. With two replicas it is minus the log of the
expectation of the swap of one time slice. So (CAS) reads: the Renyi-2 entropy of the thermal state at temperature
1/L, in a box of side L to 2L, falls by a fixed factor per doubling of L. In the words of my field: the count of
degrees of freedom that are still light at the box scale must fall geometrically. At a fixed point (free photon,
any massless factor) this count is a constant. That is the obstacle of Section 3.

### 1.2 The nearest known theorems, and the line where each stops

(a) Small-field and large-field renormalization group. Balaban (Commun. Math. Phys. 1984 to 1989); the account by
Sussman and Alpoge; the same method for phi^4_3 and QED_3 by Dimock. One step maps the class
{A/g^2 + E, E with exponentially decaying polymer bounds} into itself.
Line where it stops: the step needs g_k at most gamma_0. Two facts are used. First, on the small-field region the
action has one minimizer under the block-average constraint, and the Hessian there is bounded below. Second, a
large-field cube costs exp(-p_0(g_k)) with p_0 large, so the large-field regions form a convergent polymer gas. At
g_k of order one p_0 is of order one and both facts are lost. This is the large-field problem at order-one coupling.

(b) Strong-coupling cluster expansion. Osterwalder and Seiler (1978); Seiler's monograph (1982).
Line where it stops: the Kotecky-Preiss radius of the polymer gas whose activity is the character ratio
I_2(beta)/I_1(beta). The brief gives the ceilings reached by hand (1/3 up to 1.0109). The last ceiling is close
to the transition of compact U(1). ARGUED: a group-blind majorant cannot pass the U(1) transition.

(c) A flow that crosses an order-one region. Every theorem I know has an extra small parameter or a special
structure.
- 1/N: Kupiainen (1980, lattice O(N)); Kopper, Magnen and Rivasseau (1995, mass generation in the large-N
  Gross-Neveu model). Line where it stops: N must be large. Here N = 2.
- Hierarchical models: Gawedzki and Kupiainen (1986, hierarchical O(N) sigma model, from weak coupling to the
  high-temperature fixed point; as I recall for large N only). Line where it stops: the recursion is one-site. For gauge fields the hierarchical
  model is group-blind (the brief, route RG).
- Inequality-driven multiscale proofs at order-one coupling: Aizenman and Duminil-Copin (2021, phi^4_4 and Ising).
  Line where it stops: they need a positive geometric representation (random currents). The surface
  representations of SU(2) lattice gauge theory are signed.

(d) One non-perturbative block step at order one. Haller and Kennedy (1996); Bertini, Cirillo and Olivieri (1999
and later; years not checked): if the fine field, given the block field, is strongly mixing for every block field, then the renormalized
interaction exists and decays.
Line where it stops: the input is a finite-size mixing condition for the constrained system. It is known at high
temperature or by computer. Also it is group-blind: it defines the map, it gives no direction of flow.

(e) The two-dimensional proofs named in Section 6 of the brief are, in my terms, a stiffness iteration that is
uniform over boundary conditions. I have not read them. I use only the brief's description.

### 1.3 The line where the theorem stops, in one sentence

The flow has three regions. Region I (g_k at most gamma_0) is the account. Region III is the basin of the
high-temperature fixed point; the lane's Theorems S, SH and ZD-c are its entrance theorem, with entrance test
(Z-SEED). Region II is everything between. No quantity is known that is monotone along the flow in region II with
a strict rate and whose rate is zero for U(1). In my field's words: (K-flow) is a lower bound on a non-perturbative
beta function that has no zero in region II; (K-one) is a finite-size criterion with explicit numbers.

### 1.4 Four remarks from this seat (all ARGUED)

1. Where the bracket can enter. A selective step must use the Lie bracket in one of four forms: (i) the sign of
   the one-loop coefficient, which is the paramagnetic term in the fluctuation Hessian; (ii) the Ricci curvature
   of the group manifold; (iii) the Weyl factor of Haar measure on conjugacy classes; (iv) the fusion rules. Forms
   (i) to (iii) are zero for U(1) and are not defined for a finite group. Form (iv) separates SU(2) from Q_8 and
   the binary tetrahedral group only at spin 2 or 3 (the brief, row 838).
2. Why the gauge case is harder than the sigma-model case. In a sigma model the non-abelian global symmetry acts
   on the boundary pins. In a gauge theory a gauge rotation of the pins costs nothing, and the only global
   symmetry that acts on boundary data is the centre one-form symmetry, which is abelian and discrete. So the
   bracket gain cannot come from a symmetry acting on pins. It must come from the dynamics (the cubic and quartic
   terms of the action) or from the geometry of the group.
3. One-sided statements are cheap, two-sided ones are not. For any model, the Hessian of a block effective action
   in the boundary field is the mean Hessian minus a covariance. So an upper bound on stiffness passes through a
   block step with no loss, for every group. A lower bound needs a Poincare inequality for the constrained system.
   The consumer side of the lane asks for one-sided statements: (CAS) is a lower bound on a partition function.
4. Numbers. The Wilson axis passes near the end point of the first-order line of the mixed fundamental-adjoint
   action (Bhanot and Creutz; numerics, GUIDE). A (K-one) at Wilson beta near 2.2 must therefore separate
   beta_adjoint = 0 from beta_adjoint near 1.2 by a margin of order one, by hand. I judge this out of reach
   without a structural inequality. This is the same message as the positive-character control of Section 4.

## Step 2. Three attacks, ranked

Notation. X is a periodic spatial cube of side N. T_X is its transfer operator and K_l(w, w') is the kernel of
T_X^l on slice fields w, w'. Gamma_l = -log K_l. A "pin" is a prescribed slice or boundary field. z_k is the centre
flip of direction k. F_v = -log(Z[twist]/Z) is the centre-vortex free energy of the torus X x l.

### Attack 1 (top). USF: a uniform, one-sided stiffness flow for the Schrodinger kernel

Mechanism. For any measure, the Hessian of a block effective action in the boundary field equals the mean Hessian
minus the covariance of the boundary force. So an upper bound on stiffness passes through a sewing step with no
loss; the Cramer-Rao inequality turns the subtraction into a Schur complement. This holds for every group and
uniformly over pins, because it is a pointwise statement. A strict gain needs a second ingredient. On a group
manifold with positive Ricci curvature the sewing integral over the middle field picks up the Jacobi-field
determinant of the transverse directions, and this lowers the stiffness by a fixed amount per step. On a circle
there are no transverse directions and the gain is zero. In the marginal dimension "halve, minus a constant"
becomes "stay, minus a constant", which is the form of asymptotic freedom. I read the brief's Section 6 as saying
that the two-dimensional proofs use a gain of this kind (ARGUED; I have not read them). The consumer is one-sided
too: by Jensen, the vortex free energy is at most a mean stiffness along a path from w to z_k w, and a small F_v
gives a large flux-sector gap. So this attack does not pass through clause (L3). It aims at the flux half of
(Z-UNB) only.

First statement (three parts, with quantifiers).
- (NL, no loss). Let G be a compact Lie group with bi-invariant metric, M = G^E x G^I, Gamma smooth on M, and
  Gamma'(e) = -log of the integral of exp(-Gamma(e, i)) over i. For every e, every finite family X of
  left-invariant fields on G^E and every finite family Y of left-invariant fields on G^I:
  Hess_X Gamma'(e) <= A - B C^+ B^T, where A = E[X X Gamma] (symmetrized), B = E[X Y Gamma], C = E[Y Y Gamma]
  (symmetrized), E is the conditional mean over i, and C^+ is the pseudo-inverse. Also C >= 0.
- (JEN, consumer). For all N, l and every path w -> w_phi, 0 <= phi <= 2 pi, generated by commuting left-invariant
  rotations of the links crossing a plane, with w_{2 pi} = z_k w:
  F_v <= 2 pi^2 sup_phi E_w[ d^2/dphi^2 Gamma_l(w, w_phi) ], with w distributed as a time slice of the torus.
  And for every flux sector e: l (E_e - E_0) >= log(2 / F_v) - D, where exp(D) = Tr T^l / lambda_0^l.
- (GAIN, the selective inequality; OPEN). There are a scale-covariant mean stiffness s(L) of the symmetric torus,
  bounding the right side of (JEN), and a function c > 0 on (0, infinity), such that along the trajectory
  s(2L) <= s(L) - c(s(L)) for all dyadic L between first passage and the seed size, with c(s) >= (1 - theta) s
  for s <= 1.

Where it fails for the controls.
- Compact U(1), weak coupling: (NL) and (JEN) hold. (GAIN) fails: the measure is Gaussian up to monopoles,
  Cramer-Rao is an equality, there are no transverse Jacobi fields, so c = 0 and s is constant.
- Product with a massless factor: (GAIN) can hold for the SU(2) factor. The attack then gives large flux gaps,
  which is true there. It fails at the consumer line: (JEN) reads the centre of one factor and says nothing about
  the trivial sector or about D. USF alone never gives (W).
- Frozen Q_8 or binary tetrahedral group: (NL) has no content, because there are no tangent directions. In the
  discrete version the path from w to z_k w has two steps of cost beta each and no spreading. F_v stays of order
  beta times an area. (GAIN) fails at its first use.

Nearest item of Section 5. Route RF (curvature, Polchinski flow) and the pinned-cell port (T-pin). Differences:
RF needs a lower bound on a Hessian (convexity) and a supplier of it in the band; USF uses the opposite, cheap
inequality. (T-pin) ended with a response bound in law and needed (L3) to reach all observables; USF asks only
for the vortex free energy, where a bound in law is enough by Jensen.

Cheapest decisive test. A weak-coupling sign test, by hand: evaluate the right side of (NL) for one sewing step
of the Wilson action at one loop, with the full tangent space as score family. If the bound keeps the paramagnetic
term, the upper-bound flow has the sign of asymptotic freedom and the attack lives. If the mean Hessian A loses
gauge covariance (see step 3, line (HOL)), the bound is local only and the attack is dead in this form.

### Attack 2. LAYER: Durhuus-Frohlich layers, with the two-dimensional theorems as supplier

Mechanism. Durhuus and Frohlich (1980): in axial gauge the links of one direction between two slices are a
principal chiral model in the external gauge field of the two slices. For SU(2) the chiral model is the O(4)
model. Restrict further: the links of direction mu on one 2-plane, given all other links, are a two-dimensional
O(4) model in an external SO(4) gauge field, with single-site fields from the staples of the fourth direction.
Section 6 of the brief says the two-dimensional proofs are uniform over pins and strengths. If they are also
uniform in an external gauge field, every such layer mixes at a rate m_2(beta) > 0 for every conditioning. The
selectivity is inherited exactly. The open step is the lift from layers to four dimensions.

First statement.
- (L-2D). For every beta there are C, m_2 > 0 such that for every finite box in Z^2, every SO(4) gauge field on
  its links and every family of single-site fields h_x in R^4 (any strengths), the O(4) model with weight
  exp(beta s_x . R_xy s_y + h_x . s_x) has truncated two-point function at most C exp(-m_2 |x - y|).
- (LIFT). There is a block scale b such that, for the Wilson measure in the window, the total influence of all
  other layers on one b-block of a layer is less than 1, uniformly in the conditioning.

Where it fails for the controls. Compact U(1): the layer is a two-dimensional XY model; with zero fields it has
power-law decay at weak coupling (Frohlich and Spencer 1981), so (L-2D) fails. Frozen Q_8 or binary tetrahedral
group: the layer has a finite target and long-range order at large beta; (L-2D) fails. Product with a massless
factor: the layers of the massless factor fail (L-2D).

Nearest item of Section 5. The pinned-cell criteria and the anisotropic bridge BR-2. Difference: the supplier is
an existing theorem for a two-dimensional subsystem, uniform over pins, not a new criterion in the law of the
four-dimensional model.

Cheapest decisive test. In three dimensions no lift is needed: (L-2D) and the Durhuus-Frohlich inequality give
the area law for three-dimensional SU(2) at every beta. So the first test is whether the posted two-dimensional
proofs survive an external gauge field. For four dimensions: a numerical estimate (GUIDE) of the influence sum
in (LIFT) at beta 2.3.

### Attack 3. THERMAL: a flow in the bare coupling at fixed lattice (virial form)

Mechanism. Two exact identities. (i) d Phi_4(n; beta)/d beta = 96 n^4 (<A_p>_{2n} - <A_p>_n), where <A_p>_m is
the mean plaquette action on the periodic torus of side m. (ii) Feynman-Hellmann for the levels of a transfer
operator. For the Hamiltonian form H = (2/beta) K + (beta/2) V this reads
beta d(E_i - E_0)/d beta = <V - K>_i - <V - K>_0 (kinetic part K, magnetic part V, each with its prefactor).
For harmonic oscillators the virial theorem makes the right side zero. For the quartic zero-mode Hamiltonian of a
small torus (Luscher 1982) it equals -(E_i - E_0)/3. So the bracket shows up as a strict virial inequality. A
flow in beta at fixed lattice needs no continuum limit and starts from either end.

First statement.
- (MONO). For all n and all beta > 0: <A_p>_n <= <A_p>_{2n}. Equivalently Phi_4(n; beta) is non-decreasing in
  beta.
- (VIR, selective; OPEN). There is kappa > 0 such that for every box, every beta in the band and every level i:
  -beta d log(E_i - E_0)/d beta >= kappa.

Use. (MONO) and the small-torus expansion bound Phi_4(n; beta) by its weak-coupling value at the same n, which
is the non-selective half (BDD-Delta) up to a slowly growing term (ARGUED). (VIR) is a lower bound on the lattice
beta function in every channel.

Where it fails for the controls. Compact U(1) at weak coupling: (VIR) fails with equality, kappa = 0 (virial
theorem for the photon). Product with a massless factor: (VIR) fails on the levels of the massless factor.
Frozen groups: (VIR) fails with the wrong sign for magnetic levels, whose energies grow with beta.

Nearest item of Section 5. "One-scale numbers with no consumer". Difference: this is a flow with a consumer for
(MONO); but (VIR) only bounds gaps at strong coupling below by gaps at weak coupling, which are small. So attack
3 cannot give (Z-UNB). It is ranked last.

Cheapest decisive test. Numerics (GUIDE): Phi_4(1; beta) and Phi_4(2; beta) against beta across 1 to 3.

## Step 3. Attempt on the first statement of attack 1

Result in one line: (NL) and the Jensen form of (JEN) are proved; the path form of (JEN) stops at a named line,
(HOL); so (GAIN) cannot be fed in the stated form. All proofs below were written and checked by this worker only.
Corrected after step 4 (see 4.2): at (HOL) the failure is PROVED for field-independent directions only; for
field-dependent frames it is ARGUED, and the lane holds that case as OPEN.

### 3.1 (NL) is PROVED

Setting as in step 2. For fixed e let mu_e be the probability measure on G^I with density exp(-Gamma(e, .))/p(e),
p(e) the integral, Gamma' = -log p. Write X_a = sum_j a_j X_j (external, left-invariant), Y_b = sum_k b_k Y_k
(internal, left-invariant). Haar measure is invariant, so the integral of Y f over G^I is 0 for every smooth f.

1. Differentiating under the integral: X_a Gamma' = E[X_a Gamma] and
   X_a X_a Gamma' = E[X_a X_a Gamma] - Var(X_a Gamma). Integral curves of left-invariant fields are geodesics of
   the bi-invariant metric, so the left side is the Riemannian Hessian of Gamma' in the direction a.
2. Scores. Put S_b = Y_b Gamma. Integration by parts gives E[f S_b] = E[Y_b f] for every smooth f. With f = 1:
   E[S_b] = 0. With f = X_a Gamma, and because X and Y act on different factors and commute:
   Cov(X_a Gamma, S_b) = E[X_a Y_b Gamma] = a^T B b. With f = S_b': Cov(S_b, S_b') = E[Y_b' Y_b Gamma] = b^T C b'.
   So C is a covariance matrix: C is symmetric and C >= 0.
3. Cauchy-Schwarz. Var(X_a Gamma + S_b) >= 0 for every b, so
   Var(X_a Gamma) >= -2 a^T B b - b^T C b for every b. Hence

   (NL')   X_a X_a Gamma'(e) <= inf over b of E[(X_a + Y_b)(X_a + Y_b) Gamma].

   The infimum is finite and equals a^T (A - B C^+ B^T) a, because B^T a is orthogonal to the kernel of C (if
   C b = 0 then S_b = 0 almost surely). End of proof.

Two remarks, both PROVED by the same three lines.
- (NL-gen). The constant field Y_b may be replaced by any smooth vector field W on G^I, with score
  S_W = W Gamma - div W: X_a X_a Gamma' <= E[X_a X_a Gamma + 2 W(X_a Gamma) + W(W Gamma) - W(div W)].
- Monotone form. If (X_a + Y_b)^2 Gamma <= Q(a, b) pointwise for a quadratic form Q, then
  X_a X_a Gamma' <= inf_b Q(a, b). For Q = s times a sewing-consistent reference form this is "no loss".
  The statement holds for every compact Lie group and every Gamma. It is group-blind, as it must be.

### 3.2 The gain in the one-link model: an exact identity (PROVED) and its size (GUIDE)

Take G = SU(2) with the metric of the unit 3-sphere, rho the geodesic distance from 1, phi a smooth class
function, w = exp(-phi), and mu the probability measure with density proportional to exp(-2 phi).

Proposition G1 (PROVED). -Hess log(w*w) at the identity equals (1/6) E_mu[Laplacian phi] times the metric, which
is also (1/3) E_mu[|grad phi|^2] times the metric.

Proof. Gamma(g, h) = phi(h) + phi(h^{-1} g). At g = 1 the law of k = h^{-1} is mu. By step 1 of 3.1 the Hessian
is E[Hess phi(k)(a, a)] - Var(a.grad phi(k)). The measure mu is invariant under conjugation, so both terms are
multiples of |a|^2: the first is E[Laplacian phi] |a|^2 / 3, the second is E[|grad phi|^2] |a|^2 / 3 (the mean
of a.grad phi is 0 because k -> k^{-1} preserves mu and flips the gradient). Integration by parts gives
E_mu[Laplacian phi] = 2 E_mu[|grad phi|^2]. End of proof.

Size. On the unit n-sphere Laplacian phi = phi'' + (n - 1) cot(rho) phi'. For phi = s rho^2 / 2 (sup-Hessian s)
this is n s - (n - 1) s rho^2 / 3 + ..., and E_mu[rho^2] = n / (2 s) + ..., so the sewn stiffness at the identity
is s/2 - (n - 1)/12 + O(1/s). ARGUED (Laplace asymptotics). The flat value is s/2. The gain (n - 1)/12 is the
Ricci curvature divided by 12. It is 1/6 for SU(2), (N - 2)/12 for the O(N) sigma model, and 0 for the circle.
For the Wilson profile phi = s (1 - cos rho) the same identity gives s/2 - 3/8 on SU(2) and s/2 - 1/8 on the
circle. So 1/6 of the SU(2) gain is curvature and the rest is the shape of the action, which is group-blind.

GUIDE (numerics, not proof; scratch script `g1_check.py`, not in the repository; exact character sums against
the identity of G1):

    profile   s      sewn stiffness   (1/6)E[Lap phi]   s/2 - 1/6
    quad      10     4.83611          4.83611           4.83333
    quad      40     19.83403         19.83403          19.83333
    Wilson    10     4.62994          4.62994           (s/2 - 3/8 = 4.62500)
    Wilson    40     19.62619         19.62619          (s/2 - 3/8 = 19.62500)

In the marginal dimension "halve, minus Ricci/12" reads "stay, minus a constant per doubling". That is the form
of asymptotic freedom for a sigma model (Polyakov; Friedan). So (NL) plus G1 is a non-perturbative, pin-uniform
form of the two-dimensional mechanism. ARGUED.

### 3.3 The consumer (JEN): the Jensen form is PROVED

Inputs: (TM), (TM-c) of the brief; the kernel K_l is strictly positive (the Wilson weight is positive).
Let nu be the law of one time slice of the periodic torus X x l: nu(dw) = K_l(w, w) dw / Tr T^l.

(JEN-a) PROVED. F_v <= E_nu[ Gamma_l(w, z_k w) - Gamma_l(w, w) ], and the integrand is >= 0.
Proof. Z[twist] = Tr(T^l Z_k) is the integral of K_l(w, z_k w). So exp(-F_v) = E_nu[K_l(w, z_k w)/K_l(w, w)].
Apply Jensen. The integrand is >= 0 because K_l is a positive-definite kernel that commutes with z_k:
K_l(w, z_k w)^2 <= K_l(w, w) K_l(z_k w, z_k w) = K_l(w, w)^2.

(JEN-b) PROVED. For every flux sector e with e_k = 1: l (E_e - E_0) >= log(2/F_v) - D, exp(D) = Tr T^l / lambda_0^l.
Proof. Tr(T^l Z_k) is the even sum minus the odd sum, so the odd sum is (1 - exp(-F_v)) Tr T^l / 2, at most
F_v Tr T^l / 2. The lowest level of sector e is one term of the odd sum.

(JEN-path) PROVED as an inequality. Let n_y be unit vectors that may depend on the links outside the plane P of
k-links, and let w_phi rotate each link of P by exp(i phi n_y.tau/2). Then w_{2 pi} = z_k w, the flow preserves
Haar measure, E_nu of the first derivative at phi = 0 vanishes (symmetry of the kernel and invariance of Haar
measure), and F_v <= 2 pi^2 sup_phi E_nu[d^2/dphi^2 Gamma_l(w, w_phi)].

### 3.4 The line where the attack fails: (HOL)

Lemma HOL (PROVED). Let u be the transverse links of the layer behind P and n a direction field on that layer.
The rotation of P changes each plaquette that straddles P by the corner factor
exp(i phi n'.tau/2) exp(-i phi n.tau/2), where n' is n at the neighbour site, carried back by the link u.
(a) All corner factors are 1 for all phi if and only if n is covariantly constant for u. Then every holonomy of
the layer fixes n, so the two-dimensional connection u is reducible to U(1).
(b) Around a layer plaquette q with holonomy angle theta_q and axis m_q, the four mismatches satisfy
sum |n' - n| >= 2 |sin(theta_q/2)| |n x m_q|. So the sum over layer links of |n' - n|^2 is at least
(1/2) sum_q sin^2(theta_q/2) |n x m_q|^2.
Proof. (a) is the definition of parallel transport. (b) is the triangle inequality around q, then Cauchy-Schwarz,
then each link lies in two plaquettes of the layer.

Consequences.
1. ARGUED. For a slice drawn from nu the plaquette angles obey beta E[theta_q^2] of order one at every coupling,
   because field-strength fluctuations sit at the lattice scale. By (b) a rotation by phi/d on each of d
   consecutive planes then costs of order N^2 phi^2 / d in the pinned slice. For d = N this is of order N phi^2.
   So the right side of (JEN-path) grows at least like N. It is not small even at weak coupling. This is the
   "seagull" term of perturbation theory. In the true free energy it is cancelled by the current-current term,
   a covariance. In (JEN-path) the top slice is pinned and cannot respond, so nothing cancels it.
2. RECALLED for the continuum; ARGUED for the lattice (corrected in 4.2). The cancellation cannot be restored by
   a better path of constant twists. A centre twist is a pair of constant
   colour twists by pi about orthogonal axes in two directions. Constant twists in two directions are consistent
   only if their adjoint actions commute. So no continuous family of constant twists joins the untwisted and the
   twisted sector. The sector is the second Stiefel-Whitney class of the SO(3) bundle, which is discrete. On the
   lattice every path from w to z_k w passes through a thin-vortex line.
3. ARGUED. The same line stops the sewing step. To get the halving in (NL-gen) for a rough middle slice one needs
   a vector field W whose score equals the boundary force up to a small error. That is the Ward identity written
   as equality in Cramer-Rao. Such a W must transport the lattice-scale fluctuations covariantly. The only known
   construction is the background-field split on the small-field region, which is the account. Beyond first
   passage none is known.

Why the sigma model does not meet this line. There the pins are rotated by an element of the global symmetry
group. The orbit is compact and connected, a rotation of all pins costs nothing, and a rotation of a part of
the pins changes no local term away from the junction. A semi-concave function on a compact orbit has small
oscillation, so a one-sided bound gives a two-sided one. In the gauge theory a constant colour rotation of a
part of the pins is a gauge transformation and costs nothing at all, and the centre is not connected to 1.

### 3.5 What survives, and the verdict

- PROVED tools for the lane: (NL), (NL-gen), Proposition G1, (JEN-a), (JEN-b), Lemma HOL.
- A repaired form with reducible pins. Let C_phi be the constant abelian slice whose Polyakov loop in direction k
  is exp(i phi n.tau/2), and s_SF = sup_phi d^2/dphi^2 Gamma_l(1, C_phi). Then C_{2 pi} is gauge equivalent to
  z_k 1, Gamma_l(1, C_phi) is even in phi, and K_l(1, z_k 1)/K_l(1, 1) >= exp(-2 pi^2 s_SF). PROVED (a
  semi-concave even function on a circle). This is a statement about the Schrodinger-functional coupling of
  Luscher, Narayanan, Weisz and Wolff. To use it one needs two clauses, both OPEN:
  (OVERLAP) a lower bound on the lowest odd eigenfunction at the trivial slice;
  (GAIN-SF) s_SF(2L) <= s_SF(L) - c, which meets (HOL) at the first sewing over a rough middle slice.
- Verdict (corrected in 4.2). The first statement of attack 1 is proved in the parts (NL) and (JEN-a, b). The
  chain stops at (HOL): broken for field-independent directions (PROVED), not excluded for field-dependent frames.
  Attack 1 does not cross region II. It explains, in the terms of my field, why the two-dimensional mechanism
  does not port: the gain needs a compact connected family of pin deformations that is a symmetry of the bulk,
  and a gauge theory has none. Any port must replace the symmetry orbit by a covariant transport of the
  lattice-scale fluctuations, which is the small-field machinery of the account, or must work with the vortex
  free energy directly, where no continuous path exists.

## Step 4. Comparison with the lane (files opened only now)

Read now: `parts/gap.md` (state of attack, routes tried, route registry, test table, the exact price);
`library/gap-crux-exercise2-max.md` 6a (methods 1 to 18); `library/gap-crux-exercise3-max.md` 7.3 (route
definitions); the FINISH RESULT lines of rows 712, 825, 839, 934, 1006 to 1013, 1016, 1017, 1018, 1077, 1078, 1108,
1115, 1122, 1123, with the cross-provider check lines attached to them; `library/gap-short-step-max.md` 4.1, 4.4,
4.5 and items 9 and 10 of its check `library/gap-short-step-check-astra.md`. I read RESULT lines and the named
sections, not the full files. Keyword counts over the lane were used to look for my tools; a count is not a reading.

### 4.1 Each attack: new or already tried

Attack 1, USF: ALREADY TRIED, in substance and nearly line by line.
- The two-dimensional mechanism as I reconstructed it (a class supremum over pins, lowered per step by a bracket
  term) is the reading of row 1009.
- The direct port to four dimensions is row 1011: Proposition A (exact response to a link rotation), Proposition W
  (Ward identity with bracket term), Propositions B and B' (the supremum over pins has no bound by the classical
  action), Proposition SEAG (the start bound is not "drop the covariance"), Lemma FR (a colour frame costs at least
  the non-abelian part of the pin). Its verdict: "Compact U(1) has the twist with zero gain, SU(2) has the bracket
  with no twist." That is my line (HOL).
- My (NL) and (NL-gen) are Proposition A (ii) of row 1011 and Lemma FLOW of row 1018 ("the response equals the least
  cost over all flows"). The Schur-complement form is the special case of constant flows. Not new.
- My (JEN-a) is Lemma JEN of row 1013. My (JEN-path) is candidate C2 of row 1013 (a non-central path to the centre
  twist). The lower bound by a thermal variance is Lemma WN of row 1013, and method 17 of the set-aside list.
- My Lemma HOL is Lemma FR (row 1011), Lemma GT (row 1016) and Lemmas FR+, PROJ, SPLIT, NAB (row 1018).
- (GAIN) is the short step (T-pin) of row 1018 and "step-scaling couplings", method 4. The repaired form with
  reducible pins is "the Schrodinger-functional bound at the trivial pin", OPEN in rows 1011 and 1016.
- Status in the lane after the cross-provider checks: candidates C1 and C2 are open again with no mechanism (check
  of row 1013); route (ii), field-dependent covariant moves, is OPEN, not ARGUED-FAILS (check of row 1018).
- New in this file, small: Proposition G1 (the exact one-link identity and the split of the gain into a curvature
  part, Ricci/12, and a shape part that the circle also has; I found no "Ricci" or "Friedan" in the lane); the
  clause (OVERLAP) as a named need of the Schrodinger-functional form.

Attack 2, LAYER: ALREADY TRIED.
- The slab reduction and its ceiling: row 712 (Identity L), row 825 (Lemma R and Theorem A, area law for beta_W
  below 2/3), row 839 (Proposition TB2: every background-uniform layer twist bound is false above 1.0109), method 2.
- The embedding of the two-dimensional class: Lemma EMB (row 1011), Lemma SLAB (row 1013). The three-dimensional
  corollary I named as the cheapest test is noted in `library/gap-pinned-cell-gauge-max.md` L601 as off the
  four-dimensional path.
- The lift from sheets is route BR-2: rows 1053, 1072 to 1078 (the face as a two-dimensional system; the
  independent-sheet and conditional-ferromagnet ports fail), rows 1089 to 1115 (coupled two-dimensional O(4)
  sheets). It is blocked-local at (SING), neutral-sector mixing with no association. My (LIFT) is that step.
- New in this file: nothing.

Attack 3, THERMAL: ALREADY TRIED.
- My identity (i) is Theorem D (f). My (MONO) is route RB, "a sign in beta", (MON'): blocked-equivalent, and false
  in the class (method 5).
- My (VIR) is (VAC-SUB) of row 934 in a per-level form; Lemma VIR there says the virial identity closes only for
  Gaussian weights; (VAC-SUB) is OPEN.
- Identity R2 of my step 1 is on file in substance (row 708; row 975, the Renyi-2 drift; Lemma ADD of row 1018).
- New in this file: nothing.

### 4.2 Corrections to step 3 forced by the lane's checks

1. Line (HOL), consequence 1. I argued that every frame, also a field-dependent one, pays a cost of order N. The
   cross-provider check of row 1018 (items 9 and 10) shows that the matching universal claims fail: the defect of a
   non-central cut has a linear term and a quadratic coefficient of no fixed sign, and reducibility is sufficient,
   not necessary, for a conserved projected current (its example: constant links i, j, k, 1 on an odd torus). So
   my consequence 1 is PROVED only for field-independent directions. Proof in my notation: for a one-parameter
   Haar-preserving flow with generator G, Jensen gives E_nu[d^2/dphi^2 Gamma_l(w, w_phi)] at phi = 0 at least
   Var(G) in the state T^l / Tr T^l; for field-independent directions gauge invariance kills the cross terms and
   Var(G) = (N^2/3) <E_link^2>, which is of order beta N^2. For field-dependent frames the statement is ARGUED.
2. Line (HOL), consequence 2. The fact about constant twists and the Stiefel-Whitney class is a continuum fact,
   RECALLED, not rebuilt. The sentence about lattice paths is ARGUED. Row 1013's Lemma TWIST says there is no
   winding label on the lattice.
3. My Lemma HOL (a) and (b) are statements about corner factors and frame mismatches. They are not touched by the
   check. They do not bound the action change from below.

4. Remark 4 of my 1.4 is the lane's K7 test. The lane holds it at BELIEF grade, and row 995 doubts the 1981 end
   point. Its theorem-grade form is Proposition V (row 712).

### 4.3 What the comparison says

- I worked blind and from a different starting point (Cramer-Rao and semi-concavity, not the Ward identity). I
  reached the lane's own conclusion: the two-dimensional engine works in four dimensions only while a colour frame
  exists, which is above the band. This is agreement of a second derivation. It is not a check of the lane's proofs.
- From this seat the registry has one entry whose natural tool is the renormalization group: route (ii) of row 1018
  with blocked variables, which is (N1) to (N3) of row 1011. It is a (K-flow) statement. ARGUED: it can move first
  passage outward, and it cannot cross the band, because at order-one response the defect of any frame is of the
  size of the gain (row 1018 4.5; my 3.4).
- So a crossing needs a step that works where no frame exists. In Balaban's terms that is a bound on a large-field
  region whose probability is of order one. No theorem of my field gives one without a second small parameter
  (1/N, a hierarchical structure, or a positive geometric representation). I have no fourth attack.

## Step 5. Result

RESULT: Row 1128 (Claude Fable 5.2 max, laptop subagent, council seat for constructive field theory and the
renormalization group; one worker, checked by no one; one numeric guide run; no mass gap claimed). In my field's
terms the wall is region II of one flow: the account is region I, Theorems S, SH and ZD-c are the entrance theorem
of the high-temperature basin, and no monotone quantity with a selective rate is known between them. Three attacks
were proposed blind and ranked: USF (a one-sided, pin-uniform stiffness flow by Cramer-Rao, with a curvature gain),
LAYER (Durhuus-Frohlich layers with the two-dimensional theorems as supplier), THERMAL (a virial flow in the bare
coupling). The top attack was attempted: (NL), (NL-gen), Proposition G1, (JEN-a) and (JEN-b) are PROVED by hand
(unchecked); the chain stops at the named line (HOL), PROVED for field-independent directions, ARGUED for
field-dependent frames. After the comparison all three attacks are ALREADY TRIED: USF is rows 1009, 1011, 1013,
1016, 1018 (Lemma FLOW, Lemma FR, Lemma WN, candidate C2, route (ii), which the lane holds OPEN); LAYER is rows
712, 825, 839, 1011, 1013 and route BR-2 (blocked at (SING)); THERMAL is route RB and row 934. New and small:
Proposition G1 with the split of the one-link gain into Ricci/12 and a group-blind shape part, and the clause
(OVERLAP). OPEN: (GAIN), (OVERLAP), (LIFT), (VIR), and the wall (W), which is not moved.
