# The Cross-Plane Pair Density: an Epsilon-Assembled Two-Plaquette Object Whose Exact Quadratic Form Is the Campaign's Gram Pairing (Coefficient One), Whose Theta Parity Is Geometric (Exactly Odd Under Reflection at All Orders, Internally Flip-Even), and Whose Frame and Ordering Content Enter Through Connectors — the (ii'-final) Insertion Structurally Assembled (Bounded Theorem)

**Date:** 2026-07-02
**Claim type:** bounded_theorem (exact finite identities and gauge-invariance
certificates; not a terminal no-go, not a discharge of the theta admission).
**Status authority:** independent audit lane only. This note does not set an
audit verdict, edit registries, register primitives, change axioms, retire or
re-grade any Tier-A admission, or claim Strong-CP closure.
**Primary runner:**
[`scripts/theta_cross_plane_pair_density_geometric_oddness_connector_transport_2026_07_02.py`](../scripts/theta_cross_plane_pair_density_geometric_oddness_connector_transport_2026_07_02.py)
**Runner cache:**
[`logs/runner-cache/theta_cross_plane_pair_density_geometric_oddness_connector_transport_2026_07_02.txt`](../logs/runner-cache/theta_cross_plane_pair_density_geometric_oddness_connector_transport_2026_07_02.txt)

## Question

Block 8 (PR #4876, in-flight) reduced residual (ii') to its derivation half:
the theta-capable insertion must be a multi-link phase object whose abelian
reduction is the landed `e^{i theta Q}` (PR #4811) and whose content real
single-link weights provably drop. It also left an apparent puzzle: the
chiral-sign carrier at star level (`d`) is internally transpose-odd, yet
block 8 proved every single-link class-weight insertion is internally
transpose-even — so HOW is a theta-parity object built at all?

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

1. **Exact quadratic form = the campaign's pairing, coefficient one.** The
   epsilon assembly cancels all single-plane squares
   (`sum_{rho sigma} eps_{mu nu rho sigma} = 0`, exact combinatorics) AND
   the cubic terms: `D(eps) = [-sum eps tr(A_1 A_2)] eps^2 + O(eps^4)`
   (ratio gates at exactly 16.00). On dual-basis Cartan elements the trace
   pairing **equals** the block-5 Gram pairing with coefficient exactly one
   (exact rationals, parameter-free) — so the density's quadratic form IS
   the `Q_G` pairing whose value structure (thirds, center-pairing
   fractional part, integer odd support on root-valued fluxes) blocks 3/5
   derived. The `U(1)` reduction is the epsilon-paired product of plane
   fluxes — the abelian intersection-density shape of the landed 4D note.

2. **The theta parity is geometric, and exact.** The full object satisfies
   the internal flip table dagger → conj(D), bar → conj(D), transpose → D
   (so `Re D` is even under all three internal flips), while the coordinate
   reflection flips it **exactly at all orders**: every nonzero epsilon
   pair contains exactly one axis-0 plane, and flipping that plane's field
   equals swapping its orientation label, which flips the epsilon sign —
   `D_reflected = -D` identically (runner C3; the design-time expectation
   of only an `O(eps^4)`-controlled statement was superseded by this exact
   identity). **This resolves block 8's puzzle constructively: the theta
   parity is carried by the epsilon assembly (spacetime orientation), not
   by internal phases — which is exactly why single-link internal phases
   could only ever reach the center shadow.**

3. **Frame licensing via basing and connectors.** The connected pair
   `tr[P_1 L P_2 L^dag]` is invariant under arbitrary local gauge
   transformations — derived on an explicit link graph from the link
   transformation law, not assumed (runner D1). Its quadratic cross term is
   the **transported pairing** `tr(A_1 . L A_2 L^dag)` (runner D2): block
   6's frame transport appears inside the density, supplying exactly the
   relative-frame datum block 5 proved necessary and sufficient
   (diagonal-orbit data).

4. **The ordering (chain) content enters exactly with connectors.**
   Same-site pairs are cyclically ordering-free (`tr[U_1 U_2] = tr[U_2
   U_1]` exactly) while connected pairs are not (ordering asymmetry 1.74 at
   the fixed configuration), and two connectors differ by a loop insertion
   (runner D3-D4) — the block-6/8 chain data live in the connector
   structure of the same object.

**Wall state.** (ii'-final) is now structurally assembled: the insertion's
density exists as an explicit gauge-invariant multi-link object with (a)
the exact abelian/Cartan reduction onto the landed pairing, (b) exact
geometric theta parity, (c) connector-borne frame and ordering content. The
surviving content of the theta admission's gauge side is the **derivation
proper**: producing this insertion (with its theta coefficient) from the
framework surface — the admission's own defining task, now with the target
object fully specified at both the value level (blocks 3/5) and the
structural level (this note).

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

2. **Campaign chain** (landed PRs #4784/#4796/#4811; in-flight PRs
   #4832/#4858/#4869/#4875/#4876; repair PR #4864): the pairing, its value
   structure, the frame theorems, and the flip tables are those blocks'
   objects; every identity used here is earned inline by this runner. No
   landed note is consumed as a premise.

3. **Tier-A theta registry text** (docs/audit/data/tier_a_admissions.json,
   gauge side, quoted): the residual is "localized to the multi-plaquette /
   large-gauge-winding account (within the supplied per-plaquette class the
   local cross-plane F Ftilde slot is derived-absent; ...)". The density
   here is a PAIR object — outside the supplied per-plaquette class — so
   its existence is consistent with, and explains constructively, the
   registry's per-plaquette absence statement: the cross-plane slot lives
   exactly one plaquette-pair up.

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
  (i-a)       defect closure (block 3; unchanged);
  (i-b''-a')  global-sheet proof sliver (block 7; unchanged);
  (i-b''-b)   sector-level closed-surface statement (block 6; unchanged);
  (ii'-derive) the derivation proper: produce the epsilon-assembled
              cross-plane pair insertion, with theta as its coefficient,
              from the framework surface. The structural characterization
              is complete: quadratic form = the landed pairing
              (coefficient-one Cartan reduction; abelian reduction = the
              landed intersection density); parity geometric and exact;
              frame data connector-borne; ordering content located.

W_theta_bar_assembly: unchanged (in-flight PR #4768).
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
strong_cp_rp_half_cannot_forbid_cp_odd_imaginary_no_go_note_2026-05-16
forecloses only "the RP half-square identity alone cannot derive a
no-bare-theta-slot exclusion." No reflection positivity appears here; this
block constructs the slot's density rather than forbidding or forcing its
coefficient.

## What moves

| Prior state | After this note |
|---|---|
| (ii'-final) — required properties known, object unassembled | assembled: explicit gauge-invariant epsilon-paired two-plaquette density with exact reductions and parities |
| block-8 puzzle: internally-even objects vs the needed theta parity | resolved: the parity is geometric (epsilon assembly), exactly odd under reflection at all orders; internal phases were the wrong carrier, as block 8 proved |
| the landed pairing (blocks 3/5) vs a lattice density — relation | exact: the density's quadratic form IS the pairing, coefficient one on Cartan data, epsilon-paired product for U(1) |
| frame requirement (block 5) on a density | met inside the object: the connected pair's cross term is the connector-transported pairing (block 6's transport) |
| registry's per-plaquette cross-plane absence | explained constructively: the slot lives at plaquette-PAIR level, one step outside the supplied per-plaquette class |

## What remains

```text
(i-a)        defect closure (unchanged);
(i-b''-a')   global-sheet proof sliver (unchanged);
(i-b''-b)    sector-level closed-surface statement (unchanged);
(ii'-derive) derive the assembled insertion, with theta as coefficient,
             from the framework surface — the theta admission's own
             defining task, target now fully specified.
```

## Non-claims

This note does not claim:

- Strong-CP closure, theta retirement, or any change to the Tier-A registry;
- that the framework action contains the density (that is (ii'-derive));
- uniqueness of the density among discretizations sharing the quadratic
  form;
- an exact integer-sector statement for the density itself (the exact
  sector statements remain the landed cochain results; the density matches
  them at quadratic order and in the abelian reduction);
- physical C/P/T identification of internal flips;
- that records register the density or its ingredients;
- any new axiom, import, primitive, or admission.

## No-Go Discipline Gate (for the negative boundary)

**Status:** PASS as bounded scoping inside positive constructions. The only
negative content is inherited and scoped: internal flips cannot carry the
theta parity of this object class (its internal table is even on `Re D`),
sharpening — not contradicting — block 8's single-link no-go by locating
the parity geometrically.

### N1 — Alternative-route enumeration

| Route to the theta-parity density | Standing here |
|---|---|
| internal phases on single-link weights | EXCLUDED (block 8) — reads only the center shadow |
| internally-odd multi-link invariants (chain d) as the direct density | star-algebra shadow; the geometric route below subsumes the requirement |
| epsilon-assembled cross-plane pair density | CONSTRUCTED: exact quadratic form, exact geometric oddness, gauge-invariant, connector-borne frame data |
| per-plaquette cross-plane slot | ABSENT in the supplied class (registry-tracked, landed result) — consistent: the slot lives at pair level |
| derivation of the density from the framework surface | OPEN — (ii'-derive), the admission's own task |
| operational primitive registration | OWNER-GOVERNANCE ROUTE, not proposed (standing direction 2 -> 0) |

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

Block 8's (ii'-final) is consumed: construction half completed here at the
density level, and the residual renamed (ii'-derive) to state exactly what
survives — the derivation from the framework surface. Blocks 3/5/6
reductions all match (intersection density; Gram pairing coefficient one;
connector transport). The registry's per-plaquette absence is matched and
constructively explained.

### N5 — Rhetoric audit

No "closes/exhausted/only-route" framing. The construction is presented
with explicit non-uniqueness over discretization variants; the derivation
task is stated as the surviving content; live paths are named.

### N6 — Partial-closure path scan

Live paths: attempt (ii'-derive) — candidate mechanisms: the framework's
multi-plaquette effective weights (block-2/4 gluing flows) generating
pair-density terms with the connector structure; sector-level assembly via
(i-b''-b); settle (i-b''-a'); (i-a); the assembly side (PR #4768).

### N7 — Steelman

A hostile reviewer can press: (1) "This is the standard clover-type
topological charge density." The shape is classical; the deliverables are
the exact finite theorem set in audit format — coefficient-one Cartan
reduction onto the campaign's own pairing, the exact all-orders reflection
oddness, the connector-transport cross term, and the resolution of the
block-8 parity puzzle — wired to the named wall decomposition. (2) "The
quadratic-order match is weak; the exact sector statements live elsewhere."
Stated explicitly: exact sector content remains with the landed cochain
results; the density is the insertion-level object matching them where it
must. (3) "Nothing here derives theta." Correct and stated — the block's
job was the target's structural assembly; (ii'-derive) is the admission's
own task. All three absorbed into scope.

### N8 — Cross-cycle echo

Cumulative guards (blocks 1-8) plus this block's additions: do not seek the
theta parity in internal flips of pair densities (it is geometric, and
exactly so); do not treat the density's quadratic-order match as an exact
sector statement; and preserve the pair-level (not per-plaquette) support
when consuming the registry's absence result. Future cycles citing this
chain must supply (i-a), (i-b''-a'), (i-b''-b), and (ii'-derive)
explicitly.

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
