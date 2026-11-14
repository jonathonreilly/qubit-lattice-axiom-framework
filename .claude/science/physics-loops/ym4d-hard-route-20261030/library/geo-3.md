# geo-3: formation compatibility and the remaining geometric premises
Provenance: Codex (GPT-6; effort: xhigh), checkout `bea4a1b6f8b755f8941f3e08e913938988e20e96`; Sussman–Alpoge commit `31a47c543775`; research text, not an audit, grants no status.

**Result: REFUTED as stated.** The bounded face rule is geometrically compatible, but EXT incorrectly equates the prepared and healed domains. Section 3 gives the explicit configuration; §§4–5 prove the narrower replacement and its variational restriction step.

## 1. Target, adopted definitions and credit

This is queue row 121. It tests the geometric inputs to the A3/Proposition 2.8 route: formation compatibility of the upper face-movement rule, then GEO1, GEO2, GEO4, GEO6, EXT and the W3 nest gap in `sa-2.8-terms.md` §3 and Lemma W and `../gates/a3-close-meet-gate.md` §B. A failure changes which geometric inputs the analytic implications may consume; it is not a claim about Yang–Mills existence.

Adopt the half-cell profile of `geo-prop23.md` (5.1), Definition A of `assign-adopt.md` with the repairs in `../gates/a2-full-gate.md`, and, subject to the requested compatibility test, outward face increments at most `K m_i`, where `m_i=M L^{i-k}` and K is fixed before the coupling scale R. The profile lemma of row 118 and the conditional size/count estimates (6.1)–(6.2) of `geo-2.md` are cited, not reproved. Both files were read in full, in bounded ranges.

Credit: the source formation, class, regions, nests, preparation and healing are from Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text. “SA” refers to line numbers of their `YM4_sketch_500.tex` at the revision above, fetched once to `/tmp/sa_ym4.tex`. The literature search is reused from `lit-large-field.md` §0; the targeted source is the pinned outline. No external analytic theorem or computer calculation discharges a step here. All assertions below concern the geometric formation data, with the same scope as rows 118–119.

## 2. Formation compatibility: a uniformly bounded nest exists

**Claim (geometric compatibility, PROVED).** The class's lower gaps, alignment, quarantine and containment do not force an unbounded face movement. One may use `K=L+1`, independently of R, for every eligible component. This is an existence assertion for the supplied stage geometry, not a claim about the exactness of a new integration kernel.

Fix an odd `L>=27`, as allowed by the construction's size floors. Write `a=k-R`, `R_i=Rcheck_i`, `s_i=R_i m_i`, `C=X∩Z_a`, and `B_i=X∩Z_i`. The fixed small-component cutoff in SA 17575 is denoted `b_box`: each coordinate side of C is at most `b_box s_a`. Boxing makes C a box. Choose the coupling floor so `R>=L`; then every `R_i` in the window is a power of L at least L. Quietness and absence of joining give, literally (SA 17575–17583),

\[
 H_i=\operatorname{hull}_i(B_{i-1}),\qquad
 A_i:=X\cap\Omega_i^c=H_i^{[8]},\qquad
 B_i=H_i^{[10]}\quad(a<i\le k).
 \tag{2.1}
\]

The superscript adds cells of side `s_i` to each face. These equalities, rather than a presumed location near the centre of a coarse cell, supply the room.

Use the alternating rounding construction of `geo-prop23.md` (3.3), now separately on each of the four coordinate intervals of the arbitrary box C. Here are the details needed for this generalisation. Let `F_i=m_i(Z+1/2)` be the face grid and `D_a=C`. Initially both faces lie in `F_(a+1)` because `R_a/L` is an odd integer. At step i, the designated face is an old face in `F_i`; move it outward by exactly `m_i`. Round the opposite face outward to the first point of `F_(i+1)` at distance at least `m_i` from its old position, and designate that face next. At the last step k use `F_k`, instead of `F_(k+1)`, for this opposite rounding: no subsequent step needs the coarser grid. Lower faces are rounded downward and upper faces upward.

Since `F_(i+1)⊂F_i`, every new face is in `F_i`, and the next designated face is in the required next grid. Rounding to a grid of spacing `Lm_i` costs less than that spacing. Thus every face increment is in `[m_i,(L+1)m_i)`, with one face in each coordinate moving exactly `m_i`; the final opposite increment is less than `2m_k`. Consequently

\[
 D_{i-1}\subset D_i,\qquad
 d_\infty(D_{i-1},D_i^c)=m_i,
 \qquad D_i\subset D_{i-1}+[-Km_i,Km_i]^4,
 \quad K=L+1.
 \tag{2.2}
\]

Distances in (2.2) are between geometric carriers. Passing to the corresponding site sets preserves the lower bound. These are aligned M-cube boxes, with the asserted one-later-M-cube gap, even with equality in the carrier convention. Also `D_(i-1)` plus one level-(i-1) M-layer lies in `D_i`, because `m_i=Lm_(i-1)>m_(i-1)`.

Inductively `D_(i-1)⊂B_(i-1)⊂H_i`. Since `K=L+1<=8L<=8R_i`, (2.2) gives

\[
 D_i\subset H_i+[-8s_i,8s_i]^4=A_i\subset B_i.
 \tag{2.3}
\]

This proves containment without any bound on how far a coarse hull's centre shifts. It is the reason alignment cannot force a large jump. At an interrupted stage i<k the next unchanged hole contains `H_(i+1)^[8]`, whereas `D_i⊂B_i⊂H_(i+1)`; hence the junction clearance is at least `8s_(i+1)>m_(i+1)`. Stopping after any initial segment therefore introduces no deficient junction gap.

There is also no new gap failure across the boundary of X. The final step puts two level-k cell layers around every component of `Omega_k^c` before boxing (SA 17319–17325). The connected two-layer neighbourhood of a point of `Omega_k^c` therefore belongs to the same component of `Z_k` as that point. A surviving old hole outside X, at any earlier level, is contained in `Omega_k^c` by nesting and consequently is at distance at least `2s_k` from X. Conversely `D_j⊂D_k⊂Omega_k^c∩X` has that clearance from `X^c`. Thus new small-field points in X stay away from old holes outside X, and new small-field points in another operated component stay away from the retained holes in X. The only remaining pairs lie in unchanged regions, where the incoming gaps are preserved. The clearance `2s_k` exceeds every required `m_i`, since `m_i<=m_k` and `R>=L`. This checks the cross-component gaps, not merely the gaps between the displayed boxes.

For completeness the final box remains of size O(M), uniformly in the window. This also checks that an extremely large earlier cell size cannot defeat the construction. Let `bar B` be the fixed upper frame slope of SA 19487, let `r>=2` be its fixed logarithmic exponent, put `y_i=min_(u<=i) x_u`, and take an integer `n>r`. For

\[
 t=\log y_k\ge t_0:=\max\{1,(\bar B L n!)^{1/(n-r)}\},
 \qquad D_R:=L2^r,
 \tag{2.4}
\]

one has `R<=L t^r` and `bar B R<=exp(t)`: use the single term `exp(t)>=t^n/n!`. If a minimum defining `y_k` occurs before or at a, then `y_a=y_k`. Otherwise it occurs at some `v∈(a,k]`, and the frame bound gives `y_a<=x_a<=x_v+bar B(v-a)<=y_k+bar B R`. In both cases `y_a<=2y_k`, so `log y_a<=t+log 2<=2t`. Rounding to the next power of L now gives

\[
 R_a\le L(\log y_a)^r\le D_R R.
 \tag{2.5}
\]

Apply the already proved estimate `geo-2.md` (6.1), with its initial-size constant `B=b_box D_R`. Since `R L^{-R}<=1` for integer `R>=1` (induct on R using `R+1<=L R`), the final enlargement by one level-k M-layer has each side bounded by

\[
 \operatorname{side}(\Lambda)
 \le C_\Lambda M,\qquad
 C_\Lambda:=b_{\rm box}D_R+\frac{2KL}{L-1}+2.
 \tag{2.6}
\]

All these constants precede the coupling floor. The shell-count consequence is exactly `geo-2.md` (6.2), with this B and K, and is not rederived here.

**Multiple components, old merges, nests and the torus.** For simultaneous class components the construction stays inside their disjoint `A_i⊂X`, so one component never constrains a face of another. A merge at or before a changes only C and its interior history. A merge during `(a,k]` violates the explicit class condition and is not a case the operation must prepare. A mark of level `s<a` changes entries only at levels at most s; the construction leaves all entries through a unchanged and retains the entire core C. Thus it neither reopens an old nest nor moves an old face. Quarantine excludes operations at `[a,k)`, including a, so overlapping active preparation windows do not create additional face constraints. The original steps, future classes and quarantine decisions are unchanged: only the residual boxes inside the current eligible component have been specified. The same construction applies when a later operation eventually has this component in its older core.

SA 17583–17584 expressly imposes a torus floor giving non-wrapping lifts for class boxes and their neighbourhoods. The construction remains inside those boxes and uses grids only through level k; it is therefore available on every such torus, including a component crossing a chosen fundamental-domain seam. Changing its lift by a torus period changes every face by that period and commutes with the rounding. Other components and complements may wrap; they impose no additional face constraint on this local construction. Periodic distances, not a false global isometry of a lift, define the adopted localisation. This exhausts the proposed sources of forced large face movement. The bounded rule can be adopted as geometric data.

## 3. EXT is false: preparation and healing have different first domains

**REFUTED statement.** EXT in `sa-2.8-terms.md` §3 asserts, among other things, that `D_(pX)` and `D(L_X O^h)` have the **same domain**. In the adopted localisation their domains are their zeroth members. SA 5614–5628 defines rows with both endpoints in that member; SA 9592–9619 defines pillars as a partition of it and the variational problem as fields on it, with action summed over its inner plaquettes. Thus “domain” here has a specified mathematical meaning; it is not the ambient torus on which distances happen to be measured.

Use exactly the single-creation geometry proved in `geo-prop23.md` §3, with its ordinary bounded-increment nest, not the exceptional enlargement of row 119. To make the witness explicit, choose an odd `L>=27`, `mu=M_1'>=max(3,rho)`, `M>=L^3 mu`, and the other fixed floors stated there; use collar counts `n_col=5`, `n_sep=9`, so `(n_sep-n_col)mu=4mu>max(rho,3mu)`. Then choose a power `R=L^h`, `h>=2`, above the cited coupling floors, `a=1`, `k=R+1`, and the constant-R frame constructed there. Set `s_i=R M L^{i-k}` and let `E_i=[-s_i/2,s_i/2)^4` be the central cell. Take the same torus with side greater than `100MR`, enlarged if needed to accommodate its grids. There is a single creation at level 1, no earlier history, and no later failure or joining in the window. The geometric record is

\[
 \Omega_1^c=E_1^{[4]},\quad C=Z_1=E_1^{[6]},\qquad
 \Omega_i^c=E_i^{[8]},\quad Z_i=E_i^{[10]}\quad(2\le i\le k),
 \quad X=Z_k.
 \tag{3.1}
\]

Row 118 supplies the formation, quietness, quarantine, alignment, lower gaps and final-box checks for this record. Its ordinary nest has each face increment less than `(L+1)m_i`, so it obeys the newly adopted rule with `K=L+1`. The half-cell profile and repaired Definition A are in force. They do not change the first-domain computation below. This is a configuration of the geometric formation data; no assertion of positive weight for a complete analytic RG history is required or made.

The label starts with `Omega_0=Omega_1^~`, where the enlargement is by one layer of level-1 **cells**, as expressly specified at SA 17317. Define

\[
 J:=E_1^{[3]}=[-7s_1/2,7s_1/2)^4.
 \tag{3.2}
\]

Adding one cell layer to the exterior of the nine-cell-wide hole `E_1^[4]` removes its outer cell layer. Coordinate by coordinate, the remaining hole is exactly the seven-cell-wide box J. Hence

\[
 \Omega_0=\mathbb T\setminus J.
 \tag{3.3}
\]

This identity also holds for the aligned site sets with the source's fixed half-open convention. The origin is strictly inside J and is a bare site, so no boundary convention can remove the witness.

Preparation changes only the members with `a<i<=k`, here `2<=i<=k` (SA 17421–17437; `sa-2.8.md` §2). It leaves both `Omega_1` and `Omega_0` unchanged. Healing adds X to every member, including the first one. If the first member is instead recomputed from the healed `Omega_1`, it gives the same answer: in this one-component example `Omega_1∪X=T`. Thus

\[
 O_0^p=\mathbb T\setminus J,\qquad O_0^h=\mathbb T.
 \tag{3.4}
\]

Definition A has `T_0(X)=X` and localises by intersection at **every** level, including zero. Therefore its two localised domains are

\[
 \boxed{\quad (\mathcal L_X\mathcal O^p)_0=X\setminus J,
 \qquad (\mathcal L_X\mathcal O^h)_0=X.\quad}
 \tag{3.5}
\]

Their difference is nonempty: `0∈J⊂C⊂X`. More concretely, with bare spacing `eta=L^{-k}`, the elementary plaquette with corners `0, eta e_1, eta e_2, eta(e_1+e_2)` lies wholly in J, since `s_1=RML eta>eta`. It belongs to the healed localised action domain and not to the prepared localised action domain. This is an explicit missing plaquette, not merely a relabelling of rows.

The discrepancy is present before choosing any datum, background, profile, gauge or collar erosion at a positive level. Enlarging K, M, R or the torus cannot turn the two sets in (3.5) into equal sets. The core operation remaining unexpanded does not insert its missing sites into `O_0^p`; that would change the determining sequence and the variational problem. This refutes EXT, and hence the requested conjunction, even with all three adopted rules and even on a single quiet component. No configuration with complicated mergers or wrapping is needed for this failure.

## 4. The smaller geometric replacement, proved

Replace the domain clause of EXT by the following; keep the distinction between the two problems.

**EXT-out.** Put `J_X=X\O_0^p` and `Y=X\J_X`. The prepared localised domain is Y, the healed localised domain is X, and `J_X⊂C⊂D_k⊂Lambda`. Their members agree outside `D_k`. Their rows with **both endpoints outside Lambda**, their row functionals there, and their exterior/lifted data agree. No equality of the full domains is asserted.

**Proof for every eligible component.** For `j<=a`, a point in `X\C` belongs to `Lambda_a`, since `C=X∩Z_a` and `Z_a=Lambda_a^c`. The nested action sequence puts it in every earlier `Omega_j`. A retained partial preparation only enlarges these determining members relative to the action members; it does not delete this point. Thus it belongs to every `O_j^p` for `j<=a`. For `a<j<=k`, preparation gives `O_j^p∩X=X\D_j`, and the boxes satisfy `C⊂D_j⊂D_k`. Consequently, at every level including zero,

\[
 (O_j^h\setminus O_j^p)\cap X\subset D_k,
 \qquad J_X\subset C.
 \tag{4.1}
\]

Outside X the operation changes nothing. Healing fills X at all levels. Intersecting both sequences with the same tower `T_j(X)` preserves equality outside `D_k`. At level zero the tower is X itself, so the domains are exactly Y and X, proving the first assertion. This reasoning also covers older marks in C: their differing action/determining entries do not affect `X\C`.

The determining-row membership test uses only the endpoints' memberships in levels 0, j and `j+1` (SA 5614–5628). These memberships agree outside `D_k`, so a row with both endpoints outside Lambda is present in both problems or neither, at the same level. The source's geometric averaging row reads its double block (SA 9631), whose points are within `2xi_j<=2` of an endpoint. The added M-layer in Lambda separates an endpoint outside Lambda from `D_k` by at least `M-eta`; with `M>=4` and `eta<=1`, its double block misses `D_k`. The geometric row maps therefore read the same fields on the same sites. This also prevents a change of an interior row into an outward row there, since all local layer memberships agree.

Away from the outer localisation strip these are the unchanged level-k exterior rows: all nest boxes lie in `D_k`, and all older differences lie in C. In the localisation strip, both problems use the same tower and the same lift of the exterior `V_k`: identity on a bond internal to a level-k block and `V_k(c)` on a bond crossing its block boundary. The strip lies outside `D_k`. Indeed (2.1) and (2.3) give `d(D_k,X^c)>=2MR`, while the repaired Definition A puts the strip, including its carriers, at depth at most `3mu+3`; `M>=L^3mu`, `L>=27`, `R>=1` give `2MR>3mu+3`. Thus the strip never reads a changed shell or core datum. These two cases exhaust the common exterior rows and prove equality of their data. QED.

In the counterexample, `J_X=J` is precisely (3.2). EXT-out identifies the exact loss and proves that the exterior part of EXT survives. Filling J by convention would be a different repair, changing the original prepared problem; it is unnecessary for EXT-out.

## 5. What changes in the consumer: a restriction lemma, not a common domain

The first use broken by the literal EXT assertion is the phrase “on the common localised domain” in `sa-2.8-terms.md`, Lemma LM. Its healed action is `A_X`; the prepared problem uses `A_Y`. One cannot write `T(0)=S` as an equality of fields on identical sets in (3.5). The meaningful candidate is `T(0)=S|_Y`. The following smaller statement settles the variational part of that repair without assuming that deletion of plaquettes is harmless.

**Restriction lemma (PROVED implication).** Let the two domains and exterior rows satisfy EXT-out, with `M>=4`. Let the prepared sequence have first gap

\[
 d_\infty(Y^c,O_1^{pX})>\rho\eta,\qquad \rho\ge2.
 \tag{5.1}
\]

Give it S's own averages as datum. Suppose on X the reference field satisfies the multiplier identity

\[
 DA_X(S)=Dq_{\rm ext}(S)^{\mathsf T}\lambda_{\rm ext},
 \tag{5.2}
\]

where `q_ext` consists of the common rows with both endpoints outside Lambda. Then `S|_Y` is a constrained critical field for the prepared problem on Y. If the regular-orbit existence/uniqueness hypotheses used by LM admit this restriction, they identify `T(0)=S|_Y` modulo the prepared residual gauge. This lemma proves the variational implication, not those analytic hypotheses.

To prove it, take any differentiable curve `U(t)` on the prepared fibre through `S|_Y`. Extend it to all bare bonds of X by setting every bond not wholly in Y equal to its value in S; call the extended field `E U(t)`. Let p be a plaquette contained in X but not contained in Y. It has a corner z outside Y. Every corner of p has sup-distance at most eta from z. Thus every edge e of p whose endpoints are both in Y has both endpoints at distance at most eta from `Y^c`. By (5.1) neither endpoint belongs to `O_1^{pX}`. Such an edge is a level-zero determining row, by the exact row definition, and its prescribed datum is its value in S. Hence `U(t)(e)=S(e)`. The other edges of p equal S by the definition of the extension. This proves, for each missing plaquette separately, that its holonomy is constant along the extended curve. Summing the finite plaquette identities gives

\[
 A_X(EU(t))=A_Y(U(t))+
 \sum_{p\subset X,\ p\not\subset Y}a_p(S).
 \tag{5.3}
\]

No boundary Euler–Lagrange term has been discarded. EXT-out ensures that every exterior row has its full carrier in Y and is a prepared constraint. Consequently `q_ext(EU(t))=q_ext(S)`. Differentiate at zero, apply (5.2), and use (5.3):

\[
 \left.\frac{d}{dt}A_Y(U(t))\right|_{0}
 =DA_X(S)[(EU)'(0)]
 =\lambda_{\rm ext}\cdot
   \left.\frac{d}{dt}q_{\rm ext}(EU(t))\right|_{0}=0.
 \tag{5.4}
\]

This is constrained criticality for every such curve, proving the lemma. The last assertion is exactly uniqueness on the correctly stated domain Y.

Identity (5.2) is the part of LM's multiplier argument that is formulated entirely on the healed domain: independent variation of the box datum at its critical reference sets its box multipliers to zero. The repair above supplies the previously omitted domain-transfer step. In particular, it does not assert a counterexample to LM's intended restricted-field conclusion or to the analytic remainder estimate. It shows why the stronger geometric premise was false and gives a written replacement for this specific use. The new lemma's separated first gap is verified in the explicit witness: `O_0^p` is the exterior of the seven-cell box, `O_1^p` the exterior of the nine-cell box, so their gap is `s_1=RML eta>rho eta`; intersection with the second-rule tower contributes a gap at least `Lmu eta>rho eta`. This last assertion follows directly from the defining admission inequality for its first nonzero member and the complement-of-intersection identity.

## 6. Disposition

**REFUTED.** The conjunction requested in row 121 fails at EXT's equality-of-domains clause. The explicit configuration (3.1) has the uniformly bounded ordinary nest of row 118, satisfies the adopted profile and localisation rules, and has the distinct domains (3.5), witnessed by the specified bare plaquette. Section 2 proves that the upper face-movement rule itself can be supplied for every eligible component without conflict with the stated formation constraints. It need not be replaced. Section 4 proves the narrower geometric statement EXT-out, and §5 closes its variational domain-transfer lemma; the consumer must distinguish `S` from `S|_Y`.

Scope: this is a refutation of the geometric package as written, not an analytic counterexample, an audit verdict or scientific status. No universal closure of the remaining independent GEO1, GEO2, GEO4, GEO6 or W3 assertions is claimed. Their full treatment is not needed to decide this conjunction once EXT fails; analytic admission and uniqueness in the conditional restriction lemma retain their stated hypotheses. No numerical or computer-assisted step has been used.
