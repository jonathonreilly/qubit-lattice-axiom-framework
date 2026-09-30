#!/usr/bin/env python3
"""Independent literal-position coefficient verification; no author imports."""
import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[k]='1'
from pathlib import Path
from fractions import Fraction as F
from itertools import product,permutations
from math import lcm
import json,time,hashlib,resource

HERE=Path(__file__).resolve().parent
AUTHOR=HERE.parent/'independent-matter-cross-route'
RUNTIME=Path('/Users/jonBridger/.codex/campaigns/toe-gravity-law-24h-20260929')
ZERO=(0,0,0);GCZERO=(0,0)
def budget():
    assert time.time()<json.loads((RUNTIME/'DEADLINE.json').read_text())['deadline_epoch']
    assert not (RUNTIME/'STOP_REQUESTED.json').exists()
def plus(a,b):return tuple(x+y for x,y in zip(a,b))
def minus(a,b):return tuple(x-y for x,y in zip(a,b))
def neg(a):return tuple(-x for x in a)
def unit(j,n=1):return tuple(n if i==j else 0 for i in range(3))
def gadd(a,b):return (a[0]+b[0],a[1]+b[1])
def gscale(a,c):return (a[0]*c,a[1]*c)
def gmul(a,b):return (a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def conj(a):return (a[0],-a[1])
def put(d,k,v):
    w=gadd(d.get(k,GCZERO),v)
    if w!=GCZERO:d[k]=w
    else:d.pop(k,None)
PAULI=[{(0,0):(1,0),(1,1):(1,0)},
       {(0,1):(1,0),(1,0):(1,0)},
       {(0,1):(0,-1),(1,0):(0,1)},
       {(0,0):(1,0),(1,1):(-1,0)}]
def mm(a,b):
    d={}
    for (i,j),v in a.items():
        for (l,k),w in b.items():
            if j==l:put(d,(i,k),gmul(v,w))
    return d
def scale_mat(a,c):return {k:gmul(v,c) for k,v in a.items()}
def adj(a):return {(j,i):conj(v) for (i,j),v in a.items()}
def block(d,row,col,m,c=F(1)):
    for (i,j),v in m.items():put(d,(row,i,col,j),gscale(v,c))
def move_matrix(d,offset,c=F(1)):
    return {(plus(r,offset),i,plus(s,offset),j):gscale(v,c) for (r,i,s,j),v in d.items()}
HOPS=[(unit(j,sgn),scale_mat(PAULI[j+1],(0,F(-sgn,2)))) for j in range(3) for sgn in (-1,1)]
BODY=list(product((-1,1),repeat=3))

def source_operators():
    energy={}
    for center in BODY:
        for hop,h in HOPS:
            block(energy,center,plus(center,hop),h,F(1,16))
            block(energy,plus(center,hop),center,adj(h),F(1,16))
    currents=[]
    for axis in range(3):
        pdouble={};qb={}
        centers=[tuple(a if j==axis else 2*a-1 for j,a in enumerate(bits)) for bits in product((0,1),repeat=3)]
        for center in centers:
            for sign in (-1,1):
                h=scale_mat(PAULI[0],(0,F(-sign,4)))
                block(pdouble,center,plus(center,unit(axis,2*sign)),h,F(1,16))
                block(pdouble,plus(center,unit(axis,2*sign)),center,adj(h),F(1,16))
        ej=unit(axis)
        for hop,h in HOPS:
            # The two literal terms in Q^b, followed by their adjoints.
            for row,col,m in [(ej,hop,mm(PAULI[axis+1],h)),
                              (plus(ej,hop),ZERO,mm(adj(h),PAULI[axis+1]))]:
                block(qb,row,col,m,F(1,4));block(qb,col,row,adj(m),F(1,4))
        result={k:gscale(v,F(1,2)) for k,v in pdouble.items()}
        for center in BODY:
            for key,v in move_matrix(qb,center,F(1,16)).items():put(result,key,v)
        currents.append(result)
    def uniform(a):
        d={}
        for (r,i,c,j),v in a.items():put(d,(minus(c,r),i,j),v)
        return d
    h={}
    for hop,m in HOPS:
        for (i,j),v in m.items():put(h,(hop,i,j),v)
    assert uniform(energy)==h
    for axis,b in enumerate(currents):
        want={}
        for sign in (-1,1):
            for (i,j),v in PAULI[0].items():put(want,(unit(axis,2*sign),i,j),gmul(v,(0,F(-sign,4))))
        assert uniform(b)==want
    assert all(v==conj(energy.get((c,j,r,i),GCZERO)) for (r,i,c,j),v in energy.items())
    assert all(v==conj(b.get((c,j,r,i),GCZERO)) for b in currents for (r,i,c,j),v in b.items())
    return energy,currents

def curvature():
    result=[]
    for i in range(3):
        r={ZERO:4}
        for j in range(3):
            if i!=j:r[unit(j)]=-1;r[unit(j,-1)]=-1
        result.append(r)
    for i,j in [(0,1),(0,2),(1,2)]:
        result.append({ZERO:2,unit(i):-2,unit(j):-2,plus(unit(i),unit(j)):2})
    for r in result:
        assert sum(r.values())==0
        for j in range(3):assert sum(a[j]*c for a,c in r.items())==0
    return result

def flat_defect(energy,currents,denom):
    e={k:(int(v[0]*32),int(v[1]*32)) for k,v in energy.items()}
    assert all(v[0]*32==e[k][0] and v[1]*32==e[k][1] for k,v in energy.items())
    comm={}
    for (r,i,s,j),v in e.items():
        for (t,l,c,n),w in e.items():
            if j!=l:continue
            m=minus(s,t);col=plus(c,m)
            value=gscale(gmul((0,-1),gmul(v,w)),denom//1024)
            put(comm,(m,r,i,col,n),value)
            put(comm,(neg(m),minus(r,m),i,minus(col,m),n),gscale(value,-1))
    current={}
    for axis,b in enumerate(currents):
        ej=unit(axis)
        for (r,i,c,j),v in b.items():
            value=(int(v[0]*denom),int(v[1]*denom))
            assert value[0]==v[0]*denom and value[1]==v[1]*denom
            # D=-i[E_N,E_M]+P^B[F], since J=-P^B.
            put(current,(ej,r,i,c,j),value)
            put(current,(neg(ej),minus(r,ej),i,minus(c,ej),j),gscale(value,-1))
    defect=dict(comm)
    for k,v in current.items():put(defect,k,v)
    literal=dict(comm)
    for k,v in current.items():put(literal,k,gscale(v,-1))
    return defect,literal

def first_jets(d):
    out={}
    for (m,r,i,c,j),value in d.items():
        x=neg(r);y=minus(m,r);z=minus(c,r)
        for a,weightx in [(-1,1)]+list(enumerate(x)):
            if not weightx:continue
            for b,weighty in [(-1,1)]+list(enumerate(y)):
                if weighty:put(out,(z,a,b,i,j),gscale(value,weightx*weighty))
    return out

def coupling_checks(serial,denom,rs,defect):
    # The certificate is read as real-space density data, not multiplied
    # by an imported Laurent builder.
    coeffs=[];recombined={};count=0;radii=[]
    for t,component in enumerate(serial):
        table={};radius=lapseradius=diameter=0
        center2=ZERO if t<3 else tuple(int(k in [(0,1),(0,2),(1,2)][t-3]) for k in range(3))
        for ex,pauli,imag,val in component:
            a,b,c=tuple(ex[:3]),tuple(ex[3:6]),tuple(ex[6:])
            n=F(val)*denom;assert n.denominator==1;n=int(n)
            assert (pauli==0 and imag==1) or (pauli!=0 and imag==0),('time parity',t,ex,pauli,imag)
            table[(tuple(ex),pauli,imag)]=n
            lapse=minus(b,a);bra=neg(a);ket=minus(c,a)
            points=[center2,tuple(2*x for x in lapse),tuple(2*x for x in bra),tuple(2*x for x in ket)]
            radius=max(radius,max(abs(x-y) for pt in points[1:] for x,y in zip(pt,center2)))
            lapseradius=max(lapseradius,max(abs(x-y) for pt in points for x,y in zip(pt,points[1])))
            diameter=max(diameter,max(max(pt[j] for pt in points)-min(pt[j] for pt in points) for j in range(3)))
            value=(n,0) if imag==0 else (0,n)
            for (i,j),p in PAULI[pauli].items():
                mv=gmul(value,p)
                for shift,rc in rs[t].items():
                    put(recombined,(minus(lapse,shift),minus(bra,shift),i,minus(ket,shift),j),gscale(mv,rc))
                    put(recombined,(minus(shift,lapse),minus(bra,lapse),i,minus(ket,lapse),j),gscale(mv,-rc))
            count+=1
        coeffs.append(table);radii.append([str(F(x,2)) for x in (radius,lapseradius,diameter)])
    assert recombined==defect,('full recombination',len(recombined),len(defect),next(((k,recombined.get(k),defect.get(k)) for k in recombined.keys()|defect.keys() if recombined.get(k)!=defect.get(k)),None))
    for t,table in enumerate(coeffs):
        for (ex,p,im),v in table.items():
            a,b,c=ex[:3],ex[3:6],ex[6:]
            flipped=minus(a,c)+minus(b,c)+neg(c)
            assert table.get((flipped,p,im))==v*(-1 if im else 1)
    pairlist=[(0,0),(1,1),(2,2),(0,1),(0,2),(1,2)]
    rotations=0
    for perm in permutations(range(3)):
        parity=(-1)**sum(perm[i]>perm[j] for i in range(3) for j in range(i+1,3))
        for signs in product((-1,1),repeat=3):
            if parity*signs[0]*signs[1]*signs[2]!=1:continue
            budget();rotations+=1
            def turn(a):
                out=[0,0,0]
                for i in range(3):out[perm[i]]=signs[i]*a[i]
                return tuple(out)
            for t,table in enumerate(coeffs):
                i,j=pairlist[t];target=pairlist.index(tuple(sorted((perm[i],perm[j]))))
                anchor=[0,0,0]
                if i!=j:
                    for axis in (i,j):
                        if signs[axis]<0:anchor[perm[axis]]=-1
                for (ex,p,im),v in table.items():
                    np=0 if p==0 else perm[p-1]+1
                    sign=signs[i]*signs[j]*(1 if p==0 else signs[p-1])
                    transformed=plus(turn(ex[:3]),tuple(anchor))+turn(ex[3:6])+turn(ex[6:])
                    assert coeffs[target].get((transformed,np,im))==sign*v,('rotation',t,perm,signs,ex,p,im)
    assert rotations==24
    return {'coefficient_count':count,'position_matrix_entries':len(recombined),'exact_full_recombination':True,
            'Hermitian':True,'time_reversal_odd':True,'proper_rotations':rotations,
            'component_P_radius_lapse_radius_diameter':radii}

def mixed_checks():
    out=[]
    for axis in range(3):
        bracket={};expected={}
        for phop_sign in (-1,1):
            phop=unit(axis,2*phop_sign);pv=(0,F(-phop_sign,4))
            for hhop,hmat in HOPS:
                target=plus(phop,hhop)
                # Row-zero literal kernels of i[P,E_X]; E_X(r,c)=(r_j+c_j)H(r,c)/2.
                factor=F(phop[axis]+target[axis]-hhop[axis],2)
                for (i,j),v in hmat.items():
                    put(bracket,(target,i,j),gscale(gmul((0,1),gmul(pv,v)),factor))
                    put(expected,(target,i,j),gscale(v,F(1,2)))
        assert bracket==expected
        coeff=GCZERO
        for (i,j),v in PAULI[axis+1].items():
            coeff=gadd(coeff,gscale(gmul(conj(v),bracket.get((unit(axis,3),i,j),GCZERO)),F(1,2)))
        assert coeff==(0,F(-1,4))
        out.append({'axis':axis,'sigma_j_z_j_cubed':[str(x) for x in coeff],
                    'literal_position_matrix_entries':len(bracket)})
    return out

def main():
    budget();start=time.time()
    frozen={'REPORT.md':'e0535076030c83f451c25a2bbab81076763b798a5d782d7676912a61e0c9f8e1',
            'coupling_KA.json':'9bc29d9f43e5d83993922ec83402b9f6237c956689ce00e56bf14d9dd28a900e'}
    for name,digest in frozen.items():assert hashlib.sha256((AUTHOR/name).read_bytes()).hexdigest()==digest
    serial=json.loads((AUTHOR/'coupling_KA.json').read_text())
    denom=1024
    for comp in serial:
        for row in comp:denom=lcm(denom,F(row[-1]).denominator)
    energy,current=source_operators();rs=curvature();defect,literal=flat_defect(energy,current,denom)
    assert not first_jets(defect)
    wrong=first_jets(literal);assert wrong
    key=(unit(0,2),(-1,-1,-1),0,(1,-1,-1),0)
    assert defect[key]==(0,denom//1024)
    result={'source_energy_matrix_entries':len(energy),'literal_position_defect_entries':len(defect),
            'relative_lapse_displacements':len({k[0] for k in defect}),
            'integer_scale':denom,'correct_sign_normal_remainder_entries':0,
            'literal_plus_current_normal_remainder_entries':len(wrong),
            'delta2_witness':[str(F(x,denom)) for x in defect[key]],
            'curvature_zeroth_and_first_moments_zero':True,
            'coupling':coupling_checks(serial,denom,rs,defect),'mixed':mixed_checks()}
    budget();result['elapsed_seconds']=time.time()-start
    result['maxrss_bytes']=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    result['frozen_inputs']=frozen
    (HERE/'results.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))

if __name__=='__main__':main()
