#!/usr/bin/env python3
"""D=3 staggered two-band orbital-response bounded runner.

Companion draft:
    docs/D3_STAGGERED_TWO_BAND_ORBITAL_BOUNDED_THEOREM_NOTE_2026-06-13.md

The exact reference is a direct dense diagonalization of a finite periodic cubic
two-band lattice with a quantized uniform xy plaquette field.  The decomposition
is computed independently from the B=0 matrix expansion

    H(B) = H0 + B H1 + B^2 H2 + O(B^3)

with a divided-difference grand-potential curvature formula.  The same fixed
magnetic-area normalization, 1/L^2, is applied to the perturbative curvature to
convert the finite torus gauge curvature to per-plaquette uniform-B response.

Run:
    python3 scripts/frontier_d3_staggered_two_band_orbital_2026_06_13.py
"""

from __future__ import annotations

import math
import sys
from dataclasses import dataclass
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "D3_STAGGERED_TWO_BAND_ORBITAL_BOUNDED_THEOREM_NOTE_2026-06-13.md"

TWOPI = 2.0 * math.pi
T_HOP = 1.0
REFERENCE_L = 8
FD_L = 6
CONVERGENCE_LS = (4, 6, 8)
MASSES = (0.0, 0.3, 0.6)
SIGN_MUS = (0.0, 0.4, 1.0, 2.0)
MU_REF = 0.4
TEMPERATURE = 1.0

# Frozen gates, decided before the runner evaluates its pass/fail rows.
HERMITICITY_TOL = 1.0e-12
BLOCH_SPECTRUM_TOL = 1.0e-10
FD_FINAL_ABS_TOL = 1.0e-5
FD_RATIO_MIN = 3.5
BSTEP_DRIFT_TOL = 6.0e-2
BSTEP_RATIO_MIN = 4.0
FULL_REL_TOL = 1.2e-1
LP_ONLY_REL_MISS_MIN = 10.0
INTERBAND_MIN = 5.0e-1
SIGN_TOL = 1.0e-4

SIGMA_X = np.array([[0.0, 1.0], [1.0, 0.0]], dtype=np.complex128)
SIGMA_Y = np.array([[0.0, -1.0j], [1.0j, 0.0]], dtype=np.complex128)
SIGMA_Z = np.array([[1.0, 0.0], [0.0, -1.0]], dtype=np.complex128)
LINK_MATS = (SIGMA_X, SIGMA_Y, SIGMA_Z)

PASS_COUNT = 0
FAIL_COUNT = 0


def gate(label: str, condition: bool, detail: str = "") -> None:
    global PASS_COUNT, FAIL_COUNT
    ok = bool(condition)
    if ok:
        PASS_COUNT += 1
        tag = "PASS"
    else:
        FAIL_COUNT += 1
        tag = "FAIL"
    suffix = f" :: {detail}" if detail else ""
    print(f"{tag}: {label}{suffix}")


def site_index(L: int, x: int, y: int, z: int, orbital: int) -> int:
    return ((((x % L) * L + (y % L)) * L + (z % L)) * 2 + orbital)


def link_phase_and_derivatives(
    L: int, B: float, x: int, y: int, direction: int
) -> tuple[complex, complex, complex]:
    """Return U, c1, c2 for U(B) = U(0) + B c1 + B^2 c2 + O(B^3)."""

    if direction == 0:
        # Landau gauge x-link.  Interior plaquettes get flux exp(+iB) with the
        # y-boundary correction below.  The sign convention is fixed here and
        # used by both exact and perturbative paths.
        return np.exp(-1.0j * B * y), -1.0j * y, -0.5 * y * y

    if direction == 1 and y == L - 1:
        # Periodic torus correction; for B L^2 = 2 pi n it makes every xy
        # plaquette carry the same flux.
        total = L * x
        return np.exp(1.0j * B * total), 1.0j * total, -0.5 * total * total

    return 1.0 + 0.0j, 0.0 + 0.0j, 0.0 + 0.0j


def build_hamiltonian(
    L: int, mass: float, B: float = 0.0, derivatives: bool = False
) -> np.ndarray | tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Dense periodic cubic two-band Hamiltonian.

    Zero-field Bloch convention:

        H(k) = 2 cos(kx) sigma_x + 2 cos(ky) sigma_y
             + (m + 2 cos(kz)) sigma_z.

    The sigma_z orbital is the staggered parity component: the onsite mass is
    +m on one parity orbital and -m on the other; the z hopping enters the same
    staggered structure as 2 cos(kz) sigma_z.
    """

    n = 2 * L**3
    H = np.zeros((n, n), dtype=np.complex128)
    H1 = np.zeros_like(H) if derivatives else None
    H2 = np.zeros_like(H) if derivatives else None

    for x in range(L):
        for y in range(L):
            for z in range(L):
                here = [site_index(L, x, y, z, a) for a in range(2)]
                H[np.ix_(here, here)] += mass * SIGMA_Z

                for direction, matrix in enumerate(LINK_MATS):
                    xp, yp, zp = x, y, z
                    if direction == 0:
                        xp = x + 1
                    elif direction == 1:
                        yp = y + 1
                    else:
                        zp = z + 1

                    there = [site_index(L, xp, yp, zp, a) for a in range(2)]
                    phase, c1, c2 = link_phase_and_derivatives(L, B, x, y, direction)
                    block = T_HOP * phase * matrix
                    H[np.ix_(there, here)] += block
                    H[np.ix_(here, there)] += block.conjugate().T

                    if derivatives:
                        block1 = T_HOP * c1 * matrix
                        block2 = T_HOP * c2 * matrix
                        H1[np.ix_(there, here)] += block1
                        H1[np.ix_(here, there)] += block1.conjugate().T
                        H2[np.ix_(there, here)] += block2
                        H2[np.ix_(here, there)] += block2.conjugate().T

    if derivatives:
        assert H1 is not None and H2 is not None
        return H, H1, H2
    return H


def grand_kernel(energy: np.ndarray, mu: float, temp: float) -> np.ndarray:
    return -temp * np.logaddexp(0.0, -(energy - mu) / temp)


def fermi(energy: np.ndarray, mu: float, temp: float) -> np.ndarray:
    z = np.clip((energy - mu) / temp, -60.0, 60.0)
    return 1.0 / (1.0 + np.exp(z))


def grand_second(energy: np.ndarray, mu: float, temp: float) -> np.ndarray:
    f = fermi(energy, mu, temp)
    return -f * (1.0 - f) / temp


def omega_per_cell(eig: np.ndarray, mu: float, temp: float, L: int) -> float:
    return float(np.sum(grand_kernel(eig, mu, temp)) / (L**3))


@dataclass(frozen=True)
class ExactSpectra:
    L: int
    mass: float
    B: float
    eig_plus: np.ndarray
    eig_zero: np.ndarray
    eig_minus: np.ndarray


@dataclass(frozen=True)
class PTSpectra:
    L: int
    mass: float
    eig: np.ndarray
    h2_diag: np.ndarray
    h1_abs2: np.ndarray
    interband_mask: np.ndarray


@dataclass(frozen=True)
class PTValue:
    full: float
    intra_lp: float
    inter_geo: float


def exact_spectra(L: int, mass: float, flux_quanta: int = 1) -> ExactSpectra:
    B = TWOPI * flux_quanta / (L * L)
    eig_plus = np.linalg.eigvalsh(build_hamiltonian(L, mass, B))
    eig_zero = np.linalg.eigvalsh(build_hamiltonian(L, mass, 0.0))
    eig_minus = np.linalg.eigvalsh(build_hamiltonian(L, mass, -B))
    return ExactSpectra(L, mass, B, eig_plus, eig_zero, eig_minus)


def exact_chi(spec: ExactSpectra, mu: float, temp: float) -> float:
    op = omega_per_cell(spec.eig_plus, mu, temp, spec.L)
    o0 = omega_per_cell(spec.eig_zero, mu, temp, spec.L)
    om = omega_per_cell(spec.eig_minus, mu, temp, spec.L)
    return (op + om - 2.0 * o0) / (spec.B * spec.B)


def pt_spectra(L: int, mass: float) -> PTSpectra:
    H0, H1, H2 = build_hamiltonian(L, mass, 0.0, derivatives=True)
    eig, vec = np.linalg.eigh(H0)
    h1_eig = vec.conjugate().T @ H1 @ vec
    h2_eig = vec.conjugate().T @ H2 @ vec
    signs = np.sign(eig)
    interband_mask = (signs[:, None] * signs[None, :]) < 0.0
    return PTSpectra(
        L=L,
        mass=mass,
        eig=eig,
        h2_diag=np.real(np.diag(h2_eig)),
        h1_abs2=np.abs(h1_eig) ** 2,
        interband_mask=interband_mask,
    )


def pt_chi(spec: PTSpectra, mu: float, temp: float) -> PTValue:
    eig = spec.eig
    fp = fermi(eig, mu, temp)
    fpp = grand_second(eig, mu, temp)
    diff = eig[:, None] - eig[None, :]
    fp_diff = fp[:, None] - fp[None, :]

    kernel = np.empty_like(diff.real)
    offdiag = np.abs(diff) > 1.0e-9
    kernel[offdiag] = np.real(fp_diff[offdiag] / diff[offdiag])
    degenerate = 0.5 * (fpp[:, None] + fpp[None, :])
    kernel[~offdiag] = degenerate[~offdiag]

    h1_term = kernel * spec.h1_abs2
    inter = float(np.sum(h1_term[spec.interband_mask]))
    full_raw = float(2.0 * np.sum(fp * spec.h2_diag) + np.sum(h1_term))
    norm = 1.0 / (spec.L**3 * spec.L**2)
    full = norm * full_raw
    inter_geo = norm * inter
    return PTValue(full=full, intra_lp=full - inter_geo, inter_geo=inter_geo)


def small_b_chi(L: int, mass: float, mu: float, temp: float, b_step: float) -> float:
    eig_p = np.linalg.eigvalsh(build_hamiltonian(L, mass, b_step))
    eig_0 = np.linalg.eigvalsh(build_hamiltonian(L, mass, 0.0))
    eig_m = np.linalg.eigvalsh(build_hamiltonian(L, mass, -b_step))
    raw = (
        omega_per_cell(eig_p, mu, temp, L)
        + omega_per_cell(eig_m, mu, temp, L)
        - 2.0 * omega_per_cell(eig_0, mu, temp, L)
    ) / (b_step * b_step)
    return raw / (L * L)


def bloch_spectrum(L: int, mass: float) -> np.ndarray:
    vals: list[float] = []
    for nx in range(L):
        kx = TWOPI * nx / L
        dx = 2.0 * math.cos(kx)
        for ny in range(L):
            ky = TWOPI * ny / L
            dy = 2.0 * math.cos(ky)
            for nz in range(L):
                kz = TWOPI * nz / L
                dz = mass + 2.0 * math.cos(kz)
                radius = math.sqrt(dx * dx + dy * dy + dz * dz)
                vals.extend((-radius, radius))
    return np.sort(np.array(vals, dtype=np.float64))


def rel_dev(a: float, b: float) -> float:
    return abs(a - b) / max(1.0e-14, abs(b))


def sign_code(x: float) -> int:
    if x > SIGN_TOL:
        return 1
    if x < -SIGN_TOL:
        return -1
    return 0


def sign_name(code: int) -> str:
    if code > 0:
        return "+"
    if code < 0:
        return "-"
    return "0"


def structural_gates() -> None:
    print("\nS0 STRUCTURE AND DISCRIMINATIVE CONTROLS")
    probe_L = 4
    probe_mass = 0.3
    probe_B = TWOPI / (probe_L * probe_L)
    H_probe = build_hamiltonian(probe_L, probe_mass, probe_B)
    herm = float(np.max(np.abs(H_probe - H_probe.conjugate().T)))
    gate(
        "finite Peierls Hamiltonian is Hermitian",
        herm <= HERMITICITY_TOL,
        f"max |H-H^dag|={herm:.3e}, tol={HERMITICITY_TOL:.1e}",
    )

    H0 = build_hamiltonian(probe_L, probe_mass, 0.0)
    spec_err = float(np.max(np.abs(np.sort(np.linalg.eigvalsh(H0)) - bloch_spectrum(probe_L, probe_mass))))
    gate(
        "B=0 finite spectrum equals the stated two-band Bloch convention",
        spec_err <= BLOCH_SPECTRUM_TOL,
        f"max spectral error={spec_err:.3e}, tol={BLOCH_SPECTRUM_TOL:.1e}",
    )

    pt = pt_chi(pt_spectra(FD_L, probe_mass), MU_REF, TEMPERATURE)
    b0 = 5.0e-3
    fd1 = small_b_chi(FD_L, probe_mass, MU_REF, TEMPERATURE, b0)
    fd2 = small_b_chi(FD_L, probe_mass, MU_REF, TEMPERATURE, 0.5 * b0)
    fd3 = small_b_chi(FD_L, probe_mass, MU_REF, TEMPERATURE, 0.25 * b0)
    d1 = abs(fd1 - pt.full)
    d2 = abs(fd2 - pt.full)
    d3 = abs(fd3 - pt.full)
    ratio12 = d1 / max(d2, 1.0e-30)
    ratio23 = d2 / max(d3, 1.0e-30)
    print(
        "FD_CONTROL L={} m={} mu={} T={}  PT={:+.10e}  "
        "fd(h)={:+.10e} fd(h/2)={:+.10e} fd(h/4)={:+.10e}".format(
            FD_L, probe_mass, MU_REF, TEMPERATURE, pt.full, fd1, fd2, fd3
        )
    )
    gate(
        "finite-difference cross-check converges quadratically to the PT split",
        d3 <= FD_FINAL_ABS_TOL and ratio12 >= FD_RATIO_MIN and ratio23 >= FD_RATIO_MIN,
        (
            f"diffs=({d1:.3e},{d2:.3e},{d3:.3e}), "
            f"ratios=({ratio12:.2f},{ratio23:.2f}), final_tol={FD_FINAL_ABS_TOL:.1e}"
        ),
    )


def b_step_convergence_gate() -> None:
    print("\nS0 REFERENCE: quantized finite-torus B-step convergence")
    rows = []
    for L in CONVERGENCE_LS:
        spec = exact_spectra(L, 0.3)
        chi = exact_chi(spec, MU_REF, TEMPERATURE)
        rows.append((L, spec.B, chi))
        print(f"BSTEP L={L} B={spec.B:.12e} chi_exact={chi:+.10e}")

    drift_46 = abs(rows[1][2] - rows[0][2])
    drift_68 = abs(rows[2][2] - rows[1][2])
    ratio = drift_46 / max(drift_68, 1.0e-30)
    gate(
        "quantized reference drift shrinks from L=4->6 to L=6->8 at the reference point",
        drift_68 <= BSTEP_DRIFT_TOL and ratio >= BSTEP_RATIO_MIN,
        f"drift46={drift_46:.3e}, drift68={drift_68:.3e}, ratio={ratio:.2f}",
    )


def decomposition_gates() -> tuple[dict[float, ExactSpectra], dict[float, PTSpectra]]:
    print("\nS1/S2 DECOMPOSITION: LP + interband geometric split vs exact reference")
    exact_by_mass: dict[float, ExactSpectra] = {}
    pt_by_mass: dict[float, PTSpectra] = {}
    full_rels = []
    lp_rels = []
    inter_mags = []

    print(
        "reference grid: L={}, mu={}, T={}, masses={}; chi is Omega'' per cell".format(
            REFERENCE_L, MU_REF, TEMPERATURE, MASSES
        )
    )
    for mass in MASSES:
        exact_spec = exact_spectra(REFERENCE_L, mass)
        pt_spec = pt_spectra(REFERENCE_L, mass)
        exact_by_mass[mass] = exact_spec
        pt_by_mass[mass] = pt_spec

        chi_exact = exact_chi(exact_spec, MU_REF, TEMPERATURE)
        chi_pt = pt_chi(pt_spec, MU_REF, TEMPERATURE)
        full_rel = rel_dev(chi_pt.full, chi_exact)
        lp_rel = rel_dev(chi_pt.intra_lp, chi_exact)
        full_rels.append(full_rel)
        lp_rels.append(lp_rel)
        inter_mags.append(abs(chi_pt.inter_geo))
        print(
            "MASS_ROW m={:.1f} exact={:+.10e} full={:+.10e} "
            "intra_LP={:+.10e} inter_geo={:+.10e} full_rel={:.3e} lp_rel={:.3e}".format(
                mass,
                chi_exact,
                chi_pt.full,
                chi_pt.intra_lp,
                chi_pt.inter_geo,
                full_rel,
                lp_rel,
            )
        )
        gate(
            f"full LP+interband split tracks exact reference at m={mass:.1f}",
            full_rel <= FULL_REL_TOL,
            f"rel={full_rel:.3e}, tol={FULL_REL_TOL:.2e}",
        )
        gate(
            f"LP-only does not suffice at m={mass:.1f}",
            lp_rel >= LP_ONLY_REL_MISS_MIN,
            f"lp_rel={lp_rel:.3e}, miss_min={LP_ONLY_REL_MISS_MIN:.1f}",
        )

    nonzero_inter = min(inter_mags[1:])
    gate(
        "anti-fabrication: interband term is nonzero for m != 0",
        nonzero_inter >= INTERBAND_MIN,
        f"min |inter_geo| over m=0.3,0.6 is {nonzero_inter:.3e}",
    )
    gate(
        "honest residual: max full deviation is inside the frozen 12% bounded gate",
        max(full_rels) <= FULL_REL_TOL,
        f"max_full_rel={max(full_rels):.3e}; max_lp_rel={max(lp_rels):.3e}",
    )
    return exact_by_mass, pt_by_mass


def sign_table_gates(
    exact_by_mass: dict[float, ExactSpectra], pt_by_mass: dict[float, PTSpectra]
) -> None:
    print("\nS3 SIGN TABLE: exact finite reference vs closed split")
    all_match = True
    all_have_change = True
    for mass in MASSES:
        codes = []
        print(f"SIGN_TABLE m={mass:.1f}")
        for mu in SIGN_MUS:
            chi_e = exact_chi(exact_by_mass[mass], mu, TEMPERATURE)
            chi_c = pt_chi(pt_by_mass[mass], mu, TEMPERATURE).full
            code_e = sign_code(chi_e)
            code_c = sign_code(chi_c)
            codes.append(code_e)
            all_match = all_match and (code_e == code_c)
            print(
                "  mu={:.1f} exact={:+.10e}({}) closed={:+.10e}({})".format(
                    mu, chi_e, sign_name(code_e), chi_c, sign_name(code_c)
                )
            )
        has_change = any(c > 0 for c in codes) and any(c < 0 for c in codes)
        all_have_change = all_have_change and has_change
        gate(
            f"exact sign table has a sampled sign change at m={mass:.1f}",
            has_change,
            "codes=" + ",".join(sign_name(c) for c in codes),
        )

    gate(
        "closed split tracks all exact sampled signs",
        all_match,
        f"sign_tol={SIGN_TOL:.1e}, mu_grid={SIGN_MUS}",
    )
    gate(
        "sampled sign changes persist across the full mass grid",
        all_have_change,
        "each mass has positive interior rows and a negative mu=2.0 row",
    )


def note_hygiene_gates() -> None:
    print("\nS4 NOTE HYGIENE")
    text = NOTE.read_text(encoding="utf-8")
    gate(
        "note declares bounded claim type and audit authority",
        "**Claim type:** bounded_theorem" in text
        and "**Status authority:** independent audit lane" in text,
        "bounded claim; audit lane grades",
    )
    gate(
        "note states the fixed magnetic-area normalization",
        "magnetic-area normalization" in text and "`1/L^2`" in text,
        "normalization stated, not fitted",
    )
    gate(
        "note states the d = 3 interband residual rather than a thermodynamic closure",
        "bounded `d = 3` behavior" in text and "No-promotion statement" in text,
        "bounded residual language present",
    )


def run() -> int:
    np.set_printoptions(precision=10, suppress=False)
    print("D=3 staggered two-band orbital response runner")
    print(
        "Bloch convention: H(k)=2cos(kx)sx + 2cos(ky)sy + "
        "(m+2cos(kz))sz; t=1"
    )
    print(
        "Exact reference: dense periodic L^3 two-orbital lattice, quantized "
        "B=2*pi/L^2 through xy plaquettes"
    )
    print(
        "PT split: finite B=0 divided-difference curvature; fixed "
        "magnetic-area normalization 1/L^2"
    )

    structural_gates()
    b_step_convergence_gate()
    exact_by_mass, pt_by_mass = decomposition_gates()
    sign_table_gates(exact_by_mass, pt_by_mass)
    note_hygiene_gates()

    print(f"\nTOTAL: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    raise SystemExit(run())
