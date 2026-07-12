## Science block

This block resolves the stale Rconn prompt at the narrowest supportable level.
It proves that independent endpoint gauge rotations force the legacy separated
open-bilocal trace statistic to have ideal equilibrium expectation
`(N_c^2-1)/N_c^2`, while diagonal conjugation permits independent singlet and
adjoint weights. It does not identify that gauge-frame statistic with a
physical connected-current ratio or derive `kappa_EW = 0`.

- [Bounded theorem note](https://github.com/jonathonreilly/cl3-lattice-framework/blob/physics-loop/rconn-equivariant-kernel-obstruction-block01-20260712/docs/RCONN_ENDPOINT_GAUGE_FRAME_DICHOTOMY_BOUNDED_THEOREM_NOTE_2026-07-12.md)
- [Deterministic certificate runner](https://github.com/jonathonreilly/cl3-lattice-framework/blob/physics-loop/rconn-equivariant-kernel-obstruction-block01-20260712/scripts/frontier_rconn_endpoint_gauge_frame_dichotomy.py)
- [Trace gate](https://github.com/jonathonreilly/cl3-lattice-framework/blob/physics-loop/rconn-equivariant-kernel-obstruction-block01-20260712/.claude/science/physics-loops/rconn-endpoint-gauge-frame-dichotomy-20260712/TRACE_GATE.md)
- [Claim-status certificate](https://github.com/jonathonreilly/cl3-lattice-framework/blob/physics-loop/rconn-equivariant-kernel-obstruction-block01-20260712/.claude/science/physics-loops/rconn-endpoint-gauge-frame-dichotomy-20260712/CLAIM_STATUS_CERTIFICATE.md)
- [Review history](https://github.com/jonathonreilly/cl3-lattice-framework/blob/physics-loop/rconn-equivariant-kernel-obstruction-block01-20260712/.claude/science/physics-loops/rconn-endpoint-gauge-frame-dichotomy-20260712/REVIEW_HISTORY.md)
- [Handoff](https://github.com/jonathonreilly/cl3-lattice-framework/blob/physics-loop/rconn-equivariant-kernel-obstruction-block01-20260712/.claude/science/physics-loops/rconn-endpoint-gauge-frame-dichotomy-20260712/HANDOFF.md)

The current canonical `RCONN_DERIVED_NOTE.md` row remains untouched at its
already-audited no-go state. No audit verdict, publication surface, primitive
registry, lane registry, or repo-wide audit authority surface is changed.

## Verification

- New deterministic runner: `PASS=55 FAIL=0` for `N_c=2,3,4,5` orbit,
  projector, kernel, inequivalence, asymptotic, and source-boundary checks.
- Independent SymPy reduction: both rational identities and the equal-weight
  condition pass independently of the runner implementation.
- Regression runners: Rconn matching no-go `30/0`; EW matching-rule no-go
  `56/0` fatal and `25/0` motivation; EW object pin `20/0`.
- Runner cache freshness and Python compilation pass.
- Controlled-vocabulary lint and `git diff --check` pass.
- Audit pipeline and strict audit lint are run for compatibility only; their
  generated authority-surface changes are stripped before delivery.

## Review disposition

Two review iterations conclude: code `PASS`, physics `BOUNDED`, imports
`CLEAN`, Nature `BOUNDED`, No-Go Discipline `PASS`, labeling `PASS`, repo
governance `PASS`, and audit compatibility `PASS`. The block still requires
the independent audit lane before any retained-grade effective status.

## Remaining blockers outside this bounded theorem

1. A gauge-invariant physical current/readout definition.
2. Action-specific singlet/adjoint reduced weights, including any finite
   equality needed by the physical claim.
3. Continuum matching that selects or bounds `kappa_EW`.
