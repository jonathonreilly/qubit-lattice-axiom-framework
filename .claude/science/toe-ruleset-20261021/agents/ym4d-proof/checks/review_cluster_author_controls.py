#!/usr/bin/env python3
"""Pinned author reproduction and isolated mutation runs; no author file writes."""
import hashlib,json,subprocess,sys,time
from pathlib import Path
ROOT=Path.cwd()
OUT=ROOT/'.claude/science/toe-ruleset-20261021/agents/ym4d-proof/checks'
REV='962f97c259d8c241df632a07e27f498f4ad33b09'
PREFIX='.claude/science/toe-ruleset-20261021/agents/ym4d-proof/'
source=subprocess.check_output(['git','show',REV+':'+PREFIX+'checks/recovery_cluster_exact.py'])
expected=subprocess.check_output(['git','show',REV+':'+PREFIX+'checks/recovery_cluster_results.json'])
assert hashlib.sha256(source).hexdigest()=='5f51587d7f1630f6db15fef1dd697340a096839808ea00941b751a12bd70f0e6'
mutations=[
 ('determinant_half_factor','det_derivative = -det[tk] / (2 * det[ZERO])','det_derivative = -det[tk] / det[ZERO]','full_logdet_two_exact_paths'),
 ('trace_sign','trace_derivative = -sum(','trace_derivative = sum(','full_logdet_two_exact_paths'),
 ('long_connector','support=frozenset(range(x, y + 1))','support=frozenset([x, y])','all_log_supports_connected'),
 ('source_expected','probe_expected = F(1, 101 * 104 * 108)','probe_expected = F(1, 101 * 104 * 107)','long_jump_source_coefficient'),
 ('row_majorant','max_row == max_col == F(729, 8192)','max_row == max_col == F(729, 8191)','finite_operator_majorants'),
 ('self_polymer','if s & t:','if s != t and s & t:','direct_log_equals_connected_log_to_degree_6'),
]
results=[]
for name,needle,replacement,failure in [('replay',None,None,None)]+mutations:
    code=source.decode()
    if needle is not None:
        assert code.count(needle)==1,(name,code.count(needle))
        code=code.replace(needle,replacement)
    path=OUT/('review_cluster_author_'+name+'.py')
    path.write_text(code)
    start=time.monotonic()
    run=subprocess.run([sys.executable,str(path)],capture_output=True,cwd=ROOT)
    elapsed=time.monotonic()-start
    op=path.with_suffix('.stdout.json');ep=path.with_suffix('.stderr.txt')
    op.write_bytes(run.stdout);ep.write_bytes(run.stderr)
    payload=json.loads(run.stdout)
    exact_replay=(run.stdout==expected) if name=='replay' else None
    detected=(run.returncode==1 and payload['checks'].get(failure) is False) if name!='replay' else None
    results.append(dict(name=name,script=str(path.relative_to(ROOT)),
        script_sha256=hashlib.sha256(path.read_bytes()).hexdigest(),exit_code=run.returncode,
        duration_seconds=elapsed,stdout_sha256=hashlib.sha256(run.stdout).hexdigest(),
        stderr_sha256=hashlib.sha256(run.stderr).hexdigest(),exact_replay=exact_replay,
        expected_failed_predicate=failure,detected_at_intended_gate=detected,
        all_failed_predicates=[k for k,v in payload['checks'].items() if not v],
        mutation=None if needle is None else dict(before=needle,after=replacement)))
report=dict(scope='Reproduction and mutation sensitivity of finite author checker only; no general theorem certificate',
    frozen_revision=REV,source_sha256=hashlib.sha256(source).hexdigest(),
    exact_author_replay=results[0]['exact_replay'],
    all_six_author_mutations_detected=all(r['detected_at_intended_gate'] for r in results[1:]),runs=results)
print(json.dumps(report,indent=2,sort_keys=True))
if results[0]['exit_code']!=0 or not report['exact_author_replay'] or not report['all_six_author_mutations_detected']:
    raise SystemExit(1)
