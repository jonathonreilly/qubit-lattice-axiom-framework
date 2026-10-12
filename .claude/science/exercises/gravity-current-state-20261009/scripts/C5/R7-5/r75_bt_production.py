"""R7-5 script 2 (d = 1 lattice, continuous time): a pair-CREATING box law with an exactly
Lorentz-invariant dressed dispersion, versus instant-form comparators.

Species on the ring Z_L: a scalar phi (mass mu) and a complex scalar chi (mass m; chi, chibar).
Box dispersions (R7-1): eps(k) = sqrt(m^2 + s(k)^2), om(k) = sqrt(mu^2 + s(k)^2), s(k) = k on |k| <= B.
Sector at total lattice momentum P: { |phi(P)> } + { |chi(k) chibar(P-k)> }.

(a) BT mass-squared law with particle production (all orders, exact diagonalisation):
    M^2 = diag(mu^2, M0^2(k)) + U,  U_{k,phi} = g F(q(k)) sqrt(|dq/dk|_P * dk),
    q(k) = rest-frame relative momentum of the pair, F C^inf with compact support |q| < kap2.
    H = sqrt(M^2 + P^2) on the sector (lattice operator; in the box it is the BT Hamiltonian).
    Claim: E_phi(P)^2 - P^2 is P-independent (up to the finite-L Riemann sum), every order in g.
(b) Instant-form Lee vertex, same invariant F, Hamiltonian H = H0 + V with
    V_{k,phi} = g F(q) sqrt(dk/2pi)/sqrt(8 om(P) eps1 eps2)   (relativistic normalisation),
    no vacuum (Z-graph) term: exact diagonalisation.  Expect O(g^2) P-dependence of E^2 - P^2.
(c) Second order, instant form WITH the Z-graph (vacuum -> phi chi chibar), invariant F on both:
    2 om dE = sum |V|^2 [1/(om - W) + 1/(-om - W)] * 2 om   -> P-independent (Lorentz invariant).
(d) Second order, point vertex (F = 1, local cubic phi chi^dag chi), Z-graph included, the loop
    runs over the whole zone with the lattice dispersion: expect P-dependence (LV).
"""
import numpy as np
OUT = []
def pr(*a):
    s = ' '.join(str(x) for x in a); print(s, flush=True); OUT.append(s)

def sstep(x):
    x = np.clip(x, 0.0, 1.0)
    with np.errstate(divide='ignore', over='ignore', invalid='ignore'):
        e1 = np.where(x > 0, np.exp(-1.0/np.where(x > 0, x, 1)), 0.0)
        e2 = np.where(x < 1, np.exp(-1.0/np.where(x < 1, 1-x, 1)), 0.0)
    return e1/(e1+e2)
def plateau(x, x1, x2): return 1.0 - sstep((np.abs(x)-x1)/(x2-x1))
def wrap(k): return -(((-k) + np.pi) % (2*np.pi) - np.pi)

B, B2 = 2.6, 3.0
m, mu = 0.3, 0.5
KAP1, KAP2 = 0.25, 0.5
def s(k):
    k = wrap(k); r = plateau(k, B, B2); return r*k + (1-r)*np.sin(k)
def eps(k): return np.sqrt(m*m + s(k)**2)
def om(k): return np.sqrt(mu*mu + s(k)**2)
def F(q): return plateau(q, KAP1, KAP2)
A1, A2 = 1.4, 1.8      # leg cutoff (lattice momenta): removes the zone-edge (doubler) pairs, whose
                       # s-momenta are small; it equals 1 on the whole box-sector support used (checked)
def chi(k): return plateau(wrap(k), A1, A2)
def Fl(q, k1, k2): return F(q)*chi(k1)*chi(k2)

def pair_kin(P, L):
    k1 = wrap(2*np.pi*np.arange(L)/L); k2 = wrap(P - k1)
    e1, e2 = eps(k1), eps(k2)
    W = e1 + e2
    M02 = W*W - P*P                      # P = s(P) on the plateau (no umklapp checked below)
    # rest-frame relative momentum (1D): rapidities y_i = asinh(k_i/m) in the box; q = m sinh((y1-y2)/2)
    y1, y2 = np.arcsinh(s(k1)/m), np.arcsinh(s(k2)/m)
    q = m*np.sinh(0.5*(y1 - y2))
    # |dq/dk1| at fixed P: dq/dk1 = (m/2) cosh(eta) (dy1/dk1 + dy2/dk1*(-1)... ) with dk2/dk1 = -1
    eta = 0.5*(y1 - y2)
    dq = 0.5*m*np.cosh(eta)*(1/e1 + 1/e2)          # dy/dk = 1/eps in the box
    return k1, k2, e1, e2, W, M02, q, dq

def bt_dressed(P, L, g):
    k1, k2, e1, e2, W, M02, q, dq = pair_kin(P, L)
    on = Fl(q, k1, k2) > 0
    assert np.all(np.abs(k1[on]) < A1) and np.all(np.abs(k2[on]) < A1)   # chi = 1 on supp, legs in box
    dk = 2*np.pi/L
    u = g*Fl(q, k1, k2)*np.sqrt(dq*dk)
    n = L + 1
    M2 = np.zeros((n, n)); M2[0, 0] = mu*mu; M2[1:, 1:] = np.diag(M02)
    M2[0, 1:] = u; M2[1:, 0] = u
    z, v = np.linalg.eigh(M2)
    # H = sqrt(M^2 + P^2): dressed phi = lowest eigenvalue (below the pair threshold)
    E = np.sqrt(z[0] + P*P)
    return E, z[0], np.max(np.abs(k1[on])), np.max(np.abs(k2[on]))

def lee_dressed(P, L, g):
    k1, k2, e1, e2, W, M02, q, dq = pair_kin(P, L)
    dk = 2*np.pi/L
    v = g*Fl(q, k1, k2)*np.sqrt(dk/(2*np.pi))/np.sqrt(8*om(P)*e1*e2)
    n = L + 1
    H = np.zeros((n, n)); H[0, 0] = om(P); H[1:, 1:] = np.diag(W)
    H[0, 1:] = v; H[1:, 0] = v
    Ev = np.linalg.eigvalsh(H)
    return Ev[0]

def second_order(P, L, g, vertex):
    """2 om(P) dE(P) at O(g^2), on shell, instant-form OFPT with the Z-graph.
    vertex = 'inv' (F(q) of the pair) or 'point' (F = 1, whole zone, lattice dispersion)."""
    k1, k2, e1, e2, W, M02, q, dq = pair_kin(P, L)
    dk = 2*np.pi/L
    FF = Fl(q, k1, k2)**2 if vertex == 'inv' else np.ones_like(q)
    w = om(P)
    V2 = g*g*FF*(dk/(2*np.pi))/(8*w*e1*e2)
    # (a) phi -> chi chibar (pair momentum P); (b) Z-graph: vacuum -> phi(-P)... pair momentum -P,
    # by k -> -k symmetry of eps the pair energies are the same set; on-shell denominator -(om+W)
    dE_a = np.sum(V2/(w - W)); dE_b = np.sum(V2/(-w - W))
    return 2*w*(dE_a + dE_b), 2*w*dE_a

if __name__ == '__main__':
    pr('== (a) BT mass-squared law with pair creation: exact diagonalisation of the {phi} + {chi chibar} sector ==')
    for g in (0.1, 0.3, 0.38):
        for L in (400, 800, 1600):
            rows = []
            for n in range(0, 200):
                P = 2*np.pi*n/L
                if P > 0.7: break
                if n % max(1, int(0.1/(2*np.pi/L))) != 0: continue
                E, z, a1, a2 = bt_dressed(P, L, g)
                rows.append((P, E, E*E - P*P, a1))
            inv = np.array([r[2] for r in rows])
            pr(f'  g={g} L={L}: M_phys^2 = E^2-P^2 over P in [0,0.7] ({len(rows)} pts): mean {inv.mean():.12f} '
               f'spread {inv.max()-inv.min():.2e}; bare mu^2 = {mu*mu}; max |k| of a leg on supp F {max(r[3] for r in rows):.3f} < B={B}')
    pr('== (b) instant-form Lee vertex (one time ordering, no Z-graph), same invariant F: exact diagonalisation ==')
    for g in (0.3, 1.0):
        L = 1600
        rows = []
        for n in range(0, 200):
            P = 2*np.pi*n/L
            if P > 0.7: break
            if n % 25: continue
            E = lee_dressed(P, L, g); rows.append((P, E*E - P*P))
        inv = np.array([r[1] for r in rows])
        pr(f'  g={g} L={L}: E^2-P^2 at P = ' + ', '.join(f'{p:.3f}:{x:.8f}' for p, x in rows[::2]))
        pr(f'     spread {inv.max()-inv.min():.3e}  (mass shift mu^2 - mean = {mu*mu - inv.mean():.3e})')
    pr('== (c)/(d) O(g^2) instant form WITH the Z-graph: 2 om dE(P) must be P-independent for Lorentz invariance ==')
    for vertex in ('inv', 'point'):
        for L in (1600, 3200):
            vals = []
            for n in range(0, 400):
                P = 2*np.pi*n/L
                if P > 0.7: break
                if n % int(round(0.1/(2*np.pi/L))): continue
                full, onlya = second_order(P, L, 1.0, vertex)
                vals.append((P, full, onlya))
            f = np.array([v[1] for v in vals]); a = np.array([v[2] for v in vals])
            pr(f'  {vertex:5s} L={L}: 2om dE (with Z) spread over P in [0,0.7]: {f.max()-f.min():.3e} (mean {f.mean():.6e});'
               f'  without Z-graph: spread {a.max()-a.min():.3e}')
        if vertex == 'point':
            pr('    P-dependence of the point-vertex result (with Z): ' + ', '.join(f'{v[0]:.2f}:{v[1]:.6e}' for v in vals))
    with open(__file__.replace('.py', '.out'), 'w') as fh:
        fh.write('\n'.join(OUT) + '\n')
