#!/usr/bin/env python3
"""Post-seal authentication and independent direct-coefficient comparisons.
Does not import or execute the author checker; never writes primary files.
"""
from pathlib import Path
import hashlib,json,math,datetime
import numpy as np
from scipy.linalg import eigh
HERE=Path(__file__).resolve().parent
ROOT=HERE.parent

def ident(p):
    b=p.read_bytes()
    return dict(path=str(p.resolve()),bytes=len(b),sha256=hashlib.sha256(b).hexdigest())

def basis(cap):
    return sorted([(a,b,c) for a in range(cap+1) for b in range(cap+1)
                   for c in range(cap+1) if a+b+c<=cap],key=lambda x:(sum(x),x))

def quadratic(cap,K,w2):
    bs=basis(cap);ix={a:i for i,a in enumerate(bs)};H=np.zeros((len(bs),len(bs)))
    def f(n):return 1. if K is None else math.sqrt(max(0.,1-n/K))
    for col,ns in enumerate(bs):
        n=sum(ns)
        for i in range(3):
            H[col,col]+=(1+w2[i])/4*((ns[i]+1)*f(n)**2+ns[i]*f(n-1)**2)
            up=list(ns);up[i]+=2;up=tuple(up)
            if up in ix:
                v=(w2[i]-1)/4*math.sqrt((ns[i]+1)*(ns[i]+2))*f(n)*f(n+1)
                H[ix[up],col]+=v;H[col,ix[up]]+=v
    return bs,H

def linear(bs,K,z):
    ix={a:i for i,a in enumerate(bs)};W=np.zeros((len(bs),len(bs)),complex)
    for col,ns in enumerate(bs):
        for i in range(3):
            up=list(ns);up[i]+=1;up=tuple(up)
            if up not in ix:continue
            v=(z[i]+1j*z[3+i])/math.sqrt(2)*math.sqrt((ns[i]+1)*max(0.,1-sum(ns)/K))
            W[ix[up],col]+=v;W[col,ix[up]]+=v.conjugate()
    return W

def target(t,z):
    q=z[:3].copy();p=z[3:].copy();out=0.
    for i,w2 in enumerate([0.,.75,.75]):
        if w2==0: a=q[i];b=t*q[i]+p[i]
        else:
            w=math.sqrt(w2);co=math.cos(w*t);si=math.sin(w*t)
            a=co*q[i]-w*si*p[i];b=si/w*q[i]+co*p[i]
        out+=a*a+b*b
    return math.exp(-out/4)

def main():
    pre=json.loads((HERE/'PRE_COMPARISON_SEAL.json').read_text())
    for x in pre['sources']+pre['artifacts']:assert ident(Path(x['path']))==x
    author=json.loads((ROOT/'dimer_finite_qubit_curl_checks/RESULTS.json').read_text())
    for n,h in author['sources_sha256'].items():assert ident(ROOT/n)['sha256']==h
    for name,group in author['groups'].items():
        assert json.loads((ROOT/'dimer_finite_qubit_curl_checks'/f'{name}.json').read_text())==group
    for r in author['groups']['physical_occupation']:
        k=r['K'];assert r['symmetric_dimension']==math.comb(k+3,3)
        assert r['physical_dimension']==4**k and r['exact_nonzero_lowering_entries']==3*math.comb(k+2,3)
    for r in author['groups']['discrete_curl']:
        v=r['L']**3;z=(1 if r['L']%2 else 8)
        assert r['zero_momenta']==z and r['curl_nullity']==v+2*z
        assert r['derivative_EB_bracket_rank']==4*(v-z)
    weighted=[];w2=np.array([0.,.75,.75])
    bs,H=quadratic(5,None,w2);core=[i for i,n in enumerate(bs) if sum(n)<=3]
    for r in author['groups']['finite_block_limit']['weighted_core_differences']:
        _,HK=quadratic(5,r['K'],w2)
        A=(HK-H)[:,core]/np.array([(sum(bs[i])+1)**2 for i in core])[None,:]
        value=float(np.linalg.norm(A,2));err=abs(value-r['weighted_difference_norm'])
        assert err<3e-14
        weighted.append(dict(K=r['K'],independent_norm=value,difference=err))
    zs=[np.array([.3,.2,-.1,.4,-.2,.3]),np.array([0,0,.7,0,.6,0])]
    finite=[];targeterrs=[]
    bs,H=quadratic(4,4,w2);ev,U=eigh(H);vac=np.zeros(len(bs));vac[bs.index((0,0,0))]=1
    for r in author['groups']['finite_block_limit']['finite_block_Weyl_dynamics']:
        z=zs[r['observable']];g=target(r['t'],z);targeterrs.append(abs(g-r['gaussian_target']))
        assert targeterrs[-1]<3e-15
        assert r['dimension']==math.comb(r['K']+3,3)
        assert abs(abs(complex(r['real'],r['imag'])-g)-r['absolute_error'])<3e-15
        if r['K']!=4:continue
        evolved=U@(np.exp(-1j*r['t']*ev)*(U.T@vac))
        ew,V=eigh(linear(bs,4,z));we=V@(np.exp(1j*ew)*(V.conj().T@evolved))
        value=np.vdot(evolved,we);err=abs(value-complex(r['real'],r['imag']))
        assert err<3e-13
        finite.append(dict(time=r['t'],observable=r['observable'],independent_real=float(value.real),
                           independent_imag=float(value.imag),difference=float(err)))
    assert (ROOT/'DIMER_FINITE_QUBIT_CURL_RUN.stderr').read_bytes()==b''
    pdf=Path('/Users/jonreilly/Documents/Codex/physics-sync-2026-09-21-second/literature/Simon_analytic_vectors_R4.pdf')
    receipt=json.loads((ROOT/'DIMER_FINITE_QUBIT_ANALYTIC_VECTOR_SOURCE.json').read_text())
    assert ident(pdf)['sha256']==receipt['source']['external_pdf_sha256']
    names=['DIMER_FINITE_QUBIT_POSITIVE_CURL_LIMIT.md','dimer_finite_qubit_curl_check.py',
           'DIMER_FINITE_QUBIT_ANALYTIC_VECTOR_SOURCE.json','DIMER_FINITE_QUBIT_CURL_RUN.log',
           'DIMER_FINITE_QUBIT_CURL_RUN.stderr']
    sources=[ident(ROOT/n) for n in names]+[ident(f) for f in sorted((ROOT/'dimer_finite_qubit_curl_checks').glob('*.json'))]+[ident(pdf)]
    result=dict(created_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
                preseal_authenticated=True,source_bindings=sources,
                complete_author_code_and_results_read=True,author_code_executed=False,
                author_three_group_files_match_summary=True,
                direct_quadratic_weighted_norm_comparisons=weighted,
                dense_spectral_K4_Weyl_comparisons=finite,
                all_24_Gaussian_targets_and_errors_checked=True,
                max_Gaussian_target_discrepancy=max(targeterrs),
                scope='Direct monomial coefficients and dense spectral decomposition were independently assembled. K>4 finite Weyl rows were authenticated and their target/error arithmetic checked, not dynamically recomputed.')
    (HERE/'COMPARISON_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))

if __name__=='__main__':main()
