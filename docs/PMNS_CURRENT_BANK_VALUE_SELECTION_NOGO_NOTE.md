# PMNS Current Bank Value-Selection No-Go

**Status:** bounded - bounded or caveated result note
**Date:** 2026-04-16  
**Script:** `scripts/frontier_pmns_current_bank_value_selection_nogo.py`

## Question
Does the current exact bank contain a positive value-selection law for the
retained PMNS lane?

## Answer
No.

The current exact bank now closes the retained PMNS lane negatively:

- the sole axiom `Cl(3)` on `Z^3` gives only the trivial free lower-level
  response profiles on the retained lepton triplets
- the retained scalar deformation routes stay diagonal/scalar and are rejected
  by the one-sided PMNS closure stack
- graph-first residual symmetry restricts an explicitly supplied candidate
  block to a reduced oriented forward-cycle family
- a bounded algebraic lemma extracts cycle coordinates from a supplied block
- target-constructed response fixtures round-trip supplied reduced blocks as
  consistency checks only

Therefore the current exact bank does **not** contain a positive
value-selection law on that reduced channel.

## Exact Content

Let

\[
A_{\mathrm{fwd}}(u,v,w)
= (u + i v) E_{12} + w E_{23} + (u - i v) E_{31}.
\]

The current exact bank proves:

1. The sole axiom gives only the trivial free response profiles.
2. The retained local scalar routes never leave the diagonal/scalar sector.
3. On an explicitly supplied candidate block, the graph-first residual
   symmetry restricts the forward-cycle entries to the reduced `3`-real family
   above.
4. The bounded oriented-cycle coordinate lemma reads `(u,v,w)` exactly from a
   supplied block.
5. The response-profile examples are constructed from target reduced blocks
   and invert back to them; they are consistency-only.

So, after a candidate block is supplied, the current exact bank fixes:

- its reduced matrix support,
- the algebraic coordinate chart,
- and the exact residual symmetry,

but not a unique value.

These checks do not derive the physical carrier, a Record-compatible readout,
or an independent lower-level source of the reduced blocks. The stable-path
coordinate lemma must not be used as evidence for any of those bridges.

## Consequence

The current-bank value-selection attempt closes negatively at this boundary.

Any further positive value-selection law would require:

- genuinely new dynamics, or
- a further admitted extension.

It would also require separate retained carrier and physical-readout bridges.

## Verification

```bash
python3 scripts/frontier_pmns_current_bank_value_selection_nogo.py
```

## Audit dependency repair links

This graph-bookkeeping section records explicit dependency links named by a prior conditional audit so the audit citation graph can track them. It does not promote this note or change the audited claim scope.

- [pmns_lower_level_end_to_end_closure_note](PMNS_LOWER_LEVEL_END_TO_END_CLOSURE_NOTE.md)
- [pmns_oriented_cycle_channel_value_law_note](PMNS_ORIENTED_CYCLE_CHANNEL_VALUE_LAW_NOTE.md)
- [pmns_oriented_cycle_reduced_channel_nonselection_note](PMNS_ORIENTED_CYCLE_REDUCED_CHANNEL_NONSELECTION_NOTE.md)
- [pmns_uniform_scalar_deformation_boundary_note](PMNS_UNIFORM_SCALAR_DEFORMATION_BOUNDARY_NOTE.md)
