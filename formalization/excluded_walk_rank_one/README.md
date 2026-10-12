# Rank-one scattering algebra in Lean

`RankOneScattering.lean` proves universal statements over a complex Hilbert
space, with the inner product linear in its second entry. It is unchanged
from the source compiled in `final_compiler.log`. `SCOPE_REPORT.md` lists
all theorem statements and hypotheses. The source SHA-256 is
`2f5260a23eecc90c6bf3fabe9e26c4c05a5595fa151b98010097a7ee501b22ae`.

The verified identities are unitarity of the normalized rank-one update,
the exact bounded-observable difference, zero response of the contact vector,
the sign of an orthonormal coherent pair's response, and disjoint-channel
transfer with normalized incoming-cap weight. The cap's outgoing map is
bounded; it is interpreted as a detector probability only when it is the
intended orthogonal projection. These hypotheses remain part of the result.

The certificate is algebraic. It supplies neither the physical identification
of the scattering operator nor threshold, coarea, stationary-phase or
finite-preparation estimates. The three positive scalar controls compile;
six false identities fail at mathematical goals. Complete current control
sources/output are in `controls/`; output uses lossless `.log.gz` files. Historical development/tooling sources
and logs are preserved losslessly in `history/` as gzip files. The original
receipt uses its original task-local paths; it is a historical execution
record, not a claim that those absolute paths exist in a fresh checkout.
The milestone source map binds the committed representations.

Reproduction uses an existing clean Mathlib checkout pinned at
`939d5d5d9e6f07d1d8c80a16fa3fa39a7518b716`, with its matching
Lean `4.35.0-rc4` runtime and compiled dependency cache. The original official
arm64 macOS archive digest is recorded in the receipt. No toolchain, cache,
compiled binary or Mathlib checkout is included in this repository delta.

From the repository root, supply your local dependency paths and a new
output directory:

```sh
python3 formalization/excluded_walk_rank_one/reproduce.py \
  --mathlib /path/to/pinned/mathlib \
  --lean-bin /path/to/lean-4.35.0-rc4/bin \
  --output-dir /path/to/new/proof-output
```

The entrypoint checks the runtime version and clean dependency revision,
executes the ordinary Lake/Lean compiler, and preserves full output and
source hashes. It performs no installation. For a fresh dependency checkout,
use that revision's normal Mathlib setup and targeted cache retrieval for
`Mathlib/Analysis/InnerProductSpace/Adjoint.lean`, `Mathlib/Tactic/Ring.lean`,
`Mathlib/Tactic/Module.lean` and `Mathlib/Tactic/NormNum.lean` before compiling.
The successful original command is in `receipt.json`; `history/run_compile.py.gz`
and `history/run_false_controls.py.gz` preserve the original task-local drivers.

No independent audit status is assigned by compiling this file.
