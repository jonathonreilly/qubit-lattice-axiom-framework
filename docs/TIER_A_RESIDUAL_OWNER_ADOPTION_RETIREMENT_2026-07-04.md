# Tier-A Residual Owner Adoption and Retirement

**Date:** 2026-07-04
**Type:** meta
**Claim type:** meta
**Status authority:** owner-governance registry action plus independent audit
lane mechanics. This note records explicit owner adoption of the four exact
Block49 residual candidates and retires the live Tier-A registry rows through
`docs/audit/data/owner_governed_premise_nodes.json`. It does not derive
AC_phi_lambda or theta as theorems, does not add or amend an axiom, does not
add an approved framework primitive, and does not set any audit verdict for
source-side support or no-go packets.
**Primary runner:**
[`scripts/tier_a_residual_owner_adoption_retirement_2026_07_04.py`](../scripts/tier_a_residual_owner_adoption_retirement_2026_07_04.py)
**Cached output:**
[`logs/runner-cache/tier_a_residual_owner_adoption_retirement_2026_07_04.txt`](../logs/runner-cache/tier_a_residual_owner_adoption_retirement_2026_07_04.txt)

## Decision

The four exact governance candidates prepared in
[`TIER_A_RESIDUAL_OWNER_DECISION_PACKET_2026-07-04.md`](TIER_A_RESIDUAL_OWNER_DECISION_PACKET_2026-07-04.md)
are adopted as owner-governed residual premises, not as axioms and not as
approved framework primitives:

1. `ac_orbit_occupancy_statistical_grain_premise`
2. `ac_reta_hclass_hunit_readout_premise`
3. `theta_gauge_sector_phase_source_premise`
4. `theta_mass_determinant_channel_w2_premise`

The adoption consumes the entire current live Tier-A minimum decomposition:

| Former Tier-A target | Adopted candidate ids | Registry result |
|---|---|---|
| `AC_phi_lambda` / `staggered_dirac_realization_gate_note_2026-05-03` | `ac_orbit_occupancy_statistical_grain_premise`; `ac_reta_hclass_hunit_readout_premise` | retired from live Tier-A; registered as an owner-governed residual premise |
| `theta` / `strong_cp_theta_zero_note` | `theta_gauge_sector_phase_source_premise`; `theta_mass_determinant_channel_w2_premise` | retired from live Tier-A; registered as an owner-governed residual premise |

Accordingly, [`docs/audit/data/tier_a_admissions.json`](audit/data/tier_a_admissions.json)
now has:

```text
genuine_admitted_input_count = 0
canonical_ids = []
derivation_targets = {}
```

Historical details for AC_phi_lambda and theta remain in
`retired_derivation_targets`. Their current chain-satisfying owner-governed
premise ids are registered in
[`docs/audit/data/owner_governed_premise_nodes.json`](audit/data/owner_governed_premise_nodes.json).

## Adopted Text and Boundaries

### AC_phi_lambda

The owner-governed `AC_phi_lambda` premise is exactly the conjunction of
Candidate 1 and Candidate 2 from the decision packet.

**Candidate 1 adopted text:**

```text
For the AC_phi_lambda charged-lepton matter-action surface, the physical
statistical grain is the K/CPT orbit or holomorphic-pair occupancy grain:
the doublet contributes once per K/CPT orbit rather than once per sector or
channel. This premise supplies only the matter-action occupancy grain needed
to discharge the surviving AC(i) measure-side realization binary.
```

**Candidate 2 adopted text:**

```text
For the AC_phi_lambda charged-lepton R-eta surface, the physical readout is
the fixed-locus density class h, identity-read in h-units as the eta angle.
No additional clock-rate, transport, or normalization factor intervenes
between the retained fixed-locus density class and the charged-lepton eta
readout.
```

**Boundary:** this adoption supplies no value of `r`, `delta`, a
charged-lepton mass, a mixing angle, a probability rule, above-C3
taste/Dirac/chirality content, CKM/PMNS alignment, or sector-weight law. It
does not set any audit status for the AC support or no-go packet stack.

### theta

The owner-governed `theta` premise is exactly the conjunction of Candidate 3
and Candidate 4 from the decision packet.

**Candidate 3 adopted text:**

```text
For the strong-CP theta gauge side, the physical gauge topological-weighting
surface is the closed non-exact sector/readout surface isolated by the theta
G1/G2 support stack, and its phase source is the central-sector character
isolated by the theta G3 support stack. No independent multi-plaquette or
large-gauge winding input beyond that physical sector/readout and phase-source
surface is admitted.
```

**Candidate 4 adopted text:**

```text
For the strong-CP theta mass side, the physical mass-action readout surface is
the W2-registrable K-real determinant channel, and the determinant-orientation
readout is the physical channel by which arg det(M_q) enters theta_bar. No
additional mass-surface selector or determinant-readout bridge is admitted
beyond that W2 determinant channel.
```

**Boundary:** this adoption does not derive `theta_bar = 0` by itself, a QCD
continuum theta theorem, quark masses, CKM structure, QCD continuum dynamics,
a CP-odd coefficient theorem, an axion, or a fitted selector. It does not set
any audit status for the theta support or no-go packet stack.

## Registry and Pipeline Effect

This block introduces a third accepted-premise registry class:

```text
owner-governed residual premises
```

Those entries are Class B owner-governed governance premises. They are distinct
from both:

- `axiom_premise_nodes.json`: axioms and approved framework primitives;
- `tier_a_admissions.json`: live Tier-A derivation targets that bound
  otherwise clean dependents to `retained_bounded`.

Owner-governed residual premises chain-satisfy without Tier-A bounding, but
only inside the exact boundary recorded in
`owner_governed_premise_nodes.json` and this note. They do not make the
underlying support/no-go packets audited clean or theorem-derived.

## Firewalls

- No axiom is added or amended.
- No approved framework primitive is added or amended.
- No Tier-A target remains live.
- The prior AC_phi_lambda and theta rows are preserved only as historical
  `retired_derivation_targets`.
- `Y0` and `g0` remain vacuous survey conventions, not accepted premises.
- The source-side theorem/no-go packets retain their own audit statuses.
- The adoption cannot be broadened by title or summary; cite the registry id
  and exact boundary text.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/tier_a_residual_owner_adoption_retirement_2026_07_04.py
```

Expected close: `FAIL=0`.
