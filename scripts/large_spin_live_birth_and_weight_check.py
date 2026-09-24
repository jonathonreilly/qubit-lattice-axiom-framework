#!/usr/bin/env python3
"""Exact live-birth algebra and weighted shift estimates at larger link spin."""

AUDIT_TIMEOUT_SEC = 3600
AUDIT_INPUT_PATHS = ('scripts/large_spin_live_birth_and_weight_check.py',)
from itertools import product
from pathlib import Path
import hashlib
import json
import sympy as sp

OUT=Path(__file__).resolve().parent


def physical_ring(spin):
    casimir=sp.Integer(spin*(spin+1));ref=(1,0,1,0);basis=[]
    for matter in product((0,1,-1),repeat=4):
        if sum(matter)!=2:continue
        for first in range(-spin,spin+1):
            field=[first]
            for x in (1,2,3):field.append(field[-1]+matter[x]-ref[x])
            if field[0]-field[-1]+ref[0]-matter[0]:continue
            if any(abs(x)>spin for x in field):continue
            basis.append((matter,tuple(field)))
    index={state:i for i,state in enumerate(basis)};dim=len(basis)
    hop=sp.zeros(dim);births={(e,q):sp.zeros(dim) for e in range(4) for q in (-1,1)}
    for i,(matter,field) in enumerate(basis):
        for e in range(4):
            x,y=e,(e+1)%4
            for u,v,direction in ((x,y,1),(y,x,-1)):
                if matter[u]==0 or matter[v]!=0:continue
                shift=-direction*matter[u];m=field[e]
                if abs(m+shift)>spin:continue
                amp=sp.sqrt(1-(m*m+shift*m)/casimir)
                mm=list(matter);ff=list(field);mm[v]=mm[u];mm[u]=0;ff[e]+=shift
                hop[index[(tuple(mm),tuple(ff))],i]-=amp
            if matter[x]==matter[y]==0:
                for q in (-1,1):
                    m=field[e]
                    if abs(m+q)>spin:continue
                    amp=sp.sqrt(1-(m*m+q*m)/casimir)
                    mm=list(matter);ff=list(field);mm[x]=q;mm[y]=-q;ff[e]+=q
                    births[e,q][index[(tuple(mm),tuple(ff))],i]=amp
    assert hop==hop.T
    record=sp.diag(*[sum(x!=0 for x in m) for m,f in basis])
    nb=sp.diag(*[sum(m[x]!=0 for x in (1,3)) for m,f in basis])
    star=sp.diag(*[sum((f[x]-f[(x-1)%4])**2 for x in range(4))/sp.Integer(2) for m,f in basis])
    onsite=sp.diag(*[sum(m[x]==-1 for x in (0,2))+sum(m[x]==1 for x in (1,3)) for m,f in basis])
    assert star==onsite and record*hop==hop*record
    zero=sp.zeros(dim)
    low=sp.diag(*[int(nb[i,i]==0) for i in range(dim)])
    max_loss=0
    for e in range(4):
        x,y=e,(e+1)%4;plus,minus=births[e,1],births[e,-1]
        assert plus.T*minus==zero and minus.T*plus==zero
        want=sp.diag(*[2*int(m[x]==m[y]==0)*(1-sp.Rational(f[e]**2,casimir)) for m,f in basis])
        for operators in ([plus,minus],[plus+minus]):
            loss=sum((j.T*j for j in operators),zero).applyfunc(sp.simplify)
            assert loss==want
            for j in operators:
                assert j*low==zero and record*j-j*record==2*j
            max_loss=max(max_loss,max(loss.diagonal()))
    assert max_loss<=2
    for penalty in (nb,onsite):
        assert all(not hop[i,j] or abs(penalty[i,i]-penalty[j,j])==1 for i in range(dim) for j in range(dim))
    return {'spin':spin,'complete_physical_dimension':dim,'code_dimension':int(sp.trace(low)),
            'star_equals_onsite_charge_projectors':True,'hopping_changes_either_penalty_by_one':True,
            'record_count_and_birth_annihilation_exact':True,
            'resolved_and_coherent_loss_exact':'2 Pvac (1-E^2/C)',
            'largest_local_loss_eigenvalue_exact':str(max_loss)}


def weighted_shift_controls():
    # Exact rational squared inequalities avoid numerical square-root screens.
    checked=0;largest_ratio=sp.Rational(0)
    for spin in range(1,41):
        c=sp.Integer(spin*(spin+1))
        for m in range(-2*spin-5,2*spin+6):
            for step in (-1,1):
                a2=1-sp.Rational(m*m+step*m,c) if abs(m)<=spin and abs(m+step)<=spin else sp.Integer(0)
                assert 0<=a2<=1
                # 1-sqrt(a2) <= 1-a2 <= 2(1+m^2)/C inside;
                # outside the compressed interval the direct right side >=1.
                bound=sp.Rational(2*(1+m*m),c)
                assert 1-a2<=bound
                checked+=1
            w=sp.Integer((1+m*m)**2);wp=sp.Integer((1+(m+1)**2)**2)
            assert wp<=9*w and w<=9*wp
            assert (wp-w)**2<=36*wp*w
            largest_ratio=max(largest_ratio,wp/w,w/wp)
    x=sp.symbols('x',real=True)
    difference=sp.expand(3*(1+x*x)-(1+(x+1)**2))
    assert sp.expand(difference-(2*(x-sp.Rational(1,2))**2+sp.Rational(1,2)))==0
    return {'exact_shift_inequality_rows':checked,'sampled_spins':40,
            'largest_exact_adjacent_w_ratio_in_screen':str(largest_ratio),
            'all_real_quadratic_certificate':'3(1+x^2)-(1+(x+1)^2)=2(x-1/2)^2+1/2',
            'proof_scope':'The displayed polynomial and cutoff case proof give the universal bounds; the finite screen is a control.'}


def main():
    out={'status':'PASS','source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
         'complete_live_sectors':[physical_ring(s) for s in (1,2,3)],
         'weighted_shift_and_moment_controls':weighted_shift_controls(),
         'limits':'Exact finite-sector and scalar inequalities; does not validate a many-volume normal form or phase.'}
    text=json.dumps(out,indent=2)+'\n';(OUT/'LARGE_SPIN_LIVE_BIRTH_AND_WEIGHT_RESULTS.json').write_text(text);print(text,end='')


if __name__=='__main__':main()
