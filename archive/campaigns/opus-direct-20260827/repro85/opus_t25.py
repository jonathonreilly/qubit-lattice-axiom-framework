"""T25 - the ENERGY is a corollary of the master identity, not a separate fact.
det Q(q) = (m^2 + s.g^-1.s)^(2^(d-1)) with s_a = sin(q_a).  Continue q_0 = i*w:
sin(i w) = i sinh w, so on a Euclidean g the pole condition m^2 - sinh^2 w
+ sum_i sin^2(p_i) = 0 gives  w = arcsinh sqrt(m^2 + sum sin^2 p_i),
whose small-p limit is the relativistic sqrt(m^2+p^2).  Check the analytic pole
numerically (det Q vanishes there) in d=2 AND d=4, and against R5's MEASURED
decay rates."""
import sympy as sp, itertools, mpmath as mp
mp.mp.dps = 40
def carrier(d):
    B=[]
    for k in range(d+1): B += [tuple(c) for c in itertools.combinations(range(d),k)]
    return B, {b:i for i,b in enumerate(B)}
def gammas(d, gi):
    B,IDX = carrier(d); n=len(B); G=[]
    for a in range(d):
        M = sp.zeros(n,n)
        for Sx in B:
            if a not in Sx:
                T=tuple(sorted(Sx+(a,))); M[IDX[T],IDX[Sx]] += (-1)**sum(1 for i in Sx if i<a)
            for pos,i in enumerate(Sx):
                T=tuple(x for x in Sx if x!=i); M[IDX[T],IDX[Sx]] += (-1)**pos*gi[a,i]
        G.append(sp.Matrix(M))
    return G,n
def pole_check(d, gnum, m, ps):
    """ps = spatial momenta (d-1 of them). Solve for w, then verify det Q = 0."""
    gi = gnum.inv()
    G,n = gammas(d, gi)
    S2 = sum(mp.sin(p)**2 for p in ps)
    w = mp.asinh(mp.sqrt(m**2 + S2))
    s = [1j*mp.sinh(w)] + [mp.sin(p) for p in ps]
    Q = mp.matrix(n,n)
    for i in range(n):
        Q[i,i] = m
    for a in range(d):
        for i in range(n):
            for j in range(n):
                if G[a][i,j] != 0: Q[i,j] += 1j*complex(s[a])*float(G[a][i,j])
    dq = mp.det(Q)
    quad = sum(complex(s[a])*complex(s[b])*float(gi[a,b]) for a in range(d) for b in range(d))
    return w, abs(dq), abs(m**2 + quad)
print("d=2 EUCLIDEAN g=diag(1,1)  -- compare with R5's MEASURED omega")
for m,p,meas in [(0.75, 0.0, 0.6931471806), (0.75, 2*mp.pi/4, 1.047593013),
                 (0.75, 2*mp.pi/8, 0.9029692205)]:
    w, dq, q0 = pole_check(2, sp.diag(1,1), m, [p])
    print(f"   m={m} sin p={float(mp.sin(p)):.6f}: analytic w={mp.nstr(w,10)}  "
          f"R5 measured={meas}  |diff|={abs(float(w)-meas):.2e}   |det Q at pole|={mp.nstr(dq,3)}", flush=True)
print()
print("d=4 EUCLIDEAN g=diag(1,1,1,1)  (fibre 16) -- the physical-dimension energy")
for m,ps in [(0.5,[0.0,0.0,0.0]), (0.5,[2*mp.pi/8,0.0,0.0]), (0.5,[2*mp.pi/8,2*mp.pi/6,2*mp.pi/4])]:
    w, dq, q0 = pole_check(4, sp.diag(1,1,1,1), m, ps)
    rel = mp.sqrt(m**2 + sum(p**2 for p in ps))
    print(f"   m={m} p={[round(float(x),4) for x in ps]}: w={mp.nstr(w,12)}  "
          f"|det Q at pole|={mp.nstr(dq,3)}  |m^2+s.g.s|={mp.nstr(q0,3)}  continuum sqrt(m^2+p^2)={mp.nstr(rel,10)}", flush=True)
print()
print("small-momentum limit in d=4 (relativistic regime): w / sqrt(m^2+p^2)")
for sc in (0.2, 0.05, 0.01):
    m = 0.6*sc; ps=[0.8*sc,0,0]
    w,_,_ = pole_check(4, sp.diag(1,1,1,1), m, ps)
    rel = mp.sqrt(m**2+sum(p**2 for p in ps))
    print(f"   scale={sc}: w={mp.nstr(w,10)}  sqrt(m^2+p^2)={mp.nstr(rel,10)}  ratio={mp.nstr(w/rel,12)}", flush=True)
