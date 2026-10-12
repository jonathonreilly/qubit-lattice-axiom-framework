# Scoped Lean certificate: universal rank-one scattering algebra

This is formal algebra evidence for the target identified in
`SCOPED_OBLIGATIONS.md`. It is not a formalization of threshold regularity,
coarea estimates, stationary scattering, Cook bounds, a flux theorem, or
physical dynamics. It does not apply a retained-status decision.

`RankOneScattering.lean` is a 202-line theorem file over an arbitrary complex
Hilbert space. Its final successful compilation is recorded in
`final_compiler.log`, with the original command and source snapshot in
`logs/attempt05.{json,lean,log}`. There are no errors or warnings in that
final compiler output. The source SHA-256 is
`2f5260a23eecc90c6bf3fabe9e26c4c05a5595fa151b98010097a7ee501b22ae`.

## Exact coverage

Write `R(x,y) z = <y,z>x`, with the inner product linear in its second
argument, `S = I + (s-1)R(v,v)`, and `w = gv-<v,gv>v`.

| Lean theorem | Checked statement and hypotheses |
|---|---|
| `scattering_unitary` | If `||v||=1` and `||s||=1`, then `S` belongs to mathlib's unitary submonoid; both `S* S=I` and `S S*=I` are proved. |
| `observable_expansion`, `observable_difference` | For a bounded self-adjoint `g`, the exact expansion includes the phase-defect term `(conj(s)s-1)<v,gv>R(v,v)`. With unit phase it gives `S* g S-g=(s-1)R(w,v)+(conj(s)-1)R(v,w)`. |
| `centered_orthogonal` | `||v||=1` implies `<v,w>=0`. The operator difference itself actually holds without vector normalization; normalization is required for its unitary/off-diagonal interpretation. |
| `pure_contact_zero` | For `||v||=||s||=1`, the contact-aligned expectation change is zero. This identity even permits any bounded `g`, without self-adjointness. |
| `coherent_normalized`, `coherent_current` | Given orthonormal `v,u`, real `sigma,r`, `w=sigma u`, and `2r^2=1`, the vector `psi=r(v+i u)` has norm one and `<psi,(S* g S-g)psi>=sigma Im(s)`. The sign belongs to the explicitly chosen `+i` state. |
| `outgoing_amplitude`, `disjoint_transfer` | If a bounded outgoing map `Q` satisfies `Q phi=0`, then `Q S phi=(s-1)<v,phi>Qv`, with the corresponding exact squared-norm product. |
| `cap_normalized`, `cap_overlap`, `cap_transfer` | For a self-adjoint idempotent `A` and `Av!=0`, `phi=Av/||Av||` is normalized and `<v,phi>=||Av||`. Under `Q(Av)=0`, the exact transfer is `||Q S phi||^2=|s-1|^2 ||Av||^2 ||Qv||^2`. |

The cap algebra needs only the displayed assumptions on `Q`; it applies
in particular when `Q` is an orthogonal outgoing projection. Its projection
interpretation is not silently inferred from an arbitrary bounded map.
Unit normalization of `v` and unit phase can be supplied together with
`scattering_unitary` when interpreting the result as unitary scattering.
The packet does not formalize a continuum cap measure, construct a spectral
fiber, prove that physical scattering has this `S`, or construct `u` from a
nonzero centered vector. The coherent theorem has that relation as an
explicit hypothesis. No finite-dimensional restriction or finite matrix
substitute appears in these universal theorems.

## Trusted dependencies and source checks

The verified official archive SHA-256 is
`743f536c58c2580577ef890985b4084e90c6039fce099018d5c0c67c13724218`.
It was checked before extraction. Lean reports version `4.35.0-rc4`,
runtime commit `c29b6dda4f7c20e3eeaa717c4e565663c5cfa364`, arm64 macOS.
Mathlib is pinned at `939d5d5d9e6f07d1d8c80a16fa3fa39a7518b716`, and
its tracked source tree remains unchanged.

The imports are `InnerProductSpace.Adjoint`, `Tactic.Ring`, `Tactic.Module`,
and `Tactic.NormNum`. Targeted cache retrieval downloaded/decompressed
their 2,482-file dependency closure. It did not request the full Mathlib
cache. `source_identities.json` records dependency revisions and hashes of
the relevant source files. The necessary rank-one definitions/application
identities, adjoint hypotheses, inner-product convention, and unitary
definition were inspected in the pinned source. The complete Mathlib
library has not been manually reviewed or re-formalized by this task.

The ten `#print axioms` reports all list exactly `propext`,
`Classical.choice`, and `Quot.sound`. `axioms.txt` is an extract of the full
successful compiler output, not a separate proof run. There is no
`sorryAx`, admitted proof, or custom axiom in the final dependency reports.
The trusted base remains the pinned Lean runtime and ordinary imported
Mathlib artifacts. This certificate concerns the stated algebra, not the
correctness of every component of that trusted implementation.

## Reproduction and retained development evidence

All installation, package, cache and temporary paths are task-local.
Only each subprocess's PATH is extended with the extracted runtime.
`MATHLIB_CACHE_DIR`, `XDG_CACHE_HOME`, `LAKE_HOME`, and `TMPDIR` point inside
this directory. No global elan installation, global configuration, shared
repository, prompt file, commit, PR or audit status was changed.

Run `python3 run_compile.py RankOneScattering.lean <new-log-label>` from
this directory to compile again with a new source snapshot and full log.
Use a fresh label to preserve the frozen logs. False-statement controls
use the saved Lake dependency path followed by this task directory; on
the case-insensitive host, placing this directory first would shadow the
`Mathlib` module prefix with the local `mathlib` checkout directory.

Failed development attempts are preserved. Attempt 01 exposed Lean's
explicit root-directory requirement. Attempts 02-03 retained unresolved
proof goals; their automatically generated `sorryAx` diagnostics belong
to failed compilations and are not certificates. Attempt 04 compiled with
style warnings. Attempt 05 is the clean final compilation. The initial
local-module import failure is preserved separately and the corrected
import was successfully checked. Formal rejection controls and their
actual outcomes are recorded separately below and in the receipt.

## Deliberate rejection controls

`false_controls_manifest.json` records seven compiler invocations against
the final compiled module, including source and log hashes, commands,
exit codes and the 180-second per-process timeout. The positive control
file compiles three closed scalar witnesses: `S* S` sends `1` to `4` for
`v=1,s=2`, sends `1` to `49` for `v=2,s=-1`, and an already occupied
outgoing channel has squared norm `1` when `S=I`. Thus the controls actually
evaluate these normalization and disjointness boundary cases.

| False control | Actual compiler outcome |
|---|---|
| Unit phase omitted | Exit 1; the proposed value `1` contradicts the evaluated value `4`, leaving `False`. |
| Unit-vector normalization omitted | Exit 1; the proposed value `1` contradicts the evaluated value `49`, leaving `False`. |
| Outgoing disjointness omitted | Exit 1; the proposed zero probability contradicts the evaluated value `1`, leaving `False`. |
| Adjoint coefficient loses conjugation | Exit 1; the operator expansion reaches the unequal `conj(s)` versus `s` scalar coefficients. |
| Coherent current sign reversed | Exit 1; the true theorem reduces the attempted identity to `sigma Im(s) = -sigma Im(s)`. |
| Incoming cap weight omitted | Exit 1; the true theorem leaves the missing factor `||Av||^2` in the squared-norm product. |

Every current control log was read completely. None failed on an import,
unknown identifier, timeout or missing instance. These are deliberately
rejected proof attempts, not a general completeness test for Lean tactics
or an independent analytic scattering calculation. In particular, the
last three use the proved universal theorem to expose the incorrect
algebra; their failure is supplementary regression evidence.

The first control run is preserved in `logs/control_attempt01/`. Its
positive file failed because the simplifier did not reduce the complex
conjugate of a numeral. The scalar controls were rerun with `map_ofNat`
explicitly available; the positive witnesses then compiled, and the two
unitarity defects reduced to `False`. This correction changed only the
control harness and control files, not the frozen theorem source. The
complete original failed tooling and proof logs remain in the receipt.
