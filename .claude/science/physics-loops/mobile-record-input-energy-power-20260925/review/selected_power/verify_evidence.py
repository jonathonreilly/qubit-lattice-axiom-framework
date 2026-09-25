#!/usr/bin/env python3
from collections import Counter
from fractions import Fraction
from datetime import datetime,timezone
import hashlib,json,subprocess
from pathlib import Path

HERE=Path(__file__).resolve().parent
def sha(raw):return hashlib.sha256(raw).hexdigest()
def read(name):return json.loads((HERE/name).read_text())
pins=read('SOURCE_PINS.json')
origins=[]
for row in pins['sources']:
 raw=Path(row['origin']).read_bytes();frozen=(HERE/row['frozen_path']).read_bytes()
 assert raw==frozen and len(raw)==row['bytes'] and sha(raw)==row['sha256']
 origins.append(dict(origin=row['origin'],sha256=row['sha256'],unchanged=True))
git_rows=[]
for row in pins['sources'][:3]:
 rel='docs/'+Path(row['origin']).name
 raw=subprocess.check_output(['git','show',pins['original_main_revision']+':'+rel],cwd=HERE.parent/'campaign-working')
 assert sha(raw)==row['sha256']
 git_rows.append(dict(commit=pins['original_main_revision'],path=rel,sha256=sha(raw)))
scripts={sha(p.read_bytes()):str(p.name) for p in HERE.glob('*.py')}
executions=[]
for path in sorted(HERE.glob('*.execution.json')):
 receipt=json.loads(path.read_text());label=path.name[:-len('.execution.json')]
 assert receipt['script_sha256'] in scripts
 for stream in ('stdout','stderr'):
  raw=(HERE/(label+'.'+stream+'.txt')).read_bytes()
  assert len(raw)==receipt[stream+'_bytes'] and sha(raw)==receipt[stream+'_sha256']
 if label=='verify':
  assert receipt['exit_code']==1 and receipt['stderr_bytes']>0
  assert scripts[receipt['script_sha256']]=='verify_evidence.initial_uniform_pair_count.py'
 else:assert receipt['exit_code']==0 and receipt['stderr_bytes']==0
 executions.append(dict(label=label,source_version=scripts[receipt['script_sha256']],
   source_sha256=receipt['script_sha256'],elapsed_seconds=receipt['elapsed_seconds'],
   stdout_bytes=receipt['stdout_bytes'],stderr_bytes=receipt['stderr_bytes'],exit_code=receipt['exit_code']))
def key(flow,L=None):
 out=Counter()
 for row in flow:
  a=tuple(row['a']);b=tuple(row['b'])
  if L:a=tuple(x%L for x in a);b=tuple(x%L for x in b)
  out[a,b]+=row['shift']
 return tuple(sorted((e,n) for e,n in out.items() if n))
def poly(rows,L=None):return Counter({key(row['flow'],L):row['coefficient'] for row in rows})
def winding(f,L):
 total=[0,0,0]
 for (a,b),n in f:
  for i in range(3):
   d=b[i]-a[i]
   if L:d=d-L if d>L//2 else d+L if d<-L//2 else d
   total[i]+=n*d
 return tuple(total)
def rdict(answer,L=None):
 out={}
 for row in answer['r4']:
  a=tuple(row['a']);b=tuple(row['b'])
  if L:a=tuple(x%L for x in a);b=tuple(x%L for x in b)
  out[a,b]=Fraction(row['numerator'],4*row['denominator'])
 return out
polynomials=[]
for name in ('infinite_RESULTS.json','L6_RESULTS.json','L16_RESULTS.json'):
 payload=read(name);assert payload['code_sha256'] in scripts
 for answer in payload['answers']:
  p=poly(answer['twice_power_laurent']);g=poly(answer['twice_gain_local_laurent']);loss=poly(answer['twice_minus_anticommutator_local_laurent'])
  for f in set(p)|set(g)|set(loss):assert p.get(f,0)==g.get(f,0)+loss.get(f,0)
  for f,n in p.items():
   assert p.get(tuple((e,-v) for e,v in f))==n
   div=Counter()
   for (a,b),v in f:div[a]+=v;div[b]-=v
   assert not any(div.values())
  assert sum(n for f,n in p.items() if winding(f,payload['side'])==(0,0,0))==0
  inventory=answer['pair_inventory']
  expected_pairs=261 if payload['side']==6 else 264
  assert len(inventory)==expected_pairs==payload['local_pairs'] and all(row['power2_coefficient_sum']==0 for row in inventory)
  assert sum(row['gain_flat_diagonal'] for row in inventory)==answer['local_output_H4_flat']
  polynomials.append(dict(source=name,sigma=answer['sigma'],terms=len(p),pairs=len(inventory),
      changed_pairs=answer['changed_pairs'],nonzero_winding_terms=answer['nonzero_winding_terms']))
inf=read('infinite_RESULTS.json')['answers'][0];six=read('L6_RESULTS.json')['answers'][0]
ell={((0,0,0),(1,0,0)):1,((1,1,0),(1,0,0)):-1,((1,1,0),(0,1,0)):1,((0,0,0),(0,1,0)):-1}
ri=rdict(inf,6);rs=rdict(six)
for e in set(ri)|set(rs):assert rs.get(e,0)-ri.get(e,0)==Fraction(-3,2)*ell.get(e,0)
pi=poly(inf['twice_power_laurent'],6);ps=poly(six['twice_power_laurent'])
diff={f:ps.get(f,0)-pi.get(f,0) for f in set(ps)|set(pi) if ps.get(f,0)!=pi.get(f,0)}
assert len(diff)==7 and sum(winding(f,6)!=(0,0,0) for f in diff)==4
assert {f:n for f,n in diff.items() if winding(f,6)==(0,0,0)}=={():-6,tuple(sorted(ell.items())):3,tuple(sorted((e,-n) for e,n in ell.items())):3}
jet=read('JET_CHECK_RESULTS.json')
rjet={(tuple(row['a']),tuple(row['b'])):Fraction(row['value'],4) for row in jet['r4']}
assert rjet==rdict(inf) and len(rjet)==67
assert jet['t0']==164 and jet['h0_output_local']==-11708
assert sum(ell.get(e,0)*n for e,n in rjet.items())==6200
assert sum((rjet.get(e,0)-1675*ell.get(e,0))**2 for e in set(rjet)|set(ell))==227520
matrix=read('DIRECT_MATRIX_RESULTS.json')
assert matrix['full_H4_pairs']==972 and len(matrix['samples'])==8
assert max(abs(row['difference']) for row in matrix['samples'])<5.01e-12
old=read('FOURIER_CORRESPONDENCE_INITIAL_RESULTS.json');new=read('FOURIER_CORRESPONDENCE_RESULTS.json')
changed=[]
for i,(before,after) in enumerate(zip(old['numeric'],new['numeric'])):
 for name in before:
  if before[name]!=after[name]:changed.append((before['L'],name))
assert changed==[(6,'output_flat_H4'),(6,'vacuum_gain_limit_in_kappa_over_tau_units'),(6,'vacuum_anticommutator_subtrahend_limit_in_kappa_over_tau_units')]
assert new['numeric'][0]['output_flat_H4']==-62190
result=dict(verified_utc=datetime.now(timezone.utc).isoformat(),source_origins=origins,git_source_identities=git_rows,
  logged_executions=executions,exact_polynomial_checks=polynomials,jet_coefficients_verified=67,
  side6_haar_difference='Q6-Qinfinite = -3+3 cos(ell.A) after Haar averaging; r6-r=-(3/2)ell',
  direct_matrix_max_error=max(abs(row['difference']) for row in matrix['samples']),
  preserved_correction=dict(initial_result='FOURIER_CORRESPONDENCE_INITIAL_RESULTS.json',changed_fields=changed,
    reason='Use actual side-six +7146 full born diagonal offset; large-lift +7152 does not apply there.'),
  no_author_code_read_imported_or_run=True,no_other_active_packets_read=True)
with (HERE/'EVIDENCE_VERIFICATION.json').open('x') as f:json.dump(result,f,indent=2);f.write('\n')
print(json.dumps(result,indent=2))
