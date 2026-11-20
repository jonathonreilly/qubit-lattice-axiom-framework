lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-20T21:31Z

# gap-mini-solve-ab-opus: SU(2) Yang-Mills mass gap (Jaffe-Witten), Mac mini worker 2

Queue row 1248 of FINISH.md. Started 2026-11-20T09:31Z (date -u). Pinned at commit 59f6d02b0 on branch claude/ym4d-hard-route.

Status labels: PROVED, ARGUED, GUIDE, OPEN, as the row asks. A numeric run may guide but is never a proof step.


## Step 0. Reading log (reading only; no new claim; written 09:33Z by date -u)

Read at the pin 59f6d02b0: GOAL.md in full; FINISH.md L1-90 and L299-352; rows 1218, 1228-1251 (RESULT lines);
`parts/gap.md` L1-110 (formulation, wall, methods 1-36, lead rules); `library/prior/gap-onebound-read-sol.md`
(row 1218) in full; the sibling file `library/gap-mini-solve-aa-opus.md` Steps 0-1 (row 1244, running);
(N-phys) as stated in `library/gap-mini-branch-fable.md` L304-310.

Where the problem stands on file (cited, not re-derived):

1. Beside the premises of the Sussman-Alpoge complete account, the gap clause reads one lattice estimate,
   (N-phys) (row 1179 Theorem BP; row 1225). Modulo the ultraviolet carry (UNIV-K), the crux is a finite seed
   for Wilson SU(2) at one coupling where the running coupling is of order one (rows 1225, 1229, 1233, 1238).
2. About 45 engine families are screened with named failing steps (methods 1-36 of `parts/gap.md`; rows 1189,
   1194, 1199, 1200, 1229, 1237, 1244 Step 1.3). The missing object since row 1013 is a band-crossing step
   with a non-abelian sign at order-one response ((K-flow)), or a property of the measure at one scale in the
   band ((K-one)), which needs a number no hand expansion reaches (row 1229).
3. Row 1218's published inputs: A (Bhattacharjee, Bhattacharya, Lockwood, Romanov, Sessford, Singha Roy) gives
   a full-thermal one-scale seed (A-B*) with a proved conditional ascent (Theorem 7.56); B (the first four
   authors) gives cube-dynamics criteria (BP, BP_0, B-local, B-D) and Corollary 166, BP(n,1/2) for the
   straight-path block law of SU(2) Wilson at beta_W <= k+2 with b = 2^k, by convolution damping; C (Zeng
   Chunping) gives common-rate criteria and a conditional tunneling route. None proves the Wilson estimate at
   weak coupling.
4. Siblings on the same brief at this pin: rows 1243 (z: (S-V)), 1244 (aa: where the one-loop decrement sits in
   the stiffness split of row 1018), 1246 (astra), 1249, 1251 (queued). This row keeps its item distinct.

## Step 1. How best to attack it (judgement, ARGUED; written 09:56Z by date -u)

**1.1 The two open inputs (cited).** Beside the T0 chain, the gap clause reads (N-phys) (rows 1179, 1225). By
(ONE-K) (row 916, checked 917), (N-phys) follows from (A) the ultraviolet carry (UNIV-K) and (B) a seed at one
cutoff's window, i.e. a lattice gap with a thermal count for Wilson SU(2) at one coupling where the running coupling
is of order one (rows 1225, 1229, 1238 Step 1.1).

**1.2 Part (B): my own screening, grepped before any work (rule 0a).** I looked for an input with a definite
non-abelian sign at every coupling that fails for U(1), frozen groups and products with a massless factor. Each idea
I could name is on file, or dies at once for a reason I can state. Counts are files under `library/` and `parts/`.

| Idea | Status |
|---|---|
| Schrodinger-functional coupling as the 4D stiffness (scale-invariant boundary flux, runs at one loop, zero running for U(1)) | on file (20 files name the Schrodinger functional, 37 step scaling); it is the twist class of rows 1011-1018, 1228; its closure under conditioning holds only for typical sub-cell data, which is the (K-flow) step of rows 1243 (S-V) and 1244 (stiffness split) |
| Rigid group on integrated variables via the residual global colour symmetry of a complete gauge (tree, Landau, axial) | dies: a relative colour rotation of a region is a gauge transformation followed by a reset of the tree links that cross its boundary, i.e. a local insertion on those links, or nothing (axial case); this is CEN+ (row 1016) and row 1238's table line 2 |
| Non-abelian Casimir excess j(j+1) - j^2 = j > 0 of electric flux on a link (Kogut-Susskind form) | dies: it bounds the electric energy of a flux sector from below by (g^2/2)(3/4) per crossed slice, but the vacuum carries an extensive zero-point electric energy, so no bound on the energy difference follows at weak coupling |
| Doeblin bound on single-link conditional laws (density at least e^(-c beta) Haar) | dies: gives only a perimeter-law upper bound on Wilson loops at every beta, which also holds for U(1); not selective |
| Non-conservation of adjoint flux through two parallel plates (gluon colour charge) as the selective quantity | on file in the two-flat-plate class: check 1247 L-section (the (2,2) mixed response equals Cov(j(j+1), k(k+1))/9; the generator identity allows field colour charge above a layer; no screening rate); its decay rate in the plate distance is bounded by the neutral gap, so it restates the gap |
| Photon as Goldstone boson of a broken U(1) one-form symmetry; SU(2) has only a Z_2 one-form symmetry | not an engine: nothing forbids an emergent U(1) in the infrared; the Z_2 deconfined alternative is branch II of row 1161 (on file as (BS)) |
| Dilute topological objects at the band (instanton fugacity e^(-8 pi^2/g^2) is about e^(-30) at g^2 = 2.5) | not an engine: the perturbative fluctuations at the band are of order one and are what must be controlled; instantons do not confine in 4D (RECALLED) |
| Vortex percolation from insertion tolerance at the band scale | dies as stated: insertion tolerance holds also in the deconfined Z_2 phase, where vortices do not percolate; percolation is the dynamical question itself (Mack-Petkova, Tomboulis on file: 49 and 99 files) |

So I add no engine of a new kind. This agrees with rows 1219, 1225, 1229, 1237, 1238, 1243 and 1244.

**1.3 Part (A).** (UNIV-K) is open in (M1)-(M3), (VAC-ID) and (DENS-K) B1-B2 (row 924 table L430-466; row 1238
Step 4). Rows 1233, 1237 and 1238 worked on it today; (MAPCONV-F) = (M1)-(M3) is not a session item (row 1238 note 1).
No row has attacked (VAC-ID). It is needed even when a seed exists.

**1.4 Decision.** This row takes (VAC-ID) of row 924: show that the vacuum scalar entering M_K has the (ET8) form,
with its locality and nonwrapping hypotheses, or name the exact account statement that is missing. Moves: (UNIV-K),
the carry of the gap chain. Success: the vacuum part of (UNIV-K) is uniformly small (row 924 Lemma 5.1) and, with
(VAC-LIP), summable (Lemma 5.3). Failure: the first missing account statement, by name and line.
Rule 0a (grep at this time): `library/open-core.md` has no gap or VAC-ID entry; VAC-ID appears only in row 924's
file and the rows that cite its table (1233, 1237, 1238), none of which attacks it.

## Step 2. (VAC-ID): what the account states about the vacuum constant (READ; started 09:58Z by date -u)

Source: Ethan Sussman and Levent Alpoge's account (with Claude and Codex as authors of its text), `YM4_1400.tex` at
commit 2bc0658f91d2 (the copy and line numbers of row 924), fetched by URL into a scratch folder outside the repository.

**2.1 The first finding: row 924 stopped four dozen lines short.** Row 924 read the local companion criterion
(ET8)-(ET10) at L102529-102592 and its caveat L102586-102589 ("if nonwrapping compatibility has not been established
for the actual formation rule, (ET9) has not been proved for that construction"). The account continues. At
L102645-102670 it states, for the actual construction (quoted in part):

> "The actual vacuum constants have the decomposition
> E_{l,K} = sum_{j<K} [ E^{(j)}_I + sum_y sum_{X ni y} E^{(j+1)}(X,1,y) + sum_X R^{(j+1)}(X,1) ]."

E^{(j)}_I is "one scalar per nonpivot bond" (Haar and Gaussian factor) plus "one scalar per cell of the next lattice"
(gauge fixing), the same two scalars on both tori since the coupling sequence and the gauges are common. The remainder
R^{(j+1)}(X,1) is pointed by giving R/|X| to each root of X. Then (L102657-102667): a domain whose complete window lifts
to a cube of side at most min(l, l_*)/4 "has the same rooted value on either torus by the common companion rule of"
the section `flow-a-common-companion-and-the-torus-floor`, the other domains have length at depth u at least
c l_* L^u/M - C, and

    | E_{l,K}/l^4 - E_{l_*,K}/l_*^4 | <= C sum_{u>=0} L^{4u} e^{-c l_* L^u/M}.                         (V1)

"Thus the common companion comparison applies to the vacuum constant in the sourced construction. Neither vacuum
density need have a cutoff-independent limit."

**2.2 Consequence for row 924, if (V1) applies to the scalar of Phi^vac (to be checked in 2.3-2.5).** Take the pair
(l, L l) at one datum. Multiply (V1) by (L l)^4:

    | Phi^vac(d) | = | L^4 E_{l,K} - E_{L l,K} | <= C (L l)^4 sum_{u>=0} L^{4u} e^{-c l L^u/M},                (V2)

uniformly in K. This is row 924 Lemma 5.1's conclusion, reached without passing through (ET8) at all. So (VAC-ID) is
not needed in the form row 924 stated; what is needed is that (V1) is proved in the account and applies to the
scalar of row 924's split. Open checks, in order: (2.3) the status of the section that supplies the common companion
rule; (2.4) whether "the sourced construction" at zero source gives the scalar e^{-Ecal_(K,empty)} of row 924's split
(L96196 says "The same comparison identifies the unsourced vacuum constant"); (2.5) whether the label constants
Ecal_(K,S) for S nonempty belong to Phi^vac or to the large-field part Q_K (DENS-K).

**2.3 Which scalar enters Phi^vac (READ L4129-4149).** The account's Lemma `lem:averaging-1a-2-4` gives the constant
of one step on regions (Omega, Lambda):

    E^(k)(Omega,Lambda) = ( log sigma_H(0) - (1/2)(N^2-1) log x_k ) |Omega^(k)*| - (L^4-1) log z_G #_(k+1)(Omega)
                          + nu_g |Lambda^(k)*| + sum_{X subset Lambda} [E^(k+1) + R^(k+1)](X, 1),

"together with -Ecal_k = sum_{j<k} E^(j)(Omega_{j+1}, Lambda_{j+1}) and E = sum_{j<K} E^(j)(T_l, T_l). Here Ecal_k
depends on the label, and at the all-small-field label the vacuum constant E equals -Ecal_K." Row 924's split
(its Step 2 and Step 5a item 1) puts the label S = empty into e^(E_K(T)) Z^reg_K(T) and every label S nonempty into
Q_K(T). So the scalar of Phi^vac is the all-small-field constant E_K(T) = sum_{j<K} E^(j)(T, T) of L4149. The label
constants Ecal_(K,S) with S nonempty enter only through the ratios in Q_K, that is through (DENS-K) B1-B2. Row 924's
wording of (VAC-ID) ("-Ecal_(K,S), summed with the label weights") mixes the two; by its own split only S = empty
belongs to (VAC-ID). (ARGUED from the READ lines; this is a reading of row 924's split, not a new estimate.)

**2.4 Status of the input that (V1) uses (READ L84156-84204, L940-972, L84317-84324, L86260-86313).**
- Statement 3.4 (L84159-84176), the common companion: for each frame and weight prefix, one family on the infinite
  level-j lattice for E^(j) and one for R^(j), agreeing with the torus term on every lift of a domain that is
  nonwrapping with its margin, for every admissible (l, K'), with the same bounds and cube-translation covariance;
  b_j depends only on the frame and weights through level j-1. The account: "This compatibility is an input to the
  full interacting construction. The finite formulas proved elsewhere can verify pieces of it; their holomorphy alone
  does not prove it." The authors' overview counts this page (mixed p. 860) among its open boxes, under extensions
  (`library/prior/sa-boxes.md` L89, L98; overview Section 14.10). So Statement 3.4 is an OPEN input of the account.
- The norm (R13, L952): ||E||_(j,kappa) = sup over admissible tori and their companion, sup over X and z in X, of
  e^(kappa d_j(X)) sup_P |E(X, p(P), z)|, with d_j(X) = M^-1 times the length of a shortest tree in X meeting each
  cube; "Sums over domains require the separate lattice-animal summability bound at the chosen decay rate." The class
  bounds are ||E^(j)||_(j,kappa) <= E_0 and ||R^(j)||_(j,kappa) <= g_j^(kappa_0) (R17, L61920-61921), and kappa is
  chosen "above the domain entropy" (L86316-86318).
- The floor (L84317-84318): "Wrapping domains have d_j(X) >= c l L^(K-j)/M." (Lemma VF below proves this by hand.)
- The Gaussian local numbers (eq. flow-RF61, L86272-86301) are asserted "with common nonwrapping lifts and the
  Gaussian domain bound", and "The determinant estimates and first-step sign in RF61 remain actual Gaussian targets".
  The overview lists the Gaussian-vacuum targets as obligations too. If the account books these numbers inside
  E^(k+1)(X, 1), Statement 3.4 covers their lifts; if it books them separately, the lift clause of RF61 is a second
  input. I did not settle where they are booked (OPEN bookkeeping question, not an estimate).

**2.5 Summary of the reading.** The account itself proves (V1) for its actual vacuum constants, from Statement 3.4,
its class bounds and the floor. So (VAC-ID), as the consumer Lemma 5.1 of row 924 uses it, is not a separate open
statement: it is a consequence of the account's own inputs. Step 3 rebuilds the deduction by hand so that the lane
does not rest on the account's one-paragraph proof.

## Step 3. The vacuum comparison rebuilt by hand (written 10:03Z by date -u)

Notation. One first-passage datum d at cutoff K; its run (frame, weights, x_j, b_j). T = T_l and T' = T_(L l) are
admissible tori of that run (l >= l_*(g) of L84322-84324), with compatible sides, so that every cube partition pi_j
of T' is the lift of that of T. For a level j, n_j(T) is the side of T in level-j cubes, so n_j(T') = L n_j(T). D_j is
the set of connected unions of level-j cubes; d_j(X) = M^-1 times the length of a shortest tree in X meeting each cube
(L942-945). The all-small-field vacuum constant is E(T) = sum_{j<K} E^(j)(T, T) (L4149), and
Phi^vac(d) = L^4 E(T) - E(T') (row 924 Step 2).

**Lemma VF (the floor). PROVED.** Let X in D_j on a torus of side n level-j cubes, and w >= 0 an integer. If X,
enlarged by w cubes in every direction, lies in no box (product of cyclic arcs) whose sides are all less than n/2,
then M d_j(X) >= n/2 - 2w - 2.

Proof. If for every direction mu the projection p_mu(X) (a set of cube indices in Z_n) lay in an arc of fewer than
n/2 - 2w indices, the enlarged X would lie in the product of the enlarged arcs, whose sides are less than n/2. So for
some mu, p_mu(X) lies in no arc of fewer than n/2 - 2w indices. Let tau be a tree in X meeting every cube. Its
projection p_mu(tau) to the circle R/nZ is connected, hence an arc A or the whole circle. In the second case
length(tau) >= n. In the first, A meets [i, i+1] for every i in p_mu(X), so p_mu(X) lies in an arc of at most
length(A) + 2 indices; hence length(A) + 2 >= n/2 - 2w. The projection is 1-Lipschitz, so length(tau) >= length(A)
>= n/2 - 2w - 2. Take tau shortest. QED

This is the account's floor (L84317-84318) with c = 1/2 in cube units. With w = 0 it applies to the "sufficient
margin" of Statement 3.4 (L84163-84165: a lift inside a rectangle with sides less than half the torus side).

**Inputs of Lemma VAC (all are statements of the account; none is proved here).**
- (I1) Statement 3.4 (L84159-84176): for each level, companion families on the infinite lattice for E^(j+1) and
  R^(j+1), covariant under the translations preserving pi_(j+1), equal to the torus terms on every lift of a domain
  that lies in a rectangle with sides less than half the torus side, on every admissible torus of the run; the
  coefficients x_j, b_j are the same on T and T'.
- (I2) The class bounds (R17, L61920-61921, norm R13 at L952): |E^(j+1)(X, 1, z)| <= E_0 e^(-kappa d_(j+1)(X)) and
  |R^(j+1)(X, 1)| <= E_0 e^(-kappa d_(j+1)(X)) (take E_0 >= g^(kappa_0)), on tori and companion; and kappa "above
  the domain entropy" (L86316-86318) in the form: the number of X in D_(j+1) containing a given cube with
  M d_(j+1)(X) < t + 1 is at most C_A e^(a (t+1)), with delta := kappa/M - a > 0.
- (I3) The step constant (L4146) on a full torus: three count terms whose coefficients depend only on x_j and fixed
  constants, and whose counts (non-pivot bonds, next-level sites, bonds of Lambda) are fixed multiples of the number
  of level-j sites, plus sum_{X subset T} [E^(j+1) + R^(j+1)](X, 1).
- If the Gaussian local numbers of eq. flow-RF61 are booked outside E^(j+1)(X, 1), add (I4): their lift clause and
  decay, as RF61 asserts them (L86290-86293). The proof below treats them exactly like E^(j+1).

**Lemma VAC (the vacuum part of (UNIV-K)). PROVED GIVEN (I1)-(I3) (and (I4) if needed).** With
C_1 = C_A e^(a + delta)/(1 - e^(-delta)) and r_0 the number of roots per level-(j+1) cube,

    | Phi^vac(d) | <= 4 E_0 C_1 r_0 L^4 sum_{j<K} n_(j+1)(T)^4 e^(-delta (n_(j+1)(T)/2 - 2)),            (VAC)

uniformly in K, in the datum and in the run. Since n_(j+1)(T) = l L^(K-j-1)/s for a fixed cube side s in final
units, the sum is sum_{u>=0} (l L^u/s)^4 e^(-delta(l L^u/(2s) - 2)), which for l >= l_0 is at most
C(l_0) l^4 e^(-delta l/(4s)), as in the account's (ET10).

Proof. (1) Counts. By (I3) the count terms of E^(j)(T', T') are exactly L^4 times those of E^(j)(T, T): the
coefficients are equal (common x_j, (I1)) and every count on T' is L^4 times the count on T (T' covers T L^4 times,
block structure lifted). They cancel in Phi^vac.

(2) Pointing. Write the local sum of level j as sum over roots z of sum over X containing z of r(X, z), with
r(X, z) = E^(j+1)(X, 1, z) + R^(j+1)(X, 1)/|X|, |X| the number of roots of X (the pointing of L102653-102654 and of
L85944-85945). By (I2), |r(X, z)| <= 2 E_0 e^(-kappa d(X)). Fix the threshold D = (n_(j+1)(T)/2 - 2)/M, the same on
both tori, and split each sum into a short part (d(X) < D) and a long part.

(3) Short parts cancel exactly. Let z be a root of T and z^ a lift. If X contains z and d(X) < D, Lemma VF (w = 0)
puts X in a rectangle with sides less than n_(j+1)(T)/2, so X has a unique lift X^ containing z^, with the same tree
length, and r(X, z) = r^(X^, z^) by (I1). Conversely a companion domain X^ containing z^ with d(X^) < D has extent less
than n/2 - 2 in every direction (a tree meets all its cubes), so it projects injectively into such a rectangle. So the
short part at z equals s(z^) := sum over companion X^ containing z^ with d(X^) < D of r^(X^, z^). By the translation
covariance in (I1), s(z^) depends only on the class of z^ modulo pi_(j+1). On T' use the same D: each X with d < D also
lies in a rectangle with sides less than n_(j+1)(T')/2, so the same identity holds. The roots of T' are the L^4 lifts of
the roots of T, class by class. Hence (short part on T') = L^4 (short part on T).

(4) Long parts are small. For one root, sum over X containing it with d(X) >= D of e^(-kappa d(X)) is at most
sum_{t >= floor(MD)} C_A e^(a(t+1)) e^(-kappa t/M) <= C_1 e^(-delta M D), by (I2). The number of roots of T at
level j+1 is at most r_0 n_(j+1)(T)^4, and of T' L^4 times that. So the long parts contribute at most
2 E_0 C_1 r_0 n^4 e^(-delta M D) (L^4 + L^4) to |L^4 S_T - S_T'|.

(5) Sum over j < K. This gives (VAC). For the last estimate put u = K - j - 1 and use
sum_{u>=0} (l L^u)^4 e^(-delta l L^u/(2s)) <= e^(-delta l/(4s)) sum_{u>=0} (l L^u)^4 e^(-delta l_0 L^u/(4s)). QED

**Consequences (PROVED GIVEN the same inputs).**
1. Row 924 Lemma 5.1's conclusion holds with eta_vac := the right side of (VAC): |Phi^vac| <= eta_vac uniformly in K.
   It does not need (VAC-ID) in row 924's form: the (ET8) representation is replaced by (I1)-(I3).
2. With row 924 Lemma 5.2, the vacuum part costs 2 eta_vac in the base margin of the corrected (ONE-K). Literal
   summable increments (row 924 Lemma 5.3, which needs (VAC-LIP)) are not needed for that use.
3. eta_vac is of order L^4 l^4 e^(-delta l/(4s)); the seed needs l of the order of the infrared scale, which is many
   cubes, so eta_vac is far below any fixed margin once l is large (ARGUED: delta, s, C_A are not explicit in the
   account's lines read here, so no number is claimed).

**What Lemma VAC does not cover.** (i) Statement 3.4 itself: an open input of the account (2.4). (ii) Where the
account books the Gaussian local numbers of RF61, hence whether (I4) is a second input. (iii) The labels S nonempty:
their constants enter Q_K, i.e. (DENS-K) B1-B2. (iv) RF62, the size of the divergent vacuum sum: not needed, since the
common part cancels exactly in Phi^vac.

**3.1 Addendum: (I4) is not needed (READ L126172-126196, written 10:04Z by date -u).** The account's vacuum accounting
(eq. comparison-capsule-CP1) defines E = E_(K) with steps e_k = n_k + sum_X [ sum_{z in X} E^(k+1)(X, P_o, z)
+ R^(k+1)(X, P_o) ], P_o = (1, 0), where n_k is "the assigned field-independent step number" (Gaussian scaling
-3|X_k| log tau/2 on the non-pivot bonds, Haar and gauge-fixing counts included), and: "The family in (CP1) contains
the unnormalized local Gaussian numbers ... Those numbers must not also be added to n_k." So the Gaussian local numbers
of RF61 are booked inside the E-family, whose lifts (I1) covers. Lemma VAC therefore rests on (I1)-(I3) only. The same
chapter opens (L126163-126170): "The interacting estimates themselves remain hypotheses"; this does not change the
status of (I1)-(I3) as recorded in 2.4.

**3.2 Lemma VAC adds no premise to (UNIV-K) (READ L94112-94128; written 10:04Z by date -u).** Row 924's regular part
(its Lemma 4.1 and Proposition 4.4) uses R5, "the coupling sequence ... is the same on both tori". The account's line
behind R5 (L94127-94128) reads: "The scalar coefficients use the infinite companion, so the coupling sequence is
independent of the" torus. So the regular part of (UNIV-K) already reads Statement 3.4. Lemma VAC reads Statement 3.4,
the class bounds R17 and the step-constant lemma, which the regular part reads too (R17 is row 924's R17). Hence:
**the vacuum part of (UNIV-K) is PROVED GIVEN the inputs that its regular part already reads** (Lemma VAC with row 924
Lemma 5.2). (VAC-ID) leaves the list of separate open items of (UNIV-K).

**3.3 A side reading for (DENS-K) B1 (READ L1113-1120, L62001, L68212-68218, L72948; written 10:05Z by date -u).**
Row 924 left "the exponent's value not read" in B1's arithmetic (summable iff the exponent of p_0 exceeds 1, or equals
1 with c A_0 > 1). The account sets p_0(g) = A_0 (log g^-2)^(p0) and p_1(g) = (log g^-2)^(p1) with p0 > p1 (L1120),
requires 2 p1 > 8 r (L68218) and p0 - p1 > C r (L72948), and takes r >= 2 (L62001: "with r >= 2"). So p0 > p1 > 4r >= 8,
and sum_K exp(-c A_0 (log(c_0 K))^(p0)) converges. This settles B1's arithmetic premise only; B1's power count (that a
bare-level component shifts the unit-scale action by a marginal term of relative size O(e^(-c p_0(g_0))) per unit cell)
stays ARGUED as in row 924, and B1 stays OPEN.

