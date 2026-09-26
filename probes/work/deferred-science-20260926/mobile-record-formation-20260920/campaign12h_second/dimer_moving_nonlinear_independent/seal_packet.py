#!/usr/bin/env python3
"""Create this review's final seal once, or authenticate it without modification."""
from pathlib import Path
import datetime,hashlib,json

HERE=Path(__file__).resolve().parent

def row(path):
    data=path.read_bytes()
    return {'path':str(path),'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()}

def verify(rows):
    for r in rows:assert row(Path(r['path']))==r,r['path']

def main():
    final=HERE/'FINAL_SEAL.json'
    if final.exists():
        seal=json.loads(final.read_text());verify(seal['sources']+seal['artifacts'])
        print(json.dumps({'final_seal':row(final),'sources_verified':len(seal['sources']),
                          'artifacts_verified':len(seal['artifacts']),'report':row(HERE/'REPORT.md')}))
        return
    source_rows={};pre=[]
    for name,expected in [('PRE_COMPARISON_SEAL.json','2f689daecd524cd8d794705d868fa25f079718c1ca0b3587b358bb832d2d358d'),
                          ('ADDENDUM_PRE_COMPARISON_SEAL.json','2d483da8b77733716081012126b6b4d30fa62d5ebf7d77fbd1e389171c7766f9')]:
        assert row(HERE/name)['sha256']==expected
        seal=json.loads((HERE/name).read_text());verify(seal['sources']+seal['artifacts'])
        for r in seal['sources']:source_rows[r['path']]=r
        pre.append({'identity':row(HERE/name),'source_rows':len(seal['sources']),'artifact_rows':len(seal['artifacts'])})
    author=json.loads((HERE/'AUTHOR_SOURCE_RECEIPT.json').read_text())
    verify(author['sources'])
    for r in author['sources']:source_rows[r['path']]=r
    for name in ['INDEPENDENT_RUN_RECEIPT.json','ADDENDUM_RUN_RECEIPT.json','COMPARISON_RUN_RECEIPT.json']:
        assert json.loads((HERE/name).read_text())['returncode']==0
    report=(HERE/'REPORT.md').read_text()
    assert 'Author source comparison is pending' not in report and '30,?' not in report
    files=sorted(p for p in HERE.rglob('*') if p.is_file() and '__pycache__' not in p.parts
                 and p.name not in ['CHECKPOINT.md','FINAL_SEAL.json'])
    seal={'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
          'review_status':'Independent source-bound mathematical scrutiny completed; no actionable finding under the stated conditional hypotheses. Not a formal audit or retention verdict.',
          'read_boundary':'Qualitative source and independent controls sealed before quantitative addendum access; addendum independently sealed before all new author controls. Final author source/result/receipt hashes match parent-supplied identities.',
          'preserved_precomparison_seals':pre,
          'sources':[source_rows[k] for k in sorted(source_rows)],
          'artifacts':[row(p) for p in files],
          'limits':'No new literature, full author suite, production simulation, hydrodynamic trajectory replay or general model extension. Full all-origin author extrema/coverage loops authenticated rather than repeated. Selected rows and load-bearing identities independently reconstructed. No separate quantitative author checker exists.',
          'failures':'No independent failed execution. Author initial frozen-winding fixture failure, exact source repair, complete original traceback and receipt are source-bound; original development files left unchanged.',
          'mutable_exclusions':['CHECKPOINT.md','__pycache__/'],'seal_self_excluded':True}
    verify(seal['sources']+seal['artifacts'])
    with final.open('x') as f:json.dump(seal,f,indent=2);f.write('\n')
    print(json.dumps({'final_seal':row(final),'sources':len(seal['sources']),'artifacts':len(seal['artifacts']),
                      'report':row(HERE/'REPORT.md')}))

if __name__=='__main__':main()
