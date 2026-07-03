---
claim_id: framework_bare_alpha_ratio_assumed_input_identity_support_note_2026-04-30
claim_type_author_hint: bounded_theorem
status_authority: independent_audit_lane_only
direct_effective_status_change_allowed_from_this_note: false
---

# Framework Bare Alpha Ratio Formal Assumed-Input Identity Note

**Primary runner:** scripts/frontier_framework_bare_alpha_3_alpha_em_dimension_fixed_ratio.py

**Date:** 2026-04-30
**Status:** bounded-support / formal assumed-input identity theorem. This is
not a live retained EW-normalization theorem and not a physical coupling
derivation. It preserves only exact algebraic implications under explicit
formal hypotheses.
**Trace class:** upstream_support.
**Reachability to target:** supports only bookkeeping/firewall checks for rows
that separately supply a physical EW-normalization bridge.
**Bare retained allowed:** false.
**Audit required before effective status change:** true.

---

## 0. Provenance

The source wrapper
[`FRAMEWORK_BARE_ALPHA_3_ALPHA_EM_DIMENSION_FIXED_RATIO_SUPPORT_NOTE_2026-04-25.md`](../archive_unlanded/framework-bare-alpha-assumed-input-salvage-2026-04-30/FRAMEWORK_BARE_ALPHA_3_ALPHA_EM_DIMENSION_FIXED_RATIO_SUPPORT_NOTE_2026-04-25.md)
is archived under recovery tag
`archive_unlanded/framework-bare-alpha-assumed-input-salvage-2026-04-30/`.
The audit rejected the wrapper as an authority-boundary over-claim: the
verifier itself treats the coupling inputs as assumed support-side inputs,
not as a closed minimal-input derivation.

## 1. 2026-06-08 formal-hypothesis repair

The prior source wording called this a "conditional algebra lemma", which made
the formal hypotheses look like missing retained dependencies. This repair
states the narrower theorem directly:

```text
H1: d is a positive integer dimension variable; the lattice case substitutes d=3.
H2: g_3^2 = 1.
H3: g_2^2 = 1/(d + 1).
H4: g_Y^2 = 1/(d + 2).
```

Under H1-H4, with the usual parallel inverse coupling rule

```text
1/g_em^2 = 1/g_2^2 + 1/g_Y^2,
```

one obtains

```text
1/g_em^2 = 2d + 3,
g_em^2 = 1/(2d + 3),
alpha_3(bare) / alpha_em(bare) = 2d + 3,
sin^2(theta_W)(bare) = (d + 1)/(2d + 3).
```

At `d = 3`, these specialize to

```text
alpha_3(bare) / alpha_em(bare) = 9,
sin^2(theta_W)(bare) = 4/9.
```

That is the full load-bearing theorem. H2-H4 are formal hypotheses in this
row, not physical authorities. The row does not say the framework derives
these couplings, does not say an EW-normalization lane is retained, and does
not use the `9` or `4/9` values as phenomenological predictions.

## 2. Formal theorem

The following identities are formal consequences of H1-H4:

- if `g_3^2 = 1`, `g_2^2 = 1/(d + 1)`, and `g_Y^2 = 1/(d + 2)`, then
  `1/g_em^2 = 2d + 3`;
- under the same assumptions, `g_em^2 = 1/(2d + 3)`;
- for `d = 3`, the assumed-input ratio gives
  `alpha_3(bare) / alpha_em(bare) = 9`;
- the same substitution gives the support-side bookkeeping identity
  `sin^2(theta_W)(bare) = (d + 1)/(2d + 3)`, hence `4/9` at `d = 3`.

## 3. Status boundary

```yaml
actual_current_surface_status: bounded-support
trace_class: upstream_support
reachability_to_target: supports
artifact_role: formal_identity_theorem
load_bearing_claim: "exact algebraic implications H1-H4 => alpha_3/alpha_em = 2d+3 and sin^2(theta_W) = (d+1)/(2d+3)"
formal_hypotheses_only:
  - "g_3^2 = 1"
  - "g_2^2 = 1/(d+1)"
  - "g_Y^2 = 1/(d+2)"
physical_bridge_claimed: false
proposal_allowed: false
bare_retained_allowed: false
audit_required_before_effective_retained: true
```

## 4. Boundary

This note does not derive the coupling inputs or promote the framework
bare-coupling packet. It only preserves the algebraic consequences that
follow after those formal hypotheses are assumed.

It does not assert that a retained EW-normalization lane exists, does not
promote a `Cl(3) -> SM` support packet or minimal-input stack, and does not
claim direct low-energy phenomenology from the assumed-input identity. The
values `9` and `4/9` are formal consequences inside this theorem; their
physical use remains outside this row until a separate retained bridge supplies
the coupling normalization.
