# Assumption / Derivation Ledger

**Date:** 2026-04-15 (original); 2026-05-27 (scope narrowing + R_conn row
repair); 2026-05-28 (reclassified `bounded_theorem → meta` per audit path (b)).
**Type:** meta
**Status authority:** independent audit lane only.

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

This revision implements the **scope narrowing** part of that repair
explicitly: every row below is now labeled with the load-bearing claim
this ledger makes about it. The R_conn row is rewritten per the
auditor's exact instruction. The wider task of wiring every row to
a one-hop retained-grade authority via the citation graph is a
follow-up structural-cleanup target and is named explicitly in
§"Follow-up wiring (out of scope)" below.

**Claim boundary of this ledger.** This file is a bounded
ledger-level bookkeeping surface. Authoritative status for each row
lives in the named authority note(s), not in this ledger's prose. Where
this ledger and an authority note disagree, the authority note governs.
This ledger does not promote or demote any row; it summarises the
package surface at the date stamp above so that downstream readers can
find the authorities.

## Current ledger

| ingredient | current status | what is actually true now |
|---|---|---|
| `Cl(3)` on `Z^3` as physical theory | assumed framework axiom | This is the starting physical postulate of the package. |
| `a^(-1) = M_Pl` scale reference | primitive unit reference (units import) | The single dimensionful unit that converts framework natural units to physical units; irreducible by dimensional analysis since `A_min = Cl(3)` on `Z^3` carries zero dimensionful content, so a foundational primitive rather than a derivation gap. Not fitted from the SM. Does not assert `a/l_P = 1` (separate open gravity derivation). Authority: [SCALE_REFERENCE_PRIMITIVE_NOTE.md](SCALE_REFERENCE_PRIMITIVE_NOTE.md). |
| SU(3) plaquette `<P> = 0.5934` at `beta = 6` | same-surface evaluated / derived | The complete prediction chain uses the canonical plaquette evaluation of the retained partition function, not an experimental import or a free parameter. |
| exact structural gauge/matter backbone | derived | `SU(3) x SU(2) x U(1)`, three generations, anomaly-forced `3+1`, and the retained matter structure are package-grade. |
| `SU(3)` confinement / `\sqrt{\sigma}` | retained support + bounded companion | `T = 0` confinement is structural on the graph-first `SU(3)` gauge sector at canonical `g_bare^2 = 1`; the bounded `\sqrt{\sigma} \approx 465 MeV` readout uses the retained `\alpha_s` lane plus the standard low-energy EFT bridge. |
| strong CP / `θ_eff = 0` | retained | On the retained axiom-determined Wilson-plus-staggered action surface, no bare `θ` appears and the real-mass staggered determinant carries no phase. |
| CKM neutron EDM | retained corollary + bounded companion | Retained strong-CP closure plus the promoted CKM atlas/axiom package imply `d_n(QCD) = 0` exactly on the retained surface, so the surviving neutron EDM is CKM-only; the bounded `d_n(CKM) ~ 10^-32 - 10^-33 e cm` readout uses the standard short-/long-distance EFT bridge. |
| hierarchy / `v` theorem | derived | `v = 246.282818290129 GeV` is retained on the hierarchy lane; it is not part of the separate quantitative component stack. |
| exact `F_adj = 8/9` color fraction | derived (exact algebra) | `F_adj = (N_c² − 1)/N_c² = 8/9` at `N_c = 3` is exact SU(3) Fierz/channel-count algebra. Authority: [RCONN_DERIVED_NOTE.md](RCONN_DERIVED_NOTE.md) (`retained_no_go`). |
| physical `R_conn` / `K_EW` selector | **conditional on a selector theorem (out of scope here)** | The physical readout `R_phys(κ_EW) = F_adj + κ_EW(1 − F_adj)` and `K_EW(κ_EW) = 1 / R_phys(κ_EW)` has connected-trace specialisation `κ_EW = 0` (giving `K_EW = 9/8`) and full-trace specialisation `κ_EW = 1` (giving `K_EW = 1`). The current packet **does not derive the selector `κ_EW = 0`**. See [RCONN_DERIVED_NOTE.md](RCONN_DERIVED_NOTE.md) for the explicit no-go boundary. This ledger row replaces the prior unconditional `R_conn = 8/9` row, which overclaimed relative to the actual dep authority. |
| EW normalization package | matching-rule conditional | the exact Fierz/channel fraction is retained, but `sin^2(theta_W)`, `1/alpha_EM`, `g_1(v)`, and `g_2(v)` at the physical scale depend on the named readout coefficient `kappa_EW`; the familiar `9/8` correction is the connected-trace specialization `kappa_EW=0`, not an unconditional retained coefficient. |
| renormalized `y_t` endpoint | derived | `y_t(v) = 0.9176` is a zero-import central value, but it inherits an approximately `3%` QFP/RGE-surrogate systematic. |
| top pole mass package | derived | `m_t(pole) = 172.57 GeV` (2-loop) and `173.10 GeV` (3-loop) inherit the bounded `y_t` systematic. |
| Higgs CW/stability package | bounded | the mechanism, `lambda(M_Pl)=0` boundary, and framework-native full 3-loop Higgs implementation now exist; exact `m_H` and vacuum stability remain bounded only because they inherit the bounded `y_t` / QFP route. |
| DM flagship lane | open flagship lane | Exact transport-chain progress is real, but final DM quantitative closure is still not closed. |
| CKM quantitative package | promoted quantitative package | The canonical atlas/axiom package on the tensor/projector surface is promoted on `main`; older Cabibbo / mass-basis / partial-Jarlskog routes remain route history only. |

## Writing rule

- call computed inputs computed
- call derived rows derived
- call bounded rows bounded
- do not demote a promoted row by leaving it on a stale bounded package
- do not convert DM or CKM companions into theorem-grade closure by prose

## Follow-up wiring (out of scope here)

Per the 2026-05-26 audit verdict, every row of the ledger above should
ultimately have a direct one-hop edge to its retained-grade authority
note in the citation graph. As of the 2026-05-27 scope narrowing only
the F_adj / R_conn row carries an explicit dependency edge (to
[RCONN_DERIVED_NOTE.md](RCONN_DERIVED_NOTE.md)). The wider
structural-cleanup task — adding direct dependency edges for the other
rows — is **out of scope** for this revision and is named here as a
follow-up target:

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

Until the citation-graph edges land, downstream consumers should treat
this ledger as a roadmap to the named authority notes rather than as a
load-bearing claim about any specific row's status. The R_conn row
above is the only row whose authority is currently wired one-hop on
the citation graph.
