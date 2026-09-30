# Actual author checks

The original deadline and absence of STOP_REQUESTED were checked before the
route and are enforced again at startup by `check.py`. No dense full-torus
carrier was enumerated. The contract priced each sparse job at <=180 seconds
and <=1 GB, with OPENBLAS_NUM_THREADS=OMP_NUM_THREADS=MKL_NUM_THREADS=1.
A process observation during the mixed job showed about55 MB RSS. The tiny
alias control overlapped the mixed job briefly; no more than one substantial
job was running here. No unmanaged worker or external mutation was launched.

Commands, all from the campaign worktree:

    OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 python3 .claude/science/physics-loops/toe-gravity-law-24h-20260929/spectral-nonlinear-route/check.py --case axial
    OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 python3 .claude/science/physics-loops/toe-gravity-law-24h-20260929/spectral-nonlinear-route/check.py --case mixed
    OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 python3 .claude/science/physics-loops/toe-gravity-law-24h-20260929/spectral-nonlinear-route/check.py --case alias

Actual outputs:

* Axial: exact zero CC/GC coefficients through degree3 and GG through degree2,
  both vacuum and total scalar. Arithmetic time4.248 seconds, exit0.
* Mixed x/y Fourier axes with all six tensor components: the same six exact
  zero residuals. Arithmetic time49.868 seconds, exit0.
* Full-zone n=7 control: exact GG degree2 residual7/4; exit0 after comparison
  with the independently derived Fourier coefficient in REPORT.md.
  Arithmetic time0.012 seconds.

The JSON files retain the actual parameters and results. These are selected
input checks, not a universal proof or an independent review. No separate
numerical nested-Jacobi job was run: REPORT.md gives the contraction-tree
proof and all four explicit continuum structure-Jacobi identities instead.

Development failures are not hidden: `python` was unavailable, so the actual
commands use `python3`; an exploratory Gaussian-rational probe called an
unsupported `.conjugate()` method (not used by the implementation); the first
script launch had an `else1` syntax typo, corrected to `else 1` before any
scientific calculation. No failed scientific residual was suppressed or
prefactor tuned to a target.

Read-only source refresh reverified main9d15f404 and PR9363fd51a1f4. The final
open-PR metadata census found PR9394d72d4713; its full actual note was read
and added to the closest-prior/source record. PR9008 is an ice covariance
proposal and was not used as a gravity premise. All declared baseline
procedure/axiom/primitive/seed bytes were unchanged from selected7146.

Independent checking of the new spectral transfer and scalar extension is
pending. No formal audit, source PR, commit or push was performed here.
