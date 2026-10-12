"""R16-7 s1 (written before running): exact lattice symbols for the f-sum m1(k) and the Bogoliubov
ratio, tensor class vs U(1) control.  Conventions copied from R15-5 s1 (midpoint symbols qhat=2sin(k/2),
orthonormal Sym2 basis; N0914:87-100,200-201).
Pre-registered expectations:
 (T1) vector-invariant h-characters (R-rows, S-rows, random local combinations) -> m1_TT(k) ~ k^4 (slope 4);
      S-rows contribute exactly 0 on TT.
 (T2) Bogoliubov ratio |<[E_TT,A]>|^2/m1 for A = curvature character -> O(1) constant, so chi_TT >= c/k^4.
 (T3) non-invariant D0-type term (kappa/2) sin(h).B_N.sin(h) [R13-2 s4] -> m1_TT ~ k^2 (slope 2), and it
      does not commute with the vector Gauss law (|G-commutator symbol| != 0).
 (T4) CCR saturation: N-type chi_hh = 1/(g qhat^2) = 1/m1 ; L-type 1/(g qhat^4) = 1/m1.
 (C1) U(1) control (cubic lattice, plaquette characters, div E = 0): m1_T(k) ~ k^2 (slope 2), ratio O(1),
      chi_T >= c/k^2: same exponent as the photon; Maxwell CCR saturates (chi_AA = 1/(K qhat^2) = 1/m1).
Unit expectation values <char> = 1 are used (m1 is linear in them; they are k-independent constants).
"""
import numpy as np
np.set_printoptions(precision=5, suppress=True)

def sym_basis():
    B = []
    for i in range(3):
        M = np.zeros((3, 3)); M[i, i] = 1; B.append(M)
    for (i, j) in [(0, 1), (1, 2), (0, 2)]:
        M = np.zeros((3, 3)); M[i, j] = M[j, i] = 1/np.sqrt(2); B.append(M)
    return B
B = sym_basis()
def vec(M): return np.array([np.sum(M*b) for b in B])
def mat(v): return sum(vi*b for vi, b in zip(v, B))
eps3 = np.zeros((3, 3, 3))
for (a, b, c), s in {(0,1,2):1,(1,2,0):1,(2,0,1):1,(0,2,1):-1,(2,1,0):-1,(1,0,2):-1}.items():
    eps3[a, b, c] = s
def qhat(k): return 2*np.sin(np.asarray(k, float)/2)

def ops(k):
    q = qhat(k)
    G = np.array([[(q @ mat(e))[j] for e in np.eye(6)] for j in range(3)])
    S = np.array([[q @ mat(e) @ q - (q @ q)*np.trace(mat(e)) for e in np.eye(6)]])
    def Rop(H): return -np.einsum('iab,jcd,a,c,bd->ij', eps3, eps3, q, q, H)
    R = np.array([vec(Rop(mat(e))) for e in np.eye(6)]).T
    one = vec(np.eye(3)); K = np.eye(6) - 0.5*np.outer(one, one)
    return q, G, S, R, K

def null(A, tol=1e-12):
    u, s, vt = np.linalg.svd(A); r = np.sum(s > tol*max(1, s.max())); return vt[r:].T

dirs = {'axis': [0,0,1], 'face': [1,1,0], 'body': [1,1,1], 'gen125': [1,2,5], 'gen213': [2,1,3]}
ks = np.array([1e-3, 3e-3, 1e-2, 3e-2, 0.1, 0.3])
rng = np.random.default_rng(7)
# random local invariant patterns: m(k) = R(k) a(k) + S^T(k) b(k), a,b = random trig polynomials (support <= 1 step)
shifts = [np.array(s) for s in [(0,0,0),(1,0,0),(0,1,0),(0,0,1),(-1,0,0),(0,-1,0),(0,0,-1)]]
A_coef = rng.integers(-2, 3, size=(5, len(shifts), 6)); B_coef = rng.integers(-2, 3, size=(5, len(shifts)))
def rand_patterns(k, R, S):
    out = []
    for p in range(5):
        a = sum(A_coef[p, s]*np.exp(1j*(shifts[s]@k)) for s in range(len(shifts)))
        b = sum(B_coef[p, s]*np.exp(1j*(shifts[s]@k)) for s in range(len(shifts)))
        out.append(R@a + S.T[:, 0]*b)
    return out

def slope(y): return np.polyfit(np.log(ks), np.log(y), 1)[0]

print("== (T1,T2,T3,T4) tensor class: m1_TT(k) per TT polarization, unit <char> ==")
for name, d in dirs.items():
    d = np.array(d, float); d /= np.linalg.norm(d)
    rows = {'R-rows': [], 'S-rows': [], 'random invariant': [], 'D0 sin.B.sin (non-inv)': [], 'Bogoliubov ratio (A=R-char)': [],
            'CCR N chi*m1': [], 'CCR L chi*m1': [], 'G-violation of D0 term': []}
    for t in ks:
        k = t*d; q, G, S, R, K = ops(k)
        V = null(np.vstack([G, S]))         # TT plane (2-dim), R15-5 Lemma E
        e = V[:, 0]                          # one TT polarization (real)
        # character symbols: R-rows -> column vectors R[:,a]; m1 = sum_a |e . R[:,a]|^2
        m1R = sum(abs(e @ R[:, a])**2 for a in range(6))
        m1S = abs(e @ S.T[:, 0])**2
        m1rand = sum(abs(e @ m)**2 for m in rand_patterns(k, R, S))
        # D0 term: Hessian symbol B_N = R (h:R(h)) acting slot-wise on non-invariant single-slot sines
        m1D0 = abs(e @ R @ e)
        # does the D0 term commute with G? single-slot characters have symbol e_a; G e_a != 0
        gviol = np.abs(G).max()
        # Bogoliubov numerator for A = sum_x e^{-ikx} sin(m_x.h), m = R-row a* maximizing overlap
        num = max(abs(e @ R[:, a])**2 for a in range(6))
        rows['R-rows'].append(m1R); rows['S-rows'].append(m1S); rows['random invariant'].append(m1rand)
        rows['D0 sin.B.sin (non-inv)'].append(m1D0); rows['Bogoliubov ratio (A=R-char)'].append(num/m1R)
        # CCR saturation: N-type: m1 = e.R.e (=qhat^2), chi_hh = 1/(e.R.e) ; L-type: m1 = |R e|^2, chi = 1/(e.R^T R.e)
        rows['CCR N chi*m1'].append((1/(e@R@e))*(e@R@e)); rows['CCR L chi*m1'].append((1/(e@R.T@R@e))*sum(abs(e@R[:,a])**2 for a in range(6)))
        rows['G-violation of D0 term'].append(gviol)
    print("-- direction %s" % name)
    for key, y in rows.items():
        y = np.array(y)
        if key in ('S-rows',):
            print("   %-30s max over k = %.2e (exactly zero on TT)" % (key, y.max()))
        elif key.startswith('CCR') or key.startswith('Bogoliubov') or key.startswith('G-viol'):
            print("   %-30s values: %s" % (key, np.round(y, 6)))
        else:
            print("   %-30s slope = %.4f ; y/|k|^p (p=round) at k=1e-3: %.6f" % (key, slope(y), y[0]/ks[0]**round(slope(y))))

print("\n== (C1) U(1) control: cubic lattice, links E_i, Gauss div E, plaquette characters m_n = curl rows ==")
for name, d in dirs.items():
    d = np.array(d, float); d /= np.linalg.norm(d)
    m1s, rat, sat = [], [], []
    for t in ks:
        k = t*d; q = qhat(k)
        curl = np.array([[0, -q[2], q[1]], [q[2], 0, -q[0]], [-q[1], q[0], 0]])  # rows: plaquette normals
        Gd = q[None, :]                        # div
        e = null(Gd)[:, 0]                     # transverse polarization
        m1 = sum(abs(e @ curl[n, :])**2 for n in range(3))
        num = max(abs(e @ curl[n, :])**2 for n in range(3))
        m1s.append(m1); rat.append(num/m1)
        sat.append((1/(e@curl.T@curl@e))*m1)   # Maxwell CCR chi_AA * m1
    print("   %-7s m1_T slope = %.4f ; m1/qhat^2 at 1e-3 = %.6f ; Bogoliubov ratio = %s ; Maxwell chi*m1 = %s" % (
        name, slope(np.array(m1s)), m1s[0]/(qhat(ks[0]*d)@qhat(ks[0]*d)), np.round(rat, 4), np.round(sat, 6)))
