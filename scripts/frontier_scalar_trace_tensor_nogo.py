#!/usr/bin/env python3
"""No-go theorem for scalar-trace-only tensor completion on the current gravity branch.

This runner sharpens the remaining gravity gap beyond the restricted
strong-field package already closed on the branch.

Exact logic:
  1. The current microscopic boundary functional depends only on the scalar
     shell trace / Schur-complement data.
  2. The tensorial completion probes on the branch keep that scalar boundary
     data fixed by construction.
  3. Therefore any purported completion principle that factors only through
     the scalar shell data must assign the same output to all such probes.

Bounded witness:
  4. Explicit vector-shift and traceless-shear perturbations with the same
     scalar boundary data produce different Einstein-tensor channels.
  5. Hence no scalar-trace-only completion principle can determine the full
     `3+1` metric on the current branch. A genuinely tensor-valued matching law
     is required for full nonlinear GR.
"""

from __future__ import annotations

from dataclasses import dataclass

import frontier_coarse_grained_exterior_law as coarse
import frontier_same_source_metric_ansatz_scan as same_source
import frontier_tensorial_einstein_regge_completion as tcomp


# These are static imports on purpose. The audit packet can inspect ordinary
# import edges, while the previous _frontier_loader dynamic imports made the
# load-bearing scalar functional, probe-family, and Einstein-residual helpers
# opaque in restricted helper-runner review.
_LOAD_BEARING_HELPERS = (tcomp, same_source, coarse)


@dataclass
class Check:
    name: str
    ok: bool
    detail: str
    status: str


CHECKS: list[Check] = []


def record(name: str, ok: bool, detail: str, status: str = "EXACT") -> None:
    CHECKS.append(Check(name=name, ok=ok, detail=detail, status=status))
    tag = "PASS" if ok else "FAIL"
    print(f"[{status}] {tag}: {name}")
    if detail:
        print(f"    {detail}")


def n5_execution_certificate(
    base_oh, vec_oh, ten_oh, mix_oh, base_fr, vec_fr, ten_fr, mix_fr
) -> None:
    """Print-only record of what this runner resolves at each granularity.

    Adds no check and touches no counter.  Floating figures are interpolated
    from this run's own probe results at print time.
    """
    print("\n" + "=" * 72)
    print("N5 execution certificate (print-only; adds no check and no counter)")
    print("=" * 72)
    print(
        "per_element: resolved as named components of the 4x4 Einstein tensor -- at each probe point "
        "the reader takes |G_00| by itself, maximizes |G_0i| over the three mixed time-space entries, "
        "then subtracts one third of the spatial trace before maximizing over the nine entries of the "
        "traceless spatial part. The verdict therefore rests on which particular entries move rather "
        "than on any single lumped scalar, and G itself is assembled entry by entry from central "
        "differences of the ADM metric taken at the fixed step h = 0.04."
    )
    print(
        "per_site: checked and not executed -- neither phi grid is ever read out site by site. The "
        "15-cubed field reaches the checks through two collapsing routes only: one whole-boundary "
        "quadratic form yielding a single scalar action, and trilinear interpolation evaluated at "
        "three fixed spacetime points. No per-site amplitude, residual, or comparison is computed, "
        "printed, or asserted anywhere in this runner."
    )
    print(
        "per_mode: resolved as an explicit scalar/vector/tensor mode split -- the probes are driven "
        "by two independent named modes, a vector shift entering the shift vector as "
        "eps_vec*sin(omega t)*env*vector_mode(xyz) and a traceless shear entering the spatial metric "
        "as eps_ten*cos(omega t)*env*tensor_mode(xyz), each switched on alone at amplitude 0.02 with "
        "omega = 1.0 and then together in the mixed probe. The response is read back in the matching "
        "channel: the vector mode lights G_0i, the shear mode lights the traceless spatial block, and "
        "the mixed probe is required to light both at once on both grid classes."
    )
    print(
        "per_block: resolved as a 3+1 block decomposition of the Einstein tensor -- the time-time "
        "entry, the time-space row, and the spatial 3x3 block are separated, and that spatial block "
        "is further split into its pure-trace and traceless parts. That split is precisely what the "
        "no-go turns on: the branch currently fixes trace-type boundary data only, while the "
        "traceless and mixed blocks are shown to move under probes that leave that data untouched."
    )
    print(
        "lattice_wide: executed as a finite-N whole-grid quantity, with one caveat stated plainly -- "
        "the scalar boundary functional is the Schur-complement action 0.5*f.(Lambda f) - j.f built "
        "on the 15-cubed grid at cutoff radius 4.0, a genuinely lattice-wide object, and it is "
        "evaluated on two distinct grids. Its constancy across the four probes is however true by "
        "construction rather than measured: probe_family forms the scalar action from phi_grid alone "
        "and never forwards eps_vec, eps_ten, or omega into it, so the four probes on a given grid "
        "call one identical function on one identical argument. No grid-size scan is run and no "
        "thermodynamic limit is taken."
    )
    print(
        "Live figures at print time, since finite-difference and Schur values shift between "
        f"environments while the verdicts do not: O_h scalar action {base_oh.scalar_action:.6e} and "
        f"finite-rank scalar action {base_fr.scalar_action:.6e}; vector channel |G_0i| = "
        f"{vec_oh.e_ti:.3e} on O_h and {vec_fr.e_ti:.3e} on finite-rank; traceless shear channel "
        f"|G_ij^TF| = {ten_oh.e_spatial_tf:.3e} and {ten_fr.e_spatial_tf:.3e}; mixed probe "
        f"(|G_0i|, |G_ij^TF|) = ({mix_oh.e_ti:.3e}, {mix_oh.e_spatial_tf:.3e}) and "
        f"({mix_fr.e_ti:.3e}, {mix_fr.e_spatial_tf:.3e}). The activation thresholds these are judged "
        "against (1e-5, 1e-4, 1e-3, 1e-6) and the scalar-agreement tolerance 1e-14 are fixed literals "
        "in the source and are quoted as written."
    )
    print(
        "Determinism: no RNG, optimizer, root-finding, or Monte Carlo appears in this runner or its "
        "probe helper. The sweep is a fixed list of three spacetime points crossed with eight "
        "labelled probes at the single amplitude 0.02, and all derivatives use the fixed "
        "central-difference step h = 0.04. Every floating quantity above is interpolated from this "
        "run's own probe results; none is copied from a previous run."
    )


def main() -> None:
    print("Scalar-trace-only tensor completion no-go")
    print("=" * 72)

    phi_oh = same_source.build_best_phi_grid()
    phi_fr = coarse.build_finite_rank_phi_grid()

    base_oh = tcomp.probe_family("scalar bridge", phi_oh, eps_vec=0.0, eps_ten=0.0, omega=0.0)
    vec_oh = tcomp.probe_family("vector shift", phi_oh, eps_vec=0.02, eps_ten=0.0, omega=1.0)
    ten_oh = tcomp.probe_family("tensor shear", phi_oh, eps_vec=0.0, eps_ten=0.02, omega=1.0)
    mix_oh = tcomp.probe_family("mixed", phi_oh, eps_vec=0.02, eps_ten=0.02, omega=1.0)

    base_fr = tcomp.probe_family("finite-rank scalar bridge", phi_fr, eps_vec=0.0, eps_ten=0.0, omega=0.0)
    vec_fr = tcomp.probe_family("finite-rank vector shift", phi_fr, eps_vec=0.02, eps_ten=0.0, omega=1.0)
    ten_fr = tcomp.probe_family("finite-rank tensor shear", phi_fr, eps_vec=0.0, eps_ten=0.02, omega=1.0)
    mix_fr = tcomp.probe_family("finite-rank mixed", phi_fr, eps_vec=0.02, eps_ten=0.02, omega=1.0)

    def same_scalar_data(a, b) -> bool:
        return abs(a.scalar_action - b.scalar_action) < 1e-14

    print("O_h scalar-action invariance:")
    print(
        f"  scalar={base_oh.scalar_action:.6e}, vector={vec_oh.scalar_action:.6e}, "
        f"tensor={ten_oh.scalar_action:.6e}, mixed={mix_oh.scalar_action:.6e}"
    )
    print("Finite-rank scalar-action invariance:")
    print(
        f"  scalar={base_fr.scalar_action:.6e}, vector={vec_fr.scalar_action:.6e}, "
        f"tensor={ten_fr.scalar_action:.6e}, mixed={mix_fr.scalar_action:.6e}"
    )
    print("Tensorial residual channels:")
    print(
        f"  O_h vector |G_0i|={vec_oh.e_ti:.3e}, tensor |G_ij^TF|={ten_oh.e_spatial_tf:.3e}, "
        f"mixed (|G_0i|,|G_ij^TF|)=({mix_oh.e_ti:.3e},{mix_oh.e_spatial_tf:.3e})"
    )
    print(
        f"  finite-rank vector |G_0i|={vec_fr.e_ti:.3e}, tensor |G_ij^TF|={ten_fr.e_spatial_tf:.3e}, "
        f"mixed (|G_0i|,|G_ij^TF|)=({mix_fr.e_ti:.3e},{mix_fr.e_spatial_tf:.3e})"
    )

    record(
        "the current microscopic scalar boundary functional is invariant across vector/tensor perturbations with the same scalar shell data on the exact O_h class",
        same_scalar_data(base_oh, vec_oh) and same_scalar_data(base_oh, ten_oh) and same_scalar_data(base_oh, mix_oh),
        (
            f"scalar={base_oh.scalar_action:.6e}, vector={vec_oh.scalar_action:.6e}, "
            f"tensor={ten_oh.scalar_action:.6e}, mixed={mix_oh.scalar_action:.6e}"
        ),
    )
    record(
        "the same scalar-data invariance persists on the finite-rank class",
        same_scalar_data(base_fr, vec_fr) and same_scalar_data(base_fr, ten_fr) and same_scalar_data(base_fr, mix_fr),
        (
            f"scalar={base_fr.scalar_action:.6e}, vector={vec_fr.scalar_action:.6e}, "
            f"tensor={ten_fr.scalar_action:.6e}, mixed={mix_fr.scalar_action:.6e}"
        ),
    )
    record(
        "vector perturbations with unchanged scalar boundary data activate independent G_0i residuals",
        vec_oh.e_ti > 1e-5 and vec_fr.e_ti > 1e-5,
        f"O_h={vec_oh.e_ti:.3e}, finite-rank={vec_fr.e_ti:.3e}",
        status="BOUNDED",
    )
    record(
        "traceless shear perturbations with unchanged scalar boundary data activate independent traceless spatial residuals",
        ten_oh.e_spatial_tf > 1e-4 and ten_fr.e_spatial_tf > 1e-3,
        f"O_h={ten_oh.e_spatial_tf:.3e}, finite-rank={ten_fr.e_spatial_tf:.3e}",
        status="BOUNDED",
    )
    record(
        "mixed vector+tensor perturbations simultaneously activate both tensor channels while leaving scalar boundary data unchanged",
        mix_oh.e_ti > 1e-5 and mix_oh.e_spatial_tf > 1e-4 and mix_fr.e_ti > 1e-6 and mix_fr.e_spatial_tf > 1e-3,
        (
            f"O_h=(|G_0i| {mix_oh.e_ti:.3e}, |G_ij^TF| {mix_oh.e_spatial_tf:.3e}), "
            f"finite-rank=(|G_0i| {mix_fr.e_ti:.3e}, |G_ij^TF| {mix_fr.e_spatial_tf:.3e})"
        ),
        status="BOUNDED",
    )
    record(
        "no completion principle that factors only through the current scalar shell trace / Schur data can determine the full `3+1` metric on this branch",
        same_scalar_data(base_oh, vec_oh)
        and same_scalar_data(base_oh, ten_oh)
        and same_scalar_data(base_fr, vec_fr)
        and same_scalar_data(base_fr, ten_fr)
        and vec_oh.e_ti > 1e-5
        and ten_oh.e_spatial_tf > 1e-4
        and vec_fr.e_ti > 1e-5
        and ten_fr.e_spatial_tf > 1e-3,
        "same scalar data, different tensorial Einstein channels -> genuinely tensor-valued matching law required",
    )

    n5_execution_certificate(
        base_oh, vec_oh, ten_oh, mix_oh, base_fr, vec_fr, ten_fr, mix_fr
    )

    print("\n" + "=" * 72)
    print("SUMMARY")
    print("=" * 72)
    n_pass = sum(c.ok for c in CHECKS)
    n_fail = sum(not c.ok for c in CHECKS)
    print(f"PASS={n_pass} FAIL={n_fail} TOTAL={len(CHECKS)}")
    if n_fail == 0:
        print("All checks passed.")
    else:
        print("Some checks failed.")


if __name__ == "__main__":
    main()
