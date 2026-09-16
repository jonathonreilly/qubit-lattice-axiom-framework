#!/usr/bin/env python3
"""Verify current author-source receipts and local packet integrity, not science."""
AUDIT_TIMEOUT_SEC=120
from pathlib import Path
import hashlib,json,re,subprocess


def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    pack=Path(__file__).resolve().parents[1];repo=pack.parents[3]
    evidence=pack/'evidence';pairs=[]
    specifications=[('sparse_loop_counterexample_check',2),('compact_cover_source_check',1),('compact_score_check',2)]
    for stem,attempt in specifications:
        source=evidence/(stem+'.py');out=evidence/(stem+'.FINAL.stdout.json');err=evidence/(stem+'.FINAL.stderr.txt')
        obj=json.loads(out.read_text())
        assert obj['source_sha256']==sha(source)
        assert obj['status']=='PERSONAL_CHECKS_COMPLETED' and not err.read_bytes()
        assert out.read_bytes()==(evidence/f'{stem}.ATTEMPT{attempt}.stdout.json').read_bytes()
        assert err.read_bytes()==(evidence/f'{stem}.ATTEMPT{attempt}.stderr.txt').read_bytes()
        assert 'AUDIT_TIMEOUT_SEC=120' in source.read_text()
        pairs.append(dict(source=source.relative_to(pack).as_posix(),source_sha256=sha(source),stdout_sha256=sha(out),stderr_sha256=sha(err)))
    faults=json.loads((evidence/'formula_faults.ATTEMPT2.stdout.json').read_text())
    assert faults['harness_sha256']==sha(evidence/'run_formula_faults.py')
    assert len(faults['faults'])==9
    for row in faults['faults']:
        src=pack/row['source'];stderr=src.parent/'stderr.txt'
        assert sha(src)==row['sha256'] and sha(stderr)==row['stderr_sha256']
        assert sha(evidence/src.name)==row['original_sha256']
        assert row['returncode']!=0 and b'AssertionError' in stderr.read_bytes()
    prior=pack/'review/initial_box_separation'
    prior_obj=json.loads((prior/'sparse_loop_counterexample_check.ATTEMPT1.stdout.json').read_text())
    assert prior_obj['source_sha256']==sha(prior/'sparse_loop_counterexample_check.py')
    old_fault_root=pack/'review/formula_faults_before_separation'
    old_faults=json.loads((old_fault_root/'run.stdout.json').read_text())
    for row in old_faults['faults']:
        src=old_fault_root/row['name']/Path(row['source']).name
        assert sha(src)==row['sha256']
        assert sha(src.parent/'stderr.txt')==row['stderr_sha256']
    old=pack/'review/initial_score_refinement_failure/compact_score_check.py'
    assert 'for N in (2,3):' in old.read_text()
    assert 'assert delta<.003' in old.read_text() and 'assert delta<.003' in (evidence/old.name).read_text()
    assert b'assert delta<.003' in (old.parent/'compact_score_check.ATTEMPT1.stderr.txt').read_bytes()
    syntax=[]
    for f in sorted(pack.rglob('*.py')):
        compile(f.read_text(),str(f),'exec');syntax.append(f.relative_to(pack).as_posix())
    links=[]
    report=pack/'review/FOCUSED_VERIFY.json'
    current_markdown=list(pack.glob('*.md'))+list((pack/'notes').glob('*.md'))+list((pack/'review').glob('*.md'))
    for f in sorted(current_markdown):
        for target in re.findall(r'\[[^\]]*\]\(([^)]+)\)',f.read_text()):
            if '://' in target or target.startswith('#'):continue
            candidate=(f.parent/target.split('#')[0]).resolve()
            assert candidate.exists() or candidate==report,(f,target)
            links.append(dict(source=f.relative_to(pack).as_posix(),target=target))
    authored=list(pack.glob('*.md'))+list((pack/'notes').glob('*.md'))+list((pack/'review').glob('*.md'))+list(evidence.glob('*.py'))+[Path(__file__)]
    result=subprocess.run(['python3',str(repo/'scripts/vocab_lint.py'),'--report-only',*[str(p) for p in authored]],capture_output=True,text=True,check=True)
    (pack/'review/VOCAB_FINAL.stdout.txt').write_text(result.stdout)
    (pack/'review/VOCAB_FINAL.stderr.txt').write_text(result.stderr)
    assert '0 files with violations' in result.stdout
    subprocess.run(['git','diff','--check'],cwd=repo,check=True)
    obj=dict(status='AUTHOR_SOURCE_INTEGRITY_CHECKED',source_sha256=sha(Path(__file__)),primary_pairs=pairs,
             rejected_formula_faults=9,preserved_failed_refinement_source_sha256=sha(old),
             syntax_files=syntax,relative_links=links,historical_links='Original copied note retains its original relative-link context; only current authored Markdown is link-checked.',scope='No independent review, audit cache, formal N-packet or integration pipeline is asserted.')
    report.write_text(json.dumps(obj,indent=2)+'\n')
    print(json.dumps(dict(status=obj['status'],primary_pairs=len(pairs),formula_faults=9,compiled_python=len(syntax),relative_links=len(links))))


if __name__=='__main__':main()
