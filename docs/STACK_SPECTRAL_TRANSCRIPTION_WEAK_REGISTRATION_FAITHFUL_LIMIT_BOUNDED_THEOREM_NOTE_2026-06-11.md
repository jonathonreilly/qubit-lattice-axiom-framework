# Stack Spectral Transcription At Weak Registration: The Record-Stack Reading Mechanism

**Date:** 2026-06-11
**Claim type:** bounded_theorem (an exactly solvable record-production stack
of the retained arrow-note class whose registered covariance transcribes the
tick band, with closed-form fidelity/strength tradeoff; grounds the
kinetic-isotropy chain's record-stack spectral reading and reduces its
residual to the record-production-dynamics reading)
**Type:** bounded_theorem
**Status authority:** independent audit lane only. This source note does not
set, predict, promote, or demote any audit outcome.
**Primary runner:**
[`scripts/stack_spectral_transcription_weak_registration_2026_06_11.py`](../scripts/stack_spectral_transcription_weak_registration_2026_06_11.py)
(SCORECARD: PASS=21, FAIL=0; cached:
[`logs/runner-cache/stack_spectral_transcription_weak_registration_2026_06_11.txt`](../logs/runner-cache/stack_spectral_transcription_weak_registration_2026_06_11.txt))

---

## What this grounds

The kinetic-isotropy retirement chain's remaining ontology-level reading is
the **record-stack spectral reading**: the layer data consumed by the OS
reconstruction is the realized tick-generated record data — the
one-spectrum identification in the scope-boundary note. Until now that
reading was a named identification with a testability property but no
constructed mechanism.

This note constructs the mechanism inside the framework's own
record-production model class — the redundant-pointer-broadcast dynamics of
the retained arrow surface
([`ARROW_FROM_RECORD_FORMATION_PAST_HYPOTHESIS_RESIDUAL_NOTE_2026-06-05.md`](ARROW_FROM_RECORD_FORMATION_PAST_HYPOTHESIS_RESIDUAL_NOTE_2026-06-05.md),
`retained_bounded`) — and computes, in closed form, exactly how faithfully a
stack of records carries the band of the tick that wrote it. After this
note, the residual is no longer "an unexplained spectral identification": it
is the **record-production-dynamics reading** named by the canonical
record-principle surface (outcome structure is supplied; production dynamics
is the open row) plus a quantified faithful-limit idealization — both named,
both strictly narrower.

## The model (the arrow-note class, with a registration-strength dial)

One fiber: a `K`/CPT-symmetric two-level carrier with tick
`u = e^{-i omega sigma_z/2}` — it satisfies `K u K^{-1} = u^{-1}`, the
spectrum-reflection class of the landed unitarity cycle
([`TICK_UNITARITY_FROM_SPECTRUM_REFLECTION_CONJUGACY_BOUNDED_THEOREM_NOTE_2026-06-10.md`](TICK_UNITARITY_FROM_SPECTRUM_REFLECTION_CONJUGACY_BOUNDED_THEOREM_NOTE_2026-06-10.md))
(runner spectrum-reflection check). Per tick, a fresh ancilla register in
`|0>` couples by the von Neumann registration
`V = exp(-i eps sigma_x (x) sigma_y)`, and is never touched again. The
registered observable is the displaced pointer `X^anc`; the system sea state
is the `K`-real maximally mixed state.

Two Record-axiom features hold **by construction and are verified exactly**:
durability (a written register's marginal is fixed once registered) and
monotone record accumulation (written-register count = stack depth — the
retained arrow surface's monotonicity, reproduced).

## The theorem (closed form, verified against exact simulation)

**Pointer-displacement identity.**
`V^dag X^a V = cos(2 eps) X^a + sin(2 eps) sigma_x (x) Z^a` exactly: the
record lands in the displaced pointer with strength `sin(2 eps)`.

**Backaction channel.** The induced per-tick system channel is
`sigma_x`-dephasing: `Phi(sx) = sx`, `Phi(sy) = cos(2e) sy`,
`Phi(sz) = cos(2e) sz` (symbolic, exact).

**Registered-sector transcription law.** The registered-sector transfer is
exactly

```text
    M(eps) = R(omega) . diag(1, cos 2 eps):
    damping      r = sqrt(cos 2 eps) = 1 - eps^2 + O(eps^4),
    frequency    cos(omega_eps) = cos(omega) g(eps),
                 g(eps) = (1 + cos 2 eps)/(2 sqrt(cos 2 eps)) = 1 + eps^4/2 + O(eps^6).
```

The `eps^2` term of `g` **vanishes identically** (symbolic series check): the
registered frequency is protected to `O(eps^4)` — the band location is
parametrically better protected than the record strength (`O(eps^2)`).

**Stack covariance recovery.** Damped-Prony recovery from the **simulated
stack's own record-record covariance** reproduces `(r, omega_eps)` to
`1e-6` at every tested strength (`eps = 0.4, 0.3, 0.2, 0.1`; 12-layer
stacks; runner covariance-recovery section). The stack carries the band.

**Faithful limit and infrared window.** Measured from the stack itself:
frequency error scales as `eps^4` (log-log slope 4.16), damping deficit as
`eps^2` (slope 2.02). The transcription is oscillatory only for
`cos(omega) g(eps) < 1`: an **overdamped infrared window**
`omega < omega_c(eps) ~ eps^2` where records are too weak to resolve the
precession (transfer eigenvalues real; runner infrared-window checks).
Outside the window the relative cone-slope error is
`~ eps^4 / (2 omega^2)`; window and error vanish together as registration
weakens. The tradeoff is **soft**: at `eps = 0.18` the band error is below
`1e-3` while the record amplitude stays finite — any target fidelity is
reachable at nonzero record strength.

## What this does to the chain

```text
  before:  "the OS-consumed layer data IS the tick-generated record data"
           -- a named one-spectrum identification, testable but
           unconstructed.
  after:   the identification's mechanism EXISTS and is exactly solvable in
           the framework's own record-production class: stacks of durable,
           monotonically accumulating records carry the tick band in their own
           covariance, faithfully in the weak-registration limit, with
           closed-form rates (eps^4 band fidelity, eps^2 strength,
           eps^2-window).
  residual: the record-production-dynamics reading -- that the realized
           stack is of this class -- plus the faithful-limit idealization.
           Both named; both strictly narrower than the bare identification.
```

The kinetic-isotropy retirement residual now reads: C- and N-readings
(spectrum-reflection transport + channel envelope), finite-period
covariance (all-periods dichotomy), and **record-production-dynamics** in
place of the bare record-stack spectral identification — every member now
has a constructed mechanism or an exact theorem behind it, and none is a
free spectral coincidence.

## Hostile witnesses (wall-independence)

| stressed wall | witness | outcome |
|---|---|---|
| weak limit | `eps = pi/4` (maximal registration) | Prony roots go real; decay exactly `(cos omega)^n`; the infrared window swallows every frequency — Zeno-type loss of the band, not of the record |
| one-spectrum discipline | second frequency interleaved | recovered band shifts by `0.27`: contamination detected, not hidden |
| infrared resolution | `omega < omega_c(eps)` | transfer eigenvalues real (overdamped): exhibited, not hidden |
| record existence | `eps -> 0` | amplitude `~ sin^2(2 eps) -> 0`: perfect transcription and records coexist only asymptotically |

## What this does not do

- It does not derive that the **realized** stack is of the broadcast class:
  that is the record-production-dynamics row named by
  [`RECORD_OUTCOME_OBSERVABLE_PRINCIPLE_CANONICAL_PROPOSAL_NOTE_2026-06-05.md`](RECORD_OUTCOME_OBSERVABLE_PRINCIPLE_CANONICAL_PROPOSAL_NOTE_2026-06-05.md)),
  inherited as the named residual.
- It does not extend to the multi-fiber/field level (a separate row); the
  single fiber is the exactly solvable case, matching the per-fiber
  structure the chain's spectral steps consume.
- It does not make the registration strength `eps` a framework constant: it
  is the model's dial, and the theorem's content is the closed-form
  dependence on it.
- It does not modify the arrow note's past-hypothesis residual (the arrow
  remains the initial condition; this note's stack inherits it).
- It does not add an axiom or primitive, and it does not set audit status.

## Falsifiers

- A symbolic failure of the displacement or dephasing forms.
- A simulated stack covariance deviating from `M(eps)^n` structure beyond
  numerical tolerance (would refute the transcription and covariance-recovery
  laws).
- A nonzero `eps^2` coefficient in `g(eps)` (would refute the `O(eps^4)`
  protection).
- An oscillatory transcription inside the window or an overdamped one well
  outside it (would refute the window law).
- A second-dynamics contamination that recovery fails to detect (would
  refute the stack-level one-spectrum testability).

## Dependencies

- [ARROW_FROM_RECORD_FORMATION_PAST_HYPOTHESIS_RESIDUAL_NOTE_2026-06-05.md](ARROW_FROM_RECORD_FORMATION_PAST_HYPOTHESIS_RESIDUAL_NOTE_2026-06-05.md)
  — the model class and the monotone-accumulation surface
  (`retained_bounded`).
- [RECORD_OUTCOME_OBSERVABLE_PRINCIPLE_CANONICAL_PROPOSAL_NOTE_2026-06-05.md](RECORD_OUTCOME_OBSERVABLE_PRINCIPLE_CANONICAL_PROPOSAL_NOTE_2026-06-05.md)
  — the named record-production-dynamics residual this note reduces the
  record-stack spectral reading to.
- [TICK_UNITARITY_FROM_SPECTRUM_REFLECTION_CONJUGACY_BOUNDED_THEOREM_NOTE_2026-06-10.md](TICK_UNITARITY_FROM_SPECTRUM_REFLECTION_CONJUGACY_BOUNDED_THEOREM_NOTE_2026-06-10.md)
  — the spectrum-reflection class the model tick instantiates; landed but
  unaudited, conditionality inherited.
- [SINGLE_CLOCK_UNIQUENESS_SCOPE_BOUNDARY_2026-06-06.md](SINGLE_CLOCK_UNIQUENESS_SCOPE_BOUNDARY_2026-06-06.md)
  — the one-spectrum discipline; the second-dynamics witness is its
  stack-level content.
- [MINIMAL_AXIOMS_2026-06-05.md](MINIMAL_AXIOMS_2026-06-05.md)
  — the Record axiom whose durability clause the construction realizes.
- [KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md](KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md)
  and
  [KINETIC_ISOTROPY_PRIMITIVE_IRREDUCIBILITY_SUPPORT_2026-06-09.md](KINETIC_ISOTROPY_PRIMITIVE_IRREDUCIBILITY_SUPPORT_2026-06-09.md)
  — the retirement chain's target and independence surface (this note
  continues through the steelman door named there).

**No-promotion statement:** this note does not promote, demote, or set the
audit status of any dependency or of the kinetic-isotropy primitive. The
independent audit lane is the only status authority.
