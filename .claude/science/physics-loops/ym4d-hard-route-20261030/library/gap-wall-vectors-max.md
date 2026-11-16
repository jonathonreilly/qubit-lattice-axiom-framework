lead: anthropic/claude-fable-5-2/max mac-mini-worker
lease_until: 2026-11-17T02:36Z

# gap-wall-vectors-max (row 1053): new attack vectors from the first-principles assumptions file

Worker: Claude Fable 5.2, max effort, Mac mini worker 2. One session. Pinned at commit a31c990cd on `claude/ym4d-hard-route`. Checked by no one. Research-stage working state; it grants no status.

Lease written from `date -u` = 2026-11-16T14:36Z plus 12 h.

## Plan (eight steps; one step per response; each result is appended before the next)

1. Read `library/gap-wall-assumptions-opus.md` (row 1052) in full. Record its top fifteen assumptions and every assumption whose "what if wrong" opens something.
2. Read `parts/gap.md` and `library/gap-direction3-max.md` (row 1051), only to avoid redoing work. Grep the lane for each candidate idea before naming it.
3. Task (1), (2): for each listed assumption, say whether dropping or replacing it gives a vector. For each vector: exact statement, consumer in a chain to the mass gap, change against the current route, source, cheapest kill test.
4. Task (3): kill fast with the tests on file (Lemma PT, Proposition NP, Theorem D2, Lemma SHEET, compact U(1), frozen Q_8 and 2T, the five-dimensional test, Lemma CEN+, Lemma WN, the four-test spec check). A vector that renames an open statement is a FAIL.
5. Task (4): rank the survivors by change divided by cost to find out.
6. Task (5): for the top one or two, invent the mechanism, write the first lemma and try it by hand, or build the counterexample.
7. Task (6): literature lens on any new path.
8. Task (7): one complete brief per surviving vector for a proof row. RESULT line.

## Step log

(Each step appends below.)

### Step 1 result: what row 1052 hands over (read in full, L1-630)

Source: `library/gap-wall-assumptions-opus.md` (Claude Opus 5.5 high, row 1052, unchecked). I read all 630 lines. Nothing below is new mathematics; it is the list this row must answer.

**Its top fifteen (its ranking, L372-388):** 1 e1 (the gap is true); 2 f1 (no computer steps); 3 a2 (R^4, no compact direction); 4 c3 (seed plus scale transport); 5 c4 (order-one coupling is the hard regime); 6 e4 (asymptotic freedom holds non-perturbatively); 7 b2 (Wilson action); 8 c1 (existence before gap); 9 b3 (Euclidean); 10 a3 (gap on all of Omega-perp); 11 c7 (effective actions near-Wilson at the crossover); 12 e9 (infrared easy once strong); 13 b1 (lattice at all); 14 c2 (RG frame at all scales); 15 d2, d3, d9 (discard tests that rest on gapped models or on beliefs).

**Other assumptions whose "if wrong" entry opens something (its tables, L280-368):** b6 (periodic tori; twisted, free or Dirichlet walls), b8 (observables: a total set of smoothed bounded observables suffices), b10 (isotropic spacing; anisotropic limit), b11 (pure gauge; heavy or Higgs matter), b12 (SU(2) fields only; explicit Z_2 x SO(3) and pi_3 variables), b13 (one-loop trajectory; free irrelevant couplings), c8 (small-field / large-field split; a hard admissibility constraint), c9 (one tool), c10 (clustering apart from gap), c11 (seed by hand; parametric seed), e7 (Gribov as obstruction), e8 (instantons irrelevant), e10 (strong coupling is the only rigorous source), e12 (universality), d4, d8.

**Its 5.4 list, S1-S6 (what (W) adds to the Clay gap):** S1 bare Wilson on one trajectory; S2 uniform on every lattice of the sequence; S3 periodic tori with every flux sector; S4 partition functions only; S5 (BDD-Delta); S6 the gap leg waits for T0's (H2), (TOT).

**Its own results that this row may consume (all unchecked):** fact A2 (a uniform rate on a total set gives the gap and passes to limits); Lemma FLUX-W ((W) forces every electric flux energy of large periodic cubes above the gap); the scope correction (frozen Z_2, Q_8, 2T bind periodic-box statements only, since flat fields on simply connected regions are pure gauge); the target form T_JW-lat (L485).

**Its five "most likely wrong" (L621):** (1) periodic all-sector seed; (2) uniformity on every bare lattice; (3) Wilson's action; (4) existence before gap; (5) a seed carried by a doubling engine.

**Its routes Q1-Q9 (L536-546) and their state there:** Q1 simply connected one-box estimate (held by rows 1051, 1053: this row); Q2 dead (band again); Q3 action choice (no mechanism named); Q4 ordering only; Q5 deformation FAILS (same crux); Q6 blocked-equivalent ((LIOU)); Q7 relabel to T_JW-lat (reading); Q8 no consumer; Q9 no candidate.

What is left for this row: row 1052 named no mechanism for Q1 or Q3 and attacked neither. This row's job is to find vectors with a mechanism. Next: step 2 (read `parts/gap.md` and `library/gap-direction3-max.md`; grep before naming).

### Step 2 result: what the lane already holds (read only to avoid redoing work)

Read in full: `parts/gap.md` (257 lines) and `library/gap-direction3-max.md` (283 lines at this pin; it stops after its Section 4.2, so its Section 5 is not visible to me). Read in part, for idea titles only: `library/gap-next3-max.md` L255-300 (the inventory of rows 859, 876, 878, 899, 900) and `library/gap-global-reform-max.md` L506-605 (row 1016, candidates (GF), (HAM), (CMP)).

**What binds this row (from those files).**

- The wall is (W) on periodic tori. Every route ends at one selective inequality at order-one coupling (`parts/gap.md` L41-46, L256-257).
- The lane's idea lists are long: row 859 (52 ideas), row 876 (60), row 878, row 1004 (I1-I14), row 1013 (C1-C9), row 1016 (ten reformulations), rows 1031-1032 (A1-A10, B1-B15). A vector counts as new here only if its crux lemma is none of these.
- Row 1051 holds the port of OpenAI's one-annulus engine to the pin space of a gauge cell (its Section 3, last paragraph), and the "blind half" of every stiffness line (its 4.2). Rule 0a: I do not attack those.
- Route W (free-wall boxes, no flux sector) is on file (rows 858, 900; `gap-next3-max.md` C1). So row 1052's Q1 is found again in form; what Q1 lacks is a mechanism for the one-box estimate.

**Grep of the lane for my first candidate list (two wordings each; scope `library/` and `parts/` of this folder; counts are files).**

| Candidate | Grep words | Files | Verdict |
|---|---|---|---|
| Durhuus-Frohlich slab comparison, with the posted 2D O(4) gap as input | Durhuus; layer comparison | 29 | found again: rows 825-857 (area law below 2/3), `gap-brainstorm2-max.md` G8 (3D through the slab), row 1016 4.6 (FAILS in d = 4: the layer is 3D and orders) |
| Hyperbolic space or a sphere as infrared regulator | hyperbolic space; Callan; four-sphere | 12, 7 | found again: row 859 idea 42 (dropped), row 1004 I8 (FAILS) |
| Free-wall or simply connected boxes | free wall; Route W | many | found again: rows 858, 900, 910 |
| Transverse lattice as a gauge fixing with a rigid two-dimensional group | transverse lattice; Bardeen | 4, 1 | found again: row 1016 4.4, FAILS (Elitzur) |
| 1+3 anisotropy (path in beta_t from 0; beta_s = 0) | beta_t path; anisotropic | 64 | found again: rows 988, 992 (needs 3D mixing and (NOCRIT)); row 859 "anisotropic action from beta_s = 0" |
| Defect-angle class function (frame-averaged non-central twist) | defect-angle; w_phi | on file | found again: row 859 |
| Orbit-space curvature; Gribov region as a convex domain | Singer; Faddeev-Popov | 15 | found again: exercise 4 input 10; row 1032 B8 (not selective) |
| Twist free energy as a running coupling; gradient-flow transport | step-scaling; gradient-flow | on file | found again: row 859 |
| Z_2 x SO(3) variables, Nishimori line, planted Z_2 | SO(3) x Z_2; Nishimori | 38 | found again: rows 859, 876; K7 note in FINISH |
| Trace anomaly, low-energy theorems, a-theorem | trace anomaly; Komargodski | 14, 10 | found again: row 859 (exact scale identity), row 1031 (VIR) |
| **2+2 anisotropy: the point beta_long = infinity, beta_trans = 0, where the model is a product of 2D O(4) models** | 2+2; beta_perp; decoupled/independent chiral; product of chiral | 0 | **not found** (the transverse-lattice picture is on file only as a gauge fixing) |
| **Inverse order: fix the infrared measure first and refine (projective family)** | to be searched in step 3 | - | pending |

Next: step 3. For each top-fifteen assumption and each opener, a vector or "no vector", with the grep that backs each "found again".

### Step 3 result: assumption by assumption, vector or no vector (tasks 1 and 2)

Marks: NEW = not found in `library/` and `parts/` of this folder by the greps named (open PR branches not searched). FOUND = on file, with the place. A vector is written out only if it is NEW. Nothing in this step is a proof.

#### 3.1 The table

| Assumption (row 1052) | Drop or replace | Outcome |
|---|---|---|
| e1 gap true | drop | No vector toward the gap. It gives one new test model, V5. |
| f1 no computer step | keep; replace "one number at order one" by a parametric regime | V2 (NEW, FAILS in step 4). |
| a2 R^4 | compact direction, Higgs, sphere, hyperbolic space | FOUND: `gap-skeleton-max.md` L8, L371, L410; row 1004 I5, I6, I8; row 859 idea 42. No new vector. |
| c3 seed plus transport | another reduction | FOUND: Theorem CR (row 1017), routes RA-RG, LC. NEW: the chain of V1. V4 (NEW framing, FAILS). |
| c4 order one is the hard regime | split the hard regime | NEW reading through V1: the wall has a frame half and a singlet half; V1 names a model where the frame half is absent. |
| e4 asymptotic freedom beyond perturbation theory | - | No vector. Patrascioiu-Seiler is on file (7 files). |
| b2 Wilson action | choose the weight | FOUND: (UNIV-FP), heat kernel (row 876 idea 17), no Z_2 monopoles (row 900 item 2), mixed action (row 876 idea 31). NEW: V1 (a point on the boundary of the anisotropic Wilson family), V3. |
| c1 existence before gap | merge | FOUND: row 838 items 10, 14, 37. No mechanism, no vector. |
| b3 Euclidean | Hamiltonian | FOUND: row 859 ideas 32, 37; row 1004 I14; row 1016 4.5 (Identity HAM1). No new vector. |
| a3 gap on all of Omega-perp | charged and singlet parts apart | NEW inside V1: the rigid group splits the state space; the charged part has a mechanism, the singlet part has none (step 6). |
| c7 near-Wilson effective actions | - | FOUND: row 838 item 23. No vector. |
| e9 infrared easy once strong | - | FOUND: row 838 items 48, 49. No vector. |
| b1 lattice at all | loop equations, stochastic quantisation | FOUND: `gap-loop-eq-opus.md`, `gap-form-exercise.md` L352. No vector. |
| c2 RG frame at all scales | another tool after first passage | NEW through V1: the two-dimensional mechanism in place of an RG step, at one reference coupling. |
| d2, d3, d9 tests | which tests bind T_JW-lat | NEW: V5 (the torus normaliser binds T_JW-lat where Q_8 and 2T do not). |
| b6 walls | free, twisted, pinned | FOUND: Route W (rows 858, 900, 910); Theorem TW-T (row 1004). |
| b8 observables | smoothed total set | FOUND: gradient-flow transport (row 859). |
| b10 isotropic spacing | anisotropy | 1+3 FOUND (rows 988, 992; row 859). **2+2 NEW: V1, V2.** |
| b11 matter | Higgs | FOUND: row 1016 3.1, `gap-thermpin-opus.md` L48. |
| b12 explicit Z_2, SO(3), pi_3 | - | FOUND: rows 859, 876, 900; K8. |
| b13 trajectory | free irrelevant couplings | V2, V3 (NEW; both FAIL in step 4). |
| c8 hard constraint | freeze one plaquette orientation | NEW: this is V1 (beta_L = infinity is a hard constraint on the (0,1) plaquettes). |
| c11 seed by hand | parametric seed | V2. |
| e7 Gribov | convex region | FOUND: row 1032 B8 (not selective). |
| e8 instantons | - | FOUND: exercise 4 input 15; K8. No mechanism. |
| e10 only strong coupling gives non-abelian gaps | a third source | NEW: the posted two-dimensional theorems, imported at an exact point (V1, Lemma ANCH). |
| S1-S6 of row 1052 | - | S1: V1, V3. S2: no mechanism found. S3: row 1052's T_JW-lat; V5 corrects its test list. S4: V1 reads pins, not partition functions. S5, S6: no vector. |

#### 3.2 Vector V1 (NEW): the flat-plane face of the anisotropic Wilson family

**Source.** Assumptions b10, b2, c8, c2, a3. It answers a reopen condition that the lane wrote itself: row 1016, registry line F3, "a class of pins on which a rigid group acts and cannot be undone" (`gap-global-reform-max.md` L1040), and Lemma REM there (a colour twist of pinned data is removable unless a pinned path carries it). Nearest items on file, credited: the transverse-lattice gauge fixing of row 1016 4.4 (after Bardeen, Pearson and Rabinovici 1980), judged FAILS (Elitzur) at finite in-plane coupling; the pinned sheet of Theorem D2 (row 977) and the slab device K3' (row 1013), both used as negative devices. The difference: here the in-plane plaquettes are frozen by the coupling, the model stays in the anisotropic Wilson family, and the posted two-dimensional gap theorems are used as a positive input.

**Setting.** Lattice Z^2 x Z^2 with points (u, x); u is longitudinal (directions 0, 1), x is transverse (directions 2, 3). Three plaquette types: L in the (0,1) planes, T in the (2,3) planes, M mixed. Anisotropic Wilson weight exp(sum_p beta_type(p) x_p), x_p = (1/2) tr U_p, couplings (beta_L, beta_M, beta_T). The isotropic model is (beta, beta, beta).

**The face model M(beta_M, beta_T).** Variables Phi_l(u) in SU(2) for each transverse link l = (x, y) and each longitudinal site u. Weight
  exp( beta_M sum_l sum_<u u'> (1/2) tr(Phi_l(u) Phi_l(u')^(-1)) + beta_T sum_u sum_p (1/2) tr G_p(u) ),
G_p(u) the product of the four Phi around the transverse plaquette p at u. The group G = SU(2)^(transverse sites) acts by (g Phi)_l(u) = g_x Phi_l(u) g_y^(-1), with g independent of u.

**Exact statements (proofs in step 6).**
- Lemma FACE-LIM: on boxes with free boundary, the limit beta_L to infinity of the anisotropic Wilson measure, on gauge-invariant functions, is M(beta_M, beta_T) on G-invariant functions.
- Lemma ANCH: M(beta_M, 0) is a product over transverse links of two-dimensional O(4) models with coupling beta_M.
- Lemma RIG: in M, a twist by a field g_x(u) costs a Dirichlet form in u only, for every beta_T and every G-invariant on-site term.
- Targets, OPEN: (FACE-CH) exponential decay of every G-charged correlation in M, uniform in beta_T and in the transverse size; (FACE-SG) exponential clustering of G-invariant local observables in M(beta, beta_T), 0 <= beta_T <= beta; (BR-L) a lower bound for the clustering rate of (beta_L, beta, beta), uniform in beta_L in [beta, infinity].

**Consumer chain to the gap.** (FACE-CH) and (FACE-SG) give a gap at (infinity, beta, beta). (BR-L) carries it to (beta, beta, beta), which is T_JW-lat of row 1052 at one coupling. The account then carries one reference coupling to finer cutoffs (the lane's carry, row 978; conditional).

**What it changes.** The lane's route (ii) needs (N1) a frame on typical pins, (N2) the cancellation of the mass-like term, (N3) the gain, and (L3) decay of all observables from a small response (`gap-direction3-max.md` L104-111, L203-204). On the face (N1) and (N2) hold exactly for twists in G (Lemma RIG), so (N3) can be decided there for those twists. **Corrected in step 4:** this covers the G-charged sector only. A twist of the transverse flux still needs a frame in the transverse planes, so (N1) stays for the singlet sector, and (L3) is not reached. What is new to prove moves to (FACE-SG) and (BR-L).

**Cheapest kill tests.** (a) For the route: (BR-L) contains the target at one coupling, so the route is stronger than the target unless a mechanism for unfreezing is named. (b) For the testbed: a counter-model on the face with G-charged decay and no singlet gap (step 6 gives the scope of this). (c) Compact U(1) on the face must be massless at large beta (Gaussian computation, step 6).

#### 3.3 Vector V2 (NEW): a parametric seed near the anchor, and an anisotropic trajectory

**Statement.** There is eps > 0 such that the anisotropic model has exponential clustering in the region R = { beta_T xi_2(beta_M)^2 <= eps, beta_L >= xi_2(beta_M)^2/eps }, xi_2 the correlation length of the two-dimensional O(4) model. **Consumer:** a continuum limit taken inside R. **Source:** f1, c11, b10, b13. **Change:** the seed is parametric (a convergent expansion about Lemma ANCH), with beta_M as large as wanted. **Kill test:** does a Lorentz-invariant trajectory stay in R? (Step 4: no.)

#### 3.4 Vector V3 (NEW): frozen two-skeleton arrays

**Statement.** Take isotropic Wilson and freeze to 1 every plaquette that lies in the two-skeleton of the coarse lattice s Z^4. The frozen skeleton is simply connected, so one rigid SU(2) acts on it and twists along it cost a gradient only. Target: a clustering rate for this model, uniform in s and in the cutoff; with uniqueness of the infinite-volume Gibbs state it gives T_JW-lat as s grows. **Source:** b2, b13, S1. **Change:** the regularisation carries rigid frames on a set of measure zero. **Kill test:** is the charged decay along one frozen plane selective, and does the bulk step need the one-box estimate? (Step 4.)

#### 3.5 Vector V4 (NEW framing): fix the infrared measure first

**Statement.** Choose a coarse measure mu_0 in the cluster-expansion domain and refine it to a projective family whose fine members are asymptotically free; the gap of blocked observables is then built in. **Source:** c1, c3, b13. **Kill test:** is mu_0 a free choice? (Step 4: no.) Grep: "renormalized trajectory", "perfect action", "inverse RG": 0 files.

#### 3.6 Vector V5 (NEW as a test for T_JW-lat): the torus normaliser

**Statement.** N(T) = Pin(2), the normaliser of the maximal torus of SU(2), is a non-commutative, infinite, compact subgroup with abelian Lie algebra. Its frozen lattice gauge theory is the model of a massless branch of pure SU(2) by abelian dominance. Claim to test: it has no gap on Z^4 at large coupling, so it binds tools for T_JW-lat. **Source:** e1, d2, row 1052 6c (which removed Q_8 and 2T as tests of T_JW-lat). **On file:** one mention, row 859 idea 12 ("U(1), Pin(2) and every finite group are amenable", `gap-brainstorm-max.md` L291); BD_n in Lemma F4 of row 838. Not on file as a test model for T_JW-lat. **Consumer:** the test table, not a proof.

Next: step 4, the kill pass.

### Step 4 result: the kill pass (task 3)

Tests in the exact form of the lane's kill sheet, `library/gap-invent-selective-max.md` L52-63 (K1 Lemma PT, K2 Proposition NP, K3 Theorem D2, K3' slab device, K4 Lemma SHEET, K5 compact U(1), K6 frozen Q_8 and 2T, K7 five dimensions, K8 refilling, K9 the spec check S0-S4), with Lemma CEN+ and Lemma WN of rows 1016 and 1013. Valid form: a model refutes a claim only if the hypothesis holds there and the conclusion fails. A pass is no support.

#### 4.1 V1, the flat-plane face

| Test | Result for V1 |
|---|---|
| K5 compact U(1) | Lemma RIG holds for every compact group. The commutator gain behind (FACE-CH) vanishes for an abelian group, as K5 requires. (FACE-SG) is false for U(1) at large coupling at the Gaussian level (step 6, ARGUED). Pass, as a constraint. |
| K6 frozen Q_8, 2T; and V5 Pin(2) | The twist uses infinitesimal rotations. For a finite group Lemma RIG is void. For Pin(2) the Lie algebra is abelian and the gain vanishes. Pass. |
| K7 five dimensions | (FACE-CH) is a statement on two-dimensional planes. It holds verbatim in a 2+3 split. So it is blind to the dimension and cannot be the gap. The dimension must enter (FACE-SG): the stiffness of a block of b^(d_perp) sheets scales like b^(d_perp - 2), marginal only for d_perp = 2 (ARGUED). |
| K3, K3' pinned sets | (FACE-CH) is uniform over pins on the boundary of a cell in u. Such pins cut out systems that are at most two-dimensional in u, so no ordered three-dimensional sheet arises. Pins on transverse link sets are not in the class. Pass in this restricted form. |
| K4 SHEET, fixed-b form | (FACE-CH) may be uniform over transverse plaquette strengths in [0, b], because every cut-out system keeps the rigid group. (FACE-SG) must not be claimed uniformly over coupling fields; it is stated for constant beta_T only. |
| K1 product | The product of the SU(2) face with a compact U(1) face has G-charged decay of the SU(2) factor and no singlet gap. So "(FACE-CH) gives (FACE-SG)" FAILS as a soft implication. (FACE-SG) must read the whole state space. |
| K2 | No induction on D. Not engaged. |
| K8 | Twists are rigid rotations, no refilling. Not engaged. |
| Lemma CEN+, Lemma REM | No conflict. G is a group of gauge transformations, as CEN+ says every rigid map must be. The twist is honest because flatness pins every path in a plane (the exception in Lemma REM). |
| Lemma WN | No conflict. The fixed cost per site of a lab-frame move comes from non-flat in-plane links. On the face there are none. |
| S0 (renaming) | **FAIL for the route.** (BR-L) contains T_JW-lat at coupling beta. In the weaker form "(BR-L'): a gap on the face gives a gap at every beta_L >= beta" there is no mechanism and no refutation. |
| S1-S4 | S1 yes (commutators). S2: a rate only for the charged sector. S3: only through (FACE-SG), open. S4: (FACE-SG) is not uniform over fields. |

**Correction to step 3.2 (made in place there).** I wrote that on the face (N1) and (N2) hold exactly, so (N3) and (L3) could be decided there. That is true only for twists in G. The singlet sector is moved by flux twists. A flux twist with a slowly varying angle needs its colour axis to be covariantly constant on a three-dimensional set (the side of the Dirac volume): along the planes, which the face gives, and along a transverse path, which it does not (the mixed plaquettes on that side are not flat). So (N1) stays, in transverse form.

**Why more freezing does not help (ARGUED, a dimension count).** Freeze the plaquettes inside a family of parallel k-dimensional flats and gauge the links inside to 1. A rigid SU(2) then acts on each flat, and a twist field lives on a k-dimensional set with a Dirichlet cost. The capacity gives disorder only for k <= 2. For k = 3 the links that leave the flats form three-dimensional O(4) layers, which order at large coupling (the slab device K3' of row 1013; Frohlich, Simon and Spencer 1976, recalled). A flux twist needs k = 3. So freezing flats gives honest twists exactly where they do not carry flux. Scope: this is an argument about this one device, not a theorem.

**Verdict on V1.** As a route to the gap: FAILS (S0 at (BR-L); (FACE-SG) keeps the frame problem in transverse form). What survives: (i) Lemma ANCH and its corollary, a positive control with a posted theorem behind it; (ii) Lemma RIG and Lemma FACE-MW, proved by hand in step 6; (iii) the target (FACE-CH), a selective statement at weak coupling in a four-dimensional SU(2) model, which would decide (N3) for gauge-frame twists.

#### 4.2 V2, the parametric seed near the anchor

Kill test: a Lorentz-invariant anisotropic trajectory has couplings (xi^2 beta, beta, beta/xi^2) at leading order, xi = a_perp/a_long. The sheets then have two-dimensional coupling g(a_perp) at the scale a_perp, so xi_2 = xi exp(4 pi/g(a_perp)^2) in units of a_long (one loop; step 6.6). The transverse plaquette strength per site is (4/g^2) xi^(-2). So beta_T xi_2^2 = (4/g(a_perp)^2) exp(8 pi/g(a_perp)^2). This is small only if g(a_perp)^2 is large. Inside R the transverse spacing stays above the physical correlation length, and the limit keeps a transverse cutoff. To remove it the trajectory must leave R and cross the band in a_perp. **FAILS (S0: it renames the band).** ARGUED, one-loop numbers recalled. K7: the region R exists in a 2+3 split as well, which is consistent, since R is not near the isotropic continuum limit. What survives: the anchor region as a positive control (not proved here; it needs a convergent expansion about Lemma ANCH).

#### 4.3 V3, frozen two-skeleton arrays

(a) The charged decay along a frozen face is blind. A link that leaves a frozen face has its other end in the unfrozen bulk. Its correlation along the face is a Wilson loop of width 1 with one long side on the face, and that decays exponentially by the perimeter law for compact U(1) too (ARGUED; the standard weak-coupling perimeter law). (b) The bulk step, a clustering rate across a coarse cell of side s uniform in s, is the one-box estimate at scale s. The identification with the state without defects needs uniqueness of the Gibbs state, which is open. **FAILS (S0).**

#### 4.4 V4, the infrared measure first

The coarse measure is not a free choice. The fine members must be asymptotically free, and the irrelevant directions contract under blocking, so the projective family is one orbit of the scale group (ARGUED; it is the uniqueness of the account's limit along its trajectory). "mu_0 lies in the cluster-expansion domain" is then (EXIT) of row 838 items 21-26, or the absence of a critical element in Theorem CR (row 1017). **FAILS (S0).**

#### 4.5 V5, the torus normaliser

Not a route. As a test it is belief-grade: on Z^4 at large coupling the component field of Pin(2) is flat up to rare vortex sheets, and the rest is compact U(1) at the same coupling, read through even observables (Lemma EVEN, step 6.7). The Gaussian value of an even correlation is a power law. No theorem is cited for even observables. **Survives as a GUIDE-grade test**, with the consequence in step 6.7.

#### 4.6 Ideas tried in this run and dropped before they became vectors (so they are not redone)

- A Durhuus-Frohlich comparison with two-dimensional sheets as layers. FAILS: for beta_T > 0 the transverse plaquettes act on a sheet as an external field, so the conditional two-point function does not tend to zero; and the lane's warning G8 (`gap-brainstorm2-max.md` L263) applies.
- Localising the space-time rotation group SO(4). FAILS: the cost of an elastic twist is extensive in lattice volume (it moves every ultraviolet mode); there is no dimensionless stiffness.
- A chessboard estimate in the transverse directions to reduce to a two-dimensional model. FAILS: the chessboard norm of an observable is again a four-dimensional expectation.
- A Hamiltonian with an exactly known ground state (the Fokker-Planck operator of a three-dimensional lattice measure). FAILS as a regularisation of the target: at weak coupling its long-distance theory is the Langevin dynamics of three-dimensional Yang-Mills (ARGUED by power counting: the extra two-plaquette term dominates for momenta above g^2/a).
- Dielectric (linear quaternion) links after Mack. No selective statement: the radial mode is a mean of thin Wilson loops and is ultraviolet-dominated.
- The thermal form of the gap (pressure below T^4 at low temperature). FOUND: the Casimir forms (BDD-Delta), (GS-CAS).

Next: step 5 (ranking), then step 6 (hand proofs).

### Step 5 result: ranking (task 4)

No vector passes the wall as a route. V2, V3, V4 FAIL at S0. V1 FAILS as a route and leaves three pieces. V5 is a test. Ranked by what each surviving piece would change, divided by the cost to find out:

| Rank | Piece | What it would change | Cost to find out | Kind |
|---|---|---|---|---|
| 1 | V1 (ii)-(iii): Lemma RIG, Lemma FACE-MW (proved in step 6) and the target (FACE-TW) | It decides whether the commutator gain of OpenAI's annulus estimate works in a four-dimensional SU(2) model once frames are given. It cannot give the gap: it reaches the G-charged sector only (step 4.1). | One proof row: port of about eight pages (Lemma 2.1 to Proposition 3.1 of the OpenAI O(n) text, as row 1007 reads it). | (K-one), blind half proved, selective half a port |
| 2 | V5: Pin(2) as a test for T_JW-lat | It restores the content of K6 for tools aimed at T_JW-lat, after row 1052 removed Q_8 and 2T there. | A lead edit of the test table, after a check of step 6.7. | test, GUIDE grade |
| 3 | V1 (i): Lemma ANCH with the posted theorem | A positive control: a member of the anisotropic SU(2) Wilson family with a gap at arbitrarily large mixed coupling, selective at the level of theorems. No consumer in a chain to (W). | Nothing more for the exact point; a full row for a neighbourhood. | positive control |

The honest reading of the ranking: rank 1 is cheap, and its outcome would be a two-dimensional theorem placed in a four-dimensional model. It would not move (W) or T_JW-lat. I do not recommend it ahead of the lane's held lines unless the lead wants (N3) decided apart from (N1) and (N2).

Next: step 6, the hand proofs behind these verdicts.

### Step 6 result: hand work on V1 and V5 (task 5)

Rule 0a before the attempt. `library/open-core.md` has no line for the face model, for a frozen plaquette orientation or for Pin(2) (grep "anisotrop", "flat plane", "Pin", "normaliser": no hit on these objects). FINISH rows: the nearest are row 1016 (4.4, transverse-lattice gauge fixing, FAILS at finite in-plane coupling), row 977 (Theorem D2, pinned sheet) and row 1051 (running; it ports the annulus engine to the pin space of a cell of the isotropic model, in a section I cannot see at this pin). The objects below are in a different model (beta_L = infinity), so I proceed, and I name the overlap risk with row 1051 in step 8.

Conventions. SU(2) as unit quaternions; x_p = (1/2) tr. For a unit vector a-hat, a = (i/2) a-hat . sigma and e^(ta) = cos(t/2) + i sin(t/2) a-hat . sigma, a rotation by the angle t. For W = w_0 + i w . sigma: (1/2) tr(W e^(ta)) = w_0 cos(t/2) - (w . a-hat) sin(t/2).

#### 6.1 Lemma FACE-LIM (PROVED; a standard axial-gauge argument)

**Statement.** Let Lambda = Lambda_long x Lambda_perp be a product of two rectangles with free boundary. Let F be a continuous gauge-invariant function. Then the expectation of F in the anisotropic Wilson measure with couplings (beta_L, beta_M, beta_T) tends, as beta_L tends to infinity, to the expectation in M(beta_M, beta_T) of the restriction of F to the configurations with all longitudinal links equal to 1.

**Proof.** In each plane {x} x Lambda_long take the comb tree: all links of direction 0, and the links of direction 1 on the row u_0 = 0. Gauge transformations at the sites of the plane set the tree links to 1 (Haar measure is kept; F is unchanged). Let V(u) be the direction-1 link at u; V = 1 on the row u_0 = 0. The (0,1) plaquette with lower left corner u is then V(u + e_0) V(u)^(-1) up to orientation. So the longitudinal factor of the weight is a product over rows of chains with step weight w(V(u + e_0) V(u)^(-1)), w = exp(beta_L x). The normalised step weight tends weakly to the point mass at 1. The other factor, exp(beta_M sum + beta_T sum), is a bounded continuous function of all links. So the measure converges weakly to the measure with V = 1 and density exp(beta_M sum + beta_T sum) in the transverse links. With all longitudinal links 1, a mixed plaquette is (1/2) tr(Phi_l(u) Phi_l(u')^(-1)). The gauge transformations that keep all longitudinal links at 1 are the g_x that do not depend on u. QED

#### 6.2 Lemma ANCH and what the posted theorems give at the anchor

**Lemma ANCH (PROVED).** M(beta_M, 0) is the product, over the transverse links l, of the measures with density exp(beta_M sum_<u u'> s(u) . s(u')) on maps s from Lambda_long to S^3, where Phi_l = s_0 + i s . sigma.
Proof. (1/2) tr(Phi Phi'^(-1)) = s . s' for unit quaternions, Haar measure is the uniform measure on S^3, and at beta_T = 0 no term couples two links. QED

**Corollary ANCH-W (PROVED given ANCH).** At the anchor, the mixed-plane Wilson loop with longitudinal side R and transverse side T has expectation G(R)^T, G(R) = E[s(0) . s(R)] of one O(4) model. A loop in a transverse plane has expectation 0. Proof: for one sheet, E[Phi(0) Phi(R)^(-1)] commutes with the left action, so it is G(R) times the identity; the T sheets are independent; a transverse loop contains some sheet once and E[Phi] = 0. QED

**What the posted theorems add (GIVEN, unrefereed, read by the lane only).** OpenAI, "Exponential decay in two-dimensional classical O(n) models" (Theorem 1.1 as row 1007 reads it, n = 4): G(R) <= A e^(-mR) with free boundary, uniformly in subgraphs and strengths. So the mixed-plane loops obey an area law with tension at least m, for every beta_M. For clustering of every local observable at the anchor one needs the mixing bound of OpenAI's O(4) text (rows 1009, 1010, reading only) or an equivalent; the O(n) text itself disclaims it (row 1007 B(1)).

**Selectivity at the anchor (theorem-grade inputs, all recalled through the lane's reads).** Compact U(1): the anchor is a product of plane-rotator models; at large coupling the two-point function has no exponential upper bound (Frohlich and Spencer 1981, as cited by OpenAI, row 1007 B(3)). Finite subgroups: the sheets are two-dimensional models with a finite symmetry group; at large coupling they order (Peierls). SU(2): exponential decay at every coupling (GIVEN above). So the anchor separates SU(2) from U(1) and from finite groups by theorems. Credit: the 2D theorems are OpenAI's and Ding, Huang and Yang's; the transverse-lattice picture is Bardeen, Pearson and Rabinovici's.

**Remark (which split is selective; ARGUED from cited facts).** Freeze the plaquettes inside parallel k-dimensional flats and switch off the plaquettes transverse to them. k = 1 (nothing to freeze; spatial plaquettes off): one-dimensional chains, gapped for every compact group (FOUND: row 859, "anisotropic action from beta_s = 0"). k = 3: three-dimensional O(4) layers, ordered at large coupling for U(1) and SU(2) alike (FOUND: slab device K3'). k = 2 is the only split where the group decides. This is Migdal's correspondence between gauge fields in dimension 4 and spin models in dimension 2, exact at one point.

#### 6.3 Lemma RIG (PROVED): on the face a twist in G costs a Dirichlet form in u only

**Setting.** A finite set C of longitudinal sites, its neighbour set dC, a finite Lambda_perp. The pin omega fixes Phi_l(u) for u in dC and all l. Z_C(omega) is the integral over Phi_l(u), u in C, of exp(S), where S contains the bonds <u u'> with at least one end in C and the on-site terms at u in C. The on-site terms may be any functions that are invariant under g_x at each u (the Wilson term beta_T sum_p x_p is one).
For a transverse site x, a unit vector a-hat and a real function theta on C and dC, let tau_theta rotate the links at x: Phi_l(u) to e^(theta(u) a) Phi_l(u) if l starts at x, and Phi_l(u) to Phi_l(u) e^(-theta(u) a) if l ends at x.

**Statement.** Z_C(tau_theta omega) Z_C(tau_(-theta) omega) >= exp(- beta_M D(theta)) Z_C(omega)^2, with D(theta) = sum over the bonds <u u'> that meet C of (theta(u) - theta(u'))^2.

**Proof.** tau_theta at fixed u is the gauge transformation e^(theta(u) a) at x, so every on-site term is unchanged. For a link l that starts at x and a bond <u u'>, by cyclicity of the trace, (1/2) tr(e^(theta(u) a) Phi_l(u) Phi_l(u')^(-1) e^(-theta(u') a)) = (1/2) tr(W e^(delta a)), W = Phi_l(u) Phi_l(u')^(-1), delta = theta(u) - theta(u'). For a link that ends at x the bond term is (1/2) tr(W' e^(-delta a)) with W' = Phi_l(u')^(-1) Phi_l(u), the same form. By the convention above the sum of the values at delta and - delta is 2 w_0 cos(delta/2). So
  (1/2)(S o tau_theta + S o tau_(-theta)) - S = - beta_M sum over the links at x and the bonds of w_0 (1 - cos(delta/2)) >= - (beta_M/8) sum delta^2 >= - (beta_M/2) D(theta),
because abs(w_0) <= 1, 1 - cos y <= y^2/2, and at most four links meet x. The interior change of variables Phi to tau_theta Phi keeps the Haar measure. By the Cauchy-Schwarz inequality,
  Z_C(tau_theta omega) Z_C(tau_(-theta) omega) >= ( integral of exp((S o tau_theta + S o tau_(-theta))/2) )^2 >= exp(- beta_M D(theta)) Z_C(omega)^2. QED

**Scope.** Every compact Lie group, every beta_T >= 0, every transverse size, every pin. No mass-like term appears. In the isotropic model the same move, with the in-plane links held, has the fixed cost per site of Lemma WN (row 1013); with the in-plane links moved too it is a gauge transformation and costs nothing. The face is the case where the in-plane links are held at 1 by the model itself.

#### 6.4 Lemma FACE-MW (PROVED): the frame is forgotten at a logarithmic rate (the blind half)

**Statement.** Let B_r and B_R be the boxes abs(u)_inf <= r and <= R, R >= e r, with any pin omega outside B_R. Let f be a bounded function of the configuration in B_r with values in R^3 that turns as a vector under the constant rotations in G_x (for example the vector part of a transverse plaquette holonomy based at x). Then every component of E[f] in M on B_R with pin omega is at most 12 pi^2 beta_M sup abs(f) / log(R/r) in absolute value. If instead f changes sign under the rotation by 2 pi (centre-odd at x), then abs(E[f]) <= 48 pi^2 beta_M sup abs(f) / log(R/r).

**Proof.** Let p be the density of the configuration zeta in B_r. Then p(g zeta)/p(zeta) = W(g zeta, omega)/W(zeta, omega) for a constant g in G_x, where W is the partition function of the annulus between the layer abs(u) = r and the pin (the weight inside B_r is invariant under constant g). Apply Lemma RIG to the annulus with theta = t on B_r and theta(u) = t log(R/abs(u)_inf)/log(R/r) in between. Only bonds between consecutive square shells contribute; shell k has at most 8k + 4 such bonds, each with difference at most t/(k log(R/r)). So D(theta) <= (12 t^2/log^2(R/r)) sum_(k=r)^(R-1) 1/k <= 12 t^2 (1 + log(R/r))/log^2(R/r) <= 24 t^2/log(R/r). Hence p(e^(ta) zeta) p(e^(-ta) zeta) >= e^(-eps) p(zeta)^2 with eps = 24 beta_M t^2/log(R/r). By the inequality between the arithmetic and the geometric mean, q = (1/2)(p o e^(ta) + p o e^(-ta)) >= e^(-eps/2) p. Both are probability densities, so the integral of (p - q)_+ is at most 1 - e^(-eps/2) <= eps/2, and abs(E[(1/2)(f o e^(ta) + f o e^(-ta))] - E[f]) <= eps sup abs(f). For a vector f and t = pi the average is the reflection (2 a-hat a-hat^T - 1) f, so the left side is twice the part of E[f] orthogonal to a-hat. Take a-hat orthogonal to the chosen component. For a centre-odd f take t = 2 pi: the average is - f. QED

**Reading.** At beta_L = infinity gauge-variant quantities are physical, and Elitzur's theorem is replaced by the Mermin-Wagner estimate. The method is Dobrushin and Shlosman's, McBryan and Spencer's and Pfister's. It holds for compact U(1) as well, so it is blind.

#### 6.5 The selective half on the face: the target (FACE-TW), and what it gives (PROVED as an implication)

**(FACE-TW), OPEN (a port).** For every beta_M there are C and N_0 such that, for every N >= N_0, every beta_T >= 0 (every G-invariant on-site term), every finite Lambda_perp, every x, every pair of pins (eta, eta') on the two boundary layers of the annulus D_N = {N <= abs(u)_inf <= 2N}, and every constant g in G_x:
  W_N(eta, g eta') >= (1 - C/log N) W_N(eta, eta').
Source: Proposition 3.1 of OpenAI's O(n) text, as row 1007 B(2) reads it (steps 1 to 5: an auxiliary edge field for the rotation group, the gradient estimates of Lemma 2.1, the identity W(dF) = W(B) with B the commutator field, the fourth-order inequality of Proposition 2.2, plane waves on frequency shells). Why a port is plausible (ARGUED; I did not read the OpenAI text, only the lane's digest): those steps use the exact rigid invariance and the bond structure in u, which Lemma RIG gives on the face with beta replaced by 4 beta_M; the digest states that Proposition 2.2 does not depend on the fixed spins. Two points the port must check: the digest states Proposition 3.1 for constant pins only, and (FACE-TW) needs arbitrary pins; and the on-site terms must drop out of every derivative used (they do in Lemma RIG, because each tau_theta is a gauge transformation at fixed u).

**Proposition ITER (PROVED): (FACE-TW) gives decay of G-charged expectations faster than every power.** Let N_j = 2^j N_0, let (FACE-TW) hold at the scales N_j with eps_j = C/log N_j < 1. Let f be a bounded function of the configuration in B_(N_(j_0)) whose average over the constant rotations in G_x is zero. Then for every pin omega outside B_(N_J): abs(E[f]) <= sup abs(f) prod_(j = j_0)^(J-1) eps_j.
Proof. Let eta_j be the configuration on the layer abs(u)_inf = N_j. The model is Markov in u, so (eta_J, ..., eta_(j_0)) is a Markov chain with kernels K_j(eta_(j+1), d eta_j), whose density is proportional to Z_in(eta_j) W_(N_j)(eta_j, eta_(j+1)). Z_in is invariant under a constant g. So by (FACE-TW) the image of K_j(eta_(j+1), .) under every g is at least (1 - eps_j) K_j(eta_(j+1), .). Averaging over g: K_j >= (1 - eps_j) Kbar_j, with Kbar_j the G_x-average of K_j. Hence K_j = (1 - eps_j) Kbar_j + eps_j R_j with a probability kernel R_j. Put F_j(eta_j) = E[f given eta_j]. For every j the average of F_j(g eta_j) over g is E[average of f o g given eta_j] = 0. So the integral of F_j against the invariant kernel Kbar_j vanishes, F_(j+1) = eps_j R_j F_j, and sup abs(F_(j+1)) <= eps_j sup abs(F_j). QED
With eps_j = C/(j log 2 + log N_0) the product is exp(- (1 + o(1)) J log J): faster than every power of N_J. For compact U(1) the Gaussian value of a charged correlation on the face is a power (6.6), so (FACE-TW) fails there, as it must.

**What (FACE-TW) would and would not be.** It would be the first selective statement at weak coupling in a four-dimensional SU(2) lattice model on file: the correlation of the vector part of a transverse plaquette holonomy at two points of the same plane (the gluon field strength, transported trivially along the flat plane) decays faster than every power, for every beta_M and beta_T. It is still a two-dimensional theorem (a model with rigid symmetry and an invariant on-site term). It gives nothing for G-invariant observables: step 4.1, K1. The step from here to an exponential rate in the O(n) text uses sign clusters and the inequalities of Ginibre and FKG (row 1007 B(2) steps 6 to 9); the transverse plaquette term is not a ferromagnetic pair interaction in the embedded Ising variables, so that part does not port for beta_T > 0 (ARGUED).

#### 6.6 Checks by hand at the Gaussian level (ARGUED; they guide, they prove nothing about the compact models)

- **Compact U(1) on the face.** Angles theta_i(u, x), i = 2, 3. Quadratic action (beta_M/2) sum (d_u theta_i)^2 + (beta_T/2) sum (d_2 theta_3 - d_3 theta_2)^2. In Fourier variables (p for u, q for x) the form is beta_M p^2 on the gradient direction q and beta_M p^2 + beta_T q^2 on the curl direction. The curl field B is G-invariant and local, and its correlation at equal x has the transform integral d^2q q^2/(beta_M p^2 + beta_T q^2), which contains p^2 log p^2. So the correlation decays like abs(u)^(-4): no singlet gap. The charged correlation exp(i(theta_i(u) - theta_i(0))) has exponent 1/(4 pi beta_M) from the gradient modes: a power law.
- **The estimate behind 4.2.** One loop, recalled: d(1/g^2)/d log mu is 11 N/(24 pi^2) in four dimensions and N/(8 pi) for the chiral field with action (1/g^2) tr abs(d Phi)^2; for N = 2 these are 0.0929 and 0.0796, ratio 3 pi/11. At equal lattice coupling the scales are exp(2.69 beta) (four dimensions) and exp(pi beta) (decoupled sheets). A sheet seen at the two-dimensional scale a_perp has coupling g(a_perp), hence xi_2 = (a_perp/a_long) exp(4 pi/g(a_perp)^2), which gives the formula of 4.2.
- **The dimension count behind 4.1.** Under blocking of the transverse directions only, by b, the leading-order couplings go to (b^2 beta_L, beta_M b^(d_perp - 2), beta_T/b^2). For d_perp = 2 the mixed coupling is marginal and the flow goes toward the anchor corner; its last steps are at strong coupling at the transverse scale, which is the band again. For d_perp = 3 the mixed coupling grows.

#### 6.7 V5: Lemma EVEN and the Pin(2) test (PROVED for the lemma; the test is belief-grade)

**Lemma EVEN (PROVED).** Let T be the diagonal torus of SU(2) and j = i sigma_2. Every gauge-invariant function, restricted to configurations with all links in T, is invariant under U_l to U_l^(-1) on all links at once.
Proof. j t j^(-1) = t^(-1) for t in T. The constant gauge transformation by j maps a T-valued configuration to the configuration of the inverses. QED

**Consequence (ARGUED).** If pure SU(2) had a massless branch carried by an abelian field in the sense of abelian dominance, no gauge-invariant local observable would be odd in that field; the branch would show only in even correlations (two-photon exchange, a power law with twice the exponent). The matching comparison model is the frozen Pin(2) theory, not compact U(1): its gauge-invariant functions on the identity component are exactly the even ones. On Z^4 at large coupling its component field is flat up to rare closed sheets, the rest is compact U(1), and the Gaussian value of an even correlation, for example of x_p = cos theta_p, is 2 (the photon propagator of the field strength)^2, a power abs(x)^(-8). So the frozen Pin(2) theory is expected to have no gap on Z^4. No theorem is cited for even observables of compact U(1); this is a belief.

**What it changes.** Row 1052 6c found that frozen Q_8 and 2T do not test tools aimed at T_JW-lat. The requirement that those tests carried, K6 ("the selective identity must use the Lie algebra, not only that the group is non-commutative"), stays in force for T_JW-lat on the authority of Pin(2), in a sharper form: the identity must use non-commuting infinitesimal rotations. Pin(2) is non-commutative, infinite and has a Lie algebra; it fails only that. On file before: one line (row 859 idea 12 lists Pin(2) among amenable groups). Not on file: Pin(2) as a test model.

#### 6.8 Remark: the doubly flat corner (ARGUED; not used)

At beta_L = beta_T = infinity on a simply connected lattice the transverse links are h(u, x) h(u, y)^(-1), and the model is the site model with weight exp(beta sum over mixed plaquettes of (1/2) tr(h_1 h_2^(-1) h_3 h_4^(-1))). The twists in G act transitively on its pins, so a full port of the two-dimensional mixing argument would give clustering of every observable along u, and by the symmetry between the two pairs of directions along x as well. Its U(1) version has the Gaussian propagator 1/(p^2 q^2) and is massless. It carries no flux in the frozen planes, and it is not Lorentz invariant in any limit; I record it only as the third corner of the square of couplings (beta_L, beta_T) at which a theorem looks reachable.

#### 6.9 What failed, and what is left

- Failed: every attempt to reach the G-invariant (singlet) sector on the face from the rigid symmetry. Reason: singlets are moved by flux twists, and a flux twist needs a frame on a three-dimensional set (4.1). The product test K1 shows that no soft step from charged decay to a singlet gap exists.
- Failed: a bridge from the face to the isotropic model. (BR-L) contains the target at one coupling; (BR-L') has no mechanism.
- Left, as exact statements: (FACE-TW) (a port); (FACE-SG) (the wall, with the frame problem in transverse form); (BR-L').
- Exact point where I stopped: after Proposition ITER. I did not read OpenAI's text, so (FACE-TW) is OPEN, not ARGUED.
