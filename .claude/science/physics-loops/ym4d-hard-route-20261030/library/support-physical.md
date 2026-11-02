lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-03T07:56Z

# support-physical: (D-F) on the physical label datum (queue row 96)

Provenance: Anthropic claude-opus-5-5, effort max, Mac mini worker, checkout `d4226aaf7`. Section 1 gates a Codex section (cross-provider read, one reader, not an audit, no status); Sections 2-7 are new proofs by the same model, **ungated**. Sources: Ethan Sussman and Levent Alpoge (with Claude and Codex as authors of their text), `YM4_sketch_500.tex` ("SA n") and `theorem_0_complete_account_raw_I.tex` ("raw I n") at `31a47c543775`, fetched once into a private scratch folder; T. Balaban, CMP 119 (1988) 243-285, OCR in `~/ym4d-papers/` (read in place, not copied). Balaban CMP 122 (1989) is not in hand. No numeric job was run (memory 64 percent free; none was needed).

**Moves:** `library/route-decisions.md` position H (Package C rank 1, floor screening): the support input (D-F) of `library/floor-screen.md` Theorem R, on the physical label datum V_l on Γ_l of the old core (SA 17709).

## 0. Result

| Item | Verdict or status |
|---|---|
| `support-envelope.md` §15, initial strip (15.1) | ADVANCE |
| §15, positive-level ordinary read and ordinary seams | ADVANCE |
| §15, its read sets against CMP 119 | confirmed; one non-breaking difference at the first step (D1) |
| Healed draws of older operations (§4 here) | proved, bound 2ε_s; **Proposition 2.4 is not used** |
| Islands, the second-class draws (§5) | proved given Proposition 2.4 (cited-pending) and reading R1 of the cut-off; under the other reading, (D-F) fails |
| Inherited raised cells and drop-out bare integrals (§6) | proved from the arrested attempt's own passed stage tests |
| (D-F) on the physical label datum, every case (§7) | proved, conditional on Proposition 2.4 (islands only), R1, and the outline's read sets (CMP 119 (3.1)-(3.5); SA 17624) |

The case list is complete by raw I's list of level-assigning operations (§2). Healed draws need no Proposition 2.4, so the gate's statement that older draws read Proposition 2.4 narrows to islands. Raw I's inherited-datum hypothesis concerns a different quantity, the near-group total, and is not needed here.

## 1. Gate of `support-envelope.md` Section 15

**Read sets, checked against the CMP 119 OCR.** First step (pp. 246-248): (1.4) is χ_1(□') = 1{sup over p ⊂ □'^~ of |U_{1,□'}(V,∂p) − 1| ≤ ε_1 L^{−2}}, with U_{1,□'} = U(B_1(□'^{~4}), M^·(Q_1^* V)) from (1.2). (1.8)-(1.9) give χ'_0(□') = 1{|U(b)U_{1,□'}(b)^{−1} − 1| < 2δ_0 on (□'^{~2})^*}, where * keeps every bond with an end point in □'^{~2} except the pivots b_0(c) of coarse bonds c touching □'^{~2}, and δ_0 = (A_1/A_0)ε_0. Ordinary step (pp. 264-265, (3.2)-(3.5)): plaquette tests on the cubes of (Z_k^{~4})^c; gauge fixing outside P'^~ ∪ Z^{~5}; approximate tests (3.3)-(3.4) on (P'^{~2} ∪ Z^{~6})^c with reference V_k^{(□)} = M^k U_{k+1,□}; and Ω_{k+1}^c = Q'^{~2} ∪ P'^{~4} ∪ Z^{~8}. These are the read sets of the note's 14.1 and the layer numbers of SA 17320.

**(15.1), initial strip: ADVANCE.** I redid each step:

- The clearances (10.1).
- The approximate test at D was made, since C misses P'^{~2} and there is no older region.
- Both tests passed, since C is in neither Q'_1 nor P'_1.
- The footprint inclusion: the bonds of p and the double blocks of its at most four pivot rows lie within 4L of the corner, which is inside D^~ once the test side exceeds 8L.
- The top member of D's tower contains D^~ (14.1; gate of row 94, §1(c)), so M(W)(c) = V_1(c) = M(V_0)(c).
- The pivot lemma, then (3.3).

The rows read only their own pivot (SA 8167-8175), and * removes exactly the pivots. The pivot lemma and (5.1)/(5.3) are inputs, so I re-derived them:

- In a row, L of the L^4 parallel segments cross the pivot, so w = L^{−3}.
- (4.2) and the choice wE + La + b ≤ πw/4 keep P and the off-pivot closed transports a fixed distance from −1.
- d/dt[e^{(1−t)X}e^{tY}] = e^{(1−t)X}(Y − X)e^{tY} gives ‖e^X − e^Y‖ ≤ ‖X − Y‖.
- At the flat field the pivot derivative of the row logarithm is wI: +I from the central transport, and −(1 − w)I from the off-central closed transports.
- (5.2) is the Stokes sum over the L×L squares of the L^4 segments, with total weight L².
- The iteration (5.3) closes under exp(2K_L ε/(L²(L²−1))) ≤ 2.

No defect in either.

**Positive-level ordinary read and ordinary seams: ADVANCE.**

- A test loop with a bond in Γ_t has an end point in Ω_t (SA 9607).
- The chosen cell avoids Ŷ^{~8} and P'^{~4}, so χ_t(D) was made outside the four-cell margin and passed.
- At step t the delta function gives V_t = M(V_{t−1}) on every coarse bond, so a mixed test equals ∂V_t(p') of the step-t field, and (5.3) gives 2ε_t.

The note uses (3.1). The value is the same, fixed at the coarse side's birth (§3 here).

**Defects (none breaks the section):**

- **D1 (non-breaking).** CMP 119's own first step has a level-0 large-field set P_0 with one-layer margins ((1.2) tests on (P'_0^~)^c; (1.10)). The outline has none: ρ_0 is the bare Wilson density, and SA 23265 starts the determining set at Ω_0 = Ω_1^~. So Y = ∅ at step 1, as the note says. With P_0 present the clearances would be dist(C, Q'_1) ≥ 2, dist(C, P'_1) ≥ 3 and dist(C, P'_0) ≥ 4, and the proof is unchanged.
- **D2 (scope).** "Ordinary" must mean that the coarse bonds received their values and level at T_t, with an end point in Ω_t as set by step t. Parts of the current Ω_t added later by a completed decision or a preparation raise are the cases of §§4-6 here.
- **D3 (support).** §15 carries (15.1) forward by §4's persistence of values. Persistence **on supports** also needs the passed indicators to stay in force after the factors are reorganised. Lemma P (§2) supplies this.

Section 15 does not treat draws, raises or collar lifts, and says so.
