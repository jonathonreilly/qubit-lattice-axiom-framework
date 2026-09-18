#!/usr/bin/env python3
"""Focused source/receipt closure; not an independent scientific verdict."""
AUDIT_TIMEOUT_SEC=120
from pathlib import Path
import ast,hashlib,json,re,subprocess


def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()


def main():
    pack=Path(__file__).resolve().parents[1];repo=pack.parents[3];base=pack/'evidence'
    programs=['bridge_cubic_check','convex_carrier_check','integer_filling_check','magnetic_covariance_check']
    evidence=[]
    for name in programs:
        source=base/(name+'.py');output=base/(name+'.FINAL.stdout.json')
        data=json.loads(output.read_text())
        if name=='convex_carrier_check':
            assert data['input_sha256']=={n:sha(base/n) for n in ('convex_carrier_check.py','bridge_cubic_check.py')}
        else:assert data['source_sha256']==sha(source)
        assert data['status']=='PERSONAL_CHECKS_COMPLETED'
        assert (base/(name+'.FINAL.stderr.txt')).read_text()==''
        tree=ast.parse(source.read_text())
        timeout=[n.value.value for n in tree.body if isinstance(n,ast.Assign)
                 and any(isinstance(t,ast.Name) and t.id=='AUDIT_TIMEOUT_SEC' for t in n.targets)]
        assert timeout==[120]
        evidence.append(dict(source=str(source.relative_to(pack)),sha256=sha(source),output_sha256=sha(output)))
    faults=json.loads((base/'run_formula_faults.ATTEMPT2.stdout.json').read_text())
    assert faults['source_sha256']==sha(base/'run_formula_faults.py')
    assert faults['helper_sha256']=={'bridge_cubic_check.py':sha(base/'bridge_cubic_check.py')}
    assert sha(base/'formula_faults/bridge_cubic_check.py')==sha(base/'bridge_cubic_check.py')
    assert len(faults['cases'])==12
    for row in faults['cases']:
        assert row['original_sha256']==sha(base/row['original_file'])
        mutant=base/'formula_faults'/(row['name']+'.py')
        assert row['mutant_sha256']==sha(mutant) and row['exit_code']!=0
        assert 'AssertionError' in (base/row['stderr_file']).read_text()
    histories=[]
    for name,attempt in [('bridge_cubic_check',1),('convex_carrier_check',1),('integer_filling_check',2)]:
        src=base/f'{name}.ATTEMPT{attempt}_SOURCE.py'
        data=json.loads((base/f'{name}.ATTEMPT{attempt}.stdout.json').read_text())
        identity=data.get('source_sha256',data.get('input_sha256',{}).get(name+'.py'))
        assert identity==sha(src)
        if name=='convex_carrier_check':
            assert data['input_sha256']['bridge_cubic_check.py']==sha(base/'bridge_cubic_check.ATTEMPT1_SOURCE.py')
        histories.append(dict(source=src.name,sha256=sha(src),status='previous_success_preserved'))
    for name in ('integer_filling_check','run_formula_faults'):
        src=base/f'{name}.ATTEMPT1_SOURCE.py'
        diagnostic=json.loads((base/f'{name}.ATTEMPT1.diagnostic.json').read_text())
        assert diagnostic['source_sha256']==sha(src)
        assert (base/f'{name}.ATTEMPT1.stderr.txt').read_text()
        histories.append(dict(source=src.name,sha256=sha(src),status='failed_attempt_preserved'))
    py=sorted(pack.rglob('*.py'))
    compiled=subprocess.run(['python3','-m','py_compile',*[str(x) for x in py]],capture_output=True,text=True)
    assert compiled.returncode==0,compiled.stderr
    links=[];md=sorted(pack.rglob('*.md'))
    for file in md:
        for target in re.findall(r'\[[^\]]*\]\(([^)]+)\)',file.read_text()):
            if re.match(r'https?://',target) or target.startswith('#'):continue
            assert not target.startswith('/')
            resolved=(file.parent/target.split('#')[0]).resolve()
            assert resolved.is_relative_to(repo) and resolved.is_file(),(file,target)
            links.append(dict(source=str(file.relative_to(pack)),target=target))
    run=subprocess.run(['git','diff','--check','--cached'],cwd=repo,capture_output=True,text=True)
    assert run.returncode==0,run.stdout+run.stderr
    report=dict(status='FOCUSED_AUTHOR_CHECKS_COMPLETED',primary=evidence,histories=histories,
                formula_fault_count=len(faults['cases']),compiled_python_count=len(py),
                markdown_count=len(md),relative_links=links,
                limitations='No independent review, canonical cache/readiness, formal N-gate or integrated landing-pipeline PASS.')
    (pack/'review/FOCUSED_VERIFY.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))


if __name__=='__main__':main()
