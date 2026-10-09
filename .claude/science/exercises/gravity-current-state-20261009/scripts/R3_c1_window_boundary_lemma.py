"""C1: window/boundary lemma for a covariant integrand on a fixed label-space window.

E_D(t) = int_D phi(k^T exp(-t h) k) d^3k/(2pi)^3, h traceless symmetric, tr h^2 = 1.
Claim (exact): E_D''(0) = int_D [phi'(|k|^2) k.h^2.k + phi''(|k|^2)(k.h.k)^2]
                       = 1/2 oint_{dD} phi'(|p|^2) (p.h.p)(p.h.n) dS        (all /(2pi)^3)
Ball radius L: E'' = phi'(L^2) L^5 tr(h^2) / (30 pi^2).  For phi=-sqrt(s): -L^4/(60 pi^2).
A window that follows the strain (D_t = exp(t h/2) D) gives E'' = 0 identically.
Checks: (i) sympy exact for the ball; (ii) cube [-pi,pi]^3: bulk vs boundary vs finite differences.
"""
import numpy as np
import sympy as sp
from numpy.polynomial.legendre import leggauss

# ---------- (i) ball, exact ----------
r, L, th, ph = sp.symbols('r L theta phi', positive=True)
def ball_hessian_exact(hmat, phi_s):
    s = sp.Symbol('s', positive=True)
    f = phi_s(s)
    f1 = sp.diff(f, s); f2 = sp.diff(f, s, 2)
    n = sp.Matrix([sp.sin(th)*sp.cos(ph), sp.sin(th)*sp.sin(ph), sp.cos(th)])
    H = sp.Matrix(hmat)
    k = r*n
    integrand = (f1.subs(s, r**2)*(k.T*H*H*k)[0] + f2.subs(s, r**2)*((k.T*H*k)[0])**2)
    val = sp.integrate(sp.integrate(sp.integrate(sp.simplify(integrand*r**2*sp.sin(th)), (ph, 0, 2*sp.pi)), (th, 0, sp.pi)), (r, 0, L))
    return sp.simplify(val/(2*sp.pi)**3)

hEg = sp.Matrix([[1, 0, 0], [0, -1, 0], [0, 0, 0]])/sp.sqrt(2)
hT2 = sp.Matrix([[0, 1, 0], [1, 0, 0], [0, 0, 0]])/sp.sqrt(2)
for name, hm in [('E_g', hEg), ('T_2g', hT2)]:
    v = ball_hessian_exact(hm, lambda s: -sp.sqrt(s))
    print(f"ball, phi=-sqrt(s), {name}: E'' = {v}   ; -L^4/(60 pi^2) match: {sp.simplify(v + L**4/(60*sp.pi**2)) == 0}")

# ---------- (ii) cube [-pi,pi]^3, numeric ----------
hE = np.array([[1, 0, 0], [0, -1, 0], [0, 0, 0]])/np.sqrt(2)
hT = np.array([[0, 1, 0], [1, 0, 0], [0, 0, 0]])/np.sqrt(2)
phi = lambda s: -np.sqrt(s)
phi1 = lambda s: -0.5/np.sqrt(s)
phi2 = lambda s: 0.25*s**-1.5

def gl(n, a, b):
    x, w = leggauss(n); return 0.5*(b-a)*x + 0.5*(b+a), 0.5*(b-a)*w

def bulk(h, n=120):
    # split each axis into [-pi,0],[0,pi] to keep the |k| kink at a node boundary
    xs, ws = [], []
    for a, b in [(-np.pi, 0.0), (0.0, np.pi)]:
        x, w = gl(n, a, b); xs.append(x); ws.append(w)
    x = np.concatenate(xs); w = np.concatenate(ws)
    K = np.stack(np.meshgrid(x, x, x, indexing='ij'), -1).reshape(-1, 3)
    W = np.einsum('i,j,k->ijk', w, w, w).reshape(-1)
    s = np.einsum('ni,ni->n', K, K)
    khk = np.einsum('ni,ij,nj->n', K, h, K)
    kh2k = np.einsum('ni,ij,nj->n', K, h@h, K)
    return np.sum(W*(phi1(s)*kh2k + phi2(s)*khk**2))/(2*np.pi)**3

def boundary(h, n=300):
    tot = 0.0
    x, w = gl(n, -np.pi, np.pi)
    U, V = np.meshgrid(x, x, indexing='ij'); WW = np.outer(w, w)
    for ax in range(3):
        for sgn in (+1, -1):
            o = [a for a in range(3) if a != ax]
            P = np.zeros(U.shape + (3,)); P[..., ax] = sgn*np.pi; P[..., o[0]] = U; P[..., o[1]] = V
            nvec = np.zeros(3); nvec[ax] = sgn
            s = np.einsum('...i,...i->...', P, P)
            php = np.einsum('...i,ij,...j->...', P, h, P)
            phn = np.einsum('...i,ij,j->...', P, h, nvec)
            tot += np.sum(WW*phi1(s)*php*phn)
    return 0.5*tot/(2*np.pi)**3

def E_of_t(h, t, n=120):
    xs, ws = [], []
    for a, b in [(-np.pi, 0.0), (0.0, np.pi)]:
        x, w = gl(n, a, b); xs.append(x); ws.append(w)
    x = np.concatenate(xs); w = np.concatenate(ws)
    K = np.stack(np.meshgrid(x, x, x, indexing='ij'), -1).reshape(-1, 3)
    W = np.einsum('i,j,k->ijk', w, w, w).reshape(-1)
    ev, evec = np.linalg.eigh(h)
    G = evec @ np.diag(np.exp(-t*ev)) @ evec.T
    s = np.einsum('ni,ij,nj->n', K, G, K)
    return np.sum(W*phi(s))/(2*np.pi)**3

for name, h in [('E_g', hE), ('T_2g', hT)]:
    b = bulk(h); bd = boundary(h)
    t = 1e-3
    fd = (E_of_t(h, t) - 2*E_of_t(h, 0) + E_of_t(h, -t))/t**2
    print(f"cube [-pi,pi]^3, phi=-sqrt(s), {name}: bulk {b:.8f}  boundary {bd:.8f}  finite-diff {fd:.6f}")
# reference: ball of equal volume (radius (6/pi)^(1/3) pi) and inscribed ball (radius pi)
for Lr, lab in [(np.pi, 'inscribed ball r=pi'), (np.pi*(6/np.pi)**(1/3), 'equal-volume ball')]:
    print(f"{lab}: -L^4/(60 pi^2) = {-Lr**4/(60*np.pi**2):.8f}")
