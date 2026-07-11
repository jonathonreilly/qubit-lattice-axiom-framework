# The Cross-Plane Pair Density: an Epsilon-Assembled Two-Plaquette Object Whose Exact Quadratic Form Is a Coefficient-One Cartan Gram Pairing, Whose Theta Parity Is Geometric (Exactly Odd Under Reflection at All Orders, Internally Flip-Even), and Whose Frame and Ordering Content Enter Through Connectors — the (ii'-final) Insertion Structurally Assembled (Bounded Theorem)

**Date:** 2026-07-02
**Type:** bounded_theorem
**Claim type:** bounded_theorem (exact finite identities and gauge-invariance
certificates; not a terminal no-go and not a change to the theta retirement
record).
**Status authority:** independent audit lane only. This note does not set an
audit verdict, edit registries, register primitives, change axioms, retire or
re-grade any Tier-A admission, or claim Strong-CP closure.
**Current-main posture (2026-07-07):** theta is already retired from live
Tier-A by retained derivation. This note banks a historical bounded support
calculation for the theta-side cross-plane density campaign; it does not
reopen, modify, or re-grade the theta retirement record or
`premise_decision_history.json`.
**Primary runner:**
[`scripts/theta_cross_plane_pair_density_geometric_oddness_connector_transport_2026_07_02.py`](../scripts/theta_cross_plane_pair_density_geometric_oddness_connector_transport_2026_07_02.py)
**Runner cache:**
[`logs/runner-cache/theta_cross_plane_pair_density_geometric_oddness_connector_transport_2026_07_02.txt`](../logs/runner-cache/theta_cross_plane_pair_density_geometric_oddness_connector_transport_2026_07_02.txt)

## Question

The current theta residual asks for an insertion-level object with the
cross-plane `F u F` shape, geometric oddness, and connector-borne relative
frame data. In wall-decomposition language, this is the structural half of (ii'):
before deriving a theta coefficient from the framework surface, the target
density itself must be specified. The apparent puzzle is that internal
phase flips are the wrong carrier for this parity; the construction below
keeps the oddness in the epsilon assembly rather than in a single-link
internal phase.

Question answered here: assemble the insertion's density explicitly and
locate where each required property lives.

## Answer

The object is the **epsilon-assembled cross-plane pair density**

```text
D(x) = sum_{mu nu rho sigma} eps_{mu nu rho sigma}
       tr[ U_{mu nu}(x) . L . U_{rho sigma}(x') . L^dag ]
```

(two plaquettes in complementary planes, joined by a connector `L`; the
same-site case has `L = 1`). Four exact results (runner 12/12; every gate
deterministic; convergence-ratio gates discriminate):

1. **Exact quadratic form = a coefficient-one Cartan pairing.** The
   epsilon assembly cancels all single-plane squares
   (`sum_{rho sigma} eps_{mu nu rho sigma} = 0`, exact combinatorics) AND
   the cubic terms: `D(eps) = [-sum eps tr(A_1 A_2)] eps^2 + O(eps^4)`
   (ratio gates at exactly 16.00). On dual-basis Cartan elements the trace
   pairing equals the same two-generator Cartan Gram form with coefficient
   exactly one (exact rationals, parameter-free). The `U(1)` reduction is
   the epsilon-paired product of plane fluxes, matching the abelian
   intersection-density shape in
   [`THETA_4D_CARRIER_FLUX_COHOMOLOGY_INTERSECTION_PAIRING_CLOSED_BRANCH_AND_DEFECT_CLOSURE_RESIDUAL_BOUNDED_THEOREM_NOTE_2026-07-02.md`](THETA_4D_CARRIER_FLUX_COHOMOLOGY_INTERSECTION_PAIRING_CLOSED_BRANCH_AND_DEFECT_CLOSURE_RESIDUAL_BOUNDED_THEOREM_NOTE_2026-07-02.md).

2. **The theta parity is geometric, and exact.** The full object satisfies
   the internal flip table dagger → conj(D), bar → conj(D), transpose → D
   (so `Re D` is even under all three internal flips), while the coordinate
   reflection flips it **exactly at all orders**: every nonzero epsilon
   pair contains exactly one axis-0 plane, and flipping that plane's field
   equals swapping its orientation label, which flips the epsilon sign —
   `D_reflected = -D` identically (runner C3; the design-time expectation
   of only an `O(eps^4)`-controlled statement was superseded by this exact
   identity). **This resolves the parity-carrier puzzle constructively:
   the theta parity is carried by the epsilon assembly (spacetime
   orientation), not by internal phases.**

3. **Frame licensing via basing and connectors.** The connected pair
   `tr[P_1 L P_2 L^dag]` is invariant under arbitrary local gauge
   transformations — derived on an explicit link graph from the link
   transformation law, not assumed (runner D1). Its quadratic cross term is
   the **transported pairing** `tr(A_1 . L A_2 L^dag)` (runner D2):
   relative-frame data enter inside the density through the connector.

4. **The ordering (chain) content enters exactly with connectors.**
   Same-site pairs are cyclically ordering-free (`tr[U_1 U_2] = tr[U_2
   U_1]` exactly) while connected pairs are not (ordering asymmetry 1.74 at
   the fixed configuration), and two connectors differ by a loop insertion
   (runner D3-D4) — ordering data live in the connector structure of the
   same object.

**Historical wall state.** (ii'-final) is now structurally assembled: the insertion's
density exists as an explicit gauge-invariant multi-link object with (a) a
coefficient-one Cartan quadratic form and `U(1)` reduction matching the
linked carrier/intersection comparison surface, (b) exact geometric theta
parity, and (c) connector-borne frame and ordering content. The surviving
content of the historical theta-side gauge task is the **derivation
proper**: producing this insertion (with its theta coefficient) from the
framework surface. The exact identities T1-T4 are proved inline by this
note's runner.

## Source surface (named authorities)

1. **Record axiom, current clauses used** (approved axiom node
   `minimal_axioms`,
   [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md); memo
   under active clarification — sentences quoted from the current tip):

   > "Only records are readable. A readout value is determined by record
   > content alone."

   Used as licensing discipline (the density is gauge-invariant and its
   frame data are connector-borne, i.e. configurational); record occurrence
   is not claimed.

2. **4D carrier/intersection comparison surface** (bounded theorem note,
   audit-lane authority remains independent):
   [`THETA_4D_CARRIER_FLUX_COHOMOLOGY_INTERSECTION_PAIRING_CLOSED_BRANCH_AND_DEFECT_CLOSURE_RESIDUAL_BOUNDED_THEOREM_NOTE_2026-07-02.md`](THETA_4D_CARRIER_FLUX_COHOMOLOGY_INTERSECTION_PAIRING_CLOSED_BRANCH_AND_DEFECT_CLOSURE_RESIDUAL_BOUNDED_THEOREM_NOTE_2026-07-02.md).
   Used only to name the abelian intersection-density comparison. The
   coefficient-one Cartan/Gram check, parity checks, gauge-invariance
   check, and connector-ordering checks are earned inline by this runner.

3. **Wall chronology labels:** references to prior wall labels below are
   context labels for the decomposition, not load-bearing dependencies on
   open sibling PRs.

4. **Retired theta registry text**
   ([`docs/audit/data/premise_decision_history.json`](audit/data/premise_decision_history.json),
   historical gauge-side context, quoted from the retired entry): the
   residual was "localized to the multi-plaquette / large-gauge-winding
   account (within the supplied per-plaquette class the local cross-plane F
   Ftilde slot is derived-absent; ...)". The density here is a PAIR object
   — outside the supplied per-plaquette class — so its existence is
   consistent with the retired entry's per-plaquette absence statement: the
   cross-plane slot lives exactly one plaquette-pair up. The retired
   registry text is context only, not a proof premise.

No external comparator, measured value, fitted number, Monte Carlo, or
continuum input enters anywhere.

## Theorem statements

**T1 (assembly and quadratic form; runner A1-A3, B1-B2).** Single-plane
cancellation is exact; `D(eps)` equals its cross-plane-pairing quadratic
form with `O(eps^4)` remainder (ratio 16.00 gates); `D` is real; the Cartan
reduction equals the Gram pairing with coefficient one; the `U(1)`
reduction is the epsilon-paired flux product.

**T2 (parities; runner C1-C3).** Internal flips: dagger and bar conjugate
`D`, transpose fixes it. Geometric reflection: `D_reflected = -D` exactly
at all orders (orientation-label argument displayed in the runner).

**T3 (gauge invariance and transport; runner D1-D2).** The connected pair
is gauge-invariant by the link transformation law on an explicit graph; its
quadratic cross term is the connector-transported pairing.

**T4 (ordering content; runner D3-D4).** Connector path-dependence is a
loop insertion; ordering asymmetry exists exactly for connected (not
same-site) pairs.

## Corollary (wall state)

```text
W_theta_Q_context (current decomposition):
  (i-a)       defect closure (unchanged);
  (i-b''-a')  global-sheet proof sliver (unchanged);
  (i-b''-b)   sector-level closed-surface statement (unchanged);
  (ii'-derive) the derivation proper: produce the epsilon-assembled
              cross-plane pair insertion, with theta as its coefficient,
              from the framework surface. The structural characterization
              is complete: coefficient-one Cartan quadratic form;
              abelian reduction matches the linked intersection-density
              comparison surface; parity geometric and exact;
              frame data connector-borne; ordering content located.

W_theta_bar_assembly: unchanged by this note.
```

## Identification checkpoint (what objects these are)

The density is a construction in the gluing calculus: no claim is made that
the framework action contains it (that is (ii'-derive)), that records
register it, that the fixed fields/staples model the physical sector, or
that the internal flips are physical C/P/T (the geometric reflection is a
lattice coordinate reflection; physical naming is downstream). The
same-site and connected versions are presented as the minimal and the
frame-complete members of one family; no uniqueness claim is made over
discretization variants (e.g. clover averaging), whose quadratic forms
coincide by T1's mechanism.

## Relation to the RP-half no-go (route independence)

The retained no-go row
[`STRONG_CP_RP_HALF_CANNOT_FORBID_CP_ODD_IMAGINARY_NO_GO_NOTE_2026-05-16.md`](STRONG_CP_RP_HALF_CANNOT_FORBID_CP_ODD_IMAGINARY_NO_GO_NOTE_2026-05-16.md)
forecloses only "the RP half-square identity alone cannot derive a
no-bare-theta-slot exclusion." No reflection positivity appears here; this
block constructs the slot's density rather than forbidding or forcing its
coefficient.

## What moves

| Prior state | After this note |
|---|---|
| (ii'-final) — required properties known, object unassembled | assembled: explicit gauge-invariant epsilon-paired two-plaquette density with exact reductions and parities |
| parity-carrier puzzle: internally-even objects vs the needed theta parity | resolved for this density: the parity is geometric (epsilon assembly), exactly odd under reflection at all orders |
| linked intersection-density comparison vs a lattice density | matched in the `U(1)` reduction; the Cartan quadratic form is coefficient one |
| relative-frame requirement on a density | met inside the object: the connected pair's cross term is the connector-transported pairing |
| registry's per-plaquette cross-plane absence | explained constructively: the slot lives at plaquette-PAIR level, one step outside the supplied per-plaquette class |

## What remains

```text
(i-a)        defect closure (unchanged);
(i-b''-a')   global-sheet proof sliver (unchanged);
(i-b''-b)    sector-level closed-surface statement (unchanged);
(ii'-derive) derive the assembled insertion, with theta as coefficient,
             from the framework surface — the historical theta-side
             target now fully specified.
```

## Non-claims

This note does not claim:

- Strong-CP closure, theta retirement, or any change to the Tier-A registry;
- that the framework action contains the density (that is (ii'-derive));
- uniqueness of the density among discretizations sharing the quadratic
  form;
- an exact integer-sector statement for the density itself (the exact
  sector statements remain with the linked carrier/intersection cochain
  surface; the density matches them at quadratic order and in the abelian
  reduction);
- physical C/P/T identification of internal flips;
- that records register the density or its ingredients;
- any new axiom, import, primitive, or admission.

## No-Go Discipline Gate (for the negative boundary)

**Status:** PASS as bounded scoping inside positive constructions. The only
negative content is local and scoped: internal flips do not carry the theta
parity of this object class (its internal table is even on `Re D`), because
the parity is located geometrically.

### N1 — Alternative-route enumeration

| Route to the theta-parity density | Standing here |
|---|---|
| internal phases on single-link weights | not used here; this construction carries oddness geometrically |
| internally-odd multi-link invariants (chain d) as the direct density | star-algebra shadow; the geometric route below subsumes the requirement |
| epsilon-assembled cross-plane pair density | CONSTRUCTED: exact quadratic form, exact geometric oddness, gauge-invariant, connector-borne frame data |
| per-plaquette cross-plane slot | ABSENT in the supplied class (registry-tracked statement) — consistent: the slot lives at pair level |
| derivation of the density from the framework surface | OPEN in this historical support surface — (ii'-derive), the theta-side target |
| operational primitive registration | APPROVED-PRIMITIVE PROPOSAL, not proposed (standing direction 2 -> 0) |

### N2 — Wall-independence audit

Nothing here binds the mass side or `W_theta_bar_assembly`. The
construction makes no claim about the framework action; it supplies the
target object for (ii'-derive) and does not prejudge whether the derivation
succeeds, fails, or lands on a variant discretization with the same
quadratic form.

### N3 — Hidden-wall scan

Every gate is displayed: exact combinatorics (A1), discriminating ratio
gates (A2, B2, D2 — a wrong form plateaus), exact rational Cartan algebra
(B1), full-object identities (C1-C3), and link-law-derived gauge invariance
(D1). The reflection identity's proof sketch (orientation-label swap) is in
the runner comment; the design-time weaker expectation and its supersession
are documented. No normalization is fitted anywhere (the Cartan coefficient
is exactly one).

### N4 — Residual matching

The (ii') structural target is specified at the density level, and the
residual is named (ii'-derive) to state exactly what survives — the
derivation from the framework surface. The linked carrier/intersection
comparison surface is matched in the `U(1)` reduction, while the
coefficient-one Cartan form and connector transport are checked inline. The
registry's per-plaquette absence is respected by keeping the object at
plaquette-pair level.

### N5 — Rhetoric audit

No "closes/exhausted/only-route" framing. The construction is presented
with explicit non-uniqueness over discretization variants; the derivation
task is stated as the surviving content; live paths are named.

### N6 — Partial-closure path scan

Live paths: attempt (ii'-derive) — candidate mechanisms include the
framework's multi-plaquette effective weights generating pair-density terms
with the connector structure; sector-level assembly via (i-b''-b); settle
(i-b''-a'); (i-a); and the separate theta-bar assembly side.

### N7 — Steelman

A hostile reviewer can press: (1) "This is the standard clover-type
topological charge density." The shape is classical; the deliverables are
the exact finite theorem set in audit format — coefficient-one Cartan
reduction, the `U(1)` match to the linked carrier/intersection comparison
surface, the exact all-orders reflection oddness, the connector-transport
cross term, and the resolution of the parity-carrier puzzle — wired to the
named wall decomposition. (2) "The
quadratic-order match is weak; the exact sector statements live elsewhere."
Stated explicitly: exact sector content remains with the linked
carrier/intersection cochain surface; the density is the insertion-level
object matching it where it must. (3) "Nothing here derives theta." Correct
and stated — this note's job was the target's structural assembly;
(ii'-derive) is the historical theta-side target. All three absorbed into
scope.

### N8 — Cross-cycle echo

Cumulative guard added here: do not seek the theta parity in internal flips
of pair densities (it is geometric, and exactly so); do not treat the
density's quadratic-order match as an exact sector statement; and preserve
the pair-level (not per-plaquette) support when consuming the registry's
absence result. Future cycles citing this chain must supply (i-a),
(i-b''-a'), (i-b''-b), and (ii'-derive) explicitly.

## Verification

Run:

```bash
python3 scripts/theta_cross_plane_pair_density_geometric_oddness_connector_transport_2026_07_02.py
```

Expected close:

```text
TOTAL: PASS=12 FAIL=0
```

Sections: A assembly ground (epsilon cancellation; ratio-gated quadratic
form with O(eps^4) remainder; reality); B reductions (coefficient-one
Cartan/Gram; U(1) epsilon-paired flux product); C parities (internal flip
table; exact quadratic reflection flip; exact all-orders full-object
oddness); D connectors (link-law gauge invariance on an explicit graph;
transported-pairing cross term; loop-insertion path dependence; ordering
content entering exactly with connectors).
