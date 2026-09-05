# RESULTS — block 217, the other assembly at the covariant cells, and the bench (Fable primary seat)

Runner: `scripts/admissibility_dirac_kahler_overlap_assembly_covariant_cells_2026_09_05.py`
Note: `docs/ADMISSIBILITY_DIRAC_KAHLER_OVERLAP_ASSEMBLY_COVARIANT_CELLS_BOUNDED_THEOREM_NOTE_2026-09-05.md`
Exact arithmetic only (SymPy integers, rationals, symbols, `QQ(sqrt 6)` and `QQ(sqrt 6, i)`; fraction-free determinants;
lex Groebner bases with their radicals; factorization over `QQ(sqrt 6)`; signed permutation matrices; exact charpolys of
`8 x 8` and `16 x 16` matrices over algebraic number fields); gate I measures zero `sp.nsimplify`, zero float literals
and zero float call sites in the runner's own source.

## Headline

At each of Block 216's 8 rule-A cells, with Block 213's curve witness transported by class, the overlap fold
`H0 = H0(0) + (s/4) P111` sees the four duality parameters only through their sum `s` — measured at SYMBOLIC face
signs and moduli, so a lemma at every cell, with the parity block `(s/4) P111` and the twelve two-flip couplings
`-(s_f0 g0 v0 v1 + s_f1 g1)/(4 v0)` (Block 213's `h_f`) at `s = 0` — and its `s = 0` locus does NOT meet covariance
there the way the onsite plane does: the fold's strict stabiliser is the identity alone for every `s` (under the
cell's own `S3_body` the order-3 elements force `g0 = g1 = 0` at symbolic moduli, the order-2 elements force
`g0 v0 v1 + g1 = 0` with a shear killed or with `g0 v0 v1 - g1 = 0`, and the curve gives `g0 v0 v1 +- g1 = 3/4, -1/4`
where `pi0 = +1` and `7/9, 1/9` where `pi0 = -1` — no variant is satisfied), its twisted stabiliser is a `D4_face` about
the `x` axis for EVERY `s` (no rotation forces `s = 0`; the `S3_body` is not inside it; the two assemblies share one
twisted `C2_edge`), so the TWO ASSEMBLIES DIFFER IN COVARIANCE AT THE COVARIANT CELLS (the exact negative of the
contract's (e), N1-N8 in the note). The union locus (`det M = det B^2` in `kappa`) is exactly `s = 0` at all 10
witnesses (`det M` of degree 4 in `s`, `det B` `s`-free). The overlap cone at `s = 0` is a pair of DISTINCT rational
quadrics differing in the sign of the `kt ky` term alone (`c_xx, |c_1|, |c_ty| = 59701/57109, 24516/57109, 2988/57109`
at `pi0 = +1`; `64961/61889, 27664/61889, 2192/61889` at `pi0 = -1`), proportional to neither the onsite `k^T G1 k` nor
each other — Block 213's non-Hodge pair, now at the covariant cells, NOT one metric's cone and NOT the onsite cone —
and for symbolic `s` it is ONE irreducible polynomial (degree 2 in `s`, 4 in `kappa`) squared: the pair merges into an
irreducible quartic off `s = 0`. On Block 213's `(4,2,2)` bench at L+-'s own cell (mask 2) with the parameters on the
star line at `1/4`: sixteen exact degree-16 charpolys with Bloch union = direct at every one; the onsite pencil
multiset `{0 x8, 9/8 x2, 16/11 x2, 18/11 x4}` is `G1_tt = 9/8` times Block 216's four branch constants
`{1, 128/99, 16/11 x2}`, because the onsite pencil bench charpoly is EXACTLY `lam^8` times the charpoly of
`(H0^-1 M(e_t))^2` (an identity at the witness, the all-plus control and the flat cell) — the bench reads the principal
part at ONE direction and the cone's shape is invisible to it; the onsite form is `lam^8` times an irreducible quartic
squared; the overlap form `{0 x8, 36481/55296 x4, 89401/55296 x4}` and pencil `{0 x8, 1 x8}` (R5's) EQUAL their
zero-parameter values, because the overlap Bloch fold at the bench's nonzero point `z = (i, 1, 1)` is parameter-free
at symbolic everything — the bench does not see the overlap sum. At the all-plus `W1` control the fold is twisted-`O`
for every `s` with a trivial strict stabiliser, the onsite bench pencil is `lam^8 (15 lam - 16)^2` times an irreducible
cubic squared and the overlap form is Block 214's `OVERLAP_FORM_W1`; at the flat cell both assemblies give `H = I`,
the fold `I + (s/4) P111` is strictly `D4_face`-covariant for every `s`. Nothing selected; the covariance antecedent
stays a reading; no continuum or light-cone reading of the bench.

## Run record (every run's summary line)

| run | command | summary | exit |
| --- | --- | --- | :---: |
| probe 1 (scratch, 18:24Z) | `probe1.py` | the fold sees only `s` at symbolic signs; `(s/4) P111`; the twelve couplings; the shear relation at symbolic moduli at all 8 cells (order-3: `g0, g1`; order-2: `g0, g0 v0 v1 + g1, g1` twice and `g0 v0 v1 +- g1` once) with the curve values `3/4, -1/4` / `7/9, 1/9`; at cells 2, 11, 38: strict stabiliser `(0,)`, twisted `{0,1,2,3,20,21,22,23}` for all `s`; union locus `(s,)` (0.8 s each); `det M(s)` one `(2,4,4,4)` factor squared (2.9 s); `det B(0)` two distinct rational quadrics; bench at L+- and W1 (8 charpolys, 0.1-0.4 s each, Bloch = direct); onsite pencil at `e_t` = the bench multiset; the overlap Bloch fold at `(i,1,1)` parameter-free — 59 s total | 0 |
| probe 2 (scratch, 18:33Z) | `probe2.py` | the identity bench pencil = `lam^8` charpoly((H0^-1 M(e_t))^2) True at L+-, W1, flat (onsite); False for the form reading and the overlap assembly; overlap multisets at the line point = zero-parameter ones; Bloch fold `(i,1,1)` vs `H0(0)`: 16 entries differ; W1 all-plus: strict `{0}`, twisted all 24 for all `s`, union `(s,)`, `det B(0)` two quadrics; flat: strict `{0,1,2,3,20,21,22,23}` all `s` + 16 at `s = 0`, twisted all 24, union `(s,)`, `det B(0)` one quadric squared; the twisted set is the class `D4_face` — 23 s | 0 |
| harness run 1 (d1f4415d5c, 18:23Z) | full runner | `TOTAL: PASS=26 FAIL=3` in 87 s: `D-3` (axis literal `(1,0,0)`, measured `(0,1,0)` — defect 1), `E-1` (`ky -> -ky` relation False — defect 2), `I-1` (note not yet written) | 1 |
| harness run 2 (9fcd400b9e, 18:25Z) | full runner | `TOTAL: PASS=28 FAIL=1` in 86 s: only `I-1` (the note's fence appended after the run started) | 1 |
| certified baseline (781f00c0fe) | `runner_cache.execute_and_write_cache(..., 600)` | see "Certified baseline" below | see below |
| mutations (781f00c0fe) | `--mutation <name>` x 29, one helper invocation per mutation, 4-way parallel, concurrent with the certification | see the table below | see below |

## Defects found in this seat's own drafts (before certification) and fixed

1. The declared axis of the overlap fold's twisted `D4_face` was written as `(1, 0, 0)`, which in the lane's `(t, x, y)`
   coordinates is the `t` axis; the measured axis is `(0, 1, 0)`, the `x` axis, as the note's argument (the odd face is
   `ty`, the 4-fold about `x` exchanges `tx` and `xy`) requires. Literal corrected; no mathematics changed.
2. The pair of overlap quadrics was declared "related by `ky -> -ky`"; that reflection also flips the `kx ky` term, which
   the pair shares. The measured relation is that `Q+ - Q-` is a multiple of `kt ky` alone (the pair differs in the sign
   of the `kt ky` coefficient, Block 213's "t-y plane terms"). Fact and literal corrected; no mathematics changed.

## Modelling choices not forced by the landed chain

- The witnesses: Block 216's — Block 213's curve points transported by class of `pi0`; W1's moduli at the all-plus
  cell; the flat moduli. The loci and the cone are measured at all 8 rule-A cells (not one per class).
- The overlap parameter: `s` symbolic for the loci, the stabilisers and the cone (`(s, 0, 0, 0)` placed on `D07`,
  which is exact by the fold lemma); the bench at the numeric star-line point `(D16, D25, D34) = (1/4, -1/4, 1/4)`,
  `D07 = 0`, i.e. `s = 1/4` — and at zero parameters for the overlap comparison.
- The bench: L+-'s own cell (mask 2) as the covariant witness, the all-plus W1 and the flat cell as controls; the
  direct `16 x 16` charpoly over `QQ(sqrt 6)` and the Bloch union over `QQ(sqrt 6, i)` — Block 213's `domain_symbol`
  re-implemented over algebraic number fields (its own runs were at rational witnesses in `QQ(i)`).
- The stabilisers in `s`: feasibility per (rotation, sign vector) from the entries of `T H0(s) T^T - H0(s)` (a nonzero
  constant = infeasible; a multiple of `s` = `s = 0` forced; zero = free), rather than Block 215's `constraints`,
  whose forced-set bookkeeping assumes symbolic moduli.
- The shear relation: the non-volume factors of the residual entries at symbolic moduli at each cell's own signs,
  under the cell's own onsite `S3_body` (Block 216's stabiliser), then evaluated on the curve.
- The small-`k` statement is an exact polynomial identity between two charpolys (bench and principal part at `e_t`),
  not a limit; the cone at `e_t` is reported as the number `c G1_tt^4`.

## What could NOT be established (honest list)

- The bench at the other seven rule-A cells, at symbolic parameters, at other line multiples or with `D07 != 0`: not
  run (one witness, one numeric point, as contracted; the overlap charpolys at the line point equal those at zero
  parameters, so for the overlap assembly the point does not matter on this bench).
- The two-direction `(4,4)` bench at a covariant witness: not run; the `x`-axis distinction of the overlap `D4` and of
  `Q+-` is measured on the principal part only.
- The flat cell's onsite form charpoly on the bench: measured (Bloch = direct, degree 16) but its factor shape is not
  declared as a literal.
- The overlap loci symbolically in the moduli at the rule-A cells (the stabilisers at symbolic `g0, g1, v0, v1` with
  `s` symbolic): only the shear relation (the `S3_body`'s forced conditions) is symbolic in the moduli; the twisted
  `D4_face` and the union locus are at the 10 exact witnesses.
- Whether the overlap cone's `Q+-` at the rule-A cells has a closed form in the moduli (Block 213's
  `OVERLAP_CONE_PLUS/MINUS` in `h0, h_f`): not compared symbolically; the rational coefficients are declared per class.
- The refuting checker: pending (`CHECK_VERDICT = "FABLE-PRIMARY-REFUTING-CHECKER-PENDING"`); the independence class
  is left to the supervisor.
