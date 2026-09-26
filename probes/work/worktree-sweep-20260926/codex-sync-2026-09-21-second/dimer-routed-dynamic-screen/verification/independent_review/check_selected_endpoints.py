#!/usr/bin/env python3
"""Two phases: reconstruct selected binaries first, then compare saved fields."""
from pathlib import Path
from datetime import datetime,timezone
import json,sys
sys.dont_write_bytecode=True
import numpy as np
from independent_decode import (identity,seeded_colors,decode_geometry,read_state,
                                reconstruct_fields,as_json_complex,verify_physical_keys)
OUT=Path(__file__).resolve().parent
ROOT=Path('/Users/jonreilly/Documents/Codex/physics-sync-2026-09-21-second/dimer_routed_dynamic_screen')

def exact_identity(r,path=None):
    value=identity(path or r['path'])
    assert (value['bytes'],value['sha256'])==(r['bytes'],r['sha256']),(r,value)
    return value

def reconstruct():
    selected=json.loads((OUT/'ENDPOINT_SELECTION.json').read_text())
    m=json.loads((ROOT/'MANIFEST.json').read_text());d=json.loads((ROOT/'DISPATCH.json').read_text())
    assert len(m['jobs'])==960 and len({j['seed'] for j in m['jobs']})==960
    assert len({(j['N'],j['kind'],j['replicate']) for j in m['jobs']})==960
    exact_identity(d['manifest']);exact_identity(d['wrapper']);exact_identity(m['binary'])
    sources=[]
    for s in d['source_snapshots']:
        value=exact_identity(s['original'],s['snapshot']['path']);exact_identity(s['snapshot'])
        sources.append(value)
    # The frozen dispatch predates the acknowledged prose-only gamma qualifier.
    prior=OUT.parent/'dimer_routed_f1_fix/DIMER_ROUTED_RECORD_TRANSPORT.before.md'
    exact_identity(m['construction'],prior)
    for role in ['protocol','source','setup']:exact_identity(m[role])
    jobs={(j['N'],j['kind'],j['replicate']):j for j in m['jobs']}
    geos={(g['N'],g['kind']):g for g in m['geometry']}
    rows=[];geo_rows=[]
    for cell in selected['cells']:
        n,kind=cell['N'],cell['geometry']
        declarations=[j for j in m['jobs'] if (j['N'],j['kind'])==(n,kind)]
        assert len(declarations)==cell['declared_history_count']
        assert sorted(j['replicate'] for j in declarations)==list(range(1,len(declarations)+1))
        gr=geos[n,kind];exact_identity(gr['file']);g=decode_geometry(gr['file']['path'])
        assert g['N']==n
        if kind=='winding':
            assert np.array_equal((g['xyz']+np.array([1,0,0]))%n,
                                  np.column_stack((g['white']//(n*n),(g['white']//n)%n,g['white']%n)))
        else:assert gr['generator']['proposals']==8*n**3 and gr['generator']['accepted_flips']>0
        geo_rows.append({'N':n,'kind':kind,'geometry_identity':g['identity'],'routes':g['route_summary']})
        for rep in cell['replicate_ids']:
            job=jobs[n,kind,rep];path=Path(job['output']);state=Path(str(path)+'.state')
            # Receipt existence is only a completion gate; no JSON observable
            # or receipt payload is read during this reconstruction phase.
            assert Path(str(path)+'.receipt.json').exists()
            assert job['command']==[m['binary']['path'],'run',gr['file']['path'],str(job['seed']),str(path)]
            sizeindex=[16,32,64,128].index(n);kindindex=['winding','irregular'].index(kind)
            assert job['seed']==202609211810+100000*sizeindex+10000*kindindex+rep-1
            keys,colors=read_state(state,n);initial,rejected=seeded_colors(job['seed'],g['K'])
            assert np.array_equal(colors,initial)
            counts=np.bincount(initial,minlength=14)
            assert np.array_equal(np.bincount(colors[keys],minlength=14),counts)
            physical=verify_physical_keys(g,keys)
            f0=reconstruct_fields(initial,g['xyz'],n);ff=reconstruct_fields(colors[keys],g['xyz'],n)
            rows.append({'N':n,'kind':kind,'replicate':rep,'seed':job['seed'],'job':job,
                         'state_identity':identity(state),'full_initial_lookup_rng_matches':True,
                         'initial_color_draw_rejections':rejected,'keys_checked':g['K'],
                         'physical_record_check':physical,'color_counts':counts.tolist(),
                         'initial_fields':as_json_complex(f0),'final_fields':as_json_complex(ff)})
            print('reconstructed selected endpoint',n,kind,rep,flush=True)
    assert len(rows)==16
    result={'created_utc':datetime.now(timezone.utc).isoformat(),
            'read_boundary':'Selected binary states reconstructed without reading any history JSON/receipt payload or aggregate output.',
            'manifest':identity(ROOT/'MANIFEST.json'),'dispatch':identity(ROOT/'DISPATCH.json'),
            'binary':m['binary'],'frozen_sources':sources,'geometry_checks':geo_rows,'rows':rows}
    (OUT/'SELECTED_RECONSTRUCTION.json').write_text(json.dumps(result,indent=2)+'\n')

def compare():
    seal=json.loads((OUT/'SELECTED_RECONSTRUCTION_SEAL.json').read_text())
    for r in seal['artifacts']:exact_identity(r)
    r=json.loads((OUT/'SELECTED_RECONSTRUCTION.json').read_text())
    rows=[];evidence=[]
    for a in r['rows']:
        path=Path(a['job']['output']);receiptpath=Path(str(path)+'.receipt.json')
        receipt=json.loads(receiptpath.read_text())
        assert receipt['status']=='complete_verified_receipt' and receipt['returncode']==0
        assert receipt['job']==a['job']
        for item in receipt['outputs']:evidence.append(exact_identity(item))
        evidence.append(identity(receiptpath));exact_identity(a['state_identity'])
        value=json.loads(path.read_text())
        assert (value['N'],value['seed'],value['mode'])==(a['N'],a['seed'],'production')
        assert value['geometry']==a['job']['command'][2]
        assert value['pairs']==a['keys_checked'] and value['channels']==5*a['keys_checked']
        assert value['minimum_nontrivial_cycle']>=a['N']//2
        assert value['gamma']==1 and value['k0']==1.1
        assert value['color_counts']==a['color_counts']
        assert value['key_permutation_verified'] and value['counts_verified']
        assert 0<=value['color_changes']<=value['accepted']<=value['attempts']
        assert [s['t'] for s in value['snapshots']]==[0,7/16,7/8,21/16,7/4]
        errors=[]
        for index,key in [(0,'initial_fields'),(-1,'final_fields')]:
            independently=np.array(a[key]);stored=np.array(value['snapshots'][index]['fields'])
            assert stored.shape==(3,6,2)
            diff=independently-stored
            error=float(np.max(np.hypot(diff[:,:,0],diff[:,:,1])))
            assert error<1e-8;errors.append(error)
        assert Path(str(path)+'.stderr').read_bytes()==b''
        rows.append({'N':a['N'],'kind':a['kind'],'replicate':a['replicate'],
                     'keys_checked':a['keys_checked'],'initial_final_max_complex_error':errors,
                     'complete_receipt_and_all_selected_payload_hashes_verified':True})
        print('compared selected endpoint',a['N'],a['kind'],a['replicate'],'max error',max(errors),flush=True)
    result={'scope':'Only the 16 preselected endpoints; no aggregate production statistics or analyzer read.',
            'selected_count':len(rows),'total_pair_keys_checked':sum(x['keys_checked'] for x in rows),
            'max_complex_Fourier_error':max(max(x['initial_final_max_complex_error']) for x in rows),
            'rows':rows,'authenticated_selected_evidence':evidence,
            'intermediate_time_fields_independently_reconstructed':False,
            'full_trajectory_or_all_RNG_properties_checked':False}
    (OUT/'SELECTED_COMPARISON_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')

if __name__=='__main__':
    {'reconstruct':reconstruct,'compare':compare}[sys.argv[1]]()
