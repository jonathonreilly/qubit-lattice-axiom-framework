# Repo search

The lead searched main and PRs 10114, 10133, 10134 and 10141 before dispatch.
The target-specific prior digest is absent at pinned `bc343b5d6`. I read the
November 8 general digest in full. Its closest hit is PR 10114's
`MASS_GAP_LOCAL_BLOCK_ASTRA.md`, read at lines 1–18 and 95–157 at
`f76f6c649cff7dffbab664d8976e680e8f287fe9`. It gives a positive one-step
centered-loop correlation, not a comparison of spectral gaps. Its blob was
rechecked; the digest reports the same source on PR 10133. It does not supply
this test. Searches of `open-registry.md`, `open-core.md` and `l17c.md` found
no competing owner for the target.

[Row 1089](gap-descent-window-astra.md), read in full with every Python script,
already supplies the n=2/n=3 window signs and brackets. Those results are
reused. This work extends its leakage code and its trivalent Wilson basis;
it also reuses row 1087's exact-factorial Clebsch–Gordan and squared-6j code.
Row 1085 supplies the zero-charge and charged-pillow reductions. No earlier
result is claimed as new.

Author: **Codex, gpt-6-astra, xhigh (dispatch identity)**, 2026-11-17.
Research text: **GUIDE only**, not an audit; no scientific status granted.
Not covered: a numerically converged n=3 Wilson endpoint comparison, certified
truncation errors, intermediate couplings, larger transverse cross-sections,
infinite-volume descent, or a mass-gap proof. Author controls are not an
independent review. No run discharges a proof step.

## Outcome and checkpoint

**GUIDE:** all twelve new heat-kernel window signs are positive at both
cutoffs. The first detected crossings move down through n=6 but stay above
3.41645. **OPEN:** the limiting trend and Wilson (MON-L). The two n=3 Wilson
truncations also give positive endpoint differences throughout the requested
grid, but **FAILS:** their declared 1e-4 convergence test.

Completed 2026-11-17 07:34 UTC,
source pin `bc343b5d672fd4f07c66ec39247981322f110f18`. The requested finite
truncation grids and bisections are saved. n=7 was not started because of the
memory inventory below. The Wilson convergence obligation remains open.

## Box, operators and credited inputs

The spatial graph is the open box {0,1} x {0,1} x {0,...,n-1}, with an
infinite transfer direction. It has 4n horizontal edges, 4(n-1) longitudinal
edges, n transverse plaquettes and 4(n-1) side plaquettes. All vertex gauges
are imposed. Thus n=3 has 20 edges and 11 spatial plaquettes.

Use x_p=chi_(1/2)(U_p)/2 and a_j(b)=I_(2j+1)(b)/I_1(b). The Wilson operator is

    K = product_horizontal a_j(beta_M) product_longitudinal a_j(beta_L),
    V = beta_M sum_side x_p + beta_T sum_transverse x_p,
    T = K^(1/2) exp(V) K^(1/2),    m = log(lambda_0/lambda_1).

At beta_L=infinity, every longitudinal kinetic factor is one. This is a
Wilson endpoint calculation. It is distinct from the heat-kernel large-t
calculation, whose limiting projector is the Wilson beta_L=0 endpoint.
**A heat-kernel sign does not determine the Wilson sign.**

Index-first reads: `sa-index/README.md`, chunk-02's GL3/GL8 and neighbouring
rows, and `obligations.md:19–28`; then outline lines 588–599, 2195–2257 and
2313–2335. GL3 supplies the Bessel coefficients; GL8 supplies the
gauge-projected transfer construction. Credit **Ethan Sussman and Levent
Alpoge, with Claude and Codex as authors of their text**. Their outline and
complete account were fetched once at `31a47c543775`, into the new empty
`/tmp/sa-gap-descent-n-trend-astra.VKVSv4`. The CA-I 4.12–4.19 index concerns
stage admission and supplies no input to this calculation. No Balaban paper
is used. Hashes and source revisions are in `source_receipt.json`.

BR-2 was read at `gap-bridge-exercise-opus.md:406–420`; row 1085's reductions
at `gap-descent-sign-2.md:36–52,95–118`; row 1087's `recompute.py` in full.
Current-main operating rules were read at `8b11ae2bb95e641494fe75ed83d108ee712fa3a9`.
Planning supplies no science status. This is the dispatched GUIDE probe.

## Heat-kernel method and window values

Keep row 1089's cutoffs C1=(A,D,Q)=(10,12,32) and C2=(14,18,44).
A is the retained character count per layer, D the maximum doubled side-loop
spin, and Q the class-angle sine-quadrature count. For the first contributing
longitudinal Casimir level 3/2, use its formula

    l_i = ||P_1 M phi_i||^2 / lambda_i^2,
    n_1(t)-n_0(t) = (3/2) exp(-3t/2) (l_1-l_0) + O(exp(-2t)),

with the simple-eigenvalue qualifications of row 1085. This run supplies no
analytic verification of those qualifications for the untruncated operator.

The zero-charge operator is W [product_(s=1)^(n-1) Z_(s,s+1)] E_T W,
with W=product_layers a_j(beta)^2. Sequential quadrature eliminates a site
only after including its adjacent Z factors. At most two angle axes remain
live; spectator blocks are streamed. This reorders finite sums without
changing row 1089's finite quadrature operator.

For a charged gap, omit only that gap's Z factor before the pillow map. Keep
all other Z factors and every spectator weight a_j^4 in the squared norm.
Sum four adjacent and two opposite charged pairs, then all n-1 gaps.
The active-pair map B can be evaluated directly or by H=B^T B, including
its output kinetic weights and multiplicities. The direct and Gram norms
were compared during the n=6 repairs and at the final window control.

All entries below have beta_M=beta_T=beta. Digits identify the calculation;
they are not certified physical error bars.

| n | beta | C1 l1-l0 | C2 l1-l0 |
|---|---:|---:|---:|
| 4 | 2.3 | 1.184967904781 | 1.184967904781 |
| 4 | 2.4 | 1.115477880353 | 1.115477880353 |
| 4 | 2.5 | 1.026870679312 | 1.026870679312 |
| 4 | 2.6 | 0.923816900388 | 0.923816900388 |
| 5 | 2.3 | 1.192479157136 | 1.192479157135 |
| 5 | 2.4 | 1.102571124440 | 1.102571124440 |
| 5 | 2.5 | 0.996949178446 | 0.996949178446 |
| 5 | 2.6 | 0.881706127217 | 0.881706127217 |
| 6 | 2.3 | 1.182262909474 | 1.182262909474 |
| 6 | 2.4 | 1.079589307486 | 1.079589307487 |
| 6 | 2.5 | 0.966580552947 | 0.966580552947 |
| 6 | 2.6 | 0.848900543438 | 0.848900543438 |

Maximum window cutoff disagreement: 1.101e-13.
The largest sampled lambda_2/lambda_1 in this window is
0.998868204940; this is only a numerical separation.
No window counterexample was found in this form.

## First detected crossing versus n

The grid is row 1089's
0.5,1,1.5,2,2.3,2.4,2.5,2.6,3,3.5,4,5,6,8,10.
For each new n, the sweep stops at its first detected positive-to-negative
pair, [3,3.5]. Both cutoffs are evaluated at **every midpoint** until width
<=1e-5. These are detected grid crossings, not proved smallest continuum
couplings; a missed crossing between earlier samples is not excluded.

| n | Positive endpoint | Negative endpoint | C1 endpoint signs | C2 endpoint signs |
|---|---:|---:|---:|---:|
| 2 (row 1089) | 3.972358703613281 | 3.972366333007812 | +1.5825630e-06 / -1.0703645e-06 | +1.5825630e-06 / -1.0703644e-06 |
| 3 (row 1089) | 3.592376708984375 | 3.592384338378906 | +2.8088279e-06 / -2.3959145e-06 | +2.8088279e-06 / -2.3959145e-06 |
| 4 | 3.470840454101562 | 3.470848083496094 | +2.6984656e-06 / -3.1107307e-06 | +2.6984657e-06 / -3.1107308e-06 |
| 5 | 3.429191589355469 | 3.429199218750000 | +3.8672225e-06 / -1.9705743e-06 | +3.8672225e-06 / -1.9705743e-06 |
| 6 | 3.416458129882812 | 3.416465759277344 | +4.0313716e-06 / -1.7610033e-06 | +4.0313716e-06 / -1.7610033e-06 |

The maximum C1/C2 disagreement over the new accepted bisection points is
3.885e-12. The measured decreases become
smaller and the brackets remain above 2.6. This is compatible with leveling
off above the window. **OPEN:** whether the limit does so; no extrapolation
or fitted limit is a result. Only the displayed brackets are measured.
The negatives at beta=3.5 are outside the requested window and concern only
the heat-kernel form. They are not Wilson endpoint counterexamples.

At n=7, C2 has 105,413,504 character states. Three double-precision retained
eigenvectors alone require 2,529,924,096 bytes. The conservative full-workspace
estimates are 2.528 GB (C1) and 25.741 GB (C2). The gate therefore rejects n=7
before allocation. This is a limit of this representation, not of tensor
compression or every possible method.

## Wilson n=3: feasible retained spectra, failed convergence

The middle four-valent invariant couples the two horizontal spins to r,
the two vertical spins to r, and the channels to a normalized singlet.
The lower and upper vertices reuse row 1089's trivalent contractions.
A side plaquette changes the affected middle channels by ±1/2; a transverse
plaquette preserves them. Every allowed choice is included.

J bounds doubled horizontal spins; E bounds sum_horizontal (2j)(2j+2).
All longitudinal spins and middle channels allowed by the vertex triangles
are retained. No symmetry sector is omitted. The two computed cutoffs are:

| J | E | States | Nonzero magnetic entries |
|---:|---:|---:|---:|
| 4 | 44 | 689,478 | 22,051,432 |
| 4 | 48 | 1,233,578 | 41,501,888 |

As in row 1089, T_cut=K_cut^(1/2) exp(beta sum_p P_cut x_p P_cut) K_cut^(1/2).
This compresses before exponentiating; it is **not** P_cut T P_cut and has
no certified tail enclosure. A shifted Taylor action and sparse Lanczos give
the three largest retained eigenvalues. Maximum recorded relative residual:
1.176e-12. The declared convergence criterion was absolute change <=1e-4
in both m and Delta=m(beta_L)-m(infinity).

Delta(infinity)=0. Each finite m is m(infinity) plus the displayed Delta.

| beta | E | m(infinity) | Delta(4 beta) | Delta(2 beta) | Delta(beta) |
|---|---:|---:|---:|---:|---:|
| 2.3 | 44 | 2.006477428 | 0.336889756 | 0.689139615 | 1.331289533 |
| 2.3 | 48 | 1.991585757 | 0.325463785 | 0.659986949 | 1.273202118 |
| 2.4 | 44 | 2.053927661 | 0.310793866 | 0.634762233 | 1.238795160 |
| 2.4 | 48 | 2.041930847 | 0.301954197 | 0.609118200 | 1.173110607 |
| 2.5 | 44 | 2.105439314 | 0.288982846 | 0.588182130 | 1.157784778 |
| 2.5 | 48 | 2.095675524 | 0.282939223 | 0.566903908 | 1.085653192 |
| 2.6 | 44 | 2.159977966 | 0.270744303 | 0.548492312 | 1.087814591 |
| 2.6 | 48 | 2.151801123 | 0.267481643 | 0.532005600 | 1.010238697 |

All finite differences are positive at both cutoffs; the smallest is
+0.267481643. **FAILS (numerical convergence
criterion):** the largest gap change is 0.085752737 and
largest Delta change is 0.077575894, exceeding 1e-4.
These are retained-matrix GUIDE values, not a numerically converged Wilson
answer. No window negative is present at both cutoffs, so no requested
Wilson GUIDE counterexample is claimed. **OPEN:** the untruncated endpoint
comparison.

The inventory is broader than row 1089's uncut counts: it records horizontal
Casimir cutoffs at J=1,2,3,4. For example, J=4,E=80 already has 159,591,505
states; J=4,E=100 has 1,471,428,971. The full J=3 basis has 2,770,335,927.
An optimistic order-16 point-group dimension bound is saved separately.
No symmetry-reduced eigensolver, longitudinal-transfer eigensolver, or
low-rank tensor solver was implemented here; none is declared infeasible.
The present full sparse representation was actually run at the two stated
cutoffs. A more accurate Wilson calculation remains additional work.

## Controls, rejected routes and resource record

- The streamed contraction matches a separate full quadrature tensor at
  n=4,A=3,Q=9, including every omitted gap. A single n=3,beta=2.4 regression
  checks the extension against row 1089; it is not new evidence for that row.
- Four-valent intertwiner norms, every plaquette matrix's symmetry and its
  vacuum-to-loop amplitude were checked. Freezing the upper layer reproduces
  the 63-state J=1 trivalent cube matrix exactly up to explicit basis phases.
  The J=1 Taylor action agrees with SciPy's exponential action to 5.6e-16.
  The row-block assembly was checked again after the memory repair.
  Restricting the E48 magnetic matrix to all 689,478 E44 states reproduces
  the earlier E44 matrix with maximum recorded entry difference zero.
- Two early n=6 eigensolver outputs failed explicit residual checks and were
  rejected. Enlarging the Krylov space and using kinetic-weighted random
  starting data retained all character states.
- A post hoc reflection scan rejected n=6 C1 at beta=0.5 and C2 at beta=1
  and 3.416015625. Their mirror-gap defects were 3.18e-9, 1.99e-6 and 2.27e-6.
  Later failing evaluations were stopped. Rejected JSON and logs remain.
  Direct-map/Gram comparisons and reflection checks validate the replacements.
  The cause of the sporadic defects was not conclusively isolated. During
  troubleshooting, periodic SIGALRM checks were replaced by synchronous
  peak-RSS checks between numerical operations; the 2 GB stop remains.
  No causal claim about the timer or numerical library is made.
- The final n=6,beta=2.6 C2 control uses both norms and the revised guard.
  Its change from the saved window value is
  +0.000e+00; its mirror defect is
  4.452e-13. All accepted samples pass the final
  reflection scan. No control is a proof or an independent review.
- The first E=48 Wilson build stopped at a conservative allocation gate.
  The accepted retry saves individual faces and assembles bounded row blocks,
  without deleting states or changing entries. Peak accepted Wilson RSS was
  1.755988 GB; peak accepted heat-kernel RSS was
  1.992770 GB.

Jobs ran serially under the successfully acquired lab numeric lock, launched
with `nice -n 10`. The final control records effective niceness 20; launch
increments can include inherited niceness, so exact effective nice 10 is not
claimed. All six BLAS/OpenMP thread environment variables were set to one;
the runtime thread-pool inventory was empty, so it did not independently
measure the effective thread count. The 2 GB peak-RSS stop remained enabled.
Each process checked the >=50 percent free-memory start gate; the initial
reading was 86 percent. The numeric lock was released after the final controls.
The missing
`automation_lock.py` helper was supplied from current main through scratch
PYTHONPATH; no repository helper was changed. No queue, registry, audit or
science-status file was edited.

All scripts and raw records are in `../runs/gap-descent-n-trend-astra/`.
`leakage.py` and `sweep.py` implement the large-t calculation; `wilson.py`,
`wilson_inventory.py` and `wilson_sweep.py` implement the Wilson attempt.
`sweep.json`, per-point JSON, `wilson_J4E44.json`, `wilson_J4E48.json` and
`summary.json` contain the accepted values. Failed and rejected records are
explicitly named. `final_controls.py`, its logs, `environment.json` and
`source_receipt.json` preserve controls and provenance. Large matrices and
downloaded sources remain in scratch. To reproduce a point, acquire the lock
and run `leakage.py --n N --beta B --cutoff A D Q --output NEWFILE` with nice 10.
For Wilson, use `wilson.py build --J 4 --E E --basis NEWDIR`, then
`wilson.py run --basis NEWDIR --output NEWFILE`. Use new destinations.

RESULT: GUIDE — no window negative at both cutoffs for n=4,5,6 heat-kernel leakage; first detected brackets are [3.4708404541,3.4708480835], [3.4291915894,3.4291992188], [3.4164581299,3.4164657593], all above 2.6. n=7 exceeds this representation's memory gate. n=3 Wilson differences are positive at E44/E48 but fail the declared convergence criterion. MON-L and the infinite-volume trend remain OPEN; no proof step or mass gap is claimed.
