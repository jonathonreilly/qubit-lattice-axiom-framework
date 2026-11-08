## Repo search

The lead found no live-strip proof on main or PRs #10114, #10133 and #10134.
I reused `prior/repo-search-2026-11-08.md`, especially its section 6, rather than repeating that search.
`prior/live-nj.md` is absent at this checkout.

I fetched main and read its workflow at `43a1fcc374711ca50626eca667441d3ca575c7d1`.
I fetched PR #10141 at `c73ad7b177d94f89ff37b77386936e3d52b48b05` and checked its named hits:

| Hit in `research/ym4d/library/` | What it supplies; closeness |
|---|---|
| `in1.md:153–161` | Genealogy remains an input. It supplies no persistent-strip or probe proof. |
| `st1-r4.md:1698–1710` | SLOT-ST/SLOT-CA require a coordinate match. This concerns a different operation interface. |
| `open-registry.md:221–230` | GEOH-O1/O3/O4/O6 own separate realization, preparation, slot and lifting questions. |

These are snapshots of our work, not independent proofs.
The current registry leaves O-live-geometry open without another owner; FINISH row 549 assigns this subproblem.
The searches of `open-core.md`, `l17c.md` and `port-map.md` found no competing proof of this target.
The separate GEOH-O1 interface is not undertaken here.

I read `live-fgi.md`, `geoh-live-ab.md` and `../gates/geoh-live-ab-check.md` whole.
Codex's `geoh-live-ab.md`, checked line by line by Claude (Opus 5.5), supplies (a)–(e), (h), and \(m\le h\).
Its check confirms that the closed-endpoint rule removes the case \(h=m\).
`live-fgi.md` supplies the joining counterexample and the conditional ports for the present clauses.
Its counterexample is excluded here. Its probe-scale separation was still missing.
Neither prior result is rederived below.

# Live geometry with no joining in an operation window

Codex, 2026-11-08. Source revision `cf13e06cc5db4b85832b077e26e7b4649a584ac1`.
FINISH row 549. Research text, not an audit. This text grants no status.
Written and author-checked by Codex; not yet checked by the other model.
No computation supplies a proof step. Only this file is written.
The shared checkout advanced during writing; the cited prior notes and index were unchanged from the source revision.

## 1. Sources, rules and units

Credit Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text.
Credit Tadeusz Bałaban for the large-field method and its preparation geometry.
Every port below identifies its source lines. The source keys are:

- **I:** [complete account, Part I](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex), commit `31a47c543775`.
- **SA:** [original outline](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM4_sketch_500.tex), the same commit.
- **N:** [revised outline](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/2bc0658f91d2d03ba44e20bf695067e0a56a2ed9/YM4_1400.tex), commit `2bc0658f91d2d03ba44e20bf695067e0a56a2ed9`.

The index was used first: README, chunk 16's neighbouring rows on SA 17415–17583, and the corresponding obligations.
The CA 4.12–4.19 index points to I 45962–46032 and 53737–53819.
The full CA index has no entry for the unfinished live-geometry remark.
Its anchors and the prior note locate I 63772–63971 and the target, I 85575–85644.
The latter calls its geometric assertions hypotheses and labels their proof outstanding.
N 127750–127758 uses the stronger probe-scale collar; it does not prove its persistence there.

### The restriction

At an attempted operation of level \(k\), put \(h=k-N_k\ge1\).
Let \(C\) be a component of the input \(Z_k=\Lambda_k^c\), and put \(G_i=C\cap Z_i\).
Retain the account's geometric parameter and size requirements.
Impose the outlines' admission rule, with the explicit small-box cutoff of 100:

1. For every \(h\le i\le k\), \(G_i\) is one nonempty component contained in a cube of side \(100R_i\) in native level-\(i\) units.
2. For \(h<i\le k\), there is no creation and no absorbed second component: \(G_i=\Phi_i(G_{i-1})\).
3. No operation acts on this lineage at a level in \([h,k)\). In particular, no surviving mark has a level in that interval.

The small-component boxing rule makes these small components boxes, as used at N 63751–63760.

SA 17575 says “single component”, “does not absorb a second component”, and “the lower end point included”.
N 63684 repeats that rule. N 73101–73110 requires “single-box traces” and quarantine “including its lower endpoint”.
SA 17440 states “Marks wait” and \(s<t_\flat\).
These quotations distinguish both restrictions: no joining, and a closed lower endpoint.

SA 17415–17449 also fixes the transitions used here.
Healing removes the whole component. An island retains the component with a flat top label.
An interruption retains its prepared prefix and a standing mark.
The determining sequence uses the retained prefix; the action sequence keeps the formation label.
We use the determining sequence for cells and distances, as in `geoh-live-ab.md`.
The account's extra retained raise on the variable-change exit remains covered by that prior proof.

This admission rule restricts I 45992–46000 on the same input history.
Its first condition supplies (i) and the preceding-window size bounds in (ii-a).
Its second condition excludes exactly the creations forbidden in (ii-a), and excludes joining as well.
Its third condition excludes all the marks forbidden by (ii-b), including the additional level \(h\).
The window comparison is also stated at I 46024–46027.
This is a restriction of eligibility on a fixed label; it does not equate the two dynamic runs.
Joining outside an admitted window remains possible.

### Geometric construction retained

Write \(u_i\) for the physical side of a native cube of \(\pi_i\), so \(u_{i+1}=Lu_i\).
Write \(R_i=\check R_i\), \(a_i=R_i u_i\), and \(q_i=\lfloor(R_i-1)/2\rfloor\).
The boxing grid has side \(a_i\); current cells have native sides \(u_i\).
These are different grids, I 62735–62788 and 53737–53743.
Use the source inputs \(L\ge3\) odd, \(R_i\ge38\), and \(R_i/R_{i+1}\in\{1,L\}\).
In particular, \(R_i\le LR_{i+1}\).
Operation boxes and their stated enlargements use the admissible nonwrapping charts of SA 17583.

The strip is the fixed birth box \(S=Y^\sharp=Y^{(q_m)}\), I 63523–63544.
It lives until its containing component passes localisation.
An interrupted preparation before localisation does not kill it.

We use the published prepared construction, not just an arbitrary nest with one-layer gaps.
N 63749–63834 supplies its explicit quiet-box realization.
In particular, its first upper member and its terminal member are specified boxes.
I 63685–63692 and 63788–63799 state these same endpoint constructions.
The proof below retains them. No claim is made for a different upper selector specified only by nesting.

## 2. The previously proved clauses survive

Apply the transition induction in `geoh-live-ab.md` with this stronger admission rule.
Every T transition and every retained preparation prefix is still one of its transitions.
Declining an attempt forbidden by the stronger rule leaves that component unchanged and preserves the invariant.
Whole-component healing and island outcomes are unchanged.
Thus its induction supplies (a)–(e) and (h), with their original constants.
Clause (a) retains its stated domain \(i\ge m\).

More precisely, a live birth at \(m\) carries a standing mark until its consuming localisation.
If its component is treated with lower index \(h\), closed-endpoint quarantine gives
\[
 m<h. \tag{1}
\]
The prior proof gives \(Y\subset Z_i\) for \(i\ge m\), and \(S\subset Z_i\) for \(i>m\).
Consequently, at this treatment,
\[
 S\subset G_h. \tag{2}
\]
The prior induction's exceptional case \(h=m\) is now empty.
Every later preparation on this lineage leaves \(\Omega_{m+1}\) unchanged while the pocket lives.
Foreign operations do not alter its protected collar. Localisation ends the assertion for that pocket.
Thus no new persistence proof is needed for those clauses.
The stronger all-scale estimate needed for probes is proved in section 6 below.

## 3. Port of the quiet boxes and their preparation

This is Sussman–Alpoge's construction, N 63718–63834, in native cube units.
It is the box supplier missing on the larger class in `live-fgi.md`.
For a box \(B\), write \(B^{[r]}\) for its closed sup-norm enlargement by physical distance \(r\).
Set \(H_i=\widehat{G_{i-1}}\), using the boxing grid of side \(a_i\).

First identify the surviving inputs.
An earlier-label point in \(G_i\) remains in one top component at each intermediate step.
A healing would remove it from that earlier label.
An island at a later level would do the same.
An interruption would leave a mark in \([h,k)\), unless a later completed operation removed the point.
Both alternatives contradict survival or quarantine.
Whole-component transitions therefore leave the entire predecessor, and its step buffer, intact.
This is the tracing argument at N 63718–63746.

The admission rule makes \(G_h\) one small boxed component.
The hull of a box is a box: in each coordinate, take all meeting grid intervals.
Its endpoints extend by at most \(a_i\) on each face, so
\[
 G_{i-1}\subset H_i\subset G_{i-1}^{[a_i]}.
\]
No creation or joining contributes another input in this window.
The eight-layer T complement and the ten-layer large-field output are therefore
\[
 O_i:=\Omega_i^c\cap C=H_i^{[8a_i]},\qquad
 G_i=H_i^{[10a_i]},\qquad h<i\le k. \tag{3}
\]
Boxing fixes these boxes. Induction proves (3) on the retained input label.
These are N 63749–63771's equalities, also printed at SA 17578–17583.
Unlike the account's unrestricted class, this argument has one predecessor at every step.

Let \(k_0=k-N_0\), with
\[
 a_{k_0+1}=u_k,\qquad h+1\le k_0\le k-2. \tag{4}
\]
This is the preparation scale choice, I 53762–53774 and N 63773–63777.
Write \(H_*=H_{k_0+1}\), and \(D_i=Z''_i\cap C\).
The explicit preparation at N 63778–63825 is
\[
 D_i=
 \begin{cases}
 H_i^{[3a_i]},&h<i\le k_0,\\
 H_*^{[3u_k-w_i]},&k_0<i\le k,
 \end{cases} \tag{5}
\]
where
\[
 w_{k_0+1}=2u_k,\qquad w_k=0,\qquad
 w_i=\sum_{q=i+1}^{k}u_q\quad(k_0+2\le i<k).
\]

Here is the geometric check of this port.
Eroding \(O_i=H_i^{[8a_i]}\) by five boxing layers leaves \(H_i^{[3a_i]}\).
Each face of \(O_i\) borders its complement inside \(G_i\); the latter extends two more layers.
Thus this erosion uses the actual distance to \(\Omega_i\), not a distance to an artificial boundary.
At upper levels the prescribed erosion distance is \(5u_k+w_i\), giving the second line of (5).
Its faces lie on the native level-\(i\) grid: \(H_*\) is made of \(\pi_k\)-cubes and \(w_i\) is a multiple of \(u_i\).
The lower boxes are made of their boxing cells, hence also of native cubes.

For consecutive lower members, \(D_i\subset G_i\subset H_{i+1}\).
The next member adds three layers of side \(a_{i+1}\), which exceed the required native layer.
At the change of scale, \(D_{k_0}\subset G_{k_0}\subset H_*\), and the next member adds \(u_k\).
For upper pairs after the first one, the gap is \(w_i-w_{i+1}=u_{i+1}\).
At the first upper pair, if its second index is \(k\), the gap is \(2u_k\).
Otherwise,
\[
 w_{k_0+2}\le\sum_{r=0}^{\infty}L^{-r}u_k
 =\frac{L}{L-1}u_k\le\frac32u_k.
\]
The gap is then at least \(u_k/2\ge u_{k_0+2}\), since \(k_0+2<k\) and \(L\ge3\).
Thus (5) realizes the grid, nesting and one-layer requirements in I 53776–53814.
No computed estimate is used.

The two endpoint boxes deserve emphasis:
\[
 D_{k_0+1}=H_*^{[u_k]},\qquad D_k=H_*^{[3u_k]}.
 \tag{6}
\]
The first is also the one-layer formula at I 63685–63686.
The second is the five-layer erosion at I 63788–63792, using (3).
For probe separation, only (6), the lower formula, and nesting will be needed.
Thus the proof also covers other intermediate upper completions with these same endpoints and nesting.

## 4. The enlarged integration box: clause (f)

Port I 63788–63857, now with the single-box premise supplied by (3).
The actual boxes are
\[
 \Lambda_C=D_k^{[u_k]}=H_*^{[4u_k]},\qquad
 \widetilde\Lambda_C=\Lambda_C^{[u_k]}=H_*^{[5u_k]}.
 \tag{7}
\]
They are unions of native level-\(k\) cubes.
The first equality is the one-layer construction at I 53786–53804.

The small-box bound at level \(k_0+1\) and (3) give
\[
 \operatorname{side}(G_{k_0+1})
 =\operatorname{side}(H_*)+20u_k\le100u_k
\]
in each coordinate. Hence
\[
 \operatorname{side}(H_*)\le80u_k,\quad
 \operatorname{side}(D_k)\le86u_k,\quad
 \operatorname{side}(\Lambda_C)\le88u_k,\quad
 \operatorname{side}(\widetilde\Lambda_C)\le90u_k\le112u_k.
 \tag{8}
\]
This is N 63827–63834's \(88M\) integration-box bound, followed by one native layer.
Its level-\(k\) lattice unit has cube side \(M\); I's native cube unit divides these lengths by \(M\).
The stronger bound 90 therefore implies the account's requested bound 112.

Also, \(\Lambda_C\subset G_{k_0+1}\subset G_{k-1}\subset H_k\), by (4).
Since \(C=G_k=H_k^{[10a_k]}\),
\[
 \operatorname{dist}(\Lambda_C,C^c)\ge10a_k.
\]
Let \(Z\) be the running union of treated components at this site, so \(C\subset Z\).
Enlarging \(\Lambda_C\) by \(u_k\) yields
\[
 \operatorname{dist}_k(\widetilde\Lambda_C,Z^c)
 \ge10R_k-1\ge9R_k. \tag{9}
\]
This is the ten-layer distance argument of I 63837–63857.
It applies while the component is treated and its integration boxes are attached.
Thus all of (f) holds.

## 5. The core and touching cubes: clause (g)

Port I 63861–63906. Equation (1) strengthens its level inequality to \(m<h\).
The specified core, using the same component restriction as the preparation, is
\[
 \mathsf C_C=(Z'_h)^{\sim}\cap C
 =H_{h+1}^{[a_{h+1}]}. \tag{10}
\]
Indeed, \(G_{h+1}=H_{h+1}^{[10a_{h+1}]}\subset C\), so intersection with \(C\) clips nothing.
The hull and layer are boxes. This is precisely where no joining excludes `live-fgi.md`'s disconnected core.

The hull adds at most \(a_{h+1}\) at each face of \(G_h\).
The final layer adds the same amount again.
Thus each core side, in level-\(h\) units, is at most
\[
 100R_h+4LR_{h+1}\le104LR_{h+1}. \tag{11}
\]
This is the source's size calculation, I 63872–63877.

The core lies inside \(O_{h+1}=H_{h+1}^{[8a_{h+1}]}\) before preparation.
It lies inside \(D_{h+1}=H_{h+1}^{[3a_{h+1}]}\) after that member is prepared.
It therefore stays in \(\Omega_{h+1}^c\) at every applicable P or L site before localisation.
No current cell of level above \(h\) can meet its interior.
Its faces lie on the level-\(h\) native grid, since \(a_{h+1}/u_h=LR_{h+1}\) is an integer.
A cell of level at most \(h\) cannot straddle such a face.
The core is consequently a union of whole current cells, all of levels at most \(h\).
Boundary ownership uses the fixed convention of `geoh-live-ab.md`; distances use closed carriers.
This supplies the cell-union conclusion of I 63879–63892 without assuming that the inner cells have one level.

By (2), \(S\subset G_h\subset H_{h+1}\).
Consequently
\[
 S\subset\mathsf C_C,\qquad
 \operatorname{dist}_h(S,\mathsf C_C^c)
 \ge LR_{h+1}\ge R_h\ge\frac{R_h+1}{2}. \tag{12}
\]
This is I 63898–63900's \(m<h\) branch.
Its separate \(m=h\) subtraction is unnecessary on the present class.

Finally, \(S\subset D_{h+1}\subset D_k\).
Let a native cube of level \(j\le k\) touch \(S\), and take a contact point \(y\).
Every point of that cube is within sup-distance \(u_j\le u_k\) of \(y\).
The entire cube lies in \(D_k^{[u_k]}=\Lambda_C\).
This is the touching-cube argument of I 63905–63906, including boundary contact.
It completes every part of (g).

## 6. Separation in the probe's own units: clause (i1)

The source's probe argument, I 63919–63924, needs an estimate in level-\(n\) units for every \(n>m\).
Dividing clause (c)'s birth collar by \(L^{n-m}\) does not provide it.
We supply its persistent input using the published boxes (5)–(6).

**Lemma.** For every finite history of these rules, every live strip \(S=Y^\sharp\), and every existing level \(n>m\),
\[
 \operatorname{dist}_n(S,\Omega_n)\ge3. \tag{13}
\]
This holds on the determining labels, including every retained preparation prefix.
The distance to an empty domain is interpreted as infinity.

**Proof.** Induct over steps and component operations, including their intermediate stages.
At a strip's birth, no higher level has yet been formed, so there is nothing to check.
The earlier-level domains are unchanged by a T step.
It remains to check a newly formed \(\Omega_n\), and the changes made by R.

At T from level \(n-1\) to \(n\), the eight-layer rule surrounds the hull of \(Z_{n-1}\).
This is the T-buffer port already used in `geoh-live-ab.md`, equation (4), from I 50196–50229 and 50342–50368.
If \(m<n-1\), the prior invariant puts \(S\subset Z_{n-1}\), and the distance is at least \(8R_n\).
If \(m=n-1\), only \(Y\subset Z_m\) is used, and the strip reaches \(q_m u_m\) further.
Then
\[
 \operatorname{dist}_n(S,\Omega_n)
 \ge8R_n-\frac{q_m}{L}
 \ge8R_n-\frac{R_m}{2L}
 \ge\frac{15}{2}R_n\ge3. \tag{14}
\]
Extra failures or boxing enlarge the large-field side, so cannot reduce this distance.

Now consider R at level \(k\ge n\).
First suppose it acts on a component different from the one containing the strip.
Since \(k\ge n>m\), the prior invariant puts the entire strip in its own top component.
Distinct top components have distance at least \(a_k\).
Every changed point is inside the operated component.
Its distance from the strip, in level-\(n\) units, is at least
\[
 \frac{a_k}{u_n}=R_k L^{k-n}\ge38.
\]
Unchanged points of \(\Omega_n\) retain (13). Thus foreign operations preserve the estimate.
The same reasoning covers siblings already removed from the running class.

Suppose instead that R treats the component containing the strip.
Until localisation the strip remains live.
By (1)–(2), \(m<h\) and \(S\subset G_h\).
If \(n\le h\), its domain is unchanged.
For \(n>h\), a replacement changes the domain inside \(C\) to \(C\setminus D_n\).
We bound its distance directly.

For \(h<n\le k_0\),
\[
 S\subset G_h\subset G_{n-1}\subset H_n,\qquad
 D_n=H_n^{[3a_n]}.
\]
Hence \(\operatorname{dist}_n(S,D_n^c)\ge3R_n\ge3\).

For \(k_0<n<k\), use the first upper box and nesting:
\[
 S\subset G_h\subset G_{k_0}\subset H_*,\qquad
 D_n\supset D_{k_0+1}=H_*^{[u_k]}.
\]
It follows that
\[
 \operatorname{dist}_n(S,D_n^c)
 \ge\frac{u_k}{u_n}=L^{k-n}\ge L\ge3. \tag{15}
\]
At \(n=k\), the terminal box gives
\[
 \operatorname{dist}_k(S,D_k^c)\ge3,\qquad D_k=H_*^{[3u_k]}.
 \tag{16}
\]
Outside \(C\), the domain is unchanged and retains the inductive estimate.
Each changed member therefore satisfies (13); each unreplaced member retains it.
Any interrupted prefix, including the extra retained raise before an omitted integral, has the same property.
A later attempt is covered afresh by the same argument, without adding any loss.
When localisation occurs, the old pocket dies and its assertion ends.
A new second-class output starts a new induction at its own birth level.
These cases exhaust the transitions. This proves (13). \(\square\)

Equations (15)–(16) supply the missing all-label use of the source's upper preparation.
They also explain why the narrow gaps between adjacent upper strata are harmless here.
The distance is measured from the retained old box inside \(H_*\), not between consecutive stratum boundaries.
I 63953–63959 suggests the same lower/upper split for its related core estimate.
The all-move persistence argument above is the additional step beyond `live-fgi.md`.

Now port I 63919–63924's implication.
A probe \(Q\) of level \(n\) has an anchor cell \(\Delta_n\subset\Omega_n\) and satisfies
\[
 \Delta_n\subset Q\subset
 \{x:\operatorname{dist}_n(x,\Delta_n)\le2\},
 \qquad \operatorname{side}_n(Q)\le5.
 \tag{17}
\]
This is the definition at I 62779–62788.
If \(n>m\), (13) gives \(\operatorname{dist}_n(S,\Delta_n)\ge3>2\).
No point of \(S\) belongs to \(Q\).
Therefore every probe meeting \(Y^\sharp\) has level at most \(m\), which proves (i1).

## 7. How many strips a probe meets: clause (i2)

This is Sussman–Alpoge's vertex argument, I 63926–63933, already recorded in `live-fgi.md`, section 2.
The new input is (i1), proved above for the present histories.

Let \(Q\) have level \(n\), and let it meet a live strip born at \(m\).
By (i1), \(n\le m\).
Its side in birth units is at most \(5L^{n-m}\le5\).
Every side of the birth component, and hence of its strip, is at least \(R_m\ge38\).
This lower bound comes from the boxed birth geometry, I 63547–63562 and 63650–63661.
It does not follow from clause (a)'s upper bound.

For completeness, consider one coordinate of an intersecting axis-parallel strip and probe in their local chart.
The strip interval is longer than the probe interval.
If it contained neither endpoint of the probe interval, intersection would force it strictly inside that interval.
That would contradict the length inequality.
Choose one contained endpoint in each coordinate.
Their product is a vertex of \(Q\) contained in the strip.
Admissible nonwrapping charts identify these vertices with the vertices of the original probe on the torus.

Distinct live strips are disjoint closed sets by the prior clause (b).
They cannot contain the same vertex of \(Q\).
Since \(Q\) has \(2^d\) vertices, it meets at most \(2^d\) live strips.
This proves (i2), including strips from different birth levels.
Only \(5<38\) is used; the source's unnecessary intermediate inequality \(5/L\le1\) is not used.

## 8. Result and full clause table

**Outcome (a): all four requested clauses are proved for the stated no-joining histories and published preparation.**
Together with `geoh-live-ab.md`, this supplies every geometric clause (a)–(i2) in I 85575–85644.
The result concerns finite histories of the specified geometric transitions.
It does not assert Wilson-field support for arbitrarily chosen test outcomes or identify a different revised operation with these rules.
The contour and counting hypotheses beginning after I 85644 remain outside this task.
The new argument and the ports here have not yet received an independent model check.

| Clause | Conclusion under the outlines' rule | Proof or credited input |
|---|---|---|
| (a), \(i\ge m\) | \(s_i(Y)\le(101R_m-1)L^{-(i-m)}\le101R_i\) | Prior `geoh-live-ab.md`, equation (3); unchanged on this subclass. |
| (b) | Meeting cells have level at most \(m\) and lie in the strip; strips are disjoint; cell ownership is unique. | Prior section 5; retained by section 2 here. |
| (c) | Birth collar \(5R_m/2\), its cell ceiling, and containment in the own component at every \(i>m\). | Prior sections 3–5. The narrow \(h=m\) case is absent here. |
| (d) | At T, \(\operatorname{dist}_i(Y^\sharp,\Omega_{i+1})\ge7R_i\). | Prior T-buffer proof; section 2 here. |
| (e) | An untreated strip lies in its component and has distance at least \(R_k\) from the running treated region. | Prior sections 5–6; section 2 here. |
| (f) | \(\widetilde\Lambda_C\) is a box; sides \(\le90\le112\) at level \(k\); distance from \(Z^c\) at least \(9R_k\). | Section 4, porting N 63749–63834 and I 63788–63857 with single predecessors. |
| (g): level and core | \(m<h\), hence \(m\le h\); the core is a box of current cells of levels at most \(h\); sides \(\le104LR_{h+1}\). | Sections 2 and 5; I 63861–63892. |
| (g): containment and margin | \(Y^\sharp\subset\mathsf C_C\); \(\operatorname{dist}_h(Y^\sharp,\mathsf C_C^c)\ge R_h\ge(R_h+1)/2\). | Equation (12); the source's \(m<h\) branch, I 63898–63900. |
| (g): touching cubes | Every native cube of level at most \(k\) touching the strip lies in \(\Lambda_C\). | Section 5; I 63905–63906. |
| (h) | Treated P-collar distance \(5R_{h+1}/2\); untreated distance \(R_k\); no P integration bond meets a live strip. | Prior sections 5–6, including its actual coordinate and bond checks. |
| (i1) | A probe meeting the strip has level at most \(m\). | Section 6: persistent separation \(\operatorname{dist}_n(Y^\sharp,\Omega_n)\ge3\) in the probe's own units for every \(n>m\); I 63919–63924's implication. |
| (i2) | A probe meets at most \(2^d\) live strips. | Section 7: I 63926–63933's vertex argument, now supplied with (i1) and the prior disjointness. |

**First open input:** none for these four clauses under the stated geometric construction.
GEOH-O1 remains the separately owned match to a different revised operation; this result does not close that interface.
