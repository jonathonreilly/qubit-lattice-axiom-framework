#!/usr/bin/env python3
"""Independent torus assembly; production code used only for final comparison.

All polynomial variables are explicit site-labelled variables on Z/11Z.
Poisson brackets differentiate full finite sums at each canonical coordinate;
there is no relative-slot alignment or translation quotient in that operation.
"""
import ast
from collections import defaultdict
from fractions import Fraction as Q
import hashlib
import importlib.util
from itertools import combinations_with_replacement as cwr, product
import json
import os
from pathlib import Path
import sys
import time

for _name in ('OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','OMP_NUM_THREADS'):
    os.environ[_name]='1'
sys.dont_write_bytecode = True
HERE=Path(__file__).resolve().parent
PACK=HERE.parent
RUNTIME=Path('/Users/jonBridger/.codex/campaigns/toe-gravity-law-24h-20260929')
L=11
START_HASH='427e83efa1d55c836465c61c672e0cf4c0814420a59fc64430e2b80e6aae9528'

def budget():
    assert time.time()<json.loads((RUNTIME/'DEADLINE.json').read_text())['deadline_epoch']
    assert not (RUNTIME/'STOP_REQUESTED.json').exists()

def var(k,c=0,x=0): return k,c,x
def key(m): return tuple(sorted(m))
def clean(p): return {m:c for m,c in p.items() if c}
def linear(terms):
    p=defaultdict(Q)
    for c,m in terms: p[key(m)]+=Q(c)
    return clean(p)
def add(*ps):
    return linear((a*c,m) for a,p in ps for m,c in p.items())
def times(p,q):
    return linear((a*b,m+n) for m,a in p.items() for n,b in q.items())
def functional(terms):
    return linear((c,tuple((k,i,(x+s)%L) for k,i,x in m))
                  for c,m in terms for s in range(L))
def one(m,c=1): return functional([(c,m)])
def gradient(p):
    out=defaultdict(lambda:defaultdict(Q))
    for m,c in p.items():
        for j,v in enumerate(m):
            if v[0] in ('h','p'):
                out[v][m[:j]+m[j+1:]]+=c
    return {v:clean(q) for v,q in out.items()}
def pb(p,q):
    a,b=gradient(p),gradient(q)
    pieces=[]
    for i,x in product(range(3),range(L)):
        for k,l,sgn in [('h','p',1),('p','h',-1)]:
            aa=a.get((k,i,x),{}); bb=b.get((l,i,x),{})
            if aa and bb: pieces.append((sgn,times(aa,bb)))
    return add(*pieces)
def change(p,a,b):
    return linear((c,tuple((b if k==a else k,i,x) for k,i,x in m))
                  for m,c in p.items())
def recenter(m,anchor):
    anchors=[x for k,i,x in m if k==anchor]
    assert len(anchors)==1
    a=anchors[0]
    def rep(x): return (x-a+L//2)%L-L//2
    return key((k,i,rep(x)) for k,i,x in m)
def reduce_torus(p,anchor):
    # Each complete monomial contains exactly one labelled anchor variable;
    # every orbit therefore has L elements and no translational stabilizer.
    out=defaultdict(Q)
    for m,c in p.items(): out[recenter(m,anchor)]+=c/Q(L)
    return clean(out)
def canonical_uniform(m):
    lo=min(x for k,i,x in m)
    return key((k,i,x-lo) for k,i,x in m)

def c1(smear):
    return functional([(4*w,(var(smear),var('h',i,x)))
                       for i in (1,2) for x,w in [(-1,1),(0,-2),(1,1)]])
def t2(smear):
    terms=[]
    for i,j in cwr(range(3),2):
        terms.append((Q(1,8) if i==j else Q(-1,4),
                      (var(smear),var('p',i),var('p',j))))
    return functional(terms)
def g1(smear):
    return functional([(2,(var(smear),var('p',0))),
                       (-2,(var(smear),var('p',0,1)))])
def f0_compose(h,p):
    return functional([(1,(var('N'),var('M',0,1),h,p)),
                       (-1,(var('M'),var('N',0,1),h,p))])

def build():
    names=[]; rows=defaultdict(dict); rhs={}
    def put(fam,m,j,c):
        if c: rows[fam,m][j]=rows[fam,m].get(j,Q(0))+c
    def addpoly(fam,p,j,sgn=1):
        anchor='N' if fam in ('CC2','GC1') else 'X'
        for m,c in reduce_torus(p,anchor).items(): put(fam,m,j,sgn*c)
    def new(n): names.append(n); return len(names)-1
    cn,cm=c1('N'),c1('M'); tn,tm=t2('N'),t2('M')
    gx,gy=g1('X'),g1('Y')
    hs=[var('h',i,x) for i in range(3) for x in (-1,0,1)]
    ps=[var('p',i,x) for i in range(3) for x in (-1,0,1)]
    eh=[var('h',i,x) for i in range(3) for x in (0,1)]
    ep=[var('p',i,x) for i in range(3) for x in (0,1)]
    for mon in cwr(hs,2):
        j=new('V2:'+repr(mon)); f=one((var('N'),)+mon)
        addpoly('CC2',add((1,pb(f,tm)),(1,pb(tn,change(f,'N','M')))),j)
        addpoly('GC1',pb(gx,f),j)
        put('uniform_V2',canonical_uniform(mon),j,Q(1))
    # Expand -2 (B_1-B_0)(C_1-C_0), quotient ONLY after N=1.
    for x,y in product((0,1),repeat=2):
        mon=canonical_uniform((var('h',1,x),var('h',2,y)))
        rhs['uniform_V2',mon]=rhs.get(('uniform_V2',mon),Q(0))-2*(2*x-1)*(2*y-1)
    for h in hs:
        for pair in cwr(ps,2):
            mon=(h,)+pair; j=new('T3:'+repr(mon)); f=one((var('N'),)+mon)
            addpoly('CC2',add((1,pb(cn,change(f,'N','M'))),(1,pb(f,cm))),j)
            put('continuum_T3',key((k,i,0) for k,i,x in mon),j,Q(1))
            if j%100==0: budget()
    # Different path for cubic normalization: differentiate the actual smooth
    # diagonal Hamiltonian, including its determinant, then read coefficients.
    import sympy as s
    e=s.symbols('e'); h=s.symbols('A B C'); p=s.symbols('P Q R')
    g=[1+e*hi for hi in h]
    numerator=sum(g[i]**2*p[i]**2 for i in range(3))-sum(g[i]*p[i] for i in range(3))**2/2
    exact=numerator/(4*s.sqrt(s.prod(g)))
    cubic=s.Poly(s.diff(exact,e).subs(e,0).expand(),*(h+p))
    for powers,c in cubic.terms():
        mon=[]
        for i,n in enumerate(powers): mon.extend([var('h' if i<3 else 'p',i%3)]*n)
        rhs['continuum_T3',key(mon)]=Q(str(c))
    print('Independent continuum T3:',cubic.as_expr(),flush=True)
    for h,p in product(eh,ep):
        j=new('G2:'+repr((h,p))); f=one((var('X'),h,p))
        addpoly('CC2',f0_compose(h,p),j,-1)
        addpoly('GC1',pb(f,cn),j)
        addpoly('GG1',add((1,pb(gx,change(f,'X','Y'))),(1,pb(f,gy))),j)
        ij=(h[1],p[1])
        put('continuum_G2_0',ij,j,Q(1))
        put('continuum_G2_dh',ij,j,Q(h[2])-Q(1,2))
        put('continuum_G2_dp',ij,j,Q(p[2])-Q(1,2))
    for i in range(3):
        rhs['continuum_G2_dh',(i,i)]=Q(-1 if i==0 else 1)
    rhs['continuum_G2_dp',(0,0)]=Q(-2)
    for h in eh:
        j=new('F1:'+repr((h,0,1)))
        terms=[]
        for px,pc in [(0,2),(1,-2)]:
            terms.extend([(pc,(var('p',0,px),h,var('N'),var('M',0,1))),
                          (-pc,(var('p',0,px),h,var('M'),var('N',0,1)))])
        addpoly('CC2',functional(terms),j,-1)
        put('continuum_F1',(h[1],),j,Q(1))
    rhs['continuum_F1',(0,)]=Q(-1)
    for xp,np in product((-1,0),(-1,0,1)):
        j=new('U0:'+repr((xp,np)))
        terms=[(4*w,(var('X',0,xp),var('N',0,np),var('h',i,x)))
               for i in (1,2) for x,w in [(-1,1),(0,-2),(1,1)]]
        addpoly('GC1',functional(terms),j,-1)
        put('continuum_U0_0',(),j,Q(1))
        put('continuum_U0_dN',(),j,Q(np))
        put('continuum_U0_dX',(),j,Q(xp)+Q(1,2))
    rhs['continuum_U0_dN',()]=Q(1)
    for xp,yp in [(a,b) for a in (-1,0,1) for b in (-1,0,1) if a<b]:
        j=new('V0:'+repr((xp,yp)))
        terms=[]
        for px,pc in [(0,2),(1,-2)]:
            terms.extend([(pc,(var('p',0,px),var('X',0,xp),var('Y',0,yp))),
                          (-pc,(var('p',0,px),var('Y',0,xp),var('X',0,yp)))])
        addpoly('GG1',functional(terms),j,-1)
        put('continuum_V0',(),j,Q(yp-xp))
    rhs['continuum_V0',()]=Q(1)
    rows={k:clean(r) for k,r in rows.items()}
    return names,rows,rhs

def compare(names,rows,rhs):
    frozen=HERE/'axial_cc_start.py'
    assert hashlib.sha256(frozen.read_bytes()).hexdigest()==START_HASH
    spec=importlib.util.spec_from_file_location('frozen_author',frozen)
    a=importlib.util.module_from_spec(spec); spec.loader.exec_module(a)
    original=a.assemble(1,True,True)
    assert names==original.names
    def remap(k):
        fam,m=k
        return (fam,recenter(m,'N' if fam in ('CC2','GC1') else 'X')) if fam in ('CC2','GC1','GG1') else k
    oldrows={remap(k):clean(r) for k,r in original.rows.items()}
    oldrhs={remap(k):c for k,c in original.rhs.items()}
    keys=set(rows)|set(oldrows)|set(rhs)|set(oldrhs)
    for k in keys:
        assert rows.get(k,{})==oldrows.get(k,{}), ('matrix mismatch',k,rows.get(k),oldrows.get(k))
        assert rhs.get(k,0)==oldrhs.get(k,0), ('rhs mismatch',k,rhs.get(k),oldrhs.get(k))
    return keys

def solve_and_verify(names,rows,rhs,keys):
    # Independent Fraction row reduction without author's eliminator. Track
    # augmented rows, then substitute a particular solution and each basis
    # vector into all original independently assembled rows.
    basis={}; n=len(names)
    for idx,k in enumerate(sorted(keys,key=repr)):
        if idx%100==0: budget()
        r=dict(rows.get(k,{})); r[n]=rhs.get(k,Q(0)); r=clean(r)
        for pivot in sorted(basis):
            if pivot in r:
                factor=r[pivot]
                for col,c in basis[pivot].items(): r[col]=r.get(col,Q(0))-factor*c
                r=clean(r)
        if not r: continue
        pivot=min(r)
        assert pivot<n, ('inconsistency',k,r)
        scale=r[pivot]; basis[pivot]={j:c/scale for j,c in r.items()}
    free=sorted(set(range(n))-set(basis))
    def back(freecol=None):
        x=[Q(0)]*n
        if freecol is not None: x[freecol]=1
        for i in sorted(basis,reverse=True):
            r=basis[i]
            x[i]=(r.get(n,0) if freecol is None else 0)-sum(c*x[j] for j,c in r.items() if j not in (i,n))
        for k in keys:
            value=sum(c*x[j] for j,c in rows.get(k,{}).items())
            assert value==(rhs.get(k,0) if freecol is None else 0), ('solution residual',k)
        return x
    particular=back(); kernel=[back(j) for j in free]
    payload={'source_hash':START_HASH,'torus_side':L,'columns':n,'nonzero_rows':sum(bool(rows.get(k)) for k in keys),
             'rank':len(basis),'nullity':len(free),'free_columns':free,
             'particular':[[j,str(x)] for j,x in enumerate(particular) if x],
             'kernel':[[[j,str(x)] for j,x in enumerate(v) if x] for v in kernel]}
    (HERE/'independent_solution.json').write_text(json.dumps(payload,indent=2)+'\n')
    print(json.dumps({k:v for k,v in payload.items() if k not in ('particular','kernel')}),flush=True)
    print('Every independent particular and nullspace vector recombined exactly against all equations.',flush=True)

def main():
    budget(); started=time.time()
    names,rows,rhs=build()
    print('Torus derivative assembly complete',len(names),'columns',len(rows),'row keys',flush=True)
    keys=compare(names,rows,rhs)
    print('Exact comparison to frozen author assembly: every column, row and RHS identical.',flush=True)
    solve_and_verify(names,rows,rhs,keys)
    print('Elapsed seconds:',time.time()-started,flush=True)

if __name__=='__main__': main()
