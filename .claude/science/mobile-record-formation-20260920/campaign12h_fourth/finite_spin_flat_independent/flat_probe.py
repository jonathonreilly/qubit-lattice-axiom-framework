from collections import defaultdict
from fractions import Fraction
import json
import sympy as sy
from physical_builder import *

f=sy.Symbol('f',integer=True)

def word(C,r):
    occ=[i for i in range(8) if i%2==0 or i//2 in C]
    return tuple(0 if i not in occ else (-1 if occ.index(i)==r else 1) for i in range(8))

def coord(q):
    return tuple(i//2 for i in range(1,8,2) if q[i]),[x for x in q if x].index(-1)

def flat_mode(a,r,z=0):
    if a==0:
        c=-1 if r==0 else 1
        return {(word((0,1),r),z):sy.Integer(1),(word((2,3),(r-1)%6),z+c):sy.Integer(-1)}
    return {(word((0,3),r),z):sy.Integer(1),(word((1,2),r),z):sy.Integer(-1)}

def flat_coord(q,z):
    C,r=coord(q)
    if C==(0,1):return (0,r,z),1
    if C==(2,3):
        pre=(r+1)%6;c=-1 if pre==0 else 1
        return (0,pre,z-c),-1
    if C==(0,3):return (1,r,z),1
    if C==(1,2):return (1,r,z),-1
    return None,0

def clean(v):return {k:sy.expand(a) for k,a in v.items() if sy.expand(a)!=0}

def h2_apply(v,correction=False):
    ret=defaultdict(lambda:sy.Integer(0))
    for (q,z),a in v.items():
        for qq,d,(g,k),(h,l) in h2_paths(q):
            coeff=((f+z+g)*(f+z+g+k)+(f+z+h)*(f+z+h+l))/2 if correction else -1
            ret[qq,z+d]+=a*coeff
    return clean(ret)

def hop_apply(v,need):
    ret=defaultdict(lambda:sy.Integer(0))
    for (q,z),a in v.items():
        for qq,d,*_ in hop_data(q):
            if grade(qq)==need:ret[qq,z+d]-=a
    return clean(ret)

def h4_apply(v):
    m2=h2_apply(h2_apply(v))
    z2=v
    for g in (1,2,1,0):z2=hop_apply(z2,g)
    ret=defaultdict(lambda:sy.Integer(0),m2)
    for k,a in z2.items():ret[k]-=a/2
    return clean(ret)

def jump_apply(v,coherent=False):
    hopped=hop_apply(v,1);ret=defaultdict(lambda:defaultdict(lambda:sy.Integer(0)))
    for (q,z),a in hopped.items():
        for qq,d,e,c,g in birth_data(q):
            ch=e if coherent else (e,c)
            ret[ch][qq,z+d]-=a
    return {ch:clean(v) for ch,v in ret.items()}

def loss_apply(v,coherent=False):
    """B†B via reconstructing all possible source states for each finite output."""
    outputs=jump_apply(v,coherent); ret=defaultdict(lambda:sy.Integer(0))
    # Reverse effective paths by finite candidate input neighborhood; exact range <=2.
    fields=[z for q,z in v];lo=min(fields)-2;hi=max(fields)+2
    for q in PWORDS:
        for z in range(lo,hi+1):
            images=jump_apply({(q,z):sy.Integer(1)},coherent)
            a=0
            for ch,image in images.items():
                a+=sum(aa*outputs.get(ch,{}).get(s,0) for s,aa in image.items())
            if a:ret[q,z]=a
    return clean(ret)

def compress(v):
    ret=defaultdict(lambda:sy.Integer(0))
    for (q,z),a in v.items():
        k,sign=flat_coord(q,z)
        if k is not None:ret[k]+=sign*a/2
    return clean(ret)

def project(v):
    ret=defaultdict(lambda:sy.Integer(0))
    for (a,r,z),amp in compress(v).items():
        for s,b in flat_mode(a,r,z).items():ret[s]+=amp*b
    return clean(ret)

def residual(v):
    ret=defaultdict(lambda:sy.Integer(0),v)
    for s,a in project(v).items():ret[s]-=a
    return clean(ret)

def serial(v):return [{'state':str(k),'coefficient':str(a)} for k,a in v.items()]

def main():
    result={'operators':{},'flat_eigen_residuals':[]}
    for a in range(2):
        for r in range(6):
            v=flat_mode(a,r); h=h2_apply(v)
            for k,b in v.items():h[k]=h.get(k,0)+4*b
            assert not clean(h)
            result['flat_eigen_residuals'].append([a,r,0])
    for name,op in [('D',lambda v:h2_apply(v,True)),('H4',h4_apply),('loss_res',loss_apply),('loss_coh',lambda v:loss_apply(v,True))]:
        rows=[]
        for a in range(2):
            for r in range(6):
                got=op(flat_mode(a,r))
                rows.append({'input':[a,r],'compression':serial(compress(got)),'leakage':serial(residual(got))})
        result['operators'][name]=rows
        print(name,'leakage_count',sum(bool(row['leakage']) for row in rows))
        for row in rows:print(row)
    Path=__import__('pathlib').Path
    Path('FLAT_PROBE_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')

if __name__=='__main__':main()
