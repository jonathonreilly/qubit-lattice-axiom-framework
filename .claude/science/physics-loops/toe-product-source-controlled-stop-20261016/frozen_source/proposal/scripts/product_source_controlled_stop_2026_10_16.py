"""Bounded provenance verification only. No mathematical computation or approval."""
from pathlib import Path
import argparse,hashlib,json,sys
ROOT=Path(__file__).resolve().parents[2]
EXPECTED_MANIFEST_SHA256='121736e7f9ccf2a02ab30b3d8f792e0af897dfa681f310897913f5da9a3fcad1'
def ident(b):return {'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()}
def require(ok,message):
 if not ok:raise ValueError(message)
def same(b,row,label):require(ident(b)=={k:row[k] for k in ('bytes','sha256')},label)
def local(rel):
 p=ROOT/rel;require(p.resolve().is_relative_to(ROOT.resolve()),'capture escapes packet');return p

def verify():
 raw=local('INPUT_MANIFEST.json').read_bytes()
 require(ident(raw)['sha256']==EXPECTED_MANIFEST_SHA256,'input manifest changed')
 m=json.loads(raw);note=local(m['note']['path']).read_bytes();same(note,m['note'],'note changed')
 for row in m['bodies']:
  b=note[row['start_byte']:row['end_byte']];same(b,row,'embedded body changed: '+row['label'])
  same(Path(row['original']).read_bytes(),row,'original body changed: '+row['label'])
 for row in m['evidence']:
  same(local(row['capture']).read_bytes(),row,'evidence capture changed')
  same(Path(row['original']).read_bytes(),row,'original evidence changed: '+row['original'])
 parent=m['direct_parent'];same(Path(parent['path']).read_bytes(),parent,'direct parent changed')
 aliases={row['original']:local(row['capture']).read_bytes() for row in m['evidence']}
 def saved(path):return aliases[str(path)]
 def original_and_saved(path,row):
  same(saved(path),row,'receipt capture mismatch');same(Path(path).read_bytes(),row,'receipt original mismatch')
 members=0
 for path in m['selected_freezes']:
  f=json.loads(saved(path))
  for row in f['members']:
   p=Path(path).parent/row['path'];require(p.resolve().is_relative_to(Path(path).parent.resolve()),'freeze path escape')
   same(p.read_bytes(),row,'selected freeze member changed: '+str(p));members+=1
 for run in m['historical_runs']:
  p=Path(run['directory']);e=json.loads(saved(run['receipt']))
  require(e['exit_code']==0,'historical outcome changed')
  if run['kind']=='exposed_review_metadata_v1':
   require(e['argv'][1:]==['-B',str(p/'inspect_sources.py')] and e['cwd']==str(p),'historical command/source linkage')
   require(e['scientific_executions']==0 and e['source_unchanged_during_run'] is True and not e['timed_out'],'historical review scope')
   require(e['started_at']<=e['finished_at'] and e['elapsed_seconds']>=0 and e['timeout_seconds']==30,'historical timing')
   require(saved(p/'inspect_sources.py')==saved(p/'metadata/executed_source.py'),'executed review source differs')
   require(ident(saved(p/'inspect_sources.py'))['sha256']==e['source_sha256'],'review source digest')
   require(saved(p/'record_metadata.py')==saved(p/'metadata/launcher_source.py'),'launcher capture differs')
   require(ident(saved(p/'record_metadata.py'))['sha256']==e['launcher_sha256'],'launcher digest')
   require(saved(p/'metadata/stderr')==b'','historical stderr changed')
  elif run['kind']=='root_metadata_v1':
   require(e['argv'][1]==e['child_source_at_launch']['path'],'root argv/source-at-launch linkage')
   original_and_saved(e['child_source_at_launch']['path'],e['child_source_at_launch'])
   original_and_saved(e['source_capture']['path'],e['source_capture'])
   require(saved(e['child_source_at_launch']['path'])==saved(e['source_capture']['path']),'root captured child differs')
   for key in ('stdout','stderr','recorder'):original_and_saved(e[key]['path'],e[key])
   require(e['start_utc']<=e['end_utc'] and e['elapsed_seconds']>=0,'root timing')
  else:raise ValueError('unknown historical receipt schema')
 for path in m['source_decisions'].values():
  e=json.loads(saved(path));require(e['kind']=='root_conditional_analytical_acceptance' and e['scientific_executions']==0,'source decision scope')
  for row in e['sources']:same(Path(row['path']).read_bytes(),row,'source decision binding')
  q=e.get('qualification',e.get('qualifications'));same(Path(q['path']).read_bytes(),q,'controlling qualification binding')
 require(all(v is None for v in m['integration'].values()),'source-only integration fields changed')
 require(m['scientific_executions']==0 and m['editable_prompt_files_changed']==[],'scope changed')
 return dict(scope='source identities and historical metadata only; not proof or scientific execution',bodies=len(m['bodies']),evidence_aliases=len(m['evidence']),selected_freeze_members=members,historical_metadata_runs=len(m['historical_runs']),scientific_executions=0,wrapper_root_approval=None,canonical_execution=None,publication=None)

def main():
 global ROOT
 parser=argparse.ArgumentParser(description=__doc__)
 parser.add_argument('--packet-root',type=Path,default=ROOT,help='exact frozen source-packet directory; supports unchanged helper copied to another location')
 parser.add_argument('--require-approved',action='store_true',help='refuse: this source packet cannot authorize canonical/publication use')
 args=parser.parse_args();ROOT=args.packet_root.resolve()
 try:result=verify()
 except (OSError,KeyError,ValueError,TypeError) as error:
  print(json.dumps({'metadata_verification':'failed','reason':str(error),'scientific_executions':0}));return 1
 if args.require_approved:
  result.update(metadata_verification='verified',approval='refused',reason='Source acceptance is real; this wrapper, selected base, canonical execution, staged review and child publication remain unbound.')
  print(json.dumps(result,indent=2));return 2
 result['metadata_verification']='verified';print(json.dumps(result,indent=2));return 0
if __name__=='__main__':sys.exit(main())
