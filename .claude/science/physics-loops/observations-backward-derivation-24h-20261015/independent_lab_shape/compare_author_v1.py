from pathlib import Path
import json,csv,hashlib,datetime,time,subprocess
from fractions import Fraction as F
import numpy as np
O=Path(__file__).resolve().parent;P=O.parent
names=['LAB_SHAPE_DERIVATION_v1.md','LAB_SHAPE_PLAN_v1.json','LAB_SHAPE_RESULTS_v1.md','check_lab_shape_v1.py','LAB_SHAPE_CONTROLS_v1.json','LEE2020_APPENDIX_A1_v1.csv']
hashes=lambda:{n:hashlib.sha256((P/n).read_bytes()).hexdigest() for n in names}
before=hashes();start=datetime.datetime.now(datetime.timezone.utc).isoformat();t=time.monotonic()
r=subprocess.run(['/usr/local/bin/python3','-B',str(P/'check_lab_shape_v1.py')],cwd=O,capture_output=True,timeout=120);elapsed=time.monotonic()-t
(O/'AUTHOR_REPRODUCTION_STDOUT_v1.txt').write_bytes(r.stdout);(O/'AUTHOR_REPRODUCTION_STDERR_v1.txt').write_bytes(r.stderr)
a=json.loads(r.stdout);saved=json.loads((P/'LAB_SHAPE_CONTROLS_v1.json').read_text());own=json.loads((O/'INDEPENDENT_RESULTS_v1.json').read_text())
rows=list(csv.DictReader((P/'LEE2020_APPENDIX_A1_v1.csv').open(newline='')));s=[F(row['separation_um']) for row in rows];ds=[F(row['separation_sigma_um']) for row in rows]
exact_positions=sorted(set(s));expected_pairs={(i,j) for i in range(95) for j in range(95) if s[i]+ds[i]<s[j]-ds[j]}
checks=[]
def check(name,ok,detail=None):checks.append({'name':name,'passed':bool(ok),'detail':detail})
check('original source byte identity',before==hashes());check('return code zero',r.returncode==0);check('exact reproduced stdout',r.stdout==(P/'LAB_SHAPE_CONTROLS_v1.json').read_bytes());check('parsed reproduced output',a==saved);check('all original CSV fields',a['records']==rows);check('root count',a['counts']=={'checks':158,'failed':0,'passed':158})
comparisons={};scount=0;max_slack_error=0;max_reduced_error=0;max_dual_gap=0
for ch,modes in a['development'].items():
 y=np.array([float(row[ch+'_fNm']) for row in rows]);sig=np.array([float(row[ch+'_sigma_fNm']) for row in rows]);comparisons[ch]={}
 for mode,result in modes.items():
  if mode=='interval_monotone_relaxation':expected_assignment=list(range(95));expected_positions=list(map(float,s));own_mode='interval_monotone'
  else:expected_assignment=[exact_positions.index(v) for v in s];expected_positions=list(map(float,exact_positions));own_mode=mode
  assignment=np.array(result['assignment']);positions=np.array(result['positions_um']);latent=np.array(result['latent_values_fNm']);rowt=np.array(result['row_latent_fNm']);kk=result['k'];x=np.r_[latent,kk];n=len(latent)
  check(ch+mode+' assignments',result['assignment']==expected_assignment and result['positions_um']==expected_positions)
  check(ch+mode+' row readouts',max(abs(rowt-latent[assignment]))==0 and max(abs((rowt-y)/sig-np.array(result['row_standardized_residual'])))<1e-12)
  edges=[];A=[];b=[];allslacks=[];duals=[]
  for c in result['constraints']:
   tokens=c['label'].split(':');kind=tokens[0];ids=list(map(int,tokens[1:]));row=np.zeros(n+1)
   if kind=='data_upper':j=ids[0];row[assignment[j]]=1;row[-1]=-sig[j];bound=y[j]
   elif kind=='data_lower':j=ids[0];row[assignment[j]]=-1;row[-1]=-sig[j];bound=-y[j]
   elif kind in ['decrease','interval_decrease']:
    i,j=ids;row[i]=-1;row[j]=1;bound=0
    if kind=='interval_decrease':edges.append((i,j))
   elif kind=='convex':
    i,j,k=ids;dl=positions[j]-positions[i];dr=positions[k]-positions[j];row[i]=-dr/(dl+dr);row[j]=1;row[k]=-dl/(dl+dr);bound=0
   else:raise ValueError(kind)
   slack=bound-row@x;max_slack_error=max(max_slack_error,abs(slack-c['slack']));A.append(row);b.append(bound);allslacks.append(slack);duals.append(c['dual']);scount+=1
  A=np.array(A);b=np.array(b);duals=np.array(duals);c=np.r_[np.zeros(n),1.];reduced=c-A.T@duals
  max_reduced_error=max(max_reduced_error,float(max(abs(reduced-np.array(result['reduced_costs'])))));gap=abs(c@x-b@duals);max_dual_gap=max(max_dual_gap,float(gap))
  check(ch+mode+' independently rebuilt certificate',min(allslacks)>-1e-8 and min(x)>-1e-8 and max(duals)<1e-8 and min(reduced)>-1e-8 and gap<1e-8)
  if edges:check(ch+mode+' exact interval relation',set(edges)==expected_pairs)
  objective_delta=kk-own['channels'][ch][own_mode]['lp']['objective'];check(ch+mode+' independent optimum',abs(objective_delta)<1e-9,objective_delta)
  diff=np.abs(rowt-np.array([q[{'central_monotone':'central_monotone_lp_t','central_convex':'central_convex_t','interval_monotone':'interval_monotone_lp_t'}[own_mode]] for q in own['channels'][ch]['rows']]))
  comparisons[ch][mode]={'objective':kk,'independent_objective_delta':objective_delta,'max_latent_difference':float(max(diff)),'interpretation':'Primal optimizing curves need not be unique; compare objective and each complete certificate rather than demand same curve','row_count':len(rowt),'constraint_count':len(result['constraints'])}
check('all stored constraint slacks',max_slack_error<1e-10,max_slack_error);check('all stored reduced costs',max_reduced_error<1e-10,max_reduced_error)
result={'scope':'Post-exposure source/certificate comparison and unchanged reproduction, distinct from frozen independent computation','started_utc':start,'elapsed_seconds':elapsed,'timeout_seconds':120,'returncode':r.returncode,'source_before':before,'source_after':hashes(),'stdout_sha256':hashlib.sha256(r.stdout).hexdigest(),'stderr_sha256':hashlib.sha256(r.stderr).hexdigest(),'checks':checks,'passed':sum(x['passed'] for x in checks),'failed':sum(not x['passed'] for x in checks),'compared_rows':855,'compared_constraint_records':scount,'max_slack_identity_error':max_slack_error,'max_reduced_cost_identity_error':max_reduced_error,'max_recomputed_duality_gap':max_dual_gap,'comparisons':comparisons}
(O/'AUTHOR_COMPARISON_v1.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k not in ['source_before','source_after','checks','comparisons']},indent=2));print(json.dumps(comparisons,indent=2));assert result['failed']==0
