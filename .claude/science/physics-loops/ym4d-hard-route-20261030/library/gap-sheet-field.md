lead: Claude Opus 5.5 lead session, row queued 2026-11-17 06:33Z
row: FINISH 1096, written by Claude Fable 5.2 medium (laptop subagent)

# gap-sheet-field (FINISH row 1096)

Research text, not an audit. It grants no status. It claims no Yang-Mills mass gap.
PROVED means a written hand argument in this file. Nobody has checked it yet. Nothing was formalized in Lean.

## Plan (eight steps; refined after step 1)

1. Read row 1096, row 1091's file, row 1092's reading and the check files that exist. Restate the target.
2. Read Pei (arXiv:2611.01532v2) in full; read Ding, Huang and Yang Theorem 5.2 and its boundary class; read OpenAI's O(4) Theorem 3.1 and Section 3.11.
3. State the weakest sheet statement that still feeds Theorem FST-BD (iv) and prove that it suffices.
4. Hardest first, part 1: Pei's transfer in a field of varying direction. Lemma by lemma: which step needs the sign-flip symmetry; the Radon-Nikodym factor.
5. Hardest first, part 2: what the surviving steps give in a field (crossing estimates, coarse orientations), and the exact failing statements with counterexamples.
6. (Rewritten after the lead's correction, see step 5.0.) From crossing estimates in a field to the Lipschitz kernel FST-F1 for all observables, charged ones included: what is proved, what is open. No route through FST-N.
7. Controls, marks, limits, credits.
8. RESULT line.

## Step log

### Step 1 result: the brief and the inputs

Brief (FINISH row 1096, read in full). Target: FST-F of row 1091 for the O(4) sheet at beta in [2.3, 2.6], or the weakest statement that still feeds Theorem FST-BD (iv), for fields of arbitrary site-varying direction with sup norm at most h_0 > 0, uniform in the torus. Hardest first: (1) does Pei's transfer survive a single-site field H.Phi of varying direction, and which step needs the sign-flip symmetry; does a field of norm h_0 on a box of side R change the crossing estimate by at most e^{c h_0 R^2}; (2) from crossing estimates in a field, decay for neutral observables (FST-N) and the Lipschitz two-point kernel; (3) exact failing statements and counterexamples.

Inputs read in full: `library/gap-face-stability.md` (row 1091, Claude Fable 5.2 medium, 330 lines); `library/prior/gap-face-stability-read-luna.md` (row 1092, gpt-6-luna high). After `git pull --ff-only`: `library/prior/gap-fstn-read-luna.md` (row 1095) is absent; `library/gap-face-stability-check-astra.md` (row 1094) is absent; `library/gap-face-stability-check-opus.md` (row 1093) exists but holds only its steps 1 and 2 (the brief and a list of claims), no verdict. So row 1091 is still unchecked when this row starts.

What this row takes from row 1091 (unchecked): M1, M2 (a sheet of the face is a two-dimensional O(4) model in a field H with |H_u| <= 2 lambda; the field at u is a 1-Lipschitz function, times lambda, of each of six neighbouring links at u); Theorem FST-BD (i)-(iv); Theorem FST-F; the failing steps G1, G2; the open item FST-N.

Notation. The sheet in a field H on a finite graph (a torus Z/L x Z/M or a subgraph of Z^2), with couplings b_e in [0, beta]: density proportional to exp{ sum_e b_e Phi(x).Phi(y) + sum_u H_u.Phi(u) } with respect to the product of uniform measures on S^3. E_H, Cov_H. |H| = sup_u |H_u|. Lip_x, osc_x, Lc as in row 1091.

### Step 2 result: sources read

Each download sits in its own new directory under /tmp. No paper was copied into the repository.

- **Pei, arXiv:2611.01532v2** (LaTeX source, `/tmp/sheetfield-pei.ebz2ta`). Read in full (all 1559 source lines except the preamble). The paper has two separate proofs. (S) Sections 2 to 5: sign clusters, for S^2 and by projection for S^{n-1}; input Ding, Huang and Yang's Theorem 5.2 on one annulus pinned at the pole; transfer by Lemma 3.3 (`lem:rn`). (O) Section 6: coarse orientations for n = 4, input OpenAI's (3.54), (3.58) and Section 3.10.1, taken as assumptions (I1)-(I3); transfer by Lemmas `lem:celltransfer`, `lem:badsite`; pins and signed couplings allowed; odd observables only. Pei's Remark `rem:twosite` states that a field h sum sigma^1 satisfies the cell transfer but not the symmetry lemma `lem:pm1`, and that the conclusion of his Theorem 6.1(a) then fails. His Remark `rem:scope` lists single-site anisotropy as not carried out.
- **Ding, Huang and Yang, arXiv:2611.04908v1** (LaTeX source, `/tmp/sheetfield-dhy.oMtmEs`). Read: Theorem 1.1 and Remarks 1.2, 1.3; Section 2.2.2 (local-time boundary conditions, the xy class); Theorem 5.2 and the first half of the proof of Theorem 5.1 (the domain Markov step). Statement lines only: the FKG theorem for the XY loop model and the remark that the all-x condition xi* is the largest. Not read: the proof of Theorem 5.2. Two facts matter here. (a) Theorem 5.2 is uniform over xy local-time boundary conditions: prescribed x- and y-local times on the boundary with zero z-local time, and arbitrary boundary partitions. In spin language the amplitudes of the boundary spins are prescribed and the signs are summed with a parity rule; they are not pinned. (b) Remark 1.3: the authors write that decay under all spin boundary conditions is natural to expect but "does not seem to be that immediate".
- **OpenAI, Sharp mass bounds for the two-dimensional O(4) model.** No new download. I read row 1078's copy (`/tmp/opus-face2d-openai.NylL2Z/src/preliminary.tex`; row 1091 records the pin 4eaee875, which I did not re-verify): Theorem 3.1 and the outline (lines 1-64) and Section 3.11 in full (lines 1018-1182). Section 3.11 has three nested levels: alpha, then two XY sectors, then the angles gamma and two Ising sign species each. Every level uses association of an amplitude marginal (FKG lattice condition), Newman's covariance inequality (3.11-1) and monotonicity in couplings. The section opens: "use the untwisted zero-field ferromagnet ... This restriction is essential."
- **Ding, Song and Sun, arXiv:2107.09243** (abstract page only, `/tmp/sheetfield-dss2.*`). Abstract: for ferromagnetic Ising models on finite graphs with an inhomogeneous external field, the influence of boundary conditions on any spin is largest at zero field; spin-spin correlations are largest at zero field with free boundary. The paper was not read. It is used only in a remark (6.1) and carries no PROVED mark.

### Step 3 result: the weakest statement I can feed to FST-BD (iv), and the proof that it suffices

Write L°_G = osc(G) + max_b Lip_b(G) for a function G of finitely many coordinates. L°_G does not change when a constant is added to G.

**Hypothesis FST-F1(h_0, a, X_1, X(.))** for the sheet at coupling beta. There is L_0 such that on every torus D with L, M >= L_0 and for every field H with |H| <= h_0:

- (R) response to one site. For every site u, every unit vector e in R^4 and every F in Lc (local or not): |Cov_H(F, e.Phi(u))| <= X_1 sum_w Lip_w(F) e^{-2a|u-w|_1}.
- (L) covariance with a local observable. For every finite B in D, every G in Lc that depends on the B-coordinates only, and every F in Lc (local or not): |Cov_H(F, G)| <= X(B) L°_G sum_w Lip_w(F) e^{-a d(w,B)}. X(B) is any finite number. It may depend on B in any way.

FST-F(h_0, a, X) of row 1091 implies FST-F1 with X_1 = X and X(B) = X |B|. (For (L): sum_{w,b} Lip_w(F) Lip_b(G) e^{-2a|w-b|} <= max_b Lip_b(G) |B| sum_w Lip_w(F) e^{-2a d(w,B)}.) FST-F1 is weaker in three ways: only one of the two observables is non-local; the local one may enter through its oscillation; the dependence on its support is free. So a bound of the shape of OpenAI's Theorem 3.1 on the G side is enough. The F side must still be a sum of one-site Lipschitz constants, for non-local F.

**Theorem FST-F1 (PROVED GIVEN row 1091's M1, M2 and FST-BD (i), (ii), step D; these are unchecked).** Assume FST-F1(h_0, a, X_1, X(.)). Put S_a = ((1+e^{-a})/(1-e^{-a}))^2 and gamma = 6 lambda X_1 e^a S_a. If lambda <= h_0/2 and gamma < 1, then for all T >= 3, all L, M >= L_0, every f in Lc and every g in Lc that depends only on the coordinates in a finite set B of D x E_T,

    |Cov(f, g)| <= (X_B L°_g / (1 - gamma)) sum_x Lip_x(f) e^{-a d(x, B)},   X_B = max over sheets e of X(B_e),  B_e = {u : (u,e) in B}.

So (17) holds for 0 <= lambda <= min(h_0/2, 1/(12 X_1 e^a S_a)) with rate a and constants independent of L, M, T, lambda and the state.

Proof. Use FST-BD with the round metric and the blocks V_e = D x {e}, as in row 1091's Theorem FST-F. (C) and (D_a): a change of the link (u, e'), e' ~ e, changes only H_u, by delta with |delta| <= lambda rho. Along the segment H + s delta the sup norm stays at most 2 lambda <= h_0. So mu^{H+delta}(F) - mu^H(F) = integral_0^1 Cov_{H+s delta}(F, delta.Phi(u)) ds, and (R) gives (C) with k = lambda X_1 e^{-2a|u-w|}. Then (D_a) holds with gamma as stated; FST-BD (i), (ii) and the identity (BD2) hold. Now redo row 1091's step F with (L) in place of (I). Let g > 0. For a block V_e that does not meet B the term nu(h - P_V h) is zero. For a block that meets B, nu(h - P_V h) is the nu-average of Cov_{mu_V^eta}(h, g)/mu_V^eta(g). For fixed eta, g is a function of the B_e-coordinates of the sheet, with oscillation and one-site constants at most those of g. (L) gives |Cov_{mu_V^eta}(h, g)| <= X(B_e) L°_g sum_{u in V} Lip_u(h) e^{-a d(u, B_e)}. Put W(x) = e^{-a d(x,B)} on D x E_T. For u in V_e, d(u, B) <= d(u, B_e), so the bound is at most X_B L°_g sum_{u in V} W(u) Lip_u(h). W is allowed in FST-BD (i). Each site lies in one block. So sum_V |nu(h_n - P_V h_n)| <= (X_B L°_g / inf g) Delta_W(h_n) <= (X_B L°_g / inf g) theta^n Delta_W(f), with theta = 1 - (1-gamma)/N. Summing (BD2): |nu(f) - mu(f)| <= X_B L°_g Delta_W(f) / (inf g (1-gamma)). Replace g by g + c and let c tend to infinity: L°_g and the covariance do not change and mu(g+c)/inf(g+c) tends to 1. QED

Scope. I do not claim that FST-F1 is the weakest statement that exists. It is the weakest for which this file has a proof. Within the scheme of FST-BD the two parts cannot be dropped: (R) is hypothesis (C) for sheet blocks, and without (L) the scheme gives decay in the transverse distance only (row 1091's (iii) has B+ equal to whole sheets).

Dual form (not used). By the comparison identity, (L) says: the law mu^H tilted by a positive local function g of B differs from mu^H, on every F in Lc, by at most X(B) (L°_g / inf g) sum_w Lip_w(F) e^{-a d(w,B)}. A coupling of the two laws with E rho(Phi_w, Phi'_w) <= c e^{-a d(w,B)} gives it. So does (R) from a coupling of mu^H and mu^{H + delta at u}.

### Step 4 result: Pei's transfer in a field of varying direction, lemma by lemma

Short answer to question (1) of the brief. The Radon-Nikodym step survives, with the factor e^{2 h_0 #sites}: Lemma RN below. It is not the step that needs the symmetry. The symmetry is needed by the step that makes one annulus (or one collar) independent of the rest of the lattice. In Pei's proof (S) that step is the pinning monotonicity (his Proposition 2.8), which rests on Griffiths' and Ginibre's inequalities. In his proof (O) the decoupling is uniform in the pins and survives; there the symmetry is needed one step later, in Lemma 6.4 (`lem:pm1`), to kill the observable. So in a field (S) loses the decoupling, and (O) keeps the decoupling but controls nothing about neutral observables.

**Lemma RN (PROVED).** Take a finite graph, strengths b_e (any sign), pins on a set P, and two fields H, H' on the unpinned sites. Put D = sum over unpinned v of |H_v - H'_v|. Then the density of mu^H with respect to mu^{H'} lies in [e^{-2D}, e^{2D}]. The same holds for the joint law of spins and any auxiliary variables drawn from a kernel that depends on the spins only (Pei's bonds). So P^H(E) <= e^{2D} P^{H'}(E) for every event E.

Proof. The two Hamiltonians differ pointwise by at most D. So the partition functions differ by a factor in [e^{-D}, e^{D}] and the densities by a factor in [e^{-2D}, e^{2D}]. The kernel is common. QED

On an annulus D_N(z) the number of sites is at most (4N+1)^2 <= 21 N^2. So a field of sup norm h_0 changes every pinned-annulus probability by a factor at most e^{42 h_0 N^2}. This is the factor e^{c h_0 R^2} of the brief, with c = 42 for R = N. It is absorbed at one fixed scale N when h_0 <= c' / N^2.

**Lemma MK (Markov and RN; PROVED).** Take a finite graph G with strengths b, pins P and a field H with |H| <= h_0. Let R_1, ..., R_k be sets of unpinned sites with no edge of G between R_i and R_j for i different from j. Let E_j be an event of the spins in R_j and of auxiliary variables whose kernel depends only on the spins of R_j and of its outer neighbours. Then

    P^H(E_1 and ... and E_k) <= prod_j e^{2 h_0 |R_j|} sup_omega P_0^{R_j, omega}(E_j),

where P_0^{R_j, omega} is the zero-field law of the graph induced on R_j and its outer neighbours, with the outer neighbours pinned at omega, and the supremum is over all omega.

Proof. Condition on all spins outside the union of the R_j. By the Markov property the R_j are then independent, and R_j has the law of the pinned system with field H restricted to R_j. Apply Lemma RN with H' = 0 to each. QED

Lemma MK is the whole transfer principle. A zero-field statement transfers to every field of norm at most h_0, at cost e^{2 h_0 |R|}, if and only if (for this argument) it is uniform over all pins on the boundary of a box R. A statement for free boundaries, or for pins at the pole only, does not transfer by it.

#### 4.1 Pei's proof (S), sign clusters. Sheet in a field H; the sign component is the first one

Pei's numbers below are my count from his source (one counter per section); his labels are given where a number could be misread.

| Pei's step | In a field H | Reason |
|---|---|---|
| Lemma 2.1 decomposition | survives, with new terms | The Ising signs get the field h_v = H^1_v r_v, of any sign. The complementary part gets a one-site term q_v H^perp_v . u_v of varying direction. |
| Lemma 2.2 bonds | the coupling survives; the identity (2.2) FAILS | Lemma B below. |
| Lemma 2.4 Griffiths | FAILS | Two sites, K small, fields of opposite sign: <tau_x tau_y> = tanh h_x tanh h_y + O(K) < 0. |
| Lemma 2.5 planar Ginibre | FAILS | Row 1091's G1 (site terms cos(theta_v - phi_v) with two phases). |
| Lemma 2.6 amplitude association | FAILS | Lemma A1 below (two sites, fields +h e_1 and -h e_1, small b). Row 1091's G2 is the same failure for OpenAI's split. |
| Lemma 2.7 joint association; Proposition 2.8 pinning | FAIL | Lemma P1 below. |
| Lemma 2.9 crossing identity | FAILS, and is not needed | With a field Z(pi)/Z(0) is not 1 - P(crossing): the two pin choices differ by cosh factors of the clusters. The transfer acts on the probability itself (Lemma RN). |
| Proposition 3.1 isotropic input | untouched | It is a zero-field statement, for layers pinned at the pole. |
| Lemma 3.3 annulus transfer | SURVIVES | Lemma RN. For layers pinned at the pole: P^H(crossing) <= e^{42 h_0 N^2} eps_N(beta). |
| Lemma 3.4 independent crossings | FAILS at its first line | It pins the layers of all annuli at the pole by Proposition 2.8. Lemma MK replaces that line, at the price of a supremum over all pins (4.3). |
| Proposition 3.5 coarse paths | survives | It uses only the conclusion of Lemma 3.4. |
| End of the proof of Theorem 1.1 | FAILS | It uses (2.2). |

**Lemma B (the bond coupling in a field; PROVED).** Keep Pei's bond rule P(eta_e = 1 | sigma) = p_e 1{tau_x = tau_y}, p_e = 1 - e^{-2 K_e}, K_e = b_e r_x r_y. For a cluster C put h(C) = sum_{v in C} H^1_v r_v. Conditionally on the amplitudes, the complementary parts and the bonds, the signs are constant on open clusters, the cluster signs are independent, and a cluster without pins has sign + with probability e^{h(C)} / (2 cosh h(C)). Conditionally on the amplitudes and the complementary parts, the bond law is proportional to prod_e p_e^{eta_e} (1-p_e)^{1-eta_e} prod_C 2 cosh h(C). For unpinned systems

    E[tau_x tau_y | amplitudes, complementary parts, bonds] = 1{x <-> y} + 1{x not<-> y} tanh h(C_x) tanh h(C_y).

Proof. Pei's expansion e^{K tau tau'} = e^K [(1-p) + p 1{tau = tau'}] does not involve the field. The factor exp(sum_v h_v tau_v) is exp(sum_C s_C h(C)) on configurations that are constant on clusters. Sum over the cluster signs. QED

So the step that needs the sign-flip symmetry inside Lemma 2.2 is "the cluster signs are fair". With a field the two-point function is not a connection probability. Only the conditional covariance is: Cov(tau_x, tau_y | ...) = 1{x <-> y} (1 - tanh^2 h(C_x)).

**Lemma P1 (pinning is not monotone in a field; PROVED; a numeric guide agrees).** Sites B, x, y in S^3; edges {B,x} of strength b >= 0 and {x,y} of strength beta > 0; field -h e_1 at y only, h > 0. Let A be the increasing event {eta_xy = 1}. Then for every small h > 0 there is b_0(h) > 0 such that for 0 < b < b_0(h): P(A with B pinned at e_1) < P(A with B free).

Proof. With B free, integrating out the spin at B gives a constant. So P_free(A) = E_h[k], where E_h is the two-site law proportional to exp(beta sigma_x.sigma_y - h sigma_y^1) and k = phi(t), t = sigma_x^1 sigma_y^1, phi(t) = (1 - e^{-2 beta t}) for t > 0 and 0 otherwise. With B pinned at e_1, P_pin(A) = E_h[k e^{b sigma_x^1}] / E_h[e^{b sigma_x^1}]. Its b-derivative at 0 is c(h) = Cov_h(k, sigma_x^1). At h = 0, c = 0 (flip the first coordinate at both sites: k is even, sigma_x^1 is odd). The h-derivative of c at 0 is -kappa_3(k, sigma_x^1, sigma_y^1) under E_0. All odd moments vanish, so kappa_3 = E_0[k t] - E_0[k] E_0[t] = Cov_0(phi(t), t). phi is nondecreasing and strictly increasing on t > 0, and t has a law with a density that is positive on (0,1). So Cov_0(phi(t), t) = (1/2) E[(phi(t) - phi(t'))(t - t')] > 0. Hence c(h) < 0 for small h > 0, and P_pin(A) - P_free(A) = b c(h) + O(b^2) < 0 for small b. QED

Guide run (pure Python, importance sampling, 4 x 10^5 samples, one serial job, nice 10; script `/tmp/sheetfield-num/pin2.py`, not in the repository): Cov_h(k, sigma_x^1) = -0.0165 +- 0.0006 at beta = 2.5, h = 0.2; +0.0153 +- 0.0006 at h = -0.2; -0.0006 +- 0.0006 at h = 0. The run only guides. The proof is the derivative computation.

Scope of P1. The model satisfies every input of Pei's Proposition 2.8 except zero field: strengths in [0, beta], a pin at the pole, an increasing bond event. The violation is of size b h. P1 refutes the proposition as a general lemma for every nonzero field strength. It does not refute a crossing bound in a field. For a field that points along +e_1 at every site the sign of c(h) is reversed, and the ghost-spin form of the FKG inequality gives the monotonicity (classical; not rebuilt here; ARGUED). So the failure is exactly the varying direction.

**Lemma A1 (the amplitude law is not associated; PROVED).** Pei's S^2 model on two sites, strength b, fields +h e_1 at x and -h e_1 at y, h > 0. The amplitude density is proportional to Z_I Z_P with Z_I = 2 e^{K} cosh(h r_x - h r_y) + 2 e^{-K} cosh(h r_x + h r_y), K = b r_x r_y, and Z_P = I_0(b q_x q_y). As b tends to 0, Z_I Z_P = 4 cosh(h r_x) cosh(h r_y) [1 - b g(r_x) g(r_y) + O(b^2)], g(r) = r tanh(h r), uniformly on [0,1]^2. g is strictly increasing. So Cov(r_x, r_y) = -b [Cov_a(r, g(r))]^2 + O(b^2) < 0 for small b, where a is the one-site law proportional to cosh(h r) on [0,1]. Two increasing functions are negatively correlated. QED. Scope: as G2 of row 1091: small b only.

#### 4.2 Pei's proof (O), coarse orientations, n = 4. Sheet in a field H with pins

| Pei's step | In a field H | Reason |
|---|---|---|
| (I1)-(I3) | untouched | Zero-field statements. (I3) is uniform in the rings outside the collar. That uniformity is what Lemma MK needs. |
| Lemma 6.2 cell transfer | SURVIVES | Split each one-site term among the cells that contain the site. Then |A^H_c - A^iso_c| <= |H| (2s+1)^2 <= 9 |H| s^2, so |F^H_c - F^iso_c| <= 9 |H| s^2 and the displacement of a collar changes by at most 18 K_coll |H| s^2. |
| Lemma 6.3 bad-site bound | SURVIVES when 18 K_coll |H| s^2 <= eps_*/4 | Its proof uses only the cell transfer and (I1)-(I3). Steps 1 to 5 are unchanged. |
| Lemma 6.4 (`lem:pm1`), the symmetry sigma -> -sigma | FAILS | A^H_c(-rho, -iota) = A^{-H}_c(rho, iota). This is the one place where (O) uses the symmetry (Pei says so after the lemma, and in Remark 6.10). |
| Lemma 6.5 odd observables | (a), (b) survive; (c) FAILS | (c) is the oddness of O* under T; it uses Lemma 6.4. |
| Lemma 6.6 disagreement coupling | survives | It is abstract. |
| Proposition 6.7 pinned decay | the coupling step survives; the oddness step FAILS | Lemma CO below states what is left. |

**Lemma CO (what (O) gives in a field; PROVED GIVEN Pei's (I1)-(I3) and his Lemmas 6.2 to 6.6 as written; these rest on OpenAI's unrefereed (3.54), (3.58)).** Take a pinned square with couplings b_e in [-beta, beta] and two data sets j = 1, 2: pins omega^j on the boundary and fields H^j with 18 K_coll |H^j| s^2 <= eps_*/4. Assume H^1 = H^2 on every cell with a corner in U (the tested coarse vertices). Let O be any bounded observable on A, with d the sup distance from A to the boundary, d > 2s(w+2). Let m^j be the law of the gauge-fixed ring configuration omega-tilde in system j, and Psi(omega-tilde) the mean of O* under the conditional law of the coarse orientations in system 1. Then

    E^1[O] - E^2[O] = integral of Psi d(m^1 - m^2) + Rem,   |Rem| <= 2^{4+w} |A| ||O|| exp(-(log 2) d / (2s)).

Proof. By Lemma 6.5(a), E^j[O] = integral of nu^j_{omega-tilde}(O*) dm^j. (O* is the same function in both systems: the cells that meet A have four free corners and the same field.) For a fixed omega-tilde the two conditional laws of the orientations have the same factor on every cell that meets U: such a cell has four free corners, contains no pin, and carries the same field. The good and bad vertices are the same in both systems. Lemma 6.6 gives |nu^1(O*) - nu^2(O*)| <= 2 ||O|| P_p(A* <-> W). Average over m^2 and use Lemma 6.3(c) for system 2, as in Pei's proof of Proposition 6.7. QED

Reading of Lemma CO (ARGUED). For every free coarse vertex set, Phi(kg) = k Phi(g) for a common left rotation k. So after the Haar average over g, the function Psi is a quasi-local function of the ring configuration that is invariant under common left rotations, up to the pinned boundary. So (O) in a field turns the influence of far pins and far fields on any observable into their influence on one neutral quasi-local ring observable. This is a description of what is left, not a reduction to a sufficient input: row 1094 found that row 1091's FST-N is not a quantified statement (step 5.0). At zero field and for charged O, OpenAI's Section 3.10 shows that Psi itself is small; in a field it is not, and nothing in (O) bounds the integral against m^1 - m^2.

#### 4.3 The exact statement that proof (S) needs in a field

**Hypothesis PIN-U(N, p).** For every z, every annulus graph on D_N(z) with strengths in [0, beta], and every pin configuration omega in (S^3)^{layers}, the zero-field O(4) law pinned at omega on both layers has P(the annulus is crossed by open bonds of the first sign component) <= p.

Pei's Proposition 3.1 with his projection (Theorem 1.3(b)) is PIN-U for the single pin configuration omega = e_1. Ding, Huang and Yang's Theorem 5.2 is uniform over local times and partitions, with the boundary signs summed. PIN-U asks for all pinned signs and all pinned complementary parts.

**Theorem T2 (PROVED GIVEN PIN-U(N, p)).** Assume PIN-U(N, p), N >= 2. Let h_0 >= 0 and p' = e^{42 h_0 N^2} p with 4 p'^{1/25} < 1. Then for every finite subgraph G of Z^2 without pins, all strengths in [0, beta] and every field with |H| <= h_0, the bond law of Lemma B satisfies P^H(x <-> y) <= A' e^{-m' ||x-y||_2}, with A' = p'^{1/25} / (alpha' (1 - alpha')), alpha' = 4 p'^{1/25}, m' = log(1/alpha') / (sqrt 2 N), whenever ||x-y||_inf > 4N.

Proof. Pei's proof of Proposition 3.5, with one change. For annuli with pairwise disjoint closed 2N-boxes let R_j be the set of vertices of G with N < ||v - z_j||_inf < 2N. Pei's Lemma 3.4 shows that every edge at R_j ends in R_j or on a layer of annulus j, and that a crossing uses a sub-path whose edges all meet R_j. Lemma MK with these R_j gives P^H(all k annuli crossed) <= (e^{42 h_0 N^2} p)^k. The coarse-path sum is Pei's. QED

**Lemma PIN+ (one-signed pins; PROVED GIVEN Pei's Theorem 6.1(a) at theta = 0, that is OpenAI's (3.61), hence (I1)-(I3)).** If every pin has a nonnegative first component (amplitudes and complementary parts arbitrary), then at zero field P(the annulus is crossed) <= 12 N A_* exp(-(N/2 - 1)/Xi(beta)).

Proof. By Lemma B at H = 0 with pins: a cluster that contains a pin with r > 0 has the sign of that pin, here +; pins with r = 0 carry no open bond; other clusters have fair signs. So for an unpinned x, E[sgn sigma_x^1] = P(x <-> pins). sgn sigma^1 is an odd one-site observable. Pei's Theorem 6.1(a) with theta = 0 bounds its mean by A_* exp(-dist_inf(x, pins)/Xi(beta)), uniformly in the pins and in strengths in [-beta, beta]. A crossing path meets the ring ||v - z||_inf = floor(3N/2), which has at most 12N sites, each at sup distance at least N/2 - 1 from the layers. Sum over the ring. QED

For pins of both signs the same computation gives E[sgn sigma_x^1] = P(x <-> pins with +) - P(x <-> pins with -). The charged bound controls the difference. PIN-U needs the sum. That is the exact gap between OpenAI's (3.61) and PIN-U.

### Step 5 result: correction from the check of row 1091, and what the surviving steps give for all observables

#### 5.0 Lead correction (received during step 4) and its effect on this file

The cross-provider check of row 1091 landed (`library/gap-face-stability-check-astra.md`, row 1094, gpt-6-astra xhigh). I read its sections 1, 2, 5 and its verdict table. Its findings that bind this row:

- FST-N as written in row 1091 FAILS as a sufficient input (no subtracted expectation, prefactor, volume, or support of the field change), and no proof gives FST-P or FST-F from it. So this file does not route through FST-N. Plan step 6 is rewritten. Wherever "FST-N" appears above it names an unquantified issue, never an input.
- FST-P implies FST-F ((Q2), (Q3) of row 1094); FST-T implies FST-F; no ordering of FST-P against FST-T is known. So the targets are FST-F, FST-P or FST-T, or FST-F1 of step 3, which FST-F implies.
- A face observable restricted to one sheet can be charged (the plaquette trace with three links fixed is Re q). So the sheet statement must cover all observables. FST-F1 does: (R) is a statement about the charged one-site function e.Phi(u), and F, G are arbitrary.
- (17) holds for periodic local limits only. Theorem FST-F1 of step 3 has the same scope: its bound is on tori, with periodic distance; (17) for a fixed separation n follows on tori large enough to avoid wrapping, then in the local limit.
- Row 1094 checked M1, M2 and FST-BD (i)-(iv) line by line and found that they hold (one sentence of step E corrected; it does not touch (i), (ii) or step F). Its identity (Q1), Cov_mu(f,g) = (1/N) sum_n sum_V mu[Cov_{mu_V^eta}(P^n f, g)], gives the proof of Theorem FST-F1 in one line without the shift g + c: bound each conditional covariance by (L). So Theorem FST-F1 is PROVED GIVEN statements that row 1094 checked. Theorem FST-F1 itself is unchecked.

Nothing in steps 3 and 4 used FST-N as an input. Lemma CO's reading was reworded.

#### 5.1 The sign sector for all observables, non-local ones included. PROVED

Fix the first coordinate. Let X be the triple (amplitudes r, complementary parts, bonds) of Lemma B. For a function F put F_X = E_H[F | X].

**Proposition SS (PROVED).** Take a torus or a finite graph without pins, strengths in [0, beta], any field H. Let F be in Lc and let G be bounded and depend on the coordinates in B only. Then

    |Cov_H(F, G) - Cov_H(F_X, G_X)| <= pi osc(G) sum_w Lip_w(F) P^H(w <-> B),

where w <-> B means that the open cluster of w meets B.

Proof. Cov_H(F,G) - Cov_H(F_X, G_X) = E_H[Cov(F, G | X)]. Given X, the spin configuration is a function of the cluster signs, and these are independent (Lemma B). List the clusters C_1, ..., C_m and let E_i be the conditional expectation given X and the signs of C_1, ..., C_i. Then Cov(F, G | X) = sum_i E[(E_i F - E_{i-1} F)(E_i G - E_{i-1} G) | X]. If C_i does not meet B, G does not depend on its sign and the term is zero. If it does, |E_i G - E_{i-1} G| <= osc(G), and |E_i F - E_{i-1} F| is at most the change of F when the sign of C_i is flipped. The flip moves each spin of C_i by at most pi in round distance, so the change is at most pi sum_{w in C_i} Lip_w(F). Each site lies in one cluster. Sum over i and average. QED

**Corollary SS.** Given PIN-U(N, p) and h_0 as in Theorem T2, the right side is at most pi osc(G) |B| A'' sum_w Lip_w(F) e^{-m' d_2(w,B)} on finite subgraphs of Z^2 (A'' = max(A', e^{4 sqrt 2 N m'})). On tori with sides at least 10N the same holds with the periodic distance: the proof of Theorem T2 is local (ARGUED; I did not write the torus bookkeeping).

So the sign sector has exactly the form of (L) and (R) of FST-F1, for all observables, charged or not, with sup norm only on the local side. It needs PIN-U and nothing else.

#### 5.2 What is left: the even sector. OPEN, stated precisely

**Hypothesis EV(h_0, a, X_ev(.))** for the sheet at coupling beta. On every torus with sides at least L_0 and for every field with |H| <= h_0: for every F in Lc, every finite B and every G in Lc on B,

    |Cov_H(F_X, G_X)| <= X_ev(B) L°_G sum_w Lip_w(F) e^{-a d(w,B)}.

F_X and G_X are functions of the amplitudes |Phi^1|, of the complementary parts and of the bonds. They are even under every cluster flip. For a charged G they do not vanish in a field: for G = Phi^1(u), G_X = r_u tanh h(C_u).

**Theorem SS+EV (PROVED GIVEN PIN-U on tori and EV).** PIN-U(N, p) (in the torus form of Corollary SS) and EV(h_0, a, X_ev), with h_0 as in Theorem T2, give FST-F1(h_0, a', X_1, X(.)) with a' = min(a, m'/sqrt 2)/2, X(B) = X_ev(B) + pi |B| A'', X_1 = 3 X({u}). Hence, by Theorem FST-F1, (17) on a positive interval of lambda.

Proof. (L) is Proposition SS plus EV, with osc(G) <= L°_G and d_2 >= d_1/sqrt 2. (R) is (L) for the one-site function e.Phi(u), whose L° is at most 3. QED

This is a splitting, not a reduction. Given the cluster bound, EV is equivalent to (L). I state EV because it is the quantified form of the item that every route below leaves open. It replaces the unquantified FST-N.

#### 5.3 Where proofs of PIN-U and of EV stop. Exact failing statements

- **PIN-U, by Pei's and OpenAI's association.** It would follow from: for pins of both signs, the amplitude law under the pins makes the increasing functional Q(r) = (wired FK probability of x <-> pins at couplings b r r') no larger than under the same pins with all first components made nonnegative. Conditionally on the amplitudes this is the FKG inequality for the wired random-cluster measure (the event "no open path joins pins of opposite sign" is decreasing). The amplitude law under the two pin sets differs by the factor FK(no such path), which is decreasing in r. So the claim holds if the amplitude law under one-signed pins is associated. Its density contains the partition function of the complementary system with pins of arbitrary direction. Association then needs Ginibre-type inequalities with boundary terms of several directions, which FAIL as general lemmas (G1 of row 1091; A1 above shows the same for the Ising factor). FAILS as a proof; the claim itself is OPEN. With Lemma PIN+ it would give PIN-U.
- **PIN-U, by OpenAI's (3.61).** (3.61) is uniform in all pins. It bounds P(x <-> + pins) - P(x <-> - pins). PIN-U needs the sum (4.3). OPEN.
- **PIN-U, by Ding, Huang and Yang.** Their Theorem 5.2 sums the boundary signs with a parity rule. A sign-pinned law is the wired law conditioned on the decreasing event above for the x-copy and on the same event for the y-copy, which is increasing in their x-preferred order. The two conditionings pull in opposite directions in their FKG theorem. Their Remark 1.3 records that all spin boundary conditions are "not that immediate". OPEN. (From statement lines; their proofs were not read.)
- **EV, by OpenAI's Section 3.11.** The route is: Newman's inequality for an associated amplitude field, then spin two-point bounds for the amplitude covariances. In a field the amplitude fields are not associated (G2 of row 1091, A1 above). The sign level alone survives: an Ising model with fields of any sign is associated (its log-density is supermodular), so (3.11-1) holds for the signs given the amplitudes, with Cov_h(tau_i, tau_j | amplitudes). FAILS at the amplitude levels as a proof. EV is OPEN.
- **EV, by Pei's proof (O).** Lemma CO: (O) controls the coarse orientations given the gauge-fixed rings and says nothing on the law of the gauge-fixed rings. OPEN.
- **Both, by differentiation in the field strength (ARGUED).** d/dt Cov_{tH}(F,G) = sum_u kappa_3(F, G, H_u.Phi(u)). A two-observable kernel at rate 2a bounds the third cumulant only through the largest isolation distance, which is half the separation when u lies midway (row 1091, Lemma K3). So a kernel at rate 2a at time t gives a derivative bound at rate a. The differential inequality does not close at any fixed rate. FAILS as a proof.
- **Both, from free boundaries to all pins (ARGUED).** OpenAI's Theorem 3.1 on the free graph Lambda with its outer ring gives Var(E[F | ring spins]) <= C poly(l) L_F^2 e^{-c d/Xi}: for typical ring spins the pinned mean is near the free mean. To pass to all pins one compares the law of an inner ring under given pins with its free law. The density ratio is bounded only by e^{16 beta l'} for a ring of side l' (each of its bonds to the outside costs e^{2 beta}). The gain is e^{-c d/Xi} with d <= l'/2. So the step needs c/(2 Xi) > 16 beta. That is false at these couplings. FAILS as a proof. In one dimension the ring has two sites and the step works.

#### 5.4 A model that satisfies every input of the sign-cluster argument and violates EV. PROVED GIVEN the long-range order of the two-dimensional Ising model (Peierls; classical, cited, not rebuilt)

On S^3 put phi(sigma) = +1 if (sigma^1)^2 + (sigma^2)^2 >= 1/2 and -1 otherwise. Take the density proportional to exp{ J sum_<xy> phi(sigma_x) phi(sigma_y) + b sum_<xy> sigma_x.sigma_y } with b = 0. Under Haar measure (sigma^1)^2 + (sigma^2)^2 is uniform on [0,1], so the variables phi(sigma_x) form the nearest-neighbour Ising model at coupling J, and given them the spins are independent. The interaction is even under each coordinate reflection, so Lemma B, Lemma MK, Proposition SS and Theorem T2 hold for each of the four coordinate sign components with the same proofs. There are no open bonds (p_e = 0), so PIN-U(N, 0) holds for every N, uniformly in pins and fields. Let psi(sigma) = (sigma^1)^2 + (sigma^2)^2 - 1/2. It is Lipschitz and a function of the amplitudes, and E[psi(sigma_x) | phi] = phi(sigma_x)/4. So Cov(psi(sigma_x), psi(sigma_y)) = Cov(phi(sigma_x), phi(sigma_y))/16. For J above the critical coupling this does not tend to zero with the distance on tori at zero field. So EV fails for F = psi(sigma_x), G = psi(sigma_y), and so does FST-F.

Scope. The model is not O(4)-invariant and has no pair coupling. It refutes one implication only: "crossing bounds for the coordinate sign clusters, uniform in pins and fields, give the covariance kernel". It says nothing about the O(4) sheet. It shows that a proof of FST-F for the sheet must use the O(4) structure in the even sector. Sign-cluster crossing estimates, in a field or not, cannot supply it alone.

### Step 6 result: from crossing estimates in a field to the Lipschitz kernel. Summary of the chain, and two remarks

The chain that is proved in this file:

    PIN-U (zero field, all pins, one annulus)  --Lemma MK, Theorem T2-->  cluster decay in every field with |H| <= h_0, h_0 of order 1/N^2
        --Proposition SS-->  the sign part of Cov_H(F, G) has the kernel of FST-F1, for all observables
    + EV (even part)  --Theorem SS+EV-->  FST-F1  --Theorem FST-F1-->  (17) on 0 <= lambda <= min(h_0/2, 1/(12 X_1 e^a S_a)), periodic local limits.

Neither PIN-U nor EV is proved. So question (2) of the brief has this answer: crossing estimates in a field give the sign part of the kernel and no more (Proposition SS, model 5.4). The even part is a separate statement, EV, and the Lipschitz kernel is the sum of the two.

**6.1 Remark on the Ising level (ARGUED; uses Ding, Song and Sun from their abstract only).** Write each spin as (tau^k a^k), k = 1..4, with amplitudes a^k = |Phi^k|. Given all amplitudes, the four sign species are independent ferromagnetic Ising models with couplings b a^k_x a^k_y and fields H^k_x a^k_x of any sign. Each is associated. By the abstract of Ding, Song and Sun, the influence of a boundary condition on a spin, and the spin-spin correlation, are largest at zero field. If that statement is used as read, then given the amplitudes the sign covariances in a field are at most the zero-field connection probabilities at the same amplitudes. This would remove the mixed-sign difficulty at fixed amplitudes. It does not give PIN-U or EV: the amplitudes are then distributed by the field law, and the zero-field connection probability is an increasing function of amplitudes whose law is not associated. The paper must be read before any use.

**6.2 Remark on aligned fields (ARGUED).** If H_u = h_u e with h_u >= 0 and one fixed e, the sign species along e has a nonnegative field, the complementary sectors have none, and Pei's Section 2 goes through with a ghost spin: Griffiths, Ginibre, amplitude association and pinning all hold. Then Pei's transfer survives in full and gives cluster decay for |H| <= c/N^2. The face does not produce aligned fields (M1: the field of a sheet is a function of the neighbouring links). So this case does not serve the target. It locates the failure: the varying direction, not the field.

### Step 7 result: controls, marks, limits, credits

#### 7.1 Controls

- **Lemma P1 and Lemma A1 at h = 0.** Both first-order terms vanish at h = 0 (c(0) = 0; g = 0). This agrees with Pei's Proposition 2.8 and Lemma 2.6 at zero field.
- **High temperature.** For beta small Dobrushin's one-site condition holds for the sheet uniformly in pins and fields. Then FST-P, hence FST-F and FST-F1, hold by row 1094's (Q2), (Q3). Nothing here conflicts with that. The window [2.3, 2.6] is outside that regime.
- **Compact U(1).** Lemma RN, Lemma MK and Theorem FST-F1 are group-blind. For XY sheets at large stiffness PIN-U fails at the anchor: at zero field with pole pins the crossing probability does not tend to zero (Frohlich and Spencer; cited, not rebuilt). No conflict with row 1077's (18).
- **Five dimensions.** As in rows 1091 and 1094: twelve neighbours, |H| <= 4 lambda, lambda <= h_0/4, gamma = 12 lambda X_1 e^a S_a. This step does not separate four from five dimensions and need not.
- **Model 5.4.** It satisfies PIN-U and violates EV. It marks the line between the two hypotheses.
- **Numerics.** One guide run (Lemma P1). No statement rests on it.

#### 7.2 Marks

| Mark | Statement and scope |
|---|---|
| PROVED GIVEN M1, M2, FST-BD (i), (ii), (Q1) (checked line by line by gpt-6-astra xhigh, row 1094) | Theorem FST-F1: the one-sided hypothesis FST-F1 ((R) one-site response and (L) covariance with a local observable, both with a sum of one-site Lipschitz constants on the non-local side only) gives (17) on 0 <= lambda <= min(h_0/2, 1/(12 X_1 e^a S_a)), for periodic local limits. FST-F implies FST-F1. Not claimed to be the weakest statement that exists. |
| PROVED | Lemma RN and Lemma MK: a field of sup norm h_0 changes any pinned-box probability by at most e^{2 h_0 #sites} (e^{42 h_0 N^2} on an annulus of scale N); a zero-field bound that is uniform over all pins of a box transfers to every such field. |
| PROVED | Lemma B: the bond coupling in a field; cluster signs are independent with bias tanh h(C); the two-point function is not a connection probability. |
| PROVED (counterexamples to steps) | P1: pinning at the pole lowers the probability of an increasing bond event, for every small field strength h > 0 against the pole and small strength b (three sites; first-order computation). A1: with fields +h e_1, -h e_1 the amplitudes of two sites are negatively correlated for small b. |
| FAILS (as general lemmas in a field of varying direction) | Pei's Lemmas 2.4, 2.5, 2.6, 2.7, Proposition 2.8, identity (2.2), Lemma 2.9, the first line of Lemma 3.4; Pei's Lemma 6.4 and Lemma 6.5(c). Each is a failure of one step of one proof at the stated parameters. None is a failure of FST-F, FST-P, PIN-U, EV or (17). |
| PROVED GIVEN PIN-U(N, p) | Theorem T2: exponential decay of sign-cluster connections in every field with 4 (e^{42 h_0 N^2} p)^{1/25} < 1, on finite unpinned subgraphs of Z^2. On tori: ARGUED. |
| PROVED GIVEN Pei's Theorem 6.1(a) at theta = 0 (OpenAI's (3.61); unrefereed) | Lemma PIN+: PIN-U for pins whose first components are all nonnegative. |
| PROVED GIVEN Pei's (I1)-(I3) and his Lemmas 6.2 to 6.6 | Lemma CO: in a field with 18 K_coll |H| s^2 <= eps_*/4 the bad-site bound holds, and the effect of far pins or far fields on any observable equals its effect on the law of the gauge-fixed rings, tested against one function, up to an exponentially small term. |
| PROVED | Proposition SS: the sign part of Cov_H(F, G) is at most pi osc(G) sum_w Lip_w(F) P^H(w <-> B), for every field and non-local F. |
| PROVED GIVEN PIN-U (torus form) and EV | Theorem SS+EV: FST-F1, hence (17) on a positive interval. |
| PROVED GIVEN Peierls | Model 5.4: PIN-U holds, EV and FST-F fail. Scope: a model without O(4) invariance; it refutes one implication, not a statement about the sheet. |
| ARGUED | The reading of Lemma CO; the torus form of T2; remarks 6.1 and 6.2; the two failed routes at the end of 5.3 (constants not tracked). |
| OPEN | PIN-U (all pins; the gap to OpenAI's (3.61) is the sum against the difference of connection probabilities to pins of the two signs). EV. Hence FST-F1, FST-F, FST-P, FST-T for the sheet at beta in [2.3, 2.6], and the target. No counterexample to any of them for the O(4) sheet was found. |

#### 7.3 Answers to the brief

1. Pei's transfer in a field. The Radon-Nikodym step survives with the factor e^{42 h_0 N^2}; a small h_0 absorbs it at one fixed scale. The step that needs the symmetry is the decoupling of annuli: Proposition 2.8 (pinning monotonicity), through Lemmas 2.4 to 2.7. In a field of varying direction it is false (P1). The replacement (Lemma MK) needs the zero-field crossing bound for all pins, PIN-U. For the coarse-orientation proof the decoupling survives and the symmetry is needed in Lemma 6.4 only; what is left is Lemma CO.
2. From crossing estimates to the kernel. Crossing estimates in a field give the sign part for all observables (Proposition SS). The even part is EV. It does not follow from crossing estimates (model 5.4).
3. Exact failing statements: 5.3. Counterexamples on models that satisfy every input used: P1, A1, model 5.4; G1, G2 of row 1091.

#### 7.4 Limits

- Nobody has checked this file. Row 1091's M1, M2, FST-BD were checked by row 1094; row 1093's file had no verdict when I read it.
- OpenAI's and Ding, Huang and Yang's papers and Pei's paper are unrefereed. Every statement marked GIVEN one of them is conditional on it. Ding, Huang and Yang's proofs were not read; their Theorem 5.2 enters only through Pei's Proposition 3.1 and in 5.3.
- Ding, Song and Sun: abstract only. Frohlich and Spencer, Peierls, the ghost-spin FKG argument: from memory, cited, not rebuilt; none carries a PROVED mark except Peierls in model 5.4, marked GIVEN.
- PIN-U is stated for the first sign component and annulus graphs. The O(4) invariance covers every direction, since the pins are arbitrary.
- Lemma CO compares two systems on one pinned square. Tori need Pei's box conditioning; not written.
- Files changed: this file only. Scratch: `/tmp/sheetfield-pei.*`, `/tmp/sheetfield-dhy.*`, `/tmp/sheetfield-dss*`, `/tmp/sheetfield-num`. No commit, no push.

#### 7.5 Credits

Yan Ru Pei for the one-scale Radon-Nikodym transfer, the adapted sign-cluster chain, the transfer of the bad-site estimate and the remark that a field breaks only the symmetry lemma. OpenAI's authors for the O(4) mixing theorem, the pinned charged decay (3.61), the bad-site estimate (3.58), the coarse orientations and the association argument of Section 3.11. Jian Ding, Fenglin Huang and Peng Yang for the annulus crossing theorem, uniform over local-time boundary conditions, and for stating the open case of all spin boundary conditions. Jian Ding, Jian Song and Rongfeng Sun for the Ising inequality with external fields. Massimo Campbell and Lincoln Chayes, Ulli Wolff, Robert Edwards and Alan Sokal for the sign-cluster representation. Jean Ginibre; Robert Griffiths; Cees Fortuin, Pieter Kasteleyn and Ginibre; Charles Newman; Jacob van den Berg and Christian Maes; Roland Dobrushin and Senya Shlosman; Rudolf Peierls; Jurg Frohlich and Thomas Spencer; Christophe Garban and Nathan de Montgolfier for the results named in the text. Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, and Tadeusz Balaban, for the account and the ultraviolet construction that the face route serves; neither is a gap input here. Row 1091 (Claude Fable 5.2 medium) for M1, M2, FST-BD, FST-F, G1, G2; row 1094 (gpt-6-astra xhigh) for the check, (Q1)-(Q3) and the corrections of 5.0; row 1092 (gpt-6-luna high) for finding Pei's paper; rows 1077, 1078 for the face law and (17).

### Step 8 result

RESULT: FST-F for the O(4) sheet at beta in [2.3, 2.6] is NOT proved and stays OPEN; no counterexample for the sheet was found. PROVED GIVEN row 1091's FST-BD (checked by row 1094): the weaker one-sided statement FST-F1 (one-site field response plus covariance with a local observable, Lipschitz sum on the non-local side only, all observables) still gives (17) on 0 <= lambda <= min(h_0/2, 1/(12 X_1 e^a S_a)) for periodic local limits. Pei's transfer in a field of varying direction: the Radon-Nikodym step SURVIVES with factor e^{42 h_0 N^2} (PROVED, Lemmas RN and MK); the step that needs the symmetry is the pinning monotonicity that decouples annuli (Pei's Proposition 2.8 with Lemmas 2.4 to 2.7), which FAILS in every nonzero field against the pole (PROVED three-site counterexample P1; amplitude counterexample A1), and Lemma 6.4 in his coarse-orientation proof. PROVED GIVEN PIN-U (zero-field annulus crossing bound uniform over all pins): cluster decay in every field with h_0 of order 1/N^2 and, for all observables, the sign part of the covariance kernel (Proposition SS). PROVED GIVEN PIN-U and EV (the same kernel for the even conditional means): FST-F1. PIN-U is PROVED GIVEN OpenAI's (3.61) only for one-signed pins; for mixed signs (3.61) bounds a difference where PIN-U needs the sum; EV is not given by crossing estimates (PROVED GIVEN Peierls: a non-O(4) model with PIN-U and without EV). PIN-U and EV are OPEN; the seven proof routes of section 5.3 stop or FAIL at stated steps. FST-N is not used as an input (row 1094's correction). Unchecked, not formalized, no mass gap claimed.
