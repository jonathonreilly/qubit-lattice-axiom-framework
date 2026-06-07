# Inertial Mass Is the Record-Stiffness (Generator-Invariant) — Bounded Support Toward the Equivalence-Principle Gap

**Date:** 2026-06-06
**Type:** bounded_theorem
**Claim type:** bounded_theorem — **bounded support** toward the **open** equivalence-principle gap, **not** a WEP
closure. [`EQUIVALENCE_PRINCIPLE_NOTE.md`](./EQUIVALENCE_PRINCIPLE_NOTE.md) is a meta-demotion recording that
`m_inertial = m_gravitational` is an **open derivation gap**; its closure list names **component #5: "a derivation
of a shared action coupling producing both responses with equal coefficients."** The prior inertial-mass route
[`MATTER_INERTIAL_CLOSURE_NOTE.md`](./MATTER_INERTIAL_CLOSURE_NOTE.md) is **negative** — Gaussian wave-packet
"mass" varied **123%** across packets because it was wave-packet **dispersion** (packet-width `σ` dependent), not a
generator-invariant inertial mass. This note supplies the missing piece: under
[`RECORD_DURABILITY_EQUALS_POSITIVE_MASS_CURVATURE_CONTINUOUS_DOF_BOUNDED_NOTE_2026-06-06.md`](./RECORD_DURABILITY_EQUALS_POSITIVE_MASS_CURVATURE_CONTINUOUS_DOF_BOUNDED_NOTE_2026-06-06.md)
(#2988), the inertial mass is the **record-stiffness** `m² = V''(φ₀)` — **generator-invariant**.
**Claim scope:** **conditional / bounded support**, not a closure. Conditional on (i) #2988 (record-stiffness mass,
bounded), (ii) [`BROAD_GRAVITY_DERIVATION_NOTE.md`](./BROAD_GRAVITY_DERIVATION_NOTE.md) (`ρ=|ψ|²` gravitational
source, bounded), and (iii) the **standard relativistic bridge** `E²=p²+m²` + gravity-couples-to-energy (textbook
**comparator**, not derived here). The new content is that the *common quantity is the record-stiffness* — which
fixes the named `MATTER_INERTIAL_CLOSURE` failure. It does **not** supply the other closure components (a
registered field/mass-sweep runner, an operational lattice force-observable, the full discrete mass-extraction
theorem).
**Status authority:** independent audit lane only. No effective-status change; **Independent audit required.**
**Runner:** [`scripts/audit_companion_ep_inertial_mass_is_record_stiffness_exact.py`](./../scripts/audit_companion_ep_inertial_mass_is_record_stiffness_exact.py)

## The gap and the fix

The equivalence principle on the discrete surface is open, and the prior route failed for a *specific, diagnosed*
reason: the inertial "mass" extracted from a Gaussian wave-packet's deflection was **dispersion** — it scaled with
the packet width `σ`, so it varied 123% across packets and was not a generator-invariant property of a localized
object (`MATTER_INERTIAL_CLOSURE_NOTE`). What was missing is exactly a **generator-invariant inertial mass**.

#2988 supplies it. Reproven in the runner (sympy, 8/8):

1. **The record-stiffness is generator-invariant.** `m² = V''(φ₀)` is the curvature of the energy at the recorded
   vacuum — a property of the **durable recorded object**, with **no dependence on the state/packet width `σ`**.
   (Runner (1).) The failed route used the `σ`-**dependent** dispersion response `~1/(mσ)` — the source of the 123%
   non-universality. (Runner (2).)
2. **It is the inertial mass — directly on the lattice.** From the dispersion `E²=p²+m²`, the inertial mass is
   the rest gap `m_inertial = (d²E/dp²)⁻¹|_{p=0} = m` = the record-stiffness, `σ`-independent. (Runner (3).) And
   this needs **no continuum comparator**: the lattice dispersion `E²(p) = V''(φ₀) + (2/a²)Σ_i(1−cos p_i a)` has
   rest gap at `p=0` equal to `V''(φ₀)` **exactly on the discrete surface** — the continuum `E²=p²+m²` is only a
   low-`p` comparator, while the gap (the inertial mass) is lattice-native. (Runner (5b),(5c).)
3. **Gravity couples to the same recorded energy.** With `ρ=|ψ|²` the recorded matter density (`BROAD_GRAVITY`),
   gravity sources the recorded energy `E`; at rest `m_gravitational = E|_{p=0} = m`. (Runner (4).)
4. **Hence `m_i = m_g`, exactly and universally.** `m_grav/m_inert = 1` with **no object/packet dependence**
   (Runner (5)) — the universality the failed route lacked. Both the inertial response (the rest gap) and the
   gravitational response (the recorded-energy source) couple to the **same recorded energy**, which is the
   **shared coupling** of `EQUIVALENCE_PRINCIPLE_NOTE`'s closure component #5.

## What this is, and what it is not

| | statement | status |
|---|---|---|
| inertial mass = the record-stiffness | generator-invariant `m²=V''(φ₀)`, `σ`-independent | **bounded** (conditional on #2988) |
| fixes the `MATTER_INERTIAL_CLOSURE` failure | replaces `σ`-dependent dispersion with the invariant gap | **derived** (runner) |
| shared coupling = the recorded energy | both responses couple to it ⟹ `m_i=m_g`, ratio `1`, universal | **bounded** (closure component #5) |
| the relativistic bridge (`E=mc²`, gravity↔energy) | standard physics | **comparator** (not derived here) |
| gravity sources `ρ=|ψ|²` | from `BROAD_GRAVITY` | **bounded dependency** |
| a full WEP closure | the other closure components (sweep runner, lattice force-observable, mass-extraction theorem) | **open** (not supplied) |

**Net.** mass=recordedness contributes the one structurally-new ingredient the open EP gap needed: a
**generator-invariant inertial mass** (the record-stiffness), which is the *same* recorded energy that sources
gravity — so `m_i = m_g` follows universally, fixing the diagnosed `MATTER_INERTIAL_CLOSURE` non-universality and
supplying closure component #5. This is **support toward** the open gap, conditional on the record-stiffness mass,
the `ρ=|ψ|²` source, and the standard relativistic bridge; it is **not** the full closure.

## No-go discipline / steelman

**Strongest objection (this is just `m_i=m_g=E` from standard relativity).** The relativistic identity (inertia
and gravity both couple to energy) is standard and cited as a comparator. The **new** content is narrow and
specific: it identifies the inertial mass with the **record-stiffness** (#2988), a generator-invariant property,
which is *exactly* the ingredient the framework's own prior route (`MATTER_INERTIAL_CLOSURE`) was missing (it got
`σ`-dependent dispersion instead). Without #2988 the framework had no generator-invariant inertial mass; with it,
the shared-coupling argument goes through. **Second objection (conditional on `BROAD_GRAVITY`).** Granted — the
`ρ=|ψ|²` source is a bounded dependency, so the gravitational half is conditional. **Third objection (not a
closure).** Granted and stated: the registered sweep runner, the operational lattice force-observable, and the
full mass-extraction theorem are not supplied; this is bounded support, not closure. Parts 1–4 stand within scope.

## Forbidden-import / reprove-and-cite

The structural facts (record-stiffness `σ`-independence; the dispersion `σ`-dependence; `m_inertial = m`;
`m_grav = m` at rest; ratio `= 1`) are reproven from primitives in the runner (sympy, 8/8). The relativistic
dispersion `E²=p²+m²`, gravity-couples-to-energy, and the `m=E` rest identity are **comparators** only. No PDG
values; no fitted exponents (the retracted `MATTER_INERTIAL_CLOSURE` numbers are **not** reused).

## Dependencies (citation-graph visible)

- [`RECORD_DURABILITY_EQUALS_POSITIVE_MASS_CURVATURE_CONTINUOUS_DOF_BOUNDED_NOTE_2026-06-06.md`](./RECORD_DURABILITY_EQUALS_POSITIVE_MASS_CURVATURE_CONTINUOUS_DOF_BOUNDED_NOTE_2026-06-06.md)
- [`EQUIVALENCE_PRINCIPLE_NOTE.md`](./EQUIVALENCE_PRINCIPLE_NOTE.md)
- [`MATTER_INERTIAL_CLOSURE_NOTE.md`](./MATTER_INERTIAL_CLOSURE_NOTE.md)
- [`BROAD_GRAVITY_DERIVATION_NOTE.md`](./BROAD_GRAVITY_DERIVATION_NOTE.md)

**Independent audit required.** This note asserts no effective-status change and changes no Tier-A registry entry.
