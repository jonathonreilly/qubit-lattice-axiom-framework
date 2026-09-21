# Final source review: empty-start motion response

No unresolved mathematical defect was found in the corrected sources below. Four narrow findings were reported and corrected by the primary author. This is a source-bound mathematical review, not an audit, retained-status decision, or landing verdict. The local-activity unit is outside this review.

## Findings and corrections

1. **Common vector eigenvalue was missing from the scope.** The original Section 5 said the three-component unit-vector structure factor has the same coefficient as a centered scalar eigenfunction for arbitrary symmetric row-six `W`. That requires all three coordinate functions to be eigenfunctions with the same eigenvalue. The corrected text states this condition and names the j-family as an example. A decisive admissible counterexample to the unqualified sentence is `W=J+u u^T/10`, `u=(2,-1,-1,0,0,0)`: scalar `chi=u` has `theta=3/5`, whereas the vector coefficient uses `(1/6) sum_i v_i^T W v_i=1/6`.
2. **Fourier adjacency formula needed a size condition.** On a simple side-two torus the positive and negative coordinate neighbors coincide; the adjacency eigenvalue is not `2 sum_i cos(k_i)`. Section 5 now refers to the previously stated side-`L>=6` family.
3. **The relative generator needed explicit proposal premises.** Section 8 now specifies a simple nearest-neighbor torus, side at least three, with unit symmetric proposals. The displayed endpoint factor two and rate then have precisely the stated meaning; arbitrary edge-dependent proposals from the general finite model are not silently included.
4. **The two coefficient suites were conflated.** Section 9 now attributes fifteen three-site block checks to the separately sealed independent suite and distinguishes the portable runner's twelve cases, including one four-cycle.

`verify_fixes.py` reverses exactly these four edits and recovers the original frozen SHA-256. There were no additional changes. The primary runner remained byte-identical. All four findings are resolved.

## Proof reconstruction and scope

The entire note and runner were read. The earlier independent reports, code, outputs and seals were reverified against their original hashes and preserved. Their proofs remain applicable to the supplied finite simple graph, positive symmetric row-six menu, empty initial state, immutable contents, birth holding terms, and reversible vacancy-hop dynamics. No assumption that content counts identify motion classes is used.

The identities `delta_0 B H=delta_0 B^2 H=0`, the two-record nonstationary part `-2wb` of `delta_0 B^3`, and the Dirichlet conversion give the stated first possible distribution order four and population coefficient `kappa epsilon^4 D_2 t^5/60`. The general-first-level proof is also valid: weighted deletion preserves actual class-constant functions by pairing parents across each legal hop; before the first hazard-sensitive level `m`, multiplication by the hazard preserves the same kernel. The first nonstationary row is therefore `-m! b` on level `m`, up to a kernel element. Ordered integration gives the factor `1/(m+1)` in `G_m`, and the spectral theorem gives its positivity, monotonicity and concavity in mobility. If no such level exists, every pure-birth row is motion stationary, which proves equality of the entire empty-start law. Positivity of all weights and proposals ensures the parent hops used in the deletion argument remain legal.

The fixed-time epsilon expansion retains the whole motion semigroup; its coefficient is an unnormalized weighted sum. Its projection and Dirichlet bounds, the three-site two-mode formula, and the finite-volume remainder `2V exp(epsilon beta t)(epsilon beta t)^5/120` follow with `beta=2 max b`. The last remainder follows by bounding every Dyson term with the motion contraction and `||N||_infinity=V`. These are fixed finite-model results; neither the large-mobility coefficient limit nor the epsilon expansion asserts a uniform finite-density approximation or all-time finite-epsilon monotonicity.

The torus geometry count and strict positivity criterion agree with the earlier sealed geometry review. In particular, `W^2-6J=(W-J)^2` and symmetry imply `sum h_ab^2=tr[(W-J)^4]>0` unless `W=J`. The uniform Taylor estimate keeps local differences grouped and counts jumps whose **updated sites** meet each individual term's support. Birth and hop rates depend only on the updated sites and their neighbors after cancelling unchanged pair factors. Each word increases its support by at most `K=2(z+1)`; summing word norms gives the product bound in the note. Markov contraction then justifies the displayed degree-six remainder. Its volume uniformity holds with degree, weights and rates fixed. The certified numerical window is indeed about `2.13e-17` in the stated abstract example; it makes no claim about moderate density.

For the added relative-position reduction, label the two occupied endpoints temporarily and write `r=y-x`. Moving either endpoint to produce a given allowed relative step gives rate `w_g(r')/[w_g(r)+w_g(r')]`, so the aggregate is twice that rate. Thus the ordered endpoint generator intertwines exactly with `H_g`. The hazard is `6(V-2)+h_ab c(r)`, and its constant part is annihilated by `I-exp(kappa s H)`. The sum over `(x,r,a,b)` counts each physical two-record state twice, including identical contents; translation supplies the factor `V`. Consequently the full weighted quadratic form is `(V/2) sum_ab h_ab^2 <c,(I-exp(kappa s H_g))c>`, which gives the stated `1/6` after the Dyson factor `1/3`. This argument needs neither pair-sector irreducibility nor an equilibrium replacement.

The scalar content-pair and normalized structure-factor formulas follow directly from the signed second birth-generator power. Their remainders are correctly limited to a fixed finite model. The j-family population coefficient has an explicit `j^4` factor while its finite-state motion kernel stays bounded and continuous near zero; the stated fixed-model `O(j^4)` is justified. The corrected vector scope supplies its necessary common-eigenvalue premise.

## Executable evidence and limits

- The unchanged primary runner reproduced **57 PASS / 0 FAIL**. Its maximum block-coefficient discrepancy was `3.2614438927325295e-11`, within the stated tolerance. The complete output is `PRIMARY_BASELINE.log`.
- New exact checks independently construct labeled endpoint hops and verify every relative-generator row in **28 cases, 4,296 ordered rows**. The side-two cases are extra boundary checks; they do not expand the corrected note's torus scope.
- Separate physical two-record content generators on a four-cycle and a `3x3` torus, with a positive non-axis-symmetric row-six menu, match the reduced weighted coefficients through `H^3` exactly. They use **216 and 1,296 physical content states**, respectively, and compute the actual birth hazard directly.
- **166 exact scalar-moment assertions** cover a singleton, path, triangle, disconnected graph and star with positive and negative centered eigenvalues. The vector counterexample above is exact.
- Reproduction of the primary relative-position gate gives maximum error `2.7755575615628914e-16`, agreeing with the note's `2.78e-16`. This metric reproduction calls the primary helpers and is not represented as independent evidence; the rational generator-intertwining checks are independent implementations.

The finite cases check the formulas and normalizations, not every graph or menu. The arbitrary-level theorem relies on its deletion proof; the rook witness establishes `m=3` using constant pair geometry and one strictly positive three-record edge, not full `7^16` enumeration. The local norm checks support the written word-by-word proof rather than replacing it. Matrix exponential and quadrature checks are floating point. The primary author ran the eight declared mutations; those runs were not independently repeated here and are not part of this report's execution claim. No physical clock, force, infinite-volume process, phase or axiom adoption is inferred.

## Source identities and reproduction

Review worktree: `/Users/jonreilly/Documents/Codex/mobile-record-empty-start-publication-20260921`, based at `689941783bea870e08458e079ddb208257d0083d`.

| Source | SHA-256 |
|---|---|
| Corrected note, `docs/MOBILE_RECORDS_EMPTY_START_MOTION_RESPONSE_BOUNDED_THEOREM_NOTE_2026-09-21.md` | `a8e9d26399a8c810a7bb919edaaa9e9a5554f18139e601c790c2b23c24177a74` |
| Unchanged runner, `scripts/mobile_records_empty_start_motion_response_2026_09_21.py` | `56aeb1083d9a66a5dba5ad68b625f539e67fbd9fa458e835ca4fae60ee697156` |
| Initial frozen note | `693f13683a377cbc81587122f0d4568458736c5901dfd9a0503806ff1486c890` |
| Original independent empty-start report | `fff040b1b6b3acc5929ab267fe04905bf3aed7d014b4733d615687f97a7bdb84` |
| Original geometry review | `a3aaac0298e989545c3b6b60b0eccdf6c41535c392c45894495fbf7874687739` |
| Original independent formation-intensity report | `1ed67a3f52776551660f78fc8df2358c0e4dfba9a825ecb0fb4bf08fa6bb9a6e` |

From the worktree root:

```sh
python3 scripts/mobile_records_empty_start_motion_response_2026_09_21.py
python3 .claude/science/mobile-record-empty-start-response-20260921/final_source_review/selective_checks.py
python3 .claude/science/mobile-record-empty-start-response-20260921/final_source_review/verify_fixes.py
```

The two review scripts deliberately check these source identities. A subsequent metadata-only completion reference requires a separate hash acknowledgment; it does not silently update this sealed review. `SEAL.json` records source, instruction and evidence hashes. The installed physics-claim-reviewer skill matched the pinned worktree copy; its relevant references were read from that same worktree revision. No network freshness check, source edit, Git mutation, PR action, audit action, delegation, or editable-prompt change was performed by this reviewer.
