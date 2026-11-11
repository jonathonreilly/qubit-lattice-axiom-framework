lead: anthropic/claude-fable-5-2 laptop lead (combination of two max author plans)
written: 2026-11-11 UTC

# Mass gap for the 4D SU(2) theory: the final skeleton

FINISH row 676. This file combines the two plans that Claude Fable 5.2 wrote at max effort, each from a no-bias position.

**No mass gap is proved here.** No statement in this file was checked by a model that did not write it.

## 0. What this file is

Sources, each read in full by the lead:

- Run 1: `library/gap-skeleton-max.md` at commit c0debcb59 (575 lines). FINISH row 669.
- Run 2: `library/gap-skeleton-max-b.md` (589 lines) and `library/gap-zero-transport.md` (108 lines) at commit 33623ab44. FINISH row 670.

Rules of reading:

1. The two runs did not open each other's files or the earlier high draft `library/gap-skeleton.md`. This file does not use the high draft.
2. Two runs of one model are two samples. They are not a check of each other. Where they agree, the agreement is evidence about the model and not a proof.
3. This file adds no mathematics. Where its wording differs from a source, the source's exact statement wins. Line numbers point to the sources.
4. The lead read no primary paper for this file. Every statement about the literature is the runs' statement, with their reading state (section 11).
5. Marks: PROVED-UNCHECKED = proved by hand in a source, not checked by another model. OPEN = no proof exists here. Section 4.3 and section 10 are the lead's reading and are marked so.

## 1. The object and the target

**Object.** The account `YM4_1400.tex` of Sussman and Alpoge (written with Claude and Codex), commit 2bc0658f91d2. It is a conditional outline of the continuum tr(F^2) theory for Wilson SU(2) in four dimensions at small reference coupling g. Its hypotheses are the packages A-H. Existence is not proved. The runs read its statements and not its proofs.

**Target (GAP).** Let sigma be a canonical component of a volume-first limit at reference coupling g, with Hilbert space H(sigma), vacuum Omega, Hamiltonian H >= 0 and ker H = C Omega. Then there is m > 0 with spec(H) contained in {0} union [m, infinity). (Run 2, 0.4, lines 56-73; run 1, Part 0.)

Two facts fix what the target means (run 2, lines 67-70).

1. H(sigma) is the cyclic sector of the one scalar field tr(F^2). A gap for the whole theory needs more observables.
2. The unit of length is the scale where the running coupling is g. The expected gap is of order exp(-12 pi^2 / (11 g^2)) up to a power of g. Between distance 1 and distance 1/m the coupling runs from g to order 1. No estimate of the account reaches those scales.

**Which results below do not use the account:** S1 and S2 of section 7.

## 2. The verdict of both runs

Both runs reached the same verdict, in their own words.

Run 1 (3.0, line 448 on): "No approach has a real chance at its crux with known methods. The reason is one fact: between the unit of length, where the existence account ends, and the correlation length there is a finite range of scales on which the coupling is of order one, and every exact tool found here (reflection positivity, the transfer operator, convexity, the doubling identities, transport) is true for U(1) as well and so cannot decide what happens there."

Run 2 (3.3, line 526 on): "I judge that neither tree can be closed by hand with known structures. N6 and M3 are statements about the Wilson theory at couplings of order 1, where no expansion has a small parameter and no exact structure is known that U(1) or the fundamental-adjoint action does not share."

So the skeleton is not a route to a proof with every step in sight. It is:

- two conditional theorems, each with one named hypothesis (section 4);
- one finite form of the gap that would close both (section 5);
- six theorems short of the gap that look provable now (section 7);
- a queue that attacks the two hypotheses first (section 9).

This is the plan's honest state. The owner's goal is the gap. The plan says where the proof is missing, and it does not say the proof exists.

## 3. Filters that every route must pass

Both runs tested each approach against known cases. A route that does not pass these is wrong.

| Filter | What it kills | Source | Standing |
|---|---|---|---|
| U(1) in four dimensions has no gap at weak coupling | every argument that uses only reflection positivity, the transfer operator, convexity or positivity of the measure | run 1, 1.A; run 2, 1.1 | recalled by both runs |
| Z_2 gauge theory in four dimensions has a gap at weak coupling (run 2's K3, finite groups) and still has a transition in beta | every argument for "no zeros between strong and weak coupling" that uses only the centre | run 2, K3 and node N6 | recalled |
| SU(2) on a slab of width 1/T_c is critical: no gap along the infinite directions (run 2's K6) | every argument that proves decay on a slab uniformly in its width | run 2, K6 | recalled |
| The fundamental-adjoint action has a transition line with an end point (run 2's K7) | every argument that does not use the exact Wilson form or the continuum limit | run 2, K7 | recalled |
| Rate: the lattice gap is at most C' exp(-c_AF beta (1+o(1))) | every mechanism that gives a gap of size beta^(-p) at the unit scale | run 1, Lemma 6 (3.5), PROVED-UNCHECKED, uses the account | - |
| Upper bounds: m <= (log 3 + 8 log(9/2)) / (3 d) (run 1, Lemma 6); (8 + o(1)) / r (run 2) | a claimed gap above these | PROVED-UNCHECKED | - |
| Two dimensions is solved exactly | a route whose statements fail there | run 2, 2.5 tests | used as a test |

## 4. The two chosen routes

### 4.1 Route T (run 1's B14): the thin torus with a twist

Nodes are run 1's N0-N7 (3.1, lines 459-475), renamed T0-T7.

**Objects.** Lattice Lambda(n, M) = (Z/n)^2 x (Z/M)^2, coordinates (x_1, x_2 | x_3, x_4). The second factor is the base. The twisted action is A^tw(U) = sum over p not in P_0 of (1 - (1/2) tr U_p) + sum over p in P_0 of (1 + (1/2) tr U_p), where P_0 is the set of (1,2)-plaquettes based at (x_1, x_2) = (n-1, n-1). The measure is mu^tw = Z^(-1) exp(-beta A^tw) dU. The twist-eating configuration V (U_1 = i sigma_1 on links with x_1 = n-1, U_2 = i sigma_2 on links with x_2 = n-1, all others 1) has A^tw(V) = 0.

**Why this object.** The twist removes the flat directions. The minimum of the action is one gauge orbit with stabilizer +-1 (Facts 1, 2), and the Hessian has the gap (2 sin(pi / 2n))^2 on the transverse space (Fact 3). The pair (i sigma_1, i sigma_2) does not exist for U(1). So the route passes the U(1) filter at its first step.

| Node | Statement (short form; exact form in the source) | State |
|---|---|---|
| T0 | The account (form N1 or M1 of the source). | conditional outline; statements read, proofs not read |
| T1 | Port of the account to T^2_s x T^2_l with twist for s below l_*(g): after K block steps the measure on Lambda(n_0, M) is exp(-beta_* A^tw - W), with W small in a polymer norm that decays in the base, uniformly in K and M. | OPEN. Statement made exact and corrected in Section 13.3 (row 684): conditional on the account's inputs and on three estimates for regions that wrap the fibre |
| T2 | (W-twist-lat). For each n >= 2 there are beta_0(n), eps_0(n) and an absolute c > 0 with: covariance of gauge-invariant F, G in [-1, 1] over base sets X, Y is at most C(n, beta) size(X) size(Y) exp(-(c/n) dist(X, Y)), for beta >= beta_0(n), all M, and all W with norm at most eps_0(n). | OPEN; run 1: "Looks provable now" (items `gap-twist-chart`, `gap-twist-lat`). The chart (CH) is proved, and checked line by line by Claude Opus 5.5 (Section 13.2; rows 679, 695). For use after T1 the statement must be made again for the class of Section 13.3 |
| T3 | Area law for loops in the base. (a) From the gap: Lemma 5 + Lemma 4 + the Tomboulis-Yaffe inequality. (b) Without the gap, at every beta > 0 and n: tension at least c (-log tanh(beta n^2)). | (a) sketch; (b) remark; neither checked (item `gap-flux-identities`) |
| T4 | (W-twist). For s <= s_0 the continuum limit on R^2 x T^2_s with twist exists along subsequences, with decay exp(-(c/s) d) uniformly in K. So m(s) >= c/s. | OPEN; from T1, T2 and row 668 |
| **T5** | **(AC'). There is m_0 > 0 such that for every s >= s_0 and every K the theory on R^2 x T^2_s with twist has decay exp(-m_0 d).** Lattice form (AC'-lat): there is beta_1 with inf over n >= 2 of m(beta, n) > 0 for every beta >= beta_1. | **OPEN. Run 1: "The approach dies here."** (item `gap-ac-lat`) |
| T6 | Limit points as s goes to infinity are infinite-volume Gibbs states at the first-passage datum with decay exp(-m_0 d) in x_3. Their continuum limits have a unique vacuum and spec(H) in {0} union [m_0, infinity). | OPEN; run 1: routine-looking |
| T7 | (GAP) for every canonical component of every volume-first limit. | OPEN. Needs uniqueness of the Gibbs state at the datum. (AC') alone does not give it; (D) of section 5 does. |

**Conditional theorem T.** The account and (AC') give (GAP) for at least one theory of the account's class (run 1, 3.0).

**Run 1's own warning (2.10).** The centre symmetry of the fibre could break at an intermediate size. That is a phase transition in s and it would make (AC') false. Run 1 reports that a Monte Carlo study saw no transition for the string tension along T^2 x R^2. A run is a guide and not a proof.

### 4.2 Route Z (run 2's A13, after its own correction): zeros of the partition function of boxes with free walls

Nodes are run 2's N0-N11 (3.1, lines 484-513), renamed Z0-Z11.

**The handle.** Theorem Z (run 2, line 347): if the partition function has no zeros in a domain D of the complex beta plane that contains the strong-coupling disc and a real interval, then the gap at real beta in D is at least kappa_0 times the harmonic measure omega_D(beta). The proof is a two-constants argument (Theorem LP, Lemma HM) applied to g_q = log Z(k) - (1/q) log Z(q k). The gap is known in the strong-coupling disc and analytic continuation carries a lower bound along the real axis.

**Run 2's correction of itself (2.5, lines 448-479).** On a periodic torus the zero-flux sector contains pairs of winding flux tubes and the vacuum energy contains spatial sheets. Their weights have dimension two. So every partition function of a periodic torus has zeros near c_a times abs(Im beta) = pi/4, the zero-free tube has half-width at most 11/(12 pi), its harmonic measure is of order a(beta)^2, and Theorem Z gives a lattice mass of order a^2. That is zero in physical units. The repair: a spatial box B with free boundary conditions, periodic time k, and Z(k, B; beta) = Tr T_B^k. A box with free walls has no winding flux.

| Node | Statement (short form; exact form in the source) | State |
|---|---|---|
| Z0 | The account's estimates, used through a(beta) and Z9-Z11. | conditional outline |
| Z1 | (TM_B). The transfer operator T_B of the box is positive, trace class, with a simple largest eigenvalue. | OPEN, routine (row 667's construction with free walls; part of item `gap-zero-transport-check`) |
| Z2 | (SC_B). abs(log Z(k, B; beta) - (1/q) log Z(q k, B; beta)) <= C_0 size(B) k exp(-kappa_0 k) for abs(beta) <= 2 r_0, k >= 4, q >= 1. | PROVED on abs(beta) <= 1/12800, with r_0 = 1/51200, C_0 = 1/100, kappa_0 = 4 log 2 and k >= 3; checked line by line by Codex gpt-6-astra, holds after correction (Section 13.1; rows 683, 694) |
| Z3 | Theorem LP and Lemma HM. | PROVED-UNCHECKED |
| Z4 | Theorem ZB. Given Z1, Z2 and (ZF_B) on D: m_B(beta) = log(lambda_0 / lambda_1) >= kappa_0 omega_D(beta) for real beta in D above r_0, independent of the size of B. | PROVED-UNCHECKED given Z1, Z2. Second form (row 680; checked by Claude Opus 5.5 high, row 696): Theorem V of `library/gap-zf-box-s.md` gives the same bound from a simple, strictly dominant eigenvalue on D', with no zero-freeness and no shape condition (Section 13.6) |
| Z5 | (HM). omega_D(beta) >= eps a(beta) for real beta >= beta_1. | PROVED, checked by Claude Opus 5.5 high (row 696), for the model scale function beta^p exp(-c beta) and for every admissible scale function (Theorems HM-s and HM-s' of `library/gap-zf-box-s.md`, row 680). The use for the account's a(beta) needs the new open input (2L): a(beta) <= C_2 beta^p exp(-c beta) (Section 13.6) |
| **Z6** | **(ZF_B-x). Z(k, B; beta) has no zeros in a complex neighbourhood of [r_0, beta_1], for all boxes with sides at least n_min and all k >= k_0(B).** Real form: factorial bounds on the cumulants of the action, uniform in B and k. | **OPEN. Run 2: "The node where the approach dies if it dies."** False for U(1), for Z_2, and beyond the fundamental-adjoint end point. (item `gap-zf-box-x`) |
| Z7 | (ZF_B-s). No zeros in the scaling region beyond beta_1. | REPLACED (row 680; checked by Claude Opus 5.5 high, row 696). As stated it does not follow from positivity of the levels (Example 3.8 of `library/gap-zf-box-s.md`). New form (DOM_B-s): a simple, strictly dominant eigenvalue of the continued transfer operator in the scaling region. Under the named hypothesis (SCAL_B) it follows from the positivity statement (CP) for the continuum levels. (SCAL_B) and (CP) are OPEN (Section 13.6) |
| Z8 | Corollary 5'. Z1, Z2, Z5 and (ZF_B) for every box with sides at least n_min give m_B(beta) >= kappa_0 eps a(beta): a gap of at least kappa_0 eps in physical units, uniform in the box and the cutoff. | PROVED-UNCHECKED as an implication. Second form (row 680; checked by Claude Opus 5.5 high, row 696): Corollary 5'' with hypotheses (ZF_B-x) on the tube lens, (DOM_B-s) and (2L) |
| Z9 | Infinite volume at fixed spacing (the interface of row 668). | OPEN as a written proof (item `gap-limit-chain`) |
| Z10 | Limits of boxes give a periodic Gibbs state through a translation average. | OPEN, routine to hard. The identification with the limit points of tori needs uniqueness; run 2 does not claim it. (item `gap-box-to-periodic`) |
| Z11 | Continuum limit and components give (GAP). | OPEN as a written proof (item `gap-limit-chain`) |

**Conditional theorem Z.** The routine nodes and (ZF_B) give Corollary 5' (run 2, 3.3).

**Costs that run 2 names.** (i) The account's estimates are for periodic tori, so the box needs Z10. (ii) (ZF_B) is equivalent to "the largest eigenvalue of the continued T_B(beta) stays strictly largest in modulus on D"; run 2 cites Beraha-Kahane-Weiss from memory for this. (iii) Numbers: zeros of periodic lattices are expected near 0.29 and reported above 0.15 on 4^4 and 6^4 (arXiv:1005.1993, read by run 2). Boxes with free walls are expected zero-free to 11/(6 pi) = 0.58, and run 2 writes "no data known to me".

### 4.3 What the two routes have in common, and where they disagree (the lead's reading)

**In common.**

1. Both routes leave the periodic torus, for the same physical reason. On a periodic torus the flat directions and the winding flux spoil the estimate. Route T removes them with a twist (a unique minimum, tree-level mass pi/s). Route Z removes them with free walls.
2. Both cruxes say one thing in two variables: no phase transition across the range where the coupling is of order one. Route T varies the size s at fixed large beta. Route Z varies the coupling beta at a fixed large box. No implication between (AC') and (ZF_B) is known or claimed.
3. Both trees end at the same question: uniqueness of the Gibbs state at the first-passage datum (T7; Z10).
4. Each route carries a new theorem that needs no crux (S1, S2 of section 7).
5. Both name transport in the coupling as a second route and both leave it undecided (section 5).

**Disagreements, with the item that decides each.**

1. *The zero-free strip.* Run 1 judged its approach B2 to have "the same content as the gap and no handle of its own" and cited zeros of the periodic 4^4 lattice at Im beta of about 0.18 to 0.22 (arXiv:0710.5771). Run 2 found the handle (Theorems Z, ZB) and found by itself that the periodic object fails. The two agree on the periodic torus. Run 1 did not consider boxes with free walls. Decider: guide G1 of section 9, then items `gap-zero-transport-check` and `gap-zf-box-x`.
2. *Transport in the coupling.* Run 1: the pointwise bound is false for the product transport (Lemma 3), holds to first order for the gradient transport (Lemma 7), and is not decided. Run 2: a heuristic obstruction that needs a sharp constant, and the expected inequality d(m^4)/d beta >= -C as a named failed way. Decider: the question in item `gap-transport-check` (is Hess phi_b bounded below uniformly in L in the chain model?).
3. *The strong-coupling Poincare threshold.* Run 1's node M2 writes "b_0 < 1/48" from the abstract of Shen-Zhu-Zhu (arXiv:2204.12737): abs(beta) < 1/(16(d-1)). Run 2 (line 405) converts to its normalisation and gets beta < 1/12; its own bound is 1/15. The lead's arithmetic: if their action is N beta Re sum tr Q_p, then for N = 2 the Wilson coupling in beta (1 - (1/2) tr) is 4 beta, and 4/48 = 1/12. Under that assumption run 1's 1/48 is true and not sharp. No one here read the body of the paper. Decider: read the paper's definition of the action before any statement uses 1/12.

## 5. Second routes and the finite form

| Route | Crux | Where it stops | Source |
|---|---|---|---|
| Transport in the coupling (run 1's B1) | (T-avg): an averaged lower bound on the Hessian of the transport potential along the flow | no a priori estimate in the coupling | run 1, 1.D, 3.2 |
| Multiscale Poincare (run 2's A3) | (HESS): a Hessian bound for the effective actions | no bound for effective couplings between about 1/15 and about 40; and the rate comes out as sqrt(rho), not rho (node M4) | run 2, 3.2 |
| Finite-size criterion (run 1's B6) | (D): at one scale on the unit lattice, for the effective measures at beta_*, the law of the inner half of one cube of side R depends on the boundary condition by less than delta_4 in total variation | (D) is the gap in finite form | run 1, 3.3 |

**Why (D) matters.** (D) is a statement about finitely many integrals. With a constructive criterion of Dobrushin-Shlosman type, rebuilt for gauge fields (run 1's node D1; the paper is NOT READ), it gives decay and uniqueness together. So it gives (GAP) for every component, closes T7, and identifies the limits of Z10 with the limit points of tori. Run 2's remark on Chatterjee's strong mass gap (run 2, 2.3) is the same family. No computer-assisted proof is allowed in this lane, so (D) is a target for a proof by hand or a guide for a run. It is not a shortcut.

**Correction 2026-11-11 (row 691, `library/gap-ds-gauge.md`; proved by Claude Fable 5.2 medium, check queued as row 693).** The criterion is not proved with the plain hypothesis (D). The block argument stops at the collar of the cube, and a range-one Z_2 specification with hard constraints has (D) with delta = 0 and two Gibbs states (Proposition H there; it is not translation invariant and not positive, so it does not decide the case of Wilson's weight). The criterion is proved with the weighted hypothesis (W): one changed boundary link changes on average at most k_z links of the whole cube, and the sum of the k_z per direction is below delta times the number of links of that direction in the cube (Theorem W there). Read (D) as (W) in this section and in Section 7. (W) at (R, delta) forces R to be at least of the order of the correlation length, so it is still the gap in finite form.

Run 2 (3.2): "A3 dies by a threshold and a rate. A13 dies by a zero of an entire function. A proof of N6 would not give M3, and a proof of M3 would not give N6."

## 6. Statements proved by hand in the sources and not checked

Each needs one line-by-line check by a model that did not write it.

| Statement | Source | Content | Check item |
|---|---|---|---|
| Lemma 1 (transport) | run 1, line 224 | flow of -grad phi_t carries mu_s to mu_t; Hess phi_t >= -c gives gamma(b) >= gamma(s) exp(-2c(b-s)) | `gap-transport-check` |
| Lemma 2 (four forms of the derivative of the gap) | run 1, line 227 | (T-avg) is the necessary and sufficient form | `gap-transport-check` |
| Lemma 3 | run 1, line 248 | the pointwise bound fails for the product transport in the chain model | `gap-transport-check` |
| Lemma 7 | run 1, 3.6 | the bound holds to first order for the gradient transport | `gap-transport-check` |
| Lemma 4 (doubling identities) | run 1, line 266 | (D-sheet), (D-plane); everything reduces to entropies of slabs | `gap-flux-identities` |
| Lemma 5 (a gap gives the area law in the family) | run 1, line 297 | run 1's own note: not new in substance (Durhuus-Frohlich 1980; Chatterjee 2020) | `gap-flux-identities` |
| Lemma 6 (upper bounds) | run 1, 3.5 | m <= (log 3 + 8 log(9/2))/(3d); lattice gap <= C' exp(-c_AF beta (1+o(1))) | `gap-transport-check` |
| Facts 1, 2, 3 | run 1, lines 501-505 | minimum, uniqueness and stabilizer, Hessian of A^tw at V | `gap-transport-check` |
| Lemmas 1, 1', 2 | run 2, lines 247-256; transport note | free energy bounds the spectrum; zero electric flux; integral formula | `gap-zero-transport-check` |
| Lemma 3 (centre flips), Proposition 3 | run 2, line 263; transport note | finite volume: a uniform count of states, from (ST5) and (V-ext) | `gap-zero-transport-check` |
| Theorem LP, Lemma HM | run 2, lines 299-302 | two constants; harmonic measure of the half-strip | `gap-zero-transport-check` |
| Theorem Z, Corollaries A, B | run 2, line 347; transport note | no zeros implies the gap, periodic tori | `gap-zero-transport-check` |
| Theorem ZB, Corollary 5' | run 2, lines 460-465 | the same for boxes with free walls | `gap-zero-transport-check`; then a cross-check by Codex gpt-6-astra |
| Hessian bound Ric + beta Hess A >= 2 - 30 beta | run 2, 1.4 | Poincare inequality for beta < 1/15 | `gap-zero-transport-check` |

Both runs found the doubling identity for the partition function by themselves (run 1, Lemma 4; run 2 names it as a Renyi-2 entropy). That is one identity found twice, not a check.

## 7. Theorems short of the gap that look provable now

None is the gap. Each would be new by the runs' reading of the literature, and that reading is not complete.

| Mark | Theorem | Needs | New? (the run's words) |
|---|---|---|---|
| S1 | T2, (W-twist-lat): exponential decay at rate c/n for the twisted thin torus at beta >= beta_0(n), uniformly in the base size. No account input. | `gap-twist-chart`, `gap-twist-lat` | run 1: a mass gap for a four-dimensional SU(2) lattice theory at weak coupling with two infinite directions |
| S2 | Theorem ZB at a fixed coupling: zero-freeness on D gives a gap for the box, independent of the size of the box. No account input. | Z1, Z2, and the check | run 2: "Not found in the sources read" |
| S3 | An explicit zero-free complex neighbourhood of an interval [0, beta_1] with beta_1 above 1/12 for boxes with free walls. With S2 it gives a lattice gap at a coupling where none is proved. | step (a), (b) of `gap-zf-box-x` | run 2: "Any beta_1 above 1/12 is a new lattice theorem" (subject to disagreement 3 of 4.3) |
| S4 | T4, (W-twist): the same in the continuum limit, uniformly in the cutoff, with the area law by T3. | S1, T1, the account | run 1 |
| S5 | Proposition 3 / (W2): a uniform count of states in finite volume. | `gap-finite-volume`; the account's source bound | run 2 |
| S6 | T3(b): area law in the family at every beta > 0 and n, tension at least c (-log tanh(beta n^2)). | `gap-flux-identities` | run 1: remark, not checked |

## 8. The merged tree

```
(GAP) for every canonical component of every volume-first limit
 |
 |-- Route Z:  Z1 (TM_B) -- Z2 (SC_B) -- Z3 (LP, HM) --> Z4 Theorem ZB
 |             Z4 + Z5 (HM) + Z6 (ZF_B-x) [CRUX] + Z7 (ZF_B-s) --> Z8 Corollary 5'
 |             Z8 --> Z9 infinite volume --> Z10 box to periodic [uniqueness not claimed] --> Z11
 |
 |-- Route T:  T1 port -- T2 (W-twist-lat) --> T4 (W-twist) [gap c/s for thin tori]
 |             T4 + T5 (AC') [CRUX] --> T6 limit s to infinity --> T7 [needs uniqueness]
 |
 |-- Finite form:  (D) + constructive criterion for gauge fields
                   --> decay and uniqueness --> closes T7, identifies Z10, gives (GAP) alone
```

The three hypotheses (ZF_B), (AC'), (D) are three statements of one fact: no phase transition at couplings of order one. A proof of one of them is the mass gap up to nodes that the runs judge routine or hard-but-known in kind.

## 9. The queue

**Stop rule for every proof item.** Stop only at (i) a proof, (ii) a counterexample or a proved transition, or (iii) one named lemma that failed in three different ways, each way written down. After two stops on the same statement it goes back to a max author for a restatement. No gap catalogues.

**Save rule.** Every worker writes its file in steps as it goes (FINISH row 675).

Worker 1 writes proofs (Claude Fable 5.2, medium effort). Worker 2 checks, ports and does routine proofs (Claude Opus 5.5, high effort). A proof is checked by a model that did not write it.

| Order | Worker 1 (proofs) | Source of the brief |
|---|---|---|
| 1 | `gap-zf-box-x`: crux of Route Z, node Z6 | run 2, Part 4, Item 1, lines 534-541 |
| 2 | `gap-ac-lat`: crux of Route T, node T5 in lattice form | run 1, Part 4, P1, lines 541-547 |
| 3 | `gap-twist-chart`, then `gap-twist-lat`: theorem S1 | run 1, Part 4, P2, P3, lines 548-559 |
| 4 | `gap-zf-box-s`: nodes Z5, Z7 | run 2, Part 4, Item 2, lines 542-548 |

| Order | Worker 2 (checks, ports, routine) | Source of the brief |
|---|---|---|
| 1 | `gap-zero-transport-check`: every statement of run 2 in section 6, and (TM_B) written out | run 2, Part 4, Item 3, lines 549-554 |
| 2 | `gap-transport-check`: every statement of run 1 in section 6 marked for it, and the chain-model question | run 1, Part 4, P5, lines 565-569 |
| 3 | `gap-sc-box`: node Z2 | run 2, Part 4, Item 4, lines 555-559 |
| 4 | `gap-twist-port`: node T1 | run 1, Part 4, P6, lines 570-575 |
| later | `gap-box-to-periodic`, `gap-limit-chain`, `gap-flux-identities`, `gap-finite-volume` | run 2, Items 5-7; run 1, P4 |

**Why the Z crux goes first.** Its first step (a zero-free neighbourhood near small beta for boxes with free walls) is concrete, its second step would already be a new lattice theorem (S3), and its check item runs at the same time on worker 2. If the check finds an error in Theorem ZB, the crux item is stopped and Route T moves up.

**Guides. A run may guide or refute. It never discharges a proof step.**

- G1 (run 2): Fisher zeros of small boxes with free walls against periodic lattices of the same size, from the density of states. Prediction: the zeros of the box with free walls lie higher. This is the cheapest test of run 2's correction. If the prediction fails, Route Z as corrected is in doubt.
- G2 (run 2): the O(N) model at infinite N with free boundary conditions. Does the height of the zeros move from (pi/2) B toward pi B?
- G3 (run 2): is the bound of Theorem ZB sharp in that model?
- Run 1's three: the sign of c_1 in s m(s) = pi (1 + c_1 g(s)^2 + ...); a read of the bodies of arXiv:2505.10396 and arXiv:2201.06166; the one-loop Hessian of phi_b.

## 10. What would change the plan (the lead's reading)

1. G1 data against the prediction. Then Route Z needs a new object or stops.
2. A broken centre or cyclic symmetry of the fibre at an intermediate size (run 1, 2.10). Then (AC') is false as stated and Route T needs a different family.
3. A negative sign of c_1 with a large coefficient. It would be a warning for (AC') and not a refutation.
4. An error in Theorem ZB or in Facts 1-3 found by a check. Then the affected route goes back to a max author.
5. A proof of (D) at one scale by hand, or a proved inequality that bounds the difference of slab entropies in Lemma 4 (run 1's named missing bound). Either would move the plan to the finite form.

## 11. Credits and reading state

- Sussman and Alpoge, with Claude and Codex: the account `YM4_1400.tex`. Both runs read statements and not proofs.
- Balaban: the renormalization group method that the account builds on.
- Tanizaki and Unsal, arXiv:2201.06166: the thin torus with 't Hooft flux. Sections read by run 1. The continuity (AC') is their conjecture.
- Tomboulis, arXiv:0707.2179 (introduction and section 6 read by run 1); the Tomboulis-Yaffe inequality as quoted there.
- Durhuus and Frohlich 1980, as restated in arXiv:2509.04688 (read by run 1). Chatterjee, arXiv:2006.16229 (read by the digest).
- Denbleyker, Du, Liu, Meurice, Zou, arXiv:1005.1993 (TeX read by run 2); Denbleyker, Du, Meurice, Velytsky, arXiv:0710.5771 (cited by run 1); arXiv:1112.2734 (cited by run 2).
- Shen, Zhu, Zhu, arXiv:2204.12737 (abstract only, both runs). Bauerschmidt, Bodineau, Dagallier (abstract only, run 2).
- Lebowitz and Penrose (abstract read by run 1; from memory in run 2). Beraha, Kahane, Weiss (from memory, run 2). Dobrushin and Shlosman 1985 (NOT READ). Osterwalder and Seiler (to be rebuilt in `gap-sc-box`).
- The digests `library/prior/gap-prior.md`, `library/gap-lit.md`, `library/gap-lit-2.md` (FINISH rows 655, 656, 661).

Every citation above is the runs' statement. Before any outward post, each one is read in the primary text.

## 12. Results after the first round (2026-11-11)

Two items of the queue ended. **No mass gap is proved.** The source files win over this summary.

### 12.1 Route Z, the transport theorem (FINISH row 681)

Source: `library/gap-zero-transport-check.md`. It is one line-by-line reading by Claude Opus 5.5 high, which did not write the proofs.

- Theorem ZB, Theorem Z and Corollary 5′ hold after a correction. No bounded domain satisfies the shape condition (TUBE), so the theorems were vacuous as written. The check replaces (TUBE) with (TUBE′), adds the hypotheses (X) and (C), and proves Lemma S. The conclusion $m_B(\beta) \ge \kappa_0\,\omega_D(\beta)$ is unchanged. Use the corrected statement of its Section 3.6.
- Theorem LP holds; one step of its proof was replaced. Lemma HM, Lemmas 1, 1′, 2, 3, Proposition 3 and the Hessian bound hold.
- (TM_B) is written out there as a port of `library/gap-transfer.md` (row 667). The check of row 667 by another model is `library/gap-transfer-check.md` (row 671).
- Constraint on node N5: its domain must satisfy (TUBE′), or the item must prove its own replacement of Lemma S. A slit strip does not satisfy (TUBE′) near the slit tips.

### 12.2 Route Z, the crux (FINISH row 677)

Source: `library/gap-zf-box-x.md`, written by Claude Fable 5.2 medium. **It is not checked by another model.** The check is FINISH row 685.

- Theorem A (the base). For every box with free walls, of every size, $Z(\beta)$ has no zero in a tube around $\lvert \mathrm{Re}\,\beta\rvert \le 1/10$. The tube does not depend on the box. At real $\beta$ the condition is Dobrushin’s, with threshold near 0.102. This is a strong-coupling statement: the crossover is near $\beta = 2$.
- Theorem ZB-chain. Theorem ZB along a chain of discs, with no shape condition and no global domain. If its check holds, it replaces (TUBE′) on real intervals.
- Proposition B. Take any hypothesis in which a common gap $\mu$ gives a zero-free disc of radius $c\,\min(1,\mu)^p$. Then the continuation ends at a finite coupling. So a zero-free radius that shrinks with the gap cannot cross the region of coupling of order one.
- The one exact next statement, (HS-sup): for some explicit $\beta_2 > 1/10$ and every real $\beta$ in $[1/10, \beta_2]$, a constant independent of the lattice bounds the link gradient of the solution of the Poisson equation for the action. Prove it, or give a family of boxes where it fails.

### 12.3 What changes in the plan (the lead’s reading)

1. Route Z stays. Its transport theorem is now a checked implication from (TM_B), (SC_B) and (ZF_B).
2. The crux of Route Z is sharper. (ZF_B) above $\beta = 1/10$ needs a zero-free radius that does not shrink with the gap. (HS-sup) is the exact form. This is the first stop on this statement; a second stop sends it back to a max author for a new statement.
3. Order of work: `gap-ac-lat` (the crux of Route T) runs next. The lead then compares the two cruxes before `gap-zf-box-x-2` is queued.
4. Section 6 of this file still lists the statements of run 2 as not checked. Row 681 is their check; the table is kept as a record of the state at 2026-11-11 01:40 UTC.

## 13. Results after the second round (2026-11-11)

Three more items ended, and one check. **No mass gap is proved.** The source files win over this summary.

### 13.1 Route Z, node Z2: (SC_B) on the strong-coupling disc (FINISH rows 683, 694)

Source: `library/gap-sc-box.md`, written by Claude Opus 5.5 high. Check: `library/gap-sc-box-check.md`, a line-by-line reading by Codex gpt-6-astra high, which did not write the proof. Verdict: holds after correction. The lead applied the corrections in the source on 2026-11-11.

- Theorem SC. Let B be a finite subset of Z^3 with free walls, k >= 3 and q >= 1. Then Z(k, B; beta) has no zero for abs(beta) <= R = 1/12800, and for abs(beta) < R: abs(log Z(k, B; beta) - (1/q) log Z(qk, B; beta)) <= (size(B) k / 100) (12800 abs(beta))^(4k).
- So (SC_B) holds in the form that Theorem ZB reads, with r_0 = 1/51200, C_0 = 1/100 and kappa_0 = 4 log 2.
- The corrections do not change a constant. They are: the case q = 1 of the covering argument, one fixed majorant for the analytic logarithm, the description of the Sussman-Alpoge polymer theorem, and one credit.
- This is a strong-coupling disc. The check did not cover Theorem ZB, Theorem ZB-chain, (TM_B), or (ZF_B) outside the disc.

### 13.2 Route T, the chart (CH) (FINISH row 679)

Source: `library/gap-twist-chart.md`, written by Claude Fable 5.2 medium. Check: `library/gap-twist-chart-check.md` (FINISH row 695), a line-by-line reading by Claude Opus 5.5 high, which did not write the proof. All ten points hold. Two corrections are applied in the source: the radius r of the locality statement is an integer, and one arithmetic value. The two absolute constants C_3 and C_4 of the group estimates come from compactness and have no value, so delta_0(n) is explicit only up to them. No other provider has checked it.

- Theorem (CH). Let n >= 2, let B be a rectangle of the base with free base boundary, and let U have all plaquette defects at most delta <= delta_0(n). Then:
  - (a) a gauge transformation h gives U^h = V exp(X) with X transverse and sup abs(X) <= C(n) sqrt(delta). The chart is unique up to the centre among charts with small X;
  - (b) A^tw(U) >= (mu_n / 16) sum_l abs(X_l)^2, with mu_n = (2 sin(pi / 2n))^2;
  - (c) locality: if two configurations agree within base distance r of a link, their charts differ at that link by at most C_c(n) (sqrt(delta) + sqrt(delta')) exp(-r / (3n)). The two configurations may live on different rectangles.
- Constants: C(n) = 6.1e4 n^9 and delta_0(n) of order n^(-32). The file does not decide if the natural size n^(-4) holds.
- Not proved there: the chart over base regions with holes (the class in H^1(D; Z_2) is an extra datum), derivative bounds for the map from U to X, and the bound on bad regions.

### 13.3 Route T, node T1 made exact (FINISH row 684)

Source: `library/gap-twist-port.md`, written by Claude Opus 5.5 high. It is a port reading of the account's text `YM4_1400.tex` at 2bc0658f. The statements of the account were read; its proofs were not. **It is not checked by another model.**

**Correction of the T1 row of Section 4.1.** Read that row with these four changes.

1. Not "after K block steps". The block steps stop at the level i_s, the last level i <= K at which the fibre side s L^(K-i) is at least the account's floor 2 L^11 M R_i. The floor is there so that localization cubes do not wrap the fibre.
2. Not "one fixed n_0". The fibre side at the stopping level is n_s, with 2 L^11 M R <= n_s < 2 L^12 M R. It grows like (log beta_*)^r.
3. Not "exp(-beta_* A^tw - W) with W small in a polymer norm". The law of the block field after i_s steps lies in the account's class F_(i_s) on the lattice (Z/n_s)^2 x (Z/M_s)^2. That is a sum over large-field labels of a small-field characteristic function times exp(-beta_* A^tw(U_(i_s)(V)) + a sum of local terms), with the account's bound on the large-field mass.
4. beta_* = x_(i_s)(beta), the account's flow at the stopping level, and beta_* >= g^(-2) + lambda log_L(1/s) - C. It grows as the fibre gets thin.

**State of T1.** An exact statement, conditional on two groups of inputs.

- The account's inputs, with the changes that the port file names (its packages A1-A4, B1-B4, C1-C4, E1). Below the stopping level, a term on a domain that does not wrap the fibre equals the term of the periodic torus. The port file derives this; the derivation is not checked. It needs the account's Statement 3.4 to be natural under covering maps composed with constant gauge transformations.
- Three estimates that the account does not have, for regions that wrap the fibre: (W1) the background field and its response on small-field regions, a global elliptic problem whose admitted flat holonomies include the commuting adjoint pair of the twist; (W2) the activities of polymers that wrap the fibre; (W3) the stability floor.

**Consequences.**

- T2 must be stated again for the class of change 3. The Hessian lower bound of its background action at the twisted minimum is open.
- The match of T1 to T2 needs the thresholds of T2 to be polynomial in n. The threshold delta_0(n) of (CH) is polynomial.
- For T4: reflection positivity at mirrors through the fibre is open. At base mirrors it holds.
- The physical decay rate stays c/s.

### 13.4 The two cruxes (FINISH rows 677, 678, 691, 693)

Rows 677 and 678 both stopped at a finite-box criterion. Row 691 proved the criterion from the weighted hypothesis (W) (see the correction in Section 5). Its check is row 693, `library/gap-ds-gauge-check.md`, by Claude Opus 5.5 high: no statement fails; three small corrections are applied in the source (the covariance bound is proved as written for distances of at least R + 1, and for all distances with a constant larger by the factor delta^(-1/2)). The checker derived the main step again by a second route. The check did not cover the geometry of Lemma C of row 678, so the use for the twisted actions is still an implication from that lemma. (W) itself is open for Wilson's SU(2) weight at couplings of order one. By the stop rule of Section 9, the statement goes back to a max author for a new statement. That item waits for the second literature pass (row 690).

### 13.5 What changes in the plan (the lead's reading)

1. Z2 is closed on the disc. The open inputs of Route Z are the crux (ZF_B) beyond the base region, the nodes Z5 and Z7 (row 680, done: see Section 13.6, which replaces this list by four inputs), and the reading of the check of (TM_B) (row 671).
2. Route T has one more layer than Section 4.1 says. T1 feeds T2 a class of measures, not the Wilson weight with a small term. The stand-alone theorem S1 (plain Wilson weight, fixed n) is still a target of its own.
3. Done: the check of (CH) (row 695), see Section 13.2. Not queued until T2 is stated again: `gap-twist-lat` and `gap-twist-bad`. The port file names (W1) as the next exact statement of T1.

### 13.6 Route Z, nodes Z5 and Z7 (FINISH row 680)

Source: `library/gap-zf-box-s.md` (328 lines; Claude Fable 5.2 medium; read whole by the lead). **Checked line by line by Claude Opus 5.5 high** (`library/gap-zf-box-s-check.md`, 218 lines, FINISH row 696; read whole by the lead): no statement fails; five corrections, none of which changes a conclusion, are applied to the file. The checker and the author are models of the same vendor; no other provider has checked it. No mass gap is proved.

1. **Z5, the harmonic-measure bound.** Theorem HM-s: for an explicit Lipschitz lens D_X that follows the two curves on which beta^p exp(-c beta) is imaginary, omega_{D_X}(beta) >= eps beta^p exp(-c beta) for real beta in [beta_1, X - s], with eps independent of X. Theorem HM-s' gives the same for every admissible scale function. The lens has every shape property that the corrected Theorem ZB asks for. The proof is by hand (a comparison function in a curvilinear rectangle and the maximum principle). eps comes from a compactness argument and has no value.
2. **A new input, (2L).** The bound of item 1 is about an explicit function. Its use for the account's scale needs a(beta) <= C_2 beta^p exp(-c beta) for real beta >= beta_1. The worker read the account's flow statement (their technical statement B3) and reports that its error term is not summable, so the account fixes a(beta) only up to a factor exp(O(beta^(1/2) polylog beta)) and has no two-loop form. Lemma 2L reduces (2L) to a one-sided flow law with a second coefficient and a summable remainder, named (B3+, one-sided). It is open. The check (row 696, Point 1) read their lines at commit 2bc0658f91d2 and confirms both: the account's bound on the increment error is not summable, and a search of their whole file finds no two-loop form of the scale. The lead has not read those lines.
3. **Z7 is replaced.** The node as stated, "no zeros of Z(k, B; .) in the whole scaling region for k >= k_0", does not follow from positivity of the real parts of the levels: Example 3.8 is an abstract family that scales exactly, has a positive gap in the whole region, and has zeros of its traces inside the region for every large k. The worker expects the same for the lattice theory (not proved).
4. **Theorem V, the transport from dominance.** Let (DOM_B) on a set mean: at every point the continued transfer operator T_B(beta) has an eigenvalue of algebraic multiplicity one that is strictly largest in modulus. If (DOM_B) holds on D', then m_B(beta) >= kappa_0 omega_D(beta) on D', kappa_0 = 4 log 2. The proof uses the subharmonicity of the logarithm of the spectral radius (Vesentini; rebuilt in the file), the strong-coupling disc (Theorem SC through Lemma G and Proposition C), and the Perron class. It needs no zero-freeness, no shape condition and no limit in k. Proposition D: zero-freeness on a lens gives dominance there, so the two forms of the crux agree.
5. **The scaling region.** Under one named hypothesis (SCAL_B) (each level of the box is the scale function times a function of the complex size l = n exp(-psi(beta)), with a one-sided error relative to the real part), dominance in the scaling region follows from the statement (CP): Re(e^(-i theta) (E_i - E_0)(abs(l) e^(-i theta))) > 0 for the continuum box, for all angles below pi/2 (Theorem R). (CP) passes the free-particle and small-box tests. It fails for a level that grows linearly with the size, and at a branch point of the vacuum level. (SCAL_B) and (CP) are open; no part of (SCAL_B) is proved, at real or at complex coupling.
6. **Corollary 5''** is the new conditional theorem of Route Z. Hypotheses: (ZF_B-x) on the tube lens (node Z6, the crux), (DOM_B-s) in the scaling region, (2L). Conclusion: m_B(beta) >= (kappa_0 eps / C_2) a(beta) for real beta >= beta_1, with a constant that does not depend on the box.

The lead's reading. (a) The crux of Route Z can now be asked in the dominance form: (DOM_B) on one complex neighbourhood of [r_0, beta_1] for all boxes with sides at least n_min. At real beta dominance is automatic (the transfer operator is positive), so the content is the width of the neighbourhood, uniform in the box. This is the form to give to the max author of the restatement, next to (W) and (HS-sup). (b) Route Z now has four open inputs: the crux, (SCAL_B), (CP), (2L). Before row 680 it had two named nodes there (Z5, Z7) with no exact statement. (c) The times written inside the file are not clock times: the driver log has the run from 04:39Z to 05:01Z.

From the check (row 696). (i) The five corrections: line numbers and one wording in the reading of the account; a parameter condition (B0) for the Lipschitz constant of the lens (true for every use); the statement of Proposition D restricted to points with omega_D > 0 (all of D' for a lens); the converse of Theorem R read pointwise; the condition g^(-2) + B_sharp > 2 c_0 in Lemma 2L. (ii) The cited input (FD) is now rebuilt by hand in the form that Lemma G uses, without determinants. (iii) The checker derived Theorem V again for diagonal families by a different route, with the same result, and shows that kappa_0 omega_D cannot be improved under the boundary hypothesis alone; four attempts to break the theorem with finite-dimensional families fail. (iv) In Example 3.8 every zero lies in the band next to the side curves (abs(Im phi) at least 1.354), which agrees with Lemma E. (v) Still open on the inputs: (TM_B) (row 667) has no check by a model other than Claude Opus 5.5.

### 13.7 The second literature pass and the next step (FINISH rows 690, 697)

Source: `library/prior/gap-crux-lit-2.md` (417 lines; Codex gpt-6-luna high; a reading item; read whole by the lead). The reader stopped at its 3-hour limit: theme F1 (finite-box criteria) is complete, themes F2 to F7 are partial and say so. Every item below is a GUIDE. None is a proof input until its statement is rebuilt and proved in this lane.

**What the pass did not find.** (a) No published finite-box criterion for a lattice gauge theory with a compact Lie group. (b) No mechanism that is established for the 4D SU(2) Wilson theory and false for the 4D U(1) Wilson theory. Every general criterion found treats all groups alike. The digest says that these are limits of the sources read, not a proof that no route exists.

**Leads.**

1. **The Tomboulis-Yaffe inequality.** Kanazawa, arXiv:0808.3442, Annals of Physics 324 (2009) 1634-1665, Theorem 1: for SU(2) on a periodic lattice and a rectangle C in the plane of two directions, the expectation of the Wilson loop W(C) is at most 2 (1/2 (1 - Z^(-)/Z))^(A_C / (L_mu L_nu)). Here Z^(-) is the partition function with the sign of the plaquettes changed on a stacked set that winds around the other d - 2 directions. The proof uses site-reflection positivity and holds for every one-plaquette action. An exponentially small 1 - Z^(-)/Z in the transverse area gives the area law. *Read by the lead on the arXiv HTML page (Section 2.1, equations (2) to (4)).* Two limits. First, the conclusion is the area law for Wilson loops; it is not decay of all gauge-invariant correlations. Second, the same paper states the inequality for U(N) and for U(1) (its Theorem 4). So the inequality does not separate SU(2) from U(1); the group must enter through the twist ratio. The paper's closing note says that Borgs and Seiler already had a result much like its Theorem 2 (the SU(N) form). This is the published form of the link that Route T uses between the twist and the string tension.
2. **A seed criterion that separates a non-Abelian model from the Abelian one.** Ursachi, Research Square preprint rs-11440706/v1 (posted 2026-10-21), on the 2D lattice O(3) sigma model. By its abstract (read by the lead on the Research Square page and in Crossref): a finite criterion from two partition-function ratios on small tori; a proof that the criterion at one seed size gives a transfer-matrix gap uniform in the volume; a computer-assisted verification at eight couplings up to beta = 0.85; for all couplings, a reduction to one inequality (the free-energy defect of doubling the torus falls below 0.2239 at some finite size), with an exact dichotomy; the statement fails for O(2) and for a deformed O(3). Nobody here has read the body. A preprint, not reviewed. Under our rule its computer-assisted part can only guide. It is the one item found whose finite criterion is reported true for the non-Abelian model and false for the Abelian one. The object is the same as ours: ratios of partition functions on small tori and a doubling step.
3. **Logarithmic Sobolev inequalities.** Piazza and Shen, arXiv:2610.35286: for the 2D SU(N) Wilson measure at every fixed beta, with a constant uniform in the volume, by a two-scale disintegration (abstract checked by the lead; the HTML page ends before the theorem). Stroock and Zegarlinski, CMP 144 (1992) 303-323: by the reader's report, for compact continuous spins with finite range a uniform logarithmic Sobolev inequality is equivalent to the Dobrushin-Shlosman mixing condition (the lead checked title and journal only). Bauerschmidt, Bodineau and Dagallier, arXiv:2307.07619, Theorem 3.6: a criterion along the Polchinski flow, on a linear field space (reader's report).
4. **Finite-size conditions.** Dobrushin and Shlosman 1985 (a one-box uniqueness condition) and 1987 (complete analyticity: constructive, from volumes of bounded size, with a zero-free implication); Martinelli and Olivieri 1994 (one cube gives all multiples). All are stated for finite or discrete single-site sets (reader's report). Forsstrom, Lenells and Viklund, CMP 393 (2022) 1311-1346: decay of correlations for finite Abelian groups in 4D at large beta, with a bound on the dependence on the box (abstract checked by the lead).
5. **Orbit-space curvature.** No lower bound on the Ricci curvature of SU(2)^n modulo gauge with a constant independent of the volume was found. Capel et al., arXiv:2606.13453: a logarithmic Sobolev inequality on a quotient under a free action; the action of the periodic lattice gauge group is not free (the constant centre acts trivially), and the result covers U(1) too (reader's report).

**The lead's reading.** (a) The pass agrees with both max plans and with row 691: the inequalities and the criteria are the same for every group, so a proof must put the group into the premise. (b) Two objects now carry that premise in the published work and in this lane: the twist ratio Z^(-)/Z on a box (Route T, lead 1) and the dominance of the transfer operator on a complex neighbourhood (Route Z, Section 13.6). Lead 2 reports a seed-and-doubling criterion on exactly the first kind of object, in a model one step simpler. (c) Next step, by the stop rule of Section 9: one author run by Claude Fable 5.2 max for a new statement of the crux (FINISH row 697). It gets the three stop statements, the test against U(1) and Z_2, and these leads as data.

### 13.8 The crux restated by the max author: one seed inequality (FINISH rows 697 to 702)

Source: `library/gap-crux-restate.md` (353 lines; Claude Fable 5.2 max as author; read whole by the lead). **Nothing in it is checked by a model that did not write it. No mass gap is proved.** The lead derived the main chain again and found no error; the lead is the same model as the author, so that is not an independent check.

**The new conditional form (C1).** Let F = log Z for the Wilson SU(2) theory on a periodic torus, and

```math
\Phi(n) \;=\; 16\,F(n,n,n,n) \;-\; F(2n,2n,2n,2n) \;\ge\; 0 .
```

*Theorem D (b).* The thermal sum $`s = S(n;(2n)^3)`$ of the periodic cube of side 2n at time n obeys $`1 + s \le e^{\Phi(n)}`$.

*Theorem S.* For n at least 3:

```math
S(2n;(4n)^3) \;\le\; \big((1+s)^{64}-1\big)^2 .
```

If $`s < 1/5041`$, then every periodic cube of side $`2^{k+1} n`$ has a transfer-operator gap of at least $`\log(1/(5041\,s))/n`$.

So one inequality at one size,

```math
\textbf{(SEED)}\qquad \Phi(n) \;\le\; 1.9\times 10^{-4}\quad\text{for one } n \ge 3 ,
```

gives a gap of at least 0.04/n on all the dyadic cubes. The gap is on the whole space, flux sectors included.

**What it uses.** A positive trace-class transfer operator in each direction with a simple top eigenvalue (TM); the centre flips (TM-c) for the flux statements; the invariance of Z under exchange of two axes. The step that the two max plans left open closes by a new lemma (Lemma K): the deficit $`\kappa(b) = e(b) - \ell\,b`$ of the ground-state energy against the bulk free energy is non-negative, convex and non-increasing in the side b. Convexity comes from the crossed direction, in which the same partition function is a trace of powers.

**What it no longer needs.** Free or fixed walls, a complex neighbourhood of the coupling, (2L), (SCAL_B), (CP), (HS-sup), (W). The price: the seed is a statement at a size of the order of the correlation length (side times mass about 24, by the author's estimate), so it is false in a small physical volume and it lives where the coupling is of order one.

**The test against U(1) and Z_2.** Theorem S holds for every group. The group enters only through the seed. By recalled estimates, used in no proof, the seed fails for U(1) at weak coupling at every size (the photon keeps Phi at about 0.04 or more) and for Z_2 at its transition. So this form passes test (ii) in the right way: the general part is the same for all groups and the premise is not.

**The flux half.** Theorem F: the odd-flux weight v on a torus obeys $`v(ja,kb) \le v(a,b)^{jk}`$, so one seed v below 1 gives area decay on all multiples at a fixed section. Proposition T: a transverse inequality (TUBE), a bounded defect and one seed give the area law of the odd-flux weight on dyadic symmetric tori. The exact open statement is (TUBE'): $`\operatorname{Tr}\Lambda^2(T_{tw}^{\,c}) \le \operatorname{Tr}\Lambda^2(T^{c})`$ on tori with a square section. It is needed at every scale. Identity 4.4 writes the SU(2) odd-flux weight as a mean of Z_2 odd-flux weights over SO(3) environments.

**Where the program stands (the lead's reading).**

1. The crux of the gap half now has three conditional forms: (DOM_B) (Route Z, Section 13.6), (W) (Section 13.4) and (SEED). (SEED) is the only one that is a single inequality at one size with no boundary values. It becomes the working form, if the two checks hold.
2. The difficulty has not moved. The author made no attempt at the seed at a coupling of order one and names no tool. The author does not recommend another restatement run. A proof of the seed needs a correlation inequality of Griffiths type for SU(2), or a representation with positive weights, or a quantity that is monotone along the scale.
3. A dependency to settle first: `library/gap-transfer.md` (row 667) states the transfer operator for the cube with equal sides. Theorem S uses boxes with unequal sides. The extension is expected to be routine; it is not established. Both checkers give a verdict on it.

**Queued.**

| Row | Item | Model | What it settles |
|---|---|---|---|
| 698 | `gap-seed-check` | Claude Opus 5.5 high | line-by-line check of the whole file; the transfer operator on boxes with unequal sides |
| 699 | `gap-seed-check-astra` | Codex gpt-6-astra high | second check, other provider: the chain to Theorem S only |
| 700 | `gap-seed-limit` | Claude Fable 5.2 medium | (SEED) gives exponential clustering in every limit state; the scaling form; the converse question |
| 701 | `gap-seed-sc` | Claude Fable 5.2 medium | the seed on the strong-coupling disc with explicit constants; test of Theorem S against the known rate |
| 702 | `gap-seed-lit` | Codex gpt-6-luna high | is Theorem S or Lemma K published; tools for the seed (correlation inequalities, positive dual forms, monotone quantities, finite-volume results) |

Not queued: the author's items `gap-seed-guide` (a numeric guide under the numeric lock), `gap-seed-shape` (a better constant from the shape of the box) and `gap-tube-test`. They wait for the two checks.

### 13.9 Theorem S checked by two models; the limit theorem (FINISH rows 698 to 700, 703)

**No mass gap is proved.** The seed inequality at a coupling of order one is not proved and no tool for it is named.

**Theorem S is checked.** Proved by Claude Fable 5.2 (row 697). Checked line by line by Claude Opus 5.5 (row 698, `library/gap-seed-check.md`) and by Codex gpt-6-astra (row 699, `library/gap-seed-check-astra.md`). Both find no failing step in the chain Lemma A, Lemma K, Lemma X, Lemma E, Theorem S, and both verify the constants. The statement: if s = S(n; (2n)^3) is below 1/5041 at one n at least 3 (it suffices that 16 F(n^4) - F((2n)^4) is at most 1.9e-4), the cubes of side 2^(k+1) n have gap at least log(1/(5041 s))/n.

**The transfer operator on boxes with unequal sides is settled.** Theorem S uses boxes (y, 2n, 2n), (4n, y, 2n), (4n, 4n, y). `library/gap-transfer.md` states the operator for equal sides. Both checks find that no step there uses equal sides (Lemma 1.1 of `gap-seed-check.md`; point 1 of `gap-seed-check-astra.md`).

**Corrections, all applied to `library/gap-crux-restate.md`.** (TM-c): the twist replaces the weight exp(-beta(1 - (1/2) tr U_p)) by exp(-beta(1 + (1/2) tr U_p)); it is not a changed sign of beta (both checks). Lemma A (b) needs a nonzero operator (row 699). Lemma K (c) holds for b at least 4 (both). Wording of Proposition R; scope of Corollary S2 (row 698).

**One disagreement, resolved.** The proof of Corollary S3 used that every integer L at least 2N is 2^k b with an integer b in [2N, 4N). That is false (N = 3, L = 13). Row 698 accepted the step; row 699 refuted it and repaired it with Lemma E': for integers h at least b, b above a, a at least 3, 1 + S(a; h) is at most (1 + S(a; b))^(h/(b-a)). The repair gives a stronger result, Corollary S3': **one seed below 1/5041 at size N gives gap at least log(1/(5041 s))/N on every cube of integer side at least 2N.** Seeds on a block of sizes are not needed. Written by Codex gpt-6-astra; the lead (Claude Fable 5.2) re-derived it line by line.

**What Theorem S does not use.** Nothing about SU(2) beyond the transfer operator and the axis symmetry. The group enters only through the seed. The claims that the seed fails for U(1) and Z_2 stay RECALLED: the checks prove only versions at fixed size and large beta.

**The limit theorem (row 700, `library/gap-seed-limit.md`; Claude Fable 5.2 medium; not checked by another model; check queued as row 703).** Given the conclusion of Theorem S:

- on the tori (L_k)^3 x T the truncated two-point function of two bounded local functions at time distance d is at most e^(-m_0 d) + 6 s_k^(floor(d'/n_k)) times the sup norms, where d' is the distance around the back of the time circle and must be at least n_k; on the symmetric tori the second term is at most 0.12 percent of the first;
- every sequence of sizes k_i to infinity with T_i - n_(k_i) to infinity has a convergent subsequence; the limit state does not depend on the time extents; it is invariant under translations and the hypercubic group, reflection positive, and clusters with rate m_0 in each of the four coordinate directions; its transfer operator has a unique vacuum and norm at most e^(-m_0) on the complement;
- a seed that holds uniformly in the cutoff at a fixed physical size gives a rate in physical units that is uniform in the cutoff; the continuum datum is an open input (the T0 chain);
- converse: a uniform gap together with a count of states N(E) at most A e^(theta n E) with theta below 1 gives the seed. A uniform gap alone is not shown to give it. The seed itself gives the count with theta = 1.
- rate filter: the seed can hold only at a size n above 8.5 correlation lengths of the cube.

Open in that file: (U), whether the limit depends on the subsequence of sizes; (NS-gap), the state count; the rate in diagonal directions (proved: m_0/2). Its open item on sides other than 2^(k+1) n is covered for the gap by Corollary S3'; row 703 asks for the limit-state form on all integer sides.

**State of the chain.** (SEED) at one size gives: gap on all cubes of side at least 2N (checked by two models) and exponential clustering in every limit state (one author, check queued). What is missing is (SEED) itself. Rows 701 (the seed at strong coupling, as a test that the criterion can be met at all) and 702 (literature pass 3) are the two items aimed at it.

### 13.10 The seed is proved at strong coupling; the limit theorem is checked; literature pass 3 (FINISH rows 701 to 706)

**No mass gap at a coupling of order one is proved.** The seed inequality there is not proved and no tool for it is named.

**The chain works end to end in one regime (row 701, `library/gap-seed-sc.md`; Claude Fable 5.2 medium; checked line by line by Claude Opus 5.5, row 704: every statement holds).** For beta below 1/12800 the seed is proved by hand with explicit constants: Phi(n; beta) is at most 0.16 n^4 (12800 beta)^e(n) with e(n) = min(4n, n^2), so Phi(n; beta) is at most 1.9e-4 for every n at least 4 with n (12800 beta)^n at most 0.18. With Theorem S and Corollary S3' every periodic cube of integer side at least 2n has gap at least 4 log(1/(12800 beta)) - (4 log n + log 1614)/n. The plan's target was false at n = 3: on the torus 3^4 a plane of 9 plaquettes winds, and Phi(3; beta) has exact order beta^9. The exact leading term for n at least 5 is 192 n^3 (beta/4)^(4n). Theorem S loses nothing in the exponential rate here. This regime is the known strong-coupling regime. Its value is that every input of the chain seed, Theorem S, gap on all cubes is now proved somewhere.

**The limit theorem is checked (row 703, `library/gap-seed-limit-check.md`; Claude Opus 5.5 high).** Every statement of `library/gap-seed-limit.md` holds; one remark that no proof uses is corrected. Part B ports it to every integer side: (G-all), Lemma V (time extents down to max(N, (6/m_0) log L)), constant 1.085 off the dyadic sides, the symmetric tori L^4 for every integer L. Removed open items: other sizes; compatibility of sequences. Still open: (SEED), (U), (NS-gap), the diagonal rate.

**Literature pass 3 (row 702, `library/prior/gap-seed-lit.md`; Codex gpt-6-luna; reading only).** It found no published tool that bounds the SU(2) seed and is false for U(1). That is a limit of what was read. A preprint by Ursachi (two-dimensional O(3) model, abstract only) states a criterion of the same form as Theorem S. Not reached: Luscher 1983; Frohlich, Simon and Spencer 1981; Koller and van Baal 1986 and 1988; the body of the Ursachi preprint.

**The shape of what is left (the lead's reading, Claude Fable 5.2 high).** The proof has three parts.

- Ultraviolet: from the lattice spacing to a box of small physical size. This is the account of Sussman and Alpoge after Balaban (the T0 chain); in a small box the coupling is small.
- Infrared: from one box that holds the seed to every larger cube and to every limit state. This is Theorem S (checked by two models) with the limit theorem (checked by one).
- Between: a finite range of box sizes, from the small box to a box of about 17 correlation lengths (rate condition alone; Section 13.11 corrects this to about 20), where the coupling is of order one. The seed is the statement at the upper end of this range. For a fixed lattice coupling it is one inequality on one finite lattice. No by-hand tool is known for it, and every exact tool found so far holds for U(1) as well.

A scale-invariant theory keeps S(n; (2n)^3) of order one at every size. A theory with a gap drives it to zero. The threshold 1/5041 is what the present lemmas give; the best possible threshold of a theorem of this kind is at most of order one. Row 705 asks how far the threshold can be raised, which moves the infrared end of the open range down. Row 706 puts published numbers on the size of the seed box at beta from 2.2 to 2.6.

**Queue.** Row 704: check of the strong-coupling seed (worker 2, Opus 5.5 high). Row 705: the seed for other shapes, the limit of the method and a ceiling (worker 1, Fable 5.2 medium). Row 706: size of the seed box from published data (Codex gpt-6-luna; guide). Not queued: the numeric part of the author's item 3 (a measurement of Phi at n = 3, 4 for SU(2) and U(1); a guide, and row 706 first says where it could see anything); `gap-tube-test`.

### 13.11 Theorem S for every shape; a ceiling; the size of the seed box; the attack on the middle (FINISH rows 704 to 708)

**No mass gap at a coupling of order one is proved.** The seed inequality there is not proved and no tool for it is named.

**The strong-coupling chain is proved and checked (row 704, `library/gap-seed-sc-check.md`; Claude Opus 5.5 high).** Every numbered statement of `library/gap-seed-sc.md` holds; no correction. The checker counted the leading coefficients by hand before reading the author's count, and the counts agree. For beta below 1/12800 the chain from the seed through Theorem S to a gap on every periodic cube is proved and checked line by line (Theorem S by two providers; the seed and the limit theorem by Claude Opus 5.5 only). This is the known strong-coupling regime.

**Theorem S for every shape (row 705, `library/gap-seed-shape.md`; Claude Fable 5.2 medium; checked line by line by Claude Opus 5.5 high, row 707: no statement fails, six hold after correction, see Section 13.12).** Theorem SH: a thermal sum S(a; B) below a threshold on one box B of any shape gives a uniform gap on every larger cube. Thresholds on S(a; b^3) with r = b/a, by hand: 1/1650 at r = 2, 1/100 at r = 3, 1/25 at r = 4, 1/10 at r = 6, 3/10 for r at least 24, and values that tend to 1 along a family of shapes. Theorem D-shape: the seed is an inequality between free energies of tori over one spatial box, 2F(a, B) - F(2a, B) at most log(1 + t(r)). It holds for every gauge group.

**A ceiling (row 705; the same file).** The supremum of the threshold over shapes is exactly 1 (the upper half given Peierls, recalled). The class of models in which the lemmas hold contains two models with no gap: the four-dimensional Ising model at large J, with S tending to 1 at every shape; and a compact Gaussian model with windings, with S at least about 3.1 at r = 2 (guide values). So the lemmas of this class cannot make the thermal sum fall along the scale. The fall has to come from the group.

**The size of the seed box (row 706, `library/prior/gap-seed-size.md`; Codex gpt-6-luna; guide only).** With published SU(2) masses and a dilute gas model, the seed S(n; (2n)^3) at 1/5041 needs a time extent n of about 12 inverse masses of the lightest glueball, so a spatial side of about 24: n = 10 at beta 2.30, n = 24 at beta 2.60. No n up to 8 passes at the sampled couplings. The free gas model of row 705 agrees (11.7 at 1/5041, 10.4 at 1/1650). Section 13.10 said about 17 correlation lengths for the largest side of the tori; that number used the rate condition alone. The models give about 23 to 28 with the old criterion and about 20 with Theorem SH.

**One sentence of Section 13.10 is corrected (row 704, remark 2).** "Theorem S loses nothing in the exponential rate" is a comparison of two formulas at strong coupling, not a theorem.

**The shape of what is left (the lead's reading, Claude Fable 5.2 high).** The infrared end moved a little: the threshold at r = 2 rose by a factor of 3, and the seed can be read from two free energies. The middle did not move. It is a finite range of box sizes at a coupling of order one, and its upper end is a box of about 20 correlation lengths. Every exact statement found so far holds for groups with no gap.

**Queue.** Row 707: check of the shape file (worker 2, Claude Opus 5.5 high). Row 708: one author run on the middle range (worker 1, Claude Fable 5.2 max; one run, not parallel with another max run): candidate mechanisms with the U(1) and Z_2 test, then real attempts on the best two or three. Not queued: a strong-coupling bound for the shape defect; the best threshold at a fixed ratio; the numeric guide run at n = 3, 4 (row 706 shows it could see the seed only below the sampled couplings).

### 13.12 Theorem SH is checked; the middle range gets a name; the seed for beta below 1/18 (FINISH rows 707 to 711)

Written by the lead (Claude Fable 5.2 high) from the two files of the round, both read whole. **No mass gap at a coupling of order one is proved.**

**Theorem SH is checked (row 707, `library/gap-seed-shape-check.md`; Claude Opus 5.5 high; same provider).** No statement fails. The thresholds 1/1650 (r = 2), 1/100 (3), 1/25 (4), 1/10 (6) and 3/10 (r at least 24) stand. Six statements hold after correction; no correction changes a threshold or a conclusion. The corrections are in the lead note at the top of `library/gap-seed-shape.md`. One of them changes how a result is marked: the ceiling "the supremum of thresholds is exactly 1" rests on two recalled facts about the four-dimensional Ising model at large J (long-range order uniform in the torus, and that it forces the tunnelling gap of the cube to zero). It is a conditional statement, not a theorem of the file. The check found by a different route that the method at r = 2 ends near 1/1500, so 1/1650 is close to what this recursion can give.

**The author run on the middle (row 708, `library/gap-mid-max.md`; Claude Fable 5.2 max as author; not checked, check = row 709).** It proves no seed at a coupling of order one and names no tool for it. It does five things.

1. *A larger proved range.* Theorem DOB: for beta below 1/18 the plaquette means of the tori of time extents a and 2a differ by at most 8 alpha^(floor(a/2) - 1)/(1 - alpha), alpha = 18 beta. With Theorem SH this gives a gap on every periodic cube for beta below 1/18 (before: 1/12800). The proof is Dobrushin's comparison estimate, rebuilt in the file. It holds for every compact group, so it is still strong coupling.
2. *A name for the middle.* Theorem CRIT: the couplings that have a seed (below 1/25 at ratio 4) form an open set that contains the strong-coupling range. If the set ends at a finite beta*, then at beta* no box size has a seed and the seed size diverges on approach. So the mass gap at every coupling is the statement **(NOCRIT): beta* is infinite for Wilson SU(2).**
3. *A form with no small number.* Theorem TR and Corollary TR1: a seed at strong coupling is carried to any beta_1 if, on one cube of side b, the thermal quantity G falls along the coupling no faster than a logarithmic rate K, and the integral of K is at most log(b/(2 ceil(log_2 b))). This is **(VIR-log)**. It implies (NOCRIT). It is a change of form, not of difficulty: three attempts to prove the rate bound failed, and the cube it needs at beta = 2.3 has a side of 10^3 to 10^4 lattice units (guide).
4. *A new test, K7.* The mixed fundamental and adjoint SU(2) weight has a first-order line (recalled from Bhanot and Creutz, not read). On that line the seed fails at every size. That weight shares the group, the centre, reflection positivity, the Ricci curvature and the one-loop coefficient with the Wilson weight. So every statement that follows from those properties alone cannot give the seed at every coupling. A proof must use the Wilson weight itself, which means its loop equations. This is sharper than the U(1) test of Section 13.10, which only excluded statements that ignore the group.
5. *Two routes ended.* Curvature (Bakry-Emery) at a block scale: Proposition BE gives a configuration with negative curvature for beta above 1/3 for every blocking that leaves one link free. The scale recursion (CAS): it restates the seed step by step.

Also proved (unchecked): Proposition Delta (a seed from the Casimir free energy Delta(a^4) at most 6.1 x 10^(-4)), Identity FL (the thermal sum splits exactly into a zero-flux part and a flux part, and the two are independent in the class), Lemma M and Proposition MIX (the seed is the locality of one plaquette's response to a cut of the torus).

**The one candidate that passes K7 the right way** is a positivity certificate over the loop equations, (BOOT_eps): any two states on a cube that satisfy the loop equations and reflection positivity have central plaquette means within eps. Published bootstrap bounds of this kind are numerical and do not compare volumes. No hand certificate is known. It is a direction, not a proof step.

**The shape of what is left (the lead's reading).** The range with a written proof grew by a factor of about 700 in beta (Theorem DOB, not yet checked) and is still strong coupling. The open range now has three exact forms, (NOCRIT), (VIR-log) and (BOOT_eps), and one sharp requirement: the proof object must change when an adjoint term is added to the weight. Nothing in the repo or in the literature read so far has that property and is rigorous. The author of row 708 advises against another max run on the middle range before a new tool exists; the lead follows that advice.

**Queue.** Row 709: check of `library/gap-mid-max.md` (worker 2, Claude Opus 5.5 high). Row 710: (VIR_K) and (LEV_K) at strong coupling, proof or counterexample, uniform in the cube (worker 1, Claude Fable 5.2 medium); it decides whether the coupling-direction route is usable at all. Row 711: literature on the new named statements (Codex gpt-6-luna). Not queued: Theorem DOB with the sharper one-link bound (beta up to about 1/10; same regime); a two-dimensional Ising guide run for the rate K; a check of Theorem DOB by a model of another provider.

### 13.13 Theorem DOB is checked; the coupling route needs the same mixing input (FINISH rows 709 to 715)

Written by the lead (Claude Opus 5.5) from rows 709 and 710, both read whole. **No mass gap at a coupling of order one is proved.**

**Theorem DOB is checked (row 709, `library/gap-mid-check.md`; Claude Opus 5.5 high; same provider).** No statement of `library/gap-mid-max.md` fails; five hold after correction (lead note at the top of that file). So the seed, and with Theorem SH a gap on every periodic cube, is proved and checked for beta below 1/18 (before: 1/12800). Theorem TR, Corollary TR1, Theorem CRIT, Proposition Delta, Identity FL, Lemma M and Proposition MIX are checked too. Proposition BE proves only that the curvature route ends at beta = 1/3 at most.

**The coupling route at strong coupling (row 710, `library/gap-vir-sc.md`; Claude Fable 5.2 medium; not checked, check = row 715).** The rate bound (VIR_K) is proved with the rate 2/(s log(1/s)) only on a range of order 1/b^3; that reaches nothing new. Two results matter more than the range:

1. *Theorem U, an exact formula at every coupling below 4.* For every level of every box, s times the coupling derivative of log lambda is the electric number of the state, minus s times its spatial action, minus a small correction; and the level is at least log(4/s) times the electric number. This is the lattice form of the action sum rule (Michael; Rothe; to be read in row 714).
2. *Where it breaks, exactly.* Each state alone obeys the inequality. The difficulty is the subtraction of the vacuum: an excited state of a large cube must differ from the vacuum by a bounded amount of action per time slab. At small coupling this is (BAND-sc). At a coupling of order one it is a mixing statement of the same kind as (W) of row 691 and Proposition MIX of row 708.

**The shape of what is left (the lead's reading).** The three directions tried so far (scale, coupling, flux) now meet at one kind of statement: locality, or mixing, of an excitation or of one plaquette's response, uniformly in the box, at a coupling of order one. Test K7 says the proof of it must use the Wilson weight itself. (BAND-sc) is not queued: it gives strong coupling only, already covered by Theorem DOB.

**Queue.** Row 712: Fable 5.2 max, first principles and the assumptions exercise on the crux and on the tool blockage (started 12:16Z). Row 713: luna, mathematics literature (uniform gap criteria, log-Sobolev on compact groups, positive-operator contraction, absence of transitions, recent lattice Yang-Mills). Row 714: luna, full read of the ranked open papers (downloads allowed by the owner on 2026-11-11). Row 715: check of `library/gap-vir-sc.md` (worker 2, Claude Opus 5.5 high).
