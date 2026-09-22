from pathlib import Path
import json,hashlib,subprocess,ast
r=Path('/private/tmp/review-drain-20260915');wt=r/'drain-review8146'
h=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
i=json.loads((r/'drain8146-original-inventory-with-blobs.json').read_text())
claims={
8138:{'constructive':'Q1 factorization, Q2 finite witnesses, Q3 finite positive chain, Q4 coupling/existence bounds; retain precise hypotheses','repair':'Q1(f) universal nonconstant third-body assertion, Q4(e) unconditional rotational noninvariance; negative packet; minor zero-c bound'},
8139:{'constructive':'DLR specification and covariance orbit under repaired exterior-cylinder proof; conditional generic distinction with mixed-difference proof; finite irreversibility witness','repair':'L1 exterior tests, R3 opposite-corner generic proof and finite-cylinder mixing, mixture terminology, negative packet'},
8141:{'constructive':'T1/T2 Gibbs factorization and containing graph; T3 canonical potential with maximality; exact mixed ratios at two triples','repair':'T4 every headline needs nonzero mixed-difference hypothesis; negative packet'},
8142:{'constructive':'Exact six-point pair-additive classification, nonzero pair part, polynomial identities','repair':'X2 p=r interpretation; X4 unsupported exceptional-locus eight-law extension; negative packet'},
8146:{'constructive':'Level-coordinate identity, exact noise formulas, eroder bound, domination, finite-chain metastability, row/column decay','repair':'S0 spatial-invariance premise, S1 strict majority inequality, S5 all-phase overclaim; negative packet'}}
rows=[]
for c in i['constituents']:
 for x in c['paths']:
  p=x['path'];row={**x,'pr':c['pr'],'original_head':c['head'],'original_base':c['merge_base']}
  if p.startswith('.claude/'):
   row['disposition']='Preserve exact historical source/control/evidence version; full incremental delta read; historical verdicts not current authority; no primary runtime consumer.'
  elif p.startswith('docs/audit/data/'):
   row['disposition']='Exclude generated citation manifest from scientific authority; current-main regeneration belongs integration.'
  elif p.startswith('logs/'):
   row['disposition']='Historical original cache; preserve provenance and replace live evidence only after corrected-source genuine capture.'
  else:row['disposition']='Canonical scientific source fully read; correction required per findings; final mapping/hash pending author freeze.'
  row.pop('initial_disposition',None);rows.append(row)
full=['docs/MINIMAL_AXIOMS_2026-06-29.md','docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md','docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md','docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md','docs/repo/DEFERRED_DECISIONS.md','docs/repo/ACTIVE_REVIEW_QUEUE.md','docs/repo/REVIEW_FEEDBACK_WORKFLOW.md','docs/audit/data/axiom_premise_nodes.json','docs/audit/data/premise_decision_history.json','docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md','docs/ai_methodology/skills/review-loop/SKILL.md']
for name in ['REVIEW_SETUP','REVIEW_UNITS','SCIENCE_LENSES','OPERATIONS','FIXES_AND_REPORTING','AUDIT_COMPATIBILITY','UNIT_RECEIPT','SALVAGE','LANDING']:
 full.append('docs/ai_methodology/skills/review-loop/references/'+name+'.md')
inputs={p:{'sha256':h(wt/p),'role':'authority/methodology','read_scope':'full'} for p in full if (wt/p).exists()}
parents={
'ADMISSIBILITY_PLANE_FORMATION_DIAGONAL_INTERACTION_NOTE_2026-09-08.md':'full81lines; rectangle consistency, DLR proof, two diagonal classes',
'ADMISSIBILITY_RULE_MONOTONE_ORDER_FORMATION_LAW_ROWS_COLUMNS_CHAINS_CORNER_LAW_BOUNDED_THEOREM_NOTE_2026-09-07.md':'1-530; full P1-P7 used arguments, exact scope and negative gate; remaining certificate/history not load-bearing',
'ADMISSIBILITY_RULE_INFINITE_STRIP_ROW_SWEEP_FORMATION_LAW_VERSUS_STATIC_LAW_BOUNDED_THEOREM_NOTE_2026-09-06.md':'headings;77-146 premises;201-363 C1/C2/E1-E4 complete used proofs',
'ADMISSIBILITY_RULE_FORMATION_LAW_VERSUS_STATIC_LAW_FINITE_WINDOW_CLASSIFICATION_BOUNDED_THEOREM_NOTE_2026-09-06.md':'headings;73-146 premises;195-366 A/B full used proofs;677-690 corrected scope'}
for p,scope in parents.items():inputs['docs/'+p]={'sha256':h(wt/'docs'/p),'role':'actual mathematical repository premise','read_scope':scope}
# Runtime declarations are separately frozen from semantic dependencies; no metadata import of primary.
declared={}
for c in i['constituents']:
 d=r/'drain8146-originals'/str(c['pr'])
 for p in (d/'scripts').glob('*.py'):
  vals=[]
  for node in ast.parse(p.read_text()).body:
   if isinstance(node,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='AUDIT_INPUT_PATHS' for t in node.targets):
    try:vals=list(ast.literal_eval(node.value))
    except Exception:vals=['NON_LITERAL_REQUIRES_INSPECTION']
  declared[str(c['pr'])]={'paths':vals,'primary_sha256':h(p)}
artifacts=['drain8146-findings-provisional.md','drain8146-original-inventory-with-blobs.json','drain8146-original-api-preflight.json','drain8146-independent-controls.py','drain8146-independent-controls.json','drain8146-independent-finite-controls.py','drain8146-independent-finite-controls.json']
report={'status':'ORIGINAL SOURCE REVIEW COMPLETE WITH BLOCKING FINDINGS; NOT FINAL PASS','reviewer_session':'/root/review_8012','current_main':i['current_main'],'original_constituents':i['constituents'],'original_dispositions':rows,'claim_dispositions':claims,'source_input_context_hashes':inputs,'original_runtime_declarations':declared,'external_mathematics':'Finite probability/positive finite Markov chain contraction; countable extension, compact Feller existence, conditional uniqueness, ergodic decomposition only within stated hypotheses; Sympy exact rational algebra. These are distinct from repository axioms and do not supply a physical menu/order/selection. No external theorem of noisy-eroder stability used as closure.','controls':{a:h(r/a) for a in artifacts},'read_coverage':'All five full canonical notes and all five full primary programs; all five full incremental historical proof/control deltas including saved outputs. No primary execution. Generated audit data inventoried only, excluded as authority.','pending_final_confirmation':['Root-authored corrected notes/runner and exact archive mapping','Remaining routine setup router/reference sections before final PASS: controlled vocabulary, harness index, audit README; any newly used premise/context source','Final candidate exact citations/helper/input parser closure and one bounded capture per changed primary after cold confirmation','Same-session final source/claim/path disposition hashes and schema receipt; combined gate owned root'],'no_source_edits':subprocess.check_output(['git','status','--porcelain'],cwd=wt,text=True)==''}
(r/'drain8146-original-review-report.json').write_text(json.dumps(report,indent=2)+'\n')
(r/'drain8146-original-review-report.md').write_text('# Original source review: 8138,8139,8141,8142,8146\n\nOriginal source review complete with blocking findings; **no final PASS**.\n\nAll five canonical arguments/programs and all constituent historical deltas were read. The exact 116 original path/mode/blob/hash rows and claim dispositions are bound in the adjacent JSON. See `drain8146-findings-provisional.md` for twelve concrete corrections and salvage paths. Two independent standalone exact controls completed under90s/30s caps; no primary program was executed.\n\nActual current-main metadata APIs recognize all five bounded-theorem Types and900-second declared timeouts; repository helper imports are empty. Source and mathematical inputs are distinguished from external standard mathematics. The clean reviewer checkout remains untouched.\n\nFinal source acceptance requires root corrections, remaining routine setup/reference coverage, same-session affected review and genuine frozen-source evidence. Historical author PASS/mutation reports are preserved only as provenance. Negative packet shortages cannot be cured by renaming or invented attempts; constructive salvage and explicit deferred negative certification remain available.\n')
print('wrote immutable original report',len(rows),'rows',h(r/'drain8146-original-review-report.json'))
