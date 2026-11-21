lead: openai/gpt-6-astra/max mac-mini-codex
lease_until: 2026-11-02T04:00Z

## State of attack

*Lead note, 2026-11-01 (Opus 5.5, not independent, not an audit).* Launched as `codex exec -m gpt-6-astra` at reasoning effort max on the Mac mini: 12:08Z finish, 38,788 output tokens. The lead read the library proof once and found no error, and compared the mismatch with `quiet-boundary-rarity.md` lines 47, 81, 189; it reads as stated. The proof has had no independent check; queue item 8a asks for one.

Honest stop at pinned commit `c72caef9ea6ca9431d7a529104500fd69aae806d`.
Item 8, mapped side only. **The multiplicative fill in the literal (F2)
statement is discharged by the author proof in
`../library/fill-cubical-extension.md`; (F2) as Lemma OW consumes it
remains gap.** The centre-sheet attack gives an exact sharp transverse
area bound and does not refute the widened fill.

The new proof replaces compactness by a quantitative boundary gauge and
an explicit cubical connection. It proves the interpolation and restriction
steps, including equality of boundary links, with an absolute constant.
Its output multiplies the input threshold. Lemma OW instead needs the
same threshold T_2 on both sides; the exact missing inequality is (EXT=)
below. Frozen-brick preservation is an implication under the explicit
discrete alignment and bond requirements (FG); these are not silently
inferred from a continuum picture of bricks.

Next useful task, if resumed: prove or refute (EXT=), or change the
consumer's rough-set/threshold bookkeeping with its losses proved again.
No compactness theorem needs to be imported to obtain the multiplicative
fill already proved here. No claim is made that (EXT=) is false.

This is author research, not an audit or independent review. No numerical
experiment has been run. Only this part, new library notes, and `checks/fill/`
may be written. No other attempt is read.

## Frozen target

At the pinned source, `library/quiet-boundary-rarity.md:47` asks: given a
level-l SU(2) lattice field V with plaquette flux at most T off X, find
V^fl equal to V off tube(X), with flux at most C_a T everywhere, C_a
absolute. The tube has width at least a fixed multiple of T^(-1/2), and
the proposed grid scale is R_1 with T R_1^2 = K_1, K_1 fixed.
Its compactness and lattice interpolation steps are explicitly unproved.

Theorem Z at lines 81–87 instead defines X using threshold T_2 and asks
for a reference of flux at most T_2. The relation between this use and the
T-to-C_a T statement must be checked, not silently assumed.

## First attack: the long centre sheet

**Discharged (necessary condition only).** For any rectangular lattice disk
D with N plaquettes, write its boundary holonomy as an ordered product of
conjugated plaquette holonomies by successively removing rows and then
plaquettes. Bi-invariance of the SU(2) distance and its triangle inequality
give d(1, Hol(boundary D)) <= sum_D theta_p. Thus boundary holonomy -1
forces pi <= N sup_D theta_p, in any non-abelian fill. In particular a
square of side 2r requires 4 r^2 C_a T >= pi. Length of the sheet in the
other two coordinates does not enter.

The constant-flux cap on an n by n disk is explicit: for
H = diag(i,-i), set U_1(x,y)=1 and
U_2(x,y)=exp(H theta x/n^2), theta in [0,pi]. Every plaquette is
exp(H theta/n^2), the boundary holonomy is exp(H theta), and the
maximum angle is exactly theta/n^2. Extend unchanged in the other two
coordinates, with U_3=U_4=1; all mixed plaquettes are trivial. Boundary
links with the same total holonomy are vertex-gauge equivalent on the
boundary cycle: solve for the gauge successively, whose closing condition
is precisely equality of the two holonomies. Extend that vertex gauge
arbitrarily to the interior. Hence the area condition is sharp for this
product sheet. This does not prove a fill for a sheet with varying data.

No numerical result is claimed for this argument.

## What the new fill proves

**Discharged.** In `../library/fill-cubical-extension.md`, Lemmas E and G
give a gauge on the boundary of every 3- or 4-dimensional rectangular
lattice cell with side lengths in [n,2n]: boundary flux K/n^2 implies
boundary link angles G(K)/n, where G is explicit and independent of n.
The only maps extended continuously have domain boundary dimension at
most two. A covering-volume argument on SU(2)=S^3 supplies an omitted
point with a uniform distance; stereographic projection then gives an
explicit extension. There is no appeal to compactness of connections.

**Discharged.** Lemma C constructs a tangential cubical 1-form with the
specified edge transports exactly. Its curvature estimate is proved by
differentiating the interpolant, cutting it off radially, and deriving
the holonomy-area inequality from the transport ODE. The boundary gauge
is undone at lattice vertices only; no degree-sensitive smooth gauge
extension is assumed. This addresses a boundary whose continuum gauge
class changes, as well as a centre vortex.

**Discharged.** Theorem S fills a complex successively in dimensions
2, 3, 4, with all previously fixed links preserved. There are three
stages, not one step per component or unit of length. F2-mult then gives

    max_p theta_p(V^fl) <= C_a t,
    V^fl = V outside tube(X),                 theta(V)<=t off X,

with K_0=16pi, n=ceil(sqrt(K_0/t)), d_x>=32n and
C_a=C_*(4K_0)/K_0. Equations (5)–(7), (12) of the library note give
explicit, very loose formulas for C_*. All constants depend only on
dimension four, SU(2), and the fixed numerical K_0. In particular C_a
is free of x, L, level, depth, volume, and the boundary's topology.
The support has at most 2^16 n^4 |X| fine cells. No energy improvement,
same-parent constraint, or multilevel stability is inferred from this.

**Implication, exactly conditional on (FG).** If the frozen whole bricks
are closed unions of cells of the integer rectangular mesh, all frozen
bonds are contained in these bricks, and the brick pattern is compatible
with the domain/periodicity, then their regular data are preserved. The
mesh exists for the literal integer-wall version of Lemma BG when
t_0>=8n: its walls lie on (t_0/8)Z, whose intervals can be subdivided
into integer lengths in [n,2n]. The construction preserves every regular
coarse cell, independently of which are frozen. Thus the reference can
be a Borel function of the level field alone, for fixed mesh geometry.
The proof does not identify the set of crossing bonds in the draft's
site-centered block convention with (FG); that identification remains
**unchecked**. Arbitrary frozen bonds are not covered by a room estimate
alone.

## The consumer gap: exactly which inequality is missing

**Gap (EXT=).** At `quiet-boundary-rarity.md:189`, Lemma OW defines
X_i by flux >T_2 and asks for V_i^# class, meaning flux <=T_2 by that
file's Setting, equal to V_i off tube(X_i). Theorem Z at lines 81–85
asks for that same reference. It is used again for W_B^# in Step 4,
before invoking the class-only value bound. For an allowed level field
V, let

    X_2(V) = { cells with flux(V)>T_2 },
    B_fix = bonds outside tube(X_2(V)) together with frozen bonds,
    m(V,B_fix) = min_{W : W|B_fix=V|B_fix} max_p theta_p(W).

For a finite lattice the minimum exists: the unfrozen link space is a
finite product of S^3, a minimizing sequence has a convergent subsequence
by successive extraction in its finitely many coordinates, and the
plaquette angles and their finite maximum are continuous. This elementary
compactness proves existence of the minimum only. The missing uniform
estimate is

    (EXT=)    m(V,B_fix) <= T_2

for every allowed V, level, finite volume and quiet boundary datum, on
the *specified* tube at the draft's allowed constants. No volume-, depth-,
or L-dependent enlargement of the class threshold is permitted.

The theorem proved here instead gives, when its prescribed-cell geometry
holds,

    m(V,B_fix) <= C_a T_2.                                     (EXTx)

Applying the original (F2) with t=T is invalid here: outside X_2 one
only knows flux <=T_2=C_p C_a T, not <=T. Applying it with t=T_2
gives (EXTx), which does not put the reference in the class used by
Step 4. The explicit constant of this construction is larger than one;
no claim that a different construction must lose a constant is made.

Two possible repairs are **gap**, not implemented: prove the
threshold-preserving extension (EXT=); or replace X_2 by a set defined
at a lower threshold and reprove every changed loss and class-top clause.
The latter is not a rename: a class field can have cells above T, so
the enlarged set need not be empty at a class top, whereas Lemma OW's
last step uses X_l empty there. Merely increasing T_2 moves both input
and output thresholds and leaves the same multiplicative mismatch.

**Implication.** If (EXT=) and the required exact frozen-bond realization
are proved, the reference-existence part of Lemma OW and Theorem Z is
available. Their inequalities still require their other named inputs:
in particular (CI-N)^d, (LNC), stability and the energy comparisons.
Those are outside this item and are not certified here.

## Relation to existing arguments and checks

`lattice-uhlenbeck.md` was read at Lemma U and its gauge-flow/growth
proof, Lemma F, and Lemma RF. Their small-energy estimates do not supply
the present bound directly: a four-dimensional cell at scale n with
flux t and t n^2=K_0 has the upper energy scale t^2 n^4=K_0^2, which
is not a small-energy hypothesis. None of these lemmas is used as a
black box in the new proof. The statement of Lemma LIFT in
`hard-core--excess.md` concerns a lift in a blocking fibre, not an
arbitrary-boundary fill; it is not used either.

Read scope: GOAL and FINISH; targeted (F2) hits in the mapped part;
the Setting, Theorem Z statement, Steps 1–4 and Lemma OW in
`quiet-boundary-rarity.md`; the stratified-fill paragraph at
`relative-density-bound.md:297`; the relevant Lemma OC flux-sheet
finding D1 at gate `theorem-z-repaired-60036ba4d.md`; the passages just
listed in `lattice-uhlenbeck.md`; the brick definition/geometry at
`fibre-propagator.md:134`; and excess summary/LIFT passages.
No independent-attempt part or gate was read. The Arnold–Awanou abstract
was consulted for method attribution only, not as a theorem source.

No numerical computation was run, so no numeric lock or numerical PASS
is claimed. The proof was reread for the boundary matching, gauge
degree, seam plaquettes, constants, and finite-volume cases. This is an
author check, **unchecked by an independent reader**. Only the two
permitted new Markdown files were written. No audit, commit, push or PR
was performed.

## Final disposition

- **Discharged:** the sharp area test for a product centre sheet; a
  quantitative cubical multiplicative fill; the exact interpolation
  and lattice restriction; uniform constants with no component or depth
  factor. This supplies the literal T-to-C_a T form of (F2).
- **Implication:** frozen-brick preservation under (FG), t_0>=8n and
  compatible periodicity; the reference can then depend on V alone.
- **Gap:** (EXT=), the same-threshold bound needed by the pinned Lemma
  OW/Theorem Z. **Unchecked:** the draft's exact frozen crossing-bond
  convention against (FG), and independent review of the new proof.

Stop here. The literal multiplicative fill has a proof; the consumer's
stronger reference requirement remains open with its exact inequality
displayed. No claim about Yang–Mills existence follows.
