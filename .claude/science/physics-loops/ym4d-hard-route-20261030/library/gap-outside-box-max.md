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
| 4 Test, grep | done | Section 4: all five seed families are on file with the same verdict (rows 669, 697, 842, 858, 876 and the constraint table); new to the lane: the exterior/sphere frame, Lemmas TW, LYP, GG |
| 5 Rank | done | Section 5: no idea survives as a route; ranked items are four statements decidable by hand |
| 6 Attempts, part 1 | done | Section 6: Lemma LYP (the crux (LY) of B9 is false for one plaquette, every beta > 0), Lemma GG (adjoint Higgs family ends at compact U(1) exactly), Lemma TW (engine only in clean directions); all PROVED by hand, unchecked |
| 7 Attempts, part 2 | done | Section 7 and new file `library/gap-transfer-twisted.md`: (TM-tw) written as one lemma with proof (Theorem TW-T), PROVED given `gap-transfer.md` (1)-(4); guard run for Lemma LYP passed (6.4) |
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

**Observation SCH (frames are schemes; ARGUED, a reading with examples, not a theorem).** In each frame X with a size parameter L there is a pure number u_X(L): L times the gap of the periodic cube (the lane's z); the same for a twisted box; R times the gap on a 3-sphere of radius R; l^2 times the string tension of base-plane loops on Z^2 x (a 2-torus of side l); the ratio w = Z_twisted/Z_periodic of the symmetric torus; the Casimir free energy D. In a scale-invariant theory each u_X is a constant in L. In a gapped, confining theory each tends to its extreme value (z to infinity, w to 1, D to 0). At small L each is a function of the running coupling g(L): z ~ g^(2/3) (Luescher; recalled), l^2 sigma = (3/8) g^2 (two-dimensional Yang-Mills from the zero modes; recalled), w ~ g^3 up to a logarithm (my count, corrected in step 7: at a generic flat connection the periodic torus has four moduli and a one-dimensional stabilizer, the twisted one has neither, so the periodic integral has three fewer Gaussian directions and w is of order beta^(-3/2); this agrees with the lane's count 9 n^4 - 3 behind "765 log(1/g)", and it gives -log w = (3/2) log beta, where idea 8 of row 858 writes "about 3 log beta"; neither count is checked), D ~ C log(1/g) (the lane's GUIDE). So a frame is a renormalization scheme, and u_X(2L) against u_X(L) is its step-scaling function. Whether the flow stops at an interior value does not depend on the scheme. **A change of frame of kinds (a) and (b) therefore changes where the threshold sits and whether an engine exists; it does not remove the statement "the flow does not stop in the band".** The periodic frame is the one frame where an engine is known.

### 3.1 (a) Literally outside the box

- **I1. Time boundaries: free, fixed, twisted, sheared, reflected.** Statement: a bound on the weighted thermal sum S_w(t; B) = sum over i >= 1 of (c_i/c_0)(lambda_i/lambda_0)^t, c_i = |<1, psi_i>|^2, of the slab with free ends. It sees centre-even states only (the vector 1 is invariant under every C_nu). Consumer: the even-sector statement (route RE), not (W). By Lemma FR it is the same operator. First reading: S0 (same crux on a sector).
- **I2. The exterior of a block; the radial frame.** Statement: let K_r be the conditional-expectation operator from functions of the field outside the cube of side 2r to functions of the field inside the cube of side r, in the infinite-volume state. Its second singular value rho(r) tends to 0 as r grows. In a scale-invariant theory rho(r) is a constant, 2^(-Delta) with Delta the lowest scaling dimension (free scalar: 1/2; Maxwell field strength: 1/4; computed for Gaussian fields from the mean-value property). In a gapped theory rho(r) <= C r^3 exp(-m r). The Dirichlet-to-Neumann operator of the exterior is the Gaussian case of K_r. The radial picture identifies this with the 3-sphere frame I7 (the exterior of a ball is a half-cylinder over S^3 in the variable log r). Consumer: none on file; there is no reflection through a sphere on the lattice, so no engine. First reading: S0, and it loses A8.
- **I3. A coupling profile: weak inside, strong outside.** Statement: for the cube C_n at coupling beta in a sea at coupling beta_out <= beta_sc, bounds uniform as beta_out rises to beta. At beta_out = 0 this is the free boundary. With the weight exp(beta (1/2) tr U_p) and positivity of the character coefficients, F_free is superadditive, so F_free(n)/n^4 <= f~ <= F_per(n)/n^4: both sides are finite-volume numbers. The distance between them is a surface term of order n^3, against the Casimir term of order 1 that the seed needs. Consumer: none. First reading: fails for size (the surface term hides the quantity), not for a test.
- **I4. The logarithm that a box with a boundary carries.** Statement: for a cube with free walls, F(n) = f n^4 + s_3 n^3 + s_2 n^2 + s_1 n + s_0(n); a five-fold doubling difference isolates s_0(2n) - s_0(n), which tends to 0 in a gapped theory and to -kappa log 2 in a scale-invariant one (kappa from the trace anomaly and the corners). Consumer: none; it is a finite-size form of the counting monotones of row 1002 (H1 to H3). First reading: blind as a monotone, selective only as a limit; S0.

### 3.2 (b) Other geometries

- **I5. R^3 x a small circle, centre-stabilised or twisted, and continuity in the circle size.** Statement in two parts. (I5-s) For circle size l <= l_0 (in physical units) the theory with a centre-stabilising term has a gap m(l) > 0, uniformly in the cutoff; expected size m(l) l ~ exp(-2 pi^2/g^2(l)) (Unsal and Yaffe; recalled). (I5-c) l m(l) is unbounded as l grows. Consumer: a mass-gapped limit theory directly, if the limit l -> infinity is identified with the T0 theory. First reading: (I5-s) is a small-parameter problem of the size of the existence proof plus a three-dimensional Coulomb-gas theorem (Goepfert and Mack for the pure U(1) case); it is not on the path. (I5-c) is the crux in the scheme u = l m(l): S0. "No phase transition in l" is not enough: a free field with an antiperiodic direction has a gap pi/l at every l, no transition, and no gap in the limit.
- **I6. R^2 x a small 2-torus with one unit of 't Hooft flux.** Statement: (I6-s) at small l the twisted fibre has a unique classical vacuum and a perturbative gap of order pi/l; the two-dimensional seed (doubling the two long sides only) holds; (I6-c) the same as l grows. Consumer: as I5. First reading: S0 for (I6-c). Structural facts (PROVED, elementary): a Z_2 twist in a plane is lost when a side of that plane is doubled (the flux doubles); and no non-zero twist tensor on the 4-torus is both invariant under all exchanges of axes and free of a twist in a time plane, so the engine, which needs a positive trace in each of the four directions and the exchange of axes, has no twisted form (Lemma TW in step 4).
- **I7. The 3-sphere of radius R.** Statement: R m(R) is unbounded as R grows. At small R: no flat directions, a unique flat connection, R m(R) = 4 + O(g^2(R)) (at g = 0 a gluon mode has energy 2/R and the Gauss law on a compact space asks for a singlet, so the lowest state has two gluons; the anomalous dimension of tr F^2 suggests the correction -2 b_0 g^2, but I did not compute the coefficient on the sphere; recalled, GUIDE). A Maxwell field has R m = 2. Consumer: none on the lattice (no hypercubic lattice, no doubling of spheres). First reading: S0; loses A8; if the correction is negative, u first falls.
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

## 4. Test and compare with the lane (step 4)

The attack files were opened here. Search scope for every "new" mark: `grep -rliE` over `library/` and `parts/` (801 files at this pin), by the object and by at least two wordings; FINISH rows by row name; `library/open-core.md` (no entry on the gap, on twists or on any frame). A hit list is in the appendix. Lines were read at the places cited.

**Main finding of the compare step (plain).** The five seed families of the row are already on file, with the same verdict that my fresh pass reached. They came mainly from run 1 (row 669, `gap-skeleton-max.md`, Part 1.B: B8 to B13), the means note (`gap-means-max.md` 2.2, (M6), (M9)), row 842 (S1, the thin twisted torus), the 52 ideas of row 858 (`gap-brainstorm-max.md`, ideas 8, 9, 31 to 42 and G7, G15), row 876 (`gap-brainstorm2-max.md`, idea 24), and the constraint table of `gap-constraints-max.md` (rows 1 to 14; A4, A5). My three general statements are also on file in other words. Credit goes to those rows (Claude Fable 5.2, Claude Opus 5.5 and Codex gpt-6-astra, as their headers say).

### 4.1 The three general statements

| Statement here | Already on file? | Where | Mark |
|---|---|---|---|
| Lemma FR (twisted, sheared, reflected, walled lattices are the same operators on sectors) | yes, in pieces | (TM-c) `gap-crux-restate.md` Section 1; the twist split Z^k = Tr(T_(k_mag)^n C^(e)) <= Z^(k_mag) in `gap-assume-opus.md` L494; sheared tori A4 and the reflected gluing A5 in `gap-constraints-max.md` L185-198, 7.4; wall states, idea 35 of row 858 (`gap-brainstorm-max.md` L320, L408); "only traces cross", `gap-constraints-max.md` row 14 | found again; here it is one statement |
| Proposition CB (carry-back is uniformity) | yes | C19 of `gap-crux-exercise-astra.md` L384: "The removal needs a positive lower rate uniform in the removal parameter ... A phase diagram or continuity at each finite box is insufficient." | found again; here with the one-line proof and the form "seeds of bounded size" |
| Observation SCH (frames are schemes) | partly | "Common finding of 4c and 4d" in `gap-brainstorm-max.md` L661 (the form of the seed moves, its location does not); idea 8 (the twist free energy as a running coupling) and idea 36 (the step-scaling function of Luescher, Weisz and Wolff); row 1002 H16 | found again; the list of frames and the free-limit remark of 4.3 are the additions |

### 4.2 The eighteen ideas

Columns: S0 = same crux renamed; S1 non-abelian; S2 a rate; S3 the whole state space; S4 typical fields; S5 names a four-dimensional or gauge input. "-" = the test does not apply because the idea has no tool (no written implication to (W)); D2 and SHEET (S4) apply to no idea here, because none has a supremum over tilts or over coupling fields.

| # | Idea | On file? Where (credit) | Spec check | Verdict |
|---|---|---|---|---|
| I1 | time walls, boundary states | yes: idea 35 of row 858; free walls FW1 (check 902), rows 898, 907, 910 per `gap-constraints-max.md` rows 11, 14 ("a gap on a cyclic subspace only"; "doubling needs a new input at every scale") | S0 | FAILS (same operator, one sector); found again |
| I2 | exterior of a block, radial frame | **new to the lane** (no hit for radial quantisation, scaling dimension, exterior operator; one unrelated hit for Dirichlet-to-Neumann in `gap-novelty-opus.md` L101; maximal correlation is on file for other pairs of regions, `convex-maximal-correlation.md`) | S0; no engine | FAILS (no reflection through a sphere on the lattice; the doubling of the four sides in Theorem S is already the lattice form of a radial doubling) |
| I3 | coupling profile, strong-coupling exterior | partly: Lemma SHEET (row 996) for coupling fields; idea 4 (tilts), idea 49 (cut the sheet), idea 51 (two-sided subadditivity) of row 858 | - | FAILS for size (a surface term of order n^3 against a number of order 1) |
| I4 | the logarithm of a box with walls | partly: idea 29 of row 858 (trace anomaly, sum rules); row 1002 H1 to H3 (counting monotones are blind) | S0 as a limit; blind as a monotone | FAILS (no engine; blind) |
| I5 | small circle, centre kept, continuity | yes: B10 of row 669 with crux (AC) and the sentence "(AC) is the wall" (`gap-skeleton-max.md` L182-188); `gap-means-max.md` 2.2; `gap-ac-lat.md` (AC'-lat), candidate C5 of row 697 | S0; passes S1 to S3 at small size only; S5: the monopole is three-dimensional | FAILS (same crux); found again |
| I6 | small 2-torus with 't Hooft flux | yes: row 842 (Theorem S1, `gap-s1-opus.md`), ideas 31 and 36 and G7 of row 858, the one-sided step-scaling form (MON') (`gap-brainstorm-max.md` L659, L681), credit Tanizaki and Unsal there | S0 | FAILS (same crux); found again. The explicit reason that the four-direction engine has no twisted form is Lemma TW below (small, new as a statement) |
| I7 | 3-sphere of radius R | **new to the lane** as a space (the 49 hits for "3-sphere" are the group manifold) | S0; no lattice, no engine | FAILS (cost of an existence proof on another lattice, and the crux stays) |
| I8 | hyperbolic space | yes: idea 42 of row 858, verdict "Dropped" (`gap-brainstorm-max.md` L438: no translation-invariant transfer operator, the gap is geometric) | S0; S1 fails at fixed radius | FAILS; found again |
| I9 | sheared tori, the modular group | yes: A4 of `gap-constraints-max.md` L185-195 and 7.4 ("It changes a constant, not the crux") | blind identities | FAILS for the wall; found again |
| I10 | fundamental Higgs | yes: B9 of row 669 (`gap-skeleton-max.md` L175-180), idea 33 of row 858 (L406), (M6) of `gap-means-max.md` L109, C19 | S0 by Proposition CB | FAILS; found again |
| I11 | adjoint Higgs family | partly: the "third test" of row 669 (`gap-skeleton-max.md` L77-80), `gap-means-max.md` L51, L70, L112, E3 of `gap-crux-exercise-r858-max.md` L342 ("It moves toward the U(1) test"); all "recalled". The exact end point (Lemma GG) is not written anywhere | a test, not a tool | no route; the lemma is small and new as a statement |
| I12 | soft-broken supersymmetry, heavy matter | yes: C19; `gap-means-max.md` L51 | S0 by CB; no supplier | FAILS; found again |
| I13 | N, and the dimension | yes: idea 33, idea 34 of row 858; the N-test and the dimension test of `gap-crux-fp.md` F15, L76, L283 (five dimensions, GUIDE); B8 of row 669 with crux (DF2), credit Durhuus and Froehlich | S2 or false hypothesis | FAILS; found again |
| I14 | Hamiltonian, stability along a path | yes: ideas 32, 37 and G15 of row 858 ("strong coupling. Not order one"); Wall C (block criteria of Knabe type fail); row 786 (the Langevin gap of Villain U(1) tends to 0, so a group-blind continuation is false) | S0 | FAILS; found again |
| I15 | gradient flow | partly: idea 9 of row 858 (the flow as a transport map). The flow coupling t^2 E(t) as a selective number: no hit | no consumer | FAILS (no consumer) |
| I16 | stochastic quantisation | yes: rows 786, 812 to 829 (ranges of the Langevin gap; (G2) equivalent to the uniform gap; W23 "curvature criterion = the gap") | S0 | FAILS; found again |
| I17 | Lee-Yang in a centre-breaking field | yes: B9 of row 669 with crux (LY) (`gap-skeleton-max.md` L177-180), (M6) with a counterexample at beta = infinity from recalled theorems, and `gap-skeleton-max-b.md` L581 (zeros of one 3-cube in the right half-plane, a numeric GUIDE, for the plaquette field) | not selective; stops at kappa > 0 | FAILS; found again. **New here: a hand proof that the crux (LY) is false already for one plaquette, at every beta > 0 (Lemma LYP, Section 6).** |
| I18 | complex beta | yes: C4 of row 697, Theorem V (`gap-zf-box-s.md`), Theorems Z and ZB (`gap-skeleton-max-b.md`) | stronger than the target | blocked-equivalent or stronger; found again |

### 4.3 What the fresh pass added, and what it only found again

Added (each is small; none is on the path of the wall):

1. The exterior, radial and 3-sphere frame (I2, I7), with its failure reason. With it, one remark (ARGUED, a reading): **in every frame the first-passage value of the frame's number is a small perturbation of the value of free massless fields in that same frame.** Examples: on the periodic torus z ~ g^(2/3), against 0 for the flat directions; on the 3-sphere R m = 4 + O(g^2), against 4 for free gluons under the Gauss law (a Maxwell field has 2); in a twisted box the momenta are shifted by pi/L for SU(2) as for free fields with the same boundary signs. Free massless fields with the same boundary condition are massless models, so an engine that is valid for them has its threshold at or above the free value. So in no frame does a class-wide engine fire at first passage. This is the frame-independent form of "blind engine, selective seed" (`gap-brainstorm-max.md` L661).
2. Lemma TW (Section 6): the reason that a twisted family has no four-direction engine.
3. Lemma LYP (Section 6): the crux (LY) of B9 is false for one plaquette.
4. Lemma GG (Section 6): the end point of the adjoint Higgs family is compact U(1) exactly.

Only found again: everything else in Sections 3.0 to 3.5.

No correction of the earlier work came out of the compare step. In two places the earlier work has the stronger form and I use it: C19 for Proposition CB, and (M6) for the infinite-volume failure of a zero-free half-plane.

## 5. Ranking (step 5)

Rule of the row: what the item would change, divided by the cost to find out.

**No idea of the list survives as a route to (W), to (CAS) or to the gap.** Each one either returns the crux in another scheme (I1, I2, I5 to I10, I12, I14, I16), or has no consumer (I3, I4, I15), or has a false hypothesis or no rate (I13), or is on file as stronger than the target (I18), or is a test (I11). Under the proof-search governance every frame family is `blocked-equivalent` (terminal obligation: the flow of the frame's number does not stop in the band) or `retired`. The reopen condition is the same for all: a mechanism that makes one step of the flow selective. A change of frame does not supply one.

What is left to rank are statements that can be decided by hand and that close something on file:

| Rank | Item | What it changes | Cost | Status after this run |
|---|---|---|---|---|
| 1 | (TM-tw) as a lemma of its own: the transfer operator of a twisted box. It is the first lemma of the one frame change that is on the lane's path (the flux half reads twisted partition functions). It was asked for in row 731 (`gap-flux-exercise.md` L660, item 2: "Write `library/gap-transfer-twisted.md`") and in the ledger of row 838 (`gap-assume-opus.md` rows 58, L265, L486-490: "proposed in row 731, never queued. Cheap."). No file of that name exists at this pin; FINISH has no row for it. | Theorem R, the full and kappa seeds and the fusion consumer rest on it; today it lives in two check files | one port from `gap-transfer.md` | Section 7 |
| 2 | Lemma LYP: the crux (LY) of B9 is false for one plaquette | closes a verdict that rested on "no theorem known" and on a recalled infinite-volume fact | one page | Section 6, PROVED |
| 3 | Lemma GG: the adjoint Higgs end point | makes the "third test" exact at its end point | half a page | Section 6, PROVED |
| 4 | Lemma TW: no twisted four-direction engine | a reason on record for "continuation in the fibre size has no engine" | a few lines | Section 6, PROVED |
| - | I2, I7 (exterior, sphere) | nothing on the wall | an existence proof on another lattice | not proposed |

## 6. Real attempts, part 1: three statements decided by hand (step 6)

Rule 0a before each: `library/open-core.md` has no entry for any of them; FINISH has no row for a Lee-Yang statement, for the adjoint end point or for a twisted engine (searched by "Lee-Yang", "(LY)", "B9", "adjoint Higgs", "Georgi", "TM-tw"). All three are off the direct path of the wall: they close or sharpen verdicts on frame changes.

Notation. I_n is the modified Bessel function, J_n the Bessel function, n an integer. Facts used (classical; each is one line from the series or the integral representation): I_n(iy) = i^n J_n(y) for real y; |I_n(kappa)| <= exp(|Re kappa|) (from I_n(kappa) = (1/2 pi) times the integral over theta of exp(kappa cos theta) cos(n theta)); I_(n-1) - I_(n+1) = (2n/x) I_n; J_n' = (n/y) J_n - J_(n+1); two solutions of the Bessel equation that vanish with their derivative at a point y != 0 vanish identically.

### 6.1 Lemma LYP: a Lee-Yang property in the link field is false for one plaquette

**Setting.** G is Z_2, U(1) or SU(2), with normalized Haar measure, and chi is the function sigma, cos theta or (1/2) tr U. One plaquette with four links U_1, ..., U_4. For beta >= 0 and complex kappa,

  Z_G(beta, kappa) = integral of exp( beta chi(U_1 U_2 U_3^(-1) U_4^(-1)) + kappa (chi(U_1) + chi(U_2) + chi(U_3) + chi(U_4)) ) dU_1 ... dU_4.

For SU(2) this is the weight of B9 (`gap-skeleton-max.md` L177): a fundamental Higgs field of fixed length in the unitary gauge, on the smallest lattice with a plaquette.

**Lemma LYP (PROVED by hand here; checked by no one).** Let beta > 0 and G one of the three groups.
- (a) kappa -> Z_G(beta, kappa) is an even entire function with |Z_G(beta, kappa)| <= exp(beta + 4 |Re kappa|).
- (b) Z_G(beta, i y) > 0 for every real y.
- (c) Z_G(beta, .) has a zero, and every zero has a non-zero real part. So it has a zero with Re kappa > 0.

So the crux (LY) of B9, "Z_Lambda(b, kappa) is not zero for Re kappa > 0, for every b >= 0 and every Lambda", is false for Lambda = one plaquette and every b > 0. At beta = 0 the zeros are on the imaginary axis (four independent links).

**Proof.** Formulas. Expand the plaquette weight in characters and integrate each link.

- Z_2: summing the 16 configurations by the number of minus signs, with x = cosh 2 kappa,
  Z = (1/16) [ e^beta (e^(4 kappa) + 6 + e^(-4 kappa)) + e^(-beta) (4 e^(2 kappa) + 4 e^(-2 kappa)) ] = (e^beta/4) [ x^2 + 2 e^(-2 beta) x + 1 ].
- U(1): exp(beta cos phi) = sum over n in Z of I_n(beta) e^(i n phi), and the integral of exp(kappa cos theta) e^(+-i n theta) d theta/2 pi is I_n(kappa). So
  Z = sum over n in Z of I_n(beta) I_n(kappa)^4.
- SU(2): exp(x (1/2) tr U) = sum over j of a_j(x) chi_j(U) with a_j(x) = I_(2j)(x) - I_(2j+2)(x) = 2 (2j+1) I_(2j+1)(x)/x (the character is sin((2j+1) theta)/sin theta and the class measure is (2/pi) sin^2 theta d theta). For a class function f with f(U^(-1)) = f(U), the integral of f(U) D^j(U) dU is (1/d_j)(integral of f chi_j) times the identity (Schur), d_j = 2j + 1. So the integral of chi_j(U_1 U_2 U_3^(-1) U_4^(-1)) times the four link weights is d_j (a_j(kappa)/d_j)^4, and with n = 2j + 1:
  Z = sum over n >= 1 of (2 n^2 I_n(beta)/beta) (2 I_n(kappa)/kappa)^4.

(a) Each term is entire and even in kappa (I_n(-kappa) = (-1)^n I_n(kappa), fourth power). The coefficients are positive and sum to a finite number: at kappa-weights replaced by their bound, sum over n of I_n(beta) = e^beta for U(1), and sum over j of a_j(beta) d_j = e^beta for SU(2) (the expansion at U = 1). With |I_n(kappa)| <= e^(|Re kappa|) and |a_j(kappa)/d_j| <= e^(|Re kappa|) (the integral of |f chi_j| is at most d_j sup |f|), the series converge uniformly on compact sets and |Z| <= e^(beta + 4 |Re kappa|). For Z_2 the formula is explicit.

(b) Z_2: at kappa = i y, x = cos 2y lies in [-1, 1], and x^2 + 2 e^(-2 beta) x + 1 >= 1 - e^(-4 beta) > 0 (minimum at x = -e^(-2 beta)). U(1): I_n(i y)^4 = (i^n J_n(y))^4 = J_n(y)^4 >= 0, so Z(beta, i y) >= I_0(beta) J_0(y)^4 + 2 I_1(beta) J_1(y)^4. J_0 and J_1 = -J_0' have no common zero. SU(2): for y != 0, (2 I_n(i y)/(i y))^4 = (2 i^(n-1) J_n(y)/y)^4 = 16 J_n(y)^4/y^4 >= 0, so Z(beta, i y) >= (32/(beta y^4)) (I_1(beta) J_1(y)^4 + 4 I_2(beta) J_2(y)^4). If J_1(y) = J_2(y) = 0 at y != 0 then J_1'(y) = J_1(y)/y - J_2(y) = 0 and J_1 vanishes identically, which is false. At y = 0, Z(beta, 0) = 2 I_1(beta)/beta > 0.

(c) Z_2: the zeros are the solutions of cosh 2 kappa = -e^(-2 beta) +- i (1 - e^(-4 beta))^(1/2), a non-real number. For kappa = a + i b, Im cosh(2a + 2ib) = sinh 2a sin 2b, so a != 0. U(1) and SU(2): suppose Z(beta, .) has no zero. Then h = log Z is entire with Re h <= beta + 4 |kappa|. By the Borel-Caratheodory inequality and the Cauchy estimates, h is a polynomial of degree at most 1, h = a kappa + b. Z is even, so a = 0 and Z is constant in kappa. But for real kappa -> infinity the first term alone tends to infinity (I_0(kappa) or I_1(kappa)/kappa). So Z has a zero kappa_0. By (b) Re kappa_0 != 0. Z is even, so -kappa_0 is a zero too, and one of the two has positive real part. QED

**Remarks.** (1) Where the zeros go (ARGUED, first order in beta, SU(2)): near a zero i j of 2 I_1(kappa)/kappa the function is A (kappa - i j)^4 + beta B with A, B of one sign on the imaginary axis, so the four-fold zero splits into four zeros at distance of order beta^(1/4) in the four diagonal directions. (2) What this does and does not show. It refutes the half-plane form of the crux as B9 states it. It does not refute a zero-free neighbourhood of the positive real kappa-axis; that weaker form is what the two-constants argument of B9 would use, and (M6) of `gap-means-max.md` L109 names its failure in infinite volume at beta = infinity (recalled theorems on the four-dimensional O(4) model). B9 was already set aside; its verdict "no Lee-Yang property for a plaquette interaction" (`gap-skeleton-max.md` L409) now has a proof at the smallest size. (3) The same computation with the field on the plaquette instead of the links is the positive statement on file: the one-plaquette integral 2 I_1(beta)/beta has imaginary zeros only (`gap-skeleton-max-b.md` L581). (4) The method (positivity on the imaginary axis from a fourth power) uses that a plaquette has four links; it is the four-body nature of the interaction in one line.

### 6.2 Lemma GG: the adjoint Higgs family ends at compact U(1), exactly

**Setting.** A finite lattice (a torus or a box) with sites V, links E, plaquettes P. Link variables U_l in SU(2) with Haar measure dU. Site variables phi_x in S^2, the unit sphere of the Lie algebra su(2) = R^3, with the normalized rotation-invariant measure. w is a continuous, strictly positive class function on SU(2). For kappa >= 0 the weight is

  W_kappa(U, phi) = product over p of w(U_p) times product over links l = (x, y) of exp( kappa (<phi_x, Ad(U_l) phi_y> - 1) ).

It is invariant under U_xy -> g_x U_xy g_y^(-1), phi_x -> Ad(g_x) phi_x. Let H = {u(alpha) = exp(i alpha sigma_3)} be the stabilizer of e_3 = the direction of sigma_3. The compact U(1) model with weight w has link angles theta_l with normalized Lebesgue measure and weight product over p of w(u(theta_p)), theta_p the oriented sum around p.

**Lemma GG (PROVED by hand here; checked by no one).** For every continuous gauge-invariant function F of (U, phi),

  lim as kappa -> infinity of <F>_kappa = <F~>_(U(1), w),  F~(theta) = F( (u(theta_l))_l , phi = e_3 at every site ).

Also c_kappa^(-|E|) Z_kappa -> Z_(U(1), w), with c_kappa = (1 - e^(-2 kappa))/(2 kappa). For the Wilson weight w(U) = exp(beta (1/2) tr U) the limit is compact U(1) with the Wilson weight exp(beta cos theta_p) at the same beta.

**Proof.** Step 1 (unitary gauge). Choose a measurable map s from S^2 to SU(2) with Ad(s(phi)) phi = e_3. For fixed phi put g_x = s(phi_x). By gauge invariance F W_kappa at (U, phi) equals F W_kappa at (g_x U_xy g_y^(-1), e_3). The map U -> (g_x U_xy g_y^(-1)) preserves the Haar measure. So the integral of F W_kappa over U at fixed phi equals the integral of F(U, e_3) W_kappa(U, e_3) dU, which does not depend on phi. The phi-integral is then 1.
Step 2 (one link). Let t(U) = <e_3, Ad(U) e_3> and nu_kappa(dU) = c_kappa^(-1) exp(kappa (t(U) - 1)) dU. Under Haar measure Ad(U) e_3 is uniform on S^2, so t is uniform on [-1, 1]; this gives c_kappa and nu_kappa(t <= 1 - delta) = (e^(-kappa delta) - e^(-2 kappa))/(1 - e^(-2 kappa)) -> 0 for every delta > 0. The set {t = 1} is H. nu_kappa is invariant under U -> hU and U -> Uh, h in H, because t is and Haar measure is. SU(2) is compact, so every sequence kappa -> infinity has a weakly convergent subsequence; a limit is a probability measure carried by H and invariant under the translations of H, so it is the Haar measure of H. So nu_kappa -> Haar_H weakly.
Step 3. <F>_kappa is the quotient of the integrals of F(U, e_3) product of w(U_p) and of product of w(U_p) against the product measure of the nu_kappa over the links. Both integrands are continuous. Finite products of weakly convergent probability measures on compact metric spaces converge weakly. The limit of the denominator is Z_(U(1), w) > 0. QED

**Corollary GG1 (PROVED given (TM) for the family; the extension of (TM) to a site field is ARGUED, not written: the time-like hopping kernel exp(kappa <phi, phi'>) is strictly positive and of positive type, and the proof of `gap-transfer.md` runs on the enlarged slice space; credit Osterwalder and Seiler for the gauge-Higgs transfer operator, recalled).** For every box B and time k, the thermal sum S_kappa(k; B) tends to S_(U(1), w)(k; B). Proof: by Lemma A applied to the normalized partition functions Z~ = c_kappa^(-|E|) Z, (Z~(2j)/Z~(j))^(1/j) <= lambda~_0 <= Z~(j)^(1/j) for every j. Let kappa -> infinity, then j -> infinity. Both ends tend to the top eigenvalue of the U(1) model. So lambda~_0,kappa converges to it, and S = Z~(k)/lambda~_0^k - 1 converges. QED

**Reading.** Take for w the class function on SU(2) that equals the Villain function on H: w(U) = sum over n of exp(-(beta/2)(theta(U) - 2 pi n)^2), theta(U) the class angle. It is continuous, positive and of positive type on SU(2) (its character coefficients are differences (1/2)(v_(2j) - v_(2j+2)) of the decreasing Fourier coefficients v_k = c exp(-k^2/(2 beta))). At kappa = 0 the family is a pure SU(2) gauge model of the lane's class. At kappa = infinity it is Villain U(1) at beta, the lane's theorem-grade test (no seed at beta >= 2^14, row 786 and the test table). So for every N_max there is kappa_0 with no seed of size up to N_max for kappa >= kappa_0. The models of the family share with the target: the gauge group SU(2), the plaquette weight, the centre symmetry (an adjoint field does not see the centre, so the twisted partition functions and the flips exist for every kappa), reflection positivity, locality. They differ by the site field, and through it in one more point: for kappa > 0 a twist is no longer free classically (the twist eaters i sigma_1 and i sigma_2 fix no common adjoint direction, so a twisted torus forces a defect of the site field or an abelian flux; at kappa = infinity the Z_2 twist is half a flux quantum of U(1), with cost of order beta). **So a class-wide tool must use that the state space holds the gauge field only, or the zero classical cost of the twist (Fact T of row 697), which the family loses at once.** This is the content of the "third test" of row 669 (`gap-skeleton-max.md` L77-80, "recalled"); the lemma makes its end point exact. It binds T_fix-tools, and T_W-tools with no ultraviolet clause. For finite kappa the absence of a seed at every size is a BELIEF (the Coulomb phase of the four-dimensional Georgi-Glashow model), not a theorem here.

### 6.3 Lemma TW: which twisted families have an engine

Twist classes k in Z_2^6 (k_(mu nu) for mu < nu), partition functions Z^k(n) and the operators T_(B,m) as in `gap-flux-exercise.md` 3.0 ((TM-tw); see Section 7). Call a direction mu **clean** for k if k_(mu nu) = 0 for every nu.

**Lemma TW (PROVED given (TM-tw) and the reading of the engine's needs in `gap-constraints-max.md` row 1: "The engine needs a trace in both channels of an exchanged pair. ... Spectator directions need (TM) only").**
- (a) If mu is clean, Z^k(n) = Tr(T_(B,m)^(n_mu)) with T_(B,m) positive, and Lemma A holds in the side n_mu. If mu is not clean, Z^k(n) = Tr(T_(B,m)^(n_mu) C) with a product C != 1 of centre flips: a signed sum of the lambda_i^(n_mu). Then Z^k(n) >= lambda_0^(n_mu) holds only if the centre-odd thermal sum is at most the centre-even one.
- (b) Multiplying the side n_mu by an integer j multiplies every k_(mu nu) by j modulo 2. So doubling a side removes the twists in the planes through it, and an odd multiple keeps them.
- (c) An exchanged pair with positive traces in both channels is a pair of clean directions. The classes with two clean directions are k = 0 and the six single-plane twists. For a single-plane twist the engine runs in the two directions outside the plane, at a fixed size of the twisted plane. It does not move the size of the twisted plane: by (b) a doubling leaves the family, and by (a) an odd multiple has a signed trace in the crossed channel.
- (d) A class that is invariant under all exchanges of axes has all six entries equal. The non-zero one has no clean direction.

Proof. (a) is the split of a twist into its planes through mu (flips) and the others (the operator), `gap-assume-opus.md` L494, with Lemma A for the positive operator. For the last sentence write Tr(T^j C) = lambda_0^j (1 + S_even(j) - S_odd(j)); the top eigenvector is even. (b): a plane twist is a product of flips on a stack of plaquettes that the plane (mu, nu) meets once per period; a torus with side j n_mu is a j-fold cover in direction mu, and the pulled-back class is j k_(mu nu). In operator form: Tr((T^(n_mu) C)^j) and C^2 = 1. (c): if mu and nu are clean then k_(mu rho) = k_(nu rho) = 0 for all rho, and only the entry of the complementary plane is free. (d) is immediate. QED

Reading. The thin twisted torus (row 842, ideas 31 and G7 of row 858) has an engine in its two long directions only. "No monotonicity in n is known" (`gap-brainstorm-max.md` L404) has this structural reason behind it: the twisted plane is exactly the pair of directions where the engine's traces lose their sign.

### 6.4 A guard run for Lemma LYP (a run can refute or guide; it proves nothing)

Pre-registered before the run (2026-11-15, before any output was seen). Purpose: catch an algebra slip in the three formulas of 6.1 and in part (b). Script and output: a scratch folder under /tmp (path in the log line below); under the numeric lock; memory free 69 percent at start.

- R1 (formula). For SU(2) at beta = 1, kappa = 0.7 (real) compare the series of 6.1 with a direct Monte Carlo integral over four Haar-random unit quaternions (2 x 10^6 samples). PASS reading: agreement within 4 standard errors. FAIL reading: a disagreement above that (then the Schur step or a coefficient is wrong).
- R2 (part (b)). For beta = 1 evaluate Z_G(1, i y) on the grid y = 0, 0.01, ..., 40 for U(1) and SU(2). PASS: the minimum is positive. FAIL: a value <= 0 (then (b) is false as written).
- R3 (part (c)). For beta = 1 search a zero by Newton iteration started off the axis near i j, j the first positive zero of J_1 (SU(2)) or of J_0 (U(1)). PASS: a zero with |Re kappa| > 10^(-3) and |Z| < 10^(-25) there. FAIL: no such zero found from five starting points (this would not refute (c), which is a proof of existence; it would send me back to the formulas).

Result of the run (2026-11-15T16:57Z; script `lyp_guard.py` and output `lyp_guard.out` in the scratch folder /tmp/gob-num-94236, not in the repository; mpmath 1.3.0 at 40 digits, numpy 2.4.1; lock holder gob-1004-94236, released). All three readings PASS. A guide only.

- R1: series 1.4417815, Monte Carlo 1.44095 +- 0.00102 (2 x 10^6 samples); difference -0.82 standard errors.
- R2: the minimum of Z_G(1, i y) on the grid is positive: 1.78 x 10^(-4) at y = 39.34 for U(1), 1.16 x 10^(-9) at y = 39.17 for SU(2) (the terms fall like y^(-2) and y^(-6)).
- R3: zeros off the axis at beta = 1: for U(1) kappa = 0.503093 + 3.057435 i and 0.452334 + 6.192486 i; for SU(2) kappa = 0.607619 + 4.458436 i, -0.497009 + 7.621804 i, -0.516819 + 12.481157 i; |Z| below 10^(-41) at each. For Z_2 the explicit zero is kappa = 0.439055 + 0.833431 i.

What the run can and cannot establish: it found no slip in the formulas and it shows zeros where the lemma says they are. It does not replace any step of the proof, and the proof does not use it.

## 7. Real attempts, part 2: the first lemma of the twisted frame, written (step 7)

**What was done.** The item ranked first in Section 5, (TM-tw), is written as a lemma of its own with its proof: `library/gap-transfer-twisted.md` (new file, this run). Rule 0a: `library/open-core.md` has no entry; FINISH has no row for it (`grep -c "TM-tw\|transfer-twisted" FINISH.md` = 0); the file did not exist at this pin. The work item is item 2 of `gap-flux-exercise.md` L660 (row 731), repeated in `gap-assume-opus.md` L265 and L486-490 (row 838).

**Statement (Theorem TW-T there; PROVED by hand, given Statements (1) to (4) and Lemmas A0 to A3 of `gap-transfer.md`, which were checked in row 671; this file is checked by no one).** For every box with sides at least 3, every magnetic twist m and every time extent T >= 2: (T1) the gauge-projected operator T_(P,m) is an integral operator with a continuous, symmetric kernel between exp(-12 beta |Lambda|) and 1; (T2) it is positive, Hilbert-Schmidt and trace class; (T3) its top eigenvalue is simple with a continuous, positive, gauge-invariant eigenvector; (T4) the centre flips are commuting unitary involutions that commute with it, and the ground state is even; (T5) Tr(T_(P,m)^T C^e) is the twisted partition function Z^(e,m); (T6) the sector sums are non-negative and satisfy (F1); (T7) the partition function does not depend on the positions of the stacks (Lemma P) and is carried along by permutations of the axes, so every direction can be the time; (T8) Z_(chi,m) <= Z_(0,m), 0 < Z^k <= Z^0, lambda_m <= lambda_0.

**How it is proved.** Section 3.1 there lists every use that Sections 1 to 4 of `gap-transfer.md` make of the cube and of the potential V: the numbers of sites, links and plaquettes, and three properties of V (real and continuous; between 0 and 6 beta times the volume; gauge invariant), plus the identity that the spatial part of the action of a slice is V of that slice. The twisted potential V_m has the three properties. The flips need one new line: the two links of direction k in a spatial plaquette have the same k-coordinate, so every u_p, and so V_m for every m, is invariant under the flip. The trace with flips is a computation with the kernel A_m(u, Z^e w). Lemma P moves a stack by changing the sign of one layer of links.

**Standing.** Nothing in it is new mathematics: the content was in `gap-seed-check.md` (Lemma 1.1, Remark F3) and `gap-flux-exercise.md` (3.0, C2), and row 732 checked the statement. The new thing is the single written proof. It is on the lane's path only through the flux half (Theorem R, the seeds, the fusion consumer); it does not move the wall. It needs one check by another model; the points to test first are listed in its Section 5.

**Not done.** Statement (5) of `gap-transfer.md` for the twisted box (a positive gap of each finite twisted box) is not ported; no consumer on file reads it.
