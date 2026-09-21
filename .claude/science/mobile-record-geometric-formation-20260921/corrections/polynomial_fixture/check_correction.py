from pathlib import Path
import contextlib, datetime, hashlib, importlib.util, json, math, shutil, sys, tempfile

HERE = Path(__file__).resolve().parent
RAW = HERE.parent
OLD = HERE / 'before_geometric_polynomial_relaxation_check.py'
NEW = RAW / 'geometric_polynomial_relaxation_check.py'
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
assert sha(OLD) == 'fded420e936b93bee16aeba4bfed676363d0298e6c1268fa5193cea5ef0c0202'
assert sha(NEW) == '996c2098b94a0f3e3331cfb7152af40bf18e7b6307e5a806204e9569e04478f0'
before = OLD.read_text()
assert NEW.read_text() == before.replace("['all_four_63','cycle6','cube','odd_barbell','path_10']", "['all_four_63','cycle_6','cube','odd_barbell','path_10']")
assert not (HERE / 'RESULTS.json').exists()
with tempfile.TemporaryDirectory(prefix='geometric-polynomial-fixture-fix-') as td:
    temp = Path(td)
    for name in ['geometric_polynomial_relaxation_check.py', 'geometric_general_graph_check.py', 'geometric_partner_formation_check.py']:
        shutil.copy2(RAW / name, temp / name)
    sys.path.insert(0, td)
    sys.dont_write_bytecode = True
    spec = importlib.util.spec_from_file_location('corrected_polynomial', temp / NEW.name)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    module.killing_bounds()
    rows = module.ROWS[0]['rows']
    assert len(module.ROWS) == 1 and len(rows) == 40
    assert sum(r['case'] == 'cycle_6' for r in rows) == 5
    old_result = json.loads((RAW / 'geometric_polynomial_relaxation_checks/RESULTS.json').read_text())
    previous = old_result['rows'][2]['rows']
    reused = [r for r in rows if r['case'] != 'cycle_6']
    assert len(previous) == len(reused) == 35
    maximum_delta = 0.
    for old, new in zip(previous, reused):
        assert set(old) == set(new)
        for key, value in old.items():
            if isinstance(value, float):
                maximum_delta = max(maximum_delta, abs(value - new[key]))
                assert math.isclose(value, new[key], rel_tol=1e-11, abs_tol=1e-11), (key, value, new[key])
            else:
                assert value == new[key]
    result = {'scope': 'Only the affected numerical killing group rerun; all old sources/results preserved. No mathematical note changed.',
              'created_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
              'old_source_sha256': sha(OLD), 'new_source_sha256': sha(NEW),
              'original_results_sha256': sha(RAW / 'geometric_polynomial_relaxation_checks/RESULTS.json'),
              'rows': rows, 'cycle_6_rows_added': 5, 'previous_rows_rechecked': 35,
              'maximum_delta_on_previous_rows': maximum_delta,
              'pass': True}
    (HERE / 'RESULTS.json').write_text(json.dumps(result, indent=2, allow_nan=False) + '\n')
    print(json.dumps({key: result[key] for key in ['cycle_6_rows_added', 'previous_rows_rechecked', 'maximum_delta_on_previous_rows', 'pass']}))
