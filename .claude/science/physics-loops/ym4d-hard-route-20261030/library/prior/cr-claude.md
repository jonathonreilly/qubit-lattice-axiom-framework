# Prior work: CR (outside re-blocking)

Reading digest at `a123fc509`; research text, not an audit or independent mathematical check. No status is granted.
Paths are relative to `ym4d-hard-route-20261030/`. I/II/III are Sussman–Alpoge's complete account at `31a47c543775`; SA is its outline. Copies: `/tmp/sa_ca_I.tex`, `/tmp/ym-prior-digests/sa_ca_II.tex`, `/tmp/ym-prior-digests/sa_ca_III.tex`, `/tmp/sa_ym4.tex`.
Credit Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, and Tadeusz Balaban. Source proof labels retain their hypotheses; this digest grants no new proof standing.

Search scope: whole-folder tracked `git grep` for target symbols, note names, account labels, paper names and equation numbers; both complete-account TSVs, outline chunks/neighbours and obligations were searched. Full hit logs: `/tmp/ym-prior-digests/cr-complete-search.txt`, `cr-outline-index.txt`, `cr-upstream-labels.txt`. These are navigation records, not proof evidence.

## 1. Target and statement sites

Exact CR: `library/rb.md:280`–296, equation (20), repeated Results `:298`, `:548`, `:796`; `library/open-core.md:69`–97 (CR); K2 `library/t0-tree.md:172`; FINISH rows 310/348 (`FINISH.md:374`, `:412`). Consumer restatement and weaker tests: `library/crca.md:13`–153.
Under exactly I:45085–45100 (`4.12:prop-reblocking-outside`) and the inherited I:44129–44150 hypotheses, take every actual consumer E, slot p and read domain X''⊂X', with X'∩C=∅, X' fitting no healed box of side ≤204M, and {c_E<p}∩X'' nonempty. Put B=B_E(p,X''), D=M_B Ubar, η=L^-k, ℓ_n=L^(n-k), α_k=tilde α_0k. Its regular minimizer U(B,D) must exist at ε1=2α_k ℓ_p². On every plaquette/bond ξ in X''~2, n=n_E(ξ), require:

| Case | Normalized curvature η^-2 norm(∂U−1) | Physical current norm(J(U)) |
|---|---|---|
| n≥p | ≤2L²B3 α_k | ≤2L³B3 α_k ℓ_p^-1 |
| n<p | ≤3L²BH Kb α_k ℓ_n^-1 | ≤3L³BH Kb α_k ℓ_n^-2 |

Here Kb=(π/3)(d−1)cQ cd(1+3L²)204M. Uniformity covers depth, domain, diameter, block count and the **actual boundary tower**. Add no containing box, global small gauge, source restriction or new-row compatibility hypothesis. J(U) is physical, not the independent current.
Constants: fix §4.12 inputs/response constants before M; M≥max(M1,2M1/δ,2M1 log(2L)/δ); then Kb,N*, then the coupling ceiling (`library/rb.md:270`, `:786`; I:43559–43595).
Their exact counterpart is I:45085–45106, **Proof outstanding**, referring to inside conclusions (a),(b). Its proposed relative-datum identities are I:45114–45133 (`eq-reblocking-outside-1,-2`); its alternative tower comparison is I:45135–45159 (`-3`), with new-boundary compatibility expressly unproved. Inside proposition I:44127 is **incomplete**; real-factor corollary I:44803 inherits it. No outline theorem proves outside CR: SA:9678–9684,9755,9783–9789,9860–9868,9913 are scoped/sketched regularity, settled-tower and joined-collar arguments.
Index search: `library/sa-index/chunk-09.md:28`–39, `library/sa-index/obligations.md:461`–480; `library/sa-index/ca-4.12-4.19/chunk-01.md:168`–235 and `library/sa-index/chunk-02.md:120`–227; full `library/sa-index/ca-full/index.tsv:166`–176, `library/sa-index/ca-full/leaves.tsv:16`–18. Source text governs status.

## 2. Already proved portions; no full outside supplier

| Result | Coverage / what it does not give |
|---|---|
| I:43690–44125: monotone paths, box axial gauge, perturbed plaquettes, minimizer covariance, gain arithmetic (`library/sa-index/ca-full/index.tsv:166`–170) | Individual inputs to inside proof; box/regularity hypotheses remain. |
| RB Proposition 2, `library/rb.md:32`–148 | Repaired inside implication and real-factor slots, including whole J2 stencil; preserves general-group logarithm ceiling and level-k qualification. Not outside coverage. |
| RB Lemmas 3–5, `library/rb.md:154`–246 | One common-box relative datum; gluing **already aligned** gauges; exact quadratic refinement identity. Do not supply uniform tower alignment or inverse. |
| RB Lemmas 6–7, `library/rb.md:304`–426 | Uniform coarse-cover anchoring yields a global relative gauge and first-order refined datum (27a), under complete-cube/averaging inputs. Variable boundary towers are outside its conclusion. |
| RB Lemma 8, `library/rb.md:427`–489 | Scaled-distance collar gives the missing local-scale power, conditional on a genuine tower comparison and universal collar coverage. |
| RB Lemma 9, `library/rb.md:490`–538 | Curvature projection identity; local inequality (34) implies weighted maximum bound (35). Energy contraction does not prove (34). |
| RB §8, `library/rb.md:540`–546 | Existence and n≥p bounds follow if the source-curvature bound covers **every** carrier and the determining-set input applies. No all-consumer admission claim. |
| RB Corollary 10, `library/rb.md:572`–613 | MU nesting identifies restriction with the minimum at its **induced** datum; common complete rows agree. It does not replace that datum by the prescribed cut datum. |
| RB Lemma 11, `library/rb.md:614`–668 | Exact admitted response u_dot=(I−CK)E d_dot, with actual lift and Lagrange Hessian, including multiplier term. Not a uniform response/admission bound. |
| RB Lemmas 12–13, `library/rb.md:669`–784 | Real cube-germ extension; summing assumed local boundary response preserves CR powers. Missing admitted path/row-collar coverage remains explicit. |
| MU, OC, PDA and P4/P7 (`library/rb.md:556`–570, `:643`–665) | Admitted minimizer nesting, own-constant cube gauges, prepared geometry, fluctuation operators and local transport. None admits every new outside datum/tower. |

The account's all-cell bound gives α_k ℓ_p² ℓ_n^-2 curvature and α_k ℓ_p² ℓ_n^-3 current below slot. The extra ℓ_p²/ℓ_n cannot be absorbed uniformly into CR; weaker consumer tests still have an unpaid α_k/α_n factor at p=k (`library/crca.md:30`–107). This is failure of that inference, not a CR counterexample.

## 3. Attempts already exhausted

| Attempt | Exact failure |
|---|---|
| Account route (i), RB 1 | `library/rb.md:154`–226: local axial frames need compatible constant rotations around all overlaps/cycles; one-box estimates do not supply this. |
| RB 2, constrained variation | `library/rb.md:228`–246: mean-zero refined datum gives no size/scale gain; uniform covariant-curl sup inverse and nonlinear admission missing. |
| Account route (ii), RB 3 | `library/rb.md:248`–268: cut tower changes constraint rows; compatibility missing. Physical-distance error also loses one ℓ_n power, equation (18). |
| RB 4, anchored coarse gauges | `library/rb.md:304`–426: uniform-cover alignment succeeds, but actual tower curvature (28) costs ℓ_p²/s_y; enlarged cubes/changed rows not covered. |
| RB 5, scaled distance | `library/rb.md:427`–489: geometric scale gain succeeds; actual changed-tower analytic comparison and every-readout collar do not follow. |
| RB 6, curvature first | `library/rb.md:490`–538: energy norm does not control absolute rows/pointwise readouts; local inequality (34) and nonlinear multiplier absorption missing. |
| RB 7, exact MU nesting | `library/rb.md:572`–613: induced datum D_Y^W differs from D_Y^0; tower saturation criterion fails to cover arbitrary lower-level readouts. |
| RB 8, use P4 response | `library/rb.md:614`–668: P4 fluctuation source is not the averaged-datum lift. No uniform lift/Hessian identification or admitted continuation; diagonal finite-dimensional example (45) disproves inference from inverse bounds alone. |
| RB 9, torus extension | `library/rb.md:669`–784: extension and conditional summed-response arithmetic succeed; transfer to original constraints lacks admitted path, changed-row and healed-cube coverage. |

Related failed routes must not be relabelled CR proofs: MF's primitive-patch completion lacks an admitted common extension (`library/mf.md:280`–352); local operator/word arguments retain their own continuation/majorant gaps (`:353`–474, `:1528`–1590). ARR's seed/nesting and transport attempts likewise fail at actual data/admission (`library/arr.md:558`, `:677`, `:752`). None is equivalent to CR.
L16 attacks common tree chart, then interpolation of averaged data (`library/l16.md:27`–96): neither gives a global admitted path. Its third attack claims a topological obstruction on an actual closed-torus stage (`:97`–312), with critical correction and geometry explicitly checked by its author. Result `:313`–331 is **unchecked by another provider**, conditional on its admission/background inputs. It refutes the unrestricted path premise if correct; it does not refute CR, joined-system comparisons, sector-specific endpoints or path-free methods.

## 4. Consumers and weaker adequate theorem

`library/crca.md:109`–153 contains the semantic and literal-use inventory. The outside label has no invocation outside its declaration/Route; that does not remove its exported role.

| Consumer | Weakest identified need |
|---|---|
| K1 old E,R, I:43346–43363 | All allowed minima/real-factor tests; n=j≥p, so no below-slot case. K1 is excluded by the exact outside proposition's X'∩C condition; retain for related inside uses. |
| K2 old B, I:43364 | Same tests on lower old collars, including n<p, for all read domains. Box-only theorem insufficient. |
| K3 last-step B, I:43348–43365 | Same tests allowing p=k>n: the no-scale-decay case persists. |
| K4 C terms in U_N, I:43348–43366; mixed examples I:44993–45003 | Same tests on actual mixed Z''k/old Ωk domains and boundary towers. |
| K5, I:43367 | Exactly its K1–K4 constituent's tests. |
| Four W composites, I:44803–44844 | Derived real slots for their actual consumer. Same Ubar does not identify determining sets. |
| Group-factor clause, I:9988–10078; twist I:10557–10595; cube extension I:10895–10908; landing I:11724–11776 | Actual all-subdomain/all-slot real-factor membership. Twist transfers already admitted slots; no replacement by an unpaid all-cell estimate. |
| Closure through T, new B, straddling-domain independence, I:10018–10058; composite/production closure I:41976–42010,42083–42089,42164–42171 | Same membership on actual target triples. Dominating-radius heredity works only when its same-triple premise holds. U2's separate target-slot input is not CR. |

All these admission consumers can use a weaker theorem than CR's sharp table: **regular minimizers on all actual towers with the target real-factor radii**, namely |∂U−1|≤vartheta_E α_n η²ℓ_n^-2 and |J(U)|≤vartheta_E α_n ℓ_n^-3 L^(n−p)_+, with their exact strictness/domain conventions (`library/crca.md:48`–65; I:43402–43419). No current result supplies this on all consumers. A fixed smaller margin is payable on the inside box class, not a cure for outside coverage (`library/crca.md:93`–107).

## 5. Overlaps and disposition

Same obligation: FINISH `rb` row 310, `open-core` row 322, `cr-claude` row 348, `crca` row 353; see `FINISH.md:374`, `:386`, `:412`, `:417`. `library/open-core.md:69` and `library/t0-tree.md:172` are restatements. L17/L17c are complex tower admission; CR is actual real outside re-blocking, with no proved endpoint equivalence (`library/t0-tree.md:175`; `library/open-core.md:5`–17). CM/CA/LOC/DOM overlap in possible comparison methods, not in an established common solution. Neither `prior-1.md` nor `open-registry.md` exists here. This reading starts no proof lane.

partly covered: inside boxes, uniform covers, exact response identities and conditional scaled comparisons are present; actual all-consumer outside admission and below-slot real-factor bounds remain.
