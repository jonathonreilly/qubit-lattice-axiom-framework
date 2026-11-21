#!/usr/bin/env python3
"""Full SU(2) cube spin networks; trivalent magnetic contractions. GUIDE only."""
import guard
import os
for key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS','NUMEXPR_NUM_THREADS','BLIS_NUM_THREADS'):
    os.environ[key]='1'
import atexit
import argparse, importlib.util, itertools, json, math, signal, time
from functools import lru_cache
from pathlib import Path
import numpy as np
from scipy.sparse import csr_matrix, save_npz, load_npz
from scipy.sparse.linalg import LinearOperator,eigsh,expm_multiply
from scipy.special import ive
from numba import njit
spec=importlib.util.spec_from_file_location('base',Path(__file__).resolve().parents[1]/'gap-descent-sign-2-astra/recompute.py')
base=importlib.util.module_from_spec(spec);spec.loader.exec_module(base)
signal.signal(signal.SIGALRM,lambda *_:base.memory_check());signal.setitimer(signal.ITIMER_REAL,1,1)
atexit.register(lambda: signal.setitimer(signal.ITIMER_REAL,0))
EDGES=[(i,(i+1)%4) for i in range(4)]+[(4+i,4+(i+1)%4) for i in range(4)]+[(i,i+4) for i in range(4)]
VE=np.array([[(i-1)%4,i,8+i] for i in range(4)]+[[4+(i-1)%4,4+i,8+i] for i in range(4)])
ORIENT=[(-1,1,1)]*4+[(-1,1,-1)]*4
FACES=[(0,1,2,3),(4,5,6,7)]+[(i,8+(i+1)%4,4+i,8+i) for i in range(4)]

@njit
def enumerate_basis(J,H,do_build,E=100000):
    count=0
    # Double pass avoids a huge Python list/dictionary.
    rows=np.empty((1,12),np.int16)
    for repeat in range(2 if do_build else 1):
      if repeat:
        if count>8000000:raise MemoryError("basis inventory above 8 million states")
        rows=np.empty((count,12),np.int16);count=0
      for a in range(J+1):
       for b in range(J+1):
        for c in range(J+1):
         for d in range(J+1):
          for e in range(J+1):
           for f in range(J+1):
            for g in range(J+1):
             for h in range(J+1):
              if a+b+c+d+e+f+g+h>H:continue
              if a*(a+2)+b*(b+2)+c*(c+2)+d*(d+2)+e*(e+2)+f*(f+2)+g*(g+2)+h*(h+2)>E:continue
              if (a+d+e+h)%2 or (a+b+e+f)%2 or (b+c+f+g)%2 or (c+d+g+h)%2:continue
              for s in range(max(abs(d-a),abs(h-e)),min(d+a,h+e)+1,2):
               for t in range(max(abs(a-b),abs(e-f)),min(a+b,e+f)+1,2):
                for u in range(max(abs(b-c),abs(f-g)),min(b+c,f+g)+1,2):
                 for v in range(max(abs(c-d),abs(g-h)),min(c+d,g+h)+1,2):
                  if repeat: rows[count]=np.array([a,b,c,d,e,f,g,h,s,t,u,v])
                  count+=1
    return count,rows

@lru_cache(None)
def inv(js,ms,ori):
    ts=tuple(m*s for m,s in zip(ms,ori))
    if sum(ts):return 0.
    a,b,c=js;x,y,z=ts
    sign=(-1.0)**((a-b-z)//2)
    for j,m,s in zip(js,ms,ori):
        if s==-1:sign*=(-1.0)**((j-m)//2)
    return sign*base.cg(a,x,b,y,c,-z)/math.sqrt(c+1)

@lru_cache(None)
def vertex(old,new,unchanged,ori):
    face=[i for i in range(3) if i!=unchanged]
    terms=[]
    for m0 in range(-old[0],old[0]+1,2):
      for m1 in range(-old[1],old[1]+1,2):
        m2=-(ori[0]*m0+ori[1]*m1)*ori[2]
        ms=(m0,m1,m2)
        if abs(m2)>old[2] or (old[2]-m2)%2:continue
        ini=inv(old,ms,ori)
        if not ini:continue
        for alpha in (-1,1):
            al=[0,0,0];al[face[0]]=alpha;al[face[1]]=-ori[face[0]]*ori[face[1]]*alpha
            half=tuple(0 if i==unchanged else 1 for i in range(3))
            Jv=inv(half,tuple(al),ori)
            newms=tuple(m+x for m,x in zip(ms,al))
            fin=inv(new,newms,ori)
            if not fin or not Jv:continue
            C=1.
            for i in face:C*=base.cg(old[i],ms[i],1,al[i],new[i],newms[i])
            terms.append(ini*fin*Jv*C)
    return math.fsum(terms)

def face_sign(face):
    # Evaluate the normalized fundamental loop spin network at all U_e=1.
    vertices=[v for v in range(8) if sum(e in face for e in VE[v])==2]
    total=0.
    for inds in itertools.product((-1,1),repeat=4):
        mag=dict(zip(face,inds));term=1.
        for v in vertices:
            js=tuple(int(e in face) for e in VE[v]);ms=tuple(mag.get(e,0) for e in VE[v])
            term*=inv(js,ms,ORIENT[v])
        total+=term
    value=4*total # sqrt(2) per loop edge
    assert abs(abs(value)-2)<1e-12,value
    return 1 if value>0 else -1

@njit
def make_keys(rows,B):
    keys=np.zeros(len(rows),np.int64)
    for i in range(len(rows)):
      for e in range(12):keys[i]=keys[i]*B+rows[i,e]
    return keys

@njit
def assemble(rows,J,H,table,VE,faces,signs):
    B=2*J+2
    keys=make_keys(rows,B);order=np.argsort(keys);sortedkeys=keys[order]
    # Up to sixteen destinations per face per row; store one face at a time.
    rr=np.empty(len(rows)*16,np.int32);cc=np.empty_like(rr);vv=np.empty(len(rr));n=0
    face=faces[0]
    for idx in range(len(rows)):
      old=rows[idx]
      for mask in range(16):
        new=old.copy();ok=True;factor=signs[0]*.5
        for p in range(4):
          edge=face[p];new[edge]+=1 if (mask>>p)&1 else -1
          if new[edge]<0 or new[edge]>(J if edge<8 else 2*J):ok=False;break
          factor*=math.sqrt(2*(old[edge]+1)/(new[edge]+1))
        if not ok or np.sum(new[:8])>H:continue
        for v in range(8):
          changed=0;unchanged=0;code=0;k=0
          for a in range(3):
            edge=VE[v,a]
            if old[edge]!=new[edge]:
              changed+=1
              if new[edge]>old[edge]:code+=1<<k
              k+=1
            else:unchanged=a
          if changed:
            factor*=table[v//4,unchanged,old[VE[v,0]],old[VE[v,1]],old[VE[v,2]],code]
        if abs(factor)<1e-15:continue
        key=0
        for e in range(12):key=key*B+new[e]
        loc=np.searchsorted(sortedkeys,key)
        if loc>=len(rows) or sortedkeys[loc]!=key:continue
        rr[n]=order[loc];cc[n]=idx;vv[n]=factor;n+=1
    return rr[:n],cc[:n],vv[:n]

def build(J,H,dest,E=100000):
    start=time.monotonic();N,rows=enumerate_basis(J,H,True,E)
    print('BASIS',J,H,N,flush=True)
    if N>1200000:raise MemoryError('basis size above declared 1200000-state cap')
    L=2*J+1;tab=np.zeros((2,3,L,L,L,4))
    triples=set(tuple(map(int,row[edges])) for row in rows for edges in VE[:4])
    # The top layer has the same allowed triple set.
    triples.update(tuple(map(int,row[edges])) for row in rows for edges in VE[4:])
    for oriidx,ori in enumerate((ORIENT[0],ORIENT[4])):
      for old in sorted(triples):
       for un in range(3):
        changed=[i for i in range(3) if i!=un]
        for code in range(4):
          new=list(old)
          for k,i in enumerate(changed):new[i]+=1 if (code>>k)&1 else -1
          if not base.triangle(*new):continue
          tab[oriidx,un,*old,code]=vertex(old,tuple(new),un,ori)
    dest.mkdir(exist_ok=True)
    np.save(dest/'basis.npy',rows)
    for fi,face in enumerate(FACES):
        rr,cc,vv=assemble(rows,J,H,tab,VE,np.array([face]),np.array([face_sign(face)]))
        X=csr_matrix((vv,(rr,cc)),shape=(N,N));delta=X-X.T
        asym=float(np.max(np.abs(delta.data))) if delta.nnz else 0.
        assert asym<2e-12,(fi,asym)
        target=np.zeros(12,dtype=int);target[list(face)]=1
        pos=np.flatnonzero(np.all(rows==target,axis=1))[0]
        assert abs(abs(X[pos,0])-.5)<1e-12,(fi,X[pos,0])
        save_npz(dest/f'face{fi}.npz',X)
        print('FACE',fi,'nnz',X.nnz,'asym',asym,flush=True);base.memory_check()
    (dest/'meta.json').write_text(json.dumps(dict(J=J,H=H,E=E,N=N,seconds=time.monotonic()-start,peak_RSS_bytes=base.memory_check()),indent=2)+'\n')


def run(dest,betas,mults,out,transverse=None):
    start=time.monotonic();rows=np.load(dest/'basis.npy');Xs=[load_npz(dest/f'face{i}.npz') for i in range(6)]
    XT=Xs[0]+Xs[1];XM=sum(Xs[2:]); del Xs
    results=[]
    for b in betas:
        bT=b if transverse is None else transverse
        # Scalar shift keeps the magnetic exponential bounded by one.
        V=b*XM+bT*XT
        shift=4*b+2*bT
        from scipy.sparse import eye
        V=V-shift*eye(len(rows),format='csr')
        r=base.ratios(b,int(rows[:,:8].max()))
        kh=np.prod(r[rows[:,:8]],axis=1)
        values=[];last=None
        for mul in mults:
            bL=math.inf if mul==0 else 0.0 if mul==-1 else b*mul
            kv=(np.ones(len(rows)) if mul==0 else np.all(rows[:,8:]==0,axis=1).astype(float) if mul==-1 else np.prod(base.ratios(bL,int(rows[:,8:].max()))[rows[:,8:]],axis=1))
            w=np.sqrt(kh*kv)
            def matvec(x):return w*expm_multiply(V,w*x,traceA=-shift*len(rows))
            op=LinearOperator((len(rows),len(rows)),matvec=matvec)
            ev,U=eigsh(op,k=3,which='LA',tol=3e-11,ncv=16,v0=np.linspace(.9,1.1,len(rows)) if last is None else last)
            order=np.argsort(ev)[::-1];ev=ev[order];U=U[:,order];last=U[:,0]
            gap=float(np.log(ev[0]/ev[1]));res=[float(np.linalg.norm(matvec(U[:,i])-ev[i]*U[:,i])/ev[0]) for i in range(3)]
            item=dict(beta=b,beta_T=bT,beta_L='infinity' if mul==0 else bL,multiplier=mul,gap=gap,eigenvalues=ev.tolist(),residuals=res)
            values.append(item);print('VALUE',json.dumps(item),flush=True)
            results.append(item)
            out.write_text(json.dumps(dict(grade='GUIDE',basis=str(dest),results=results,seconds=time.monotonic()-start,peak_RSS_bytes=base.memory_check()),indent=2)+'\n')
        minf=next(x['gap'] for x in values if x['multiplier']==0)
        for x in values:x['difference']=x['gap']-minf
        out.write_text(json.dumps(dict(grade='GUIDE',basis=str(dest),results=results,seconds=time.monotonic()-start,peak_RSS_bytes=base.memory_check()),indent=2)+'\n')

def main():
 p=argparse.ArgumentParser();p.add_argument('action',choices=['count','build','run']);p.add_argument('--J',type=int,default=3);p.add_argument('--H',type=int,default=12);p.add_argument('--E',type=int,default=100000);p.add_argument('--basis',type=Path);p.add_argument('--betas',type=float,nargs='+',default=[2.4]);p.add_argument('--mults',type=float,nargs='+',default=[0,8,4,2,1]);p.add_argument('--transverse',type=float);p.add_argument('--output',type=Path);a=p.parse_args()
 if a.action=='count':print('COUNT',a.J,a.H,enumerate_basis(a.J,a.H,False,a.E)[0])
 elif a.action=='build':build(a.J,a.H,a.basis,a.E)
 else:run(a.basis,a.betas,a.mults,a.output,a.transverse)
if __name__=='__main__':main()
