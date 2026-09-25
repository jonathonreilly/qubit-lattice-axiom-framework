"""Exact integer primitive and geometry controls, not a dynamical simulation."""
from collections import Counter, deque
from itertools import combinations, product
from pathlib import Path
import hashlib, json, time

def geometry(L):
    vertices=list(product(range(L),repeat=3)); index={x:i for i,x in enumerate(vertices)}
    A=[i for i,x in enumerate(vertices) if sum(x)%2==0]
    B=[i for i,x in enumerate(vertices) if sum(x)%2]
    def shift(x,d):
        y=list(x);y[d]=(y[d]+1)%L;return tuple(y)
    edges=[]
    for a in A:
        near=set()
        for d in range(3):
            for sign in (-1,1):
                y=list(vertices[a]);y[d]=(y[d]+sign)%L;near.add(index[tuple(y)])
        edges.extend((a,b) for b in sorted(near))
    edge_index={frozenset(e):i for i,e in enumerate(edges)}
    neighbors={v:[] for v in range(len(vertices))}
    for i,(a,b) in enumerate(edges):
        neighbors[a].append((b,i,1));neighbors[b].append((a,i,-1))
    def cycle(points):
        vec={}
        for x,y in zip(points,points[1:]+points[:1]):
            u,v=index[x],index[y];i=edge_index[frozenset((u,v))]
            vec[i]=vec.get(i,0)+(1 if edges[i][0]==u else -1)
        return {i:v for i,v in vec.items() if v}
    plaquettes={}
    for x in vertices:
        for i,j in combinations(range(3),2):
            v=cycle([x,shift(x,i),shift(shift(x,i),j),shift(x,j)])
            key=tuple(sorted(v.items()));negative=tuple((e,-f) for e,f in key)
            plaquettes[min(key,negative)]=v
    loops=list(plaquettes.values())
    winding=cycle([(x,0,0) for x in range(L)]) if L>2 else loops[0]
    for v in loops+[winding]:
        div=[0]*len(vertices)
        for e,x in v.items():a,b=edges[e];div[a]+=x;div[b]-=x
        assert not any(div)
    incidence=Counter(e for v in loops for e,c in v.items() for _ in range(c*c))
    z=3 if L==2 else 6;r=2 if L==2 else 4
    assert set(incidence.values())=={r} and len(incidence)==len(edges)
    assert all(len(neighbors[x])==z for x in neighbors)
    return dict(L=L,vertices=vertices,A=A,B=B,edges=edges,neighbors=neighbors,
                loops=loops,winding=winding,z=z,r=r)

def gauss(g,q,E):
    div=[0]*len(q)
    for (a,b),x in zip(g['edges'],E):div[a]+=x;div[b]-=x
    return div==[x-(i in g['A']) for i,x in enumerate(q)]

def flow(g,q):
    root=g['A'][0];parent={root:None};order=[root]
    for v in order:
        for u,e,s in g['neighbors'][v]:
            if u not in parent:parent[u]=(v,e,-s);order.append(u)
    subtotal=[x-(i in g['A']) for i,x in enumerate(q)];E=[0]*len(g['edges'])
    for v in reversed(order[1:]):
        u,e,s=parent[v];E[e]=s*subtotal[v];subtotal[u]+=subtotal[v]
    assert subtotal[root]==0 and gauss(g,q,E)
    return E

def electric(g,q,E):
    return sum(E[i]*(E[i]-q[a]) for i,(a,b) in enumerate(g['edges']) if q[b]==0)

def translated(E,v,sign=1):
    output=list(E)
    for e,k in v.items():output[e]+=sign*k
    return output

def response(g,q):
    return sum(2*sum(v*v for e,v in loop.items() if q[g['edges'][e][1]]==0)
               for loop in g['loops'])

def words(g):
    if g['L']==2:
        for ac in product((-1,1),repeat=len(g['A'])):
            for bc in product((-1,0,1),repeat=len(g['B'])):
                q=[0]*len(g['vertices'])
                for a,v in zip(g['A'],ac):q[a]=v
                for b,v in zip(g['B'],bc):q[b]=v
                if sum(q)==len(g['A']):yield q
    else:
        n=len(g['A'])
        for m in (0,2,4,n//2,n):
            q=[0]*len(g['vertices'])
            for a in g['A']:q[a]=1
            for b in g['B'][:m]:q[b]=1
            for a in g['A'][:m//2]:q[a]=-1
            assert sum(q)==n
            yield q

def primitive(g,q,E):
    """Actually execute F_a then j_(ab,sigma), checking every full output."""
    maps={};paths=0
    for a in g['A']:
        for b,eb,_ in g['neighbors'][a]:
            for sig in (-1,1):
                column=Counter()
                for c,ec,_ in g['neighbors'][a]:
                    if not q[a] or q[c]:continue
                    out=list(q);field=list(E);charge=out[a]
                    out[a]=0;out[c]=charge;field[ec]-=charge
                    assert gauss(g,out,field)
                    if out[a] or out[b]:continue
                    out[a]=sig;out[b]=-sig;field[eb]+=sig
                    assert all(out[x] for x in g['A']) and gauss(g,out,field)
                    assert sum(abs(x) for x in out)==sum(abs(x) for x in q)+2
                    assert response(g,out)-response(g,q)==-4*g['r']*g['z']
                    column[(tuple(out),tuple(field))]+=1;paths+=1
                maps[(a,b,sig)]=column
    resolved=sum(v*v for c in maps.values() for v in c.values())
    coherent=0
    for a in g['A']:
        for b,_,_ in g['neighbors'][a]:
            plus=maps[(a,b,1)];minus=maps[(a,b,-1)]
            assert not set(plus)&set(minus)
            both=plus+minus;coherent+=sum(v*v for v in both.values())
    assert resolved==coherent==paths
    return paths,resolved,coherent

def main():
    t=time.monotonic();rows=[];geometry_rows=[]
    for L in (2,4,6):
        g=geometry(L);qwords=list(words(g));n=len(g['A'])
        assert len(qwords)==(65 if L==2 else 5)
        geometry_rows.append({'side':L,'vertices':len(g['vertices']),'A_sites':n,
            'edges':len(g['edges']),'plaquettes':len(g['loops']),
            'edge_squared_incidence':g['r'],'degree':g['z'],
            'response_coefficient_in_K':2*g['r']*g['z'],
            'per_birth_decrement_in_K':4*g['r']*g['z'],
            'complete_charge_enumeration':L==2,'charge_words':len(qwords)})
        for wi,q in enumerate(qwords):
            m=sum(q[b]!=0 for b in g['B']);base=flow(g,q)
            assert response(g,q)==2*g['r']*g['z']*(n-m)
            second_differences=0;count=0;details=[]
            for winding_multiple in (-2,0,3):
                E=translated(base,g['winding'],winding_multiple)
                assert gauss(g,q,E);D=electric(g,q,E)
                for loop in g['loops']:
                    ep=translated(E,loop);em=translated(E,loop,-1)
                    assert gauss(g,q,ep) and gauss(g,q,em)
                    diff=electric(g,q,ep)+electric(g,q,em)-2*D
                    expected=2*sum(v*v for e,v in loop.items() if q[g['edges'][e][1]]==0)
                    assert diff==expected>=0;second_differences+=1
                # One flow suffices for all primitive columns; both nonzero
                # circulation controls still test the full electric identity.
                if winding_multiple==0:
                    count,resolved,coherent=primitive(g,q,E)
                details.append({'winding_multiple':winding_multiple,'D':D,
                    'electric_squared_norm':sum(e*e for e in E)})
            if m==0:assert count==2*n*g['z']*(g['z']-1)
            if m==n:assert count==0 and response(g,q)==0
            rows.append({'side':L,'word_index':wi,'charges':q,'B_occupied':m,
                'exact_response_in_K':response(g,q),'second_differences':second_differences,
                'primitive_paths':count,'resolved_loss_diagonal':resolved,
                'coherent_loss_diagonal':coherent,'flows':details})
    result={'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'scope':'Exact integer full-charge/Gauss/rotor and primitive-column checks; no finite-time simulation, microscopic response transfer or empirical identification.',
        'geometry':geometry_rows,'rows':rows,'all_assertions_passed':True,
        'second_difference_checks':sum(r['second_differences'] for r in rows),
        'primitive_paths_checked':sum(r['primitive_paths'] for r in rows),
        'elapsed_seconds':time.monotonic()-t}
    body=json.dumps(result,indent=2)+'\n'
    (Path(__file__).parent/'RESPONSE_SUM_RESULTS.json').write_text(body)
    print(body,end='')

if __name__=='__main__':main()
