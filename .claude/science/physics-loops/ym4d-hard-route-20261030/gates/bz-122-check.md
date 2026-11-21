# Check of library/bz-122.md

Checked line by line by Claude (Opus 5.5), one reading. Not an audit.
Branch claude/ym4d-hard-route at a4fd42831.
Sources read: 122a PDF pp. 180 and 188 (rendered from balaban_cmp122_175.pdf), 122a text 110-300, 480-535;
122b text 352-362, 774-790, 968-1236 (anchors only); 99b text 286-330;
I 92510-92540, 131566-131569, 131724-131751, 137563-137572, 49503-49510.
CMP 119 itself was not read (not on this machine); its (2.14) display is taken from I 92525-92530.

## Verdict: ADVANCE

The counterexample (8)-(9) is right. It is a fact about sets and needs only one input:
the outer region of the localized problem is X_a. Item 10 and Balaban both fix that.
The note correctly limits the result to the proposed BZ-CUT interface.
Findings 5, 7 and 10 ask for small wording repairs. Finding 11 suggests a sharper open input. None blocks.

## Findings

### (1) Balaban's localization

1. **(1.19) and (1.20).** Note 52-72; 122a p. 180 (PDF). CONFIRMED.
   Printed: "the set B_k ∩ (Ω_k ∪ Z^c) is replaced by B_k(Z) ∩ Ω_k. Thus, according to the definition (2.14) [III], ... B_k^{(n)}(Z) = B_k^{(n)} ∪ B_k(Z)."
   (1.20) uses M'(Q_k^{s*}V_k) on Z∩Ω_k and V on Z∩Ω_k^c. The note's domains match. The first domain is Z∩Ω_k, not Z^c∩Ω_k.
   Page 180 also says each Γ_j means its intersection with Z. So B_k^{(n)}(Z) lives inside Z.
2. **Wrong-paper citation.** Note 58-62; I 131725; 122b text 360, 790; 122a/122b bibliographies. CONFIRMED.
   122b p. 361 and p. 370 say "joining ... is given by (2.14) [III]". [III] is CMP 119, 243-285. No (2.14) of 122b's own appears.
3. **CMP 119 (2.14) display.** Note 118-127; I 92525-92530. CONFIRMED via the account's quotation.
   "B ∪ B_j(Ω) = (B ∩ Ω^{~-2}) ∪ (B_j(Ω) ∩ (Ω \ Ω^{~-2}))". So (4) is the right instance. The collar uses the minimal tower, whose D_0 = X.
4. **Item-10 layer is the p. 188 layer.** Note 74-80; 122a p. 188 (PDF). CONFIRMED.
   (1.55) excludes the failed components. (1.56) relocalizes. (1.58) names H_Z^{(j)}.
   Printed: H_Z^{(j)} "is an analytic function of the configuration U_k^{(n+1)} restricted to Z". I 131740 identifies H_σ at σ≡1 with this function.
5. **"Internal" layer.** Note 77; 122a p. 188. MISMATCH (wording only).
   Balaban says "a support in the boundary layer of the width 2M_1 at the boundary of Z". He does not say "internal".
   Inside Z is the right reading, since the two backgrounds differ only on X\C. Say "inferred" or quote him.
6. **Grade k at the outer band; single-stratum proviso.** Note 128-135. UNCLEAR.
   This rests on CMP 119 p. 256, not read here. I 92523 confirms only that (2.14) needs ∂Ω in the top stratum.
   Not load-bearing for (9); see finding 9. It matters only for (5).
7. **"Exterior part".** Note 65-66. MISMATCH (wording only).
   B_k ∩ (Ω_k ∪ Z^c) is the good-region-plus-outside part, not an exterior part. Use Balaban's set name.
8. **Tower algebra (5)-(7).** Note 137-175. CONFIRMED.
   With P_0 the whole lattice, T_m^c = P_m^c ∪ D_m^c gives (6). (7) follows from D_1 alone.
   M_1 L η > 2L(r_N+2)η iff M_1 > 2(r_N+2). Correct.

### (2) The counterexample (8)

9. **b_+ is read and lies outside X_a.** Note 195-231; c0-sup.md 64-90 (1) and Prop. 3.1; pi-admit.md 459-485. CONFIRMED.
   F(X) holds all fine bonds with an endpoint in X. b has both endpoints in X, so b ∈ F(X).
   p contains b, so ∂p ⊂ R_X, and b_+ ∈ ∂p. Neither endpoint of b_+ is in X.
   The outer region is X_a: finding 1 puts B_k^{(n)}(Z) inside Z, and I 131731 gives the ambient continuation only "on Z_W = X_a".
   PI field bonds are fine bonds at every grade (c0-sup.md 86-88: level-zero rows are identities; positive rows are constraints).
   So (9) holds even without finding 6. It is independent of grade, field, radii and inner gaps, as the note says (228-229).
   The rectangular-component citation (122a pp. 177, 179) is CONFIRMED in the text. Any face with two coplanar boundary sites would do.

### (3) Does item 10 use the whole-action convention?

10. **Item 10 is native, not whole-action.** Note 186-193, 300-318, 348; I 131568, 131725-131751, 137565-137571. CONFIRMED.
    I 131568: "The following statements are used as inputs." Item 10 asks for the layer theorem "at the determining set B_Z localised to Z", holomorphy on D_H(Y), and the ambient condition on X_a.
    It never names the whole-action Hessian or protruding plaquettes. I 137566-137567: the set "lies outside the geometry" of the stage spaces.
    So the failure is only of the proposed BZ-CUT interface. The note says exactly this.
    Wording repair: the summary's page cite "pp. 177, 179" fits the component geometry; (1.19)-(1.20) are on p. 180, as note 50 says.

### (4) The open input and a native Dirichlet route

11. **Open input.** Note 351-358. CONFIRMED as stated; could be sharper.
    It is exact: an operator/domain representation of H_σ on its original domain, by a native boundary theorem or an exact change of representation.
    Two sharpenings, both from sources:
    (a) 122a p. 184 (text 494) derives H from "(106)-(108), (159)-(163) in [12]". 122b text 968 cites "(106) [12]" again. That formula is the native operator to port. The note does not name it.
    (b) 99b (text 286-330): Balaban uses only Dirichlet operators Δ|_{Ω_0} = Ω_0 Δ Ω_0, with Ω_0 a chosen union of big blocks containing Ω_1. He says they "depend on the configuration U restricted to Ω_0".
    For a 1-form Hessian, compression to bonds in Ω_0 still keeps plaquettes through those bonds. So Dirichlet compression alone is the whole-action convention and still reads b_+.
    The 99b route works only with Ω_0 chosen one spacing inside X (or one block layer). That changes the variable set.
    pi-admit.md (18) shows trimming gives a Schur complement, not D_II. So this is the "exact change of representation" branch, not a free native theorem.
    It is still the natural route: Balaban states the Ω_0-only dependence and leaves Ω_0 free.
12. **Section 4 table.** Note 245-284. UNCLEAR (spot-checked).
    122b (1.22) at p. 361 and (1.52) at p. 370 are where the note says. (1.61)-(1.72) anchors exist. The p. 376 claim Y'_2=Y'_3=Y'_4=∅ was not read.
    None of these rows is load-bearing for (9).

## Not checked

CMP 119 pp. 256-257 directly. 122b pp. 373-379 in full. SA 10287 and 10505. The identity of reference [12].
