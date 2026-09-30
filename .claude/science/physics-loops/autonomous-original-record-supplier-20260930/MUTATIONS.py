"""Actual scratch source mutations, exercised one at a time in fresh processes.

No prior artifacts are loaded. Each expected rejection must be AssertionError
inside its selected mathematical check; import/input failures do not count.
At most one small child is active; 120-second timeout, BLAS/OpenMP one.
"""
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile

AUDIT_TIMEOUT_SEC = 120
REPO = Path(__file__).resolve().parents[4]
PRIMARY = REPO/'scripts/autonomous_local_original_rotor_supplier_2026_09_30.py'
OUT = Path(__file__).with_name('MUTATION_RESULTS.json')
source=PRIMARY.read_text()
cases=[
 ('original_birth_Gauss_shift','source_words',[], 'shifts[b]=sigma;shifts[d]=-qa','shifts[b]=sigma;shifts[d]=qa'),
 ('coherent_mark_environment','source_words',[], 'coherent_label=(0,)','coherent_label=(0,sigma)'),
 ('magnetic_internal_excursion','source_words',[], 'apply_internal_cutoff=False','apply_internal_cutoff=True'),
 ('rotor_prefix_projection','rotor_words',[], 'abs(key[1])<=R','abs(key[1])<=R//4'),
 ('correct_boundary_loss','rotor_words',[], 'correct=gamma(edge,4)','correct=old'),
 ('weighted_rotor_resource','rotor_resources',[], 'k=16*(X+Y+N+1)','k=1*(X+Y+N+1)'),
 ('clock_packet_resource','clock_resources',[1346132804], 'ell*ell/(8*sigma*sigma*theta)','ell*ell/(800*sigma*sigma*theta)'),
 ('magnetic_whole_star_geometry','clock_resources',[1346132804], 'whole_pair_qubits=24+66*qE','whole_pair_qubits=22+60*qE'),
 ('nonwrapped_clock','clock_matrix_fixture',[], 'shift[0,-1]=0.0','shift[0,-1]=1.0'),
 ('controller_interaction_ledger','clock_matrix_fixture',[], "ledger_balance=changes['system']+changes['clock']+changes['interaction']", "ledger_balance=changes['system']+changes['clock']"),
 ('clock_prefix_projection','clock_words_and_records',[], 'abs(mp)>K:continue','abs(mp)>K-1:continue'),
 ('matched_record_code','clock_words_and_records',[], 'gfe=copy@np.kron(gf,np.eye(dF,dtype=int))@copy.T','gfe=copy@np.kron(gf,np.eye(dF,dtype=int))'),
]
child="""import runpy,sys,json,traceback
namespace=runpy.run_path(sys.argv[1])
try:
    namespace[sys.argv[2]](*json.loads(sys.argv[3]))
except AssertionError:
    print('MUTATION_REJECTED_BY_ASSERTION')
    traceback.print_exc(limit=2)
    sys.exit(19)
print('MUTATION_SURVIVED')
"""
env=os.environ.copy()
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS','NUMEXPR_NUM_THREADS'):env[k]='1'
rows=[]
with tempfile.TemporaryDirectory(prefix='autonomous-supplier-mutations-',dir=REPO/'outputs') as scratch:
    for label,fn,args,old,new in cases:
        assert source.count(old)==1,(label,source.count(old))
        mutated=source.replace(old,new)
        path=Path(scratch)/(label+'.py');path.write_text(mutated)
        run=subprocess.run([sys.executable,'-c',child,str(path),fn,json.dumps(args)],capture_output=True,text=True,env=env,timeout=AUDIT_TIMEOUT_SEC)
        rejected=run.returncode==19 and 'MUTATION_REJECTED_BY_ASSERTION' in run.stdout
        rows.append({'family':label,'function':fn,'old':old,'new':new,'exit_code':run.returncode,'rejected_by_assertion':rejected,'stdout':run.stdout.strip(),'stderr':run.stderr.strip(),'mutated_source_sha256':hashlib.sha256(mutated.encode()).hexdigest()})
        assert rejected,(label,run.returncode,run.stdout,run.stderr)
result={'primary_sha256':hashlib.sha256(source.encode()).hexdigest(),'method':'Physical scratch copies; sequential fresh processes; only mathematical AssertionError counts as rejection. Scratch copies removed after execution.','mutations':rows,'total_rejected':len(rows)}
OUT.write_text(json.dumps(result,indent=2)+'\n')
print('Mutations rejected by mathematical assertions:',len(rows))
print('Primary SHA256:',result['primary_sha256'])
