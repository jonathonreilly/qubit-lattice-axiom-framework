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
