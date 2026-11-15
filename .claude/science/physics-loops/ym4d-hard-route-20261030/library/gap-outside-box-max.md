lead: anthropic/claude-fable-5-2/max mac-mini-worker
lease_until: 2026-11-16T03:55Z

# gap-outside-box-max: change the frame, not the inequality (row 1004)

Provenance: Claude Fable 5.2, max effort, Mac mini worker 2, fresh session, pinned at commit 95fecd964. Not an audit. No status is granted by this note. Research-stage working state.

## Plan (at most eight steps; one step per response; each result is appended before the next step)

1. **Read the frame.** `parts/gap.md` (lead rules, registry, test table, price), row 1002 (`library/prior/gap-kflow-read-opus.md`), row 1003's scope, and the exercise skill at main commit 8b11ae2bb9. Record here: the crux as it stands, the consumers ((W), (CAS), the gap), the four-test spec check, the test table.
2. **Assumption lens.** List what the present frame fixes without saying so (space, boundary, state space, coupling, group, time). Each entry is one candidate frame change.
3. **Generate.** Seeds (a)-(e) of the row plus my own. Each idea stated as mathematics, with the exact statement to prove and its consumer.
4. **Test.** Four-test spec check and the test table (Lemma PT, Theorem D2, Lemma SHEET, compact U(1), the 2D O(N) filter) on every idea. Same crux renamed = FAIL, named as such. Grep the lane before any novelty claim.
5. **Rank** survivors by (what it would change) / (cost to find out).
6. **Top survivor:** first lemma, proof by hand or counterexample.
7. **Second survivor:** first lemma, proof by hand or counterexample.
8. **Close.** Marks (PROVED, ARGUED, OPEN, FAILS), work items as complete briefs, RESULT line.

## Log

- 2026-11-15T15:55Z: file created. Steps follow below, in order.

## Header (exercise skill, Output rules)

- Written by: Anthropic, Claude Fable 5.2, max effort, Mac mini worker 2, one fresh session. Commit 95fecd964. Date 2026-11-15.
- **Nothing in this file is checked by another model.**
- Skill used: `exercise` at main commit 8b11ae2bb9 (fetched to a scratch folder with `proof-search-governance.md`, `assumption-import-audit.md`, `RULES.md`, `procedures/research.md`, `procedures/check.md`, same commit). The framework refresher list is replaced by `GOAL.md` and `FINISH.md` of this target, as the skill allows for a standalone proof target.
- Binding limits of the brief: no subagents, no commit, no other file edited, no computer-assisted step in any proof, scope = the frame (row 1003 has the inputs inside the frame, row 1005 the literature on frame changes).
- What this run did not cover (kept true as the run goes): see the end of the file.

## Status block (kept current)

| Step | State | Main result |
|---|---|---|
| 1 Read the frame | done | Section 1 |
| 2 Assumption lens | done | Section 2: ten assumptions, ranked; A8 (the engine exists in one frame only) and A7 (growth, not a number) carry the frame |
| 3 Generate | done | Section 3: Lemma FR, Proposition CB, Observation SCH; eighteen ideas I1-I18 as statements with consumers |
| 4 Test, grep | not started | |
| 5 Rank | not started | |
| 6 Top survivor | not started | |
| 7 Second survivor | not started | |
| 8 Close | not started | |

## 1. The frame as it stands (step 1)

Read in full: `GOAL.md`; `parts/gap.md`; FINISH rows 1002 to 1005 and the sections Where it stands, How we work, Working efficiently, Rules; `library/prior/gap-kflow-read-opus.md` (row 1002); the skill and its governance file. Read in part: `library/gap-crux-exercise3-max.md` L100-160 and L686-760 (the wall, Lemma PT, Proposition KF); `library/gap-crux-restate.md` L1-80 (objects, (TM), (TM-c), candidates C1 to C5); `library/gap-phys-seed.md` L286-335 (Theorems ZD, ZD-c, Corollary Z4); `library/gap-mid-max.md` L58-70 ((CAS)); `library/gap-tiltproof-max.md` L236-262 (Theorem D2).

### 1.1 The crux (quoted, not rewritten)

Objects (`gap-crux-restate.md` Section 1): Wilson SU(2) on a periodic torus with sides n_mu >= 3; Z(n), F = log Z, f = inf F(n)/|n|; for a 3-box B the transfer operator T with eigenvalues lambda_0 > lambda_1 >= ...; m(B) = log(lambda_0/lambda_1); S(k; B) = sum over i >= 1 of (lambda_i/lambda_0)^k; D(a) = F(a^4) - f a^4 >= 0.

The wall (row 998 L129-131): "(W) There is a physical size L in P with z^-(L) > 256 D_0 + 30, where D_0 bounds D^+ on the sizes from L/4 on." Here z^-(L) = liminf_j (L/a_j) m_j((L/a_j)^3) and D^+(L) = limsup_j D_j(L/a_j) along the account's trajectory.

Price on record (`parts/gap.md`): (W) iff (BDD-Delta) and (Z-UNB) (Theorem ZD-c). (W) follows from (CAS): D(2a) <= theta D(a) with theta < 1 on a bounded range, with an extensive base. In words: one selective inequality at every scale between first passage and the seed size. Selective means false for a product with a massless factor (Lemma PT).

Consumers: (W) -> (PHYS-SEED) -> uniform gap on all larger dyadic cubes (Theorem S) -> the mass gap of the limit theory. The mass gap is a later target; T0 itself does not ask for it (`GOAL.md`).

### 1.2 What the present frame fixes

- F1 space: a hypercubic lattice, all four directions periodic, one lattice spacing in all directions.
- F2 shape: the symmetric torus a^4 for D; the box (2N)^3 at time N for the seed.
- F3 boundary: none. Twists enter only as the centre flips C_nu of (TM-c).
- F4 state space: gauge-invariant L^2 of the link field on one periodic 3-slice, all flux sectors together.
- F5 coupling: one real coupling beta for the whole torus; the trajectory (a_j, beta_j) moves it with the cutoff only.
- F6 theory: gauge group SU(2), Wilson weight, no matter field.
- F7 time: the Euclidean lattice time of the transfer operator. No other flow.
- F8 engine: Theorem S, which uses (TM), Lemma A and the invariance of Z under exchange of two axes; it holds for every group of the class.

### 1.3 The tests an idea must face

Test table of `parts/gap.md` (copied there from row 998 6c). For a tool for T_W the theorem-grade tests are: compact U(1) at weak coupling, the free photon, the product with a massless factor (Lemma PT, Corollary PT1), Theorem D2 (no supremum over tilts), Lemma SHEET (no uniformity over coupling fields). Row 1002 adds the 2D O(N) filter (a plausibility test, not a theorem).

**Reading of "the four-test spec check" (a reading; the phrase is defined in no file of the lane, searched in FINISH, library/, parts/, docs/ai_methodology).** I take it as point 2 under the test table: a tool for T_W must use (S1) the non-abelian structure (else compact U(1) binds), (S2) a rate (else the free photon binds), (S3) the whole state space (else a product with a massless factor binds), (S4) typical fields (else D2 or SHEET binds). To these I add (S5) the 2D O(N) filter: the step names its four-dimensional or gauge-specific input. And the row's own rule (S0): a frame change that returns the same crux under another name is a FAIL.

### 1.4 Open now / closed until the compare step

Open now: the statements quoted above. Closed until step 4 (the compare step): the attack files of the lane (the four exercises, the direction and brainstorm notes, `gap-ac-lat.md`, `gap-ds-gauge.md`, `gap-zf-box-*.md`, the literature digests under `prior/`). Step 3 is written before they are opened; step 4 opens them by grep and nothing is called new before that.

## 2. Assumption lens: what the frame assumes (step 2)

Written with the attack files closed. "Needed by" says who needs the assumption: the target (the mass gap of the limit theory), or the method (the engine, Theorem S). Marks: all rows are readings of the definitions in Section 1 unless a mark is given.

| ID | Assumption of the present frame | Needed by | If dropped or changed | Easier? |
|---|---|---|---|---|
| A1 | All four directions are periodic and the torus is rectangular. | method (Lemma A and the exchange of axes need it) | Other flat lattices: twisted, shifted (sheared), reflected, free or fixed walls. | Section 3, I1, I5, I6, I9 |
| A2 | The seed is asked of the whole slice space, all flux sectors together. | method. The target needs the flux-free sector only (in infinite volume the vacuum sector has no flux sector). | A frame with no flux sector (free time boundary, S^3, a centre-breaking field). | I1, I7, I10 |
| A3 | One coupling for the whole torus. | method | A coupling profile, an exterior at strong coupling, a complex coupling. | I3, I17 |
| A4 | The size parameter is the side of a symmetric box. | method | A thin direction with its own size; a curvature radius; a radial variable. | I2, I5-I8 |
| A5 | The state space holds the gauge field only. | target (pure Yang-Mills) | A larger theory with a parameter that returns the pure theory at one end. | I10-I13 |
| A6 | The only time is the lattice time of T. | method | Continuous time (Hamiltonian), a stochastic time, a flow time. | I14-I16 |
| A7 | The massless alternative is told from the gapped one by a number at one size (z against 256 D_0 + 30). | method | In every frame I know, the two are told apart only by growth: size times gap is bounded in a massless theory and unbounded in a gapped one. | Section 3.0 |
| A8 | The engine exists only in this frame. | belief of this run | If another frame had an engine with a lower threshold, the seed could sit where a small parameter exists. | Section 3.0, I5, I6 |
| A9 | The gap is carried from finite boxes to the limit, not the other way. | method | A gap proved in infinite volume, or in another frame, needs its own carry-back. | Section 3.0 (CB) |
| A10 | The proof may not use a run. | owner rule (questioned on paper only) | Not used. | no |

Ranking by how much the problem changes if the assumption is dropped: A8, A7, A5, A2, A4. One line each.

- A8: if a second frame had an engine, the lane would move the seed to the frame where the seed is cheapest. Section 3.0 says why I expect none; I6 gives a proved reason for twisted frames.
- A7: if some frame told massless from gapped by a number that asymptotic freedom fixes at small size, the band would vanish. Section 3.0 argues that no frame of kinds (a) and (b) does.
- A5: a larger theory helps only if it proves seeds of bounded size up to the pure end (Proposition CB below).
- A2: dropping the flux sectors weakens the wall to the even-sector statement; the lane has that as route RE.
- A4: a thin direction gives semiclassical control at small size and nothing in the band.

## 3. Frame changes, stated as mathematics (step 3)

Written before the lane's attack files were opened. Each idea has: the statement that would be proved, the consumer, and the first reading of the tests. "On file?" is filled in step 4.

### 3.0 Three general statements that the list uses

**Lemma FR (frames of the flat lattice; PROVED here, elementary).** Let B be a periodic 3-box and T_B its transfer operator in direction 4 ((TM)). Let G be a unitary on the slice space that commutes with T_B: a centre flip C_nu, a lattice translation tau_s, a reflection, or a product of these. Let u, v be vectors of the slice space. Then:
- (i) Z of the torus B x n closed with G (a centre twist in a time plane, a sheared torus, a reflected gluing) is Tr(T_B^n G) = sum over i of g_i lambda_i^n, with g_i the eigenvalues of G on a joint eigenbasis, |g_i| = 1.
- (ii) Z of the slab B x [0, n] with boundary vectors u, v is <u, T_B^n v> = sum over i of <u, psi_i><psi_i, v> lambda_i^n. Free time boundaries are u = v = 1 (the constant function), up to the convention for the boundary plaquettes.
- (iii) So every decay rate in n of every such quantity is one of log(lambda_0/lambda_i), and is at least m(B) on the terms i >= 1. A gap statement in a frame of kind (i) or (ii) is a statement about T_B on a sector (an eigenspace of G, or the cyclic subspace of u, v). The periodic seed implies each of them at the same box. None of them implies the periodic seed without the sectors it does not see.
- (iv) A change of a space-like boundary (a wall in direction 1) is, by exchange of the axes 1 and 4, a change of the time boundary of another box. So it is again of kind (ii), for the operator T of the box (n_2, n_3, n_4).

Proof. (i) and (ii) are the spectral theorem for the positive trace-class operator T_B and the definition of the transfer operator: a closed lattice of n time steps with the gluing map G is the trace of T_B^n G, and an open one is the matrix element. (iii) follows. (iv) is the invariance of the weight under the exchange of two axes. QED

Reading: twisted, sheared, reflected and walled flat lattices are not new frames. They are the same operators T_B, read on sectors.

**Proposition CB (carry-back is uniformity; PROVED here, elementary).** Let M_t, t in [0, 1], be models of the engine's class on the same lattices, with Z_t(n) continuous in t for every torus n. Then for each N the set {t : S_t(N; (2N)^3) < 1/5041} is open. So M_0 has a seed if and only if there are one N and a sequence t_k -> 0 with a seed of size N at every t_k.
Proof. S_t(N; B) = Z_t(N, B)/lambda_0,t(B)^N - 1, and lambda_0,t(B) = lim over k of Z_t(k, B)^(1/k) is the top eigenvalue of T_t. Z_t(k, B) = Tr T_t^k for k = 1, 2 is continuous in t, and Tr T^2 controls the Hilbert-Schmidt norm, so T_t is continuous in Hilbert-Schmidt norm; the simple top eigenvalue of a norm-continuous family of compact self-adjoint operators is continuous. So S_t is continuous in t and the set is open. The second sentence is the first one read at t = 0. QED (The step "Z_t(1), Z_t(2) continuous gives T_t continuous in Hilbert-Schmidt norm" needs the kernels: for the families used below the kernel of T_t is jointly continuous in t and the fields on a compact space, which gives it. Mark: PROVED given that.)

Reading: a larger theory with a parameter (a Higgs coupling, a source, a deformation) helps only if it proves seeds of **bounded size** all the way to the pure end. A gap at every t > 0 whose seed size grows without bound as t -> 0 gives nothing.

**Observation SCH (frames are schemes; ARGUED, a reading with examples, not a theorem).** In each frame X with a size parameter L there is a pure number u_X(L): L times the gap of the periodic cube (the lane's z); the same for a twisted box; R times the gap on a 3-sphere of radius R; l^2 times the string tension of base-plane loops on Z^2 x (a 2-torus of side l); the ratio w = Z_twisted/Z_periodic of the symmetric torus; the Casimir free energy D. In a scale-invariant theory each u_X is a constant in L. In a gapped, confining theory each tends to its extreme value (z to infinity, w to 1, D to 0). At small L each is a function of the running coupling g(L): z ~ g^(2/3) (Luescher; recalled), l^2 sigma = (3/8) g^2 (two-dimensional Yang-Mills from the zero modes; recalled), w ~ g^4 (four flat directions of the periodic torus against none of the twisted one; my count), D ~ C log(1/g) (the lane's GUIDE). So a frame is a renormalization scheme, and u_X(2L) against u_X(L) is its step-scaling function. Whether the flow stops at an interior value does not depend on the scheme. **A change of frame of kinds (a) and (b) therefore changes where the threshold sits and whether an engine exists; it does not remove the statement "the flow does not stop in the band".** The periodic frame is the one frame where an engine is known.

### 3.1 (a) Literally outside the box

- **I1. Time boundaries: free, fixed, twisted, sheared, reflected.** Statement: a bound on the weighted thermal sum S_w(t; B) = sum over i >= 1 of (c_i/c_0)(lambda_i/lambda_0)^t, c_i = |<1, psi_i>|^2, of the slab with free ends. It sees centre-even states only (the vector 1 is invariant under every C_nu). Consumer: the even-sector statement (route RE), not (W). By Lemma FR it is the same operator. First reading: S0 (same crux on a sector).
- **I2. The exterior of a block; the radial frame.** Statement: let K_r be the conditional-expectation operator from functions of the field outside the cube of side 2r to functions of the field inside the cube of side r, in the infinite-volume state. Its second singular value rho(r) tends to 0 as r grows. In a scale-invariant theory rho(r) is a constant, 2^(-Delta) with Delta the lowest scaling dimension (free scalar: 1/2; Maxwell field strength: 1/4; computed for Gaussian fields from the mean-value property). In a gapped theory rho(r) <= C r^3 exp(-m r). The Dirichlet-to-Neumann operator of the exterior is the Gaussian case of K_r. The radial picture identifies this with the 3-sphere frame I7 (the exterior of a ball is a half-cylinder over S^3 in the variable log r). Consumer: none on file; there is no reflection through a sphere on the lattice, so no engine. First reading: S0, and it loses A8.
- **I3. A coupling profile: weak inside, strong outside.** Statement: for the cube C_n at coupling beta in a sea at coupling beta_out <= beta_sc, bounds uniform as beta_out rises to beta. At beta_out = 0 this is the free boundary. With the weight exp(beta (1/2) tr U_p) and positivity of the character coefficients, F_free is superadditive, so F_free(n)/n^4 <= f~ <= F_per(n)/n^4: both sides are finite-volume numbers. The distance between them is a surface term of order n^3, against the Casimir term of order 1 that the seed needs. Consumer: none. First reading: fails for size (the surface term hides the quantity), not for a test.
- **I4. The logarithm that a box with a boundary carries.** Statement: for a cube with free walls, F(n) = f n^4 + s_3 n^3 + s_2 n^2 + s_1 n + s_0(n); a five-fold doubling difference isolates s_0(2n) - s_0(n), which tends to 0 in a gapped theory and to -kappa log 2 in a scale-invariant one (kappa from the trace anomaly and the corners). Consumer: none; it is a finite-size form of the counting monotones of row 1002 (H1 to H3). First reading: blind as a monotone, selective only as a limit; S0.

### 3.2 (b) Other geometries

- **I5. R^3 x a small circle, centre-stabilised or twisted, and continuity in the circle size.** Statement in two parts. (I5-s) For circle size l <= l_0 (in physical units) the theory with a centre-stabilising term has a gap m(l) > 0, uniformly in the cutoff; expected size m(l) l ~ exp(-2 pi^2/g^2(l)) (Unsal and Yaffe; recalled). (I5-c) l m(l) is unbounded as l grows. Consumer: a mass-gapped limit theory directly, if the limit l -> infinity is identified with the T0 theory. First reading: (I5-s) is a small-parameter problem of the size of the existence proof plus a three-dimensional Coulomb-gas theorem (Goepfert and Mack for the pure U(1) case); it is not on the path. (I5-c) is the crux in the scheme u = l m(l): S0. "No phase transition in l" is not enough: a free field with an antiperiodic direction has a gap pi/l at every l, no transition, and no gap in the limit.
- **I6. R^2 x a small 2-torus with one unit of 't Hooft flux.** Statement: (I6-s) at small l the twisted fibre has a unique classical vacuum and a perturbative gap of order pi/l; the two-dimensional seed (doubling the two long sides only) holds; (I6-c) the same as l grows. Consumer: as I5. First reading: S0 for (I6-c). Structural facts (PROVED, elementary): a Z_2 twist in a plane is lost when a side of that plane is doubled (the flux doubles); and no non-zero twist tensor on the 4-torus is both invariant under all exchanges of axes and free of a twist in a time plane, so the engine, which needs a positive trace in each of the four directions and the exchange of axes, has no twisted form (Lemma TW in step 4).
- **I7. The 3-sphere of radius R.** Statement: R m(R) is unbounded as R grows. At small R: no flat directions, a unique flat connection, R m(R) = 4 - 2 b_0 g^2(R) + ... (the lowest singlet state is two gluons; the anomalous dimension of tr F^2; recalled, GUIDE). A Maxwell field has R m = 2. Consumer: none on the lattice (no hypercubic lattice, no doubling of spheres). First reading: S0; loses A8; note that u first falls.
- **I8. Hyperbolic space of radius rho.** Statement: rho m(rho) unbounded. Even a Maxwell field decays exponentially in geodesic distance there (hyperbolic 4-space is conformal to a ball), so the gap alone is not selective at fixed rho; only the growth is. Physics literature expects a transition in rho Lambda between a deconfined small-radius regime and confinement (Callan and Wilczek; Aharony, Berkooz, Tong and Yankielowicz; recalled, BELIEF). So continuity in the radius is expected to fail. First reading: fails by its own physics; S0.
- **I9. General flat tori Z^4/Gamma (shear; the modular group).** Statement: Z depends on the sublattice Gamma only, not on its basis; this gives identities beyond the exchange of axes, for example Tr(T_(n1,n2,n3)^n tau_(s e_1)) = Tr(T_(n2,n3,n n1/d)^d tau_(alpha n e_4)) with d = gcd(s, n1) and alpha s = d mod n1. Sums over shifts project on momentum. Consumer: a possible engine with momentum-resolved thermal sums (a smaller seed box), not (W). First reading: blind (every model of the class satisfies the identities); S0 for the wall.

### 3.3 (c) A larger theory around SU(2)

- **I10. A fundamental Higgs field of fixed length, hopping parameter kappa.** Statement: the gauge-Higgs model has a seed at (beta, kappa) for kappa >= kappa_0(beta) (the Higgs regime; Osterwalder and Seiler, Fradkin and Shenker; recalled), and the seed size stays bounded as kappa falls to 0 at fixed beta. Consumer: (W) by Proposition CB. First reading: the second half is the crux at the pure end (CB); the analytic connection of Fradkin and Shenker runs through strong gauge coupling; at weak gauge coupling the path in kappa meets the Higgs transition or its crossover. S0. One real change: the centre is broken, so there are no flux sectors.
- **I11. An adjoint Higgs field of fixed length (the Georgi-Glashow family).** Statement (Lemma GG, to prove): for a class-function plaquette weight w on SU(2), the model with a unit adjoint site field and hopping kappa is, at kappa = infinity, exactly the compact U(1) model with plaquette weight w restricted to the maximal torus, at the same coupling. So the lane's main test model is the end point of a family of local, reflection-positive SU(2) gauge models with centre symmetry. Consumer: the test table, not the wall. First reading: a test device; it says a tool must use that the state space has no site field.
- **I12. Soft-broken supersymmetry; heavy adjoint fermions.** Statement: a gap for the theory with a gluino of mass M, uniform as M grows. Consumer: (W) by CB. First reading: no rigorous end point; the fermion weight is non-local; matter can create massless phases (the conformal window row of the test table). S0 plus no supplier.
- **I13. SU(N) and continuation in N; continuation in the dimension.** Statement: a gap at N = infinity with corrections controlled down to N = 2; or an inequality that bounds the four-dimensional theory by a lower-dimensional one. For the dimension: Durhuus and Froehlich bound the Wilson loop of the nu-dimensional gauge theory by two-point functions of (nu - 1)-dimensional chiral models in external gauge fields (recalled). For nu = 4 the hypothesis is a mass gap of a three-dimensional chiral model at weak coupling, which is false for zero external field. On a thin fibre (base Z^2) the chiral model is quasi-one-dimensional and has a gap; this gives an area law at every fibre size with a rate that vanishes as the fibre grows. Consumer: none for (W). First reading: fails S2 (no rate) or its hypothesis is false.

### 3.4 (d) Another time or flow

- **I14. The Hamiltonian with Gauss law; gap stability along a path.** Statement: the Kogut-Susskind Hamiltonian H(g) has a gap uniform in the volume for all g on a path from g = infinity. Stability theorems (Bravyi, Hastings and Michalakis; Michalakis and Zwolak; recalled) give a neighbourhood of the frustration-free point g = infinity. Along the path the gap is the hypothesis of quasi-adiabatic continuation, not its conclusion. A frustration-free form at every coupling exists for the heat-bath generator of the Euclidean measure (a sum of commuting-or-neighbouring projections 1 - E_l); its gap is a Poincare inequality, route RF. First reading: S0 (strong coupling, or RF).
- **I15. Gradient flow.** Statement: t^2 <E(t)> is unbounded as the flow time t grows. Selective in kind (constant for a Maxwell field). No monotonicity theorem; Hamilton's monotonicity formula for the Yang-Mills heat flow reduces, after the average over a translation-invariant state, to "the action decreases". Consumer: none (growth of this coupling does not give a gap). First reading: no consumer.
- **I16. Stochastic quantisation.** Statement: a spectral gap of the Langevin generator, uniform in the volume. The group S^3 has Ricci curvature bounded below by a constant that does not depend on the number of links, and U(1) has none; so the Bakry-Emery criterion is selective in kind. It holds only while beta times the Hessian of the action stays below the curvature: strong coupling. First reading: S0 (route RF).

### 3.5 (e) The complex plane

- **I17. A Lee-Yang property in a centre-breaking field.** Precedent (recalled): for ferromagnets the Lee-Yang theorem gives, at every temperature, analyticity and a mass gap in a non-zero field (Lebowitz and Penrose; Froehlich and Rodriguez). It is an exact property with no small parameter. Statement: (LY-link) Z(beta, kappa), with kappa the hopping parameter of a fundamental Higgs field in unitary gauge (a field on links), has zeros only at imaginary kappa; (LY-loop) on Z^3 x Z_Nt, Z(h) = <exp(h sum over x of tr P_x)> has zeros only at imaginary h, P the Polyakov loop. Consumer: a gap at every coupling for kappa or h not 0, then (W) only through Proposition CB, that is, with a seed size bounded as the field goes to 0. First reading: it is not selective (it would hold for U(1) too) and it does not reach zero field; but it is a statement of another type. Kept for a real attempt because it can be decided by hand at the first step.
- **I18. The complex coupling beta.** Statement: Z has no zero in a complex neighbourhood of the real axis, uniformly in the box. The lane's candidate C4 (`gap-crux-restate.md` Section 2). First reading: on file, stronger than the target.
