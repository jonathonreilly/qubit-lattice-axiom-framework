from pathlib import Path
import hashlib,json,subprocess,datetime
OUT=Path(__file__).resolve().parent
RAW=OUT.parents[4]
assert RAW.name=='mobile-record-formation-20260920', RAW
base=RAW/'.claude/science/mobile-record-formation-20260920'
paths=[
('science_local_compensation',base/'campaign12h_fourth/local_compensation_author/LOCAL_COMPENSATION_COMMON_FIELD_RECORD_LIMIT.md'),
('science_general_target',base/'campaign12h_fourth/local_compensation_author/BOUNDED_BLOCK_DIAGONAL_COMPENSATION_TARGET.md'),
('science_general_target_correction',base/'campaign12h_fourth/local_compensation_author/ROOT_GENERAL_TARGET_CORRECTION.md'),
('science_fourth_order_parent',base/'campaign12h_third/FINITE_FORMATION_WITH_RETAINED_FOURTH_ORDER_DYNAMICS.md'),
('science_operator_definitions',base/'campaign12h_third/FINITE_RATE_REPEATED_RECORD_FORMATION.md'),
('repository_agent_pointer',RAW/'AGENTS.md'),
('science_workflow',RAW/'docs/ai_methodology/SCIENCE_WORKFLOW.md')]
entries=[]
(OUT/'sources').mkdir(exist_ok=True)
for key,path in paths:
 data=path.read_bytes();saved=OUT/'sources'/f'{key}.md';saved.write_bytes(data)
 entries.append({'role':key,'path':str(path),'sha256':hashlib.sha256(data).hexdigest(),'snapshot':str(saved.relative_to(OUT))})
planning='eb1f1ca8338848cf2046582e13aef372d8540937'
pdata=subprocess.check_output(['git','show',planning+':AGENTS.md'],cwd=RAW)
pdest=OUT/'sources/planning_agents.md';pdest.write_bytes(pdata)
entries.append({'role':'planning_agents','git_revision':planning,'git_path':'AGENTS.md',
                'sha256':hashlib.sha256(pdata).hexdigest(),'snapshot':str(pdest.relative_to(OUT))})
head=subprocess.check_output(['git','rev-parse','HEAD'],cwd=RAW,text=True).strip()
assert head=='f82e21b82f209871f84d671bfc020cea0116e693'
main='61fa847f032d25c90bca2c1273b7edb5713fe160'
mdata=subprocess.check_output(['git','show',main+':docs/ai_methodology/SCIENCE_WORKFLOW.md'],cwd=RAW)
assert mdata==(RAW/'docs/ai_methodology/SCIENCE_WORKFLOW.md').read_bytes()
report={'stage':'PRE; no author energy source comparison','recorded_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
'raw':str(RAW),'head':head,'verified_main':main,'planning':planning,'sources':entries,
'permitted_scientific_sources_only':True,
'not_read':['CHECKPOINT.md','high_flux_energy_author','high_flux_energy_independent','external autonomous-reservoir-personal calculations','old executable model/builders'],
'additional_procedure_read':{'path':'/Users/jonreilly/.codex/skills/physics-claim-reviewer/SKILL.md',
'role':'Examined applicability; full landing review workflow not invoked for this bounded independent reconstruction.',
'sha256':hashlib.sha256(Path('/Users/jonreilly/.codex/skills/physics-claim-reviewer/SKILL.md').read_bytes()).hexdigest()}}
(OUT/'SOURCE_BINDINGS.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'head':head,'bound_sources':len(entries),'main_workflow_matches':True}))
