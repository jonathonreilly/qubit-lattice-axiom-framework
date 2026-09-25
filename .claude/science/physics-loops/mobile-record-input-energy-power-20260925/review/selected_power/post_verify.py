#!/usr/bin/env python3
"""Final source and execution verification; no scientific calculation rerun."""
from datetime import datetime, timezone
from pathlib import Path
import ast
import hashlib
import json
import platform
import subprocess
import sys

import numpy

HERE = Path(__file__).resolve().parent
REVISION = 'b47a67e3a08febd2aaf3545eae9a278b4901a72d'


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def read(name):
    return json.loads((HERE/name).read_bytes())


pre_raw = (HERE/'PRE_SEAL.json').read_bytes()
assert sha(pre_raw) == 'a1cc8dc5b9af73952b55402902076e1b7b28b7bc7bbc2de4834c65dd8297031d'
pre = json.loads(pre_raw)
for row in pre['members']:
    raw = (HERE/row['path']).read_bytes()
    assert len(raw) == row['bytes'] and sha(raw) == row['sha256']

pins = read('POST_SOURCE_PINS.json')
for row in pins['author_sources']:
    raw = (HERE/row['frozen_path']).read_bytes()
    assert raw == Path(row['origin']).read_bytes()
    assert len(raw) == row['bytes'] and sha(raw) == row['sha256']
for row in pins['reused_PRE_sources']:
    assert sha(Path(row['origin']).read_bytes()) == row['sha256']

executions = []
for label, script, output in [('post_freeze', 'post_freeze.py', 'POST_SOURCE_PINS.json'),
                              ('post_check', 'post_check.py', 'POST_CHECK_RESULTS.json')]:
    receipt = read(label+'.execution.json')
    assert receipt['script_sha256'] == sha((HERE/script).read_bytes())
    assert receipt['exit_code'] == 0
    assert Path(receipt['argv'][1]) == HERE/script
    for stream in ('stdout', 'stderr'):
        raw = (HERE/(label+'.'+stream+'.txt')).read_bytes()
        assert len(raw) == receipt[stream+'_bytes'] and sha(raw) == receipt[stream+'_sha256']
    assert (HERE/(label+'.stdout.txt')).read_bytes() == (HERE/output).read_bytes()
    assert not (HERE/(label+'.stderr.txt')).read_bytes()
    executions.append(dict(label=label, script_sha256=receipt['script_sha256'],
        stdout_sha256=receipt['stdout_sha256'], stderr_bytes=0, exit_code=0,
        elapsed_seconds=receipt['elapsed_seconds']))

git_rows = []
for row in pins['reused_PRE_sources'][:3]:
    relative = 'docs/'+Path(row['origin']).name
    command = ['git', '-C', str(HERE.parent/'campaign-working'), 'show', REVISION+':'+relative]
    run = subprocess.run(command, capture_output=True)
    assert run.returncode == 0 and not run.stderr
    assert sha(run.stdout) == row['sha256']
    assert run.stdout == (HERE/row['frozen_path']).read_bytes()
    git_rows.append(dict(argv=command, exit_code=run.returncode, stderr_bytes=len(run.stderr),
        stdout_bytes=len(run.stdout), stdout_sha256=sha(run.stdout),
        complete_stdout_retained_at=row['frozen_path'], equals_PRE_source_bytes=True))

check = read('POST_CHECK_RESULTS.json')
assert check['source_sha256'] == sha((HERE/'post_check.py').read_bytes())
assert check['exact_coefficient_correspondence']['all_author_words_read_and_compared'] == 606
assert check['exact_coefficient_correspondence']['all_author_pair_rows_read_and_compared'] == 528
assert check['exact_filling']['link_equalities'] == 525 and check['exact_filling']['all_equalities_exact']
assert check['author_spectral_arithmetic']['all_rows_read'] == 18
assert check['author_code_run_or_imported'] is False

# Static imports show that the new scientific checker is self-contained.
tree = ast.parse((HERE/'post_check.py').read_text())
imports = []
for node in ast.walk(tree):
    if isinstance(node, ast.Import):
        imports += [name.name for name in node.names]
    elif isinstance(node, ast.ImportFrom):
        imports.append(node.module)
assert set(imports) == {'collections','datetime','fractions','itertools','pathlib','hashlib','json','math','time','numpy'}

report_raw = (HERE/'POST.md').read_bytes()
result = dict(created_utc=datetime.now(timezone.utc).isoformat(),
    scope='Final exact-source and execution verification; no scientific rerun or audit verdict',
    source_sha256=sha(Path(__file__).read_bytes()),
    PRE_seal_sha256=sha(pre_raw), PRE_members_unchanged=len(pre['members']),
    released_author_files_plus_seal_unchanged=len(pins['author_sources']),
    prior_live_origins_unchanged=len(pins['reused_PRE_sources']),
    own_execution_log_bindings=executions, refreshed_main_exact_git_sources=git_rows,
    checker_imports=imports, author_imports_or_execution=False,
    report_sha256=sha(report_raw), report_bytes=len(report_raw),
    python_executable=sys.executable, python_version=sys.version,
    numpy_version=numpy.__version__, platform=platform.platform())
raw = json.dumps(result, indent=2)+'\n'
with (HERE/'POST_FINAL_VERIFICATION.json').open('x') as output:
    output.write(raw)
print(raw, end='')
