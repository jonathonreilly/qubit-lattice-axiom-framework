#!/usr/bin/env python3
"""All eight reflection sectors of the same cube operator. GUIDE computation."""
from cube import *
from exponential import taylor

def actions():
    perm=[];reverse=[];odd=[]
    for g in range(8):
        vp=[(4*(1-v//4) if g&4 else 4*(v//4))+(((-v%4) if g&2 else v%4)+2*(g&1))%4 for v in range(8)]
        ep=[];rev=[]
        for u,v in EDGES:
            a,b=vp[u],vp[v]
            dest=next(e for e,(c,d) in enumerate(EDGES) if {a,b}=={c,d})
            ep.append(dest);rev.append(int(EDGES[dest]!=(a,b)))
        parity=[]
        for v in range(8):
            positions=[list(VE[vp[v]]).index(ep[e]) for e in VE[v]]
            parity.append(sum(positions[i]>positions[j] for i in range(3) for j in range(i+1,3))%2)
        perm.append(ep);reverse.append(rev);odd.append(parity)
    return np.array(perm),np.array(reverse),np.array(odd)

@njit
def mapped(row,g,perms,revs,odds,VE,B):
    new=np.empty(12,np.int16);exponent=0
    for e in range(12):new[perms[g,e]]=row[e];exponent+=revs[g,e]*row[e]
    for v in range(8):
        if odds[g,v]:exponent+=(row[VE[v,0]]+row[VE[v,1]]+row[VE[v,2]])//2
    key=0
    for e in range(12):key=key*B+new[e]
    return key,1 if exponent%2==0 else -1

@njit
def orbit_data(rows,perms,revs,odds,VE,B):
    keys=make_keys(rows,B);mins=keys.copy();gs=np.zeros(len(rows),np.int8);phases=np.ones(len(rows),np.int8)
    for i in range(len(rows)):
      for g in range(1,8):
        key,phase=mapped(rows[i],g,perms,revs,odds,VE,B)
        if key<mins[i]:mins[i]=key;gs[i]=g;phases[i]=phase
    return keys,mins,gs,phases

@njit
def allowed_sectors(reps,repkeys,perms,revs,odds,VE,B,characters):
    allowed=np.ones((8,len(reps)),np.bool_)
    for i in range(len(reps)):
      for g in range(8):
        key,phase=mapped(reps[i],g,perms,revs,odds,VE,B)
        if key==repkeys[i]:
          for c in range(8):
            if characters[c,g]*phase!=1:allowed[c,i]=False
    return allowed

@njit
def sector_entries(keys,reps,orbit,sizes,gs,phases,allowed,chars,J,H,table,VE,faces,signs,capacity):
    pos=np.full(len(reps),-1,np.int32);nr=0
    for i in range(len(reps)):
      if allowed[i]:pos[i]=nr;nr+=1
    rr=np.empty(capacity,np.int32);cc=np.empty_like(rr);vv=np.empty(len(rr));n=0
    B=2*J+2
    for oi in range(len(reps)):
      if not allowed[oi]:continue
      old=reps[oi]
      for fi in range(6):
       face=faces[fi]
       for mask in range(16):
        new=old.copy();ok=True;factor=signs[fi]*.5
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
          if changed:factor*=table[v//4,unchanged,old[VE[v,0]],old[VE[v,1]],old[VE[v,2]],code]
        if abs(factor)<1e-15:continue
        key=0
        for e in range(12):key=key*B+new[e]
        loc=np.searchsorted(keys,key)
        if loc>=len(keys) or keys[loc]!=key:continue
        oj=orbit[loc]
        if not allowed[oj]:continue
        factor*=math.sqrt(sizes[oi]/sizes[oj])*phases[loc]*chars[gs[loc]]
        if capacity:
          rr[n]=pos[oj];cc[n]=pos[oi];vv[n]=factor
        n+=1
    return rr,cc,vv,n

def build_sym(J,H,E,dest):
    start=time.monotonic();N,rows=enumerate_basis(J,H,True,E);print('FULL_BASIS',N,flush=True)
    perms,revs,odds=actions();characters=np.array([[(-1)**((c&g).bit_count()) for g in range(8)] for c in range(8)])
    keys,mins,gs,phases=orbit_data(rows,perms,revs,odds,VE,2*J+2)
    assert np.all(keys[1:]>keys[:-1])
    repindices=np.flatnonzero(keys==mins);reps=rows[repindices];repkeys=keys[repindices]
    orbit=np.searchsorted(repkeys,mins);sizes=np.bincount(orbit);del mins
    allowed=allowed_sectors(reps,repkeys,perms,revs,odds,VE,2*J+2,characters)
    assert sum(np.sum(allowed,axis=1))==N
    print('SECTOR_SIZES',np.sum(allowed,axis=1).tolist(),flush=True)
    del rows,repindices
    L=2*J+1;tab=np.zeros((2,3,L,L,L,4))
    triples=[(a,b,c) for a in range(J+1) for b in range(J+1) for c in range(2*J+1) if base.triangle(a,b,c)]
    for oriidx,ori in enumerate((ORIENT[0],ORIENT[4])):
      for old in triples:
       for un in range(3):
        changed=[i for i in range(3) if i!=un]
        for code in range(4):
          new=list(old)
          for k,i in enumerate(changed):new[i]+=1 if (code>>k)&1 else -1
          if base.triangle(*new):tab[oriidx,un,*old,code]=vertex(old,tuple(new),un,ori)
    import gc
    inv.cache_clear();vertex.cache_clear();base.cg.cache_clear();gc.collect()
    dest.mkdir(exist_ok=True)
    diagnostics=[]
    for c in range(8):
        args=(keys,reps,orbit,sizes,gs,phases,allowed[c],characters[c],J,H,tab,VE,np.array(FACES),np.array([face_sign(f) for f in FACES]))
        _,_,_,capacity=sector_entries(*args,0)
        rr,cc,vv,used=sector_entries(*args,capacity)
        assert used==capacity
        sectorrows=reps[allowed[c]];X=csr_matrix((vv,(rr,cc)),shape=(len(sectorrows),len(sectorrows)));del rr,cc,vv
        XT=X.T.tocsr();asym=0.
        for first in range(0,len(sectorrows),10000):
            diff=X[first:first+10000]-XT[first:first+10000]
            if diff.nnz:asym=max(asym,float(np.max(np.abs(diff.data))))
        del XT,diff
        assert asym<2e-12,(c,asym)
        save_npz(dest/f'sector{c}.npz',X,compressed=False);np.save(dest/f'rows{c}.npy',sectorrows)
        diagnostics.append({'sector':c,'N':len(sectorrows),'nnz':X.nnz,'asymmetry':asym});print('SECTOR',diagnostics[-1],flush=True)
        del X;base.memory_check()
    (dest/'meta.json').write_text(json.dumps(dict(J=J,H=H,E=E,N=N,sectors=diagnostics,seconds=time.monotonic()-start,peak_RSS_bytes=base.memory_check()),indent=2)+'\n')

def run_sym(dest,betas,mults,out,sectors):
    start=time.monotonic();results=[];prior_seconds=0.;prior_rss=0
    if out.exists():
        prior=json.loads(out.read_text())
        assert prior['basis']==str(dest),'refuse to mix basis cutoffs'
        results=prior['results'];prior_seconds=prior.get('seconds',0.);prior_rss=prior.get('peak_RSS_bytes',0)
        print('RESUMING',len(results),'saved spectra',flush=True)
    completed={(x['sector'],x['beta'],x['multiplier']) for x in results}
    for c in sectors:
      X=load_npz(dest/f'sector{c}.npz');rows=np.load(dest/f'rows{c}.npy');last=None
      from scipy.sparse import eye
      for b in betas:
        shift=6*b
        r=base.ratios(b,int(rows[:,:8].max()));kh=np.prod(r[rows[:,:8]],axis=1)
        for mul in mults:
          if (c,b,mul) in completed:continue
          kv=np.ones(len(rows)) if mul==0 else np.all(rows[:,8:]==0,axis=1).astype(float) if mul==-1 else np.prod(base.ratios(b*mul,int(rows[:,8:].max()))[rows[:,8:]],axis=1)
          w=np.sqrt(kh*kv)
          def apply(x):return w*taylor(X,b,w*x)
          op=LinearOperator((len(rows),len(rows)),matvec=apply)
          k=3 if c==0 else 1
          tolerance=3e-11 if c==0 else 1e-8
          seed=np.linspace(.9,1.1,len(rows));seed/=np.linalg.norm(seed)
          initial=seed if last is None else last/np.linalg.norm(last)+1e-3*seed
          ev,U=eigsh(op,k=k,which='LA',tol=tolerance,ncv=12 if c==0 else 8,v0=initial)
          order=np.argsort(ev)[::-1];ev=ev[order];U=U[:,order]
          last=U@np.linspace(1.,.6,k)
          residual=float(np.linalg.norm(apply(U[:,0])-ev[0]*U[:,0])/ev[0])
          item=dict(beta=b,multiplier=mul,beta_L='infinity' if mul==0 else 0.0 if mul==-1 else b*mul,sector=c,eigenvalues=ev.tolist(),residual=residual,solver_tolerance=tolerance)
          results.append(item);print('VALUE',json.dumps(item),flush=True)
          temporary=out.with_suffix(out.suffix+'.tmp')
          temporary.write_text(json.dumps(dict(grade='GUIDE',exponential='scaled Taylor, final Poisson term below 1e-20',basis=str(dest),results=results,seconds=prior_seconds+time.monotonic()-start,peak_RSS_bytes=max(prior_rss,base.memory_check())),indent=2)+'\n')
          temporary.replace(out)
      del X,rows

def main():
 p=argparse.ArgumentParser();p.add_argument('action',choices=['build','run']);p.add_argument('--J',type=int,default=6);p.add_argument('--H',type=int,default=48);p.add_argument('--E',type=int,default=100000);p.add_argument('--basis',type=Path,required=True);p.add_argument('--betas',type=float,nargs='+',default=[2.4]);p.add_argument('--mults',type=float,nargs='+',default=[0,8,4,2,1]);p.add_argument('--sectors',type=int,nargs='+',default=list(range(8)));p.add_argument('--output',type=Path);a=p.parse_args()
 if a.action=='build':build_sym(a.J,a.H,a.E,a.basis)
 else:run_sym(a.basis,a.betas,a.mults,a.output,a.sectors)
if __name__=='__main__':main()
