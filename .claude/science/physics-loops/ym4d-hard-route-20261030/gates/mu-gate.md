# MU gate: line-by-line check of library/mu.md (Lemma 4.13:lem-minimizer-unique)

First failing step: none

Text checked: `library/mu.md` (268 lines) against CA-I L45162-45201 (statement, Route, consumer sentence), the next lemma `4.13:lem-own-constant` (L45203; not used by mu, correctly), every content use of the nesting identity that I could find, CMP 109 OCR pp. 260, 262, 277-280, CMP 102b OCR pp. 278-281 and §G/Prop. 9 (pp. 305-307), and CMP 98 OCR Props. 4 and 6.

## Statement and consumers

- The label occurs only at its declaration (CA-I L45163) in CA-I/II/III. mu L24 is correct.
- 4.13(b) itself defines the required property: the nesting identity CMP 109 (3.38) read for an arbitrary sub-domain. The Route (L45193-45197) asks for this identity. It does not ask for finite-range response.
- Consumers read: CA-I 33602-33827 (4.8 near case; the identity, then only the norms of R(g)); 32422 (4.7 "nesting lemma for (3.38)", U:=1); 29235-29240 and 31073-31131 (4.7, condition (iv) from (iii) through the identity at Z ⊂ X ⊂ \tilde□^2); 121185-121470 and 123120-123132 (4.26, conjugator norm at triples X' ⊆ X_T ⊂ \tilde□^2); CA-II 35714 (identity on boxes □'_0); CA-II 44422, 44454 (cite "(3.38)" for a bound on ℋ, a response bound, not the identity).
- No consumer I read uses a finite-range response property under the name of 4.13. mu's reading of "locality" (nesting plus dependence on the intrinsic layered datum) is what the consumers use.
- 4.8 states X ∈ D_j, X ⊂ \tilde□^2 (CA-I 33605-33608), and every label (p,Z) has Z ⊂ X. mu §3 L49 uses the same scope.
- The meaning of (a) is consistent with Balaban. CMP 109 p. 260 (1.1) says "exactly one regular, critical orbit ... and it is a minimal orbit". CMP 102b Theorem 1 (p. 279) gives a minimal orbit in (8) and uniqueness of the critical orbit in (6). The account's continuation convention (CA-I 38500-38680; Def. 4.10, items (a)-(d)) gives the complex reading. mu §1 L36 and L262 match this.

## Findings

1. L163, L262, §5 last paragraph, (a) on the regular class. Existence comes from the Theorem 1 orbit in (8). "At most one" comes from criticality in the open space and uniqueness in (6). Together they give exactly one minimal orbit in the regular space, and one axial representative. The text says "every attained real minimizer in the problem's regular open space". This is right, but it does not name which space: the problem is posed on (8), or on (6) wherever the Theorem 1 orbit is minimal there. Wording only, not fatal. Repair: name CMP 102b (8) as the variational space and (6) as the uniqueness space.

2. §4.1, L67-86. The weighted value bound is correct. CMP 102b (172) gives |V'-1| < C_1ε_1. (173) gives (19)-(21) with ε_2 = B_5ε_1. The first inequality of (19) is |A| < ε_2 (L^jη)^{-1}, that is, ℓ|A| < B_5ε_1. At base 1, (7) holds for any ε_1 > 0, so ε_1 = ε_* is allowed. The vector Schwarz argument (one scalar holomorphic function per norm-one functional, value 0 at 0) is correct and does not depend on dimension. It uses only analyticity and value bounds, not (189)-(190). Checked, no defect.

3. §4.2, L88-118, (4.3). The unit rescaling (fine spacing h/s, potential sF) is consistent with CMP 98 Prop. 6 (164) and the level sizes (159)-(162). The literal-frame proof (CA-I 17673-17683) reads that proposition the same way. For the Q bound, Prop. 4 (131), (134)-(135) exists at the cited numbers, but the OCR of its displayed inequality is garbled. I could not read the exact form C_A s sup|F| from the OCR. Not fatal; the port is plausible and is not quoted as an exact formula. Repair: check Prop. 4 (134) against the PDF. Admission into the existence set of CA-I 38650-38673 is correct. Lemma 4.10:lem-averaged-data (CA-I 38430ff) requires supp_p(c) ⊂ bd(Z), so the carriers lie in Z ⊂ \tilde□^2 ⊂ □_j, where ℓ = 1. Then (4.2) gives |H_j| ≤ K‖D‖, and (4.5) gives margin.

4. §5, L120-163, real restriction. The steps are correct:
   - The seam test constant: C_D = 4C_A L, with Lδ < a_98/2. This uses the CMP 102b p. 278 (7) seam convention.
   - Theorem 1 at ε_1 = C_D‖D‖ < a_1.
   - The refined tower (5.3): admissible, memberwise smaller, empty terminal members harmless.
   - The port of CA-III 9.3:lem-refinement (read at CA-III 36939-37007). Its fibre-inclusion proof applies. mu's (5.2) covers its 2B_3ε test with C_7 ≥ 2.
   - The change of action domain (5.4). Changed bonds touch only Ω_1(Z). Every plaquette containing one lies in the inner action domain. Refined level-zero rows are fixed. So the inner derivative equals the refined derivative, which is zero.
   - Local-scale monotonicity, so W|_Z lies in the inner uniqueness space.
   - Inner data test C_7ε_W and the second Theorem 1 call. Both B_3 factors are kept in (5.2).

   Axial representative (5.5): CA-I 130021-130052 (HBA) imposes the tree conditions block by block on globally defined trees. Inner structure blocks (level ≤ n ≤ j) sit inside outer level-j blocks of the top region. So the inner conditions are a subset of the outer ones, and the residual-gauge argument gives literal equality. Checked, no defect.

5. §6, L165-191, complex continuation. Both sides of (6.1) are holomorphic on the whole δ-ball:
   - the left side through (4.4)-(4.5) and the base-one inner chart;
   - the right side through §G's u_j(D).

   They agree on the real slice (a totally real slice of full dimension), so they agree on the connected ball. The covariance step is the account's Def. 4.10(d) / CMP 102b (181), with ṽ constant on blocks and equal to v at the roots, and equal to u_j on the fixed shell. That is consistent with the shell bonds being data and the bonds touching Ω_1 being variables. Checked, no defect.

6. L179-183 and L268, product order. Under the account's action U^h(b) = h(b_-)U(b)h(b_+)^{-1} and (U^a)^c = U^{ca} (CA-I 129758-129790, "as in CMP 109 (1.10)"; CMP 109 p. 262 (1.10) agrees), my own computation gives:
   - U_T(M_T(𝒰|_Z)) = (W|_Z)^{ū^{-1}} = (𝒰|_Z)^{ū^{-1}u_j};
   - pointwise g(x) = u_j(y)^{-1}u_j(x).

   The account prints g = u_jū^{-1} and g(x) = u_j(x)u_j(y)^{-1}. So the correction is real as a statement about their text. But:
   - (a) It is not load-bearing. Every consumer uses only ‖Ad_g^{±1}‖ ≤ |g||g^{-1}| (CA-I 33698-33735, 31085, 121448-121455). Both orders give the same bound. L268's "required in the near-case consumer" overstates this: the correction is needed for the printed identity to be literally true, not for any bound.
   - (b) The account already uses the correct element g = ū^{-1}u_ℓ at 121440 and 123129, and its remark 130178-130191 says the acting element is "fixed by the chain of equalities". mu L9 acknowledges this.
   - (c) mu names only 33615 and 33686-33689. The same reversed product also appears at 29236 (definition g_⟨3.38⟩ := u_jū_j^{-1}), 31077, 31110, and 121436-121437 ("up to the gauge transformation u_ℓū_ℓ^{-1}").

   Repairable wording: list all sites, and say "needed for the identity, not for the bounds".

7. §7, L193-236, admission of the actual datum.
   - Imported clauses: CA-I 4.5:lem-literal-frame (AX1), (AX2-poly) and the first paragraph of (AX3) are proved at CA-I 17673-17770 from published results only. Hypothesis (A) is first used in the paragraph after the log bound. (C) is restricted to (AX1-𝐔)/(AX2-pt). mu's claim at L203 is correct.
   - (7.1) matches (AX2-poly) and |B_V| ≤ 2|V-1|.
   - Unit check of (7.2): the literal-frame window tower is the same {□_n}. On □_{q-1} the incoming level is ≥ q-1. Then s_q·L^{-1}|ℋ| ≤ L^{q-n}K‖B_V‖ ≤ LK‖B_V‖. Correct.
   - The BCH log bound with t ≤ log(4/3) is correct (derivative e^t/(2-e^t) ≤ 2).
   - (7.4) follows. mu writes H_{k+1}(B_V) where CMP 109 (3.30) has H_{k+1}(□_0, τ log V). This is harmless for |τ| ≤ 1, since (4.2) is linear in ‖B‖. Notation only.

8. §8, L238-246, order of choice. Fixed after (d,L) and before M and the amplitudes: ε_*, r, K, a_98, C_A, C_D, C_7, δ. Theorem 1's a_0, a_1, B_3 "depend on d and L only" (CMP 102b p. 279), and C_1, B_5 are absolute or (d,L) constants ((172)-(173)). The new conditions are ceilings α ≤ c(d,L,M), of the same form as the account's existing ceilings (CA-I 34818: "chosen after (L,B^(109),M)"). Every existing coupling among amplitudes bounds a later amplitude by an earlier one (α_0 by α_1; α_3 by α_0, α_1; α_2 by α_3). So "decrease in the same order" closes with no cycle and is uniform in j, n, p, Z. One note: at the account's running radii α_{·,i}, the new ceiling must be imposed on every running radius. It has the same form, so no new obstruction. Not fatal.

9. L26 and L256, side remarks. Two wording issues, no effect on the result:
   - CA-II 44422/44454 cite "(3.38)" for ℓ_j sup|ℋ(B)| ≤ B_3|B|_∞. mu's (4.2) proves a bound of exactly this form, with K in place of B_3. So "the present proof does not establish" response estimates understates it slightly. These are not uses of 4.13.
   - Table L34: "The proof consumes PH3" refers to hma Theorem 8, not to mu (mu never uses PH3). L256 says mu "supplies the minimizer identity needed by the complete account's use of PH3", but PH3 is our hma hypothesis, not the account's. Repair: rephrase.

10. Scope of use. mu's admission (§7) is written for D = τB + B', |τ| ≤ 1, |B'| < 2α_3, Z ⊂ X ⊂ \tilde□^2. This covers 4.8 and 4.7 (32422; 31104-31112 at labels (p,Z) ∈ T_{i'}(X) with Z ⊂ X ⊂ \tilde□^2, provided its radius α^♯_{3,i'} ≤ 2α_3 at the running radii).
    - 4.26 (121185ff) reads (3.38) at X' ⊆ X_T ⊂ \tilde□^2, at the full datum ςQ + ςQ' + B' with |B'| < α_3(T).
    - CA-II 35714 reads it on boxes □'_0 ⊂ Q^{~-2} with data 𝔅^*_j.

    mu does not check those radii and geometries. The §§4-6 mechanism needs only two things: the outer datum in the δ-ball of a base-one chart, and Z's carriers in the outer top region. It would transfer once each radius is checked against δ. These uses lie outside 4.13 as stated (which is about Lemma 4's fields and domain). Not fatal. Repair: state the theorem in that general form and check each consumer's radius.

11. Quotations. These match the sources:
    - CA-I: 45162-45201 ("Proof outstanding."); 33602-33618, 33654-33682; 129758-129790; 130178-130191; 17533 (C_7); 17519-17597, 17673-17778; 34745-34883; 111211 (CA-III).
    - CMP 109: p. 260 (1.1); p. 262 (1.10); (3.30); (3.37)-(3.38) (pp. 277-278); Lemma 4 / (3.53) and "sufficiently small and satisfying all the restrictions" (p. 280).
    - CMP 102b: pp. 278-279 (2)-(8), (4), (7) seam convention, Theorem 1; (172)-(173), (181), Prop. 9 (pp. 305-307).
    - CMP 98: Props. 2, 4, 6; (52), (131), (134)-(135), (159)-(164) exist at the cited numbers.

    mu marks OCR-damaged formulas as not quoted exactly. I found no fabricated quotation or line reference. I did not open CA-I 18616-18620, 24239-24405, 32839-33043 except 32970-32988, or 34241-34418.

## Verdict

CA-I Lemma 4.13:lem-minimizer-unique is proved as stated, read in the account's own regular-real / continued-complex meaning (CMP 109 (1.1); Def. 4.10). This covers (a) uniqueness of the minimal orbit and of the axial minimizer in Balaban's regular space, with the holomorphic continuation at complex fields, and (b) the nesting identity for every sub-domain Z ⊂ X ⊂ \tilde□^2, either tower rule, and 1 ≤ n ≤ p ≤ j. The ceilings are explicit, have no cycle, and are uniform in depth and domain.

It is also proved as used by the near-case consumer 4.8 and the 4.7 nesting uses. For those consumers, "locality" means nesting, not finite-range response. The product-order correction is real but cosmetic: no estimate changes, and the account already uses the correct order elsewhere.

Uses at other data radii or geometries (4.26 stage composites, CA-II 35714) are not covered by the written admission step. They need the radius check of finding 10. All findings are repairable wording or scope notes. None is fatal.

The port of CMP 98 Prop. 4 (134) for Q was checked only against garbled OCR.

Checked line by line by Claude (fresh session).
