"""Full-output original center loss on the closed first translation component.

Only the input/final D0 block is compressed. No P0 is inserted between B* and B.
The identity Gamma_a=2(5-o)F_a*F_a includes all original birth outputs.
"""
from collections import Counter
from pathlib import Path
import hashlib,json,sqlite3,time
import numpy as np
from scipy import sparse
import cubic_one_pair_primitives_2026_09_26 as m
from cubic_closed_quotient_2026_09_26 import canonical

def decode(raw):
    return m.pack({tuple(v):q for v,q in raw[0]},
                  {(tuple(a),tuple(b)):e for (a,b),e in raw[1]})

def hazard_row(state):
    q,_=m.unpack(state)
    occupied={v for v,c in q.items() if not m.even(v) and c}
    assert len(occupied)==2
    active={a for b in occupied for a in m.nb(b)}
    out=Counter();diagonal=0
    for a in sorted(active):
        o=sum(b in occupied for b in m.nb(a));weight=2*(5-o)
        diagonal+=weight*(6-o)-60
        for t,_ in m.outgoing(state,a):
            for y,_ in m.incoming(t,a):
                if y!=state and m.cost(y)==0:out[y]+=weight
    b,c=sorted(occupied)
    assert diagonal==-240+4*len(set(m.nb(b))&set(m.nb(c)))
    return diagonal,out

def calculate(work):
    work=Path(work);start=time.monotonic()
    con=sqlite3.connect('file:'+str(work/'quotient-closed.sqlite3')+'?mode=ro&immutable=1',uri=True)
    words=[decode(json.loads(raw)) for raw, in con.execute('select word from states order by id')]
    con.close();idx={s:i for i,s in enumerate(words)};n=len(words)
    records=[];diagonal=[]
    for i,s in enumerate(words):
        d,col=hazard_row(s);diagonal.append(d)
        for y,c in col.items():
            word,tau=canonical(y)
            assert word in idx,('missing original-loss target',i,word)
            records.append((i,idx[word],*tau,c))
    entries=Counter(records);assert entries and max(entries.values())==1
    for a,b,x,y,z,c in records:assert entries[b,a,-x,-y,-z,c]==1
    arr=np.array(records,dtype=np.int64);src,dst,tau,coeff=arr[:,0],arr[:,1],arr[:,2:5],arr[:,5]
    diag=np.array(diagonal,dtype=np.int64);off=np.zeros(n,dtype=np.int64)
    np.add.at(off,dst,np.abs(coeff))
    bound=int(np.max(abs(diag)+off));lo=int(np.min(diag-off));hi=int(np.max(diag+off))
    assert n==11322 and len(records)==118092 and bound==684 and (lo,hi)==(-684,212)
    assert np.max(np.abs(tau))==2
    out=work/'projected_hazard.npz'
    np.savez_compressed(out,src=src,dst=dst,tau=tau,coefficient=coeff,diagonal=diag)
    data=np.load(work/'closed_quotient_operator.npz')
    G0=sparse.coo_matrix((coeff,(dst,src)),shape=(n,n)).tocsr()+sparse.diags(diag,dtype=np.int64)
    initial={}
    for name,expected in [('first_minus',-1164/5),('first_plus',-1044/5),('first_coherent',-1104/5)]:
        v=data[name];value=float(np.vdot(v,G0@v).real)
        assert abs(value-expected)<1e-10;initial[name]=value
    result={'dimension':n,'directed_displacement_entries':len(records),'missing_targets':0,
            'reverse_displacement_Hermiticity':True,'absolute_full_stencil_bound':bound,
            'exact_uniform_Gershgorin_range':[lo,hi], 'maximum_anchor_jump':2,
            'initial_excess':initial,'diagonal_histogram':dict(Counter(map(int,diag))),
            'seconds':time.monotonic()-start,
            'scope':'exact integer original-loss stencil and numerical normalization checks; not a detector identity'}
    (work/'ORIGINAL_HAZARD_RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result),flush=True)
    return result
