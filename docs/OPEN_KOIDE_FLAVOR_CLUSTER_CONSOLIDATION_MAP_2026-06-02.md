# Open Koide/Flavor PR Cluster — Consolidated Map (for the reviewer; anchor #2453)

**Date:** 2026-06-02
**Claim type:** meta / cross-PR consolidation map. **Sets no audit status, assigns no grade, and changes no row.** A read-only map of the open koide/flavor PR cluster to help the reviewer land it coherently. References other PRs read-only; recommends — does not direct.
**Status authority:** independent audit lane only.
**Runner:** `scripts/flavor_open_cluster_consolidation_map_2026_06_02.py` (re-verifies the one-operator/one-residual thesis; SCORECARD 4/4; asserts no audit status).
**Source:** read-only review workflow `wf_bc1b02b5` (6 agents over ~30 open PRs).

## Verdict: the cluster coheres — one operator, one residual, six convergent routes
Every flavor PR attacks the *same single object*: the charged-lepton value `Q=2/3` and its companion
asymmetry `2/9`, both on **one** native operator `H=aI+bC+b̄C²` on the C₃ generation factor. Six
independent routes (built without coordinating with the #2453 capstone) all reduce to the **same single
residual bit** — equal-block (`r=1/2→Q=2/3`) vs dimension (`r=1→Q=1`), i.e. `AC_φλ` / det_C-vs-det_R,
formalized by the no-go `koide_frobenius_isotype_split_uniqueness`. That convergence is the no-coincidence
signal of *one derivation with one pin*, not many accidents.

## Thread map (canonical / most-complete per thread)
| thread | PRs | canonical / most-complete |
|---|---|---|
| **VALUE** (r=1/2 / det_C-vs-det_R / Q-lanes / not-forced) | #2453, #2406, #2407, #2412, #2425, #2441, #2444, #2445 | **#2453** (consolidated value campaign); sharpest single mechanism = **#2441** (Berry unification) |
| **ASYMMETRY** (δ=2/9 / signed-eta / Lefschetz / convention) | #2404, #2451, #2454, #2455, #2457 | **#2451** (operator-intrinsic signed equivariant-eta), tightened by **#2454** (finite Molien, not continuum eta) |
| **CARRIER / MATTER-ATTACHMENT** (chirality / fermionic frame / faithfulness / KS / graded-statistics / Weyl boosts) | #2405, #2443, #2460, #2461→#2465, #2466 | **#2465** (cascade endpoint → one cross-site graded-statistics gate); **#2460** standalone Weyl-boost piece |
| **RECORDS / RP** (records dynamics / RP+spectrum / transfer-positivity) | #2442, #2446, #2449, #2450, #2467, #2468 | **#2450** (D3 2-atom proof) + **#2449** (corrected conditional-not-forced standing) |
| **READOUT-CLASS** (signed-vs-singular / Fisher-Rao / anticommuting-vs-circulant) | #2409, #2458, #2459 | **#2409** (reality-of-D necessary-not-sufficient lemma); #2459 reconciles the two readouts |
| **NON-FLAVOR** (exclude) | #2402, #2413, #2422, #2440 | — (meson OS / β=6 / hierarchy α_LM; no Koide content) |

## Convergence (the no-coincidence signal)
Six independent routes land on the same single residual: Kähler-triple orientation/modulus-independence
(#2406), Kähler-Dirac dynamics-silence (#2407), reality-of-D admitting both Pfaffian/det readouts (#2409),
records-capacity extremizing continuously (#2449/#2450), Berry curvature (zero↔Q=1, monopole↔Q=2/3, #2441),
and the matter-attachment cascade (#2465). Separately the ASYMMETRY thread converges that `2/9` is the
spectral/Molien weight of the *same* H whose doublet magnitude gives Q=2/3 (#2451/#2454/#2455). This is the
structural-identity-not-coincidence pattern — *one operator, one handle, many lenses* — matching #2453's
"the whole gate = the chirality/fermionic-frame import" exactly.

## Complements to land alongside #2453 (genuine pieces the value anchor lacks)
- **#2441** — Berry-monopole **unification**: the single mechanism behind "whole gate = chirality" (zero Berry↔non-chiral↔Q=1; monopole↔chiral↔Q=2/3).
- **#2465** — matter-attachment cascade endpoint: all four probes fail for one reason (D's spatial covariance factors through SO(3), blind to the SU(2) cover) → reduces the import to the **cross-site graded-statistics gate = the generation-ID chirality gate** (pull its #2461→#2464 cascade in as support).
- **#2460** — on-site Weyl boosts from Cl(3,0) bivectors `K_i=iσ_i/2` closing `so(3,1)` exactly, **Grassmann-free** — breaks the multi-site L1 circularity (a strict improvement in kind).
- **#2412** — K0-real / real-Wedderburn-block reading (`ℝ[Z₃]=ℝ⊕ℂ`, 2 real blocks → r=1/2): the **K-reality half** of `AC_φλ`, no new axiom.
- **#2450 + #2449** — records D3 binary-record fact + the corrected conditional-not-forced standing.
- **#2409 + #2459** — reality-of-D necessary-not-sufficient readout lemma + anticommuting-vs-circulant reconciliation.
- **#2451 (+#2454)** — the operator-intrinsic `2/9` (hardens #2453's topological-2/9 leg).
- **#2404** — the explicit Tier-A `AC_φλ` admission companion (the same input #2453 names; this session's local branch).
- **#2406, #2407** — the cleanest independent convergence corroborations (orientation/modulus-independence; dynamics-silence).

## Dedupe (reviewer lands one)
- **#2425 / #2444 / #2445** — the same `Q=(1+2r)/3=2/3` identity three ways. Land **#2445** (the operator-level 3-channel Fourier anatomy, most complete); fold the one-line insights of #2425 (orientation-blind count) and #2444 (two-observables) rather than landing all three.
- **#2451 / #2454** — sequential refinements of the one `2/9` identity (physical-id leg → finite-vs-continuum tightening); land #2451, fold/append #2454.

## Self-corrected — do NOT land as-written
- **#2446** over-claims in its headline that the records pointer *grounds* the equal-block r=1/2 weight ("per-block counting is native"). It is **explicitly retracted by #2449** (same worker): "the pointer grounds the 2-channel structure, NOT the equal-block weight." Treat **#2449** as the standing claim; do not land #2446's headline.

## Conflicts + audit-lane flags (surfaced, not adopted or changed)
- **#2442** ("Q=1", branch `codex/q1-hunt`, 42 files +8171): ships a `.claude/science/physics-loops/` working-loop scaffold (STATE.yaml, NO_GO_LEDGER, PR_BACKLOG, HANDOFF) + ~17 probe runners, several without paired cached logs — **violates the review-loop source-only policy**. Not landable as-is.
- **Audit-language items — for the audit lane only; this map neither adopts nor changes them:** #2409, #2425, #2468 each *assert* a status for `koide_signed_eigenvalue_vs_singular_value_readout` ("audited_failed"), and #2468 lists `AC_φλ` as "audited_renaming / chain_closes=False". These are **status claims to verify against `git show origin/main:docs/audit/data/audit_ledger.json`** before being relied on. Likewise #2466 surfaces an internal correction (that `axiom_first_microcausality_lieb_robinson` over-asserts per-site grading → cross-site anticommutation, and #2462's byte-identical Lieb–Robinson claim was walked back) — **routed to the audit lane**, not resolved here.

## The shared gap
The cluster has thoroughly *isolated* but not *derived* the single residual: the measure/weight selection
(`AC_φλ` / equal-block-vs-dimension) is proven NOT forced by rep theory (#2407), records dynamics (#2449),
reality-of-matrix (#2409), or the native circulant's Berry curvature (#2406/#2441/#2443 → zero Berry → Q=1).
The chirality / cross-site-graded-statistics gate (#2465) is the **same** gate generation-ID needs. So the
combined cluster's honest standing: **structure fully derived; the entire value sector pinned to one shared
chirality/measure import (`AC_φλ`).**

## Suggested landing order (recommendation, not a directive — audit lane decides)
1. **#2453** — canonical consolidated value anchor (+ its chain-of-custody capstone).
2. **#2404** — the `AC_φλ` Tier-A admission companion.
3. Complements: **#2441, #2465** (+ #2461→#2464 cascade), **#2460, #2412, #2450+#2449, #2409+#2459, #2451(+#2454), #2406, #2407**.
4. Convention pieces: **#2455** (δ-radian π-convention), **#2457** (Fisher-Rao reorganization).
5. **Do not land #2446** as-written (use #2449's corrected form).
6. **Audit-lane fixes/flags** (above): verify the status assertions in #2409/#2425/#2468; route #2466's microcausality flag.
7. **Exclude from the flavor map:** #2402, #2413, #2422, #2440. Watch #2442/#2467/#2468 for corollary-churn density.

## Provenance
- The one-operator / one-residual thesis re-verified directly (runner 4/4). Cluster classification from the read-only review `wf_bc1b02b5`.
- This map **sets no audit status and assigns no grade**; all grading and the status-assertion flags above are the independent audit lane's call. References all other PRs read-only; edits none.
