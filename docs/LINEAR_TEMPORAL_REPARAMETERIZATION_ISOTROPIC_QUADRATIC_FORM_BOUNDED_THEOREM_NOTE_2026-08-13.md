---
claim_id: linear_temporal_reparameterization_isotropic_quadratic_form_bounded_theorem_note_2026-08-13
claim_type: bounded_theorem
claim_scope: "For the declared isotropic Euclidean quadratic form Q_E=c(k4^2+|k|^2), c>0, and declared linear substitutions k4=i a omega with a>0, the continued forms are Q_a=c(-a^2 omega^2+|k|^2). For every a,b>0 they obey Q_b((a/b)omega,k)=Q_a(omega,k), so the displayed coefficient changes are exactly related by an invertible frequency-coordinate reparameterization. No physical clock map, Lorentzian dynamics, time metric, or Record readout is selected."
upstream_dependencies:
  - kinetic_isotropy_primitive
runner: scripts/linear_temporal_reparameterization_isotropic_quadratic_form_2026_08_13.py
---

# Linear Temporal Reparameterization Of An Isotropic Quadratic Form

**Date:** 2026-08-13
**Type:** bounded_theorem
**Scope:** exact algebra for a declared Euclidean isotropic quadratic form and
a declared family of linear temporal-coordinate substitutions.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/linear_temporal_reparameterization_isotropic_quadratic_form_2026_08_13.py`](../scripts/linear_temporal_reparameterization_isotropic_quadratic_form_2026_08_13.py)

## Result Up Front

Let

```text
Q_E(k4,k) = c (k4^2 + |k|^2),    c > 0,
```

and, for each declared `a > 0`, substitute

```text
k4 = i a omega.
```

Then

```text
Q_a(omega,k) = c (-a^2 omega^2 + |k|^2).
```

For every `a,b > 0`, the invertible frequency-coordinate rescaling

```text
omega_b = (a/b) omega_a
```

gives the exact identity

```text
Q_b(omega_b,k) = Q_b((a/b) omega_a,k) = Q_a(omega_a,k).
```

Thus the coefficient triples produced by different positive `a` values are
coordinate presentations of this declared quadratic-form family. They are not,
by themselves, distinct physical clocks or distinct Lorentzian theories.

The approved
[`KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md`](KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md)
supplies only equality of the Euclidean temporal and spatial kinetic-form
coefficients, `c_t=c_s`. It does not supply the overall representative
normalization `c`; this note therefore keeps `c` symbolic. It also supplies no
Lorentzian dynamics or clock-selection rule. The theorem below does not try to
derive one.

## Exact Theorem

For `c,a,b > 0`, define

```text
Q_E(k4,k) := c (k4^2 + kx^2 + ky^2 + kz^2),
Q_a(omega,k) := Q_E(i a omega,k).
```

Then:

1. `Q_a = c(-a^2 omega^2+|k|^2)`.
2. The ratio of the coefficient of `-omega^2` to any spatial quadratic
   coefficient is `a^2`; the overall `c` cancels.
3. `Q_b((a/b)omega,k)=Q_a(omega,k)`.
4. The map `omega -> (a/b)omega` is invertible, with inverse
   `omega -> (b/a)omega`, and these maps compose multiplicatively.
5. In the normalized coordinate `Omega:=a omega`, every member is the same
   form `c(-Omega^2+|k|^2)`.

The proof is direct substitution. Positivity excludes `a=0`, where the
coordinate map is singular and the temporal term disappears.

## Representative Values

At the separately chosen illustration `c=1/4`:

| `a` | coefficient of `-omega^2` | coefficient ratio | normalized coordinate |
|---|---:|---:|---|
| `1/2` | `1/16` | `1/4` | `Omega=omega/2` |
| `1` | `1/4` | `1` | `Omega=omega` |
| `2` | `1` | `4` | `Omega=2 omega` |

The three raw coefficients are distinct, but the reparameterization identity
above maps every row to the same normalized form. The table is an algebraic
illustration, not a primitive normalization or a physical discriminator.

## Proof-Obligation Graph

| Obligation | Disposition |
|---|---|
| represent Euclidean kinetic-form isotropy by one common coefficient `c` | declared algebra consistent with `c_t=c_s` |
| derive `Q_a` | closed by substitution |
| derive the temporal/spatial coefficient ratio | closed by coefficient extraction |
| prove pairwise reparameterization equivalence | closed by `omega_b=(a/b)omega_a` |
| prove invertibility and composition | closed for `a,b>0` |
| select a physical frequency coordinate or clock | outside the claim |

The obligation graph is acyclic. Every leaf of the bounded algebraic theorem
is closed. Physical clock selection is not a proof leaf because it is expressly
not part of the target.

## Framework Boundary

The theorem uses no Record functional and no Record-to-time bridge. In
particular, it does not restore the retired named scalar `I`, finite Record
additivity, or a scalar value at absence. Current Record supplies none of those
objects and assigns no value to a site without a record.

The theorem also does not claim that the approved kinetic-isotropy primitive
selects or fails to select a physical clock. Such a statement first requires a
definition of the physical frequency coordinate, a time metric, and a dynamics
or reconstruction interface. Here `omega` and `a` are declared coordinates,
and the result is their exact transformation law.

## Imports And Claim Boundary

| Item | Role | Provenance / status |
|---|---|---|
| `c_t=c_s` | Euclidean equal-coefficient context | approved kinetic-isotropy primitive |
| `c>0` | declared overall quadratic-form normalization | symbolic; no numerical value imported |
| `a,b>0` | declared coordinate parameters | universally quantified theorem variables |
| `k4=i a omega` | declared linear substitution | mathematical input, not a physical Wick/clock law |
| `c=1/4`, `a in {1/2,1,2}` | exact illustration | declared rationals; no observational role |

There are no measured, fitted, literature, or observational inputs. A physical
clock map, Lorentzian reconstruction, dynamics, and empirical normalization
remain outside the result.

## Review Record

The submitted source framed the three raw coefficients as evidence that
Euclidean kinetic isotropy does not fix a physical clock map. Review removed
that conclusion for three reasons:

1. the primitive supplies a coefficient ratio, not the submitted overall
   normalization `1/4`;
2. the submitted family members are exactly related by an invertible frequency
   rescaling, so the raw coefficient is coordinate-dependent; and
3. the source quoted scalar/additive Record semantics removed by the
   owner-approved 2026-08-13 premise update.

The durable salvage is the positive reparameterization-equivalence theorem
above. No negative clock-selection claim lands.

## Machine Status

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "The exact substitution, coefficient ratio, pairwise coordinate equivalence, inverse, and composition laws close for the declared quadratic-form family; physical clock selection is outside scope."
trace_class: upstream_support
target_claim_id: physical_lorentzian_clock_map
target_blocker_text: "construct and justify a physical frequency coordinate and Lorentzian clock interface"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "Use the equivalence identity to quotient coordinate normalization before testing any physical clock candidate."
conditional_surface_status: "exact for the declared positive-parameter quadratic-form family; no physical clock or Lorentzian dynamics is supplied"
hypothetical_axiom_status: no edit
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Primary Runner

The paired runner performs exact symbolic and rational checks of the theorem,
including inverse/composition laws, singular and wrong-direction mutations,
the representative table, source-boundary pins, and note/runner agreement.
