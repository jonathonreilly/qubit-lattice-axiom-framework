"""Complete physical cube spin builders and exact first-sector path controls.

Reusable functions are guarded from output-writing execution. No ring flat
frame or asymptotic dispersive assumption enters these controls.
"""

AUDIT_TIMEOUT_SEC = 3600
AUDIT_INPUT_PATHS = ('scripts/cube_physical_controls.py', 'scripts/second_event_probe.py')
from pathlib import Path
from itertools import product,combinations
from collections import defaultdict
from functools import lru_cache
import importlib.util,hashlib,json,math
import numpy as np
import scipy.sparse as sparse
import sympy as sym
D=Path(__file__).resolve().parent
parent=D/'second_event_probe.py'
assert hashlib.sha256(parent.read_bytes()).hexdigest()=='c003d9b3de6c0e541e6639d8e5209a261e68002707e253bdb5c2fdada0caff9a'
spec=importlib.util.spec_from_file_location('physical_paths',parent)
paths=importlib.util.module_from_spec(spec);spec.loader.exec_module(paths)
edges,aset=paths.graph('cube');tree=[(0,1),(0,2),(0,4),(1,3),(1,5),(2,6),(3,7)]
ti=[edges.index(e) for e in tree];ci=[j for j,e in enumerate(edges) if e not in tree]
inc=sym.zeros(8,12)
for e,(u,v) in enumerate(edges):inc[u,e]=1;inc[v,e]=-1
inverse=inc.extract(range(1,8),ti).inv()
assert abs(inc.extract(range(1,8),ti).det())==1
cycle=np.zeros((12,5),dtype=np.int64)
cycle[ci,:]=np.eye(5,dtype=np.int64)
cycle[ti,:]=np.array(-inverse*inc.extract(range(1,8),ci),dtype=np.int64)
assert np.array_equal(np.array(inc,dtype=np.int64)@cycle,np.zeros((8,5),dtype=np.int64))
background=np.array([int(i in aset) for i in range(8)],dtype=np.int64)

def grade(q):return sum(q[a]==0 for a in aset)

@lru_cache(None)
def offset(q):
    E=np.zeros(12,dtype=np.int64)
    E[ti]=np.array(inverse*sym.Matrix((np.array(q)-background)[1:]),dtype=np.int64).ravel()
    assert np.array_equal(np.array(inc,dtype=np.int64)@E,np.array(q)-background)
    return E

@lru_cache(None)
def hop_table(q):
    rows=[]
    for qq,delta in paths.legal_hops(q,edges):
        assert paths.gauss_difference(q,qq,delta,edges)
        e=next(j for j,x in enumerate(delta) if x)
        rows.append((qq,tuple(delta[j] for j in ci),e,delta[e]))
    return rows

@lru_cache(None)
def birth_table(q):
    rows=[]
    for e in range(12):
        for sigma in [-1,1]:
            out=paths.create(q,edges,e,sigma)
            if out:
                qq,delta=out;assert paths.gauss_difference(q,qq,delta,edges)
                rows.append((qq,tuple(delta[j] for j in ci),e,sigma))
    return rows

def states(number,w,S):
    fs=np.array(list(product(range(-S,S+1),repeat=5)),dtype=np.int64)
    common=fs@cycle.T;words=[];fieldrows=[]
    for q in paths.charges(number):
        if grade(q)!=w:continue
        Es=common+offset(q)
        mask=np.all(abs(Es)<=S,axis=1)
        for f,E in zip(fs[mask],Es[mask]):
            words.append((q,tuple(int(x) for x in f)));fieldrows.append(E)
    return words,np.array(fieldrows,dtype=np.int64)

def weight(E,k,S):
    if not -S<=E+k<=S:return 0.
    return math.sqrt(max(0.,1-E*(E+k)/(S*(S+1))))

def hops(source,target,S):
    words,fields=source;ix={s:i for i,s in enumerate(target[0])};rr=[];cc=[];vv=[]
    for j,((q,f),E) in enumerate(zip(words,fields)):
        for qq,df,e,k in hop_table(q):
            to=(qq,tuple(a+b for a,b in zip(f,df)));i=ix.get(to)
            if i is None:continue
            v=weight(int(E[e]),k,S)
            if v:rr.append(i);cc.append(j);vv.append(-v)
    return sparse.csc_matrix((vv,(rr,cc)),shape=(len(target[0]),len(words)))

def jumps(source,target,S):
    words,fields=source;ix={s:i for i,s in enumerate(target[0])}
    data={(e,sigma):([],[],[]) for e in range(12) for sigma in [-1,1]}
    for j,((q,f),E) in enumerate(zip(words,fields)):
        for qq,df,e,k in birth_table(q):
            i=ix.get((qq,tuple(a+b for a,b in zip(f,df))))
            if i is None:continue
            v=weight(int(E[e]),k,S)
            if v:
                rr,cc,vv=data[e,k];rr.append(i);cc.append(j);vv.append(v)
    return {key:sparse.csc_matrix((vv,(rr,cc)),shape=(len(target[0]),len(words)))
            for key,(rr,cc,vv) in data.items()}

def exact_first_paths():
    q0=tuple(int(a in aset) for a in range(8));zero=(0,)*12
    def hop(v,w):
        result=defaultdict(int)
        for (q,E),amp in v.items():
            for qq,delta in paths.legal_hops(q,edges):
                if grade(qq)==w:result[qq,paths.add(E,delta)]-=amp
        return {s:a for s,a in result.items() if a}
    seed={(q0,zero):1}
    M={s:-a for s,a in hop(hop(seed,1),0).items()}
    assert M=={(q0,zero):-12}
    zz=seed
    for w in [1,2,1,0]:zz=hop(zz,w)
    h4={s:sym.Rational(-a,2) for s,a in zz.items()}
    h4[q0,zero]+=144
    expected={(q0,zero):sym.Integer(60)};facewords=[]
    for fixedbit in range(3):
        moving=[b for b in range(3) if b!=fixedbit]
        for value in [0,1]:
            a=value<<fixedbit;b=a^(1<<moving[0]);c=b^(1<<moving[1]);d=a^(1<<moving[1])
            shift=[0]*12
            for u,v in [(a,b),(b,c),(c,d),(d,a)]:
                e=edges.index((min(u,v),max(u,v)));shift[e]+=1 if u<v else -1
            assert np.array_equal(np.array(inc,dtype=int)@np.array(shift),np.zeros(8,dtype=int))
            facewords.append(shift)
            expected[q0,tuple(shift)]=-2;expected[q0,tuple(-x for x in shift)]=-2
    assert h4==expected
    return {'H2_diagonal':-12,'H4_diagonal':60,'ZdaggerZ_diagonal':zz[q0,zero],
            'face_shifts':facewords,'H4_face_coefficient':-2,'total_H4_Laurent_terms':len(h4)}

def controls():
    rows=[]
    for S in [1,2]:
        p4=states(4,0,S);q4=states(4,1,S)
        p6=states(6,0,S);q6=states(6,1,S);r6=states(6,2,S);p8=states(8,0,S)
        A4=hops(p4,q4,S);M4=A4.T@A4
        E2=np.sum(p4[1]**2,axis=1)
        identity=M4-sparse.diags(12-E2/(S*(S+1)))
        error=float(max(abs(identity.data),default=0.));assert error<2e-13
        j4=jumps(q4,p6,S);B4={k:-v@A4 for k,v in j4.items()}
        G4=sum(b.T@b for b in B4.values()).tocsc()
        G4off=G4-sparse.diags(G4.diagonal());G4off.eliminate_zeros()
        assert G4off.nnz==0 and min(G4.diagonal())>=-1e-14 and max(G4.diagonal())<=48+1e-12
        seedindex=p4[0].index((tuple(int(a in aset) for a in range(8)),(0,)*5))
        assert abs(G4[seedindex,seedindex]-48)<1e-12
        A=hops(p6,q6,S);R=hops(q6,r6,S);js=jumps(q6,p8,S)
        jgram=sum(j.T@j for j in js.values()).tocsc()
        off=jgram-sparse.diags(jgram.diagonal());off.eliminate_zeros()
        assert off.nnz==0 and max(jgram.diagonal())<=2+1e-12
        assert max(np.diff(A.tocsc().indptr),default=0)<=6
        assert max(np.diff(A.tocsr().indptr),default=0)<=3
        assert max(np.diff(R.tocsc().indptr),default=0)<=3
        assert max(np.diff(R.tocsr().indptr),default=0)<=6
        cross=max((float(max(abs((js[e,1].T@js[e,-1]).data),default=0.)) for e in range(12)))
        assert cross==0
        rows.append({'S':S,'dimensions':{'P4':len(p4[0]),'Q4':len(q4[0]),'P6':len(p6[0]),'Q6':len(q6[0]),'R6':len(r6[0]),'P8':len(p8[0])},
                     'first_electric_identity_max_error':error,'first_loss_diagonal_range':[float(min(G4.diagonal())),float(max(G4.diagonal()))],
                     'first_zero_field_loss':float(G4[seedindex,seedindex]),
                     'P6_to_Q6_max_column_entries':int(max(np.diff(A.tocsc().indptr))),
                     'P6_to_Q6_max_row_entries':int(max(np.diff(A.tocsr().indptr))),
                     'Q6_to_R6_max_column_entries':int(max(np.diff(R.tocsc().indptr))),
                     'Q6_to_R6_max_row_entries':int(max(np.diff(R.tocsr().indptr))),
                     'next_bare_creation_gram_range':[float(min(jgram.diagonal())),float(max(jgram.diagonal()))],
                     'coherent_resolved_cross_gram_max':cross})
        print(json.dumps(rows[-1]),flush=True)
    return rows

def main():
    out={'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
         'exact_rotor_first_sector':exact_first_paths(),'complete_spin_operator_controls':controls(),
         'scope':'Finite complete physical spin matrices corroborate exact combinatorial bounds. No finite-window limiting dynamics inferred numerically.'}
    p=D/'CUBE_LOCAL_LIMIT_CONTROLS.json';assert not p.exists();p.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))
if __name__=='__main__':main()
