# α_s Direct Wilson-Loop Honest-Status Audit

**Date:** 2026-05-02
**Claim type:** open_gate
**Status:** demotion / status-correction packet for
[`ALPHA_S_DIRECT_WILSON_LOOP_DERIVATION_THEOREM_NOTE_2026-04-30.md`](ALPHA_S_DIRECT_WILSON_LOOP_DERIVATION_THEOREM_NOTE_2026-04-30.md)
which is currently `proposed_retained, unaudited` in the audit ledger. This
audit applies the seven retained-proposal certificate criteria honestly and
recommends demotion to **bounded support theorem on retained graph-first
surface with admitted Sommer-scale and standard QCD-running imports**.
**Primary runner:** unchanged — `scripts/frontier_alpha_s_direct_wilson_loop.py`
PASS=22 FAIL=0 after the current-normalization source-boundary refresh.

## 0. Audit context

The note `ALPHA_S_DIRECT_WILSON_LOOP_DERIVATION_THEOREM_NOTE_2026-04-30`
proposes a direct Wilson-loop / static-potential extraction of α_s(M_Z)
on the Cl(3)/Z³ graph-first surface with `g_bare = 1`, β = 6, giving:

```text
α_s(M_Z) = 0.1179962733 ± 0.0067923686
```

This is consistent with PDG world average `0.1180 ± 0.0009` within 1σ.

The note is currently at `proposed_retained, unaudited` (per
`audit_ledger.json`). Transitive descendants: 259. Load-bearing score: 9.52.

This review packet does **not** challenge the runner result or the algebra —
both are verified at PASS=20/0 strict mode. It applies the **seven
retained-proposal certificate criteria** to the note's actual current
authority surface and recommends an honest status.

## 1. Seven retained-proposal certificate criteria — honest assessment

| # | Criterion | Pass? | Notes |
|---|---|---|---|
| 1 | `proposal_allowed: true` | **NO** | Review recommends false. |
| 2 | No open imports for the claimed target | **NO** | Sommer scale `r_0 = 0.5 fm` is an external matching number. The QCD running bridge to `M_Z` (4-loop β-function, threshold matching) is an external standard correction. Both are admitted, not derived. |
| 3 | No observed values, fitted selectors, **admitted unit conventions, or literature values** are load-bearing proof inputs | **NO** | The Sommer scale `r_0 = 0.5 fm` is a literature value — it is the standard convention adopted in Sommer (1993) and FLAG. The α_s(M_Z) extraction depends on it as a load-bearing scale-setting input. The QCD running bridge uses literature 4-loop β-function. Both are admitted standard corrections, but the retention claim depends on them. |
| 4 | Every dependency is retained, retained corollary, or explicitly allowed exact support | **PARTIAL** | `graph_first_su3_integration_note` is retained (provides Wilson SU(3) gauge surface). The current framework baseline is `MINIMAL_AXIOMS_2026-06-05.md` / the stable `minimal_axioms` premise node, and that baseline explicitly does not supply `g_bare = 1` convention handling. The older `MINIMAL_AXIOMS_2026-04-11.md` citation is historical only and is not a normalization authority for this route. The open normalization dependency is therefore the separate `g_bare = 1` / beta=6 Wilson-surface gate, not the current minimal axiom memo. |
| 5 | Runner or proof artifact checks dependency classes, not only numerical output | **YES** | The strict runner (`scripts/frontier_alpha_s_direct_wilson_loop.py`) explicitly verifies **forbidden authority key avoidance** (no `u_0`, `alpha_lm`, `alpha_bare_over_u0_squared`, `mean_link`, `plaquette_authority`, `alpha_s_v_definition`). It enforces `used_as_authority = false` for the existing α_LM/u_0 chain and checks that the source-boundary note does not use the historical April minimal-axioms memo as current normalization authority. PASS=22 FAIL=0 verified 2026-06-18. |
| 6 | Review-loop disposition is `pass` | **PENDING** | This review packet is the branch-local self-review. Independent audit recommended. |
| 7 | PR body explicitly says independent audit is still required | **YES** | The note itself states "It remains `proposed_retained`: the audit ledger, not this note, decides whether the theorem is ratified." |

**Result:** Criteria 1, 2, 3, 6 fail or are partial; Criterion 4 is
partial. The note is **NOT eligible for `proposed_retained`** under the
current authority surface.

## 2. Recommended honest status

```yaml
actual_current_surface_status: bounded support theorem
conditional_surface_status: |
  bounded by admitted Sommer-scale matching and standard QCD-running bridge.
  Admitted external imports:
    - Sommer scale r_0 = 0.5 fm
    - 4-loop QCD beta function
    - threshold matching at quark mass thresholds
  Open current-surface import:
    - g_bare = 1 / beta = 6 Wilson normalization authority
hypothetical_axiom_status: null
admitted_observation_status: |
  Sommer scale r_0 from physical anchoring (literature standard correction;
  narrow non-derivation role).
  QCD running bridge from PDG-standard 4-loop machinery.
proposal_allowed: false
proposal_allowed_reason: |
  Criterion 3 fails — load-bearing literature standard corrections (Sommer
  scale, QCD running bridge) cannot underwrite a retention claim.
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

Non-authoritative review recommendation for the independent audit lane:
- classify the route as bounded support unless retained bridge theorems close
  the named imports;
- mark the Sommer-scale and QCD-running-bridge as admitted standard
  corrections in the assumption/import ledger if the audit lane agrees;
- do not route the `g_bare = 1` normalization dependency through
  `MINIMAL_AXIOMS_2026-04-11.md`; that memo is historical-only for this
  route, and the current minimal axiom surface explicitly leaves the
  convention outside the axioms.

## 3. What the note correctly does

- The strict runner enforces decoration-trap avoidance: it forbids
  `alpha_lm/u_0` chain as authority, forbids using `<P>` or `u_0` as a
  running-coupling input, and explicitly cross-checks against (rather
  than imports from) the existing α_LM/u_0 chain.
- The Wilson-loop / static-potential / Sommer-scale / running-bridge route
  is a methodologically clean route in the standard lattice-QCD framework.
- The numerical agreement with PDG (0.1180 ± 0.0067 inside the 1σ band of
  0.1180 ± 0.0009) is reproducible and statistically defensible.

## 4. What this review packet is not

- This is **not** a proof that the route is wrong. The route is correct as
  far as a standard lattice-QCD `α_s(M_Z)` extraction goes.
- This is **not** a no-go — the note's content is a legitimate bounded
  support route. The status correction is from `proposed_retained` to
  `bounded support theorem`.
- This is **not** a runner failure. The strict runner passes (22/0).

## 5. Path to retention (forward-looking)

For the note to lift from `bounded support` to a retained-grade theorem:

| Required step | Difficulty |
|---|---|
| Retire `r_0 = 0.5 fm` Sommer-scale dependency via a framework-derived scale anchor | hard — would need a Cl(3)/Z³ native scale-setting theorem independent of literature |
| Retire 4-loop QCD running bridge dependency | hard — requires framework-native running theorem |
| Supply current retained or approved premise authority for the `g_bare = 1` / beta=6 Wilson normalization gate | very hard — the 2026-06-05 minimal axiom memo explicitly does not supply this convention |

Current normalization citation repair: `MINIMAL_AXIOMS_2026-06-05.md` is the
current minimal-axiom baseline and the stable `minimal_axioms` premise node is
the corresponding dependency surface. That baseline is useful because it says
what the axioms do and do not provide. It does not supply `g_bare = 1`.
`MINIMAL_AXIOMS_2026-04-11.md` is historical only for this route and should not
be used as an authority that would close the Wilson normalization dependency.
The small-`a` Wilson matching theorem
`WILSON_SMALL_A_MATCHING_BETA_GBARE_NARROW_THEOREM_NOTE_2026-06-07.md` supplies
the relation `beta = 2 N_c / g_bare^2` inside a supplied Wilson action surface;
it does not select `g_bare = 1`.

Until at least one of these is closed, the current bounded support status
is honest.

## 6. Effect on downstream rows

The 259 transitive descendants under `alpha_s_direct_wilson_loop_derivation_theorem_note_2026-04-30`
should treat the α_s(M_Z) value as a **bounded support input with admitted
Sommer-scale and QCD-running-bridge corrections**, not as a retained-grade
zero-input derivation. Equivalently, downstream rows may cite the value only
as bounded support input, not as a retained-grade zero-input derivation.

### Downstream source-boundary firewall

Allowed downstream uses of this packet are limited to:

- cite the Wilson-loop/static-potential certificate as a reproducible
  bounded-support extraction on the stated gauge surface;
- cite the decoration-trap avoidance check that the `alpha_LM/u0` chain is
  not used as authority;
- cite the status correction itself: the broad physical α_s(M_Z) promotion
  route remains open until its named bridges are supplied.

Forbidden downstream uses without new retained bridge theorems:

- do not cite this packet as a framework-derived Sommer scale;
- do not cite this packet as a framework-native 4-loop QCD running and
  threshold-matching bridge;
- do not cite this packet as a pure-gauge-to-full-QCD sea-quark transfer;
- do not cite this packet as a retained alpha_s(M_Z) theorem or as a retained
  zero-input physical prediction;
- do not use PDG agreement as proof of framework derivation;
- do not use this packet to close the current axiom-surface normalization
  dependency;
- do not cite `MINIMAL_AXIOMS_2026-04-11.md` as a live `g_bare = 1`
  normalization authority;
- do not cite the current minimal axiom memo as a source of `g_bare = 1`;
  `MINIMAL_AXIOMS_2026-06-05.md` explicitly does not supply `g_bare = 1`
  convention handling.

The broad physical α_s(M_Z) lane can be re-audited only after retained bridge
theorems supply Sommer scale setting, QCD running/threshold matching,
pure-gauge-to-full-QCD sea-quark transfer, and current axiom-surface
normalization. Until then, the runner's numerical PASS result is a
bounded-support certificate plus a source-boundary guard, not a promotion
certificate.

## 7. Cross-references

- [`ALPHA_S_DIRECT_WILSON_LOOP_DERIVATION_THEOREM_NOTE_2026-04-30.md`](ALPHA_S_DIRECT_WILSON_LOOP_DERIVATION_THEOREM_NOTE_2026-04-30.md) — parent note being audited
- [`scripts/frontier_alpha_s_direct_wilson_loop.py`](../scripts/frontier_alpha_s_direct_wilson_loop.py) — strict runner (PASS=22/0)
- [`MINIMAL_AXIOMS_2026-06-05.md`](MINIMAL_AXIOMS_2026-06-05.md) — current minimal-axiom baseline; explicitly does not supply `g_bare = 1`
- `MINIMAL_AXIOMS_2026-04-11.md` — historical-only older memo; context
  handle only, not a citation-graph dependency and not a live normalization
  authority for this route
- [`WILSON_SMALL_A_MATCHING_BETA_GBARE_NARROW_THEOREM_NOTE_2026-06-07.md`](WILSON_SMALL_A_MATCHING_BETA_GBARE_NARROW_THEOREM_NOTE_2026-06-07.md) — Wilson matching relation inside a supplied action surface; does not select `g_bare = 1`
- [`GRAPH_FIRST_SU3_INTEGRATION_NOTE.md`](GRAPH_FIRST_SU3_INTEGRATION_NOTE.md) — retained Wilson SU(3) gauge surface
- Sommer, "A New Way to Set the Energy Scale" — arXiv:hep-lat/9310022
- FLAG Review 2021, Eur. Phys. J. C 82, 869 (2022)
- PDG 2025 QCD review, Section 9.4
