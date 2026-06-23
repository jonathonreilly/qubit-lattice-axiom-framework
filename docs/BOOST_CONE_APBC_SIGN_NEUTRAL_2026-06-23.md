# The Boost-Cone and Antiperiodic-Boundary Routes to the Lorentzian Sign are Both Closed

> **Key terms used in this doc** are indexed A–Z at `docs/KEY_TERMINOLOGY.md`.

**Date:** 2026-06-23
**Claim type:** no_go
**Type:** negative route pruning (sub-route mapping)
**Status authority:** independent audit lane only. This source note does not set
or predict an audit outcome.

**Primary runner:**
[`scripts/boost_cone_apbc_sign_neutral_2026_06_23.py`](../scripts/boost_cone_apbc_sign_neutral_2026_06_23.py)
**Cached runner output:**
[`logs/runner-cache/boost_cone_apbc_sign_neutral_2026_06_23.txt`](../logs/runner-cache/boost_cone_apbc_sign_neutral_2026_06_23.txt)

## What this is

Companion to `RECORD_TICK_SIGNATURE_NEUTRAL_2026-06-23`, which showed the
record-tick is signature-neutral and named one harder candidate route to the
Lorentzian sign `eps = e_4^2 = -1`: the metric sign is equivalent to a
**non-compact (boost) symmetry** of the emergent record-causal cone, which one
might hope to source from the per-axis `Z_2` **antiperiodic-`tau` boundary
datum** (fermionic APBC on the temporal circle vs PBC on spatial circles). This
note certifies that candidate sub-route is **closed**, for four independent
structural reasons. It does **not** reduce, amend, narrow, retire, or re-approve
any registered primitive or admission, and adds no axiom/import: `eps = -1`
stays a separate, load-bearing binary admission in the register-not-read class.

## Certified facts (runner, `PASS=16 FAIL=0`, memory-trivial)

**(A) The boost-cone-automorphism route is circular.** A `4D` diagonal metric
has a non-compact (boost) stabilizer generator iff exactly one sign is `-1`
(Euclidean `diag(+,+,+,+)` → `0` boosts, compact `O(4)`; Lorentzian
`diag(-,+,+,+)` → `3` boosts, non-compact `O(3,1)`). A non-compact boost
stabilizer **is** `eps = -1` — so "derive `eps` from the boost symmetry"
presupposes the boost, i.e. presupposes the answer.

**(B) The discrete record-causal cone admits only a compact automorphism
group.** The cone is the Lieb-Robinson nearest-neighbor forward-reachability
polytope `{t >= 0, ||x||_1 <= v t}` (per `AXIOM_FIRST_MICROCAUSALITY`,
`retained_bounded`, and `LATTICE_NN_LIGHT_CONE`). A hyperbolic boost preserves
this polytope **only in 1+1**; for spatial dimension `>= 2` (the actual case) it
shears the `l1`/`l_inf` cone outside itself, so it is **not** a cone
automorphism. The surviving linear automorphisms are the finite hyperoctahedral
(signed axis permutation) group `×` discrete time-translation — **compact**, no
unbounded orbit. A finite-circle boundary identification cannot enlarge a compact
group to a non-compact one.

**(C) The antiperiodic-`tau` datum is sign-neutral, not sign-bearing.** Its wrap
operator (`C^L = -I`) has eigenvalues **exactly on the unit circle**
(`max||lambda|-1| ~ 1e-15`) — a compact `U(1)/Z_2` phase, not an off-circle
boost. The `Z_2` wrap group `{+1,-1}` has **no element squaring to `-1`**, so it
structurally cannot host `e_4` (`e_4^2 = -1`); the Lorentzian sign lives in a
categorically different object, the **Clifford fiber** (the `i` in
`gamma^j = i gamma^E_j`, per `WICK_ROTATION_COMPACT_SO4...`, `retained_bounded`).
The time↔space exchange map `W` is **real-orthogonal** (`W W^T = I`,
`det = +/-1`), so it preserves the Euclidean `(+,+,+,+)` form and transports
APBC across axes carrying **which axis wraps**, never **what signature** — fully
consistent with, and within the scope of, the retained
[`SINGLE_CLOCK_KMS_APBC_AXIS_SUPPLIER_NO_GO_NOTE_2026-06-16.md`](SINGLE_CLOCK_KMS_APBC_AXIS_SUPPLIER_NO_GO_NOTE_2026-06-16.md)
(axis-supply scope). Every reading that upgrades APBC to sign-bearing (thermal
`beta` = inverse temperature → `Tr e^{-itH}`) presupposes `tau -> it`, the Wick
answer (cardinal circularity).

**(D) The peripheral/unitary summand carries a compact phase, not a boost.** A
peripheral eigenvalue `e^{i theta}` (`|lambda| = 1`) is a compact `SO(2)` angle
(`eps = +1`); a boost `SO(1,1)` has eigenvalues **off** the unit circle
(`e^{+/- eta}`). So even a nonzero peripheral phase is compact — the wrong
generator class. Forcing `eps = -1` needs an unbounded/non-unitary generator
that lives **off** the peripheral `|lambda| = 1` summand.

**(E) Independent corroboration.** The retained
[`QUANTUM_LOCAL_ALGEBRA_DOES_NOT_FORCE_BOOST_ACTION_FAITH_NO_GO_NOTE_2026-06-02.md`](QUANTUM_LOCAL_ALGEBRA_DOES_NOT_FORCE_BOOST_ACTION_FAITH_NO_GO_NOTE_2026-06-02.md)
(`retained_no_go`) shows the on-site boost is not forced by the local algebra: a
scalar `S(eta) = exp(eta) I_2` is a valid spin-blind action on `C^2`, and the
faithful `K = -i sigma/2` (which closes `so(3,1)`) requires the explicit `i`
plus a matter-attachment selector. The runner reproduces both.

## Consequence and honest boundary

`eps = e_4^2 = -1` stays a **separate, load-bearing binary admission** (the Wick
`i` / a supplied registration-direction plus a minimal bridge), in the
register-not-read import class alongside `r = 1/2` and the readout admissions.
With `RECORD_TICK_SIGNATURE_NEUTRAL` (the record-tick is signature-neutral) and
this note (the boost-cone, the boundary datum, and the peripheral phase are all
signature-neutral or circular), the boundary-datum sub-lane is mapped.

- This is a **negative / sub-route-mapping** result. It does not derive
  `eps = -1`, does not change any admission's status, and touches no primitive.
- The boundary datum is **out of scope** of the axis-supplier no-go on the
  *signature* question — a genuine crack-shaped gap exists there — but the
  antiperiodic-`tau` datum provably cannot fill it (facts C above); that is a
  property of the datum, not a claim the axis-supplier no-go makes.
- The **only remaining firewall-clean opening** — the next path this opens, not
  a wall — is an *emergent* non-compact symmetry of the record-formation
  **dynamics** (a Hermitian, indefinite-form-preserving one-parameter generator
  over `Z^3`, not a Euclidean boundary datum), the open gate named in
  `SINGLE_CLOCK_ANTIPERIODIC_AXIS_DATUM_S4_TRANSPORT...` (`audited_conditional`).
  That relocates the question to the record-formation-dynamics lane and is
  owner-framing-gated; it is orthogonal to the static cone, the boundary datum,
  and the peripheral-phase machinery, all closed here.
- No new axioms / imports / comparators; signature-agnostic inputs only.

## Reproduce

```
python3 scripts/boost_cone_apbc_sign_neutral_2026_06_23.py
# expect: TOTAL: PASS=16 FAIL=0   (memory-trivial, single process)
```
