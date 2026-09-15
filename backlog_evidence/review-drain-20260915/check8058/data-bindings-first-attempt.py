from pathlib import Path
import json,hashlib,gzip,subprocess,sys
from fractions import Fraction as F
r=Path('/private/tmp/review-drain-20260915');q=r/'check8058';w=r/'author-pool/author-backlog';inv=json.loads((q/'inventory.json').read_text());anchors=json.loads((r/'8058-archive-anchor.json').read_text());sha=lambda b:hashlib.sha256(b).hexdigest();result={}
for c in inv['constituents']:
 a=anchors[str(c['pr'])];mp=Path(a['manifest_path']);assert sha(mp.read_bytes())==a['manifest_sha256'];m=json.loads(mp.read_text());maps={x['original_path']:x for x in m['entries']};raw=subprocess.check_output(['git','-C',str(r/'coordinator'),'ls-tree','-r','-z',c['head'],'--',a['prefix']]);git={}
 for line in raw.split(b'\0'):
  if line:
   meta,p=line.split(b'\t');mode,kind,blob=meta.decode().split();git[p.decode()]=(mode,blob)
 assert set(git)==set(maps)
 for p,x in maps.items():
  assert git[p]==(x['original_mode'],x['git_blob']);b=(mp.parent/x['stored_path']).read_bytes();assert sha(b)==x['stored_sha256'];d=gzip.decompress(b) if x['encoding']=='gzip' else b;assert d==(q/str(c['pr'])/'original'/p).read_bytes();assert sha(d)==x['raw_sha256']
 result[str(c['pr'])]={'archive_paths':len(maps),'manifest_sha256':a['manifest_sha256'],'mode_blob_and_all_decoded_bytes_match':True}
sys.path.insert(0,str(r/'unit8058/scripts'));import native_weak_electric_candidate_decoder_2026_09_08 as decoder
p=r/'unit8058/outputs/native_weak_electric_spectator_gap_2026_09_08_inputs';prefix=json.loads((p/'PREFIXES.json').read_text());rows=[]
for bridge in [0,3,9,12,36,96]:
 z,pr,vs=decoder.load(p/f'bridge_{bridge}.json',prefix);assert all(v[2]==next(t['word_count'] for t in pr['prefixes'] if int(t['boundary_used_mask'])==k[0] and t['bridge_count']==k[1]) for k,v in vs.items() if k!=(0,0));rows.append({'bridge':bridge,'candidate_rows':len(vs),'finite_binary64_values':512*len(vs),'sha256':sha((p/f'bridge_{bridge}.npz').read_bytes())})
result['candidate_arrays']={'scope':'Actual complete strict decode and all prefix word-count bindings, not a coefficient rerun; canonical decoder imported and source read, independent support control establishes prefix completeness','rows':rows}
a=anchors['8058'];map=a['mapping'];get=lambda suffix:next(q/'8058/original'/s for s in map if s.endswith(suffix))
pins=json.loads(get('native-l4-third-vertex-post-review/INPUTS.json').read_text());D=get('native-l4-third-vertex-run-1085/RESULT.json').parent
assert set(pins)=={'RESULT.json','SOLVE_VECTORS.json'}
for n,h in pins.items():assert sha((D/n).read_bytes())==h
v=json.loads((D/'SOLVE_VECTORS.json').read_text());z=json.loads((D/'RESULT.json').read_text());assert len(v['first'])==15 and len(v['second'])==15;assert all(len(row)==32 for row in list(v['first'].values())+v['second']);values=[F(x) for row in list(v['first'].values())+v['second'] for x in row];assert len(values)==960
assert {k:F(x) for k,x in z['particle_weights'].items()}=={'1':F(99225,4096),'3':0,'5':0}
result['third_vertex_data']={'exact_rational_entries':960,'saved_residual_vectors':30,'pin_membership':pins,'recorded_weight':'99225/4096','scope':'parsed all saved exact vectors and result; final live residual replay remains pending'}
(q/'data-bindings.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
