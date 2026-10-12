"""R15-5 s1: exact-constraint N-type tensor gauge theory on Z^3 (midpoint symbols qhat=2 sin(k/2)).

Pre-registered checks (written before running):
 (1) extended Hessian of H_N on the 6 pairs is indefinite (PSD of Lemma P/Thm G/G-mix/Thm C fails);
 (2) physical (reduced) phase space V(k) = ker G ∩ ker S has dim 2 for k != 0 in every direction;
 (3) reduced frequencies: exactly 2 branches, linear, omega^2 = J g qhat^2 (isotropic at small k);
 (4) stabilizer characters of V along C4 axis, C3 body diagonal, C2' face diagonal = helicity +-2 values
     (-1,-1), (w,wbar), (+1,+1);
 (5) reduced Hamiltonian positive on the whole zone except k=0 (no doubler);
 (6) projector onto V is discontinuous at k=0 (Theorem C's continuity boundary);
 (7) static scalar source S h = rho: minimum field energy is negative ~ -rho^2/qhat^2 (attractive 1/r);
 (8) variants: rotor (E integer, h compact): h-side |R(h)|^2 -> omega ~ k^2;
     dual rotor (h integer, E compact): E-side |C(E)|^2 -> omega ~ k^2; both compact (H_L) -> k^3.
Conventions: orthonormal basis of Sym^2 (6 dims); canonical pairing E:hdot.
"""
import numpy as np
np.set_printoptions(precision=6, suppress=True)

# orthonormal basis of symmetric 3x3 matrices
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

eps = np.zeros((3, 3, 3))
for (a, b, c), s in {(0,1,2):1,(1,2,0):1,(2,0,1):1,(0,2,1):-1,(2,1,0):-1,(1,0,2):-1}.items():
    eps[a, b, c] = s

def qhat(k): return 2*np.sin(np.asarray(k, float)/2)

def ops(k):
    q = qhat(k)
    # G: Sym2 -> R^3, (G E)_j = q_i E_ij
    G = np.array([[np.sum(q[:, None]*mat(e)[:, :])[()] if False else (q @ mat(e))[j] for e in np.eye(6)] for j in range(3)])
    # S: Sym2 -> R, S h = q_i q_j h_ij - q^2 tr h   (vector-gauge invariant)
    S = np.array([[q @ mat(e) @ q - (q @ q)*np.trace(mat(e)) for e in np.eye(6)]])
    # R(h)_ij = eps_iab eps_jcd q_a q_c h_bd  (linearized curvature, symmetric, divergence free)
    def Rop(H):
        # Fourier symbol of R_ij = eps_iab eps_jcd d_a d_c h_bd : d -> i q gives an overall minus sign
        return -np.einsum('iab,jcd,a,c,bd->ij', eps, eps, q, q, H)
    R = np.array([vec(Rop(mat(e))) for e in np.eye(6)]).T
    # C(E)_ij = eps_iab q_a (E_bj - delta_bj trE/2), symmetrized (scalar-gauge-invariant E-character content)
    def Cop(E):
        X = np.einsum('iab,a,bj->ij', eps, q, E - np.eye(3)*np.trace(E)/2)
        return (X + X.T)/2
    C = np.array([vec(Cop(mat(e))) for e in np.eye(6)]).T
    one = vec(np.eye(3))
    K = np.eye(6) - 0.5*np.outer(one, one)        # E:E - (trE)^2/2
    return q, G, S, R, C, K

def null(A, tol=1e-10):
    u, s, vt = np.linalg.svd(A)
    r = np.sum(s > tol*max(1, s.max() if s.size else 1))
    return vt[r:].T

def physV(k):
    q, G, S, R, C, K = ops(k)
    A = np.vstack([G, S])
    return null(A)

J, g = 1.0, 1.0
print("== (1) extended Hessian of H_N at k = 0.3 z ==")
q, G, S, R, C, K = ops([0, 0, 0.3])
print("eig K (E side):", np.linalg.eigvalsh(J*K))
print("eig R (h side, /qhat^2):", np.linalg.eigvalsh(g*R)/(q@q))
print("checks: |R G^T|=%.1e (R vector-gauge inv), |S G^T|=%.1e (constraints commute), |G R|=%.1e (R div-free)" % (
    np.abs(R@G.T).max(), np.abs(S@G.T).max(), np.abs(G@R).max()))
# K scalar-gauge invariant on G=0: P_kerG K S^T = 0 ?
PG = null(G); print("|P_kerG K S^T| = %.1e  (K weakly invariant on G=0)" % np.abs(PG.T@K@S.T).max())
print("|C S^T| = %.1e (C scalar-gauge invariant)" % np.abs(C@S.T).max())

def reduced(k, Eside, hside):
    V = physV(k)
    Kv = V.T@Eside@V; Rv = V.T@hside@V
    w2 = np.linalg.eigvals(Kv@Rv)
    return V, np.sort(np.sqrt(np.abs(w2.real))), Kv, Rv

dirs = {'axis z': [0, 0, 1], 'face (110)': [1, 1, 0], 'body (111)': [1, 1, 1], 'generic (1,2,5)': [1, 2, 5], 'generic (2,1,3)': [2, 1, 3]}
print("\n== (2,3) reduced phase space and frequencies (CCR N-type) ==")
for name, d in dirs.items():
    d = np.array(d, float); d /= np.linalg.norm(d)
    out = []
    for t in [1e-2, 1e-3]:
        q, G, S, R, C, K = ops(t*d)
        V, w, Kv, Rv = reduced(t*d, J*K, g*R)
        out.append((V.shape[1], w/t))
    print("%-16s dimV=%d  omega/|k| at 1e-2: %s  at 1e-3: %s  min eig Kv,Rv/q^2 = %.4f, %.4f" % (
        name, out[0][0], out[0][1], out[1][1], np.linalg.eigvalsh(Kv).min(), np.linalg.eigvalsh(Rv).min()/(qhat(1e-3*d)@qhat(1e-3*d))))

# (4) stabilizer characters on V
def rot(axis, ang):
    a = np.array(axis, float); a /= np.linalg.norm(a)
    Kx = np.array([[0, -a[2], a[1]], [a[2], 0, -a[0]], [-a[1], a[0], 0]])
    return np.eye(3) + np.sin(ang)*Kx + (1-np.cos(ang))*Kx@Kx
def act(Rm):  # action on Sym2 coordinates
    return np.array([vec(Rm@mat(e)@Rm.T) for e in np.eye(6)]).T
print("\n== (4) stabilizer eigenvalues on physical V (k small along the axis) ==")
for name, axis, ang in [('C4 about z', [0, 0, 1], np.pi/2), ('C3 about 111', [1, 1, 1], 2*np.pi/3), ("C2' about 110", [1, 1, 0], np.pi)]:
    V = physV(1e-3*np.array(axis, float)/np.linalg.norm(axis))
    Dm = V.T@act(rot(axis, ang))@V
    print("%-14s eigenvalues: %s   (closure |V V^T D V - D V| = %.1e)" % (name, np.round(np.linalg.eigvals(Dm), 6),
          np.abs(V@V.T@act(rot(axis, ang))@V - act(rot(axis, ang))@V).max()))

# (5) whole-zone positivity of reduced blocks
print("\n== (5) whole zone: min eigenvalues of reduced K_V and R_V/qhat^2 on a 16^3 grid (k != 0) ==")
mins = [np.inf, np.inf, np.inf]; maxw = 0
grid = 2*np.pi*np.arange(16)/16 - np.pi
for kx in grid:
    for ky in grid:
        for kz in grid:
            k = np.array([kx, ky, kz])
            if np.allclose(k, 0): continue
            q, G, S, R, C, K = ops(k)
            V = physV(k)
            if V.shape[1] != 2: mins[2] = min(mins[2], -V.shape[1]); continue
            mins[0] = min(mins[0], np.linalg.eigvalsh(V.T@K@V).min())
            mins[1] = min(mins[1], np.linalg.eigvalsh(V.T@R@V).min()/(q@q))
print("min eig K_V = %.6f ; min eig R_V/qhat^2 = %.6f ; dimV != 2 anywhere: %s" % (mins[0], mins[1], "no" if mins[2]==np.inf else "YES"))

# (6) discontinuity of the physical bundle at k = 0
print("\n== (6) projector onto V: ||P(e z) - P(e x)|| as e -> 0 ==")
for e in [1e-2, 1e-4, 1e-6]:
    Pz = physV([0, 0, e]); Px = physV([e, 0, 0])
    print("e=%.0e  ||Pz - Px||_2 = %.4f" % (e, np.linalg.norm(Pz@Pz.T - Px@Px.T, 2)))

# (7) static scalar source: minimize (g/2) h.R h subject to S h = rho, h ⊥ range(G^T)
print("\n== (7) static scalar-source energy ==")
for kk in [0.3, 0.1, 0.03]:
    for d in [[0, 0, 1], [1, 1, 1]]:
        k = kk*np.array(d, float)/np.linalg.norm(d)
        q, G, S, R, C, K = ops(k)
        Pg = null(G)          # h ⊥ range(G^T) == ker G (gauge-fixed representative)
        Rr = Pg.T@R@Pg; Sr = S@Pg
        # stationary point of 1/2 h R h with S h = 1 (unit source): KKT
        n = Pg.shape[1]
        KKT = np.block([[g*Rr, Sr.T], [Sr, np.zeros((1, 1))]])
        sol = np.linalg.solve(KKT, np.concatenate([np.zeros(n), [1.0]]))
        h = sol[:n]; En = 0.5*g*h@Rr@h
        print("|k|=%.2f dir=%s  E_static(rho=1) = %.6f ; E*qhat^2 = %.6f" % (kk, d, En, En*(q@q)))

# (8) variants
print("\n== (8) variants: number of physical branches and exponent z (fit over |k| = 1e-2..1e-3 along (1,2,5)) ==")
d = np.array([1, 2, 5], float); d /= np.linalg.norm(d)
def zfit(Eform, hform):
    ws = []
    ts = [1e-2, 1e-3]
    for t in ts:
        q, G, S, R, C, K = ops(t*d)
        EE = {'K': K, 'CC': C.T@C}[Eform]; hh = {'R': R, 'RR': R.T@R}[hform]
        V, w, Kv, Rv = reduced(t*d, EE, hh)
        ws.append(w)
    ws = np.array(ws)
    return ws.shape[1], np.log(ws[0]/ws[1])/np.log(ts[0]/ts[1])
for name, Ef, hf in [('CCR N-type   (K, h:R(h))', 'K', 'R'), ('rotor: E in Z, h compact   (K, |R(h)|^2)', 'K', 'RR'),
                     ('dual rotor: h in Z, E compact (|C(E)|^2, h:R(h))', 'CC', 'R'), ('both compact, H_L (|C(E)|^2, |R(h)|^2)', 'CC', 'RR')]:
    nb, z = zfit(Ef, hf)
    print("%-52s branches=%d  z=%s" % (name, nb, np.round(z, 4)))
print("gauge checks for variants: |R^T R G^T| = %.1e ; |C^T C S^T| = %.1e" % (np.abs(R.T@R@G.T).max(), np.abs(C.T@C@S.T).max()))
