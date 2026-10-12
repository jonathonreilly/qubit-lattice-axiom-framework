# R14-4 s1: exact basis of proper-cubic (O, 24 elements) covariant quadratic forms
#   Q(k,h) = h . V(k) . h,   V(k) = sum_ij k_i k_j V^{ij},   h a traceless symmetric 3x3 tensor,
# i.e. biquadratic invariants of degree (2 in k, 2 in h).  Exact rational arithmetic (sympy).
# Prints: the dimension (with O and with O_h), the basis, and the C4v sector values at k = z-hat
#   TT1 = (xx-yy)/sqrt2,  TT2 = xy-type,  VEC = xz/yz-type,  S = (2zz-xx-yy)/sqrt6.
import sympy as sp, itertools, pickle, os
kx,ky,kz=sp.symbols('kx ky kz'); K=sp.Matrix([kx,ky,kz])
a,b,c,d,e=sp.symbols('a b c d e')   # traceless coordinates: h = a*T1 + b*S + c*X + d*Y + e*Z  (orthonormal)
r2,r6=sp.sqrt(2),sp.sqrt(6)
T1=sp.Matrix([[1,0,0],[0,-1,0],[0,0,0]])/r2
S =sp.Matrix([[-1,0,0],[0,-1,0],[0,0,2]])/r6
X =sp.Matrix([[0,1,0],[1,0,0],[0,0,0]])/r2   # xy  (TT2 at k||z)
Y =sp.Matrix([[0,0,0],[0,0,1],[0,1,0]])/r2   # yz  (vector at k||z)
Z =sp.Matrix([[0,0,1],[0,0,0],[1,0,0]])/r2   # xz  (vector at k||z)
BAS=[T1,S,X,Y,Z]; hv=[a,b,c,d,e]
H=sum((x*B for x,B in zip(hv,BAS)),sp.zeros(3,3))
def group(proper=True):
    G=[]
    for p in itertools.permutations(range(3)):
        for s in itertools.product([1,-1],repeat=3):
            R=sp.zeros(3,3)
            for i in range(3): R[i,p[i]]=s[i]
            if (not proper) or R.det()==1: G.append(R)
    return G
def coords(M):   # traceless symmetric -> orthonormal coordinates
    return [sp.simplify(sum(M[i,j]*B[i,j] for i in range(3) for j in range(3))) for B in BAS]
# monomials k_i k_j h_p h_q
kmon=[kx*kx,ky*ky,kz*kz,kx*ky,ky*kz,kx*kz]
hmon=[hv[p]*hv[q] for p in range(5) for q in range(p,5)]
mons=[km*hm for km in kmon for hm in hmon]
def reynolds(poly,G):
    out=0
    for R in G:
        k2=R*K; h2=R*H*R.T; hc=coords(h2)
        sub={kx:k2[0],ky:k2[1],kz:k2[2]}
        sub.update({hv[i]:hc[i] for i in range(5)})
        out+=poly.xreplace(sub)
    return sp.expand(out/len(G))
def span(polys):
    allm=sorted(set().union(*[sp.Poly(p,kx,ky,kz,*hv).monoms() for p in polys if p!=0]))
    M=sp.Matrix([[sp.Poly(p,kx,ky,kz,*hv).coeff_monomial(m) if p!=0 else 0 for m in allm] for p in polys])
    return M, allm
if __name__=="__main__":
    out={}
    for proper in (True,False):
        G=group(proper)
        avg=[reynolds(m,G) for m in mons]
        M,allm=span(avg)
        rref,piv=M.T.rref()
        basis=[avg[i] for i in piv]
        print("group order",len(G),": dimension of invariant biquadratic forms on traceless h =",len(basis))
        out[proper]=basis
    # Choose a readable basis for O (proper): express known invariants and check they span.
    h=H; k=K
    hk=h*k
    cand={
     'I1 = k^2 h:h':  (k.dot(k))*sum(h[i,j]**2 for i in range(3) for j in range(3)),
     'I2 = |h k|^2':   hk.dot(hk),
     'I3 = sum_i k_i^2 h_ii^2': sum(k[i]**2*h[i,i]**2 for i in range(3)),
     'I4 = sum_i k_i^2 (h^2)_ii': sum(k[i]**2*(h*h)[i,i] for i in range(3)),
     'I5 = sum_ij k_i k_j h_ij h_ii': sum(k[i]*k[j]*h[i,j]*h[i,i] for i in range(3) for j in range(3)),
     'I6 = k^2 sum_i h_ii^2': (k.dot(k))*sum(h[i,i]**2 for i in range(3)),
    }
    cp=[sp.expand(v) for v in cand.values()]
    M,allm=span(out[True]+cp)
    print("rank(O-basis + candidates) =",M.rank(),"; rank(candidates) =",span(cp)[0].rank())
    # invariance check of candidates
    G=group(True)
    for name,p in zip(cand,cp):
        ok=sp.expand(reynolds(p,G)-p)==0
        print("  %-32s O-invariant: %s"%(name,ok))
    # sector values at k = z
    zsub={kx:0,ky:0,kz:1}
    print("C4v sector values at k = z-hat (coefficient of the sector coordinate squared; off-diagonals listed if nonzero):")
    for name,p in zip(cand,cp):
        q=sp.expand(p.xreplace(zsub))
        P=sp.Poly(q,*hv)
        diag=[P.coeff_monomial(x**2) for x in hv]
        off=[(hv[i],hv[j],P.coeff_monomial(hv[i]*hv[j])) for i in range(5) for j in range(i+1,5) if P.coeff_monomial(hv[i]*hv[j])!=0]
        print("  %-32s TT1=%s TT2=%s S=%s VECy=%s VECx=%s off=%s"%(name,diag[0],diag[2],diag[1],diag[3],diag[4],off))
    pickle.dump({'cand':{n:sp.srepr(p) for n,p in zip(cand,cp)}},open(os.path.join(os.path.dirname(__file__),'s1_invariants.pkl'),'wb'))
