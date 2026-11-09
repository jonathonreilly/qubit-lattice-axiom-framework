# Final decoder delta confirmation

Date: 2026-11-09. Scope: the added causal-path sentence, the record-derived
atomic transition, its new checks, and the supplied rerun artifacts. This is
a source-exposed delta confirmation, not a new broad review or audit. No
science script was executed, and neither earlier report was edited.

## Exact source identities

Candidate root:
`/Users/jonreilly/.codex/worktrees/gb1-cf-pair/Physics/.claude/science/physics-loops/gb1-cf-boundary-gluing-20261107/joint_record_law/`.

| Source | SHA-256 |
|---|---|
| `RESULT.md` | `d11abd8953071b60f674c87a16c095a01478344f34b363c07a9f944b51ebd6a3` |
| `ASSUMPTIONS.md`, unchanged | `83b5b28fc7063912a11040ace091658d71c63fbe17d58905396374b5f7c5bba8` |
| `check.py` | `782e08dd478c6089ed1b61e01088a5616ad0947c0a1564593c0aa936ab8b5169` |
| `outputs/decoder_change.diff` | `4796fb975f35d608528ece617b2f9d776821c3bba428220a5586b82ec7e9dcb4` |
| `outputs/exact.stdout` | `dee06cf5aa654076d683f876fc1da23fdde50bd707e256dae51cb881c2c7f739` |
| `outputs/execution.json` | `a216e82ea686eef9a9abd61f3ea3e95c8535ca662c5c4272f9e6c233d5c245aa` |
| `outputs/exact.stderr`, empty | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| `outputs/independent-draws.stderr` | `4bd67808030600a8714eb708051e557af18735b1b6d4ab91b6a089989651d992` |
| `outputs/remote-setting.stderr` | `fc99c3a77b105a59d4ffb345ed8906949de08abb71dd377f538e4edfddbdd3ce` |
| `outputs/missing-buddy.stderr` | `f147badb454dd0a75c0ff3bb7ff5d7d765b8117eb7d8a7942f8ef3f7b0f51f2a` |

The preserved `outputs/initial/check.py` hashes to the previously reviewed
`7db139b9378dc3f1e2f3b9f456672454e1cfdf3d33e7e6da337e9f88f860e081`.
Generating a unified text diff from that file and the current script gives
exactly the supplied `decoder_change.diff`. The changed function and all
changed call sites were read together with their required neighboring
definitions. Unchanged arithmetic, instruments, and apparatus arguments
retain their prior source check rather than being relabeled newly proved.

Removing exactly the three added causal-path lines from current `RESULT.md`
recovers its prior hash
`41dcf8d69f3183aafb2e18976a3be3c7907b76f3ae0cd7fa2b8e30063407f61f`.
Thus this proof-source delta contains no other textual or premise change.

## What changed and what is confirmed

**Causal-path sentence.** RESULT lines 220-222 now explicitly say that a
single pair node with both settings as parents and both outcomes as children
has setting-to-opposite-outcome paths. This correctly distinguishes the
atomic kernel from the earlier Bell no-directed-path premise. It leaves the
separate supplied tensor-local quantum implementation theorem intact. The
precision suggestion in `SOURCE_CHECK.md` is resolved.

**Actual record decoding.** `atomic_transition` obtains the target sites
from `targets_from_records(R)`. At each target it reads the complete
neighbor collection, identifies the unique setting record, subtracts `2I`,
checks Hermiticity, and recovers the three coefficients by
`n_j=Tr((X-2I)sigma_j)/2`. The Pauli expansion check and unit-norm check
match the declared Hermitian-involution apparatus. The Born kernel now
receives these decoded directions, not the loop's separately declared
directions. On a ready state it returns copies of `R` with both new scalar
outcomes, retaining every old entry and dropping zero-weight branches.

The `fixed_source_density` argument is held at the same singlet throughout
these transitions. A fixed parameter of a law is not an additional varying
state variable: this code defines the family member `T_rho_s(R)`. Varying
that argument at fixed `R` would describe a different law or an extra state
input, and is not a tested or claimed feature here. The source tag's physical
meaning remains supplied.

**Terminal behavior and excluded prefixes.** When both targets are occupied,
the function checks that their contents are `+/-I` and that the corresponding
prepared joint branch has nonzero weight; it returns exactly the unchanged
state with probability one. If exactly one target is occupied, it raises the
specific `ValueError` before producing a transition. This is the declared
atomic domain, not a sequential completion or a solution to the previously
identified conditional-probability conflict.

**Target ordering and covariance.** Sorting target coordinates can reverse
the two wings after a spatial transformation. In this fixed singlet law,
`p(a,b|n,m)=p(b,a|m,n)`, so the reversal gives the same weighted record
configuration. It therefore creates no preferred spatial ordering on the
claimed family. A nonsymmetric arbitrary density would require a separate
wing-identification convention; the new function is not here certified for
that generalization. The transformed-kernel test now compares complete
weighted post-states, with a nonzero-correlation direction pair, not merely
target locations or local menus.

**Finite evidence.** In each of the 49 already declared direction pairs,
the decoded weights are compared against the original effect/pointer
diagnostic weights. Each of the 182 positive terminal states is checked for
absorption. All 24 proper cubic transformations with the supplied translation
compare the transformed entire kernel. Two one-outcome states are explicitly
required to raise the declared rejection. Those counters correspond to
actual assertions in the changed code, not to unsupported output labels.

These changes address the old script's specific implementation boundary in
`SOURCE_CHECK.md`: the updated script does execute an `R -> transition`
decoder, terminal absorption, and transformed-kernel equality on its declared
test apparatus. The old report remains an accurate record of the old hash.

## Remaining scope limits

`atomic_transition` is not a complete apparatus-domain validator. Source-tag
presence, absence of extraneous records, and the full permitted spatial
template are preconditions; the function does not establish them merely
because it returns a result. Its local checks and explicit prefix rejection
are compatible with this stated restriction. No arbitrary-mosaic validation
or law on every configuration has been demonstrated.

The new execution still uses exact finite directions in `Q(i,sqrt(2))`:
49 ready kernels at `L=6`, the positive terminal branches, and one direction
pair at `L=17` under 24 transformations. The analytical source supports the
continuum and spatial generalizations; the finite replay is not exhaustive
over them. It does not execute the eighteen-record setting-port variant,
construct preparation genesis, make a local physical sampler, or derive a
causal speed. The joint kernel continues to use the supplied Born law and
singlet preparation.

## Rerun artifacts inspected, without replay

The new stdout names the exact current script hash and reports the new
49/182/2 counters, with the original 2674 support instances and 24 spatial
transformations. Its Bell and polynomial scores are unchanged.
`execution.json` reports exit 0 for the exact run and exit 1 for each of
the three deliberate controls. The complete inspected error streams agree:

* `independent-draws` fails at `record-decoded kernel`, now earlier than
  the old pointer comparison;
* `remote-setting` fails at `remote setting entered Alice instrument`;
* `missing-buddy` fails the support check at `(0,1,0)`.

The exact run's stderr is empty. These are source-bound execution artifacts
and intelligible negative controls; I did not independently rerun them or
attest their runtime environment. Their checks do not establish completeness
against every possible wrong decoder or hidden causal dependency.

## Delta disposition

Confirmed within the stated domain: the added causal sentence is accurate,
and the decoder plus new diagnostics implement the advertised record-input,
absorption, covariance, and prefix-rejection changes. I found no defect
requiring a correction in this delta. No physical premise is retired by the
new computation, and the intermediate-record physical bridge remains open.
This confirmation grants no general PASS, retained status, or audit verdict.

Previous reports remain unchanged:
`INDEPENDENT.md` is
`b7a8451d1529c843a2cdf2da9a7b1356362a05b1f0be691386ead91f76d16c55`;
`SOURCE_CHECK.md` is
`1d1bd376c63d8db75221721676b98940e3b4cc26b321aa55989cc851dd9478b0`.
Only this `DELTA_CHECK.md` was written. No source edit, science execution,
commit, push, or audit operation was performed.
