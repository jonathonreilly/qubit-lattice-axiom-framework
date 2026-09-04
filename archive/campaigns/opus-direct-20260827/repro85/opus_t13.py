"""T13 — IS THE COMMITTED BENCH ON THE PROPAGATION LOCUS?  And what changes if
it is put on it?
The committed bench uses shear c = CARRIER_SIGMA = 3/5 and the 'xgraded'
volumes  v = (1 + ((3t+2x) mod 5))/3 + 1/2.
The selector (Result 1) says the rule propagates only on  v^2 = 1 - c^2."""
import sympy as sp
R = sp.Rational
c = R(3, 5)
need = sp.sqrt(1 - c**2)
vols = sorted({R(1 + ((3*t + 2*x) % 5), 3) + R(1, 2) for t in range(6) for x in range(4)})
print(f"committed shear c = {c};  selector demands v = sqrt(1-c^2) = {need}", flush=True)
print(f"committed xgraded volumes actually used: {vols}", flush=True)
print(f"any cell on the locus? {any(sp.simplify(v**2 - (1-c**2)) == 0 for v in vols)}", flush=True)
print(f"closest cell: v={min(vols, key=lambda v: abs(float(v-need)))} vs required {need}", flush=True)
# ---- what does the record-weight profile look like ON vs OFF the locus?
BAS = [(), (0,), (1,), (0,1)]; IDX = {b:i for i,b in enumerate(BAS)}
def epsm(a):
    M = sp.zeros(4,4)
    for Sx in BAS:
        if a in Sx: continue
        T = tuple(sorted(Sx+(a,))); M[IDX[T], IDX[Sx]] = (-1)**sum(1 for i in Sx if i < a)
    return M
def iota(a, gi):
    M = sp.zeros(4,4)
    for Sx in BAS:
        for pos,i in enumerate(Sx):
            T = tuple(x for x in Sx if x != i); M[IDX[T], IDX[Sx]] += (-1)**pos * gi[a,i]
    return M
def weights(cc, vv, L=4, m=R(1,2)):
    g = sp.Matrix([[1, cc],[cc, 1]]); gi = g.inv()
    D = sp.diag(vv, vv*gi[0,0], vv*gi[1,1], vv*gi.det())
    D[1,2] = vv*gi[0,1]; D[2,1] = vv*gi[1,0]
    Gam = [sp.Matrix(sp.expand(epsm(a) + iota(a, gi))) for a in range(2)]
    N = L*L; sid = {}
    sites = [(x,y) for x in range(L) for y in range(L)]
    for i,s in enumerate(sites): sid[s] = i
    K = sp.zeros(4*N, 4*N)
    for s in sites:
        for a in range(2):
            for sgn, r in ((+1, ((s[0]+(a==0))%L, (s[1]+(a==1))%L)),
                           (-1, ((s[0]-(a==0))%L, (s[1]-(a==1))%L))):
                i, j = sid[s]*4, sid[r]*4
                for p in range(4):
                    for q in range(4): K[i+p, j+q] += sgn*R(1,2)*Gam[a][p,q]
    Q = sp.Matrix(4*N, 4*N, lambda i,j: (m if i==j else 0) + K[i,j])
    Qi = Q.inv()
    Dg = sp.zeros(4*N,4*N)
    for s in sites:
        i = sid[s]*4
        for p in range(4):
            for q in range(4): Dg[i+p, i+q] = D[p,q]
    # W9-analog: normalised diagonal of the hermitian part of the on-site block
    blk = sp.Matrix(4,4, lambda p,q: R(1,2)*(Qi[p,q] + Qi[q,p]))
    tot = sum(blk[k,k] for k in range(4))
    return [sp.cancel(blk[k,k]/tot) for k in range(4)], sp.cancel(tot)
w_off, t_off = weights(c, vols[0])
w_on,  t_on  = weights(c, need)
print(f"\nOFF locus (c={c}, v={vols[0]}): weights = {[str(x) for x in w_off]}", flush=True)
print(f"                                   spread = {sp.nsimplify(max(w_off)-min(w_off))}", flush=True)
print(f"ON  locus (c={c}, v={need}):  weights = {[str(sp.nsimplify(x)) for x in w_on]}", flush=True)
print(f"                                   spread = {sp.nsimplify(sp.simplify(max(w_on)-min(w_on)))}", flush=True)
print(f"\nON-locus weights all equal (flat record distribution)? "
      f"{sp.simplify(max(w_on)-min(w_on)) == 0}", flush=True)
