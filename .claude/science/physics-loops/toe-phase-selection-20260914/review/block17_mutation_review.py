from pathlib import Path
import json,hashlib,time
R=Path('/Users/jonreilly/Documents/Codex/toe-coupled-defect-convexity-20260915/scripts/free_cubic_magnetic_local_fillings_and_positive_electric_current_convex_extension_2026_09_15.py')
source=R.read_text()
faults=[
 ('relative_path_endpoint','for j in range(m):h[:j+1,j]=1','for j in range(m):h[:j,j]=1'),
 ('relative_homology_projection','np.eye(m+1,dtype=np.int64)-h@B','np.zeros((m+1,m+1),dtype=np.int64)'),
 ('absolute_projection_sign','np.eye(m+1,dtype=np.int64)-B@h','np.eye(m+1,dtype=np.int64)+B@h'),
 ('boundary_tensor_sign','sgn=(-1)**sum(g for g,z in a[:j])','sgn=1'),
 ('homotopy_tensor_sign','* (-1)**sum(g for g,z in a[:j])','* 1'),
 ('top_homology_discarded',"assert rows[-1]['projection_rank']==1","assert rows[-1]['projection_rank']==0"),
 ('unit_top_charge_local_fill','assert least==min(m//2+1,m-m//2)','assert least<=1'),
 ('thin_rectangle_locality','assert least==(m[0]+1)*min(mid+1,m[1]-mid)','assert least//(m[0]+1)<=np.sum(abs(q))'),
 ('Hodge_curl_coefficient','H=D[p-1]*D[p-1].T','H=2*D[p-1]*D[p-1].T'),
 ('source_missing_Green','f=D[1]*G1*J','f=D[1]*J'),
 ('magnetic_Hodge_coefficient','H3=D[2]*D[2].T','H3=2*D[2]*D[2].T'),
 ('real_current_rep_invariance','sp.exp(sp.pi*sp.I*shift))==-1','sp.exp(2*sp.pi*sp.I*shift))==-1'),
 ('electric_chain_rule_N','-(N*M)**2*(zpp/z','-M**2*(zpp/z'),
 ('electric_inverse_beta','curvature=N*N*float(E)/beta','curvature=N*N*float(E)*beta'),
 ('electric_source_metric','E=sp.Rational(5,6);M=float(E)','E=sp.Rational(1,6);M=float(E)'),
 ('electric_source_phase','2*mp.pi*N*mp.mpf(5)/6*y*k','2*mp.pi*mp.mpf(5)/6*y*k'),
]
# The exact source uses no whitespace between the multiplication and sign.
faults=[(n,o.replace('* (-1)','*(-1)'),v) if n=='homotopy_tensor_sign' else (n,o,v) for n,o,v in faults]
results=[]
for name,old,new in faults:
 assert source.count(old)==1,(name,source.count(old))
 ns={'__name__':'personal_mutation'};exec(compile(source.replace(old,new),'<mutation:'+name+'>','exec'),ns);start=time.monotonic()
 try:ns['run']()
 except AssertionError as e:results.append(dict(name=name,detected=True,failure=str(e)[:300],elapsed_sec=time.monotonic()-start))
 else:results.append(dict(name=name,detected=False,elapsed_sec=time.monotonic()-start))
 print(name,results[-1]['detected'],flush=True)
record=dict(runner_sha256=hashlib.sha256(R.read_bytes()).hexdigest(),faults=results,qualification='Personal deliberate-fault challenges; not independent proof review or an audit verdict.')
Path(__file__).with_name('BLOCK17_MUTATIONS.json').write_text(json.dumps(record,indent=2)+'\n')
assert all(r['detected'] for r in results),[r['name'] for r in results if not r['detected']]
