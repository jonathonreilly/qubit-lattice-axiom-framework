"""R19-3 Lemma D check: the forward bilinear Q(pure gauge, X) for ARBITRARY X and OFF-SHELL k.
   Claim (proved in the report): for the weight-1 contravariant density [sqrt(-g) G^{ab}]^(2) it vanishes identically
   (the scalar Lie-derivative terms cancel for weight 1, and the remaining terms are k_a G1^{ab}[X] = 0 by the linearized
   Bianchi identity).  For weight 0 (G2_ab, treatment B) and weight 2 ((-g)G^{ab}, treatment A) it does not.
   Reuses the expansion of r193_gauge_family.py (exec of its first part; same k = (-k0, 0, 0, kz), symbolic)."""
src = open(__file__.rsplit('/', 1)[0] + '/r193_gauge_family.py').read().split('# ---- sanity')[0]
exec(src)
v = sp.symbols('v0:4'); X = sp.symbols('X0:10')
egauge = sp.Matrix(4, 4, lambda a, b: k[a]*v[b] + k[b]*v[a])
Xm = sp.zeros(4, 4)
for i, kk in enumerate(keys):
    Xm[kk[0], kk[1]] = Xm[kk[1], kk[0]] = X[i]
def sub_e(q, emat): return sp.expand(q.subs({E[kk]: emat[kk[0], kk[1]] for kk in keys}, simultaneous=True))
for name, Q in (('B  (G2_ab, weight 0)', QB), ('A  ((-g)G^ab, weight 2 = LL)', QA), ("A' (sqrt(-g)G^ab, weight 1)", QAp)):
    worst = 0
    nz = 0
    for a in idx:
        for b in idx:
            if b < a: continue
            bil = sp.expand(sub_e(Q[a, b], egauge + Xm) - sub_e(Q[a, b], egauge) - sub_e(Q[a, b], Xm))
            if bil != 0: nz += 1
    gg_ = max(sp.expand(sub_e(Q[a, b], egauge)) != 0 for a in idx for b in idx)
    print(f'{name:32s}: Q(gauge,gauge) nonzero off shell: {gg_};  components with 2Q(gauge, X) != 0 (arbitrary X, off-shell k): {nz}/10')
print(f'time {time.time()-T0:.1f}s')
