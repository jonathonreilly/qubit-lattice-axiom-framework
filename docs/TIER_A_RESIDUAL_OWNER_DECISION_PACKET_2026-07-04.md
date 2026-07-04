# Tier-A Residual Owner Decision Packet

**Date:** 2026-07-04
**Type:** meta
**Claim type:** meta
**Authority class:** Class D proposal per
[`docs/audit/DOCUMENT_AUTHORITY_AND_CITATION_POLICY.md`](audit/DOCUMENT_AUTHORITY_AND_CITATION_POLICY.md).
This document has no premise weight until an owner channel explicitly consumes
one or more candidates below and records the adoption in the relevant policy
and machine registry.
**Status:** source-side owner-decision packet; independent audit required
before any effective-status change. This packet does not retire
AC_phi_lambda or theta, does not edit any Tier-A registry, axiom, approved
primitive, audit verdict, or publication-status surface, and does not adopt
any governance premise.
**Primary runner:**
[`scripts/tier_a_residual_owner_decision_packet_2026_07_04.py`](../scripts/tier_a_residual_owner_decision_packet_2026_07_04.py)
**Cached output:**
[`logs/runner-cache/tier_a_residual_owner_decision_packet_2026_07_04.txt`](../logs/runner-cache/tier_a_residual_owner_decision_packet_2026_07_04.txt)

## Purpose

The residual governance readiness packet establishes the current fact pattern:
the approved premise allowlist contains exactly `minimal_axioms`,
`scale_reference_primitive`, `kinetic_isotropy_primitive`, and
`realized_state_primitive`, while the Tier-A registry still contains
AC_phi_lambda and theta with four live residual atoms. No current axiom or
approved primitive absorbs those atoms.

This packet turns that map into exact owner-decision text. It is deliberately
not an adoption. It is a narrow proposal surface for the case where theorem
routes are intentionally bypassed.

## Current Default

The default decision is **no adoption**:

```text
No owner-governance candidate in this packet has premise weight.
AC_phi_lambda and theta remain Tier-A derivation targets.
The four live residual atoms remain theorem targets unless later adopted
through an explicit owner channel and recorded in the relevant registry.
```

## Candidate Decisions

Each candidate is independently selectable. Adopting one candidate would not
adopt the others, and no candidate should be broadened by title or summary.

### Candidate 1: AC Orbit-Occupancy Statistical-Grain Premise

**Candidate id:** `ac_orbit_occupancy_statistical_grain_premise`

**Draft adoption text:**

```text
For the AC_phi_lambda charged-lepton matter-action surface, the physical
statistical grain is the K/CPT orbit or holomorphic-pair occupancy grain:
the doublet contributes once per K/CPT orbit rather than once per sector or
channel. This premise supplies only the matter-action occupancy grain needed
to discharge the surviving AC(i) measure-side realization binary.
```

**Registry effect if adopted:** remove `reading_occupancy_selection` from
AC_phi_lambda's `minimum_decomposition`, or reclassify that atom to the adopted
owner-governed premise named above. AC_phi_lambda itself remains Tier-A unless
`delta_readout_identification_R_eta` is also retired.

**Boundary:** no value of `r`, `delta`, a charged-lepton mass, a mixing angle,
or a probability rule is supplied. Above-C3 taste/Dirac/chirality content,
CKM/PMNS alignment, and any sector-weight law remain outside this candidate.

### Candidate 2: R-Eta H-Class/H-Unit Readout Premise

**Candidate id:** `ac_reta_hclass_hunit_readout_premise`

**Draft adoption text:**

```text
For the AC_phi_lambda charged-lepton R-eta surface, the physical readout is
the fixed-locus density class h, identity-read in h-units as the eta angle.
No additional clock-rate, transport, or normalization factor intervenes
between the retained fixed-locus density class and the charged-lepton eta
readout.
```

**Registry effect if adopted:** remove
`delta_readout_identification_R_eta` from AC_phi_lambda's
`minimum_decomposition`, or reclassify that atom to the adopted
owner-governed premise named above. AC_phi_lambda itself remains Tier-A unless
`reading_occupancy_selection` is also retired.

**Boundary:** this candidate supplies the h-class/h-unit readout license only.
It does not supply the fixed-locus arithmetic theorem, the matter-action
occupancy grain, a fitted magnitude, any PDG comparator, or a general
density-as-angle rule outside the named charged-lepton R-eta surface.

### Candidate 3: Theta Gauge Sector/Phase-Source Premise

**Candidate id:** `theta_gauge_sector_phase_source_premise`

**Draft adoption text:**

```text
For the strong-CP theta gauge side, the physical gauge topological-weighting
surface is the closed non-exact sector/readout surface isolated by the theta
G1/G2 support stack, and its phase source is the central-sector character
isolated by the theta G3 support stack. No independent multi-plaquette or
large-gauge winding input beyond that physical sector/readout and phase-source
surface is admitted.
```

**Registry effect if adopted:** remove `gauge_side_winding_account` from
theta's `minimum_decomposition`, or reclassify that atom to the adopted
owner-governed premise named above. Theta itself remains Tier-A unless
`mass_side_orientation_determinant_readout_bridge` is also retired.

**Boundary:** this candidate does not set `theta_bar = 0` by itself, does not
derive a continuum theta theorem, does not add an axion or fitted selector, and
does not supply the mass-side determinant channel.

### Candidate 4: Theta Mass Determinant-Channel/W2 Premise

**Candidate id:** `theta_mass_determinant_channel_w2_premise`

**Draft adoption text:**

```text
For the strong-CP theta mass side, the physical mass-action readout surface is
the W2-registrable K-real determinant channel, and the determinant-orientation
readout is the physical channel by which arg det(M_q) enters theta_bar. No
additional mass-surface selector or determinant-readout bridge is admitted
beyond that W2 determinant channel.
```

**Registry effect if adopted:** remove
`mass_side_orientation_determinant_readout_bridge` from theta's
`minimum_decomposition`, or reclassify that atom to the adopted
owner-governed premise named above. Theta itself remains Tier-A unless
`gauge_side_winding_account` is also retired.

**Boundary:** this candidate does not derive quark masses, CKM structure,
QCD continuum dynamics, a CP-odd coefficient theorem, or the gauge-side
winding account.

## Full Tier-A Elimination Gate

The Tier-A registry can honestly reach zero only after all four live atoms are
handled by retained theorem work or explicit owner-governance adoption:

```text
AC_phi_lambda retires only if Candidate 1 or a retained theorem handles AC(i),
and Candidate 2 or a retained theorem handles AC(ii).

theta retires only if Candidate 3 or a retained theorem handles the gauge-side
winding account, and Candidate 4 or a retained theorem handles the mass-side
determinant-readout bridge.
```

No registry deletion should occur from this packet alone.

## Registry Patch Sketch If All Four Are Adopted Later

The later adoption PR, if explicitly approved, would need to:

1. record the owner approval in
   [`docs/audit/AXIOM_MINIMALITY_POLICY.md`](audit/AXIOM_MINIMALITY_POLICY.md)
   or another owner-channel policy that carries Class B registry authority;
2. update [`docs/audit/data/tier_a_admissions.json`](audit/data/tier_a_admissions.json)
   so `genuine_admitted_input_count` becomes `0`, `canonical_ids` becomes
   empty, and `derivation_targets` becomes empty;
3. preserve a historical retirement record for AC_phi_lambda and theta naming
   the four adopted candidates and their boundaries;
4. update the human-readable Tier-A registry note and rerun the full audit
   pipeline so bounded dependents can cascade only through audit-owned
   machinery.

This sketch is not executable authority. It is a checklist for a later
explicit adoption PR.

## Firewalls

- No candidate in this packet is adopted.
- No axiom or approved primitive is added or amended.
- No Tier-A registry row is removed.
- No audit verdict is set.
- No source-side no-go is overridden.
- No theorem route is declared impossible.
- No current Class C support/no-go packet is promoted beyond its audited or
  unaudited scope.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/tier_a_residual_owner_decision_packet_2026_07_04.py
```

Expected close: `FAIL=0`.
