# Independent all-stage finite-graph review

2026-09-21. **No unresolved mathematical or implementation finding at the
source identities below.** The corridor construction, all nonfull geometric
connectivity, fixed-graph joint rare-birth law, counting bound and conditional
two-level comparison hold under the stated premises. This is selective
mathematical scrutiny, not a formal audit, retained-status decision or new
physical-emergence claim.

## Read boundary and identities

The complete candidate note was read before either new author checker or its
outputs. `PRE_COMPARISON_DERIVATION.md`, an independently written checker and
its complete results/logs were fixed by `PRE_COMPARISON_SEAL.json`, SHA-256
`e1cdf112190c195c6fd9d30298a244dde2db62c521716ffbe586361cd66d3cea`.
Only after that seal were the complete author checker and its corridor helper
read, and their results/logs parsed and authenticated. The note remained
unchanged. Earlier independently checked premises were reused by identity.

| Reviewed source/evidence | SHA-256 |
|---|---|
| `GEOMETRIC_ALL_STAGE_FORMATION_CLOCK.md` | `e7d47eb97d62fad65153d377bc19257ebcc2ff8aa1b0f0c5027a5424afe0eabd` |
| `geometric_all_stage_check.py` | `e75dde7de0a9570e58a4b10f1bea076548a0fe7ba369fc44c38cfaf925c1f560` |
| `geometric_corridor_transport_check.py` | `76ac19c67cd1d9d1c724f88f49a36c990524a5ee955a52058af4292c933d7f0c` |
| `geometric_all_stage_checks/RESULTS.json` | `6f2c10b01bc606ebc4a2fc385c7cef66f61a19e1de5a374963705e77f8bca8fc` |
| `GEOMETRIC_ALL_STAGE_RUN.log` | `288fbcde014367be1a48957697f52c4cdbd5ebecfa6e0e2f377c7df912517b03` |
| preliminary corridor `RESULTS.json` | `50537d09948e1ce4317ba5d1ccd81532b44d7b48d254496db700002f07e3c645` |

The full source/dependency/artifact bindings are in `FINAL_SOURCES.json` and
`FINAL_SEAL.json`; the stderr source is empty. No primary source was edited.
The note's prospective evidence paragraph records its pre-review status; this
report supplies the completed reconstruction without changing that frozen text.

## Load-bearing reconstruction

**Geometry.** For any reference matching T, contract its occupied edges and
retain uncovered vertices as singleton nodes. On a simple quotient path,
each segment with s empty singleton sites moves an actual pair backwards in
s+2 slides. The total is 2(r-1)+s_total <= V-2. Intermediate states are parents
T-e or T-e-f+g; the simple-path construction prevents repeated transitions.
The inverse restores every immutable record ID. Virtual reference edges are
never physically inserted.

For M in Omega_j and a fixed perfect P, M symmetric-difference P has exactly
K-j P-augmenting paths and alternating cycles. Align the paths first, leaving
a vacant P edge. Transport that vacancy to one M edge of each remaining cycle
using T=M+h, then align the cycle in r-1 slides. The resulting j-edge subsets
of P connect by the same parent construction. This proves irreducibility for
all j<K, including the empty singleton. It does not prove marked-state
ergodicity or connect distinct full matchings with vacancy slides.

**Arbitrary hazard and stage composition.** With A the birth incidence and
h=A1, every upper matching has j+1 parents. Thus pi A=p U and
p=(j+1)a_(j+1)/a_j>0, even when h vanishes at individual lower states. For an
exit event, write the killed solution u=c+v, pi v=0. Its centered equation
and 0<=u<=1 give ||v||_infinity <= beta m B; the constant equation gives
|c-U(D)| <= ||v||_infinity. This verifies Eq. (5), including cancellation of
p from the denominator. Adding lambda beta p to the killing gives precisely
Eq. (6). For w=beta p E tau, pi(hw)=p and
||w-1|| <= 2 beta m B ||w|| give Eq. (7), after finiteness of the finite-chain
mean is established. No constant-hazard premise is being smuggled in.

Uniformity over entrance states allows strong-Markov composition of the finite
stage kernels. With arbitrary nonnegative stage parameters s_j, each limiting
kernel is the uniform exit row times p_j/(p_j+s_j). Interposed geometry-event
diagonals show independence of all successive post-birth geometries and scaled
waiting times in the joint limit. Uniform conditional mean convergence,
separately from weak convergence, yields C(G)=sum_j 1/p_j. The geometric rates
must remain autonomous; correlated immutable contents do not themselves alter
them in the supplied model.

**Counting and ordered volume statement.** For an augmenting component Q,
(M,P,Q) maps to (U,W)=(M symmetric-difference Q,P symmetric-difference Q).
W has exactly two holes, the endpoints of Q. Within U symmetric-difference W
they recover Q, then M and P. Hence
(K-j)a_j Z <= a_(j+1)a_(K-1), and summing the reciprocal rates gives

    R/K <= C(G) <= 2 R H_K/(K+1).

The named Taggi input is reused from the unchanged prior clock review, with
even torus side N>=4, fixed d>2, unweighted all-sector counts and the checked
positive-time-return convention. Its statement and hypotheses had been
verified against the pinned v3 PDF; its full proof was not independently
reproved here. The factor V=2K gives the displayed bounds on C(G)/V without
a factor-of-two error. The order remains beta->0 at each fixed graph, then
volume. It does not provide a fixed-beta upper bound or a limiting coefficient.
No Dagum--Luby theorem or fixed-distance-from-maximum quantitative estimate
was imported.

**Two-level comparison.** The lemma is checked for 1<=j<K, k=j+1, consistent
with the previously defined S_j. In unnormalized undirected energies, the
lower exchange energy is D_slide+U, the cross-level energy is U/k, and the
upper-level energy is at most 2mU/k. The last bound uses the unique common
parent of adjacent upper states and at most m neighbors through each parent.
For any physical transition, its oriented moving edge identifies reference
matchings of the forms M+e or (M-g)+e+f. Both orientations give at most
2(m+m^2) candidates. Length <=V-2, no repeated transition and k(k-1)/2
unordered parent pairs therefore give

    U <= (V-2)(m+m^2)k(k-1)D_slide,
    C_(V,m,k)=1+(V-2)(m+m^2)(k-1)(k+1+2m).

The lower-level uniform mass appears in both the Dirichlet normalization and
the variance lower bound and cancels, proving gap(S_j)>=gap(B)/C. The auxiliary
chain is connected, but a polynomial volume bound on its gap remains an
explicit open input. Its nonlocal comparison exchanges are not events of the
physical record process.

## Independent controls and comparisons

The sealed precomparison program covers ten fixed graphs: paths 4,6,10;
cycle 4; diamond; complete 6; two triangles joined by a bridge; triangle with
a tail; two squares joined by a bridge; and the cube. Its independent matching
enumerator/slide actions were reused from the earlier sealed general-graph
checker. New code constructs the corridor, marked forward/inverse replay,
all-stage incidence matrices, counting injection and growing-chain kernels.

- Every one of the 21 nonempty nonfull layers is connected. There are 698
  independently constructed unordered parent routes and 3,389 injection
  triples with exact inverse reconstruction.
- Exact rational matrix identities verify lower exchange = slide + U,
  cross energy = U/k, and the complete compressed auxiliary form. Numerical
  eigenvalue/PSD controls support the analytic inequalities; they are not
  presented as exact eigenvalue proofs.
- Twenty-four exact rational killed-resolvent rows test two beta values,
  with two nonzero transform parameters and arbitrary exit events recovered
  by positive/negative row sums. Intermediate hazards include 0 through 3.
- Symbolic multistage products use different parameters at different stages
  and intervening post-birth geometry events. With kappa=1, examples are

      C4:      beta E T_total = 5/4,
      diamond: beta E T_total = (beta+29)/20,
      path6:   beta E T_total =
        (30 beta^3+228 beta^2+398 beta+157)/[20(3 beta^2+7 beta+3)].

  Their limits are 5/4, 29/20 and 157/60. The diamond is a direct countercontrol
  to interpreting C(G) as an exact finite-beta formula.
- The path-ten witness T={01,89} requires eight slides, attaining V-2.
  One intermediate-level slide is used by nineteen reference matchings in
  the chosen routing. Thus the earlier near-perfect two-reference bound
  cannot silently be reused here; the new larger bound covers this case.
- Disconnected disjoint edges leave a disconnected one-pair slide chain;
  a star with no perfect matching cannot reach full packing. These retain
  the connectivity/perfect-matching hypothesis boundaries.

After sealing, `compare_author.py` authenticated all four author group files
against the combined result, all declared source hashes and the complete log.
The reported preliminary 842 graphs/115,062 paths, and final 24,333 counting
graphs/2,291,317 injections, are authenticated author receipts, not independently
replayed exhaustive computations. I independently rebuilt all 42 final
connectivity graph inventories and selected seven stage matrices. Twenty-eight
selected author alignment routes were replayed by the independent marked
implementation, including a nonbipartite bridge example, plus the length-eight
corridor. All agreed.

A separately assembled complete transient growing generator reproduced exactly
all twelve stored whole-clock mean and Laplace rows on cycle4, paw4, cycle6
and irregular6 at beta=1,1/100,1/1000000. This assembly did not use the author's
recursive stage equations. The author runner uses kappa=1 consistently and
does not add its auxiliary comparison events to the physical generator.

## Failures, reproduction and limits

The precomparison check passed on its first run. The first postcomparison
helper run failed because it tried to concatenate tuple matching layers with
a list. Its source, complete traceback and receipt are preserved under
`failed_attempt_01/`. Replacing that bookkeeping operation with a flattening
comprehension fixed it; no source theorem, primary runner or numerical target
changed. The corrected run passed with empty stderr.

The runnable sources are `independent_check.py` and `compare_author.py`.
The first deliberately refuses to overwrite its sealed result; to reproduce
it, copy that source into a new sibling evidence directory so its unchanged
relative dependency resolves and retain all new outputs there. To reproduce
the comparison without overwriting this evidence, use another new sibling
directory containing both scripts and copies of the nine precomparison
artifacts plus their seal. The pre-seal authentication deliberately continues
to bind the absolute original artifact paths. Python, NumPy and SymPy are
required. Neither invokes
the author suite's main routine or writes to primary sources. All logs remain
on disk.

The conclusions concern a supplied classical matching process. The limits
require fixed finite G and fixed positive kappa before beta tends to zero.
Added conservative channels must preserve symmetric autonomous geometric rates
for the stationary-kernel argument to apply. No all-stage polynomial schedule,
fixed-rate thermodynamic law, total-clock sharp asymptotic, marked-state
ergodicity, quantum implementation, phase theorem or propagating field is
established by this review. There are no requested source corrections.
