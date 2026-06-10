# Claim Status Certificate — block01 (chiral velocity quantization)

```yaml
actual_current_surface_status: conditional-support
target_claim_type: bounded_theorem
trace_class: direct_blocker_closure
reachability_to_target: partially_closes
conditional_surface_status: >
  the chiral (winding) carrier's cone slope is quantized to |v| = 1 EXACTLY
  (1D/per-axis), hence c_t = c_s under the named OS0 Wick bridge B-W;
  conditional on {P1 strict reading of the retained license + P2 unitary
  strict-tick reading + P3 CPT-pairing-of-the-tick reading + P4
  realized-carrier winding identification + B-W}. The retained surface
  supplies the license theorem and the CPT note the readings transfer from.
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: >
  The quantization theorem (monomial lemma + band-winding saturation) is
  exact and runner-derived (29/29 after adversarial review round 1), but the
  P1/P2/P3 readings, the P4 realization identification, and the B-W bridge
  are named conditional inputs, so the actual current-surface status cannot
  exceed conditional/bounded support. The independence-sharpening legs
  (bosonic, Hamiltonian, split-step, symmetric-brickwork, S+C witnesses)
  are exact.
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Promotion Value Gate (V1-V5)

| # | Answer |
|---|---|
| V1 | The #3360 support note's own N7 steelman: "a future retained dynamics could derive the same kinetic isotropy and retire the primitive. This would defeat a universal non-derivability claim, so the landed claim is narrowed to the current listed structures." This PR supplies exactly that derivation route, consuming three structures absent from the listed set (strict license form, unitary tick, band winding). |
| V2 | New derivation: the monomial lemma for unimodular Laurent amplitudes + the band-winding saturation theorem (winding forces beta=0, |gamma|=1, hence exactly linear bands) + the continuous-time no-winding fact + the three-premise hostile-witness wall table. None of this machinery exists anywhere in the repo (grep: no "winding", "monomial", "quantum cellular"-class result on the kinetic surface). |
| V3 | No. The quantization needs the framework's specific conjunction (strict radius-1 license + discrete tick + CPT pairing + chirality); standard math machinery alone does not know the license is strict or that the tick is the framework's time atom. The audit lane cannot reach this from retained primitives without the new lemma chain. |
| V4 | Yes: "discrete time quantizes (not merely permits) the kinetic isotropy" is a genuinely non-trivial structural result; the Collins-route surface only showed discrete time PERMITS protection at xi=1. |
| V5 | No. Closest prior cycles: #3360 (independence support — this consumes its named steelman door, opposite claim direction); the B4 stability note (assumes c_t=c_s, derives protection — this derives the assumption conditionally). Distinct premises, distinct mechanism, distinct conclusion. |

## No-Go Discipline (N1-N8)

Recorded in the source note's "No-Go Discipline Gate" section (the negative
legs: dial-nonexistence in the winding cell; no continuous-time winding).
All four drop-outs (P1, P2, P3, P4) now have explicit witnesses after
review round 1 (the P3 witness S_+ C(theta) was added on the referee's
finding).

## Review-loop disposition

pass — adversarial review round 1 returned 1 BLOCKER + 4 MAJOR, all resolved
with computed fixes (see REVIEW_HISTORY.md); the referee's verdict on the
core theorem: "correct under its premises".

---

# Claim Status Certificate — block02 (site-licensed tick dichotomy)

```yaml
actual_current_surface_status: conditional-support
target_claim_type: bounded_theorem
trace_class: direct_blocker_closure
reachability_to_target: partially_closes
conditional_surface_status: >
  for the realized carrier density (one Grassmann per site, landed
  scheme-forcing), every site-licensed unitary 2-site-periodic tick is
  FLAT or SATURATING (|v| = 1 edge/tick exactly); block01's P3 is
  discharged and P4 reduces to "the realized tick is dispersive (nonflat)".
  Remaining conditional set: {P1' site-strict reading + P2 unitary reading
  + B-W Wick bridge + scheme-forcing (landed, unaudited) + a dispersive
  realized tick + 2-site periodicity scope}.
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: >
  The dichotomy is exact and runner-derived (16/16: structural degree
  table, unitarity cross-term kill, two-circles lemma, seeded sweep),
  but the named readings, the unaudited scheme-forcing dependency, and
  the periodicity scope cap the actual surface status at
  conditional/bounded support.
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Promotion Value Gate (V1-V5) — block02

| # | Answer |
|---|---|
| V1 | Block01's premise table names P3 and P4 as conditional inputs ("named conditional reading" / "named realization premise... exhibited at the brickwork level, not closed"). This block closes both at the carrier's natural periodicity. |
| V2 | New derivation: the site-radius degree table (diagonal Bloch entries constant — absent from every landed note), the unitarity cross-term kill, and the two-circles cardinality lemma. None exists anywhere on the surface. |
| V3 | No: the collapse requires the license read in site units against the SPECIFIC landed carrier density; the anisotropy gate counts coefficients under symmetry, not under the license. |
| V4 | Yes: "dispersiveness forces winding" eliminates the selection problem entirely — a structurally different result from block01 (where winding had to be assumed). |
| V5 | No: block01 works at 2-component-cell generality and NEEDS P3+P4; this block works at the realized density and DISCHARGES them. Different premise set, different structural mechanism (trace-constancy vs trace-family analysis). |

## Review-loop disposition — block02

pass — adversarial review round 1: NO BLOCKERS; 3 MAJOR (B5 sweep acceptance
gate + label, P4 "discharged" vs "reduced" ledger honesty, B2/B3/B4
cannot-fail checks) + 4 MINOR + 3 NIT, all resolved with computed fixes
(see REVIEW_HISTORY.md). Referee verdict: "the central theorem is correct —
I independently re-derived and numerically confirmed every load-bearing
leg"; the two-circles lemma is STRONGER than stated (det confined to ONE
value for T != 0).
