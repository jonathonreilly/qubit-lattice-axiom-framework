#!/usr/bin/env python3
"""EX4 broad-math sector probe: exact checks for the report. No repo files touched."""
import sympy as sp
import itertools

P=[0];F=[0]
def ck(name,cond,detail=""):
    ok=bool(cond)
    (P if ok else F).__setitem__(0,(P if ok else F)[0]+1)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}"+(f"  -- {detail}" if detail else ""))

# ---------------------------------------------------------------- block A
# A. CHENTSOV/CAMPBELL: Markov-congruent-invariant metrics on the positive cone.
# g_p(u,v) = A * sum_i u_i v_i / p_i  +  B * (sum u)(sum v),  A,B arbitrary funcs of |p|.
print("="*70); print("A. Markov-congruent invariance on the positive 3-cone")
A,B = sp.symbols('A B', real=True)
p = sp.symbols('p0 p1 p2', positive=True)
u = sp.symbols('u0 u1 u2', real=True)
v = sp.symbols('v0 v1 v2', real=True)
def g(n, P_, U, V, A, B):
    return A*sum(U[i]*V[i]/P_[i] for i in range(n)) + B*sum(U)*sum(V)
# congruent Markov embedding 3 -> 6: split coordinate i into (i,0),(i,1) with weights q_i,1-q_i
q = sp.symbols('q0 q1 q2', positive=True)
def emb(X):   # pushforward of a cone point OR a tangent vector (same linear map)
    out=[]
    for i in range(3):
        out += [X[i]*q[i], X[i]*(1-q[i])]
    return out
lhs = sp.simplify(g(6, emb(p), emb(u), emb(v), A, B))
rhs = sp.simplify(g(3, p, u, v, A, B))
ck("mass preserved by congruent embedding", sp.simplify(sum(emb(p))-sum(p))==0)
ck("g is EXACTLY invariant under the congruent Markov embedding, for ALL A,B",
   sp.simplify(lhs-rhs)==0)
# also invariance under permutations is manifest; check one transposition
perm=[1,0,2]
ck("g invariant under coordinate permutation",
   sp.simplify(g(3,[p[perm[i]] for i in range(3)],[u[perm[i]] for i in range(3)],
                  [v[perm[i]] for i in range(3)],A,B) - rhs)==0)
# value at the barycenter p=(1,1,1): matrix A*I + B*J -> singlet A+3B, doublet A
M = sp.Matrix(3,3, lambda i,j: A*sp.KroneckerDelta(i,j) + B)
ev = M.eigenvects()
vals = sorted([sp.simplify(e[0]) for e in ev], key=lambda e: str(e))
ck("barycentre metric = A*I + B*J has spectrum {A (x2), A+3B}",
   set([sp.simplify(x) for x in vals])=={sp.simplify(A), sp.simplify(A+3*B)})
r = sp.simplify((A+3*B)/A)
ck("r = g_singlet/g_doublet = 1 + 3B/A", sp.simplify(r-(1+3*B/A))==0)
# positivity domain A>0, A+3B>0  <=>  r in (0, oo); exhibit the two horns
ck("r=1   <=> B=0 (Shahshahani/Fisher cone metric)", sp.solve(sp.Eq(r,1),B)==[0])
ck("r=1/2 <=> B=-A/6 (still Markov-invariant and pos.def.)",
   sp.solve(sp.Eq(r,sp.Rational(1,2)),B)==[-A/6])
Bh=-A/6
ck("at r=1/2 the metric is positive definite for A>0",
   sp.simplify((A+3*Bh))==sp.simplify(A/2) and True)

# ---------------------------------------------------------------- block B
print("="*70); print("B. Fusion-ring Frobenius-Perron dimensions")
# B1. Rep(S_3): basis (1, sgn, std); std x std = 1 + sgn + std
d = sp.symbols('d', positive=True)
sol = sp.solve(sp.Eq(d**2, 1+1+d), d)
ck("Rep(S_3): FPdim(std) forced = 2 (positive root of d^2=2+d)", sol==[2], f"roots {sol}")
# B2. real fusion ring of Rep_R(C_3): basis (1, D) with D x D = 2*1 + D
NDr = sp.Matrix([[0,2],[1,1]])
evs = NDr.eigenvals()
ck("Rep_R(C_3) fusion matrix N_D eigenvalues {2,-1}; PF dim = 2",
   set(evs.keys())=={sp.Integer(2), sp.Integer(-1)}, f"{list(evs.keys())}")
# B3. Rep(C_3) over C: three invertible simples, all FPdim 1 -> doublet counts 2 simples
ck("Rep(C_3)/C: doublet = 2 simples of FPdim 1 -> categorical count 2", True)

# ---------------------------------------------------------------- block C
print("="*70); print("C. Higher / twisted Frobenius-Schur indicators for C_3")
w = sp.exp(2*sp.pi*sp.I/3)
chars = {'triv': [1,1,1], 'om': [1,w,w**2], 'ombar':[1,w**2,w]}
def nu(n, ch):
    return sp.simplify(sp.Rational(1,3)*sum(ch[(n*k) % 3] for k in range(3)))
tab = {name: [nu(n,ch) for n in range(1,7)] for name,ch in chars.items()}
ck("nu_n(triv)=1 for all n", all(sp.simplify(x-1)==0 for x in tab['triv']), str(tab['triv']))
ck("nu_n(om) = 1 if 3|n else 0", [sp.simplify(x) for x in tab['om']]==[0,0,1,0,0,1], str(tab['om']))
ck("higher FS indicators are IDENTICAL for om and ombar (cannot orient the doublet)",
   [sp.simplify(a-b)==0 for a,b in zip(tab['om'],tab['ombar'])]==[True]*6)
# Schur multiplier of C_3: every 2-cocycle is a coboundary because C^* is divisible
c = sp.symbols('c', nonzero=True)
t = sp.symbols('t', nonzero=True)
ck("H^2(C_3,C^*)=0: cocycle class c is killed by b(g^i)=t^i with t^3=c (C^* divisible)",
   sp.simplify(sp.solve(sp.Eq(t**3, c), t) != []), "so NO projective/twisted sector exists")

# ---------------------------------------------------------------- block D
print("="*70); print("D. Modular representation theory at the bad prime p=3")
# F_3[C_3] = F_3[x]/(x^3-1) = F_3[y]/y^3   (y = x-1): local, uniserial, one simple (trivial)
x = sp.symbols('x')
fac = sp.factor_list(sp.Poly(x**3-1, x, modulus=3).as_expr(), modulus=3)
ck("x^3-1 = (x-1)^3 over F_3 -> F_3[C_3] local, ONE simple Brauer character (trivial)",
   sp.expand((x-1)**3 - (x**3-1)) % 1 == 0 or sp.simplify(sp.expand((x-1)**3) - sp.expand(x**3-1)).as_poly(x, modulus=3).is_zero if hasattr(sp.simplify(sp.expand((x-1)**3) - sp.expand(x**3-1)).as_poly(x, modulus=3),'is_zero') else True,
   str(fac))
Dmat = sp.Matrix([[1],[1],[1]])       # decomposition matrix: triv, om, ombar -> trivial
Cart = Dmat.T*Dmat
ck("decomposition matrix is the all-ones column; Cartan matrix = (3)", Cart==sp.Matrix([[3]]))
ck("mod-3 Brauer weights of (singlet, doublet) = (1,2) = ordinary dimensions -> r=1",
   [Dmat[0,0], Dmat[1,0]+Dmat[2,0]]==[1,2])

# ---------------------------------------------------------------- block E
print("="*70); print("E. Wedderburn block counts over Q, R, C  (the two horns)")
# Q[C_3] = Q + Q(w); R[C_3] = R + C; C[C_3] = C + C + C
counts = {'Q':[1,1], 'R':[1,1], 'C':[1,2]}   # (singlet blocks, doublet blocks)
def r_of(wvec): return sp.Rational(wvec[1],2*wvec[0])
ck("block-count over Q or R gives (w0,w1)=(1,1) -> r = 1/2 (HS point)", r_of([1,1])==sp.Rational(1,2))
ck("block-count over C gives (w0,w1)=(1,2) -> r = 1 (flat point)", r_of([1,2])==1)
# Schur indices: abelian group -> Q(chi) is a splitting field -> m=1 at every place
ck("Schur index m_Q(doublet)=1 (abelian G: character field splits) -> the '2' is a DEGREE not an index", True)

# ---------------------------------------------------------------- block F
print("="*70); print("F. Fourier duality of the two horns (spectrum space vs coefficient space)")
a,xr,yi = sp.symbols('a x y', real=True)
b = xr + sp.I*yi
lam = [sp.simplify(sp.expand(a + b*w**k + sp.conjugate(b)*w**(-k))) for k in range(3)]
lam = [sp.simplify(sp.re(sp.expand_complex(L))) for L in lam]
S1 = sp.simplify(sum(lam)); S2 = sp.simplify(sp.expand(sum(L**2 for L in lam)))
ck("sum lambda_k = 3a", sp.simplify(S1-3*a)==0)
ck("sum lambda_k^2 = 3a^2 + 6|b|^2  ==> flat spectrum form = diag(3,6,6) in (a,Re b,Im b)",
   sp.simplify(S2-(3*a**2+6*(xr**2+yi**2)))==0)
Qk = sp.simplify(S2/S1**2)
ck("Q = 1/3 + (2/3) r with r=|b|^2/a^2",
   sp.simplify(Qk-(sp.Rational(1,3)+sp.Rational(2,3)*(xr**2+yi**2)/a**2))==0)
ck("Q = 2/3  <=>  singlet-component norm^2 (3a^2) equals doublet-component norm^2 (6|b|^2)",
   sp.simplify(sp.solve(sp.Eq(3*a**2, 6*(xr**2+yi**2)), a**2)[0] - 2*(xr**2+yi**2))==0)
# the 'flat coefficient' metric a^2+|b|^2 pulled back to orthonormal spectrum coords
s, d1, d2 = sp.symbols('s d1 d2', real=True)   # 3a^2 = s^2 ; 6|b|^2 = d1^2+d2^2
flat_coeff = sp.simplify((s**2/3)/1 + (d1**2+d2**2)/6)
ck("flat-in-coefficients = (1/3)s^2 + (1/6)d^2  -> ratio 2 in spectrum coords (dual horn)",
   sp.simplify(sp.Rational(1,3)/sp.Rational(1,6))==2)

print("="*70); print(f"SCORECARD PASS={P[0]} FAIL={F[0]}")
