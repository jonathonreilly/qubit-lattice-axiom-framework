"""Source implementation of the frozen candidate, not a proof oracle."""
import itertools
from functools import lru_cache
import sympy as s

NORM_SQUARED = s.Integer(1)
ANCILLARY_PARITY = True
STATE_CHILD_FACTOR = True

I = s.I
_mul = {
    ('X','Y'):(I,'Z'),('Y','X'):(-I,'Z'),
    ('Y','Z'):(I,'X'),('Z','Y'):(-I,'X'),
    ('Z','X'):(I,'Y'),('X','Z'):(-I,'Y')}

def clean(p):
    return {k:s.expand(v) for k,v in p.items() if s.expand(v)!=0}

def add(*ps):
    out={}
    for p in ps:
        for k,v in p.items(): out[k]=out.get(k,0)+v
    return clean(out)

def scale(c,p): return clean({k:c*v for k,v in p.items()})

def mul(p,q):
    out={}
    for a,x in p.items():
        for b,y in q.items():
            c=x*y;w=[]
            for u,v in zip(a,b):
                if u=='I': w.append(v)
                elif v=='I': w.append(u)
                elif u==v: w.append('I')
                else:
                    z,t=_mul[u,v];c*=z;w.append(t)
            key=''.join(w);out[key]=out.get(key,0)+c
    return clean(out)

def star(p): return {k:s.conjugate(v) for k,v in p.items()}
def unit(n): return {'I'*n:s.Integer(1)}
def word(n,items):
    a=['I']*n
    for j,c in items.items():a[j]=c
    return {''.join(a):s.Integer(1)}

def gamma(n,k):
    j,r=divmod(k,2)
    return {'Z'*j+('X' if r==0 else 'Y')+'I'*(n-j-1):s.Integer(1)}

def gamma_word(n,indices):
    p=unit(n)
    for k in indices:p=mul(p,gamma(n,k))
    return p

def refined_word(n,indices,levels=1):
    """n coarse sites; even input word, including repetitions."""
    if len(indices)%2:raise ValueError('even words only')
    children=2**levels;out=unit(n*children)
    for k in indices:
        j,r=divmod(k,2)
        out=mul(out,add(*(gamma(n*children,2*(children*j+b)+r)
                          for b in range(children))))
    return scale(NORM_SQUARED**(levels*len(indices)//2),out)

@lru_cache(None)
def inverse_even_basis(n):
    out={}
    for r in range(0,2*n+1,2):
        for inds in itertools.combinations(range(2*n),r):
            p=gamma_word(n,inds)
            assert len(p)==1
            w,c=next(iter(p.items()));out[w]=(c,inds)
    return out

def refine_poly(p,n,levels=1):
    out={};basis=inverse_even_basis(n)
    for w,c in p.items():
        phase,inds=basis[w]
        out=add(out,scale(c/phase,refined_word(n,inds,levels)))
    return out

def coarse_even_basis(n):return sorted(inverse_even_basis(n))

def expected_z(n,j):
    f=2*n;l=2*j
    return scale(s.Rational(1,2),add(word(f,{l:'Z'}),word(f,{l+1:'Z'}),
      scale(-1,word(f,{l:'X',l+1:'X'})),scale(-1,word(f,{l:'Y',l+1:'Y'}))))

def expected_bond(n,j):
    f=2*n;l=2*j
    return scale(s.Rational(1,2),add(
      word(f,{l:'X',l+1:'Z',l+2:'X'}),
      word(f,{l:'X',l+1:'Z',l+2:'Z',l+3:'X'}),
      word(f,{l+1:'X',l+2:'X'}),word(f,{l+1:'X',l+2:'Z',l+3:'X'})))

def inserted_bond(n,j):
    d={2*j:'X',2*(j+1):'X'}
    if ANCILLARY_PARITY:d[2*j+1]='Z'
    return word(2*n,d)

def state_weight(k,np):
    return 1+np.cos(k) if STATE_CHILD_FACTOR else np.ones_like(k)
