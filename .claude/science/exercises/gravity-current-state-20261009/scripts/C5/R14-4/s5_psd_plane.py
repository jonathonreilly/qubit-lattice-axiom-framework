# R14-4 s5: on the plane TT1=TT2=1, VEC=S=0 (c=(1,c2,c3,-2-c2,1/2-c3,0)), which members are PSD?
# Necessary conditions near the axis (exact, sympy): V(z) has kernel N=span(S,Y,Z); PSD at z+eps forces the N-block
# of the first-order terms V^{xz}, V^{yz} to vanish, and then the second-order Schur complement on N to be PSD.
# Also the general (TT1, TT2) cone: c1=TT2, c6=TT1-TT2 (no normalisation), VEC=S=0.
import sympy as sp
from s2_rank_lemma import Q, C, hv, kx, ky, kz
c2,c3,t1,t2,ex,ey=sp.symbols('c2 c3 t1 t2 ex ey')
def Vm(sub,kv):
    q=sp.expand(Q.xreplace(sub).xreplace({kx:kv[0],ky:kv[1],kz:kv[2]}))
    return sp.Matrix(5,5,lambda i,j: sp.Rational(1,2)*sp.diff(q,hv[i],hv[j]))
for label,sub in [("TT1=TT2=1",{C[0]:1,C[1]:c2,C[2]:c3,C[3]:-2-c2,C[4]:sp.Rational(1,2)-c3,C[5]:0}),
                  ("TT1=t1,TT2=t2",{C[0]:t2,C[1]:c2,C[2]:c3,C[3]:-2*t2-c2,C[4]:None,C[5]:t1-t2})]:
    if sub[C[4]] is None:
        # S=0: c1 + 2/3(c2+c3+c4+c5) + c6 = 0  -> c5
        c5=sp.solve(sp.Eq(t2+sp.Rational(2,3)*(c2+c3+(-2*t2-c2)+sp.Symbol('c5'))+(t1-t2),0),sp.Symbol('c5'))[0]
        sub[C[4]]=c5
    Vz=Vm(sub,(0,0,1)); print(label,": V(z) diag =",[sp.simplify(Vz[i,i]) for i in range(5)])
    V=Vm(sub,(ex,ey,1))
    N=[1,3,4]   # S, Y, Z (kernel at the axis)
    first=sp.Matrix(3,3,lambda i,j: sp.expand(sp.diff(V[N[i],N[j]],ex).subs({ex:0,ey:0})))
    first2=sp.Matrix(3,3,lambda i,j: sp.expand(sp.diff(V[N[i],N[j]],ey).subs({ex:0,ey:0})))
    conds=[x for x in list(first)+list(first2) if x!=0]
    print("   first-order N-block conditions (must vanish):",sorted(set(map(sp.factor,conds)),key=str))
    sol=sp.solve(conds,[c2,c3],dict=True); print("   solutions:",sol)
    for s in sol:
        Vs=V.xreplace(s)
        # second-order Schur complement on N:  N-block at O(eps^2) minus R-N first-order couplings^2 / R-block
        R=[0,2]
        Vnn2=sp.Matrix(3,3,lambda i,j: sp.expand(Vs[N[i],N[j]]))   # quadratic in eps now
        Vrn1=sp.Matrix(2,3,lambda i,j: sp.expand(sp.diff(Vs[R[i],N[j]],ex)*ex+sp.diff(Vs[R[i],N[j]],ey)*ey).subs({ex:0,ey:0}) if False else sp.expand((sp.diff(Vs[R[i],N[j]],ex)*ex+sp.diff(Vs[R[i],N[j]],ey)*ey).xreplace({})))
        Vrn1=sp.Matrix(2,3,lambda i,j: sp.expand(sp.diff(Vs[R[i],N[j]],ex).subs({ex:0,ey:0})*ex+sp.diff(Vs[R[i],N[j]],ey).subs({ex:0,ey:0})*ey))
        Vrr0=sp.Matrix(2,2,lambda i,j: Vs[R[i],R[j]].subs({ex:0,ey:0}))
        Sch=sp.simplify(Vnn2-Vrn1.T*Vrr0.inv()*Vrn1)
        print("   second-order Schur complement on N(eps) =",sp.factor(Sch))
        for e2 in [(1,0),(0,1),(1,1),(1,-1),(2,1)]:
            M=Sch.xreplace({ex:e2[0],ey:e2[1]})
            print("      eps dir",e2,": eigenvalues",[sp.simplify(x) for x in M.eigenvals(multiple=True)])
