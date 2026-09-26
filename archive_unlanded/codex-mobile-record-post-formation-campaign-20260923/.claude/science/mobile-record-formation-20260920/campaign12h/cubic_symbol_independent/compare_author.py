#!/usr/bin/env python3
"""Post-seal author-source comparison, executing only private copied checkers."""
from pathlib import Path
import hashlib,json,subprocess,sys
HERE=Path(__file__).resolve().parent;ROOT=HERE.parent
sha=lambda b:hashlib.sha256(b).hexdigest()
identities=[]
def identify(p):
 raw=p.read_bytes();row={'path':str(p),'bytes':len(raw),'sha256':sha(raw)};identities.append(row);return raw
for filename,expected in [('BASE_PRE_COMPARISON_SEAL.json','5c3ad0cd053ea4822b1137953e6610300b25ed5f699867d410d7d943aa12a0a9'),('SELECTION_PRE_COMPARISON_SEAL.json','24eeaed4f6c837cef2c6b2cd4dd2fdae3a43165530305bc4e23632fa94a80c96')]:
 raw=identify(HERE/filename);assert sha(raw)==expected
 seal=json.loads(raw)
 assert sha(Path(seal['source']['path']).read_bytes())==seal['source']['sha256']
 for row in seal['artifacts']:
  raw=Path(row['path']).read_bytes();assert sha(raw)==row['sha256'] and len(raw)==row['bytes']
for name in ['CUBIC_ENTROPY_PRINCIPAL_SYMBOL_CLASSIFICATION.md','CUBIC_SYMBOL_REVERSAL_AND_CONSERVED_DIVERGENCES.md']:
 identify(ROOT/name)
out=HERE/'author_comparison_run';out.mkdir(exist_ok=True)
results=[]
for source,result,log in [('cubic_entropy_symbol_check.py','CUBIC_ENTROPY_SYMBOL_RESULTS.json','CUBIC_ENTROPY_SYMBOL_RUN.log'),('cubic_symbol_selection_check.py','CUBIC_SYMBOL_SELECTION_RESULTS.json','CUBIC_SYMBOL_SELECTION_RUN.log')]:
 code=identify(ROOT/source);recorded=identify(ROOT/result);original_log=identify(ROOT/log)
 assert json.loads(recorded)==json.loads(original_log)
 copy=out/source;copy.write_bytes(code)
 run=subprocess.run([sys.executable,str(copy)],cwd=out,capture_output=True,text=True)
 (out/(source+'.stdout')).write_text(run.stdout);(out/(source+'.stderr')).write_text(run.stderr)
 assert run.returncode==0 and not run.stderr
 observed=json.loads((out/result).read_text());expected=json.loads(recorded)
 assert observed==expected
 if 'source_sha256' in observed:assert observed['source_sha256']==sha(code)
 results.append({'source':source,'source_sha256':sha(code),'result_sha256':sha(recorded),
                 'original_log_sha256':sha(original_log),'private_execution_returncode':run.returncode,
                 'private_output_equals_recorded_result':True,
                 'original_result_has_embedded_source_hash':'source_sha256' in observed})
for row in identities:assert sha(Path(row['path']).read_bytes())==row['sha256']
record={'scope':'Post-precomparison authentication and private-copy reproduction of two small author controls; not additional independent mathematics.',
 'author_sources_and_receipts':results,'identities':identities,'all_checks_passed':True,
 'production_or_primary_files_modified':[]}
(HERE/'AUTHOR_COMPARISON_RESULTS.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
