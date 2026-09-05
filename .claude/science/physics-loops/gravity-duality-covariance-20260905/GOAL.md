# GOAL — block 215: the covariance locus of the four duality parameters (the plane-or-sum question)

Campaign `gravity-duality-covariance-20260905` (owner GO 2026-09-05T11:08Z, runtime 24h). Selected from the
block-214 closing refresh of `gravity-weighted-kernel-20260905/OPPORTUNITY_QUEUE.md` (queue head). Branch
`physics-loop/toe-axiom-closure-block215-duality-covariance-locus-20260905`, stacked on Block 214 (PR #7988;
stack #7753 -> #7981 -> #7988 -> this). Blocks 201-214 are landed in this branch history and are the
scientific parents; the note must be self-contained in the lane's format (Block 214's note is the template:
banner, word fences, gates, N1-N8, N5 fence byte-gated, readings, N6 stop/reopen, N7 record, Review record).

## The wall, quoted (Block 214 `N6`, REOPEN item 1 — verbatim)

> 1. A framework principle prefers the plane `D16 = D34 = −D25` (onsite) or `s = 0` (overlap). The cone
> would then be Block 213's union everywhere on the box, and Block 213's coincidence theorem would hold
> verbatim there.

and Block 214's banner: "**THE PLANE IS EXHIBITED AND NOT PREFERRED.** `D16 = D34 = −D25` is where the odd–odd
block of `M` vanishes identically. No premise prefers it." Block 213's `N6` names the route: "derive the
assembly from the rule's covariance (Block 201's fork uses the overlap one)". The Admissibility axiom's own
clause (`docs/MINIMAL_AXIOMS_2026-06-29.md`, verbatim): "There is one fixed nearest-neighbor admissibility
rule, covariant under lattice translations and proper cubic rotations."

## Exact target contract (proof-search governance)

Target statement | On Block 211's six-face-compatible family (all four corner-sign gauge classes, symbolic
moduli `(v0, g0, v1, g1)` on the family's ties), with the four duality parameters `D07, D16, D25, D34` free
(Block 211 `N2`: `D = [[v0, a],[a, 1/v1]] (+) [[v1 M1, X],[X^T, M2/v0]]`, `X = [[0,0,b],[0,c,0],[d,0,0]]` on
corners `(1,2,4) x (3,5,6)`, `a = D07`, `b = D16` at `(1,6)`, `c = D25` at `(2,5)`, `d = D34` at `(4,3)`),
determine EXACTLY:
(a) **THE STAR LEMMA.** Derive the Hodge-complement (star) map of the lane's cube complex in the lane's own
wedge signature (Block 209's signature as implemented by Block 213's `eta`/`lane_rules`/`raising_rules` and
Block 214's `hodge_complement_permutation`; derive the signs, never assume them) on 1-forms -> 2-forms and on
0-forms -> 3-forms, and prove: the cross-parity block of the cell form is a scalar multiple of the star on
`1 <-> 2` EXACTLY on the plane `D16 = D34 = −D25` (or exhibit the exact sign pattern the lane's star gives,
if it differs — then Block 214's plane is NOT the star line and that is the result), with `D07` the free
`0 <-> 3` star multiple. State the exact identity of loci: {union of the two Hodge cones, Block 214 `F-4`} =
{`1 <-> 2` cross block star-proportional}. Hand-check: the star must square to `±1` on each degree and
intertwine `D(κ)` with its adjoint in the flat metric (verify the identity the lane's conventions give).
(b) **THE TWISTED-COVARIANCE CENSUS.** The 24 proper cubic rotations act on the eight corners of the cell
with the lane's signs. Obtain the action either from Block 201's landed exact intertwiners (its runner,
read-only, if they act on the eight-corner cell) or by building the corner action from the geometric action
on `(t, x, y)` with the wedge signature — and in either case VERIFY it is a representation (24 distinct
matrices, closure, identity, element orders 1/2/3/4 in the counts 1/9/8/6) and that it intertwines the
raising part: `R D(κ) R^{-1} = D(R κ)` exactly. The corner-sign gauge is Block 211's congruence `D -> E D E`
(64 sign vectors). For the full group `O` and for EVERY conjugacy class of subgroups of `O` (enumerate the
classes from the group itself — the runner must compute them — not from memory), compute the
TWISTED-COVARIANCE LOCUS: the exact set of parameter values (as a variety/ideal in `(D07, D16, D25, D34)` at
symbolic moduli, per gauge class) such that for every `R` in the subgroup there is a sign vector `E_R` with
`(E_R R) H (E_R R)^T = H`. Report, per subgroup class: the locus; whether it is the plane, the origin
`D16 = D25 = D34 = 0`, everything, or something else; and — SEPARATELY and first — whether the family's
SHEARS survive (whether the locus forces `g0 = 0` and/or `g1 = 0`, i.e. whether any curved cell of the
family is covariant under that subgroup even up to gauge). Identify the minimal subgroup classes whose
covariance forces the plane, and whether the full `O` forces the plane, the flat cell, or both.
(c) **THE OVERLAP SUM.** Under the overlap assembly (`H0 = H0(0) + (s/4) P111`, Block 214 `F-3`), whether any
subgroup's covariance forces `s = 0`; what `s = 0` is exactly (grade-parity preservation of the fold; `P111`
commutes with every rotation — prove it); the exact statement.
(d) **CONTROLS.** Positivity does not select (Block 214's inherited witness `W1 + D16 = 1/4` is positive
definite off the plane — re-verify by exact leading minors); onsite grade parity is broken by every
parameter (Block 214 `F-1`), so parity preservation cannot select the plane onsite — state it as a lemma;
the flat cell (`g0 = g1 = 0`, `v0 = v1 = 1`) with parameters: its covariance loci.
(e) **THE PRINCIPLE, FENCED AS A CONDITIONAL.** The axiom clause governs the RULE; the cell form `H` is an
imposed candidate weight of the lane (the banner). Whether `H` inherits the clause is a READING (enumerate
it among the readings; gate it as not licensed; mutation `claim_covariance_inherited`). The block's theorem
is the exact conditional: IF the cell form is twisted-covariant under `G`, THEN the parameters lie on the
locus `L(G)` (and the shears on `S(G)`). The note asserts the antecedent nowhere. If the census shows that
`O`-covariance (even up to gauge) kills the shears, the note's headline must say so — the plane would then
be selected by covariance only together with flatness, and the honest statement is that dichotomy.
Quantifiers/domain | one cell form, Block 211's family on its ties, all four gauge classes, symbolic moduli
(the covariance equations are linear in the entries of `H`, so every locus is exact linear algebra over
`QQ(v0, g0, v1, g1)`, per sign choice, unioned over the 64 gauge choices); both assemblies for (c); the
`(4,2,2)` bench is NOT needed (no dispersion is computed; the kernel enters only through the star lemma).
Allowed premises | the four axioms and the approved primitives (registry check before every wall sentence;
none used as content); the landed objects read through their own runners: Block 201 (intertwiners, if on the
cell), Block 209 (corners, degree indices, wedge signature), Block 211 (the family, the ties, the gauge
congruence, `solve_pinned`/`face_system`/`branch_moduli`), Block 213 (`eta`, `lane_rules`, `raising_rules`,
`formal_family`, `hodge_complement_permutation` via Block 214), Block 214 (`cell_with_parameters`,
`principal_part`, the plane, `F-1`..`F-4`); the axiom text quoted verbatim.
Forbidden weakenings | any float or nsimplify (gate I); selecting a subgroup as "the" symmetry, an assembly,
a reading, or a parameter value; asserting that `H` inherits the axiom's covariance; using rotation matrices
from memory without the representation and intertwining checks; reading the cone as a light cone or the
symbol as a dynamics (word fences inherited verbatim); any continuum statement.
Required edge cases | the trivial subgroup (locus = everything); the `C3` about the body diagonal (cycles
`t -> x -> y`); the `C2` about a face axis and the `C2` about an edge axis (different classes); `C4` about a
face axis; the all-plus gauge class AND the three others (the loci may differ by gauge class — report each);
the flat cell; the overlap fold; the `0 <-> 3` pairing `D07` (expected free under every subgroup — prove or
refute).
Completion witness | `scripts/admissibility_dirac_kahler_duality_covariance_locus_2026_09_05.py` in the
lane's format (authority gate with the pins re-resolved live and the Block 214 parent artifacts content-bound
by blob; banner/fence gate; construction fidelity; the representation and intertwining checks; the star
lemma; the census; the overlap sum; the controls; scope fences; note present with the N5 fence
byte-identical; nsimplify/float counts zero) with declared mutations each flipping exactly one family; the
note `docs/ADMISSIBILITY_DIRAC_KAHLER_DUALITY_COVARIANCE_LOCUS_BOUNDED_THEOREM_NOTE_2026-09-05.md` in Block
214's format with the physics-loop machine-status fields; the cache receipt via
`runner_cache.execute_and_write_cache(<runner>, 600)`; `RESULTS_block215.md`; V1-V5 in `REVIEW_HISTORY.md`;
N1-N8 in the note for every negative.
Outcomes that do not count | "the plane is natural"; a symmetry argument without the exact gauge-twisted
census; a claim that the axiom selects the plane (only the conditional is claimable); a group-theory
prediction the runner does not verify; a census at one gauge class only; a census that never says what
happens to the shears.

## Value gate V1-V5 (draft; the primary answers it in writing before any PR)
V1: Block 214's REOPEN item 1, quoted above — the exact open question of the delivered block. V2: the star
lemma (the plane as the star line, with the lane's own signs), the twisted-covariance census with an exact
locus per subgroup class and per gauge class, the shear-survival statement, the overlap-sum statement, the
parity-cannot-select lemma. Prior-art sweep (recorded in ROUTE_PORTFOLIO.md at origin/main 4407b6a0e0):
nothing on origin/main or on the stack computes a covariance locus of the duality parameters; Block 201's
intertwiners exist for the rule encoding and are inputs here. V3: needs the chain's objects (Block 211's
family and gauge, Block 201's intertwiners or the lane's signature, Block 214's parameter placement); the
audit lane has no such construction. V4: exact linear algebra over `QQ(v0, g0, v1, g1)`; no fit, float,
literature constant or continuum equation. V5: not a relabel — Block 214 exhibited the plane and recorded
that no premise prefers it; this block computes, for the first time, what the axiom's named symmetry does
to the four parameters and to the curved family.
