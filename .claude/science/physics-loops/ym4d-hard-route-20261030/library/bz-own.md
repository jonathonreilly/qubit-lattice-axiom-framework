## Repo search

The lead searched main and PRs #10114, #10133, #10134 and #10141.
It found no outside-lane construction closing this target.
`prior/repo-search-2026-11-08.md`, section 1, records the relevant hits.
`prior/bz-own.md` is absent at this pin.
I fetched main and the named PR sources without changing the working tree.
Main was `43a1fcc374711ca50626eca667441d3ca575c7d1`.

| Source checked | Closeness and use |
|---|---|
| PR #10141, `c73ad7b177d94f89ff37b77386936e3d52b48b05`, `research/ym4d/library/layer-thm-part.md:698–703,1385–1408` | Already identifies the boundary-gauge and ambient-continuation problems. This is our prior diagnosis. |
| The same PR, `research/ym4d/library/out-pi.md:273–303,324–356` | Supplies conditional PI and interior admission. Its boundary counterexamples do not identify reached item-10 entries. |
| The same PR, `research/ym4d/library/out-gw.md:54–64` | Supplies the frame estimate after PI admission. Localized admission remains additional. |
| PR #10114, `f76f6c649cff7dffbab664d8976e680e8f287fe9`, `.claude/science/toe-ruleset-20261021/agents/ym4d-proof/RTARGET.md:716–725` | Proposes local gauges and compressed walks for a different soft Hessian. It supplies no cut for this problem. |
| `leaf-bz.md`, `bz-geom.md`, `c0-sup.md`, and `gates/c0-sup-check.md` | Supply the bare-rim argument, first-spacing read, sufficient filling, and earlier failed deductions. They are reused, not proved again. |
| `leaf-hy.md` | Precedent for choosing a new construction and checking its consumers. Its hybrid nest does not itself supply a localized layer. |

The PR #10141 passages are snapshots of this route's Claude and Codex work.
They are not independent confirmations.
The registry retains PI-ADMIT under `pi-admit`.
The targeted registry and prior-work searches found no separate owner for this authorized BZ-CUT continuation.

# An own buffered cut for the localized layer

Codex. Research base `b940c2a85b5f2d400e674039527f67fc6da13e8d`.
FINISH row 563, `bz-own`. Research text, not an audit. This note grants no status.
This session writes only this file. No computation supplies a mathematical proof step.
During the final check, another process had advanced HEAD to `60ddc80b975233996a1adbbe6fb44cf2d86f5ab7` and changed unrelated files.
The cited local science files, indices, prior notes, registry, GOAL and C0 check were unchanged from the requested pin.
Those concurrent changes were left untouched; they supply no new premise here.

Credit Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text.
Credit Tadeusz Bałaban for the graded localization and background-field methods.
**I** denotes their complete account I at `31a47c543775`.
**SA** denotes their outline at that revision.
**Y** denotes `YM4_1400.tex` at `2bc0658f91d2d03ba44e20bf695067e0a56a2ed9`.
The three named scratch copies already existed. None was downloaded again.
Source reads use the supplied indices and bounded excerpts.
No CMP 122 result is imported as a supplier for the new cut.

This task permits a new construction. Equality with the old, unspecified cut is not its proof obligation.
Its obligation is to preserve every required consumer, including the actual shift, its domain, and its estimate.
The ordinary interior PI hypotheses and other layer-theorem premises remain separate throughout.

## 1. What can be changed, and what must be kept

Item 10 is an input, I 131568 and 131725–131746.
Its localized assertion is used without a complete proof, I 137565–137583.
The outline distinguishes the same two boundary issues.
SA 10262 gives gauge transfer on supplied traces.
SA 10287 includes protruding plaquettes in the compressed Hessian.
SA 10505 puts crossing models in a bare rim.
These are Sussman and Alpoge's statements, with their stated scope.

There is room to choose a new cut inside an arrested component.
Write \(A=X_{\mathfrak a}\), \(k=k_{\mathfrak a}\), and \(W=A\cap\Omega_k^c\).
I 131946–131984 gives \(A\setminus W\) as the two-layer collar, at level \(k\).
Its cell side is \(MR_k\ell_k\), where \(\ell_q=L^q\eta\).
Use the account's compatible grids and metric interpretation of layers, I 48149–48168.
Thus, on the component's admitted geometric trace,

\[
 W^{(+2MR_k\ell_k)}\subset A. \tag{1}
\]

This uses the account's collar declaration. It does not prove the separately assumed history geometry.
The parent is the birth stage partition
\(\mathfrak B_{\rm par}=\mathbb B_k^{(n+1)}\restriction A\).
Its grade on \(A\setminus W\) is \(k\).
The cut below is frozen at birth and is reused at later readings of that term.
Each new birth gets its own cut by the same rule.

The interrupted shift acts on
\[
 S^P=(\Omega_{j+1}^c\setminus Z''_{j+1})^{(j)*}\cap A,
 \qquad j=h+n<k. \tag{2}
\]
This is I 137320–137340.
Nesting puts its inner endpoints in \(W\).
An outward endpoint or a full level-\(j\) block read adds at most a fixed multiple of \(\ell_k\).
We retain a larger fixed neighbourhood of \(W\), so these endpoints are not cut off.
The class's completed number of stages is unchanged.

The smallest analytic requirement is more than smallness of some newly defined function.
The strip identity, SA 17521–17526, uses
\[
 e^{iH}=V_j^{\rm bg}(V_j^{\rm loc})^{-1}. \tag{3}
\]
Here the averages and representatives are the actual ones used by the stage.
This is the reason an arbitrary small layer, including zero, is not an answer.
Section 4 below isolates this requirement after the geometric construction.

## 2. The cut and its partition

Distinguish PI's fixed gap number \(R_{\rm PI}\) from the running radius \(R_k\).
First fix the common PI constants, including \(M_b,r_N,R_{\rm PI}\).
Choose a power \(m\) of \(L\) such that
\[
 m\ge12M_b,\qquad
 mL>R_{\rm PI}M_b+1,\qquad m>2(r_N+2).
 \tag{4}
\]
Choose the already free construction size \(M\), a multiple of \(m\), with
\[
 M\ge \max\{L^3m,\ 20(r_N+L+2)\}.
\]
All these choices precede \(R_k\).
Set \(w=16L\). Its value does not depend on a history, cutoff, or running radius.

Let \(\mathcal Q\) be the birth grid of cubes of side \(M\ell_k\).
For \(Q\in\mathcal Q\), \(Q^{[w]}\) adds \(w\) layers of that grid, including corner neighbours.
Define
\[
 Z=\bigcup\{Q\in\mathcal Q:Q^{[w]}\subset A\}. \tag{5}
\]
For \(A\) equal to the whole torus, take \(Z=A\); no boundary read then occurs.
The empty component has no call.

On \(Z\), use the second-rule erosion of I 32861–32894:
\[
 D_0=Z,\qquad
 D_q=\bigcup\{Q\text{ of side }m\ell_q:
             Q\subset D_{q-1},\ d_\infty(Q,D_{q-1}^c)\ge m\ell_q\},
 \quad1\le q\le k.
 \tag{6}
\]
Put \(C=D_k\).
Let \(P_q\) be the positive parent regions before restriction to \(A\).
Set
\[
 \Omega^{\rm cut}_0=Z,\qquad
 \Omega^{\rm cut}_q=P_q\cap D_q\quad(1\le q\le k),
 \qquad\Omega^{\rm cut}_{k+1}=\varnothing.
 \tag{7}
\]
All intersections use the compatible cell grids.
Corner-block rows are then formed by PI's existing rule, including its outward rows.
We do not clip a row's averaging carrier at \(\partial C\).

The elementary erosion estimate is already proved in I 147765–147805 and Y 37093–37119.
Its weaker form, sufficient here, is
\[
 Z\setminus D_k\subset
 \{x\in Z:d_\infty(x,Z^c)\le3m\ell_k\}. \tag{8}
\]
We port that rejected-cube argument from Sussman and Alpoge, rather than prove it again.
It applies with \(m\) replacing their fixed \(M_1\).

Two simple facts about (5) locate the changed band.
First, \(d_\infty(Z,A^c)\ge wM\ell_k\).
Each retained cube has its entire \(w\)-layer enlargement in \(A\).
Second, each point of \(A\setminus Z\) is within \((w+1)M\ell_k\) of \(A^c\).
Its grid cube was rejected, so that cube's \(w\)-layer enlargement meets \(A^c\).
The diameter of the original cube costs the remaining \(M\ell_k\).
Approaching \(\partial Z\) from rejected cubes and using (8) therefore gives
\[
 Z\setminus C\subset
 \{x:d_\infty(x,A^c)\le[(w+1)M+3m]\ell_k\}. \tag{9}
\]
Using \(w+2\) in this bound covers every boundary convention.

Fix \(r_K=4(r_N+L+2)\).
Impose the running-radius floor
\[
 2MR_k>(w+3)M+3m+r_K. \tag{10}
\]
Equations (1), (8) and (9) then imply
\[
 W^{(+r_K\ell_k)}\subset C,
 \qquad Z\setminus C\subset A\setminus W.
 \tag{11}
\]
The first inclusion follows by subtracting the bound in (9) from the distance in (1).
The positive remainder exceeds \(r_K\ell_k\).
In particular, a nonempty protected core is not lost by erosion.

**Partition identity.** Let \(\mathbf B_k^{m}(Z)\) be the partition defined by (6).
Then the partition defined by (7) obeys
\[
 \boxed{\quad
 \mathfrak B^{\rm cut}=
 (\mathfrak B_{\rm par}\restriction C)
 \ \cup\
 (\mathbf B_k^{m}(Z)\restriction(Z\setminus C)).\quad}
 \tag{12}
\]
On \(C=D_k\), every \(D_q\) is present, so (7) retains the parent grade.
Off \(C\), (11) puts the parent at grade \(k\).
There (7) has exactly the grade of (6).
The boundary of \(C\) lies in that same top stratum.
Its grid is a union of whole parent top blocks, since \(m\) is an integer power of \(L\).
Hence these are disjoint block families with union \(Z\), not clipped pieces of blocks.
This proves (12) for our partition. It makes no equality claim about the old CMP 122 partition.
The graded splice is Bałaban's method, already quoted from CMP 119 (2.14) at I 92517–92536 and used in `bz-geom`.
The new choices here are the inset (5) and its protected-core calculation.

**Gaps.** Use the weaker printed parent gap \(M\ell_q\), I 45559–45593, condition (A1).
We do not need the stronger convention in SA 17398–17407.
As elsewhere in the lane, those supplied nest conditions remain inputs.
For \(q\ge1\), the complement of (7) is \(P_q^c\cup D_q^c\).
Distance to that union is the minimum of the two distances.
Thus
\[
 d_\infty((\Omega_q^{\rm cut})^c,\Omega_{q+1}^{\rm cut})
 \ge\min\{M,mL\}\ell_q
 =mL\ell_q>R_{\rm PI}M_b\ell_q.
 \tag{13}
\]
At \(q=0\), use \(D_1\) directly to get the same bound.
Empty later regions impose no obstruction.
All regions are unions of level-\(q\) big blocks.
The sup-distance bound implies PI's Euclidean-distance bound.
Equation (4) also gives
\[
 d_\infty(\Omega_1^{\rm cut},Z^c)>2L(r_N+2)\eta.
 \tag{14}
\]
Thus crossing PI patches are bare, by the existing argument in `bz-geom`, Lemma 3.1.
The prescribed torus-room condition of PI is retained.

## 3. The first exterior read is now supplied

`c0-sup`, Proposition 3.1 and Lemma 3.2, put every boundary coefficient and reference-norm read in \(Z_\eta\).
Equation (5) gives the stronger inclusion
\[
 Z_\eta\subset A,
 \qquad d_\infty(Z_\eta,A^c)\ge wM\ell_k-\eta>0.
 \tag{15}
\]
This includes the outermost touching plaquette.

For the old kill test, write \(A=\{x_1\le0\}\) locally.
The unbuffered choice \(Z=A\) reads the tangential edge at \(x_1=\eta\), outside \(A\).
With a flat face of the new cut at \(x_1=-b\), where \(b\ge wM\ell_k\), that edge is at
\[
 x_1=-b+\eta\le0.
\]
The whole plaquette lies in \(A\).
The positive-parent case also stays bare at the new rim by (14).
These tests concern the same whole-action operator; no boundary plaquette is deleted.

Here the actual call offers more than a generic raw boundary.
Every crossing patch and its required read lies in the parent's top collar.
Use the conservative patch reach \(2L(r_N+2)\eta\) from \(\partial Z\).
The floors on \(M\), and \(k\ge1\), put this reach below one tenth of a top \(M\ell_k\)-cell.
Equations (9)–(10) leave more than one \(M\ell_k\)-cube between that read and \(W\).
Equation (5) leaves more than one such cube between it and \(A^c\).
Take a surrounding box of side at most \(M\ell_k\).
The containing-cube lemma, I 48263–48335, supplies a single cube \(Q\) of that side in the top collar.
It may slide across the partition grid.
The printed top family permits this, I 48479–48500.
No joining of independently chosen gauges is required.

The ambient member in item 10 supplies the pair on \(Q\subset A\).
Define the pair for the new coefficient matrices by its restriction, including (15).
The equality of pairs on every read then holds by definition, for every parameter.
This uses the pair's own continuation, as required at I 119615–119650.
It does not choose a new exterior extension.

At later sources and images, use the frozen birth cut and birth top family.
I 138558–138575 carries that family's positive-stratum clauses and cubes.
The omitted moved raw clauses on \(Y'\) do not occur on this top collar.
This is an application of the stated ambient input, not a proof of the arrest theorem.
In particular, no chronological heredity theorem is applied to the new, lowered grades.

Write the supplied top-scale bounds as
\[
 \ell_k|A_Q|\le A_*R_k,\qquad \ell_k|a|<T_* . \tag{16}
\]
Here \(A_*,T_*\) bound the original domains, not smaller replacement discs.
For the printed gauges one may use
\(A_*=L^2\mathsf c_1BM\bar\alpha_0\), with a uniform ceiling \(\bar\alpha_0\) on their real radii.
This is the hull-gauge domination proved at I 49120–49234, also valid for the top cube itself.
For the relaxed \(K_{109}\) member, (3.37) supplies a fixed twist ceiling \(T_*\).
The definition and the coupling-free upper ceilings are I 110264–110317.
Any larger fixed factors in a prescribed stage domain are included in \(A_*,T_*\) before the following floor.

The account reads Bałaban's size parameter as \(R_k=\check R_k\), I 49747–49764.
An actual preparatory call has \(k> N_k=\check R_k\), I 51262–51268.
Therefore the existing conversion `c0-sup` (9) gives
\[
 \eta|A_Q|\le A_*R_kL^{-k}\le A_*R_kL^{-R_k},
 \qquad \eta|a|<T_*L^{-k}\le T_*L^{-R_k}. \tag{17}
\]
Choose a fixed floor \(R_*\), after \(A_*,T_*\), with
\[
 A_*RL^{-R}\le\tfrac14L^2a_0^*,\qquad
 T_*L^{-R}\le\tfrac14a_1^*\qquad(R\ge R_*).
 \tag{18}
\]
Such a floor exists without computation.
For positive integers \(s\), the ratio of successive \(sL^{-s}\) is at most \(2/L<1\).
The same conclusion holds for the allowed subsequence of powers of \(L\).
This increases a running-radius floor. It does not shrink an assigned parameter disc.

Equations (14)–(18) give C0-ETA for the new coefficient entry, on its whole prescribed ambient domain.
`c0-sup`, Proposition 4.1, now gives its boundary PI estimates.
The gauge may depend on the real reference, as finding 6 of its Claude check permits.
Interior admission, current identification and the nonlinear layer equation have not been inferred from this boundary argument.

## 4. First new supplier: BZ-JOIN

The construction above is a coefficient entry. It is not yet a construction of the function used in the change of variables.
This distinction matters even if all the standing interior and nonlinear estimates of Theorem LAYER are granted.
Changing the cut changes the constraints and the normalized background.
Theorem LAYER is an implication for its furnished equation and admitted inputs.
Its fixed-kernel Lipschitz estimate does not identify an equation after its determining set changes.

Here is the first cut-specific supplier still needed. It is an analogue of the actual-data alignment lemma in Y, not a request to recover Bałaban's old cut.

**BZ-JOIN — full-domain alignment of the two actual cut data.**
Fix one item-10 call, its original parameter domain \(D\), and (5)–(7).
On the real own-current slice, take these two data on the new determining set:

1. the datum induced by restricting the stage's actual background;
2. the literal joined datum: retain its old determining rows in \(C\), and use the level-\(k\) face lift on the new collar rows.

The face lift is the one defined in SA 9783: identity inside an old block, and the old top datum across its face.
Keep the actual mean contours and their normalization. Include the full preceding block of each outward row.
The collar carrier \(\Gamma\) consists of the new or changed rows, their complete reads, and these normalization paths.
It is confined to the changed top collar with a fixed enlargement.
Geometric rows common to both problems have identical complete reads on the protected part (11).

The required lemma is the following.
These actual data admit a common holomorphic chart throughout \(D\), with the prescribed independent current and switches, and with a uniform larger margin for their interpolation.
The chart uses the new cut's actual seven-term equation (S5) of `layer-thm-part`.
On the physical slice its endpoints are the two backgrounds just specified, in the same retained-node frame.
Its difference datum vanishes off \(\Gamma\); its field and current slots have the local, scale-weighted bound required before applying the layer response estimate.
The normalization and datum maps retain their complete-read locality on the term's domain \(Y\).
The lemma must concern the original domains, not a smaller ball selected after seeing an input.

More explicitly, its chart margin must be a fixed positive \(r_{\rm join}\).
After putting the two equations on common variables, let \(f_{\rm cut}\) be the field Euler forcing before applying the inverse, and \(b_{\rm cut}\) the raw logarithmic row forcing.
These include the independent-current terms in the exact subtraction, not a difference of physical output currents substituted for them.
Require support on the complete collar carrier and constants \(K_{\rm join},p_{\rm join}\), independent of mesh, depth and history, such that
\[
 \sup_{P\in D}\max\left\{
   \sup_y\ell_{\lambda(y)}^3|f_{\rm cut}(y;P)|,
   \sup_c|b_{\rm cut}(c;P)|\right\}
 \le K_{\rm join}R_k^{p_{\rm join}}\bar\alpha_k^{\rm fat}.
 \tag{BJ}
\]
Here \(\lambda\) is the cut grade and the powers are the physical field/row units of GW.
This allows a fixed polynomial collar loss. It assumes no exponential conclusion.

This is a chart-and-datum supplier. It does not assume the desired exponentially small layer.
Once such an identity is supplied, an admitted weighted inverse can estimate its forcing.
SA 12228–12255 explicitly separates those two steps.
The ordinary LAYER premises still have their existing status; BZ-JOIN does not silently discharge them.

In particular, C0-ETA says nothing about the current slot of this difference equation.
Nor does it identify a newly defined small solution with the shift in (3).
The needed common chart is the cut-specific instance of UA.A0/T and ID/EQ/PH, not FM-MATCH's fibre-density identification.
No FM-MATCH or HCM-TB result is claimed here.

## 5. Three routes to BZ-JOIN

These attempts concern the explicit new cut. They do not repeat `leaf-bz`'s attempts to infer an unspecified CMP 122 partition.

### Route 1. Restrict the existing solution and use the fixed-kernel estimate

The geometric restriction preserves the old rows on the protected core.
It also supplies every boundary coefficient needed by the new inverse.
Try to restrict the old solution, subtract the two equations, and apply LAYER's Lipschitz bound.

The subtraction needs an exact common-row identity first.
The new row map is not a restriction of the old row map on the staircase.
Already in the abelian linearization, an old averaging functional can annihilate a nonzero fine field which a new raw row reads.
For example, on two equally weighted contributions,
\[
 Q_{\rm old}(u,-u)=0,\qquad Q_{\rm raw}(u,-u)=u. \tag{19}
\]
One may place the two opposite contributions inside a larger averaging carrier.
This is a counterexample to the proposed row-intertwining identity, not to Yang–Mills localization.
No size of the inset makes the two row maps equal on all fields.

On common variables the necessary equation would instead have the form
\[
 \left[\int_0^1 D\mathcal F_{\rm cut}(X_t)\,dt\right]
       (X_1-X_0)=f_{\rm cut}. \tag{20}
\]
Here \(f_{\rm cut}\) includes the changed constraints, the boundary rows, the gauge restoration, and any cutoff commutator.
Both the segment and this identity must be admitted before its right side is estimated.
These are precisely the qualifications of SA 12228–12241 and 12285–12292.
They are not consequences of a coefficient inverse at a single reference.

The norm estimate in `layer-thm-part` §3.2 compares data for one furnished kernel and equation.
The new constraints in (19) change both.
Thus the attempt fails at constructing the admitted common-row identity (20).
C0-ETA repairs a prerequisite of this route. It does not finish it.

### Route 2. Port the physical cut comparison and continue it analytically

This route gets substantially further.
SA 9783–9789 and 9913 describe a joined sequence with a collar in one parent layer.
Our altered band has exactly that geometry.
Y 37060–37125 constructs the finer cut and protects complete inner reads.
Y 37181–37389 supplies the actual alignment argument:
normalize the two data separately by mean-contour descent, compare their face lifts, put their logarithms in one physical chart, and use regular-fibre uniqueness to identify the endpoints.
The descent is uniform in depth. The node frames agree on common free pillars.
Y 37390–37460 then gives its cut comparison for the specified settled curvature and full-current readouts.
These are Sussman and Alpoge's results, not new proofs here.

Our `mu.md` §§4–5 likewise supplies uniform admission and restriction for its stated regular-real/continued-complex minimizer problem.
Its scope is used as written.
It is not a theorem about every independent-current, switched instance of (S5).

The proposed analytic continuation from those physical results is invalid.
They vary the fine input and take its physical current.
Item 10 varies the current independently and admits switches.
The physical graph is not a uniqueness set for holomorphic functions of all those variables.
On any physical chart, let \(J_{\rm ph}(W)\) be its physical current and let \(\lambda\) be a nonzero linear functional on the current slot.
For any fixed output vector \(v\),
\[
 F_\epsilon(W,J)=F(W,J)
       +\epsilon\,\lambda(J-J_{\rm ph}(W))v \tag{21}
\]
agrees with \(F\) on the whole physical graph, yet differs off it.
On a bounded chart the extra term can be made arbitrarily small.
An additional term proportional to \(\sigma-1\) gives the same obstruction for switches.
Thus even physical equality plus a small uniform bound does not identify the required continuation.

This example does not assert that both extensions solve (S5).
It shows why the missing equation identification cannot be replaced by the identity theorem.
The native inner problem also has its own boundary convention; its restriction theorem does not identify PI's compressed whole-action problem at the changed outer rows.
The route fails at extending the actual common-row equation and its chart to the original independent-current domain.
It does not fail for lack of a physical alignment theorem.

### Route 3. Choose a new small shift and rebuild the change of variables

There is freedom to change the construction. Use it directly: choose an admitted small holomorphic \(\widehat H\) on the buffered cut, and use its bondwise diffeomorphism and Jacobian.
This gives a legitimate change of integration coordinates when its usual smallness conditions hold.
It does not by itself give the required localized tests.

The obstruction is visible in one commuting subgroup of \(SU(2)\).
Let the actual relative background be \(e^{idT}\), and let the proposed shift be \(\widehat hT\), with a fixed unit Lie algebra generator \(T\).
At a bond where the cutoff equals one, write the new variable as \(e^{iaT}\).
Its coordinate relative to the proposed local background is then
\[
 a+d-\widehat h. \tag{22}
\]
The intended local test would use \(a\).
Put \(\Delta=d-\widehat h>0\), with \(\Delta\) arbitrarily small, and choose
\(a=2\delta-\Delta/2\).
The test \(|a|<2\delta\) passes, whereas
\(|a+\Delta|<2\delta\) fails.
For a nonconstant smooth cutoff, choose a point in its transition interval instead.
Thus a small error does not give equality of the retained test factors.

This is the exact use of the relative-background identity in SA 17518–17526 and `st1-r4`'s strip calculation.
I 137392–137395 replaces the shift in the same change-of-variables construction by the localized stage function.
Its real function must consequently be rebuilt together with the actual local background and the tests.
Defining that background by \(V^{\rm loc}=e^{-i\widehat H}V^{\rm bg}\) enforces (3), but does not prove locality: the right side still contains the original nonlocal background.
That returns to BZ-JOIN.

Hence exact coordinate substitution alone does not complete the new construction.
This is not a counterexample to every buffered cut.
It is a failure of the third proposed route to the same supplier.

**Stopping condition (c).** BZ-JOIN remains unsupplied after these three routes: restriction of the fixed equation, continuation of the physical comparison, and replacement by an arbitrary small shift.
No counterexample to BZ-JOIN or to every buffered construction has been proved.

## 6. Consumer check

I searched the account for the localized layer, its \(H_Z^{(j)}\) notation, the T-step lemma and its equation labels.
I also searched the library for localized-layer/BZ-CUT/C0-ETA references and U22/U24.
The existing `layer-find` catalog supplies the use numbering and the complete T-step caller list.
Its quoted targets were checked against the bounded source excerpts above.
The following table groups repeated uses of the same property; it does not count them as separate suppliers.

| Consumer | What survives the new geometry | What remains required |
|---|---|---|
| Item 10, I 131725–131746; U22 | A specified cut, partition, PI gaps and supplied bare boundary. | The same-constant layer theorem on this cut, on the original domain, and its actual-function identification. BZ-JOIN is not supplied. |
| Interrupted change, I 137320–137440,137559–137615; U24 | The bonds \(S^P\), their full local carriers and the stage count remain in the protected core. The original stage datum \(b(\mathsf B)\) and the operators in families \(\beta1,\beta2\) are not replaced by cut operators. | Family \(\beta3\) uses the actual new relative shift, its Jacobian and its domain. Its exponential estimate cannot be inferred from the boundary inverse alone. |
| Shifted arguments, I 137587–137615; cutoff-dependence lift, I 81183–81265,81446–81568 | The algebra still gives a segment from the 6.3-radius ball into the 6.6-radius ball if \(2H_{\max}<0.3\delta'_j\). It applies to any correctly identified shift satisfying its hypotheses. | The new function must be holomorphic on the prescribed lifted domain and obey the bound there. Smallness at real fields is insufficient. |
| Layer ceiling, I 131820–131845,131910–131938 | A fixed enlargement of the coefficient of \(H_{\max}\) can be paid by the existing final coupling ceiling argument. | This does not prove that the new shift has the advertised \(e^{-4R_k}\) profile. |
| Birth and later reading of arrested terms, I 138540–138630,138935–138975,139010–139050 | The original component, piece and frozen birth threshold stay the same. The new boundary lies on the supplied positive birth stratum, even at later readings. | The new terms must depend on their declared \(Y\), and all composites must use the actual continuation. Boundary trace containment does not establish that nonlinear locality. |
| Strip and retained tests, SA 17518–17526; `st1-r4`, Lemma F1 and LOC-form | The bondwise diffeomorphism argument and protected strip reads remain available. | Equation (3) and the corresponding local background must be supplied. Route 3 shows the precise failed substitution. This gives no result on the separately owned fibre measure. |
| New-term estimate and stored-term domains, I 137425,137495–137536,137622–137633 | Their radius and counting arguments can use a new common fixed layer constant. | Their actual H-function, source profile and complete-domain hypotheses remain inputs. The fixed inset does not imply them. |
| Ordinary T calls, I 131633–131699,136306–136438,137189–137275; completion and later-map calls, I 138055,138106,139875 | These use the original stage/completion determining sets. The proposed inset is applied only to item-10 localizers. Their geometric objects are therefore retained. | All their original layer and admission premises remain. The raw-point qualifications at I 136323 and 140824–140876 are not removed by this note. |
| Other localized small-solution calls, U05–U13, especially I 94185–95916,99780–99892 | These are the separately specified \(\mathfrak B^0,\mathfrak B^C\), shifted-base or derivative problems in `layer-find`. They are not identified with our new item-10 cut. | Their F2 scope clauses, original domains and physical identifications retain their status. Our boundary certificate is not a blanket supplier for them. |

The library-side check is as follows.

| Library premise or use | Disposition |
|---|---|
| `leaf-bz`, `bz-geom`, `hstep-tree` BZ-TRACE branch; `c0-sup` Proposition 4.1; `pi-admit` §4 | The own-cut geometry and C0-ETA implication in §§2–3 are supplied, conditional on the account's declared birth geometry and ambient memberships. The old literal-cut identification is not asserted. |
| `layer-thm-part` PI and UA.L0 | The tower floors and the bare crossing patches are checked. Interior real gauges, exterior twists on other reads, and every original PI premise are still required where previously required. |
| `layer-thm-part` GW; `walks-gw` U22/U24 | The graph-walk theorem can be used on an admitted new PI problem. Its absolute-tail and weighted-response conclusions do not admit that problem or identify its physical layer. |
| AV and UA.R/A0 | Complete reads on the retained core and boundary are protected. A changed positive staircase row still needs its actual branch and full carrier frame. Grade lowering is not chronological heredity. Full chart entry is part of BZ-JOIN and the standing UA premises. |
| UA.S | The frozen boundary uses the birth positive cubes and their own continuation. Earlier-frame, old-origin and exceptional cube obligations elsewhere in S are retained. |
| UA.T and ID/EQ/PH/LC | BZ-JOIN is the first new cut-specific gap. The common intermediate chart, seven-term equation, normalized actual function and full-footprint locality have not been proved. An own-current identification does not identify the independent-current continuation. |
| UA.P2 | The geometric cut is deterministic in the label, so both cutoff references can use the same cut. This does not admit either complex-parent interpolation. |
| M/RJ, full response tuples and partial segments; `ca-f`/`ca-claude` | No current identity is replaced by a value bound. The weighted response tuple and the current of the actual segment remain necessary. These notes treat additional constructions, not an alternative proof of item-10 entry. |
| `adm-pl`, `layer-pkg`, `layer-r3`, `layer-thm`, and their prior snapshots | Their U22/U24 rows retain the same original-domain and actual-operator qualifications. The new C0 result supplies only the boundary part. The snapshots add no independent theorem. |
| `hcm-repair`/`hcm-tb` | Keeping positive top rows at the outer boundary leads to their separately owned TB-BC problem. Our construction has a bare outer rim; it does not solve or reuse a claimed solution of TB-BC. |
| `joint-loc` | Its JOINT-CONTAIN and nonlinear old-projection tasks concern prescribed full boxes and joint supported expansions. They do not supply the item-10 alignment for this new cut; no work on those owned targets is claimed here. |

Thus every affected consumer has a disposition, but not every required analytic consumer is verified.
The unverified entries are why the outcome is (c), rather than a completed BZ-CUT construction.

## 7. Constants, scope and result

The geometric choices are uniform over histories, births and later readings.
They are made in this order:
\[
 (L,\text{common PI constants})\ ;\quad m\ ;\quad M\ ;\quad w=16L\ ;\quad
 R_*\ ;\quad\text{the final coupling ceiling}. \tag{23}
\]
Keep the account's other earlier choices in their original order.
Choose the old free block constants to meet the new lower bounds at their own places in that order.
The following changes have actually been justified.

| Constant or domain | Change |
|---|---|
| Erosion block size | Use the fixed \(m\) of (4), with the same compatible divisibility as PI. |
| Construction size \(M\) | Enlarge its original fixed lower bound by the bound following (4). This also makes the containing-cube argument fit. |
| Buffer width | \(w\) top-grid cells. In physical units it is \(wM\ell_k\); the cell count is fixed before \(R_k\). |
| Running-radius floor | Add (10) and (18). Since \(R_k=\check R_k\) grows under the final small-coupling choice, these are fixed floors, not new history-dependent constants. |
| Original parameter radii | No disc for an admitted entry is replaced by a smaller disc. The coefficient argument uses its original supremum bounds. |
| Original component and test thresholds | Keep \(X_{\mathfrak a}\), \(W_{\mathfrak a}\), \(S^P\), \(N_k\), \(\delta'_j\), and the 6/6.3/6.6 margins. \(Z\) is an auxiliary localizer, not a new large-field label. |
| Analytic constants \(B_\sharp,C_F,K_{\mathfrak f},C_{22}^P\), and the layer contribution to the final ceiling | No numerical or symbolic enlargement is certified before BZ-JOIN and the actual weighted profile are supplied. A fixed proved loss could be absorbed by taking common maxima before the final ceiling, as in I 131910–131938. An unknown loss is not a constant choice. |

A changed metric or a shorter collar also cannot be handled by simply retaining the printed exponent.
For example, if a future comparison proves a loss of at most a fixed \(b_0\) in its scaled distance, its exponential bound costs \(e^{\delta b_0}\).
That elementary observation does not prove the needed comparison or its \(e^{-4R_k}\) envelope.
The source set \(\mathfrak L\) in I 137582–137585 must be the one for the actual reconstructed layer; it cannot be replaced by an arbitrary distant set.

The named Balaban scratch directory was absent on this machine.
The method and formula used here were read in the account's quoted CMP 119 passages.
No search outside the authorized locations was made.
No CMP 122 proof or computer calculation discharges any step.

**Result: stopping condition (c).** There is a buffered geometric candidate with a supplied bare-boundary coefficient entry.
There is not a completed consumer-preserving localized layer construction.
The next step is an actual common-chart/datum proof, not a larger buffer or a smaller replacement parameter box.

| Requested part | Status of this research note |
|---|---|
| (i) Partition identity | Proved for the explicit cut, (12), on the declared birth geometry. |
| (ii) PI gaps and bare crossing patches | Proved for that cut, (13)–(14), retaining the stated parent gaps and torus conditions. |
| (iii) Complete exterior read and C0-ETA | Proved for the restricted ambient coefficient pair, (15)–(18), under the original item-10 ambient memberships. Includes the outward tangential edge of the kill test. |
| (iv) Every localized-layer consumer | Checked for requirements; not all verified. The full-domain actual-function step remains open. |
| Complete proof or counterexample to every buffer | Neither is claimed. |
| Three-route stopping condition | Met at the one supplier BZ-JOIN, §5. Failure of those routes is not a refutation of the lemma. |
| Scientific/audit status | None granted or changed. |

**First open input: BZ-JOIN (§4), the full original-domain alignment of the actual induced and literal joined cut data, with the independent current, switches, common normalization and admitted interpolation.**
