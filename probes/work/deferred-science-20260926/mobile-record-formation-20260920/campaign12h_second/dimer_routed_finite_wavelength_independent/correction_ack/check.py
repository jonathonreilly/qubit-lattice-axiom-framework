#!/usr/bin/env python3
from pathlib import Path
from datetime import datetime, timezone
import hashlib,json

OUT=Path(__file__).resolve().parent
REVIEW=OUT.parent
RAW=REVIEW.parent
FIX=RAW/'dimer_routed_finite_wavelength_f1_fix'
NEW=RAW/'dimer_routed_finite_wavelength_comparison_corrected'

def ident(p):
    b=p.read_bytes()
    return dict(path=str(p),bytes=len(b),sha256=hashlib.sha256(b).hexdigest())

def main():
    seal=json.loads((REVIEW/'FINAL_SEAL.json').read_text())
    for row in seal['artifacts']:
        assert ident(Path(row['path']))==row
    old=FIX/'compare_dimer_routed_finite_wavelength.py'
    new=RAW/'compare_dimer_routed_finite_wavelength.py'
    assert ident(old)['sha256']=='14fbb2aa97e2a5e8da70ca963c57a28db1e57307248b24661b9c43193b4b3bd5'
    assert ident(new)['sha256']=='27ceae7150c95ce5f32e77c4525b6c96ef0422b36fa9b6586011b7935ed146c4'
    removed='ax.set_ylim((-.08,2.3) if panel==0 else (-.15,1.18))'
    inserted=removed.replace('2.3','2.4')
    before,after=old.read_text(),new.read_text()
    assert before.count(removed)==after.count(inserted)==1
    assert before.replace(removed,inserted)==after
    assert after.replace(inserted,removed)==before
    original=json.loads((FIX/'RESULTS.json').read_text())
    corrected=json.loads((NEW/'RESULTS.json').read_text())
    changed={k for k in original if original[k]!=corrected[k]}
    assert changed=={'created_utc','comparison_source'}
    assert original['by_axis']==corrected['by_axis'] and original['mode_average']==corrected['mode_average']
    upper=max(row['observed_mean'][t][0]+row['observed_standard_error'][t][0] for row in corrected['by_axis'] for t in range(5))
    assert 2.3<upper<2.4
    old_receipt=json.loads((FIX/'RECEIPT.json').read_text())
    for row in old_receipt['outputs']:
        p=FIX/Path(row['path']).name
        got=ident(p);assert got['sha256']==row['sha256'] and got['bytes']==row['bytes']
    receipt=json.loads((NEW/'RECEIPT.json').read_text())
    for row in [receipt['source']]+receipt['inputs']+receipt['outputs']:
        assert ident(Path(row['path']))==row
    qa=json.loads((NEW/'ROOT_VISUAL_QA.json').read_text())
    assert ident(Path(qa['viewed_file']))['sha256']==qa['sha256']
    report={'created_utc':datetime.now(timezone.utc).isoformat(),'finding':'F1','status':'closed',
      'scope':'Only the declared plot-limit correction, preserved-source recovery and unchanged scientific payloads checked; no mathematical or statistical rerun.',
      'original_review':ident(REVIEW/'REPORT.md'),'original_seal':ident(REVIEW/'FINAL_SEAL.json'),
      'original_artifacts_unchanged':len(seal['artifacts']),
      'before_source':ident(old),'after_source':ident(new),
      'complete_forward_and_inverse_recovery':True,'scientific_arrays_exactly_unchanged':True,
      'changed_result_keys':sorted(changed),'largest_error_plus_one_SE':upper,'new_limit':2.4,
      'preserved_files':[ident(p) for p in sorted(FIX.iterdir()) if p.is_file()],
      'corrected_files':[ident(p) for p in sorted(NEW.iterdir()) if p.is_file()],
      'visual_check':'Corrected PNG viewed independently; complete upper cap is visible with margin. PDF bytes authenticated, not separately rendered.',
      'read_limit':'An unnecessary display of the already reviewed preserved RESULTS was truncated; no inference relied on that display. Complete scientific-payload equality was checked programmatically.',
      'unresolved_findings':[]}
    (OUT/'F1_ACK.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({'status':'closed','unchanged_artifacts':len(seal['artifacts']),'maximum_upper_SE':upper}))

if __name__=='__main__':main()
