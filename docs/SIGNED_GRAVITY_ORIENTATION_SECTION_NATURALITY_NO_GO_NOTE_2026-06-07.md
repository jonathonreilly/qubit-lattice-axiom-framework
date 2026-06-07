# Signed Gravity Orientation Section Naturality No-Go

**Date:** 2026-06-07
**Claim type:** no_go
**Actual current-surface status:** no-go source-note proposal; independent
audit required before any effective retained_no_go status.
**Trace class:** negative_route_pruning
**Reachability to target:** prunes
**Primary runner:** [`scripts/frontier_signed_gravity_orientation_section_naturality_no_go_2026_06_07.py`](../scripts/frontier_signed_gravity_orientation_section_naturality_no_go_2026_06_07.py)
**Cached runner output:** [`logs/runner-cache/frontier_signed_gravity_orientation_section_naturality_no_go_2026_06_07.txt`](../logs/runner-cache/frontier_signed_gravity_orientation_section_naturality_no_go_2026_06_07.txt)

## Role

This note attacks the second chirality-resolution route: can the hosted
determinant/orientation line choose a canonical section by sewing, flat
transport, or gauge/relabeling naturality?

The finite answer is no.  A `Z_2` orientation line is a torsor.  Its sign-flip
automorphism has no fixed section, so an equivariant canonical section cannot be
extracted from the host alone.  Sewing and flat transport preserve both choices;
they do not rank them.

This prunes the route:

```text
determinant orientation-line host
  + sewing / flat local-system naturality
  -/-> canonical section
  -/-> active chi_eta rho Phi source
```

It does not say a source section is impossible.  It says the section is not
derived by the tested host/naturality data.

## Setup

Let the hosted orientation line have two unit sections:

```text
Sec = {+1, -1}.
```

The torsor automorphism flips the sign:

```text
tau(+1) = -1
tau(-1) = +1.
```

A canonical section derived from the host and invariant under relabeling/gauge
would have to satisfy:

```text
s = tau(s).
```

No such section exists.

## Result

The runner verifies exact finite facts:

- the sign-flip automorphism has no fixed point on `{+1,-1}`;
- no constant section selector is invariant under the torsor automorphism;
- multiplicative sewing is compatible with both section choices;
- a flat three-patch local-system proxy has both `(+,+,+)` and `(-,-,-)` global
  sections, related by a global gauge flip;
- the orientation-even positive source `[+1,+1]` and desired orientation-odd
  source `[+1,-1]` require different section choices;
- the torsor host without a section supplies `[0,0]`, not an active source.

So a theorem can legitimately say the determinant package **hosts** the
orientation line, but a separate theorem is needed to **select** the section.

## Consequence For Signed Gravity

The existing
[`SIGNED_GRAVITY_NATURALLY_HOSTED_ORIENTATION_LINE_NOTE.md`](SIGNED_GRAVITY_NATURALLY_HOSTED_ORIENTATION_LINE_NOTE.md)
already draws the host-vs-section boundary.  This packet sharpens that boundary
into an equivariant naturality no-go: no functorial, gauge-invariant section can
be extracted from a free `Z_2` torsor action.

The existing
[`SIGNED_GRAVITY_RETAINED_BOUNDARY_SOURCE_PRINCIPLE_NO_GO_NOTE.md`](SIGNED_GRAVITY_RETAINED_BOUNDARY_SOURCE_PRINCIPLE_NO_GO_NOTE.md)
shows the retained APS/Wald/Gauss source basis spans only the orientation-even
positive source plus source-neutral spectators.  This packet adds the section
side: even the naturally hosted orientation line does not canonically choose the
orientation-odd source branch.

## No-Go Discipline Gate

### Alternative Route Enumeration

| Route | Attempted forcing step | Result |
|---|---|---|
| Torsor fixed point | Choose a section invariant under sign flip. | No fixed point exists. |
| Sewing | Use determinant-line multiplication under disjoint sums. | Both signs sew coherently. |
| Flat transport | Use flat local-system consistency over patches. | Both global sections exist and are gauge-related. |
| Positive magnitude | Use `|det|` / positive source magnitude. | Magnitude is orientation-even and sign-blind. |
| Desired source branch | Pick `[+1,-1]`. | This is exactly the missing section choice. |

### Wall Independence

The collapsed wall is the canonical section.  Hosting, sewing, and transport are
real structure, but all are compatible with both section choices.

### Hidden-Wall Scan

The proof uses only the finite `Z_2` torsor action, multiplication, and a
three-patch flat local-system proxy.  It does not import a physical
signed-gravity source, a hard boundary-sector axiom, a fitted sign, or an
observed target.

### Residual Matching

The residual is not whether an orientation line exists.  It is whether the
existing host/naturality data choose the section needed for the active
orientation-odd source.  This packet answers that residual negatively.

### Rhetoric Audit

"No-go" means no-go for deriving the section from the tested torsor,
sewing, and flat-transport naturality data.  A later retained theorem could
still supply a section by adding genuinely new native structure.

### Partial-Closure Path

The next route should attack an eta/spectral-flow boundary filter.  It would
need to produce an oriented boundary/index sector that is not merely a free
torsor host.

## Reprove-And-Cite Ledger

- Reproven here: no fixed point for the `Z_2` torsor sign flip; sewing and flat
  transport preserve both section choices; source vectors differ only after a
  section is chosen.
- Cited for downstream context:
  [`SIGNED_GRAVITY_NATURALLY_HOSTED_ORIENTATION_LINE_NOTE.md`](SIGNED_GRAVITY_NATURALLY_HOSTED_ORIENTATION_LINE_NOTE.md),
  [`SIGNED_GRAVITY_RETAINED_BOUNDARY_SOURCE_PRINCIPLE_NO_GO_NOTE.md`](SIGNED_GRAVITY_RETAINED_BOUNDARY_SOURCE_PRINCIPLE_NO_GO_NOTE.md),
  [`SIGNED_GRAVITY_APS_LOCKED_SOURCE_ACTION_PROPOSAL_NOTE.md`](SIGNED_GRAVITY_APS_LOCKED_SOURCE_ACTION_PROPOSAL_NOTE.md),
  [`MINIMAL_AXIOMS_2026-06-05.md`](MINIMAL_AXIOMS_2026-06-05.md).

No new axiom, no fitted input, no observed target, and no audit verdict are
introduced by this packet.
