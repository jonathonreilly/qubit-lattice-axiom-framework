"""Independent bounded controls for number-offset record and energy identities.

Part 1 reconstructs the full physical P space of a three-vertex A--(B,B)
tree from charges and integer Gauss fields. Part 2 is an explicitly abstract
three-sector finite-dimensional model of the parent algebra; it is not a
cube truncation or an extra physical preparation. No author code is imported.
"""
from pathlib import Path
import hashlib
import json
import platform
import time
from itertools import product

import numpy as np
from numpy.polynomial.legendre import leggauss
from scipy.linalg import expm
import scipy

HERE = Path(__file__).resolve().parent
START = time.perf_counter()


def norm(a):
    return float(np.linalg.norm(a))


def real(a):
    z = complex(a)
    assert abs(z.imag) < 1e-11, z
    return float(z.real)


def tr(a, rho):
    return real(np.trace(a @ rho))


def generator(h, jumps):
    d = len(h)
    eye = np.eye(d)
    out = -1j * (np.kron(eye, h) - np.kron(h.T, eye))
    for jump in jumps:
        loss = jump.conj().T @ jump
        out += np.kron(jump.conj(), jump)
        out -= (np.kron(eye, loss) + np.kron(loss.T, eye)) / 2
    return out


def evolve(gen, rho, duration):
    return (expm(duration * gen) @ rho.reshape(-1, order="F")).reshape(rho.shape, order="F")


def pinching(a, numbers):
    return a * (numbers[:, None] == numbers[None, :])


def effect(jump):
    return jump.conj().T @ jump


def energy_power(h, jump):
    loss = effect(jump)
    return jump.conj().T @ h @ jump - (loss @ h + h @ loss) / 2


def path_operator(h, jumps, times, labels, horizon):
    loss = sum((effect(j) for j in jumps), np.zeros_like(h))
    g = -1j * h - loss / 2
    result = np.eye(len(h), dtype=complex)
    last = 0.0
    for t, label in zip(times, labels):
        result = jumps[label] @ expm((t - last) * g) @ result
        last = t
    return expm((horizon - last) * g) @ result


def star_control():
    # A is always occupied. On this oriented tree, E_(A,B_i)=-q_(B_i).
    # The remaining A Gauss equation is q_A+q_B0+q_B1=1.
    charges = [q for q in product((1, -1), (0, 1, -1), (0, 1, -1)) if sum(q) == 1]
    words = [(q, (-q[1], -q[2])) for q in charges]
    position = {word: i for i, word in enumerate(words)}
    n = np.array([sum(x != 0 for x in q) for q, e in words])
    d = len(words)
    h = np.zeros((d, d), complex)
    assert d == 4 and list(n).count(1) == 1 and list(n).count(3) == 3
    electric_values = []
    for q, e in words:
        assert sum(e) == q[0] - 1
        assert all(-e[i] == q[i + 1] for i in range(2))
        electric_values.append(sum(e[i] * (e[i] - q[0]) for i in range(2) if q[i + 1] == 0))
    assert electric_values == [0] * d
    # One A means there are no distinct-A magnetic pairs.
    jumps = []
    primitive_rows = []
    kappa = 0.7
    for edge in range(2):
        for sign in (1, -1):
            j = np.zeros_like(h)
            for source, (q, electric) in enumerate(words):
                # F_A must vacate A by hopping its old charge to the other B.
                destination = 1 - edge
                if q[edge + 1] or q[destination + 1]:
                    continue
                newq = list(q)
                newe = list(electric)
                old = q[0]
                newq[0] = 0
                newq[destination + 1] = old
                newe[destination] -= old
                # The original resolved creation j_(edge,sign).
                newq[0] = sign
                newq[edge + 1] = -sign
                newe[edge] += sign
                target = position[(tuple(newq), tuple(newe))]
                j[target, source] += np.sqrt(kappa)
                primitive_rows.append({"edge": edge, "sign": sign, "input": source,
                                       "output": target, "number_change": int(n[target] - n[source])})
            jumps.append(j)
    vacuum = int(np.flatnonzero(n == 1)[0])
    v = np.zeros(d, complex)
    v[vacuum] = 1
    rho_vacuum = np.outer(v, v.conj())
    dark = next(i for i in range(d) if n[i] == 3)
    v[dark] = 1j
    v /= np.linalg.norm(v)
    rho = np.outer(v, v.conj())
    f = np.diag(np.where(n == 1, -0.35, 1.2)).astype(complex)
    duration = 0.6
    cases = []
    for label, instrument in (("resolved", jumps), ("coherent_unscaled_sign_sum", [jumps[0] + jumps[1], jumps[2] + jumps[3]])):
        g0, gf = generator(h, instrument), generator(h + f, instrument)
        r0, rf = evolve(g0, rho, duration), evolve(gf, rho, duration)
        rv0, rvf = evolve(g0, rho_vacuum, duration), evolve(gf, rho_vacuum, duration)
        survival = real(rv0[vacuum, vacuum])
        p_error = abs(survival - np.exp(-4 * kappa * duration))
        powers = [tr(energy_power(h + f, j), rho_vacuum) for j in instrument]
        rates = [tr(effect(j), rho_vacuum) for j in instrument]
        assert max(abs(p - 1.55 * r) for p, r in zip(powers, rates)) < 1e-12
        assert norm(pinching(rf - r0, n)) < 1e-12
        assert norm(rvf - rv0) < 1e-12 and p_error < 1e-12
        assert norm(rf - r0) > 0.1
        cases.append({"instrument": label, "vacuum_survival": survival,
                      "exact_survival_error": p_error, "state_difference_coherent_initial": norm(rf - r0),
                      "number_diagonal_difference": norm(pinching(rf - r0, n)),
                      "state_difference_number_definite_initial": norm(rvf - rv0),
                      "selected_rates": rates, "selected_offset_powers": powers})
    coherent_output = (jumps[0] + jumps[1]) @ rho_vacuum @ (jumps[0] + jumps[1]).conj().T
    unresolved_output = jumps[0] @ rho_vacuum @ jumps[0].conj().T + jumps[1] @ rho_vacuum @ jumps[1].conj().T
    coherence_discriminator = norm(coherent_output - unresolved_output)
    assert coherence_discriminator > 0.5
    return {"physical_scope": "Complete Gauss-legal rotor P space on the three-site tree; all energy-diagonal values zero and no magnetic pair.",
            "kappa": kappa, "duration": duration,
            "words": [{"charges": q, "fields_A_to_B": e, "N": int(n[i])} for i, (q, e) in enumerate(words)],
            "primitive_birth_rows": primitive_rows, "electric_diagonal": electric_values,
            "cases": cases, "coherent_vs_unresolved_density_difference": coherence_discriminator}


def abstract_control():
    numbers = np.array([0, 0, 2, 2, 4, 4])
    number = np.diag(numbers).astype(complex)
    h = np.zeros((6, 6), complex)
    blocks = [np.array([[0.3, 0.22 + 0.11j], [0.22 - 0.11j, -0.4]]),
              np.array([[1.1, -0.13j], [0.13j, 0.2]]),
              np.array([[-0.1, 0.32], [0.32, 0.8]])]
    for i, block in enumerate(blocks):
        h[2 * i:2 * i + 2, 2 * i:2 * i + 2] = block
    jp, jm = np.zeros_like(h), np.zeros_like(h)
    jp[2:4, 0:2] = [[0.7, 0.1j], [0.2, 0.4]]
    jp[4:6, 2:4] = [[0.3, 0.5], [-0.2j, 0.6]]
    jm[2:4, 0:2] = [[0.2, 0.4j], [-0.3, 0.5]]
    jm[4:6, 2:4] = [[0.4, -0.1j], [0.2, 0.15]]
    vector = np.array([1, 1j, -0.6, 0.8 + 0.3j, -0.2j, 0.5])
    rho = 0.83 * np.outer(vector, vector.conj()) / np.vdot(vector, vector).real + 0.17 * np.eye(6) / 6
    horizon = 0.73
    paths = [([], []), ([0.18], [0]), ([0.18, 0.49], [0, 1])]
    rows = []
    max_error = 0.0
    discriminators = []
    for ilabel, jumps in (("resolved", [jp, jm]), ("coherent_single_mark", [jp + jm])):
        assert norm(number @ h - h @ number) == 0
        for j in jumps:
            assert norm(number @ j - j @ number - 2 * j) < 1e-14
        g0 = generator(h, jumps)
        r0 = evolve(g0, rho, horizon)
        rd0 = evolve(g0, pinching(rho, numbers), horizon)
        for flabel, vals in (("scalar", {0: 0.47, 2: 0.47, 4: 0.47}),
                             ("affine", {0: -0.4, 2: 0.2, 4: 0.8}),
                             ("nonlinear", {0: -0.7, 2: 0.9, 4: -0.2})):
            fdiag = np.array([vals[int(n)] for n in numbers])
            f = np.diag(fdiag)
            shifted_f = np.diag([vals.get(int(n) + 2, 0.0) for n in numbers])
            delta_f = shifted_f - f
            gf = generator(h + f, jumps)
            rf = evolve(gf, rho, horizon)
            rdf = evolve(gf, pinching(rho, numbers), horizon)
            errors = {"unconditional_number_blocks": norm(pinching(rf - r0, numbers)),
                      "number_diagonal_input_full_state": norm(rdf - rd0),
                      "mean_offset": abs(tr(h + f, rf) - tr(h, r0) - tr(f, r0))}
            base_mean, offset_mean = tr(h, r0), tr(f, r0)
            expected_var = tr(h @ h, r0) - base_mean ** 2
            expected_var += tr(f @ f, r0) - offset_mean ** 2
            expected_var += 2 * (tr(h @ f, r0) - base_mean * offset_mean)
            errors["variance_shift"] = abs(tr((h + f) @ (h + f), rf) - tr(h + f, rf) ** 2 - expected_var)
            energy_rows = []
            for j in jumps:
                loss = effect(j)
                operator_diff = energy_power(h + f, j) - energy_power(h, j)
                errors["power_operator"] = max(errors.get("power_operator", 0), norm(operator_diff - loss @ delta_f))
                rate = tr(loss, r0)
                power_difference = tr(energy_power(h + f, j), rf) - tr(energy_power(h, j), r0)
                expected_power_difference = tr(loss @ delta_f, r0)
                output_difference = tr(j.conj().T @ (h + f) @ j, rf) - tr(j.conj().T @ h @ j, r0)
                centered_difference = output_difference - rate * tr(f, r0)
                errors["power_expectation"] = max(errors.get("power_expectation", 0), abs(power_difference - expected_power_difference))
                errors["raw_output_energy"] = max(errors.get("raw_output_energy", 0), abs(output_difference - tr(loss @ shifted_f, r0)))
                energy_rows.append({"rate": rate, "power_difference": power_difference,
                                    "raw_output_energy_difference": output_difference,
                                    "centered_jump_energy_rate_difference": centered_difference})
            path_rows = []
            for times, labels0 in paths:
                labels = [i % len(jumps) for i in labels0]
                k0 = path_operator(h, jumps, times, labels, horizon)
                kf = path_operator(h + f, jumps, times, labels, horizon)
                boundaries = [0, *times, horizon]
                phases = []
                for n in numbers:
                    # Unreachable starting sectors have zero path columns; extend f by zero.
                    phi = sum(vals.get(int(n) + 2 * i, 0.0) * (boundaries[i + 1] - boundaries[i]) for i in range(len(boundaries) - 1))
                    phases.append(np.exp(-1j * phi))
                phase_error = norm(kf - k0 @ np.diag(phases))
                effect_error = norm(kf.conj().T @ kf - k0.conj().T @ k0)
                s0, sf = k0 @ rho @ k0.conj().T, kf @ rho @ kf.conj().T
                probability = real(np.trace(s0))
                block_error = norm(pinching(sf - s0, numbers))
                assert probability > 0
                path_rows.append({"times": times, "labels": labels, "record_density": probability,
                                  "phase_formula_error": phase_error, "effect_error": effect_error,
                                  "conditional_number_block_error": block_error / probability,
                                  "conditional_full_state_difference": norm(sf - s0) / probability})
                max_error = max(max_error, phase_error, effect_error, block_error / probability)
            nodes, weights = leggauss(24)
            loss = sum((effect(j) for j in jumps), np.zeros_like(h))
            integrated = sum(w * tr(loss @ delta_f, evolve(g0, rho, (x + 1) * horizon / 2)) * horizon / 2 for x, w in zip(nodes, weights))
            errors["integrated_offset_balance"] = abs(tr(f, r0) - tr(f, rho) - integrated)
            u = expm(-1j * horizon * f)
            global_rotation_difference = norm(rf - u @ r0 @ u.conj().T)
            if flabel in ("scalar", "affine"):
                errors["global_rotation_special_case"] = global_rotation_difference
            else:
                assert global_rotation_difference > 0.005
            if flabel == "scalar":
                errors["scalar_full_state"] = norm(rf - r0)
            else:
                assert norm(rf - r0) > 0.02
            if flabel == "nonlinear":
                distinction = max(abs(r["power_difference"] - r["centered_jump_energy_rate_difference"]) for r in energy_rows)
                assert distinction > 0.02
                discriminators.append({"instrument": ilabel,
                                       "incorrect_global_rotation_residual": global_rotation_difference,
                                       "incorrect_full_state_invariance_residual": norm(rf - r0),
                                       "centered_rate_vs_GKLS_power_difference": distinction,
                                       "Hamiltonian_loss_noncommutation": norm(h @ loss - loss @ h)})
            assert max(errors.values()) < 2e-11, errors
            max_error = max(max_error, *errors.values())
            rows.append({"instrument": ilabel, "offset": flabel, "offset_by_N": vals,
                         "errors": errors, "full_state_difference": norm(rf - r0),
                         "global_rotation_residual": global_rotation_difference,
                         "energy_rows": energy_rows, "path_rows": path_rows})
    return {"scope": "Abstract bounded number-graded parent class; six states, three number sectors, no Gauss or rotor assertion.",
            "horizon": horizon, "initial_density_eigenvalues": np.linalg.eigvalsh(rho).tolist(),
            "max_comparison_error": max_error, "rows": rows, "wrong_claim_discriminators": discriminators}


if __name__ == "__main__":
    result = {"star": star_control(), "abstract": abstract_control()}
    result["execution"] = {"python": platform.python_version(), "numpy": np.__version__,
                           "scipy": scipy.__version__, "elapsed_seconds": time.perf_counter() - START,
                           "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                           "author_programs_run_or_imported": []}
    print(json.dumps(result, indent=2, allow_nan=False))
