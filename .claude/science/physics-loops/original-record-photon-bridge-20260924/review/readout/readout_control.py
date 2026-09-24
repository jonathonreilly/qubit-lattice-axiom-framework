#!/usr/bin/env python3
"""Own bounded PRE controls; no author imports and no microscopic simulation.

Exact unit-coefficient qutrit/rotor paths on the requested side-six torus;
independent finite Fourier/Gauss-Hermite readout checks; finite-band phase check.
The analytic PRE, not these finite checks, carries all general quantifiers.
"""
from __future__ import annotations

from collections import Counter, defaultdict
from dataclasses import dataclass
from itertools import product
import json
import math
from pathlib import Path
import sys

import numpy as np

HERE = Path(__file__).resolve().parent
CHECKS: list[dict] = []


def check(name: str, condition: bool, **evidence) -> None:
    entry = {"name": name, "satisfied": bool(condition), **evidence}
    CHECKS.append(entry)
    print(json.dumps(entry, sort_keys=True), flush=True)
    if not condition:
        raise AssertionError(name)


L = 6
VERTICES = tuple(product(range(L), repeat=3))
INDEX = {v: i for i, v in enumerate(VERTICES)}
NVERT = len(VERTICES)
NLINK = 3 * NVERT
Q0 = tuple(1 if sum(v) % 2 == 0 else 0 for v in VERTICES)
A, B, D, F = (0, 0, 0), (5, 0, 0), (1, 1, 0), (2, 1, 0)


def neighbor(v, axis, sign):
    w = list(v)
    w[axis] = (w[axis] + sign) % L
    return tuple(w)


def neighbors(v):
    return tuple(neighbor(v, axis, sign) for axis in range(3) for sign in (-1, 1))


def link(v, w):
    """Index and sign for the unit oriented edge v -> w, stored positively."""
    matches = []
    for axis in range(3):
        if w == neighbor(v, axis, 1):
            matches.append((3 * INDEX[v] + axis, 1))
        if w == neighbor(v, axis, -1):
            matches.append((3 * INDEX[w] + axis, -1))
    if len(matches) != 1:
        raise ValueError((v, w, matches))
    return matches[0]


def shift_add(field, edge, coefficient):
    values = dict(field)
    values[edge] = values.get(edge, 0) + coefficient
    return tuple(sorted((k, v) for k, v in values.items() if v))


def field_difference(right, left):
    ans = right
    for edge, value in left:
        ans = shift_add(ans, edge, -value)
    return ans


def divergence(field):
    div = [0] * NVERT
    for edge, value in field:
        start = VERTICES[edge // 3]
        end = neighbor(start, edge % 3, 1)
        div[INDEX[start]] += value
        div[INDEX[end]] -= value
    return tuple(div)


def field_description(field):
    return [{"start": list(VERTICES[e // 3]), "axis": e % 3, "value": n}
            for e, n in field]


def q_description(q):
    return [{"vertex": list(v), "initial": Q0[i], "final": q[i]}
            for i, v in enumerate(VERTICES) if Q0[i] != q[i]]


@dataclass(frozen=True)
class PathWord:
    q: tuple
    field: tuple
    hops: tuple
    birth_signs: tuple
    intermediate: tuple | None = None


def mark(path, a, b, signs):
    """Apply F_a followed by legal j_(a,b,sigma), without collapsing paths."""
    out = []
    ia, ib = INDEX[a], INDEX[b]
    old_charge = path.q[ia]
    if old_charge == 0:
        return out
    for destination in neighbors(a):
        iu = INDEX[destination]
        if path.q[iu] != 0:
            continue
        qhop = list(path.q)
        qhop[ia] = 0
        qhop[iu] = old_charge
        edge, orientation = link(a, destination)
        fhop = shift_add(path.field, edge, -old_charge * orientation)
        # This legality check, not an imposed list of five destinations,
        # excludes an old hop into the edge on which the pair must form.
        if qhop[ia] != 0 or qhop[ib] != 0:
            continue
        for sign in signs:
            qbirth = qhop.copy()
            qbirth[ia], qbirth[ib] = sign, -sign
            edge, orientation = link(a, b)
            fbirth = shift_add(fhop, edge, sign * orientation)
            qfinal = tuple(qbirth)
            out.append(PathWord(qfinal, fbirth,
                                path.hops + (destination,),
                                path.birth_signs + (sign,),
                                qfinal if path.intermediate is None else path.intermediate))
    return out


def effect(paths, dephase_intermediate=False):
    groups = defaultdict(list)
    for path in paths:
        key = (path.q, path.intermediate) if dephase_intermediate else path.q
        groups[key].append(path)
    result = Counter()
    for members in groups.values():
        for bra in members:
            for ket in members:
                result[field_difference(ket.field, bra.field)] += 1
    return result


def polynomial_json(poly):
    return [{"translation": field_description(k), "coefficient": v}
            for k, v in sorted(poly.items())]


def exact_paths():
    initial = PathWord(Q0, (), (), ())
    circle = (A, (1, 0, 0), D, (0, 1, 0), A)
    loop = ()
    for v, w in zip(circle, circle[1:]):
        edge, orientation = link(v, w)
        loop = shift_add(loop, edge, orientation)
    reverse_loop = tuple((e, -n) for e, n in loop)
    shared = set(neighbors(A)).intersection(neighbors(D))
    check("geometry", len(VERTICES) == 216 and len(shared) == 2
          and B not in neighbors(D) and F not in neighbors(A),
          volume=NVERT, links=NLINK, common_neighbors=sorted(shared))
    check("primitive_loop_gauss_and_winding", not any(divergence(loop))
          and all(sum(n for e, n in loop if e % 3 == axis) == 0 for axis in range(3)),
          loop=field_description(loop))
    choices = {"plus": (1,), "minus": (-1,), "coherent": (1, -1)}
    certificates = []
    summaries = []
    total_paths = 0
    all_gauss = True
    all_counts = True
    for name_i, signs_i in choices.items():
        first = mark(initial, A, B, signs_i)
        expected_first = Counter({(): 5 * len(signs_i)})
        check(f"first_effect_{name_i}", effect(first) == expected_first,
              paths=len(first), effect=polynomial_json(effect(first)))
        for name_j, signs_j in choices.items():
            pair = [out for one in first for out in mark(one, D, F, signs_j)]
            mult = len(signs_i) * len(signs_j)
            expected = Counter({(): 23 * mult, loop: mult, reverse_loop: mult})
            actual = effect(pair)
            dephased = effect(pair, dephase_intermediate=True)
            final_multiplicities = sorted(Counter(p.q for p in pair).values())
            check(f"ordered_effect_{name_i}_{name_j}", actual == expected,
                  paths=len(pair), final_matter_words=len(final_multiplicities),
                  singleton_outputs=final_multiplicities.count(1),
                  double_outputs=final_multiplicities.count(2),
                  effect=polynomial_json(actual))
            check(f"dephased_effect_{name_i}_{name_j}",
                  dephased == Counter({(): 23 * mult}),
                  effect=polynomial_json(dephased))
            for p in first + pair:
                all_gauss &= divergence(p.field) == tuple(q - q0 for q, q0 in zip(p.q, Q0))
                all_counts &= (sum(q != 0 for q in p.q)
                               == sum(q != 0 for q in Q0) + 2 * len(p.hops))
                all_counts &= sum(p.q) == sum(Q0)
            total_paths += len(pair)
            summaries.append({"first": name_i, "second": name_j,
                              "path_count": len(pair), "multiplicity": mult,
                              "effect": polynomial_json(actual),
                              "dephased_effect": polynomial_json(dephased)})
            certificates.append({
                "first": name_i, "second": name_j,
                "paths": [{"hops": [list(x) for x in p.hops],
                           "birth_signs": list(p.birth_signs),
                           "intermediate_matter_changes": q_description(p.intermediate),
                           "final_matter_changes": q_description(p.q),
                           "electric_translation": field_description(p.field)} for p in pair]
            })
    check("all_enumerated_paths_gauss", all_gauss, total_two_mark_paths=total_paths)
    check("all_enumerated_paths_record_count_and_charge", all_counts)
    check("first_total_rate_count", 3 * NVERT * 2 * 5 == 30 * NVERT,
          resolved_channels=6 * NVERT, coherent_channels=3 * NVERT,
          total_loss_coefficient=30 * NVERT)
    (HERE / "PATH_CERTIFICATES.json").write_text(json.dumps(certificates, indent=2) + "\n")
    return summaries


def harmonic_readout():
    momenta = 2 * np.pi * np.array(list(product(range(L), repeat=3))) / L
    q = np.exp(1j * momenta) - 1
    lam = np.sum(np.abs(q) ** 2, axis=1)
    mask = lam > 1e-20
    vp = float(np.sum((np.abs(q[mask, 0]) ** 2 + np.abs(q[mask, 1]) ** 2)
                      / np.sqrt(lam[mask])) / (2 * NVERT))
    ks = np.array([[2 * np.pi / L, 0, 0], [2 * np.pi / L, 2 * np.pi / L, 0]])
    eps = np.array([[0, 1, 0], [1 / math.sqrt(2), -1 / math.sqrt(2), 0]], complex)
    qs = np.exp(1j * ks) - 1
    lambdas = np.sum(np.abs(qs) ** 2, axis=1)
    transverse = np.sum(np.conj(qs) * eps, axis=1)
    cs = np.array([1, np.exp(0.37j)]) / math.sqrt(2)
    local_modes = (lambdas ** (-0.25)
                   * (-qs[:, 1] * eps[:, 0] + qs[:, 0] * eps[:, 1])
                   / math.sqrt(2 * NVERT))
    t = 0.2
    frequency = np.sqrt(lambdas)
    amplitude = complex(np.dot(local_modes, cs * np.exp(-1j * frequency * t)))
    f2 = abs(amplitude) ** 2
    check("two_mode_transverse_normalization", np.max(np.abs(transverse)) < 1e-14
          and abs(np.vdot(cs, cs) - 1) < 1e-14,
          transverse_residual=float(np.max(np.abs(transverse))),
          one_particle_norm=float(np.vdot(cs, cs).real))
    check("local_response_cauchy_schwarz", 0 < f2 <= vp,
          vacuum_local_variance=vp, one_particle_local_excess=2 * f2,
          local_amplitude_re_im=[amplitude.real, amplitude.imag])
    nodes, weights = np.polynomial.hermite.hermgauss(128)
    z = math.sqrt(2) * nodes
    w = weights / math.sqrt(math.pi)
    x = math.sqrt(vp) * z
    alpha = f2 / vp
    density = 1 - alpha + alpha * z * z
    check("one_particle_reduced_quadrature_density", np.min(density) >= 0
          and abs(np.dot(w, density) - 1) < 2e-14,
          alpha=alpha, normalization=float(np.dot(w, density)))
    rows = []
    sensitivity = []
    for g in (0.4, 0.2, 0.1, 0.05):
        phase = np.cos(g * x)
        # Difference is integrated directly with its constant part removed.
        quad_difference = float(np.dot(w, alpha * (z * z - 1) * 2 * (phase - 1)))
        formula = -2 * g * g * f2 * math.exp(-g * g * vp / 2)
        q0 = float(np.dot(w, 23 + 2 * phase))
        q1 = float(np.dot(w, density * (23 + 2 * phase)))
        check(f"harmonic_characteristic_g_{g}", abs(quad_difference - formula) < 2e-14
              and abs((q1 - q0) - formula) < 2e-13,
              direct_quadrature_difference=quad_difference,
              formula_difference=formula,
              effect_vacuum=q0, effect_one_particle=q1,
              divided_by_g2=quad_difference / (g * g))
        rows.append({"g": g, "effect_vacuum": q0, "effect_one_particle": q1,
                     "contrast": quad_difference, "formula": formula,
                     "contrast_over_g2": quad_difference / (g * g),
                     "dephased_contrast": 0.0})
        # Algebraic state-error diagnostic: not an evolved compact-rotor state.
        psi2_over_psi0 = (z * z - 1) / math.sqrt(2)
        pert_over_psi0 = (1 + g * g * psi2_over_psi0) / math.sqrt(1 + g ** 4)
        observable = 2 * (1 - phase)
        norm_error = math.sqrt(float(np.dot(w, (pert_over_psi0 - 1) ** 2)))
        obs_on_vac = math.sqrt(float(np.dot(w, observable ** 2)))
        expectation_difference = float(np.dot(w, (pert_over_psi0 ** 2 - 1) * observable))
        rigorous_algebraic_bound = 2 * norm_error * obs_on_vac + 4 * norm_error ** 2
        check(f"observable_specific_error_bound_g_{g}",
              abs(expectation_difference) <= rigorous_algebraic_bound * (1 + 1e-12)
              and obs_on_vac <= g * g * math.sqrt(3) * vp * (1 + 1e-12),
              state_norm_error=norm_error, observable_on_vac_norm=obs_on_vac,
              expectation_difference=expectation_difference,
              difference_over_g4=expectation_difference / g ** 4,
              bound=rigorous_algebraic_bound)
        sensitivity.append({"g": g, "norm_error": norm_error,
                            "observable_on_vac_norm": obs_on_vac,
                            "expectation_difference": expectation_difference,
                            "difference_over_g4": expectation_difference / g ** 4,
                            "bound": rigorous_algebraic_bound})
    # For all translated xy plaquettes, sum of the local excess is the xy
    # part of the general Gram identity; the chosen modes have no z component.
    amplitudes = []
    for v in VERTICES:
        phase = np.exp(1j * (ks @ np.array(v)))
        amplitudes.append(np.dot(local_modes, phase * cs * np.exp(-1j * frequency * t)))
    gram = float(sum(abs(f) ** 2 for f in amplitudes))
    gram_expected = float(np.dot(np.abs(cs) ** 2, frequency) / 2)
    check("all_plaquette_response_gram_identity_for_xy_modes",
          abs(gram - gram_expected) < 2e-13,
          translated_xy_sum=gram, half_one_particle_frequency=gram_expected)
    return {"box_side": L, "c_over_a": 1, "time": t,
            "vacuum_variance": vp, "local_amplitude_squared": f2,
            "frequencies": frequency.tolist(), "rows": rows,
            "algebraic_state_error_diagnostic": sensitivity,
            "scope": "Harmonic finite-mode/quadrature check only; no compact rotor evolution or parent control executed."}


def band_translation():
    side = 48
    spacing = 2 * math.pi / side
    carrier = spacing * np.array([8, 4, 0.0])
    offsets = spacing * np.array([[0, 0, 0], [1, 0, 0], [-1, 0, 0],
                                 [0, 1, 0], [0, -1, 0]], float)
    ks = carrier + offsets
    lam = lambda k: 4 * np.sum(np.sin(np.asarray(k) / 2) ** 2, axis=-1)
    omega0 = math.sqrt(float(lam(carrier)))
    omegas = np.sqrt(lam(ks))
    velocity = np.sin(carrier) / omega0
    affine = omega0 + offsets @ velocity
    delta = float(np.max(np.linalg.norm(offsets, axis=1)))
    safe_min = omega0 - delta  # sqrt(lambda) is 1-Lipschitz.
    M = 2 / safe_min
    coefficients = np.array([1, 0.8j, -0.3, 0.5 + 0.2j, -0.1j], complex)
    coefficients /= np.linalg.norm(coefficients)
    t = 2.0
    exact = coefficients * np.exp(-1j * t * omegas)
    linear = coefficients * np.exp(-1j * t * affine)
    error = float(np.linalg.norm(exact - linear))
    rms_fourth = math.sqrt(float(np.dot(np.abs(coefficients) ** 2,
                                        np.sum(offsets ** 2, axis=1) ** 2)))
    bound = abs(t) * M * rms_fourth / 2
    coarser = abs(t) * M * delta * delta / 2
    check("finite_band_phase_translation_bound", safe_min > 0 and error <= bound
          and bound <= coarser * (1 + 1e-14),
          side=side, time=t, band_radius=delta, sqrt_lambda_lower_bound=safe_min,
          Hessian_norm_upper_bound=M, vector_error=error,
          weighted_remainder_bound=bound, maximum_radius_bound=coarser)
    interpolation_errors = []
    carrier_phase = np.exp(-1j * t * (omega0 - np.dot(velocity, carrier)))
    for position in (np.array([0, 0, 0]), np.array([1, 2, 0]), np.array([7, -3, 5])):
        lhs = np.dot(linear, np.exp(1j * (ks @ position)))
        rhs = carrier_phase * np.dot(coefficients, np.exp(1j * (ks @ (position - velocity * t))))
        interpolation_errors.append(float(abs(lhs - rhs)))
    check("affine_phase_is_trigonometric_interpolation_translation",
          max(interpolation_errors) < 2e-14,
          interpolation_errors=interpolation_errors, lattice_velocity=velocity.tolist())
    return {"side": side, "carrier": carrier.tolist(), "time": t,
            "band_radius": delta, "lattice_velocity": velocity.tolist(),
            "error": error, "bound": bound, "coarser_bound": coarser,
            "scope": "Five finite allowed modes; fixed time; no large-volume or growing-time theorem inferred."}


def main():
    result = {"description": __doc__, "paths": exact_paths(),
              "harmonic": harmonic_readout(), "band": band_translation()}
    result["checks"] = CHECKS
    result["all_checks_satisfied"] = all(c["satisfied"] for c in CHECKS)
    result["check_count"] = len(CHECKS)
    result["runtime_versions"] = {"python": sys.version, "numpy": np.__version__}
    (HERE / "CONTROL_RESULTS.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({"completed": True, "check_count": len(CHECKS)}, sort_keys=True))


if __name__ == "__main__":
    main()
