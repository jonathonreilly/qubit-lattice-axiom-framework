import sympy as sp
ii=sp.Symbol('ii')
def combine(rb,coeffs):
    """coeffs: list of sympy exprs (linear in unknowns). returns dict n -> [f,g1,g2,g3] exprs"""
    W={}
    for b,c in zip(rb,coeffs):
        if c==0: continue
        for n,v in b.items():
            n=tuple(int(x) for x in n)
            w=W.setdefault(n,[0,0,0,0])
            for k in range(4):
                if v[k]!=0: w[k]+=sp.sympify(v[k]).subs(sp.I,ii)*c
    return {n:[sp.expand(x) for x in w] for n,w in W.items()}
def reim(e):
    e=sp.expand(e)
    p=sp.Poly(e,ii) if e.has(ii) else None
    if p is None: return e,0
    re=0; im=0
    for (k,),c in p.terms():
        k4=k%4; s=[1,1,-1,-1][k4]
        if k4%2==0: re+=s*c
        else: im+=s*c
    return sp.expand(re),sp.expand(im)
def unit_eqs(W):
    """coefficients of f^2+g.g-1 ; returns list of real polynomial equations"""
    P={}
    items=list(W.items())
    for n,v in items:
        for m,w in items:
            s=tuple(a+b for a,b in zip(n,m))
            if s<tuple(-x for x in s): continue   # keep half (real fn: coefficient at -s is conjugate)
            P[s]=P.get(s,0)+sum(v[k]*w[k] for k in range(4))
    eqs=[]
    for s,e in P.items():
        if s==(0,0,0): e=e-1
        re,im=reim(e)
        for x in (re,im):
            if x!=0: eqs.append(x)
    return eqs
def line_coeffs(W,p,a,comp):
    """restriction of component comp to line p*pi + t a: dict j-> expr (with ii)"""
    out={}
    for n,v in W.items():
        s=(-1)**(sum(pi*ni for pi,ni in zip(p,n))%2); j=sum(ai*ni for ai,ni in zip(a,n))
        out[j]=out.get(j,0)+s*v[comp]
    return {j:sp.expand(e) for j,e in out.items()}
def target_cos(eps,m,J):
    # eps*cos(m t) coefficients
    d={j:0 for j in range(-J,J+1)}
    if m==0: d[0]=eps
    else: d[m]+=sp.Rational(eps,2); d[-m]+=sp.Rational(eps,2)
    return d
def target_sin(eps,m,J):
    # eps*sin(m t) = eps (e^{imt}-e^{-imt})/(2i) ; as coefficients with ii: 1/(2i) = -ii/2
    d={j:0 for j in range(-J,J+1)}
    if m!=0: d[m]+=-ii*sp.Rational(eps,2); d[-m]+=ii*sp.Rational(eps,2)
    return d
def lin_eqs_from(dl,dt):
    eqs=[]
    for j in set(dl)|set(dt):
        e=sp.expand(dl.get(j,0)-dt.get(j,0))
        re,im=reim(e)
        for x in (re,im):
            if x!=0: eqs.append(x)
    return eqs
def to_sing(e): return str(e).replace('**','^')
def to_sing(e):
    e=sp.expand(e)
    if e==0: return '0'
    syms=sorted(e.free_symbols,key=str)
    if not syms: return '(%s)'%sp.Rational(e)
    p=sp.Poly(e,*syms)
    terms=[]
    for mon,c in p.terms():
        c=sp.Rational(c)
        m='*'.join('%s^%d'%(s,k) if k>1 else str(s) for s,k in zip(syms,mon) if k>0)
        terms.append('(%s)'%c+('*'+m if m else ''))
    return '+'.join(terms)
