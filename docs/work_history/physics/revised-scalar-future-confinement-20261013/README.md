# Future-confinement milestone evidence

As of October 13, 2026. This directory preserves the author and focused-checker
evidence for the conditional exponential-scalar future-confinement theorem.
It assigns no effective audit status and records no formal audit.

The active scientific source is `docs/EXPONENTIAL_SCALAR_FUTURE_CONFINEMENT_BOUNDED_THEOREM_NOTE_2026-10-13.md`;
the self-contained primary runner is `scripts/exponential_scalar_future_confinement_check.py`.
Run it from a checkout with Python, SymPy and mpmath installed. The canonical
cache is `logs/runner-cache/exponential_scalar_future_confinement_check.txt`.
The runner reported 22 checks passed and zero failed; actual damaged copies
rejected seven coefficient/sign changes. A finite runner supports, but does
not substitute for, the handwritten continuation and convergence proof.

`evidence_v1.tar.gz` is an immutable recovery archive with only regular files.
Extract into a fresh temporary directory. Its `ARCHIVE_MANIFEST.json` gives
every constituent path, byte count and SHA-256. Original absolute source paths
in historical receipts are preserved as provenance; snapshots and artifact
paths inside the archive make their reviewed bytes recoverable without those
original worktrees. No absolute runtime path is needed by the canonical runner.

Archive SHA-256: `482f665431162b2abd95ec337ae49f98e38c02dbeb322519446fd4a5d562b2e9`.

The most relevant extracted records are:

- `campaign/initial_state/independent_energy_v1/REPORT_v1.md` and
  `HAND_DERIVATION_v1.md`: complete independent proof check, including
  normalization and future-fluid-domain clarifications.
- `campaign/initial_state/independent_energy_v1/RECEIPT_v1.json`: 41 artifacts,
  receipt `44c051a7684b86f60da27dd020801040d5aeecd5693f828dc7826382f8da3559`.
  Thirteen symbolic identities, six 80-digit arbitrary states, six damaged
  controls and seven finite-time trajectories were checked independently.
- `campaign/initial_state/independent_energy_v1/canonical_packaging_v1/REPORT_v1.md`
  and `RECEIPT_v1.json`: the same checker's final-source correspondence check,
  receipt `4e898ddd19104b9c1679835e1be0a33f677a1f0890b929429602e0abdd4837a8`.
  The original 41 artifacts remained unchanged. The 117 packaging inspection
  items are mostly provenance checks, not additional physics results.
- `campaign/initial_state/canonical_controls_v1/MUTATION_RECEIPT.json` and
  the seven actual damaged sources/outputs: friction, trace sign, coupling
  denominator, Phi normalization, fluid dilution, integral coefficient and
  convergence coefficient controls.
- `campaign/initial_state/FUTURE_PROTOCOL_v1.json` and `future_evidence_v1/`:
  18 author solver runs over nine exact decimal initial states, two solvers
  each; six runs use k=0 and are explicitly outside the fixed-positive-k
  theorem. These are diagnostics, not a rigorous enclosure of the preceding
  cosmological history or independent observational tests.

The archive also preserves inherited source bytes, initial-state probes and
radiation diagnostics needed to reproduce those contextual trajectories.
Those are not additional canonical claims or premises of the self-contained
future theorem. The original reviewer serialization failure and its original
code/output remain present. No failed result was replaced by a success log.

Focused source, identity, premise, vocabulary and diff checks precede this PR.
The combined current-main integration pipeline, strict lint and changed-evidence
pass remain pending for the eventual landing review. This campaign does not
merge science or run formal audits.
