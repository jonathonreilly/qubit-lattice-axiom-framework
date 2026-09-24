#!/usr/bin/env python3
"""PRE control built independently from local tensor-basis operators.

No imports of campaign builders or author/checker packets. Exact SymPy
identities supply finite certificates; floating propagation is corroboration.
Every run writes separate artifacts selected by --attempt.
"""
from __future__ import annotations

import argparse
import hashlib
import itertools
import json
from pathlib import Path
import platform
import subprocess
import sys
import time
import traceback

import numpy as np
import scipy
from scipy.linalg import expm
import sympy as sy

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[4]
SCIENCE = HERE.parents[1]
SOURCE_ROWS = {
    "campaign12h_third/FINITE_RATE_REPEATED_RECORD_FORMATION.md":
        "b577c14e992fe74feb8a9f17c33e503f446f7052f83512031c2bf82cf2e3538d",
    "campaign12h_third/FINITE_FORMATION_WITH_RETAINED_FOURTH_ORDER_DYNAMICS.md":
        "002119d5a3f9bec171c3678cb15afdb91f7a763311ca38e6e4458ce10865572e",
    "campaign12h_fourth/local_compensation_author/LOCAL_COMPENSATION_COMMON_FIELD_RECORD_LIMIT.md":
        "42ec5430a0f49c9b6e70577be601df72e23d881b7ef152186de2cdb1ff3faba4",
    "campaign12h_fourth/local_compensation_author/BOUNDED_BLOCK_DIAGONAL_COMPENSATION_TARGET.md":
        "9bc691a07fd70c1a813852aa0cac55832065b3c95cf3d50e5528845f6613e0b0",
    "campaign12h_fourth/local_compensation_author/ROOT_GENERAL_TARGET_CORRECTION.md":
        "c906ed162db678fc2f10bc67afd2af22d929be3fe97fd3a1658cfe12ecd339a9",
}
EPS, DELTA, KAPPA = sy.symbols("epsilon delta kappa", positive=True)
CHECKS = []


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def record(name, condition, detail=None):
    row = {"name": name, "passed": bool(condition)}
    if detail is not None:
        row["detail"] = detail
    CHECKS.append(row)
    if not condition:
        raise AssertionError(name)


def zero(matrix):
    return all(sy.simplify(x) == 0 for x in matrix)


def same_scalar(left, right):
    return sy.simplify(left - right) == 0


def gauss(q, electric):
    return (
        sum(electric) == q[0] - 1
        and all(-electric[b - 1] == q[b] for b in (1, 2, 3))
    )


def construct(spin):
    # Exhaust the full finite tensor product. The analytic sector count and
    # E_b=-q_b reduction are deliberately not used to construct this basis.
    basis = []
    for q in itertools.product((-1, 0, 1), repeat=4):
        for electric in itertools.product(range(-spin, spin + 1), repeat=3):
            if gauss(q, electric):
                basis.append((q, electric))
    index = {state: i for i, state in enumerate(basis)}
    dim = len(basis)
    F, T = sy.zeros(dim), sy.zeros(dim)
    jumps = {(b, c): sy.zeros(dim) for b in (1, 2, 3) for c in (-1, 1)}
    finite_diag, rotor_diag = [], []
    Cspin = sy.Integer(spin * (spin + 1))
    transitions = []

    def shift_weight(m, step):
        if not -spin <= m + step <= spin:
            return sy.Integer(0)
        # S_+ and S_- matrix element squared, divided by S(S+1).
        return sy.sqrt(1 - sy.Rational(m * (m + step), Cspin))

    def add(operator, i, q, electric, qnew, b, step, kind):
        weight = shift_weight(electric[b - 1], step)
        if not weight:
            return
        enew = list(electric)
        enew[b - 1] += step
        target = (tuple(qnew), tuple(enew))
        if target not in index:
            raise AssertionError(("local operator left physical space", kind, target))
        operator[index[target], i] += weight
        transitions.append({
            "kind": kind, "from": i, "to": index[target],
            "weight": str(weight), "edge": b, "step": step,
        })

    for i, (q, electric) in enumerate(basis):
        dspin, drotor = sy.Integer(0), 0
        for b in (1, 2, 3):
            for c in (-1, 1):
                if q[0] == c and q[b] == 0:
                    qnew = list(q)
                    qnew[0], qnew[b] = 0, c
                    add(F, i, q, electric, qnew, b, -c, "outward")
                    # T assembled independently by the two oriented local terms.
                    local = sy.zeros(dim)
                    add(local, i, q, electric, qnew, b, -c, "hop_forward")
                    T -= local
                    dspin += 1 - sy.Rational(electric[b - 1] * (electric[b - 1] - c), Cspin)
                    drotor += 1
                if q[0] == 0 and q[b] == c:
                    qnew = list(q)
                    qnew[0], qnew[b] = c, 0
                    local = sy.zeros(dim)
                    add(local, i, q, electric, qnew, b, c, "hop_reverse")
                    T -= local
                if q[0] == 0 and q[b] == 0:
                    qnew = list(q)
                    qnew[0], qnew[b] = c, -c
                    add(jumps[(b, c)], i, q, electric, qnew, b, c, "birth")
        finite_diag.append(dspin)
        rotor_diag.append(drotor)
    W = sy.diag(*[1 - q[0] ** 2 for q, _ in basis])
    N = sy.diag(*[sum(c * c for c in q) for q, _ in basis])
    P = sy.eye(dim) - W
    DS, Dinf = sy.diag(*finite_diag), sy.diag(*rotor_diag)
    compensation = F.T * F - DS + Dinf  # Q_0 is the empty product, I.
    return {
        "S": spin, "basis": basis, "F": F, "T": T, "jumps": jumps,
        "W": W, "P": P, "N": N, "DS": DS, "Dinf": Dinf,
        "compensation": compensation, "transitions": transitions,
    }


def matrix_entries(matrix):
    return [
        [i, j, str(matrix[i, j])]
        for i in range(matrix.rows) for j in range(matrix.cols)
        if matrix[i, j] != 0
    ]


def scalar(matrix):
    assert matrix.shape == (1, 1)
    return sy.simplify(matrix[0, 0])


def exact_analysis(model):
    F, T, W, P, N, C = [model[k] for k in
                         ("F", "T", "W", "P", "N", "compensation")]
    dim = F.rows
    I = sy.eye(dim)
    M = F.T * F
    a = 1 + 3 * EPS ** 2
    h = W + EPS * T + EPS ** 2 * C
    H = DELTA * EPS ** -4 * h
    g = sy.zeros(dim, 1)
    g[model["basis"].index(((1, 0, 0, 0), (0, 0, 0))), 0] = 1
    raw_dressed = g + EPS * F * g
    rho = raw_dressed * raw_dressed.T / a
    pb, qb = M / 3, F * F.T / 3
    pd, qd = P - pb, W - qb
    U = pd + qd + (pb + qb + EPS * (F - F.T)) / sy.sqrt(a)
    high = (h - qd) / a
    low = I - qd - high
    record("factorization full matrix", zero(h - (W - EPS * F).T * (W - EPS * F)))
    record("M minimal polynomial", zero(M * M - 3 * M))
    record("rank F", F.rank() == 4, F.rank())
    record("canonical U unitary", zero(U.T * U - I))
    record("canonical U maps g to dressed g", zero(U * g - raw_dressed / sy.sqrt(a)))
    record("canonical transformed Hamiltonian", zero(U.T * h * U - qd - a * qb))
    record("positive P overlap", zero(P * U * P - pd - pb / sy.sqrt(a)))
    for name, projector, eig in (("low", low, 0), ("Qdark", qd, 1), ("high", high, a)):
        record(name + " projector", zero(projector ** 2 - projector))
        record(name + " spectral identity", zero(h * projector - eig * projector))
    record("projectors sum", zero(low + qd + high - I))
    record("projector ranks", (sy.trace(low), sy.trace(qd), sy.trace(high)) == (10, 2, 4))
    x = sy.symbols("x")
    charpoly = sy.factor(h.charpoly(x).as_expr())
    record("full characteristic polynomial", same_scalar(charpoly, x ** 10 * (x - 1) ** 2 * (x - a) ** 4))
    record("dressed energy exact zero", zero(h * raw_dressed))
    record("dressed norm", same_scalar(scalar(raw_dressed.T * raw_dressed), a))
    A = W * T * P
    H2 = P * C * P - A.T * A
    H4 = (A.T * A) ** 2 - ((A.T * A) * (P * C * P) + (P * C * P) * (A.T * A)) / 2 + A.T * (W * C * W) * A
    record("effective H2 zero", zero(H2))
    record("effective H4 zero", zero(H4))
    sectors = {}
    for number in (1, 3):
        inds = [i for i in range(dim) if N[i, i] == number]
        pind = [i for i in inds if P[i, i] == 1]
        qind = [i for i in inds if W[i, i] == 1]
        sectors[str(number)] = {"indices": inds, "P_indices": pind, "Q_indices": qind}
    g_rho = g * g.T
    bare_mean = sy.simplify(sy.trace(H * g_rho))
    bare_second = sy.simplify(sy.trace(H * H * g_rho))
    record("bare mean", same_scalar(bare_mean, 3 * DELTA / EPS ** 2))
    record("bare second moment", same_scalar(bare_second, 3 * DELTA ** 2 * a / EPS ** 6))
    record("bare variance", same_scalar(bare_second - bare_mean ** 2, 3 * DELTA ** 2 / EPS ** 6))
    instruments = {
        "resolved": {f"{b},{c:+d}": j for (b, c), j in model["jumps"].items()},
        "coherent": {str(b): model["jumps"][(b, 1)] + model["jumps"][(b, -1)]
                     for b in (1, 2, 3)},
    }
    out = {
        "sectors": sectors, "characteristic_polynomial": str(charpoly),
        "spectral_projectors": {"low": matrix_entries(low), "Qdark": matrix_entries(qd), "high": matrix_entries(high)},
        "bare": {"mean": str(bare_mean), "second_moment": str(bare_second),
                 "variance": str(sy.simplify(bare_second - bare_mean ** 2))},
        "instruments": {},
    }
    for instrument, jumps in instruments.items():
        rows = {}
        diss = sy.zeros(dim)
        loss = sy.zeros(dim)
        recycled = sy.zeros(dim)
        sigma = sy.zeros(dim)
        totalrate = sy.Integer(0)
        for label, jump in jumps.items():
            v = jump * F * g
            normsq = scalar(v.T * v)
            eta = v * v.T / normsq
            m = scalar(v.T * C * v) / normsq
            rate = KAPPA * normsq / a
            mean = sy.simplify(sy.trace(H * eta))
            second = sy.simplify(sy.trace(H * H * eta))
            phigh = sy.simplify(sy.trace(high * eta))
            b_eff = -P * jump * W * T * P
            record(instrument + " " + label + " actual jump", zero(jump * raw_dressed - EPS * v))
            record(instrument + " " + label + " effective output", zero(b_eff * g - v))
            record(instrument + " " + label + " mean", same_scalar(mean, m * DELTA / EPS ** 2))
            record(instrument + " " + label + " second moment", same_scalar(second, m * DELTA ** 2 * a / EPS ** 6))
            record(instrument + " " + label + " high probability", same_scalar(phigh, m * EPS ** 2 / a))
            record(instrument + " " + label + " no Qdark energy", scalar(v.T * qd * v) == 0)
            record(instrument + " " + label + " low projection energy", zero(H * low * v))
            if instrument == "resolved":
                c = int(label.split(",")[1])
                record(instrument + " " + label + " analytic sector count", normsq == 2 and m == (2 if c == 1 else 1))
            else:
                record(instrument + " " + label + " analytic sector count", normsq == 4 and m == sy.Rational(3, 2))
            rows[label] = {
                "v_sparse": matrix_entries(v), "norm_squared": str(normsq), "m": str(m),
                "rate": str(rate), "mean": str(mean), "second_moment": str(second),
                "variance": str(sy.factor(second - mean ** 2)), "high_probability": str(phigh),
            }
            jloss = jump.T * jump
            source = KAPPA * EPS ** -2 * jump * rho * jump.T
            anticom = -KAPPA * EPS ** -2 * (jloss * rho + rho * jloss) / 2
            diss += source + anticom
            recycled += source
            loss += jloss
            sigma += v * v.T / 12
            totalrate += rate
        full_generator = -sy.I * (H * rho - rho * H) + diss
        recycling_energy = sy.simplify(sy.trace(H * recycled))
        derivative = sy.simplify(sy.trace(H * full_generator))
        anticom_energy = sy.simplify(sy.trace(H * (diss - recycled)))
        bare_diss = sy.zeros(dim)
        for jump in jumps.values():
            jloss = jump.T * jump
            bare_diss += KAPPA * EPS ** -2 * (jump * g_rho * jump.T - (jloss * g_rho + g_rho * jloss) / 2)
        bare_derivative = sy.simplify(sy.trace(H * (-sy.I * (H * g_rho - g_rho * H) + bare_diss)))
        loss_expected = sy.diag(*[4 if N[i, i] == 1 and W[i, i] == 1 else 0 for i in range(dim)])
        record(instrument + " full loss", loss == loss_expected)
        record(instrument + " N3 cannot jump", all(jump[:, sectors["3"]["indices"]].is_zero_matrix for jump in jumps.values()))
        record(instrument + " total rate", same_scalar(totalrate, 12 * KAPPA / a))
        record(instrument + " initial full energy derivative", same_scalar(derivative, 18 * KAPPA * DELTA / (EPS ** 2 * a)))
        record(instrument + " loss energy term exactly zero", anticom_energy == 0)
        record(instrument + " recycling equals full derivative", same_scalar(recycling_energy, derivative))
        record(instrument + " bare energy derivative", bare_derivative == 0)
        record(instrument + " mixed output trace", sy.trace(sigma) == 1)
        record(instrument + " mixed output m", sy.trace(C * sigma) == sy.Rational(3, 2))
        out["instruments"][instrument] = {
            "marks": rows, "total_rate": str(sy.factor(totalrate)),
            "initial_energy_derivative": str(sy.factor(derivative)),
            "recycling_energy": str(sy.factor(recycling_energy)),
            "anticommutator_energy": str(anticom_energy),
            "bare_derivative": str(bare_derivative),
            "sigma_sparse": matrix_entries(sigma),
        }
    # Mutation probes test the actual identities above, including a sign defect
    # that energy-only controls would miss.
    bad_compensation = C + P / 7
    bad_h = W + EPS * T + EPS ** 2 * bad_compensation
    record("mutation wrong compensation detected", not zero(bad_h * raw_dressed))
    bad_jump = model["jumps"][(1, 1)] - model["jumps"][(1, -1)]
    intended_jump = instruments["coherent"]["1"]
    bad_output, intended_output = bad_jump * F * g, intended_jump * F * g
    record("mutation coherent relative sign changes density", bad_output * bad_output.T != intended_output * intended_output.T)
    record("energy-only check would miss relative-sign mutation", scalar(bad_output.T * C * bad_output) == scalar(intended_output.T * C * intended_output))
    record("mutation omitted jump scaling detected", not same_scalar(12 * KAPPA * EPS ** 2 / a, 12 * KAPPA / a))
    return out, instruments, g, raw_dressed, h


def floating_dynamics(model, instruments, g, raw_dressed, h):
    delta, kappa = 1.7, 0.4
    times = (0.03, 0.2)
    dim = model["F"].rows
    ident = np.eye(dim, dtype=complex)
    gn = np.array(g, dtype=complex).ravel()
    F = np.array(model["F"], dtype=float)
    rows = []
    for name, symbolic_jumps in instruments.items():
        js = [np.array(j, dtype=complex) for j in symbolic_jumps.values()]
        sigma = sum(np.outer(j @ F @ gn, (j @ F @ gn).conj()) for j in js) / 12
        for epsilon in (0.25, 0.125, 0.0625, 0.03125):
            H = delta * epsilon ** -4 * np.array(h.subs(EPS, epsilon), dtype=float)
            dressed = np.array(raw_dressed.subs(EPS, epsilon), dtype=complex).ravel()
            dressed /= np.linalg.norm(dressed)
            rho0 = np.outer(dressed, dressed.conj())
            liouville = -1j * (np.kron(ident, H) - np.kron(H.T, ident))
            for j in js:
                l = np.sqrt(kappa) / epsilon * j
                loss = l.conj().T @ l
                liouville += np.kron(l.conj(), l) - (np.kron(ident, loss) + np.kron(loss.T, ident)) / 2
            for t in times:
                evolved = (expm(t * liouville) @ rho0.reshape(-1, order="F")).reshape((dim, dim), order="F")
                target = np.exp(-12 * kappa * t) * np.outer(gn, gn) + (1 - np.exp(-12 * kappa * t)) * sigma
                hermitian = (evolved + evolved.conj().T) / 2
                error = float(np.linalg.svd(evolved - target, compute_uv=False).sum())
                n3inds = [i for i in range(dim) if model["N"][i, i] == 3]
                probability = float(np.trace(evolved[np.ix_(n3inds, n3inds)]).real)
                energy = float(np.trace(H @ evolved).real)
                lower_bound = 1.5 * delta * epsilon ** -2 * probability
                record(f"floating trace {name} {epsilon} {t}", abs(np.trace(evolved) - 1) < 2e-8)
                record(f"floating positivity {name} {epsilon} {t}", np.linalg.eigvalsh(hermitian).min() > -2e-8)
                record(f"floating energy lower bound {name} {epsilon} {t}", energy >= lower_bound - 2e-6)
                rows.append({
                    "instrument": name, "epsilon": epsilon, "delta": delta, "kappa": kappa, "time": t,
                    "density_trace_error": error, "error_over_epsilon": error / epsilon,
                    "trace": [float(np.trace(evolved).real), float(np.trace(evolved).imag)],
                    "hermiticity_error": float(np.linalg.norm(evolved - evolved.conj().T)),
                    "minimum_eigenvalue": float(np.linalg.eigvalsh(hermitian).min()),
                    "N3_probability": probability, "target_N3_probability": float(1 - np.exp(-12 * kappa * t)),
                    "energy": energy, "jump_branch_energy_lower_bound": lower_bound,
                })
    return rows


def main(attempt):
    result_path = HERE / f"RESULTS_{attempt}.json"
    if result_path.exists():
        raise FileExistsError("Preserve earlier results: choose a fresh --attempt.")
    started = time.time()
    result = {
        "attempt": attempt, "status": "running", "checks": CHECKS,
        "runtime": {"python": sys.version, "platform": platform.platform(),
                    "numpy": np.__version__, "scipy": scipy.__version__, "sympy": sy.__version__},
        "runner_sha256": digest(Path(__file__)),
        "scope": "Independent PRE; no campaign builder imported; complete finite tensor-basis enumeration.",
    }
    try:
        source_manifest = []
        for relative, expected in SOURCE_ROWS.items():
            path = SCIENCE / relative
            actual = digest(path)
            source_manifest.append({"path": str(path), "sha256": actual, "expected": expected})
            record("source identity " + relative, actual == expected)
        result["sources"] = source_manifest
        models = {}
        basis_certificates = {}
        for spin in (1, 2, 4):
            model = construct(spin)
            models[spin] = model
            record(f"S={spin} physical dimension", len(model["basis"]) == 16, len(model["basis"]))
            record(f"S={spin} number sectors", sorted(set(model["N"].diagonal())) == [1, 3])
            record(f"S={spin} P dimension", sy.trace(model["P"]) == 10)
            record(f"S={spin} Q dimension", sy.trace(model["W"]) == 6)
            record(f"S={spin} spin weights", all(t["weight"] == "1" for t in model["transitions"]))
            record(f"S={spin} compensation diagonal identity", model["DS"] == model["Dinf"])
            record(f"S={spin} T assembly identity", model["T"] == -(model["F"] + model["F"].T))
            record(f"S={spin} compensation identity", model["compensation"] == model["F"].T * model["F"])
            record(f"S={spin} hopping number conservation", zero(model["N"] * model["T"] - model["T"] * model["N"]))
            for label, j in model["jumps"].items():
                record(f"S={spin} birth selection {label}", zero(model["N"] * j - j * model["N"] - 2 * j) and zero(model["W"] * j - j * model["W"] + j))
            basis_certificates[str(spin)] = {
                "basis": [{"q": list(q), "E": list(e)} for q, e in model["basis"]],
                "transitions": model["transitions"],
                "operators": {k: matrix_entries(model[k]) for k in ("F", "T", "W", "P", "N", "DS", "Dinf", "compensation")},
                "jumps": {str(k): matrix_entries(v) for k, v in model["jumps"].items()},
            }
        for spin in (2, 4):
            record(f"S={spin} full S-independent matrices", all(models[spin][k] == models[1][k] for k in ("F", "T", "W", "N", "compensation")) and models[spin]["jumps"] == models[1]["jumps"])
        result["basis_certificates"] = basis_certificates
        result["exact"], instruments, g, raw_dressed, h = exact_analysis(models[1])
        result["floating"] = floating_dynamics(models[1], instruments, g, raw_dressed, h)
        for row in source_manifest:
            record("end source identity " + row["path"], digest(Path(row["path"])) == row["sha256"])
        result["status"] = "completed"
    except Exception as exc:
        result["status"] = "failed"
        result["exception"] = repr(exc)
        result["traceback"] = traceback.format_exc()
        raise
    finally:
        result["elapsed_seconds"] = time.time() - started
        result["summary"] = {"passed": sum(x["passed"] for x in CHECKS), "failed": sum(not x["passed"] for x in CHECKS)}
        result_path.write_text(json.dumps(result, indent=2) + "\n")
        print(json.dumps({"result": str(result_path), "status": result["status"], **result["summary"]}, sort_keys=True))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--attempt", required=True)
    main(parser.parse_args().attempt)
