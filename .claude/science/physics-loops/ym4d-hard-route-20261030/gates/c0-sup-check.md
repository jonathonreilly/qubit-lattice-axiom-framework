# Check: library/c0-sup.md (C0-SUP second round, stop (c) at C0-ETA)

Checked line by line by Claude (Opus 5.5), 2026-11-08. One reading. Not an audit.
Clone `04e7c612f`. Note: `library/c0-sup.md` (577 lines, Codex gpt-6-astra).
Sources read in bounded ranges: I (`theorem_0_complete_account_raw_I.tex`), SA (`YM4_sketch_500.tex`),
N (`YM4_1400.tex`), and the repo files `pi-admit.md`, `pi-admit-check.md`, `out-pi.md`.
Original Balaban papers were not opened. CMP 122b (2.14) is not on this machine.

## Verdict: ADVANCE

Every step that the note marks as proved here is correct.
The citations I read say what the note says they say.
C0-ETA is a sufficient reduced form of C0-SUP. It is not an exact or minimal form (finding 6).
Stop (c) is honest. No counterexample is claimed.
I found no statement in I near 131725 or 137566 that supplies C0-ETA at `B_Z`.
Findings 4, 6, 9, 11, 13 and 15 ask for wording or scope repairs. Finding 15 is the most important one.
None of them changes a proved result.

## Findings

### Section 3: what PI reads

1. **Prop 3.1, plaquette reach.** Note 82-84; out-pi 100-104. CONFIRMED.
   A plaquette through a field bond has a vertex in `X`. Its other vertices differ from that vertex
   by at most `eta` in each coordinate. This holds whichever endpoint of the bond lies in `X`.
   So every plaquette bond has both endpoints in `X_eta`.
   This is sharper than out-pi's `2 eta` domain `Omega_0^+`. It agrees with pi-admit-check finding 13.

2. **Prop 3.1, other coefficients.** Note 86-92; out-pi 96-104, 161-199, 683-685. CONFIRMED.
   `D_U` reads its field bond. Level-zero rows are identities. Rows of level `j >= 1` read only bonds
   inside `Omega_0` (out-pi 104). `A_s`, `P`, `R`, `Delta_a`, `G_0`, `q_0` are built from these.

3. **Prop 3.1, local models.** Note 94-100; out-pi 817-834. CONFIRMED.
   The model sets are `Omega_n^tau = Omega_n cap K_n`. So model field bonds are actual field bonds.
   Model plaquettes lie in `P(X)`. The model read lies in `N(x_tau)`, or in `N(z_tau)` for an exterior tile.

4. **Notation clash.** Note 94. MISMATCH (wording only).
   The note writes `X_tau` for the model's outer region `X cap K_0`.
   out-pi 829 uses `X_tau` for the model's read set. Repair: rename the outer region, for example `X^tau_0`.

5. **Lemma 3.2.** Note 110-126; out-pi 205-217. CONFIRMED.
   First differences: both components nonzero means both bonds are field bonds.
   Their endpoints lie in `X_eta`, so the transport link does too. One nonzero component has a
   transport-free norm. Second scalar differences: a path with a nonzero end value ends in `X`.
   Its middle site lies in `X_eta`. So an uncarried link can only be its first link, with initial site
   outside `X_eta`. Then only the two-step value can be nonzero. For distinct directions that value
   is also zero (sup-distance). For a repeated direction it is one transported value. Its norm is
   transport-free. The phrase "contributing path" (119) is needed. With it, the sentence is right.

### Section 4: C0-ETA and its sufficiency

6. **Is C0-ETA exactly what PI needs?** Note 142-159. CONFIRMED as sufficient. Not exact.
   It keeps what (5)-(6a) show PI needs: control on non-field links of the first collar.
   It drops the second collar. Section 3 proves PI never reads it.
   It asks more than PI needs in three ways:
   (a) value bounds at a quarter of the ceilings (2), to pay for the zero filling;
   (b) value bounds only, with differences derived by the triangle inequality;
   (c) one **parameter-independent** gauge `u` (145). PI needs a gauge per real reference only.
   The inverse is fixed by its coefficients (note 191; out-pi 909-910). Holomorphy comes from Cramer's rule.
   I 119605-119606 says no stage changes the unitary part. So (c) costs nothing if `U_r` is fixed.
   Repair: say "for each real reference" or explain why (c) is needed. The note already disclaims minimality (157-159).

7. **(4) and the filled model.** Note 165-186; out-pi 856-881. CONFIRMED.
   `eta^2|grad A| = eta|A(b') - A(b)| <= 2 eps_r` is the flat difference. The twist difference uses unitary
   transport. With `a_0 = a_0^*/2` and `a_1 = a_1^*/2`, Lemma 5.2 gives (5.4) on the filled model.
   The filled values agree with the actual ones on `X_eta`. Prop 3.1 and Lemma 3.2 then give the same
   coefficients and norms. Strictness of the twist bound is kept.

8. **Prop 4.1, rest.** Note 188-203. CONFIRMED.
   No gluing is needed: each model inverse is fixed by its coefficients. Interior models are untouched.
   The proof never shrinks a domain.

### Section 5: route 1

9. **(5).** Note 213-237; out-pi 189-199. CONFIRMED.
   With `Omega_1` empty, `Q = I` and `Q' = I`. Then `P = G'(G'^2)^{-1}G' = I`, so `R = 0`.
   So `Delta_a = Delta(U) + eta^{-2} I` and `q_0 = Delta_a`.

10. **(6).** Note 240-255; out-pi 734-744. CONFIRMED.
    The plaquette `0, eta e_1, eta e_1 + eta e_2, eta e_2` contains `b` and `b_+`. It is the only one of the six
    plaquettes of `b` that does. The holonomy is `exp(i(theta - eta t alpha)H)`. The second derivative is
    `eta^2 alpha^2 cos theta`. With PI's normalization this gives (6). The field is admitted for small `theta`.

11. **(6a).** Note 258-282; out-pi 1191-1209 (Prop 3.3 method). CONFIRMED.
    Each of the six plaquettes of the normal bond `(0, eta e_1)` holds exactly one changed tangential link.
    At `theta = pi` each holonomy is `-I`. With `R = 0` the form is `(-6+1) eta^{-2} ||v||^2`.
    The continuity argument is the one of out-pi Prop 3.3.
    This is new: out-pi Prop 3.3 changes the crossing field bond. Here all field links stay at one.
    Wording repair (284): the second collar is shown expendable in sections 3-4, not by this route.

### Section 6: route 2

12. **(7).** Note 297-310; I 50153-50229. CONFIRMED.
    I 50224-50226 prints `Omega_t^c = Q'^{~2} cup P'^{~4} cup Yhat^{~8}` for `2 <= t <= K`.
    `Y = Z_k = Lambda_k^c` (I 50163-50166). The cell side is `W_t = L M check R_t` in step-`k` units (I 50153-50155).
    The hull definition is at I 50168-50171.

13. **Lemma 6.1.** Note 315-331. CONFIRMED as geometry. UNCLEAR in use.
    Cells of `Omega_t` are at distance at least 9, 5, 3 from `H_Y`, `P'`, `Q'`. A cell of `X_t` holding `x`
    is one step away. `q eta < W_t` makes every cell meeting `Q_x` touch it. So (8) holds.
    `Y subset H_Y` gives `Q_x subset Lambda_k`. The test-domain remarks (338-344) are also right.
    UNCLEAR: the note does not cite that `X_t = Omega_t^{~1}` is the outer region of an actual ordinary-step PI entry.
    For `t = 1` pi-admit used N 61992 (`Omega_0 = Omega_1^~`). For `t >= 2` no source is given.
    Repair: cite the ordinary-step outer region, or call `X_t` a model set.

14. **(9) and the ports.** Note 348-373; I 49495-49515, 119598-119650. CONFIRMED.
    (9) is a rescaling with out-pi's convention `U_r^u = e^{i eta A}`, weight `s`.
    Repair (small): state that convention. A parent certificate in its own lattice units gives no factor `eta/s`.
    I 49507-49508: "The gauges are taken on the sets Q cap Omega_0". So nothing is supplied beyond that trace.
    I 119605-119606: no stage changes the unitary part. I 119632-119650: the input pair is kept outside the
    cutoff support, and holomorphy is along "the pair's own continuation".

15. **Section 6.3 and B_Z's geometry.** Note 377-421; I 131568, 131633, 131668, 131725-131746, 137565-137571. CONFIRMED, with one scope gap.
    I 131568 opens the list with "The following statements are used as inputs". Item 10 (I 131725) is in that list.
    So the localized layer at `B_Z` is an assumed input.
    The lemma at I 131633 is headed "Stated; proof incomplete at the step marked (∗)".
    Its (∗) is the division by `C_H^sharp` at I 131668. It is not about `B_Z`. The note says this (391-395). Correct.
    The account does not use the words "geometry incomplete". Its exact words are:
    I 137566-137567: "That set lies outside the geometry in which the spaces of pairs of the inputs of
    Lemma [T-step layer] are defined."
    I 137569-137570: supplied "by the part of Lemma [T-step layer] on the localised layer function (proof incomplete)".
    Citation repair: the note's range 137565-137569 (384) should be 137565-137571. Add I 131568.
    `B_Z` occurs only at I 131725, 137565 and 137583. None of them states where `Omega_0(B_Z)` sits.
    Scope gap (UNCLEAR): C0-ETA and Prop 4.1 assume PI's tower class (T) at `Omega_0(B_Z)`, with the bare first gap.
    The account quotes Balaban's localization display from CMP 119 (2.14) at I 92525-92530.
    There the collar `Omega minus Omega^{~-2}` carries level-`j` blocks, with `partial Omega` in the stratum of level `j`.
    If CMP 122b (2.14) builds `B_Z` the same way with `j >= 1`, the boundary of `B_Z` is not bare.
    Then (T) fails at `partial Omega_0(B_Z)`, crossing patches are not bare, and Prop 4.1 does not apply.
    Repair: add "(T) holds at `Omega_0(B_Z)` with a bare first gap" to the first open input, or check CMP 122b (2.14).

16. **Nesting example.** Note 397-402. CONFIRMED. It tests an inference, as the note says.

### Section 7: route 3

17. **(10)-(13).** Note 435-477; SA 7943-8000. CONFIRMED.
    The blocks are centred with `L` odd. So each block holds one full period of `x_1`.
    All transports lie in `{exp(isH)}`. Translation by `L e_mu` maps each contour family to its translate,
    and the field is invariant under it. So the two lateral means cancel. `Z_x = exp(i theta (f(x_1) - f(y_1)) H)`.
    The block sum of `f` is zero, so `M(U)(c) = I`. The other directions give `I` too. Phases stay below `2 theta`.

18. **(14)-(16).** Note 479-513. CONFIRMED.
    The plaquette at `x_1 = 0` has holonomy `exp(-2i theta H/L)`, norm defect `2 sin(theta/L)`.
    Gauge covariance, unitary telescoping and `|e^{itH_0} - I| <= |t||H_0|` give (15).
    (16): `eta sup|a_z| = |z|/L`, difference `2|z|/L`, coarse perturbation identically zero.
    The plaquette crosses `partial X`, so it is a real PI read. This differs from pi-admit (14)-(15), which used an unread bond.

19. **Ports in route 3.** Note 520-530; SA 7357-7370, N 35276-35292. CONFIRMED.
    SA's Lemma 1a.1.9 has separate `C varpi` and `2 delta` terms. N's regularity supremum is "over inner plaquettes".

### Distinctness and closure

20. **Routes distinct from pi-admit 5-7 and from each other.** Note 543-549. CONFIRMED, with one caveat.
    Route 1 deletes exterior reads. Route 3 inverts the coarse average. Both are new and fail where stated.
    Route 2 is new in method: the cell count for `t >= 2` and the parent transfer (9).
    Caveat: it stops at the same place as pi-admit 5.2 and 6. No named parent cube and no same pair at `B_Z`.
    It adds no new obstruction at `B_Z`.

21. **Is there a route that closes C0-ETA at B_Z?** UNCLEAR. Not closed by anything I found in I.
    Choosing the localized set so that Lemma 6.1 applies is not open to us. `Z` comes from Balaban's R-operation.
    Lemma 6.1 is about `Omega_t^{~1}`, not `Omega_0(B_Z)`.
    The closest route uses item 10's own strata list (I 131732-131737): cubes on `X_a cap Omega_1`,
    index-zero members at raw points, and `(3.35)_0` on `Y'`.
    By I 134749-134755 the index-zero members include bare `(3.35)` gauges on cubes of side at most `2 M L eta`.
    Then (9), with the hull gauges of I 49120-49234 when a patch spans two cubes, would give (3). It needs three facts I does not state:
    (a) the `eta`-collar of `Omega_0(B_Z)` lies in `X_a = Omega_0(B°)`, where the `K_109` pairs live;
    (b) the pair at `B_Z` is the same pair as the `K_109(B°)` member on those reads;
    (c) finding 15's tower question.
    Balaban's (2.14) provisos would give (a) if checked for `B_Z`: `partial Omega` lies in one parent stratum, at distance at least `2M` from the others.
    I 94755-94812 checks them only for the sets `B^0` and `B^C`.
    This is a fourth route worth one lane. It is a geometric check of `B_Z`, not new analysis.

22. **Scope and honesty.** Note 551-558, 560-577. CONFIRMED.
    No counterexample is claimed. Constants are fixed before thresholds. No computer-assisted step is used.

## Not checked

SA 10262, 17369-17447; N 35634-35704, 35771-35822; I 49120-49234, 52362-52420, 52620-52647,
12725-12728 (read only 12720-12729), 16321-16380 (read only 16321-16330), 134756-134826.
The table rows citing these were checked in pi-admit-check or are inputs, not proofs, of this note.
