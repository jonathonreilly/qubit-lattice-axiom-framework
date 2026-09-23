from pathlib import Path
import json,hashlib

p=Path(__file__).resolve().parent
def read(n):return json.loads((p/n).read_text())
def sha(q):return hashlib.sha256(q.read_bytes()).hexdigest()
receipts=[]
for name in ['finite_control_corrected_run_RECEIPT.json','star_analytic_run_RECEIPT.json','path_absorption_run_RECEIPT.json']:
    r=read(name);assert r['exit_code']==0
    for key in ['runner','stdout','stderr']:
        q=Path(r[key]['path']);assert q.is_relative_to(p)
        assert sha(q)==r[key]['sha256'] and q.stat().st_size==r[key]['bytes']
    receipts.append(name)
for row in read('RECOVERY_PATHS.json')['rows']:
    q=Path(row['preserved_path']);assert sha(q)==row['sha256']
first=read('FINITE_CONTROL_RESULTS.json');second=read('STAR_ANALYTIC_RESULTS.json')
for name in ['resolved','coherent']:
    a=first['star4']['instruments'][name];b=second['first_birth_and_absorption'][name]
    assert a['nonfull_trapped_probability']==b['trapped_weight']
    assert a['eventual_full_probability']==b['full_probability']
    assert a['first_state_purity']==b['first_event_purity']
    assert first['star2']['instruments'][name]['eventual_full_probability']=='1'
    assert first['path_S1']['intertwiner'][name]['matrix_units']==16
    assert first['path_S1']['intertwiner'][name]['Q2_correction_nonzero']
for r in read('PATH_ABSORPTION_RESULTS.json')['rows']:
    assert r['boundary_plus_one_hop_rank']==r['lossless_transient_dimension']==3
out={'final_scientific_receipts_verified':receipts,'preserved_initial_receipt_recovered':True,'separate_electric_and_charge_word_results_agree':True,'path_multiple_vacancy_identity_and_absorption_checked':True,'report_sha256':sha(p/'REPORT.md'),'author_new_source_access':False}
(p/'PRE_VALIDATION_RESULTS.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
