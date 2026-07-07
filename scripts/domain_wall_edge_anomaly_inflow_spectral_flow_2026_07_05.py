#!/usr/bin/env python3
"""Domain-wall edge spectral-flow check.

This runner is a free-field background-field diagnostic:

* start from the prior record-time Wilson-domain-wall Hamiltonian;
* couple a non-dynamical U(1) background gauge field by Peierls phases;
* put one magnetic flux quantum through the transverse x-y torus;
* thread a twist phi through the z cycle;
* diagonalize H(phi) on a phi grid and follow localized edge levels by
  eigenvector overlap;
* count zero crossings of the tracked wall and anti-wall edge branches.

The calculation is deterministic and uses only numpy.
"""

from __future__ import annotations

from dataclasses import dataclass
import math

import numpy as np

np.set_printoptions(precision=12, suppress=True, linewidth=160)

PASS = 0
FAIL = 0


def check(name: str, cond: bool, detail: str = "") -> None:
    global PASS, FAIL
    if cond:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    suffix = f"  ({detail})" if detail else ""
    print(f"{tag} - {name}{suffix}")


def section(title: str) -> None:
    print("\n" + "=" * 92)
    print(title)
    print("=" * 92)


def wrap_to_pi(k: float) -> float:
    return float((k + math.pi) % (2.0 * math.pi) - math.pi)


def sign_int(x: float, tol: float = 1.0e-9) -> int:
    if x > tol:
        return 1
    if x < -tol:
        return -1
    return 0


def norm(A: np.ndarray) -> float:
    return float(np.linalg.norm(A))


def periodic_distance(n: int, center: int) -> np.ndarray:
    x = np.arange(n)
    d = np.abs(x - center)
    return np.minimum(d, n - d)


# Prior-domain-wall diagnostic gamma matrices.
I2 = np.eye(2, dtype=complex)
sigma_1 = np.array([[0, 1], [1, 0]], dtype=complex)
sigma_2 = np.array([[0, -1j], [1j, 0]], dtype=complex)
sigma_3 = np.array([[1, 0], [0, -1]], dtype=complex)
tau_1 = sigma_1.copy()
tau_2 = sigma_2.copy()
tau_3 = sigma_3.copy()

G_x = np.kron(tau_1, sigma_1)
G_y = np.kron(tau_1, sigma_2)
G_z = np.kron(tau_1, sigma_3)
G_s = np.kron(tau_2, I2)
G_m = np.kron(tau_3, I2)
edge_chirality = 1j * G_s @ G_m


def covariant_xy_operators(
    Lx: int,
    Ly: int,
    n_flux: int = 1,
) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """Magnetic translations on a two-torus with n_flux U(1) flux quanta.

    Landau gauge:
        U_y(x,y) = exp(i B x)
        U_x(Lx-1,y) = exp(-i B Lx y)
    with B = 2 pi n_flux / (Lx Ly). This gives periodic links with uniform
    plaquette flux modulo the boundary convention.
    """
    n_xy = Lx * Ly
    B = 2.0 * math.pi * n_flux / n_xy
    Ux = np.ones((Lx, Ly), dtype=complex)
    Uy = np.ones((Lx, Ly), dtype=complex)
    for x in range(Lx):
        for y in range(Ly):
            Uy[x, y] = np.exp(1j * B * x)
            if x == Lx - 1:
                Ux[x, y] = np.exp(-1j * B * Lx * y)

    Kx = np.zeros((n_xy, n_xy), dtype=complex)
    Ky = np.zeros((n_xy, n_xy), dtype=complex)
    Lxy = np.zeros((n_xy, n_xy), dtype=complex)

    def idx(x: int, y: int) -> int:
        return (x % Lx) * Ly + (y % Ly)

    for x in range(Lx):
        for y in range(Ly):
            i = idx(x, y)
            for j, u, K in (
                (idx(x + 1, y), Ux[x, y], Kx),
                (idx(x, y + 1), Uy[x, y], Ky),
            ):
                K[i, j] += -0.5j * u
                K[j, i] += 0.5j * np.conj(u)
                Lxy[i, i] += 0.5
                Lxy[j, j] += 0.5
                Lxy[i, j] += -0.5 * u
                Lxy[j, i] += -0.5 * np.conj(u)

    return Kx, Ky, Lxy, Ux, Uy


def plaquette_fluxes(Ux: np.ndarray, Uy: np.ndarray) -> np.ndarray:
    Lx, Ly = Ux.shape
    phases = []
    for x in range(Lx):
        for y in range(Ly):
            loop = (
                Ux[x, y]
                * Uy[(x + 1) % Lx, y]
                * np.conj(Ux[x, (y + 1) % Ly])
                * np.conj(Uy[x, y])
            )
            phases.append(math.atan2(loop.imag, loop.real))
    return np.array(phases, dtype=float)


def record_time_operators(n_s: int) -> tuple[np.ndarray, np.ndarray]:
    K = np.zeros((n_s, n_s), dtype=complex)
    L = np.zeros((n_s, n_s), dtype=complex)
    for s in range(n_s):
        K[s, (s + 1) % n_s] += -0.5j
        K[s, (s - 1) % n_s] += 0.5j
        L[s, s] += 1.0
        L[s, (s + 1) % n_s] += -0.5
        L[s, (s - 1) % n_s] += -0.5
    return K, L


def mass_profile(n_s: int, M: float, front_width: float = 0.0) -> tuple[np.ndarray, int, int]:
    wall = n_s // 4
    anti_wall = wall + n_s // 2
    if front_width <= 0.0:
        m = -M * np.ones(n_s, dtype=float)
        m[wall:anti_wall] = M
    else:
        x = np.arange(n_s)
        phase = np.sin(2.0 * math.pi * (x - wall) / n_s)
        m = M * np.tanh(phase / front_width)
    return m, wall, anti_wall


@dataclass(frozen=True)
class FlowConfig:
    Lx: int = 3
    Ly: int = 3
    Ns: int = 14
    Lz: int = 7
    M: float = 0.8
    front_width: float = 0.0
    phi_steps: int = 15
    n_flux: int = 1
    twist_offset: float = 0.31
    window_width: float = 2.0
    edge_weight_cut: float = 0.10
    chirality_cut: float = 0.40
    crossing_energy_cut: float = 0.30


class DomainWallFluxModel:
    def __init__(self, cfg: FlowConfig):
        self.cfg = cfg
        self.n_xy = cfg.Lx * cfg.Ly
        self.n_sites = self.n_xy * cfg.Ns

        Kx, Ky, Lxy, Ux, Uy = covariant_xy_operators(cfg.Lx, cfg.Ly, cfg.n_flux)
        Ks, Ls = record_time_operators(cfg.Ns)
        m, self.wall, self.anti_wall = mass_profile(cfg.Ns, cfg.M, cfg.front_width)

        Ixy = np.eye(self.n_xy, dtype=complex)
        Is = np.eye(cfg.Ns, dtype=complex)
        In = np.eye(self.n_sites, dtype=complex)

        kinetic = (
            np.kron(np.kron(Kx, Is), G_x)
            + np.kron(np.kron(Ky, Is), G_y)
            + np.kron(np.kron(Ixy, Ks), G_s)
        )
        mass_base = np.kron(Lxy, Is) + np.kron(Ixy, np.diag(m) + Ls)
        self.H_base = kinetic + np.kron(mass_base, G_m)
        self.H_z_wilson = np.kron(In, G_m)
        self.H_z_kinetic = np.kron(In, G_z)
        self.chirality_operator = np.kron(In, edge_chirality)
        self.plaquette_phases = plaquette_fluxes(Ux, Uy)

        self.windows: dict[str, np.ndarray] = {}
        for name, center in (("wall", self.wall), ("anti", self.anti_wall)):
            d = periodic_distance(cfg.Ns, center)
            self.windows[name] = np.exp(-((d / cfg.window_width) ** 2))

    def H(self, kz: float) -> np.ndarray:
        return self.H_base + (1.0 - math.cos(kz)) * self.H_z_wilson + math.sin(kz) * self.H_z_kinetic

    def localization_weights(self, evecs: np.ndarray, center_name: str) -> np.ndarray:
        arr = evecs.reshape(self.n_xy, self.cfg.Ns, 4, -1)
        window = self.windows[center_name]
        return np.sum(np.abs(arr) ** 2 * window[None, :, None, None], axis=(0, 1, 2)).real

    def chirality_expectations(self, evecs: np.ndarray) -> np.ndarray:
        return np.einsum("ij,ij->j", evecs.conj(), self.chirality_operator @ evecs).real


@dataclass
class Branch:
    z_index: int
    energies: list[float]
    momenta: list[float]
    weights: list[float]
    chiralities: list[float]

    @property
    def min_abs_energy(self) -> float:
        return min(abs(e) for e in self.energies)

    @property
    def min_weight(self) -> float:
        return min(self.weights)

    @property
    def mean_chirality(self) -> float:
        return float(np.mean(self.chiralities))


@dataclass
class Crossing:
    z_index: int
    phi_index: int
    e0: float
    e1: float
    k0: float
    k1: float
    w0: float
    w1: float
    chi0: float
    chi1: float

    @property
    def sign(self) -> int:
        if self.e0 < 0.0 < self.e1:
            return 1
        if self.e0 > 0.0 > self.e1:
            return -1
        return 0


@dataclass
class FlowResult:
    cfg: FlowConfig
    flow: dict[str, int]
    crossings: dict[str, list[Crossing]]
    branches: dict[str, list[Branch]]
    min_bulk_gap: float
    min_edge_crossing_weight: float
    min_abs_crossing_chirality: float


def allowed_kz(cfg: FlowConfig, z_index: int, phi: float) -> float:
    return wrap_to_pi(2.0 * math.pi * (z_index + cfg.twist_offset) / cfg.Lz - math.pi + phi / cfg.Lz)


def select_edge_state(
    model: DomainWallFluxModel,
    evals: np.ndarray,
    evecs: np.ndarray,
    center_name: str,
    previous: np.ndarray | None,
) -> tuple[int, float, float]:
    weights = model.localization_weights(evecs, center_name)
    chiralities = model.chirality_expectations(evecs)
    cfg = model.cfg
    candidates = np.where((weights > cfg.edge_weight_cut) & (np.abs(chiralities) > cfg.chirality_cut))[0]
    if candidates.size == 0:
        scores = weights * np.abs(chiralities) / (1.0 + np.abs(evals))
        candidates = np.argsort(scores)[-12:]

    if previous is None:
        score = weights[candidates] * np.abs(chiralities[candidates]) / (1.0 + np.abs(evals[candidates]))
    else:
        overlap = np.abs(evecs[:, candidates].conj().T @ previous)
        tie_break = 1.0e-3 * weights[candidates] * np.abs(chiralities[candidates]) / (1.0 + np.abs(evals[candidates]))
        score = overlap + tie_break

    i = int(candidates[int(np.argmax(score))])
    return i, float(weights[i]), float(chiralities[i])


def count_crossings(branch: Branch, energy_cut: float) -> list[Crossing]:
    crossings: list[Crossing] = []
    for j in range(len(branch.energies) - 1):
        e0 = branch.energies[j]
        e1 = branch.energies[j + 1]
        near_zero = max(abs(e0), abs(e1)) < energy_cut
        if not near_zero:
            continue
        if e0 < 0.0 < e1 or e0 > 0.0 > e1:
            crossings.append(
                Crossing(
                    z_index=branch.z_index,
                    phi_index=j,
                    e0=e0,
                    e1=e1,
                    k0=branch.momenta[j],
                    k1=branch.momenta[j + 1],
                    w0=branch.weights[j],
                    w1=branch.weights[j + 1],
                    chi0=branch.chiralities[j],
                    chi1=branch.chiralities[j + 1],
                )
            )
    return crossings


def run_flow(cfg: FlowConfig) -> FlowResult:
    model = DomainWallFluxModel(cfg)
    phis = np.linspace(0.0, 2.0 * math.pi, cfg.phi_steps)
    tracked: dict[str, list[Branch]] = {"wall": [], "anti": []}
    min_bulk_gap = float("inf")

    for z_index in range(cfg.Lz):
        previous: dict[str, np.ndarray | None] = {"wall": None, "anti": None}
        data = {
            "wall": {"energies": [], "momenta": [], "weights": [], "chiralities": []},
            "anti": {"energies": [], "momenta": [], "weights": [], "chiralities": []},
        }

        for phi in phis:
            kz = allowed_kz(cfg, z_index, float(phi))
            evals, evecs = np.linalg.eigh(model.H(kz))
            wall_weights = model.localization_weights(evecs, "wall")
            anti_weights = model.localization_weights(evecs, "anti")
            chiralities = model.chirality_expectations(evecs)
            edge_like = (
                (np.maximum(wall_weights, anti_weights) > cfg.edge_weight_cut)
                & (np.abs(chiralities) > cfg.chirality_cut)
                & (np.abs(evals) < 1.2)
            )
            bulk_abs = np.abs(evals[~edge_like])
            min_bulk_gap = min(min_bulk_gap, float(np.min(bulk_abs)))

            for center_name in ("wall", "anti"):
                i, weight, chirality = select_edge_state(model, evals, evecs, center_name, previous[center_name])
                previous[center_name] = evecs[:, i]
                data[center_name]["energies"].append(float(evals[i]))
                data[center_name]["momenta"].append(kz)
                data[center_name]["weights"].append(weight)
                data[center_name]["chiralities"].append(chirality)

        for center_name in ("wall", "anti"):
            tracked[center_name].append(
                Branch(
                    z_index=z_index,
                    energies=data[center_name]["energies"],
                    momenta=data[center_name]["momenta"],
                    weights=data[center_name]["weights"],
                    chiralities=data[center_name]["chiralities"],
                )
            )

    crossings: dict[str, list[Crossing]] = {
        center_name: [
            crossing
            for branch in tracked[center_name]
            for crossing in count_crossings(branch, cfg.crossing_energy_cut)
        ]
        for center_name in ("wall", "anti")
    }
    flow = {
        center_name: sum(crossing.sign for crossing in crossings[center_name])
        for center_name in ("wall", "anti")
    }

    all_crossings = crossings["wall"] + crossings["anti"]
    min_edge_crossing_weight = min(
        [min(c.w0, c.w1) for c in all_crossings],
        default=0.0,
    )
    min_abs_crossing_chirality = min(
        [min(abs(c.chi0), abs(c.chi1)) for c in all_crossings],
        default=0.0,
    )

    return FlowResult(
        cfg=cfg,
        flow=flow,
        crossings=crossings,
        branches=tracked,
        min_bulk_gap=min_bulk_gap,
        min_edge_crossing_weight=min_edge_crossing_weight,
        min_abs_crossing_chirality=min_abs_crossing_chirality,
    )


def print_crossing_summary(label: str, result: FlowResult) -> None:
    print(f"\n{label}")
    print(
        "config: "
        f"Lx={result.cfg.Lx} Ly={result.cfg.Ly} Ns={result.cfg.Ns} Lz={result.cfg.Lz} "
        f"M={result.cfg.M:+.3f} width={result.cfg.front_width:.3f} "
        f"phi_steps={result.cfg.phi_steps} flux={result.cfg.n_flux}"
    )
    print(f"flow: wall={result.flow['wall']:+d} anti={result.flow['anti']:+d} net={result.flow['wall'] + result.flow['anti']:+d}")
    print(f"bulk_gap_min={result.min_bulk_gap:.12f}")
    for center_name in ("wall", "anti"):
        print(f"  {center_name} crossings:")
        for c in result.crossings[center_name]:
            print(
                "    "
                f"z={c.z_index} phi_step={c.phi_index}->{c.phi_index + 1} "
                f"E={c.e0:+.12f}->{c.e1:+.12f} "
                f"k={c.k0:+.12f}->{c.k1:+.12f} "
                f"weight={c.w0:.6f}->{c.w1:.6f} "
                f"chi={c.chi0:+.6f}->{c.chi1:+.6f} "
                f"sign={c.sign:+d}"
            )
    print("  near-zero tracked branch endpoints:")
    for center_name in ("wall", "anti"):
        for branch in result.branches[center_name]:
            if branch.min_abs_energy < 0.25:
                print(
                    "    "
                    f"{center_name} z={branch.z_index}: "
                    f"E0={branch.energies[0]:+.12f} Eend={branch.energies[-1]:+.12f} "
                    f"min|E|={branch.min_abs_energy:.12f} "
                    f"min_weight={branch.min_weight:.6f} "
                    f"mean_chi={branch.mean_chirality:+.6f}"
                )


def verify_background_flux() -> None:
    section("1. Background U(1) flux and Hermiticity")
    cfg = FlowConfig()
    model = DomainWallFluxModel(cfg)
    flux_total = float(np.sum(model.plaquette_phases))
    expected_total = 2.0 * math.pi * cfg.n_flux
    H0 = model.H(0.123)
    check(
        "magnetic Peierls links carry one total U(1) flux quantum",
        abs(flux_total - expected_total) < 1.0e-12,
        f"sum_plaquette_phase={flux_total:.12f} expected={expected_total:.12f}",
    )
    check(
        "gauge-coupled domain-wall Hamiltonian is Hermitian",
        norm(H0 - H0.conj().T) < 1.0e-12,
        f"||H-H^dagger||={norm(H0 - H0.conj().T):.3e}",
    )


def main() -> None:
    verify_background_flux()

    section("2. Spectral flow of localized wall and anti-wall edge branches")
    main_cfg = FlowConfig(M=0.8, front_width=0.0, Ns=14, Lz=7, phi_steps=15)
    main_result = run_flow(main_cfg)
    print_crossing_summary("positive mass orientation", main_result)
    wall_cross = main_result.crossings["wall"][0]
    anti_cross = main_result.crossings["anti"][0]
    check(
        "wall spectral flow is the integer +1",
        main_result.flow["wall"] == 1 and len(main_result.crossings["wall"]) == 1,
        f"wall_flow={main_result.flow['wall']} crossings={len(main_result.crossings['wall'])}",
    )
    check(
        "anti-wall spectral flow is the integer -1",
        main_result.flow["anti"] == -1 and len(main_result.crossings["anti"]) == 1,
        f"anti_flow={main_result.flow['anti']} crossings={len(main_result.crossings['anti'])}",
    )
    check(
        "record-time torus has zero net spectral flow",
        main_result.flow["wall"] + main_result.flow["anti"] == 0,
        f"net={main_result.flow['wall'] + main_result.flow['anti']}",
    )
    check(
        "crossing states are localized edge states",
        main_result.min_edge_crossing_weight > 0.45 and main_result.min_abs_crossing_chirality > 0.97,
        f"min_crossing_weight={main_result.min_edge_crossing_weight:.6f} min|chi|={main_result.min_abs_crossing_chirality:.6f}",
    )
    check(
        "bulk states stay gapped while edge levels cross",
        main_result.min_bulk_gap > 0.55,
        f"min_bulk_gap={main_result.min_bulk_gap:.12f}",
    )
    check(
        "flow sign tracks measured edge chirality",
        wall_cross.sign == sign_int(0.5 * (wall_cross.chi0 + wall_cross.chi1))
        and anti_cross.sign == sign_int(0.5 * (anti_cross.chi0 + anti_cross.chi1)),
        (
            f"wall sign/chi={wall_cross.sign:+d}/{0.5 * (wall_cross.chi0 + wall_cross.chi1):+.6f}; "
            f"anti sign/chi={anti_cross.sign:+d}/{0.5 * (anti_cross.chi0 + anti_cross.chi1):+.6f}"
        ),
    )

    section("3. Chirality flip re-diagonalizes and reverses the flow")
    flip_cfg = FlowConfig(M=-0.8, front_width=0.0, Ns=14, Lz=7, phi_steps=15)
    flip_result = run_flow(flip_cfg)
    print_crossing_summary("flipped mass orientation", flip_result)
    flip_wall_cross = flip_result.crossings["wall"][0]
    flip_anti_cross = flip_result.crossings["anti"][0]
    check(
        "flipping the wall chirality reverses wall and anti-wall flow",
        flip_result.flow["wall"] == -main_result.flow["wall"]
        and flip_result.flow["anti"] == -main_result.flow["anti"],
        (
            f"M=+ flow=({main_result.flow['wall']:+d},{main_result.flow['anti']:+d}); "
            f"M=- flow=({flip_result.flow['wall']:+d},{flip_result.flow['anti']:+d})"
        ),
    )
    check(
        "flipped flow sign tracks flipped measured chirality",
        flip_wall_cross.sign == sign_int(0.5 * (flip_wall_cross.chi0 + flip_wall_cross.chi1))
        and flip_anti_cross.sign == sign_int(0.5 * (flip_anti_cross.chi0 + flip_anti_cross.chi1)),
        (
            f"wall sign/chi={flip_wall_cross.sign:+d}/{0.5 * (flip_wall_cross.chi0 + flip_wall_cross.chi1):+.6f}; "
            f"anti sign/chi={flip_anti_cross.sign:+d}/{0.5 * (flip_anti_cross.chi0 + flip_anti_cross.chi1):+.6f}"
        ),
    )

    section("4. Quantization and robustness")
    robust_configs = [
        FlowConfig(M=0.8, front_width=0.0, Ns=12, Lz=5, phi_steps=11),
        FlowConfig(M=0.8, front_width=0.0, Ns=14, Lz=7, phi_steps=11),
        FlowConfig(M=0.8, front_width=0.45, Ns=14, Lz=7, phi_steps=11),
        FlowConfig(M=0.8, front_width=0.0, Ns=16, Lz=7, phi_steps=11),
    ]
    robust_rows = []
    for cfg in robust_configs:
        result = run_flow(cfg)
        robust_rows.append(result)
        print(
            f"robust row: Ns={cfg.Ns:2d} Lz={cfg.Lz:2d} width={cfg.front_width:.2f} "
            f"wall={result.flow['wall']:+d} anti={result.flow['anti']:+d} "
            f"net={result.flow['wall'] + result.flow['anti']:+d} "
            f"bulk_gap={result.min_bulk_gap:.12f}"
        )
    check(
        "integer flow is stable under lattice-size and front-width changes",
        all(r.flow["wall"] == 1 and r.flow["anti"] == -1 for r in robust_rows),
        "rows=" + ", ".join(f"({r.flow['wall']:+d},{r.flow['anti']:+d})" for r in robust_rows),
    )
    check(
        "robustness rows keep the bulk gapped",
        all(r.min_bulk_gap > 0.55 for r in robust_rows),
        "min_bulk_gap=" + f"{min(r.min_bulk_gap for r in robust_rows):.12f}",
    )

    print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
    if FAIL:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
