#!/usr/bin/env python3
"""Exact small-patch test of ring plus nearest-neighbor exchange closure."""
from pathlib import Path
import datetime, hashlib, itertools, json, math
import sympy as s

HERE = Path(__file__).resolve().parent

def patch(shape):
    xyz=list(itertools.product(*(range(n) for n in shape)))
    index={x:i for i,x in enumerate(xyz)}
    edges=[]; loops=[]
    for x in xyz:
        for a in range(len(shape)):
            y=list(x);y[a]+=1
            if tuple(y) in index:edges.append((index[x],index[tuple(y)]))
        for a,b in itertools.combinations(range(len(shape)),2):
            y=list(x);y[a]+=1;z=list(y);z[b]+=1;w=list(x);w[b]+=1
            if all(tuple(v) in index for v in (y,z,w)):
                loops.append(tuple(index[tuple(v)] for v in (x,y,z,w)))
    black={i for i,x in enumerate(xyz) if sum(x)%2==0}
    return xyz,edges,loops,black

def matchings(n,edges):
    neighbors={x:[] for x in range(n)}
    for x,y in edges:neighbors[x].append(y);neighbors[y].append(x)
    def recurse(left,chosen):
        if not left:
            yield tuple(chosen);return
        x=min(left)
        for y in neighbors[x]:
            if y in left:yield from recurse(left-{x,y},chosen+[(x,y)])
    return list(recurse(set(range(n)),[]))

def main():
    out=HERE/'geometric_local_quantum_combination_checks';out.mkdir(exist_ok=False)
    rows=[]
    for shape in [(2,2),(2,3),(2,4),(2,2,2),(2,2,3)]:
        xyz,edges,loops,black=patch(shape);n=len(xyz);K=n//2
        states=[z for z in itertools.product((0,1),repeat=n) if sum(z)==K]
        state_index={z:i for i,z in enumerate(states)}
        covers=matchings(n,edges)
        D=s.zeros(len(states),len(covers))
        for j,cover in enumerate(covers):
            for i,z in enumerate(states):
                value=1
                for x,y in cover:
                    if x not in black:x,y=y,x
                    if z[x]==z[y]:value=0;break
                    value*=1 if z[x]==0 else -1
                D[i,j]=value
        G=D.T*D;assert G.rank()==len(covers)
        def act(permutation):
            A=s.zeros(*D.shape)
            for i,z in enumerate(states):
                target=[0]*n
                for x in range(n):target[permutation[x]]=z[x]
                A[state_index[tuple(target)],:]=D[i,:]
            return A
        NN=s.zeros(*D.shape);RR=s.zeros(*D.shape)
        for x,y in edges:
            p=list(range(n));p[x],p[y]=p[y],p[x];NN+=act(p)
        for square in loops:
            for sense in (-1,1):
                p=list(range(n))
                for j,x in enumerate(square):p[x]=square[(j+sense)%4]
                RR+=act(p)
        AN=G.inv()*D.T*NN;AR=G.inv()*D.T*RR
        LN=NN-D*AN;LR=RR-D*AR
        assert G*AN==AN.T*G and G*AR==AR.T*G
        where=next(((i,j) for i in range(LN.rows) for j in range(LN.cols) if LN[i,j]!=0),None)
        if where:
            i,j=where;alpha=-LR[i,j]/LN[i,j]
            residual=LR+alpha*LN
            closes=residual==s.zeros(*residual.shape)
            counter=next(([a,b,str(LR[a,b]),str(LN[a,b]),str(residual[a,b])]
                          for a in range(residual.rows) for b in range(residual.cols)
                          if residual[a,b]!=0),None)
        else:
            alpha=None;residual=LR;closes=LR==s.zeros(*LR.shape);counter=None
        rows.append(dict(shape=shape,sites=n,degree_range=[min(sum(x in e for e in edges) for x in range(n)),max(sum(x in e for e in edges) for x in range(n))],
          singlet_covers=len(covers),magnetization_zero_dimension=len(states),
          NN_leakage_rank=LN.rank(),ring_leakage_rank=LR.rank(),
          NN_squared_Frobenius_leakage=str(s.trace(LN.T*LN)/2**K),
          ring_squared_Frobenius_leakage=str(s.trace(LR.T*LR)/2**K),
          cancellation_coefficient_for_ring_plus_alpha_NN=str(alpha) if alpha is not None else 'unrestricted if ring already closes',
          exact_subspace_closure=closes,
          remaining_squared_Frobenius_leakage=str(s.trace(residual.T*residual)/2**K),
          counter_entry=counter,
          coefficient_matrix=str(AR+alpha*AN) if closes and alpha is not None else None))
        print(json.dumps({k:v for k,v in rows[-1].items() if k!='coefficient_matrix'}),flush=True)
    ans=dict(created_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
             source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),rows=rows,
             scope='Open rectangular finite patches, exactly rational computations. No infinite cubic closure, gap, prepared state, or photon theorem.')
    (out/'RESULTS.json').write_text(json.dumps(ans,indent=2)+'\n')

if __name__=='__main__':main()
