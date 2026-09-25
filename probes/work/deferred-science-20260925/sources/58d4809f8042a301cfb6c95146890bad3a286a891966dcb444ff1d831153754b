from pathlib import Path
import hashlib,json,time
import numpy as np
import mpmath as mp

def control(L):
    n=np.fft.fftfreq(L)*L
    s=4*np.sin(np.pi*n/L)**2
    D=s[:,None,None]+s[None,:,None]+s[None,None,:]
    xy=s[:,None,None]+s[None,:,None]+np.zeros((1,1,L))
    root=np.sqrt(D);weight=np.zeros_like(D)
    np.divide(xy,root,out=weight,where=D>0)
    V=L**3;v=float(weight.sum()/(2*V));normalization=float(xy.sum()/V)
    assert abs(normalization-4)<1e-12
    assert abs(v-float(root.sum()/(3*V)))<1e-12
    assert v>=1/np.sqrt(3)-1e-12
    rows=[]
    for eps in [.1,.2,.4,.7,1.,1.5,2.]:
        mask=(D>0)&(D<=eps**2);N=int(mask.sum());low=float(weight[mask].sum()/(2*V))
        bound=27*eps**4/128;cube=(2*int(np.floor(L*eps/4))+1)**3-1
        assert N<=cube
        assert low<=bound+1e-14
        assert low/v<=27*np.sqrt(3)*eps**4/128+1e-14
        if N:assert L*eps>=4-1e-12
        else:assert low==0
        rows.append({'epsilon':eps,'nonzero_momenta_in_band':N,'cube_count_upper':cube,'v_low':low,'v_low_upper':bound,'max_eta':low/v,'eta_upper':27*np.sqrt(3)*eps**4/128,'normalized_band_packet_available':bool(N)})
    return {'L':L,'vertices':V,'plaquette_norm_squared':normalization,'v_p':v,'v_p_lower':1/np.sqrt(3),'rows':rows}

start=time.perf_counter();mp.mp.dps=85
EQ=mp.mpf('6.9e20');C=27*mp.sqrt(3)/64
unit=[]
for E in ['1','2','3']:
    eps=6*mp.mpf(E)/EQ
    unit.append({'supplied_E_lab_eV':E,'epsilon_strict_upper':str(eps),'limiting_relative_probability_excess_strict_upper':str(C*eps**4),'status':'Conditional reference-band bound, not a measured detector rate or finite-g error certificate.'})
result={'scope':'Finite Fourier consistency checks and conditional SI arithmetic; no full dynamics or interval certificate.','lattice_rows':[control(L)for L in (6,8,16,32,64,96)],'SI_rows':unit,'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'elapsed_seconds':time.perf_counter()-start}
Path(__file__).with_name('OPTICAL_BAND_RESULTS.json').write_text(json.dumps(result,indent=2,allow_nan=False)+'\n');print(json.dumps(result,indent=2,allow_nan=False))
