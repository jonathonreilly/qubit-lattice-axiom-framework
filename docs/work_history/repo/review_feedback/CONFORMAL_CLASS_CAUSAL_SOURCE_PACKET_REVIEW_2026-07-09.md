# Conformal-Class Causal-Source Packet Review (Repair Before Audit)

**Date:** 2026-07-09
**Type:** meta
**Archive role:** detailed review evidence; the live decision surface is
`docs/repo/ACTIVE_REVIEW_QUEUE.md`
**Status authority:** independent audit lane only. This note reports
verified defects and safe reduced claims; it neither retains nor
rejects anything.
**Method:** two adversarial worker reviews (gpt-5.6-sol/max,
refute-first charter), every load-bearing finding then independently
verified by the supervisor against the current files, and all three
runners supervisor-executed on 2026-07-09. Only verified findings
appear here.

## Headline

The metric's conformal-class assembly
([`EMERGENT_METRIC_CONFORMAL_CLASS_FROM_RECORDS_SCALE_IS_THE_CLOCK_RATE_NO_GO_NARROW_THEOREM_NOTE_2026-06-06.md`](../../../EMERGENT_METRIC_CONFORMAL_CLASS_FROM_RECORDS_SCALE_IS_THE_CLOCK_RATE_NO_GO_NARROW_THEOREM_NOTE_2026-06-06.md))
is listed as conditional on two unaudited inputs. Sending those two
inputs to audit NOW would waste the audit lane: both need repair
first, and the consumer itself has a live defect that would
misinterpret even clean audits. Nothing here disturbs the season's
gravity-chain results, which do not route through this packet.

## Verified defect register

### A. Record-order input
([`RECORD_HISTORY_ORDER_TIME_RATE_FIREWALL_2026-06-05.md`](../../../RECORD_HISTORY_ORDER_TIME_RATE_FIREWALL_2026-06-05.md))

- **A1 (critical, type laundering).** The note's own 2026-06-17 repair
  states: "This row is not a positive time/rate theorem. Its source
  payload is negative route pruning... this row only prevents
  downstream notes from importing them from record-history order
  alone." The downstream consumer nevertheless uses it POSITIVELY as
  its "record event order / prefix-count axis", and the downstream
  runner marks the row `load_bearing_causal_input: True` while its
  `RETAINED_STATUSES` set includes `retained_no_go`
  (`emergent_metric_conformal_class_from_records_runner.py:28-38`). A
  clean audit of the NEGATIVE claim would mechanically read as
  ratification of the POSITIVE premise. Verified verbatim.
- **A2 (critical, missing bridge).** No cited authority constructs the
  map record atom -> formation event -> causal/chronological order on
  the same event set as the light cone. The post-reset comparability
  note states the wall explicitly: the landed sentences supply no
  causal dependency relation among formation events
  (`RECORD_COMPARABILITY_IMPORT_DISCIPLINE_...2026-07-07.md`). The
  "order" the runners test is index order of hard-coded Python lists
  (true by construction).
- **A3 (high, premise migration).** The note still cites the
  superseded 2026-06-05 axiom memo. Under the current axioms the
  record object is a site-tagged locked admissible possibility;
  serialization of spacelike formations is exactly the choice the
  Qualification clause forbids without admission.
- **A4 (safe reduced claim, worth auditing after a scope split).**
  Given a supplied abstract order/word and optional per-step kernel
  with no clock datum, order and counts do not determine durations,
  rates, a generator, or clock normalization. The runner's Poisson and
  two-grid witnesses support exactly this and nothing more
  (supervisor-executed: 44/44, exit 0, matches cache).

### B. Microcausality input
([`RECONSTRUCTED_H_QUASILOCAL_FROM_ANALYTIC_DISPERSION_MICROCAUSALITY_BRIDGE_NARROW_THEOREM_NOTE_2026-06-06.md`](../../../RECONSTRUCTED_H_QUASILOCAL_FROM_ANALYTIC_DISPERSION_MICROCAUSALITY_BRIDGE_NARROW_THEOREM_NOTE_2026-06-06.md))

- **B1 (critical, spectrum misidentification).** The note writes
  `spec(T^2) = e^{-2E(p)} in [e^{-2E_max}, e^{-2E_min}]`. Its own
  cited RP authority gives the full Fock operator
  `T^2 = tensor_p diag(1, e^{-2E(p)})` with norm 1 (vacuum): the
  vacuum eigenvalue lies outside the claimed interval, and
  multiparticle products lie below it. The claimed interval is the
  ONE-PARTICLE contraction spectrum. Verified against both notes.
- **B2 (major, normalization drop).** The note defines
  `H = -log(T^2)/(2 a_tau)` and then writes `H = E(p)`; the correct
  display is `E(p)/a_tau`. Harmless for decay, load-bearing for any
  velocity or cone slope.
- **B3 (critical for the downstream use).** The packet contains no
  quasilocal Lieb-Robinson composition (the note itself says the tail
  composition remains open), and exponential tails are not a strict
  cone: Malament/HKM rigidity consumes an exact causal relation, not
  a non-sharp upper envelope whose slope depends on the chosen weight.
- **B4 (safe reduced claim).** For the supplied free one-particle
  symbol at fixed m > 0, the one-coordinate contour argument gives
  exponentially decaying kernel coefficients (supervisor-executed:
  9/9, exit 0, matches cache). The "complex strip" phrase should be
  narrowed to the one-coordinate strip (the simultaneous polystrip of
  the same width is false: R vanishes at every p_mu = i*arcsinh(m/
  sqrt(d))). The m = 0 statement "H(x) ~ x^-4" holds for the d = 3
  axis marginal, not as a general-d exponent.

### C. The consumer runner
([`scripts/emergent_metric_conformal_class_from_records_runner.py`](../../../../scripts/emergent_metric_conformal_class_from_records_runner.py))

- **C1 (critical, broken exit semantics — live-confirmed).** `main()`
  counts failures but returns nothing, and the module calls `main()`
  bare, so the process exits 0 regardless. Supervisor execution
  2026-07-09: `TOTAL: PASS=48 FAIL=4`, exit 0. The repo cache
  (3 FAILs, header `status: ok`) is already stale against live status
  drift. Any tooling that trusts exit codes or the `ok` header is
  being misled today.
- **C2 (high, observable substitution).** The runner computes a
  maximum SAMPLED GROUP VELOCITY of the dispersion on a 31^3 grid and
  prints it as "finite LR-cone diagnostic v_LR" behind an arbitrary
  `0 < v < 10` gate. Group velocity is not the Lieb-Robinson velocity
  of a quasilocal interaction; no theorem in the packet connects them.
- **C3.** The "record-prefix order" input to the packet gate is a
  hard-coded five-symbol list whose prefix lengths increase by
  construction.

## Repair list (cheapest honest path, in order)

1. Scope-split the record-order note: keep it as the pure no-go (A4
   wording), remove causal-order language from its downstream unlocks.
2. Author the missing positive bridge as its own note: record/formation
   events, the supplied or derived successor relation, spacelike
   incomparability, and cone-compatibility on one event set — or park
   the conformal-class assembly as conditional on a NAMED absent
   bridge rather than on this no-go.
3. Narrow the microcausality note to the one-particle statement (B1,
   B2, B4 wordings) and add the quasilocal-LR composition dependency
   explicitly (the later transfer-log/LR-bridge notes are candidates,
   themselves unaudited).
4. Fix the consumer runner's exit semantics (`raise SystemExit(1 if
   FAIL else 0)`), replace the group-velocity print with an honestly
   labeled diagnostic, drop `retained_no_go` from positive
   load-bearing acceptance, and regenerate its cache.
5. Only then queue the two inputs for independent audit.

## Three questions for whoever picks this up

1. What typed map takes a site-tagged record to a formation event and
   then to the causal order on the cone's event set — and where is it
   proved rather than defined?
2. Which object does the cone input actually name: one-particle group
   velocity, a quasilocal LR velocity (for which weight), or a sharp
   front — and which one does Malament rigidity lawfully consume?
3. Should `retained_no_go` ever satisfy a positive load-bearing gate
   anywhere in the runner fleet? (A fleet-wide grep for this pattern
   is cheap and likely worth it.)
