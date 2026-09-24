from pathlib import Path
import datetime,hashlib,json,subprocess
OUT=Path(__file__).resolve().parent;RAW=OUT.parents[4];BASE=OUT.parent
assert RAW.name=='mobile-record-formation-20260920'
known={
'campaign12h_fourth/local_compensation_author/LOCAL_COMPENSATION_COMMON_FIELD_RECORD_LIMIT.md':'42ec5430a0f49c9b6e70577be601df72e23d881b7ef152186de2cdb1ff3faba4',
'campaign12h_fourth/local_compensation_author/BOUNDED_BLOCK_DIAGONAL_COMPENSATION_TARGET.md':'9bc691a07fd70c1a813852aa0cac55832065b3c95cf3d50e5528845f6613e0b0',
'campaign12h_fourth/local_compensation_author/ROOT_GENERAL_TARGET_CORRECTION.md':'c906ed162db678fc2f10bc67afd2af22d929be3fe97fd3a1658cfe12ecd339a9',
'campaign12h_third/FINITE_FORMATION_WITH_RETAINED_FOURTH_ORDER_DYNAMICS.md':'002119d5a3f9bec171c3678cb15afdb91f7a763311ca38e6e4458ce10865572e',
'campaign12h_third/FINITE_RATE_REPEATED_RECORD_FORMATION.md':'b577c14e992fe74feb8a9f17c33e503f446f7052f83512031c2bf82cf2e3538d',
'campaign12h_fourth/field_energy_completion_author/LOCAL_ELECTRIC_COMPLETIONS_AND_POSTBIRTH_FIELD_PHASE.md':'a9db2a928a0cf16cb2e9dfbaafe36d3f775a42053d4f3074032b8d191e87a617',
'campaign12h_fourth/field_energy_completion_author/ROOT_SCOPE_CORRECTION.md':'fd098fa5b571ea5af03766ecc2eef74f5bdefe2dd9df3e1f01ab046517c398fa'}
def sha(b):return hashlib.sha256(b).hexdigest()
entries=[];root=RAW/'.claude/science/mobile-record-formation-20260920'
for rel,expected in known.items():
 p=root/rel;b=p.read_bytes();assert sha(b)==expected,p
 dest=OUT/'sources'/rel;dest.parent.mkdir(parents=True,exist_ok=True);dest.write_bytes(b)
 entries.append({'path':str(p),'sha256':expected,'snapshot':str(dest.relative_to(OUT))})
main='5efa36e7c357ae2a62ee586a5407f90982f6ded9'
workflow=subprocess.check_output(['git','show',main+':docs/ai_methodology/SCIENCE_WORKFLOW.md'],cwd=RAW)
assert sha(workflow)=='d74718214335d4feae4b40d75720482ca93bd1560a3c35174e7bf875b5b59cc4'
planning='eb1f1ca8338848cf2046582e13aef372d8540937'
plan=subprocess.check_output(['git','show',planning+':AGENTS.md'],cwd=RAW)
for name,b in [('SCIENCE_WORKFLOW.md',workflow),('planning_AGENTS.md',plan),('repository_AGENTS.md',(RAW/'AGENTS.md').read_bytes())]:
 (OUT/'sources'/name).write_bytes(b)
 entries.append({'instruction':name,'sha256':sha(b),'snapshot':'sources/'+name})
packet={'stage':'PRE before root microscopic electric-robustness author exposure',
 'recorded_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'raw':str(RAW),
 'observed_HEAD':subprocess.check_output(['git','rev-parse','HEAD'],cwd=RAW,text=True).strip(),
 'verified_main_workflow_revision':main,'planning_instruction_revision':planning,
 'instructions_reused_from_prior_verified_read':True,'sources':entries,
 'not_read':['CHECKPOINT','microscopic_birth_energy author/checker directories','microscopic_electric_robustness_author','external personal calculations'],
 'scope':'Complete physical star matrices and supplied common initial state; no imported campaign builder.'}
(OUT/'SOURCE_BINDINGS.json').write_text(json.dumps(packet,indent=2)+'\n')
print(json.dumps({'scientific_sources_verified':len(known),'governing_workflow_unchanged':True,'observed_HEAD':packet['observed_HEAD']}))
