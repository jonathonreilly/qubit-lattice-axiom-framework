# EW kappa_EW Weighting Is Not Axiom-Derivable

**Date:** 2026-06-09
**Claim type:** no_go
**Status authority:** independent audit lane only. This source note writes no
audit verdict and does not retag any ledger row.
**Primary runner:**
[`scripts/frontier_ew_kappa_weighting_not_axiom_derivable.py`](../scripts/frontier_ew_kappa_weighting_not_axiom_derivable.py)
**Runner cache:**
[`logs/runner-cache/frontier_ew_kappa_weighting_not_axiom_derivable.txt`](../logs/runner-cache/frontier_ew_kappa_weighting_not_axiom_derivable.txt)

## Summary

This is a narrow axiom-boundary no-go:

```text
kappa_EW is a weighting/readout-bridge choice.
The approved axiom and primitive baseline supplies no weighting or physical
observable bridge.
Therefore kappa_EW is not derivable from that baseline alone.
```

The claim is not that no future theory can fix `kappa_EW`. A future derivation,
owner-approved admission, or owner-approved registry update could change the
status. This note only records that the current approved baseline,
`Lattice + Quantum + Record` plus the registered scale-reference and
kinetic-isotropy primitives, does not supply the missing weighting rule.

## Load-Bearing Facts

1. The EW color readout uses a family

   ```text
   Pi_phys = C + kappa_EW S,
   ```

   where `C` and `S` are the adjoint and singlet channel contributions. The
   central-sector partition gives the cardinality count `8/9`; it does not pick
   the inter-sector weight `kappa_EW`.

2. The Record axiom says a record supplies no readout context, weighting,
   normalization, probability, dynamics, or occupancy rule.

3. The Quantum axiom says it supplies no physical observable bridge.

4. The approved primitives do not supply the missing item: the scale-reference
   primitive supplies only unit conversion, and the kinetic-isotropy primitive
   supplies only the structural OS0 kinetic-form ratio `c_t = c_s`.

5. `docs/audit/data/tier_a_admissions.json` currently registers two admitted
   derivation targets and does not register `kappa_EW`.

Together these facts show that `kappa_EW` is not derivable from the approved
baseline alone. Calling it a candidate admission is descriptive, not an approval:
review-loop does not register it, audit it, or grant it.

## Scope

Can claim:

- `kappa_EW` is a weighting/readout-bridge choice.
- The current approved axiom/primitive baseline does not supply such a rule.
- The EW absolute normalization remains conditional on a future derivation or
  explicit governance/admission action.
- Within the existing construction, a common `K_EW` factor cancels from
  `sin^2(theta_W)`, so that ratio is insensitive to `kappa_EW` placement as
  implemented here.

Cannot claim:

- `kappa_EW = 0` or `kappa_EW = 1` is forced.
- `kappa_EW` is approved as a Tier-A admission.
- The Tier-A registry should be edited by review-loop.
- The framework is wrong or the axioms are defective.
- No possible future non-axiom theory, convention, or owner-approved admission
  can close the wall.

## No-Go Discipline Gate

**N1 - Alternative routes.**

| Route | Result | Marker |
|---|---|---|
| Use the central-sector count `8/9` to fix the coefficient. | Fails: count is not an inter-sector weight; the runner checks `Pi(0)=C` and `Pi(1)=C+S` with the same count. | ATTEMPTED |
| Use Record registration. | Fails: Record explicitly supplies no readout context or weighting. | RULED OUT BY AXIOM |
| Use the Quantum axiom. | Fails: Quantum explicitly supplies no physical observable bridge. | RULED OUT BY AXIOM |
| Use approved primitives. | Fails: the primitive registry contains only scale-reference and kinetic-isotropy primitives, neither of which supplies weighting or a readout bridge. | ATTEMPTED |
| Use prior route-specific packets such as CMT/OZI/tracelessness/MC/register-not-read. | They are contextual support only; they do not supply an axiom-level weighting. | RULED OUT BY PRIOR |
| Add a selector, readout convention, or admitted observable-bridge placement. | This can be a legitimate future closure route, but it is extra non-axiom content and therefore not a derivation from the approved baseline alone. | OPEN |

**N2 - Wall independence.** The collapsed wall set has one wall: the missing
weighting/readout-bridge rule. The count-versus-weight algebra classifies the
target; the axiom text states why the baseline does not supply it.

**N3 - Hidden-wall scan.** Phrases such as "current construction" and
"registered" refer only to current repo data parsed by the runner. They are not
extra physics premises. No standard-QFT, fitted, PDG, or empirical value is
load-bearing.

**N4 - Residual matching.** Prior kappa no-gos are cited only as contextual
support. The shipped residual is narrower: "not derivable from the approved
baseline alone." Any prior witness with a different residual is not load-bearing
for this note.

**N5 - Rhetoric audit.** The negative claim is not "no weighting exists" and not
"no route can ever close kappa_EW." It is only "the approved baseline does not
supply the weighting/readout-bridge rule."

**N6 - Partial-closure scan.** The legitimate closure path remains open: an
explicit future derivation, owner-approved admission, or owner-approved registry
update could supply the missing rule. Approved primitives were checked and do
not supply it.

**N7 - Steelman.** A hostile reviewer could say: "The axioms permit a supplied
readout context, and a sufficiently constrained EW readout context might force
`kappa_EW`." That would defeat a broad no-go, but not this one: supplying that
readout context is exactly extra non-axiom content.

**N8 - Cross-cycle echo.** The registered admissions and approved primitives show
that governance can legitimately add baseline-adjacent content. The same kind
of mechanism may eventually apply to `kappa_EW`; this note does not block it.

**No-go discipline status:** PASS for the narrow axiom-baseline no-go.

## Verification

```bash
python3 scripts/frontier_ew_kappa_weighting_not_axiom_derivable.py
```

Expected: `RUNNER STATUS: PASS (PASS=7 FAIL=0)`.

## Honest Auditor Read

Audit this as a narrow no-go: `kappa_EW` is not derivable from the current
approved axiom/primitive baseline alone. Do not audit it as an approved Tier-A
admission, an audit verdict, or a claim that no future non-axiom closure route
can exist.
