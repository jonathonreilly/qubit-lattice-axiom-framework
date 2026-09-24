# Final publication comparison: live-birth field response, Part II only

2026-09-24. The publication implements all four narrow POST corrections. Its complete Part II and closing bridge agree with the frozen root argument after exactly those edits and a trailing blank line. The control functions and field-response values are unchanged, and the published source, declared-input fingerprint, result, cache, and external execution record correspond.

This is a final-source comparison, not a new derivation, independent numerical replication, publication decision, or audit verdict. Part I's mathematics and observational interpretation remain outside this review. No primary runner was executed, and no active Part I checker packet was accessed.

## Frozen identities and coverage

The publication worktree is `/Users/jonreilly/Documents/Codex/physics-sync-2026-09-24-fifth/photon-observation-publication`, at supplied base `0e6ad8285096ed668816f18caaa6fbbfbd9c50e8`. The following complete bytes were verified against the released hashes and copied into `publication_sources/worktree/`:

| Publication member | SHA256 |
|---|---|
| `docs/PHOTON_DISPERSION_OBSERVATIONAL_CONSTRAINTS_AND_LIVE_FORMATION_RESPONSE_BOUNDED_THEOREM_NOTE_2026-09-24.md` | `acf74cfce461cfbf607f7ba2994ff0a3d5986b9571bf7c5efacecebdf9ab5d7b` |
| `scripts/photon_dispersion_observation_and_live_formation_response_2026_09_24.py` | `268ee539b5978dca070bbb719eb370b181c63257f9ff5319f76969c8534476c5` |
| `outputs/photon_observation_live_formation_20260924/PHOTON_OBSERVATION_LIVE_FORMATION_RESULTS.json` | `587bf71a3daf63ac62399b93a8fd4d33ab5bc874b75bcdade55a44d317e968d6` |
| `logs/runner-cache/photon_dispersion_observation_and_live_formation_response_2026_09_24.txt` | `21ec8d09699c6d4a5bfd98a068f32d0e004315df8c3430869bfc5d07649b0bcf` |

The publication frontmatter/prologue at lines 1-32, complete Part II at lines 154-282, and complete closing context at lines 283-end were read. The whole runner and its complete difference from the frozen root control were read. The additional Part I numerical payload in the released execution record was encountered and mechanically compared as unchanged data, without a scientific verdict on it. No independent Part I review result is imported.

`PUBLICATION_SOURCE_PINS.json` records thirteen complete snapshots and their current origins: the four publication members above, all five declared parent inputs, the cache-format helper, and the three external `FOURTEENTH_*` records. The five parent files and helper were also checked byte-for-byte against the base git revision. Scientific coverage of those parents remains exactly the bounded PRE/POST coverage; hashing their complete bytes for cache identity does not recertify their arguments.

The root baseline is the POST-frozen derivation SHA256 `15c48725d54c95abe43de50de23b62fbf9d983029ee2152c125f361a9ca316ba` and control SHA256 `b00520addc22448ae3fed5981964b4907a92ebe093a0bee326c5c17b7e0d8bbc`. The original PRE seal, SHA256 `20a5ff20eddc860b016023cca25cb7dcab93abf63dce817a938515682de3fb2d`, retains all 22 members unchanged. The POST seal, SHA256 `92518a7b7a2fa017b26634c7352e8a0e766ad2e74f5e515d16b1ba8da5bc861b`, retains all 20 members unchanged. Both were reverified at the start and during this comparison.

## The four corrections and unchanged scope

1. **Trace-norm convention, line 198.** The note now says “trace-norm distance,” retaining `2(1-exp(-lambda t))`. This is the correct full joint-state equality established in POST. It is not asserted as an equality after tracing matter or as a photon absorption probability.
2. **Physical angular observables, lines 205 and 210.** The note now specifies bounded gauge-invariant periodic angle functions. Divergence-free Wilson loops remain the physical observables used in the acceleration formula.
3. **Oscillator domain, lines 241-242.** The diagnostic now explicitly requires a positive-frequency transverse oscillator and `omega_k>0`. The chart and oscillator-identification qualification remains. Zero-frequency winding modes are not included in the division by omega.
4. **Joint-path proof, line 270.** The acceleration proof now sums “the original joint marked paths (8), including their output matter.” It no longer purports to evaluate a q-dependent observable using only the matter-traced field map (9).

`PUBLICATION_PART_II_DELTA.diff` gives the complete root-to-publication difference for Part II and the closing bridge. A deterministic textual check applies exactly these six literal replacements, covering the four corrections, to the frozen root block and obtains the publication block after removing trailing whitespace. No other Part II mathematical change is hidden in that comparison.

In particular, the same original resolved/coherent instruments and their different joint outputs remain explicit. The exact initial loss, gradient drift, centered covariance, transverse field-diagnostic injection, changed B-occupancy mask, and changed A charge are retained. Equation (14) still uses the full common slow Hamiltonian and has `r_B=4 kappa z(z-1)`, giving 24 kappa for the cube and 120 kappa for degree six. The finite-word/moment-domain restriction and the warning against uniform trace-class claims remain. The initial acceleration is not promoted to finite-duration damping, photon mass, attenuation, or an astronomical bound on kappa.

The closing context still distinguishes the older decreasing formation schedule from the fixed-kappa common process, and identifies full source-to-detector dynamics and physical calibration as separate obligations. The new evidence section accurately describes the independent PRE's primitive magnetic and full dual-Wilson checks, including its nonzero coherent field superposition. The publication's `proposed_retained` label is not treated here as retained status; its text explicitly separates selective review from independent audit authority.

## Runner and existing execution correspondence

The complete `PUBLICATION_RUNNER_DELTA.diff` shows only the disclosed wrapper adaptations: timeout/input declarations, output path, metadata, original-root fingerprint, timing placement, and printed summary. Exact source-segment comparison confirms that `graph`, `graph_control`, and `dispersion_controls` are unchanged copies of the sealed root functions. The last comparison is a source-identity check, not a Part I scientific endorsement.

All three graph result rows are exactly equal to the root's sealed rows. The cube, degree-four square torus, and degree-six cubic torus retain their initial path counts 48, 432, and 6480; per-edge drift -4, -6, and -10 in units of kappa; covariance diagonals 8, 12, and 20; and loop-acceleration coefficients 24, 48, and 120. Mutant diagnostics are unchanged. The complete dispersion payload also compares equal as opaque data. Thus there is no new numerical content or new independence claim attached to this disclosed rerun.

The six literal `AUDIT_INPUT_PATHS` consist of the publication note and the five pinned parents. I read the cache helper's literal-path parsing, v1 fingerprint, and cache-format definitions, then independently reconstructed the content fingerprint in the read-only correspondence checker. It hashes the prefix `runner-cache-input-fingerprint-v1` followed by a zero byte, then each declared path and complete file body with their eight-byte big-endian lengths, in declaration order. The result is

    0a004bc3e1d50958450b87fde302135af636dc5ee2da558cd4ade6c4dc89b9cc

and matches the cache header. This includes the corrected publication note's actual current bytes, not a historical candidate fingerprint. The result's `source_sha256` matches the publication runner, and `reused_root_source_sha256` matches the sealed root control.

The complete external execution stdout equals the result JSON bytes followed by `TOTAL: PASS=4 FAIL=0` and a newline. External stderr is empty, status is `ok`, exit code is zero, and timeout is 120 seconds. Reconstructing the entire cache text from that execution record, current runner hash, and current input fingerprint gives exact byte equality with the released cache. No stdout/stderr truncation occurred. The external frozen-source and root-verification records agree with the same note, runner, result, and cache hashes.

The inspected existing primary record reports outer wall time `0.372133731842041` seconds. Its runner-internal elapsed value is `0.24922312516719103` seconds, while the cache prints the rounded outer time `0.37`. These timings are distinct. I inspected their binding and did not execute or independently time the primary.

## Binding evidence and stopping point

`publication_binding_check.py` executes only source, text, hash, and existing-data comparisons. It does not import either scientific runner or invoke the cache/audit execution path. Its full result is `PUBLICATION_BINDING_CHECK.json`, with complete stdout, empty stderr, and an explicit execution record. All assertions passed. The complete output was inspected.

The root's preserved `defaultdict(set())` harness failure and the independent PRE's initially vacuous auxiliary-check history remain in their prior unchanged seals. Neither is erased or relabeled by the new primary. No publication file, author file, prior report, audit state, or axiom was changed by this checker.

No further discrepancy was found in the requested Part II/source-cache correspondence. The report, exact source snapshots, deltas, checker and complete binding evidence are frozen in a separate publication-comparison seal. Work stops here; no new independent physics claim or Part I verdict is issued.
