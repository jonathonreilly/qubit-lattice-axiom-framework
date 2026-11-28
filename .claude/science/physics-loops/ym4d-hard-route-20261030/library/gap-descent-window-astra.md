# Repo search

The lead searched main and PRs 10114, 10133, 10134 and 10141 before queuing
this target. The supplied prior-work material contains no calculation of this
window descent. The target-specific prior digest is
absent at pinned `05298f1c7fea4e205a9540d1af52956afcab04a0`. I read the November 8
general digest and checked its closest hit directly: PR 10114's
`MASS_GAP_LOCAL_BLOCK_ASTRA.md`, header and lines 95–157, at
`f76f6c649cff7dffbab664d8976e680e8f287fe9`. It is a positive one-step
centered-loop witness, not a comparison of spectral gaps; the digest reports
the same blob on PR 10133. No other hit in that digest supplies this test.
A targeted `open-registry.md` search found no competing owner for this target.

Rows [1085](gap-descent-sign-2.md), [1087](gap-descent-sign-2-recompute-astra.md)
and [1088](gap-descent-sign-2-check-opus.md), read in full, already supply the
zero-charge reduction, leakage formula, independent recoupling code and
corrected scope. Their negative examples do not test beta_M=beta_T in
[2.3,2.6], beta_L>=beta_M. This row builds on those results and extends row
1087's `recompute.py`; it does not redo their completed target.

Author: Codex, dispatched as **gpt-6-astra, xhigh**, 2026-11-17.
Research text and computations: **GUIDE only**, not an audit; no status granted.
Not covered: full n=3 finite-beta_L spectra, larger boxes, continuous coupling
intervals, certified truncation errors, infinite volume, or a mass-gap proof.

## Checkpoint

Completed 2026-11-17 06:05Z, source pin 05298f1c7. All 20 required n=2 window points
have global spectra at both E180 and E200, with all eight symmetry sectors
included. The 1e-4 cutoff criterion passes. Both n=2/n=3 leakage truncations
and first detected crossing brackets are complete. Full n=3 finite-beta_L
spectra were skipped for the documented resource reason. No requested
feasible calculation remains pending. The numeric lock has been released.
Scientific MON-L and infinite-volume obligations remain untouched.

## Definition and existing inputs

Use one transverse plaquette and n longitudinal layers. For n=2 the spatial
graph is a cube with eight horizontal edges and four longitudinal edges.
Write x_p=chi_(1/2)(U_p)/2 and

    a_j(b) = I_(2j+1)(b) / I_1(b),
    K(j) = product_horizontal a_j(beta_M) product_longitudinal a_j(beta_L),
    V = beta_M sum_four_sides x_p + beta_T sum_two_transverse_faces x_p,
    T = K^(1/2) exp(V) K^(1/2),    m = log(lambda_0/lambda_1).

Gauge invariance is imposed by the spin-network basis. Common scalar
normalizations cancel from m. At beta_L=infinity the four longitudinal
kinetic factors are set to one, exactly within the retained basis.
At positive beta_T the free-sheet shortcut of row 1087 is unavailable.
BR-2 was read at `gap-bridge-exercise-opus.md:406–420`; Lemma KIN at
`gap-bridge-vectors-max.md:303–345` supplies the transfer representation.

Index-first source reads: `sa-index/README.md`, chunk-02's GL3/GL8 rows and
neighbours, `obligations.md:19–28`, then outline lines 588–599, 2195–2257 and
2313–2335. The Bessel coefficients and gauge-projected transfer construction
are existing inputs in GL3/GL8. Credit **Ethan Sussman and Levent Alpoge, with
Claude and Codex as authors of their text**. Both requested texts were fetched
once at `31a47c543775` into the new empty directory
`/tmp/sa-gap-descent-window-astra.PKRugA`. The CA-I 4.12–4.19 index was consulted;
its stage-admission material is not an input here. No claim is made from
not reading the remainder. No Balaban paper is used in this computation.
`source_receipt.json` records hashes. Current main's operating rules were read
at `8b11ae2bb95e641494fe75ed83d108ee712fa3a9`; planning supplied no science status.

## Full n=2 Wilson calculation

The basis uses normalized trivalent 3j tensors. Magnetic-index contraction
with row 1087's exact-factorial Clebsch–Gordan routine constructs multiplication
by each fundamental plaquette. Incoming indices use duality
(-1)^(j-m); the loop sign is fixed by its value +2 at identity. Multiplication
by x_p on the constant has amplitude of magnitude 1/2. The retained operator is

    T_cut = K_cut^(1/2) exp(sum_p beta_p P_cut x_p P_cut) K_cut^(1/2).

This compresses before exponentiating; it is not P_cut T P_cut and has no
certified tail enclosure. Let J bound doubled horizontal spins, H bound their
sum, and E bound sum_horizontal (2j)(2j+2). All longitudinal spins allowed by
the endpoint triangles are retained. The final cutoffs are:

| E | J | H | Full basis dimension | Largest symmetry block |
|---|---:|---:|---:|---:|
| 180 | 9 | 72 | 3,933,626 | 504,234 |
| 200 | 10 | 80 | 7,120,629 | 907,780 |

Resolve all eight characters of ring half-turn R, ring reflection S and layer
swap L. Edge reversal contributes (-1)^(2j); an odd permutation of a vertex's
slots contributes (-1)^(j_1+j_2+j_3). Signed orbit projection includes a
character when its stabilizer phases match, with normalization 1/sqrt(orbit
size). The eight dimensions sum to the full dimension. Quarter-turn
conjugation sends S to RS, pairing sectors 1 with 3 and 5 with 7. Thus six
distinct spectra cover all eight sectors, including their multiplicities.

Sparse Lanczos obtains three eigenvalues in sector 0 and the largest in every
other distinct sector. Tolerances are 3e-11 and 1e-8 respectively; any other
sector within 2% of the candidate first excited eigenvalue requires a tighter
solve. A scaled Taylor action for exp(beta sum X_p - 6 beta) stops when the
decreasing Poisson term is below 1e-20. Twelve comparisons with SciPy's
exponential action (six sectors, beta=2.4 and 4) agree to 6.8e-16.

Before comparing the final cutoffs, the declared numerical convergence
criterion was absolute change <=1e-4 in both m and Delta=m(beta_L)-m(infinity).
E160/E180 failed it (1.8042e-4 at beta=2.6), so E200 was added. E180/E200's
largest global gap change is 4.2441e-5 and largest Delta change is 1.8110e-5.
This is a GUIDE reporting criterion, not a bound on the untruncated operator.

Here beta_M=beta_T=beta. A finite m is the displayed m(infinity) plus Delta;
Delta(infinity)=0. Saved JSON includes every m and eigenvalue. Extra digits
identify the computation, not certified physical accuracy.

| beta | E | m(infinity) | Delta(8 beta) | Delta(4 beta) | Delta(2 beta) | Delta(beta) |
|---|---:|---:|---:|---:|---:|---:|
| 2.3 | 180 | 2.15808014 | 0.09932002 | 0.19549916 | 0.39919019 | 0.85020296 |
| 2.3 | 200 | 2.15807336 | 0.09932130 | 0.19550114 | 0.39919268 | 0.85020427 |
| 2.4 | 180 | 2.18206179 | 0.09450906 | 0.18222798 | 0.36113531 | 0.76026541 |
| 2.4 | 200 | 2.18204885 | 0.09451159 | 0.18223194 | 0.36114039 | 0.76026887 |
| 2.5 | 180 | 2.20940001 | 0.09264096 | 0.17493223 | 0.33463927 | 0.68659863 |
| 2.5 | 200 | 2.20937615 | 0.09264574 | 0.17493975 | 0.33464912 | 0.68660640 |
| 2.6 | 180 | 2.23786716 | 0.09322893 | 0.17284145 | 0.31885718 | 0.62953539 |
| 2.6 | 200 | 2.23782472 | 0.09323753 | 0.17285506 | 0.31887529 | 0.62955109 |

Every listed finite Delta is positive at both truncations. The minima are
+0.09264096 (E180) and +0.09264574 (E200), at beta=2.5, beta_L=20. The first
excited eigenvalue is in sector 0 at every point. The largest other-sector
eigenvalue divided by it is 0.805509 (E180) and 0.805483 (E200), so no tighter
competing-sector solve was required. Maximum recorded relative residuals
are 1.66e-13 and 3.53e-10 respectively. No window counterexample was found.

The exploratory E180 grid also includes beta=3,3.5,4 with the same beta_L
multipliers. Its minimum finite Deltas are +0.108114, +0.126516 and +0.135877.
Those absolute gaps are not converged to the window's 1e-4 criterion. No
negative Wilson-gap bracket was found on this grid, so no Wilson bisection
was performed. This does not locate a smallest negative value outside the
sampled set or exclude a missed crossing between samples.

## Heat-kernel large-t calculation, n=2 and n=3

Use row 1085's l_i=norm(P_1 M phi_i)^2/lambda_i^2 for the first contributing
heat-kernel level 3/2. Here M has identity longitudinal kinetic factors,
P_0 projects onto zero longitudinal spins, P_1 onto total longitudinal
Casimir 3/2, and phi_i are eigenvectors of P_0 M P_0. Under the simple-eigenvalue
conditions in that row, its large-t criterion is

    n_1(t)-n_0(t) = (3/2) exp(-3t/2) (l_1-l_0) + O(exp(-2t)).

The zero-charge operator is W Z_12 E_T W for n=2 and W Z_12 Z_23 E_T W
for n=3, where each layer contributes W=a_j(beta)^2. For a charged gap,
retain the inactive Z factor before the pillow contraction; the spectator
kinetic factor is a_j^4. Sum four adjacent and two opposite charged pairs,
and both longitudinal gaps when n=3. Row 1087's rational half-spin 6j squares
supply the recoupling. Eigenvectors are recomputed at beta_T=beta.

Cutoff C1=(A,D,Q)=(10,12,32), C2=(14,18,44): A input characters per layer,
D maximum doubled side-loop spin, Q class-angle sine quadrature nodes. All
output spins allowed by the retained character and side-loop labels are
included. The window results are:

| beta | n=2, C1 | n=2, C2 | n=3, C1 | n=3, C2 |
|---|---:|---:|---:|---:|
| 2.3 | 0.936371955108 | 0.936371955108 | 1.131707458946 | 1.131707458946 |
| 2.4 | 0.928210788768 | 0.928210788768 | 1.089805758690 | 1.089805758690 |
| 2.5 | 0.905244209515 | 0.905244209515 | 1.028809873241 | 1.028809873241 |
| 2.6 | 0.868288795414 | 0.868288795414 | 0.951327019551 | 0.951327019551 |

All eight signs are positive. Maximum C1/C2 disagreement is 3.2e-14.
The largest lambda_2/lambda_1 in the window is 0.947301 for n=2 and 0.979532
for n=3, so the sampled first excited eigenvalues are numerically separated.

The equal-coupling grid is beta=0.5,1,1.5,2,2.3,2.4,2.5,2.6,3,3.5,4,5,6,8,10.
Bisection of its first positive-to-negative bracket, evaluating both cutoffs
at every midpoint, gives:

| n | Positive endpoint | Negative endpoint | Endpoint l_1-l_0 at C2 |
|---|---:|---:|---:|
| 2 | 3.972358703613281 | 3.972366333007813 | +1.582563e-6 / -1.070364e-6 |
| 3 | 3.592376708984375 | 3.592384338378906 | +2.808828e-6 / -2.395914e-6 |

Maximum cutoff disagreements during these bisections are 4.3e-14 and 7.5e-14.
These are the first **detected grid crossings**, not proved smallest continuum
couplings. At beta=4, C2 gives -0.009360072073165 (n=2) and
-0.203261874026520 (n=3), with the same signs at C1. They are additional equal-coupling GUIDE-grade
counterexamples to unrestricted heat-kernel monotone descent on these boxes,
extending the failure already known from row 1085 at small beta_T.
They lie outside [2.3,2.6]. The smaller cutoff loses digits at beta=8 and 10
(up to 1.85e-4 over the full sweep); those samples are not used in the brackets.

Large t tends to the projector which is also the Wilson beta_L=0 endpoint.
The heat-kernel derivative sign does not determine the Wilson derivative:
the representation weights differ. In particular these large-t negatives
are not counterexamples on beta_L>=beta in the requested window.

## Controls, limits and failed routes

- At full J=3, sorting all eight symmetry sectors reproduces full-matrix gaps
  at beta=2.4 and 4, beta_L=infinity and beta, within 5e-16. Magnetic matrices
  are symmetric to 9e-16. These check the symmetry implementation, using the
  same plaquette contractions; they are not an independent accuracy proof.
- The beta_T=0 leakage regressions recover row 1087: n=2, beta_M=2.4 gives
  1.281922541024201; n=3, beta_M=2 gives 1.420803683208228.
- At beta_M=beta_T=2.6, beta_L=0, the separate character representation gives
  m=3.441399732399102. The cube gives 3.441466541233806 (E180) and
  3.441415393465132 (E200), discrepancies 6.6809e-5 and 1.5661e-5.
  This compares different representations with shared Bessel normalization.
- Smaller full-cube cutoffs were not accepted: (J,H)=(3,12) misses known
  beta_T=0 endpoint gaps; (5,20)/(6,22) differ by 0.00703 at beta=2.6.
  The latter run was stopped deliberately and its partial data retained.
  Full per-edge J=3 also has material cutoff error.
- A Chebyshev action trial failed its 2e-12 diagnostic tolerance (relative
  difference 1.63e-11) and was rejected. No Chebyshev value enters a sign.
  An initial standalone Taylor control loaded NumPy before thread limits;
  it was rerun with limits set first (`taylor_control_single_thread.log`).
- Early software errors from NumPy integer labels and an exit-time alarm
  were fixed before accepted runs. The first E200 build exceeded the 2 GB
  RSS guard and was stopped. A retry with blockwise symmetry checks and
  reduced temporary allocation retained every state and peaked at 1.69 GB.

Full n=3 finite-beta_L spectra were **skipped**. The uncut horizontal-spin
inventory is 5,177 states at j<=1/2, 8,424,461 at j<=1, and 2,770,335,927 at
j<=3/2, with four-valent middle-layer intertwiners. A converged extension of
this full-spin representation is not feasible within this run's 2 GB gate.
This is not a claim that all compressed or tensor approaches are infeasible.
The n=3 zero-charge/leakage calculation was completed at both cutoffs.

Production numerics ran serially, nice 10, one BLAS thread, with a 2 GB RSS
stop and a >=50% free-memory start gate. Initial memory was 86% free. The
numeric lock was acquired, refreshed and released after completion. The checkout lacked
`automation_lock.py`; the current-main copy was supplied only from scratch
through PYTHONPATH. No repository helper or science-status file changed.

## Meaning for BR-2 and saved evidence

The two numerically converged n=2 truncations find no counterexample on the
requested Wilson grid. The heat-kernel window signs are also positive. Positive
samples do not establish MON-L, control intermediate beta_L, or imply
infinite-volume descent. The outside-window heat-kernel negatives have the
limited scope just stated. No mass gap is claimed and no proof obligation is
discharged by a run.

All scripts and raw records are in `../runs/gap-descent-window-astra/`:
`cube.py`, `symmetry.py`, `exponential.py` and `guard.py` implement the cube;
`leakage.py` and `sweep_leakage.py` implement the reduced calculation;
`inventory.py` records feasibility; `collect.py` and `summarize.py` only
collect saved data. `E*_sector0.json`, `E*_other.json`, `E*_gaps.json`,
`E*_zero_control.json`, `leak_sweep.json` and `brackets.json` hold the values.
`summary.json`/`.log` collect the final comparisons. Matching logs, basis
metadata, `environment.json` and `source_receipt.json`
preserve resources, controls, failures and provenance. Large sparse matrices
and downloaded texts remain in scratch, not in the checkout.

For reproduction, `symmetry.py build --J 9 --H 72 --E 180 --basis DIR`
and the corresponding `--J 10 --H 80 --E 200` build create the final bases.
Use fresh scratch destinations. `symmetry.py run` takes `--betas 2.3 2.4 2.5 2.6`,
`--mults 0 8 4 2 1` (0 denotes infinity), `--sectors 0 1 2 4 5 6`, and a new
`--output FILE`. `sweep_leakage.py --output FILE` performs the saved leakage
grid and bisections. Acquire the lab numeric lock, run serially with nice 10,
and retain the guards. Outputs resume only against the same basis path.

RESULT: GUIDE only — no BR-2 descent counterexample on the requested n=2 Wilson grid at beta_M=beta_T=2.3,2.4,2.5,2.6 and beta_L=infinity,8 beta,4 beta,2 beta,beta; minimum finite gap difference +0.09264574 at E200, confirmed positive at E180. Large-t l_1-l_0 is positive at all four couplings for n=2 and n=3; first detected equal-coupling negative brackets are [3.97235870,3.97236634] and [3.59237670,3.59238434], outside the window. Full n=3 finite-beta_L spectra skipped for resources. MON-L remains unproved; no status or mass gap is claimed.
