# 2D slice theorem via 1D line lemma: on lines k2=0 and k2=pi, V(t,.) = c*(cos(mt) + i sin(mt) sigma_x), |m|<=2, c=+-1.
# Impose these exact linear constraints for every case and compute the Groebner basis of the remaining system over Q.
import pickle, sympy as sp, itertools, time
d=pickle.load(open('slice2d.pkl','rb')); P=d['params']; c0=d['c0']; cu=d['cu']; eqs=d['eqs']
def target(n1,m,c):
    # Fourier coefficient at e^{i n1 t} of c*cos(mt) and c*sin(mt)
    if m==0: return (c if n1==0 else 0), 0
    cs = sp.Rational(c,2)*((n1==m)+(n1==-m))
    sn = c/(2*sp.I)*((n1==m)-(n1==-m))
    return cs, sn
results=[]
T=time.time()
for (m,c,mp,cp) in itertools.product(range(-2,3),[1,-1],range(-2,3),[1,-1]):
    lin=[]
    for sgn,(mm,cc) in [(1,(m,c)),(-1,(mp,cp))]:
        for n1 in range(-2,3):
            s0=sum(c0[(n1,n2,0)]*sp.Integer(sgn)**n2 for n2 in range(-2,3))
            sv=[sum(cu[(n1,n2,0)][j]*sp.Integer(sgn)**n2 for n2 in range(-2,3)) for j in range(3)]
            cs,sn=target(n1,mm,cc)
            for x in [s0-cs, sv[0]-sn, sv[1], sv[2]]:
                x=sp.expand(x)
                for y in (sp.re(x),sp.im(x)):
                    y=sp.expand(y)
                    if y!=0: lin.append(y)
    A,b=sp.linear_eq_to_matrix(lin,P)
    sol=list(sp.linsolve((A,b),P))
    if not sol:
        results.append(((m,c,mp,cp),'linear-inconsistent')); continue
    sub=dict(zip(P,sol[0]))
    free=sorted(set().union(*[sp.sympify(s).free_symbols for s in sol[0]]),key=str)
    red=[sp.expand(e.subs(sub)) for e in eqs]; red=[e for e in red if e!=0]
    if not free:
        results.append(((m,c,mp,cp),'no free vars; residual eqs nonzero:'+str(bool(red)))); continue
    G=sp.groebner(red,*free,order='lex') if red else None
    if G is None: results.append(((m,c,mp,cp),'NO EQUATIONS LEFT, free=%s'%free)); continue
    if G.exprs==[1]: results.append(((m,c,mp,cp),'GB=[1] (no solution)')); continue
    sols=sp.solve(G.exprs,free,dict=True)
    full=[{p:sp.simplify(sp.sympify(sub[p]).subs(s)) for p in P} for s in sols]
    results.append(((m,c,mp,cp),'GB=%s ; solutions=%s'%(G.exprs,full)))
for r in results: print(r)
print("time %.1fs"%(time.time()-T))
