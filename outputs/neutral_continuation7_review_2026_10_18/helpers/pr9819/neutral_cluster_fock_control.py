"""Exact sparse aligned-column motif algebra, not a microscopic eigensolve."""
AUDIT_TIMEOUT_SEC=300
import cmath,json,math
from collections import defaultdict

def control(R):
    def idx(x,y):return (x%R)*R+y%R
    def syndrome(cols):
        z=0
        for x,y in cols:
            for dx,dy in [(0,0),(-1,0),(0,-1),(-1,-1)]:z^=1<<idx(x+dx,y+dy)
        return z
    motifs=[]; incoming=defaultdict(set)
    for x in range(R):
      for y in range(R):
       for dx,dy in [(1,0),(0,1)]:
        s=syndrome([(x,y),(x+dx,y+dy)]);sites=[i for i in range(R*R) if s>>i&1]
        F=0
        for i in sites:
         u,v=divmod(i,R)
         for a in range(-2,3):
          for b in range(-2,3):
           if abs(a)+abs(b)<=2:F|=1<<idx(u+a,v+b)
        a=len(motifs);motifs.append((s,F,x,y))
        for i in sites:incoming[i].add(a)
    modes=[[cmath.exp(2j*math.pi*k*x/R)/(R*math.sqrt(2)) for s,F,x,y in motifs] for k in [0,1]]
    def create(state,f):
        out=defaultdict(complex)
        for C,v in state.items():
          for a,(s,F,_,_) in enumerate(motifs):
            if not C&F:out[C|s]+=v*f[a]
        return dict(out)
    def lower(state,f):
        out=defaultdict(complex)
        for C,v in state.items():
          candidates=set();bits=C
          while bits:
            b=bits&-bits;bits-=b;candidates.update(incoming[b.bit_length()-1])
          for a in candidates:
            s,F,_,_=motifs[a]
            if C&s==s and not (C^s)&F:out[C^s]+=v*f[a].conjugate()
        return dict(out)
    def norm(a):return math.sqrt(sum(abs(v)**2 for v in a.values()))
    def err(a,b):return norm({k:a.get(k,0)-b.get(k,0) for k in a.keys()|b.keys()})
    vac={0:1.0};one=[create(vac,f) for f in modes]
    rows=[]
    for i,j in [(0,0),(0,1)]:
        two=create(one[j],modes[i]);low=lower(two,modes[i]);expected={k:(2 if i==j else 1)*v for k,v in one[j].items()}
        assert all(C.bit_count()==8 for C in two)
        rows.append(dict(modes=[i,j],two_norm_squared=norm(two)**2,ideal_norm_squared=2 if i==j else 1,full_lowering_error=err(low,expected),configurations=len(two)))
    assert abs(norm(one[0])-1)<1e-12
    return dict(R=R,one_norm=norm(one[0]),rows=rows)
if __name__=='__main__':
    rows=[control(R) for R in [10,14,18]]
    for j in range(2):assert rows[-1]['rows'][j]['full_lowering_error']<rows[0]['rows'][j]['full_lowering_error']
    print(json.dumps(dict(status='bounded-support',scope='Exact finite motif algebra with complete syndrome buffers; not full Hamiltonian dynamics',rows=rows),indent=2))
