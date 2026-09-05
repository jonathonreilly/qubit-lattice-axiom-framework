# GOAL — block 214: the duality parameters and the principal part (gravity mainline)

Selected from OPPORTUNITY_QUEUE.md (block-213 closing refresh: the new queue head). Branch
physics-loop/toe-axiom-closure-block214-duality-parameters-principal-part-20260905, stacked on
Block 213 (PR #7981). Block 213's note, runner and pack are landed in this branch history and are
the scientific parent; this block's note must be self-contained in the lane's format (Block 213's
note is the template: banner, fences, gates, N1-N8, N5 fence byte-gated, readings, N6 stop/reopen,
N7 record, review record).

## Exact target contract (proof-search governance)
Target statement | Block 211 solves the six-face system at every compatible moduli point of its
per-offset-isotropic family with EXACTLY FOUR free duality parameters D07, D16, D25, D34 (read
Block 211's note and runner for their definition and its open bounded positive-definite region —
quote its bound at scope). Block 213 proved its graded-cone theorem at the degree-diagonal
representative D07 = D16 = D25 = D34 = 0, and its refuting checker exhibited that at W1 with
D16 = 1/4 (on the variety, positive definite, inside the bound) the folded onsite H0 stops
preserving grade parity and det M becomes an irreducible quartic squared, while D07 = 1/4 leaves
the union of the two Hodge cones intact. Determine EXACTLY, on the full four-parameter cell form
at symbolic (D07, D16, D25, D34) over Block 211's family (symbolic moduli where feasible, else at
the rational witnesses W1, W2, W3, mixed, honest_face and the two QQ(sqrt 6) locus witnesses):
(a) which parameters break grade parity of the folded H0 under each assembly (onsite and overlap)
and why D07 (a grade 0 <-> 3 coupling) does not change the cone while D16, D25, D34 (grade 1 <-> 2)
do — the exact mechanism, as a lemma; (b) the characteristic polynomial det M(kappa) of the full
principal part M = H0 D + D^T H0 as a polynomial in kappa and the four parameters: its factorization
type as a function of the parameters (union of two quadrics / one quadric squared / irreducible
quartic squared / other), with the exact locus in the parameters where the factorization type
changes; (c) whether ANY point of the four-parameter positive-definite box restores a scalar
principal symbol or a single metric's cone off flat — i.e. whether the coincidence locus of Block
213 extends, shrinks or is replaced when the parameters are switched on (exact algebraic answer,
fail-closed); (d) the dispersion branches (eigenvalues of the pencil block) at one or two exact
witnesses with a parameter on — do the transverse branches remain algebraic in kappa, does a new
branch appear; (e) shear and volume registration under the parameters (do the parameters move the
cone independently of the shears; does any parameter cancel a shear's registration).
Quantifiers/domain | the (4,2,2) bench's period-2 Bloch reduction and the principal part at the
degenerate zero; Block 211's family and its four-parameter box; symbolic where the fraction-free
machinery reaches, exact rational witnesses otherwise; "restores" and "extends" are exact
polynomial statements (proportionality of quadratic forms; factorization over QQ / QQ(sqrt 6)).
Allowed premises | the four axioms and approved primitives (registry check before every wall
sentence; nothing used as content); the landed objects read through their own runners (Blocks
105, 201, 209, 211, and Block 213's runner on this branch: import it read-only for the period-2
machinery, the assemblies, metric_candidates and principal_objects; never edit it); PR #7970 at
its own conditional scope if the registration question touches it.
Forbidden weakenings | any float or nsimplify (gate I as in Block 213); reading the cone as a
light cone or the symbol as a dynamics (the word fences, inherited verbatim); selecting an
assembly, a reading, or a parameter value; claiming anything about the continuum; using Block
213's headline as a premise for a parameter-on statement (re-derive at the parameter point).
Required edge cases | D07 alone (the union survives — prove why); one of D16/D25/D34 alone; all
four on; the PD boundary of the box (Block 211's bound); the two locus witnesses with a parameter
on (does mu stay, does the cone stay one quadric); the flat cell with parameters on (is R5's
control still reproduced? if not, say exactly how the flat symbol deforms — this is the sharpest
edge case: the "flat" cell with nonzero duality parameters is not the identity).
Completion witness | scripts/admissibility_dirac_kahler_duality_parameters_principal_part_2026_09_05.py
in the lane's format (authority gate with the five pins re-resolved live and the Block 213 parent
artifacts content-bound by blob; banner/fence gate; construction fidelity to Block 213's objects;
the control; the lemmas at symbolic parameters; the witnesses; registration; scope fences; note
present with the N5 fence byte-identical; nsimplify/float counts zero) with declared mutations
each flipping exactly one family; the note
docs/ADMISSIBILITY_DIRAC_KAHLER_DUALITY_PARAMETERS_PRINCIPAL_PART_BOUNDED_THEOREM_NOTE_2026-09-05.md
in Block 213's format with the physics-loop machine-status fields; the cache receipt via
runner_cache.execute_and_write_cache; RESULTS_block214.md; V1-V5 in REVIEW_HISTORY.md.
Outcomes that do not count | "plausibly"; a parameter scan without the exact locus of the
factorization change; a claim at the degree-diagonal slice restated; a selection of a parameter
value; a continuum reading.

## Value gate V1-V5 (draft; the primary answers it in writing before any PR)
V1: Block 213's REOPEN item 7 and its scope restriction (CK-01) — the theorem's domain is the
question. V2: the parity-breaking lemma with its mechanism, the factorization-type locus in the
four parameters, the fate of the coincidence locus, the flat-cell deformation. V3: needs the
chain's objects (Block 211's duality parameters, Block 213's principal-part machinery) and exact
symbolic algebra. V4: no fit, float, literature constant or continuum equation is load-bearing.
V5: not a relabelling — Block 213 proved nothing off the degree-diagonal slice; this block is the
first statement on the four-parameter box. Prior-art sweep against the refreshed origin/main is
mandatory at block start.
