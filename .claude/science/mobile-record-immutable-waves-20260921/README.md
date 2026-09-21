# Immutable record waves — review evidence

This packet supports the adjacent conditional theorem note and its exact
runner. Its base is main `5d784d8ccda5268f2b7c056fcdf0d81fdb703319`.
The author personally derived and assembled the construction and proofs;
one separate checker reconstructed the load-bearing arguments and performed
selective finite controls. This is not an independent audit verdict.

The supplied model has seven local states, immutable labels, four-site read
context, nearest-neighbor exchanges including occupied-occupied swaps, and a
fixed positive rate floor. It supports an isotropic linear acoustic pair at
every interior isotropic density for nonzero coupling, a smooth-profile Euler
limit, and a stationary finite-mode fluctuation limit. Uniform slow births
are included only in the smooth-profile theorem. The model's alphabet, rates
and clock are assumptions; the framework's four axioms do not select them.

## Evidence map

- `PRIMARY_RESULTS.json`, `AUTHOR_RUNS.json`, `AUTHOR_VERIFICATION.json`:
  final source-bound author baseline and all seven declared mutations. Their
  complete stdout/stderr is preserved. Finite checks do not prove limit
  theorems.
- Four `independent_*.zip` capsules: exact sealed reconstruction reports,
  independent scripts and raw attempts, with their original dependency hashes.
  `INDEPENDENT_CAPSULES.json` maps them. The readable report copies are byte
  identical to the archived reports. Run `verify_capsules.py` to authenticate
  all four capsules, 41 artifacts and 15 dependency links.
- `final_source_review/`: full review of the actual publication note and
  runner, a selective complete-generator check, its raw log and source seal.
  The review found an omitted nonzero-coupling qualifier in the summary.
  `CORRECTION_ACK.json` checks the entire two-location correction and closes
  that finding. The theorem body and runner were unchanged.
- `before_alpha_scope_correction/`: exact reviewed note, primary evidence and
  canonical cache before that narrow correction. These preserve the original
  review seal's dependencies after final source-dependent evidence refresh.
- `author_development/`: earlier unsuccessful author runs and their exact
  sources. They are historical snapshots, not alternate current runners.
- `VALIDATION.json`: final source identities, graph delta, cache freshness,
  vocabulary and compile checks, evidence authentication and explicit pending
  landing gates.
- `RAW_EVIDENCE_WHITESPACE.json`: the sole full-diff whitespace finding is
  the original blank line after the historical cache's empty stderr section.
  Its bytes are preserved; all other staged files pass the whitespace check.

## Reproduction and limits

From the repository root:

```bash
python3 scripts/mobile_records_immutable_context_exchange_acoustic_limits_2026_09_21.py
python3 .claude/science/mobile-record-immutable-waves-20260921/verify_capsules.py
```

The author runner requires NumPy and SymPy. The selective source-review control
also uses SciPy. Its historical cached-source identity check refers to the
original reviewed note and author evidence; use the preserved versions when
reproducing that historical run. The correction acknowledgment binds the final
note to the completed review. Capsules retain their original directory layout
and source identities rather than rewriting old evidence to appear current.

The fluctuation claim fixes full-support density, a finite time interval and
finitely many Fourier modes before taking the lattice limit. The supremum is
outside expectation. The Euler theorem assumes a smooth interior solution;
it does not prove global smoothness. No finite-wave-number damping law,
nonstationary fluctuation theorem, nonlinear rotational invariance, quantum
implementation, gravity, axiom adoption or TOE closure is claimed here.
Campaign simulations and later constructions are excluded from this milestone.

The full integration pipeline, strict audit lint and changed-evidence landing
gates remain for the combined landing candidate. No editable prompt file,
primitive registry or audit verdict is changed by this packet.
