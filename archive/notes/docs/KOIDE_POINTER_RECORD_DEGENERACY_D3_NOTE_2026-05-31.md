# Koide Pointer Record Degeneracy D3: Two-Outcome S Record, Weight Still Open

**Date:** 2026-05-31
**Claim type:** bounded_theorem
**Claim boundary:** finite `C_3` regular-representation algebra and the associated
Koide block-weight comparison. This note proves the `S=C+C^2` record degeneracy and
demarcates what it does and does not select. It does not choose the physical measure.
**Primary runner:**
`scripts/frontier_koide_pointer_record_degeneracy_d3.py`
with cache
`logs/runner-cache/frontier_koide_pointer_record_degeneracy_d3.txt`.

## Result

For the `C_3` regular representation, the sector pointer
`S = C + C^2 = J - I` has exactly two distinct eigenvalues: `+2` on the singlet
projector and `-1` on the rank-2 doublet projector. A sharp `S` record is therefore a
two-outcome record, and the two doublet microstates are record-degenerate for this
chosen pointer. The conjugate pointer `A = i(C-C^2)` is Hermitian, commutes with `S`, and
has three distinct eigenvalues `{0, +/-sqrt(3)}`, so the degeneracy is pointer-relative.

This sharpens the Koide residual. Counting the two `S` record atoms equally gives the
`(1,1)` block weight, hence `r=1/2` and `Q=2/3`. Weighting by projector rank/Born weight
gives `(1,2)`, hence `r=1` and `Q=1`. D3 fixes the two-atom record algebra; it does not
fix the measure on those atoms.

## Computed Content

The runner checks:

- `C^3=I` and the signed Koide skeleton `Q=(1+2r)/3` over a free scan of `r`.
- `S=C+C^2` has spectrum `{+2,-1,-1}` with ranks `(1,2)`.
- `A=i(C-C^2)` resolves the doublet, so the two-outcome statement is about the `S`
  pointer, not every record observable.
- Equal atom counting gives `r=1/2 -> Q=2/3`; rank/dimension weighting gives
  `r=1 -> Q=1`.
- Budget-free binary atom-share entropy and binary-channel mutual information are
  maximized at balanced atoms, while the unconstrained log-capacity is monotone unless a
  budget/share convention is supplied.
- Three blockers to a forced `(1,1)` selection: the mass operator generically resolves
  the doublet, the `I/3` pushforward through the `S` projectors is rank-weighted
  `(1/3,2/3)`, and the `S` split has unequal ranks in dimension 3.

The D3 algebra itself names no state. The `I/3` calculation is only the rank-weighted
comparison prong and does not load-bear on the D3 spectrum statement.

## Boundary

D3 supplies the outcome-merge half of the per-block candidate: for the `S` pointer there
really are two record atoms. The remaining question is the measure on those atoms:
counting symbols once versus weighting by rank/Born probability. This is the same
measure selector isolated by the cited Koide block-weight and isotype-split notes, now
localized in records language.

This note therefore opens a precise next target rather than closing the Koide lane:
derive the atom-counting measure from source structure, derive the rank/trace measure, or
explicitly admit a convention outside this note.

## Load-Bearing Authorities

[KOIDE_CIRCULANT_Q_TWO_THIRDS_ALGEBRAIC_NARROW_THEOREM_NOTE_2026-05-10.md](KOIDE_CIRCULANT_Q_TWO_THIRDS_ALGEBRAIC_NARROW_THEOREM_NOTE_2026-05-10.md)
[CHARGED_LEPTON_KOIDE_CONE_ALGEBRAIC_EQUIVALENCE_NARROW_THEOREM_NOTE_2026-05-10.md](CHARGED_LEPTON_KOIDE_CONE_ALGEBRAIC_EQUIVALENCE_NARROW_THEOREM_NOTE_2026-05-10.md)
[SOURCE_MEASURE_SHARP_RECORD_TANGENT_SPACE_THEOREM_NOTE_2026-05-30.md](SOURCE_MEASURE_SHARP_RECORD_TANGENT_SPACE_THEOREM_NOTE_2026-05-30.md)
[KOIDE_FROBENIUS_ISOTYPE_SPLIT_UNIQUENESS_NOTE_2026-04-21.md](KOIDE_FROBENIUS_ISOTYPE_SPLIT_UNIQUENESS_NOTE_2026-04-21.md)
[KOIDE_Q23_BLOCK_WEIGHT_FRONTIER_BOUNDED_NOTE_2026-05-29.md](KOIDE_Q23_BLOCK_WEIGHT_FRONTIER_BOUNDED_NOTE_2026-05-29.md)
[ACTION_NORMALIZATION_NOTE.md](ACTION_NORMALIZATION_NOTE.md)
[PRE_RECORD_REFERENCE_STATE_TRACIAL_DERIVATION_NOTE_2026-05-20.md](PRE_RECORD_REFERENCE_STATE_TRACIAL_DERIVATION_NOTE_2026-05-20.md)
[THREE_GENERATION_OBSERVABLE_THEOREM_NOTE.md](THREE_GENERATION_OBSERVABLE_THEOREM_NOTE.md)
[THREE_GENERATION_HW1_DISTINCT_TRANSLATION_CHARACTERS_NARROW_THEOREM_NOTE_2026-05-10.md](THREE_GENERATION_HW1_DISTINCT_TRANSLATION_CHARACTERS_NARROW_THEOREM_NOTE_2026-05-10.md)

Non-load-bearing lane context: `KOIDE_READOUT_LANE_DEMARCATION_NOTE_2026-05-30`.

## No-Go Discipline Gate

**N1 - Alternative routes.** Five routes were checked. Route 1: `S` degeneracy forces
equal atom weight; attempted, fails because degeneracy fixes the sigma-algebra but not
the measure. Route 2: the mass record fuses the doublet; attempted, fails because a
generic Hermitian circulant `H` has three distinct eigenvalues. Route 3: the `I/3`
ensemble selects atom counting; attempted, fails because the `S` pushforward is
rank-weighted `(1/3,2/3)`. Route 4: equal-rank binary-record transport supplies the
balanced reference; attempted, fails because the `S` ranks are `(1,2)` in odd dimension
3. Route 5: pointer preference or `A` can be ignored; attempted, fails as a forced
selector because `A` is a commuting record observable that resolves the doublet.

**N2 - Wall independence.** The collapsed residual is one wall: a measure selector for
the two `S` atoms. The apparent walls "equal block metric" and "objectivity
maximization" are sufficient inputs for the conditional route, but neither is forced by
D3 and neither follows from the other.

**N3 - Hidden-wall scan.** The proof only uses the finite `C_3` matrices, the stated
Koide `Q(r)` skeleton, and the explicitly linked comparison notes. The phrases
"record," "objectivity," and "`I/3`" are bounded to the stated comparison prongs; none is
used as an unstated selector.

**N4 - Residual matching.** The residual matches the block-weight frontier and
isotype-split residual: select `(1,1)` versus `(1,2)`. The action-normalization citation
is only a witness that a normalization principle does not by itself choose that weight.

**N5 - Rhetoric audit.** "D3 does not force `(1,1)`" means only that the sharp `S`
record degeneracy does not choose the atom measure. It is not a claim that no later
records theorem or convention could select `(1,1)`.

**N6 - Partial-closure path.** A source theorem deriving atom counting, a source theorem
deriving rank weighting, or an explicit convention/admission could close this residual.
This note does not call for an axiom change.

**N7 - Steelman.** The strongest pro-`(1,1)` route is that `S` is the coarse sector
pointer and a records/objectivity principle should count objective symbols rather than
Hilbert rank. The runner grants the two-symbol structure and shows the conditional route;
what remains missing is the selector that makes symbol-counting physical.

**N8 - Cross-cycle echo.** The same residual appears in the readout demarcation,
`det_R`/`det_C`, block-weight frontier, and isotype-split notes. D3 refines that residual
in records language without relabeling it as closed.
