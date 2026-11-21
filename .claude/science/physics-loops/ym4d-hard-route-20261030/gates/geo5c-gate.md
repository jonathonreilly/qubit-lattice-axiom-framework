# Gate: GEO5(c), queue row 128
Provenance: Codex (GPT-6; effort: xhigh as requested), checkout `8fac7b66059b7951e8691344c772a0c5ebef69bd`; Sussman–Alpoge commit `31a47c543775`; research text, not an audit, grants no status.

## 0. Scope and recovery checkpoint

This checks Claude's `library/geo5c-count.md`, including its stronger intermediate count and its application to `sa-2.8-terms.md` Theorem 2.8-T. Credit for the source history, frame, regions, marks, nests, profiles and determining sets: Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text. Their pinned outline was fetched once to `/tmp/sa_ym4.tex`; references below use its line numbers. All mathematical checks are written arguments; no computation is evidence of discharge. Only this report is edited.

Initial sources: `GOAL.md`; `FINISH.md` instructions and rows 118–124, 127–128; `gates/geo-gate.md`; `library/geo-5.md`; the target note and the exact GEO5(c)/Lemma W consumer. The three supplied definitions remain in force: profile (5.1), Definition A with its repairs, and the upper face-movement rule. This report checks implications under that formation data, not realizability of every history by a nonzero integration measure.

Source identities (SHA-256): target `1ca9ece86b472bbea39dcbd4aa478778bd15ba7570bec08e2672fbb5e38f0018`; outline `d7f77d4da3eb23038250c52468a341281d9ba86b4af21d3371d208a2537d4b6f`. The workflow and repository instructions were read from this commit's Git objects where absent from the sparse working tree. No planning branch or different science revision supplies a premise.

Checkpoint: complete. GC, F1–F4 and both Section 3 inequalities survive. Section 4 supplies the exact consumer transfer and a required bookkeeping correction to its order of constants. The target and outline hashes were rechecked unchanged; the checkout remains at the specified commit and this report is the only working-tree change. No mathematical check remains pending within this item. The owner's next action is the consumer's constant-order edit together with the already listed predecessor corrections, not another count lemma.

## 1. Target Section 1: statement and counterexample attack

**ADVANCE. First failing step: none.** The conclusion concerns profiles of the global **action** regions and corners carried by the global **determining** sequence. It does not assert an action-sequence cell gap for an eroded localisation. For actual profiles use the adopted (5.1), with its carrier convention and `0 <= phi <= 1`. The broader plateau assumption suffices for the count alone.

The strongest simple attack is a full drop-out with a very thin nest, viewed at its top level. Here is an admissible family for which deleting `w` is false. Take the single-creation history of `geo-prop23.md` Section 3: odd `L >= 27`, `R=L^h`, `a=1`, `k=R+1`, `h >= 4` sufficiently large, and `R_i=R` throughout. Use `r=2` and an allowed fixed slope `lambda`, with

`theta_i = exp(sqrt(R/2)) + lambda(k-i)`.

The increment is exactly `lambda(j-i)`. The logarithms lie between `sqrt(R/2)` and `sqrt(R/2)+lambda k exp(-sqrt(R/2))`; for large h their squares lie strictly between `R/L` and R. Exponential dominance here follows, for example, from `exp(z) >= z^n/n!` with any fixed integer `n>4`. Thus this is an R19 frame with rounded value R, at an arbitrarily small allowed coupling. Choose a torus larger than every specified box neighbourhood.

At step a let `C=E_a^[6]`, of side `13s_a`, and `Omega_a^c=E_a^[4]`. Thereafter choose no creations or mergers. Since `13<L` and `21<L`, the successive hulls are the central cells E_i, and

`A_i=Omega_i^{circ c}=E_i^[8]`, `B_i=Z_i^circ=E_i^[10]` (`a<i<=k`).

There are no earlier eligible operations: `t-R<1` for `t<k`. The sole component is small, quiet and quarantined. Use the alternating aligned-face recursion (3.3) of that note: one face moves exactly `m_i`, the other moves in `[m_i,(L+1)m_i)`, switching designations each time. Odd nested grids preserve alignment; every face therefore meets both the local lower gap and the adopted upper bound `K=L+1`. Summing face movements gives absolute face positions below

`13R m_a/2 + (L+3)m_i`.

Dividing by `s_i` bounds this by `13/(2L)+(L+3)/R<1/2`, so `D_i subset E_i subset A_i`. Also `13R L^(-R)<1`: induction gives `R<=2^(R-1)`, and `13*2^(R-1)<27^R<=L^R`. The final faces therefore lie within `(L+4)M` of the origin. These inequalities prove containment, alignment, gaps and the final `O(M)` size without a numerical check. Record a failure after all R stages (e.g. at the extension test): this is a drop-out, not an island.

Choose the level-k site `x=((L+6)M,0,0,0)` and a bare plaquette from it in the other two coordinate directions. Its corners lie in one level-k pillar, outside D_k with more than a block of clearance and well inside X. Thus its determining carrier has `j=k`. But for every `k-h+1 <= i <= k`, `s_i >= LM`; the centred action hole B_i has half-side `21s_i/2`, and contains the whole plaquette. All h of these adopted half-cell profiles are zero. For `i<=k-h`, the hole's half-side is at most `21M/2`, while `s_i<=M`; its distance to the plaquette exceeds M, so all remaining profiles are one. Thus the count is exactly h (and `j'=k-h`):

`count = h > 1+k-j = 1`, while `w=ceil(log_L(12R))=h+1`.

This attacks the first inequality on a genuine active window, under all three adopted rules; it does not contradict that inequality. Definition A only intersects regions. In this example the point has depth of order RM in X, whereas its tower erosion is at most `3mu`, so it also survives localisation at level k. The adopted localisation and upper face rule therefore do not remove the need for w. This is geometric admissibility; no claim of positive measure for the record is used.

## 2. Target Section 2: F1–F4

### 2.1 F1 (line 19)

**ADVANCE. First failing step: none.** R19 gives `R_i <= L R_(i+1)`, whence `s_i/s_(i+1)=R_i/(L R_(i+1)) <= 1`. The running minimum defining R also gives `R_i >= R_(i+1)`; these are different inequalities, and F3 needs the latter. Since `R_i>=1`, `M>=1`, and `xi_i>=eta`, `s_i>=M eta>=eta`. Empty/full members, periodic seams and the number of components do not enter.

### 2.2 F2 (lines 21–25)

**ADVANCE. First failing step: none.** Here is the temporal induction behind the compressed phrase “the live `Z_(t-1)`.” It must refer to the live set when step t was performed, not assert equality with a later, already filled historical member.

At step `i+1`, the top action entry `Lambda_i` equals the live entry. Earlier marks change only levels through their own tops; at a drop-out's own top `Lambda_t` is unchanged, even when all stages were completed. The step formula at SA 17320 therefore encloses this entire live set in the eight-cell enlargement forming `Omega_(i+1)^c`. The initial distance from `Z_i^act` to `Omega_(i+1)^act` is at least `8s_(i+1)`.

Induct on all later events. Ordinary steps leave old members alone. An action-choice drop-out restores the old entries in its window, and changes nothing else. Healing fills both members in its component Q. An island at t fills `Omega_(i+1)` and `Lambda_i` when `i+1<=t`, since `i<t`, even though it retains `Lambda_t`. Thus only filling can introduce a new small-field point q into the later member. It removes every earlier action hole in Q.

Any surviving hole z paired with q is outside Q. Before step t, nesting put the earlier action holes in its live input `Z_(t-1)`; intervening operations at t can only remove such holes. Hence z was in `Omega_t^{circ c}` when the step was formed. Its cell and two-cell neighbourhood form a connected subset of the pre-operation live `Z_t` (SA 17321); if that neighbourhood touched Q, it would belong to Q. Consequently `d(z,Q)>=2s_t>=2s_(i+1)`. This argument uses the pre-operation padded set, so a later filling does not erase its justification. It handles simultaneous components by the same pairwise argument. Distances and connectivity are periodic, and any older mergers are already in the live input. Induction proves F2 for every finite history, not just for one quiet lineage.

### 2.3 F3 and the definition of w (lines 15, 27–35)

**ADVANCE. First failing step: none.** Write `a=t_flat=t-R_t`. SA 6098–6105 restores the former regions exactly on `(a+nu,a+n]`; SA 17417–17440 gives the same prescription with its Lambda and S qualifications. In particular the determining/action discrepancy of **Omega** is confined to `(a,a+n]`, including `j=t` if `n=R_t`. It is not confined to `j<t`: only the top **Lambda** entry is excluded from replacement. Confusing these two top-entry rules would wrongly set w to zero in the stress configuration above.

For a site x in determining layer j, let `j'=max{l<=j:x in Omega_l^act}`, with the stated zero convention. Nesting and `D_l subset Omega_l^{circ c}` give `Omega_l^act subset Omega_l^det`.

**Case 1.** If no standing drop-out containing x is active at j, the two Omega entries agree *at j itself*. Thus `x in Omega_j^act`, `j'=j`, and nesting gives every lower action membership. This is a shorter proof of line 31. Its older-window argument is also consistent: a surviving old mark remains in the live set; subsequent drop-outs cannot expose its points above its top, because quarantine puts it in their retained cores. A subsequent healing or island which could remove that obstruction erases the mark. No sum over older windows is needed.

**Case 2.** At most one standing mark containing x has j in its completed window: mark levels in a later eligible component are strictly below its window's lower endpoint. For that unique Y, determining membership gives `x in Y minus D_j`. Since `C=D_a subset D_j`, x is outside C. Every older standing mark in Y belongs to the live lineage at a and is contained in C; it cannot affect this x. Every younger standing mark meeting Y contains Y and has lower window endpoint strictly greater than t; it changes none of the levels `l<=j<=t`. Disjoint marks change no entry at x. These facts justify the “only Y's entries matter” sentence, even with arbitrarily many older marks and earlier mergers.

For `l<=a`, the entries at a in Y are unaffected by any mark window. Hence `Y minus C subset Lambda_a^act subset Omega_l^act`. This proves the lower branch of line 34, including `j-w<=a`.

For `a<l<=j-w`, quietness gives actual single boxes

`B_u=H_u^[10]`, `A_u=H_u^[8]`, `H_u=hull_u(B_(u-1))`, `B_a=C`.

In each coordinate a cell hull extends a box face by at most `s_u`; the ten added layers extend it by `10s_u`. Iteration, then `R_u<=R_a`, gives

\[
 A_l\subset B_l\subset C+[-\tau_l,\tau_l]^4,\qquad
 \tau_l=11\sum_{u=a+1}^{l}s_u
 \le11R_a\sum_{u=a+1}^{l}m_u
 <\frac{11L}{L-1}R_a m_l\le12R_a m_l.
\]

The strict inequality is the finite geometric-series inequality; it remains strict at `L=12`. The use of a hull is legitimate because the class requires one box throughout the quiet window, not an arbitrary disconnected core at these levels.

Independently, the local lower gap moves **every** face of D_u outwards by at least `m_u`. On carriers this follows from the common face grid: a smaller increment would be at most `m_u-m_(u-1)`, giving site distance at most that plus eta, less than `m_u` under the adopted sizes. Thus

\[
 D_j\supset C+[-\sigma_j,\sigma_j]^4,\qquad
 \sigma_j\ge\sum_{u=a+1}^{j}m_u\ge m_j.
\]

Since `w=ceil(log_L(12R_a))`, `j-l>=w` implies
`m_j=L^(j-l)m_l >=12R_a m_l>tau_l`.
Therefore `A_l subset D_j`, whereas x is outside D_j. It follows that `x in Omega_l^act`. Combined with the lower branch, this proves `j'>=j-w`; if `j-w<0` it is already implied by `j'>=0`.

This proof uses the **lower** face movement; an unusually large admissible D_j only improves the inclusion. The supplied upper face rule is satisfied by the stress example but is not needed for F3. Definition A neither changes the global action profiles nor enters this proof. Non-wrapping lifts are used only for the class box Y and its contained nests; no lift of a global wrapping complement is assumed.

**History endpoints.** If `n=0` there is no completed window and w is zero. At `j=a` the unchanged entry gives w zero. At `j=a+n` the second case applies, including full completion. Above `a+n` that mark's entries agree and the first case applies unless a different mark is active at j. Healing and islands remove swallowed marks and fill the appropriate entries. Thus neither many disjoint components nor repeated nested standing marks require a sum of w's. The exclusion of older marks is a consequence of `x notin C`, not merely of disjoint window intervals.

### 2.4 F4 and C_1 (lines 37–39)

**ADVANCE. First failing step: none.** Put `q=k-u`, `y_u=min_(i<=u) theta_i`. If a minimiser of `y_k` occurs at or before u, `y_u=y_k`. Otherwise choose such a minimiser v with `u<v<=k`; R19 gives
`y_u<=theta_u<=theta_v+Bbar(v-u)<=y_k+Bbar q`.
Thus `log y_u <= log y_k+log(1+Bbar q)`, since `y_k>e>1`.

For `z>0`, `z^(1-1/r)<=1+z`: for `z<=1` it is at most 1, and for `z>=1` it is at most z. Hence
`d(r z^(1/r))/dz=z^(1/r-1)>=1/(1+z)`.
Integrating from zero (both functions are continuous there) proves `log(1+z)<=r z^(1/r)` for real `r>=2`. Convexity then gives

\[
 (\log y_u)^r
 \le2^{r-1}\big((\log y_k)^r+r^r\bar Bq\big).
\]

Rounding upward to a power of L gives `R_u<L(log y_u)^r`, also at an exact power, while `(log y_k)^r<=R_k`. Consequently

\[
 R_u<L2^{r-1}(R_k+r^r\bar Bq)
 \le C_1(1+R_k)(1+q),\qquad
 C_1=L2^{r-1}(1+r^r\bar B).
\]

This is uniform in u, k and all histories; it uses the auxiliary frame, not an identification with the running coupling. It allows threshold crossings of R. In particular it does not reuse the false `R_a<=2R_k` bound repaired in `geo-5.md`.

## 3. Target Section 3: proof of GC and C_4, d_0

**ADVANCE. First failing step: none.** Alignment makes each determining pillar a whole level-j block contained in layer j: both adjacent members are unions of blocks of that size. Hence its chosen plaquette corner x_0 is in that same layer. For `1<=i<j'(x_0)`, nesting gives `x_0 in Omega_(i+1)^act`, so F2 and the at-most-eta sup-distance from x_0 to the plaquette give

\[
 d_\infty(p,Z_i^{act})\ge2s_{i+1}-\eta
 \ge s_{i+1}\ge s_i.
\]

Every such profile equals one. Only indices in `[max(1,j'),k]` can be counted. If `j'=0`, this set has k members, still at most `1+k-j'`; otherwise it has exactly `1+k-j'`. F3 proves the first claimed bound `count<=1+k-j+w`. For `j=0`, the trivial `count<=k` also settles the assertion. No nearest-hole or same-mark assumption is made about the other corners; F2 bounds distance to the **entire** action complement.

Check the constants separately. Set `A=1+R_k`, `H=1+k-j`, `c=log_L C_4`. In the active-window case `j<=t<=k`, `a=t-R_t>=0`. F4 first gives

\[
 R_t\le C_1AH,\qquad
 1+k-a=1+k-t+R_t\le H+C_1AH\le(1+C_1)AH.
\]

A second application gives `R_a<=C_1(1+C_1)A^2H`. With the printed `C_4=12C_1(1+C_1)` and `ceil z<=z+1`,

\[
 w\le1+c+2\log_L(1+R_k)+\log_L(1+k-j)
 \le1+c+2R_k+(k-j).
\]

The last inequality uses `log_L(1+z)<=z`: integrate `1/((1+z)log L)<=1`, valid for `L>=12`. Thus the count is at most `2H+2R_k+c`; the note's `2H+2R_k+1+c` is a harmless extra unit. Since `AH>=H`, `AH>=R_k`, and `AH>=1`, that printed bound is at most

\[
 [2+2+(1+c)]AH=(5+\log_L C_4)(1+R_k)(1+k-j).
\]

Here `c>0`, because `C_1>=L2^(r-1)>1`. This checks **exactly** the stated `d_0=5+log_L C_4`; no enlargement or integer rounding of d_0 is needed. If w is zero, `H<=d_0AH` immediately. The constants depend only on `L,r,Bbar`, not on M, the face-bound K, volume, history length, the mark count, or the position of a frame threshold.

## 4. Target Section 4: the actual 2.8-T consumer

**ADVANCE for the consumer implication; CORRECT-NO-ADVANCE for the provenance/status bullet. First failing mathematical step: none.** There is one order-of-choice correction to the printed consumer, stated below. No analytic implication is promoted by this gate.

**Exact weight.** GC applies to the healed label because healing is one of the fates included in F2–F3. Its action profiles are precisely those defining v in `sa-2.8-terms.md` Section 1 and Lemma W(4), not the prepared weight also denoted w there. Distinguish that weight from GC's integer window allowance. With the adopted `0<=phi_i<=1` and FLOW's `|b_i|<=B_*`,

\[
 |v(p)-x|=\left|\sum_{i=1}^k b_i(1-\phi_i(p))\right|
 \le B_*\#\{i:\phi_i(p)<1\}
 \le B_*d_0(1+R_k)(1+k-j_h(p)).
\]

This proves W(4), and also the absolute-value bound needed if the summation estimate is applied to `|v|(1-chi)`. No positivity of each increment b_i is assumed. The plateau alone proves GC; the range `[0,1]` used in this algebra comes from the supplied profile (5.1), not from GC's broader standalone plateau hypothesis.

**Exact level in R_1.** W4 compares the global prepared and healed backgrounds outside Lambda, where their members and rows agree by EXT-out. Its intermediate joined sequence is the adopted meet. Write `j_h(x)` for a corner's healed determining layer and `j_m(x)` for its meet layer. Definition A gives `Omega_q^meet subset Omega_q^h`, hence `j_m(x)<=j_h(x)`. Taking the minimum over the four corners, as required by the consumer's finest-pillar assignment, preserves this inequality:

`j_m(p)=min_x j_m(x) <= min_x j_h(x)=j_h(p)`.

Thus GC's bound with `j_h(p)` implies the same bound with the actual summation level `j_m(p)`. It is uniform over every plaquette carried by any particular meet top. The proof does **not** recompute the profiles on eroded regions, and it does not claim F2's cell gap for the artificial tower. The upper face rule supplies other geometric estimates already used by 2.8-T; GC neither consumes nor replaces them.

For `x>=1`, this gives exactly

`|v(p)|(1-chi(p)) <= x(1+B_*d_0)(1+R_k)(1+k-j_m(p))`.

On the support of `1-chi`, all action plaquettes lie in the common prepared/healed domain: the symmetric-difference plaquettes are in the inner region where chi is one, by the existing EXT-out repair. Consequently the above is the weight bound used in `sa-2.8-terms.md` 5.5, with the same power **one** of `1+k-j`. Its already stated decay and Lemma BC summation therefore receive exactly the same factor `(1+B_*d_0)(1+R_k)` and the displayed R_1 estimate is unchanged. There is no extra window sum, volume factor or loss of the decay rate.

**One concrete consumer correction.** `sa-2.8-terms.md` Section 6 currently chooses d_0 in step 2 and r in step 4. With this explicit d_0 that literal ordering is backwards. Move the choice of d_0 (and its local auxiliary constants C_1 and C_4) to immediately after `r` and the frame slope bound `Bbar` have been fixed, still before step 5's coupling ceiling. No earlier choice of M or other geometry uses the newly explicit d_0, so this is a complete repair, with no circular dependence or changed estimate. The GC constant C_4 is unrelated to the analytic response constant called C_4 in the consumer's step 1; qualify it as `C_4^GC` there. These are instructions for the owner, not edits made to that file. The earlier consumer corrections listed in `geo-gate.md` Section 6 item 3 remain necessary.

**Scope wording.** “At every plaquette, on the whole torus” means every *carried plaquette in the action's field domain*, uniformly in the torus; `Omega_0` need not be the whole torus, and no pillar top is defined in an excluded bare hole. GC has that correct carried-plaquette quantifier. It also does not prove the different stored-collar/history sum at SA 21021–21023 (`sum_j #_j(Z_j^+)`); that sum is not GEO5(c) and is not read in this consumer step.

## 5. Disposition

| Target section / statement | Verdict | First failing step |
|---|---|---|
| Section 1, GC and its w | **ADVANCE** | None |
| Section 2, F1 | **ADVANCE** | None |
| Section 2, F2 | **ADVANCE** | None; event times made explicit above |
| Section 2, F3 | **ADVANCE** | None; full top window included, older marks excluded by the core |
| Section 2, F4 and C_1 | **ADVANCE** | None |
| Section 3, both inequalities, C_4 and d_0 | **ADVANCE** | None |
| Section 4, W(4) and R_1 implication | **ADVANCE** | None in the estimate; move d_0 after r in the consumer's choice order |
| Section 4, provenance/status recap | **CORRECT-NO-ADVANCE** | None; it supplies no mathematical premise or status |

GEO5(c), the profile-count input to 2.8-T, is proved under the stated formation rules. The stress example shows that its window allowance cannot simply be deleted, even under all three adopted definitions. The geometric proof covers arbitrary finite histories, components, allowed mergers, interrupted stages, standing marks, and periodic geometry as detailed above. This resolves queue row 128's mathematical question; it does not close I1–I5, FLOW, any further RG step or a global Yang–Mills result. No audit, status change, commit, push, PR, external post, subagent, numerical proof or other file edit is part of this work.
