"""R19-10 probe (a)/(c) companion: ground-state energy of a lattice with the defect that LOCAL Z^d-preserving
insertion requires (R12-2: an inserted half-plane = dislocation; climb = insertion).  2D proxy, NN scalar.
Graph: Lx x Ly torus; rows y1 .. y1+l-1 carry one extra site (an inserted column segment of length l at x0):
a dislocation dipole (two cores, opposite Burgers vectors).  Law on the graph: H = (1/2) sum pi^2 +
(1/2) m^2 sum phi^2 + (1/2) sum_bonds (phi_i - phi_j)^2, i.e. K = m^2 + graph Laplacian (the same bond rule
everywhere; core sites have 3 bonds).  E0 = (1/2) sum sqrt(eig K).
Defect energy: dE(l) = E0(defected, N + l sites) - (N + l) e0_2D, with e0_2D the perfect-lattice value.
For large l, dE -> 2 delta_core (two cores).  A 3D dislocation line costs ~delta per lattice step along the core
(suggested proxy).  Lattice units.
"""
import numpy as np, time
T0 = time.time()
out = []
def pr(*a):
    s = ' '.join(str(x) for x in a); print(s, flush=True); out.append(s)

def e0_2d(m, L=400):
    k = 2*np.pi*np.arange(L)/L; s = 4*np.sin(k/2)**2
    return 0.5*np.sqrt(m*m + s[:, None] + s[None, :]).mean()

def graph_E0(Lx, Ly, x0, y1, l, m):
    rows = []                      # list of site ids per row, in x order
    nid = 0
    for y in range(Ly):
        n = Lx + (1 if y1 <= y < y1 + l else 0)
        rows.append(list(range(nid, nid + n))); nid += n
    K = np.zeros((nid, nid))
    def bond(a, b):
        K[a, a] += 1; K[b, b] += 1; K[a, b] -= 1; K[b, a] -= 1
    for y in range(Ly):
        r = rows[y]
        for i in range(len(r)):
            bond(r[i], r[(i+1) % len(r)])
        r2 = rows[(y+1) % Ly]
        if len(r) == len(r2):
            for i in range(len(r)): bond(r[i], r2[i])
        else:
            short, long_ = (r, r2) if len(r) < len(r2) else (r2, r)
            for i in range(len(short)):
                j = i if i <= x0 else i + 1          # long-row index x0+1 is the inserted site
                bond(short[i], long_[j])
    K += m*m*np.eye(nid)
    w = np.linalg.eigvalsh(K)
    return 0.5*np.sqrt(np.maximum(w, 0)).sum(), nid

for m in (1.0, 0.3, 0.1):
    e0 = e0_2d(m)
    pr('m=%.1f: e0_2D = %.8f' % (m, e0))
    for L in (24, 32):
        E0p, Np = graph_E0(L, L, L//2, L//4, 0, m)
        pr('   L=%d perfect torus: E0/N - e0 = %.2e' % (L, E0p/Np - e0))
        for l in (2, 4, 8, 12):
            E0d, Nd = graph_E0(L, L, L//2, L//2 - l//2, l, m)
            dE = E0d - Nd*e0
            dEp = E0d - E0p - l*e0
            pr('   L=%d l=%2d: dE = E0 - (N+l) e0 = %+.6f ; per core %+.6f ; [E0(def) - E0(perfect) - l e0 = %+.6f]'
               % (L, l, dE, dE/2, dEp))

# ---- 3D straight edge-dislocation pair = (2D dipole graph) x Z, exactly (product graph, separation of k_z) ----
pr('=== 3D straight edge dislocation lines (2D dipole x Z): energy per unit line length, per line ===')
pr('    delta_line = (1/2) int dk_z/(2 pi) dE_2D(m^2 + 4 sin^2(k_z/2)) [two lines in the dipole]; Gauss-Legendre in k_z')
xg, wg = np.polynomial.legendre.leggauss(12)
kz = 0.5*np.pi*(xg + 1); wz = 0.5*np.pi*wg/np.pi        # int_0^pi dk/pi  (even integrand)
for m in (1.0, 0.3, 0.0):
    L = 24; l = 8
    acc = 0.0
    for k, w in zip(kz, wz):
        meff = np.sqrt(m*m + 4*np.sin(k/2)**2)
        e0 = e0_2d(meff)
        E0d, Nd = graph_E0(L, L, L//2, L//2 - l//2, l, meff)
        acc += w*(E0d - Nd*e0)
    pr('   m=%.1f (L=%d, l=%d): delta_line = %+.5f per lattice step along the line (hbar c / a per a)' % (m, L, l, acc/2))
pr('elapsed %.1f s' % (time.time() - T0))
