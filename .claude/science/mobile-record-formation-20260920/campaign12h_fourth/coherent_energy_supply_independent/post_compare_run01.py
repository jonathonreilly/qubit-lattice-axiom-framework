#!/usr/bin/env python3
"""POST comparison; uses the checker's frozen star engine, no author imports."""
from pathlib import Path
import argparse
import datetime
import hashlib
import importlib.util
import json
import sys
import traceback

sys.dont_write_bytecode = True
import sympy as sy

HERE = Path(__file__).resolve().parent
AUTHOR = HERE.parent / "coherent_energy_supply_author"
STAR = HERE.parent / "microscopic_birth_energy_independent"
CHECKS = []
PINS = {
    HERE / "PRE_SEAL.json": "ec6d33b271b05faf74700d9f9346921a5f652fb860c967b631d79b21a8b51d0d",
    AUTHOR / "AUTHOR_SEAL.json": "350648ccf962bf0b225e8c0eb8cbe0e101bd80eefe307e064603d61cddbf7d90",
}


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def check(name, value, detail=None):
    row = {"name": name, "passed": bool(value)}
    if detail is not None:
        row["detail"] = detail
    CHECKS.append(row)
    if not value:
        raise AssertionError(name)


def zero(m):
    return all(sy.simplify(x) == 0 for x in m)


def equal(a, b):
    return a.shape == b.shape and zero(a - b)


def outer(v):
    return v * v.T


def tensor(a, b):
    return sy.kronecker_product(a, b)


def authenticate():
    for path, expected in PINS.items():
        check("seal " + str(path), sha(path) == expected)
        record = json.loads(path.read_text())
        for row in record.get("artifacts", record.get("files", [])):
            check("artifact " + str(path.parent / row["path"]),
                  sha(path.parent / row["path"]) == row["sha256"])


def main(attempt):
    output = HERE / f"POST_RESULTS_{attempt}.json"
    if output.exists():
        raise FileExistsError("Use a fresh attempt name; previous results stay fixed.")
    result = {
        "created_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "runner_sha256": sha(Path(__file__)), "attempt": attempt,
        "status": "running", "checks": CHECKS,
        "author_code_imported": False, "full_instrument_packet_read": False,
    }
    try:
        authenticate()
        source = STAR / "microscopic_star_complete_matrix_check.py"
        check("independent star engine pin",
              sha(source) == "6652f0c847d478f0db29b3fc4f9f739c309ce4126be69dd48221ab5d9377892b")
        spec = importlib.util.spec_from_file_location("independent_checked_star", source)
        pre = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(pre)
        model = pre.construct(1)
        F, T, W, C, N = [model[x] for x in ("F", "T", "W", "compensation", "N")]
        g = sy.zeros(16, 1)
        g[model["basis"].index(((1, 0, 0, 0), (0, 0, 0))), 0] = 1
        own = json.loads((HERE / "RESULTS_01.json").read_text())
        author = json.loads((AUTHOR / "COHERENT_FUEL_RESULTS.json").read_text())
        author_U = sy.Matrix(author["abstract_unitary"])
        own_U = sy.Matrix(own["generic"]["generic_U"])
        check("entire abstract U agrees with independently sealed U", author_U == own_U)
        odds, omega = sy.symbols("r Omega", positive=True)
        locals_ = {"r": odds, "Omega": omega}
        p = odds / (1 + odds)
        check("author abstract free-energy diagonal",
              sy.Matrix([sy.sympify(x, locals=locals_) for x in author["total_free_energy_diagonal"]])
              == sy.Matrix([0, omega, 0, omega, omega, 2 * omega]))
        check("author fuel mean", sy.simplify(
            sy.sympify(author["fuel_mean_energy"], locals=locals_) - p * omega) == 0)
        check("author trace coherence", sy.simplify(
            sy.sympify(author["fuel_and_output_trace_asymmetry"], locals=locals_)
            - 2 * sy.sqrt(p * (1 - p))) == 0)
        rows = []
        r0, r1 = sy.eye(2)[:, 0], sy.eye(2)[:, 1]

        def reconstruct(e, mark):
            a = 1 + 3 * e ** 2
            h = W + e * T + e ** 2 * C
            H = h / e ** 4  # Author embedding rows specify delta=1.
            E = a / e ** 4
            qdark = W - F * F.T / 3
            Phi = (h - qdark) / a
            dressed = (g + e * F * g) / sy.sqrt(a)
            if mark == "plus":
                j = model["jumps"][(1, 1)]
            elif mark == "minus":
                j = model["jumps"][(1, -1)]
            else:
                j = model["jumps"][(1, 1)] + model["jumps"][(1, -1)]
            v = j * F * g
            norm2 = (v.T * v)[0]
            phi = v / sy.sqrt(norm2)
            highpart = Phi * phi
            lowpart = phi - highpart
            p = sy.simplify((highpart.T * highpart)[0])
            low, high = lowpart / sy.sqrt(1 - p), highpart / sy.sqrt(p)
            m = sy.simplify((phi.T * F.T * F * phi)[0])
            return H, E, dressed, low, high, phi, p, m, norm2

        for announced in author["physical_star_embeddings"]:
            e, mark = sy.Rational(announced["epsilon"]), announced["mark"]
            H, E, d, low, high, phi, p, m, norm2 = reconstruct(e, mark)
            prefix = f"{e} {mark}"
            values = {
                "c": m, "p_high": p, "fuel_gap": E, "fuel_energy": p * E,
                "minimum_stationary_trace_norm_distance": 2 * sy.sqrt(p * (1 - p)),
            }
            for key, computed in values.items():
                check(prefix + " " + key,
                      sy.simplify(computed - sy.sympify(announced[key])) == 0)
            frame = sy.Matrix.hstack(d, low, high)
            check(prefix + " exact actual star frame", equal(frame.T * frame, sy.eye(3)))
            check(prefix + " exact frame energies", equal(
                H * frame, frame * sy.diag(0, 0, E)))
            U = sy.eye(32) - outer(tensor(d, r0) - tensor(low, r0)) - outer(tensor(d, r1) - tensor(high, r0))
            Hsum = tensor(H, sy.eye(2)) + tensor(sy.eye(16), sy.diag(0, E))
            check(prefix + " full 32-state unitarity", equal(U.T * U, sy.eye(32)))
            check(prefix + " full 32-state energy conservation", zero(U * Hsum - Hsum * U))
            frame6 = sy.Matrix.hstack(*[
                tensor(v, r) for v in (d, low, high) for r in (r0, r1)
            ])
            check(prefix + " author six-state action matches full embedding",
                  equal(frame6.T * U * frame6, author_U))
            check(prefix + " full orthogonal complement is identity",
                  zero((U - sy.eye(32)) * (sy.eye(32) - frame6 * frame6.T)))
            eta = sy.Matrix([sy.sqrt(1 - p), sy.sqrt(p)])
            check(prefix + " actual exact output",
                  equal(U * tensor(d, eta), tensor(phi, r0)))
            rows.append({"epsilon": str(e), "mark": mark,
                         **{key: str(value) for key, value in values.items()}})
        result["exact_author_embedding_comparisons"] = rows

        # Independently realize the author's classical-selector claim as
        # orthogonal flag blocks; no need to densify a 192-state matrix.
        ensemble_rows = []
        e = sy.Rational(1, 5)
        for instrument in ("resolved", "coherent"):
            branch_data = []
            if instrument == "resolved":
                labels = [(b, sign) for b in (1, 2, 3) for sign in (-1, 1)]
            else:
                labels = [(b, 0) for b in (1, 2, 3)]
            raw_norms = []
            for b, sign in labels:
                j = model["jumps"][(b, sign)] if sign else model["jumps"][(b, 1)] + model["jumps"][(b, -1)]
                raw = j * F * g
                raw_norms.append(sy.simplify((raw.T * raw)[0]))
            total_norm = sum(raw_norms)
            mean_energy, total_coherence = sy.Integer(0), sy.Integer(0)
            for (b, sign), norm2 in zip(labels, raw_norms):
                mark = "plus" if sign == 1 else "minus" if sign == -1 else "coherent"
                H, E, d, low, high, phi, p, m, _ = reconstruct(e, mark)
                weight = norm2 / total_norm
                fuel = sy.Matrix([sy.sqrt(1 - p), sy.sqrt(p)])
                fuel_off = outer(fuel) - sy.diag(1 - p, p)
                output_off = outer(phi) - (1 - p) * outer(low) - p * outer(high)
                check(f"selector {instrument} {b} {sign} input block trace norm",
                      equal((weight * fuel_off) ** 2, weight ** 2 * p * (1 - p) * sy.eye(2)))
                check(f"selector {instrument} {b} {sign} output block trace norm",
                      equal((weight * output_off) ** 2,
                            weight ** 2 * p * (1 - p) * (outer(low) + outer(high))))
                mean_energy += weight * p * E
                total_coherence += 2 * weight * sy.sqrt(p * (1 - p))
                branch_data.append({"edge": b, "sign": sign, "weight": str(weight),
                                    "p": str(p), "mean_energy": str(weight * p * E)})
            check("selector " + instrument + " mark weights normalize",
                  sum(raw_norms) / total_norm == 1)
            check("selector " + instrument + " mean energy matches author",
                  sy.simplify(mean_energy - 3 / (2 * e ** 2)) == 0)
            ensemble_rows.append({
                "instrument": instrument, "epsilon": str(e), "delta": "1",
                "branches": branch_data, "mean_supplied_energy": str(sy.simplify(mean_energy)),
                "weighted_trace_coherence": str(sy.simplify(total_coherence)),
                "orthogonal_flag_blocks_saturate_weighted_bound": True,
            })
        result["selector_reconstruction"] = ensemble_rows

        # The author's preserved first failure was an expression-form issue.
        check("author failed structural equality reproduced",
              1 - odds / (1 + odds) != 1 / (1 + odds))
        check("author corrected symbolic equality valid",
              sy.simplify(1 - odds / (1 + odds) - 1 / (1 + odds)) == 0)
        authenticate()
        check("final independent star engine pin",
              sha(source) == "6652f0c847d478f0db29b3fc4f9f739c309ce4126be69dd48221ab5d9377892b")
        result["status"] = "completed"
    except Exception as exc:
        result["status"] = "failed"
        result["exception"] = repr(exc)
        result["traceback"] = traceback.format_exc()
        raise
    finally:
        result["summary"] = {"passed": sum(row["passed"] for row in CHECKS),
                             "failed": sum(not row["passed"] for row in CHECKS)}
        output.write_text(json.dumps(result, indent=2) + "\n")
        print(json.dumps({"result": str(output), "status": result["status"], **result["summary"]}))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--attempt", required=True)
    main(parser.parse_args().attempt)
