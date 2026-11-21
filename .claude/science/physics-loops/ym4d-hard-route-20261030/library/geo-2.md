# geo-2: geometry after adopting the profile and localisation rules
Provenance: Codex (GPT-6; effort: xhigh), checkout `eb96016c91d341a01b921c22fd78915d259d1084`; Sussman–Alpoge commit `31a47c543775`; research text, not an audit, grants no status.

## 1. Target and adopted data

Queue row 119 asks whether GEO1–GEO4, GEO6, EXT and the W3 nest gap follow for every admissible class configuration. These are the geometric inputs of the A3/Proposition 2.8 route, listed in `sa-2.8-terms.md` §3 and used in its Lemma W. Failure of one refutes this conjunction; it does not refute an analytic implication retaining that input as a hypothesis or Yang–Mills existence.

I adopt the half-cell profile `geo-prop23.md` (5.1), and Definition A of `assign-adopt.md` with the repairs in `../gates/a2-full-gate.md`. Row 118, `geo-prop23.md` §§3–5, already checks one quiet component, refutes the inference of GEO5 from arbitrary supplied profiles, and proves the half-cell locality rule. Those results are cited, not repeated.

Credit: the outline's class construction, regions, nests, preparation and healing are due to Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text. References “SA” mean line numbers of their `YM4_sketch_500.tex` at the revision above, fetched once to `/tmp/sa_ym4.tex`. All conclusions below require written mathematical arguments; no computation discharges a step.

## 2. The hardest quantitative clause

The literature search is reused from `lit-large-field.md` §§0–1: Balaban's CMP 122 papers supply the operation, whereas the cited Dimock constructions do not contain this recycling operation. The targeted reading here is the pinned SA text, especially 6070–6120, 17317–17334, 17398–17446, 17576–17640 and the order of constants in (2e), 19469–19487. No unverified theorem from those papers is used.

Put `a=k-N_k`, `m_i=M L^(i-k)` and `R=Rcheck_k`. The quantitative clause of GEO3 under attack is

\[
 \operatorname{side}(\text{nest box enclosing levels }<l)
 \le C_n M(RL^{a-l}+L)L^{l-k}.
 \tag{2.1}
\]

Here `C_n` is fixed before the coupling, hence before arbitrarily large R. At levels far above a, (2.1) says the box has uniformly bounded size in local M-cubes. A bound on the final box alone does not have this consequence: a large box at an intermediate level can still be extremely small in level-k units. The test below keeps the one-M-cube gaps, including the equality mentioned in Proposition 2.3, and the small final box. It changes an intermediate box. The question of whether the stage prescription admits this change is part of the attack, not something inferred from failure to find a formula.

## 3. Two components and an intermediate enlargement

Choose an odd `L>=27` and the earlier constants in (2e), with `mu=M_1'>=max(3,rho)`, `M>=L^2 M_2>=L^3 mu` and `M>=varpi_T`. For the repaired localisation collars take the collar counts 5 and 9; their difference times mu is `4mu>max(rho,3M_1')`. For the fixed decay rate theta take the stipulated floors `theta min(M,rho)>=64 log L`. These choices are independent of the coupling. Now let `C_n` be any proposed finite positive constant, allowed to depend on all these earlier choices. Choose a power `R=L^h`, `h>=2`, so large that

\[
 R>\max\{128C_n(L+1),\,16(L+4),\,256\}.
 \tag{3.1}
\]

Increase h for the frame and coupling floors of `geo-prop23.md` §3. Use that section's constant-R frame, `a=1`, `k=R+1`, quiet step regions and creation record, without changing them. In particular, if E_i is the central level-i cell of side `s_i=Rm_i`, the initial core is `C=E_a^[6]`, of side `13Rm_a`, and the later step regions in the component are `E_i^[8]` and `E_i^[10]`. These are the admitted single-creation regions of SA 17583; their admission and quarantine were checked in row 118.

Take two translated copies, with centres 0 and `50s_k e_1`. Their final boxes `X_1,X_2` have side `21s_k`, so their distance is `29s_k`. Earlier boxes are smaller. Translation by `50s_k e_1` preserves every grid. Thus no hull, added layer, boxing or test collar in either lineage meets the other, and neither lineage joins the other. The disjoint-history rule of SA 17446 and 18890–18910 gives their union. Choose the torus side `2L^J>400s_k`, increasing J to meet any earlier torus floor. Both components and their box neighbourhoods have common non-wrapping lifts. The complement used for W4 wraps, but its adopted localisation is defined by periodic distance. Both components are eligible at k; neither is withheld from the operation.

Use the following prepared nest in both components, translating it with the component. The first supplies the witness. Write

\[
 r=a+(R-1)/2,\qquad F_i=m_i(\mathbb Z+1/2),\qquad
 D_i=[\alpha_i,\beta_i)^4,\qquad D_a=C.
 \tag{3.2}
\]

The nesting grids have `F_(i+1) subset F_i`. Use the alternating face recursion (3.3) of row 118 at every step except r; choose its initial parity so that the lower face is designated at r. Explicitly, a designated lower face moves down by `m_i` and the upper face is rounded up to the first point of `F_(i+1)` at least `beta_(i-1)+m_i`; for a designated upper face interchange upper and lower. At r instead set

\[
 \alpha_r=\alpha_{r-1}-m_r,\qquad
 \beta_r=\min\{u\in F_{r+1}:u\ge Rm_r/4\}.
 \tag{3.3}
\]

Thereafter resume the alternating recursion, designating the upper face at `r+1`. This is an explicit finite geometric rule, with the same fixed coordinate convention as the cited row 118 nest; it is the same in translated components and on common lifts. The rule itself does not depend on C_n. Put `Z''_i=D_i` and let `Lambda` be D_k with one level-k M-layer added.

Every elementary estimate below is a written inequality. In particular, no selection of r, grid face or torus size uses a search over configurations.

## 4. What the configuration satisfies

**Alignment, nesting and all minimum gaps.** At each ordinary step the designated old face belongs to F_i, its new face still belongs to F_i, and the opposite new face belongs to F_(i+1). These facts hold initially since R is divisible by L, and propagate to the next step. Formula (3.3) preserves the same induction. Every D_i is therefore a union of level-i M-cubes.

For odd `R>=5`, `R L^(-(R-1)/2)<1`: it holds at R=5 for `L>=27`, and increasing R by 2 multiplies the numerator by `(R+2)/R<3` and the denominator by `L>=27`. Thus

\[
 RL^{a-r}<1,\qquad RL^{r-k}<1/L.
 \tag{4.1}
\]

Before r, the face bound already proved in row 118 is

\[
 |\alpha_i|,|\beta_i|
 <\tfrac{13}{2}Rm_a+(L+3)m_i.
 \tag{4.2}
\]

It implies `beta_(r-1)<8m_r`: divide by m_r and use (4.1) and `(L+3)/L<=10/9`. Since `R/4>9`, the exceptional upper face moves by more than m_r. The lower face moves by exactly m_r. At every ordinary step one face moves by m_i and the opposite face by an amount in `[m_i,(L+1)m_i)`. Consequently all D_i increase, contain C, and

\[
 d_\infty(D_{i-1},D_i^c)=m_i\quad(a<i\le k)
 \tag{4.3}
\]

for geometric carriers. On bare site sets the distance is at least this value. This is the one-M-cube-of-the-later-level separation of Proposition 2.3, even with its asserted equality in the carrier convention. Adding one level-(i-1) M-layer to D_(i-1) stays inside D_i, since `m_i=Lm_(i-1)` and `L>1`. In particular the other two inclusions in SA 17404–17407 hold for the prepared nest.

**Containment in the original holes.** All lower faces obey (4.2). Before r so do the upper faces. As checked in row 118, for `i>a` this puts those faces strictly inside the central cell E_i, since

\[
 \tfrac{13}{2}L^{a-i}+\frac{L+3}{R}
 \le\frac{13}{2L}+\frac{L+3}{L^2}<\tfrac12.
 \tag{4.4}
\]

At r, `Rm_r/4<=beta_r<(R/4+L)m_r<Rm_r/2`. After r, summing the ordinary face increments gives

\[
 \beta_i<(R/4+L)m_r+(L+3)m_i\quad(i>r).
\]

Dividing by `Rm_i`, the right side is at most `1/(4L)+(L+4)/R<1/2`. Hence `D_i subset E_i subset Omega_i^c intersect X_1` at every `i>a`. The exceptional box is a retained *subset* of the old hole, never a new large-field creation.

**Small final box, uniformly in R.** The sum of the two face increments at an ordinary step is less than `(L+2)m_i`. Over all such steps their sum is less than `(L+4)m_k`. The exceptional positive-face increment is less than `(R/4+L)m_r`; overcounting the ordinary increment at that step only enlarges the bound. Therefore

\[
 \operatorname{side}(D_k)
 <13Rm_a+(L+4)M+(R/4+L)m_r<(L+6)M,
 \qquad \operatorname{side}(\Lambda)<(L+8)M.
 \tag{4.5}
\]

Here `13R L^(-R)<1` is the row 118 estimate, and (4.1) gives `(R/4+L)L^(r-k)<1/(4L)+1/R<1`. Thus the source's final-box condition holds with the named constant `C_Lambda=L+8`, fixed before R. The exceptional face movement itself is less than M in level-k units; its large size is in its own level-r units.

**Stage and history interpretation.** At stage i retain D_i and integrate the stored level-(i-1) variables in the outer part of the old level-i box; the retained level-(i-1) shell is `D_i minus D_(i-1)`. The stage changes the members inside X to `X minus D_i`, as in SA 17421–17427; the action update is precisely SA 17630–17636. Every intermediate stopping choice uses an initial segment of these boxes. At its junction with an unprepared member, `D_i subset E_i` and the latter member's eight-cell margin give at least `8s_(i+1)>m_(i+1)` of clearance. Thus the construction satisfies the geometric clauses for every interrupted stage, not only the fully prepared sequence. There are no earlier marks in this example, and the second component does not change any of these checks.

The scope of admission is the source's **geometric formation data**. SA 6055–6078 requires those data to specify the actual regions and integration variables; SA 17415 and (2b) prescribe increasing residual boxes, outer-shell integration, the minimum gaps and the final `O(M)` box. The rule (3.2)–(3.3) supplies those objects. Integrating a smaller outer part leaves a larger residual shell and violates none of these conditions. At the level of moves in SA 17499 this is deletion of the designated stored variables; it does not require a new test outcome or a creation. The source's quantitative shell-side bound `CMLR` in SA 17662 also holds: every D_i lies in E_i, whose side in level-(i-1) units is `MLR`. The word “thin” in SA 17585 is not a specified upper face-increment rule. If it is intended to impose such a rule, that is extra formation data; §6 gives a precise sufficient version. This configuration is not asserted to be the output of a particular unstated Balaban box algorithm, or to prove the analytic induction for modified formation data.

## 5. REFUTED: the intermediate size and shell-count clauses of GEO3

The prepared sequence in X has `Omega_i^p=X minus D_i` for `a<i<=k`. Consequently D_r is the nest box enclosing the shells of levels below r, and its outermost such shell is `D_r minus D_(r-1)`, at level `j=r-1`. Formula (3.3) and `alpha_r<0` give

\[
 \operatorname{side}(D_r)>Rm_r/4
 >C_n(L+1)m_r
 >C_n(RL^{a-r}+L)m_r.
 \tag{5.1}
\]

The second inequality follows from (3.1), and the last from (4.1). This is the opposite of (2.1). The excess is unbounded as R increases with L, M and C_n fixed. It cannot be repaired by increasing a fixed C_n or lowering the coupling ceiling.

The failure is also present in the number of actual shell tops, not just in a choice of enclosing box. Consider the open cube

\[
 Q=(Rm_r/8,\,3Rm_r/16)^4.
 \tag{5.2}
\]

Every coordinate is greater than `beta_(r-1)<8m_r`, while every coordinate is less than `beta_r>=Rm_r/4`. Thus Q lies inside `D_r minus D_(r-1)`. Its distance from both relevant faces is greater than one level-j lattice spacing `xi_j=m_r/(LM)`, using `R>256`. Each level-j lattice point in Q is therefore the endpoint of a level-j bond wholly in that shell. It is a determining top by SA 5614–5628. The old first domain contains Q: its excluded creation region is within C, whereas Q is outside D_(r-1), which contains C.

An open interval of length t in a lattice of spacing delta contains at least `t/delta-1` lattice points: consecutive points cut it into intervals of length delta, with at most two incomplete end intervals. For `t/delta>=2` this is at least `t/(2delta)`. Applying this separately in four coordinates to Q gives

\[
 \#\{\text{level-j tops in }Q\}
 \ge (RLM/32)^4.
 \tag{5.3}
\]

On the other hand `RL^(a-j)=L RL^(a-r)<L`, so the proposed GEO3 bound is strictly less than `(2C_nML)^4`. Since `R>64C_n`, (5.3) exceeds it. No machine count is used.

The adopted localisation does not remove these tops. The whole nest lies in the central level-k cell of X, hence at depth at least `10s_k` from X's boundary. This exceeds `3mu`; the proved erosion bound of Definition A puts the nest in every member of the second-rule tower of X. Localising therefore retains the same prepared shell there. The half-cell profile changes weights, not these regions or tops.

This counterexample even retains the W3 nest clearance: for `q>a`, `C subset D_(q-1)` and (4.3) imply `d(C,Omega_q^p)>=m_q=M xi_q`. The exterior of X is farther still. Thus violating the shell-count clause did not require a failure of the separation on which the W3 comparison relies.

## 6. The smaller missing condition, and its consequence proved

A sufficient extra formation rule is a uniform **upper** bound on the movement of each face. Suppose boxes D_i contain C, their faces move outwards, the initial side in each coordinate is at most `B R m_a`, and every face at step i moves by at most `K m_i`, with B and K fixed before R. Then, for every l,

\[
 \operatorname{side}(D_l)
 \le BRm_a+2K\sum_{i=a+1}^l m_i
 \le BRm_a+\frac{2KL}{L-1}m_l.
 \tag{6.1}
\]

The first inequality adds the two opposite face movements in each coordinate. For the second, divide the finite geometric series by m_l; it is at most `1+L^(-1)+...=L/(L-1)`. Set

\[
 C_{\rm side}=\max\{B,2K/(L-1)\}.
\]

Equation (6.1) is then at most `C_side (R L^(a-l)+L)m_l`, exactly the size form (2.1). A shell of level `a<=j<k` lies in D_(j+1). Dividing (6.1) at `l=j+1` by `xi_j=m_j/M` bounds its coordinate length in level-j sites by

\[
 M\{BRL^{a-j}+2KL^2/(L-1)\}.
\]

An interval of length d has at most `d/xi_j+1` such sites. Because `M>=1` and `L>=1`, taking

\[
 C_{\rm tops}=\max\{B,\,2KL/(L-1)+1\}
 \tag{6.2}
\]

bounds the number of shell tops by `[C_tops M(RL^(a-j)+L)]^4`. The level-k shell inside Lambda adds one M-layer to D_k. Its site count per coordinate is at most `M{BRL^(a-k)+2KL/(L-1)+2}+1`, also bounded by `C_tops M(RL^(a-k)+L)`: the remaining constant inequality follows from `2KL+L>=3`, valid for `K>=0` and `L>=3`. This proves the required count under the extra face-movement rule. The ordinary alternating rounding used in row 118 has `K=L+1`; the exceptional move (3.3) has no R-independent K. Thus the extra condition excludes exactly the mechanism above. This is a proved implication with named constants, not a claim that the pinned outline already supplies that condition.

## 7. Disposition

**REFUTED as a universal geometric implication from the stated formation rules:** even after adopting the requested profile and localisation definitions, the GEO1–GEO4, GEO6, EXT and W3 conjunction does not follow. The two-component, depth-R configuration (3.2)–(3.3) satisfies the class's quietness and quarantine, the cell and box alignment, the prepared and interrupted-stage minimum gaps, containment in the original holes, and the final-box bound with `C_Lambda=L+8`. It violates GEO3 by (5.1) and by the explicit top count (5.3). The practical change is to specify and verify an upper face-movement rule before using GEO3 to obtain the shell volume in `sa-2.8-terms.md` §§5.4–5.9. Section 6 proves the size/count consequence of such a rule; the minimum-gap assertion of Proposition 2.3 cannot replace it.

Scope: this refutes derivation from the outline's stated geometric data, not Balaban's particular operation, an analytic theorem assuming GEO3, or existence of a complete analytic presentation for arbitrary replacement data. No universal verdict on the remaining independent premises is claimed. In particular, no finite computational test, audit result or scientific status is being supplied.
