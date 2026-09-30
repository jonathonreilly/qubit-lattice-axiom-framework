"""Narrow correction of invalid spin1 input in historical mean-field controls."""
from pathlib import Path
import hashlib,json,time,resource
here=Path(__file__).resolve().parent
old=here/'check_mean_field_algebra.py'
# Execute only the unchanged physical definitions and historical fixture assembly.
# Do not execute or overwrite any historical control or capture.
namespace={'__file__':str(old)}
exec(compile(old.read_text().split('assert all(gauss(k) for k in inputs+list(seed_births))')[0],str(old),'exec'),namespace)
for name,value in namespace.items():
 if not name.startswith('__'):globals()[name]=value
start=time.process_time()
names=['Omega','seed','one','ordinary','loopbirth','gamma','beta']
def legal(k):return all(abs(e)<=1 for e in unpack(k)[1].values())
old_validity={name:legal(namespace[name])for name in names}
assert old_validity=={name:name!='loopbirth' for name in names}
# Explicit original source: hop from a_loop to +x; resolved + birth to -x.
# Each step is a nonzero Gauss-preserving spin1 path with unit normalized weight.
old_B=add(aloop,(1,0,0));new_B=add(aloop,(-1,0,0))
legal_hop=move(seed,aloop,old_B,'out')
legal_birth=move(legal_hop,aloop,new_B,'birth',1)
assert legal_hop is not None and legal_birth is not None
assert legal(legal_hop) and legal(legal_birth) and gauss(legal_hop) and gauss(legal_birth)
assert legal_birth in birth_op(step_op({seed:1},aloop,False,True),aloop,new_B,(1,),True)
inputs=[Omega,seed,one,ordinary,legal_birth,gamma,beta]
assert all(legal(k) and gauss(k) for k in inputs)
# Assert every INPUT to spin operations, including intermediate linear supports.
original_step=step_op;original_birth=birth_op
input_assertions=0
def step_op(v,aa,reverse=False,spin=False):
 global input_assertions
 if spin:
  assert all(legal(k) for k in v);input_assertions+=len(v)
 return original_step(v,aa,reverse,spin)
def birth_op(v,aa,bb,signs,spin=False):
 global input_assertions
 if spin:
  assert all(legal(k) for k in v);input_assertions+=len(v)
 return original_birth(v,aa,bb,signs,spin)
# Original functions hold namespace globals; update them so nested calls check inputs.
namespace['step_op']=step_op;namespace['birth_op']=birth_op
comm_cases=block_cases=nonzero=0
for aa in [h,aloop]:
 centers=near(aa)|{aa,add(aa,(6,0,0))}
 for key in inputs:
  for dv in dirs:
   for signs in [(1,),(-1,),(-1,1)]:
    bb=add(aa,dv);v={key:1}
    b=birth_op(step_op(v,aa,False,True),aa,bb,signs,True)
    d=step_op(birth_op(v,aa,bb,signs,True),aa,False,True)
    full=plus((1,birth_op(fall(v,centers,False,True),aa,bb,signs,True)),(-1,fall(birth_op(v,aa,bb,signs,True),centers,False,True)))
    assert full==plus((1,b),(-1,d));comm_cases+=1;nonzero+=bool(full)
    assert not inner(b,d)
    assert all(charge(unpack(k)[0],aa)!=0 for k in b)
    assert all(charge(unpack(k)[0],aa)==0 for k in d)
    assert all(legal(k) and gauss(k) for k in full);block_cases+=1
for key in [Omega,ordinary,legal_birth]:
 assert not literal_h2(key,near(h)|near(aloop)|{h,aloop},True)
assert nonzero>0
result={'scope':'narrow affected spin1 controls only; historical rotor and W1 controls not rerun',
 'historical_runner_sha256':hashlib.sha256(old.read_bytes()).hexdigest(),
 'historical_output_sha256':hashlib.sha256((here/'MEAN_FIELD_ALGEBRA_RESULTS.json').read_bytes()).hexdigest(),
 'runner_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'historical_input_validity':old_validity,'original_invalid_input':namespace['loopbirth'],
 'legal_source_word':{'seed':seed,'hop_center':aloop,'hop_B':old_B,'birth_B':new_B,'original_resolved_sign':1,'legal_hop':legal_hop,'legal_birth':legal_birth},
 'spin1_neighbor_commutator_cases':comm_cases,'spin1_occupancy_block_cases':block_cases,
 'nonzero_commutator_cases':nonzero,'spin1_W0_cancellation_cases':3,'asserted_spin_input_states':input_assertions,
 'unaffected_scope':'all original rotor controls; six W1 full-row inputs; rotor/spin1 boundary differences from legal seed; coherent Omega+one input',
 'cpu_seconds':time.process_time()-start,'peak_rss_bytes':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}
assert result['cpu_seconds']<5 and result['peak_rss_bytes']<50*1024**2
(here/'MEAN_FIELD_SPIN_INPUT_CORRECTION.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:result[k]for k in ['historical_input_validity','spin1_neighbor_commutator_cases','spin1_occupancy_block_cases','nonzero_commutator_cases','spin1_W0_cancellation_cases','asserted_spin_input_states','cpu_seconds','peak_rss_bytes']},indent=2))
print('TOTAL: PASS=4 FAIL=0')
