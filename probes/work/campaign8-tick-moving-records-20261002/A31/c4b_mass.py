"""A31 c4b: in the spin-rotation-invariant signed exchange, is there a pi-flux pattern whose site sums are
constant AND whose sign on each axis does not depend on the coordinate along that axis? Then bond
dimerization changes no site sum and acts as a clean (two-site) mass. Annealing on 4^3, then the
one-excitation gap at the cone on 8^3 with 10% dimerization on all axes."""
import signal, itertools, numpy as np
signal.alarm(55)
rng = np.random.default_rng(11)
L = 4
# eta_a(x) depends on the two coordinates transverse to a: tables T[a][u][v] with (u,v) = the other two coords
def eta_of(T, s, a):
    o = [c for i,c in enumerate(s) if i != a]; return T[a][o[0] % L][o[1] % L]
sites = list(itertools.product(range(L), repeat=3))
E = [(1,0,0),(0,1,0),(0,0,1)]
def ad(p,e): return tuple((p[t]+e[t]) % L for t in range(3))
def cost(T):
    c = 0
    for s in sites:
        tot = sum(eta_of(T,s,a) + eta_of(T,ad(s,tuple(-x for x in E[a])),a) for a in range(3))
        c += abs(abs(tot) - 2)          # want site sum = +-2 everywhere (|sum_a eta| = 1)
        for a,b in [(0,1),(1,2),(0,2)]:
            pr = eta_of(T,s,a)*eta_of(T,ad(s,E[a]),b)*eta_of(T,ad(s,E[b]),a)*eta_of(T,s,b)
            c += (pr + 1) // 2 * 4       # penalty if flux 0
    return c
found = None
for rep in range(20):
    T = [rng.choice([1,-1], size=(L,L)) for _ in range(3)]
    c = cost(T); temp = 3.0
    for sw in range(300):
        a = rng.integers(3); u, v = rng.integers(L, size=2)
        T[a][u][v] *= -1; c2 = cost(T)
        if c2 <= c or rng.random() < np.exp(-(c2-c)/temp): c = c2
        else: T[a][u][v] *= -1
        temp = max(0.05, temp*0.98)
        if c == 0: break
    if c == 0: found = T; break
print("axis-independent pi-flux pattern with constant |site sum| = 2:", "FOUND" if found is not None else "not found (20 restarts)")
if found is not None:
    sums = set()
    for s in sites:
        sums.add(sum(eta_of(found,s,a) + eta_of(found,ad(s,tuple(-x for x in E[a])),a) for a in range(3)))
    print("  site sums:", sorted(sums))
    # one-excitation spectrum on 8^3 with and without dimerization
    L8 = 8; s8 = list(itertools.product(range(L8), repeat=3)); idx = {s:i for i,s in enumerate(s8)}; N = len(s8)
    def H1(dimer):
        H = np.zeros((N,N)); ss = np.zeros(N)
        for s in s8:
            for a in range(3):
                t = tuple((s[i]+E[a][i]) % L8 for i in range(3))
                e = eta_of(found, s, a) * (1 + dimer*(-1)**s[a])
                i, j = idx[s], idx[t]; H[i,j] += 2*e; H[j,i] += 2*e; ss[i] += e; ss[j] += e
        H[np.diag_indices(N)] += -2*ss
        return H, ss
    for d in (0.0, 0.1):
        H, ss = H1(d); w = np.linalg.eigvalsh(H); Ec = -2*ss[0]
        dd = np.sort(np.abs(w - Ec))
        print(f"  dimerization {d:.1f}: site sums {sorted(set(np.round(ss,6)))}; cone energy E_c = {Ec:+.1f} (relative to the emptiness); "
              f"gap at E_c = {2*dd[0]:.4f}")
