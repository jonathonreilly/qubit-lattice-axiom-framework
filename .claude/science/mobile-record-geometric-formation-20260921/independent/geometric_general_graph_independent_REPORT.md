# Independent review: general-graph two-vacancy connectivity

The supplied connectivity proof is correct under its stated finite connected simple graph and perfect-matching hypotheses. Its virtual-reference construction uses only legal immutable-record slides, and the stated diameter bound follows. The fixed-graph rare-birth uniform exit and joint exponential clock results inherit with the qualifications already stated. I found no unresolved mathematical defect or consequential prose/code drift in the frozen note and runner. This is selective scientific scrutiny, not a formal audit or a mixing/phase claim.

## Read boundary and source identities

The complete 125-line candidate was read first. I independently reconstructed the proof, implemented its moves with explicit immutable labels, enumerated small graphs, and solved a separate nonbipartite killed-chain example before opening the author checker or results. `PRE_COMPARISON_SEAL.json`, SHA-256 `c4f317495ea680b27397bc77ff85a3d8b113a4a29e788ab7ee0dfe66d42145a7`, preserves that boundary and all ten initial artifacts. Its separate derivation is `PRE_COMPARISON_DERIVATION.md`.

After that seal I read the complete 189-line author runner, its entire result JSON and run log, and its empty stderr. Its unchanged geometric-record helper was reused by its previously reviewed identity. No production simulation values, separate mixing comparison, or unrelated new sources were accessed. No primary source or previous seal was edited.

| Source | SHA-256 |
|---|---|
| `GEOMETRIC_TWO_VACANCY_GENERAL_GRAPH.md` | `70af6469a0e81cbb592ae710eaac07a61912d9754bc98d277ffbf5023301a959` |
| `geometric_general_graph_check.py` | `331fd79fc327bca466892b548207d216477a2375d34ba6b38f675bdf07790039` |
| `geometric_partner_formation_check.py` | `3766230651e8e69c8f51228cd3c3e7ded55140e96bf4b28255042e28e87cb259` |
| Author `geometric_general_graph_checks/RESULTS.json` | `6424acb9eb4885aac401935cefbc83055071f9f2d93eae188ae534421719bd29` |
| Author `GEOMETRIC_GENERAL_GRAPH_RUN.log` | `cdbf685a16c089fe5ff64ca2e1f68d846684bdee1babc131b6f60cfc8b4bf89a` |
| `GEOMETRIC_PARTNER_RECORD_FORMATION.md` | `1bc76bc39c672c7eec318fb4e999dc6e2b1f80aad9a058683dbeb7f7ae247969` |
| `GEOMETRIC_RARE_BIRTH_UNIFORM_SELECTION.md` | `bb01519ad5a072da32a1d53075048a847a9a3c2675b9874327cb94ab496d1e1e` |
| `GEOMETRIC_LAST_PAIR_CLOCK_AND_MONOMERS.md` | `0f5c6bdb5ce0c2ac3e7aa32bef5dfe57e1de0f914c81af984e4195d92722ebd7` |

The final seal includes the empty author stderr, three unchanged procedures, the prior independent model/rare-birth/clock reports and seals, and all current evidence. No external literature theorem is newly imported here.

## Reconstruction of the load-bearing proof

Write a slide as (a,b,c), with a vacant, bc present and ab an edge. If the records at b,c are R,S, the new records at a,b are R,S. Each moves one graph edge; c becomes vacant. The reverse (c,b,a) restores them exactly. This is a two-record atomic slide, so all path-length bounds count those events rather than individual record displacements.

Fix a perfect matching F only as a reference. Its contracted edge graph is connected. If holes occupy e=aa' and a graph edge ab joins e to f=bb', apply

    (a,b,b'), then (a',a,b).

The first operation puts the old f records on ab; the second puts those same records on aa'. The state changes from F-e to F-f in two legal slides. At no stage are records assigned to the missing reference edge by fiat, inserted, relabeled or deleted. A simple path through the K contracted vertices costs at most 2(K-1) slides. This works when the connecting edge is a bridge and when it belongs to no perfect matching.

For an F-alternating cycle v0,...,v(2r-1), bring the missing edge to v0v1. The r-1 slides (v(2j-1),v(2j),v(2j+1)), j=1,...,r-1, leave v0 fixed vacant while the other vacancy traverses the cycle. The final matching is (F symmetric_difference C) minus v(2r-1)v0. The reference changes only after these actual legal moves. Odd cycles elsewhere in G are irrelevant: the symmetric difference of two matchings has only even alternating cycles.

For an arbitrary near-perfect M, compare with any perfect P. The symmetric difference has exactly two degree-one vertices, the holes, and all other degrees zero or two. Hence there is one alternating path between the holes, starting/ending in P edges, plus disjoint cycles. Sliding across its r<=K-1 present M edges leaves adjacent holes. Adding their edge defines a *virtual* completion F, while the actual state remains F-e with K-1 records pairs. Prepare the target T in the same way. Transform the resulting full references cycle by cycle, place the final missing edge, and reverse the target's preparation path. The resulting geometry is T. The labels transported there need not equal an arbitrarily prescribed target labeling.

For c alternating cycles with lengths 2r_j, simplicity gives c<=floor(K/2), r_j>=2 and sum r_j<=K. The two preparations and final missing-edge placement cost at most 4(K-1); cycle relocations cost at most 2(K-1)c; internal slides cost sum(r_j-1)<=K. Thus the total is at most

    4(K-1)+2(K-1)floor(K/2)+K <= K^2+4K-4,

which implies the stated K^2+4K bound. K=1 is a singleton and requires zero slides. None of this bounds path congestion, a spectral gap, a mixing time, or a rate of convergence uniform in graph size.

## Independent finite controls and marked replay

`independent_check.py` uses its own matching enumeration, graph adjacency, slide updates, full-reference transport and cycle decomposition. Its `Tracked` object verifies after **every** actual slide that there are exactly K-1 pairs, all original labels occur once, immutable partner labels remain paired, and each moved label traverses exactly one graph edge. It never creates labels for a virtual completion.

Before author-code access, exhaustive labeled graph controls covered every connected simple graph on 2, 4 and 6 vertices having a perfect matching: respectively 1, 34 and 24,298 graphs, with 327,823 near-perfect states in total. All their slide graphs are connected; the constant K birth-predecessor count is checked for every perfect matching. Two independently constructed endpoint paths per graph supply 48,666 marked path checks. The six-vertex set contains 22,338 nonbipartite graphs.

The separate named suite includes paths, cycles, the diamond, two triangles joined by a mandatory perfect-matching bridge, two squares joined by a bridge absent from all full matchings, a 2-by-4 grid, K6, the Petersen graph, and independently seeded irregular graphs on 8 or 10 vertices. It computes actual slide-graph diameters and runs all endpoint pairs when the near-perfect space has at most 120 states; for larger spaces it runs two constructive pairs. Across these and the exhaustive suite, 116,974 constructive paths and 26,493 alternating-cycle changes were verified. These are coverage figures, not a substitute for the argument above.

`BRIDGE_EXCURSION.json` preserves a particularly relevant seven-slide marked history: on two squares joined by edge 34, holes initially lie on reference edge 45 in the right square. The path flips the full reference in the left square and returns the holes to 45, crossing the connecting bridge. Every actual intermediate state has three pairs; the bridge is used temporarily even though no full matching can contain it. This directly tests the possible bridge/virtual-bookkeeping obstruction.

## Exit law and clock inheritance

The actual continuous-time slide generator Q is symmetric because **each channel**, not each state's total jump rate, has rate kappa. Its new connectivity yields uniform invariant pi on Omega. Let h(M) be the indicator that the two holes are adjacent and R(M,F) the insertion matrix. Simplicity makes h either zero or one. Each full matching F has exactly K distinct deleted-edge predecessors, so

    p = pi h = K Z/|Omega| > 0,      (pi R)(F)=p/Z.

The stationary law would generally change for a different constant-total-rate normalization; that is not the supplied process.

For fixed G and positive conservative rates, the joint discounted exit column is

    q_beta = beta [s beta I-Q+beta diag(h)]^(-1) R_F.

Splitting q_beta=c_beta*1+u_beta with pi u_beta=0, the centered restriction of -Q is invertible. For s>=0, the centered equation gives u_beta=O(beta), while the pi equation gives (p+s)c_beta+pi(h u_beta)=p/Z. Therefore q_beta tends to p/[Z(p+s)] uniformly over the finite entrance set. This proves the Exp(p) scaled clock and independence of its uniform full exit. At s=0 it gives the first-full distribution.

Mean convergence does not follow from weak convergence alone. Here the same finite inverse calculation applied to v_beta=beta E[tau], satisfying (-Q+beta diag(h))v_beta=beta*1, gives v_beta->1/p. The prior checked finite-graph filling argument ensures entrance into the last level from every initially nonfull matching. A strong Markov decomposition and the uniform-over-entrances last-level limit prove the first-full law even if that entrance distribution depends on beta. They do not identify the total empty-start waiting-time law.

Fixed extra conservative channels preserve this result when their **geometric aggregate generator** is symmetric and independent of beta; adding them cannot remove existing communication. The statement is not extended to arbitrary content-dependent marked updates that fail to induce that symmetric geometric generator. Likewise the previously corrected post-filling observation-time qualification remains necessary.

As an independent exact irregular/nonbipartite test, the diamond has five near-perfect states, two full states and p=4/5. At kappa=1, the dark central-edge state has mean remaining time 5/(4 beta)+1/4; the four bright states have mean 5/(4 beta). A bright state's two exit probabilities are (2 beta+5)/[2(beta+5)] and 5/[2(beta+5)], with assignment determined by its direct birth exit. At beta=1 these are 7/12 and 5/12, providing a finite-rate nonuniform countercontrol. The exact joint scaled Laplace limit for either full exit is 2/(5s+4). A separately added symmetric rate 7/3 channel preserves the rare uniform limit. These expressions were solved from the independently enumerated generator before comparison; `EXACT_CLOCK.json` retains the full matrix and formulas.

The counting identity |Omega|=sum_unordered{u,v} Z(G-{u,v}) follows by partitioning states by their holes. Opposite-side restriction on bipartite graphs is valid. No translation-averaged fixed-origin monomer identity or torus literature asymptotic is transferred to arbitrary graphs by this argument.

## Preserved counterexamples and comparison coverage

The independent disconnected edge-plus-square example has near-state components of sizes 1,1,4. In the two singleton components, the already full square is frozen and filling the isolated edge gives different deterministic exits, contradicting a global uniform-exit assertion without connectedness. A connected four-vertex star has near-perfect states but no perfect matching and no last-pair birth exit. On P4, the geometric three-state near-perfect chain is connected, but the six states of one prescribed oriented immutable pair split into two components of size three. This is why the note's geometric-versus-marked distinction matters.

After the precomparison seal, all author result rows and their exact source bindings were read and authenticated; JSON rows equal their run-log entries and stderr is empty. Author small-graph and near-state counts agree with the independent enumeration. A separate incidence calculation fixes a directed slide template and enumerates graph completions: 13 admissible completions times 24 templates at n=4 gives 312 channels; 3,830 completions times 360 templates at n=6 gives 1,378,800 channels, matching the author counts by a different counting order.

To avoid the author's top-level output-directory mutation, `compare_author.py` extracts only its six pure construction/component functions from the exact source AST. It supplies independently implemented edge/partner helpers and independently replays 87 returned paths and their inverses with tracked immutable labels. All pass. The author's disconnected two-square example is also independently reconstructed: four components of size four, each reaching only two of the four full matchings.

The remaining author 80 seeded sparse examples and eight larger periodic summaries were fully read, source-bound and checked for their stated parameter/bound consistency; they were not all rerun. Their PASS rows are author evidence, not additional independent calculations. The unchanged helper's prior read/check is reused by hash. No code/prose discrepancy affecting the theorem was found.

## Evidence and limitations

The precomparison scripts, exact outputs, complete stdout/stderr and receipt are sealed unchanged. No independent attempt failed; expected hypothesis counterexamples are retained in `COUNTERCONTROLS.json`. Postcomparison outputs are separate. To reproduce the independent finite suite without overwriting sealed files, from this directory run:

    python3 independent_check.py --output "$PWD/reproduce_fresh"

`compare_author.py` is a source-bound one-shot receipt generator and refuses to overwrite an existing comparison. Its source and full log remain available for inspection; it is not advertised as a fresh blind derivation.

No open correction is requested for this frozen candidate. The scope is finite geometric connectivity and fixed-graph rare-birth inheritance. Marked irreducibility, operational quantum recognition, uniform-in-volume rates, polynomial mixing, fixed-rate uniform selection, Coulomb phases and waves remain outside this check. The separate new mixing argument was deliberately not opened. The separately queued fixed-rate analyzer correction acknowledgment is not part of this report.
