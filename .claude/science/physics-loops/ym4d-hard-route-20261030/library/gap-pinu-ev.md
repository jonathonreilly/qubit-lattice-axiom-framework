lead: Claude Opus 5.5 lead session, row queued 2026-11-17 07:07Z
row: FINISH 1099, written by Claude Fable 5.2 medium (laptop subagent)

# gap-pinu-ev (FINISH 1099)

## Plan (at most eight steps; refined after step 1)

1. Read row 1099 in FINISH.md in full; restate the target and its inputs here.
2. Read the source files the row names; record the exact definitions used.
3. Check the repo and prior files for the same statement (git grep).
4. Pull; see whether the optional check files (rows 1097, 1098) are finished.
5. Write the proof or the counterexample for the row's main claim.
6. Do the secondary claims of the row.
7. Guide-only numeric check if the row allows one.
8. Marks, scope of each mark, credits, RESULT line.

Research text, not an audit. It grants no status. It claims no Yang-Mills mass gap.
PROVED means a written hand argument in this file. Nobody has checked it yet. Nothing was formalized in Lean.

## Step log

### Step 1 result: the brief, the inputs, the check files

Brief (FINISH row 1099, read in full). For the two-dimensional O(4) model at beta in [2.3, 2.6]:
(A) EV in the form of row 1096, or a replacement that with Proposition SS still gives FST-F1.
(B) PIN-U, or a replacement that still gives cluster decay in a small field of varying direction (the role of Theorem T2).
Hardest first. Ideas to test, not to assume: for (B) the sum of the connection probabilities to pins of the two signs against the difference; re-signed pins; a sign-flip coupling on the complementary components; Ding, Huang and Yang's local-time boundary conditions. For (A) a reduction of the even sector to lower models; an induction on n.

After `git pull --ff-only` (2026-11-17):
- `library/gap-sheet-field.md` (row 1096): read in full (281 lines).
- `library/prior/gap-fstn-read-luna.md` (row 1095): read in full.
- `library/gap-sheet-field-check-opus.md` (row 1097): exists, 5.5 kB, its last line is not a RESULT line. It is unfinished. I do not use it.
- `library/gap-sheet-field-check-astra.md` (row 1098): absent.
So row 1096 is unchecked when this row starts. Everything below that is marked GIVEN a statement of row 1096 is conditional on it.

Definitions taken from row 1096 (exact text there): Lemma B (bond coupling in a field), Lemma RN, Lemma MK, Hypothesis PIN-U(N, p), Theorem T2, Lemma PIN+, Proposition SS, Hypothesis EV(h_0, a, X_ev), Theorem SS+EV, model 5.4, FST-F1 with parts (R) and (L).

### Step 2 (first part): sources opened, and working notes saved before the proofs

Downloads, each in a new empty directory, nothing copied to the repository:
- Pei, arXiv:2611.01532 (e-print source, `/tmp/pinuev-pei.RYIkOC/x/aniso-heisenberg.tex`, 1559 lines).
- Ding, Huang and Yang, arXiv:2611.04908 (e-print source, `/tmp/pinuev-dhy.rDOJGb/x/`, six TeX files).
- OpenAI O(4) paper: no new download; I read row 1078's copy at `/tmp/opus-face2d-openai.NylL2Z/src/preliminary.tex` (row 1091 records its pin; I did not re-verify the pin).
- `library/prior/gap-face-stability-read-luna.md` (row 1092): read in full.

Facts read so far that the proofs below use (exact places):
- Pei, Theorem 6.1 (`thm:main4`), n = 4, assumes (I1)-(I3): for every (beta, theta)-admissible system (finite V in Z^2, any edge set, any pin set P with any values, b_e in [-beta, beta]), every odd one-spin observable O and every one-spin observable O': (a) |<O(sigma_x)>| <= A_* ||O|| exp(-dist_inf(x,P)/Xi(beta)); (b) |<O(sigma_x) O'(sigma_y)>| <= A_* ||O|| ||O'|| exp(-min{||x-y||_inf, dist_inf(x,P)}/Xi(beta)). In (b) only the odd site x must be far from the pins. I use (a) at theta = 0 only.
- Ding, Huang and Yang, proof of their Theorem 5.1 from Theorem 5.2 (file `Fractality_1025.tex`, lines 17-75). They decouple annuli with no pinning monotonicity. They condition on the sigma-field F_w^ext: the xy local times outside the interior of the annulus, the connectivities outside, and the z-copy local time of loops that meet the outside. The conditional law inside is their loop model with an xy local-time boundary condition, and Theorem 5.2 is uniform over these. Signs are not conditioned on.
- Ding, Huang and Yang, Section 2.3, display (2.11) in my count (`eq: relation between spin boundary condition and local time boundary condition`): the law under a spin boundary condition zeta equals the law under the local-time boundary condition, times 2^{-kappa^x - kappa^y}, times the indicators that boundary vertices of opposite sign are not connected, copy by copy. Remark 1.3: decay for all spin boundary conditions "does not seem to be that immediate".

Working notes (ideas found while reading; each is tested in the steps below; none is a result yet):
- N1. Exact identity: the law under mixed-sign pins is the law under the re-signed pins conditioned on the event D that no cluster joins pins of opposite sign. Same statement as Ding, Huang and Yang's display, in Pei's bond language.
- N2. Exploration of the clusters of the minus pins. Given their union S and the spins on S, the rest is a model whose only sign-breaking pins are the plus pins. So P(x <-> plus pins | S) is the mean of an odd one-site observable there, and Pei's Theorem 6.1(a) bounds it by A_* exp(-dist(x, S and pins)/Xi). Plus and minus pin clusters can reach deep only together.
- N3. A wall-monotonicity lemma would finish PIN-U from N2. It fails as a general lemma on two sites (the wall can cancel the complementary pull of a pin).
- N4. In a field, the cluster representation in all four coordinates turns the field into even cluster weights cosh h(C). The outside of an annulus then acts through boundary blocks with fields a_j. Blocks with small |a_j| cost nothing. Blocks with large |a_j| are sign pins. So an unsigned crossing bound (the class of Ding, Huang and Yang's Theorem 5.2) replaces PIN-U exactly when long clusters are excluded a priori. The a priori bound is circular in my attempts.
- N5. Duplicate system: swapping the two replicas on a swap cluster is an exact symmetry in every field and under every pin. It bounds the full covariance, with no even part left. But the swap variable (sigma - sigma')/2 has four components, its zero set has codimension four, and the swap clusters should percolate. To test by a guide run.
- N6. For EV: given the amplitudes r, the complementary parts form an O(3) model in a field and the bonds an Ising bond model; they are independent. So Cov(F_X, G_X) splits into an O(3)-in-field piece, an Ising bond piece and an amplitude piece. The amplitude piece does not reduce to a lower model. Model 5.4 violates exactly it.

Refined plan for the remaining steps:
3. Finish the source reading: OpenAI (3.61) and Section 3.11 statement lines; Pei Remark 7.10 (`rem:twosite`); Ding, Huang and Yang's definition of xy boundary conditions and their Theorem 5.3. Decide which of (A), (B) to attack first.
4. (B): N1, N2, N3 with proofs; the layer-wise one-signed case; the exact open statement.
5. (B) in a field: N4 with proofs; the replacement statement and what it needs.
6. (A): N6 with proofs; N5 with proof and guide run.
7. Marks, limits, credits.
8. RESULT line.

### Lead note received during step 2, and its effect

The lead reported that the same-provider check of row 1096 landed. After a new `git pull --ff-only` the file `library/gap-sheet-field-check-opus.md` (row 1097, Claude Opus 5.5 max, by hand) is finished: its last line is a RESULT line, verdict "HOLDS AFTER CORRECTION, no item FAILS". I read its steps 4 to 8 (lines 75-199). Row 1098's file is still absent. The corrections that bind this row:

- C1. In FST-F1 and in EV the numbers X(B) and X_ev(B) depend on B only up to translation. They do not depend on the torus, the field or the observables. Every replacement below is stated with this rule.
- C2. Lemma MK needs: the auxiliary families of distinct blocks are independent given the spins (for bonds: the bonds of edges with an endpoint in R_j).
- C3. P1 holds for small h > 0 and b < b_0(h), against the pole. A1 holds for small b only; row 1097's quadrature guide shows its sign positive at b = 2.5. Neither is a statement at the window couplings.
- C4. The torus form of Theorem T2 is ARGUED.
- C5. "(3.61) bounds the difference, PIN-U needs the sum" is where one derivation stops. It is not "the exact gap". Other routes to PIN-U are not excluded.
- C6. Route 1 of row 1096's 5.3 already contains my note N1 (mixed-sign pinned law = one-signed law conditioned on D; conditional FKG; the tilt by FK(D | r)). Row 1097 confirmed it and corrected one parenthesis: under one-signed pins the Ising factor is log-supermodular in r; the obstruction to amplitude association is the complementary factor with pins of several directions. So N1 is prior work of row 1096, not new here.
- Lemma B's bond-law formula is for unpinned systems. Row 1097 confirms PIN-U, with EV and the torus bookkeeping, as the exact remaining input of row 1096's route.

### Step 3 result: rest of the reading; which target first

- OpenAI, Section 3.10 (source lines 975-1016 of `preliminary.tex`; label `eq:pre:10-3`; this is the display that Pei and row 1096 call (3.61), I did not recount the number). For a bounded observable O on A whose average under a common left rotation is identically zero, in the signed, twisted, pinned class: |E O| <= C ||O|| |A| e^{-c d_pin/s}. It covers observables of several spins. Section 3.11 opens with "use the untwisted zero-field ferromagnet ... This restriction is essential. Neither the association argument nor its conclusion is being claimed for arbitrary pinned or frustrated systems."
- OpenAI, Theorem 3.1 (lines 22-40): unpinned tori with sides at least C Xi, and unpinned free subgraphs; 0 <= beta_e <= beta; local F, G on A, A' at distance d: |Cov(F,G)| <= C (1 + beta + |A| + |A'| + d)^20 L_F L_G e^{-c d/Xi}. Both observables are local.
- Pei, Remark 7.10 in the brief's count (`rem:twosite`): for the isotropic model OpenAI's Section 3.10 gives decay for every bounded observable with zero common-left average; for anisotropic couplings this fails on two sites for (u^1)^2 - 1/4. So at zero field and isotropic couplings, which is the setting of PIN-U, the larger class of OpenAI is available. Pei's restriction to odd observables is a restriction of his anisotropic theorem.
- Ding, Huang and Yang, Section 2.2.2 (`prelim_1029.tex` lines 110-133) and Theorem 5.2: the boundary class is copywise: local times xi^x, xi^y on the boundary and partitions P^x, P^y. Their domain Markov step for the z-copy conditions on the z-loops that meet the outside and lowers the local-time budget to beta - beta^z. They state the case 2 < N <= 3 and write that N > 3 "follows verbatim". I did not read the proof of Theorem 5.2 or 5.3.

Which target first (ARGUED, a judgment). I started with (B). Reason: Lemma CR below shows that all sign information of the pins travels through the pin clusters. If pin clusters stay shallow, the deep region sees the pins only through sign-free data. So (B) decides whether the sheet has any pin-uniform statement for even quantities, and (A) is of that kind. I found no reason to expect that either statement is false for the O(4) sheet.

### Step 4 result: (B) at zero field. What is proved about mixed-sign pins

Setting for this step. A finite graph G = (V, E) in Z^2, strengths b_e in [0, beta], a pin set P with values omega, zero field, the O(4) law P_omega on the unpinned sites, with Pei's bonds for the first coordinate: given the spins, eta_e = 1 with probability p_e 1{tau_x = tau_y}, p_e = 1 - exp(-2 b_e r_x r_y), independently. Here sigma_v = (tau_v r_v, q_v u_v), r_v = |sigma_v^1|, u_v in S^2. Pi_+ and Pi_- are the pins with positive and negative first coordinate. A pin with r = 0 carries no open bond. "x <-> Pi_+" means that the open cluster of x contains a site of Pi_+. S_- is the union of the open clusters that meet Pi_-; S_+ likewise. Row 1096's Lemma PIN+ and route 1 of its 5.3 are prior work (C6).

**Lemma CR (the plus clusters reach only where the minus clusters reach; PROVED GIVEN Pei's Theorem 6.1(a) at theta = 0, which assumes (I1)-(I3)).** For every unpinned x, almost surely on {x not in S_-},

    P_omega(x <-> Pi_+ | S_-, sigma on S_-) <= A_* exp(-(dist_inf(x, S_- united with P) - 2)/Xi(beta)).

The same holds with the signs exchanged.

Proof. Fix a set S_0 containing Pi_- and a spin configuration s on S_0 with negative first coordinates. The event {S_- = S_0} is the intersection of an event of the bonds inside S_0 (every site of S_0 is joined to Pi_- inside S_0) and the event that every edge between S_0 and its complement is closed. The joint density of spins and bonds is a product over edges of e^{b_e sigma_x.sigma_y} times the bond kernel. So, given S_- = S_0 and sigma = s on S_0, the spins on V \ S_0 have density proportional to

    exp{ sum over edges e inside V \ S_0 of b_e sigma_x.sigma_y + sum over edges e = {x,y}, x in S_0, y not in S_0, of phi_e(s_x, sigma_y) },
    e^{phi_e} = e^{b_e s_x.sigma_y} (1 - p_e 1{tau_y = -}) = exp{ b_e q_x q_y u_x.u_y - b_e r_x |sigma_y^1| },

and the bonds inside V \ S_0 keep Pei's kernel. (For tau_y = -: b r_x r_y - 2 b r_x r_y; for tau_y = +: -b r_x r_y.) Call this system Sys. The wall terms phi_e are even in sigma_y^1. The pins of Sys with r > 0 all lie in Pi_+ (S_0 holds no site of Pi_+, since a cluster has one sign). In Sys take an open cluster C without such a pin and reflect the first coordinate on C. Edges inside C keep their weight. Edges from C to its complement are closed, and e^{b sigma.sigma'}(1 - p 1{same sign}) = exp(b q q' u.u' - b r r') for either relative sign. The wall terms are even. So the weight is invariant: clusters without a pin of Pi_+ have a fair sign, clusters with one have sign +. Hence E_Sys[tau_x] = P_Sys(x <-> Pi_+).
Put d = dist_inf(x, S_0 united with P). If d <= 2 the bound is trivial (A_* >= 1 may be assumed). Let B be the set of v in V with ||v - x||_inf <= d - 2. No site of B, and no neighbour of B, lies in S_0 or P. The spin marginal of Sys is a nearest-neighbour Gibbs law. Condition on all spins of V \ (S_0 united with B). On B the law is then the isotropic O(4) law with strengths in [0, beta] and pins on the outer neighbours of B; no wall term touches B. sgn sigma^1 is an odd bounded one-spin observable. Pei's Theorem 6.1(a) with theta = 0 gives |E[tau_x | outside]| <= A_* exp(-(d-1)/Xi) <= A_* exp(-(d-2)/Xi); with no outer neighbour the mean is zero. Average over the outside. QED

**Corollary CR2 (PROVED GIVEN the same).** For x unpinned and every integer d with 2 <= d <= dist_inf(x, P), let T_d(x) be the event that S_+ and S_- both contain a site within sup distance d of x (a two-colour event). Then

    P_omega(x <-> P) <= 2 A_* e^{-(d-2)/Xi} + 2 P_omega(T_d(x)).

Proof. P(x <-> Pi_+) = P(x <-> Pi_+, dist(x, S_-) >= d) + P(x <-> Pi_+, dist(x, S_-) < d). Lemma CR bounds the first term by A_* e^{-(d-2)/Xi}. The second event lies in T_d(x). Exchange the signs and add. QED

**Lemma FREE (clusters that meet no pin; PROVED GIVEN Pei's Theorem 6.1(b) at theta = 0).** For unpinned x, y:

    P_omega(x <-> y) <= A_* exp(-min{||x-y||_inf, dist_inf(x,P)}/Xi) + P_omega(x <-> Pi_+, y <-> Pi_-) + P_omega(x <-> Pi_-, y <-> Pi_+).

Proof. Given the amplitudes, the complementary parts and the bonds, a cluster with a pin of r > 0 has the sign of that pin and the other clusters have independent fair signs (the reflection argument above, without walls). So E[tau_x tau_y | ...] = 1{x <-> y} + 1{x not<-> y} m_x m_y, with m_x = +1, -1 or 0 when the cluster of x meets Pi_+, Pi_- or neither. Take expectations and use Theorem 6.1(b) with O = O' = sgn sigma^1. QED

**Hypothesis PIN-2(N, d, p_2).** For every annulus graph on D_N(z) with strengths in [0, beta], every pin configuration on the two layers, and every unpinned x with dist_inf(x, layers) >= N/4: P_omega(T_d(x)) <= p_2.

**Theorem B1 (PROVED GIVEN Pei's Theorem 6.1(a), (b) at theta = 0).** Let N >= 8 and 2 <= d <= N/4. Let E' be the event that an open path inside the middle annulus {v : 5N/4 <= ||v - z||_inf <= 7N/4} joins its inner ring to its outer ring. PIN-2(N, d, p_2) gives, for all pins,

    P_omega(E') <= 196 N^2 [ A_* e^{-N/(4 Xi) + 1/Xi} + 2 A_* e^{-(d-2)/Xi} + 2 p_2 ].

Theorem T2 of row 1096 holds with E' in place of the crossing event and this number in place of p.

Proof. On E' some x on the inner ring and y on the outer ring of the middle annulus are joined. Each ring has at most 14N sites. ||x - y||_inf >= N/2 - 1 and dist_inf(x, P) >= N/4, so the first term of Lemma FREE is at most A_* e^{-(N/4 - 1)/Xi}. The other two terms are at most P(x <-> Pi_+) + P(x <-> Pi_-) restricted as in Corollary CR2, that is 2 A_* e^{-(d-2)/Xi} + 2 p_2. For T2: a path from x to y at sup distance above 4N crosses the middle annulus of each annulus on its coarse path; E' is an event of bonds with both ends in R_j; Lemma MK applies with correction C2. The rest is Pei's count, as checked by row 1097. QED

So PIN-U can be replaced by PIN-2: only the two-colour event of the pin clusters must be bounded. PIN-U(N, p) with crossings joined to the layers implies PIN-2 with p_2 of order N^2 p at a smaller scale; I do not write that direction. PIN-2 is OPEN.

**Lemma LS (layer-wise one-signed pins; PROVED GIVEN Pei's Theorem 6.1 at theta = 0 and row 1096's route 1 identity, checked by row 1097).** If the pins of one layer have nonnegative first coordinates and those of the other layer nonpositive ones, then P_omega(E') <= p'/(1 - p_+), with p' = 196 N^2 A_* e^{-(N/4 - 1)/Xi} and p_+ = 12 N A_* e^{-(N/2 - 1)/Xi}.

Proof. Let nu be the law with all first coordinates of the pins made nonnegative. P_omega = nu(. | D), D = {no cluster holds pins of both signs} (route 1). Under nu, D fails only if the layers are joined; Lemma PIN+ gives nu(D^c) <= p_+. Under nu the last two terms of Lemma FREE vanish, so nu(E') <= p'. QED

So mixed signs are a difficulty only when the sign changes along one layer.

**Lemma DA (PIN-U is a neutral statement up to a small error; PROVED GIVEN OpenAI's Section 3.10 display `eq:pre:10-3`).** Let p_e(sigma) be the conditional probability, given the spins, that the middle annulus is crossed by open bonds of the sign clusters of the coordinate sigma.e. Let rho(sigma) be the Haar average of p_e(sigma) over e in S^3. Then rho is invariant under common left rotations, and for all pins |P_omega(E') - E_omega[rho]| <= C |A| e^{-c N/(4 s)}, A the middle annulus.

Proof. p_{e_1}(k sigma) = p_{k^{-1} e_1}(sigma), so p_{e_1} - rho has zero common-left average. It is bounded by 1 and is a function of the spins of the middle annulus, at distance at least N/4 from the pins. QED

Reading (ARGUED). PIN-U is thus one case of the neutral question: bound E_omega[rho] for one rotation-invariant function, uniformly in the pins. Every direction e has the same crossing probability up to the error. For a direction e with all pins in one closed half-space, Lemma PIN+ applies. Pins that lie in no half-space are the open case.

**Lemma W (a wall-monotonicity step FAILS as a general lemma; PROVED).** Lemma CR would give PIN-U if the wall terms of Sys never raised P_Sys(x <-> Pi_+) above its value on the graph with S_0 deleted (there Lemma PIN+ applies with the plus pins only). That monotonicity is false on this example. One free site y, one pin p = (r, q u) with 0 < r < 1, strength b > 0 on {p, y}. The wall is one site x with sigma_x = (-r, -q u), strength b on {x, y}; its term is phi = -b q u.sigma_y^perp - b r |sigma_y^1|. Then for small r > 0: E_wall[tau_y] > E_no wall[tau_y]; both equal the probability that y is joined to p.

Proof. Write s = sigma_y^1. With the wall the density is proportional to exp(b r s - b r |s|). Without it, to exp(b r s + b q u.sigma_y^perp). Both means vanish at r = 0 for every q. The r-derivatives at 0 are b E_unif|s| and b E_kappa|s|, where E_kappa is the law proportional to exp(kappa u.sigma^perp), kappa = b (the even term -b r|s| and the change of q do not enter at first order). d/dkappa E_kappa|s| = Cov_kappa(|s|, u.sigma^perp). Put rho = |sigma^perp|. Given rho, sigma^perp/rho is von Mises-Fisher on S^2 with parameter kappa rho, so E[u.sigma^perp | rho] = rho (coth(kappa rho) - 1/(kappa rho)), strictly increasing in rho; |s| = sqrt(1 - rho^2) is strictly decreasing; rho has a positive density. So the covariance is negative for every kappa >= 0 and E_unif|s| > E_b|s|. QED

Guide quadrature (below, one job): E|s| = 0.4244 uniform; 0.4218 at kappa = 0.5; 0.3756 at kappa = 2.5. Scope: the wall site cancels the complementary pull of the pin. Lemma W refutes one lemma. It does not refute PIN-U or PIN-2. It holds at every b > 0, the window included, for small r.

Where (B) stands at zero field. PROVED GIVEN the cited inputs: PIN-U for layer-wise one-signed pins; the reduction of PIN-U to the two-colour bound PIN-2; the reduction to one neutral mean. OPEN: PIN-2, hence PIN-U for pins whose signs change along a layer. Failing step of the direct route: after exploring S_-, the bound of Lemma CR needs distance from S_-, and nothing read controls the system Sys within distance of order Xi log N of the wall.

### Step 5 result: (B) in a field. What the outside of an annulus does

Use all four coordinates. sigma_v = (tau_v^k a_v^k), k = 1..4, a_v^k = |sigma_v^k|. Bonds eta^k for each coordinate: eta_e^k = 1 with probability (1 - exp(-2 K_e^k)) 1{tau_x^k = tau_y^k}, K_e^k = b_e a_x^k a_y^k, independently.

**Lemma J (PROVED).** On an unpinned finite graph with field H, the joint density of (a, tau, eta) with respect to the product of the amplitude laws and counting measures is proportional to

    prod over k, e of (2 sinh K_e^k)^{eta_e^k} (e^{-K_e^k})^{1 - eta_e^k}  x  1{tau^k is constant on the eta^k-clusters, all k}  x  exp{ sum over k, v of H_v^k a_v^k tau_v^k }.

Proof. e^{K tau tau'} times the kernel is e^{K}(1 - e^{-2K}) 1{tau = tau'} for eta = 1 and e^{-K} for eta = 0. QED

**Lemma BF (block fields; PROVED).** Let R be a set of sites and dR its outer neighbours. Let F_4 be the sigma-field of the amplitudes a_v, v not in R, and of the bonds eta_e^k on edges with no end in R. A block is a pair j = (k, piece), where the piece is a cluster of eta^k restricted to those edges that contains a site of dR; its field is a_j = sum over v in the piece of H_v^k a_v^k. Then, given F_4, the law of the spins of R and of the bonds on edges with an end in R is

    sum over s of pi(s) Z_R^H(s) P_{R, s}^H(.)  /  sum over s of pi(s) Z_R^H(s),     pi(s) = prod_j e^{s_j a_j},

where s runs over the signs of the blocks, P_{R,s}^H is the law on R in the field H restricted to R with dR pinned at the amplitudes given by F_4 and the signs s, and Z_R^H(s) is its partition function.

Proof. By Lemma J the signs outside R enter through the constraint and the field factor only. Sum over the signs of the outside clusters. Clusters without a site of dR give factors 2 cosh(field) that do not depend on R. A block with sign s_j gives e^{s_j a_j}. The remaining factors are the weight of the pinned system on R. QED

**Corollary BF (PROVED).** Let P^sym_R be the mixture with pi = 1 and H = 0 (zero field, block signs summed with the weights Z_R^0(s)). For every event E of the spins and bonds of R:

    P^H(E | F_4) <= exp{ 2 sum_j |a_j| + 2 |H| |R| } P^sym_R(E),   and sum_j |a_j| <= |H| times the number of sites in the pieces.

Proof. pi(s) lies in [e^{-sum|a_j|}, e^{sum|a_j|}]. The unnormalised weights Z^H P^H and Z^0 P^0 differ by a factor in [e^{-|H||R|}, e^{|H||R|}], since sum_k |H_v^k| a_v^k <= |H_v|. QED

**Hypothesis UNS(N, p).** For every annulus graph and all boundary data (amplitudes on the layers, a partition of the layer sites into blocks for each coordinate): P^sym_R(E') <= p.

UNS is PIN-U with the sup over the block signs replaced by the average with weights Z(s). It is the bond-language form of a crossing bound uniform over local-time boundary conditions with partitions. Ding, Huang and Yang's Theorem 5.2 with their domain Markov step is a statement of this kind for N in (2, 3], with "verbatim" claimed for N > 3. The translation to four coordinates and to this conditioning is not written here: UNS is ARGUED GIVEN their Theorem 5.2, not proved.

**Theorem B2 (PROVED GIVEN UNS(N, p)).** Take a finite unpinned subgraph of Z^2, strengths in [0, beta], a field with |H| <= h_0, and annuli j = 1..k with pairwise disjoint closed 2N-boxes. Let E'_j be the crossing of the middle annulus of j and G_j(W) the event that the pieces of annulus j have at most W sites in total. Put q = e^{2 h_0 (W + 21 N^2)} p. Then

    P^H(E'_1 and ... and E'_k) <= q^k + sum_{i=1}^{k} q^{k-i} P^H(G_i(W)^c) <= q^k + max_i P^H(G_i(W)^c)/(1 - q)   if q < 1.

Proof. E'_i for i < k is F_4-measurable for annulus k (its bonds have no end in R_k), and so is G_k(W). By Corollary BF and UNS, P^H(E'_k | F_4) <= q on G_k(W). So u_k <= q u_{k-1} + P(G_k(W)^c). Iterate. QED

Where this stops (the exact failing step). With W = 1/(2 h_0) the factor is harmless. G_j(W)^c needs a cluster of at least 1/(2 h_0 #pieces) sites, of some coordinate, that touches a layer: a long cluster in the field model. Its probability is the quantity under proof, at a larger scale. In the union over coarse paths the term max P(G^c)/(1-q) is multiplied by the number of paths, so an a priori bound on long clusters in a field is needed first. I found none. On graphs with at most 1/(2 h_0) sites the theorem gives nothing beyond Lemma RN.

**Remark (why the average cannot replace the sup inside this scheme; PROVED as stated).** In Lemma BF let the fields a_j tend to plus or minus infinity. The mixture tends to the single pinned law with those signs. Every sign pattern that is constant on blocks arises, and singleton blocks arise when the outside bonds are closed. So a bound on P^H(E | F_4) that is uniform in the outside data, with no control of the a_j, is PIN-U for all four coordinates. The only slack is control of sum_j |a_j|.

Result for (B) in a field. UNS can replace PIN-U exactly when the field mass sum_j |a_j| of the outside clusters at an annulus is controlled. That control is OPEN (circular in my attempts). Cluster decay in a small field of varying direction stays OPEN.

### Step 6 result: (A). The even sector

**Lemma EV-split (PROVED).** Unpinned graph, field H, first-coordinate representation, X = (r, u, eta). Given the amplitudes r: (i) u and (tau, eta) are independent; (ii) u has the law on (S^2)^V proportional to exp{ sum_e b_e q_x q_y u_x.u_y + sum_v q_v H_v^perp.u_v }, an O(3) model with strengths in [0, beta] and a field of norm at most |H| and varying direction; (iii) eta has the bond law of Lemma B at the couplings b_e r_x r_y. For f = F_X, g = G_X:

    Cov(f, g) = E[ E_eta Cov_u(f, g | r, eta) ] + E[ Cov_eta(E_u f, E_u g | r) ] + Cov(E[F | r], E[G | r]).

Proof. Given r the density factors into the Ising part in tau and the part in u (row 1096's Lemma 2.1 reading, checked by row 1097 under Lemma B). Apply the law of total covariance twice. QED

Test of the idea "an induction on n". The first piece is a covariance in an O(3) model in a field. To bound it for all r one needs the kernel (L) for O(3), uniformly in strengths in [0, beta] and in fields: the target one component lower, with nothing known in the sources read (OpenAI's Theorem 3.1 and Section 3.10 use the group S^3). One more step down asks for the kernel for O(2) uniformly in strengths in [0, beta]; at beta in [2.3, 2.6] the constant strength beta lies in the regime where the plane rotator is expected to have power-law decay (Frohlich and Spencer prove it for large coupling; I did not check that 2.3 is large enough for their proof). So the induction asks at its lower levels for statements that are open (n = 3) or expected false (n = 2). ARGUED; the scheme stops at its first step. The third piece, the amplitude covariance, does not reduce to a lower model at all; row 1096's model 5.4 violates exactly this piece (there u and eta are trivial). So any proof of EV must bound Cov(E[F | r], E[G | r]) by O(4)-specific means.

**Lemma EV0 (zero field, both observables local; PROVED GIVEN OpenAI's Theorem 3.1, Pei's Theorem 6.1(b), (c) at theta = 0 and row 1096's Proposition SS).** On unpinned free subgraphs and on tori with sides at least C Xi, strengths in [0, beta], H = 0, F and G local on A, A' at distance d:

    |Cov_0(F_X, G_X)| <= C (1 + beta + |A| + |A'| + d)^20 L_F L_G e^{-c d/Xi} + pi osc(G) A_* e |A'| sum_w Lip_w(F) e^{-dist(w, A')/Xi}.

Proof. Cov(F_X, G_X) = Cov(F, G) - E Cov(F, G | X). Theorem 3.1 bounds the first term. Proposition SS bounds the second by pi osc(G) sum_w Lip_w(F) P_0(w <-> A'), and without pins P_0(w <-> b) = E_0[tau_w tau_b] (Lemma FREE with no pins), which Theorem 6.1(b), (c) bounds. QED

So at zero field without pins EV holds for local pairs with OpenAI's polynomial prefactor. EV as row 1096 states it asks for more: a non-local F entering through sum_w Lip_w(F), a constant X_ev(B) depending on B up to translation only (C1), and every field with |H| <= h_0. Each of the three is OPEN. Failing step of the transfer: Lemma RN moves a zero-field bound into a field only on a box of one scale and only if the bound is uniform over the pins of the box; Theorem 3.1 has no pins.

**Proposition SW (the duplicate system removes the even part; PROVED).** Take any finite graph, strengths b_e >= 0, any field H, any pins (the same in both copies). Let (sigma, sigma') be two independent copies and d_v = (sigma_v - sigma'_v)/2. Given the pair, open the swap bond zeta_e with probability 1 - exp(-4 b_e (d_x.d_y)_+), independently. Then for F in Lc and G bounded on B:

    |Cov_H(F, G)| <= (pi/2) osc(G) sum_w Lip_w(F) (P^H x P^H)(w is joined to B by swap bonds).

Proof. sigma_x.sigma_y + sigma'_x.sigma'_y = 2 (s_x.s_y + d_x.d_y) with s = (sigma + sigma')/2, and H.(sigma + sigma') = 2 H.s. Let S be a union of swap clusters and T_S the exchange of sigma_v and sigma'_v for v in S. It maps d to -d on S and fixes s. Edges inside S or outside S keep d_x.d_y. Edges between S and its complement are closed, and e^{2b d.d'}(1 - p) = e^{-2b|d.d'|} is invariant. The field term and the product reference measure are invariant. Pins have d = 0, carry no bond and are fixed. So T_S preserves the joint law when S is a function of the bonds. Take S = the union of the clusters that meet B and T = T_S. Then G(sigma) - G(sigma') changes sign under T. With DF = F(sigma) - F(sigma'): E[DF DG] = -E[(DF o T) DG], so 2 Cov(F,G) = E[DF DG] = (1/2) E[(DF - DF o T) DG]. |DF - DF o T| <= 2 pi sum over w in S of Lip_w(F), and |DG| <= osc(G). QED

Proposition SW needs no PIN-U and no EV: decay of the swap connectivity, uniform in tori and fields, would give (L) and (R) of FST-F1 with X(B) = (pi/2) A |B|, which satisfies C1. It answers the brief's idea of a sign-flip coupling: the exchange is an exact symmetry in every field and under all pins.

**The swap replacement at the window couplings: refuted by a guide run, not by a proof.** The swap vector d has four components; its zero set has codimension four in a two-dimensional lattice, so no closed curve of weak bonds is forced. Guide run (pure Python, Wolff updates, two independent replicas, zero field, torus; one serial job, nice 10; script and output in the session scratch folder `.../scratchpad/pinuev-num/guide.py`, `guide.out`, not in the repository; 12 measurements per line, no error bars):

| L | beta | swap bond density | largest swap cluster / volume | P(x joined to x + L/2), swap | same for first-coordinate sign clusters |
|---|---|---|---|---|---|
| 24 | 2.5 | 0.836 | 0.976 | 0.952 | 0.376 |
| 48 | 2.5 | 0.847 | 0.974 | 0.949 | 0.116 |
| 48 | 2.3 | 0.785 | 0.953 | 0.908 | 0.089 |

The swap clusters fill the torus at both sizes; the sign clusters shrink with L. So the right side of Proposition SW does not decay there. Mark: the replacement "swap-cluster decay" FAILS at beta = 2.3 and 2.5 at zero field according to the guide run; no proof of percolation is given. Proposition SW itself stands. It is useful only where swap clusters are small (for example small beta).

Result for (A). EV stays OPEN. Proved: its split into three pieces; the zero-field local case; a duplicate-system bound that has no even part but whose clusters percolate in the guide run. Failing steps: the amplitude piece has no lower-model form; the field transfer needs pins.


### Step 7 result: marks, limits, credits

#### 7.1 Marks

| Mark | Statement and scope |
|---|---|
| PROVED GIVEN Pei's Theorem 6.1(a) at theta = 0 (assumes (I1)-(I3), OpenAI's unrefereed (3.54), (3.58)) | Lemma CR: given the clusters S_- of the minus pins, P(x <-> plus pins) <= A_* exp(-(dist_inf(x, S_- and pins) - 2)/Xi). Corollary CR2. |
| PROVED GIVEN Pei's Theorem 6.1(b) at theta = 0 | Lemma FREE: connections between unpinned sites are bounded by the charged two-point bound plus two opposite-sign pin terms. |
| PROVED GIVEN Pei's Theorem 6.1(a), (b) at theta = 0 | Theorem B1: PIN-2 (a bound on the two-colour event of the pin clusters near a deep site) gives the middle-annulus crossing bound for all pins, and with row 1096's Lemma MK (correction C2) and Theorem T2 the cluster decay in a field on finite subgraphs. Tori: ARGUED, as in row 1096 (C4). |
| PROVED GIVEN the same and row 1096's route 1 identity | Lemma LS: the crossing bound holds when each layer is one-signed. |
| PROVED GIVEN OpenAI's Section 3.10 display for observables with zero common-left average | Lemma DA: the crossing probability equals the mean of one rotation-invariant function up to C N^2 e^{-cN/(4s)}. |
| PROVED | Lemma W: the wall-monotonicity step fails on a one-site example, for every b > 0 and small r. Scope: one lemma; not PIN-U, not PIN-2. |
| PROVED | Lemma J, Lemma BF, Corollary BF: in the four-coordinate bond representation the outside of a region acts through block fields a_j; the conditional law is a mixture of sign-pinned laws with weights prod e^{s_j a_j} Z(s). |
| PROVED GIVEN UNS(N, p) | Theorem B2: P^H(k annuli crossed) <= q^k + max P^H(G^c)/(1 - q). It does not give cluster decay: the term P^H(G^c) is not bounded. |
| ARGUED GIVEN Ding, Huang and Yang's Theorem 5.2 and their "verbatim" claim for N > 3 | UNS (translation of representations not written; their proofs not read). |
| PROVED | Lemma EV-split: Cov(F_X, G_X) is the sum of an O(3)-in-field piece, an Ising bond piece and an amplitude piece. |
| PROVED GIVEN OpenAI's Theorem 3.1, Pei's Theorem 6.1(b), (c) at theta = 0, row 1096's Proposition SS | Lemma EV0: EV at zero field, no pins, both observables local, with OpenAI's polynomial prefactor (on tori with Pei's capped distance). |
| PROVED | Proposition SW: |Cov_H(F, G)| <= (pi/2) osc(G) sum_w Lip_w(F) P(w joined to B by swap bonds of two replicas), every field, all pins. |
| FAILS (guide run only; no proof) | The replacement "swap-cluster connectivity decays" at beta = 2.3 and 2.5, zero field, L = 24, 48: the largest swap cluster holds 95 to 98 percent of the torus. |
| ARGUED | The induction on n stops at its first step (the O(3) kernel in a field is not in the sources read; the O(2) level is expected false at these strengths); the judgment that (B) is the harder target; the reading of Lemma DA. |
| OPEN | PIN-2; PIN-U for pins whose signs change along a layer; control of the block fields (long clusters in a field), hence cluster decay in a small field of varying direction; EV (non-local F, constant with C1, fields); hence FST-F1 for the sheet at beta in [2.3, 2.6]. No counterexample to PIN-U, PIN-2 or EV for the O(4) sheet was found. |

#### 7.2 Answers to the brief

- (A). EV is not proved and no replacement that gives FST-F1 is proved. Proposition SW is a replacement without an even part; the guide run says its hypothesis fails at the window couplings. Exact failing steps: the amplitude covariance has no lower-model form (model 5.4 violates this piece); the field transfer needs a zero-field bound uniform over pins.
- (B). PIN-U is not proved. Replacements proved to suffice: PIN-2 (weaker in form: a two-colour event only). In a field, UNS suffices only together with a bound on the block fields. Tested ideas: the sum is bounded by the difference for the re-signed pins only when each layer is one-signed (Lemma LS); a symmetry gives Lemma CR and Lemma DA, not the sum; the sign-flip coupling on the complementary parts fails at the wall step (Lemma W); Ding, Huang and Yang's uniform boundary class enters as UNS and stops at the block fields, which in the limit are sign pins (Remark of step 5).

#### 7.3 Limits

- Nobody has checked this file. Nothing was formalized in Lean. Every proof is a hand argument.
- Pei's, OpenAI's and Ding, Huang and Yang's papers are unrefereed. Pei's Theorem 6.1 assumes (I1)-(I3). I did not re-derive them. I used Theorem 6.1 for finite graphs with arbitrary pin sets as its statement allows; I did not recheck Pei's reduction of general systems to pinned squares. Lemma DA uses OpenAI's display on the same class; the same caveat applies.
- Rows 1096 and 1097 are same-provider work; row 1098 (cross-provider) was absent. What I take from row 1096: Lemma B, Lemma MK with C2, Lemma PIN+, Theorem T2, Proposition SS, route 1 of 5.3.
- Constants were not optimised. Sup-norm distances throughout step 4. Theorem B1 is stated for N >= 8.
- The guide run is one serial pure-Python job (about two minutes), 12 measurements per line, no error analysis, zero field only. It guides; it proves nothing. Frohlich and Spencer's theorem is cited from memory and not rebuilt.
- Files changed: this file only. Scratch: `/tmp/pinuev-pei.RYIkOC`, `/tmp/pinuev-dhy.rDOJGb`, and the session scratch folder `pinuev-num`. No commit, no push.

#### 7.4 Credits

Yan Ru Pei for Theorem 6.1 (pinned decay of odd observables), the bond coupling and the remark on which observables transfer. OpenAI's authors for the O(4) mixing theorem, the Section 3.10 decay of observables with zero common-left average, the coarse orientations and Section 3.11. Jian Ding, Fenglin Huang and Peng Yang for the annulus theorem uniform over local-time boundary conditions, the domain Markov decoupling without pinning monotonicity, and the relation between spin and local-time boundary conditions. Titus Lupu for the isomorphism behind it. Massimo Campbell and Lincoln Chayes, Ulli Wolff, Robert Edwards and Alan Sokal for the sign-cluster and embedded-cluster representations. Oliver Redner, Jonathan Machta and Lincoln Chayes for two-replica cluster moves, the idea behind Proposition SW. Jacob van den Berg and Christian Maes for disagreement percolation. Cees Fortuin, Pieter Kasteleyn and Jean Ginibre; Robert Griffiths; Jurg Frohlich and Thomas Spencer for the results named. Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, and Tadeusz Balaban, for the account and the ultraviolet construction that the face route serves; neither is an input here. Row 1096 (Claude Fable 5.2 medium) for PIN-U, EV, Lemma MK, Theorem T2, Proposition SS, model 5.4 and route 1; row 1097 (Claude Opus 5.5 max) for the check and corrections C1 to C6; rows 1092 and 1095 (gpt-6-luna high) for the readings.

### Step 8 result

RESULT: PIN-U and EV for the O(4) sheet at beta in [2.3, 2.6] are NOT proved and stay OPEN; no counterexample for the sheet was found; unchecked, not formalized, no mass gap claimed. (B), PROVED GIVEN Pei's Theorem 6.1 at theta = 0 (which assumes OpenAI's (I1)-(I3)): Lemma CR (given the clusters of the minus pins, a site is joined to the plus pins with probability at most A_* exp(-(dist to those clusters and the pins - 2)/Xi)), Lemma FREE, and Theorem B1: PIN-U can be replaced by PIN-2, a bound on the two-colour event that plus and minus pin clusters both come near one deep site; PIN-U holds when each layer is one-signed (Lemma LS); PIN-2 is OPEN. PROVED GIVEN OpenAI's Section 3.10: the crossing probability is the mean of one rotation-invariant function up to an exponentially small error (Lemma DA). PROVED: the wall-monotonicity step that would close PIN-U from Lemma CR FAILS as a general lemma (Lemma W, one site, every b > 0). (B) in a field, PROVED: the outside of an annulus acts through block fields (Lemma BF); an unsigned crossing bound UNS (ARGUED from Ding, Huang and Yang's Theorem 5.2) replaces PIN-U only if the block fields are controlled (Theorem B2), and that control, a bound on long clusters in a field, is OPEN. (A), PROVED: EV splits into an O(3)-in-field piece, an Ising bond piece and an amplitude piece that has no lower-model form (Lemma EV-split; the induction on n stops at its first step, ARGUED); EV at zero field for local pairs follows from OpenAI's Theorem 3.1 (Lemma EV0); Proposition SW bounds the whole covariance in every field and under all pins by the swap-cluster connectivity of two replicas, with no even part, but a guide run (not a proof) shows swap clusters filling the torus at beta = 2.3 and 2.5, so that replacement FAILS there. Row 1097's corrections C1 to C6 are applied; row 1098 was absent.
