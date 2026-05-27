---
claim_id: yt_one_higgs_top_carrier_selection_support_note_2026-05-26
claim_type_author_hint: bounded_theorem
status_authority: independent_audit_lane_only
direct_effective_status_change_allowed_from_this_note: false
---

# Y_T One-Higgs Top-Carrier Selection Support

**Claim type:** bounded_theorem  
**Role:** narrow carrier-selection support for the Y_T source-action lane.  
**Status:** exact support for the one-Higgs up-type top operator skeleton; no
retained or proposed-retained Y_T closure by this note.
**Primary runner:**
`scripts/frontier_yt_one_higgs_top_carrier_selection_support.py`  
**Generated output:**
`outputs/yt_one_higgs_top_carrier_selection_support_2026-05-26.json`

## Claim

On the one-Higgs Standard Model charge table, the unique renormalizable Dirac
Yukawa carrier connecting the quark doublet `Q_L` to the up-type singlet
`u_R` is

```text
bar Q_L tilde H u_R.
```

The rejected partner

```text
bar Q_L H u_R
```

has nonzero hypercharge and is not gauge invariant.

This note is deliberately narrow.  It selects the top operator skeleton used
by the Y_T source lane.  It does not select the numerical Yukawa coefficient,
the generation matrix entry, or a physical source normalization.

## Inputs And Scope

The runner uses the explicit doubled-hypercharge table:

```text
Q_L   : (3, 2)_{+1/3}
L_L   : (1, 2)_{-1}
u_R   : (3, 1)_{+4/3}
d_R   : (3, 1)_{-2/3}
e_R   : (1, 1)_{-2}
nu_R  : (1, 1)_0
H     : (1, 2)_{+1}
tilde H : (1, 2)_{-1}.
```

The hypercharge arithmetic itself is supported by the retained-bounded
algebraic solution enumeration row
`sm_hypercharge_uniqueness_algebraic_solution_enumeration_narrow_theorem_note_2026-05-10`.
The broader one-Higgs gauge-selection note remains unaudited; this packet
does not rely on its author-status.

## Proof

A renormalizable one-Higgs Dirac Yukawa monomial has the form

```text
bar F_L S f_R,
```

with `F_L` a left doublet, `S` either `H` or `tilde H`, and `f_R` a right
singlet.  Gauge invariance imposes:

1. color singlet;
2. `SU(2)` singlet from `bar F_L` and `S`;
3. total hypercharge zero:

```text
-Y(F_L) + Y(S) + Y(f_R) = 0.
```

For the up-type quark carrier:

```text
-Y(Q_L) + Y(tilde H) + Y(u_R)
  = -1/3 - 1 + 4/3
  = 0.
```

For the rejected partner:

```text
-Y(Q_L) + Y(H) + Y(u_R)
  = -1/3 + 1 + 4/3
  = 2 != 0.
```

The color contraction `bar Q_L u_R` is a color singlet through
`bar 3 x 3 -> 1`, and `bar Q_L tilde H` is an `SU(2)` singlet through
`bar 2 x 2 -> 1`.  Therefore `bar Q_L tilde H u_R` is the unique one-Higgs
up-type quark carrier.

## Exhaustion Check

The same enumeration gives the four allowed one-Higgs Dirac carriers:

```text
bar Q_L tilde H u_R,
bar Q_L H d_R,
bar L_L H e_R,
bar L_L tilde H nu_R.
```

No quark/lepton crossed Yukawa passes the color condition, and no wrong-Higgs
partner passes the hypercharge condition.

## What This Burns Down

This note removes the carrier ambiguity for the local Y_T source theorem:

```text
top carrier = one-Higgs up-type operator skeleton bar Q_L tilde H u_R.
```

It gives the physical-intervention uniqueness gate a clean local target
operator skeleton.  The coefficient remains outside this note.

## What Still Remains

Gauge selection leaves a free generation matrix:

```text
L_Y includes -bar Q_L Y_u tilde H u_R.
```

This packet does not determine `(Y_u)_{33}`.  The coefficient still requires
the physical intervention law from the source-action route or a strict
same-source top/W response measurement.

## Non-Claims

This note does not:

- claim retained or proposed-retained Y_T closure;
- derive `y_t`, `m_t`, `v`, physical-scale `g_2`, or matching/running;
- select any numerical Yukawa matrix entry;
- prove the physical top intervention law;
- prove strict top/W pole-response evidence;
- use `H_unit`, `yt_ward_identity`, `y_t_bare`, observed W/Z/top masses, PDG
  values, `alpha_LM`, plaquette/u0, Planck, alpha_s, or a fitted selector as
  proof inputs.

## Claim-Status Certificate

```yaml
actual_current_surface_status: exact-support
trace_class: upstream_support
reachability_to_target: supports
proposal_allowed: false
proposal_allowed_reason: |
  The note selects the one-Higgs up-type top carrier skeleton, but the Yukawa
  coefficient, physical intervention law, same-scale g_2, and matching/running
  remain outside this packet.
bare_retained_allowed: false
audit_required_before_effective_retained: true
```

## Verification

Run:

```text
python3 scripts/frontier_yt_one_higgs_top_carrier_selection_support.py
```

Expected result:

```text
SUMMARY: PASS=... FAIL=0
```
