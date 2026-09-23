#!/usr/bin/env python3
from pathlib import Path
import hashlib,json
base=Path(__file__).resolve().parent

def bind(p):
 b=p.read_bytes();return {'path':str(p),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()}
def check(row):assert bind(Path(row['path']))=={k:row[k] for k in ['path','bytes','sha256']}
def main():
 pre=base/'PRE_COMPARISON_SEAL.json';assert bind(pre)['sha256']=='bc1f83597d26466a02d2a1375fea91624b3adb99dcac25f7902262935a9feeb2'
 P=json.loads(pre.read_text())
 for row in P['sources']+P['artifacts']:check(row)
 auth=json.loads((base/'COMPARISON_AUTH.stdout').read_text());rows=[];seals=[]
 for packet in auth['author_packets']:
  check(packet['seal']);seals.append(packet['seal'])
  for row in packet['bindings']:check(row);rows.append({k:row[k] for k in ['path','bytes','sha256']})
 for label in ['COMPARISON_AUTH','COMPARISON_CHECK']:
  r=json.loads((base/(label+'_RECEIPT.json')).read_text());assert r['exit_code']==0
  for row in r['inputs']+r['outputs']:check(row)
  assert (base/(label+'.stderr')).read_bytes()==b''
  f=base/(label+'_RESULTS.json');assert not f.exists();f.write_bytes((base/(label+'.stdout')).read_bytes())
 D4=base.parent;L=D4/'local_compensation_author';G=D4/'local_compensation_locality_author'
 result_specs=[(L,'LOCAL_COMPENSATION_CONTROLS.json','LOCAL_CONTROLS'),(L,'MECHANISM_CONTROLS.json','MECHANISM'),(G,'GENERAL_GRAPH_LOCALITY_RESULTS.json','LOCALITY')]
 coverage=[]
 for directory,name,label in result_specs:
  result=(directory/name).read_bytes();out=(directory/(label+'.stdout.log')).read_bytes()
  assert out.endswith(result) and (directory/(label+'.stderr.log')).read_bytes()==b''
  receipt=json.loads((directory/(label+'_RUN_RECEIPT.json')).read_text());assert receipt.get('exit_code',receipt.get('returncode'))==0
  coverage.append({'result':bind(directory/name),'stdout_contains_exact_result_suffix':True,'empty_stderr':True,'successful_actual_receipt':True})
 graph=json.loads((G/'GENERAL_GRAPH_LOCALITY_RESULTS.json').read_text());assert len(graph['graphs'])==9 and sum(len(g['checks']) for g in graph['graphs'])==45
 draft=json.loads((G/'ANALYTIC_DRAFT_SEAL.json').read_text());check(draft)
 r=json.loads((base/'COMPARISON_CHECK_RESULTS.json').read_text())
 assert r['sum_of_squares']['exact_H_kernel_dimension']==9
 assert all(x['small_time_population8_coefficient_over_kappa_squared']==192 for x in r['all_mark_second_event']['all_instrument_combinations'])
 assert r['general_graph_first_sector']['compensated_scalar']==-40 and r['detuning_non_scalar_countercontrol']['variance_M']==8
 identities={'author_seals':seals,'author_bound_sources_and_evidence':rows,'read_scope':'Complete three new notes, three new control sources, all result fields, distinct log prefixes, and all receipts. Cube inherited builder only needed definitions; prior second-event builder only required charge/hop/birth functions. No unprepared consequence theorem or other packet reviewed.'}
 f=base/'COMPARISON_SOURCE_BINDINGS.json';assert not f.exists();f.write_text(json.dumps(identities,indent=2)+'\n')
 return {'pre_bindings_unchanged':len(P['sources'])+len(P['artifacts']),'author_seals_verified':len(seals),'author_seal_rows_verified':len(rows),'author_recorded_results_authenticated':coverage,'author_graph_control_count':{'graphs':9,'seeds':45},'new_independent_control_passed':True,'material_findings':[],'failure_history':'No new failure or repaired threshold. PRE countercontrols remain unchanged.'}
if __name__=='__main__':print(json.dumps(main(),indent=2))
