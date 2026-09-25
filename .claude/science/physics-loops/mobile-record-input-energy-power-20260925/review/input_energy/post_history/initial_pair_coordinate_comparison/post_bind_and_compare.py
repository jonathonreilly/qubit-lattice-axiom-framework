"""Released-source bindings and exact comparison with this checker's sealed PRE.

No author program is imported or executed. Every coefficient is mapped from
literal edge coordinates to the independently sealed Laurent certificate.
"""
from pathlib import Path
from hashlib import sha256
from datetime import datetime,timezone
from collections import defaultdict,Counter
from itertools import combinations
import json
import magnetic_increment_control as own

BASE=Path(__file__).resolve().parent
AUTHOR=BASE.parent/'photon-added-energy-personal'

def sha(p):return sha256(p.read_bytes()).hexdigest()
def centered(x,L):return tuple((int(t)+L//2)%L-L//2 for t in x)
def clean(d):return tuple(sorted((k,v) for k,v in d.items() if v))

def signed_word(rows,L):
    out=defaultdict(int)
    for a,b,power in rows:
        a=centered(a,L);b=centered(b,L)
        assert sum(abs(x-y) for x,y in zip(a,b))==1
        out[a,b]+=power
    return clean(out)

def positive_word(word):
    out=defaultdict(int)
    for (a,b),power in word:
        mu=next(i for i in range(3) if a[i]!=b[i])
        if b[mu]>a[mu]:out[a,mu]+=power
        else:out[b,mu]-=power
    return clean(out)

def independent_word(row,data):
    return signed_word([(data['vertices'][data['edges'][ed][0]],
                         data['vertices'][data['edges'][ed][1]],power)
                        for ed,power in row['flow']],data['summary']['side'])

def plaquette_boundary(origin,mu,nu,sign):
    x=tuple(origin);y=list(x);y[mu]+=1;y=tuple(y)
    z=list(y);z[nu]+=1;z=tuple(z)
    t=list(x);t[nu]+=1;t=tuple(t)
    out=defaultdict(int)
    for a,b in ((x,y),(y,z),(z,t),(t,x)):
        axis=next(i for i in range(3) if a[i]!=b[i])
        tail=a if b[axis]>a[axis] else b
        out[tail,axis]+=sign*(1 if b[axis]>a[axis] else -1)
    return out

def main():
    expected={'ADDED_REFERENCE_EXCITATION_ACTUAL_ENERGY_ROOT.md':'5feb53d99a0e1008019ff4563c16ba880ab3ab6e38fee5fd2682e62f081ee157',
              'AUTHOR_SEAL.json':'4dd7d35946c80fda3c70322c5ee61b475ea9f5fba4fde7a0e7cbae3521ed23cd'}
    for name,value in expected.items():assert sha(AUTHOR/name)==value
    seal=json.loads((AUTHOR/'AUTHOR_SEAL.json').read_text())
    frozen=BASE/'post_frozen_author';frozen.mkdir(exist_ok=True)
    origins=[]
    for rel,item in [*seal['files'].items(),('AUTHOR_SEAL.json',{'sha256':expected['AUTHOR_SEAL.json']})]:
        src=AUTHOR/rel;assert sha(src)==item['sha256']
        dst=frozen/rel;dst.parent.mkdir(parents=True,exist_ok=True);dst.write_bytes(src.read_bytes())
        origins.append({'path':str(src),'frozen_path':str(dst),'sha256':item['sha256'],
                        'bytes':src.stat().st_size})
    # PRE members remain immutable and are verified, not rebuilt.
    presealed=json.loads((BASE/'PRE_SEAL.json').read_text())
    assert sha(BASE/'PRE_SEAL.json')=='6dfea4b57bd88c1f127e385fa2c11294df50956079f748b48952fbf0b7965c43'
    for row in presealed['members']:assert sha(BASE/row['path'])==row['sha256']
    pins={'created_utc':datetime.now(timezone.utc).isoformat(),'author_inputs':origins,
          'preserved_PRE_seal_sha256':sha(BASE/'PRE_SEAL.json'),'preserved_PRE_members':len(presealed['members']),
          'external_source_handling':'Root SOURCE_PINS was read as metadata. The optical packet it names was not opened; the needed cube estimate is fully in the released note. The old flat helper was not opened or executed.'}
    (BASE/'POST_SOURCE_PINS.json').write_text(json.dumps(pins,indent=2)+'\n')
    independent=json.loads((BASE/'LAURENT_DATA_L8.json').read_text())
    ipoly={independent_word(row,independent):row['coefficient'] for row in independent['haar_defect_polynomial']}
    ipairs={tuple(sorted(centered(v,8) for v in row['A_pair'])):
            (len(row['terms']),sum(t['coefficient'] for t in row['terms']))
            for row in independent['changed_pairs']}
    author_poly=json.loads((frozen/'ENERGY_POLYNOMIAL_RESULTS.json').read_text())
    polynomial_rows=[]
    for row in author_poly['rows']:
        rp={signed_word(term['word'],row['side']):term['coefficient'] for term in row['words']}
        assert rp==ipoly
        comparisons=[]
        for pair in row['pair_rows']:
            key=tuple(sorted(centered(v,row['side']) for v in pair['pair']))
            actual=(pair['terms'],pair['flat_excess'])
            assert actual==ipairs.get(key,(0,0))
            comparisons.append({'pair':key,'terms':pair['terms'],'flat_excess':pair['flat_excess']})
        nonzero=sum(r['terms']!=0 for r in comparisons)
        assert nonzero==len(ipairs)==262
        polynomial_rows.append({'side':row['side'],'all_141_coefficients_equal_sealed_PRE':True,
                                'active_pairs':len(comparisons),'nonzero_pairs':nonzero,
                                'pair_summary_rows':comparisons})
    spectral=json.loads((frozen/'ENERGY_SPECTRAL_RESULTS.json').read_text())
    positive_poly={positive_word(word):value for word,value in ipoly.items() if word}
    seen={};fill_rows=[]
    for row in spectral['fillings']:
        word=tuple(( (tuple(edge[0]),int(edge[1])),int(power)) for edge,power in row['word'])
        total=defaultdict(int)
        for origin,mu,nu,sign in row['filling']:
            for edge,power in plaquette_boundary(origin,mu,nu,sign).items():total[edge]+=power
        assert clean(total)==word
        assert row['coefficient']==positive_poly[word]
        assert row['area_l1']==len(row['filling'])
        seen[word]=row['coefficient']
        fill_rows.append({'coefficient':row['coefficient'],'area':row['area_l1'],'word_exact':True,'surface_exact':True})
    assert seen==positive_poly
    assert sum(row['coefficient']*row['area']**2 for row in fill_rows)==436
    # Independent graph construction checks the author's conservative local
    # active union without invoking any author helper or polynomial builder.
    vertices,index,aa,n,edges,eid,axes=own.graph(16);aa=set(aa)
    def v(x):return index[tuple(t%16 for t in x)]
    negatives=set(map(v,[(1,1,0),(2,2,0)]))
    occupied_union=set(map(v,[(1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]))
    reverse=defaultdict(list)
    for a,b in edges:reverse[b].append(a)
    pairs=set()
    for values in reverse.values():pairs.update(combinations(sorted(values),2))
    active={(a,b) for a,b in pairs if {a,b}&negatives or (set(n[a])|set(n[b]))&occupied_union}
    neighborhood={x for a,b in active for x in [a,b,*n[a],*n[b]]}
    coords=[centered(vertices[x],16) for x in neighborhood]
    bounds=[[min(v[mu] for v in coords),max(v[mu] for v in coords)] for mu in range(3)]
    author_active={tuple(sorted(centered(x,16) for x in row['pair']))
                   for row in author_poly['rows'][1]['pair_rows']}
    assert {tuple(sorted((centered(vertices[a],16),centered(vertices[b],16)))) for a,b in active}==author_active
    assert all(-5<=x<=6 for coord in coords for x in coord)
    old=json.loads((frozen/'history/pre-electric-occupancy-correction/ENERGY_SPECTRAL_RESULTS.json').read_text())
    assert spectral['fillings']==old['fillings']
    histories=[]
    for previous,current in zip(old['rows'],spectral['rows']):
        assert (previous['side'],previous['epsilon'],previous['empty'])==(current['side'],current['epsilon'],current['empty'])
        if current['empty']:
            histories.append({'side':current['side'],'epsilon':current['epsilon'],'empty':True});continue
        for key in ('band_modes_k','vp','vlow','reference_mean_energy_times_tau'):
            assert previous[key]==current[key]
        assert previous['defect_energy_loss_times_tau']==current['magnetic_defect_energy_loss_times_tau']
        loss=current['electric_occupancy_energy_loss_times_tau']
        difference=previous['limiting_added_full_mean_energy_times_tau']-current['limiting_added_full_mean_energy_times_tau']
        assert abs(difference-loss)<1e-13
        growdiff=[]
        for pr,cu in zip(previous['finite_g_harmonic_rows'],current['finite_g_harmonic_rows']):
            assert pr['g']==cu['g']
            value=pr['uncut_harmonic_full_mean_increment_times_tau']-cu['uncut_harmonic_full_mean_increment_times_tau']
            assert abs(value-loss)<1e-13
            growdiff.append({'g':cu['g'],'old_minus_corrected':value})
        histories.append({'side':current['side'],'epsilon':current['epsilon'],'empty':False,
                          'electric_loss':loss,'old_minus_corrected_limit':difference,
                          'finite_g_corrections':growdiff})
    binding=[]
    for result,stdout,execution,code in [
        ('ENERGY_POLYNOMIAL_RESULTS.json','CONTROL.stdout','EXECUTION.json','prepared_energy_polynomial.py'),
        ('ENERGY_SPECTRAL_RESULTS.json','SPECTRAL.stdout','SPECTRAL_EXECUTION.json','energy_spectral_controls.py'),
        ('history/pre-electric-occupancy-correction/ENERGY_SPECTRAL_RESULTS.json',
         'history/pre-electric-occupancy-correction/SPECTRAL.stdout',
         'history/pre-electric-occupancy-correction/SPECTRAL_EXECUTION.json',
         'history/pre-electric-occupancy-correction/energy_spectral_controls.py')]:
        assert sha(frozen/result)==sha(frozen/stdout)
        info=json.loads((frozen/execution).read_text());assert info['code_sha256']==sha(frozen/code)
        assert info['exit_code']==0
        binding.append({'result':result,'sha256':sha(frozen/result),'stdout_exact_equal':True,
                        'execution_code_hash_matches':True,'author_exit_code':info['exit_code'],
                        'author_elapsed_seconds':info['elapsed_seconds']})
    assert spectral['source_sha256']==sha(frozen/'ENERGY_POLYNOMIAL_RESULTS.json')
    result={'source_pins_sha256':sha(BASE/'POST_SOURCE_PINS.json'),'PRE_45_members_unchanged':True,
            'author_20_members_and_seal_verified':True,'polynomial_rows':polynomial_rows,
            'all_140_oriented_fillings_verified':fill_rows,'independent_active_union':len(active),
            'independent_neighborhood_coordinate_bounds':bounds,'electric_correction_history':histories,
            'source_execution_bindings':binding,
            'code_sha256':sha(Path(__file__))}
    (BASE/'POST_EXACT_COMPARISON.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'author_members_verified':len(origins)-1,'preserved_PRE_members':len(presealed['members']),
                      'polynomial_sides':[r['side'] for r in polynomial_rows],
                      'exact_coefficient_comparisons':2*len(ipoly),'oriented_fillings':len(fill_rows),
                      'pair_summary_comparisons':sum(len(r['pair_summary_rows']) for r in polynomial_rows),
                      'history_rows':len(histories),'active_union_bounds':bounds,
                      'result_sha256':sha(BASE/'POST_EXACT_COMPARISON.json')},indent=2))

if __name__=='__main__':main()
