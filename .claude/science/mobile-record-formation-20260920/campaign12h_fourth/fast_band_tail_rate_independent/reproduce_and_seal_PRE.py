#!/usr/bin/env python3
from pathlib import Path
import datetime,hashlib,json,os,platform,subprocess,sys,time
import numpy,scipy,sympy
HERE=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
assert not (HERE/'PRE_SEAL.json').exists(),'Refuse to overwrite immutable PRE'
bindings=json.loads((HERE/'SOURCE_BINDINGS.json').read_text())
for row in bindings['sources']:
 p=HERE/row['snapshot'];assert sha(p)==row['sha256'] and p.stat().st_size==row['bytes']
start=time.monotonic()
with (HERE/'LOCAL_RATE.stdout').open('wb') as out,(HERE/'LOCAL_RATE.stderr').open('wb') as err:
 code=subprocess.run([sys.executable,str(HERE/'local_rate_control.py')],cwd=HERE,env={**os.environ,'PYTHONDONTWRITEBYTECODE':'1'},stdout=out,stderr=err).returncode
assert code==0 and not (HERE/'LOCAL_RATE.stderr').read_bytes()
result=json.loads((HERE/'LOCAL_RATE_RESULTS.json').read_text());assert result['all_assertions_passed']
prior=json.loads((HERE/'sources/fast_band_tail_author/EXACT_TAIL_RESULTS.json').read_text())
# Check the entire supplied flat bright-dark certificate by charge labels,
# independently of either builder's enumeration order.
words=[tuple(q) for q in result['charge_order']];index={q:i for i,q in enumerate(words)}
flat={}
for row in prior['bright_dark_Laurent_entries']:
 key=(tuple(prior['bright_words'][row['bright_row']]),tuple(prior['dark_words'][row['dark_column']]))
 flat[key]=flat.get(key,0)+row['coefficient']
checks=0
for q in prior['bright_words']:
 for r in prior['dark_words']:
  key=(tuple(q),tuple(r));assert result['G_zero'][index[key[0]]][index[key[1]]]==flat.get(key,0);checks+=1
for row,old in zip(result['actual_first_marks'],prior['actual_first_mark_flat_fiber_weights']):
 convert=lambda entries:{(tuple(x['q']),tuple(x['E'])):x['coefficient'] for x in entries}
 assert convert(row['physical_R'])==convert(old['physical_R'])
 assert row['b']==old['b'] and row['physical_R_norm_squared']==old['r']
 assert row['flat_projection_squared_normalized']==old['flat_fiber_surviving_normalized_weight']
# Gauss test uses the independently stored actual physical words.
A=(0,3,5,6);B=(1,2,4,7);edges=[(a,b) for a in A for b in B if a^b in (1,2,4)]
for row in result['actual_first_marks']:
 for word in row['physical_R']:
  div=[0]*8
  for (a,b),e in zip(edges,word['E']):div[a]+=e;div[b]-=e
  assert div==[q-int(i in A) for i,q in enumerate(word['q'])]
receipt={'completed_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'python':platform.python_version(),'python_executable':sys.executable,'libraries':{'numpy':numpy.__version__,'scipy':scipy.__version__,'sympy':sympy.__version__},'script':'local_rate_control.py','script_sha256':sha(HERE/'local_rate_control.py'),'exit_code':code,'wall_seconds':time.monotonic()-start,'stdout_sha256':sha(HERE/'LOCAL_RATE.stdout'),'stderr_sha256':sha(HERE/'LOCAL_RATE.stderr'),'result_sha256':sha(HERE/'LOCAL_RATE_RESULTS.json'),'all_1728_prior_flat_certificate_entries_match_new_local_matrix':checks==1728,'actual_physical_first_mark_certificates_match':True,'actual_physical_Gauss_checks_pass':True,'relative_minus_input_discriminator_projection_squared':result['relative_minus_mark_discriminator_projection_squared'],'prior_values_known_before_control':True,'author_new_rate_sources_accessed':False,'unresolved_execution_failures':[]}
(HERE/'EXECUTION_RECEIPT.json').write_text(json.dumps(receipt,indent=2)+'\n')
files=[]
for p in sorted(HERE.rglob('*')):
 if p.is_file():
  assert not p.is_symlink() and '__pycache__' not in p.parts
  files.append({'path':str(p.relative_to(HERE)),'bytes':p.stat().st_size,'sha256':sha(p)})
seal={'stage':'independent PRE; new rate-author comparison not performed','sealed_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'scope':'For each of the three actual zero-field first-mark rotor curves and fixed delta,kappa>0, f_i(tau)>=c_i(1+tau)^(-5/2) with c_i>0, hence no eventual A exp(-a tau) upper bound with finite A,a>0.','argument_sha256':sha(HERE/'PRE_RATE_ARGUMENT.md'),'source_bindings_sha256':sha(HERE/'SOURCE_BINDINGS.json'),'source_count':len(bindings['sources']),'independence':'Prior full-fiber/compact-time sources and expected prior constants were supplied; new rate proof and local matrix code were independently written without importing campaign builders or reading the withheld rate work.','supported':['A weaker (1+tau)^(-5) lower bound follows directly from contractive Duhamel without simple spectral perturbation.','A rank-one local eigenprojection and the original dissipative quadratic form give the (1+tau)^(-5/2) bound.','Exact physical first-mark words, Gauss law, flat null mode, rank23 and nonzero overlaps were reconstructed; all1728 supplied flat coupling entries match.'],'excluded':['Sharp asymptotic, matching upper rate, optimal exponent or constants, complete exceptional-set classification.','Arbitrary-input lower bound, any claim that operator-norm nondecay alone supplies fixed-input rate.','Fixed-positive-physical-time microscopic or finite-spin large-time conclusions, interchange of limits, energy moments, heat/bath/reservoir/selection claims.','Audit/landing verdict, axiom adoption, publication or new rate-author source comparison.'],'failures_and_limits':['The relative-minus alternative coherent input has zero flat overlap and is excluded; the proof does not claim its rate.','Numerical near-fiber samples are illustrations, not a proof or fit of a sharp exponent.','The full physical Gauss representation and global Laurent identity remain explicitly supplied dependencies.','Ordinary repository-wide no-go/landing workflow is outside the authorized source-isolated PRE; no formal packet-validator PASS is claimed.'],'unresolved_scientific_obligations_for_stated_lower_bound':[],'unresolved_execution_failures':[],'files':files}
(HERE/'PRE_SEAL.json').write_text(json.dumps(seal,indent=2)+'\n')
for row in files:
 p=HERE/row['path'];assert sha(p)==row['sha256'] and p.stat().st_size==row['bytes']
print(json.dumps({'PRE_seal_sha256':sha(HERE/'PRE_SEAL.json'),'argument_sha256':seal['argument_sha256'],'bound_files':len(files),'sources':len(bindings['sources']),'exact_prior_flat_entries_compared':checks,'new_rate_source_access':False},indent=2))
