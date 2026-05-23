# Born Rule Negative — Interpretive Conditional Reading

**Date:** 2026-04-11 (interpretive scope narrowed 2026-05-23)
**Claim type:** bounded_theorem (interpretive conditional reading; the
negative conclusion "gravity does not select α=2" is stated as a
CONDITIONAL on two NAMED EXTERNAL ADMISSIONS that are explicitly OUT
OF SCOPE of this note; this note does not derive either admission).
**Status authority:** independent audit lane only. This source note
does not set or move its own audit verdict; downstream audit lane and
packet status are decided by the audit lane.
**Primary runner:** None. This is an interpretive note only; no
runner is supplied, and no derivation of the contraction-rate ranking
is performed here.

## 0. Why this note exists (scope discipline)

The 2026-05-10 audit verdict (`audited_failed`) on the prior framing
of this note recorded the following claim boundary:

> "Claim boundary until fixed: this is only an interpretive note about
> what a prior Hartree convergence test would mean if the stated PDE
> comparison were established."

This revised note adopts EXACTLY that claim boundary. It does not
attempt to repair the missing derivation; it scopes the note to
INTERPRETIVE content only, with the two load-bearing structural
inputs declared OUT OF SCOPE as named external admissions.

In particular, this note does NOT claim to derive:
- the Hartree-loop contraction-rate ranking
  `α=1.0 < 1.5 < 2.0 < 3.0 < 4.0` (no Banach-map hypotheses, no
  Lipschitz proof, no completed runner is supplied);
- the measurement/dynamics layer separation (asserted, not closed
  within this packet).

What this note DOES claim is conditional: IF those two admissions are
supplied by an external authority (proof note or completed runner),
THEN their joint reading is that gravitational self-consistency under
the Hartree test does not pick out α=2.

## 1. Named external admissions (explicitly OUT OF SCOPE)

The conditional reading rests on two NAMED EXTERNAL ADMISSIONS. This
note does not provide either; both must be sourced from elsewhere to
upgrade the conditional reading.

- **(X1) Hartree contraction-rate ranking (admission, not derived).**
  Under some suitable norm and Banach-map hypotheses, the
  fixed-point map ψ → V(|ψ|^α) → H(V) → ψ' contracts strictly faster
  for α < 2 than for α = 2 than for α > 2. CONCRETELY ADMITTED form:
  the Lyapunov ordering
  `α = 1.0 < 1.5 < 2.0 < 3.0 < 4.0`. This admission is NOT proven
  here; no Banach-map hypotheses are stated, no Lipschitz inequality
  is derived, no runner is registered. The textbook intuition is
  recorded in §3 only as MOTIVATION for what such an admission would
  look like, not as a derivation.
- **(X2) Measurement/dynamics layer separation (admission, not
  derived).** The Born rule is a MEASUREMENT postulate (interface
  between quantum state and classical observables); gravitational
  self-consistency is a DYNAMICS statement (how ψ and Φ co-evolve).
  These are different levels of the theoretical stack. This note
  asserts but does not close the layer separation; a proof would
  require a separate scoped claim (e.g., a no-go that unitary
  dynamics alone, with no environment / measurement structure, cannot
  distinguish α values).

## 2. Interpretive theorem (conditional)

**Interpretive reading (conditional on (X1) and (X2) as named external
admissions).** Given (X1) and (X2) as stated in §1:

1. **(Conditional on X1)** A Hartree-loop convergence test that
   measures Banach fixed-point contraction rate would rank α values
   according to source-term regularity, with lower α giving faster
   convergence. The minimum of that Lyapunov ranking would NOT be at
   α=2. Hence the convergence test alone would NOT select the Born
   exponent.
2. **(Conditional on X2)** Because the test under (X1) operates at
   the dynamics layer (deterministic, unitary co-evolution of ψ and
   Φ), it does NOT probe the measurement-layer object the Born rule
   addresses (probability of finding the particle at x). The
   convergence test is therefore SILENT on the Born rule by
   construction of the layer separation.
3. **(Interpretive conclusion)** Conditional on (X1) and (X2), the
   reading is: "gravitational self-consistency under the Hartree test
   does not select α=2" should not be read as evidence against the
   Born rule. It should be read as evidence that the Hartree loop
   does not couple to the Born rule's natural domain.

The conclusion is NOT a no-go theorem against α=2 selection by any
other carrier; it is a reading of what the Hartree test would say
about α=2 if (X1) and (X2) held.

## 3. Motivation for (X1) (NOT a derivation)

The motivation for (X1) — recorded for reading-comprehension only,
NOT as a derivation — is the textbook expectation for elliptic PDE
fixed-point iteration with source term `|ψ|^α`:

- α < 2: sublinear source → smoother source term → motivation
  suggests faster contraction;
- α = 2: Born rule → standard density;
- α > 2: superlinear source → rougher source term → motivation
  suggests slower contraction.

The Lyapunov ordering `α=1.0 < 1.5 < 2.0 < 3.0 < 4.0` is the textbook
Banach-contraction-mapping motivation. To upgrade this paragraph from
motivation to (X1) requires: (a) explicit choice of function-space
norm; (b) explicit Banach-map hypotheses on the H(V) solver; (c) an
explicit Lipschitz inequality on |ψ|^α as a multiplier; (d) a proof
or runner registering the resulting contraction-rate ordering. None
of (a)-(d) is supplied here.

## 4. Motivation for (X2) (NOT a derivation)

The motivation for (X2) — recorded for reading-comprehension only,
NOT as a derivation — is the standard physics intuition for the
quantum-theory layering:

- Dynamics: deterministic, unitary co-evolution preserving the full
  function |ψ(x)| up to phases.
- Measurement: probabilistic, non-unitary collapse interfacing the
  quantum state with classical observables.

The textbook reading is that unitary dynamics cannot distinguish α
values because it preserves the entire function |ψ(x)| up to phases;
the Hartree loop in this framing never asks "what is the probability
of finding the particle at x?". To upgrade this paragraph from
motivation to (X2) requires a separately scoped claim — e.g., a no-go
that the Hartree dynamics map factors through `|ψ|^α` in such a way
that the choice of α does not couple to any observable in the
restricted (dynamics-only, no environment) packet.

## 5. What this interpretive reading positively claims

1. The note adopts the verdict-recorded "claim boundary": it is only
   an interpretive note about what a prior Hartree convergence test
   would mean IF the stated PDE comparison were established.
2. Under the two named external admissions (X1) and (X2), the
   interpretive reading is that gravity (as probed by Hartree
   self-consistency) does NOT select α=2.
3. The interpretive reading is independent of the framework's
   spectral results (area law, CDT flow, sign selectivity); those
   depend on the spectrum of H, which exists regardless of α and
   does not require either admission.
4. Downstream notes that cite this note for the LAYER-SEPARATION
   reading (Born = measurement, gravity = dynamics) cite (X2) as an
   admission, NOT as a derivation. This is the only role this note
   plays in those downstream chains.

## 6. What this interpretive reading does NOT claim

- Does NOT derive the Hartree contraction-rate ranking; (X1) is a
  NAMED EXTERNAL ADMISSION.
- Does NOT close the measurement/dynamics layer separation; (X2) is
  a NAMED EXTERNAL ADMISSION.
- Does NOT state Banach-map hypotheses or supply a Lipschitz
  inequality.
- Does NOT register a primary runner; helper_runner_paths empty.
- Does NOT prove a no-go that gravity cannot select α=2 by any
  carrier. The conclusion is conditional on (X1)+(X2) and silent on
  other carriers.
- Does NOT make a measurement-level claim about the Born rule itself
  (e.g., does not derive p(x) = |ψ(x)|² from any axiom).
- Does NOT promote downstream notes that cite this one; downstream
  citations of the layer-separation reading are themselves
  conditional on (X2) being supplied externally.
- Does NOT introduce new repo vocabulary; "Banach contraction,"
  "Hartree iteration," "Lyapunov ranking," "measurement postulate,"
  "dynamics" are standard textbook vocabulary.

## 7. What this means for the model (under (X1)+(X2))

CONDITIONAL on (X1) and (X2):

- The framework's spectral results (area law, CDT flow, sign
  selectivity) are robust against α, since they depend on the
  spectrum of H rather than on which probability measure is laid on
  |ψ|.
- Trajectory results (Penrose, DP, BH) that depend on the Born rule
  through the density-matrix formalism need additional structure
  beyond what this Hartree loop probes (e.g., environment +
  decoherence).
- Gravity and quantum probability are LOGICALLY INDEPENDENT at the
  level the Hartree test probes — a CONDITIONAL reading that
  confirms the standard physics intuition under (X1)+(X2), not a
  framework-wide no-go.
- To convert this conditional reading into a structural prediction,
  one would need a separately scoped many-body + environment +
  decoherence claim asking whether the resulting mixed-state dynamics
  is α-sensitive. That is OUT OF SCOPE here.

## 8. Audit verdict acknowledgment (2026-05-23)

The 2026-05-10 audit verdict (`audited_failed`) flagged that:

> "the load-bearing contraction-rate theorem is stated, not derived,
> and no one-hop authority or completed runner is supplied. Why this
> blocks: the negative conclusion that gravity does not select α=2
> rests on that unverified fixed-point ranking plus a
> measurement/dynamics separation that is asserted rather than closed
> in the restricted packet. Repair target: supply a bounded theorem
> with explicit Banach-map hypotheses and proof, or a runner/log that
> computes the contraction ranking under stated norms, and separately
> scope the measurement-level independence claim. Claim boundary
> until fixed: this is only an interpretive note about what a prior
> Hartree convergence test would mean if the stated PDE comparison
> were established."

The narrow repair (2026-05-23) ACCEPTS the verdict's claim boundary
verbatim and adopts it as this note's only scope:

- The Hartree contraction-rate ranking is moved to (X1) — NAMED
  EXTERNAL ADMISSION, explicitly OUT OF SCOPE.
- The measurement/dynamics separation is moved to (X2) — NAMED
  EXTERNAL ADMISSION, explicitly OUT OF SCOPE (and noted as needing
  a separately scoped claim per the verdict's guidance).
- The note's positive content is reduced to the CONDITIONAL
  interpretive reading: under (X1) and (X2), the Hartree test does
  not select α=2 — which is exactly the "interpretive note" boundary
  the auditor preserved.
- The note's `claim_type` is `bounded_theorem` (the conclusion is
  conditional on external admissions; no positive derivation is
  claimed here).
- No runner is registered. `helper_runner_paths` empty. The repair
  does NOT attempt to invent a Banach-map proof.

Re-audit is invited under the narrowed interpretive scope; a future
proof note or completed runner for (X1) (Hartree contraction ranking
under named norms) and a separately scoped claim for (X2) (dynamics-
only layer separation) would be the standard route to upgrade the
admissions and lift conditionality.

## 9. Cited dependencies

This interpretive note cites only the two NAMED EXTERNAL ADMISSIONS
(X1), (X2). It does NOT promote any other note's status; it relies on
no retained authority load-bearingly; and it has no markdown-link
dependencies that the citation-graph parser must follow.

Downstream notes that cite this note (e.g.,
[`G_NEWTON_BORN_AS_SOURCE_POSITIVE_THEOREM_NOTE_2026-05-10_gnewtonG2.md`](G_NEWTON_BORN_AS_SOURCE_POSITIVE_THEOREM_NOTE_2026-05-10_gnewtonG2.md),
[`HIGGS_MASS_S4_BORN_EXTENSION_BOUNDED_NOTE_2026-05-10_higgsS4.md`](HIGGS_MASS_S4_BORN_EXTENSION_BOUNDED_NOTE_2026-05-10_higgsS4.md),
[`CLOSURE_T2_GNEWTON_REAUDIT_NOTE_2026-05-10_t2gnewton.md`](CLOSURE_T2_GNEWTON_REAUDIT_NOTE_2026-05-10_t2gnewton.md),
[`CLOSURE_C_BB_F2_1_CORRECTION_NOTE_2026-05-10_cBB_correction.md`](CLOSURE_C_BB_F2_1_CORRECTION_NOTE_2026-05-10_cBB_correction.md))
cite the layer-separation reading (X2) as a NAMED EXTERNAL ADMISSION
themselves; this note does not upgrade that admission for those
downstream chains.

## 10. Forbidden-imports check

- No new axiom introduced.
- No new repo vocabulary.
- No PDG / experimental observable consumed.
- No `audit_status` or `effective_status` promotion language; status
  authority is independent audit lane only.
- No load-bearing reliance on unaudited authorities; the two
  load-bearing structural inputs are NAMED EXTERNAL ADMISSIONS,
  explicitly OUT OF SCOPE.
- No runner registered; no completed runner is claimed.
- Citation form: markdown links for downstream-cited notes (none
  required by this note's own argument; cross-references for context
  only).
