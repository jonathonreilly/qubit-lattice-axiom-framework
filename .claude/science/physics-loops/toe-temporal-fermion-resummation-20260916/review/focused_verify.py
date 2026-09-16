#!/usr/bin/env python3
"""Focused pack checks, not canonical runner evidence or an audit verdict."""
import datetime,hashlib,json,re,subprocess
from pathlib import Path

PACK=Path(__file__).resolve().parents[1]
REPO=PACK.parents[3]
PRIMARY=[
 ('block01_temporal_resummation_check.py','BLOCK01_TEMPORAL_RESUMMATION_ATTEMPT1'),
 ('block02_physical_curl_hessian_check.py','BLOCK02_CURL_HESSIAN_ATTEMPT1'),
 ('block03_open_boundary_hamiltonian_check.py','BLOCK03_OPEN_HAMILTONIAN_ATTEMPT1'),
 ('block04_dynamical_gauge_join_check.py','BLOCK04_DYNAMICAL_GAUGE_ATTEMPT3'),
 ('block05_integer_local_filling_check.py','BLOCK05_INTEGER_FILLING_ATTEMPT2'),
 ('block06_third_curl_variation_check.py','BLOCK06_THIRD_VARIATION_ATTEMPT1'),
]

def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()

def run():
    rows=[]
    for source,stem in PRIMARY:
        p=PACK/'evidence'/source;out=PACK/'evidence'/(stem+'.stdout.txt');err=PACK/'evidence'/(stem+'.stderr.txt')
        data=json.loads(out.read_text());sha=digest(p)
        assert data['source_sha256']==sha,(source,'stale successful output')
        assert err.stat().st_size==0,(source,'nonempty final stderr')
        rows.append({'source':source,'source_sha256':sha,'output':out.name,'output_sha256':digest(out)})
    mutations=[]
    for harness,stem in [('challenge_blocks01_03.py','BLOCKS01_03_MUTATIONS_ATTEMPT1'),('challenge_blocks04_06.py','BLOCKS04_06_MUTATIONS_ATTEMPT2')]:
        data=json.loads((PACK/'evidence'/(stem+'.stdout.txt')).read_text())
        assert data['harness_sha256']==digest(PACK/'evidence'/harness)
        assert (PACK/'evidence'/(stem+'.stderr.txt')).stat().st_size==0
        for row in data['formula_faults']:
            assert row['assertion_rejected'] and row['exit_code']!=0,row['fault']
            assert row['original_sha256']==digest(PACK/'evidence'/row['original_source'])
        mutations.append({'harness':harness,'faults_rejected':len(data['formula_faults']),'output':stem+'.stdout.txt'})
    py=sorted(PACK.rglob('*.py'))
    for p in py:compile(p.read_text(),str(p),'exec')
    links=[];md=sorted(PACK.rglob('*.md'))
    for p in md:
        for target in re.findall(r'\]\(([^)]+)\)',p.read_text()):
            if '://' in target or target.startswith('#'):continue
            target=target.split('#',1)[0]
            if not target:continue
            q=(p.parent/target).resolve();assert q.exists(),(str(p),target)
            links.append({'source':str(p.relative_to(PACK)),'target':target})
    diff=subprocess.run(['git','diff','--check','e0ef7cf4633034a8c1e6d57f5812cc4275bf1349','--',str(PACK)],cwd=REPO,capture_output=True,text=True)
    assert diff.returncode==0,diff.stdout+diff.stderr
    report={'checked_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'kind':'focused author verification; no canonical audit status','primary_hash_receipts':rows,'mutation_receipts':mutations,'python_files_compiled':len(py),'markdown_files_checked':len(md),'relative_links_checked':links,'base_diff_check':{'exit_code':diff.returncode,'stdout':diff.stdout,'stderr':diff.stderr},'vocab_report':'FOCUSED_VOCAB.stdout.txt','registration_and_integrated_audit':'pending'}
    (PACK/'review/FOCUSED_VERIFICATION.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({'primary_sources':len(rows),'final_fault_tests':sum(r['faults_rejected'] for r in mutations),'compiled_python_files':len(py),'markdown_files':len(md),'relative_links':len(links),'base_diff_check':diff.returncode},indent=2))

if __name__=='__main__':run()
