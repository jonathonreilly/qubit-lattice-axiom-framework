"""Kill-round independent checks for T25 (Sonnet 5.5, same family as attacker).
K1: embedding-independent Schur argument against Z3 commuting with SM content on C^8 (6+2).
K2: independent derivation of the covariant NN Hermitian spinor class using only generators (C4z, C3[111]) and Hermiticity.
K3: unitary one-tick nearest-neighbour covariant spinor class: is there any nontrivial unitary member?
"""
import numpy as np, itertools
np.set_printoptions(precision=5, suppress=True, linewidth=140)
s = [np.array([[0,1],[1,0]],complex), np.array([[0,-1j],[1j,0]]), np.array([[1,0],[0,-1]],complex)]
I2 = np.eye(2, dtype=complex)

# ---------- K1: Schur ----------
# SM irreps on C^8: (3,2)_{1/3} dim 6 and (1,2)_{-1} dim 2, multiplicity free. Commutant of G_SM is C+C (dim 2).
# The tensor-position C3 has eigenvalues:
def perm8(perm):
    M = np.zeros((8,8), complex)
    for b in itertools.product(range(2), repeat=3):
        nb = tuple(b[perm[i]] for i in range(3))
        M[4*nb[0]+2*nb[1]+nb[2], 4*b[0]+2*b[1]+b[2]] = 1
    return M
C3 = perm8([2,0,1])
ev = np.round(np.angle(np.linalg.eigvals(C3))/(2*np.pi/3)).astype(int) % 3
print("K1 C3 eigenvalue classes (0=1, 1=w, 2=w^2) multiplicities:", {k:int((ev==k).sum()) for k in range(3)})
print("K1 element of commutant of multiplicity-free 6+2 has <=2 distinct eigenvalues; C3 has 3 => C3 cannot commute with G_SM on C^8 for ANY embedding of 6+2.")
# and C3 acting as an inner element (Z3 subset SU(3)_c) acts on 3-dim colour multiplets; then hw=1 would be a colour triplet, not a generation triplet.

# ---------- K2: covariant class from generators ----------
# rotor lifts of C4 about z and C3 about (1,1,1); axis-permutation action on hopping directions
def rot_axis_angle(n, th):
    n = np.array(n, float); n /= np.linalg.norm(n)
    Rm = np.eye(3)*np.cos(th) + (1-np.cos(th))*np.outer(n,n) + np.sin(th)*np.array([[0,-n[2],n[1]],[n[2],0,-n[0]],[-n[1],n[0],0]])
    D = np.cos(th/2)*I2 - 1j*np.sin(th/2)*sum(n[i]*s[i] for i in range(3))
    return np.round(Rm), D
gens = [rot_axis_angle([0,0,1], np.pi/2), rot_axis_angle([1,1,1], 2*np.pi/3), rot_axis_angle([1,0,0], np.pi/2)]
dirs = [(a, sg) for a in range(3) for sg in (1,-1)]
def herm_hop_basis():
    # unknowns: M0 (4 real, Hermitian), hop matrices for +e_a (8 real each, general complex 2x2); M_{-e_a}=M_a^dag
    B = []
    H = [np.array([[1,0],[0,0]],complex), np.array([[0,0],[0,1]],complex), np.array([[0,1],[1,0]],complex), np.array([[0,1j],[-1j,0]])]
    for h in H: B.append(('M0', h))
    for a in range(3):
        for i in range(2):
            for j in range(2):
                m = np.zeros((2,2),complex); m[i,j]=1
                B.append((a, m)); B.append((a, 1j*m))
    return B
B = herm_hop_basis()
def unpack(c):
    M0 = np.zeros((2,2),complex); Ma = [np.zeros((2,2),complex) for _ in range(3)]
    for ck,(key,m) in zip(c,B):
        if key=='M0': M0 += ck*m
        else: Ma[key] += ck*m
    return M0, Ma
def hopdict(Ma):
    d = {}
    for a in range(3): d[(a,1)] = Ma[a]; d[(a,-1)] = Ma[a].conj().T
    return d
rows = []
for R, D in gens:
    cols = []
    for k in range(len(B)):
        e = np.zeros(len(B)); e[k]=1
        M0, Ma = unpack(e); hd = hopdict(Ma)
        res = [M0 - D@M0@D.conj().T]
        for (a,sg), M in hd.items():
            v = np.zeros(3); v[a]=sg; w = R@v; a2 = int(np.argmax(abs(w))); s2 = int(round(w[a2]))
            res.append(hd[(a2,s2)] - D@M@D.conj().T)
        cols.append(np.concatenate([np.concatenate([r.real.ravel(), r.imag.ravel()]) for r in res]))
    rows.append(np.array(cols).T)
A = np.vstack(rows)
sv = np.linalg.svd(A, compute_uv=False)
print("K2 covariant Hermitian NN spinor class dimension (generators only):", len(B) - int((sv>1e-9).sum()))
# analytic: T_x = a + i c sigma_x, a,c real; H(k)=c0+2a sum cos k - 2c sigma.sin k ; touching iff sin k = 0 -> 8 corners
# ---------- K3: unitary one-tick NN class ----------
# covariant (no Hermiticity): M0 complex scalar, M_{+e_a} = alpha + beta sigma_a, M_{-e_a} = alpha - beta sigma_a (C2 about a perpendicular axis)
# U(k) = c0 + 2 alpha sum cos k_a + 2 i beta sum_a sigma_a sin k_a . Minimise ||U^dag U - 1|| over params and k-grid.
from scipy.optimize import minimize
ks = np.linspace(0, 2*np.pi, 9, endpoint=False)
K = np.array(list(itertools.product(ks, ks, ks)))
def Uk(p, k):
    c0 = p[0]+1j*p[1]; al = p[2]+1j*p[3]; be = p[4]+1j*p[5]
    return (c0 + 2*al*np.cos(k).sum())*I2 + 2j*be*sum(np.sin(k[a])*s[a] for a in range(3))
def loss(p):
    tot = 0.0
    for k in K:
        U = Uk(p, k); tot += np.linalg.norm(U.conj().T@U - I2)**2
    return tot/len(K)
rng = np.random.default_rng(0)
best = []
for t in range(30):
    p0 = rng.normal(size=6)
    r = minimize(loss, p0, method='BFGS')
    best.append((r.fun, r.x))
best.sort(key=lambda t: t[0])
print("K3 lowest residuals of U^dag U = 1 over the 6-parameter covariant one-tick class:", [round(b[0],6) for b in best[:6]])
p = best[0][1]
print("K3 best member: beta=", p[4]+1j*p[5], " (beta ~ 0 means the rule is the trivial scalar step; a beta != 0 unitary member would be a nontrivial NN tick)")
