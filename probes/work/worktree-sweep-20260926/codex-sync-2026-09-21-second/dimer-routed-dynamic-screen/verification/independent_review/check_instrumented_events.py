#!/usr/bin/env python3
"""Small implementation traces; all generated files stay in this directory."""
from pathlib import Path
from datetime import datetime,timezone
from itertools import product
import json,random,struct,subprocess,sys,time,hashlib
sys.dont_write_bytecode=True
import numpy as np
from independent_decode import (identity,FEATURE,DIRECTIONS,decode_geometry,
                                seeded_colors,read_state,reconstruct_fields)
OUT=Path(__file__).resolve().parent
RAW=OUT.parent
PROD=Path('/Users/jonreilly/Documents/Codex/physics-sync-2026-09-21-second/dimer_routed_dynamic_screen')

def execute(cmd,prefix):
    start=time.monotonic();p=subprocess.run([str(v) for v in cmd],capture_output=True)
    Path(str(prefix)+'.stdout').write_bytes(p.stdout);Path(str(prefix)+'.stderr').write_bytes(p.stderr)
    Path(str(prefix)+'.receipt.json').write_text(json.dumps({'created_utc':datetime.now(timezone.utc).isoformat(),
        'command':[str(v) for v in cmd],'exit_code':p.returncode,'elapsed_seconds':time.monotonic()-start,
        'stdout_sha256':hashlib.sha256(p.stdout).hexdigest(),'stderr_sha256':hashlib.sha256(p.stderr).hexdigest()},indent=2)+'\n')
    assert p.returncode==0,(cmd,p.stderr.decode())
    assert not p.stderr,(cmd,p.stderr.decode())

def own_fixture(n,kind,path):
    xyz=list(product(range(n),repeat=3));index={v:i for i,v in enumerate(xyz)}
    def move(v,i):return tuple((v[j]+(1 if i==j else 0))%n for j in range(3))
    pairs={}
    starts=[v for v in xyz if (sum(v)%2==0 if kind=='winding' else v[0]%2==0)]
    for a in starts:
        b=move(a,0);pairs[a]=b;pairs[b]=a
    accepted=0
    if kind=='irregular':
        rand=random.Random(531921)
        for _ in range(8*n**3):
            a=rand.choice(xyz);i,j=rand.sample(range(3),2)
            b,d=move(a,i),move(a,j);c=move(b,j)
            if pairs[a]==b and pairs[d]==c:new=[(a,d),(b,c)]
            elif pairs[a]==d and pairs[b]==c:new=[(a,b),(d,c)]
            else:continue
            for v,w in new:pairs[v]=w;pairs[w]=v
            accepted+=1
        assert accepted>0
    path.write_bytes(b'DRPAIR01'+struct.pack('<I',n)+np.array([index[pairs[v]] for v in xyz],dtype='<u4').tobytes())
    return accepted

def run():
    directory=OUT/'small_event_controls';directory.mkdir(exist_ok=False)
    source=RAW/'dimer_routed_dynamics.cpp';text=source.read_text()
    assert identity(source)['sha256']=='473e2981132f06bbf1fcf5f1b4dbf28e004d391485dc468d4dd93cc7c63f9dcb'
    replacements=[
      ('    std::vector<U>key(g.K);',
       '    std::ofstream catalog(output+".channels");\n'
       '    for(const auto &z:channels)catalog<<z.l<<","<<z.u<<","<<z.v<<","<<z.r<<","<<int(z.axis)<<","<<int(z.sign)<<"\\n";\n'
       '    catalog.close();std::ofstream trace(output+".trace");trace<<std::setprecision(17);\n'
       '    std::vector<U>key(g.K);'),
      ('            const Channel &c=channels[rng.bounded(channels.size())];',
       '            uint64_t chosen=rng.bounded(channels.size());const Channel &c=channels[chosen];'),
      ('            if(rng.bounded(42)<uint64_t(numerator)){std::swap(key[c.u],key[c.v]);++accepted;changed+=a!=b;}',
       '            uint64_t draw=rng.bounded(42);\n'
       '            trace<<t<<","<<chosen<<","<<key[c.u]<<","<<key[c.v]<<","<<h2<<","<<numerator<<","<<draw<<"\\n";\n'
       '            if(draw<uint64_t(numerator)){std::swap(key[c.u],key[c.v]);++accepted;changed+=a!=b;}')]
    modified=text
    for old,new in replacements:
        assert modified.count(old)==1;modified=modified.replace(old,new)
    instrumented=directory/'instrumented.cpp';instrumented.write_text(modified)
    (directory/'INSTRUMENTATION.json').write_text(json.dumps({'source':identity(source),
        'changes':[{'old':a,'new':b} for a,b in replacements],
        'instrumented':identity(instrumented),
        'scope':'Only logs channel catalog and existing random draws; no extra RNG draw or altered state update.'},indent=2)+'\n')
    binary=directory/'instrumented';execute(['clang++','-std=c++17','-O2',instrumented,'-o',binary],directory/'compile')
    manifest=json.loads((PROD/'MANIFEST.json').read_text());original=Path(manifest['binary']['path'])
    assert identity(original)==manifest['binary']
    rows=[]
    for kind in ['winding','irregular']:
        geom=directory/(kind+'.bin');flips=own_fixture(8,kind,geom);g=decode_geometry(geom)
        seed=761003 if kind=='winding' else 761027
        expected_colors,_=seeded_colors(seed,g['K'])
        plain=directory/(kind+'_original.json');logged=directory/(kind+'_instrumented.json')
        execute([original,'validate',geom,seed,plain],directory/(kind+'_original_run'))
        execute([binary,'validate',geom,seed,logged],directory/(kind+'_instrumented_run'))
        assert Path(str(plain)+'.state').read_bytes()==Path(str(logged)+'.state').read_bytes()
        x=json.loads(plain.read_text());y=json.loads(logged.read_text())
        for k in set(x)-{'wall_seconds'}:assert x[k]==y[k],k
        catalog=[tuple(map(int,line.split(','))) for line in Path(str(logged)+'.channels').read_text().splitlines()]
        assert catalog==g['catalog']
        state=np.arange(g['K']);event_rows=Path(str(logged)+'.trace').read_text().splitlines()
        epochs={t:[] for t in [.005,.01,.015,.02]}
        for line in event_rows:
            cells=line.split(',');epochs[float(cells[0])].append(tuple(map(int,cells[1:])))
        def s2(axis,a,b):
            return int((np.cross(FEATURE[a,:3],FEATURE[b,3:])+np.cross(FEATURE[b,:3],FEATURE[a,3:]))[axis])
        accepted=changed=same=0;errors=[]
        f=reconstruct_fields(expected_colors,g['xyz'],8);stored=np.array(y['snapshots'][0]['fields'])
        errors.append(float(np.max(abs(f-(stored[:,:,0]+1j*stored[:,:,1])))))
        for epoch,(t,events) in enumerate(epochs.items(),1):
            for chosen,ku,kv,h2_saved,numerator_saved,draw in events:
                l,u,v,r,axis,sign=catalog[chosen]
                assert (int(state[u]),int(state[v]))==(ku,kv)
                a,b,c,d=[int(expected_colors[state[z]]) for z in [l,u,v,r]]
                h2=sign*(s2(axis,a,b)+s2(axis,b,d)-s2(axis,a,c)-s2(axis,c,d))
                numerator=22+5*h2
                assert (h2,numerator)==(h2_saved,numerator_saved) and 0<=draw<42
                if draw<numerator:
                    state[u],state[v]=state[v],state[u];accepted+=1;changed+=b!=c;same+=b==c
            f=reconstruct_fields(expected_colors[state],g['xyz'],8);stored=np.array(y['snapshots'][epoch]['fields'])
            errors.append(float(np.max(abs(f-(stored[:,:,0]+1j*stored[:,:,1])))))
        assert accepted==y['accepted'] and changed==y['color_changes'] and len(event_rows)==y['attempts']
        final,colors=read_state(str(logged)+'.state',8)
        assert np.array_equal(final,state) and np.array_equal(colors,expected_colors)
        assert max(errors)<1e-12 and same>0
        rows.append({'kind':kind,'N':8,'seed':seed,'fixture_flips':flips,
                     'all_catalog_rows_reconstructed':len(catalog),'all_small_trace_attempts_checked':len(event_rows),
                     'accepted':accepted,'color_changes':changed,'same_color_distinct_key_swaps':same,
                     'all_five_snapshots_reconstructed_max_error':max(errors),
                     'instrumented_and_frozen_binary_state_rng_counters_and_fields_equal':True})
        print(json.dumps(rows[-1]),flush=True)
    result={'scope':'Two small validation traces, not production trajectory replay or an RNG statistical audit.',
            'frozen_production_binary':identity(original),'instrumented_binary':identity(binary),'rows':rows}
    (OUT/'SMALL_EVENT_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')

if __name__=='__main__':run()
