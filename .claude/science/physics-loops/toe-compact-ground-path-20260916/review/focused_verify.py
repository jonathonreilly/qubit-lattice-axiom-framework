#!/usr/bin/env python3
"""Focused branch-pack checks; no scientific or audit verdict is issued."""
AUDIT_TIMEOUT_SEC = 120
from pathlib import Path
import ast
import hashlib
import json
import re
import subprocess


def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()


def main():
    pack=Path(__file__).resolve().parents[1]
    repo=pack.parents[3]
    programs=['block01_geometry_and_rotor_check','block02_reflection_and_path_check','block03_coarse_current_check']
    evidence=[]
    for name in programs:
        source=pack/'evidence'/(name+'.py')
        output=pack/'evidence'/(name+'.FINAL.stdout.json')
        err=pack/'evidence'/(name+'.FINAL.stderr.txt')
        data=json.loads(output.read_text())
        assert data['source_sha256']==sha(source)
        assert data['status']=='PERSONAL_CHECKS_COMPLETED'
        assert err.read_text()==''
        tree=ast.parse(source.read_text())
        timeout=[n.value.value for n in tree.body if isinstance(n,ast.Assign)
                 and any(isinstance(t,ast.Name) and t.id=='AUDIT_TIMEOUT_SEC' for t in n.targets)]
        assert timeout==[120]
        evidence.append(dict(source=str(source.relative_to(pack)),sha256=sha(source),output_sha256=sha(output)))
    faults=json.loads((pack/'evidence/challenge_formula_faults.ATTEMPT1.stdout.json').read_text())
    assert faults['source_sha256']==sha(pack/'evidence/challenge_formula_faults.py')
    assert len(faults['cases'])==11
    for row in faults['cases']:
        assert row['source_sha256']==sha(pack/'evidence'/row['source'])
        mutant=pack/'evidence/formula_faults'/(row['name']+'.py')
        assert row['mutant_sha256']==sha(mutant)
        assert row['returncode']!=0
        stderr=mutant.with_suffix('.stderr.txt').read_text()
        assert 'AssertionError' in stderr or 'KeyError' in stderr
    py=sorted(pack.rglob('*.py'))
    compiled=subprocess.run(['python3','-m','py_compile',*[str(x) for x in py]],capture_output=True,text=True)
    assert compiled.returncode==0,compiled.stderr
    links=[]
    md=sorted(pack.rglob('*.md'))
    for file in md:
        for target in re.findall(r'\[[^\]]*\]\(([^)]+)\)',file.read_text()):
            if re.match(r'https?://',target) or target.startswith('#'):continue
            assert not target.startswith('/')
            resolved=(file.parent/target.split('#')[0]).resolve()
            assert resolved.is_relative_to(repo) and resolved.is_file(),(file,target)
            links.append(dict(source=str(file.relative_to(pack)),target=target))
    run=subprocess.run(['git','diff','--check','--cached'],cwd=repo,capture_output=True,text=True)
    assert run.returncode==0,run.stdout+run.stderr
    report=dict(status='FOCUSED_AUTHOR_CHECKS_COMPLETED',primary=evidence,
                formula_fault_count=len(faults['cases']),compiled_python_count=len(py),
                markdown_count=len(md),relative_links=links,
                limitations='No independent review, canonical cache/readiness, N-gate or integrated landing-pipeline PASS.')
    dest=pack/'review/FOCUSED_VERIFY.json';dest.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))


if __name__=='__main__':main()
