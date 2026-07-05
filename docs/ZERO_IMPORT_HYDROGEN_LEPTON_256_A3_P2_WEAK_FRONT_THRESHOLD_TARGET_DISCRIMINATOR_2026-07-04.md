# Zero-Import Hydrogen: Lepton `1/256` A3 P2 Weak-Front Threshold Target Discriminator

**Date:** 2026-07-04
**Type:** partial-narrowing discriminator note
**Claim type:** meta / precision-placement target support
**Status:** support-only. This note does not derive `C_A3`, does not derive a
weak threshold correction, does not derive `m_e`, and does not derive hydrogen.
**Verifier:** `scripts/frontier_zero_import_hydrogen_lepton_256_a3_p2_weak_front_threshold_target_discriminator.py`

## Scope

The A3 correction-placement discriminator splits the small
`256.082435...` precision residual into five possible placements. This note
attacks only P2:

```text
P2 front-factor/threshold correction:
  F_phys = C_A3 * g_2 * (1/sqrt(2))
```

while keeping the source-side scaffold exact:

```text
S_l = 1/256.
```

This is useful because the source-side F/L/P/R path can, at best, give the
exact normalized source singleton. It cannot silently spend a later weak,
threshold, pole, or scheme correction unless that placement is declared.

## P2 Target Algebra

The A3 comparator residual is:

```text
N_A3 = 256.08243522600384
C_A3 = 256 / N_A3 = 0.9996780910571587
delta_front = C_A3 - 1 = -0.0003219089428413424
```

So a P2 theorem has a precise target:

```text
F_0    = g_2 * (1/sqrt(2))
F_phys = C_A3 * F_0
```

Equivalently, if the correction is read as a shift in `alpha_2 = g_2^2/(4 pi)`,

```text
1/alpha_2_phys = (1/C_A3^2) * 1/alpha_2_0.
```

Using the same comparator constants as the existing A3 verifier only to size
the target,

```text
g_2 ~= 0.652825229349
1/alpha_2 ~= 29.4860096979
Delta(1/alpha_2) ~= 0.01899279085.
```

With the structural above-threshold SU(2) coefficient

```text
b_2 = 19/6,
```

that inverse-coupling shift is equivalent, at one loop, to a small logarithmic
interval:

```text
ell_A3 = (2 pi / b_2) * Delta(1/alpha_2) ~= 0.03768480771
exp(ell_A3) ~= 1.038403884.
```

This is target bookkeeping, not a derivation. It says that a P2 closure must
produce either `C_A3` directly as a weak-front matching factor or the
equivalent threshold/matching log, without using observed `m_W`, observed
charged-lepton masses, or the fitted divisor as proof inputs.

## Required P2 Closure Inputs

For hydrogen purposes, P2 closes only if all of these are visible:

| input | content |
|---|---|
| `EXACT_SOURCE_SINGLETON_RETAINED` | the source-side path supplies `S_l = 1/256` without using A3 data |
| `WEAK_FRONT_BASE_RETAINED` | the lepton weak front `g_2 * (1/sqrt(2))` is retained with its own dependency graph |
| `CHARGED_LEPTON_FRONT_MATCHING_RETAINED` | a charged-lepton-specific front, threshold, pole, or scheme matching theorem supplies the multiplicative `C_A3` or equivalent log |
| `NO_SOURCE_DOUBLE_COUNT` | the correction is not also spent in the source singleton or Koide/electron readout |
| `NO_MW_OR_LEPTON_COMPARATOR_PROOF_INPUT` | observed `m_W`, observed charged-lepton masses, fitted `a_l`, and fitted `N_A3` are excluded as proof inputs |
| `AUDIT_ACCEPTANCE` | independent audit accepts the placement and dependency graph |

If those are supplied, the P2 branch leaves the source result exact:

```text
y_scale = (C_A3 * g_2 * (1/sqrt(2))) * (1/256).
```

If they are not supplied, multiplying by `C_A3` is only comparator
bookkeeping.

## Current Standing

| surface | current P2 relevance |
|---|---|
| `ZERO_IMPORT_HYDROGEN_LEPTON_256_A3_CORRECTION_PLACEMENT_DISCRIMINATOR_2026-07-04.md` | names P2 as a possible placement but does not derive it |
| `ZERO_IMPORT_HYDROGEN_LEPTON_256_PRECISION_CORRECTION_FIREWALL_2026-07-04.md` | quantifies `C_A3` and shows common loop-size factors are not automatically the target |
| `LEPTON_SCALE_FRONTIER_PROBE_2026-06-05.md` | factorizes the charged-lepton scale as `g_2 * (1/sqrt(2)) * (1/256)` after the empirical gate |
| `ZERO_IMPORT_HYDROGEN_WEAK_FRONT_BASE_RATIFICATION_DECISION_PACKET_2026-07-05.md` | packages the uncorrected `F_0 = g_2 * (1/sqrt(2))` base as a separate owner/audit handoff |
| weak-front-base contract | exposes `WEAK_FRONT_BASE_TEXT_LOCK`, `SU2_WEAK_COUPLING_CONTEXT_RETAINED`, `CHARGED_LEPTON_D17_BLOCK_NORMALIZATION_RETAINED`, and `UNCORRECTED_FRONT_SCOPE_LOCK`; it still does not supply the charged-lepton front matching correction |
| `ZERO_IMPORT_HYDROGEN_LEPTON_256_A3_P2_CHARGED_LEPTON_FRONT_MATCHING_CURRENT_SURFACE_NO_GO_2026-07-05.md` | records that current retained, primitive, and open-PR surfaces do not supply `CHARGED_LEPTON_FRONT_MATCHING_RETAINED`; P2 remains an open route |
| `LEPTON_YUKAWA_256_STRUCTURAL_PROBE_2026-06-05.md` | records that the data-preferred divisor is noninteger and the exact integer still needs a correction or direct noninteger theorem |
| `SU2_WEAK_BETA_COEFFICIENT_STRUCTURAL_CLOSED_FORM_THEOREM_NOTE_2026-04-26.md` | supplies structural `b_2 = 19/6` support, not the charged-lepton threshold or scheme matching |
| primitive registry | approved primitives supply scale conversion, OS0 kinetic-form isotropy, and realized-state evaluation only; no weak-front matching or A3 correction |

## Open PR Alignment

Open PRs were refreshed on 2026-07-04 before this note was written. The latest
moving PR is visible but not a P2 closure:

| PR | status | A3/P2 effect |
|---|---|---|
| `#5011` eta twisted walk family runner | `CLEAN` at latest refresh | runner stabilization surface; no charged-lepton weak-front threshold correction |
| `#5010` YT P1 I_s re-audit packet bridge repair | `CLEAN` | YT/P1 diagnostic repair; no A3 P2 placement |
| `#5009` S3 spacetime tensor primitive runner | `CLEAN` | bounded S3 tensor support context; no charged-lepton front matching |
| `#5008` quark mass-ratio CP probe repair | `CLEAN` | quark CP-area context; no lepton weak-front correction |
| `#5007` Koide native zero-section route guard | `CLEAN` | Koide route-guard context; P3-adjacent, not P2 |
| `#5006` static-source I1 hygiene companion | `CLEAN` | static-source hygiene; no A3 P2 placement |

Merge-state labels are moving review metadata, not proof inputs.

## Lane Consequence

This discriminator makes P2 auditable:

```text
exact source singleton 1/256
  + retained weak-front base
  + retained charged-lepton front matching C_A3
  + no comparator proof input
  -> A3 precision via P2.
```

It also prevents two common mistakes:

1. treating the small size of the correction as a derivation;
2. using a weak running coefficient such as `b_2 = 19/6` as if it supplied
   the charged-lepton threshold/matching log.

## No-Go Discipline Gate

The broad claim "P2 cannot close A3" is **not** shipped. The narrowed claim is:
P2 has a concrete target, but current retained surfaces supply only structural
weak-running support and the exact source scaffold, not the charged-lepton
front/matching theorem that would derive `C_A3`.

### N1 - Alternative route enumeration

| route | attempt | result |
|---|---|---|
| exact source route | Keep `S_l = 1/256` and put all A3 precision in P2. | OPEN TARGET. This note computes the needed `C_A3` and equivalent one-loop log. |
| raw fitted multiplier | Multiply the final product by fitted `C_A3`. | RULED OUT AS ZERO-IMPORT ROUTE. It uses the empirical divisor as proof input. |
| structural `b_2` route | Use retained `b_2 = 19/6` to claim the correction. | ATTEMPTED AS COMPLETE P2 ROUTE. `b_2` supplies slope, not a charged-lepton threshold/matching interval. |
| weak-front base route | Use `g_2 * (1/sqrt(2))` from the lepton-scale factorization. | PARTIAL ONLY. It supplies the uncorrected front, not the A3 shift. |
| Koide/readout route | Move the correction into phase/species/pole readout. | VALID ALTERNATIVE PLACEMENT P3, not P2. It must not be double-counted with a P2 correction. |
| direct noninteger divisor route | Derive `N_A3` directly rather than correcting the weak front. | VALID ALTERNATIVE PLACEMENT P4, not P2. It bypasses P2. |
| source-readout route | Derive corrected `S_l = C_A3/256`. | VALID ALTERNATIVE PLACEMENT P1, not P2. It changes source readout rather than front. |

### N2 - Wall-Independence Audit

| pair | closes automatically? | conclusion |
|---|---|---|
| exact source singleton <-> weak-front base | no in either direction | independent |
| weak-front base <-> front matching `C_A3` | no in either direction | independent |
| front matching `C_A3` <-> no-comparator boundary | no in either direction | independent |
| P2 front matching <-> P1 source readout | no; alternate placements | must avoid double count |
| P2 front matching <-> P3 Koide readout | no; alternate placements | must avoid double count |
| P2 front matching <-> P4 direct divisor | P4 bypasses P2; P2 does not imply P4 | separate placement |

The collapsed P2 target is not "derive every placement." It is one front-side
matching theorem plus the exact source singleton and audit.

### N3 - Hidden-Wall Scan

| phrase class | classification |
|---|---|
| `threshold` / `matching` | explicit P2 wall; not background. |
| `b_2 = 19/6` | structural slope support only; not a matching interval. |
| `comparator` / `fitted` | excluded as proof input. |
| `front` | explicit placement target; not silently source-side. |
| `primitive` / `registry` | registry checked; approved primitives do not supply this correction. |

No front/matching theorem is buried as standard context.

### N4 - Residual Matching

| cited surface | residual it attacks | match? |
|---|---|---|
| `ZERO_IMPORT_HYDROGEN_LEPTON_256_A3_CORRECTION_PLACEMENT_DISCRIMINATOR_2026-07-04.md` | placement degeneracy and P2 target class | yes |
| `ZERO_IMPORT_HYDROGEN_LEPTON_256_PRECISION_CORRECTION_FIREWALL_2026-07-04.md` | magnitude of `C_A3` | yes |
| `LEPTON_SCALE_FRONTIER_PROBE_2026-06-05.md` | uncorrected front factorization | yes for base front, not correction |
| `LEPTON_YUKAWA_256_STRUCTURAL_PROBE_2026-06-05.md` | noninteger precision residual | yes |
| `SU2_WEAK_BETA_COEFFICIENT_STRUCTURAL_CLOSED_FORM_THEOREM_NOTE_2026-04-26.md` | structural `b_2` slope | partial support, not matching interval |
| `axiom_premise_nodes.json` | primitive boundary | guard only |

No cited weak-running slope is counted as the A3 front-matching theorem.

### N5 - Rhetoric Audit

The note avoids saying "weak thresholds do not explain A3." Tested
resolutions:

| resolution | tested? | outcome |
|---|---|---|
| product algebra | yes | P2 is product-equivalent to P1/P3/P4 but dependency-distinct. |
| front correction magnitude | yes | `delta_front = -0.0003219089`. |
| one-loop log equivalent | yes | `ell_A3 ~= 0.03768480771` using `b_2 = 19/6`. |
| actual retained charged-lepton front matching | not closed | named as required input. |
| all future threshold/scheme theorems | not closed | left open. |

### N6 - Partial-Closure Path Scan

Legitimate closure paths remain:

| path | what it could close |
|---|---|
| retained charged-lepton weak-front threshold theorem | P2 directly |
| retained finite matching/scheme theorem at the lepton scalar source | P2 directly |
| corrected source-readout theorem | P1 alternative |
| Koide/pole/species readout theorem | P3 alternative |
| direct noninteger divisor theorem | P4 alternative |

These are import-retirement paths, not new axioms. The discriminator keeps
P2 visible enough for audit.

### N7 - Steelman

A hostile reviewer can argue that P2 is the most natural home for A3: exact
`1/256` is a bare source factor, while the physical charged-lepton scale is a
pole-scale quantity, so a `0.032%` finite weak or threshold matching factor is
exactly where the small offset should appear. The note accepts that steelman
as a live route. It only says that the current packet has not derived the
matching factor or its scale interval without comparator input.

### N8 - Cross-Cycle Echo

This mirrors prior lanes where a structural integer was promoted too quickly
to a physical pole quantity. The disciplined route is to keep the integer
scaffold, name the front/readout/pole placement, and require the correction
theorem before precision is claimed.

**Gate result:** broad P2 no-go fails; narrowed weak-front threshold target
discriminator passes.

## Explicit Non-Claims

- No derivation of `C_A3 = 0.999678091...`.
- No derivation of a charged-lepton weak-front threshold correction.
- No derivation of a finite matching or scheme correction.
- No derivation of corrected `S_l`.
- No derivation of `m_e`, `alpha(0)`, or hydrogen spectroscopy.
- No use of observed charged-lepton masses, observed `m_W`, fitted `a_l`, or
  fitted `N_A3` as proof inputs.
- No audit status change for any cited row.
- No new axiom, primitive, or admitted import.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_zero_import_hydrogen_lepton_256_a3_p2_weak_front_threshold_target_discriminator.py
```

The verifier checks the P2 target arithmetic, the equivalent one-loop
threshold log, placement separation, primitive boundary, live PR alignment,
no-go discipline section, and explicit non-claims.
