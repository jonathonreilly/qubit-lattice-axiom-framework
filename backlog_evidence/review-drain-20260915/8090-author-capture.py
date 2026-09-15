"""Capture each frozen PR8090 primary once; retain every completed result."""
from pathlib import Path
import hashlib
import json
import subprocess
import sys

root = Path.cwd()
out = root.parent
record_path = out / '8090-unit-v1-preexecution.json'
record = json.loads(record_path.read_text())
preflight = json.loads((out / '8090-preexecution-preflight.json').read_text())
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
assert preflight['mechanical_status'] == 'ok'
assert preflight['record_sha256'] == sha(record_path)
assert preflight['tree'] == record['source']['tree']
assert subprocess.check_output(['git', 'write-tree'], text=True).strip() == record['source']['tree']
inputs = {row['path']: row['sha256'] for row in record['source']['paths']}
for rows in record['inputs'].values():
    for row in rows:
        assert row['path'] not in inputs or inputs[row['path']] == row['sha256']
        inputs[row['path']] = row['sha256']
for p, h in inputs.items():
    assert sha(root / p) == h, p
sys.path.insert(0, str(root / 'scripts'))
import runner_cache

# The primary also emits this detailed receipt. Preserve its exact original bytes
# before the sole attempt; it is an output, not an execution input.
output_rel = 'outputs/native_interacting_weyl_2026_09_13.json'
output_path = root / output_rel
original_output = out / '8090-original-output-before-capture.json'
assert not original_output.exists(), 'Never repeat a prior capture'
for rows in record['inputs'].values():
    assert output_rel not in {row['path'] for row in rows}, 'Never authorize drift of an input'
with original_output.open('xb') as handle:
    handle.write(output_path.read_bytes())
assert sha(original_output) == inputs[output_rel]
completed_caches = set()
for note, count in zip(record['notes'], (153,), strict=True):
    runner = note['primary_runner']
    receipt_path = out / ('8090-execution-' + Path(runner).stem + '.json')
    assert not receipt_path.exists(), 'Never overwrite or repeat a prior attempt'
    result, cache = runner_cache.execute_and_write_cache(runner, timeout_sec=60)
    receipt = {'runner': runner, 'limit_sec': 60, 'preexecution_record_sha256': sha(record_path),
               'result': result, 'cache_path': str(cache) if cache else None,
               'cache_sha256': sha(cache) if cache else None,
               'original_output_sha256': sha(original_output),
               'output_path': output_rel, 'output_sha256': sha(output_path)}
    with receipt_path.open('x') as handle:
        json.dump(receipt, handle, indent=2)
        handle.write('\n')
    assert result['status'] == 'ok' and result['exit_code'] == 0, receipt_path
    assert f'TOTAL: PASS={count} FAIL=0' in result['stdout'], receipt_path
    assert cache and runner_cache.cache_status(runner) == 'fresh'
    completed_caches.add(output_rel)
    completed_caches.add(cache.resolve().relative_to(root.resolve()).as_posix())
    for p, h in inputs.items():
        if p not in completed_caches:
            assert sha(root / p) == h, p
    subprocess.run(['git', 'add', str(cache), output_rel], check=True)
    print(runner, count, 'PASS; seconds', result['elapsed_sec'], flush=True)
for args in [('diff', '--check'), ('diff', '--cached', '--check'), ('diff', 'HEAD', '--check')]:
    subprocess.run(['git', *args], check=True)
print('Final staged tree', subprocess.check_output(['git', 'write-tree'], text=True).strip(), flush=True)
