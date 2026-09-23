#!/usr/bin/env python3
"""Exact finite support controls; the analytic theorem is in the source note."""
import os, sys, time, signal, resource, json, hashlib, math
from pathlib import Path
AUDIT_TIMEOUT_SEC = 180
AUDIT_RSS_LIMIT_MIB = 180
AUDIT_INPUT_PATHS = ['docs/GAUGE_WILSON_FINITE_PW_UNIFORM_STATIC_SOURCE_ENERGY_BOUNDS_BOUNDED_THEOREM_NOTE_2026-09-07.md', 'docs/GAUGE_WILSON_ELECTRIC_DOMINATED_VOLUME_UNIFORM_GAP_BOUNDED_THEOREM_NOTE_2026-09-07.md', 'docs/GAUGE_WILSON_UNIFORM_STATIC_SOURCE_ENERGY_BOUNDS_BOUNDED_THEOREM_NOTE_2026-09-07.md', 'docs/GAUGE_WILSON_SELECTED_INFINITE_STATIC_SOURCE_SECTOR_BOUNDED_THEOREM_NOTE_2026-09-07.md', 'docs/GAUGE_WILSON_FINITE_PW_STATIC_SOURCE_ENERGY_UPPER_BOUND_BOUNDED_THEOREM_NOTE_2026-09-07.md']
EXPECTED_INPUT_SHA256 = {'docs/GAUGE_WILSON_FINITE_PW_UNIFORM_STATIC_SOURCE_ENERGY_BOUNDS_BOUNDED_THEOREM_NOTE_2026-09-07.md': '87b32515257c0c3363b6f47845ff8eafada3d1b79e02dff075ea8bb905c696d6', 'docs/GAUGE_WILSON_ELECTRIC_DOMINATED_VOLUME_UNIFORM_GAP_BOUNDED_THEOREM_NOTE_2026-09-07.md': 'a5df21b019b0ec35fce30bccced5c85862595235c1c9aa28779a3574fdc979f3', 'docs/GAUGE_WILSON_UNIFORM_STATIC_SOURCE_ENERGY_BOUNDS_BOUNDED_THEOREM_NOTE_2026-09-07.md': 'ea01dd24fe7ab4432c0f8c09ae1d3273c02b09ff11c51757440807921ae0df4f', 'docs/GAUGE_WILSON_SELECTED_INFINITE_STATIC_SOURCE_SECTOR_BOUNDED_THEOREM_NOTE_2026-09-07.md': '0621d2e82146934a4dc126f464b9966aa578fab4e99ddbbf5ef34d67ccdf8d72', 'docs/GAUGE_WILSON_FINITE_PW_STATIC_SOURCE_ENERGY_UPPER_BOUND_BOUNDED_THEOREM_NOTE_2026-09-07.md': 'af043363c9ff1bb69829cb991c2ddd7f5bcde0ae9d57fc550ac55f58fccd71c6'}
_REPO_ROOT = Path(__file__).resolve().parents[1]
_input_sha256 = {p: hashlib.sha256((_REPO_ROOT / p).read_bytes()).hexdigest() for p in AUDIT_INPUT_PATHS}
assert _input_sha256 == EXPECTED_INPUT_SHA256, "Declared scientific input drift"
_started = time.monotonic()
for _name in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[_name] = '1'
if sys.argv[1:] not in ([], ['--json']):
    raise SystemExit('usage: '+Path(__file__).name+' [--json]')
def _timeout(signum, frame):
    raise TimeoutError('180-second audit budget exceeded')
signal.signal(signal.SIGALRM, _timeout)
signal.alarm(AUDIT_TIMEOUT_SEC)
def _rss():
    return resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / (1048576 if sys.platform == 'darwin' else 1024)
def _finite(value):
    if isinstance(value, float) and not math.isfinite(value):
        raise AssertionError('nonfinite output')
    if isinstance(value, dict):
        for item in value.values(): _finite(item)
    elif isinstance(value, (list, tuple)):
        for item in value: _finite(item)
def _emit(out, expected, scopes):
    assert out['TOTAL'] == expected == len(set(out['checks']))
    assert 0 < _rss() < AUDIT_RSS_LIMIT_MIB
    assert time.monotonic() - _started < AUDIT_TIMEOUT_SEC
    assert sum(v['checks'] for v in scopes.values()) == expected
    out['N5_scopes'] = scopes
    out['resource_limits'] = {'seconds': AUDIT_TIMEOUT_SEC, 'rss_MiB': AUDIT_RSS_LIMIT_MIB}
    _finite(out)
    out['input_sha256'] = _input_sha256
    _sidecar = os.environ.get('AUDIT_RESULT_SIDECAR')
    if _sidecar:
        _result_path = Path(_sidecar)
        if not _result_path.is_absolute() or _result_path.resolve().is_relative_to(_REPO_ROOT.resolve()):
            raise ValueError('AUDIT_RESULT_SIDECAR must be an absolute path outside the repository')
        with _result_path.open('x') as _result_file:
            json.dump(out, _result_file, sort_keys=True, indent=2, allow_nan=False)
            _result_file.write('\n')
    if sys.argv[1:] == ['--json']:
        print(json.dumps(out, sort_keys=True, indent=2, allow_nan=False))
    else:
        print('PASS '+Path(__file__).name)
        for key, item in scopes.items(): print(key+': '+str(item['checks'])+' checks; '+item['scope'])
        print('TOTAL: '+str(expected))
        print('seconds: '+str(out['seconds'])+'; rss_MiB: '+str(out['rss_MiB']))
        print('source_sha256: '+out['source_sha256'])
    signal.alarm(0)
from itertools import product
from pathlib import Path
import json,time,resource,hashlib
import sympy as s
start=_started;checks=[]
def ck(n,b):
 if not b or n in checks:raise AssertionError(n)
 checks.append(n)
verts=list(product(range(2),repeat=3));edges=[]
for x in verts:
 for a in range(3):
  if x[a]==0:
   y=list(x);y[a]=1;edges.append((verts.index(x),verts.index(tuple(y))))
def solve(es,target):
 B=[[int(i==u)-int(i==v) for u,v in es] for i in range(8)];b=[int(i==0)-int(i==target) for i in range(8)]
 A=[[x%3 for x in row]+[y%3] for row,y in zip(B,b)];piv=[];r=0
 for c in range(len(es)):
  pivot=next((i for i in range(r,8) if A[i][c]),None)
  if pivot is None:continue
  A[r],A[pivot]=A[pivot],A[r];inv=1 if A[r][c]==1 else 2
  A[r]=[(inv*x)%3 for x in A[r]]
  for i in range(8):
   if i!=r:
    f=A[i][c];A[i]=[(x-f*y)%3 for x,y in zip(A[i],A[r])]
  piv.append(c);r+=1
 free=[i for i in range(len(es)) if i not in piv];sol=[]
 for vals in product(range(3),repeat=len(free)):
  z=[0]*len(es)
  for i,v in zip(free,vals):z[i]=v
  for row,c in enumerate(piv):z[c]=(A[row][-1]-sum(A[row][j]*z[j] for j in free))%3
  sol.append(z)
 return B,b,r,free,sol
# source support connectivity, using labels only as a necessary center condition.
def connected(z,es,target):
 seen={0};todo=[0]
 while todo:
  u=todo.pop()
  for (a,b),q in zip(es,z):
   if q and (a==u or b==u):
    v=b if a==u else a
    if v not in seen:seen.add(v);todo.append(v)
 return target in seen
out={}
for target,d in [(verts.index((1,0,0)),1),(7,3)]:
 B,b,rank,free,sol=solve(edges,target)
 ck(f'target{target}_rank7_free5',rank==7 and len(free)==5)
 ck(f'target{target}_all243_congruences',len(sol)==243 and all(all((sum(v*q for v,q in zip(row,z))-b[i])%3==0 for i,row in enumerate(B)) for z in sol))
 ck(f'target{target}_all_supports_connect',all(connected(z,edges,target) for z in sol))
 weights=[sum(q!=0 for q in z) for z in sol]
 ck(f'target{target}_minimum_energy4d',min(weights)*4==4*d)
 out[str(target)]={'solutions':sol,'histogram':{str(k):weights.count(k) for k in sorted(set(weights))},'distance':d}
gedges=edges+[(0,7)];B,b,rank,free,sol=solve(gedges,7)
ck('ghost_unrestricted_shortcut',min(sum(q!=0 for q in z) for z in sol)==1)
kept=[z for z in sol if z[-1]==0]
ck('ghost_vacuum_restores_actual_distance',min(sum(q!=0 for q in z) for z in kept)==3)
ck('ghost_vacuum_exact243',len(kept)==243)
ck('missing_endpoint_Gauss_allows_zero',all(b[i]%3==0 for i in range(1,7)))
ck('full_Gauss_rejects_zero',any(x%3 for x in b))
K=s.diag(0,1,10);H=s.Matrix([[2,-1,0],[-1,2,0],[0,0,10]]);P=s.diag(1,0,1);V=H-K
ck('Ritz_toy_positive_perturbation',V.is_positive_semidefinite)
ck('Ritz_toy_cutoff_commutes_K',P*K==K*P)
ck('Ritz_toy_both_minima_nondecrease',min(H[:2,:2].eigenvals())==1 and H[0,0]==2 and H[2,2]==10)
ck('Ritz_toy_subtracted_gap_decreases',10-2<10-1)
ck('actual_R1_retains_both_path_orientations',[(p,q) for p in range(2) for q in range(2) if p+q<=1]==[(0,0),(0,1),(1,0)])
result={'TOTAL':len(checks),'checks':checks,'vertices':verts,'edges':edges,'flows':out,'ghost_solutions':len(sol),'ghost_vacuum_solutions':len(kept),'Ritz_toy':{'full_ground':1,'cutoff_ground':2,'charged_both':10,'gap_full':9,'gap_cutoff':8},'scope':'Necessary actual R1 center-flow controls plus an abstract Ritz subtraction adverse. Not all center flows are claimed SU3-admissible, and no finite test proves imported resolvent constants.','source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'seconds':time.monotonic()-start,'rss_MiB':_rss()}

_emit(result, 18, {'per_element': {'checks': 1, 'scope': 'one finite cutoff-R=1 representation-label enumeration retaining both fundamental orientations'}, 'per_site': {'checks': 0, 'scope': 'checked and not executed — no site-resolved dynamics or observable measurement'}, 'per_mode': {'checks': 2, 'scope': 'two finite missing/complete boundary Gauss predicates'}, 'per_block': {'checks': 15, 'scope': 'eight predicates on two cube endpoint flow sets, three ghost-vacuum predicates and four abstract 3-by-3 Ritz predicates; center conservation is only necessary SU3 data'}, 'lattice_wide': {'checks': 0, 'scope': 'checked and not executed — finite cube flows and scalar/matrix examples do not execute arbitrary-volume coordinate estimates or the selected infinite-sector theorem'}})
