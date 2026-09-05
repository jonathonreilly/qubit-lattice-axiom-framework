# RESULTS — block 214, the duality parameters and the principal part (Fable primary, relaunched seat)

Runner: `scripts/admissibility_dirac_kahler_duality_parameters_principal_part_2026_09_05.py`
Note: `docs/ADMISSIBILITY_DIRAC_KAHLER_DUALITY_PARAMETERS_PRINCIPAL_PART_BOUNDED_THEOREM_NOTE_2026-09-05.md`
Exact arithmetic only (SymPy rationals, symbols, QQ(sqrt 6) at the two locus witnesses, fraction-free
DomainMatrix determinants and charpolys over the polynomial rings, lex Groebner bases); gate I measures
zero `sp.nsimplify`, zero float literals and zero float call sites in the runner's own source.

## Headline

Every one of the four duality parameters is a cross-parity entry of the cell, so the onsite folded `H0`
stops preserving grade parity for each of them; but the principal part `M = H0 D + D^T H0` has a
parameter-free off-diagonal block (`M_eo = B`, Block 213's) and the parameters enter only the diagonal
blocks: `M_ee` = the bordering of corner 0 by `u = ((D07+D34) kt, (D25-D07) kx, (D07+D16) ky)`, `M_oo` =
the zero-diagonal `[(D16+D25) kt, (D34-D16) kx, -(D25+D34) ky]` on the 1-forms. `D07` is removed from `M`
by the exact unipotent congruence `U = I - (D07/D3) E_70`, which shifts `D0 -> D0 - D07^2/D3` in `H0`: the
cone never sees `D07`, and the 0-form pencil branch is rescaled by `1/(1 - D07^2 v1/v0)` (diverging at
Block 211's bound). `det M = det B^2` — the union of the two Hodge cones — holds exactly on the plane
`D16 = D34 = -D25` (any `D07`; overlap: `s = D07+D16+D25+D34 = 0`) and nowhere else at every witness;
off it `det M = Q^2` with `Q = Q0 + Q2` one irreducible quartic, `Q2` an even quadratic in the
parameters, absolutely irreducible on the declared slices except at `s = 0`, with no line factor. No
parameter point restores a single metric's cone at any non-locus witness; at the locus witnesses the
single-quadric cone persists exactly on the plane. The flat cell with a parameter on is not the identity.
The shears register with the parameters on and no parameter cancels either; the volumes enter the
cone through the parameters (formal family).

## Run record (every run's summary line)

| run | command | summary | exit |
| --- | --- | --- | :---: |
| exploration 1-3 (scratchpad, not deliverables) | scratch | parity blocks, D07 congruence, union-locus Groebner, slice eliminants measured; the linear x cubic Groebner timed out (replaced by the exhaustive three-chart line test) | — |
| exploration 4 (scratchpad) | scratch | killed after 17 min with buffered output: the thirteen-unknown two-quadric lex basis in (D16, D25, D34) did not finish (recorded as a could-not) | killed |
| measurement run 1 (6f63e1aa08) | baseline | killed in its branch phase: generic symbolic 8x8 charpolys too slow for the 600 s cache (defect 1, fixed by the fraction-free DomainMatrix charpoly) | killed |
| measurement run 2 (fast charpolys) | baseline | killed in its cone phase after 4 min: the two QQ(sqrt 6) witnesses through generic `berkowitz` + `factor_list(extension=sqrt 6)` at three symbolic parameters (defect 2, fixed by the algebraic-field DomainMatrix determinant and the `r^2 - 6` ring trick) | killed |
| measurement run 3 (b476d1d886) | baseline | killed in its cone phase after 8 CPU-min: the line-factor and two-quadric-slice Groebner systems at all five rational witnesses (defect 3, fixed by scoping those two tests to W1 and re-scoping the fence, the note and the checks identically) | killed |
