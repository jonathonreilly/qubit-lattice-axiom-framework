#!/usr/bin/env python3
"""Retrospective bookkeeping inventory of previously emitted coordinate data.
No model, inverse, quantum fixture or scientific test is rerun here.
"""
from pathlib import Path
import hashlib,json,datetime
root=Path(__file__).resolve().parent
raw=(root/'EXACT_RESULT.json').read_bytes(); data=json.loads(raw)
original={tuple(v) for v in data['original_coordinates']}
owner={tuple(v):c['axis'] for c in data['components'] for v in c['coordinates']}
all_sites=original|set(owner)
declared={tuple(sorted((tuple(a),tuple(b)))) for c in data['components'] for a,b in c['auxiliary_edges']+c['source_detuning_edges']}
rows=[]
for a in sorted(all_sites):
    for axis in range(3):
        b=list(a); b[axis]+=1; b=tuple(b)
        if b not in all_sites or (a not in owner and b not in owner): continue
        if a in original or b in original: kind='fresh_original'
        elif owner[a]!=owner[b]: kind='intercomponent'
        else: kind='same_component'
        ed=tuple(sorted((a,b)))
        rows.append({'edge':[list(ed[0]),list(ed[1])],'kind':kind,'declared':ed in declared,'component_a':owner.get(a),'component_b':owner.get(b)})
counts={}
for r in rows:
    key=r['kind']+('_declared' if r['declared'] else '_undeclared')
    counts[key]=counts.get(key,0)+1
out={'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'status':'Retrospective deterministic inventory of existing selected-fixture coordinates; not a predeclared check, independent validation, second model execution or new scientific fixture.','input':'EXACT_RESULT.json','input_sha256':hashlib.sha256(raw).hexdigest(),'inventory_source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'counts':counts,'all_NN_pairs_touching_fresh_within_recorded_factor_inventory':rows,'outside_inventory':'Additional occupied factors require an updated inventory and their own complete coupling/isolation budget.'}
(root/'ISOLATION_ADJACENCY_INVENTORY.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'retrospective_inventory_counts':counts,'output':'ISOLATION_ADJACENCY_INVENTORY.json'},indent=2))
