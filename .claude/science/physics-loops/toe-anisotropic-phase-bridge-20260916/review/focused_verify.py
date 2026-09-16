#!/usr/bin/env python3
"""Check this discovery packet's byte closure; not canonical audit evidence."""
AUDIT_TIMEOUT_SEC = 180
import ast
import datetime
import hashlib
import json
import py_compile
import re
import subprocess
from pathlib import Path

PACK = Path(__file__).resolve().parents[1]
REPO = PACK.parents[3]
PRIMARY = [
 ('block01_anisotropic_conditional_and_poisson_check.py','BLOCK01_ANISOTROPIC_POISSON_ATTEMPT2.stdout.txt','BLOCK01_ANISOTROPIC_POISSON_ATTEMPT2.stderr.txt'),
 ('block02_coupled_jump_and_response_check.py','BLOCK02_COUPLED_RESPONSE_ATTEMPT2.stdout.txt','BLOCK02_COUPLED_RESPONSE_ATTEMPT2.stderr.txt'),
 ('block03_phase_corrector_check.py','block03_phase_corrector_check.ATTEMPT3.stdout.json','block03_phase_corrector_check.ATTEMPT3.stderr.txt'),
 ('block04_local_heat_and_orthogonality_check.py','block04_local_heat_and_orthogonality_check.ATTEMPT2.stdout.json','block04_local_heat_and_orthogonality_check.ATTEMPT2.stderr.txt'),
 ('block05_quantum_comparison_check.py','block05_quantum_comparison_check.FINAL.stdout.json','block05_quantum_comparison_check.FINAL.stderr.txt'),
 ('block06_raw_curl_counterexample.py','block06_raw_curl_counterexample.FINAL.stdout.json','block06_raw_curl_counterexample.FINAL.stderr.txt'),
 ('block07_positive_mixture_check.py','block07_positive_mixture_check.FINAL.stdout.json','block07_positive_mixture_check.FINAL.stderr.txt'),
 ('block08_bridge_action_check.py','block08_bridge_action_check.FINAL.stdout.json','block08_bridge_action_check.FINAL.stderr.txt'),
]
BASE = 'e0ef7cf4633034a8c1e6d57f5812cc4275bf1349'


def digest(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def main():
    rows = []
    for source, output, stderr in PRIMARY:
        f, out, err = [PACK/'evidence'/name for name in (source, output, stderr)]
        data = json.loads(out.read_text())
        assert data['source_sha256'] == digest(f), ('source/output mismatch', source)
        assert err.stat().st_size == 0, ('nonempty successful stderr', stderr)
        tree = ast.parse(f.read_text())
        declarations = [ast.literal_eval(n.value) for n in tree.body if isinstance(n,ast.Assign)
                        and any(isinstance(t,ast.Name) and t.id=='AUDIT_TIMEOUT_SEC' for t in n.targets)]
        assert declarations == [180], (source, declarations)
        rows.append(dict(source=source, source_sha256=digest(f), output=output,
                         output_sha256=digest(out), timeout_sec=declarations[0]))
    phase = json.loads((PACK/'evidence'/PRIMARY[2][1]).read_text())
    assert phase['parent_sha256'] == digest(PACK/'evidence'/PRIMARY[1][0])
    harness = PACK/'evidence/challenge_formula_faults.py'
    fault_output = PACK/'evidence/challenge_formula_faults.ATTEMPT1.stdout.json'
    data = json.loads(fault_output.read_text())
    assert data['harness_sha256'] == digest(harness)
    assert not (PACK/'evidence/challenge_formula_faults.ATTEMPT1.stderr.txt').read_text()
    for row in data['formula_faults']:
        f = PACK/'evidence'/row['source_path']
        assert row['original_sha256'] == digest(PACK/'evidence'/row['source'])
        assert row['mutated_sha256'] == digest(f)
        assert row['exit_code'] != 0 and row['assertion_rejected']
        assert row['stdout_sha256'] == digest(f.with_suffix('.stdout.txt'))
        assert row['stderr_sha256'] == digest(f.with_suffix('.stderr.txt'))
    py = sorted(PACK.rglob('*.py'))
    for f in py:
        py_compile.compile(str(f), doraise=True)
    links = []
    pending_report_links = []
    md = sorted(PACK.rglob('*.md'))
    for f in md:
        for target in re.findall(r'\]\(([^)]+)\)',f.read_text()):
            if '://' in target or target.startswith('#'):
                continue
            path = target.split('#',1)[0]
            if not path:
                continue
            assert not Path(path).is_absolute(), (f,target)
            q = (f.parent/path).resolve()
            assert q.is_relative_to(REPO), (f,target)
            if q == PACK/'review/FOCUSED_VERIFICATION.json' and not q.exists():
                pending_report_links.append(q)
            else:
                assert q.is_file(), (f,target)
            links.append(dict(source=str(f.relative_to(PACK)),target=path))
    diff = subprocess.run(['git','diff','--check',BASE,'--',str(PACK)],cwd=REPO,
                          capture_output=True,text=True)
    assert diff.returncode == 0, diff.stdout+diff.stderr
    report = dict(checked_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
                  verifier_sha256=digest(Path(__file__)), base_main=BASE,
                  scope='focused author verification; no formal audit verdict',
                  primary_pairs=rows, fault_harness_sha256=digest(harness),
                  formula_faults=len(data['formula_faults']),
                  fault_output_sha256=digest(fault_output),
                  python_files_compiled=len(py), markdown_files=len(md),
                  relative_links=links, full_base_diff_check_exit=diff.returncode,
                  pending='canonical registration and caches, independent review, integrated landing gates')
    (PACK/'review/FOCUSED_VERIFICATION.json').write_text(json.dumps(report,indent=2)+'\n')
    assert all(q.is_file() for q in pending_report_links)
    print(json.dumps({k:report[k] for k in ['checked_utc','formula_faults','python_files_compiled','markdown_files','full_base_diff_check_exit']},indent=2))


if __name__ == '__main__':
    main()
