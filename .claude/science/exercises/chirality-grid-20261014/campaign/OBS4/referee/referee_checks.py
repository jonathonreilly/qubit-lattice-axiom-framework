"""Independent numerical spot-checks for the OBS-4 referee record.

The flavour reconstruction below intentionally does not import obs4_core.py:
singular vectors are obtained from Hermitian eigensystems rather than the
worker's SVD helper.  The optional ``potential`` mode reruns the worker's
reported differential-evolution point solely to test boundedness from below.
"""

from __future__ import annotations

import itertools
import sys

import numpy as np


VEV = 174.1
MU = np.array([2.16e-3, 1.2730, 172.57])
MD = np.array([4.70e-3, 0.0935, 4.183])
LAM = {
    "K_Re": 1.8e4,
    "K_Im": 3.2e5,
    "D_Re": 6.2e3,
    "D_Im": 1.5e4,
    "Bd_Re": 1.9e3,
    "Bd_Im": 3.6e3,
    "Bs_abs": 3.7e2,
}
SUPPORT = {
    "0": [(0, 0), (1, 1), (2, 2)],
    "x": [(1, 2), (2, 1)],
    "y": [(0, 2), (2, 0)],
    "z": [(0, 1), (1, 0)],
}


def ckm_target() -> np.ndarray:
    lam, a, rhobar, etabar = 0.22501, 0.826, 0.1591, 0.3523
    s12 = lam
    s23 = a * lam**2
    z = (
        a
        * lam**3
        * (rhobar + 1j * etabar)
        * np.sqrt(1 - a**2 * lam**4)
        / (np.sqrt(1 - lam**2) * (1 - a**2 * lam**4 * (rhobar + 1j * etabar)))
    )
    s13, delta = abs(z), np.angle(z)
    c12, c23, c13 = np.sqrt(1 - s12**2), np.sqrt(1 - s23**2), np.sqrt(1 - s13**2)
    e = np.exp(1j * delta)
    return np.array(
        [
            [c12 * c13, s12 * c13, s13 / e],
            [-s12 * c23 - c12 * s23 * s13 * e, c12 * c23 - s12 * s23 * s13 * e, s23 * c13],
            [s12 * s23 - c12 * c23 * s13 * e, -c12 * s23 - s12 * c23 * s13 * e, c23 * c13],
        ]
    )


def texture(p: np.ndarray, d120: bool) -> np.ndarray:
    phases = np.zeros((3, 3))
    phases[0, 1], phases[0, 2], phases[1, 0], phases[1, 2], phases[2, 0], phases[2, 1] = p[1:7]
    z = np.exp(1j * phases)
    diag = np.exp(p[0]) * (np.exp(2j * np.pi * np.arange(3) / 3) if d120 else 1)
    z[np.diag_indices(3)] = diag
    return z


def mass_matrix(p: np.ndarray, masses: np.ndarray, d120: bool) -> np.ndarray:
    z = texture(p, d120)
    largest = np.sqrt(np.linalg.eigvalsh(z @ z.conj().T).max())
    return z * masses[-1] / largest


def diagonalise(m: np.ndarray) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    values, left = np.linalg.eigh(m @ m.conj().T)
    order = np.argsort(values)
    singular = np.sqrt(np.clip(values[order], 0, None))
    left = left[:, order]
    right = m.conj().T @ left / singular[None, :]
    # Correct the tiny loss of orthogonality in the light singular vector.
    right, _ = np.linalg.qr(right)
    phases = np.angle(np.diag(left.conj().T @ m @ right))
    right = right @ np.diag(np.exp(-1j * phases))
    return left, singular, right


def rephase_to_pdg(wu, xu, wd, xd):
    target = ckm_target()
    current = wu.conj().T @ wd
    alpha = np.angle(current[:, 0]) - np.angle(target[:, 0])
    beta = alpha[0] - np.angle(current[0, :]) + np.angle(target[0, :])
    da, db = np.diag(np.exp(1j * alpha)), np.diag(np.exp(1j * beta))
    return wu @ da, xu @ da, wd @ db, xd @ db


def projected_hats(m, left, right):
    out = {}
    for key, positions in SUPPORT.items():
        p = np.zeros_like(m)
        for i, j in positions:
            p[i, j] = m[i, j]
        out[key] = left.conj().T @ p @ right
    return out


def pair_sum(hats, i, j, vk):
    return sum(hats[k][i, j] * np.conj(hats[k][j, i]) / vk**2 for k in SUPPORT)


def flavour_check(tag: str, d120: bool):
    p = np.load(f"scripts/univ_{tag}.npz")["p"]
    mu, md = mass_matrix(p[:7], MU, d120), mass_matrix(p[7:], MD, d120)
    wu, su, xu = diagonalise(mu)
    wd, sd, xd = diagonalise(md)
    j = (wu.conj().T @ wd)[0, 1] * (wu.conj().T @ wd)[1, 2]
    j *= np.conj((wu.conj().T @ wd)[0, 2]) * np.conj((wu.conj().T @ wd)[1, 1])
    if j.imag < 0:
        mu, md = mu.conj(), md.conj()
        wu, su, xu = diagonalise(mu)
        wd, sd, xd = diagonalise(md)
    wu, xu, wd, xd = rephase_to_pdg(wu, xu, wd, xd)
    hu, hd = projected_hats(mu, wu, xu), projected_hats(md, wd, xd)
    vk = VEV / 2
    print(f"{tag}: max mass residual u={np.max(abs(su-MU)):.3e} GeV d={np.max(abs(sd-MD)):.3e} GeV")
    print(f"  max |V-V_PDG|={np.max(abs(wu.conj().T @ wd-ckm_target())):.3e}")
    print(f"  |Y0_uc|={abs(hu['0'][0,1])/vk:.6f}, |Y0_cu|={abs(hu['0'][1,0])/vk:.6f}")
    print(f"  |Y0_sd|={abs(hd['0'][1,0])/vk:.6f}, |Y0_ds|={abs(hd['0'][0,1])/vk:.6f}")
    light_u = sum(hu.values()) / VEV
    light_d = sum(hd.values()) / VEV
    print(
        "  Higgs-direction offdiag maxima "
        f"u={np.max(abs(light_u-np.diag(np.diag(light_u)))):.3e} "
        f"d={np.max(abs(light_d-np.diag(np.diag(light_d)))):.3e}"
    )
    z = {
        "K": pair_sum(hd, 1, 0, vk),
        "D": pair_sum(hu, 1, 0, vk),
        "Bd": pair_sum(hd, 2, 0, vk),
        "Bs": pair_sum(hd, 2, 1, vk),
    }
    rows = {
        "K_Re": LAM["K_Re"] * np.sqrt(abs(z["K"].real)),
        "K_Im": LAM["K_Im"] * np.sqrt(abs(z["K"].imag)),
        "D_Re": LAM["D_Re"] * np.sqrt(abs(z["D"].real)),
        "D_Im": LAM["D_Im"] * np.sqrt(abs(z["D"].imag)),
        "Bd_Re": LAM["Bd_Re"] * np.sqrt(abs(z["Bd"].real)),
        "Bd_Im": LAM["Bd_Im"] * np.sqrt(abs(z["Bd"].imag)),
        "Bs_abs": LAM["Bs_abs"] * np.sqrt(abs(z["Bs"])),
    }
    print("  pair sums " + ", ".join(f"{k}={v.real:+.6e}{v.imag:+.6e}i" for k, v in z.items()))
    print("  M* rows (TeV) " + ", ".join(f"{k}={v:.3f}" for k, v in rows.items()))
    print(f"  M* max={max(rows.values()):.3f} TeV")


def translation_and_quartic_count():
    corners = {
        "hw0": (0, 0, 0),
        "hx": (1, 0, 0),
        "hy": (0, 1, 0),
        "hz": (0, 0, 1),
        "Kx": (0, 1, 1),
        "Ky": (1, 0, 1),
        "Kz": (1, 1, 0),
        "hw3": (1, 1, 1),
    }
    translations = [n for n in itertools.product(range(2), repeat=3) if all(sum(k * x for k, x in zip(corners[name], n)) % 2 == 0 for name in ("Kx", "Ky", "Kz"))]
    labels = {name: tuple(sum(q * n_i for q, n_i in zip(momentum, n)) % 2 for n in translations) for name, momentum in corners.items()}
    print(f"residual translations mod 2: {translations}")
    print("residual labels: " + ", ".join(f"{name}:{label}" for name, label in labels.items()))

    q = [0, 1, 2, 3]
    quads = [t for t in itertools.product(range(4), repeat=4) if q[t[0]] ^ q[t[1]] ^ q[t[2]] ^ q[t[3]] == 0]
    seen, orbits = set(), []
    for a, b, c, d in quads:
        orbit = {(a, b, c, d), (b, a, d, c), (c, d, a, b), (d, c, b, a)}
        if (a, b, c, d) not in seen:
            seen |= orbit
            orbits.append(orbit)
    all_distinct = [orbit for orbit in orbits if len(set(next(iter(orbit)))) == 4]
    print(f"quartic Hermitian orbits={len(orbits)}, all-four-field source orbits={len(all_distinct)}")
    vx = 57.5 / np.sqrt(4 * np.pi)
    product = ((VEV**2 - vx**2) / 3) ** 1.5
    one = np.sqrt(4 * np.pi * product / vx) / 1e3
    coherent = np.sqrt(len(all_distinct)) * one
    print(f"single-source 4pi ceiling={one:.6f} TeV; coherent {len(all_distinct)}-source scale={coherent:.6f} TeV")


def potential_bfb_check(lmax: float = 4 * np.pi):
    from scipy.optimize import differential_evolution

    sys.path.insert(0, "scripts")
    import obs4_potential as pot

    bounds = [(-1, 1)] * pot.NL + [(0.0, np.pi / 2)] * 3
    result = differential_evolution(
        pot.objective,
        bounds,
        args=(lmax,),
        seed=int(lmax),
        maxiter=150,
        popsize=12,
        tol=1e-8,
        polish=False,
    )
    eigenvalues, vevs, _ = pot.spectrum(result.x, lmax)
    print(f"reproduced objective={-result.fun:.6f} TeV; vevs={np.round(vevs, 3)}")
    print(f"physical masses={np.round(np.sqrt(np.clip(np.sort(eigenvalues[3:]), 0, None))/1e3, 6)}")
    tensor = pot.lam_tensor(result.x[: pot.NL] * lmax)
    rng = np.random.default_rng(9417)
    best = np.inf
    best_neutral = np.inf
    for _ in range(200):
        raw = rng.normal(size=(512, 4, 2)) + 1j * rng.normal(size=(512, 4, 2))
        raw /= np.sqrt(np.sum(abs(raw) ** 2, axis=(1, 2)))[:, None, None]
        bilinear = np.einsum("nai,nbi->nab", raw.conj(), raw)
        values = np.einsum("abcd,nab,ncd->n", tensor, bilinear, bilinear).real
        best = min(best, values.min())
        neutral = raw.copy()
        neutral[:, :, 0] = 0
        neutral /= np.sqrt(np.sum(abs(neutral) ** 2, axis=(1, 2)))[:, None, None]
        bilinear_n = np.einsum("nai,nbi->nab", neutral.conj(), neutral)
        values_n = np.einsum("abcd,nab,ncd->n", tensor, bilinear_n, bilinear_n).real
        best_neutral = min(best_neutral, values_n.min())
    print(f"sampled min V4 on unit sphere: general={best:.6e}, neutral={best_neutral:.6e}")
    print("BFB sampled result: " + ("FAIL (negative quartic direction found)" if best < 0 else "no negative direction found"))


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] in {"potential", "potential8"}:
        potential_bfb_check((8 if sys.argv[1] == "potential8" else 4) * np.pi)
    else:
        flavour_check("B_gen", False)
        flavour_check("B_gen120", True)
        translation_and_quartic_count()
