# Check: library/leaf-sc.md (SC-NATIVE)

Checked line by line by Claude (Opus 5.5), 2026-11-08. One reading.
Note at branch `claude/ym4d-hard-route` head `2faf203b2`.

**Verdict: ADVANCE.**

Both kill tests are run and come out as the note says. Every ported
estimate matches its source, with the same hypotheses. The native site
substitution and (9)-(16) check out. The consumer matches GW1 (2) and
PI's whole-action convention. The note claims nothing beyond its
restricted scope. Four small repairs are listed. None changes a result.

Sources read: Y = scratchpad `sa1400/YM4_1400.tex`. SA =
`/Users/jonreilly/ym4d-lead/sa/YM4_sketch_500.tex`. The note's `/tmp`
copies are gone. Every cited line range matched its content.
Library files read at the cited lines: out-pi, b98p5, walks-gw, gw1,
b99-w, print-inverse-r2, hstep-tree §4, a41-avg, gates/a41-avg-check.

## Findings

1. **Note 54-86, flat two-layer test; out-pi 619-643 (Lemma 4.5),
   539-541 (Lemma 4.4(iii)), 604-606; SA 7085-7090. CONFIRMED.**
   h_1 - h_2 = -((L-1)/2) L eta (1,1,1,1) is in the level-1 lattice.
   h_2 is not, since (L^2-1)/(2L) is not an integer. The flat
   straightened field rows of both schemes are the long straight mean.
   Both flat site rows are the block mean. Boundary-block and
   outward-row membership is preserved, as out-pi 636-641 says.
   The test is done by the general identity, not by a drawn instance.
   That is enough here.

2. **Note 88-169, seam test; SA 7065-7070, 7092-7095. CONFIRMED.**
   BCH gives log(XY), log(YX) as written. The Federbush mean of the two
   has log a+b+O(eps^3): the second-order term cancels. The quadrant
   weight is w=(r/L)^2. -(w/2)[a,b] = w i eps^2 sigma_3 is correct.
   With W_0=1, SA's node factor gives M(W)(c)=u(c_-), u(c_+)=1, so the
   straightened row is zero in both schemes.
   For (K): the bilinear term is (1/2)(avg[A,z]-[Abar,zbar]).
   The difference is -(1/4)w(1-w)[[a,b],i sigma_1] = -i w(1-w) eps^2 sigma_2.
   The terms with two linear A legs are common to both schemes.
   Minor: SA's comb has order 4,3,2,1 (SA 7065), not "(1,2)".
   The note's sign remark covers this. The test shows the equality of
   curved maps fails. The native route does not use that equality.

3. **Note 195-221; print-inverse-r2 403-412; Y 4007-4028;
   b98p5 394-436. CONFIRMED.** The prior remark names the five row
   properties of Lemma 4.4. Y lists the six axioms and the flat
   straightened identification. b98p5 §2.5 proves holomorphy,
   G^c covariance by anchoring, the arithmetic-mean derivative, and
   (10)-(16) for M_sym. b98p5 says M_sym is SA (PX141), the same map
   as SA 7069.

4. **Note 233-277, field rows and (1); b98p5 (9), (10), (12)-(15);
   SA PX142, PX146-PX149. CONFIRMED.** Row sum 1 and column sum n^{-4}
   follow from (9) after the factor eta/s. Sum t_i < 1/(L-1) is right.
   The flat errors are SA PX149's telescoped errors, in common frames.

5. **Note 279-287, native site substitution; SA 7108-7111; out-pi
   597-609; b98p5 (12)-(13), (17). CONFIRMED.** SA averages gauges
   with the same contours. Its linear part is avg Ad(T)lambda. A mean
   of paths with at most 4L edges has log at most twice the largest
   path log (b98p5 (17)). So each level costs C eps t_i. The weights
   are n^{-4}, one block per site. Repair (minor): say that the level-m
   transport is the mean at background M^m(U), and that b98p5 (12)-(13)
   bound its reference factors.

6. **Note 240, 289-295; b98p5 359-363; SA 11606-11610; out-pi 491.
   CONFIRMED.** At most 2d carriers per height, two heights, so 4d.
   Outward rows are included.

7. **Note 242-243, 297-303; SA PX151-PX153; b98p5 §2.4; gw1 (11).
   CONFIRMED.** sum_b' |D_b D_b' q_c| <= C_L s (eta/s)^4 is PX153.
   The raw density C_L s^{-3} is gw1 (11), also for the mean.

8. **Note 305-353; walks-gw 316-327, 399-439; gw1 (1);
   b98p5 677-688. CONFIRMED.** GW uses no derivative of an averaging
   density. (2) is the row commutator that walks-gw describes. The
   Holder gap is gw1 (1). The Holder bounds for h follow by
   interpolation. (3) is b98p5's identity. Minor: (3) itself is the
   fundamental theorem of calculus. Translation covariance is needed
   only to read it as a spatial difference, so h must be a coarse
   translation.

9. **Note 357-375, (4). CONFIRMED.** The identity is out-pi 632.
   h_j - h_k is in the level-j lattice for odd L. Nested centred
   subblocks match: h_j - h_{j-1} = r l_{j-1}(1,1,1,1).

10. **Note 377-401, (5); out-pi 688-735 (Lemma 5.1). MISMATCH (minor).**
    The chain is right. But the step needs s_c^{-2} <= C m_b^{-2}, that
    is m_b <= C s_c. The note cites s_c/m_b <= L, which is the other
    direction. out-pi gets the needed one from layers j-1, j (m <= l_j).
    Note line 241 also gives it. Repair: replace "s_c/m_b <= L" with
    "m_b <= s_c on the carrier (layers j-1, j)".

11. **Note 403-419, (6); walks-gw 320-324. CONFIRMED.** The bound
    matches. Wording: the factor eta^4 cancels the fine pairing volume
    (walks-gw), not "the row volume s^4". Repair: fix the phrase.

12. **Note 421-473, (7), (8); gw1 (9), (10), (12), §7-§8;
    walks-gw (P10). CONFIRMED.** (7) is gw1 (12) with the native
    density. The double-block carrier is the same, so (9)'s junction
    cost does not change. The constant order is GW's.

13. **Note 477-494, (9); out-pi 175-200; SA 10141-10146. CONFIRMED.**
    G', R, Delta_a are out-pi's. Lambda and Pi=I-D Lambda are SA's
    lambda_A and S.

14. **Note 496-503, intertwining. CONFIRMED.** I checked the linear
    step. Plain M is covariant with g at the coarse centres
    (SA 7069-7070). The node factor linearizes to
    alpha_bar + lambda(y) - (Q'lambda)(y). So QD lambda = -D'(Q' lambda),
    and it vanishes when Q'lambda=0 at both ends. SA PX93 also states
    Q S = Q. At an outward end, the level-j site value is the one-step
    mean of level-(j-1) site values, by the recursion. This needs site
    rows on all child blocks. Those blocks lie in the preceding region.

15. **Note 505-514, (10). CONFIRMED.** Q'G'R=0, R^T=R, R^2=R hold.
    R D^T Pi = 0 and Pi^2 = Pi follow from D^T D = G'^{-1} - Q'^T s^{-2} Q'.
    Q Pi = Q needs finding 14.

16. **Note 516-534, (11); SA 10163-10198. CONFIRMED.** (11) is SA's
    displayed form, character for character. It has no derivative of J.

17. **Note 535-551, (12)-(13); gw1 (2), (11); SA 10149-10159.
    CONFIRMED.** gw1 (2) defines K_J = Theta'_J + Pi^T Theta_J Pi with
    <A,Theta_J A> = 2<C^(2)(lA), H^{J,T}J>, and G_1^J = (Delta_a-K_J)^{-1}.
    (13) is that operator. The normalization matches SA's G_1 with
    H_SA = H s and (A,Delta^(2)[j]A) = 2(C^(2)(A), j).

18. **Note 553-561; b99-w 185-218; SA 10195-10198. CONFIRMED.**
    b99-w Lemma 3.1 uses only f_V(A_t)=f_V(A). The whole Wilson action
    with exterior links fixed is invariant under gauges supported on
    Omega_0 sites. D lambda lands in touching bonds, which are PI's
    variables. G' is Dirichlet on Omega_0^c, so lambda has that support.
    SA states the identity for the inner action and flags the
    whole-lattice boundary comparison. The note checks the hypothesis
    for S_var directly and does not identify the two Hessians.

19. **Note 563-579, (14); SA PX93-PX96; Y 23905-23915. CONFIRMED.**
    j_U = Q^T omega and SA's QH=1 give omega = s w, because the note's
    H is SA's H times s^{-1}. Y's warning on normalization is respected.
    (14) is PX95. Positivity at independent J is not claimed.

20. **Note 581-603, (15)-(16); SA PX97, PX99, PX100; Y 23838-23847.
    CONFIRMED.** Both endpoint derivatives are kept. The datum term
    goes away only under PX100. Y separates the physical Hessian from
    an independently named extension, as the note says.

21. **Note 605-640, scope and handoff; hstep-tree 300-322; gw1 §1;
    a41-avg 362-382. CONFIRMED.** The result is an implication on the
    admitted PI/GW class. It keeps the whole action, no-inward rows,
    complete reads and physical pairings. It does not claim fibre
    congruence or general A4. It makes SC-GAUGE unnecessary only for
    this consumer, as hstep-tree 321 allows. PI-ADMIT keeps its owner.
    Repair (minor): the admitted class is the translate of PI's
    corner-grid geometry (tiles, big blocks, regions). Add to the first
    open input that the caller's mean-scheme regions must be those
    translates, next to the action match.

22. **Y 16661-16865. CONFIRMED: no conflict.** This is the Route A
    comparison (mean = T(comb + E)). The note does not use it. Nothing
    in the note contradicts its warnings on real versus complex
    references or on outward rows.

## Repairs (minor; ADVANCE does not wait on them)

R1. Line 393: replace "s_c/m_b <= L" with "m_b <= s_c" (finding 10).
R2. Line 405: "cancels the fine pairing volume" (finding 11).
R3. Lines 279-284: name the level-m mean transport at M^m(U) and cite
    b98p5 (12)-(13) (finding 5).
R4. Line 639: add the translated region geometry to the caller match
    (finding 21).
