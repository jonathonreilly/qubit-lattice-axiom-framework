# PMNS `C3` Character Holonomy Closure

**Status:** bounded - bounded or caveated result note
**Date:** 2026-04-16  
**Script:** `scripts/frontier_pmns_c3_character_holonomy_closure.py`

## Question

For the explicitly supplied forward-cycle matrix `C`, do its three character
phases give an invertible coordinate map on the supplied reduced cycle family?

## Answer

Yes.

For the supplied finite matrices, the stable-path coordinate lemma verifies
that the displayed compression equals `C`. The characters of this supplied
`C` are exactly:

- `1`
- `omega = exp(2 pi i / 3)`
- `omega^2 = exp(4 pi i / 3)`

So the supplied character phases are:

- `0`
- `2 pi / 3`
- `4 pi / 3`

## Reduced-Cycle Law

On the reduced graph-first family

`A_fwd(u,v,w) = (u + i v) E12 + w E23 + (u - i v) E31`

the corresponding character holonomies are exactly the one-angle holonomies at
those canonical phases. Their design matrix is

```text
[[ 2,  0,        1],
 [-1,  sqrt(3),  1],
 [-1, -sqrt(3),  1]]
```

and has nonzero determinant.

Therefore `(u,v,w)` are reconstructed exactly from the supplied `C3`
character-functional triple.

## Consequence

This strengthens the earlier three-flux theorem.

Before:
- a generic three-flux family was admitted and shown to close `(u,v,w)`

Now, algebraically:
- the supplied cycle matrix provides the canonical three character phases;
- the resulting `3 x 3` coordinate map is invertible on the supplied reduced
  matrix family.

## What It Does Not Claim

This still does **not** give full sole-axiom positive neutrino closure.

This note does not promote those functionals to a physical readout. The
retained carrier, Record-compatible observable map, and selection of the
matrix/coordinate values remain open.

The stable-path parent supplies only bounded coordinate algebra for a supplied
block; it does not close any of those physical bridges.

## Verification

```bash
python3 scripts/frontier_pmns_c3_character_holonomy_closure.py
```

## Audit dependency repair links

This graph-bookkeeping section records explicit dependency links named by a prior conditional audit so the audit citation graph can track them. It does not promote this note or change the audited claim scope.

- [pmns_oriented_cycle_channel_value_law_note](PMNS_ORIENTED_CYCLE_CHANNEL_VALUE_LAW_NOTE.md)
- [pmns_three_flux_holonomy_closure_note](PMNS_THREE_FLUX_HOLONOMY_CLOSURE_NOTE.md)
- [pmns_twisted_flux_transfer_holonomy_boundary_note](PMNS_TWISTED_FLUX_TRANSFER_HOLONOMY_BOUNDARY_NOTE.md)
