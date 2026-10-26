# Supplied finite-interval signed transport identity

**Date:** 2026-10-24
**Type:** bounded_theorem
**Status:** conditional theorem source; independent confirmation and execution pending.
**Status authority:** independent audit lane only.
**Primary runner:** `scripts/supplied_finite_interval_signed_transport_identity_2026_10_24.py`
**Claim scope:** scalar real linear ODE on a supplied finite compact interval, with integrable coefficients and signed output. No physical transport, Boltzmann, HRAD, cosmological or selector identification.

## Hypotheses and theorem

Fix finite real a<b. Supply real W,S in L1([a,b]) and a real initial value B_a.
Here L1 means Lebesgue integrable including the endpoints, not merely locally
integrable on (a,b). The equation is B'=S-WB almost everywhere.
There is exactly one absolutely continuous real solution B on [a,b] with
B(a)=B_a, and for every t in [a,b],

    B(t) = B_a exp(-integral_a^t W(u) du)
           + integral_a^t S(z) exp(-integral_z^t W(u) du) dz.       (1)

In particular (1) at t=b is the finite-endpoint signed transport identity.
No sign restriction on W, S or B_a is needed. If a supplied absolutely
continuous N has S=-N' almost everywhere, substitution yields that alternative
notation; no separate dynamics for N or its physical interpretation is derived.

## Proof, existence and uniqueness

Define A(t)=integral_a^t W. It is absolutely continuous and bounded by ||W||_1.
Thus mu(t)=exp(A(t)) and its reciprocal are absolutely continuous, bounded,
and strictly positive; mu'=W mu almost everywhere by the chain rule. The
integrable product mu S has an absolutely continuous indefinite integral.
Set

    B(t) = mu(t)^(-1) [B_a + integral_a^t mu(z) S(z) dz].

This product is absolutely continuous and has initial value B_a. Its derivative
is S-WB almost everywhere by the product rule. This proves existence. Conversely
any absolutely continuous solution is bounded on the compact interval, so WB
is integrable; the product rule gives (mu B)'=mu S almost everywhere. Integration
and the initial condition give the same formula and therefore uniqueness.
Since mu(z)/mu(t)=exp(-integral_z^t W), this is (1), including both endpoints.
All displayed integrals are finite under the stated hypotheses.

## Sign, initial data and endpoint boundaries

With B_a=0, B(b) equals the signed source integral, while |B(b)| equals the
absolute value of that integral. Dropping the absolute value is justified, for
example, by the additional hypotheses S>=0 almost everywhere and B_a>=0:
both terms in (1) are then nonnegative, because real exponential weights are
positive even if W changes sign. These conditions are sufficient, not necessary.

Negative-source control: on [0,1], W=2, S=-2, B_a=0 yields
B(t)=-(1-exp(-2t)). Thus B(1)<0 and |B(1)| is not the signed integral.
Initial-term control: on [0,1], W=2, S=0, B_a=3 yields B(1)=3 exp(-2),
whereas the source integral alone is zero. These are counterexamples to omitting
sign or initial-data qualifications, not counterexamples to (1).
The theorem is finite-interval only. For W=2,S=2,B_a=0 the endpoint is
1-exp(-2), not 1; replacing the endpoint by an infinite-time limit requires
additional hypotheses and is not performed here.

The integrability hypotheses are substantive: W(t)=1/t on (0,1] is locally
integrable in the open interval but not L1([0,1]); a finite A(0)-based
integrating factor is not furnished by this proof. We make no impossibility
claim about other formulations under weaker assumptions.

## Executable controls and their role

The primary uses exact symbolic integration/differentiation, with no numerical
ODE solver, upstream physical constants or helper import. It compares (1) to
closed analytic solutions for positive/negative constant sources, a nonzero
initial homogeneous solution, zero washout with a sign-changing source,
variable washout W=2t, and an L1 endpoint singularity W=1/sqrt(t). It verifies
the latter solution's derivative only for t>0; the proof above supplies its
absolutely continuous endpoint extension. A piecewise-constant jump fixture
checks continuity and the two interval formulas separately, as required for
an a.e. equation. Documentary note checks are provenance observations, not
mathematical evidence. Exact controls do not establish the theorem for all L1
data; that conclusion rests on the complete proof above.

## Recovery and scope

This extracts the elementary integrating-factor content historically embedded
in PR9847's transport-integral note and runner. Those older sources, their
finite BDF/trapezoid diagnostics, empirical constants, caches and broader
unresolved authority claims remain unchanged and are not certified by this
owner. This note is not their repaired physical transport theorem. No infinite
tail estimate, Boltzmann derivation, physical sign/yield mapping, HRAD closure,
source selection, new physical primitive or audit promotion is supplied.

## Command

`python3 scripts/supplied_finite_interval_signed_transport_identity_2026_10_24.py`
