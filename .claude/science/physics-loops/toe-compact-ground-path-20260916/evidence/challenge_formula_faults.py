#!/usr/bin/env python3
"""Run specified formula faults in frozen scratch copies; keep actual failures.

Reads the three package-local checker sources and writes mutant sources and
raw stdout/stderr under this evidence directory. No external scientific input
or audit cache is read or modified. These are author sensitivity checks.
"""
AUDIT_TIMEOUT_SEC = 120
from pathlib import Path
import hashlib
import json
import subprocess
import sys
import time


CASES=[
 ('reflected_face_orientation','block01_geometry_and_rotor_check.py',
  'ans[(y, i)] -= 1','ans[(y, i)] += 1'),
 ('trial_variance','block01_geometry_and_rotor_check.py',
  'v = 1/3 - 2/math.pi**2','v = 1/3 - 1/math.pi**2'),
 ('plaquette_diffusivity','block01_geometry_and_rotor_check.py',
  'diag = 2*g*g*n*n + 1/(g*g)','diag = .5*g*g*n*n + 1/(g*g)'),
 ('reduced_clock_edge_count','block02_reflection_and_path_check.py',
  'r*(2*single+pair).toarray()','r*(single+pair).toarray()'),
 ('shared_boundary_reflection','block02_reflection_and_path_check.py',
  'reflected=[0,3,2,7,6,11,10]','reflected=[0,3,2,6,7,11,10]'),
 ('constrained_path_kernel','block02_reflection_and_path_check.py',
  'K=heat-np.diag([math.exp(-r*T),0])','K=heat-np.diag([.5*math.exp(-r*T),0])'),
 ('ground_path_diffusivity','block02_reflection_and_path_check.py',
  'g*g*n*n/2+1/(g*g)','2*g*g*n*n+1/(g*g)'),
 ('binary_clock_tail_coefficient','block02_reflection_and_path_check.py',
  'r=4*g*g;v=1/(g*g)','r=2*g*g;v=1/(g*g)'),
 ('cochain_boundary_sign','block03_coarse_current_check.py',
  'sum((-1)**r*(form','sum((1)**r*(form'),
 ('dual_current_Hodge_sign','block03_coarse_current_check.py',
  'dual={(x,i):(-1)**i*J','dual={(x,i):(1)**i*J'),
 ('current_witness_exponent','block03_coarse_current_check.py',
  'p=min(1,6*mp.exp(logstar/24))','p=min(1,6*mp.exp(logstar/12))'),
]


def main():
    root=Path(__file__).resolve().parent
    scratch=root/'formula_faults';scratch.mkdir(exist_ok=True)
    start=time.monotonic();rows=[]
    for name,filename,old,new in CASES:
        source=root/filename;raw=source.read_bytes();text=raw.decode()
        assert text.count(old)==1,(name,text.count(old))
        changed=text.replace(old,new,1)
        path=scratch/(name+'.py');path.write_text(changed)
        run=subprocess.run([sys.executable,str(path)],cwd=root.parent.parent.parent.parent.parent,
                           capture_output=True,text=True,timeout=120)
        path.with_suffix('.stdout.txt').write_text(run.stdout)
        path.with_suffix('.stderr.txt').write_text(run.stderr)
        assert run.returncode!=0,(name,'fault survived')
        assert 'AssertionError' in run.stderr or 'KeyError' in run.stderr,(name,run.stderr)
        rows.append(dict(name=name,source=filename,source_sha256=hashlib.sha256(raw).hexdigest(),
                         mutant_sha256=hashlib.sha256(path.read_bytes()).hexdigest(),
                         old=old,new=new,returncode=run.returncode,
                         final_error_line=run.stderr.strip().splitlines()[-1]))
    ans=dict(source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
             status='ALL_SPECIFIED_FAULTS_REJECTED',elapsed_seconds=time.monotonic()-start,
             cases=rows,
             limitations='No fault test proves its parent theorem; check actual failing line before assigning sensitivity to a later assertion.')
    print(json.dumps(ans,indent=2,sort_keys=True))


if __name__=='__main__':main()
