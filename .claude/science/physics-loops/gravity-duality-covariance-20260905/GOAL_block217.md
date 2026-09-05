# GOAL — block 217: the other assembly at the covariant cells, and the bench (gravity mainline)

Selected from OPPORTUNITY_QUEUE.md (block-216 closing refresh: the new queue head). Branch
physics-loop/toe-axiom-closure-block217-overlap-assembly-covariant-cells-20260905, stacked on Block 216.
Blocks 201-216 are landed in this branch history; Block 216's note is the format template.

## The wall, quoted
Block 216 `N6` REOPEN item 2, verbatim: "The overlap assembly is run at the 16 cells: whether its `s = 0` locus
meets covariance there the way the onsite plane does." Block 213 `N6`: "derive the assembly from the rule's
covariance (Block 201's fork uses the overlap one)". Block 215 (F-2): under the overlap fold H0 = H0(0) + (s/4) P111,
no subgroup's twisted covariance forces s = 0, and strict covariance forces s = 0 only together with a shear
relation (g0 v0 v1 + g1 = 0 at all-plus, its variants elsewhere). Block 216: at the 8 rule-A cells the onsite cell
at Block 213's curve point is strictly S3-covariant with one metric's cone on the star line.

## Exact target contract (proof-search governance)
Target statement | At the 8 rule-A star-pattern cells with Block 213's curve witnesses (L+-'s moduli where pi0 = +1,
L-+'s where pi0 = -1) and, for the controls, the all-plus W1 cell and the flat cell, determine EXACTLY:
(a) THE OVERLAP FOLD's LOCI: with the four parameters symbolic, the overlap H0 (Block 214's principal_part(cell,
"overlap")) depends on them only through s (re-measure at these cells); its union locus det M = det B^2 in s
(Block 214: s = 0 at all-plus witnesses — measure at the 8 cells); its strict stabiliser at s = 0 and at symbolic s
(does the rule-A curve satisfy the shear relation Block 215 found, g0 v0 v1 + g1 = 0 or its cell variant? compute
the relation at symbolic signs, then evaluate on the curve); its twisted stabiliser; (b) THE OVERLAP CONE at the
witnesses: det M at s = 0 and at symbolic s — is it one metric's cone, a union of two, or an irreducible quartic
squared (Block 213 found the overlap cone a non-Hodge pair "everywhere measured" — at all-plus cells; measure at
the rule-A cells); its relation to the onsite cone (proportional? the same quadric?); (c) THE BENCH: Block 213's
(4,2,2) bench spectra (form and pencil readings) at ONE covariant witness (L+-'s cell, mask 2) with (D16, D25, D34)
= (1/4, -1/4, 1/4), D07 = 0, under both assemblies — the exact charpoly multisets, Bloch union = direct bench (Block
213's E-gate machinery), and the same at the all-plus W1 control; (d) THE SMALL-k STRUCTURE: from the period-2 Bloch
reduction (Block 213/214 machinery) the principal part's cone versus the bench's lowest branch — state exactly
what the bench data say about the onsite one metric's cone (no continuum claim); (e) if the overlap fold at a
rule-A witness is strictly S3-covariant only at s = 0 together with a shear relation the curve violates, say so
as the exact negative (N1-N8): the two assemblies would then differ in covariance at the covariant cells.
Quantifiers/domain | the 8 rule-A cells at their curve witnesses; the all-plus and flat controls; symbolic
parameters (s under overlap); the (4,2,2) bench at one witness and one control; exact QQ(sqrt 6) arithmetic;
the baseline under 600 s (budget the bench: Block 213's bench charpolys at symbolic parameters are the risk — use
the numeric line point (1/4) for the bench and symbolic s only for the folded loci).
Allowed premises | the four axioms and the approved primitives (registry check; none used as content); Blocks
213 (bench machinery: bench_assembly, bloch_spectrum_charpoly, direct_bench_charpoly, multiset_of), 214
(principal_part both assemblies, ff_det, coefficient_ideal, radical_generators), 215 (the lift, constraints,
subgroup_locus), 216 (the census, the witnesses, strict_stabiliser, formal, curve_moduli), 211 (the solve,
positivity) read through their runners. Forbidden weakenings | floats/nsimplify; selecting an assembly, a cell, a
reading or a parameter value; asserting the covariance antecedent; any continuum, light-cone or dynamics reading.
Required edge cases | both mixed classes among the rule-A cells; the all-plus control (Block 213's overlap
statements were made there); the flat cell (both assemblies coincide with H = I at zero parameters — Block 213 D-1);
s symbolic AND s = 0; both readings on the bench. Completion witness |
scripts/admissibility_dirac_kahler_overlap_assembly_covariant_cells_2026_09_05.py (lane format; authority gate
with the Block 216 parent artifacts content-bound by blob; gates A-I; declared literals; mutations each flipping
one family; N5 fence byte-gated; zero floats/nsimplify);
docs/ADMISSIBILITY_DIRAC_KAHLER_OVERLAP_ASSEMBLY_COVARIANT_CELLS_BOUNDED_THEOREM_NOTE_2026-09-05.md; the cache
receipt; RESULTS_block217.md; V1-V5 in REVIEW_HISTORY.md; N1-N8 for every negative. Outcomes that do not count |
"the assembly is decided"; a bench multiset without the Bloch = direct check; a continuum reading of the bench.

## Value gate V1-V5 (draft; the primary answers it in writing before any PR)
V1: Block 216 REOPEN 2 and Block 213's named assembly-from-covariance route, quoted above. V2: the overlap side of
the covariant cells (loci, stabilisers, cone) and the first bench data on a covariant curved cell. Prior-art sweep at
block start. V3: needs the chain's objects. V4: exact. V5: not a relabel — Block 216 measured the onsite assembly
only and no bench; Block 213's overlap statements were at all-plus cells only.
