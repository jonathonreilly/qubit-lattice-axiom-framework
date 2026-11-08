# Live strips through an interrupted preparation

Checked line by line by Claude (Opus 5.5), gates/geoh-live-ab-check.md: ADVANCE; citation repairs applied.

Codex, 2026-11-08. Source revision `34be8fadc9f113211d6f5968d756e57241515b62`.
FINISH row 498. Research text, not an audit. This text grants no status.
No numerical calculation or machine enumeration supplies a proof step.
Written and author-checked by Codex; the subsequent line-by-line check is recorded above.

## 1. Sources and the exact target

Credit Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text.
Credit Tadeusz Bałaban for the large-field method and its preparation geometry.
The source keys below always refer to these revisions.

* **I:** [complete account, Part I](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex), commit `31a47c543775`.
* **SA:** [YM4_sketch_500.tex](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM4_sketch_500.tex), at the same commit.
* **N:** [YM4_1400.tex](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/2bc0658f91d2d03ba44e20bf695067e0a56a2ed9/YM4_1400.tex), commit `2bc0658f91d2d03ba44e20bf695067e0a56a2ed9`.

The local starting points are `prior/geoh.md`, `geoh.md:1–60,360–400`, and `../gates/geoh-gate.md`.
Their genealogy, waiting, code-counting implications and prepared-gap arguments are not new work here.
`prior/geoh-live-ab.md` is absent at this checkout.
The registry leaves O-live-geometry unowned; FINISH assigns these two subclauses to this lane.
GEOH-O1, O2 and O6 remain separate rows.

The target is I 85575–85621 and 85635–85639.
The source calls this definition “Proof outstanding”.
It expressly uses the listed assertions as hypotheses, at I 85598.
Here we distinguish geometric supply from the consequences of those hypotheses.

Use periodic distances on the torus.
Only bounded operation boxes require a common nonwrapping chart.
This follows the proposed contract in `geoh-o6.md`, section 7.
It does not assert a lift for every recursive carrier.

### Port ledger

Each row records what its cited passage supplies, before any use below.
“Proved” describes the source argument, under its stated premises.
It is not an independent check of its entire dependency chain.

| Premise or step | Source | Source standing and permitted use |
|---|---|---|
| Nested cube grids, native cells, touch and meet | I 62735–62780 | Definitions; cells here have side one in their own cube units. |
| Fixed birth strip and its lifetime | I 63523–63544 | Definitions; birth means a second-class output of R. |
| Same-level strip separation | I 20441–20468; 63547–63562 | Fixed-grid geometric statement; the birth component assumptions remain explicit. |
| Radius comparison across levels | I 63563–63569, 63643–63649 | Proved by telescoping the adjacent ratios. |
| T avoids the incoming large-field collar | I 12103–12144, 12187–12265 | Proved from the eight-layer construction and the radius comparison; port its geometric argument. |
| Prepared nests and stage collars | I 53737–53819 | Definitions and cited Bałaban construction; not an all-history collar theorem. |
| Thin-zone gap | I 63670–63700 | Conditional proof using the stated T and prepared geometries. |
| Treated-strip separation from every preparatory collar | I 63908–63916 | Conditional proof from the lower prepared member and strip containment. |
| Live geometry, clauses (a)–(d) | I 85575–85617 | Explicit hypotheses; the persistent invariant is not proved by this definition. |
| Untreated-component and integration-site clauses | I 85618–85621, 85635–85639 | Explicit hypotheses; they must be matched to actual sites. |
| Raised cells and arrested attempts | I 64796–64876 | Definitions and stated assertions; their supplier must be inspected before use. |
| Scaled side used in reception bounds | N 81378–81393 | Uses the birth size and radius comparison. |
| Level ceiling and collar used for depth | N 85170–85188 | Uses native strip geometry; does not construct it. |
| Prescribed separated strips used in filing | N 85294–85302 | Conditional filing construction. |
| Birth collar pays strip counts | N 127515–127539 | Conditional analytic counting consequence. |
| Old-strip buffer pays crossing length | N 127686–127697 | Conditional crossing consequence. |

The index was searched first for strips, cells, histories, interruptions and preparations.
Relevant entries are SA chunks 05 and 16, their obligations, and CA 4.12–4.19 chunks 03 and 09.
The CA full index omits definitions and remarks such as `4.21:def-strips-geometry`.
Their source anchors were therefore searched directly.

## 2. The actual strip and the cell convention

Write \(u_j\) for the physical side of a cube of \(\pi_j\).
Thus \(u_i/u_m=L^{i-m}\).
Write \(R_j=\check R_j\) and \(q_j=\lfloor(R_j-1)/2\rfloor\).
Use the source floors: odd \(L\ge3\), \(M\ge1\), and \(R_j\ge38\).
The radii are powers of \(L\), with \(R_j/R_{j+1}\in\{1,L\}\).
They are scale inputs, as specified at I 63563–63569 and 63621–63623.
Local birth and operation boxes use their supplied admissible torus charts.

A live pocket is a second-class region \((Y,m)\) created by \(\mathbf R_m\).
Its strip is the fixed set
\[
 S_Y=Y^\sharp=Y^{(q_m)}.
 \tag{1}
\]
The enlargement uses \(\pi_m\)-cubes, once, at birth.
It is not recomputed on the current grid.
These are Sussman–Alpoge's definitions, I 63523–63544.
An interruption before localisation does not kill the old pocket.
A later localisation of its containing component does kill it, whichever class follows.
An arrested attempt is a separate mark, I 64796–64847.
It does not create another second-class strip around the containing component.
Otherwise nested arrests would create overlapping copies of the very object being counted.

Two cell notions must stay distinct.
The boxing cells of `geoh.md:9–21` have side \(R_j u_j\).
The native cells in I 62763–62769 have side \(u_j\).
The current determining sequence assigns each native cell its level.
Clause (b) concerns these native cells.
It does not require one large strip to fit inside a single native cell.
Its ownership assertion assigns each current cell to at most one live strip.

For precision, assign boundary points by a fixed half-open grid convention.
Use the closed carriers for distance and touching.
Meeting means sharing a cube on one grid, or an interior point on different grids.
This is the convention of I 62740–62748, with boundary ownership made explicit.
Once cell saturation and strip disjointness are established, define
\[
 \operatorname{owner}(\Delta)=
 \begin{cases}
 (Y,m),&\Delta\text{ meets }S_Y,\\
 \varnothing,&\text{no live strip meets }\Delta.
 \end{cases}
 \tag{2}
\]
Formula (2) does not itself prove that its first case is single-valued.

The birth size gives a port, not a fresh research claim.
If the birth component has side at most \(100R_m u_m\), then
\[
 s_i(Y)=s_m(Y)L^{-(i-m)}
 \le(100R_m+2q_m)L^{-(i-m)}
 \le(101R_m-1)L^{-(i-m)}\le101R_i.
 \tag{3}
\]
The first bound is the birth component specification in I 63547–63562.
The last is the proved radius comparison in I 63643–63649.
The identity uses the fixed strip, not a succession of enlargements.
For simultaneous births, separated boxing cells give
\(\operatorname{dist}_m(S_Y,S_{Y'})\ge R_m-2q_m\ge1\).
This is the same-level port from I 20441–20468.
It does not establish separation between two different birth levels.

## 3. The lower prepared member on the same history

Put \(a_j=R_j u_j\). This is a boxing-cell side, not a native-cell side.
For a set of boxing cells, \(N_r\) means adjoining \(r\) cell layers.
For \(t\ge2\), the T rule is
\[
 (\Omega_t^{T})^c
   =N_2Q'_t\cup N_4P'_t\cup N_8\widehat{Z_{t-1}},
 \qquad Z_t^{T}\supset N_2(\Omega_t^{T})^c.
 \tag{4}
\]
Boxing and subsequent failures only enlarge the second set.
This is the construction in SA 17317–17332 and I 50196–50229, 50342–50368.
Thus new failures and joining cannot reduce either buffer in (4).
The T-buffer argument is already proved in I 12187–12265; we port it here.
That lemma's coupling argument is unnecessary because the present radius comparison is already available.
The first step has its separate tests and no incoming pockets, I 50231–50300.
No first-step version of (4) is needed for a live strip.

For an attempt on \(C\) at step \(k\), put \(h=k-N_k\) and \(D_i=Z''_i\cap C\).
The lower preparation uses five layers of the boxing grid of level \(i\).
Its layer side is \(a_i\), for \(h<i\le k_0\).
The five-layer rule is I 53783; the layer side is specified at I 63703–63716.
N 63773–63812 makes the lower construction explicit for its quiet-box special case.
The first member has \(h+1\le k_0\), since \(N_k>N_0\).
The upper members use their prescribed native grids.
They are nested and obey
\[
 D_i\subset D_{i+1},\qquad
 \operatorname{dist}(D_i,D_{i+1}^{c})\ge u_{i+1}
 \quad(h<i<k).
 \tag{5}
\]
Distances here are inside the operation box, with its exterior margin retained.
The upper gap is the stated one-layer rule at I 53778–53781.
N 63798–63825 gives quiet-box formulas for the special case without joining; those formulas are not used for the broader class here.
We use that existing preparation; we do not replace its grid or selector.
In the lower range, its gap follows directly from (4) and (6), applied at consecutive levels.
The next hull contains \(Z_i\cap C\), which contains \(D_i\).
Its three added layers give distance at least \(3a_{i+1}\ge u_{i+1}\).
The upper range uses the one-layer rule quoted at I 53778–53781.
This proof does not use the statement at I 64468–64472 that live-region geometry already applies.

**Lower-member calculation.** On the actual label at this attempt,
\[
 N_3 H_{h+1}\subset D_{h+1},
 \qquad H_{h+1}:=\widehat{Z_h\cap C}
       \quad\text{on the level-}(h+1)\text{ boxing grid}.
 \tag{6}
\]
Here is the endpoint check needed to use the published calculation.
CA's exclusion interval is \((h,k)\), at I 45992–46032.
An earlier standing second-class region in \(C\) therefore has birth level \(m\le h\).
A standing arrest in \(C\) has step at most \(h\), by the same rule.
The closed lower endpoint of SA 17575 is stronger and is not used here.

Trace a surviving component of the current \(Z_h\cap C\) back to step \(h+1\).
Each intervening T step leaves the earlier entries unchanged.
An intervening completed operation on that component would remove its level-\(h\) entry.
An intervening interruption would leave a standing mark in \((h,k)\).
If that mark later disappeared, a completed operation would again remove the entry.
The first alternative contradicts survival; the second contradicts eligibility.
Operations on other components cannot cut this component or its connected buffer.
They act on whole top components.
Thus the eight-layer buffer made at step \(h+1\) survives in the current \(\Omega_{h+1}^c\).
In particular,
\[
 N_8H_{h+1}\subset\Omega_{h+1}^c\cap C.
 \tag{7}
\]
This is the surviving-component argument of N 63718–63771, with its endpoint use stated explicitly.
Only steps strictly above \(h\) occur in this argument.
An operation at \(h\) is already included in the input to T at \(h+1\).
No prohibition of that operation is needed.
Joining may add other predecessors. It does not invalidate the inclusion (7).

Now remove five layers from the eight-layer buffer.
In cell indices, a cell within three steps of \(H_{h+1}\) is at least six steps from any exterior cell.
Five layers added to that exterior cannot reach its interior.
The retained closed carriers give (6).
This also proves the inclusion for a union of hull cells; no box equality is needed.
For a box, it is exactly Sussman–Alpoge's erosion calculation, N 63785–63812.
All its sets lie in \(C\), since (4) also supplies the ten-layer buffer.
The same tracing and erosion apply at every lower index \(h<i\le k_0\).
They give \(N_3\widehat{Z_{i-1}\cap C}\subset D_i\) on that index's boxing grid.
This justifies the lower gaps used in (5), including when the retained lower label contains an older arrest.

Consequently, for any old live \((Y,m)\) in \(C\),
\[
 Y\subset Z_h\cap C,\qquad
 \operatorname{dist}_{h+1}(Y,D_{h+1}^c)\ge3R_{h+1}.
 \tag{8}
\]
The first inclusion uses retention of \(Y\) and label nesting.
It does not assert that the larger strip already lies in \(Z_h\) when \(h=m\).

## 4. The critical interrupted cycle

Fix one actual history with a live pocket \((Y,m)\).
Suppose its containing component \(C\) is attempted at step \(k\), with \(h=k-N_k=m\).
Include a standing interrupted mark \(\mathfrak a=(A,m,n,n^+,e)\) in \(C\).
At step \(m\), \(A\) and \(Y\) were different components with different outcomes.
Later T steps may join their descendants.
CA's class permits this joining and the mark at its lower endpoint, I 45992–46032.
The lower index is shared; the earlier interiors and their determining cells need not be flat.
In (6), retain all of \(Z_m\cap C\), including the interrupted component.
Replacing that set by \(Y\) would discard the history that must be checked.
All sets in this section belong to this history and its current determining label.
We do not infer existence of a field configuration by assigning arbitrary test outcomes.
The argument covers every actual branch with these data.

The strip extends beyond \(Y\) by \(q_m u_m\).
Equation (8), converted to birth units, gives
\[
 \begin{aligned}
 \operatorname{dist}_m(S_Y,D_{m+1}^c)
 &\ge3LR_{m+1}-q_m\\
 &\ge3R_m-\frac{R_m-1}{2}
   =\frac52R_m+\frac12.
 \end{aligned}
 \tag{9}
\]
The worst radius comparison is \(R_m=LR_{m+1}\).
When the hull adds no extra width, this calculation leaves exactly the displayed lattice margin.
The contract uses only \(5R_m/2\).
It does not require equality with that weaker number.

Set
\[
 B_Y:=\{x:\operatorname{dist}_m(x,S_Y)<5R_m/2\}.
 \tag{10}
\]
Equation (9) puts \(B_Y\) inside the first prepared member.
The same member contains \(A\), since the standing mark remains in \(Z_m\cap C\).
Thus the old interruption is not integrated by a preparatory collar of this attempt.
Every later prepared member contains it by (5).
Stopping after any prefix therefore leaves it outside the current \(\Omega_{m+1}\).
Stopping before any relabelling leaves the wider T buffer instead.

One branch needs separate care.
At the exit corresponding to Bałaban's (1.55), the variable change is performed but its fluctuation integral is not.
The retained geometry has \(n^+=n+1\), not \(n\).
This is I 64420–64442 and 64527–64535; the variable description is I 81735–81756.
For \(n=0\), it already retains \(D_{m+1}\).
Thus (9) applies even when no fluctuation integral was completed.
For \(n>0\), every additionally retained member contains \(D_{m+1}\).
The same bound applies.
The stopped component stays in the top large-field region, and its mark stands.

Now perform the next complete cycle, T at \(k+1\) followed by R at \(k+1\).
The old strip lies in the stopped top component of \(Z_k\).
Equation (4) therefore gives
\[
 \operatorname{dist}_k(S_Y,\Omega_{k+1}^{T})
       \ge8LR_{k+1}\ge8R_k>7R_k.
 \tag{11}
\]
The step changes no earlier domain, including \(\Omega_{m+1}\).
New failures may join this component to others. Its existing buffer remains.

R at \(k+1\) cannot treat the resulting component.
Its standing mark has step \(k\), strictly inside \((k+1-N_{k+1},k+1)\), since \(N_{k+1}\ge3\).
Every treated component is consequently different from this component.
Distinct top components are separated by at least \(a_{k+1}\).
All their preparation collars and their main integration regions stay inside those components.
Thus every such region is at distance at least \(R_{k+1}\) from \(S_Y\), in level-\(k+1\) units.
Their integration bonds cannot bridge that gap; section 6 gives the bond check.
No operation in this cycle changes the old strip or its birth collar.

If a still later attempt on this lineage occurs at step \(b\), its lower index satisfies \(h_b\ge k\).
This is the open-window timing rule, proved in I 132162–132176.
Hence \(h_b>m\).
Its preparation leaves \(\Omega_{m+1}\) unchanged.
The narrow birth collar is never charged a second loss.
The next completed localisation removes the old pocket; it does not leave a damaged live strip.

## 5. Induction over all moves

**Theorem.** Use the printed T rule, whole-component outcomes and prepared sequence specified above.
For every finite history of these rules, the following assertions hold at every applicable read site.
No test outcome, field value, age, stage count or number of components enters the constants.

1. For \(i\ge m\), the fixed strip satisfies (3).
2. Distinct live strips are disjoint. Every current native cell meeting \(S_Y\) lies in it and has level at most \(m\).
3. Once level \(m+1\) exists, \(B_Y\subset\Omega_{m+1}^c\). Every cell at birth-distance less than \(5R_m/2\) has level at most \(m\).
4. For every existing \(i>m\), \(B_Y\) lies in the component of \(\Lambda_i^c\) containing \(Y\).
5. The T-site bound is \(\operatorname{dist}_i(S_Y,\Omega_{i+1}^{T})\ge7R_i\).
6. At P and L, an old strip in an untreated component has distance at least \(R_k\) from the treated region.
7. At P, the treated-strip bound is \(\operatorname{dist}_{h+1}(S_Y,R_\nu)\ge5R_{h+1}/2\).
   The untreated-strip bound is \(\operatorname{dist}_k(S_Y,R_\nu)\ge R_k\).
   No P integration bond meets a live strip.

Here an old strip at R at step \(k\) has \(m<k\).
New second-class outputs of that operation enter the next cycle.
The size assertion also uses \(i\ge m\), as in I 63567 and N 81388–81390.
It does not assert the displayed bound on arbitrarily finer grids.

**Proof.** Order the moves by step, then by preparation stage and component decision.
Initially there are no pockets.
At a birth, retain the old pockets until their containing component is localised.
Remove those pockets at that localisation.
Insert its new second-class pocket only if the final class decision supplies one.
This is the lifetime rule of I 63524–63545 and the whole-component rule of I 64479–64497.
Thus a new pocket never coexists with its consumed ancestors.

First prove retention of the set \(Y\), without using strip disjointness.
At birth, \(Y\subset Z_m\).
T leaves earlier entries alone and surrounds the current top component.
For any later attempt containing \(Y\), the birth factor and the exclusion rule give \(h\ge m\).
Preparation changes only levels above \(h\), so it leaves \(Z_m\) unchanged.
Another component cannot change points of \(Y\).
A completed operation on its own component ends its life.
Induction gives \(Y\subset Z_m\subset Z_i\) for every existing \(i\ge m\) while it lives.
This establishes the retention used in (8).

Next prove the birth collar.
Immediately after birth, every native cell has level at most \(m\).
There is no higher domain yet to check.
At T at \(m+1\), (4) and the strip's reach give
\[
 \operatorname{dist}_m(S_Y,\Omega_{m+1}^{T})
 \ge8LR_{m+1}-q_m
 \ge\frac{15R_m+1}{2}>\frac52R_m.
 \tag{12}
\]
Hence (10) lies outside \(\Omega_{m+1}\).

Suppose this collar survives up to a later move.
T does not change \(\Omega_{m+1}\).
For R, nesting gives \(B_Y\subset\Omega_{m+1}^c\subset Z_i\) at every existing \(i>m\).
The set \(B_Y\) is connected and contains \(Y\).
It therefore belongs to the same top component as \(Y\).
An operation on another component changes no part of it.
An operation on its own component has \(h\ge m\).
If \(h>m\), it leaves \(\Omega_{m+1}\) unchanged throughout preparation.
If \(h=m\), (9) protects \(B_Y\) after the first replacement.
Later replacements are nested, and an interruption freezes a prefix, including the extra raise when applicable.
Thus every incomplete branch preserves the collar.
If localisation completes, this pocket dies and the assertion ends.
This proves assertions 3 and 4 by induction.
The proof uses the determining sequence. It does not substitute the action sequence for it.

A native cell of level \(n>m\) has its interior in \(\Omega_n\subset\Omega_{m+1}\).
It cannot have an interior point in \(B_Y\).
If its closed carrier had distance less than \(5R_m/2\) from \(S_Y\), nearby interior points would lie in \(B_Y\).
That is impossible.
This proves the collar's cell-level assertion.
In particular, a cell meeting \(S_Y\) has level at most \(m\).
The strip is a union of \(\pi_m\)-cubes, and the grids are nested.
A finer cell whose interior meets it lies wholly in one of those cubes.
At equal levels, meeting already means having the same cube.
Thus every meeting cell lies wholly in \(S_Y\).

We can now prove mixed-birth disjointness.
Old strips do not move under T, joining or an interrupted operation.
Consider a new birth at step \(k\) on component \(C\).
An old pocket in \(C\) has been removed by localisation.
Any remaining old strip lies wholly in a different top component \(C'\), by assertion 4.
Before the operations, top components are disjoint unions of boxing cells of side \(a_k\).
Their closed carriers have distance at least \(a_k\).
The new strip extends beyond \(C\) by only \(q_k u_k\).
Hence
\[
 \operatorname{dist}_k(S_Y,S_{\rm new})
 \ge R_k-q_k\ge(R_k+1)/2>0.
 \tag{13}
\]
For two new births, the stronger same-level port after (3) gives distance at least one.
Healing deletes pockets; it creates no strip.
This completes the disjointness induction.
Cell saturation now makes (2) single-valued.

For the T-site bound, let the input level be \(i\).
Use the ported T-buffer argument from I 12187–12265.
If \(m<i\), assertion 4 puts \(S_Y\) inside the input \(Z_i\).
Equation (4) gives distance at least \(8LR_{i+1}\ge8R_i\).
If \(m=i\), subtract the birth reach \(q_i\), as in (12).
Both cases give assertion 5.
Failure rounds and boxing add sets, so the bound survives creation and joining.

At R at level \(k\), an untreated old strip lies in its own top component \(C'\).
Every treated component is different from \(C'\).
The same boxing-grid separation gives distance at least \(R_k\), proving assertion 6.
It holds throughout P and at L, because those sites act inside the selected components.
If one selected component has already exited, treating it as untreated for later integrations only removes integration sites.

Finally suppose the containing component is treated.
By (8), its first prepared member has three layers beyond \(Y\).
In units of level \(h+1\), the strip's additional reach is at most
\[
 q_m L^{-(h+1-m)}\le\tfrac12 R_{h+1}.
\]
The radius comparison is the port used in (3).
Every collar \(R_\nu\) lies outside \(D_{h+1}\), by nesting.
Subtracting this reach from (8) gives assertion 7's treated bound.
This is the conditional argument already printed at I 63909–63915.
The induction above now supplies its retained-strip premise.
For an untreated component, \(R_\nu\) is inside the treated region, so assertion 6 gives the other bound.
The remaining bond assertion is checked next. \(\square\)

## 6. Every integration site

**Preparatory collar and rim.** At stage \(n+1\), put \(j=h+n\).
I 74309–74320 gives the two actual coordinate sets:
\[
 (\Omega_{j+1}^c\setminus D_{j+1})^{(j)*},
 \qquad (Z_{j+1}\cap\Omega_{j+1})\cap C.
 \tag{14}
\]
Both lie in the complement of \(D_{j+1}\) inside the treated component.
The first carries \(B_j\); the second carries the rim variables \(A_j\).
Use the incident-bond convention, which is the larger convention.
I 159058–159075 counts bonds with at least one endpoint in the coordinate set.
Removing pivots can only reduce this set.
A level-\(j\) bond has length \(u_j/M\le u_j\).

For the first stage, (8) and the strip-reach subtraction give
\[
 \operatorname{dist}(S_Y,D_{h+1}^c)
       \ge\tfrac52R_{h+1}u_{h+1}>u_h.
 \tag{15}
\]
For a later stage, \(j>h\), the strip lies in \(D_j\).
The prepared gap (5) gives distance at least \(u_{j+1}=Lu_j>u_j\) from either set in (14).
An incident bond of length at most \(u_j\) cannot reach the strip.
This treats every stage, including the coarse stages where the birth-unit bound alone would not control a bond length.

For a foreign strip in an untreated component, assertion 6 gives distance \(R_k u_k\).
Every stage has \(j<k\), so its bonds are shorter than this distance.
Its rim bonds are covered by the same estimate.
An exited sibling has no subsequent integration on its own component.
The additional variable change on the (1.55) exit uses the same separated coordinate set.
It introduces no integration bond on a strip.

**Main integration and localisation.** This is a different site.
The main box contains \(D_k\), by I 53786–53804.
For an old pocket in the treated component, \(S_Y\subset D_{h+1}\subset D_k\).
Thus the main integration can meet its strip.
Clause (h) excludes integration bonds only at P; it does not exclude this main integration.
The completed localisation consumes the old pocket, by the lifetime definition.
Its output either heals the component or assigns a new birth level to a second-class component.
An early exit has no main integration.
A late exit retains the prepared label; its first member still protects the birth collar.
The late exits and their retained coordinates are listed at I 132008–132026.
In particular, the last two exits may include the main integration.
They must not be misreported as P integrations or as new strip births.

For a foreign pocket, the entire main box stays in another top component.
Assertion 6 and the bond-length bound again exclude contact.
This checks every integration site in the cycle of section 4 and in the induction.

## 7. Result and remaining interfaces

The result is a proof of the finite-history strip invariant from the specified construction rules.
It supplies the missing persistence step; it does not assume clauses (b), (c) or (d) of I 85575–85617.
The endpoint interruption leaves the collar (9), and the next cycle preserves it.
The geometric constants do not depend on the age or on the number of attempts.

The proof uses CA's open-endpoint class for the critical cycle.
The stronger closed-endpoint class in SA and N deletes that cycle and satisfies the same bounds.
It does not follow that a separate revised operation implements either class.
That dictionary remains GEOH-O1 and is not claimed here.
The preparation and whole-component rules are those stated above, not rules inferred from an analytic bound.
No conclusion about contour admission, retained norms, probe counts, or the quantum measure follows here.
The shared checkout advanced during writing; the source files used for the proof did not change from the stated revision.
Only this output file was written by this lane.

| Claim | Standing in this text | Source or first input |
|---|---|---|
| Fixed birth strip and lifetime | Ported definitions | I 63524–63545; 64479–64497 |
| Native cell convention | Ported definition | I 62735–62780 |
| Birth size and simultaneous-birth separation | Ported from the fixed-grid argument | I 20441–20468; 63547–63562 |
| Radius comparison and scaled size for \(i\ge m\) | Ported from a proved argument | I 63643–63649; equation (3) here |
| Eight-layer T construction | Input: specified transition rule | I 50196–50229, 50342–50368; SA 17317–17332 |
| Lower preparation grid and upper prepared gap | Input: specified preparation; lower gap proved by (6), upper gap supplied by the one-layer rule | I 53783 (five layers), 63703–63716 (layer side), 53778–53781 (upper gap); N 63773–63825 is the quiet-box special case only |
| Whole-component exits and flat second-class output | Input: specified transition rule | I 64420–64442, 64479–64497; SA 17415–17440 |
| Lower-member buffer at the open endpoint | Proved here from those rules | Equations (6)–(8); tracing method from N 63718–63771 |
| Worst interrupted cycle, including \(n^+=n+1\) | Proved here | Section 4; exit rule I 64420–64442 |
| Persistent birth collar and level ceiling | Proved here | Section 5, equations (9)–(12) |
| Mixed-birth disjointness and unique cell ownership | Proved here | Section 5, equation (13) |
| T-site bound | Ported buffer argument, with retained-strip containment proved here | I 12187–12265; section 5 |
| Untreated R-site bound | Proved here | Section 5 |
| Treated P-collar bound | Ported argument with its containment premise proved here | I 63909–63915; sections 3–5 |
| No P integration bond on a strip | Proved here | Section 6, with coordinate definitions I 74309–74320 and 159058–159075 |
| Main integration and late exits | Ported site distinction; checked against the invariant here | I 53786–53804, 132008–132026; section 6 |
| First open input | None for the stated finite-history theorem | A match to a different revised operation is the separately owned GEOH-O1 interface. |
