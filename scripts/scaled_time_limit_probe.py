#!/usr/bin/env python3
"""Finite-spin diagnostics for the exact t=tau/C strong-limit theorem."""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 3600
AUDIT_INPUT_PATHS = ('scripts/scaled_time_limit_probe.py', 'scripts/spectral_fixed_time_probe.py')

import importlib.util
import json
import math
from pathlib import Path

import numpy as np
from scipy.linalg import eigh_tridiagonal
from scipy.special import j0

AUDIT_TIMEOUT_SEC = 3600

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("spectral_probe", HERE / "spectral_fixed_time_probe.py")
spectral = importlib.util.module_from_spec(spec)
spec.loader.exec_module(spectral)


def local_curvature_over_C2(spin: int) -> float:
    lo, hi, diag, off = spectral.finite_spin_m(spin)
    C = spin * (spin + 1)
    i = -lo
    a0 = diag[i]
    nearest = (
        off[i - 1] * (a0 + diag[i - 1] - C),
        off[i] * (a0 + diag[i + 1] - C),
    )
    next_nearest = (
        off[i - 2] * off[i - 1],
        off[i] * off[i + 1],
    )
    return -2 * sum(x * x for x in nearest + next_nearest) / C**2


def run(spins=(8, 12, 16, 24, 32, 48, 64), taus=(0.25, 0.5, 1.0)):
    rows = []
    for spin in spins:
        lo, hi, diag, off = spectral.finite_spin_m(spin)
        C = spin * (spin + 1)
        eig, vec = eigh_tridiagonal(diag, off)
        origin = -lo
        weight = vec[origin, :]
        values = []
        for tau in taus:
            phase = np.exp(-1j * tau * (eig * eig / C - eig))
            psi = vec @ (phase * weight)
            n = np.arange(lo, hi + 1)
            vacancy = float(np.sum(np.abs(psi[n % 3 == 0]) ** 2))
            limit = 1 / 3 + 2 / 3 * float(j0(2 * math.sqrt(3) * tau))
            # Independently evaluate the Fourier multiplier difference for the
            # residue-three projector, then compare with the displayed Bessel law.
            angles=2*np.pi*(np.arange(1024)+0.5)/1024
            phase_difference=2*np.cos(angles-2*np.pi/3)-2*np.cos(angles)
            fourier_limit=(1+2*np.mean(np.exp(1j*tau*phase_difference)).real)/3
            assert abs(limit-fourier_limit)<1e-12, (tau,limit,fourier_limit)
            values.append({
                "tau": tau,
                "finite_spin_vacancy": vacancy,
                "bessel_limit": limit,
                "absolute_difference": abs(vacancy - limit),
                "norm_squared": float(np.vdot(psi, psi).real),
            })
        assert all(abs(v['norm_squared']-1)<2e-11 and -1e-12 <= v['finite_spin_vacancy'] <= 1+1e-12 for v in values)
        rows.append({
            "S": spin,
            "C": C,
            "dimension": hi - lo + 1,
            "p_second_derivative_over_C2": local_curvature_over_C2(spin),
            "scaled_times": values,
        })
    return {
        "status": "double-precision diagnostics only; theorem is the strong-operator argument in SHORT_TIME_SCALING_NOTE_2026-09-23.md",
        "spins": list(spins),
        "taus": list(taus),
        "results": rows,
    }


if __name__ == "__main__":
    result = run()
    payload = json.dumps(result, indent=2) + "\n"
    (HERE / "SCALED_TIME_LIMIT_CHECK.json").write_text(payload)
    print(payload, end="")
