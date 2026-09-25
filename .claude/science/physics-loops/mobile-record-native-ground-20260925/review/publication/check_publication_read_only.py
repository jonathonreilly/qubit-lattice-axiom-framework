"""Read-only bounded correspondence check: reads inputs and prints JSON only.

No author/scientific module is imported or executed; no files are created,
modified, chmodded, or removed. The separate run_logged.py owns new local logs.
This verifies stored payloads and exact certificates, not new primitive runs.
"""
import ast
from collections import Counter
import difflib
from fractions import Fraction
import hashlib
from itertools import product
import json
import math
from pathlib import Path
import re

HERE = Path(__file__).resolve().parent
BASE = HERE.parent.parent
SRC = HERE / "sources"
PUB = SRC / "native-ground-publication"
SHA = lambda x: hashlib.sha256(x).hexdigest()
read = lambda p: json.loads(p.read_text())
inv = read(HERE / "SOURCE_INVENTORY.json")
manifest = read(SRC / "NATIVE_GROUND_PUBLICATION_FROZEN_SOURCES.json")
assert SHA((SRC / "NATIVE_GROUND_PUBLICATION_FROZEN_SOURCES.json").read_bytes()) == "d0460afcbbcf15a646e655d44888069bde0648552797e5af3b043c7651846b6f"
for row in inv["sources"]:
    local, live = HERE / row["copy"], Path(row["origin"])
    assert local.read_bytes() == live.read_bytes()
    assert SHA(local.read_bytes()) == row["sha256"] and local.stat().st_size == row["bytes"]
for seal in inv["prior_seals"]:
    assert SHA(Path(seal["origin"]).read_bytes()) == seal["sha256"]
    for m in seal["members"]:
        body = Path(m["path"]).read_bytes()
        assert SHA(body) == m["sha256"] and len(body) == m["bytes"]
for rel, sha in manifest["files_sha256"].items():
    assert SHA((PUB / rel).read_bytes()) == sha

# All mathematical source words are compared after only heading demotion. The
# small remaining diffs are emitted in full for human scientific review.
note = (PUB / manifest["note"]).read_text()
parts = ["## Part I —", "## Part II —", "## Part III —", "## Verification and physical boundary"]
note_diffs = []
for i, item in enumerate(manifest["source_notes"]):
    origin = SRC / Path(item["origin"]).relative_to(BASE)
    assert SHA(origin.read_bytes()) == item["sha256"]
    demoted = re.sub(r"^(#{1,5}) ", lambda m: "##" + m[1] + " ", origin.read_text(), flags=re.M)
    start = note.index("\n", note.index(parts[i])) + 1
    end = note.index(parts[i+1])
    section = note[start:end].strip()
    diff = "".join(difflib.unified_diff(demoted.strip().splitlines(True), section.splitlines(True),
                                      fromfile=item["unit"] + "/sealed_author_heading_demoted",
                                      tofile=item["unit"] + "/publication", n=4))
    note_diffs.append({"part": item["unit"], "source_sha256": item["sha256"],
                       "publication_section_sha256": SHA(section.encode()), "full_diff": diff})

# Exact copies include the imported helper bodies. Parse as data, never import.
runtime = []
for row in manifest["origins"]:
    original = SRC / Path(row["origin"]).relative_to(BASE)
    public = PUB / row["publication"]
    assert original.read_bytes() == public.read_bytes()
    assert SHA(public.read_bytes()) == row["sha256"]
    imports = []
    for node in ast.walk(ast.parse(public.read_text())):
        if isinstance(node, ast.ImportFrom):
            imports.append({"module": node.module, "names": [x.name for x in node.names]})
    runtime.append({"source": row["publication"], "sha256": row["sha256"], "imports": imports})
local_imports = {Path(x["source"]).name: {n["module"]: n["names"] for n in x["imports"]} for x in runtime}
assert local_imports["native_pair_local_row_certificate.py"]["native_pair_controls"] == ["local_delta_row"]
assert local_imports["native_pair_row_polynomial_certificate.py"]["native_pair_local_row_certificate"] == ["neighbors", "overlapping_pairs_near"]

out = PUB / manifest["output_directory"]
original_artifacts = {
    "pair_NATIVE_PAIR_RESULTS.json": "native-one-pair-spectrum-personal/NATIVE_PAIR_RESULTS.json",
    "pair_LOCAL_ROW_CERTIFICATE.json": "native-one-pair-spectrum-personal/LOCAL_ROW_CERTIFICATE.json",
    "pair_ROW_POLYNOMIAL_CERTIFICATE.json": "native-one-pair-spectrum-personal/ROW_POLYNOMIAL_CERTIFICATE.json",
    "filling_GROUND_FILLING_CERTIFICATES.json": "native-ground-filling-personal/GROUND_FILLING_CERTIFICATES.json",
    "activity_PRIMITIVE_RATE_ENERGY_RESULTS.json": "ground-formation-incompatibility-personal/PRIMITIVE_RATE_ENERGY_RESULTS.json",
}
all_counts, differences, artifact_rows = Counter(), [], []
def compare(old, new, path, counts):
    assert type(old) is type(new), (path, type(old), type(new))
    if isinstance(old, dict):
        assert list(old) == list(new), path
        for key in old:
            compare(old[key], new[key], path + "/" + key, counts)
    elif isinstance(old, list):
        assert len(old) == len(new), path
        for i, (a, b) in enumerate(zip(old, new)):
            compare(a, b, path + "/" + str(i), counts)
    else:
        counts[type(old).__name__] += 1
        if old != new:
            differences.append({"path": path, "original": old, "fresh": new})

for name, original in original_artifacts.items():
    counts = Counter()
    compare(read(SRC / original), read(out / name), name, counts)
    all_counts.update(counts)
    artifact_rows.append({"name": name, "original": original, "original_sha256": SHA((SRC / original).read_bytes()),
                          "fresh_sha256": SHA((out / name).read_bytes()), "fresh_bytes": (out / name).stat().st_size,
                          "all_leaf_counts": dict(counts)})
expected_paths = {x + "/elapsed_seconds" for x in original_artifacts if "ROW_POLYNOMIAL" not in x}
expected_paths |= {"pair_ROW_POLYNOMIAL_CERTIFICATE.json/prior_row_certificate_sha256",
                   "pair_NATIVE_PAIR_RESULTS.json/quotients/2/floating_top_delta_eigenvalue",
                   "pair_NATIVE_PAIR_RESULTS.json/quotients/2/floating_eigen_residual"}
assert len(differences) == 7 and {x["path"] for x in differences} == expected_paths
float_changes = []
for d in differences:
    if "/floating_" in d["path"]:
        delta = abs(d["fresh"] - d["original"])
        ulps = delta / math.ulp(d["original"])
        if d["path"].endswith("floating_top_delta_eigenvalue"):
            assert ulps == 1
        else:
            assert delta < 4e-14 and 0 <= d["fresh"] < 1e-10 and 0 <= d["original"] < 1e-10
        float_changes.append(dict(d, absolute_difference=delta, ulps=ulps))

pair = read(out / "pair_NATIVE_PAIR_RESULTS.json")
local = read(out / "pair_LOCAL_ROW_CERTIFICATE.json")
poly = read(out / "pair_ROW_POLYNOMIAL_CERTIFICATE.json")
filling = read(out / "filling_GROUND_FILLING_CERTIFICATES.json")
activity = read(out / "activity_PRIMITIVE_RATE_ENERGY_RESULTS.json")

# Re-evaluate integer/rational Perron certificates; floating eigenpairs are not
# used to certify an edge, even in the two changed L6 diagnostics.
certificates = []
for q in pair["quotients"]:
    rows = [dict(row) for row in q["delta_Q_rows"]]
    n = q["translation_orbits"]
    assert len(rows) == n == len(q["positive_integer_test_vector"]) == len(q["orbit_weights"])
    v, w, shift = q["positive_integer_test_vector"], q["orbit_weights"], q["nonnegative_shift"]
    assert all(type(x) is int and x > 0 for x in v + w)
    for i, row in enumerate(rows):
        assert len(row) == len(q["delta_Q_rows"][i])
        for j, x in row.items():
            assert type(j) is int and 0 <= j < n and type(x) is int
            assert x + (shift if i == j else 0) >= 0
            assert w[i] * x == w[j] * rows[j].get(i, 0)
        assert row.get(i, 0) + shift >= 0
    ratios = [Fraction(sum(x*v[j] for j, x in row.items()), v[i]) for i, row in enumerate(rows)]
    lower, upper = min(ratios), max(ratios)
    for field, bounds in [("exact_delta_Q_Perron_interval", (lower, upper)),
                          ("proposed_ground_gap_g2_tau_interval", (-upper/4, -lower/4))]:
        for label, value in zip(("lower", "upper"), bounds):
            stored = q[field][label]
            assert value == Fraction(stored["numerator"], stored["denominator"])
            assert float(value) == stored["float_diagnostic"]
    assert float(lower) <= q["floating_top_delta_eigenvalue"] <= float(upper) or q["side"] == 2
    certificates.append({"side": q["side"], "matrix_dimension": n,
                         "serialized_nonzero_entries": sum(len(x) for x in rows),
                         "delta_interval": [str(lower), str(upper)],
                         "g2_tau_gap_interval": [str(-upper/4), str(-lower/4)]})
cube = pair["full_colored_cube"]
for field, n in [("full_positive_Q", 36), ("occupancy_positive_Q", 6)]:
    matrix = cube[field]
    assert len(matrix) == n and all(len(row) == n for row in matrix)
    assert all(type(x) is int and x >= 0 for row in matrix for x in row)
    assert all(matrix[i][j] == matrix[j][i] for i in range(n) for j in range(n))
    assert {sum(row) for row in matrix} == {98}
assert cube["vacuum_flat_H4"] == -108 and cube["exact_flat_H4_ground_difference"] == 10
# The serialized full-cube basis groups six charge positions for each of six
# occupations. This checks the stated constant-color intertwiner algebraically.
assert all(sum(cube["full_positive_Q"][i][6*j+k] for k in range(6)) == cube["occupancy_positive_Q"][i//6][j]
           for i in range(36) for j in range(6))

# Full stored local row/case tables, checked by arithmetic rather than executing
# their primitive-enumeration builders. Geometry was independently checked in
# sealed PRE/POST; exact artifact correspondence carries those checks forward.
def pair_gram_row(z, r, sa, sc, t):
    na, nc, ni = z-sa, z-sc, r-t
    return (na*nc-ni)*((sa+1)*(sc+1)-t) + sa*ni*(nc-1) + sc*ni*(na-1) + ni*(ni-1)

assert len(poly["synthetic"]["distinct_parameter_rows"]) == 36
for z, r, sa, sc, t, delta in poly["synthetic"]["distinct_parameter_rows"]:
    assert delta == 2*(pair_gram_row(z, r, sa, sc, t) - (z*z+r*r-2*r))
single_total = 0
for row in poly["single_occupied_B_contributions"]:
    delta = 2*(pair_gram_row(6, row["r"], row["sa"], row["sc"], row["t"]) - (36+row["r"]**2-2*row["r"]))
    assert delta == row["row_contribution"]
    single_total += row["count"] * delta
assert single_total == 6048
polys_by_type = {}
for row in poly["two_occupied_B_interactions"]:
    correction = sum(x["interaction_per_pair"]*x["pairs"] for x in row["interaction_counts"])
    assert correction == row["interaction_row_correction"]
    assert sum(x["pairs"] for x in row["interaction_counts"]) == row["common_active_pairs"]
    assert row["full_row_sum"] == 2*single_total+correction
    polys_by_type[tuple(sorted(map(abs, row["displacement"])))] = row
expected_displacements = {d for d in product(range(-4, 5), repeat=3) if 0 < sum(map(abs, d)) <= 4 and sum(d) % 2 == 0}
assert len(local["near_rows"]) == len(expected_displacements) == 84
assert {tuple(x["displacement"]) for x in local["near_rows"]} == expected_displacements
groups = Counter()
for row in local["near_rows"]:
    typ = tuple(sorted(map(abs, row["displacement"])))
    poly_row = polys_by_type[typ]
    assert row["row_sum"] == poly_row["full_row_sum"]
    assert row["common_active_pairs"] == poly_row["common_active_pairs"]
    assert row["maximum_active_vertex_distance_from_nearer_input"] <= 4
    groups[typ] += 1
for group in local["cubic_symmetry_groups"]:
    typ = tuple(group["absolute_coordinate_type"])
    assert groups[typ] == group["displacements"]
    assert group["exact_row_sum"] == polys_by_type[typ]["full_row_sum"]
for row in local["far_controls"]:
    assert row["row_sum"] == 12096 and row["common_active_pairs"] == 0
    assert row["maximum_active_vertex_distance_from_nearer_input"] <= 4
all_sums = [x["row_sum"] for x in local["near_rows"] + local["far_controls"]]
assert min(all_sums) == local["min_delta_Q_row_sum"] == 11512
assert max(all_sums) == local["max_delta_Q_row_sum"] == 12248
assert local["proposed_all_L_at_least_10_g2_tau_gap_interval"] == [-3062.0, -2878.0]

choose = lambda n, k: math.comb(n, k) if 0 <= k <= n else 0
patterns_checked = 0
for table in filling["local_certificates"]:
    r = table["overlap"]
    v, a, d = (table["local_counts"][k] for k in ("v", "a", "d"))
    assert v == 36+r*r-2*r
    seen = set()
    by_ell = Counter()
    for row in table["pattern_rows"]:
        t, sa, sc = (row[k] for k in ("t", "sa", "sc"))
        assert (t, sa, sc) not in seen
        seen.add((t, sa, sc))
        value, ell, holes = row["row"], sa+sc-t, 12-r-(sa+sc-t)
        assert value == pair_gram_row(6, r, sa, sc, t)
        assert (row["occupied"], row["vacant"]) == (ell, holes)
        multiplicity = choose(r, t)*choose(6-r, sa-t)*choose(6-r, sc-t)
        assert multiplicity == row["multiplicity"] > 0
        assert value <= v+(40 if r == 1 else 44)*ell
        assert value <= (Fraction(28) if r == 1 else Fraction(104, 3))*holes
        assert row["increment_per_occupied"] == (str(Fraction(value-v, ell)) if ell else None)
        assert row["row_per_vacant"] == (str(Fraction(value, holes)) if holes else None)
        by_ell[ell] += multiplicity*value
        patterns_checked += 1
    assert seen == {(t, t+x, t+y) for t in range(r+1) for x in range(7-r) for y in range(7-r)}
    assert sum(x["multiplicity"] for x in table["pattern_rows"]) == table["complete_subsets_checked"]
    for row in table["all_m_average_rows"]:
        n, m = row["global_B_sites"], row["occupied"]
        numerator = sum(value*choose(n-(12-r), m-ell) for ell, value in by_ell.items())
        assert numerator == v*choose(n-2, m)+a*choose(n-3, m-1)+d*choose(n-4, m-2)
        assert Fraction(numerator, choose(n, m)) == Fraction(row["uniform_Rayleigh"])
assert patterns_checked == 147
for torus in filling["torus_certificates"]:
    n = torus["B_sites"]
    assert n == torus["side"]**3//2
    assert torus["overlapping_pair_counts"] == {"1": 3*n, "2": 6*n}
    assert torus["every_B_union_incidence"] == {"overlap_1": 33, "overlap_2": 60}
    half = Fraction(1905, 2) + Fraction(378, n-1) + Fraction(414*(2*n-3), (n-1)*(n-3))
    assert half == Fraction(torus["half_filling_Rayleigh_per_n"]) > Fraction(1905, 2)
    assert half-Fraction(1905, 2) == Fraction(torus["half_filling_excess_above_1905_over_2"])
    for row in torus["selected_occupancies"]:
        m = row["occupied_B"]
        value = Fraction(321*choose(n-2, m)+3666*choose(n-3, m-1)+6624*choose(n-4, m-2), choose(n, m))
        assert value == Fraction(row["Rayleigh_per_n"])
        assert row["two_row_upper_bounds_per_n"] == [str(Fraction(321*n+3960*m, n)), str(Fraction(3004*(n-m), n))]
assert (Fraction(1905, 2)-321)/3960 == Fraction(421, 2640)
assert 1-Fraction(1905, 2)/3004 == Fraction(4103, 6008)

affine_entries = 0
for col in activity["columns"]:
    words = col["complete_affine_columns"]
    assert SHA(json.dumps(words, separators=(",", ":")).encode()) == col["complete_affine_columns_sha256"]
    counts = Counter()
    ratios = []
    diagonal = None
    seen = set()
    for charges, flux, gamma, q in words:
        key = (tuple(map(tuple, charges)), tuple(map(tuple, flux)))
        assert key not in seen
        seen.add(key)
        assert type(gamma) is int and type(q) is int and gamma >= 0 and q >= 0
        assert (col["degree_B"]-1)*gamma <= 8*q
        counts["gamma_nonzero"] += gamma != 0
        counts["q_nonzero"] += q != 0
        if not charges and not flux:
            diagonal = (gamma, q)
        elif gamma:
            ratios.append(Fraction(gamma, q))
        affine_entries += 1
    if diagonal is None:
        diagonal = (0, 0)
    assert diagonal == (col["Gamma_diagonal"], col["Q_diagonal"])
    assert counts["gamma_nonzero"] == col["Gamma_nonzero_entries"]
    assert counts["q_nonzero"] == col["Q_nonzero_entries"]
    assert (str(max(ratios)) if ratios else None) == col["maximum_offdiagonal_Gamma_over_Q"]
assert len(activity["columns"]) == 72 and affine_entries == 43970

# Fresh artifact/source/helper and full stdout bindings.
source_by_program = {Path(x["publication"]).name: x["sha256"] for x in manifest["origins"]}
for name, program in [("pair_NATIVE_PAIR_RESULTS.json", "native_pair_controls.py"),
                      ("pair_LOCAL_ROW_CERTIFICATE.json", "native_pair_local_row_certificate.py"),
                      ("pair_ROW_POLYNOMIAL_CERTIFICATE.json", "native_pair_row_polynomial_certificate.py"),
                      ("filling_GROUND_FILLING_CERTIFICATES.json", "ground_filling_certificates.py"),
                      ("activity_PRIMITIVE_RATE_ENERGY_RESULTS.json", "primitive_rate_energy_controls.py")]:
    assert read(out / name)["source_sha256"] == source_by_program[program]
assert local["helper_sha256"] == source_by_program["native_pair_controls.py"]
assert poly["topology_helper_sha256"] == source_by_program["native_pair_local_row_certificate.py"]
assert poly["prior_row_certificate_sha256"] == SHA((out / "pair_LOCAL_ROW_CERTIFICATE.json").read_bytes())
assert read(SRC / original_artifacts["pair_ROW_POLYNOMIAL_CERTIFICATE.json"])["prior_row_certificate_sha256"] == SHA((SRC / original_artifacts["pair_LOCAL_ROW_CERTIFICATE.json"]).read_bytes())
for name in ["filling_GROUND_FILLING_CERTIFICATES.json", "pair_ROW_POLYNOMIAL_CERTIFICATE.json"]:
    stdout_name = "filling_ground_filling_certificates.stdout.txt" if name.startswith("filling") else "pair_native_pair_row_polynomial_certificate.stdout.txt"
    assert (out / name).read_bytes() == (out / stdout_name).read_bytes()
pair_stdout = [json.loads(line) for line in (out / "pair_native_pair_controls.stdout.txt").read_text().splitlines()]
assert len(pair_stdout) == 5
for row, stdout in zip(pair["quotients"], pair_stdout[:-1]):
    assert stdout == {k: row[k] for k in ["side", "vacuum_flat_H4", "translation_orbits", "proposed_ground_gap_g2_tau_interval", "floating_eigen_residual"]}
assert pair_stdout[-1] == {"result": "NATIVE_PAIR_RESULTS.json", "sha256": SHA((out / "pair_NATIVE_PAIR_RESULTS.json").read_bytes()), "elapsed_seconds": pair["elapsed_seconds"]}
assert read(out / "pair_native_pair_local_row_certificate.stdout.txt") == {k: local[k] for k in ["cubic_symmetry_groups", "far_controls", "min_delta_Q_row_sum", "max_delta_Q_row_sum", "proposed_all_L_at_least_10_g2_tau_gap_interval", "elapsed_seconds"]}
activity_stdout = {k: v for k, v in activity.items() if k != "columns"}
activity_stdout["rows"] = [{k: v for k, v in col.items() if k not in ["initial_charge_word", "one_exact_Gauss_flow", "complete_affine_columns"]} for col in activity["columns"]]
activity_stdout["complete_result_sha256"] = SHA((out / "activity_PRIMITIVE_RATE_ENERGY_RESULTS.json").read_bytes())
assert read(out / "activity_primitive_rate_energy_controls.stdout.txt") == activity_stdout

result = read(PUB / manifest["result"])
runner_body = (PUB / manifest["runner"]).read_bytes()
assert result["source_sha256"] == SHA(runner_body)
assert result["all_assertions_passed"] is True and len(result["stages"]) == 5
assert [x["program"] for x in result["stages"]] == manifest["runtime"]
for stage in result["stages"]:
    p = Path(stage["program"])
    stdout = (out / f"{p.parent.name}_{p.stem}.stdout.txt").read_bytes()
    stderr = (out / f"{p.parent.name}_{p.stem}.stderr.txt").read_bytes()
    assert stage["source_sha256"] == SHA((PUB / p).read_bytes())
    assert len(stdout) == stage["stdout_bytes"] and SHA(stdout) == stage["stdout_sha256"]
    assert len(stderr) == stage["stderr_bytes"] == stage["exit_code"] == 0
assert {Path(x["path"]).name for x in result["complete_scientific_artifacts"]} == set(original_artifacts)
for item in result["complete_scientific_artifacts"]:
    body = (PUB / item["path"]).read_bytes()
    assert len(body) == item["bytes"] and SHA(body) == item["sha256"]

# Independent reconstruction of the v1 content fingerprint and exact cache
# serialization, from the read implementation, without importing runner_cache.
def literal_assignment(body, name):
    matches = []
    for node in ast.parse(body).body:
        if isinstance(node, ast.Assign) and any(isinstance(t, ast.Name) and t.id == name for t in node.targets):
            matches.append(ast.literal_eval(node.value))
    assert len(matches) == 1
    return matches[0]
declared = literal_assignment(runner_body, "AUDIT_INPUT_PATHS")
assert list(declared) == [manifest["note"], *manifest["parent_paths"], *manifest["runtime"]]
assert len(declared) == len(set(declared)) == 9
digest = hashlib.sha256(b"runner-cache-input-fingerprint-v1\0")
for rel in declared:
    assert not Path(rel).is_absolute() and ".." not in Path(rel).parts and Path(rel).as_posix() == rel
    live = BASE / "native-ground-publication" / rel
    assert not live.is_symlink()
    assert all(not parent.is_symlink() for parent in live.parents if parent != BASE)
    p, body = rel.encode(), (PUB / rel).read_bytes()
    digest.update(len(p).to_bytes(8, "big")); digest.update(p)
    digest.update(len(body).to_bytes(8, "big")); digest.update(body)
fingerprint = digest.hexdigest()
assert fingerprint == "8da2fa65a2e3e4a69323a9c33164a527964bee81b95407bb3cfa2c072c05f705"
execution = read(SRC / "NATIVE_GROUND_PUBLICATION_CACHE_EXECUTION.json")
assert execution["runner"] == manifest["runner"] and execution["status"] == "ok"
assert execution["exit_code"] == 0 and execution["stderr"] == "" and execution["timeout_sec"] == 120
assert execution["stdout"] == (PUB / manifest["result"]).read_text() + "TOTAL_PASS: 5\n"
prefix = literal_assignment((PUB / "scripts/runner_cache.py").read_bytes(), "CACHE_HEADER_PREFIX")
cache = (f"{prefix}\nrunner: {manifest['runner']}\nrunner_sha256: {SHA(runner_body)}\n"
         f"input_fingerprint_sha256: {fingerprint}\ntimeout_sec: {execution['timeout_sec']}\n"
         f"exit_code: {execution['exit_code']}\nelapsed_sec: {execution['elapsed_sec']:.2f}\nstatus: {execution['status']}\n"
         f"----- stdout -----\n{execution['stdout'][-200000:]}\n----- stderr -----\n{execution['stderr'][-50000:]}\n")
assert cache.encode() == (PUB / manifest["cache"]).read_bytes()

failure1 = read(SRC / "NATIVE_GROUND_PRIMARY_VERIFICATION_ATTEMPT01_FAILURE.json")
assert {x["path"]: (x["original"], x["fresh"]) for x in failure1["all_differences"]} == {x["path"]: (x["original"], x["fresh"]) for x in differences}
failure2 = read(SRC / "NATIVE_GROUND_PRIMARY_VERIFICATION_ATTEMPT02_FAILURE.json")
for item in failure2["preserved_files"]:
    assert SHA((SRC / Path(item["path"]).relative_to(BASE)).read_bytes()) == item["sha256"]
# Compare independently computed results to root bookkeeping only after they
# have been established, rather than using its conclusions as authority.
root = read(SRC / "NATIVE_GROUND_PRIMARY_ROOT_VERIFICATION.json")
assert root["all_payload_leaf_counts"] == dict(all_counts)
assert root["input_fingerprint_sha256"] == fingerprint
assert {x["path"]: (x["original"], x["fresh"]) for x in root["all_differences"]} == {x["path"]: (x["original"], x["fresh"]) for x in differences}

report = {
    "scope": "Released-source correspondence and stored-certificate arithmetic; no primitive/eigensolver rerun, no source imports, no filesystem writes by this checker.",
    "frozen_sources_and_live_origins_checked": len(inv["sources"]),
    "prior_seals_checked": [{"origin": s["origin"], "sha256": s["sha256"], "members": s["verified_member_count"]} for s in inv["prior_seals"]],
    "publication_manifest_files": len(manifest["files_sha256"]),
    "full_note_source_differences": note_diffs,
    "runtime_exact_reuse_and_imports": runtime,
    "complete_artifacts": artifact_rows, "all_payload_leaf_counts": dict(all_counts),
    "all_differences": differences, "floating_diagnostic_differences": float_changes,
    "exact_quotient_certificates": certificates,
    "cube_exact_constant_positive_row": 98,
    "local_table_arithmetic": {"synthetic_parameter_rows": 36, "near_displacements": 84,
                              "far_controls": 4, "single_site_sum": single_total,
                              "minimum_row": 11512, "maximum_row": 12248},
    "filling_table_arithmetic": {"pattern_rows": patterns_checked, "average_rows": 26,
                                "torus_tables": 4, "selected_occupancy_rows": 28},
    "activity_table_arithmetic": {"columns": 72, "all_affine_entries": affine_entries,
                                 "interpretation": "Entrywise only, never Loewner order."},
    "cache": {"declared_inputs": list(declared), "input_fingerprint_sha256": fingerprint,
              "runner_sha256": SHA(runner_body), "whole_cache_sha256": SHA(cache.encode()),
              "cache_bytes_reconstructed_exactly": True, "header_execution_status": "ok",
              "API_freshness_classification_from_read_code": "fresh",
              "execution_elapsed_seconds": execution["elapsed_sec"],
              "primary_internal_elapsed_seconds": result["elapsed_seconds"],
              "source_or_scientific_program_reexecuted_here": False},
    "root_failure_01": "Recorded replay of an earlier unsaved overly narrow diff expectation; all seven actual differences reproduced.",
    "root_failure_02": "Preserved wrong API expectation ok versus fresh; header ok and API fresh are distinct.",
    "root_process_evidence_matches_own_computation": True,
    "all_checks_completed": True,
}
print(json.dumps(report, indent=2, allow_nan=False))
