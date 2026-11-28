# Check of library/lfi-ho.md (H-O lane)

Checked line by line by Claude (Opus 5.5), 2026-11-08. One check. Not an audit.
Clone at `04e7c612f` (branch claude/ym4d-hard-route). Note at commit `8f3484ab9`.
Sources read: Y = YM4_1400.tex (2bc0658f); SA = YM4_sketch_500.tex; I = raw_I.tex; IN1, in1-gate, prior/lfi.md, sa-2.13-2 §§6–7, loc-4 §5, src-array 222–226, open-registry, dom.md 359.

## Verdict: FIX

The ported summation and the conditional two-pair implication are correct.
The arithmetic is correct. The citations are accurate.
But D4-CARRIED is not the only open input.
The single-term collar bound is an open input inside H-O itself. It has no owner and no proof in the library.
One clause of (11) belongs to H-E, not to DOM.
The repairs are small. They change the status table, not the proof.

## Findings

1. **Target (1).** Note 16–30; IN1 (8) at in1.md 88–91, (18) at 197–201; SA 6291–6310; Y 1420–1446.
   CONFIRMED. Same sum, same power ℓ^{2p₀}, same decay. Both pairs vary independently on the fixed domain; ξ is shared.
   The note writes 𝒦_{t,X}; IN1 writes 𝒟_i(X̃). Same object. No repair.

2. **Anchor and difference (2)–(4).** Note 78–114; Y 73387–73559.
   CONFIRMED. Y 73551–73559 defines δ_R and applies Schwarz on |λ|<2/a_R. Sup of the difference ≤ 2b^♯ on that disc gives a_R b^♯ at λ=1. The supremum is complex.

3. **Disc inclusion is sketched in Y, not only a premise.** Note 114 and 63; Y 73508–73556.
   UNCLEAR. Y argues the target-space inclusion for |λ|<2/a_R from the profile comparison and running radii ("the argument stays in the target space ... uniformly on the cube polydisc and the admitted spectator range"). The note records this as a premise. Under port-first it is SKETCHED.
   Repair: add a ledger row "Y 73508–73556, inclusion from profile comparison: SKETCHED". Say why it does not close (11): src-array 225 (the profile estimate does not supply the domains) and the scalar composition counterexample in loc-4 §5 (after line 162).

4. **Member majorants and root sum (5).** Note 116–140; Y 73561–73640.
   CONFIRMED. p^♯=2p₀+12r+2, σ=9r+p^♯, Q=4L⁸, copy splitting, and the displayed sum all match.
   b^♯ is linear in the inherited B_Φ (island part) plus a strip constant. This supports note 231.

5. **Absolute sum (6) and ε.** Note 142–157; Y 73642–73647.
   CONFIRMED. 2p₀−ε = 2p₀+p₁+51r/2+2−q = 5r+E+12r+2. E+12r+2<0 gives ε>2p₀−5r. p₀>6r is IN1 row 1 (in1.md 227). So ε>0.
   Note: Y uses this sum only to get ≤N₀(ω). The note correctly uses the sharper intermediate form.

6. **Two-pair inequality (7).** Note 171–188.
   CONFIRMED. Termwise |δ(P)−δ(P')| ≤ 2 sup|δ|, sup inside the sum, P and P' independent and complex. No real bound and no path is used. This is exactly what IN1 (18) consumes, on the range where (4) holds.
   Minor repair: write the sup over all admitted triples representing P. δ_R is built from the triple 𝔷, and pair-independence uses the tie (Y 73248–73252, 73404). List the tie as an input.

7. **Output carrier X^∼, hull length zero.** Note 190–196; Y 73887–73892.
   CONFIRMED. Minor repair: say that every δ_R is formed through the full reader (Y 73466–73559 builds every T_R¹ from the formed datum). Note 191 reads as if some kept changes might not be.

8. **Tied reader (8).** Note 198–213; Y 73780–73839.
   CONFIRMED. −½θq^♮ + V^♮ + trunks equals the old exponent. The correction is ≤1 by Cauchy (Y 73810–73812). The identity-theorem argument for splitting independence of W^f is ported.

9. **Single-term collar bound is an unowned H-O input.** Note 217–220, 227, 319; Y 73843–73868.
   MISMATCH with the "only open input" claim. Y only sketches the per-carrier collar bound b_V ℓ^{2p₀}e^{−κd}. The proved collar majorant (Y 73660–73745) is a total bound C_col(1+c̄)N₀(ω). It has no per-carrier decay. No library file proves the per-carrier form. The registry has no row for it. H-O has owner "none".
   This is part of H-O (18) itself. It is not a DOM item.
   Repair: list it in the status table as an open input of this row. Either attack it here, from the Y 73843–73868 sketch, or register it as a named sub-input with an owner. The task prompt called it "already written". Written is not proved.

10. **Quadratic budget.** Note 221–224; Y 73264–73354 and 73878–73886.
    CONFIRMED. Y gives C A₁² Ř_t⁵ ℓ^{2p₁} + C. Ř_t ≤ Lℓ^r gives the note's ℓ^{2p₁+5r}. Twice the amplitude bounds the oscillation.

11. **Constants (9)–(10).** Note 230–259; IN1 rows 1 and 9 (in1.md 227, 235).
    CONFIRMED. B_Φ is fixed first. X₀ follows. γ=X₀^{−1/2} is IN1 row 9. The tail argument with n>σ is correct. A₁ only needs to precede X₀.
    Repair: write both gaps as explicit row-1 inequalities: q > 2p₀+p₁+41r/2+2, and p₁ < p₀−5r/2. Row 1 now has only q>max(p₀+2r, Cp₀) and p₁<p₀−Cr. Both permit these, but neither states them.

12. **Budget sum and induction.** Note 261–267; Y 73895–73905.
    CONFIRMED. ½+¼+¼ on X^∼. Collar ≤½ on the smaller carriers. A standing island keeps its bound by restriction. The induction from the bare presentation needs no ancestor sum.

13. **(11) assigned to D4-CARRIED.** Note 271–292; loc-4 150–162 (D4 at 156); src-array 222–226; registry row D4-CARRIED (owner DOM); dom.md 359.
    CONFIRMED for the substitution room. S_R(λ) = anchor ⊕ λ·response in the original target space is an instance of (D4), with ν=λ and F=φ_R. That is a carried-composition admission, not an H-O gap renamed.
    Repair: D4 states ϱ_F>1 plus the R11 lower bound. (11) needs ϱ_F = 2/a_R = (2/C_*)ℓ^{q−p₁−r/2}Q^{u_R}. That radius grows with depth u_R. Add this exact radius to the D4-CARRIED row. Otherwise DOM could close D4 at a smaller radius that does not supply (11).

14. **Last clause of (11) belongs to H-E.** Note 285 ("the finite member bounds used in (4) must hold on this range").
    MISMATCH in owner. For island members this clause says each spectator read lies in that island's own creation domain, where its (18) holds. That is the independent inclusion of SA 6305–6306 and IN1 H-E ("every later inner read belongs to that full creation domain", in1.md 186). H-E has owner "none" in the registry.
    Repair: split (11). Substitution room goes to D4-CARRIED (DOM). Island-read inclusion goes to H-E later admission. Record that H-E is unowned.

15. **Ported citations to I and Y.** Note 67–68, 295–302; I 84503–84678, 87328–87381, 88187–88221, 49495–49546; Y 63569–63677, 32043–32176.
    CONFIRMED. I 84503 is the two-member kept-oscillation lemma. I 87328 and 88187 are marked "proof incomplete at (∗)". I 49495 says its points "lie outside the implication". Y 63569 uses served targets.

16. **Consistency with sa-2.13-2 §7.** sa-2.13-2.md 309.
    CONFIRMED in substance. §7 names the complex-pair remainder bound sup_p|V_X| ≤ CN₀ "on the actual prepared/inner substitutions" as open. That is the same (11) issue. Minor repair: cite it.

## Answers

- **Is conditional H-O what IN1 (18) consumes?** Yes. Two independent complex pairs, sup inside the sum, complex Schwarz on the substitution disc, B_Φ before γ. No real bound is used. It is conditional on (11) and on the collar bound.
- **Is D4-CARRIED the only open input?** No. The per-carrier single-term collar bound (finding 9) is open and unowned, and it is H-O's own content. The island-read inclusion (finding 14) is H-E, also unowned.
- **Is D4-CARRIED assigned correctly?** Yes for the substitution room, once the radius 2/a_R is written into the row (finding 13).
- **Missed route.** Y 73843–73868 sketches the collar bound by the same anchored-disc argument used for δ_R. Per-carrier decay e^{−κd} needs the collar root count with length decay (Y 73660–73700) applied carrier by carrier. Not attempted.

## Corrected status table rows

| Claim | Status |
|---|---|
| Two-pair inequality (7), allocation (9)–(10) | Proved here, conditional. |
| Disc inclusion for \|λ\|<2/a_R | Sketched in Y 73508–73556; open as (11a), owner DOM (D4-CARRIED, radius 2/a_R). |
| Island spectator reads in own creation domain | Open as (11b); H-E later admission; owner none. |
| Per-carrier single-term collar bound b_V | **Open; part of H-O; owner none.** Y 73843–73868 sketch only. |
| H-O for the actual construction | Open. |
