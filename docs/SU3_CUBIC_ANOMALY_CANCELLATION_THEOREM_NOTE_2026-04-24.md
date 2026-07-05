# SU(3)^3 Cubic Gauge Anomaly Cancellation Theorem

**Date:** 2026-04-24
**Type:** positive_theorem
**Claim type:** structural-anomaly cancellation theorem (exact rational arithmetic on retained colour-charged content)
**Claim scope:** for the scoped colour-anomaly carrier in the left-handed
conjugate frame `Q_L : 3` (with weak multiplicity 2), `u_R^c : 3bar`,
`d_R^c : 3bar`, the SU(3)^3 cubic gauge-anomaly trace evaluates to
`sum_i m_i A(R_i) = +2 - 1 - 1 = 0` exactly. The local source packet now
uses the retained graph-first SU(3) carrier, the left-handed weak-fiber
`3 + 1` decomposition, the narrow one-generation anomaly-singlet completion
packet, and the narrow `A(3bar) = -1` conjugate-representation mapping
packet. Full one-generation matter closure, hypercharge uniqueness,
chirality/time selection, and branch selection remain separate downstream
or upstream problems.
**Status:** awaiting independent audit. Under the scope-aware classification framework, ratified status is computed by the audit pipeline from audit-lane data; no author-side retained tier is asserted in source.
**Runner:** [`scripts/frontier_su3_cubic_anomaly_cancellation.py`](../scripts/frontier_su3_cubic_anomaly_cancellation.py)
**Runner cache:** [`logs/runner-cache/frontier_su3_cubic_anomaly_cancellation.txt`](../logs/runner-cache/frontier_su3_cubic_anomaly_cancellation.txt)

## 2026-06-18 source-side narrow-authority rebase

Earlier source wording made the row look as if it needed the broad
one-generation matter-closure and hypercharge-uniqueness parents as direct
load-bearing inputs. That is stronger than the local SU(3)^3 colour-anomaly
arithmetic needs. This repair factors the row into the narrow pieces that are
actually used by the trace:

- `GRAPH_FIRST_SU3_INTEGRATION_NOTE.md` supplies the selected-axis weak
  2-fiber, the residual base split `3 + 1`, and the structural SU(3) carrier.
- `LEFT_HANDED_CHARGE_MATCHING_NOTE.md` records the left-handed `(2,3)` and
  `(2,1)` block decomposition; the absolute hypercharge scale is not used by
  this SU(3)^3 trace.
- `ONE_GENERATION_ANOMALY_SINGLET_COMPLETION_NARROW_THEOREM_NOTE_2026-05-10.md`
  supplies the narrow right-handed singlet hypercharge completion arithmetic
  under its named shift and branch assumptions. This row uses only the
  existence of two colored right-handed singlet slots named `u_R` and `d_R`
  as the colour-sector slots to be put into the left-handed conjugate frame;
  it does not import the broad one-generation matter-closure package.
- `RH_COMPLETION_COLOR_ANTI_FUNDAMENTAL_NARROW_THEOREM_NOTE_2026-05-17.md`
  supplies the local representation-mapping identity
  `A(Rbar) = -A(R)`, hence `A(3bar) = -1`, from the explicit SU(3)
  Gell-Mann carrier and `d^{abc}` trace algebra.

The broad notes `ONE_GENERATION_MATTER_CLOSURE_NOTE.md` and
`STANDARD_MODEL_HYPERCHARGE_UNIQUENESS_THEOREM_NOTE_2026-04-24.md` remain
reader context for full matter closure and full SM labelling. They are not
the one-hop proof inputs for the local colour-anomaly trace. Downstream rows
that require full one-generation closure, the neutral-singlet branch selector,
physical chirality/time selection, or absolute hypercharge identification
must cite and repair those rows separately.

No audit verdict, ledger status, publication status, or repo-wide authority
surface is changed by this source-side repair. Independent audit remains the
only effective-status authority.

## Statement

For chiral Weyl fermions coupled to `SU(3)`, the pure cubic gauge anomaly is
proportional to

```text
sum_i m_i A(R_i),
```

where `m_i` is the multiplicity from non-color indices and `A(R_i)` is the
`SU(3)` cubic anomaly index of the color representation:

```text
A(1) = 0,  A(3) = +1,  A(3bar) = -1,  A(8) = 0,
A(6) = +7, A(6bar) = -7.
```

On the retained one-generation content written in the left-handed conjugate
frame,

| field | `SU(3)` rep | weak multiplicity | contribution |
|---|---:|---:|---:|
| `Q_L` | `3` | 2 | `+2` |
| `u_R^c` | `3bar` | 1 | `-1` |
| `d_R^c` | `3bar` | 1 | `-1` |
| `L_L`, `e_R^c`, `nu_R^c` | `1` | any | `0` |

so

```text
sum_i m_i A(R_i) = +2 - 1 - 1 = 0.
```

Thus the retained color-charged matter content cancels the pure `SU(3)^3`
cubic gauge anomaly exactly.

## Retained Inputs

| Input | Authority | Role in this row |
|---|---|---|
| Selected-axis structural `SU(3)` carrier, weak 2-fiber, and base `3 + 1` split | [GRAPH_FIRST_SU3_INTEGRATION_NOTE.md](GRAPH_FIRST_SU3_INTEGRATION_NOTE.md) | supplies the color carrier and weak multiplicity used in `Q_L: 2 * A(3)` |
| Left-handed `(2,3)` and `(2,1)` block decomposition | [LEFT_HANDED_CHARGE_MATCHING_NOTE.md](LEFT_HANDED_CHARGE_MATCHING_NOTE.md) | names the left-handed quark/lepton block structure; absolute hypercharge scale is not used |
| Narrow right-handed singlet completion arithmetic under named shift/branch assumptions | [ONE_GENERATION_ANOMALY_SINGLET_COMPLETION_NARROW_THEOREM_NOTE_2026-05-10.md](ONE_GENERATION_ANOMALY_SINGLET_COMPLETION_NARROW_THEOREM_NOTE_2026-05-10.md) | supplies the two colored right-handed singlet slots `u_R`, `d_R` as colour-sector slots, without importing the broad matter-closure package |
| Conjugate-frame SU(3) cubic-index map | [RH_COMPLETION_COLOR_ANTI_FUNDAMENTAL_NARROW_THEOREM_NOTE_2026-05-17.md](RH_COMPLETION_COLOR_ANTI_FUNDAMENTAL_NARROW_THEOREM_NOTE_2026-05-17.md) | derives `A(3bar) = -1` and the two-slot contribution `2 * A(3bar) = -2` |
| Cubic anomaly sum linearity | finite-dimensional trace linearity and chiral-gauge anomaly definition | used only to sum the three displayed colour-sector terms |

## Proof On Retained Content

Use the left-handed conjugate frame. The right-handed color triplets are
represented as left-handed anti-triplets:

```text
u_R  ->  u_R^c in 3bar,
d_R  ->  d_R^c in 3bar.
```

The only `SU(3)`-charged fields in this scoped colour-anomaly carrier are
`Q_L`, `u_R^c`, and `d_R^c`. Leptons are color singlets and do not
contribute to SU(3)^3.

The retained quark doublet contributes two color fundamentals because it has
two weak components:

```text
Q_L: 2 * A(3) = 2.
```

The retained right-handed colored singlets contribute two anti-fundamentals:

```text
u_R^c: A(3bar) = -1,
d_R^c: A(3bar) = -1.
```

Therefore:

```text
SU(3)^3 anomaly index = 2 - 1 - 1 = 0.
```

Equivalently, the retained one-generation content is vector-like with respect
to net color fundamentals:

```text
2 copies of 3  -  2 copies of 3bar  = 0.
```

This is not automatic for `SU(3)`. It is a real matter-content condition.

## Relation To Other Anomaly Rows

This theorem is separate from:

- the hypercharge and mixed-gauge anomaly equations used in
  `ANOMALY_FORCES_TIME_THEOREM.md`;
- the SM hypercharge uniqueness theorem;
- the nonperturbative `SU(2)` Witten `Z_2` global anomaly;
- `B-L` anomaly freedom as a gaugeable option.

The pure `SU(2)^3` cubic gauge anomaly is different: it vanishes
group-theoretically because the symmetric `d^{abc}` tensor for `SU(2)` is
zero. The pure `SU(3)^3` anomaly does not vanish group-theoretically; it
vanishes here because the retained matter content has balanced `3` and
`3bar` contributions.

## Extension Surface

Starting from the retained one-generation value `0`:

| Extension | Change in `SU(3)^3` index | Status |
|---|---:|---|
| Add one chiral color fundamental with no partner | `+1` | anomalous |
| Add one chiral color anti-fundamental with no partner | `-1` | anomalous |
| Add a vectorlike `3 + 3bar` pair | `0` | allowed by this anomaly |
| Remove `u_R^c` or `d_R^c` | `+1` | anomalous |
| Add one full retained-style generation | `0` | allowed by this anomaly |
| Add one `6` with no `6bar` | `+7` | anomalous |
| Add one adjoint `8` | `0` | allowed by this anomaly |

Thus any extension with chiral color charge must preserve
`sum_i m_i A(R_i) = 0`.

## Scope

This theorem proves that the scoped one-generation color-charged carrier
cancels the pure `SU(3)^3` cubic gauge anomaly once the narrow colour-slot
and conjugate-representation inputs above are supplied.

It provides an independent colored-sector witness for the need to balance the
left-handed quark doublet with the two retained colored anti-fundamentals
`u_R^c` and `d_R^c`.

It does not prove the full right-handed sector or the full right-handed
lepton sector; leptons are color singlets and are invisible to `SU(3)^3`.

It does not close full one-generation matter closure, neutral-singlet branch
selection, chirality/time selection, or absolute SM hypercharge labelling.

It does not derive `N_c = 3`; that input comes from the graph-first color
lane.

It does not claim the retained completion is the only possible
`SU(3)^3`-anomaly-free completion, since vectorlike and other balanced
extensions can also cancel this anomaly.

It does not replace the perturbative hypercharge anomaly equations, the
Witten `SU(2)` anomaly theorem, or the `B-L` anomaly-freedom theorem.

## Reproduction

Run:

```bash
python3 scripts/frontier_su3_cubic_anomaly_cancellation.py
```

The runner checks the retained content, the exact `+2 - 1 - 1 = 0` anomaly
sum, derives the core `A(3)=+1`, `A(3bar)=-1` indices from the explicit
Gell-Mann trace, checks the source-side narrow-authority boundary, extension
scenarios, the `SU(2)^3` zero tensor, and the nonzero `SU(3)` symmetric tensor
that makes the color anomaly a genuine matter-content condition.

## Honest claim-status

```yaml
proposed_claim_type: positive_theorem
status_authority: independent audit lane only
audit_required_before_effective_retained: true
actual_current_surface_status: structural-anomaly cancellation theorem on scoped one-generation colour-charged carrier
conditional_surface_status: SU(3)^3 cubic gauge anomaly vanishes exactly as finite trace/arithmetic on the scoped `Q_L + u_R^c + d_R^c` colour-sector carrier; cancellation is a real matter-content condition (the symmetric d^{abc} tensor for SU(3) is nonzero and the anti-fundamental indices A(3bar) = -1 must balance the fundamental indices A(3) = +1)
hypothetical_axiom_status: null
admitted_observation_status: "No observed comparator is used. The core A(3)=+1 and A(3bar)=-1 indices are derived from explicit Gell-Mann trace algebra by this runner and the RH-completion narrow theorem. Extension-surface values A(6)=+7 and A(6bar)=-7 remain non-load-bearing reference controls."
proposal_allowed: false
proposal_allowed_reason: "Source note records the scoped structural cancellation theorem and a source-side dependency rebase. Effective retained tier is set by the independent audit lane; not asserted by author. Review-loop was delegated to the Codex reviewer."
bare_retained_allowed: false
```

## Source-side dependency rebase handoff

This section records the intended source-side handoff. It does not promote this
note or change any audit ledger row.

- The direct local proof inputs are the markdown-linked narrow authorities in
  the "Retained Inputs" table.
- ONE_GENERATION_MATTER_CLOSURE_NOTE.md remains the broad full matter-closure
  parent and is not closed here.
- STANDARD_MODEL_HYPERCHARGE_UNIQUENESS_THEOREM_NOTE_2026-04-24.md remains
  the broad SM-labelling/hypercharge parent and is not closed here.
- This row does not close full one-generation matter closure, does not derive
  the branch convention, does not derive chirality/time selection, and does
  not claim uniqueness among all anomaly-free colour extensions.
