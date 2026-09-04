"""T33 - RESULT 1, PROVED ANALYTICALLY IN GENERAL DIMENSION (not by enumeration).
A cross-lane review objected that finite d=2,3,4 enumeration should not carry
the theorem.  It does not have to.  Degree-by-degree proof:

On the rho-weighted carrier, degree k has inner product rho_k <,>_(Lambda^k g^-1).
For u in Lambda^k, v in Lambda^(k+1):
   <eps_a u, v>_(k+1) = rho_(k+1) <eps_a u, v> = rho_(k+1) <u, iota_a v>
   <u, eps_a^dag v>_k = rho_k <u, eps_a^dag v>
so   eps_a^dag = lambda_k iota_a  on degree k+1,  with  lambda_k = rho_(k+1)/rho_k.
Hence Gamma_a = eps_a + lambda iota_a with a DEGREE-DEPENDENT lambda.  Acting on
Lambda^k, and using eps_a eps_b + eps_b eps_a = 0, iota_a iota_b + iota_b iota_a = 0,
and iota_a eps_b + eps_b iota_a = (g^-1)_ab:

   {Gamma_a, Gamma_b} u = 2 lambda_k (g^-1)_ab u  +  (lambda_(k-1) - lambda_k) X u,
                          X = eps_a iota_b + eps_b iota_a.

Equality with 2 (g^-1)_ab for all u and all a,b forces  lambda_k = 1  (the
scalar part) and  lambda_(k-1) = lambda_k  (the X part, X != 0 in general).
lambda_k = 1 for every k is exactly  rho_(k+1) = rho_k  for every k:
ALL DEGREE WEIGHTS EQUAL.  The common value stays free.   QED, any d.

This script CHECKS that derivation mechanically (symbolic rho AND symbolic g,
degree block by degree block) for d = 2,3,4,5 -- as a check on the proof, not
as the proof."""
import sympy as sp, itertools
def run(d):
    B=[]
    for k in range(d+1): B+=[tuple(c) for c in itertools.combinations(range(d),k)]
    IDX={b:i for i,b in enumerate(B)}; n=len(B)
    deg={b:len(b) for b in B}
    g=sp.zeros(d,d)
    for i in range(d):
        for j in range(i,d): g[i,j]=g[j,i]=sp.Symbol(f'g{min(i,j)}{max(i,j)}')
    gi=g.inv()
    rho=[sp.Symbol(f'r{k}',positive=True) for k in range(d+1)]
    lam=[rho[k+1]/rho[k] for k in range(d)]          # lambda_k on degree k+1
    def epsm(a):
        M=sp.zeros(n,n)
        for Sx in B:
            if a in Sx: continue
            T=tuple(sorted(Sx+(a,))); M[IDX[T],IDX[Sx]]=(-1)**sum(1 for i in Sx if i<a)
        return M
    def iotam(a):
        M=sp.zeros(n,n)
        for Sx in B:
            for pos,i in enumerate(Sx):
                T=tuple(x for x in Sx if x!=i); M[IDX[T],IDX[Sx]]+=(-1)**pos*gi[a,i]
        return M
    E=[epsm(a) for a in range(d)]; I=[iotam(a) for a in range(d)]
    # Gamma_a = eps_a + eps_a^dag, eps_a^dag acts on degree k+1 as lambda_k * iota_a
    G=[]
    for a in range(d):
        M=sp.zeros(n,n)
        for Sx in B:                       # column = source basis element, degree k
            k=deg[Sx]
            for Tt in B:
                if E[a][IDX[Tt],IDX[Sx]]!=0: M[IDX[Tt],IDX[Sx]]+=E[a][IDX[Tt],IDX[Sx]]
                if I[a][IDX[Tt],IDX[Sx]]!=0: M[IDX[Tt],IDX[Sx]]+=lam[k-1]*I[a][IDX[Tt],IDX[Sx]]
        G.append(M)
    conds=set()
    for a in range(d):
        for b in range(a,d):
            R=sp.expand(G[a]*G[b]+G[b]*G[a]-2*gi[a,b]*sp.eye(n))
            for i in range(n):
                for j in range(n):
                    e=sp.simplify(sp.together(R[i,j]))
                    if e!=0:
                        num=sp.numer(sp.together(e))
                        for f,_ in sp.factor_list(sp.expand(num))[1]:
                            if f.free_symbols & set(rho): conds.add(sp.expand(f))
    conds={sp.simplify(c) for c in conds}
    sol=sp.solve(list(conds), rho[1:], dict=True)
    uniform=all(sp.simplify(c.subs({r:rho[0] for r in rho}))==0 for c in conds)
    print(f"d={d}  fibre {n}:  {len(conds)} distinct weight conditions", flush=True)
    print(f"   conditions: {sorted({str(sp.factor(c)) for c in conds})[:8]}", flush=True)
    print(f"   uniform rho annihilates every condition: {uniform}", flush=True)
    print(f"   solve() over rho_1..rho_d : {sol}", flush=True)
    print(flush=True)
for d in (2,3,4,5): run(d)
