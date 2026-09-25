"""Author certificates for loop fillings and prepared excitation mean energy.

Reads the exact author Laurent output. No full rotor simulation or independent
check is claimed. Fourier sums evaluate the uncut harmonic compression and the
fixed-volume g->0 coefficient, retaining the original charged preparation.
"""
from collections import defaultdict,Counter
from fractions import Fraction
from itertools import combinations,product
from pathlib import Path
import json,time,hashlib
import numpy as np


def key(d):return tuple(sorted((e,n) for e,n in d.items() if n))
def combine(a,b):
    d=defaultdict(int)
    for e,n in a+b:d[e]+=n
    return key(d)
def neg(a):return tuple((e,-n) for e,n in a)

def unwrap(v,L):return tuple(x if x<L//2 else x-L for x in v)
def positive_word(row,L):
    d=defaultdict(int)
    for xa,xb,n in row:
        a,b=unwrap(xa,L),unwrap(xb,L);step=tuple(y-x for x,y in zip(a,b))
        assert sum(abs(x) for x in step)==1
        mu=next(i for i in range(3) if step[i]);s=step[mu]
        d[(a if s==1 else b,mu)]+=s*n
    return key(d)

def face(origin,mu,nu):
    x=list(origin);y=x.copy();y[mu]+=1;z=x.copy();z[nu]+=1
    return key({(tuple(x),mu):1,(tuple(y),nu):1,(tuple(z),mu):-1,(tuple(x),nu):-1})

def fillings(rows):
    faces={}
    for x in product(range(-3,5),repeat=3):
        for mu,nu in combinations(range(3),2):
            w=face(x,mu,nu)
            faces[w]=(x,mu,nu,1);faces[neg(w)]=(x,mu,nu,-1)
    out=[]
    for row in rows:
        w=row['word']
        if not w:continue
        if w in faces:fill=[faces[w]]
        else:
            fill=None
            for f,description in faces.items():
                other=combine(w,neg(f))
                if other in faces:fill=[description,faces[other]];break
            assert fill is not None
        check=()
        for x,mu,nu,s in fill:
            f=face(x,mu,nu);check=combine(check,f if s==1 else neg(f))
        assert check==w
        out.append({'word':w,'coefficient':row['coefficient'],'filling':fill,'area_l1':len(fill)})
    return out

def word_fourier(w,k):
    out=np.zeros((len(k),3),dtype=complex)
    for (x,mu),n in w:out[:,mu]+=n*np.exp(1j*(k@np.array(x)))
    return out

def spectral(side,rows,epsilons):
    axis=2*np.pi*np.arange(side)/side
    k=np.array(list(product(axis,repeat=3)));D=4*np.sin(k/2)**2;omega=np.sqrt(D.sum(axis=1));keep=omega>0
    k=k[keep];omega=omega[keep];V=side**3
    P=word_fourier(face((0,0,0),0,1),k);p2=(abs(P)**2).sum(axis=1)
    vp=float(np.sum(p2/omega)/(2*V))
    prepared=[]
    for row in rows:
        w=word_fourier(row['word'],k)
        # A row circulation annihilates the discrete gradient.
        assert np.max(abs(np.sum(w*(np.exp(1j*k)-1),axis=1)))<2e-13
        cross=np.sum(w*np.conj(P),axis=1)/(2*V*omega)
        prepared.append((row['coefficient'],float(np.sum(abs(w)**2/omega[:,None])/(2*V)),cross,row['area_l1']))
    blocked=[]
    for b,weight in [((0,-1,0),1.),((0,0,1),1.),((0,0,-1),1.),((1,0,0),.5),((0,1,0),.5)]:
        for mu0 in range(3):
            # The positive-coordinate edges incident on b have origins b and b-e_mu.
            for offset in (0,-1):
                x=list(b);x[mu0]+=offset;blocked.append((tuple(x),mu0,weight))
    assert sum(w for _,_,w in blocked)==24
    output=[]
    for eps in epsilons:
        band=omega<=eps;vlow=float(np.sum(p2[band]/omega[band])/(2*V))
        if vlow==0:output.append({'side':side,'epsilon':eps,'empty':True});continue
        mu=float(np.sum(p2[band])/(2*V*vlow));loss=0.;grows=[]
        electric_loss=0.
        for x,mu0,weight in blocked:
            xi=np.sum(P[band,mu0]*np.exp(-1j*(k[band]@np.array(x))))/(2*V*np.sqrt(vlow))
            assert abs(xi.imag)<1e-12
            electric_loss+=weight*float(abs(xi)**2)
        if eps<=2:assert electric_loss<=mu*24*(27/128)*eps**3+1e-12
        terms=[]
        for a,vw,cross,area in prepared:
            chi=np.sum(cross[band])/np.sqrt(vlow)
            assert abs(chi.imag)<1e-12
            weight=float(abs(chi)**2);loss+=a*weight/4
            if eps<=2:assert weight<=mu*(27/128)*eps**3*area**2+1e-12
            terms.append((a,vw,weight))
        for g in (.2,.1,.05,.025):
            base=mu*(1+np.exp(-g*g*vp/2))/2
            energy=base-electric_loss-sum(a*np.exp(-g*g*vw/2)*weight/4 for a,vw,weight in terms)
            grows.append({'g':g,'uncut_harmonic_full_mean_increment_times_tau':float(energy)})
        bound=float(Fraction(3591,128)*eps**3)
        if eps<=2:assert loss+electric_loss<=mu*bound+1e-11
        output.append({'side':side,'epsilon':eps,'empty':False,'band_modes_k':int(band.sum()),
          'vp':vp,'vlow':vlow,'reference_mean_energy_times_tau':mu,
          'limiting_added_full_mean_energy_times_tau':mu-loss-electric_loss,'magnetic_defect_energy_loss_times_tau':loss,
          'electric_occupancy_energy_loss_times_tau':electric_loss,
          'relative_loss':(loss+electric_loss)/mu,'relative_loss_bound':bound if eps<=2 else None,'finite_g_harmonic_rows':grows})
    return output

if __name__=='__main__':
    started=time.perf_counter();p=Path(__file__).with_name('ENERGY_POLYNOMIAL_RESULTS.json');source=json.loads(p.read_text())
    converted=[]
    for row in source['rows']:
        converted.append([{'word':positive_word(x['word'],row['side']),'coefficient':x['coefficient']} for x in row['words']])
    assert {r['word']:r['coefficient'] for r in converted[0]}=={r['word']:r['coefficient'] for r in converted[1]}
    fills=fillings(converted[1]);weighted=sum(r['coefficient']*r['area_l1']**2 for r in fills)
    assert weighted==436
    result={'scope':__doc__,'source_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),
      'exact_summary':{'constant':4722,'nonconstant_words':len(fills),'coefficient_sum':sum(r['coefficient'] for r in fills),
       'area_squared_weighted_sum':weighted,'magnetic_relative_bound_coefficient':str(Fraction(27*weighted,512)),
       'electric_occupied_edge_weight':24,'total_relative_bound_coefficient':str(Fraction(27*weighted,512)+Fraction(24*27,128)),
       'histogram':[{ 'coefficient':c,'area':a,'count':n} for (c,a),n in sorted(Counter((r['coefficient'],r['area_l1']) for r in fills).items())]},
      'fillings':fills,'rows':sum([spectral(L,fills,(.2,.4,.7,1.,2.,3.5)) for L in (16,32)],[]),
      'elapsed_seconds':time.perf_counter()-started}
    print(json.dumps(result,indent=2))
