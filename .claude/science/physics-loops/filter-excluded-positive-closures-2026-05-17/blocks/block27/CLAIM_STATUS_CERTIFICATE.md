# CLAIM STATUS CERTIFICATE — Block 27 (axiom-first lattice Noether)

**Date:** 2026-05-17
**Campaign:** filter-excluded-positive-closures-2026-05-17
**Block:** 27 — axiom-first lattice Noether
  (target row `axiom_first_lattice_noether_theorem_note_2026-04-29`,
  desc=705, currently `audited_conditional`, claim_type
  `bounded_theorem`, chain_closes=False)
**Branch:** `physics-loop/axiom-first-lattice-noether-block27-2026-05-17`
**Slug:** `axiom-first-lattice-noether-block27-2026-05-17`
**Primary artifact:** `docs/LATTICE_NOETHER_CARRIER_INDEPENDENT_BILATERAL_IDENTITY_NARROW_THEOREM_NOTE_2026-05-17.md`
**Primary runner:** `scripts/lattice_noether_carrier_independent_bilateral_identity_narrow_2026_05_17.py`
**Runner cache:** `logs/runner-cache/lattice_noether_carrier_independent_bilateral_identity_narrow_2026_05_17.txt`

## Status

```yaml
actual_current_surface_status: carrier-independent bilateral Noether identity (narrow positive theorem)
target_claim_type: positive_theorem (narrow)
proposal_allowed: false
proposal_allowed_reason: |
  Strictly additive narrow sub-theorem note supplying a carrier-
  independent positive theorem for the bilateral Noether identity on
  the axis-translation-invariant carrier class. Parent note text is
  NOT modified; no parent note dependency is added or removed. Parent's
  audited_conditional status is unaffected. Source-only PR. Independent
  audit lane required before any retained-grade elevation.
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## V1-V5 Promotion Value Gate (fresh lane)

- **V1 (Reframing):** The parent note's audited_conditional verdict
  rationale names the staggered-Dirac/Grassmann carrier as the open-gate
  import that forces the `audited_conditional` tier. The bilateral
  algebraic identity at the core of the parent's Step 2 (eqs 7a-7c)
  does NOT require the staggered-specific structure of `eta_mu`; it
  requires only the axis-translation-invariance condition
  `c_mu(x + mu_hat) = c_mu(x)`. This reframing extracts the
  carrier-independent algebraic content as a positive theorem on the
  axis-inv class, without admitting the carrier gate. PASS.
- **V2 (Novelty):** No existing note isolates the bilateral identity
  as a carrier-independent statement on a precisely-characterized
  carrier class. Parent treats the staggered carrier as load-bearing.
  Sister staggered-Dirac substep notes treat the carrier as the
  *target* of forcing. This narrow theorem extracts the dimension- and
  gate-independent algebraic core. New content. PASS.
- **V3 (Could-audit-compile?):** Self-contained closed-form: (T1)
  anti-Hermiticity characterization, (T2) bilateral conserved current
  on AxisInv, (T3) explicit third class member, (T4) sharpness of the
  characterization, (T5) uniformity in c_mu. Each step is an
  elementary finite-Grassmann manipulation, with 8 independent runner
  exhibits at machine precision. PASS.
- **V4 (Non-trivial):** Yes — extracts the carrier-independent
  algebraic core that the parent's `audited_conditional` rationale
  treats as "tied to staggered carrier". Closes a specific slice of
  the gap (the algebraic part) without admitting the carrier gate.
  Strengthens the parent's `(N2)` U(1) result by recovering it as a
  specialization of the carrier-independent statement. PASS.
- **V5 (Distinct from prior cycles):** Yes — distinct sub-theorem on
  a strictly different scope (the carrier class
  AxisInv(Z^d), not the staggered carrier alone). The runner
  exhibits a third explicit class member (phi_mu cosine carrier) to
  certify the class is genuinely larger than {naive, staggered}. PASS.

**Disposition: PASS** for narrow sub-theorem note purposes.

## 7-criterion certificate

| # | Criterion | Pass |
|---|---|---|
| 1 | proposal_allowed | NO (sub-theorem note, strictly additive) |
| 2 | No open imports | YES (only A1, A2; AxisInv class is defined directly from the Z^d substrate; no staggered-Dirac realization gate admitted) |
| 3 | No load-bearing observed/fitted | YES (no numerical, observed, or fitted inputs) |
| 4 | Every dep retained | YES (depends only on `MINIMAL_AXIOMS_2026-05-03` framework axioms A1, A2; no new dependency added; parent note is cited but not load-bearing for the narrow theorem) |
| 5 | Runner checks dep classes | YES (8 exhibits: axis-inv carrier sweep, naive reference, staggered reference, third class member, sharpness, sigma_3 internal generator, algebraic Lie substitution, K=16 carrier uniformity) |
| 6 | Review-loop pass | self-review PASS (carrier-independent derivation written out in full; runner output cached and re-run-identical; sharpness verified by E5 counter-example) |
| 7 | PR body says independent audit required | YES |

**Honest tier:** branch-local positive narrow sub-theorem on the
explicit framework baseline. Closes a slice of the parent's
`audited_conditional` gap (the carrier-independent algebraic core),
leaving the carrier-identification slice (M ↔ M_KS) to the staggered-
Dirac realization gate and its successors. Strictly additive on the
parent note.

## Imports

None retired. None added. The new sub-theorem note has zero
admitted-context inputs (no carrier gate) and depends only on the
framework axioms A1, A2 from `MINIMAL_AXIOMS_2026-05-03.md`.

## Honest classification

**Narrow standalone positive sub-theorem note** for the bilateral
Noether identity on the axis-translation-invariant carrier class
`AxisInv(Z^d)`. Reframes the parent's bilateral algebraic content as
a positive theorem that holds for every carrier in the class, with
the staggered and naive Wilson-free carriers as two explicit
instances and a third instance (phi_mu cosine) exhibited by the
runner. The carrier-independence is *quantitative*: K=16 distinct
axis-inv carriers all give on-shell divergence < 1.2e-15 (E8).

## Runner result

```
Summary
  E1: PASS  (random axis-inv carrier sweep, K=8, worst |partial^L J| < 1e-15)
  E2: PASS  (naive Wilson-free reference c_mu = 1, |partial^L J| = 8.6e-16)
  E3: PASS  (staggered reference c_mu = eta_mu, |partial^L J| = 6.4e-16)
  E4: PASS  (third class member phi_mu cosine, |partial^L J| = 8.8e-16)
  E5: PASS  (sharpness: non-axis-inv carrier gives ||M_off+M_off^T||_max = 1.0)
  E6: PASS  (T = I (x) sigma_3 internal generator, |partial^L J| = 5.6e-16)
  E7: PASS  (algebraic J4 = i * J5 on random fields, |J4 - i*J5| = 0)
  E8: PASS  (K = 16 axis-inv carriers, worst |partial^L J| < 1.2e-15)

Overall verdict: PASS
```

All 8 exhibits pass to machine precision; sharpness exhibit (E5)
verifies the class characterization is sharp by exhibiting an O(1)
anti-Hermiticity violation on a non-axis-inv carrier.

## Cluster cap

- Volume cap: 1 of 5 PRs (this campaign block).
- Cluster: this PR is in the `axiom_first_lattice_noether_*` family;
  first PR in that cluster for this campaign.

## Hard rules adherence

- A_min only: YES — uses only Cl(3) per-site (A1), Z^d spatial substrate
  (A2), and elementary finite-Grassmann variational technique. No
  staggered-Dirac realization gate admitted.
- Source-only PR: YES — adds 1 docs/ note, 1 scripts/ runner,
  1 logs/runner-cache/ output, 2 block artifacts (this file +
  runner_output.log). No atlas/harness/audit-data writes.
- No main push: YES — work pushed only to the block27 branch.
- No merge: YES — PR opened for review; not merged.

## Stop criterion

Closure achieved at the narrow-sub-theorem level. The carrier-
identification slice (M ↔ M_KS) belongs to the staggered-Dirac
realization gate's follow-on; no churn from this block on that front.

## Honest scope of closure

This narrow theorem **does not close** the parent's `audited_conditional`
gap. It closes a specific *slice*: the algebraic content of the
bilateral identity, which the parent's verdict rationale flags as
"algebraic checks on the admitted staggered carrier", is recovered as
a positive theorem on the axis-inv class without admitting the carrier
gate. The remaining slice — the identification of the carrier with the
physical M_KS — is unchanged and remains in the parent's gate-import
status. Independent audit lane retains full authority over the
parent's effective status.
