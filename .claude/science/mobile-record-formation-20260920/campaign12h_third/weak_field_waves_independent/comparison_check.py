"""Post-seal selective comparison; no author runner is imported or executed.

The cubic vacuum coefficient is reconstructed by a Fourier trace, avoiding the
author's real-space eigenvectors.  The one-loop packet is Fourier transformed
from a periodized real-space Gaussian and propagated with sparse expm_multiply.
"""
from collections import Counter
from datetime import datetime, timezone
from hashlib import sha256
from itertools import product
from pathlib import Path
import json
import math
import numpy as np
import sympy as sp
from scipy.sparse import diags
from scipy.sparse.linalg import expm_multiply

HERE = Path(__file__).resolve().parent
BASE = HERE.parent


def identity(path):
    path = Path(path).resolve()
    data = path.read_bytes()
    return {"path": str(path), "bytes": len(data), "sha256": sha256(data).hexdigest()}


def verify(rows):
    for row in rows:
        assert identity(row["path"]) == row, row["path"]


def seals():
    pre_path = HERE / "PRE_COMPARISON_SEAL.json"
    assert identity(pre_path)["sha256"] == "d17725c9c6f2b1a973ea89791402c94b1ee87759164a9a551c38b7b499fcf0f6"
    pre = json.loads(pre_path.read_text())
    verify(pre["sources"] + pre["artifacts"])
    author_path = BASE / "WEAK_FIELD_WAVEPACKET_AUTHOR_SEAL.json"
    assert identity(author_path)["sha256"] == "d05a600d964abc3ae99ce80f1df6e710a33f1fb21415e830821957972a11eaf3"
    author = json.loads(author_path.read_text())
    rows = author["artifacts"]
    verify(rows)
    context = json.loads((BASE / "WEAK_FIELD_WAVEPACKET_SOURCE_CONTEXT.json").read_text())
    verify(context["dependencies"])
    result = json.loads((BASE / "WEAK_FIELD_WAVEPACKET_RESULTS.json").read_text())
    receipt = json.loads((BASE / "WEAK_FIELD_WAVEPACKET_CHECK_RECEIPT.json").read_text())
    verify([result["script"], receipt["source"], receipt["stdout"], receipt["stderr"]])
    assert receipt["exit_code"] == 0
    assert (BASE / "WEAK_FIELD_WAVEPACKET_CHECK.stderr").read_bytes() == b""
    assert (BASE / "WEAK_FIELD_WAVEPACKET_CHECK.stdout").read_bytes() == (BASE / "WEAK_FIELD_WAVEPACKET_RESULTS.json").read_bytes()
    return {
        "pre_seal": identity(pre_path), "pre_bindings": len(pre["sources"]) + len(pre["artifacts"]),
        "author_seal": identity(author_path), "author_bindings": len(rows),
        "additional_context_dependencies": context["dependencies"],
        "receipt_and_output_bindings_pass": True,
    }, result


def normalization():
    c, a, g, cs = sp.symbols("c a g C", positive=True)
    k = c*g**2/(2*a)
    j = c/(2*a*g**2)
    delta = c*g**6*cs**2/a
    hop = c*g**4*cs**sp.Rational(3, 2)/(sp.sqrt(2)*a)
    eps2 = 1/(2*g**4*cs)
    identities = {
        "sqrt_K_over_J_equals_g2": sp.simplify(sp.sqrt(k/j)-g**2),
        "sqrt_KJ_equals_c_over_2a": sp.simplify(sp.sqrt(k*j)-c/(2*a)),
        "epsilon_squared": sp.simplify((hop/delta)**2-eps2),
        "induced_electric_coefficient": sp.simplify(hop**2/(delta*cs)-k),
        "induced_plaquette_coefficient": sp.simplify(2*hop**4/delta**3-j),
        "loop_residual_ground": sp.Rational(105, 24**2),
        "loop_residual_first": sp.Rational(945, 24**2),
    }
    assert all(identities[key] == 0 for key in list(identities)[:5])
    return {key: str(value) for key, value in identities.items()}


def cubic_trace(author):
    out = []
    for row in author["cubic_cochains"]:
        n = row["side"]
        lambdas = [4*sum(math.sin(math.pi*k/n)**2 for k in mode)
                   for mode in product(range(n), repeat=3) if any(mode)]
        # Tr(C Cov(x) C*) = (1/2) Tr sqrt(C*C) = sum_{k!=0} sqrt(lambda(k)).
        # Translation and cubic symmetry make the 3V face variances equal.
        variance = sum(math.sqrt(x) for x in lambdas)/(3*n**3)
        quartic = math.sqrt(105)*(3*n**3)*variance**2/24
        assert max(abs(variance-x) for x in row["plaquette_vacuum_variance_range"]) < 5e-14
        assert abs(quartic-row["vacuum_potential_residual_bound_over_g2_at_c_over_a_one"]) < 2e-11
        out.append({"side": n, "face_variance_from_Fourier_trace": variance,
                    "quartic_bound_over_g2": quartic,
                    "author_difference": quartic-row["vacuum_potential_residual_bound_over_g2_at_c_over_a_one"]})
    values = [0, 1, 3, 4, 3, 1]
    histogram = Counter(sum(v) for v in product(values, repeat=3))
    exact_trace = sum(mult*sp.sqrt(lam) for lam, mult in histogram.items())
    exact_variance = sp.simplify(exact_trace/648)
    exact_bound = sp.simplify(sp.sqrt(105)*648*exact_variance**2/24)
    assert abs(float(exact_bound)-out[-1]["quartic_bound_over_g2"]) < 2e-11
    return {"rows": out,
            "side_six_exact_lambda_histogram": dict(sorted(histogram.items())),
            "side_six_exact_face_variance": str(exact_variance),
            "side_six_exact_quartic_bound": str(exact_bound),
            "printed_175_046_is_conservative_upward_decimal": float(exact_bound) < 175.046}


def selected_loop(author):
    g, duration, cutoff = 0.2, 1.0, 43
    grid = 16384
    theta = 2*np.pi*np.arange(grid)/grid
    # Explicit periodic sum.  The omitted images |j|>3 have Gaussian tails far
    # below double precision at g=.2.  This is a numerical control, not enclosure.
    samples = []
    for degree in (0, 1):
        y = sum((((theta+2*np.pi*j)/g)**degree)*np.exp(-((theta+2*np.pi*j)/g)**2/4)
                for j in range(-3, 4))
        coeff = np.fft.fft(y)/grid
        m = np.arange(-cutoff, cutoff+1)
        f = coeff[m % grid]
        f /= np.linalg.norm(f)
        samples.append(f)
    ground, first = samples
    assert abs(np.vdot(ground, first)) < 1e-12
    m = np.arange(-cutoff, cutoff+1)
    h = diags([-np.ones(2*cutoff)/(2*g*g), 2*g*g*m*m+1/(g*g),
               -np.ones(2*cutoff)/(2*g*g)], [-1, 0, 1], format="csr")
    initial = (ground+first)/math.sqrt(2)
    actual = expm_multiply(-1j*duration*h, initial)
    reference = (np.exp(-1j*duration)*ground+np.exp(-3j*duration)*first)/math.sqrt(2)
    error = float(np.linalg.norm(actual-reference))
    residuals = [float(np.linalg.norm(h@ground-ground)), float(np.linalg.norm(h@first-3*first))]
    target = next(x for x in author["compact_single_loop"] if x["g"] == g)
    recorded = next(x for x in target["dynamics"] if x["time"] == duration)
    discrepancy = error-recorded["state_norm_difference"]
    assert abs(discrepancy) < 3e-11
    assert max(abs(x-y) for x, y in zip(residuals, target["harmonic_packet_residual_norms"])) < 1e-11
    return {"g": g, "time": duration, "independent_cutoff": cutoff, "FFT_grid": grid,
            "method": "Real-space periodized Gaussian, FFT, sparse matrix exponential; no author function imported.",
            "state_error": error, "difference_from_author": discrepancy,
            "residuals": residuals, "unitarity_error": abs(float(np.linalg.norm(actual))-1),
            "approximation_limit": "Double precision periodic-image and electric cutoffs; not an infinite-matrix interval bound."}


def all_recorded_arithmetic(author):
    n_dynamics = 0
    for row in author["compact_single_loop"] + author["larger_cutoff"]:
        g = row["g"]
        for dynamic in row["dynamics"]:
            n_dynamics += 1
            assert abs(dynamic["norm_difference_over_g2"]-dynamic["state_norm_difference"]/g**2) < 1e-12
            expected = dynamic["time"]*sum(row["harmonic_packet_residual_norms"])/math.sqrt(2)
            assert abs(expected-dynamic["finite_matrix_duhamel_bound"]) < 1e-12
            assert dynamic["state_norm_difference"] <= expected+1e-10
    for small, large, diff in zip(author["compact_single_loop"], author["larger_cutoff"], author["cutoff_comparison"]):
        energy = max(abs(x-y) for x, y in zip(small["lowest_four_energies"], large["lowest_four_energies"]))
        dynamic = max(abs(x["state_norm_difference"]-y["state_norm_difference"])
                      for x, y in zip(small["dynamics"], large["dynamics"]))
        assert energy == diff["largest_energy_change"]
        assert dynamic == diff["largest_dynamical_error_change"]
    for row in author["continuum_dispersion"]:
        n = np.asarray(row["mode"], dtype=float)
        a = 2*np.pi/row["side"]
        freq = np.linalg.norm(2*np.sin(a*n/2))/a
        error = abs(freq-np.linalg.norm(n))
        bound = a*a*np.linalg.norm(n**3)/24
        assert abs(freq-row["lattice_frequency"]) < 1e-13
        assert abs(error-row["error"]) < 1e-13
        assert abs(bound-row["analytic_error_bound"]) < 1e-13
        assert error <= bound+1e-13
    return {"dynamics_rows_arithmetic_only": n_dynamics,
            "cutoff_pairs_arithmetic_only": len(author["cutoff_comparison"]),
            "continuum_rows_independent_formula": len(author["continuum_dispersion"]),
            "scope": "Recorded arithmetic authentication is not a rerun of the author diagonalizations."}


def main():
    authentication, author = seals()
    out = {"created_utc": datetime.now(timezone.utc).isoformat(), "status": "PASS",
           "runner": identity(__file__), "authentication": authentication,
           "exact_normalization": normalization(), "cubic_vacuum_trace": cubic_trace(author),
           "selected_loop": selected_loop(author), "recorded_arithmetic": all_recorded_arithmetic(author),
           "author_runner_executed": False,
           "new_external_literature_used": False,
           "failures": "None: first execution passed; no earlier attempt was suppressed."}
    data = json.dumps(out, indent=2)+"\n"
    target = HERE/"COMPARISON_RESULTS.json"
    assert not target.exists(), "Preserve existing output rather than overwrite."
    target.write_text(data)
    print(data, end="")


if __name__ == "__main__":
    main()
