# GOAL — block 219: the three-direction bench at the covariant witness (gravity mainline)

Selected from OPPORTUNITY_QUEUE.md (block-218 closing refresh). Branch
physics-loop/toe-axiom-closure-block219-three-direction-bench-covariant-witness-20260905, stacked on Block 218.
Blocks 201-218 are landed in this branch history; Block 218's note is the format template.

## The wall, quoted
Block 218 `N6` REOPEN item 1, verbatim: "A bench sampling the `y` direction (an extent with `N_y = 4`, 64 sites) is
affordable at the witness: the six entries of `G1` would then be read off the bench and the shape seen in all three
directions." Block 218 established on (4,4,2): the raising Bloch block is i D(κ_z) with the fine momenta entering
additively, the onsite pencil block charpoly equals the charpoly of (H0^-1 M(κ_z))^2 at every point, and at L+-'s
covariant cell every nonzero eigenvalue at the three nonzero points is a Block 216 branch constant times k^T G1 k.

## Exact target contract (proof-search governance)
Target statement | On Block 213's bench_matrix at extent (4,4,4) — 64 sites, Bloch momenta (z_t, z_x, z_y) ∈ {1, i}^3
(read Block 213's bench_momenta; confirm the eight points) — at L+-'s covariant cell (mask 2, the curve moduli) with the
parameters at the star-line point (0, 1/4, -1/4, 1/4), determine EXACTLY: (a) THE BLOCH-POINT LEMMA in three
directions: d_B(z) = Σ_μ (z_μ − 1/z_μ)/2 D(e_μ) at symbolic z (Block 218's E-1, now with z_y live), the onsite
similarity H_B = Z^-1 H0 Z at all eight points, and the identity of the onsite pencil block charpoly with the charpoly
of (H0^-1 M(κ_z))^2 at all eight points, κ_z ∈ {0, e_t, e_x, e_y, e_t+e_x, e_t+e_y, e_x+e_y, e_t+e_x+e_y}; (b) THE SHAPE IN
THREE DIRECTIONS: at each of the seven nonzero points every nonzero eigenvalue is a Block 216 branch constant
{1, 128/99, 16/11 ×2} times Q(κ_z) = κ_z^T G1 κ_z with G1 = D1/D0 (declare Q at all seven points from G1 =
(3/8)[[3,-1,-1],[-1,3,-1],[-1,-1,3]]: 9/8 at the pure points, 3/2 at the doubly-mixed, 9/8 + 9/8 + 9/8 − 6/8·3 = 9/8 at the
triply-mixed? — compute, do not assume); (c) G1 READ OFF THE BENCH: the six entries from the smallest nonzero
eigenvalues at the three pure and three doubly-mixed points (G1_μν = (Q(e_μ+e_ν) − Q(e_μ) − Q(e_ν))/2), and the
triply-mixed point as the consistency check (Q(e_t+e_x+e_y) predicted from the six entries vs measured); (d) THE
RESCALINGS ON THE BENCH: at a second line multiple λ = 1/2 (check positivity: λ² < v0 v1 = 3/4) and at D07 = 1/4 with
λ = 1/4, the block multisets at the pure-t point against Block 216's rescaled constants (the line multiple rescaling
the top-form and transverse constants by 1/(1 − λ²/(v0 v1)), D07 the 0-form constant by 1/(1 − D07² v1/v0) = 128/119)
times Q — Block 216's two rescalings seen on a bench; (e) Bloch union = direct for the 64 x 64 direct charpoly over
QQ(√6) where it fits under the 600 s baseline (time one first; if it does not fit, gate the eight Bloch blocks against
Block 218's (4,4,2) identities and Block 217's (4,2,2) as the declared substitute consistency gate and record the
direct check as a could-not); (f) the all-plus W1 control at the triply-mixed point only (the rational branch reads
W1's quadric; the rest irreducible) and the overlap fold's parameter dependence at the new points (the signed sums at
(i,1,i), (1,i,i), (i,i,i) at symbolic signs, moduli and parameters).
Quantifiers/domain | one witness (one control point); the numeric line points; the onsite pencil for the shape (the
other three constructions at the witness for the identity table only); exact QQ(√6)/QQ(√6, i); the baseline under
600 s — the 8 x 8 Bloch blocks are cheap, the 64 x 64 direct charpolys are the risk. Allowed premises | the four
axioms and primitives (registry check; none used as content); Blocks 213 (bench machinery), 214 (principal_part,
raising_matrix), 216 (BRANCH_TABLE, the rescalings LINE_RESCALE / D07_RESCALE, the witness), 217 (alg_charpoly,
symbol_matrix), 218 (the (4,4,2) machinery: bench_charpolys pattern, phase_matrix, kappa_of, principal_square) read
through their runners. Forbidden weakenings | floats/nsimplify; selecting an assembly, reading, cell or parameter value;
any dispersion-law, Lorentzian, light-cone or continuum reading; asserting the covariance antecedent. Required edge
cases | the zero point (eight zeros); the three pure points (Block 218's two reproduce); the triply-mixed point; the
second line multiple's positivity checked by leading minors before use. Completion witness |
scripts/admissibility_dirac_kahler_three_direction_bench_covariant_witness_2026_09_05.py (lane format; authority gate
with the Block 218 parent artifacts content-bound by blob; gates A-I; declared literals; mutations each flipping one
family; N5 fence byte-gated; zero floats/nsimplify);
docs/ADMISSIBILITY_DIRAC_KAHLER_THREE_DIRECTION_BENCH_COVARIANT_WITNESS_BOUNDED_THEOREM_NOTE_2026-09-05.md; the cache
receipt; RESULTS_block219.md; V1-V5; N1-N8 for every negative. Outcomes that do not count | a bench multiset without
the Bloch = direct check or its declared substitute; "the dispersion is Lorentzian"; a continuum reading.

## Value gate V1-V5 (draft; the primary answers it in writing before any PR)
V1: Block 218 REOPEN 1, quoted. V2: the shape in all three directions with G1 read off the bench and one consistency
check, and Block 216's two rescalings seen on a bench. Prior-art sweep at block start. V3: Blocks 213-218's machinery.
V4: exact. V5: not a relabel — 218 read one plane and left G1's y entries and the rescalings unread on any bench.
