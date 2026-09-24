#!/usr/bin/env python3
"""Exact new count coefficient, using only this task's frozen PRE primitives."""
from pathlib import Path
import hashlib,importlib.util,json,sys
sys.dont_write_bytecode=True
HERE=Path(__file__).resolve().parent
source_path=HERE/'cube_control.py'
assert hashlib.sha256(source_path.read_bytes()).hexdigest()=='cf51bc234d72cb26667b740dddf9f29b27b3c43826dac74df941401a113df125'
spec=importlib.util.spec_from_file_location('own_frozen_fast_cube',source_path)
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)

rows=[]
base=m.hop({m.OMEGA:1})
for edge,e in enumerate(m.EDGES):
    vp=m.birth(base,edge,1);vm=m.birth(base,edge,-1)
    for first,v in [('plus',vp),('minus',vm),('coherent',m.add(vp,vm))]:
        b=m.norm2(v);Fv=m.hop(v)
        for future in ('resolved','coherent'):
            total=0;parts=[]
            for k,ee in enumerate(m.EDGES):
                p=m.birth(Fv,k,1);n=m.birth(Fv,k,-1)
                outputs=[p,n] if future=='resolved' else [m.add(p,n)]
                for x in outputs:
                    assert all(all(qi!=0 for qi in word[0]) for word in x)
                    total+=m.norm2(x);parts.append(m.norm2(x))
            assert total==8*b
            rows.append({'first_edge':list(e),'first_mark':first,'future_instrument':future,'first_B_norm_squared':b,'second_source_norm_squared':total,'normalized_exact_coefficient':8,'all_individual_mark_weights':parts})
data=json.loads((HERE/'CONTROL_RESULTS.json').read_text())
numerical=[]
for row in data['complete_finite_spin_generator']['rows']:
    eps=row['epsilon'];maximum=0;cases=[]
    for tau,P,energy in zip(row['tau_grid'],row['future_birth_probabilities_by_time_and_mark'],row['predicted_spin_one_fast_energy_by_time_and_mark']):
        # PRE finite-spin run fixed delta=1 and kappa=.7.
        target=[8*.7*tau+c-f for c,f in zip((2,1,1.5),energy)]
        actual=[p/eps**2 for p in P]
        err=max(abs(a-b) for a,b in zip(actual,target));maximum=max(maximum,err)
        cases.append({'tau':tau,'actual_P8_over_epsilon_squared':actual,'fast_prediction':target,'max_difference':err})
    numerical.append({'epsilon':eps,'max_difference':maximum,'max_difference_over_epsilon_squared':maximum/eps**2,'rows':cases})
assert numerical[-1]['max_difference']<numerical[0]['max_difference']
result={'all_assertions_passed':True,'exact_primitive_cases':rows,'own_PRE_full_generator_count_comparison':numerical,'author_proof_code_or_rows_read':False,'source_sha256':hashlib.sha256(source_path.read_bytes()).hexdigest()}
(HERE/'COUNT_CONTROL_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'all_assertions_passed':True,'exact_case_count':len(rows),'normalized_coefficient':8,'own_PRE_count_error_rows':[{'epsilon':x['epsilon'],'max_error':x['max_difference'],'error_over_epsilon_squared':x['max_difference_over_epsilon_squared']} for x in numerical]},indent=2))
