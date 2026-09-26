#!/usr/bin/env python3
"""Post-seal selective source comparison; no primary checker execution."""
from pathlib import Path
from itertools import combinations,permutations,product
import hashlib,json
import numpy as np
import sympy as s
HERE=Path(__file__).resolve().parent
PARENT=HERE.parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
expected={
"MICROSCOPIC_GAUSS_IMPULSE_AND_RECORD_LOOPS.md":"684f10acda3ebf659ed4b1b47e3fbe35a29c92dfbe1fee77e9cd9469b27f0c30",
"microscopic_gauss_record_loop_check.py":"dea415ec4d6be7662efff041bd7e303c03c9b0243548cbc429552f4478f616b9",
"gauss_loop_fugacity_check.py":"f1c6921b5dc887b4de59bbfccee5e5cad1e11dfd97270864472dfdab426908e0",
"MICROSCOPIC_GAUSS_RECORD_LOOP_RESULTS.json":"3d5a46d78fd0958df7d5b79bbdcb6ed15e9ee35decb073989d2d6fd5474987b3",
"GAUSS_LOOP_FUGACITY_RESULTS.json":"1a0d8e2a71b53a28ef574998c7b297f8c7062cffc4b98da616bbe2323c761cdb"}
checks=[]
def check(name,condition,detail=None):
 assert condition,(name,detail)
 checks.append(dict(name=name,detail=detail))
 print("VERIFIED",name,json.dumps(detail,sort_keys=True),flush=True)
sources=[]
for name,digest in expected.items():
 path=PARENT/name;assert sha(path)==digest,name
 sources.append(dict(path=name,sha256=digest,bytes=path.stat().st_size))
seal=json.loads((HERE/'PRE_SOURCE_SEAL.json').read_text())
assert sha(HERE/'PRE_SOURCE_SEAL.json')=="c08bc205347df4c93f12439738293e336361935e6192f2cc1544ee02e67de817"
for row in seal["artifacts"]:
 path=HERE/row["path"];assert sha(path)==row["sha256"] and path.stat().st_size==row["bytes"]
check("blind_bytes_unchanged_and_primary_sources_authenticated",True,dict(blind_artifacts=len(seal["artifacts"]),primary_files=len(sources)))
for filename,source,count in [
 ("MICROSCOPIC_GAUSS_RECORD_LOOP_RESULTS.json","microscopic_gauss_record_loop_check.py",13),
 ("GAUSS_LOOP_FUGACITY_RESULTS.json","gauss_loop_fugacity_check.py",6)]:
 data=json.loads((PARENT/filename).read_text())
 check("authenticated_"+filename,data["source_sha256"]==expected[source] and len(data["checks"])==count and all(c["passed"] for c in data["checks"]),dict(recorded_groups=count,rerun=False))
unit=np.eye(3,dtype=int)
def canonical(records,side):
 return tuple(sorted((tuple(int(a)%side for a in point),tuple(int(a) for a in vector)) for point,vector in records))
def template(i,j,sign=1):
 return [(-unit[j],sign*unit[i]),(unit[i],sign*unit[j]),
         (unit[j],-sign*unit[i]),(-unit[i],-sign*unit[j])]
for side in (5,7):
 family={canonical(template(i,j,sign),side) for i,j in combinations(range(3),2) for sign in (1,-1)}
 actions=0
 for perm in permutations(range(3)):
  parity=(-1)**sum(perm[i]>perm[j] for i in range(3) for j in range(i+1,3))
  for signs in product((-1,1),repeat=3):
   matrix=np.zeros((3,3),dtype=int)
   for col in range(3):matrix[perm[col],col]=signs[col]
   determinant=parity*int(np.prod(signs))
   for axial in (False,True):
    transformed=[(matrix@r,(determinant if axial else 1)*(matrix@v)) for r,v in template(0,1)]
    assert canonical(transformed,side) in family
   actions+=1
 check("exact_template_membership_under_48_cubic_actions_N%d"%side,actions==48,dict(polar_and_axial=True))
sx,sy,sz,beta,kappa,nu=s.symbols("sx sy sz beta kappa nu",real=True)
wave=s.Matrix([sx,sy,sz])
cov=s.zeros(3)
for i,j in combinations(range(3),2):
 amplitude=s.zeros(3,1);amplitude[i]=2*s.I*wave[j];amplitude[j]=-2*s.I*wave[i]
 cov+=2*beta*amplitude*amplitude.conjugate().T
target=8*beta*(wave.dot(wave)*s.eye(3)-wave*wave.T)
check("birth_bracket_normalization_and_two_sector_trace",
 (cov-target).applyfunc(s.expand)==s.zeros(3) and s.expand(2*s.trace(cov)-32*beta*wave.dot(wave))==0,
 dict(empty_population_rate="48 beta",general_population_rate="16 beta sum_planes P(four vacancies)"))
q1,q2,q3=s.symbols("q1 q2 q3",real=True)
center=-2*kappa*sum(1-s.cos(q) for q in (q1,q2,q3))
matrix=center*s.eye(2)+nu*s.Matrix([[-1,1],[1,-1]])
check("isolated_center_and_circulation_modes",
 matrix*s.Matrix([1,1])==center*s.Matrix([1,1]) and matrix*s.Matrix([1,-1])==(center-2*nu)*s.Matrix([1,-1]),
 dict(center_eigenvalue=str(center),orientation_eigenvalue=str(center-2*nu)))
result=dict(scope="Post-seal source comparison and selective checks, distinct from blind reconstruction.",
 primary_sources=sources,checks=checks,source_sha256=sha(Path(__file__)),
 blind_seal_sha256=sha(HERE/'PRE_SOURCE_SEAL.json'),failed_executions=[],
 extra_source_access="None; only the five authorized primary files were read.")
(HERE/'SOURCE_COMPARISON_RESULTS.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
print("POST_SOURCE_GROUPS",len(checks),flush=True)
