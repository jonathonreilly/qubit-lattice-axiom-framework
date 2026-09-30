import itertools, math, json
import numpy as np
exec(open('test_T26.py').read().split("# ------------- TEST A")[0])   # reuse operator definitions and g8 (prints sanity line)

def centre_dim(ops, n=8):
    d, basis = commutant_dim(ops, n)
    # centre of commutant = commutant ∩ bicommutant ; bicommutant = commutant of the commutant basis
    dd, bic = commutant_dim(basis, n)
    # intersection dim: matrices in span(basis) that also commute with all basis elements
    B = np.array([b.ravel() for b in basis]).T  # n^2 x d
    cons = np.vstack([np.array([ (np.kron(np.eye(n), b) - np.kron(b.T, np.eye(n))) @ B[:, k] for k in range(d)]).T for b in basis])
    s = np.linalg.svd(cons, compute_uv=False)
    return d, d - int(np.sum(s > 1e-9))
out = {}
print("== A': structure of commutants (commutant dim, centre dim)")
for name, ops in {"S_i=X_i": X, "Gamma_i (Cl3)": Gam if 'Gam' in dir() else [X[0], Z[0]@X[1], Z[0]@Z[1]@X[2]]}.items():
    d, c = centre_dim(ops)
    print(f"  {name}: commutant dim {d}, centre dim {c}", "-> abelian" if d == c else "-> non-abelian; blocks = centre dim; if 8=4+4 => M_2+M_2")
    out[name] = (d, c)

print("\n== B1: closure(g8, translations) vs su(4)_base + su(2)_weak")
S_T = close(g8, X)
def base_su4():
    gens = []
    # traceless anti-Hermitian on C^4 (Gell-Mann style for n=4), embedded as I_fibre (x) M_4 in the repo's fibre(x)base ordering, then rotated back by U
    def gmn(n):
        ms = []
        for i in range(n):
            for j in range(i+1, n):
                m = np.zeros((n, n), dtype=complex); m[i, j] = m[j, i] = 1; ms.append(m)
                m = np.zeros((n, n), dtype=complex); m[i, j] = -1j; m[j, i] = 1j; ms.append(m)
        for k in range(1, n):
            m = np.zeros((n, n), dtype=complex)
            for i in range(k): m[i, i] = 1
            m[k, k] = -k
            ms.append(m / math.sqrt(k*(k+1)/2))
        return ms
    for m in gmn(4):
        gens.append(1j * (U @ np.kron(np.eye(2), m) @ U.conj().T))
    return gens
target = close(base_su4() + g_su2)
print("  dim closure(g8,T) =", S_T.dim, "; dim su(4)_base+su(2)_w =", target.dim,
      "; closure ⊂ target:", all(target.contains(m) for m in S_T.mats), "; target ⊂ closure:", all(S_T.contains(m) for m in target.mats))
out["B1"] = dict(closure=S_T.dim, target=target.dim, equal=bool(all(target.contains(m) for m in S_T.mats) and all(S_T.contains(m) for m in target.mats)))
# su(4) part and 6 extra generators: the (3,1)+(3bar,1) leptoquark block
print("  extra generators beyond g8: ", S_T.dim - 12, "= 15-8-1 = 6 (leptoquark-type, (3)+(3bar) of su(3); charge under u(1)_Y direction)")

print("\n== B2: which pure translations X^t normalise g8 (map g8 into itself)?")
g8span = close(g8)
res = []
for t in itertools.product((0, 1), repeat=3):
    Ut = np.eye(8, dtype=complex)
    for a in range(3):
        if t[a]: Ut = Ut @ X[a]
    ok = all(g8span.contains(Ut @ m @ Ut.conj().T) for m in g8span.mats)
    res.append((t, ok))
print("  ", res)
out["B2"] = [(list(t), bool(ok)) for t, ok in res]

print("\n== C: bond test: su(3) on Sym^2(C^2) vs single-site operators A(x)1+1(x)B on two qubits")
s0 = np.eye(2, dtype=complex); px = np.array([[0,1],[1,0]],dtype=complex); py=np.array([[0,-1j],[1j,0]]); pz=np.diag([1,-1]).astype(complex)
loc = [np.kron(p, s0) for p in (s0, px, py, pz)] + [np.kron(s0, p) for p in (px, py, pz)]   # span of single-site ops (7 indep: 1 + 3 + 3)
locS = Span(4)
for m in loc: locS.add(1j*m)
e0_, e1_ = np.array([1,0],dtype=complex), np.array([0,1],dtype=complex)
Vs = np.column_stack([np.kron(e0_,e0_), (np.kron(e0_,e1_)+np.kron(e1_,e0_))/math.sqrt(2), np.kron(e1_,e1_)])   # 4x3 Sym basis
su3b = [1j * (Vs @ (l/2) @ Vs.conj().T) for l in lam]
# dimension of span(su3b) ∩ locS
A_ = np.array([vec(m) for m in su3b]).T
L_ = np.array([vec(m) for m in locS.mats]).T
# intersection dim = dim(A)+dim(L)-dim(A+L)
rk = lambda M: int(np.sum(np.linalg.svd(M, compute_uv=False) > 1e-9))
inter = rk(A_) + rk(L_) - rk(np.hstack([A_, L_]))
print(f"  dim su(3)_Sym = {rk(A_)}, dim(single-site ops) = {rk(L_)}, dim intersection = {inter} (=3: so(3), the diagonal spin-1; 5 quadrupole generators are two-site)")
out["C"] = dict(su3=rk(A_), local=rk(L_), inter=inter)

print("\n== D: isotropy of the derived selector's vacuum H(phi)=sum phi_i S_i")
for name, phi in {"axis vertex (1,0,0)": (1,0,0), "edge (1,1,0)": (1,1,0), "generic (1,.7,.3)": (1,.7,.3), "symmetric (1,1,1)": (1,1,1)}.items():
    H = sum(p*x for p, x in zip(phi, X))
    d, _ = commutant_dim([H])
    G_ = np.array([vec(comm(g, H)) for g in g8]).T
    inter = len(g8) - rk(G_)
    print(f"  phi={name}: isotropy (commutant of H) dim {d}; dim(g8 ∩ isotropy) = {inter}")
    out.setdefault("D", {})[name] = (d, inter)
json.dump(out, open('test_T26b_results.json', 'w'), indent=1, default=str)
