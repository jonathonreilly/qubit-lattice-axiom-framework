"""R9-5 common: R7-1's free box dispersion on the dimer lattice of the Kitaev brick wall, and
translation-covariant Kitaev strings.

Brick wall in Z^2 (as R7-3): vertical (z) bond (X,Y)-(X,Y+1) iff X+Y even; x bond A(X,Y)-B(X+1,Y);
y bond A(X,Y)-B(X-1,Y); A = X+Y even.  Dimer (unit cell) n = (n1,n2): A at (X,Y) = (n1+n2, n1-n2),
B at (X, Y+1).  Dimer Bravais vectors e1 = (1,1), e2 = (1,-1) in Z^2 (orthogonal, equal length, so the
dimer-coordinate Euclidean metric is the Z^2 metric up to the factor 2).
Bond moves (dimer displacement):  from A: x -> B(n+e2), y -> B(n-e1), z -> B(n);
                                   from B: x -> A(n-e2), y -> A(n+e1), z -> A(n).
"""
import numpy as np

# ---------------- R7-1's literal box law (B = 2.0, B2 = 3.1, m = 0.3) ----------------
Bbox, B2, MASS = 2.0, 3.1, 0.3

def sstep(x):
    x = np.clip(x, 0.0, 1.0)
    with np.errstate(divide='ignore', over='ignore', invalid='ignore'):
        e1 = np.where(x > 0, np.exp(-1.0/np.where(x > 0, x, 1)), 0.0)
        e2 = np.where(x < 1, np.exp(-1.0/np.where(x < 1, 1-x, 1)), 0.0)
    return e1/(e1+e2)

def wrap(k):
    return -(((-k) + np.pi) % (2*np.pi) - np.pi)

def rho(k):
    return sstep((B2 - np.abs(wrap(k)))/(B2 - Bbox))

def s(k):
    k = wrap(k); r = rho(k)
    return r*k + (1-r)*np.sin(k)

def eps(k1, k2, m=MASS):
    return np.sqrt(m*m + s(k1)**2 + s(k2)**2)

def hopping_M(N=1024, m=MASS):
    """Real even Fourier coefficients M(r) of eps on the dimer lattice: eps(k) = sum_r M(r) e^{i k.r}.
    Returned as an N x N array indexed by r mod N."""
    k = 2*np.pi*np.fft.fftfreq(N)
    K1, K2 = np.meshgrid(k, k, indexing='ij')
    E = eps(K1, K2, m)
    Mr = np.fft.fft2(E)/N**2          # M(r) = (1/N^2) sum_k eps(k) e^{-i k r}
    return Mr.real, np.abs(Mr.imag).max()

def momentum_q(N=1024):
    """P_1 = dGamma(s(k1)): kernel p(r) = (1/N^2) sum_k s(k1) e^{-ikr} (purely imaginary, odd)."""
    k = 2*np.pi*np.fft.fftfreq(N)
    K1, K2 = np.meshgrid(k, k, indexing='ij')
    pr = np.fft.fft2(s(K1))/N**2
    return pr

# ---------------- translation-covariant paths ----------------
E1, E2 = np.array([1, 0]), np.array([0, 1])   # dimer-coordinate unit vectors

def _pairs(r1, r2, start):
    """List of (bond, from_sublattice) moves realising dimer displacement (r1,r2) by pairs of steps,
    starting on sublattice `start` ('A' or 'B') and returning to it.  Diagonal pairs first, then axis pairs."""
    mv = []
    if start == 'A':
        diag_p, diag_m = ['x', 'y'], ['y', 'x']          # A-x->B(+e2) -y->A(+e1): +(e1+e2) ; A-y->(-e1) -x->(-e2)
        ax = {(1, 0): ['z', 'y'], (-1, 0): ['y', 'z'], (0, 1): ['x', 'z'], (0, -1): ['z', 'x']}
    else:
        diag_p, diag_m = ['y', 'x'], ['x', 'y']          # B-y->A(+e1) -x->B(+e2) ; B-x->A(-e2) -y->B(-e1)
        ax = {(1, 0): ['y', 'z'], (-1, 0): ['z', 'y'], (0, 1): ['z', 'x'], (0, -1): ['x', 'z']}
    a1, a2 = r1, r2
    if a1 > 0 and a2 > 0:
        k = min(a1, a2); mv += diag_p*k; a1 -= k; a2 -= k
    elif a1 < 0 and a2 < 0:
        k = min(-a1, -a2); mv += diag_m*k; a1 += k; a2 += k
    mv += ax[(int(np.sign(a1)), 0)]*abs(a1) if a1 != 0 else []
    mv += ax[(0, int(np.sign(a2)))]*abs(a2) if a2 != 0 else []
    return mv

STEP = {('A', 'x'): (0, 1), ('A', 'y'): (-1, 0), ('A', 'z'): (0, 0),
        ('B', 'x'): (0, -1), ('B', 'y'): (1, 0), ('B', 'z'): (0, 0)}

def path(start_site, end_sub, r):
    """Sites visited from start_site=(n1,n2,sub) to the site of sublattice end_sub in dimer n+r.
    Returns list of sites (n1,n2,sub) and list of bonds (siteA, siteB, type)."""
    n1, n2, sub = start_site
    moves = _pairs(r[0], r[1], sub)
    if end_sub != sub:
        moves = moves + ['z']
    sites = [(n1, n2, sub)]; bonds = []
    cur = (n1, n2, sub)
    for b in moves:
        d = STEP[(cur[2], b)]
        nxt = (cur[0]+d[0], cur[1]+d[1], 'B' if cur[2] == 'A' else 'A')
        bonds.append((cur, nxt, b)); sites.append(nxt); cur = nxt
    assert cur == (n1+r[0], n2+r[1], end_sub), (start_site, end_sub, r, cur)
    return sites, bonds

def path_len_bound(r1, r2):
    """Length of the AB path for displacement r (number of bonds)."""
    return len(_pairs(r1, r2, 'A')) + 1
