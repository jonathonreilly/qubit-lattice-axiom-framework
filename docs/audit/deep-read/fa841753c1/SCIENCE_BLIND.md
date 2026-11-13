# Non-label re-read

Date: 2026-11-09

Pin: `fa841753c1a6296e5ad45518375660b0f1004769`

The label-clash draw is in [BLIND_TEST.md](BLIND_TEST.md). This draw is the other check: five preserved cards with `grade_clash` false whose old issue text records a content tension. The readers saw the note numbers, the paths, and the repair rule. They did not see the old cards or `FIXES.md`.

The five notes are 1635, 1704, 1715, 1716, and 1737.

## What the readers filed

Both readers filed no repair.

- Note 1635: ladder quotients match the printed cells. The reader treated section 7 as already withdrawn by the corrigendum.
- Note 1704: `w = q / (3(m^2+q))` lies strictly between `0` and `1/3` when `q > 0` and `m^2 > 0`. The note already says this is not the dust label.
- Note 1715: the polynomial reductions, roots, and induced fields are exact. The heading is the polynomial algebra, and the body disclaims a physical beta function.
- Note 1716: the printed `sigma` and `e` give `r0/a = 5.005676254205751` and the printed `global_a_fm`. The body already says the proved object is the dimensionless root.
- Note 1737: the small-correction no-go is the note's own claim. The reader computed base ratios `101.908728360781` and `6.643337541498` against printed `101.908728437` and `6.643337509`, and did not file the gap.

## Parent score

- Notes 1704, 1715, 1716, and the small-correction wording of note 1737: no repair. That agrees with the readers. The extracted title repair for note 1716 is removed. The body already separates the dimensionless root from `alpha_s(M_Z)`.
- Note 1635: repair. Section 7 still calls `rho_E(15) = +5.257476782081e+00` the sharpened target after the corrigendum says it is not. The reader did not file that leftover sentence.
- Note 1737: repair, and not the one previously extracted. The negative small-correction claim stays. The joined base-ratio equality does not hold for the printed components. The completed-slot shares do match.
- Note 1634 was not in the draw. The same leftover pattern is in its section 6, which still offers a physical selection of the size-15 floor after its corrigendum withdraws that path. That row is filed from the parent check.

Raw reader files: `batches/blind_science_a.md` and `batches/blind_science_b.md`.

## Rule change

The instruction given to those readers, that a printed corrigendum is not a second repair, is withdrawn. A withdrawn sentence that is still printed is a repair. A recomputed gap is a repair unless the note itself prints the tolerance used to waive it. The replacement rule is [PROCEDURE.md](PROCEDURE.md).
