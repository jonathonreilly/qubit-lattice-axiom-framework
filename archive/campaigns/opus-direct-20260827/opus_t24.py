"""T24 - the closed form PREDICTS T19's measured singular masses, and extends to 4D.
If det Q(q) = (m^2 + s.g^-1.s)^(2^(d-1)) with s_a = sin(q_a), then the propagator
is singular exactly at   m^2 = - s.g^-1.s.  Euclidean: never (m!=0).
Lorentzian: the LATTICE MASS SHELL  m^2 = sin^2(q_0) - sin^2(q_1).
Compare against the independently MEASURED lists from T19."""
import sympy as sp, itertools
def shell(g, L, d):
    gi = g.inv(); out=set()
    for k in itertools.product(range(L), repeat=d):
        s = [sp.sin(2*sp.pi*ki/L) for ki in k]
        q = sum(s[a]*gi[a,b]*s[b] for a in range(d) for b in range(d))
        v = sp.simplify(-q)
        if v.is_number and sp.im(v)==0 and v > 0:
            out.add(sp.nsimplify(sp.sqrt(v)))
    return sorted(out, key=lambda z: float(z))
MEASURED = {4:['1.0000000'], 6:['0.86602540'], 8:['0.70710678','1.0000000'],
            10:['0.58778525','0.74767439','0.95105652']}
print("2D LORENTZIAN g=diag(-1,1): predicted mass shell vs T19's MEASURED singular masses")
allok=True
for L in (4,6,8,10):
    pred = shell(sp.diag(-1,1), L, 2)
    ps = [f"{float(z):.8f}" for z in pred]
    ms = [f"{float(x):.8f}" for x in MEASURED[L]]
    ok = ps==ms; allok &= ok
    print(f"   L={L:2d}  predicted {ps}")
    print(f"         measured  {ms}   MATCH={ok}", flush=True)
print(f"   ALL L MATCH: {allok}")
print()
print("2D EUCLIDEAN g=diag(1,1): predicted shell must be EMPTY at every L")
print("  ", {L: shell(sp.diag(1,1), L, 2) for L in (4,6,8,10)}, flush=True)
print()
print("4D MINKOWSKI g=diag(-1,1,1,1): does the shell fill in with L?")
for L in (4,6,8):
    sh = shell(sp.diag(-1,1,1,1), L, 4)
    print(f"   L={L}: {len(sh)} distinct real masses  {[f'{float(z):.5f}' for z in sh][:8]}", flush=True)
print()
print("continuum limit: small q, s_a -> q_a, so the shell condition m^2 + q.g^-1.q = 0")
print("becomes  -E^2 + p^2 + m^2 = 0, i.e. E^2 = m^2 + p^2  -- the relativistic mass shell.")
