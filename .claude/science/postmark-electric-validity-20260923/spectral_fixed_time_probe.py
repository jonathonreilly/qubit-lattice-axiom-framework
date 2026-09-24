#!/usr/bin/env python3
"""Spectral fixed-time diagnostics for the exact and candidate Jacobi generators.

The finite-spin generator is evaluated as f(M_S)=M_S^2-C M_S, so its
propagation is computed from the symmetric-tridiagonal spectral theorem. The
candidate generator is a symmetric pentadiagonal principal compression. All
reported values are floating-point diagnostics, not enclosures or limits.
"""
from __future__ import annotations
import argparse
import importlib.util
import json
import math
from fractions import Fraction
from pathlib import Path
import numpy as np
from scipy.linalg import eigh_tridiagonal, eig_banded

AUDIT_TIMEOUT_SEC = 3600

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("core", HERE / "core_derivation.py")
core = importlib.util.module_from_spec(spec)
spec.loader.exec_module(core)
JACOBI = json.loads((HERE / "FINITE_SPIN_JACOBI_COEFFICIENTS.json").read_text())
D_TABLE = json.loads((HERE / "D_RESIDUE_POLYNOMIALS.json").read_text())
TIMES = (0.25, 0.5, 1.0)
DEFAULT_SPINS = (24, 32, 48, 64, 96, 128, 192, 256, 384)
VACANCY_RESIDUES_MOD_15 = tuple(r for r in range(15) if r % 3 == 0)


def checked_vacancy_mask(domain, states):
    mask = []
    for n, state in zip(domain, states):
        vacancy = state[0][3] == 0
        path_class = n % 3 == 0
        if vacancy != path_class:
            raise ArithmeticError((n, state[0], vacancy, path_class))
        mask.append(vacancy)
    return np.asarray(mask, dtype=bool)


def polynomial(coefficients, k: int) -> Fraction:
    a, b, c = map(Fraction, coefficients)
    return a * k * k + b * k + c


def residue_row(table, n: int):
    k, r = divmod(n, 15)
    return k, table["rows"][r]


def finite_spin_m(spin: int):
    lo, hi = -5 * spin, 5 * spin - 4
    C = spin * (spin + 1)
    diag, off = [], []
    for n in range(lo, hi + 1):
        k, row = residue_row(JACOBI, n)
        y1 = polynomial(row["return_x1_k2_k_const"], k)
        y2 = polynomial(row["return_x2_k2_k_const"], k)
        diag.append(float(2 - (y1 + y2) / C))
        if n < hi:
            x1 = polynomial(row["edge_x1_k2_k_const"], k)
            x2 = polynomial(row["edge_x2_k2_k_const"], k)
            rad = (1 - float(x1 / C)) * (1 - float(x2 / C))
            if rad < -1e-13:
                raise ArithmeticError((spin, n, rad))
            off.append(math.sqrt(max(0.0, rad)))
    return lo, hi, np.asarray(diag), np.asarray(off)


def sample_eigensystem(eigenvalues, eigenvectors, origin_index: int,
                       observable_mask, residue_index, times, phase_map):
    spectral_weight = eigenvectors[origin_index, :]
    out = []
    for t in times:
        phases = np.exp(-1j * t * phase_map(eigenvalues))
        psi = eigenvectors @ (phases * spectral_weight)
        residue_probability = [float(np.sum(np.abs(psi[residue_index == r]) ** 2))
                               for r in range(15)]
        vacancy = float(np.sum(np.abs(psi[observable_mask]) ** 2))
        probabilities_mod_3 = [sum(residue_probability[r] for r in range(15)
                                   if r % 3 == j) for j in range(3)]
        vacancy_by_cells = sum(residue_probability[r]
                               for r in VACANCY_RESIDUES_MOD_15)
        omega = complex(-0.5, math.sqrt(3) / 2)
        character = sum(probabilities_mod_3[j] * omega ** j for j in range(3))
        vacancy_from_character = (1 + 2 * character.real) / 3
        if abs(vacancy - vacancy_by_cells) > 2e-11:
            raise ArithmeticError((vacancy, vacancy_by_cells))
        if abs(vacancy - probabilities_mod_3[0]) > 2e-11:
            raise ArithmeticError((vacancy, probabilities_mod_3))
        if abs(vacancy - vacancy_from_character) > 2e-11:
            raise ArithmeticError((vacancy, vacancy_from_character, character))
        out.append({
            "time": t,
            "vacancy_B3": vacancy,
            "residue_probabilities_mod_15": residue_probability,
            "path_class_probabilities_mod_3": probabilities_mod_3,
            "vacancy_character_mod_3": [float(character.real), float(character.imag)],
            "vacancy_from_character_mod_3": float(vacancy_from_character),
            "max_residue_deviation_from_1_over_15": max(
                abs(x - 1 / 15) for x in residue_probability),
            "norm_squared": float(np.vdot(psi, psi).real),
        })
    return out


def propagate_tridiagonal(diag, off, origin_index: int, observable_mask,
                          residue_index, times, phase_map):
    eigenvalues, eigenvectors = eigh_tridiagonal(diag, off)
    return sample_eigensystem(eigenvalues, eigenvectors, origin_index,
                              observable_mask, residue_index, times, phase_map)


def exact_spin(spin: int):
    lo, hi, diag, off = finite_spin_m(spin)
    nodes = core.walk_nodes(max(abs(lo), abs(hi)) + 1)
    states = [nodes[n] for n in range(lo, hi + 1)]
    mask = checked_vacancy_mask(range(lo, hi + 1), states)
    residues = np.asarray([n % 15 for n in range(lo, hi + 1)], dtype=int)
    C = spin * (spin + 1)
    values = propagate_tridiagonal(diag, off, -lo, mask, residues, TIMES,
                       lambda x: x * x - C * x)
    return {"S": spin, "C": C, "path_domain": [lo, hi],
            "dimension": hi - lo + 1, "observable": values}


def candidate(spin: int, cutoff: int):
    C = spin * (spin + 1)
    domain = list(range(-cutoff, cutoff + 1))
    nodes = core.walk_nodes(cutoff + 1)
    # Symmetric lower-band storage: diagonal, first lower band and second
    # lower band of C H2,infinity + D + H2,infinity^2.
    bands = np.zeros((3, len(domain)), dtype=float)
    states = [nodes[n] for n in domain]
    mask = checked_vacancy_mask(domain, states)
    residues = np.asarray([n % 15 for n in domain], dtype=int)
    for i, n in enumerate(domain):
        k, row = residue_row(D_TABLE, n)
        v = polynomial(row["diag"]["quadratic_k2_k_const"], k)
        bands[0, i] = -2 * C + float(v) + 6
        if i + 1 < len(domain):
            d = polynomial(row["right"]["quadratic_k2_k_const"], k)
            bands[1, i] = -C + float(d) + 4
        if i + 2 < len(domain):
            bands[2, i] = 1.0
    eigenvalues, eigenvectors = eig_banded(bands, lower=True, eigvals_only=False,
                                           check_finite=True)
    values = sample_eigensystem(eigenvalues, eigenvectors, cutoff, mask,
                                 residues, TIMES, lambda x: x)
    return {"S": spin, "C": C, "path_cutoff": cutoff,
            "dimension": len(domain), "observable": values}


def main(spins):
    results = []
    for spin in spins:
        exact = exact_spin(spin)
        candidates = [candidate(spin, ratio * spin) for ratio in (6, 12)]
        spread = []
        for j in range(len(TIMES)):
            vals = [c["observable"][j]["vacancy_B3"] for c in candidates]
            spread.append(max(vals) - min(vals))
        results.append({"exact": exact, "candidate_cutoffs": candidates,
                        "candidate_cutoff_spread_by_time": spread})
        print(json.dumps({"S": spin, "exact": exact["observable"],
                          "candidate_cutoff_spread": spread,
                          "candidate_large_cutoff": candidates[-1]["observable"]},
                         separators=(",", ":")), flush=True)
    out = {
        "status": "uncertified double-precision spectral diagnostic; no asymptotic claim",
        "source_revision": "b6eb31bedb3134dfacd8f4ab83cb7d96fc6dc953",
        "dependency_pr": 8831,
        "observable": "bounded projector onto vacancy at B site 3",
        "times": list(TIMES),
        "residue_diagnostic": "probability on n mod 15 classes, aggregated to the exact B3 vacancy class n mod 3 = 0; the indicator also has an exact two-mode Fourier identity",
        "exact_generator": "G_S=M_S^2-C M_S, diagonalized through symmetric M_S",
        "candidate_generator": "C H2,infinity + D + H2,infinity^2, principal pentadiagonal compression",
        "candidate_cutoff_multipliers": [6, 12],
        "results": results,
        "limits": "No interval arithmetic, error enclosure, uniform tail estimate, or fixed-time limit theorem. Spectral diagonalization changes the numerical algorithm, not the scientific status.",
    }
    payload = json.dumps(out, indent=2) + "\n"
    (HERE / "SPECTRAL_FIXED_TIME_HIGH_SPIN.json").write_text(payload)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--spins", nargs="+", type=int, default=list(DEFAULT_SPINS))
    args = parser.parse_args()
    main(tuple(args.spins))
