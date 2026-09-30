#!/usr/bin/env python3
"""Finite exact controls for two supplied native record-medium constructions.

Analytic proofs supply all-volume/finite-time claims. This primary reuses the
root motif literal occupation builder with disclosed provenance; it is not an
independent implementation. It performs no external scientific file reads.
The cache envelope binds the declared source-note and actual parent inputs.
"""
AUDIT_TIMEOUT_SEC = 30
AUDIT_INPUT_PATHS = (
    "docs/NATIVE_PERMANENT_MARKERS_COHERENT_MEDIA_BOUNDED_THEOREM_NOTE_2026-09-30.md",
    "docs/NATIVE_QUBIT_PAIR_DENSITY_ONSET_BOUNDED_THEOREM_NOTE_2026-09-30.md",
)
from fractions import Fraction as F
from collections import defaultdict
from itertools import product
import argparse
import json

axes=((1,0,0),(0,1,0),(0,0,1))
def add(a,b):return tuple(x+y for x,y in zip(a,b))
def scale(a,s):return tuple(s*x for x in a)
def dist(a,b):return max(abs(x-y) for x,y in zip(a,b))
D=set()
for e in axes:
 for s in (-1,1):D.add(scale(e,2*s))
for i in range(3):
 for j in range(i+1,3):
  for s,t in product((-1,1),repeat=2):D.add(add(scale(axes[i],s),scale(axes[j],t)))
def families(c):
 ep=[frozenset((add(c,e),add(c,scale(e,-1)))) for e in axes]
 out=[(ep,[[F(int(i==j))-F(1,3) for j in range(3)] for i in range(3)],2)]
 for i in range(3):
  for j in range(i+1,3):
   st=list(product((-1,1),repeat=2)); ps=[frozenset((add(c,scale(axes[i],s)),add(c,scale(axes[j],t)))) for s,t in st]
   out.append((ps,[[F(s*t*u*v,4) for u,v in st] for s,t in st],1))
 return out
def action(word,mu,tau):
 out=defaultdict(F);n=len(word)
 out[word]+=2*mu*n
 for x in word:
  m=sum(add(x,d) in word for d in D);out[word]+=mu*(m*(m-1)//2)
 centers={add(x,scale(e,s)) for x in word for e in axes for s in (-1,1)}
 for c in centers:
  cf=families(c)
  for group,(ann,G,attr) in enumerate(cf):
   for i,p in enumerate(ann):
    if not p<=word:continue
    rem=word-p
    choices=[(c,6*tau-attr*mu)]+[(add(c,scale(e,s)),-tau) for e in axes for s in (-1,1)]
    for y,coef in choices:
     if not coef:continue
     create=families(y)[group][0]
     for j,q in enumerate(create):
      if q & rem:continue
      out[frozenset(rem|q)]+=coef*G[j][i]
 return {w:v for w,v in out.items() if v}
def markers(word):return frozenset(x for x in word if all(x==y or dist(x,y)>2 for y in word))
def pinched(word,mu,tau):return {w:a for w,a in action(word,mu,tau).items() if markers(w)==markers(word)}
def linear_action(psi,mu,tau,changed=False):
 out=defaultdict(F)
 for w,a in psi.items():
  for z,b in (pinched if changed else action)(w,mu,tau).items():out[z]+=a*b
 return {w:a for w,a in out.items() if a}
def birth(word,x):
 if any(dist(x,y)<=2 for y in word):return None
 return frozenset(word|{x})

def transport_control():
    I=frozenset(((0,0,0),(2,0,0),(4,0,0)))
    O=frozenset(((0,0,0),(3,0,0),(5,0,0)))
    assert action(I,1,0).get(O,F(0))==0
    assert action(I,0,1)[O]==F(-2,3)
    assert O not in pinched(I,0,1)
    assert markers(I)==frozenset() and markers(O)==frozenset(((0,0,0),))
    for mu in (F(1),F(1,3),F(2,5)):
        assert action(I,mu,0)[I]==F(4,3)*mu
    return dict(four_flip='-2tau/3',pinched=0,rational_mu_cases=3,
                original_terms=len(action(I,0,1)),pinched_terms=len(pinched(I,0,1)))

def packet_control():
    psi=defaultdict(int)
    for x in product((-1,0,1),repeat=3):
        weight=1
        for z in x:weight*=2 if z==0 else 1
        for i,sgn in ((0,1),(1,-1)):
            q=frozenset((add(x,axes[i]),add(x,scale(axes[i],-1))))
            psi[q]+=sgn*weight
    psi={w:a for w,a in psi.items() if a};norm=sum(a*a for a in psi.values())
    assert norm==432 and len(psi)==54
    assert linear_action(psi,F(2,5),0)=={}
    tauvec=linear_action(psi,0,1)
    energy=sum(F(a)*tauvec.get(w,0) for w,a in psi.items())
    assert energy==864 and energy/norm==2
    assert tauvec==linear_action(psi,0,1,changed=True)
    assert all(not markers(w) for w in psi)
    assert len(tauvec)==146
    return dict(states=len(psi),norm=norm,mu_action_zero=True,
                kinetic_numerator=str(energy),energy=str(energy/norm),outputs=len(tauvec))

def persistence_control():
    sites=((0,0,0),(1,0,0),(2,0,0),(3,0,0),(5,0,0),(0,2,0),(0,3,0))
    x=(0,0,0); ys=((0,0,0),(1,0,0),(2,0,0),(3,0,0),(3,3,0))
    count=0
    for bits in product((0,1),repeat=len(sites)):
        word=frozenset(s for s,b in zip(sites,bits) if b)
        output=birth(word,x)
        allowed=output is not None
        for y in ys:
            py=int(y in markers(word))
            pout=int(y in markers(output)) if allowed else 0
            # Literal diagonal adjoint gain minus full anticommutator loss.
            derivative=(pout-py) if allowed else 0
            assert derivative==(int(allowed) if y==x else 0)
            if py and allowed:assert pout
            count+=1
        if allowed:
            assert len(output)-len(markers(output))==len(word)-len(markers(word))
    old=frozenset(((0,0,0),))
    assert birth(old,(2,2,2)) is None
    output=birth(old,(3,0,0));assert output is not None and markers(output)==output
    return dict(gain_loss_cases=count,number_minus_motifs_preserved=True,
                overlapping_empty_collars_distance=3)

def diagonal_control():
    sites=((0,0,0),(2,0,0),(-2,0,0),(0,2,0),(0,-2,0),(0,0,2),(0,0,-2),(1,1,0))
    cases=0
    for bits in product((0,1),repeat=len(sites)):
        word=frozenset(s for s,b in zip(sites,bits) if b)
        dd=sum(F((sum(add(x,d) in word for d in D)-1)*(sum(add(x,d) in word for d in D)-2),2) for x in word)
        axial=plane=0
        for x in word:
            for y in word:
                if x>=y:continue
                delta=tuple(a-b for a,b in zip(y,x))
                if delta in D:
                    if sum(t!=0 for t in delta)==1:axial+=1
                    else:plane+=1
        expected=dd+F(14,3)*axial+F(9,2)*plane
        assert action(word,1,1).get(word,0)==expected
        assert dd>=len(markers(word))
        assert expected>=F(1,3)*len(word)
        cases+=1
    degree_values=[F((m-1)*(m-2),2)+F(m,3) for m in range(19)]
    assert min(degree_values)==F(1,3)
    assert max((m-1)*(m-2)//2 for m in range(19))==136
    return dict(configurations=cases,degree_values=list(map(str,degree_values)),
                axial_diagonal='14/3',plane_diagonal='9/2')

def vacuum_control():
    # A literal plane-difference row on four physical endpoints (+e1,+e2,-e1,-e2).
    pairs=((frozenset((0,1)),F(1)),(frozenset((2,3)),F(-1)))
    active=frozenset((0,2,3));r=1
    def square(word,rows):
        out=defaultdict(F)
        for pair,a in rows:
            if not pair<=word:continue
            rem=word-pair
            for created,b in rows:
                if rem & created:continue
                out[frozenset(rem|created)]+=a*b
        return {w:a for w,a in out.items() if a}
    retained=[(pair,a) for pair,a in pairs if pair<=active]
    cases=0
    for bits in product((0,1),repeat=3):
        word=frozenset(s for s,b in zip(sorted(active),bits) if b)
        compressed={w:a for w,a in square(word,pairs).items() if w<=active}
        assert compressed==square(word,retained)
        assert compressed==({word:F(1)} if frozenset((2,3))<=word else {})
        for recorded in (False,True):
            full=word|({r} if recorded else set())
            # Identity amplification at R plus its paid onsite mu n_r.
            output={frozenset(w|({r} if recorded else set())):a for w,a in compressed.items()}
            assert all((r in w)==recorded for w in output)
            assert len(full)-len(word)==int(recorded)
        cases+=1
    assert ((0-1)*(0-2)//2,(1-1)*(1-2)//2)==(1,0)
    return dict(compressed_basis_cases=cases,record_factor_cases=2*cases,
                nonmonotone_degree_zero_one=[1,0])

def geometry_control():
    support={(0,0,0)}|set(axes)|{scale(e,-1) for e in axes}|D
    assert len(support)==25
    rows=[]
    for ell in (5,6,8):
        p=ell+4;active=set(product(range(ell),repeat=3));interior=0
        for center in product(range(p),repeat=3):
            translated={tuple((center[i]+d[i])%p for i in range(3)) for d in support}
            interior+=translated<=active
        assert interior==(ell-4)**3
        remaining=p**3-interior;markers_count=p**3-ell**3
        assert remaining==24*ell**2+128 and remaining<=30*ell**2
        assert markers_count<=25*ell**2
        rows.append(dict(ell=ell,p=p,interior=interior,boundary_centers=remaining,
                         marker_sites=markers_count))
    return dict(actual_support_sites=len(support),cell_counts=rows)

def resource_control():
    mu=F(2,3);tau=F(3,5);nu=F(1,10)
    A=24**4*25*28*31*34*F(1,24)*(182*mu+240*tau)
    B=24**4*1*4*7*10*F(1,24)
    assert A==10199347200*(182*mu+240*tau) and B==3870720
    g=nu**2/(A+nu*B);u2=nu/(A+nu*B)
    assert A*u2*u2-nu*(2*u2-B*u2*u2)==-g
    h=160*mu+240*tau;C=30*h+25*(mu-nu)
    lower=2*C/g;ell=max(5,-(-lower.numerator//lower.denominator));p=ell+4
    assert -g*ell**3+C*ell**2<=-g*ell**3/2
    rR=1-F(ell**3,p**3)
    assert F(2)*g/(C+5*g)<=rR<=6*g/C
    assert F((p**3-ell**3),ell**2)<=25
    # Separate motif time-bound arithmetic, independent of any simulation.
    volume=18**3;rho=F(2,volume);v=125;gamma=F(3,7)
    eta=nu/volume;J=182*mu+240*tau;energy_rate=9826*(J+nu)
    T=min(F(1,4*v)/gamma,eta/(2*gamma*energy_rate))
    assert rho<=F(1,2*v)
    assert 1-v*(rho+gamma*T)>=F(1,4)
    assert -eta+gamma*energy_rate*T<=-eta/2
    return dict(A=str(A),B=str(B),corridor_ell=ell,
                paid_saturation=True,motif_time_positive=T>0,
                interval_scope='fixed parameters; not uniform as nu tends to zero')

CONTROLS={'transport':transport_control,'packet':packet_control,
          'persistence':persistence_control,'diagonal':diagonal_control,
          'vacuum':vacuum_control,'geometry':geometry_control,'resources':resource_control}
def main():
    parser=argparse.ArgumentParser();parser.add_argument('--group',choices=tuple(CONTROLS))
    args=parser.parse_args();chosen=[args.group] if args.group else list(CONTROLS)
    results={name:CONTROLS[name]() for name in chosen}
    print(json.dumps({'controls':results,'scope':'Finite exact controls; analytic proofs supply all-volume and dynamical claims. No phase or physical-law inference.','scientific_file_reads':[],
                      'declared_cache_inputs':list(AUDIT_INPUT_PATHS)},indent=2))
    print('TOTAL: PASS='+str(len(results))+' FAIL=0')
if __name__=='__main__':main()
