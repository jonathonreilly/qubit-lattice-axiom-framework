#!/usr/bin/env python3
"""Seal the bounded routed-transport review without modifying prior evidence."""
from pathlib import Path
import datetime,hashlib,json
HERE=Path(__file__).resolve().parent;RAW=HERE.parent

def ident(p):
    b=p.read_bytes();return {'path':str(p),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()}

def main():
    assert not (HERE/'FINAL_SEAL.json').exists()
    pre=json.loads((HERE/'PRE_COMPARISON_SEAL.json').read_text())
    for row in pre['artifacts']:assert ident(Path(row['path']))==row
    psource=pre['sources']['primary_source'];assert ident(Path(psource['path']))==psource
    for field in ['unchanged_formation_dependencies','procedures_reused_unchanged']:
        for row in pre['sources'][field]:assert ident(Path(row['path']))==row
    result=json.loads((RAW/'dimer_routed_transport_checks/RESULTS.json').read_text())
    sources=[]
    for name,h in result['sources_sha256'].items():
        row=ident(RAW/name);assert row['sha256']==h;sources.append(row)
    evidence=[ident(p) for p in sorted((RAW/'dimer_routed_transport_checks').iterdir()) if p.is_file()]
    evidence += [ident(RAW/name) for name in ['DIMER_ROUTED_TRANSPORT_RUN.log','DIMER_ROUTED_TRANSPORT_RUN.stderr']]
    manifest={'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'primary_sources':sources,
              'author_evidence_authenticated':evidence,
              'unchanged_formation_dependencies':pre['sources']['unchanged_formation_dependencies'],
              'procedures_reused_unchanged':pre['sources']['procedures_reused_unchanged'],
              'old_primary_fluctuation_note_imported':False,'external_literature_imports':[],
              'remaining_finding':{'id':'F1','source_line':277,'correction':'Qualify four propagating modes by gamma != 0; at gamma=0 all thirteen tangent modes are static.'}}
    (HERE/'FINAL_SOURCES.json').write_text(json.dumps(manifest,indent=2)+'\n')
    artifacts=[ident(p) for p in sorted(HERE.rglob('*')) if p.is_file() and p.name!='FINAL_SEAL.json']
    seal={'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'scope':'Bounded independent proof assessment and source comparison; no formal audit status.',
          'precomparison_seal':ident(HERE/'PRE_COMPARISON_SEAL.json'),'report':ident(HERE/'REPORT.md'),
          'source_manifest':ident(HERE/'FINAL_SOURCES.json'),'artifacts':artifacts,
          'failed_attempts_preserved':['failed_attempt_01/FAILURE_RECEIPT.json','failed_attempt_02/FAILURE_RECEIPT.json'],
          'unresolved_findings':['F1']}
    (HERE/'FINAL_SEAL.json').write_text(json.dumps(seal,indent=2)+'\n')
    print(json.dumps({'report':ident(HERE/'REPORT.md'),'seal':ident(HERE/'FINAL_SEAL.json'),
                      'artifact_count':len(artifacts),'primary_sources':len(sources),'author_evidence_files':len(evidence)},indent=2))

if __name__=='__main__':main()
