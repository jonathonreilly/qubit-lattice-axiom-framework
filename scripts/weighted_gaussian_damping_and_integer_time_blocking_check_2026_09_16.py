#!/usr/bin/env python3
"""Weighted curl conditionals and the actual resummed integer time-step law.

The one-dimensional Poisson comparison omits the coupled quadratic gauge
killing. It is a diagnostic of the reference measure, not a phase proof.
"""

from pathlib import Path as _InputPath
_REPO_ROOT = _InputPath(__file__).resolve().parents[1]
AUDIT_INPUT_PATHS = ['docs/WEIGHTED_GAUSSIAN_DAMPING_AND_INTEGER_TIME_BLOCKING_BOUNDED_THEOREM_NOTE_2026-09-16.md']
_INPUT_TEXT = {p: (_REPO_ROOT / p).read_text() for p in AUDIT_INPUT_PATHS}
assert 'exp[-(1/2) sum_(dual plaquettes p) w_p (d alpha)_p²],' in _INPUT_TEXT['docs/WEIGHTED_GAUSSIAN_DAMPING_AND_INTEGER_TIME_BLOCKING_BOUNDED_THEOREM_NOTE_2026-09-16.md']
def _emit_json(text):
    import json as _json
    payload = _json.loads(text)
    families = ['weighted_gaussian_check', 'integer_temporal_blocking']
    assert all(k in payload for k in families)
    payload["canonical_completed_families"] = families
    payload["canonical_total"] = len(families)
    output = _REPO_ROOT / 'logs/runner-cache/weighted_gaussian_damping_and_integer_time_blocking_check_2026_09_16.json'
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(_json.dumps(payload, indent=2, allow_nan=False)+"\n")
    print(_json.dumps(payload, indent=2, allow_nan=False))
    print("TOTAL: PASS="+str(len(families))+" FAIL=0")
    print('per_element: conditional precision and half-factor')
    print('per_site: finite4D curl complex')
    print('per_mode: finite512-mode convolution and cutoffs')
    print('per_block: Gaussian quadrature and Skellam arithmetic')
    print("lattice_wide: analytical statements checked in written proof, not executed; no volume-uniform phase computation")

AUDIT_TIMEOUT_SEC=180
import hashlib,itertools,json,math,time
from pathlib import Path
import numpy as np
from scipy.integrate import quad
from scipy.special import ive

def weighted_curl():
    vertices=list(itertools.product(range(3),repeat=4));vset=set(vertices);edges=[];idx={}
    def move(x,a):
        y=list(x);y[a]+=1;return tuple(y)
    for x in vertices:
        for a in range(4):
            if move(x,a) in vset:idx[a,x]=len(edges);edges.append((a,x))
    rows=[];types=[]
    for x in vertices:
        for a,b in itertools.combinations(range(4),2):
            keys=[(a,x),(b,move(x,a)),(a,move(x,b)),(b,x)]
            if all(k in idx for k in keys):
                row=np.zeros(len(edges))
                for k,s in zip(keys,[1,1,-1,-1]):row[idx[k]]+=s
                rows.append(row);types.append((a,b))
    C=np.array(rows);out=[];g=.4
    for delta in [1e-2,1e-4,1e-8]:
        bt=1/(g*g*delta);bs=1/(2*math.log(2*g*g/delta))
        weights=np.array([1/bs if a==0 else 1/bt for a,b in types])
        precision=C.T@(weights[:,None]*C)
        a0=float(precision[idx[0,(1,1,1,1)],idx[0,(1,1,1,1)]])
        ai=float(precision[idx[1,(1,1,1,1)],idx[1,(1,1,1,1)]])
        assert abs(a0-6/bs)<1e-12 and abs(ai-(2/bs+4/bt))<1e-12
        out.append({'delta':delta,'beta_temporal':bt,'beta_spatial':bs,'dual_temporal_precision':a0,'dual_spatial_precision':ai,'unit_current_damping_time':math.exp(-2*math.pi**2/a0),'unit_current_damping_space':math.exp(-2*math.pi**2/ai)})
    quadrature=[]
    for a,u,rho in [(1.,.3,1.3),(7.,-.4,2*math.pi),(100.,.7,2*math.pi)]:
        factor=1/math.sqrt(2*math.pi)
        actual=quad(lambda z:factor*math.exp(-z*z/2)*math.cos(rho*(u+z/math.sqrt(a))),-12,12,epsabs=2e-13)[0]+1j*quad(lambda z:factor*math.exp(-z*z/2)*math.sin(rho*(u+z/math.sqrt(a))),-12,12,epsabs=2e-13)[0]
        expected=np.exp(-rho*rho/(2*a)+1j*rho*u)
        assert abs(actual-expected)<2e-12
        wrong=np.exp(-rho*rho/a+1j*rho*u)
        assert abs(actual-wrong)>.01
        quadrature.append({'precision':a,'mean':u,'charge':rho,'quadrature_error':float(abs(actual-expected)),'missing_half_factor_error':float(abs(actual-wrong))})
    return {'curl_shape':list(C.shape),'anisotropic_conditionals':out,'conditional_character_quadrature':quadrature}

def integer_blocking():
    g=.4;T=1.;nfft=512;theta=2*math.pi*np.arange(nfft)/nfft;labels=np.arange(-nfft//2,nfft//2)
    reference=ive(abs(labels),T/g**2);assert abs(reference.sum()-1)<2e-13
    rows=[]
    for M in [64,256,1024,4096,8192]:
        delta=T/M;y=delta/(2*g*g);k=np.arange(-6,7);w=y**(k*k);w/=w.sum()
        phi=np.sum(w[:,None]*np.cos(k[:,None]*theta),axis=0)
        p=np.fft.fftshift(np.fft.ifft(phi**M).real)
        assert min(p)>-2e-13 and abs(p.sum()-1)<2e-12
        l1=float(np.sum(abs(p-reference)));bound=6*T*delta/g**4
        assert l1<bound
        step_poisson=ive(abs(k),delta/g**2)
        step_l1=float(np.sum(abs(w-step_poisson)))
        assert step_l1<24*y*y
        var=float(M*np.dot(w,k*k));real_gaussian=M/(2*math.log(1/y))
        tail=M*2*y**49/(1-y**15)
        chernoff=2*math.exp(-nfft//2)*float(np.dot(w,np.exp(k)))**M
        assert tail<1e-50 and chernoff<1e-90
        rows.append({'steps':M,'delta':delta,'blocked_L1_error':l1,'proved_sufficient_L1_bound':bound,'one_step_L1_error':step_l1,'blocked_integer_variance':var,'limiting_variance':T/g**2,'premature_real_gaussian_variance':real_gaussian,'omitted_jump_union_bound':tail,'cyclic_alias_chernoff_bound':chernoff})
    assert rows[-1]['blocked_L1_error']<rows[0]['blocked_L1_error']/30
    assert abs(rows[-1]['blocked_integer_variance']/(T/g**2)-1)<.001,rows
    assert rows[-1]['premature_real_gaussian_variance']>30*(T/g**2)
    return rows

def run():
    start=time.time();gaussian=weighted_curl();blocking=integer_blocking()
    _emit_json(json.dumps({'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'weighted_gaussian_check':gaussian,'integer_temporal_blocking':blocking,'seconds':time.time()-start},indent=2))

if __name__=='__main__':run()
