#!/usr/bin/env python3
"""Post-seal authentication and selective independent author-output checks.

No author module is imported or executed. The coefficient reconstruction
uses full-array torus convolution, not the author's index-based scatter.
"""
from pathlib import Path
import cmath,datetime,hashlib,itertools,json,math
import numpy as np

OUT=Path(__file__).resolve().parent
RAW=OUT.parent

def bind(p):
    b=p.read_bytes()
    return dict(path=str(p),bytes=len(b),sha256=hashlib.sha256(b).hexdigest())

def verify(rows):
    for row in rows:
        assert bind(Path(row['path']))==row,row['path']

def main():
    pre=json.loads((OUT/'PRE_COMPARISON_SEAL.json').read_text())
    verify(pre['artifacts']);verify(pre['source_bindings'])
    result=json.loads((RAW/'dimer_routed_quantitative_euler_checks/RESULTS.json').read_text())
    for name,digest in result['sources'].items():
        assert bind(RAW/name)['sha256']==digest
    independent=json.loads((OUT/'INDEPENDENT_RESULTS.json').read_text())
    for their,our in zip(result['open_cube_loads'],independent['open_cube_paths']):
        assert their['L']==our['L']
        assert their['ordered_paths']==our['ordered_pairs']
        assert their['physical_edges']==our['physical_edges']
        assert their['maximum_exact_load']==our['maximum_load']
        assert float(their['upper_bound_L4_over2'])==their['L']**4/2

    log=(RAW/'DIMER_ROUTED_QUANTITATIVE_EULER_RUN.log').read_text().splitlines()
    assert log[0]=='open_cube_loads PASS' and log[-1]=='linear_coefficients PASS'
    assert [json.loads(x) for x in log[1:-1]]==result['contracted_footprints']
    assert (RAW/'DIMER_ROUTED_QUANTITATIVE_EULER_RUN.stderr').read_bytes()==b''
    fixtures=[]
    for row in result['contracted_footprints']:
        L=row['L'];l=row['l'];m=row['pairs_in_footprint']
        assert L==2*l+1 and 2*m>=L**3
        assert row['inside_black']==(L**3+(-1)**l)//2
        assert row['outside_black']==m-row['inside_black']<=6*L**2
        if row['all_endpoint_pairs_checked']:
            assert row['checked_pairs']==m*(m-1)//2
        assert row['largest_physical_multiplicity']<=2
        assert row['max_path_load']<=L**4 and row['max_word_use']<=2*L**4
        assert row['max_weighted_word_use']<=12*L**5 and row['max_word_length']<=6*L
        assert row['variance_factor_bound']==48*L**2
        fixtures.append(dict(N=row['N'],radius=l,kind=row['kind'],
            theorem_global_radius_range=(l>=6 and 2*l+5<row['N']/2),
            interpretation='Finite geometric/counting control; no finite test is the all-N proof.'))
    ours=next(x for x in independent['contracted_footprints'] if x['N']==16 and x['kind']=='columnar')
    theirs=next(x for x in result['contracted_footprints'] if x['N']==16 and x['kind']=='columnar')
    assert ours['pairs']==theirs['pairs_in_footprint']
    assert ours['maximum_weighted_congestion']==theirs['max_weighted_word_use']
    assert 2*ours['maximum_word_path_length']-1==theirs['max_word_length']

    coefficient_rows=[]
    for row in result['linear_coefficients']:
        N,l=row['N'],row['l'];L=2*l+1
        coords=np.indices((N,N,N));black=(coords.sum(axis=0)%2==0)
        b=np.zeros((N,N,N),dtype=np.int64)
        b[black]=np.random.default_rng(199500+N).integers(-7,8,size=int(black.sum()))
        offsets=[d for d in itertools.product(range(-l,l+1),repeat=3) if sum(d)%2==0]
        coeff=np.zeros_like(b)
        for d in offsets:coeff+=np.roll(b,d,axis=(0,1,2))
        maximum=int(np.abs(coeff[black]).max())
        assert len(offsets)==row['cube_black_cardinality']==(L**3+(-1)**l)//2
        assert maximum<=7*len(offsets)
        assert maximum/len(offsets)==row['maximum_normalized_coefficient']
        phase_errors=[]
        for mode in row['modes']:
            k=[2*math.pi*x/N for x in mode['mode']]
            ordinary=[sum(cmath.exp(-1j*theta*r) for r in range(-l,l+1)) for theta in k]
            alternating=[sum((-1)**r*cmath.exp(-1j*theta*r) for r in range(-l,l+1)) for theta in k]
            phase=(math.prod(ordinary)+math.prod(alternating))/(2*len(offsets))
            error=abs(phase-complex(*mode['multiplier']))
            assert error<2e-15
            assert abs(abs(phase-1)-mode['error'])<2e-15
            expected=math.sqrt(3)*math.sqrt(sum((N*t)**2 for t in k))*l/N
            assert abs(expected-mode['uniform_bound'])<2e-15
            phase_errors.append(error)
        coefficient_rows.append(dict(N=N,radius=l,maximum_integer_convolution=maximum,
            block_cardinality=len(offsets),maximum_phase_comparison_error=max(phase_errors)))

    dev=RAW/'dimer_routed_development/quantitative_euler_index_api'
    old=(dev/'dimer_routed_quantitative_euler_check.py').read_text()
    new=(RAW/'dimer_routed_quantitative_euler_check.py').read_text()
    replacements=[('index[tuple(x%N for x in a)]','index(tuple(x%N for x in a))'),
                  ('index[tuple(map(int,a))]','index(tuple(map(int,a)))')]
    repaired=old
    for a,b in replacements:
        assert repaired.count(a)==1 and repaired.count(b)==0
        repaired=repaired.replace(a,b)
    assert repaired==new
    recovered=new
    for a,b in reversed(replacements):recovered=recovered.replace(b,a)
    assert recovered==old
    fix=json.loads((dev/'FIX_RECEIPT.json').read_text())
    assert hashlib.sha256(old.encode()).hexdigest()==fix['before_sha256']
    assert hashlib.sha256(new.encode()).hexdigest()==fix['after_sha256']
    assert (dev/'DIMER_ROUTED_QUANTITATIVE_EULER_RUN.log').read_text()=='open_cube_loads PASS\n'
    assert "TypeError: 'function' object is not subscriptable" in (dev/'DIMER_ROUTED_QUANTITATIVE_EULER_RUN.stderr').read_text()
    sources=[RAW/'DIMER_ROUTED_QUANTITATIVE_EULER_BOUND.md',RAW/'dimer_routed_quantitative_euler_check.py',
        RAW/'dimer_routed_transport_check.py',RAW/'dimer_routed_quantitative_euler_checks/RESULTS.json',
        RAW/'DIMER_ROUTED_QUANTITATIVE_EULER_RUN.log',RAW/'DIMER_ROUTED_QUANTITATIVE_EULER_RUN.stderr',
        *sorted(p for p in dev.iterdir() if p.is_file())]
    payload=dict(created_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
        status='pass',preseal_authentication=dict(artifacts=len(pre['artifacts']),source_bindings=len(pre['source_bindings'])),
        exact_shared_open_cube_rows=3,exact_shared_columnar_endpoint_inventory=True,
        author_fixture_scope=fixtures,independent_full_array_coefficient_comparisons=coefficient_rows,
        preserved_author_helper_failure=dict(before=fix['before_sha256'],after=fix['after_sha256'],
            exact_forward_and_inverse_recovery=True,only_replacements=replacements),
        author_files=[bind(p) for p in sources],
        scope='Full source/result/log reading plus selective reconstruction. No execution of the author suite, no all-N verification by enumeration, no production observable access.')
    (OUT/'AUTHOR_COMPARISON.json').write_text(json.dumps(payload,indent=2)+'\n')
    print(json.dumps({'status':'pass','coefficient_controls':coefficient_rows,'author_files':len(sources)},indent=2))

if __name__=='__main__':main()
