lead: anthropic/claude-opus-5-5/high mac-mini-worker
lease_until: 2026-11-02T20:25Z

# Gate: `library/rarity-fresh-x.md` (queue item 59, `rarity-x-gate`)

Status: finished 2026-11-02. Verdicts steer research and grant no status.

## Provenance

Gate by anthropic/claude-opus-5-5, effort high, on the Mac mini worker, at commit `0e8a5a4e7`. The note under test was written by OpenAI Codex (GPT-6), so this read is cross-provider, but it is one read, not an audit, and it grants no status. Mapped-side firewall of `FINISH.md` obeyed. Sections 1 to 4 of the note (statements and proofs) were read and checked before its Section 5 (its own verdicts).

## Verdicts on `library/rarity-fresh-x.md`, one per step

Each step below was redone by hand from the note's own text and the sources it quotes. No run was used; `checks/gate_rx/` holds a README only.

| Step | Verdict | Note |
|---|---|---|
| Sect. 1, consumer contract (RAR^1, RAR^ch, DM's product form, rate translation) | ADVANCE | Quotes match `parts/upper-chain.md:182–183`. Cell to brick: `upper-chain.md:178` declares a cell non-quiet iff its brick is, and 7w/3 separation gives brick separation > 12 t_0, so the injection holds. Nonregular (flux > T_2 >= 2A_f T >= 2T) lies inside the type-II test. |
| Sect. 2, exact positive partition W_x(D) | ADVANCE | A finite sum of indicators of disjoint events, which is trivially exact. It is conditional on the predicates being measurable and defined, and the note says so (quiet's Lift_B^D existence and selection are inputs per `upper-chain.md:178`). Type-II "labelled or above 2T" is a.s. the same as "labelled", since chi = 1 on [2T, pi] (mapped Text 5.2). |
| Sect. 2, bounded-degree graph D_0(Theta) | unchecked, as labelled | Plausible: D_0 ~ C L^4 with patch ranges fixed. Forced co-activity (type-II at l+1 on B^{++} makes the type-I brick at l non-quiet; a Haar parent forced by labelled children) only links tests with overlapping patches, so it stays inside one component. |
| Sect. 2, (CD) | gap, as labelled; no counterexample | Well-posed. The zero-mass clause is part of it. I looked for a structural refutation (D3) and found none. Strictly stronger than RAR, as the note says. |
| Sect. 3, the base measure nu is x-free, and the history law is proportional to exp(-tA) dnu | ADVANCE | chi, T = a_*/L^2, T_2 and the maps are fixed before x (mapped `:991`). A depends on the finest field only, so Haar parents and labels carry no action. |
| (3.1) zero-temperature limit | ADVANCE | Two-sided bound b_eps e^{-t(m+eps)} <= W_t <= nu(D) e^{-tm}; needs only 0 < nu(D) < infinity and A bounded below, both true. |
| (CD) at all large t forces (SEP) | ADVANCE (implication) | Correct given x_l(t)/t -> 1 at fixed depth, or with liminf otherwise. The all-large-x uniformity is not an extra choice for the DM replacement, since DM is stated for every x >= x_*. Polynomial prefactors drop out. |
| (3.1a), (3.2) | ADVANCE | Algebra checked. |
| "First attempted proof of (SEP)" failing at the class-chart boundary | CORRECT-NO-ADVANCE | The missing inference is real: a Hessian bound near the class branch says nothing about ess inf A on a sector whose near-minimisers lie on another label or Haar branch. But the r_(t,out) wording mixes the finite-t mass with the t -> infinity statement. (SEP) is purely variational; see D1. |
| (3.3) F'' = E[S_vv] - Var(S_v) | ADVANCE | Quotient rule redone: d E[f]/dv = E[f_v] - Cov(f, S_v), then f = S_v. |
| Two-branch calculation | ADVANCE (as a counterexample to the generic inference only) | F_t = t(v^2+a^2)/2 - log(2 cosh(tav)), F_t''(0) = t - t^2 a^2. Wording slip: each branch *action* has second derivative 1; S_t has t. It does not bear on (SEP), since both branches have the same minimum. |
| Sect. 4, counting lemma (4.1) to (4.4) | ADVANCE | Successive deletion, injectivity of D -> D\Gamma, the bound sum_Gamma h >= (1/2) sum_M h + (H/2)|Gamma|, the rooted-forest DFS encoding with d^{2(n_j-1)} strings, and the geometric sum [a/(1-d^2 a)]^{|M|} <= 1 iff e^{-H/2}(1+d^2) <= 1 were all checked. |
| Sect. 4, slopes alpha, l_1 and the choice of X | ADVANCE (implication) | Coefficients of X and of (K-l) checked against 8w_0 lambda_l and 2 lambda_l; x_l >= X/2 for all l gives h >= H. |

**First step that fails: (SEP).** Nothing in Sections 1 to 4 is wrong as written. The route stops where the note says, at (SEP) inside (CD). (SEP) is neither proved nor refuted here, and (D3) records the kill attempts.

## Defects, ranked by what each breaks

**D1. (SEP) is the classical content of (AE-R)/(AE-S), not a new obstacle. Mislocated wording, CORRECT-NO-ADVANCE on the step.** The note names the failed step as "the unbounded r_(t,out) term". But (SEP) does not depend on t. It is a statement about essential minima of the bare action A over exact sectors, and r_(t,out) is a finite-t mass that enters only (3.1a). Read at zero temperature, (SEP) is the following:

- *(SEP) with empty residual implies pointwise AE-R for one component.* At a class top the lift of a regular top has flux at most T/4 (mapped `:967`), so it lies in the sector with nothing active, and m(empty) = Acal(top). Then (SEP) says that for almost every U whose active set is one component gamma, A(U) - Acal(top) >= a T^2 |gamma|. That is (AE-R) with err = 0, counted on vertices.
- *Relative AE-R plus a fill implies (SEP), unproved.* With the residual D\gamma held as data, (SEP) follows from two things. The first is an (AE-R)/(AE-S) lower bound relative to a *rough* residual at graph distance at least 1. AE-R's printed data are quiet frozen layers, so this is a new scope. The second is a same-residual competitor: a fill whose action is within o(1) of the frozen-data minimum and which lands in the exact sector D\gamma. That is the "deletion compatibility" the note flags.

So the route escapes (HW) in its local form, but not the classical action excess of the energy route. That excess is already the row FINISH marks "open, most likely place for this route to fail". *Repair to the wording (unproved):* name the first failed step as "relative (AE-R)/(AE-S) with a rough residual, plus a same-residual fill", and keep (3.1a) as the separate, second, entropy obligation.

**D2. An order-of-constants condition that (SEP) needs and the mapped order does not display. Necessary for RAR^1 itself; not a refutation.** A box with at least m_* labelled children is dropped and its parents are Haar (mapped Text 5.2, `:612`). Haar values carry no action. So under a regular top W_r, the top bonds over a dense level-(r-1) box cost about m_* c_b T^2 in bare action, by Lemma TE and local bumps of flux just above T, whatever the top flux. The delta branch that produces a top cell of flux up to T_2 = b_2 T costs about C_cl b_2^2 T^2 per plaquette, by 4D scale invariance. If m_* c_b < C_cl n_p b_2^2, where n_p is the number of plaquettes a dropped box frees, then two things happen at such a top:

- m(dense box) < m(empty), so (SEP) fails with empty residual;
- by (3.1), the conditional law given W_r puts mass e^{-o(t)} on non-quiet level-(r-1) bricks, so RAR^1 at l = r - 1 fails for all large X.

The current order (mapped `:24`) puts A_f, b_2 before m_*, so m_* >= C b_2^2 can be chosen. No such lower bound is written there. `rarity-fresh-c.md` S3(b) assumes "T_2^2 << m_* T^2", the same condition. The other Haar route, a hull excluding half the lines, needs about c L^2 core cells (mapped `:1137`, "not yet carried into Text 5.2"), so it is harmless once L >= L_0. *Repair (unproved, constants not computed):* add "m_* >= C_D b_2^2", with C_D fixed by Lemma TE's c_b and the classical cost of a regular top cell, to the order at mapped `:24`. Check it against fresh-c S5's upper requirement m_* T^2 << L^2 T_2^2, which holds since L comes after.

**D3. Kill attempts on (CD) and (SEP). None succeeded.** By hand, at a class top with empty residual unless stated:
- (i) a labelled cell in (T, 2T]: labelling needs chi > 0, so flux > T, which costs about c T^2 (TE);
- (ii) the dense-box Haar branch: see D2;
- (iii) Haar towers: each Haar parent needs m_* or about L^2 paid children, so the cost per vertex stays at least c T^2 over the tower;
- (iv) instantons and merons: the cost per active vertex is at least a scale-free constant, much larger than T^2;
- (v) a lump under a class top, rough at levels m+1 to m+j: about T^{-2} L^{-4} vertices against action 2 pi^2, so (SEP) holds whenever a_II <= 2 pi^2 T^2 L^4 = 2 pi^2 a_*^2.

None of these is a proof of (SEP). They only show that the linear-per-vertex form is not killed by the obvious examples.

**D4. Two-branch wording (minor).** "Both branch actions have second derivative 1": true of A, while S_t has second derivative t. The example refutes "branchwise Hessian implies marginal convexity", and the note says so. It has no bearing on (SEP), since both branches have the same minimum.

**D5. Measurability and version (minor, labelled).** W_x(D) needs a measurable selection of Lift_B^D (`upper-chain.md:178` lists this as an input). The boundary-ensemble form of (3.1) needs a pointwise fibre version, which the note flags. Neither is supplied. Both are inputs, not errors.

Not checked: whether frozen quiet data in the boundary ensembles (the heavy-wall setting) can force activity at cleared locations. The note restricts vertices to cleared locations, and I did not read `heavy-wall.md`.

## Do S1 to S3 of `library/rarity-fresh-c.md` supply (SEP)?

**No, not as (SEP) is stated, and that route does not need it.** I read fresh-c Sections 1 to 4 (S1 to S3, with Lemmas EX, FC, RANK, PER and the inputs of its Section 3). This is not the `rarity-c-gate` item, and I give no verdicts on its steps.

| | rarity-fresh-x | rarity-fresh-c, S1 to S3 |
|---|---|---|
| What is compared | Bare-action masses of exact all-level active-set sectors, with the residual pattern fixed **at every level**, deleting a connected component that spans levels | F_k = -log rho_k, one level at a time, with the **level-k exterior, parents, other holes and site data held** and finer levels integrated; a mark read one level below its own when rough |
| Zero-temperature content (by (3.1), for any bound uniform in x >= x_*) | (SEP): a sector-minimum gap at fixed residual | S1: inf F_k/t on {b non-quiet, class on G} minus its conditional minimum >= c eps_q^2 T^2, given the level-k exterior. This is a relative, one-level, effective-action analogue of the type-I half of (SEP), and it implies (3.2) for those marks. S3(c): a sector comparison (lump against no lump) through (SEC_m) |
| Competitor in the deleted sector | Must keep D\gamma exactly, at all levels | V° = the label-0 fibre minimum at level k, reached through V^nat and the multiplier bound \|lambda\| <= C T. It changes the fields under G, so residual vertices at levels <= k-2 under G, which are not adjacent to b, need not survive. So S1's competitor is **not** in the sector D\gamma that (SEP) asks for |
| Product form | Peierls component count, H >= 2 log(D_0^2 + 1) | Lemma EX on a union of disjoint patches, plus the hole recursion S4 with conditional odds p_k |
| Rough intermediate parents | Vertices of the component, priced by (CD) | S3(b): the Haar plateau is paid by m_* labelled children, at most C x m_* T^2 per box |
| Where the branch comparison lives | Exposed as (SEP), unproved | Inside the inputs. (I_k), uniform in x >= x_*, carries by (3.1) exactly the statement x names as missing: beneath a class V no label or Haar branch has bare action below the class value A_k(V), at zero temperature. VAL with PER and (ADD) carry it across sectors for lumps |

So the two routes put the same variational content in different places. x makes it an explicit premise, (SEP), with all-level residuals. c puts it into the regular-package inputs (I_k), (Loc_k), VAL and (ADD), and into S1's multiplier bound, which fresh-c names as its own first step not carried, and reads it only one level at a time with the exterior held. That is weaker per statement, and easier to make true. Under its inputs, S1 to S3 would supply the consequence (3.2) for marks at regular tops, level by level, and never (SEP). D2 applies to both routes: c's S3(b) needs T_2^2 << m_* T^2, which is the same undisplayed order condition.

## What was and was not read

Read: FINISH.md and GOAL.md; `library/rarity-fresh-x.md` in full, with Sections 1 to 4 before its Section 5; `library/rarity-fresh-c.md` Sections 1 to 4, without Sections 5 to 9 except the header lines a grep returned; `parts/hard-core--mapped.md` lines 14, 24, 109, 602 to 640, 846 (the Haar-parent paragraph), 967, 991 and 1137; `parts/upper-chain.md` lines 177 to 183 (consumer statements only). Not read: the independent attempt, its gates, and every file the mapped firewall excludes; `quiet-boundary-rarity.md`, `active-energy-excess-contract.md`, `energy-by-stages.md`, `fill-supply.md`, `one-window.md` and `heavy-wall.md` beyond the quotes inside the note under test. No numerics were run. `checks/gate_rx/README.md` says so. Every step above is a written argument, and none is a computation.
