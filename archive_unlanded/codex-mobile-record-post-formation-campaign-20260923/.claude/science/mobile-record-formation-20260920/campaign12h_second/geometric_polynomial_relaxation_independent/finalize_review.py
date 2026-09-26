#!/usr/bin/env python3
"""Final seal with the post-comparison finding; preserves the pre-seal helper."""
from pathlib import Path
import datetime,hashlib,json,sys
import numpy,sympy
HERE=Path(__file__).resolve().parent
def identity(path):
    path=Path(path)
    return {'path':str(path),'bytes':path.stat().st_size,'sha256':hashlib.sha256(path.read_bytes()).hexdigest()}
pre=json.loads((HERE/'PRE_COMPARISON_SEAL.json').read_text())
comparison=json.loads((HERE/'AUTHOR_COMPARISON.json').read_text())
for section in ['sources','procedures_reused','dependencies_reused','external_extracts','artifacts']:
    for row in pre[section]:assert identity(row['path'])==row,(section,row['path'])
for row in comparison['author_evidence_sources']:assert identity(row['path'])==row
sources=pre['sources']+comparison['author_evidence_sources']
artifacts=[identity(p) for p in sorted(HERE.iterdir()) if p.is_file() and p.name!='FINAL_SEAL.json']
seal={'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
      'scope':'Bounded final-source mathematical review; no formal audit or landing verdict.',
      'sources':sources,'procedures_reused':pre['procedures_reused'],
      'dependencies_reused':pre['dependencies_reused'],'external_extracts':pre['external_extracts'],
      'artifacts':artifacts,'precomparison_seal':identity(HERE/'PRE_COMPARISON_SEAL.json'),
      'precomparison_artifacts_unchanged':True,'unresolved_mathematical_findings':[],
      'unresolved_executable_findings':comparison['findings'],
      'external_import_status':'JS1989 and Taggi statements, hypotheses and application conventions checked; whole published proofs not independently verified.',
      'runtime':{'python':sys.version,'numpy':numpy.__version__,'sympy':sympy.__version__},
      'not_done':['No whole author-suite rerun','No production trajectories','No primary edits','No Git mutations','No formal audit status']}
(HERE/'FINAL_SEAL.json').write_text(json.dumps(seal,indent=2)+'\n')
print(json.dumps({'report':identity(HERE/'REPORT.md'),'final_seal':identity(HERE/'FINAL_SEAL.json'),
                  'counts':{k:len(seal[k]) for k in ['sources','procedures_reused','dependencies_reused','external_extracts','artifacts']}},indent=2))
