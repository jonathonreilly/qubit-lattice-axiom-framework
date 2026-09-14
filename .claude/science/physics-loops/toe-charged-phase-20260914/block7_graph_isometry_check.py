#!/usr/bin/env python3
"""Explicit signed local Clifford edge-addition tests; author checks only."""
from pathlib import Path
import runpy,copy,json
from itertools import product
import numpy as np
base=runpy.run_path(str(Path(__file__).with_name('block7_encoding_check.py')))
P=base['P'];Graph=base['Graph'];mul=base['mul'];dense=base['dense'];reduce_rows=base['reduce_rows'];remainder=base['remainder']

def controlled_conj(row,control,S):
    assert not S.support()>>control&1
    a=row.anti(S);b=row.x>>control&1
    out=row@(S if b else P())@(P(z=1<<control) if a else P())
    return P((out.p+2*a*b)%4,out.x,out.z)

def cz_conj(row,e,f):
    a=row.x>>e&1;b=row.x>>f&1
    return P((row.p+2*a*b)%4,row.x,row.z^(a<<f)^(b<<e))

def permutation(row,mapping):
    x=z=0
    for i,j in enumerate(mapping):
        if row.x>>i&1:x|=1<<j
        if row.z>>i&1:z|=1<<j
    return P(row.p,x,z)

def append_edge(g,u,v,kind='refbond'):
    assert frozenset((u,v)) not in g.eid
    e=len(g.edges);g.eid[frozenset((u,v))]=e;g.edges.append((u,v,kind));g.inc[u].append(e);g.inc[v].append(e)
    return e

def conjugate_word(row,word):
    for control,S in word:row=controlled_conj(row,control,S)
    return row

def edge_add(g,u,v,path):
    assert path[0]==u and path[-1]==v and len(set(path))==len(path)
    L=P((len(path)-2)%4)@mul(g.A(a,b) for a,b in zip(path,path[1:]))
    assert L==L.dag() and L@L==P()
    S=P(0 if u<v else 2)@g.B(u)@g.B(v)@L
    assert S==S.dag() and S@S==P()
    oldAs=[g.A(a,b) for a,b,_ in g.edges];oldBs=[g.B(a) for a in range(len(g.v))]
    assert all(not S.anti(A) for A in oldAs)
    assert [i for i,B in enumerate(oldBs) if S.anti(B)]==sorted((u,v))
    e=append_edge(g,u,v)
    for a,A in enumerate(oldAs):
        x,y,_=g.edges[a];assert controlled_conj(A,e,S)==g.A(x,y)
    for a,B in enumerate(oldBs):assert controlled_conj(B,e,S)==g.B(a)
    newcycle=g.A(u,v)@L
    assert controlled_conj(P(x=1<<e),e,S)==newcycle
    # Pulling the new A back yields X_e times the old path pair.
    assert controlled_conj(g.A(u,v),e,S)==P(x=1<<e)@L
    return e,S

def dense_checks():
    CZ=np.diag([1,1,1,-1])
    for x in range(4):
        for z in range(4):
            row=P(0,x,z)
            assert np.array_equal(CZ@dense(row,2)@CZ,dense(cz_conj(row,0,1),2))
    g=Graph([(0,0,0),(1,0,0),(2,0,0)],q=1,refs=False)
    e,S=edge_add(g,0,2,[0,1,2]);assert e==2
    Id=np.eye(1<<e);Sm=dense(S,e);zero=np.zeros_like(Id);U=np.block([[Id,zero],[zero,Sm]])
    assert np.array_equal(U.conj().T@U,np.eye(1<<(e+1)))
    for x in range(1<<(e+1)):
        for z in range(1<<(e+1)):
            row=P(0,x,z)
            assert np.array_equal(U@dense(row,e+1)@U, dense(controlled_conj(row,e,S),e+1))
    # Independent product of controlled one-qubit Paulis, plus a control Z sign.
    factors=[];Y_count=(S.x&S.z).bit_count();sign=(S.p-Y_count)%4;assert sign in (0,2)
    if sign:factors.append(dense(P(z=1<<e),e+1))
    for k in range(e):
        xb=S.x>>k&1;zb=S.z>>k&1
        if not xb and not zb:continue
        Q=dense(P(int(xb and zb),xb<<k,zb<<k),e)
        factors.append(np.block([[Id,zero],[zero,Q]]))
    V=np.eye(1<<(e+1),dtype=complex)
    for f in factors:V=f@V
    assert np.array_equal(V,U)
    return {'old_edge_qubits':2,'new_edge_qubits':3,'all_Pauli_conjugations':64,'controlled_Pauli_weight':S.weight()}

def build_map(cells):
    old=Graph(cells);g=copy.deepcopy(old);target=Graph(sorted(cells),refbonds=True)
    old_edges=len(g.edges);word=[];maxS=0;bycolor={}
    streams=sorted(g.streams,key=lambda st:((st[1]//2,)+tuple(x%3 for x in st[0]),st[0]))
    for c,a,d,b in streams:
        color=(a//2,)+tuple(x%3 for x in c)
        u,v=g.vid[c,6],g.vid[d,6];path=[u,g.vid[c,a],g.vid[d,b],v]
        prev=sum(g.edges[e][2]=='refbond' for w in (u,v) for e in g.inc[w])
        e,S=edge_add(g,u,v,path)
        assert S.weight()==13-a-b+prev,(S.weight(),a,b,prev)
        assert S.weight()<=22
        maxS=max(maxS,S.weight());word.append((e,S));bycolor.setdefault(color,[]).append(S.support()|(1<<e))
    for color,supports in bycolor.items():
        seen=0
        for support in supports:assert not support&seen,(color,'parallel overlap');seen|=support
    vertex_map=[target.vid[v] for v in g.v]
    mapping=[target.eid[frozenset((vertex_map[u],vertex_map[v]))] for u,v,_ in g.edges]
    orientation_mask=sum(1<<mapping[e] for e,(u,v,_) in enumerate(g.edges) if (u<v)!=(vertex_map[u]<vertex_map[v]))
    gauges=[];maxinv=0
    for vertex in range(len(g.v)):
        sequence=[mapping[e] for e in g.inc[vertex]]
        inv=[(sequence[i],sequence[j]) for i in range(len(sequence)) for j in range(i+1,len(sequence)) if sequence[i]>sequence[j]]
        if g.v[vertex][1]!=6:assert not inv
        assert len(inv)<=15
        maxinv=max(maxinv,len(inv));gauges.extend(inv)
    def gauge(row):
        row=permutation(row,mapping)
        for e,f in gauges:row=cz_conj(row,e,f)
        return P((row.p+2*(row.x&orientation_mask).bit_count())%4,row.x,row.z)
    def image(row):return gauge(conjugate_word(row,word))
    for u,v,_ in g.edges:assert gauge(g.A(u,v))==target.A(vertex_map[u],vertex_map[v])
    for u in range(len(g.v)):assert gauge(g.B(u))==target.B(vertex_map[u])
    oldX,oldZ,oldD=old.loaders();targetX,targetZ,targetD=target.loaders()
    for i,c in enumerate(old.cells):
        j=target.cells.index(c)
        for a in range(6):
            assert image(oldX[6*i+a])==targetX[6*j+a]
            assert image(oldZ[6*i+a])==targetZ[6*j+a]
        assert image(oldD[i])==targetD[j]
    targetPiv=reduce_rows(target.cycles()+targetD,len(target.edges))
    inputRows=old.cycles()+oldD+[P(x=1<<e) for e in range(old_edges,len(g.edges))]
    outRows=[image(r) for r in inputRows]
    assert len(reduce_rows(outRows,len(target.edges)))==len(targetPiv)
    for r in outRows:assert remainder(r,targetPiv,len(target.edges))==P()
    # All-B vacuum is transported, so the logical-X images fix all matter phases.
    for u in range(len(old.v)):assert image(old.B(u))==target.B(vertex_map[u])
    # Deletion witnesses: each omitted controlled Pauli loses its cycle character.
    active=0
    for j,(e,S) in enumerate(word):
        cut=word[:j]+word[j+1:]
        row=gauge(conjugate_word(P(x=1<<e),cut))
        active+=remainder(row,targetPiv,len(target.edges))!=P()
    assert active==len(word)
    return {'cells':len(cells),'old_qubits':old_edges,'new_qubits':len(target.edges),'returned_plus_inputs':len(word),'logical_qubits':len(oldX),'maximum_controlled_Pauli_weight':maxS,'colors_used':len(bycolor),'incidence_CZ_gates':len(gauges),'orientation_Z_gates':orientation_mask.bit_count(),'max_incidence_inversions_at_vertex':maxinv,'deleted_edge_maps_detected':active}

if __name__=='__main__':
    print('CHECK dense_edge_addition',json.dumps(dense_checks()),flush=True)
    for label,cells in [('square',[(0,0,0),(1,0,0),(1,1,0),(0,1,0)]),('cube2',list(product(range(2),repeat=3))),('cube3',list(product(range(3),repeat=3))),('cube4',list(product(range(4),repeat=3)))]:
        print('CHECK local_Clifford_graph_map',label,json.dumps(build_map(cells)),flush=True)
    print('ALL_BLOCK7_GRAPH_ISOMETRY_CHECKS_PASS')
