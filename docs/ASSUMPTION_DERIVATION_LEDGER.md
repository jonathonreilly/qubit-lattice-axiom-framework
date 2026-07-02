# Assumption / Derivation Ledger

**Date:** 2026-04-15 (original); 2026-05-27 (scope narrowing + R_conn row
repair); 2026-05-28 (reclassified `bounded_theorem → meta` per audit path (b)).
**Type:** meta
**Claim scope:** non-authoritative roadmap/index of package ingredient labels;
sets no audit status and proves no ingredient row.
**Primary runner:** [`scripts/assumption_derivation_ledger_meta_check.py`](../scripts/assumption_derivation_ledger_meta_check.py)
(meta-firewall check; `PASS=16 FAIL=0` on 2026-06-18).

This file exists to stop the package from blurring axioms, computed
inputs, derived quantitative rows, and still-open companion lanes.

## 2026-05-28 Reclassification (bounded_theorem → meta)

The 2026-05-28 audit verdict on this row (`audited_conditional`) offered two
repair paths:

> *"missing_dependency_edge: wire every non-R_conn ingredient row to its
> retained-grade authority note **OR split the ledger into metadata plus
> independently audited ingredient claims.**"*

This file is, by its own explicit claim boundary (below), **not a
load-bearing theorem**: it "does not promote or demote any row" and
"summarises the package surface ... so that downstream readers can find the
authorities." Authoritative status for each ingredient lives in the named
authority note, never in this ledger's prose. The `bounded_theorem` type was
therefore a misclassification — a roadmap typed as a theorem will always read
as conditional because it asserts package-wide statuses it does not itself
certify.

This revision takes **path (b)**: the ledger is reclassified as `meta`
(bookkeeping roadmap / index). The independently-audited ingredient claims
already live in their own authority rows (e.g. the exact `F_adj = 8/9` row is
wired one-hop to [`RCONN_DERIVED_NOTE.md`](RCONN_DERIVED_NOTE.md); the
hierarchy, strong-CP, CKM, `y_t`, and Higgs rows each have their own lane
authorities listed in §"Follow-up wiring"). No ingredient claim is certified
*here*; this note is a pointer surface. No new axiom, import, or retained
bridge is introduced. The four science notes that reference this ledger cite
it as a "related"/"recorded-in"/"admitted-context" roadmap pointer, not as a
load-bearing derivation authority, so the reclassification breaks no chain.

## 2026-05-27 Scope narrowing

The 2026-05-26 audit verdict flagged that this ledger:

- asserts many package-wide status rows with no direct dependencies
  declared (the citation graph carries only one one-hop edge, to
  [`rconn_derived_note`](RCONN_DERIVED_NOTE.md));
- carries an `R_conn = 8/9` row that says "derived" while the sole
  declared dependency is a `retained_no_go` whose actual content is
  exact `F_adj = 8/9` plus an explicit no-go for deriving the physical
  connected-trace selector — i.e., the ledger row was overclaiming
  relative to the actual dep authority.

Repair instruction: *"narrow the ledger scope to status rows with
direct retained-grade authorities, rewrite the R_conn row as exact
F_adj = 8/9 with physical R_conn/K_EW conditional on a selector
theorem, and add direct dependency edges for every other ingredient
status before re-audit."*

The 2026-05-27 revision implemented the **scope narrowing** part of that
repair and rewrote the R_conn row. The 2026-05-29 revision supersedes the
remaining bounded-theorem interpretation: rows below are now roadmap
labels only, not load-bearing claims. The wider task of creating
theorem-grade ingredient rows with one-hop authority edges remains a
separate structural-cleanup target and is named explicitly in
§"Follow-up wiring (out of scope)" below.

**Claim boundary of this ledger.** This file is metadata. Authoritative
status for each row lives in `docs/audit/data/audit_ledger.json` and in
independently audited authority note(s), not in this ledger's prose.
Where this ledger and an authority note disagree, the authority note governs.
This ledger does not promote, demote, retain, or bound any row; it summarises
the package surface at the date stamp above so that downstream readers can
find the intended lanes.

## Current roadmap labels

| ingredient | roadmap label (non-authoritative) | navigation note |
|---|---|---|
| `Cl(3)` on `Z^3` as physical theory | framework axiom label | This is the starting physical postulate of the package. |
| `M_Pl` as UV cutoff | framework-scale label | Treated as the framework cutoff, not fitted from the SM. |
| SU(3) plaquette `<P> = 0.5934` at `beta = 6` | same-surface evaluation label | The complete prediction chain points to canonical plaquette evaluation of the partition function, not to an experimental import or a free parameter. |
| exact structural gauge/matter backbone | structural-backbone label | `SU(3) x SU(2) x U(1)`, three generations, anomaly-forced `3+1`, and matter-structure claims are tracked in their own authority notes. |
| `SU(3)` confinement / `\sqrt{\sigma}` | confinement-lane label | `T = 0` confinement and the bounded `\sqrt{\sigma} \approx 465 MeV` readout belong to their own confinement and EFT-bridge authority notes. |
| strong CP / `θ_eff = 0` | strong-CP-lane label | Strong-CP closure belongs to its own authority notes. This ledger is not that authority. |
| CKM neutron EDM | CKM-EDM-lane label | The CKM-only neutron-EDM statement and bounded readout belong to their own strong-CP, CKM, and EFT authority notes. |
| hierarchy / `v` theorem | hierarchy-lane label | The `v = 246.282818290129 GeV` theorem belongs to the hierarchy lane, not to this ledger. |
| exact `F_adj = 8/9` color fraction | exact-algebra pointer | `F_adj = (N_c² − 1)/N_c² = 8/9` at `N_c = 3` is tracked by [RCONN_DERIVED_NOTE.md](RCONN_DERIVED_NOTE.md). |
| physical `R_conn` / `K_EW` selector | **conditional on a selector theorem (out of scope here)** | The physical readout `R_phys(κ_EW) = F_adj + κ_EW(1 − F_adj)` and `K_EW(κ_EW) = 1 / R_phys(κ_EW)` has connected-trace specialisation `κ_EW = 0` (giving `K_EW = 9/8`) and full-trace specialisation `κ_EW = 1` (giving `K_EW = 1`). The current packet **does not derive the selector `κ_EW = 0`**. See [RCONN_DERIVED_NOTE.md](RCONN_DERIVED_NOTE.md) for the explicit no-go boundary. This ledger row replaces the prior unconditional `R_conn = 8/9` row, which overclaimed relative to the actual dep authority. |
| EW normalization package | matching-rule-conditional label | The exact Fierz/channel fraction and physical-scale EW readouts belong to their own authority notes; this row is only a pointer to that lane. |
| renormalized `y_t` endpoint | top-Yukawa-lane label | The `y_t(v) = 0.9176` endpoint and QFP/RGE-surrogate systematic belong to their own authority notes. |
| top pole mass package | top-mass-lane label | The top pole-mass readouts inherit the top-Yukawa lane status; this ledger is not a top-mass authority. |
| Higgs CW/stability package | Higgs-lane label | Higgs mechanism, `lambda(M_Pl)=0`, full 3-loop implementation, `m_H`, and stability claims belong to their own authority notes. |
| DM flagship lane | open-lane label | Exact transport-chain progress is real, but final DM quantitative closure is still not closed. |
| CKM quantitative package | CKM-lane label | The canonical atlas/axiom package and older route history belong to their own authority notes. |

## Roadmap wording rule

- call roadmap labels labels;
- do not treat this ledger as proof of any ingredient status;
- do not demote or promote a row by prose here;
- do not convert DM or CKM companions into theorem-grade closure by prose.

## Follow-up wiring (out of scope here)

Per the 2026-05-26 audit verdict, any future theorem-grade version of
this ledger would need a direct one-hop edge from every ingredient row to
its retained-grade authority note in the citation graph. This metadata
version deliberately does not attempt that. The following list is a
non-load-bearing cleanup map for future separately audited authority rows:

- `Cl(3)` on `Z^3` framework axiom → axiom-premise registry
- `M_Pl` UV-cutoff scale → framework-scale authority
- SU(3) plaquette `<P> = 0.5934` → canonical plaquette evaluation
  authority on the retained partition function
- exact structural gauge/matter backbone → retained backbone authority
- SU(3) confinement / `√σ ≈ 465 MeV` → retained confinement +
  bounded EFT bridge authorities
- strong CP `θ_eff = 0` → retained strong-CP authority
- CKM neutron EDM → retained strong-CP + CKM atlas authority + bounded
  EDM EFT bridge
- hierarchy `v` theorem → retained hierarchy-lane authority
- EW normalization package → matching-rule authority + the
  conditional-on-selector R_conn row above
- renormalized `y_t` endpoint → derived chain authority + bounded
  QFP/RGE-surrogate authority
- top pole mass package → derived `y_t` authority + bounded chain
- Higgs CW/stability package → bounded `y_t` route authority +
  framework-native Higgs implementation authority
- DM flagship lane → open-flagship-lane authority
- CKM quantitative package → promoted CKM atlas/axiom authority

Downstream consumers should treat this ledger as a roadmap only, not as
a load-bearing claim about any specific row's status.

## Review classification

```yaml
claim_type_author_hint: meta
claim_scope: "Non-authoritative roadmap/index of package ingredient labels; sets no audit status and proves no ingredient row."
primary_runner: scripts/assumption_derivation_ledger_meta_check.py
upstream_dependencies: []
admitted_context_inputs: []
```
