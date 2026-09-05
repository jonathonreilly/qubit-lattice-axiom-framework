# GOAL — block 218: the cone's shape on a two-direction bench at the covariant witness (gravity mainline)

Selected from OPPORTUNITY_QUEUE.md (block-217 closing refresh). Branch
physics-loop/toe-axiom-closure-block218-two-direction-bench-covariant-witness-20260905, stacked on Block 217.
Blocks 201-217 are landed in this branch history; Block 217's note is the format template.

## The wall, quoted
Block 217 `N6` REOPEN items 3 and 4, verbatim: "3. A bench with a small nonzero fine momentum in more than one direction
is affordable at a covariant witness: the cone's shape (the proportionality of every branch to one quadric) would then
become visible to a bench." "4. Block 213's two-direction `(4,4)` bench is run at a covariant witness: the second direction
would test the `x`-axis distinction of the overlap `D4` and of `Q±` against the onsite `S3`." Block 217's G-1: on (4,2,2)
the onsite pencil bench charpoly is exactly λ^8 times the charpoly of (H0^-1 M(e_t))^2 — one direction sampled.

## Exact target contract (proof-search governance)
Target statement | At L+-'s covariant cell (mask 2, Block 213's curve moduli (sqrt6/3, 1/3, 3 sqrt6/8, 1/2)) with the
parameters at the star-line point (0, 1/4, -1/4, 1/4), and at the all-plus W1 control (15/16, 1/4, 1, 1/4) with the same
parameters, on Block 213's two-direction (4,4) bench (extent 4 in t and 4 in x; read Block 213's bench machinery and its
note's bench sections for the exact bench definition and its Bloch momenta), determine EXACTLY: (a) every bench charpoly
(both assemblies, both readings) with Block 213's Bloch union = direct check, over QQ(sqrt 6) and QQ(sqrt 6, i); (b) the
Bloch-point decomposition: at each Bloch momentum (z_t, z_x) the 8 x 8 block's charpoly, and the exact identity with the
principal part: at the pure fine momenta (i, 1) and (1, i) with the charpoly of (H0^-1 M(e_t))^2 and (H0^-1 M(e_x))^2, and
at the MIXED point (i, i) with (H0^-1 M(e_t + e_x))^2 — state whether the identity holds exactly at the mixed point (the
Bloch raising block at (i, i) is i D(e_t + e_x) only if the two fine momenta enter additively — measure); (c) the cone's
shape from the bench: under the onsite assembly at the covariant witness, the pencil block charpoly at the mixed point
against G1's quadratic form k^T G1 k at k = e_t + e_x (= G1_tt + 2 G1_tx + G1_xx) times Block 216's four branch constants
— does every nonzero eigenvalue equal a branch constant times that quadric value (the cone's shape visible), and the same
at (i, 1), (1, i); the cross term G1_tx isolated from the three points; (d) at the all-plus W1 control, the analogous
identities fail (the cone is a union of two quadrics with an irreducible pencil cubic per Block 217's F-3) — state exactly
how; (e) the overlap assembly at the same points: the Bloch fold's parameter dependence at (i, 1), (1, i), (i, i) (217 found
it parameter-free at (i, 1, 1)); (f) if the (4,4) bench's Bloch points do not include a mixed fine point, say so first and
use the smallest bench that does (Block 213's bench_momenta for the extent; measure).
Quantifiers/domain | one witness and one control; the numeric line point; both assemblies and readings; exact
QQ(sqrt 6)/QQ(sqrt 6, i); the baseline under 600 s (time every charpoly; the (4,4) bench is 16 sites × 8 = 128 x 128 —
use the Bloch blocks (8 x 8 per momentum) for everything and the direct 128 x 128 charpoly only if it fits, else record it
as a could-not and rely on the Bloch union at the declared momenta with Block 213's smaller-extent direct check as the
consistency gate). Allowed premises | the four axioms and primitives (registry check; none used as content); Blocks 213
(bench machinery, bench_momenta, bloch_matrix, bench_matrix), 214 (principal_part, raising_matrix), 216 (formal, curve_moduli,
BRANCH_TABLE, metric_candidates through 213), 217 (alg_charpoly, symbol_matrix, bench_charpolys pattern) read through their
runners. Forbidden weakenings | floats/nsimplify; selecting an assembly, reading, cell or parameter value; any continuum,
dispersion-law or light-cone reading; asserting the covariance antecedent. Required edge cases | the zero Bloch point
(eight zeros); the pure fine points; the mixed point; the control; the overlap assembly at every point.
Completion witness | scripts/admissibility_dirac_kahler_two_direction_bench_covariant_witness_2026_09_05.py (lane format;
authority gate with the Block 217 parent artifacts content-bound by blob; gates A-I; declared literals; mutations each
flipping one family; N5 fence byte-gated; zero floats/nsimplify);
docs/ADMISSIBILITY_DIRAC_KAHLER_TWO_DIRECTION_BENCH_COVARIANT_WITNESS_BOUNDED_THEOREM_NOTE_2026-09-05.md; the cache receipt;
RESULTS_block218.md; V1-V5; N1-N8 for every negative. Outcomes that do not count | a bench multiset without the Bloch =
direct check (or its declared substitute); "the dispersion is Lorentzian"; a continuum reading.

## Value gate V1-V5 (draft; the primary answers it in writing before any PR)
V1: Block 217 REOPEN 3/4, quoted; the mainline's P3 dispersion item. V2: the first two-direction bench data at a covariant
witness and the exact mixed-point identity. Prior-art sweep at block start. V3: needs Blocks 213-217's machinery. V4: exact.
V5: not a relabel — 217 sampled one direction and found the shape invisible; this block asks whether two directions see it.
