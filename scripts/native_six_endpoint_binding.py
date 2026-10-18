from pathlib import Path
import sys,json
ROOT=Path(__file__).resolve().parents[1]
P=ROOT/'.claude/science/physics-loops/neutral-composite-24h-20261018/native'
sys.path.insert(0,str(P))
AUDIT_TIMEOUT_SEC=180
AUDIT_INPUT_PATHS=['.claude/science/physics-loops/neutral-composite-24h-20261018/native/SIX_ENDPOINT_BINDING_PROOF.md','.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_four_interval_certificate.py','.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_endpoint_cluster_model.py','.claude/science/physics-loops/neutral-composite-24h-20261018/native/six_endpoint_integer_trial.json']
from neutral_four_interval_certificate import run_all
from neutral_endpoint_cluster_model import run
rows=run_all();assert len(rows)==15
D=json.loads((P/'six_endpoint_integer_trial.json').read_text())
H,states=run(2,3,6);assert [list(s) for s in states]==D['states']
q=D['integer_trial'];assert all(type(x) is int for x in q)
norm=sum(x*x for x in q);coo=H.tocoo();num=0
for i,j,a in zip(coo.row,coo.col,coo.data):
 assert int(a)==a
 num+=q[int(i)]*int(a)*q[int(j)]
cert=10*num+71*norm
assert norm==D['norm']==9999999925139683
assert num==D['energy_numerator']==-71308060208219532
assert cert==D['certificate_10H_plus71N']==-3080607397277827<0
assert all(all(s.count(h)%2==0 for h in set(s)) for s in states)
out=dict(status='bounded-support',four_cluster_interval_certificates=rows,grid_points_per_shape=257,dimension=len(states),norm=norm,energy_numerator=num,exact_certificate=cert,essential_lower_bound=-7,trial_upper_bound=-7.1,scope='Specified native K1 boundary sector only; proof plus interval/integer certificates; not full-H particle or empirical validation')
p=ROOT/'outputs/native_six_endpoint_binding/result.json';p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
