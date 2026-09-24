#!/usr/bin/env python3
"""Independent PRE control: conservation, sharp distance and finite resources.

Only the previously sealed independent star engine is imported. No new
author packet is read. All controls are exact finite matrix identities.
"""
import argparse
import datetime
import hashlib
import importlib.util
import json
from pathlib import Path
import sys
import traceback

sys.dont_write_bytecode = True
import sympy as sy

HERE = Path(__file__).resolve().parent
PRE = HERE.parent / "microscopic_birth_energy_independent"
ENGINE = PRE / "microscopic_star_complete_matrix_check.py"
EXPECTED_ENGINE = "6652f0c847d478f0db29b3fc4f9f739c309ce4126be69dd48221ab5d9377892b"
EXPECTED_SEAL = "7b01f616bb45c9374f770bb61ede83cfe8dbc24bf51a3771b8ed4e37cad29b50"
CHECKS = []


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def check(name, condition, detail=None):
    row = {"name": name, "passed": bool(condition)}
    if detail is not None:
        row["detail"] = detail
    CHECKS.append(row)
    if not condition:
        raise AssertionError(name)


def zero(matrix):
    return all(sy.simplify(x) == 0 for x in matrix)


def equal(a, b):
    return a.shape == b.shape and zero(a - b)


def simp(matrix):
    return matrix.applyfunc(sy.simplify)


def outer(vector):
    # Every vector used below is real on its explicitly stated domain.
    return vector * vector.T


def tensor(a, b):
    return sy.kronecker_product(a, b)


def ptrace_r(matrix, ds, dr):
    return sy.Matrix(ds, ds, lambda i, j: sum(matrix[i * dr + r, j * dr + r] for r in range(dr)))


def conditional(joint, effect, ds, dr):
    # Partial-trace cyclicity makes the effect formula equal to any
    # reservoir-only instrument having this effect.
    return simp(ptrace_r(tensor(sy.eye(ds), effect) * joint, ds, dr))


def swap_vectors(a, b):
    return sy.eye(a.rows) - outer(a - b)


def matrix_rows(matrix):
    return [[str(x) for x in row] for row in matrix.tolist()]


def generic_control():
    # Mathematical domain: 0<p<1, E>0 and 0<r<=1. Transposes are adjoints.
    p, r, E = sy.symbols("p r E", positive=True)
    gd = sy.Matrix([1, 0, 0])
    low = sy.Matrix([0, 1, 0])
    high = sy.Matrix([0, 0, 1])
    r0, r1 = sy.eye(2)[:, 0], sy.eye(2)[:, 1]
    eta = sy.Matrix([sy.sqrt(1 - p), sy.sqrt(p)])
    phi = sy.sqrt(1 - p) * low + sy.sqrt(p) * high
    HS, HR = sy.diag(0, 0, E), sy.diag(0, E)
    Hsum = tensor(HS, sy.eye(2)) + tensor(sy.eye(3), HR)
    x, y = tensor(gd, r0), tensor(low, r0)
    u, v = tensor(gd, r1), tensor(high, r0)
    U = sy.eye(6) - outer(x - y) - outer(u - v)
    check("generic conserving U is unitary", equal(U.T * U, sy.eye(6)))
    check("generic conserving U commutes with free total energy", zero(U * Hsum - Hsum * U))
    initial, expected = tensor(gd, eta), tensor(phi, r0)
    check("generic exact pure output and reservoir vacuum", equal(U * initial, expected))
    check("generic input reservoir mean energy", sy.simplify((eta.T * HR * eta)[0] - p * E) == 0)
    check("generic output system mean energy", sy.simplify((phi.T * HS * phi)[0] - p * E) == 0)
    variance_r = sy.simplify((eta.T * HR ** 2 * eta)[0] - (p * E) ** 2)
    variance_s = sy.simplify((phi.T * HS ** 2 * phi)[0] - (p * E) ** 2)
    check("generic energy variance transferred", variance_r == variance_s == p * (1 - p) * E ** 2)
    rho_stationary = sy.diag(1 - p, p)
    stationary_joint = U * tensor(outer(gd), rho_stationary) * U.T
    dephased = (1 - p) * outer(low) + p * outer(high)
    check("stationary mixed reservoir produces dephased target",
          equal(ptrace_r(stationary_joint, 3, 2), dephased))
    difference = outer(phi) - dephased
    witness = low * high.T + high * low.T
    support = outer(low) + outer(high)
    check("sharp-distance difference square", equal(difference ** 2, p * (1 - p) * support))
    check("sharp-distance difference trace", sy.simplify(sy.trace(difference)) == 0)
    check("dual witness norm one", witness.eigenvals() == {-1: 1, 0: 1, 1: 1})
    a, b, c, f, g = sy.symbols("a b c f g", real=True)
    arbitrary_stationary = sy.Matrix([[a, b + sy.I * c, 0], [b - sy.I * c, f, 0], [0, 0, g]])
    check("general stationary matrix including zero-energy coherence",
          zero(HS * arbitrary_stationary - arbitrary_stationary * HS))
    check("dual witness annihilates all stationary matrices",
          sy.trace(witness * arbitrary_stationary) == 0)
    check("dual witness target value",
          sy.simplify(sy.trace(witness * outer(phi)) - 2 * sy.sqrt(p) * sy.sqrt(1 - p)) == 0)
    rcoh = outer(eta) - rho_stationary
    check("reservoir coherence has the same exact trace norm",
          equal(rcoh ** 2, p * (1 - p) * sy.eye(2)))

    # Three-level reservoir, adding a zero-energy classical failure flag.
    rs0, rs1, rf = [sy.eye(3)[:, i] for i in range(3)]
    HR3 = sy.diag(0, E, 0)
    eta_s = sy.sqrt(1 - p) * rs0 + sy.sqrt(p) * rs1
    rho_r3 = r * outer(eta_s) + (1 - r) * outer(rf)
    U3 = sy.eye(9) - outer(tensor(gd, rs0) - tensor(low, rs0)) - outer(tensor(gd, rs1) - tensor(high, rs0))
    success = sy.diag(1, 1, 0)
    Hsum3 = tensor(HS, sy.eye(3)) + tensor(sy.eye(3), HR3)
    check("heralded U unitary", equal(U3.T * U3, sy.eye(9)))
    check("heralded U conserves energy", zero(U3 * Hsum3 - Hsum3 * U3))
    check("herald compatible readout", zero(success * HR3 - HR3 * success))
    joint3 = U3 * tensor(outer(gd), rho_r3) * U3.T
    branch = conditional(joint3, success, 3, 3)
    failure = conditional(joint3, sy.eye(3) - success, 3, 3)
    check("heralded exact branch with arbitrary probability", equal(branch, r * outer(phi)))
    check("heralded failure branch unchanged", equal(failure, (1 - r) * outer(gd)))
    check("heralded average energy lower bound saturated", sy.simplify(sy.trace(HR3 * rho_r3) - r * p * E) == 0)
    rho_r3_dephased = sy.diag(r * (1 - p), r * p, 1 - r)
    check("heralded coherence lower bound saturated",
          equal((rho_r3 - rho_r3_dephased) ** 2,
                sy.diag(r ** 2 * p * (1 - p), r ** 2 * p * (1 - p), 0)))

    # Drop only readout compatibility: a stationary excited reservoir can
    # herald the coherent target by a phase-sensitive measurement.
    incoming = tensor(gd, r1)
    entangled = sy.sqrt(1 - p) * tensor(low, r1) + sy.sqrt(p) * tensor(high, r0)
    Uphase = swap_vectors(incoming, entangled)
    Mphase = outer((r0 + r1) / sy.sqrt(2))
    check("phase-readout example U unitary", equal(Uphase.T * Uphase, sy.eye(6)))
    check("phase-readout example U conserves energy", zero(Uphase * Hsum - Hsum * Uphase))
    check("phase-readout initial reservoir stationary", zero(HR * outer(r1) - outer(r1) * HR))
    phase_joint = outer(Uphase * incoming)
    check("incompatible readout yields exact coherent target",
          equal(conditional(phase_joint, Mphase, 3, 2), outer(phi) / 2))
    check("incompatible readout is detected", not zero(HR * Mphase - Mphase * HR))
    return {
        "domain": "0<p<1, E>0, 0<r<=1",
        "generic_U": matrix_rows(U),
        "sharp_distance": "2*sqrt(p*(1-p))",
        "deterministic_reservoir_energy": "p*E",
        "deterministic_reservoir_variance": str(variance_r),
        "heralded_reservoir_energy": "r*p*E",
        "heralded_trace_coherence": "2*r*sqrt(p*(1-p))",
        "phase_readout_success_probability": "1/2",
    }


def actual_star_control(pre):
    model = pre.construct(1)
    F, T, W, C, N = [model[x] for x in ("F", "T", "W", "compensation", "N")]
    e, delta = sy.Rational(1, 2), sy.Rational(7, 5)
    a = 1 + 3 * e ** 2
    h = W + e * T + e ** 2 * C
    H = delta / e ** 4 * h
    high_energy = delta * a / e ** 4
    qdark = W - F * F.T / 3
    Phi = (h - qdark) / a
    Plo = sy.eye(16) - Phi - qdark
    g = sy.zeros(16, 1)
    g[model["basis"].index(((1, 0, 0, 0), (0, 0, 0))), 0] = 1
    dressed = (g + e * F * g) / sy.sqrt(a)
    check("actual star dressed input has zero energy", zero(H * dressed))
    r0, r1 = sy.eye(2)[:, 0], sy.eye(2)[:, 1]
    HR = sy.diag(0, high_energy)
    Hsum = tensor(H, sy.eye(2)) + tensor(sy.eye(16), HR)
    n1 = sy.diag(*[int(N[i, i] == 1) for i in range(16)])
    rows = []
    instruments = {
        "resolved": {(b, c): j for (b, c), j in model["jumps"].items()},
        "coherent": {(b, 0): model["jumps"][(b, 1)] + model["jumps"][(b, -1)] for b in (1, 2, 3)},
    }
    for instrument, jumps in instruments.items():
        for label, j in jumps.items():
            raw = j * F * g
            phi = raw / sy.sqrt((raw.T * raw)[0])
            p = sy.simplify((phi.T * Phi * phi)[0])
            m = sy.simplify((phi.T * F.T * F * phi)[0])
            check(str((instrument, label)) + " actual high weight",
                  sy.simplify(p - m * e ** 2 / a) == 0 and p > 0 and p < 1)
            low, high = Plo * phi / sy.sqrt(1 - p), Phi * phi / sy.sqrt(p)
            frame = sy.Matrix.hstack(dressed, low, high)
            prefix = str((instrument, label))
            check(prefix + " exact orthonormal energy frame", equal(frame.T * frame, sy.eye(3)))
            check(prefix + " exact low/high energies", zero(H * low) and zero(H * high - high_energy * high))
            eta = sy.Matrix([sy.sqrt(1 - p), sy.sqrt(p)])
            U = sy.eye(32) - outer(tensor(dressed, r0) - tensor(low, r0)) - outer(tensor(dressed, r1) - tensor(high, r0))
            check(prefix + " full 32-state unitary", equal(U.T * U, sy.eye(32)))
            check(prefix + " full energy conservation", zero(U * Hsum - Hsum * U))
            check(prefix + " actual output supplied exactly",
                  equal(U * tensor(dressed, eta), tensor(phi, r0)))
            stationary_joint = U * tensor(outer(dressed), sy.diag(1 - p, p)) * U.T
            dephased = (1 - p) * outer(low) + p * outer(high)
            check(prefix + " dephased bound attained in full star",
                  equal(ptrace_r(stationary_joint, 16, 2), dephased))
            D = outer(phi) - dephased
            check(prefix + " sharp-distance full-star certificate",
                  equal(D ** 2, p * (1 - p) * (outer(low) + outer(high))) and sy.simplify(sy.trace(D)) == 0)
            mean = sy.simplify((phi.T * H * phi)[0])
            variance = sy.simplify((phi.T * H ** 2 * phi)[0] - mean ** 2)
            check(prefix + " microscopic mean supplied", sy.simplify(mean - p * high_energy) == 0)
            check(prefix + " microscopic variance supplied", sy.simplify(variance - p * (1 - p) * high_energy ** 2) == 0)
            check(prefix + " original jumps kill the other input",
                  all(zero(jj * low) for jj in model["jumps"].values()))
            reverse = U * tensor(low, eta)
            returned_n1 = sy.simplify((reverse.T * tensor(n1, sy.eye(2)) * reverse)[0])
            check(prefix + " fixed-input circuit is not original instrument", returned_n1 == 1 - p and returned_n1 > 0)
            rows.append({
                "instrument": instrument, "edge": label[0], "charge": label[1],
                "epsilon": str(e), "delta": str(delta), "m": str(m), "p_high": str(p),
                "E_high": str(high_energy), "energy": str(mean), "variance": str(variance),
                "sharp_trace_distance": str(2 * sy.sqrt(p * (1 - p))),
                "reverse_N1_probability": str(returned_n1),
            })
    return rows


def main(attempt):
    result_file = HERE / f"RESULTS_{attempt}.json"
    if result_file.exists():
        raise FileExistsError("Use a fresh attempt name; previous evidence is immutable.")
    result = {
        "attempt": attempt, "created_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "status": "running", "runner_sha256": sha(Path(__file__)), "checks": CHECKS,
        "author_packet_read": False, "arithmetic": "Exact SymPy finite matrix identities",
    }
    try:
        check("frozen independent engine pin", sha(ENGINE) == EXPECTED_ENGINE)
        check("frozen independent source packet pin", sha(PRE / "FINAL_COMPARISON_SEAL.json") == EXPECTED_SEAL)
        spec = importlib.util.spec_from_file_location("frozen_star_only", ENGINE)
        pre = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(pre)
        result["generic"] = generic_control()
        result["actual_star_rows"] = actual_star_control(pre)
        check("final independent engine pin", sha(ENGINE) == EXPECTED_ENGINE)
        check("final independent source packet pin", sha(PRE / "FINAL_COMPARISON_SEAL.json") == EXPECTED_SEAL)
        result["status"] = "completed"
    except Exception as exc:
        result["status"] = "failed"
        result["exception"] = repr(exc)
        result["traceback"] = traceback.format_exc()
        raise
    finally:
        result["summary"] = {"passed": sum(x["passed"] for x in CHECKS), "failed": sum(not x["passed"] for x in CHECKS)}
        result_file.write_text(json.dumps(result, indent=2) + "\n")
        print(json.dumps({"result": str(result_file), "status": result["status"], **result["summary"]}))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--attempt", required=True)
    main(parser.parse_args().attempt)
