from pathlib import Path
from fractions import Fraction as F
import json, hashlib
root=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
protocol=json.loads((root/'protocol.json').read_text())
assert sha(root/'packet/manifest.json')==protocol['packet_manifest_sha256']
assert sha(root/'review-prompt.txt')==protocol['common_prompt_sha256']
manifest=json.loads((root/'packet/manifest.json').read_text())
for item in manifest['files']:
 p=root/'packet'/item['path']; assert sha(p)==item['sha256']; assert p.stat().st_size==item['bytes']
usage={}
for name in ['reviewer-a','reviewer-b']:
 u=json.loads((root/f'{name}-usage.json').read_text())
 for name2,digest in u['report_hashes'].items():assert sha(root/name/name2)==digest
 usage[name]={k:u[k] for k in ['actual_configurations','active_task_seconds','request_count','total_token_usage','modeled_standard_credits','modeled_fast_credits','report_hashes']}
p=[F(x,16) for x in [9,3,3,1]];q=[F(x,16) for x in [1,3,3,9]];m=[(x+y)/2 for x,y in zip(p,q)]
det=lambda x:x[0]*x[3]-x[1]*x[2]
assert all(x>0 for x in p+q) and sum(p)==sum(q)==sum(m)==1
assert det(p)==det(q)==0 and det(m)==F(1,16)
control={'first_product_law':list(map(str,p)),'second_product_law':list(map(str,q)),'equal_mixture':list(map(str,m)),'determinants':list(map(str,[det(p),det(q),det(m)])),'conclusion':'Strictly positive independent conditional laws can mix to a dependent law; this refutes generic nonlinear transfer, not a particular absent block theorem.'}
(root/'averaging-control.json').write_text(json.dumps(control,indent=2)+'\n')
rows=[('cubic_fixture','F1','B-02'),('global_iff','F2','B-01'),('zero_attachment','F2 final paragraph','B-01 and sound results'),('axiom_model','F3','B-03'),('averaging',None,'B-04'),('dependency_graph','F4','B-05')]
a=usage['reviewer-a'];b=usage['reviewer-b']
result={'packet_files_verified':len(manifest['files']),'packet_manifest_sha256':protocol['packet_manifest_sha256'],'reports_frozen_verified':True,'theme_mapping':[{'theme':t,'sol_max':s,'astra_low':v} for t,s,v in rows],'sol_max_known_themes_found':5,'astra_low_known_themes_found':6,'unsupported_material_findings_identified':[],'adjudication':'Both reports support the five shared themes. Sol explicitly accepts the generic uniform-in-exterior averaging inference and does not identify the nonlinear closure restriction. Astra B-04 gives a valid positive product-law counterexample independently verified here. Missing earlier block sources limit particular attributions for both models. No material new issue beyond the rubric changes this decision.','reviewer_metrics':usage,'sol_credit_savings_percent':100*(1-a['modeled_standard_credits']/b['modeled_standard_credits']),'sol_elapsed_increase_percent':100*(a['active_task_seconds']/b['active_task_seconds']-1),'averaging_control_sha256':sha(root/'averaging-control.json'),'decision':'Keep Astra low default. One selected defective PR is insufficient to establish general model equivalence or replacement safety. No model-default or skill change.'}
(root/'adjudication.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:result[k] for k in ['packet_files_verified','sol_max_known_themes_found','astra_low_known_themes_found','sol_credit_savings_percent','sol_elapsed_increase_percent']},indent=2))
