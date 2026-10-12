#!/usr/bin/env python3
"""Independent static identities and synthetic validator logic; no galaxy solves."""
import os
for key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS',
            'VECLIB_MAXIMUM_THREADS', 'NUMEXPR_NUM_THREADS'):
    os.environ[key] = '1'
import sys
sys.dont_write_bytecode = True
import datetime
import hashlib
import json
import math
from pathlib import Path
import resource
import time
import types
import numpy as np
from scipy.integrate import quad

HERE = Path(__file__).resolve().parent
RUNTIME = Path('/Users/jonBridger/.codex/campaigns/observations-to-toe-24h-20261012')
OUT = RUNTIME/'gravity/response_inverse/independent_static_validation_review'
MANIFEST = json.loads((OUT/'snapshot_manifest_v1.json').read_text())
SOURCES = {Path(r['original']).name:r for r in MANIFEST['sources']}


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def guard():
    assert time.time() < json.loads((RUNTIME/'DEADLINE.json').read_text())['packaging_epoch']
    assert not any((RUNTIME/p).exists() for p in ['STOP_REQUESTED.json','USER_STOP_REQUESTED','STOP_CAMPAIGN.json'])
    for row in SOURCES.values():
        assert sha(row['original']) == sha(row['snapshot']) == row['sha256']


def subject(name):
    row = SOURCES[name+'.py']
    module = types.ModuleType(name)
    module.__file__ = row['original']
    sys.modules[name] = module
    exec(compile(Path(row['snapshot']).read_text(),row['original'],'exec'),module.__dict__)
    return module


def ramp(a, low, high):
    if a <= low:
        return 1.
    if a >= high:
        return 0.
    return math.log(high/a)/math.log(high/low)


def stated_B(s, low, high):
    # Literal transcription of the document's proposed primitive, the subject.
    d = math.log(high/low)
    if s <= low*low:
        return s
    if s >= high*high:
        return (high*high-low*low)/(2*d)
    return (s*math.log(high/math.sqrt(s))+(s-low*low)/2)/d


def primitive_controls():
    low, high = 2., 5.
    checks = []
    for s in [0., 2., 4., 4.000001, 10., 24.999999, 25., 100.]:
        cuts = sorted(set([0.,s]+[x for x in [low*low, high*high] if 0<x<s]))
        expected = sum(quad(lambda u:ramp(math.sqrt(u),low,high),a,b,
                            epsabs=1e-12,epsrel=2e-13)[0] for a,b in zip(cuts[:-1],cuts[1:]))
        actual = stated_B(s,low,high)
        assert abs(actual-expected) < 2e-12
        scale = 1e-10
        scaled = stated_B(s*scale*scale,low*scale,high*scale)/(scale*scale)
        assert abs(scaled-actual) < 2e-12
        checks.append({'s':s,'stated':actual,'independent_integral':expected,'SI_homogeneity_error':abs(scaled-actual)})
    derivatives = []
    for knot,expected in [(low*low,1.),(high*high,0.)]:
        h = knot*1e-6
        value = stated_B(knot,low,high)
        left = (value-stated_B(knot-h,low,high))/h
        right = (stated_B(knot+h,low,high)-value)/h
        assert max(abs(left-expected),abs(right-expected)) < 1e-6
        derivatives.append({'s':knot,'expected':expected,'left':left,'right':right})
    return {'primitive_values':checks,'one_sided_first_derivatives':derivatives}


def variation_controls():
    # One spatial dimension, 4*pi*G=1, fixed endpoint variations h(0)=h(1)=0.
    # Psi' stays positive and crosses one response knot. No field solver is used.
    low, high, weight = .5, 1.5, .4
    knot = (-.8+math.sqrt(.64+.06))/.3
    h = lambda x:x*x*(1-x)**2
    hp = lambda x:2*x-6*x*x+4*x**3
    phi = lambda x:.3*x+.1*x*x+.08*math.sin(math.pi*x)
    phip = lambda x:.3+.2*x+.08*math.pi*math.cos(math.pi*x)
    phipp = lambda x:.2-.08*math.pi**2*math.sin(math.pi*x)
    psip = lambda x:.4+.8*x+.15*x*x
    psipp = lambda x:.8+.3*x
    rho = lambda x:psipp(x)+.17
    integrate = lambda f:quad(f,0.,1.,points=[knot],epsabs=2e-12,epsrel=2e-12,limit=100)[0]
    def static(p,q):
        def value(x):
            u = psip(x)+q*hp(x)
            f = u*u+weight*stated_B(u*u,low,high)
            return .5*(-2*(phip(x)+p*hp(x))*u+f)-rho(x)*(phi(x)+p*h(x))
        return integrate(value)
    def response_derivative(x):
        a=psip(x)
        return 1+weight*ramp(a,low,high)-(weight/math.log(high/low) if low<a<high else 0.)
    expected_phi = -.17/30
    expected_psi = integrate(lambda x:(phipp(x)-response_derivative(x)*psipp(x))*h(x))
    e=1e-5
    actual_phi=(static(e,0)-static(-e,0))/(2*e)
    actual_psi=(static(0,e)-static(0,-e))/(2*e)
    assert abs(actual_phi-expected_phi)<2e-9
    assert abs(actual_psi-expected_psi)<2e-9
    return {'normalization':'4*pi*G=1','delta_Phi_expected':expected_phi,'delta_Phi_central':actual_phi,
            'delta_Phi_N_expected':expected_psi,'delta_Phi_N_central':actual_psi,
            'absolute_errors':[abs(actual_phi-expected_phi),abs(actual_psi-expected_psi)]}


def hessian_controls():
    low,high,weight=.5,1.5,.4
    u=np.array([.6,.3,.4]);a=np.linalg.norm(u);d=math.log(high/low)
    n=1+weight*ramp(a,low,high);derivative=-weight/(a*d)
    expected=2*n*np.eye(3)+2*derivative/a*np.outer(u,u)
    f=lambda v:float(v@v)+weight*stated_B(float(v@v),low,high)
    step=1e-4
    numerical=np.zeros((3,3));eye=np.eye(3)
    for i in range(3):
        for j in range(3):
            ei,ej=step*eye[i],step*eye[j]
            numerical[i,j]=(f(u+ei+ej)-f(u+ei-ej)-f(u-ei+ej)+f(u-ei-ej))/(4*step*step)
    error=float(np.max(abs(numerical-expected)))
    assert error<2e-6
    eig=np.linalg.eigvalsh(expected)
    wanted=np.sort([2*n,2*n,2*(n+a*derivative)])
    np.testing.assert_allclose(eig,wanted,rtol=1e-14,atol=1e-14)
    # Two adjacent ramps satisfying D strictly, including both constant tails.
    knots=[.3,.6,1.2];weights=[.5*math.log(2)*(1+.5*math.log(2)),.5*math.log(2)]
    energy=lambda v:float(v@v)+sum(w*stated_B(float(v@v),l,h) for w,l,h in zip(weights,knots[:-1],knots[1:]))
    rng=np.random.default_rng(971)
    gaps=[]
    for _ in range(250):
        x,y=rng.normal(size=(2,3))*rng.uniform(0,3,size=(2,1));t=rng.uniform()
        gaps.append(t*energy(x)+(1-t)*energy(y)-energy(t*x+(1-t)*y))
    assert min(gaps)>-1e-12
    bad_n=1+3*ramp(1.9,1.,2.)
    bad_longitudinal=2*(bad_n-3/math.log(2))
    assert bad_longitudinal<0
    return {'matrix_max_absolute_error':error,'eigenvalues':eig.tolist(),
            'expected_eigenvalues':wanted.tolist(),'D_min_sampled_Jensen_gap':min(gaps),
            'M_counterexample_longitudinal_eigenvalue':bad_longitudinal,
            'knots':'Hessian formula applies off knots; continuous gradient and one-sided limits suffice for convexity.'}


def boundary_controls(op,validator):
    fake=OUT/'boundary_fixture';fake.mkdir(exist_ok=True)
    name='SYNTHETIC'
    r=np.array([.5,.83,1.2,2.7,4.]);c=np.array([.1,.5,.9])
    base={'radius':r,'cosine':c,'angular_weights':np.array([.2,.5,.3]),
          'ur':np.arange(15,dtype=float).reshape(5,3),'uz':-np.arange(15,dtype=float).reshape(5,3),
          'R':np.array([.83,2.7]),'mr':np.array([7.125,12.375]),'mz':np.array([.2,.4]),
          'nr':np.array(5),'nc':np.array(3),'lmax':np.array(4)}
    original={key:value.tobytes() for key,value in base.items()}
    base_cache=fake/f'newtonian_field_{name}_base.npz';np.savez(base_cache,**base)
    np.savez(fake/'baryonic_forward_64.npz',**{name+'_A':np.array([1.,2.]),
             name+'_gas_masses':np.array([3.,4.]),name+'_disk_masses':np.array([5.,6.])})
    prior={'source_row':{'sigma':.12,'h':.34},'U':.56}
    calls=[]
    class FakeRingField:
        def __init__(self,a,sigma,gas,stars,height,hankel):
            calls.append({'constructor':[a.tolist(),sigma,gas.tolist(),stars.tolist(),height,hankel]})
        def __call__(self,radial,vertical):
            calls.append({'radius':np.hypot(radial,vertical).copy(),'radial':radial.copy(),'vertical':vertical.copy()})
            return radial+3*vertical,2*radial-vertical
    saved=(op.OUT,op.field.DATA,op.field.RingField)
    try:
        op.OUT=op.field.DATA=fake;op.field.RingField=FakeRingField
        result=validator.boundary_extension(name,base,prior)
        count=(len(result['radius'])-len(r))//2
        assert count==2 and len(calls)==2
        assert calls[0]['constructor'][-1]==8192
        np.testing.assert_allclose(calls[0]['constructor'][3],.56*np.array([5.,6.]))
        assert np.all(np.diff(result['radius'])>0)
        assert result['radius'][0]==r[0]/2 and result['radius'][-1]==r[-1]*2
        for key in ['radius','ur','uz']:
            assert result[key][count:count+len(r)].tobytes()==original[key]
        for key in ['cosine','angular_weights','R','mr','mz','nc','lmax']:
            assert result[key].tobytes()==original[key]
        assert int(result['nr'])==int(base['nr'])+2*count
        assert all(base[key].tobytes()==value for key,value in original.items())
        rr=np.r_[result['radius'][:count],result['radius'][-count:]]
        np.testing.assert_allclose(calls[1]['radius'],np.broadcast_to(rr[:,None],(2*count,len(c))))
        cached=validator.boundary_extension(name,base,prior)
        assert len(calls)==2
        assert all(cached[key].tobytes()==result[key].tobytes() for key in result)
        # Change only the synthetic parent-cache bytes; the cached extension must reject it.
        base_bytes=base_cache.read_bytes();base_cache.write_bytes(base_bytes+b'x')
        rejected=False
        try:
            validator.boundary_extension(name,base,prior)
        except AssertionError:
            rejected=True
        finally:
            base_cache.write_bytes(base_bytes)
        assert rejected
    finally:
        op.OUT,op.field.DATA,op.field.RingField=saved
    return {'old_radii':r.tolist(),'expanded_radii':result['radius'].tolist(),'nodes_each_end':count,
            'interior_coordinates_and_vectors_bitwise_preserved':True,'other_geometry_bitwise_preserved':True,
            'only_edge_source_evaluations':True,'edge_Hankel_order':8192,'cache_hit_avoids_source_call':True,
            'altered_parent_cache_rejected':True}


def validation_gate_controls(op,validator):
    fake=OUT/'validator_fixture';fake.mkdir(exist_ok=True)
    names=['NGC2976','UGC07577','KK98-251']
    labels=['clean','matrix_fail','refinement_fail','boundary_fail','negative','nonfinite','one_galaxy_fail','refined_negative']
    cases=[];operator_hashes={};received=[];geometry_calls=[]
    for i,label in enumerate(labels,1):
        weights=np.zeros(20);weights[0]=i/10;weights[1]=.12345678901234566
        cases.append({'family':'SYNTHETIC','constraints':label,'best_sampled':{'status':0,'weights':weights.tolist()}})
    cases += [{'family':'SYNTHETIC','constraints':'infeasible','best_sampled':{'status':2}},
              {'family':'SYNTHETIC','constraints':'absent','best_sampled':None}]
    for name in names:
        k=np.zeros((2,20));k[:,0]=2.
        receipt=fake/f'operator_{name}_v1.json';receipt.write_text(json.dumps({'K':k.tolist(),'g_N':[1.,1.]}))
        operator_hashes[name]=sha(receipt)
        for tag in ['base','refined','boundary_extension']:
            np.savez(fake/f'newtonian_field_{name}_{tag}.npz',synthetic=np.array([1.]))
    fits_path=fake/'synthetic_fits.json'
    fits_path.write_text(json.dumps({'operator_source_sha256':sha(op.__file__),'protocol_sha256':op.PROTOCOL_HASH,
                                    'cases':cases,'operator_receipts':operator_hashes}))
    def geo(name,tag='base',refine=False):
        geometry_calls.append([name,tag,refine])
        return {'R':np.array([1.,2.]),'name':name,'tag':tag},{},{}
    def edge(name,base,prior):
        return {'R':np.array([1.,2.]),'name':name,'tag':'boundary'}
    class FakeProjection:
        def __init__(self,data):self.data=data
        def combined(self,weights):
            received.append(weights.copy())
            i=round(weights[0]*10);label=labels[i-1];tag=self.data['tag'];name=self.data['name']
            force=np.full(2,1+2*weights[0])
            if label=='matrix_fail':force*=1.004
            if label=='refinement_fail' and tag=='refined':force*=1.006
            if label=='boundary_fail' and tag=='boundary':force*=1.004
            if label=='negative':force*=-1
            if label=='nonfinite':force[0]=np.nan
            if label=='one_galaxy_fail' and tag=='boundary' and name==names[-1]:force*=1.004
            if label=='refined_negative' and tag=='refined':force*=-1
            return force
    saved=(op.OUT,op.galaxy_geometry,op.LinearProjection,validator.boundary_extension,sys.argv)
    output=fake/'synthetic_validation.json'
    try:
        op.OUT=fake;op.galaxy_geometry=geo;op.LinearProjection=FakeProjection;validator.boundary_extension=edge
        sys.argv=['subject','--fits',str(fits_path),'--output',str(output)]
        validator.main()
    finally:
        op.OUT,op.galaxy_geometry,op.LinearProjection,validator.boundary_extension,sys.argv=saved
    result=json.loads(output.read_text())
    expected={'SYNTHETIC_'+label:(label=='clean') for label in labels}
    assert result['candidate_passes']==expected
    assert len(received)==3*3*len(labels)
    originals={c['best_sampled']['weights'][0]:np.array(c['best_sampled']['weights']) for c in cases[:-2]}
    assert all(v.tobytes()==originals[v[0]].tobytes() for v in received)
    assert geometry_calls==[[name,tag,refine] for name in names for tag,refine in [('base',False),('refined',True)]]
    clean=result['rows'][0]['candidate_results']['SYNTHETIC_clean']['relative_changes']
    assert all(v==0. for v in clean.values())
    assert result['rows'][-1]['candidate_results']['SYNTHETIC_one_galaxy_fail']['passed'] is False
    return {'candidate_passes':expected,'excluded_failed_or_absent_fit_candidates':True,
            'original_weights_bitwise_preserved':True,'projection_calls':len(received),
            'doubled_grid_request_flags':geometry_calls,'one_galaxy_failure_blocks_aggregate':True,
            'receipt_sha256':sha(output)}


def main():
    guard();started=time.time()
    result={'primitive':primitive_controls(),'variations':variation_controls(),'Hessian_convexity':hessian_controls()}
    op=subject('direct_galaxy_response_operator');validator=subject('direct_validate_inverse_fields')
    result['boundary_extension']=boundary_controls(op,validator)
    result['validation_gates']=validation_gate_controls(op,validator)
    guard()
    result.update(at=datetime.datetime.now(datetime.timezone.utc).isoformat(),passed=True,
                  script_sha256=sha(__file__),snapshot_manifest_sha256=sha(OUT/'snapshot_manifest_v1.json'),
                  elapsed_seconds=time.time()-started,max_rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
                  empirical_inputs_read=False,actual_galaxy_fields_or_fits_run=False)
    with (OUT/'synthetic_checks_v1.json').open('x') as stream:json.dump(result,stream,indent=2);stream.write('\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
