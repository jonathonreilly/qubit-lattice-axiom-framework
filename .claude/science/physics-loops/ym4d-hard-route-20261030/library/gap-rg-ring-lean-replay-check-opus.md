# Check of row 1432: Lean replay of the row 1425 ring arithmetic (Opus check)

Checker: Claude Opus 5.5 (this file). Lean was not run here. The lead re-runs Lean.

## Plan

1. Read the row report, RECEIPT.md, the row 1425 note (replay obligation, final table) and its Opus check.
2. Read all non-literal code in lean/ring/Ring.lean. Compare each summary theorem with each line of the report's Stage 1 table.
3. Check the checkers for outward rounding and for vacuous tests.
4. Write a new decoder (own code) for the histogram literals. Compare every entry with groups42.txt and vacuum28.txt.
5. Recompute the division table and the degree-16 leading coefficient in exact rationals.

Scripts live in scratchpad/check1433/ (outside the repo). Witness copies in scratchpad/w1425/.

## Findings

### F0. Inputs read (done)

I read the row report, RECEIPT.md, row 1425 in full and its Opus check (row 1429). Ring.lean has 6,713 lines and SHA-256 `46c69bc4...78642`, as in RECEIPT.md. Its only import is `Init`. A search found no `sorry`, `axiom`, `native_decide`, `implemented_by`, `extern`, `unsafe`, `partial`, `opaque`, `macro`, `notation`, `instance` or `attribute`. The file has 584 theorems and 584 `#print axioms` lines. I read every non-literal definition and every theorem statement (lines 1-236, 2371-2540, 2629-2717, 4761-4830, 5098-5265, 5497-5512, 6597-6713). The witness copies have the SHA-256 digests in RECEIPT.md.

### F3. Independent decoder (done)

My decoder (`scratchpad/check1433/decode_compare.py`, own regex code) reads each `markedRowsN` and `vacuumRowsN` block in the order of `markedChunks` and `vacuumChunks`. It also checks that each block holds nothing but 9-field tuples. It compares each tuple with the matching line of the witness file: the spin key as counts of twice-spins 1..7, and the coefficient as an exact fraction and as text.

- Marked: 1,897 Lean rows, 1,897 file rows. 1,897 match, 0 mismatch. 13 zero rows in both. All 1,897 keys are distinct. The largest twice-spin is 7, so the seven-field `Hist` loses no spin.
- Vacuum: 96 Lean rows, 96 file rows. 96 match, 0 mismatch. No zero rows. The largest twice-spin is 4. This agrees with `vacuum_uses_four_spins`.
- Every Lean fraction is in lowest terms with a positive denominator. Degrees: marked 20..46, vacuum 0..28, all even. Largest arity: marked 24, vacuum 22. Marked denominators divide 6298560000. Vacuum denominators divide 9. These agree with `histogram_inventory` and `monomial_denominators`.

### F1. Statements against the Stage 1 table (done)

`finite_ring_replay` (line 6691) is a conjunction of 18 facts. Each is an earlier named theorem, so the kernel checks the same terms. I list each table line, the theorem that states it, and what the statement says.

| Table line | Theorem and what it states | Match |
|---|---|---|
| Marked core $[-25591398,-23250036]$ | `marked_core_mesh` = `MeshCover true 512 0 markedGrid`. Cells $j=0..511$ in order. Each cell is $[2+j/131072,\,2+(j+1)/131072]$ ($q=256\cdot512$, $p=2q+j$). Its 7 $\lambda_n$ endpoints and $16/\beta^4$ endpoints equal the kernel's own Taylor-plus-remainder values. Its outward histogram sum lies inside `markedCore`. The block lengths must total 512. `marked_core_extrema` shows the two ends are attained. | Yes |
| Ordinary core $[1256795084726467,1259476223854567]$ | `vacuum_core_mesh`, the same with 128 cells, prefactor 1. | Yes |
| Marked circle 216821257148, tail $\le204047/10^{15}$ from power 48 | `circle_bound_values.2.1`, `circle_lambda_inputs`, `circle_spin_sums`, `circle_convolutions`, `rootWitness`, and `(markedTail, vacuumTail) = (204047, 524181115)` with `first = 48` in the definition. | Yes |
| Vacuum circle 15466258, tail $\le524181115/10^{12}$ from power 30 | `circle_bound_values.2.2` and the same tail conjunct, `first = 30`. | Yes |
| $N$, $Z$ intervals | `total_enclosures.1`. This is **not** a conjunct of `finite_ring_replay`, which keeps only `0 < vacuumTotal.lo`. It is a separate proved theorem. | Yes (separate theorem) |
| $\mathbb E_4T$, $\Delta_4$, $g_4-1$ | `four_dimensional_division`: `fourTable markedTotal vacuumTotal 5047 = some expectedFour`, with the three intervals. `markedTotal` and `vacuumTotal` are the mesh targets widened by the tails. | Yes |
| $\mathbb E_5T$, $\Delta_5$, $2g_5$ | `five_dimensional_division`: arithmetic on $\xi=2269$, $\eta=2934$ and $b\le87/100$. `allConditionalInputs` requires exactly these $\xi,\eta$ in the four $d=5$ tables, and `all_conditional_boxes` checks them on every box. | Yes |
| Fixed-charge $[0,0]$ | `fixed_charge_scalar_arithmetic`: `⟨1-1,1-1⟩ = ⟨0,0⟩`. This statement is a tautology. It checks nothing about the ring. The report says the identification is open. | Stated, no content |
| Leading coefficient $15655/169075682574336$ | `histogram_leading_sum` (both conjuncts) and `sphere_leading_sum`. | Yes |
| Conditional $(\eta,\xi,w)$ in $d=4,5$, $Z,W_1>0$ | `conditional_input_tables` and `all_conditional_boxes`. Both are conjuncts of `finite_ring_replay`. | Yes |

Every table line has a theorem. The meaning of `finite_ring_replay` also needs five proved theorems that are not among its conjuncts or among the three theorems the report names: `histogram_inventory` (degrees $\le46$ and $\le28$, which is what "through $z^{46}$" and the tail start mean), `monomial_denominators` (without it, `d / h.den` would floor), `vacuum_uses_four_spins` (vacuum cells set $\lambda_5..\lambda_7$ to 0), `one_plaquette_band` (the $b$ interval used in $\Delta_4$, checked on all 512 cells, and $A(513/256)<2$), and `total_enclosures.1`. All five are in the file and appear in the axiom output. This is a reading defect, not a soundness defect.

### F2. Soundness of the checkers (done)

I checked each operation against its intended outward direction.

- `Bounds.sub` pairs `lo-hi` and `hi-lo`. `widen` subtracts from lo and adds to hi. `Bounds.mul112` takes min and max over the four corner products, then floors and ceils by $2^{112}$. `timesN` multiplies by a natural number only.
- `floorAt` and `ceilAt` use Lean's `Int` `/`. In Lean 4 core this is Euclidean division, so it is the floor for a positive divisor. Every divisor here is positive. A negative lower endpoint is therefore rounded down. Supporting evidence: `marked_core_extrema` asserts equality with the producer's Python-floor value on a negative endpoint.
- Series. I re-derived the Horner recurrence in `seriesAcc`. With the extra factor $(2q)^2\cdot33\cdot(n+34)$ it gives exactly $\sum_{k\le32}t_k$ over $(2q)^{n+66}33!(n+34)!$. `firstOmitted` is $t_{33}$ on that denominator. The upper value adds $2t_{33}$. The ratio $t_{k+1}/t_k\le x^2/(4\cdot34\cdot35)\le1/2$ holds for $x\le3\cdot513/256$, which is the largest argument used.
- $\lambda_n$ on a cell pairs $L_n^-(a)$ with $L_0^+(b)$ below and $L_n^+(b)$ with $L_0^-(a)$ above, with floor and ceil. $16/\beta^4$ uses $(p+1)^4$ below and $p^4$ above. `signedTerm` takes the low monomial for a positive coefficient in the lower sum and the high monomial for a negative one. All monomials are nonnegative.
- The derivative weight $6k+n(1-n)$ is split into positive and negative parts by truncated `Nat` subtraction. That split is correct. Low is pos at $p$ minus neg at $p+1$ minus $e$. High is the reverse plus $e$. Here $e=(2(198+n(n-1))+12)t_{33}(p+1)$ bounds $\sum_{j\ge0}(6(33+j)+n(n-1))t_{33+j}$ with ratio $1/2$ and $\sum j2^{-j}=2$.
- `condBox` scales all three sums by $\beta^2$. It widens each by the tail. It tests $10^4D_{hi}\le\eta W_{1,lo}$, $10^4D_{hi}\le\xi Z_{lo}$ and $wZ_{hi}\le10^4W_{1,lo}$, and requires $W_{1,lo},Z_{lo}>0$. These directions are correct. The Chebyshev recurrences for $U,U',U''$ are correct, and $U_{-1}=0$, $U_0=1$.
- Circle. $\hat b_n$, $E$, $S_0$, $P$ (plus $E^2$), $P_Q$ (plus $E^2$), $M$ and $4M_Q$ (both capped below by the $n>24$ tail), $\alpha_k$ (ceil), $E_5$ (plus $5P^4(2S_0+E)E$), the root witness ($b<r^2$, so $r\ge\sqrt b$) and the final ceilings are all outward. The ratio test for $E$ is evaluated inside `circleSpinData`.
- Even tails. `evenTail` is $\lceil sMq^f p^2/(p^f(p^2-q^2))\rceil$, which is $sM(q/p)^f/(1-(q/p)^2)$. The vacuum tail is ceiled in $10^{-12}$ units and then multiplied by 1000.
- Division. `momentCorners` takes the hull of four quotients with positive denominators, and it requires $Z_{lo}>0$. `fourTable` returns `none` unless the upper quotient is negative. $\Delta_4$ uses $87/100$ on the lower side and $136/157$ on the upper side. $g_4-1$ uses $-6\,hi$ (with $\mathbb E W\le1$) and $-6\,lo\cdot10^8/w^2$. These are correct for a negative moment.

Search for vacuous checks:

- Empty or truncated lists. `MeshCover` and `AngleCover` require the block lengths to reach 512, 128 and 2048, and they index cells by the running start. So an empty block cannot skip a cell. `AlphaCover` requires 49 entries. The `zip` in `condBox` pairs 21 coefficients with 21 jets, and the 21 is fixed by `condInput`. `condTables` has 8 entries. My script confirms: `markedGrid` is `markedCells0,2,...,510`, each with 2 cells. `vacuumGrid` is `vacuumCells0,8,...,120`, each with 8 cells. The 271 angle theorems are consecutive and match `angleBlockSizes`, which sum to 2048 with width counts 160, 48, 18, 13, 9, 8, 11, 4. The 256 and 16 cell theorems have the right start indices.
- Ties to the band. Mesh cells are $[2+j/(256c),\,2+(j+1)/(256c)]$ for $j<c$. Conditional cells are $[2+j/1024,\,2+(j+1)/1024]$ for $j=0..3$. The circle $\lambda$ uses $[512/256,513/256]$. All three end at $513/256$.
- Ignored inputs. I found none. `validCell` uses count, index and every cell field. In `angleBlock` the fine-cell containment test is always true for consecutive cells. It is harmless, and the real test is `condBox` on the parent interval.
- Tautologies. `fixed_charge_scalar_arithmetic` is one (F1). `frozen_signs` and the last two conjuncts of `finite_ring_replay` speak only about literal constants. They gain meaning only through `fourTable ... = some expectedFour` and `allConditionalInputs`, and both of those are conjuncts. `scalar_tail_ratio` is true but stands alone. No checker calls it. The $2t_{33}$ remainder relies on it in the informal reading only.
- Corrupted inputs. On `markedTotal.neg`, `fourTable` returns `none`, so the acceptance conjunct fails. The `≠` in `reject_reversed_mark` holds through that `none`, not through a second interval. Its first conjunct gives $[1829,2054]$. On a unit vacuum, `fourTable` returns a different table ($[-2580,-2304]$, which I recomputed). The histogram corruption test only touches the degree-16 coefficient. It does not show that the mesh would reject a corrupted histogram. The mesh target is the producer's hull, so a corruption that stays inside the hull would pass. This is inherent in a hull certificate. The data identity in F3 covers it.
- The file has 584 theorems, 584 `#print axioms` lines and 584 receipt lines, with the same names in the same order. I cannot confirm from files that the receipt output came from a run.

### F4. Exact recomputation (done; `recompute.py`, `pointeval.py`, `circle_own.py`, `cellspot.py`)

- Degree-16 coefficient from groups42.txt (4 rows of degree 20, $16c/(2^{d}\prod(n+1)!^{e_n})$): $15655/169075682574336$. The sphere fixture sum gives the same value. Flipping the $-160/3$ row gives $50215/169075682574336$, as the Lean file states.
- Tails: $\lceil10^{15}\cdot216821257148\,(4/11)^{48}/(1-(4/11)^2)\rceil=204047$ (and 1543100 from power 46). The vacuum tail from power 30 is 524181115 in $10^{-12}$ units. From power 28 it would be 2653666890. circle.log labels the vacuum line "tail at degree 28", which means beyond 28. The Lean file and the report both use 30.
- $N=[-25795445,-23045989]$, $Z=[1256270903611467,1260000404969567]$ (units $10^{-15}$). $N/Z\in[-2.05333\cdot10^{-8},-1.82905\cdot10^{-8}]$ gives $\mathbb E_4T\in[-2054,-1829]/10^{11}$, $\Delta_4\in[-4072,-3488]/10^{14}$ and $g_4-1\in[109,484]/10^9$. All match. From the rounded $\mathbb E_4T$, $\Delta_4$ would be $-4073$ on the low side, so the unrounded quotient matters, as the report says.
- $\mathbb E_5T=[-5148361,10296722]/(3\cdot10^8)$. Both $\Delta_5$ fractions equal the Lean literals and the report's form. $2g_5=[131133152,234433424]/10^8>13/10$.
- My own circle code (exact series, my own loops) gives a marked bound of 216821257147.39, which ceils to 216821257148, and a vacuum bound of 15466257.26, which ceils to 15466258. $P$, $P_Q$, $E$, $S_0$, $M$, $M_Q$ and $E_5$ agree with the decoded literals to 12 digits. The root witness holds.
- My own Bessel values lie inside the literal $\lambda_n$ and $16/\beta^4$ endpoints of the cells I spot-checked: marked cells 0, 1, 256, 257, 510, 511 and vacuum cells 0-7, 64-71, 120-127. Point values with my own Bessel series: $10^{15}N_{\le46}(2)=-23515769.6$ and $10^{15}N_{\le46}(513/256)=-25319141.4$, both inside `markedCore`. $Z_{\le28}$ at the two ends lies inside `vacuumCore`. Also $b(2)=0.866255>136/157$. These point values are floating-point guides, not proof.

## Defects

1. Wording. The fixed-charge row of the table is backed only by `⟨1-1,1-1⟩ = ⟨0,0⟩`. It should not stand in a column headed "kernel-checked value". Mark it "no kernel content; Stage 2".
2. Reading. The theorems the report and file header name (`finite_ring_replay` and three more) do not state the $N$, $Z$ intervals or the four auxiliary facts. Those facts are `histogram_inventory`, `monomial_denominators`, `vacuum_uses_four_spins` and `one_plaquette_band`. The summary needs all of them, and all are proved in the file. Name them, or add them as conjuncts.
3. Minor. `scalar_tail_ratio` is not wired into any checker. `conditional_input_tables` is already a conjunct of `finite_ring_replay`, so naming it separately adds nothing.

No defect changes a number or a sign.

## Not covered

I did not run Lean. The kernel result rests on the lead's re-run. I did not check the Stage 2 identifications: Bessel character coefficients, recoupling trace, completeness of the histograms, Haar sphere fixture, temporal circle bound and Cauchy remainder, conditional minimum principle, and the routing identity with the common vacuum. I spot-checked 30 of the 640 mesh cells (6 marked, 24 vacuum) against my own Bessel values. I did not recheck the conditional coefficient tables or any angle box by my own code. The kernel recomputes those from formulas I read.

VERDICT: HOLDS. The Stage 1 statements say what the table claims. The checkers round outward and are tied to the band. The Lean histograms are the witness files exactly (marked 1,897/1,897, vacuum 96/96, 0 mismatches). Two wording fixes are recommended: the fixed-charge line has no kernel content, and the summary should name five more proved theorems.
