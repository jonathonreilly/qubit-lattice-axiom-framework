"""Direct first-order metric geometry; no forward-solver imports."""
import sympy as s

def checks():
    t,x,y,z,ep,k=s.symbols('t x y z ep k',real=True)
    coords=[t,x,y,z];a=s.Function('a')(t);f=s.Function('f')(t);chi=s.Function('chi')(t);X=s.Function('X')(t)
    wave=s.exp(s.I*k*x)
    lin=lambda q:s.expand(q).coeff(ep,0)+ep*s.expand(q).coeff(ep,1)
    g=s.diag(-(1+2*ep*f*wave),*[a*a*(1-2*ep*f*wave)]*3)
    gi=s.diag(-(1-2*ep*f*wave),*[(1+2*ep*f*wave)/(a*a)]*3)
    G={}
    for r in range(4):
     for m in range(4):
      for n in range(4):
       G[r,m,n]=lin(sum(gi[r,l]*(s.diff(g[l,n],coords[m])+s.diff(g[l,m],coords[n])-s.diff(g[m,n],coords[l]))/2 for l in range(4)))
    Ric=s.zeros(4)
    for m in range(4):
     for n in range(4):
      Ric[m,n]=lin(sum(s.diff(G[r,m,n],coords[r])-s.diff(G[r,m,r],coords[n])+sum(G[r,r,l]*G[l,m,n]-G[r,n,l]*G[l,m,r] for l in range(4)) for r in range(4)))
    scalar=lin(sum(gi[m,n]*Ric[m,n] for m in range(4) for n in range(4)))
    mixed=s.zeros(4)
    for m in range(4):
     for n in range(4):mixed[m,n]=lin(sum(gi[m,l]*Ric[l,n] for l in range(4))-(scalar/2 if m==n else 0))
    H=s.diff(a,t)/a;Hd=s.diff(H,t)
    targets={
     'Einstein_00':(mixed[0,0].coeff(ep,1)/wave,2*(k*k*f/a**2+3*H*(s.diff(f,t)+H*f))),
     'Einstein_0i':(mixed[0,1].coeff(ep,1)/(s.I*k*wave),-2*(s.diff(f,t)+H*f)),
     'Einstein_pressure':(mixed[1,1].coeff(ep,1)/wave,2*(s.diff(f,t,2)+4*H*s.diff(f,t)+(2*Hd+3*H**2)*f))}
    sqrtg=a**3*(1-2*ep*f*wave);scalarfield=chi+ep*X*wave
    box_num=sum(s.diff(lin(sqrtg*gi[m,n]*s.diff(scalarfield,coords[n])),coords[m]) for m in range(4) for n in range(4))
    box=lin((1+2*ep*f*wave)*box_num/a**3)
    targets['scalar_box']=(box.coeff(ep,1)/wave,-s.diff(X,t,2)-3*H*s.diff(X,t)-k*k*X/a**2+2*f*(s.diff(chi,t,2)+3*H*s.diff(chi,t))+4*s.diff(f,t)*s.diff(chi,t))
    rows=[]
    for name,(got,expected) in targets.items():
     res=s.factor(got-expected);rows.append({'name':name,'derived':str(s.simplify(got)),'expected':str(expected),'residual':str(res),'passed':res==0})
    return rows
