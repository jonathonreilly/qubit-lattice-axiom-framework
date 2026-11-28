# geo-5: the remaining geometric premises (queue row 124)
Provenance: Codex (GPT-6; effort: xhigh), checkout `c4de0c76afd2eb380fc7792f2dc3facaba1b62f4`; Sussman–Alpoge commit `31a47c543775`; research text, not an audit, grants no status.

## 1. Scope, adopted results and notation

This item tests GEO2, GEO4, GEO6 and the W3 nest clearance consumed by `sa-2.8-terms.md` §3 and Lemma W and by `meet-6c.md`. It moves the geometric input of the A3/Proposition 2.8 route: a proof makes that geometric premise available under the adopted definitions; a counterexample requires the consumer to use the proved narrower statement instead. No analytic background theorem or scientific status is supplied.

Credit: the source regions, class, preparation, healing, histories, nests and weighted metrics are due to Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text. SA line references below are to their `YM4_sketch_500.tex` at the pinned revision, fetched once to `/tmp/sa_ym4.tex`. The broad literature record is `lit-large-field.md` §0; the targeted source for this item is that outline. No computation discharges any assertion.

The four predecessor reports were read in full, in bounded excerpts. Adopt and cite, without redoing: the half-cell profile `geo-prop23.md` (5.1); the upper face-movement rule and size/count consequences of `geo-2.md` §6; formation compatibility, EXT-out and the restriction lemma of `geo-3.md` §§2, 4–5; and the corrected GEO1 and two-domain consumer formulation of `geo-4.md` §§3–6. Localisation means Definition A of `assign-adopt.md`, including the explicit cut-meet convention, `mu=M_1'>=rho`, the collar separation and test-grid extension repaired in `../gates/a2-full-gate.md`. These are supplied definitions, not uniqueness claims about the outline's qualitative wording.

Write `a=k-N_k`, `R=Rcheck_k=N_k`, `xi_i=L^(i-k)`, `m_i=M xi_i`, `s_i=M Rcheck_i xi_i`, `C=X intersect Z_a`, and `D_i=Z''_i(X)`, with `D_a=C`. The final box `Lambda` is `D_k` plus one level-k M-layer. Distances use the periodic sup metric; box face estimates use cubical carriers, with site conventions stated where needed. A component crossing a chosen fundamental-domain seam is treated on its allowed local lift; no lift is imposed on a wrapping complement. Constants are fixed before the coupling floor and are independent of the number of components, the depth and the history.

## 2. GEO2 — PROVED

**Attack.** Several eligible components could have unbounded total volume, and an old merger could have arbitrarily many ancestors. Neither is the set counted by GEO2: its `X` is one *current eligible component*. A merger during `(a,k]` is expressly excluded. A merger at or before a, a deep nest and a long earlier history are allowed, but the resulting component must still pass the size test at k. Wrapping around the chosen coordinate seam cannot increase a cell count, and a genuinely wrapping class box is excluded by the torus floor. Thus the potential counterexamples all reduce to whether “small” is a fixed cutoff or a cutoff varying with the history.

SA 17575 explicitly defines the class by containment in a cube of `O(1)` level-i cells, including at `i=k`. As in `geo-3.md` §2, denote this fixed construction cutoff by `b_box`. Fix

\[
 n_X=\lceil b_{\rm box}\rceil+2.                 \tag{2.1}
\]

**Proof.** On the allowed lift, let Q be a containing cube of side at most `b_box s_k`. In one coordinate, an interval of this length meets at most `ceil(b_box)+2` intervals of the partition of mesh `s_k`: after discarding its two possible end pieces, the remaining intervals have disjoint interiors of length `s_k`. Every cell of X has its four coordinate intervals among these four lists. Hence X contains at most `n_X^4` level-k cells. Projection to the torus identifies cells and cannot add any. The same constant applies separately to every component, independently of its ancestry. This proves GEO2 as worded. It uses the class definition, not an unproved assertion that free evolution makes every large component small. QED.

**Consumers.** A level-k cell contains exactly `(MR)^4` sites of the level-k lattice, using the fixed half-open grid convention. Therefore the number of level-k tops in X is at most `(n_X MR)^4`. This is precisely the first summand in `K_X` and the count in §5.2 of `sa-2.8-terms.md`. Under `supp chi`, corrected GEO1 removes the artificial outer localisation layers; the non-top-level nest contributions are counted by `geo-2.md` (6.2), not by multiplying this estimate by the depth. W3's collar lies in the removed inner margin when that count is used. `meet-6c.md` needs only the per-component geometry and its allowed lift; no argument there sums GEO2 over all components without a separate summation estimate.

## 3. GEO4 — PROVED for the admissible formation data

### 3.1 What is local input, and what is to be proved

The source's **local** minimum-gap requirement on an admissible stage nest is retained, exactly as in rows 118–122:

\[
 D_{i-1}\subset D_i\subset X\cap\Omega_i^{\circ c},\qquad
 d_\infty(D_{i-1},D_i^c)\ge m_i.                \tag{3.1}
\]

Here the circle denotes the pre-operation regions. This is the one-M-cube-of-the-later-level requirement in SA 6073–6078 and 17398–17407; `geo-2.md` §4 explicitly includes it in geometric admissibility. `geo-3.md` §2 proves that such nests with the adopted upper face bound exist for every eligible component. We retain this local lower requirement separately from the adopted upper bound and do not replace the supplied nests by a particular recursion. The task here is to pass from these **local box gaps** and the explicit step/fate formulas to all global, retained, localised and joined sequences. In particular, the global conclusion of Proposition 2.3 is not assumed in that passage.

The box bound in (3.1) can be read on carriers even if the source gap is first stated on bare sites. Opposite consecutive faces belong to the common face grid of mesh `m_(i-1)`, including `D_a=C`. Each face increment is therefore an integer multiple of `m_(i-1)`. If it were smaller than `m_i=L m_(i-1)`, it would be at most `m_i-m_(i-1)`; the distance between the corresponding site sets is at most this increment plus eta, strictly less than `m_i` since `m_(i-1)>eta`. This contradicts the site gap. Thus every face increment is at least `m_i`, giving the carrier version. The first-rule tower's strict site gap likewise gives a carrier gap at least `rho xi_i`: both boundaries lie on the common `mathfrak M xi_i` face grid and `rho xi_i` is a multiple of its mesh. In a cut meet, use the finer common face grid of all its factors; its mesh is at least eta and still divides `rho xi_i`. A carrier gap smaller than that threshold would give a site gap at most the threshold, contrary to the strict inequality. This is the non-strict carrier bound used in weighted path lengths below.

**Attack.** A thin nest can attain (3.1), so the proof may spend no extra fraction of a cell there. At the end of a partial preparation the next member is still an old step region. At the beginning it may meet arbitrary old nests. Filling one of several components can bring its newly added small-field points near another component's holes. Earlier mergers can make those holes disconnected, and repeated fillings might appear to consume the gap. Finally a cut tower is constant above its cut, so the elementary intersection argument alone cannot prove its higher gaps. These are the cases addressed below. No separation between *distinct live components themselves* is presumed.

Choose the fixed lengths as in corrected GEO1, with `M>rho>=2`, `mu>=rho`, `M>=80mu`, `L>=27`, and `theta min(M,rho)>=64 log L`. All distances in the following set arguments are periodic. Empty later members have infinite distance and cause no exception.

### 3.2 The padding fact and the ordinary step

Just after step t, the live large-field set contains the two-cell enlargement of `Omega_t^c` (SA 17319–17325). Enlarging by failures and boxing only increases this set. Consequently, if Q is a component of this live set and z is in `Omega_t^c` outside Q, then

\[
 d_\infty(z,Q)\ge2s_t.                         \tag{3.2}
\]

Indeed, the cell containing z and its two-layer neighbourhood are a connected subset of the live set. If this neighbourhood met Q, z and Q would be in the same component. Any point at distance less than `2s_t` from z lies in that neighbourhood. This proves (3.2) on the torus, including across a fundamental-domain seam. Also, inside a quiet class component, the literal formulas `Omega_t^c intersect Q=H_t^[8]` and `Q=H_t^[10]` give

\[
 d_\infty(\Omega_t^c\cap Q,Q^c)\ge2s_t.       \tag{3.3}
\]

The latter uses the admitted box lift; the former requires no box or lift for the outside component. Every old hole at an earlier level is contained in the live set of level `t-1`. The new step puts its hull and eight level-t layers into `Omega_t^c`. Thus the new last gap, from any such old hole to `Omega_t`, is at least `8s_t`. All earlier members are unchanged. At the initial level, `Omega_0=Omega_1` enlarged by one level-1 cell layer gives `d(Omega_0^c,Omega_1)>=s_1`. This is at least `LM xi_0`. These facts initialise and extend the induction below. They hold whether failures or boxing merge lineages, since those operations only enlarge the new excluded set.

### 3.3 Induction through every fate and every stopping choice

Keep, for each consistent action/stage choice, the inclusions

\[
 \Lambda_i\subset\Omega_i,\qquad
 \Omega_{i+1}\subset\Lambda_i,                 \tag{3.4}
\]

and the gaps between consecutive determining members at least `M xi_i`. The mixed gap from `Lambda_i^c` to `Omega_{i+1}` is also at least `M xi_i` whenever the later member exists. At an ordinary step it is at least `8s_(i+1)` by §3.2. “Consistent” is essential: this assertion does not pair a stored action member at one level with an independently selected determining member at the next.

Suppose an operation at t acts in Q, with `b=t-N_t`. Its core is `C_Q=Q intersect Z_b`. Quietness and quarantine mean that the members with `b<i<=t` in Q before this operation are the quiet step boxes; older marks in Q have level strictly below b. For a stop after n stages, the changed members inside Q are `Q minus D_i`, `b<i<=b+n`; the other entries remain the old ones, with the top action member retained in a drop-out as specified at SA 17423–17430. Check a pair of adjacent levels as follows.

* Below b both members are unchanged. At the lower splice, every old hole in Q at level b is contained in `C_Q=D_b`; (3.1) separates it from `Q minus D_(b+1)` by `m_(b+1)`.
* Within the prepared interval the holes are `D_i,D_(i+1)`, so (3.1) gives exactly the needed `m_(i+1)=LM xi_i`. This also proves the inclusions (3.4) there.
* At the upper splice the newly retained hole `D_(b+n)` is a subset of the old hole. The next member is unchanged. Restricting the former hole cannot reduce its distance from that member. It also preserves (3.4). If the stop reaches t, there is no next member at this moment; the next ordinary step is covered by §3.2.

These checks concern two points in Q. Two points outside every operated component retain their old gap. For a pair with just one point in Q, only two new cases need checking. A newly added small-field point in Q is compared with an old hole outside Q; that hole lies in the pre-operation `Omega_t^c`, and (3.2) supplies `2s_t`. A retained hole in Q is compared with a newly added small-field point in another component; the retained hole lies in `Omega_t^c intersect Q`, and (3.3) supplies `2s_t`. Both bounds exceed `M xi_i` for `i<t`. The same argument works simultaneously for any number of operated components.

Healing fills Q in every member. Island formation fills it in every determining member through t and in every action member below t; `Lambda_t` retains Q as a hole. Inside Q there is then no earlier hole to compare with a new small-field point. The cross-component cases are precisely (3.2)–(3.3). At the retained top action hole of an island or drop-out the next step again surrounds the entire live set, so no special subsequent splice is omitted. Changes to `Omega_0` are fillings of the same Q; the argument applies to the first gap as well. Thus all three fates preserve the induction.

An older merge, however complicated, has already been handled as an ordinary step. It changes the interior history of `C_Q`, which the current operation leaves untouched. A merge inside the quiet window is inadmissible by the class definition. Nested standing marks have disjoint windows at each point (quarantine, SA 17440). Changing a standing drop-out's stopping choice from n to `nu<=n` leaves its entire level-t live component Q in `Z_t`; it changes only the stored/stage entries described above. Subsequent hulls and cell enlargements depend on that live set and the recorded failure cells, so replaying those same recorded choices gives the same later live sets. The component sizes, creations, operation levels and quarantine decisions are consequently unchanged. Thus every stopping vector is treated by the same geometric induction; one does not assume its gaps by quoting Proposition 2.3 for a purported alternate history. No proof step subtracts a margin per event: every newly exposed pair receives the current box gap or current step padding. Induction on the finite record proves the assertions for arbitrary history length, for the action choice, the determining choice and every retained intermediate choice. Alignment is preserved by hulls, cell layers, boxing, unions in the aligned component Q and replacement by the aligned `D_i`. Intersections of two nested aligned grids are unions of their finer common cubes.

### 3.4 Full towers and localisations

For the first tower rule its defining admission inequality gives
`d(T_i^c,T_(i+1))>rho xi_i`. For the second it gives
`d(T_i^c,T_(i+1))>=mu xi_(i+1)>rho xi_i`.
For a full meet `B_i=O_i intersect T_i`,

\[
 B_i^c=O_i^c\cup T_i^c,\qquad
 d(B_i^c,B_{i+1})
 \ge\min\{d(O_i^c,O_{i+1}),d(T_i^c,T_{i+1})\}.
                                                               \tag{3.5}
\]

The strict `>rho xi_i` follows because `M>rho`. This also treats the first domain, holes of arbitrary shape, disconnected parts, the test-grid extension and wrapping complements. It proves (SEP) for the full localisations in X. The upper erosion estimates and (SEP-L) are the adopted results of `geo-4.md` §3, not consequences of (3.5).

### 3.5 Cut meets

For completeness here is the step that (3.5) cannot do by itself. Let a part A have collar level j, and let its whole inside collar of width `5mu xi_j` be in the parent's layer j. Write `F_q=T_(min(q,j))(A)`. The proved erosion bounds give

\[
 T_j^c\subset A^c\cup S,\qquad
 S\subset\{x\in A:d(x,A^c)\le e_j\},\qquad
 e_j\le\rho\xi_j\ \text{or}\ 3\mu\xi_j.       \tag{3.6}
\]

For `q<j` use (3.5). At `q=j`, a point of `O_(j+1) intersect A` has depth at least `5mu xi_j`, so its distance from `A^c union S` is at least `(5mu xi_j-e_j)>rho xi_j`. At `q>j`, a shortest path from `x in O_(q+1) intersect A` to `A^c union S` encounters a point of the inside collar, hence of `O_q^c`. The portion from x to that point has length greater than `rho xi_q` by the parent's gap. Therefore its endpoint, and every point of `T_j^c`, is farther than `rho xi_q`. Combining with the other complement `O_q^c` proves the cut-meet gap at every level. This argument applies to shortest periodic paths as well as paths on a local lift.

Above the cut, (3.6) and the collar exclusion give `O_q intersect T_j=O_q intersect A`. A parent aligned cube crossing the boundary of A would meet its forbidden inside collar, so cannot belong to `O_q`. Thus the intersection is still a union of whole parent cubes. Below the cut alignment follows from the nested grids. For multiple parts apply the same argument to each complement separately and take the minimum in (3.5). The adopted separation `(n_sep-n_col)mu>max(rho,3mu)`, with counts 9 and 5, ensures that other tower factors do not alter a given part's collar. This is the repaired cut-meet statement; no zero gap is assigned to a frozen factor.

The actual W1/W2 and W4 collars satisfy this single-layer condition by corrected GEO1 and `geo-4.md` §§3–4. For W3, `X minus C` belongs to every member through a, by (3.4) and `C=X intersect Z_a`. Its inside collar of width `(5mu+2)xi_a` misses `O_(a+1)`, since (3.1) at `a+1` separates C from that member by `LM xi_a>(5mu+2)xi_a`. The collar remains farther than `3mu+3` from `X^c`, by corrected GEO1 and `C subset D_k`. Localisation therefore leaves it in layer a, including its row-carrier margin. This verifies the collar input without yet using the full/cut identification addressed in §5.

### 3.6 Quantitative conclusion and consumers

Global label, action and prepared sequences have gap at least `M xi_i`. Every tower, full localisation and joined sequence has strict gap `>rho xi_i`. Thus GEO4 holds with the **common** constant `c_g=min(M,rho)`, and with the stronger constant M before a tower is intersected. It does not say that a tower-created layer retains gap M. The fixed floor `theta c_g>=64 log L` is exactly the one in the question's consumer.

For Lemma BC of `sa-2.8-terms.md`, take a path from a layer-j top to `E subset O_k`. For each `i=j+1,...,k-1`, take its last point outside `O_i` before its first subsequent entrance into `O_(i+1)`. That segment is in layer i, has physical length at least `c_g xi_i`, and hence weighted length at least `c_g`. The segments occur in increasing order and are disjoint: each next last-exit time is no earlier than the preceding first-entrance time. Summation gives `d_B(y,E)>=c_g(k-j-1)_+`, independently of holes, detours or wrapping. This is the exact quantitative read in BC; its remaining lattice count and geometric series are unchanged. In particular `theta' c_g/2>=16 log L` for `theta'>=theta/2` as required there. The same gaps and aligned members supply Lemma MJ, `meet-6c.md` Lemma G(c), J*, Proposition 5.1 and Theorem M, retaining their analytic inputs. The first gap is strict `>rho eta`, so the two-domain restriction lemma of `geo-3.md` §5 applies wherever its separate multiplier hypothesis holds. QED.

## 4. GEO6 — PROVED in a stronger set form; Lemma W checked

### 4.1 Attack and the old-core containment

**Attack.** The serious candidate is an old drop-out whose *action* hole was not replaced by its much smaller determining hole. Repeating such marks, or merging their lineages before a, might leave old action profiles outside the core read by the current operation. It would be invalid to identify those two sequences. There is also a different candidate: an old profile may have a long transition width even when its hole is contained in C. The first is settled by the following containment; the second needs the separate width calculation in §4.3. Several components and a seam-crossing lift do not change either argument.

**Claim.** For every old action index `1<=i<=a`, using the action choice of the same history,

\[
 X\cap\Lambda_i^c\subset C,
 \qquad X\cap(\Omega_i\setminus\Lambda_i)\subset C.     \tag{4.1}
\]

**Proof.** Apply (3.4) to the action sequence, not to a mixture of action and determining members. Iteration gives `Lambda_a subset Lambda_i` for `i<=a`, hence `Lambda_i^c subset Lambda_a^c`. At level a the action and determining entries agree **inside X**: every standing mark in X has level strictly below a, and its stored/stage choice changes only entries through its own level. The current preparation changes only levels strictly above a. Operations outside X change no entry at a point of X. Therefore `X intersect Lambda_a^c=X intersect Z_a=C`. Intersect the preceding inclusion with X to obtain the first assertion. The second follows from `Omega_i minus Lambda_i subset Lambda_i^c`. This proof applies unchanged if arbitrarily many older marks occur inside C or were swallowed earlier. It uses no assertion that their action and determining holes coincide. QED.

Thus the set content of GEO6 is true with no extra adjacent layer: the indicated old holes and strip pieces are already in C. Describing the bound as “core together with the first shell” is a harmless weaker enclosure; C itself is not asserted to lie in the shell with C removed. Since `C subset D_k subset Lambda`, the final containment required by GEO6 follows.

### 4.2 Exact profile equality outside Lambda

For `i<=a`, preparation leaves the action member unchanged and healing adds X, so its difference is exactly `X intersect Lambda_i^c`, contained in C by (4.1). For `a<i<=k`, the preparation formula gives

\[
 (\Lambda_i\cup X)\setminus
       [\Lambda_i\cup(X\setminus D_i)]
   =D_i\setminus\Lambda_i\subset D_i\subset\Lambda.      \tag{4.2}
\]

Writing an equality with all of `D_i` is unnecessary; the displayed inclusion suffices even when a determining box and a stored action entry are distinguished. The prepared member is contained in the healed one. Thus their symmetric difference at every action level lies in Lambda. The half-cell profile lemma of `geo-prop23.md` §5 gives equality of the profiles farther than `s_i/2` from Lambda. Since `Rcheck_i<=L Rcheck_(i+1)`, iterating gives `s_i<=s_k=MR`. Therefore `v=w` at carrier distance greater than `MR/2`, and in particular at the consumer's distance greater than `3MR/4`. The site convention with `C_p=3/4` is the alternative already proved in that lemma. Corrected GEO1 then gives `(v-w)(1-chi)=0`. This proves the GEO6-dependent step in Lemma W(2), hence preserves `R_2=0`. Lemma W(1), giving `R_4=0`, needs only that every healed action region contains X and the same plateau rule, so is unaffected.

### 4.3 The margin and the rounded-scale constant

Lemma W(3) also needs old profiles to be one on `supp phi`. Its printed intermediate estimate `Rcheck_a<=2R` is not valid merely from a bounded frame slope: rounding to powers of L can cross one threshold. This is a defect in that intermediate estimate, not in (4.1) or in the conclusion of W(3).

Here is an explicit scalar refutation of that estimate. Fix an allowed positive slope `lambda<=B_*`, a power `R=L^h`, `a=1`, `k=R+1`, and set

\[
 H=\exp(R^{1/r}),\qquad
 x_i=H+\lambda\bigl(R/2+a-i\bigr),\quad 0\le i\le k.
                                                               \tag{4.3}
\]

The frame is decreasing, so its running minimum at i is `x_i`. It has `x_a=H+lambda R/2>H` and `x_k=H-lambda R/2<H`. For large h, `(log x_k)^r` is strictly between `R/L` and R, whereas `(log x_a)^r` is strictly between R and LR. To check this without asymptotic numerical evidence, choose an integer `n>r`; `exp(t)>=t^n/n!` implies `R/exp(R^(1/r))` tends to zero. Hence `x_a/H` and `x_k/H` tend to one, and their logarithms differ from `R^(1/r)` by a quantity tending to zero; the distances from `R^(1/r)` to the adjacent thresholds `(R/L)^(1/r)` and `(LR)^(1/r)` tend to infinity. Their signs are fixed by `x_a>H>x_k`. Thus the rounded values are exactly `Rcheck_k=R` and `Rcheck_a=LR>2R`. The increment bound and FLOW's lower bound on the running minimum both hold. This refutes only the quoted scalar estimate; no new geometric configuration is needed for it.

Use instead the already proved frame estimate `geo-3.md` (2.4)–(2.5):

\[
 \check R_a\le D_R R,\qquad D_R=L2^r.             \tag{4.4}
\]

For `i<=a`, monotonicity of the physical cell sides gives
`w_i<=C_p s_a<=C_p D_R R m_a`. Let `n_c=floor(R/2)` and use the consumer's actual margin, the core plus shells `a,...,a+n_c-1`. Its carrier is `D_(a+n_c)`. If a bare plaquette belongs to `supp phi`, at least one corner is outside this box. Its midpoint is within eta of that corner, whereas C is at distance at least `m_(a+n_c)` from the box complement by (3.1). In particular, allowing both site/carrier and midpoint conventions gives the weaker convenient bound

\[
 d_\infty(p,C)\ge m_{a+n_c-1}-2\eta
              \ge\tfrac12 m_{a+n_c-1}.         \tag{4.5}
\]

The last inequality follows from `M>=8` and `a+n_c-1>=0`. A complement point of an old action member is either inside X, hence in C by (4.1), or outside X. The former is farther than `w_i` by (4.5) if

\[
 L^{n_c-1}>4C_pD_R R;                          \tag{4.6}
\]

the latter is at distance at least `3MR/4>=w_i` by the definition of chi and `s_i<=MR`. The adopted half-cell rule equals one also at its plateau endpoint. Thus every old profile is exactly one on `supp phi`.

Condition (4.6) is a coupling floor, not a change of cutoff or an extra history hypothesis. For an explicit sufficient floor take the odd power R with `R>=13` and `R>4C_pD_R`, in addition to the floor of (4.4). For odd integers `R>=13`,

\[
 L^{(R-3)/2}\ge3^{(R-3)/2}\ge R^2.
\]

The second inequality starts at `3^5=243>13^2=169`; increasing R by two multiplies its left side by 3, while `(R+2)^2/R^2<=225/169<3`. This proves it by induction, and proves (4.6) with the stated floor. There are exactly R remaining action indices, `a<i<=k`; each contributes at most `B_*` in absolute value. Consequently

\[
 |w(p)-x|\le B_*R\quad(p\in\operatorname{supp}\phi),     \tag{4.7}
\]

which is W(3) and the input to §5.6 (`R_5`), with its conclusion unchanged. W(4) is the separate GEO5(c) counting read and is not inferred from GEO6.

### 4.4 Remaining consumers of the containment

In `meet-6c.md` Lemma G(b), W3 requires `X minus C subset O_a`; this follows from `Omega_a^c subset Lambda_a^c` and the equality at a used in (4.1). It does not require any geometric simplicity of the action holes *inside* C. Lemma C(c) then excludes exactly the core rows; the shared shell datum and the exterior datum are the ones already checked with EXT-out in `geo-4.md` §6. The two-domain LM formulation retains `J_X subset C` and hence the absence of deleted plaquettes on `supp phi`; no filling of the prepared domain is introduced. These are all the uses of the old-core enclosure in the two named consumers. The only consumer change found here is replacement of W(3)'s factor 2 by the proved `D_R`, with (4.6); its four conclusions survive.

## 5. W3 nest gap — PROVED, including the full/cut identification

### 5.1 Attack and the clearance

**Attack.** At the thinnest permitted nest the adjacent-box gap has exactly its minimum. If C has inherited many marks, distance to the nearest old hole is irrelevant: W3 needs distance to the whole old **core**. A larger number of shells could conceivably erode away all room for an uncut tower. Also, on the torus a path may leave X or pass another component, so a clearance proved only inside X would be insufficient. The following proof uses the latest adjacent-box gap, not a sum whose constant could deteriorate with depth; it treats the exterior explicitly.

For every `a<q<=k`, for the global prepared sequence and hence its localisation in X,

\[
 \boxed{\ d_\infty(C,O_q^p)\ge M\xi_q,
 \qquad d_\infty(C,(\mathcal L_X O^p)_q)\ge M\xi_q.\ }   \tag{5.1}
\]

**Proof.** Inside X, `O_q^p=X minus D_q` and `C subset D_(q-1)`. For any `c in C` and `z in O_q^p intersect X`, (3.1) therefore gives `d(c,z)>=m_q`. For `z outside X`, use `C subset D_k subset Omega_k^{circ c} intersect X` and the two-cell padding (3.3): `d(c,z)>=2s_k>=m_q`, since `xi_q<=1` and `R>=1`. These exhaust the global member. Taking an infimum gives the first inequality; localisation only removes points, giving the second. The argument uses periodic distances. The torus floor permits the local box estimates in (3.1) and (3.3), so a coordinate seam creates no shorter unexamined route. Arbitrary other components remain in the exterior case. Every standing earlier mark of this lineage is inside C, and every later box contains C, so neither old merges nor the number of old marks enters. QED.

### 5.2 Equality of full and cut meets

Put `A=T minus C` and `B=mathcal L_X O^p`. Use the first-rule recursion for A in absolute levels, and, for the purpose of the full-meet comparison, continue that same recursion through k. The elementary erosion induction of repaired Definition A applies at each additional level: it uses only the recursion and the initial set, not a stopping index. Thus

\[
 \{x\in A:d(x,C)>e_q\}\subset T_q(A),\qquad
 e_q\le\rho\xi_q.                              \tag{5.2}
\]

The initial set A is a union of the fine grid cubes, since C is a union of level-a cells. No assertion that A is a union of level-k cells is needed to define this continuation. For `q>a`, (5.1) and `M>rho` give `B_q subset T_q(A)`. Tower nesting also gives `B_q subset T_a(A)`. Consequently

\[
 B_q\cap T_q(A)=B_q=B_q\cap T_a(A)\quad(q>a).    \tag{5.3}
\]

For `q<=a` the cut and full recursions use the identical member `T_q(A)`. Hence at every level, including zero,

\[
 B_q\cap T_q(A)=B_q\cap T_{\min(q,a)}(A).        \tag{5.4}
\]

This is exactly the identification whose sufficient premise is stated in `../gates/a3-close-meet-gate.md` §B. It is an equality for the **adopted maximal recursion**, not for arbitrary assignments satisfying only lower gaps. In particular, the stopped recursion introduces no new higher-level rows. The erosion at depth q is bounded by a geometric series in the local scale `xi_q`, whereas the latest nest clearance is `M xi_q`; the strict inequality `rho<M` is uniform in q. This proves that arbitrarily deep thin nests cannot defeat the identification.

### 5.3 The W3 consumer after the identification

The first domain is `B_0 minus C=X minus C`: EXT-out gives `B_0=X minus J_X` with `J_X subset C`. Its collar is in layer a by §3.5 and in the common prepared domain by (4.1). Its alignment is inherited from C's level-a cell grid. The repaired cut-meet lemma therefore supplies the strict first gap, all higher gaps, and the mismatch strip

\[
 \mathcal C_3\subset
 \{z\in X\setminus C:d_\infty(z,C)\le(\rho+3)\xi_a\}.
                                                               \tag{5.5}
\]

Both backgrounds `T(B)` and `P_X` have the same parent determining sequence. On rows with both endpoints outside C their shell data agree, and their exterior/lifted data agree by EXT-out and `geo-4.md` §6. New rows use the same lift of the common level-a shell datum. These are precisely Lemma C(c),(e) and Lemma D of `meet-6c.md`; (5.4) does not change any row or datum. In particular it identifies domains before a background theorem is applied, rather than pretending that a field on the healed domain is a field on the prepared one.

For clarity, the mismatch-to-core weight comparison also uses the correct direction. For any `z in mathcal C_3`, a shortest segment to C, stopped at its first entrance, stays within the collar in (5.5). On its open part the parent is layer a. The four-dimensional Euclidean length of this segment is at most `2(rho+3)xi_a`; allowing endpoints gives weighted length at most `2rho+8`. For every y, the triangle inequality gives

\[
 d_B(y,\mathcal C_3)\ge d_B(y,C)-(2\rho+8).      \tag{5.6}
\]

This is the one-sided estimate read by Theorem M and I1-W3, as repaired in the gate. An empty mismatch set means exact coincidence and requires no reverse bound. The theorem's conclusion, conditional on its unchanged regularity and response inputs, therefore still decays from C alone. Its first-domain complement also contains `X^c`, but that is not an additional mismatch or a replacement decay set.

Finally the consumer's margin is separated from C by the retained shells, not by the artificial W3 tower. A path from C to outside `D_(a+n_c-1)` must cross each of the nested shells `D_(i+1) minus D_i`, `i=a,...,a+n_c-2`. Each crossing has physical length at least `m_(i+1)` by (3.1), and the global prepared weight there is `xi_i^(-1)`, so it costs at least `LM`. These portions can be chosen disjoint by the same last-exit/first-entrance construction as in §3.6. Localisation can only increase the weight. A plaquette in `supp phi` has a corner outside `D_(a+n_c)`; moving to its assigned pillar top cannot place that top inside `D_(a+n_c-1)`. Indeed, a top there has level at most `a+n_c-2`; its pillar has sup diameter at most `xi_(a+n_c-2)`, and the plaquette adds at most eta, whereas the intervening gap to `D_(a+n_c)^c` is at least `m_(a+n_c)`. The latter is larger than both possible displacements together. Thus every relevant top lies beyond the first `n_c-1` shells, and

\[
 d_B(y,C)\ge LM(n_c-1)\ge Mn_c                 \tag{5.7}
\]

for `n_c>=2` and `L>=3`. The same reasoning holds for plaquette midpoints with their smaller endpoint allowance. This verifies the geometric decay read in `sa-2.8-terms.md` §5.4 (`R_7`); it spends the spare factor L in the local minimum gap to handle endpoint conventions. The adopted coupling floor in §4.3 already gives `n_c>=6`. No return through another component or around the torus avoids the intervening nested-box boundaries. QED.

## 6. Disposition

**PROVED:** GEO2, GEO4, GEO6 and the W3 nest gap for every admissible configuration under the adopted definitions and the source's retained local minimum-gap requirement (3.1). GEO6 has the stronger core containment (4.1); W3 gives the actual full/cut equality (5.4). The proof covers multiple components, old mergers, every stopping choice of retained marks, arbitrary history length, minimal-width nests and periodic geometry. **REFUTED and repaired in the consumer:** Lemma W(3)'s intermediate `Rcheck_a<=2R`; (4.3) refutes it, and (4.4)–(4.7) prove its required conclusion with an explicit coupling floor. The ten-term consumer changes only at that constant choice, in addition to the already adopted repairs of rows 118–122.

Scope: (3.1) is the existing local admissibility condition, not a theorem inferred from an upper face bound or an assertion about an unspecified integration kernel. The background, regularity and response hypotheses, and GEO5(c)'s separate profile-count hypothesis, retain their own standing; none is proved by this geometry. This is a written research implication, with no computer-assisted discharge, independent gate, audit verdict or scientific status.
