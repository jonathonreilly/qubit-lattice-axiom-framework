# The Poisson susceptibility discriminator measures the wrong direction — Cycle 694

Date: 2026-07-25

Claim type: bounded_theorem

Authority: none. Audit: unset. Constitutional effect: none. No new axiom or
primitive is proposed or adopted.

Runner: `scripts/physical_poisson_susceptibility_direction_repair_cycle694_2026_07_25.py`
(5 PASS / 0 FAIL, exit 0).

## The question

[Self-consistency forces Poisson](SELF_CONSISTENCY_FORCES_POISSON_NOTE.md) is
`audited_conditional`, criticality `critical`, load-bearing 18.1, with 778
transitive descendants. Its audit rationale carries a live numerical objection:

> "the measured susceptibility decays as r^(-2.805), despite the claimed
> Poisson-kernel interpretation. The note correctly names finite-family and
> linear-response limitations, but a response-kernel bridge is still missing."

An exponent near 2.8 against a 1/r target is a large discrepancy. This cycle
locates its cause.

## Result

**The objection is correct as stated, and the cause is an
observable-identification error rather than a failure of the Poisson reading.**

**1. The Poisson direction is not anomalous.** The Poisson kernel is the
source-to-field direction, `delta_phi/delta_rho = (-Laplacian)^{-1}`. Solved
here on a Dirichlet box with a declared intermediate fit window, its fitted
exponent is

| box `N` | intermediate-window fit | naive full-range fit |
|---|---|---|
| 25 | 1.471 | 1.576 |
| 31 | 1.398 | 1.579 |
| 41 | 1.364 | 1.583 |

decreasing monotonically toward the continuum target 1. The parent note's own
reported `beta ~ 1.28`, which it already flags as a finite-size effect, sits in
this family. Nothing about the field decay needs repair.

**2. The fit window is load-bearing.** On identical data the naive and declared
windows differ by more than 0.1 at every size. An exponent quoted against a
continuum target without a declared window is not a comparison. This is why the
cycle reports both.

**3. The parent runner measures the opposite direction.**
`compute_susceptibility_profile` applies a **field** bump `delta_phi` over a
3×3×3 neighbourhood, propagates a wavepacket, and returns

```text
delta_rho / delta_phi     with  delta_rho = sum |rho_p - rho_0|
```

while its own docstring asserts *"this response kernel is the inverse
Laplacian"*. Those are inverse operators; only `delta_phi/delta_rho` is the
Poisson kernel. The runner verifies both facts against the parent source on the
tree it runs on.

**4. The forward operator is local.** `(-Laplacian)` on a nearest-neighbour
lattice has stencil support radius 1 (7 nonzero entries, verified). A
`delta_rho/delta_phi` response therefore has **no power-law Green's-function
tail at all**, so an exponent extracted from it has no 1/r expectation to fail
against.

## The repair

- **Measure** `delta_phi/delta_rho`: perturb the source density at the probe
  site and measure the field response.
- **Declare** a fit window, and report the naive-window value alongside so the
  choice is auditable.
- **Expect** an exponent above 1 at accessible box sizes, drifting downward;
  1.3–1.5 at `N = 25–41` is the finite-size signature, not a defect.
- **Stop concluding** that a `delta_rho/delta_phi` exponent near 2.8 refutes a
  Poisson reading.

## Scope — what this does NOT do

This cycle repairs the **numerical discriminator only**. It does **not** supply
the missing source/action or physical-observable bridge that the gravity lane's
four conditional rows share, and it makes **no gravity claim**. The five-judge
panel's finding on that lane — that "the minimal-axiom authority expressly
withholds dynamics, weights, source/action, and physical-observable bridges,
while the runner stipulates each of those ingredients" — stands untouched by
this cycle. That bridge remains open.

## Firewalls

- No gravity, Newtonian, or field-equation claim is made.
- No source/action bridge is supplied; no physical observable is identified.
- A lattice Green's function is not a physical potential, and is not called one.
- No axiom or primitive is proposed or adopted.

## Scope for independent review

Box sizes 25/31/41 with Dirichlet walls and two declared fit windows; the
locality result is exact stencil inspection. Larger boxes, other boundary
conditions, massive kernels, and the parent's full self-consistency loop are
outside scope and untested. The N1–N8 verdict remains reviewer-owned.

## Dependency citations

The runner imports only numpy/scipy and reads the parent runner's source to
verify what it measures. It cites
[Self-consistency forces Poisson](SELF_CONSISTENCY_FORCES_POISSON_NOTE.md) for
the obstruction text and the discriminator under repair.
