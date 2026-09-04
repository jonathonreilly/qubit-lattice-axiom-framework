---
claim_id: source_measure_pcal_cumulant_mobius_theorem_note_2026-05-30
claim_type_author_hint: bounded_theorem
status_authority: independent_audit_lane_only
direct_effective_status_change_allowed_from_this_note: false
---

# Source/Measure P-Cal Cumulant-Mobius Theorem

**Claim type:** bounded_theorem / exact-support theorem.
**Role:** second source/measure P-cal retirement route.
**Status:** exact-support.  This note proves that `W = log Z` is the unique
finite-record generator of connected source responses.  It does not by itself
assert unbounded retained Y_T closure, because the physical premise
"the scalar source response of interest is the connected response" still
requires audit acceptance as native source-measure structure.
**Primary runner:** `scripts/frontier_source_measure_pcal_cumulant_mobius.py`
**Generated output:** `outputs/source_measure_pcal_cumulant_mobius_2026-05-30.json`

## Theorem

Let

```text
M[J] = E_0 exp(sum_i J_i O_i)
```

be the finite sharp-record moment generator.  The partition lattice Mobius
inversion formula defines connected responses by subtracting all disconnected
partition products.  The unique formal generator whose derivatives are those
connected responses is

```text
K[J] = log M[J].
```

Therefore, if the physical scalar source-response generator is required to
generate connected responses, the logarithm is forced.  The family
`F_p = M^p` only rescales all connected responses by `p`; unit connected
two-point/Fisher normalization selects `p = 1`.

## Mobius proof

For random variables `O_1,...,O_n`, moments and cumulants are related by

```text
E[prod_i O_i] = sum_{pi in Partitions(n)} prod_{B in pi} kappa(B).
```

Mobius inversion on the partition lattice gives

```text
kappa(1,...,n)
  = sum_{pi} (-1)^(|pi|-1) (|pi|-1)! prod_{B in pi} E[prod_{i in B} O_i].
```

For `n=3`:

```text
kappa_123 = m_123 - m_12 m_3 - m_13 m_2 - m_23 m_1 + 2 m_1 m_2 m_3.
```

If one variable is independent from the others, the factorized moments make
the mixed cumulant vanish.  This is the precise algebraic content of
"connected response."

The exponential moment generator packages all moments:

```text
M[J] = E exp(sum_i J_i O_i).
```

The standard exponential formula for set partitions says that the generating
function for connected components is the logarithm:

```text
K[J] = log M[J].
```

Equivalently, derivatives of `K` at zero are exactly the Mobius cumulants.

## Scale test

For a centered signed record,

```text
M(t) = cosh(t),
K(t) = log cosh(t),
K''(0) = 1.
```

For the scaled family

```text
K_p(t) = p log M(t),
```

the connected two-point response is

```text
K_p''(0) = p.
```

Thus connectedness alone fixes the logarithmic form, while the primitive unit
connected two-point/Fisher response fixes the scale `p=1`.  This matches the
RN-cocycle theorem:

```text
unit Fisher source coordinate <=> unit connected two-point response.
```

## Connection to P-cal

The live P-cal premise says that the physical scalar generator is the
potential for the canonical normalized-trace expectation field.  This theorem
supplies the connected-response version:

```text
physical connected source responses -> W = log Z.
```

The result does not use scalar additivity over arbitrary physical subsystems as
a postulate.  It uses finite partition-lattice Mobius inversion, which is a
mathematical identity defining connected components of record correlations.

The remaining audit decision is whether "physical scalar response" in the
observable-principle/Y_T lane should be the connected source response.  If yes,
the log generator and the source-unit normalization are forced by this theorem
plus the RN-cocycle theorem.  If no, this note remains exact support only.

## Status boundary

```yaml
actual_current_surface_status: exact-support
trace_class: direct_blocker_closure_candidate
target_blocker_text: "P-cal / connected source-response generator"
source_of_blocker_text: "observable-principle P-cal residual and Y_T source-scale blocker"
reachability_to_target: partially_closes
artifact_role: theorem
closed_if_audit_accepts_connected_response_as_native:
  - W = log Z for finite sharp-record source responses
  - p = 1 under primitive unit connected two-point normalization
remaining_if_not_accepted:
  - physical scalar response means connected source response
  - strict same-source top/W response certificate
proposal_allowed: false
bare_retained_allowed: false
audit_required_before_effective_retained: true
```

## Non-claims

This note does not claim:

- unbounded retained Y_T closure on the current surface;
- that independent audit has accepted connected source responses as the
  physical scalar response object;
- a production top-correlator or top/W response certificate;
- repair of the old Ward route;
- use of `H_unit`, `yt_ward_identity`, `y_t_bare`, PDG values, `alpha_LM`,
  plaquette/u0, or a fitted selector.

## Verification

Run:

```text
python3 scripts/frontier_source_measure_pcal_cumulant_mobius.py
```

Expected result:

```text
SUMMARY: PASS=... FAIL=0
```
