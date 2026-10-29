"""Coordinator reproduction of frozen independent reviews, not new review.

Predeclared comparison: exact parsed JSON except the top-level timing field
named for each invocation. Preserve every output and error; never overwrite.
This does not prove continuum existence or a physical mass gap.
"""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
import hashlib
import json
import shutil
import subprocess
import sys
import tempfile
import time

R = Path.cwd()
L = Path('.claude/science/toe-ruleset-20261021/agents/ym4d-proof')
C = L / 'checks'

def sha(raw):
    return hashlib.sha256(raw).hexdigest()

def dump(path, value):
    assert not path.exists(), str(path)
    path.write_text(json.dumps(value, indent=2) + '\n')

pins = {
    'review_uniform_soft_receipt.json': '33b98352bcdae4c40f9db02cefbbdfd225063395da0c7c589ee47626e0ed10a3',
    'review_source_sea_receipt.json': '06ffa9be999fd3fdf750f93629760001474f159d47d6fc1bc5ad1b0c179a5c24',
    'review_uniform_soft_scope_receipt.json': '54ef326a0accde7811db80c2ef85cb5c7907959083ca5252e4d6862b85e61dcb',
    'review_uniform_soft_scope_confirmation_receipt.json': 'd2df587d27a68cbfed6664b858fe56a24962199ab543a4ebcaa794476371a115',
}
artifacts = {}
receipts = {}
for name, expected in pins.items():
    raw = (C / name).read_bytes()
    assert sha(raw) == expected, name
    d = receipts[name] = json.loads(raw)
    artifacts[str(C / name)] = expected
    rows = d.get('files', [])
    if 'frozen_review_artifacts' in d:
        rows = [{'path': p, 'sha256': h} for p, h in d['frozen_review_artifacts'].items()]
    for row in rows:
        p, h = row['path'], row['sha256']
        assert p not in artifacts or artifacts[p] == h, p
        artifacts[p] = h
for p, h in artifacts.items():
    assert sha(Path(p).read_bytes()) == h, p

sources = {
    str(L / 'UNIFORM_SOFT_MINIMIZER_ASTRA.md'): '203d4edbf97078d88fcb488f164e525d2671fe5a2a910c5f6e49f615e8f41bfe',
    str(C / 'full_proof_uniform_tree_scope_fix.json'): 'fd2778df5869f21c7083ed1b0f2fcfb467535535cd739731a115632b24b2868e',
}
sources.update(receipts['review_source_sea_receipt.json']['frozen_inputs'])
for p, h in sources.items():
    assert sha(Path(p).read_bytes()) == h, p
old_note = subprocess.check_output(['git', 'show', '4a8afc90247d771b95c9661737dc08509456ab28:' + str(L / 'UNIFORM_SOFT_MINIMIZER_ASTRA.md')])
assert sha(old_note) == 'c7b7890187b9a350aea19e606957c606922fe741c6615382c3a4da0cd60d92c4'
dump(C / 'full_proof_next_reviews_bindings.json', {
    'created_utc': datetime.now(timezone.utc).isoformat(),
    'review_artifacts': artifacts, 'live_sources': sources,
    'preserved_original_uniform_note': {
        'revision': '4a8afc90247d771b95c9661737dc08509456ab28', 'sha256': sha(old_note)},
    'scope': 'Byte binding of frozen review artifacts and specified live inputs; full source-read coverage belongs to the review manifests.',
})

jobs = [
    ('uniform01', 'review_uniform_soft_01.py', 'review_uniform_soft_01_out.json', 'elapsed_seconds'),
    ('uniform02', 'review_uniform_soft_02.py', 'review_uniform_soft_02_out.json', 'elapsed_seconds'),
    ('uniform_scope', 'review_uniform_soft_scope_01.py', 'review_uniform_soft_scope_01_out.json', 'elapsed_seconds'),
    ('sea_geometry', 'review_source_sea_geometry.py', 'review_source_sea_geometry_01.json', 'seconds'),
    ('sea_refinement', 'review_source_sea_refinement.py', 'review_source_sea_refinement_01.json', 'seconds'),
    ('sea_su2', 'review_source_sea_su2.py', 'review_source_sea_su2_01.json', 'seconds'),
    ('sea_repair', 'review_source_sea_repair_check.py', 'review_source_sea_repair_check_01.json', None),
]
work = Path(tempfile.mkdtemp(prefix='ym-next-reviews-root-replay-'))

def run(job):
    label, script, reference, timing = job
    dest = work / label
    dest.mkdir()
    shutil.copy2(C / script, dest / script)
    copied = {script: sha((dest / script).read_bytes())}
    assert copied[script] == sha((C / script).read_bytes())
    if label == 'sea_repair':
        for name in ['source_sea_check.py', 'source_sea_check_v2.py', 'source_sea_run_02.json',
                     'source_sea_run_03.json', 'source_sea_control_fix_receipt.json',
                     'review_source_sea_author_replay_01.json']:
            shutil.copy2(C / name, dest / name)
            copied[name] = sha((dest / name).read_bytes())
            assert copied[name] == sha((C / name).read_bytes())
    start = time.time()
    result = subprocess.run([sys.executable, script], cwd=dest, capture_output=True)
    output = C / ('full_proof_next_review_' + label + '_out.json')
    error = C / ('full_proof_next_review_' + label + '_err.txt')
    assert not output.exists() and not error.exists()
    output.write_bytes(result.stdout)
    error.write_bytes(result.stderr)
    reference_bytes = (C / reference).read_bytes()
    record = {'label': label, 'script': str(C / script), 'script_sha256': copied[script],
              'copies': copied, 'temporary_directory': str(dest), 'exit_code': result.returncode,
              'wall_seconds': time.time() - start, 'stdout': str(output), 'stderr': str(error),
              'stdout_sha256': sha(result.stdout), 'stderr_sha256': sha(result.stderr),
              'reference': str(C / reference), 'reference_sha256': sha(reference_bytes),
              'excluded_top_level_timing_field': timing}
    try:
        actual, expected = json.loads(result.stdout), json.loads(reference_bytes)
        if timing is not None:
            assert timing in actual and timing in expected
            actual.pop(timing)
            expected.pop(timing)
        record['exact_non_time_json_match'] = actual == expected
        record['differing_top_level_keys'] = sorted(k for k in actual.keys() | expected.keys() if actual.get(k) != expected.get(k))
    except Exception as exc:
        record['comparison_error'] = repr(exc)
        record['exact_non_time_json_match'] = False
    record['source_unchanged'] = sha((C / script).read_bytes()) == copied[script]
    record['reference_unchanged'] = sha((C / reference).read_bytes()) == sha(reference_bytes)
    dump(C / ('full_proof_next_review_' + label + '_replay.json'), record)
    print(json.dumps({k: record[k] for k in ['label', 'exit_code', 'exact_non_time_json_match', 'wall_seconds']}), flush=True)
    return record

records = []
with ThreadPoolExecutor(max_workers=3) as pool:
    for future in as_completed([pool.submit(run, job) for job in jobs]):
        records.append(future.result())
for p, h in artifacts.items():
    assert sha(Path(p).read_bytes()) == h, p
for p, h in sources.items():
    assert sha(Path(p).read_bytes()) == h, p
ok = all(r['exit_code'] == 0 and r['stderr_sha256'] == sha(b'')
         and r['exact_non_time_json_match'] and r['source_unchanged'] and r['reference_unchanged']
         for r in records)
dump(C / 'full_proof_next_reviews_replay_summary.json', {
    'created_utc': datetime.now(timezone.utc).isoformat(), 'all_ok': ok,
    'runs': sorted(records, key=lambda r: r['label']),
    'frozen_review_artifacts_unchanged': len(artifacts), 'live_sources_unchanged': len(sources),
    'scope': 'Seven invocations reproduce review diagnostics; this is coordinator reproduction, not a further independent review.',
})
print(json.dumps({'all_ok': ok, 'runs': len(records), 'review_artifacts': len(artifacts), 'live_sources': len(sources)}), flush=True)
assert ok
