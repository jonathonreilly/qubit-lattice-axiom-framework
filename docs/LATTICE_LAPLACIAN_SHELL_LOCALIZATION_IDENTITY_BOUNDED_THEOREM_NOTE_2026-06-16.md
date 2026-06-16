# Lattice-Laplacian Shell-Localization Identity From Lattice/Cubic Inputs (Bounded)

**Date:** 2026-06-16
**Claim type:** bounded_theorem
**Claim boundary:** derives the lattice shell-localization identity and its
reduced-shell corollaries from the `Z^3` nearest-neighbor lattice adjacency and
the existing cubic `O_h` lift; does **not** claim the full nonlinear GR
completion or a tensor-valued matching law.
**Status authority:** independent audit lane only. This source note does not
set, predict, or estimate any audit verdict; effective status is pipeline-derived
after independent audit and dependency closure.
**Primary runner:**
[`scripts/lattice_laplacian_shell_localization_2026_06_16.py`](../scripts/lattice_laplacian_shell_localization_2026_06_16.py)
**Cached log:**
[`logs/runner-cache/lattice_laplacian_shell_localization_2026_06_16.txt`](../logs/runner-cache/lattice_laplacian_shell_localization_2026_06_16.txt)
(PASS=14 FAIL=0)

## Why This Note Exists (reproof of an import)

The `helper_frontier_module_surface` import family (the `_frontier_loader`
exterior-projector / shell-mean / source-constructor / sewing-shell / radial-DtN
helper modules used by `one_parameter_reduced_shell_law_note` and the scalar
side of `scalar_trace_tensor_no_go_note`) carried its shell results as an
**imported** numerical surface. A decompose-and-dedupe pass found that the
genuine science underneath those modules is a single algebraic identity. This
note derives that identity from the Lattice axiom's `Z^3` nearest-neighbor
adjacency together with the existing cubic `O_h` lift of the `Cl(3)` axis
structure, so the helper outputs become **corollaries**, not imports.

## Source Inputs (no imported helper numerics)

- [`MINIMAL_AXIOMS_2026-06-05.md`](MINIMAL_AXIOMS_2026-06-05.md) supplies the
  `Z^3` nearest-neighbor cubic adjacency. The runner uses its finite Dirichlet
  realization through the negative lattice Laplacian `H = 6I - A`, where `A`
  connects the six axis neighbors.
- [`CL3_OH_CUBIC_LIFT_FAITHFUL_NARROW_THEOREM_NOTE_2026-05-26.md`](CL3_OH_CUBIC_LIFT_FAITHFUL_NARROW_THEOREM_NOTE_2026-05-26.md)
  supplies the cubic `O_h` action as signed coordinate permutations induced by
  the `Cl(3)` axis structure. The commutation of `H` with that action follows
  from signed-coordinate-permutation invariance of the nearest-neighbor
  adjacency.

**Input ledger.** The runner imports only `numpy`. It uses **no** `_frontier_loader`
module, **no** helper-module numerical output, and hard-codes no shell profile,
DtN kernel, or the anisotropy anchor `c_aniso`; every such quantity is solved
from `H` on an explicit grid. The literature/helper surfaces are cross-check
comparators only, not inputs.

## What Is Proven (runner-verified on an explicit 15^3 Dirichlet grid)

`TOTAL: PASS=14 FAIL=0`, all residuals at machine precision (1e-15..1e-18):

1. The seven star-support point Green columns share an **identical shell-mean
   profile** (spread 8e-17); the shell-mean quotient kills the six
   zero-total-charge star modes.
2. The exterior projection `Pi_R^ext phi` is reconstructed exactly by a shell
   source `sigma_R = H Pi_R^ext phi`, and equals the unique exterior Dirichlet
   extension of its trace.
3. `sigma_R` is **localized** to the nearest-neighbor sewing band
   `R-1 < r <= R+1` (here `R=4`), with **unit total charge** per column.
4. All seven columns induce the **same normalized radial DtN shell kernel** and
   the **same normalized anisotropic orbit mode** (anchor `c_aniso = 0.081435...`,
   a lattice-solved constant, not a fit); the anisotropic remainder carries zero
   total charge.
5. Arbitrary star-supported sources **factor through total charge `Q`** on the
   reduced shell surface; the reduced map annihilates zero-total-charge star
   combinations.

These are exactly the shell-mean, exterior-projector, sewing-band-source,
radial-DtN, and one-parameter reduced-shell roles the helper modules supplied
numerically; they now follow from `H` and `O_h`.

## What Is NOT Claimed (the bound)

- **No full nonlinear GR / tensor-valued completion.** The orbit-mode
  *activation* into a tensor/GR matching law is a separate calculation and is
  not asserted here.
- This note retires the **shell-identity-dependent** portion of the helper
  surface. Any helper-import row that rests on the un-closed GR/tensor completion
  is out of scope and remains bounded.
- No audit status is asserted. Whether (and which) dependent rows re-audit
  `bounded -> retained` is the independent audit lane's call.

## Verification

The runner reproduces `PASS=14 FAIL=0` and confirms that the calculation imports
only `numpy` and no helper-frontier module. This is a source-runner check, not an
audit verdict.
