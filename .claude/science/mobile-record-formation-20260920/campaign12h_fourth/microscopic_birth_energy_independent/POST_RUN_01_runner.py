#!/usr/bin/env python3
"""POST comparison and independent extension control using only frozen PRE code.

The author notes, code and results were read after the PRE seal. No author
builder is imported or executed. Stable spectral exponentials, independently
derived from the frozen complete matrices, check the author's expm controls.
"""
from pathlib import Path
import argparse
import datetime
import hashlib
import importlib.util
import json
import sys
import traceback

sys.dont_write_bytecode = True
import mpmath as mp
import numpy as np
from scipy.linalg import expm
import sympy as sy

HERE = Path(__file__).resolve().parent
AUTH = HERE.parent / "microscopic_birth_energy_author"
EXT = HERE.parent / "microscopic_birth_energy_extension_author"
PINNED = {
    HERE / "PRE_SEAL.json": "82e5b45bc8ecf0aad7deb8f2af8c457062c2bcb860dc83d18c4538a1ac3053d9",
    AUTH / "AUTHOR_SEAL.json": "ff9362d4ad06b36c86153d71b23b361843a77a26ceb4400f7b6ed14bea12aff5",
    EXT / "AUTHOR_SEAL.json": "4812c28ae4ec3cfcace52536cecd9156557cd851b1fd2b2958d361cc49fca3b1",
}
CHECKS = []


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def check(name, condition, detail=None):
    item = {"name": name, "passed": bool(condition)}
    if detail is not None:
        item["detail"] = detail
    CHECKS.append(item)
    if not condition:
        raise AssertionError(name)


def equal_matrix(left, right):
    return left.shape == right.shape and all(sy.simplify(x) == 0 for x in left - right)


def read_pins():
    for path, expected in PINNED.items():
        check("seal " + str(path), sha(path) == expected)
        seal = json.loads(path.read_text())
        for row in seal.get("artifacts", seal.get("files", [])):
            check("artifact " + str(path.parent / row["path"]),
                  sha(path.parent / row["path"]) == row["sha256"])


def stable_spectral(epsilon, delta, kappa, time):
    """Scalar spectral formula; deliberately no matrix exponential here."""
    e, d, k, t = [mp.mpf(str(x)) for x in (epsilon, delta, kappa, time)]
    eta, a = e ** 2, 1 + 3 * e ** 2
    b = 1j * d * a + 2 * k * eta
    c = 6j * k * d
    root = mp.sqrt(b * b - 4 * eta ** 2 * c)
    if root.imag < 0:
        root = -root
    zs = -2 * c / (b + root)
    zf = -b / eta ** 2 - zs
    aa = -6 * k / a
    dd = -2 * k / (eta * a) - 1j * d * a / eta ** 2
    off = 2 * mp.sqrt(3) * k / (e * a)
    q = -off / (dd - zs)
    p = off / (zf - aa)
    determinant = 1 - p * q
    slow, fast = mp.exp(zs * t), mp.exp(zf * t)
    low = (slow - p * q * fast) / determinant
    high = q * (slow - fast) / determinant
    pb = 1 - abs(low) ** 2 - abs(high) ** 2
    eno = d * a / eta ** 2 * abs(high) ** 2
    etotal = eno + mp.mpf("1.5") * d / eta * pb
    residuals = (
        abs(aa + off * q - zs),
        abs(off + dd * q - zs * q),
        abs(aa * p + off - zf * p),
        abs(off * p + dd - zf),
    )
    return {
        "birth": pb, "no_event_energy": eno, "energy": etotal,
        "slow": zs, "fast": zf, "slow_high_ratio": q, "fast_low_ratio": p,
        "low": low, "high": high, "max_eigen_residual": max(residuals),
    }


def main(attempt):
    target = HERE / f"POST_RESULTS_{attempt}.json"
    if target.exists():
        raise FileExistsError("Select a fresh attempt; never overwrite evidence.")
    result = {
        "created_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "status": "running", "attempt": attempt, "checks": CHECKS,
        "runner_sha256": sha(Path(__file__)), "author_builders_imported": False,
    }
    try:
        read_pins()
        spec = importlib.util.spec_from_file_location(
            "frozen_independent_pre", HERE / "microscopic_star_complete_matrix_check.py")
        pre = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(pre)
        model = pre.construct(1)
        e, d, k = pre.EPS, pre.DELTA, pre.KAPPA
        locals_ = {"epsilon": e, "delta": d, "kappa": k}
        parse = lambda text: sy.sympify(text, locals=locals_)
        author = json.loads((AUTH / "EXACT_STAR_ENERGY_RESULTS.json").read_text())
        extension = json.loads((EXT / "STAR_FINITE_TIME_ENERGY_RESULTS.json").read_text())
        pre_result = json.loads((HERE / "RESULTS_02.json").read_text())
        basis, F, T, W, N, C = [model[x] for x in
                                  ("basis", "F", "T", "W", "N", "compensation")]
        qindex = {q: i for i, (q, _) in enumerate(basis)}
        for number in (1, 3):
            author_basis = author["physical_bases"][str(number)]
            permutation = [qindex[tuple(row["q"])] for row in author_basis]
            check(f"N={number} full Gauss basis", {
                (tuple(row["q"]), tuple(row["E"])) for row in author_basis
            } == {state for i, state in enumerate(basis) if N[i, i] == number})
            block = F.extract(permutation, permutation)
            check(f"N={number} entire F matrix", block == sy.Matrix(author["F_matrices"][str(number)]))
        g = sy.zeros(16, 1)
        g[qindex[(1, 0, 0, 0)], 0] = 1
        for row in author["rows"]:
            instrument, b = row["instrument"], row["edge"][1]
            if instrument == "resolved":
                label = f"{b},{int(row['mark']):+d}"
                jump = model["jumps"][(b, int(row["mark"]))]
            else:
                label = str(b)
                jump = model["jumps"][(b, 1)] + model["jumps"][(b, -1)]
            actual = jump * F * g
            announced = sy.zeros(16, 1)
            for output in row["physical_output"]:
                check("author output Gauss " + label, tuple(output["E"]) == basis[qindex[tuple(output["q"])]][1])
                announced[qindex[tuple(output["q"])], 0] = parse(output["unnormalized_amplitude"])
            check("actual complete output " + instrument + label, actual == announced)
            independent = pre_result["exact"]["instruments"][instrument]["marks"][label]
            for author_key, pre_key in (
                ("rate", "rate"), ("c", "m"), ("conditional_energy", "mean"),
                ("high_spectral_probability", "high_probability"),
                ("conditional_energy_variance", "variance"),
                ("target_B_norm_squared", "norm_squared"),
            ):
                check("author formula " + instrument + label + author_key,
                      sy.simplify(parse(row[author_key]) - parse(independent[pre_key])) == 0)
        for instrument in ("resolved", "coherent"):
            check("author full initial derivative " + instrument, sy.simplify(
                parse(author["dressed_initial_energy_derivative"][instrument]) -
                parse(pre_result["exact"]["instruments"][instrument]["initial_energy_derivative"])) == 0)

        H = d * e ** -4 * (W + e * T + e ** 2 * C)
        basis2 = sy.Matrix.hstack(g, F * g / sy.sqrt(3))
        gamma = sum((j.T * j for j in model["jumps"].values()), sy.zeros(16))
        Gfull = -sy.I * H - k / (2 * e ** 2) * gamma
        G = sy.simplify(basis2.T * Gfull * basis2)
        check("two-dimensional no-event space reduces full generator",
              equal_matrix(Gfull * basis2, basis2 * G))
        z, eta = sy.symbols("z eta")
        polynomial = sy.factor(e ** 4 * (z * sy.eye(2) - G).det())
        eta_polynomial = sy.expand(polynomial).subs(e ** 4, eta ** 2).subs(e ** 2, eta)
        z0 = sy.solve(eta_polynomial.subs(eta, 0), z)[0]
        a1 = sy.symbols("a1")
        a1eq = sy.expand(eta_polynomial.subs(z, z0 + a1 * eta)).coeff(eta, 1)
        z1 = sy.simplify(sy.solve(a1eq, a1)[0])
        check("implicit derivative nonzero", sy.diff(eta_polynomial, z).subs({eta: 0, z: z0}) == sy.I * d)
        check("slow root leading term agrees", z0 == -6 * k)
        check("slow root correction agrees", sy.simplify(z1 - (18 * k - 12 * sy.I * k ** 2 / d)) == 0)
        check("dissipativity", equal_matrix(G + G.conjugate().T, sy.diag(0, -4 * k / e ** 2)))
        H2 = sy.simplify(basis2.T * H * basis2)
        null = H2.nullspace()[0]
        null /= null[0]
        ell = sy.simplify(null / sy.sqrt((null.T * null)[0]))
        high = sy.Matrix([ell[1], -ell[0]])
        rotation = sy.Matrix.hstack(ell, high)
        rotated = sy.simplify(rotation.T * G * rotation)
        check("orthonormal low/high frame", equal_matrix(rotation.T * rotation, sy.eye(2)))
        check("no-event energy spectral decomposition",
              equal_matrix(rotation.T * H2 * rotation, sy.diag(0, d * (1 + 3 * e ** 2) / e ** 4)))
        qs = sy.series((z0 + z1 * e ** 2 - rotated[0, 0]) / rotated[0, 1], e, 0, 4).removeO()
        zfast = sy.trace(G) - z0 - z1 * e ** 2
        ps = sy.series(rotated[0, 1] / (zfast - rotated[0, 0]), e, 0, 4).removeO()
        check("slow high component starts at epsilon cubed", sy.simplify(qs + 2 * sy.sqrt(3) * sy.I * k * e ** 3 / d) == 0)
        check("fast low component starts at epsilon cubed", sy.simplify(ps - 2 * sy.sqrt(3) * sy.I * k * e ** 3 / d) == 0)
        result["exact_extension"] = {
            "polynomial": str(polynomial), "slow_z0": str(z0), "slow_z1": str(z1),
            "rotated_G": [[str(x) for x in row] for row in rotated.tolist()],
            "slow_high_leading": str(qs), "fast_low_leading": str(ps),
        }
        mp.mp.dps = 90
        joint_rows = []
        for author_row in extension["high_precision_joint_limit_rows"]:
            spin = author_row["S"]
            epsilon = 1 / mp.sqrt(spin * (spin + 1))
            exact = stable_spectral(epsilon, 1, 1, "0.2")
            differences = {
                "P_birth": abs(exact["birth"] - mp.mpf(author_row["P_birth"])),
                "no_event_energy": abs(exact["no_event_energy"] - mp.mpf(author_row["no_event_energy"])),
                "epsilon_squared_energy": abs(epsilon ** 2 * exact["energy"] - mp.mpf(author_row["epsilon_squared_energy"])),
            }
            check(f"S={spin} author high-precision rows", max(differences.values()) < mp.mpf("1e-28"))
            check(f"S={spin} spectral eigen residual", exact["max_eigen_residual"] < mp.mpf("1e-70"))
            joint_rows.append({
                "S": spin, "epsilon": mp.nstr(epsilon, 40),
                "birth": mp.nstr(exact["birth"], 40),
                "no_event_energy": mp.nstr(exact["no_event_energy"], 40),
                "epsilon_squared_energy": mp.nstr(epsilon ** 2 * exact["energy"], 40),
                "author_differences": {key: mp.nstr(value, 8) for key, value in differences.items()},
                "max_eigen_residual": mp.nstr(exact["max_eigen_residual"], 8),
            })
        result["joint_row_comparisons"] = joint_rows
        asymptotic_rows = []
        for e_text in ("0.1", "0.05", "0.025", "0.0125", "0.00625"):
            for t in ("0", "0.0001", "0.03", "0.2", "0.7"):
                epsilon = mp.mpf(e_text)
                exact = stable_spectral(epsilon, "1.7", "0.4", t)
                limiting_birth = 1 - mp.exp(-mp.mpf("4.8") * mp.mpf(t))
                asymptotic_rows.append({
                    "epsilon": e_text, "time": t,
                    "high_amplitude_over_epsilon_cubed": mp.nstr(abs(exact["high"]) / epsilon ** 3, 20),
                    "no_event_energy_over_epsilon_squared": mp.nstr(exact["no_event_energy"] / epsilon ** 2, 20),
                    "birth_error_over_epsilon_squared": mp.nstr(abs(exact["birth"] - limiting_birth) / epsilon ** 2, 20),
                    "scaled_energy_error": mp.nstr(abs(epsilon ** 2 * exact["energy"] - mp.mpf("2.55") * limiting_birth), 20),
                })
        result["asymptotic_controls"] = asymptotic_rows
        floating_rows = []
        for row in extension["full_GKLS_rows"]:
            epsilon, delta, kappa, t = [row[x] for x in ("epsilon", "delta", "kappa", "time")]
            full_H = np.array(H.subs({e: epsilon, d: delta}), dtype=complex)
            raw = np.array(g + epsilon * F * g, dtype=complex).ravel()
            raw /= np.linalg.norm(raw)
            rho = np.outer(raw, raw.conj())
            ident = np.eye(16)
            independent = stable_spectral(epsilon, delta, kappa, t)
            predicted = float(independent["energy"])
            pb = float(independent["birth"])
            for instrument in ("resolved", "coherent"):
                if instrument == "resolved":
                    js = list(model["jumps"].values())
                else:
                    js = [model["jumps"][(b, 1)] + model["jumps"][(b, -1)] for b in (1, 2, 3)]
                generator = -1j * (np.kron(ident, full_H) - np.kron(full_H.T, ident))
                for j in js:
                    ll = np.sqrt(kappa) / epsilon * np.array(j, dtype=complex)
                    jj = ll.conj().T @ ll
                    generator += np.kron(ll.conj(), ll) - (np.kron(ident, jj) + np.kron(jj.T, ident)) / 2
                evolved = (expm(generator * t) @ rho.reshape(-1, order="F")).reshape((16, 16), order="F")
                n3 = [i for i in range(16) if N[i, i] == 3]
                actual_birth = float(np.trace(evolved[np.ix_(n3, n3)]).real)
                actual_energy = float(np.trace(full_H @ evolved).real)
                check(f"full {instrument} {epsilon} {t} birth", abs(actual_birth - pb) < 5e-10)
                check(f"full {instrument} {epsilon} {t} energy", abs(actual_energy - predicted) < 5e-8 * (1 + abs(predicted)))
                check(f"author {instrument} {epsilon} {t} energy", abs(actual_energy - row["energy_full_GKLS"]) < 5e-8 * (1 + abs(predicted)))
                floating_rows.append({
                    "instrument": instrument, "epsilon": epsilon, "delta": delta, "kappa": kappa, "time": t,
                    "birth": actual_birth, "spectral_birth": pb,
                    "energy": actual_energy, "spectral_energy": predicted,
                    "no_event_energy": float(independent["no_event_energy"]),
                    "absolute_energy_error": abs(actual_energy - predicted),
                    "absolute_author_energy_difference": abs(actual_energy - row["energy_full_GKLS"]),
                    "absolute_birth_error": abs(actual_birth - pb),
                })
        result["full_matrix_extension_controls"] = floating_rows
        check("mutation dropping no-event energy detected",
              max(row["no_event_energy"] for row in floating_rows) > 1)
        bad_slow = -12 * k
        check("mutation doubling slow decay rejected by polynomial",
              sy.simplify(eta_polynomial.subs({eta: 0, z: bad_slow})) != 0)
        # Reauthenticate every bound artifact after computation.
        read_pins()
        result["status"] = "completed"
    except Exception as exc:
        result["status"] = "failed"
        result["exception"] = repr(exc)
        result["traceback"] = traceback.format_exc()
        raise
    finally:
        result["summary"] = {"passed": sum(x["passed"] for x in CHECKS), "failed": sum(not x["passed"] for x in CHECKS)}
        target.write_text(json.dumps(result, indent=2) + "\n")
        print(json.dumps({"result": str(target), "status": result["status"], **result["summary"]}))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--attempt", required=True)
    main(parser.parse_args().attempt)
