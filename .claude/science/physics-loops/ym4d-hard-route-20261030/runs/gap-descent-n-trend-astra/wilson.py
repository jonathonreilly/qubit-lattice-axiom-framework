#!/usr/bin/env python3
"""n=3 Wilson spin networks with explicit four-valent middle intertwiners.
Builds on row 1089's trivalent contractions. GUIDE, no tail certification.
"""
from leakage import *
from wilson_inventory import choices
import itertools
from functools import lru_cache
from numba import njit
from scipy.sparse import csr_matrix, save_npz, load_npz
spec=importlib.util.spec_from_file_location('prior_cube', PREV/'cube.py')
cube=importlib.util.module_from_spec(spec);spec.loader.exec_module(cube)
signal.setitimer(signal.ITIMER_REAL,0)
# Each ring column: bottom/middle/top horizontal, lower/upper vertical, middle channel.
VE=[];ORI=[]
for layer in range(3):
    for i in range(4):
        prev=(i-1)%4
        if layer==0:VE.append([6*prev,6*i,6*i+3]);ORI.append((-1,1,1))
        elif layer==1:VE.append([6*prev+1,6*i+1,6*i+3,6*i+4]);ORI.append((-1,1,-1,1))
        else:VE.append([6*prev+2,6*i+2,6*i+4]);ORI.append((-1,1,-1))
FACES=[tuple(6*i+l for i in range(4)) for l in range(3)]
FACES += [(6*i+l,6*((i+1)%4)+3+l,6*i+l+1,6*i+3+l) for l in range(2) for i in range(4)]
PAIRS=[(0,1),(0,2),(1,2),(0,3),(1,3)]

@lru_cache(200000)
def inv4(js,channel,ms):
    ts=tuple(m*s for m,s in zip(ms,(-1,1,-1,1)))
    if sum(ts):return 0.
    a,b,c,d=js;x,y,z,w=ts;M=x+y
    sign=(-1.)**((channel-M)//2)
    for j,m,s in zip(js,ms,(-1,1,-1,1)):
        if s==-1:sign*=(-1.)**((j-m)//2)
    return sign*base.cg(a,x,b,y,channel,M)*base.cg(c,z,d,w,channel,-M)/math.sqrt(channel+1)

@lru_cache(None)
def vertex4(old,r,new,rnew,pair):
    result=[];ori=(-1,1,-1,1);half=tuple(int(i in pair) for i in range(4));hr=0 if pair==(0,1) else 1
    for m0 in range(-old[0],old[0]+1,2):
      for m1 in range(-old[1],old[1]+1,2):
       for m2 in range(-old[2],old[2]+1,2):
        m3=m0-m1+m2
        if abs(m3)>old[3] or (old[3]-m3)%2:continue
        ms=(m0,m1,m2,m3);ini=inv4(old,r,ms)
        if not ini:continue
        for alpha in (-1,1):
            al=[0]*4;al[pair[0]]=alpha;al[pair[1]]=-ori[pair[0]]*ori[pair[1]]*alpha
            loop=inv4(half,hr,tuple(al));newms=tuple(m+x for m,x in zip(ms,al))
            fin=inv4(new,rnew,newms)
            if not fin or not loop:continue
            C=math.prod(base.cg(old[i],ms[i],1,al[i],new[i],newms[i]) for i in pair)
            result.append(ini*fin*loop*C)
    return math.fsum(result)


def face_sign(face):
    verts=[v for v,edges in enumerate(VE) if sum(e in face for e in edges)==2];value=0.
    for inds in itertools.product((-1,1),repeat=4):
        mag=dict(zip(face,inds));term=1.
        for v in verts:
            js=tuple(int(e in face) for e in VE[v]);ms=tuple(mag.get(e,0) for e in VE[v])
            if 4<=v<8:term*=inv4(js,0 if js[2]==js[3]==0 else 1,ms)
            else:term*=cube.inv(js,ms,ORI[v])
        value+=4*term
    assert abs(abs(value)-2)<1e-12,(face,value)
    return 1 if value>0 else -1

@njit
def enumerate_rows(hs,W,opts,E,build):
    L=len(hs);en=np.sum(hs*(hs+2),axis=1);count=0;rows=np.empty((1,24),np.int8)
    for repeat in range(2 if build else 1):
        if repeat:
            if count>1300000:raise MemoryError('full-basis preallocation gate 1300000 states')
            rows=np.empty((count,24),np.int8);count=0
        for a in range(L):
         for b in range(L):
          if W[a,b]==0 or en[a]+en[b]>E:continue
          for c in range(L):
           if W[b,c]==0 or en[a]+en[b]+en[c]>E:continue
           for d in range(L):
            if en[a]+en[b]+en[c]+en[d]>E or W[c,d]==0 or W[d,a]==0:continue
            if not repeat:count+=W[d,a]*W[a,b]*W[b,c]*W[c,d];continue
            for ia in range(W[d,a]):
             for ib in range(W[a,b]):
              for ic in range(W[b,c]):
               for idd in range(W[c,d]):
                for col,hidx in enumerate((a,b,c,d)):
                    rows[count,col*6:col*6+3]=hs[hidx]
                rows[count,3:6]=opts[d,a,ia];rows[count,9:12]=opts[a,b,ib]
                rows[count,15:18]=opts[b,c,ic];rows[count,21:24]=opts[c,d,idd];count+=1
    return count,rows

@njit
def keys(rows):
    out=np.zeros((len(rows),2),np.int64)
    for i in range(len(rows)):
        for j in range(12):out[i,0]=16*out[i,0]+rows[i,j]
        for j in range(12,24):out[i,1]=16*out[i,1]+rows[i,j]
    return out

@njit
def lookup(row,ks):
    k0=0;k1=0
    for j in range(12):k0=16*k0+row[j]
    for j in range(12,24):k1=16*k1+row[j]
    lo=0;hi=len(ks)
    while lo<hi:
        mid=(lo+hi)//2
        if ks[mid,0]<k0 or (ks[mid,0]==k0 and ks[mid,1]<k1):lo=mid+1
        else:hi=mid
    if lo<len(ks) and ks[lo,0]==k0 and ks[lo,1]==k1:return lo
    return -1

@njit
def entries(rows,ks,J,face,sign,ve,changed,midcols,tab3,tab4,capacity):
    rr=np.empty(capacity,np.int32);cc=np.empty(capacity,np.int32);vv=np.empty(capacity);used=0
    for idx in range(len(rows)):
        old=rows[idx]
        for mask in range(16):
            new=old.copy();factor=.5*sign;ok=True
            for p in range(4):
                edge=face[p];new[edge]+=1 if (mask>>p)&1 else -1
                if new[edge]<0 or new[edge]>(J if edge%6<3 else 2*J):ok=False;break
                factor*=math.sqrt(2*(old[edge]+1)/(new[edge]+1))
            if not ok:continue
            # Middle-channel choices for side plaquettes only.
            for rmask in range(1<<len(midcols)):
                okay=True
                for k,col in enumerate(midcols):
                    new[6*col+5]=old[6*col+5]+(1 if (rmask>>k)&1 else -1)
                    if new[6*col+5]<0 or new[6*col+5]>2*J:okay=False;break
                if not okay:continue
                dest=lookup(new,ks)
                if dest<0:continue
                f=factor
                for v in range(12):
                    if changed[v,0]<0:continue
                    p0=changed[v,0];p1=changed[v,1]
                    code=int(new[ve[v,p0]]>old[ve[v,p0]])+2*int(new[ve[v,p1]]>old[ve[v,p1]])
                    if 4<=v<8:
                        pairid=changed[v,2];r=old[(v-4)*6+5]
                        if pairid!=0:code+=4*int(new[(v-4)*6+5]>r)
                        f*=tab4[pairid,old[ve[v,0]],old[ve[v,1]],old[ve[v,2]],old[ve[v,3]],r,code]
                    else:
                        un=3-p0-p1
                        f*=tab3[int(v>=8),un,old[ve[v,0]],old[ve[v,1]],old[ve[v,2]],code]
                if abs(f)<1e-15:continue
                if capacity:rr[used]=dest;cc[used]=idx;vv[used]=f
                used+=1
    return rr,cc,vv,used


def build(J,E,dest):
    start=time.monotonic();hs,W,opts=choices(J);N,rows=enumerate_rows(hs,W,opts,E,True)
    print('BASIS',J,E,N,flush=True);ks=keys(rows);order=np.lexsort((ks[:,1],ks[:,0]));rows=rows[order];ks=ks[order]
    L=2*J+1;tab3=np.zeros((2,3,L,L,L,4));tab4=np.zeros((5,J+1,J+1,L,L,L,8))
    for oriidx,ori in enumerate(((-1,1,1),(-1,1,-1))):
        for a,b,c in itertools.product(range(J+1),range(J+1),range(L)):
            old=(a,b,c)
            if not base.triangle(*old):continue
            for un in range(3):
                pair=[i for i in range(3) if i!=un]
                for code in range(4):
                    new=list(old)
                    for k,i in enumerate(pair):new[i]+=1 if (code>>k)&1 else -1
                    if base.triangle(*new):tab3[oriidx,un,a,b,c,code]=cube.vertex(old,tuple(new),un,ori)
    oldset=set()
    for i in range(4):
        es=VE[4+i]
        oldset.update(tuple(map(int,x)) for x in rows[:,es+[6*i+5]])
    norms=[]
    for a,b,c,d,r in sorted(oldset):
        old=(a,b,c,d)
        norm=0.
        for m0,m1,m2 in itertools.product(range(-a,a+1,2),range(-b,b+1,2),range(-c,c+1,2)):
            m3=m0-m1+m2
            if abs(m3)<=d and (d-m3)%2==0:norm+=inv4(old,r,(m0,m1,m2,m3))**2
        norms.append(abs(norm-1))
        for pid,pair in enumerate(PAIRS):
            for code in range(4 if pid==0 else 8):
                new=list(old)
                for k,i in enumerate(pair):new[i]+=1 if (code>>k)&1 else -1
                rn=r if pid==0 else r+(1 if code&4 else -1)
                if max(new[:2])<=J and max(new[2:])<=2*J and rn<=2*J and base.triangle(new[0],new[1],rn) and base.triangle(new[2],new[3],rn):
                    tab4[pid,a,b,c,d,r,code]=vertex4(old,r,tuple(new),rn,pair)
    assert max(norms)<2e-12,max(norms)
    print('VERTICES',len(oldset),'norm error',max(norms),flush=True)
    import gc
    inv4.cache_clear();vertex4.cache_clear();cube.inv.cache_clear();cube.vertex.cache_clear();base.cg.cache_clear();gc.collect()
    ve=np.full((12,4),-1,np.int16)
    for v,es in enumerate(VE):ve[v,:len(es)]=es
    dest.mkdir(exist_ok=True);np.save(dest/'rows.npy',rows);diagnostics=[]
    for fi,face in enumerate(FACES):
        changed=np.full((12,3),-1,np.int16)
        for v,es in enumerate(VE):
            pair=tuple(i for i,e in enumerate(es) if e in face)
            if pair:
                assert len(pair)==2
                changed[v,:2]=pair
                if 4<=v<8:changed[v,2]=PAIRS.index(pair)
        midcols=np.array([v-4 for v in range(4,8) if changed[v,0]>=0 and changed[v,2]!=0],np.int16)
        args=(rows,ks,J,np.array(face),face_sign(face),ve,changed,midcols,tab3,tab4)
        _,_,_,cap=entries(*args,0)
        if cap*16+base.memory_check()>1_950_000_000:raise MemoryError('plaquette allocation gate')
        rr,cc,vv,used=entries(*args,cap);assert used==cap
        Y=csr_matrix((vv,(rr,cc)),shape=(N,N));del rr,cc,vv
        delta=Y-Y.T;asym=float(np.max(np.abs(delta.data))) if delta.nnz else 0.
        assert asym<2e-12,(fi,asym)
        target=np.zeros(24,np.int8);target[list(face)]=1;target[6*midcols+5]=1
        loc=lookup(target,ks);zero=lookup(np.zeros(24,np.int8),ks)
        assert loc>=0 and abs(abs(Y[loc,zero])-.5)<2e-12,(fi,loc,Y[loc,zero])
        diagnostics.append({'face':fi,'nnz':Y.nnz,'asymmetry':asym})
        np.save(dest/f'face{fi}_data.npy',Y.data);np.save(dest/f'face{fi}_indices.npy',Y.indices);np.save(dest/f'face{fi}_indptr.npy',Y.indptr)
        print('FACE',fi,'nnz',Y.nnz,'asym',asym,flush=True);del Y,delta;base.memory_check()
    # Different plaquettes change different physical edge sets, so their
    # off-diagonal destinations cannot overlap. Assemble in bounded row blocks.
    total=sum(d['nnz'] for d in diagnostics)
    values=np.lib.format.open_memmap(dest/'X_data.npy',mode='w+',dtype=np.float64,shape=(total,))
    indices=np.lib.format.open_memmap(dest/'X_indices.npy',mode='w+',dtype=np.int32,shape=(total,))
    indptr=np.lib.format.open_memmap(dest/'X_indptr.npy',mode='w+',dtype=np.int32,shape=(N+1,))
    faces=[]
    for fi in range(11):
        faces.append(csr_matrix((np.load(dest/f'face{fi}_data.npy',mmap_mode='r'),np.load(dest/f'face{fi}_indices.npy',mmap_mode='r'),np.load(dest/f'face{fi}_indptr.npy',mmap_mode='r')),shape=(N,N),copy=False))
    cursor=0;indptr[0]=0
    for startrow in range(0,N,4000):
        stop=min(N,startrow+4000);part=sum(f[startrow:stop] for f in faces)
        k=part.nnz;values[cursor:cursor+k]=part.data;indices[cursor:cursor+k]=part.indices
        indptr[startrow+1:stop+1]=part.indptr[1:]+cursor;cursor+=k
    assert cursor==total,(cursor,total)
    values.flush();indices.flush();indptr.flush()
    meta=dict(J=J,E=E,N=N,nnz=total,assembly='face files, row blocks of 4000',faces=diagnostics,intertwiner_norm_error=max(norms),seconds=time.monotonic()-start,peak_RSS_bytes=base.memory_check())
    (dest/'meta.json').write_text(json.dumps(meta,indent=2)+'\n');print('BUILT',meta,flush=True)


def run(dest,out):
    rows=np.load(dest/'rows.npy');N=len(rows)
    if (dest/'X_data.npy').exists():
        X=csr_matrix((np.load(dest/'X_data.npy',mmap_mode='r'),np.load(dest/'X_indices.npy',mmap_mode='r'),np.load(dest/'X_indptr.npy',mmap_mode='r')),shape=(N,N),copy=False)
    else:X=load_npz(dest/'X.npz')
    record={'grade':'GUIDE','basis':str(dest),'basis_meta':json.loads((dest/'meta.json').read_text()),'results':[]}
    if out.exists():
        record=json.loads(out.read_text());assert record['basis']==str(dest),'refuse mixed basis outputs'
    completed={(x['beta'],x['multiplier']) for x in record['results']}
    start=time.monotonic();last=None
    hor=[6*i+l for i in range(4) for l in range(3)];long=[6*i+l for i in range(4) for l in (3,4)]
    for b in (2.3,2.4,2.5,2.6):
        rh=base.ratios(b,int(rows[:,hor].max()));kh=np.prod(rh[rows[:,hor]],axis=1)
        for mul in (0,4,2,1):
            if (b,mul) in completed:continue
            kv=np.ones(N) if mul==0 else np.prod(base.ratios(b*mul,int(rows[:,long].max()))[rows[:,long]],axis=1)
            w=np.sqrt(kh*kv);shift=11*b;calls=0;point_start=time.monotonic()
            def apply(v):
                nonlocal calls
                calls+=1
                base.memory_check()
                term=math.exp(-shift)*w*v;y=term.copy();weight=math.exp(-shift)
                for k in range(1,401):
                    term=(b/k)*(X@term);y+=term;weight*=shift/k
                    if k%8==0:base.memory_check()
                    if k>shift and weight<1e-22:return w*y
                raise RuntimeError('Taylor degree exceeded')
            op=LinearOperator((N,N),matvec=apply,dtype=float)
            seed=np.sin(np.arange(N)+.31);seed/=np.linalg.norm(seed)
            initial=w*seed if last is None else last+1e-3*seed
            ev,U=eigsh(op,k=3,which='LA',ncv=16,tol=2e-11,v0=initial)
            order=np.argsort(ev)[::-1];ev=ev[order];U=U[:,order]
            res=[float(np.linalg.norm(apply(U[:,i])-ev[i]*U[:,i])/ev[0]) for i in range(3)]
            assert max(res)<1e-9,res
            last=U@np.array([1.,.7,.5])
            x={'beta':b,'beta_L':'infinity' if not mul else b*mul,'multiplier':mul,'gap':float(np.log(ev[0]/ev[1])),'eigenvalues':ev.tolist(),'residuals':res,'matvecs':calls,'point_seconds':time.monotonic()-point_start}
            record['results'].append(x)
            if mul:
                ref=next(v['gap'] for v in record['results'] if v['beta']==b and v['multiplier']==0);x['difference']=x['gap']-ref
            else:x['difference']=0.
            record['seconds']=time.monotonic()-start;record['peak_RSS_bytes']=base.memory_check()
            out.write_text(json.dumps(record,indent=2)+'\n');print('VALUE',x,flush=True)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('action',choices=['build','run']);p.add_argument('--J',type=int,default=2);p.add_argument('--E',type=int,default=40);p.add_argument('--basis',type=Path,required=True);p.add_argument('--output',type=Path);a=p.parse_args()
    if a.action=='build':build(a.J,a.E,a.basis)
    else:run(a.basis,a.output)
