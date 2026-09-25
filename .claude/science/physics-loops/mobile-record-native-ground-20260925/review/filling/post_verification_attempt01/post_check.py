#!/usr/bin/env python3
"""Read-only POST comparison: read/parse/hash stored evidence, print JSON.

No author or PRE program is imported or executed. No file is written by this
program. The caller may capture stdout/stderr into new POST evidence files.
"""
import ast
import hashlib
import json
from datetime import datetime, timezone
from fractions import Fraction as F
from math import comb, prod
from pathlib import Path

HERE = Path(__file__).resolve().parent
AUTHOR = HERE / "post_sources/native-ground-filling-personal"


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read_json(path):
    return json.loads(path.read_text())


def verify_member(base, row):
    p = base / row["path"]
    assert sha(p) == row["sha256"], str(p)
    assert p.stat().st_size == row["bytes"], str(p)


def falling(n, k):
    return prod(n - j for j in range(k))


def trial(n, m, weights):
    # Own PRE's falling-factorial organization, not the author's binomials.
    return sum(F(w * falling(m, ell - 2) * falling(n - m, 2),
                 falling(n, ell)) for ell, w in weights.items())


def main():
    expected_pre_seal = "0d420d0263cb53ed341d79f361cfc7ee2dae9125f976b6715216bd48a5cd8384"
    expected_author_seal = "0b72c3cd4dd5404a53de9808a5bf99fab48eab182defedba729b695ff4202066"
    assert sha(HERE / "PRE_SEAL.json") == expected_pre_seal
    assert sha(AUTHOR / "AUTHOR_SEAL.json") == expected_author_seal
    pre_seal = read_json(HERE / "PRE_SEAL.json")
    author_seal = read_json(AUTHOR / "AUTHOR_SEAL.json")
    for row in pre_seal["members"]:
        verify_member(HERE, row)
    for row in author_seal["members"]:
        verify_member(AUTHOR, row)
    assert len(pre_seal["members"]) == 35
    assert len(author_seal["members"]) == 9
    assert datetime.fromisoformat(author_seal["sealed_utc"]) < datetime.fromisoformat(pre_seal["sealed_utc"])

    pins = read_json(HERE / "POST_SOURCE_PINS_INITIAL.json")
    assert len(pins["sources"]) == 17
    for row in pins["sources"]:
        assert sha(Path(row["origin"])) == row["sha256"]
        assert Path(row["origin"]).stat().st_size == row["bytes"]
        if row["snapshot"] is not None:
            assert sha(HERE / row["snapshot"]) == row["sha256"]

    # Explicit allow-list: never follow one-pair context references.
    pre_pins = read_json(HERE / "SOURCE_PINS.json")
    allowed = {r["origin"]: r for r in
               pre_pins["scientific_sources"] + pre_pins["instructions"]
               if "origin" in r}
    checked_parent_rows, excluded_context = [], []
    for row in read_json(AUTHOR / "SOURCE_PINS.json")["sources"]:
        if row["path"] in allowed:
            assert row["sha256"] == allowed[row["path"]]["sha256"]
            assert sha(Path(row["path"])) == row["sha256"]
            checked_parent_rows.append(row)
        else:
            # Metadata strings only. Do not resolve, open or hash their paths.
            assert "native-one-pair-spectrum-" in row["path"]
            excluded_context.append({**row, "referenced_file_opened": False,
                                     "live_hash_checked": False})
    assert len(checked_parent_rows) == 4 and len(excluded_context) == 4

    root = read_json(AUTHOR / "GROUND_FILLING_CERTIFICATES.json")
    pre = read_json(HERE / "CONTROL_RESULTS.json")
    receipt = read_json(AUTHOR / "EXECUTION.json")
    assert (AUTHOR / "CONTROL.stdout").read_bytes() == (AUTHOR / "GROUND_FILLING_CERTIFICATES.json").read_bytes()
    assert receipt["exit_code"] == 0 and receipt["stderr_bytes"] == 0
    for stream in ("stdout", "stderr"):
        assert sha(AUTHOR / ("CONTROL." + stream)) == receipt[stream + "_sha256"]
        assert (AUTHOR / ("CONTROL." + stream)).stat().st_size == receipt[stream + "_bytes"]
    assert receipt["code_sha256"] == root["source_sha256"] == sha(AUTHOR / "ground_filling_certificates.py")
    assert pre["source_sha256"] == sha(HERE / "ground_filling_control.py")
    assert root["all_assertions_passed"] and pre["all_exact_assertions_passed"]

    pre_local = {x["r"]: x for x in pre["local_certificates"]}
    local_count = 0
    maxima_rows, average_rows = [], []
    weights_by_r = {}
    for block in root["local_certificates"]:
        r = block["overlap"]
        pb = pre_local[r]
        weights = {int(k): v for k, v in pb["squared_path_union_counts"].items()}
        weights_by_r[r] = weights
        assert block["local_counts"] == dict(zip(("v", "a", "d"), (weights[2], weights[3], weights[4])))
        assert block["union_sites"] == pb["union_size"] == 12 - r
        assert block["complete_subsets_checked"] == pb["masks_checked"] == 2 ** (12 - r)
        mapping = {(x["ua"], x["uc"], x["w"]): x for x in pb["groups"]}
        assert len(mapping) == len(block["pattern_rows"])
        seen = set()
        for row in block["pattern_rows"]:
            key = row["sa"], row["sc"], row["t"]
            assert key not in seen
            seen.add(key)
            old = mapping[key]
            assert row["row"] == old["return_count"]
            assert row["multiplicity"] == old["occupancy_masks"]
            ell = row["sa"] + row["sc"] - row["t"]
            z = 12 - r - ell
            assert (row["occupied"], row["vacant"]) == (ell, z)
            assert row["multiplicity"] == comb(r, row["t"]) * comb(6-r, row["sa"]-row["t"]) * comb(6-r, row["sc"]-row["t"])
            inc = str(F(row["row"]-weights[2], ell)) if ell else None
            vac = str(F(row["row"], z)) if z else None
            assert row["increment_per_occupied"] == inc
            assert row["row_per_vacant"] == vac
            if not ell:
                assert row["row"] == weights[2]
            if not z:
                assert row["row"] == 0
            local_count += 1
        assert seen == set(mapping)
        assert sum(x["multiplicity"] for x in block["pattern_rows"]) == 2 ** (12-r)
        for t in range(r+1):
            rows = [x for x in block["pattern_rows"] if x["t"] == t]
            inc = max(F(x["increment_per_occupied"]) for x in rows if x["increment_per_occupied"] is not None)
            vac = max(F(x["row_per_vacant"]) for x in rows if x["row_per_vacant"] is not None)
            expected = {(1,0):(F(69,2),F(28)), (1,1):(F(40),F(24)),
                        (2,0):(F(37),F(104,3)), (2,1):(F(44),F(80,3)),
                        (2,2):(F(38),F(23))}[r,t]
            assert (inc, vac) == expected
            maxima_rows.append({"r":r,"t":t,"patterns":len(rows),"increment_max":str(inc),"vacancy_max":str(vac)})
        assert F(block["maximum_increment_per_occupied"]) == max(F(x["increment_per_occupied"]) for x in block["pattern_rows"] if x["increment_per_occupied"] is not None)
        assert F(block["maximum_row_per_vacant"]) == max(F(x["row_per_vacant"]) for x in block["pattern_rows"] if x["row_per_vacant"] is not None)
        for row in block["all_m_average_rows"]:
            n, m = row["global_B_sites"], row["occupied"]
            value = trial(n,m,weights)
            assert value == F(row["uniform_Rayleigh"])
            average_rows.append({"r":r,"n":n,"m":m,"falling_factorial_value":str(value)})
    assert local_count == 147 and len(average_rows) == 26

    torus_rows, half_rows, pre_geometry_matches = [], [], []
    for block in root["torus_certificates"]:
        L, n = block["side"], block["B_sites"]
        assert L in (6,8,10,12) and n == L**3//2
        assert block["overlapping_pair_counts"] == {"1":3*n,"2":6*n}
        assert block["every_B_union_incidence"] == {"overlap_1":33,"overlap_2":60}
        assert block["all_B_sites_checked"] == n
        for row in block["selected_occupancies"]:
            m = row["occupied_B"]
            assert m % 2 == 0 and row["minus_charges"] == m//2
            value = 3*trial(n,m,weights_by_r[1])+6*trial(n,m,weights_by_r[2])
            bounds = (F(321)+F(3960*m,n), F(3004*(n-m),n))
            assert F(row["Rayleigh_per_n"]) == value
            assert tuple(map(F,row["two_row_upper_bounds_per_n"])) == bounds
            assert value <= min(bounds)
            torus_rows.append({"L":L,"n":n,"m":m,"Rayleigh_per_n":str(value),"root_bounds_per_n":list(map(str,bounds))})
        half = 3*trial(n,n//2,weights_by_r[1])+6*trial(n,n//2,weights_by_r[2])
        extra = F(378,n-1)+F(414*(2*n-3),(n-1)*(n-3))
        assert half == F(1905,2)+extra and extra > 0
        assert F(block["half_filling_Rayleigh_per_n"]) == half
        assert F(block["half_filling_excess_above_1905_over_2"]) == extra
        half_rows.append({"L":L,"half_trial_per_n":str(half),"positive_excess":str(extra)})
        for old in pre["geometry_rows"]:
            if old["lengths"] == [L]*3:
                assert old["unordered_r1_pairs"] == 3*n
                assert old["unordered_r2_pairs"] == 6*n
                assert F(old["half_filled_trial_Q"]) == 2*n*half
                assert old["empty_band_maximum_Q0"] == 642*n
                pre_geometry_matches.append({"L":L,"root_trial":str(n*half),"PRE_trial":old["half_filled_trial_Q"],"PRE_over_root":2})
    assert len(torus_rows) == 28 and len(half_rows) == 4
    assert len(pre_geometry_matches) == 2
    assert 33*40+60*44 == 3960
    assert 33*28+60*F(104,3) == 3004
    lo, hi = (F(1905,2)-321)/3960, 1-F(1905,2)/3004
    assert (lo,hi) == (F(421,2640),F(4103,6008))
    thresholds = root["necessary_lowest_energy_sector_filling"]
    assert F(thresholds["strict_lower"]) == lo and F(thresholds["strict_upper"]) == hi
    assert thresholds["lower_decimal"] == float(lo) and thresholds["upper_decimal"] == float(hi)

    # Inspect the sealed PRE utility as text/AST; never execute it.
    tree = ast.parse((HERE / "verify_pre.py").read_text())
    write_calls = [{"line":n.lineno,"expression":ast.unparse(n)} for n in ast.walk(tree)
                   if isinstance(n,ast.Call) and isinstance(n.func,ast.Attribute)
                   and n.func.attr in ("write_text","write_bytes")]
    assert len(write_calls) >= 3
    for target in ("CONTROL_EXTENSION_DIFF.txt","SOURCE_PINS.json","VERIFICATION_REPORT.json"):
        assert any(target in x["expression"] for x in write_calls)
    own_tree = ast.parse(Path(__file__).read_text())
    own_write_calls = [n for n in ast.walk(own_tree) if isinstance(n,ast.Call)
                       and isinstance(n.func,ast.Attribute)
                       and n.func.attr in ("write_text","write_bytes","mkdir","unlink","rename","replace","chmod")]
    assert not own_write_calls

    report = {
        "checked_utc":datetime.now(timezone.utc).isoformat(),
        "scope":"Released-source mathematical/evidence correspondence; no author/PRE scientific execution, no new blind reconstruction or audit verdict.",
        "source_sha256":sha(Path(__file__)),
        "PRE_seal_sha256":expected_pre_seal,
        "PRE_members_unchanged":len(pre_seal["members"]),
        "author_seal_sha256":expected_author_seal,
        "author_members_verified":len(author_seal["members"]),
        "live_pinned_origins_verified":len(pins["sources"]),
        "allowed_parent_and_workflow_origins_verified":checked_parent_rows,
        "unopened_historical_context_metadata":excluded_context,
        "chronology":{"author_sealed_utc":author_seal["sealed_utc"],"PRE_sealed_utc":pre_seal["sealed_utc"],"author_precedes_PRE":True},
        "author_stored_execution":receipt,
        "author_output_byte_identical_to_stdout":True,
        "local_rows_compared_with_independent_PRE":local_count,
        "local_masks_represented":3072,
        "root_union_maxima_from_stored_PRE_rows":maxima_rows,
        "artificial_ambient_average_checks":average_rows,
        "torus_stored_row_arithmetic_checks":torus_rows,
        "half_filling_strict_excess_checks":half_rows,
        "direct_shared_PRE_geometry_matches":pre_geometry_matches,
        "root_thresholds":{"lower":str(lo),"upper":str(hi)},
        "PRE_coarse_thresholds_on_shared_L_ge_6_domain":{"lower":str(F(421,2604)),"upper":str(F(209,336)),"strictly_sharper_than_root":F(421,2604)>lo and F(209,336)<hi},
        "sealed_PRE_tooling_limitation":{"old_verifier_executed":False,"write_calls":write_calls,"POST_verifier_has_no_file_writing_calls":True},
        "all_comparisons_passed":True,
        "limitations":["This comparison parses prior controls; it does not rerun their 3072 subsets, geometry enumeration or physical paths.","L=10,12 incidence values are checked against the proved formula and read author code, not a fresh independent graph enumeration.","No normalizable ground vector, exact minimizing filling, fixed-g thermodynamic limit, physical vacuum or empirical implication established."]
    }
    print(json.dumps(report,indent=2,sort_keys=True))


if __name__ == "__main__":
    main()
