"""Bounded post-seal checks; never imports or executes the author runners."""
from pathlib import Path
from hashlib import sha256
from datetime import datetime, timezone
import itertools
import json
import math
import numpy as np
import sympy as s

HERE = Path(__file__).resolve().parent
BASE = HERE.parent
AUTHOR_SEAL = "4b707760dab45089bda59645caadc1a3d7bdc6e9ee3cc730a3be5c48a29b3937"
PRE_SEAL = "6776ebe9567241e0d32f3ff16db4512cc9e78e0325eb0b766ce8b86886726570"


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


def read(path):
    return json.loads(path.read_text())


def bind(row):
    p = Path(row["path"])
    assert p.stat().st_size == row["bytes"], p
    assert digest(p) == row["sha256"], p
    return {"path": str(p), "bytes": row["bytes"], "sha256": row["sha256"]}


def authentication():
    author = BASE / "RK_COOLING_ADAPTATION_AUTHOR_SEAL.json"
    pre = HERE / "PRE_COMPARISON_SEAL.json"
    assert digest(author) == AUTHOR_SEAL
    assert digest(pre) == PRE_SEAL
    a, p = read(author), read(pre)
    aa = [bind(row) for row in a["artifacts"]]
    pp = [bind(row) for row in p["sources"] + p["artifacts"]]
    assert len(aa) == 20 and len(pp) == 39
    streams = []
    for stem, script in [
        ("RK_COOLING_HAMILTONIAN_CHANGE", "rk_cooling_hamiltonian_change_check.py"),
        ("CUBIC_RECORD_COOLING_STATIONARY", "cubic_record_cooling_stationary_screen.py"),
        ("LOCAL_WEIGHTED_RECORD_GROUND", "local_weighted_record_ground_screen.py"),
    ]:
        receipt = read(BASE / (stem + "_RUN_RECEIPT.json"))
        assert receipt["returncode"] == 0
        assert receipt["script_sha256"] == digest(BASE / script)
        assert receipt["command"][-1] == str(BASE / script)
        assert receipt["started_utc"] < receipt["completed_utc"]
        results = read(BASE / (stem + "_RESULTS.json"))
        assert results["status"] == "PASS"
        log = (BASE / (stem + "_RUN.log")).read_bytes()
        err = (BASE / (stem + "_RUN.stderr")).read_text()
        if stem == "CUBIC_RECORD_COOLING_STATIONARY":
            rows = [json.loads(line) for line in log.splitlines()]
            assert rows[0]["geometry"] == results["geometry"]
            assert rows[1:-1] == results["cases"]
            assert rows[-1] == {"finished": True, "runtime_seconds": results["runtime_seconds"]}
        else:
            assert log == (BASE / (stem + "_RESULTS.json")).read_bytes()
        if stem == "LOCAL_WEIGHTED_RECORD_GROUND":
            assert not err
        else:
            assert err.count("FutureWarning:") == 1
            assert "Input has data type int64" in err and "Traceback" not in err
        streams.append({"stem": stem, "receipt": "authenticated", "stderr_bytes": len(err.encode()),
                        "log_matches": "exact result bytes" if stem != "CUBIC_RECORD_COOLING_STATIONARY" else "all progress rows match corresponding complete result fields"})
    context = read(BASE / "RK_COOLING_ADAPTATION_SOURCE_CONTEXT.json")
    # No new literature or forbidden follow-up is opened. Two old, already-reviewed
    # direct dependencies are identity-checked; other context is metadata only.
    old = []
    for row in context["dependencies"][:2]:
        old.append(bind(row))
    return {"author_artifacts": aa, "preserved_pre_bindings": len(pp), "streams": streams,
            "reused_direct_dependencies": old,
            "external_context_limit": "Provenance statements read, not independently certified; no new external or later frontier source opened."}


def global_edge_target():
    # Deliberately not the author's geometry or its numerical ground vector.
    v = s.Matrix([1, 3, 2, 5, 4, 7, 6])
    dim = len(v)
    z = (v.T * v)[0]
    p = v * v.T / z
    edges = [(i, (i + 1) % dim) for i in range(dim)] + [(0, 3), (2, 5)]
    loss, m, dual = s.zeros(dim), s.zeros(dim), s.zeros(dim)
    for number, (a, b) in enumerate(edges, 1):
        va, vb = s.zeros(dim, 1), s.zeros(dim, 1)
        va[a], va[b] = v[a], v[b]
        vb[a], vb[b] = v[b], -v[a]
        w = v[a] ** 2 + v[b] ** 2
        jump = va * vb.T / w
        pm = jump.T * jump
        rate = s.Rational(number, 3)
        assert jump * v == s.zeros(dim, 1)
        assert jump * jump == s.zeros(dim)
        assert pm * pm == pm
        assert jump.T * p * jump == w / z * pm
        loss += rate * pm
        m += rate * w / z * pm
        dual += rate * (jump.T * p * jump - (pm * p + p * pm) / 2)
    assert dual == m and m * v == s.zeros(dim, 1)
    assert m.rank() == dim - 1 and loss.rank() == dim - 1
    mu = np.linalg.eigvalsh(np.array(m).astype(float))[1]
    loss_norm = np.linalg.eigvalsh(np.array(loss).astype(float))[-1]
    return {"dimension": dim, "edges": edges, "unnormalized_positive_target": list(map(int, v)),
            "normalization_squared": int(z), "dual_fidelity_identity": "exact",
            "M_and_loss_rank_exact": dim - 1, "mu_numeric": float(mu),
            "loss_operator_norm_numeric": float(loss_norm),
            "claim": "Checks the additional author global-edge construction; no local implementation inferred."}


def support_counts():
    rows = []
    for side in (2, 3, 4):
        sites = list(itertools.product(range(side), repeat=3))

        def shift(x, direction):
            return tuple((x[k] + (k == direction)) % side for k in range(3))

        faces = []
        for x in sites:
            for i, j in itertools.combinations(range(3), 2):
                faces.append(frozenset([(x, i), (shift(x, i), j), (shift(x, j), i), (x, j)]))
        face = faces[0]
        neighborhood = [f for f in faces if f & face]
        footprint = set().union(*neighborhood)
        rows.append({"side": side, "overlap": len(neighborhood), "links": len(footprint)})
    assert rows == [{"side": 2, "overlap": 11, "links": 20},
                    {"side": 3, "overlap": 13, "links": 30},
                    {"side": 4, "overlap": 13, "links": 32}]
    r, z = s.symbols("r z", positive=True)
    # Normalizations cancel: pair vector (1,r*z), where z=exp(t*Delta).
    jump = s.Matrix([[r, -1], [r*r, -r]]) / (1+r*r)
    vv = s.Matrix([1, r*z])
    g = r*(1-z)/(1+r*r*z)
    assert (jump.T*jump*vv - g*jump.T*vv).applyfunc(s.cancel) == s.zeros(2, 1)
    swap = s.Matrix([[0, 1], [1, 0]])
    reverse = swap * jump.subs(r, 1/r) * swap
    assert (reverse+jump).applyfunc(s.cancel) == s.zeros(2)
    return {"independent_link_footprints": rows, "weighted_exponential_vector_identity": "exact",
            "reversing_pair_orientation_changes_L_by_minus_sign": "exact",
            "all_volume_bound": "At most 12 other overlapping plaquettes and at most 4+12*3=40 links; not a range-zero compiler."}


def gaussian_rows():
    source = read(BASE / "RK_COOLING_HAMILTONIAN_CHANGE_RESULTS.json")["numeric_gaussian"]
    out = []
    for row in source["mismatched_bath"]:
        k, w, u, gam, ss = [row[key] for key in ("K", "W", "U", "gamma", "s")]
        a, b, r, nu = k*ss, u+w*ss, math.sqrt(k/w), gam*ss
        mismatch, denominator = a/r-b*r, nu*nu+4*a*b
        cov = np.array([[r/2+a*mismatch/denominator, nu*mismatch/(2*denominator)],
                        [nu*mismatch/(2*denominator), 1/(2*r)-b*mismatch/denominator]])
        assert np.max(np.abs(cov-np.array(row["exact_covariance"]))) < 1e-13
        energy = (a/r+b*r)/4
        jump = nu*mismatch*mismatch/(2*denominator)
        assert abs(energy-row["exact_energy"]) < 1e-13
        assert abs(jump-row["exact_jump_rate"]) < 1e-13
        for cut in row["Fock_controls"]:
            err = float(np.max(np.abs(cov-np.array(cut["covariance"]))))
            assert abs(err-cut["covariance_max_error"]) < 1e-13
        out.append({"s": ss, "K": k, "W": w, "U": u, "gamma": gam,
                    "exact_formula_comparison": "agrees", "final_Fock_covariance_error": row["Fock_controls"][-1]["covariance_max_error"]})
    return {"rows": out, "coverage": "Independent algebraic reduction of all five reported parameter rows; no repeat of Fock stationary solves."}


def variational_comparison():
    own = read(HERE / "VARIATIONAL_RESULTS.json")
    author = read(BASE / "LOCAL_WEIGHTED_RECORD_GROUND_RESULTS.json")["finite_variational"]
    cube = read(BASE / "CUBIC_RECORD_COOLING_STATIONARY_RESULTS.json")
    cert = read(BASE / "LOCAL_WEIGHTED_GROUND_OPTIMUM_CERTIFICATE.json")
    assert cert["source_results_sha256"] == digest(BASE / "LOCAL_WEIGHTED_RECORD_GROUND_RESULTS.json")
    assert author["component_states_sha256"] == cube["geometry"]["states_sha256"]
    hist = {int(k): v for k, v in own["flippability_histogram"].items()}
    edges = {int(k): v for k, v in own["edge_endpoint_flippability_sum_histogram"].items()}
    assert hist == {int(k): v for k, v in author["flippability_counts"].items()}
    assert edges == {2*int(k): v for k, v in author["edge_middegree_counts"].items()}
    x = s.Symbol("x")
    z = sum(count*x**d for d, count in hist.items())
    rows = []
    for row, certificate in zip(author["cases"], cert["cases"]):
        delta = s.Rational(row["delta"])
        numerator = (1-delta)*sum(d*count*x**d for d, count in hist.items()) - 2*sum(count*x**(total//2) for total, count in edges.items())
        assert s.expand(z-s.sympify(row["normalization_polynomial"])) == 0
        assert s.expand(numerator-s.sympify(row["energy_numerator_polynomial"])) == 0
        raw = s.Poly(s.diff(numerator,x)*z-numerator*s.diff(z,x),x)
        terms = raw.terms()
        low_power = min(monomial[0] for monomial, _ in terms)
        primitive = s.Poly(raw.as_expr()/x**low_power,x).primitive()[1]
        supplied = s.Poly(s.sympify(row["critical_polynomial_without_zero_root"]), x)
        assert primitive.monic() == supplied.monic()
        count = primitive.count_roots(0, s.oo)
        assert count == certificate["positive_critical_roots_exact"] == 1
        assert s.sign(primitive.TC()) == -1 and s.sign(primitive.LC()) == 1
        assert s.limit(numerator/z,x,0) == s.Rational(row["endpoint_energies"]["x_to_zero"])
        assert s.limit(numerator/z,x,s.oo) == s.Rational(row["endpoint_energies"]["x_to_infinity"])
        interval = row["all_positive_critical_root_intervals"][0]
        lo, hi = s.Rational(interval["lower"]), s.Rational(interval["upper"])
        assert primitive.count_roots(lo,hi) == 1
        midpoint = (lo+hi)/2
        assert abs(float(midpoint)-row["x_optimum"]) < 1e-14
        assert abs(math.log(float(midpoint))-row["theta_optimum"]) < 1e-14
        assert abs(float((numerator/z).subs(x,midpoint))-row["variational_energy"]) < 1e-12
        gapbound = (row["variational_energy"]-row["ground_energy"])/row["finite_ground_gap"]
        assert abs(gapbound-row["energy_gap_infidelity_upper_bound"]) < 1e-13
        assert abs(2*math.sqrt(gapbound)-row["all_later_time_trace_error_upper_bound"]) < 1e-13
        c = next(case for case in cube["cases"] if abs(case["delta"]-float(delta)) < 1e-14)
        assert row["ground_energy"] == c["ground_energy"]
        assert row["finite_ground_gap"] == c["ground_gap_within_component"]
        assert row["ground_infidelity"] <= gapbound
        n, m, var = 864, 24, s.Rational(16,3)
        bound = float(delta**2*var/((n-1)**2*(2*m*(3+abs(delta)))**2))
        assert abs(bound-c["conservative_analytic_intensity_lower_bound"]) < 1e-22
        assert c["stationary_jump_intensity"] >= bound
        rows.append({"delta": str(delta), "exact_positive_critical_count": int(count),
                     "theta": row["theta_optimum"], "energy": row["variational_energy"],
                     "gap_bound_from_reported_finite_spectrum": gapbound})
        if delta == s.Rational(1,5):
            assert abs(row["theta_optimum"]-own["optimum_theta_numeric"]) < 1e-12
            assert abs(row["variational_energy"]-own["optimum_energy_numeric"]) < 1e-12
            assert abs(row["ground_infidelity"]-(1-own["variational_fidelity_numeric"])) < 1e-12
            assert float(s.Rational(own["ground_energy_exact_rational_lower"])) <= row["ground_energy"] <= float(s.Rational(own["ground_energy_exact_rational_upper"]))
    return {"rows": rows, "independent_delta_one_fifth_matches": True,
            "coverage": "All four exact energy/critical polynomials reconstructed from sealed independent census, exact root counts and reported numerical consequences checked. Only delta=1/5 has the prior independent full spectral calculation and rational ground-energy enclosure; no full author stationary solve replay."}


def main():
    out = {"created_utc": datetime.now(timezone.utc).isoformat(), "script_sha256": digest(Path(__file__)),
           "authentication": authentication(), "global_edge_target": global_edge_target(),
           "weighted_and_local_support": support_counts(), "gaussian": gaussian_rows(),
           "variational": variational_comparison(),
           "finding_F1": {"source": "ADAPTING_RECORD_COOLING_AWAY_FROM_THE_RK_POINT.md:37",
                          "needed_qualification": "delta != 0, in addition to nonconstant d(c)",
                          "prior_zero_delta_countercontrol": read(HERE/"FINITE_COOLER_RESULTS.json")["detuned"]["zero_delta_original_target_stationary"]},
           "status": "Bounded comparison controls completed; one prose scope repair identified."}
    text = json.dumps(out, indent=2)+"\n"
    (HERE/"COMPARISON_RESULTS.json").write_text(text)
    print(text, end="")


if __name__ == "__main__":
    main()
