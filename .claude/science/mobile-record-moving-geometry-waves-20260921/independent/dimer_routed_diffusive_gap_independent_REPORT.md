# Independent review of the diffusive preparation comparison

2026-09-21. Bounded scientific source review, not a formal audit. No correction
or unresolved mathematical finding was identified. The displayed uniform gap,
preparation time and transfer constants reconstruct from the stated premises.
The independent derivation and controls were sealed before the author checker,
results or logs were opened. Older evidence packets remain unchanged.

The reviewed source is `DIMER_ROUTED_DIFFUSIVE_GAP_COMPARISON.md`, 7,448 bytes,
SHA-256 `1d9f7929c5600c6e097913ab2459f351857431c7f3035d4a80bc497f9d732124`.
The complete argument is independently reconstructed in
`PRE_COMPARISON_DERIVATION.md`; its source manifest identifies the unchanged
permutation Poincare, preparation-transfer and corrected moving-geometry
dependencies reused here. The precomparison seal is
`a317bd45ac244a4b4b61ce4866ee8e878193006730dcfe9a86826ab62ba1da4b`.

## Mathematical reconstruction

For even N, the one-coordinate shortest-displacement lengths sum to N^2/4
over target displacements from one start. The fixed positive half-period tie
choice is translation covariant, so each undirected cyclic edge carries N^2/4
ordered paths. A fixed coordinate-i physical edge leaves one endpoint coordinate
free in each of the other two coordinates. Thus its exact three-dimensional
load is N^4/4. This is an undirected statement; the tie choice does not imply
equal positive and negative directed loads.

The chosen lexicographically oriented black-endpoint routes form a subset of
all ordered physical paths. Projecting a route to the contracted graph and
erasing consecutive repetitions and loops cannot lengthen it or add an edge.
Each simple contracted edge has at most two physical representatives: the two
possible cross-parity connections between its dimers. Consequently, the
contracted path load is at most N^4/2, even for arbitrary irregular matchings.
The argument counts physical representatives without deduplicating the actual
routed generator.

In fact these physical paths are geodesics. Both ends of a matched edge can
occur on a geodesic only consecutively. Thus nonconsecutive projected loops do
not arise for this route family; the source's more general loop-erasure step
is harmless. Its claimed edge-preservation argument is valid independently of
that simplification.

An endpoint transposition on a simple path of length l has the forward then
reverse word of length 2l-1, with the last edge omitted in the reverse part.
It exchanges just the endpoint keys, restoring every intermediate key. Since
l<=3N/2, word length is at most 3N-1, and every path edge occurs at most twice.
The total word use of a fixed contracted edge is at most N^4. Telescoping and
Cauchy-Schwarz therefore give

    D_all <= (3N-1) N^4 D_H.

Both forms use one half times the sum of mean squared swap increments. Every
preceding word permutation preserves the uniform count-sector law, so this
comparison has no extra factor of two. Combining the already checked sufficient
permutation estimate Var<=2 D_all/K with K=N^3/2 and the actual symmetric-rate
domination D_S>=(k0/2)D_H gives

    Var <= [8N(3N-1)/k0] D_S,
    gap(S) >= k0/[8N(3N-1)].

The contraction is connected because the original torus is connected. Same-color
swaps give zero increments; singleton sectors have zero variance. The bound is
uniform in matching geometry and color counts. No sharp interchange-process
spectral theorem or typical-geometry assumption is imported.

The nonreversible forward density evolves by the stationary adjoint, whose
symmetric part has the same form. The identity
`d||f_t-1||_2^2/dt=-2D_S(f_t-1)` supplies L2 decay at the gap rate. Hence

    TV <= (1/2) sqrt(|Omega_counts|-1) exp(-g'_N t)
       <= (1/2) 14^(K/2) exp(-g'_N t).

In the inherited range 0<epsilon<1/2, the displayed waiting time is sufficient.
For epsilon_N=N^-4 its exact expanded expression is

    k0 t'_prep = (6N^5-2N^4) log14
                 + 8N(3N-1)(4 log N-log2).

The leading coefficient is therefore 6 log14/k0. The bound improves the old
sufficient schedule by the factor (K-1)/(2N); it does not identify an actual
mixing-time asymptotic.

The previous random-completion transfer continues to use multinomial color
counts independent of autonomous geometry, uniformity in the entrance
arrangement, the strong Markov property and contraction by a common subsequent
path kernel. Since the normalized squared residual is bounded by C K, its
transfer error is C K epsilon_N=C/(2N). For the separately checked moving
extension, interval semigroups contract at the common new gap and boundary
permutations are L2 isometries. Multiplication gives the same elapsed-time
estimate without a geometry-stationarity hypothesis. The comparison reference
uses the geometry at the end of preparation, as in that extension.

## Independent controls

`independent_check.py` imports no author checker. All outputs and its first-run
receipt are preserved; exit code was zero, stderr empty. Its exact inventories
cover all 262,144 ordered physical paths at N=8 and all 1,000,000 at N=10.
Every physical edge has load 1024 or 2500 respectively, including tie and
wraparound cases. These totals are 1,572,864 and 7,500,000 edge traversals.

At both sizes, independently built winding, columnar and irregular matchings
were used. Every unordered black-endpoint pair was checked, totaling 472,170
endpoint words across six matchings. Each word was applied to distinct keys;
all intermediate keys returned and only the endpoints exchanged. Every
edgewise physical-to-contracted charging inequality was checked, rather than
only the largest load. Multiplicity two is attained in the columnar and
irregular cases. The irregular N=8 case attains path length 12 and word length
23, testing the stated maximum 3N-1.

The maximal length-weighted word congestions are 5191, 9693 and 10167 at N=8,
and 15976, 30663 and 32539 at N=10, below the conservative respective bounds
94208 and 290000. Numerical one-marker-sector eigenvalues check both the
simple-edge comparison graph and the physical-multiplicity symmetric graph.
These spectra support the constants but do not prove the all-count-sector
result. Two separate small multicolor sectors have exact rational variance,
complete-form and nonlinear endpoint-word controls; they are permutation
tests, not replacements of the required torus by an undersized one.

Five schedule evaluations check the exact integer polynomial coefficients and
rational K epsilon_N, with the logarithmic TV substitution explicitly numerical.
There were no failed execution attempts and no counterexample within the stated
hypotheses. The all-volume conclusion comes from the reconstructed path proof,
not the finite inventories.

## Complete author-source comparison

After sealing, all 121 lines of `dimer_routed_diffusive_gap_check.py` and the
complete result/log were read. The checker is 6,217 bytes, SHA-256
`82a3e74f42de9e7aadbf22c60c6826f9cf1c2a484e049f0232c526123ea0bf95`.
Its inherited helper remains at the previously reviewed identity
`98aa5259d58a5355a2aa9283e19bad869160bd9432882d589db8bbb2e0f15921`.
The 5,925-byte result is
`5170574c969450f2d310cc8848be00a39415f6785619ed93befb2146be099693`.

The author path construction, matching projection, loop erasure and endpoint
word implement the note. The author numerical spectrum is that of the unit-rate
simple graph, correctly tested against 1/[4N(3N-1)]. Our k0=1 lower comparison
uses rate 1/2, so the factor-two spectral conversion is required and matches.
The author physical path controls at N=4 and N=6 test the standalone counting
identity, not the full N>=8 model; the contracted controls use N=8 and N=10.
The result expressly separates exact combinatorics from numerical spectra.

`compare_author.py` authenticates all four saved source bindings, all seven
precomparison artifacts and seven reused dependencies. The log's six geometry
rows equal the corresponding result rows, with empty stderr. For the four
winding/columnar cases shared with our independently built fixtures, path and
word maxima agree exactly and the correctly scaled numerical gaps agree. The
irregular fixtures deliberately differ; their individual saved bounds are
checked without claiming identical realizations.

All six saved schedules were recomputed at 80-digit precision from the expanded
formula with k0=11/10. Relative waiting-time discrepancies are below 2.1e-16;
gap discrepancies are below 1.2e-16. The old/new improvement factors agree
exactly. Author scientific computations were not rerun merely to duplicate
counts. Authentication and saved-witness arithmetic are recorded separately
from the precomparison independent calculations.

## Reproduction and limits

The runnable files are `independent_check.py` and `compare_author.py`; use a
reproduction copy to preserve sealed outputs. Their full stdout, stderr and
receipts are included. `PRE_COMPARISON_DERIVATION.md` contains the longer proof
reconstruction, and `FINAL_SEAL.json` binds every artifact, current source,
reused dependency and author evidence identity.

The original complete-permutation and preparation proofs were reused at their
authenticated identities, not reproved by unrelated enumeration. The optional
moving extension likewise retains its separately checked hypotheses. This is
an explicit sufficient preparation bound for the supplied classical torus
process: no arbitrary-graph diffusive gap, sharp mixing time, total empty-start
completion-time bound, physical time calibration, quantum preparation or
thermodynamic phase statement follows. Dynamic aggregates and the new
finite-wavelength follow-up remained unopened. No primary source was edited and no
formal audit status is assigned.
