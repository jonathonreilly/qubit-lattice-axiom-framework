#!/usr/bin/env python3
"""Bounded hard-bar certificate for the QNM hardening feasibility row.

This runner deliberately does not certify a positive QNM law.  It checks the
controls requested by the audit row and asserts the bounded negative result:
on the tested reduced grids, self-coupling can create apparent absorption
minima, but every such minimum lies at or beyond the lattice Nyquist boundary.
The sub-Nyquist peak set remains empty under threshold, damping, and refinement
checks, while the fixed-field Born/Sorkin check stays machine clean.
"""

from __future__ import annotations

import math
from pathlib import Path
from typing import Iterable

import numpy as np

import qnm_scaling as qnm


ROOT = Path(__file__).resolve().parents[1]
TOL_BORN = 1e-11
MAX_RELAX_RESIDUAL = 6e-3
G_TEST = 0.10
SOURCE_STRENGTH = 0.004
K_REF = 5.0


def _configure(h: float, length: float, width: float, max_d_phys: float):
    qnm.H = h
    qnm.PHYS_L = length
    qnm.PHYS_W = width
    qnm.MAX_D_PHYS = max_d_phys
    return qnm._setup()


def _relaxed_field(
    nl: int,
    nw: int,
    npl: int,
    hw: int,
    offsets,
    transfer_norm: float,
    pos: np.ndarray,
    *,
    source_strength: float,
    self_coupling: float,
    damping: float,
    iterations: int,
) -> tuple[np.ndarray, float]:
    ext = qnm._ext_field(nl, npl, pos, source_strength)
    total = ext.copy()
    self_field = np.zeros((nl, npl))
    residual = math.inf
    for _ in range(iterations):
        amps = qnm._prop(nl, nw, npl, hw, offsets, transfer_norm, total, K_REF)
        next_self_raw = qnm._self_field(amps, nl, npl, pos, self_coupling)
        next_self = damping * next_self_raw + (1.0 - damping) * self_field
        residual = float(
            np.linalg.norm(next_self - self_field) / (np.linalg.norm(next_self) + 1e-30)
        )
        self_field = next_self
        total = ext + self_field
    return total, residual


def _prop_sources(
    nl: int,
    nw: int,
    npl: int,
    hw: int,
    offsets,
    transfer_norm: float,
    field: np.ndarray,
    k_value: float,
    source_indices: Iterable[int],
) -> np.ndarray:
    amps = np.zeros((nl, npl), dtype=np.complex128)
    for source_index in source_indices:
        amps[0, source_index] += 1.0
    for layer in range(nl - 1):
        source_amp = amps[layer]
        if np.max(np.abs(source_amp)) < 1e-300:
            continue
        sf = field[layer]
        df = field[min(layer + 1, nl - 1)]
        for dy, dz, length, weight_raw in offsets:
            ymin, ymax = max(0, -dy), min(nw, nw - dy)
            zmin, zmax = max(0, -dz), min(nw, nw - dz)
            if ymin >= ymax or zmin >= zmax:
                continue
            yi, zi = np.meshgrid(
                np.arange(ymin, ymax), np.arange(zmin, zmax), indexing="ij"
            )
            src = yi.ravel() * nw + zi.ravel()
            dst = (yi.ravel() + dy) * nw + (zi.ravel() + dz)
            amp = source_amp[src]
            mask = np.abs(amp) > 1e-300
            if not np.any(mask):
                continue
            src_m, dst_m, amp_m = src[mask], dst[mask], amp[mask]
            local_field = 0.5 * (sf[src_m] + df[dst_m])
            phase = k_value * length * (1.0 - local_field)
            step = amp_m * (np.cos(phase) + 1j * np.sin(phase)) * weight_raw / transfer_norm
            np.add.at(amps[layer + 1], dst_m, step)
    return amps


def _sorkin_i3(
    nl: int,
    nw: int,
    npl: int,
    hw: int,
    offsets,
    transfer_norm: float,
    field: np.ndarray,
) -> float:
    center = hw * nw + hw
    sources = (center, (hw + 1) * nw + hw, hw * nw + (hw + 1))

    def prob(active: tuple[int, ...]) -> float:
        amps = _prop_sources(nl, nw, npl, hw, offsets, transfer_norm, field, K_REF, active)
        return float(np.sum(np.abs(amps[-1]) ** 2))

    pa, pb, pc = (prob((s,)) for s in sources)
    pab = prob((sources[0], sources[1]))
    pac = prob((sources[0], sources[2]))
    pbc = prob((sources[1], sources[2]))
    pabc = prob(sources)
    i3 = pabc - pab - pac - pbc + pa + pb + pc
    return abs(i3) / max(pabc, 1e-30)


def _peaks(k_values: np.ndarray, escapes: np.ndarray, threshold: float) -> list[float]:
    return [float(v) for v in qnm._find_absorption_peaks(k_values, escapes, threshold)]


def _sub_nyquist(peaks: Iterable[float], nyquist: float) -> list[float]:
    return [float(p) for p in peaks if p < 0.95 * nyquist]


def _case(name: str, *, h: float, length: float, width: float, damping: float) -> dict:
    nl, hw, nw, npl, offsets, transfer_norm, pos = _configure(h, length, width, 2.0)
    k_values = np.arange(2.0, 10.0, 0.5)
    windows = {
        "k2-8": k_values[k_values <= 8.0],
        "k2-10": k_values,
    }
    nyquist = math.pi / h

    g0_field, g0_residual = _relaxed_field(
        nl,
        nw,
        npl,
        hw,
        offsets,
        transfer_norm,
        pos,
        source_strength=SOURCE_STRENGTH,
        self_coupling=0.0,
        damping=damping,
        iterations=40,
    )
    g_field, g_residual = _relaxed_field(
        nl,
        nw,
        npl,
        hw,
        offsets,
        transfer_norm,
        pos,
        source_strength=SOURCE_STRENGTH,
        self_coupling=G_TEST,
        damping=damping,
        iterations=120,
    )

    g0_spectrum = qnm._absorption_spectrum(nl, nw, npl, hw, offsets, transfer_norm, g0_field, k_values)
    g_spectrum = qnm._absorption_spectrum(nl, nw, npl, hw, offsets, transfer_norm, g_field, k_values)
    born_error = _sorkin_i3(nl, nw, npl, hw, offsets, transfer_norm, g_field)

    thresholds = (0.5, 0.8)
    peak_sets = {
        window_name: {
            threshold: {
                "g0": _peaks(window_values, g0_spectrum[: len(window_values)], threshold),
                "gtest": _peaks(window_values, g_spectrum[: len(window_values)], threshold),
            }
            for threshold in thresholds
        }
        for window_name, window_values in windows.items()
    }
    sub_nyquist = {
        window_name: {
            threshold: {
                side: _sub_nyquist(values, nyquist)
                for side, values in sides.items()
            }
            for threshold, sides in threshold_sets.items()
        }
        for window_name, threshold_sets in peak_sets.items()
    }

    assert g0_residual < 1e-14, (name, g0_residual)
    assert g_residual < MAX_RELAX_RESIDUAL, (name, g_residual)
    assert born_error < TOL_BORN, (name, born_error)
    for window_name, threshold_sets in sub_nyquist.items():
        for threshold, sides in threshold_sets.items():
            assert sides["g0"] == [], (name, window_name, threshold, sides["g0"])
            assert sides["gtest"] == [], (name, window_name, threshold, sides["gtest"])

    print(
        f"{name}: h={h:.2f} damping={damping:.2f} nyquist={nyquist:.3f} "
        f"relax_residual={g_residual:.3e} born_i3={born_error:.3e}"
    )
    for window_name in windows:
        for threshold in thresholds:
            print(
                f"  window={window_name} threshold={threshold:.1f} "
                f"G0_peaks={peak_sets[window_name][threshold]['g0']} "
                f"G{G_TEST:.2f}_peaks={peak_sets[window_name][threshold]['gtest']} "
                f"sub_nyquist_G{G_TEST:.2f}={sub_nyquist[window_name][threshold]['gtest']}"
            )
    print(
        f"  min_escape_G0={float(np.min(g0_spectrum)):.3e} "
        f"min_escape_G{G_TEST:.2f}={float(np.min(g_spectrum)):.3e}"
    )
    return {
        "name": name,
        "nyquist": nyquist,
        "born_error": born_error,
        "relax_residual": g_residual,
        "sub_nyquist": sub_nyquist,
    }


def main() -> None:
    cases = [
        ("coarse-damping005", {"h": 1.0, "length": 16.0, "width": 4.0, "damping": 0.05}),
        ("coarse-damping010", {"h": 1.0, "length": 16.0, "width": 4.0, "damping": 0.10}),
        ("refined-damping005", {"h": 0.75, "length": 15.0, "width": 3.75, "damping": 0.05}),
    ]
    results = [_case(name, **kwargs) for name, kwargs in cases]
    assert all(r["born_error"] < TOL_BORN for r in results)
    assert all(r["relax_residual"] < MAX_RELAX_RESIDUAL for r in results)
    note_text = (ROOT / "docs/QNM_HARDENING_FEASIBILITY_NOTE.md").read_text(encoding="utf-8")
    note_flat = " ".join(note_text.split())
    assert "Downstream source-boundary firewall" in note_text
    assert "do not cite this packet as a positive QNM spectral law" in note_flat
    assert "stable sub-Nyquist QNM hardening peaks" in note_flat
    assert "fixed-field Born/Sorkin checks" in note_flat
    assert "dedicated note and log pair" in note_flat
    print("SOURCE FIREWALL PASS: QNM packet remains a bounded negative/open gate, not a positive spectral law")
    print(
        "CERTIFICATE PASS: no sub-Nyquist QNM hardening peak survives the "
        "G=0/null, fixed-field Born, threshold, window, damping, and "
        "refinement hard bars"
    )


if __name__ == "__main__":
    main()
