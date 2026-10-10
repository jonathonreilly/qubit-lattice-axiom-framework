"""Lane RS / S1: does the staggered symmetry group (shift symmetries, which preserve the
reduced momentum k) act multiplicity-free on the degenerate band space D_+(k)?
If yes, the group-average of any collision invariant is diagonal in symmetry sectors
(scalar functions g^s(k)), and the matrix problem reduces to scalar (Spohn) problems.

Shift: (S_mu c)_x = xi_mu(x) c_{x+mu}, xi_mu(x) = (-1)^{sum_{nu>mu} x_nu}.  Checked here
numerically on a periodic lattice: [S_mu, h(m=0)] = 0; S_mu h(m) S_mu^+ = h(-m); for m != 0
the products S_mu S_nu (mu != nu) and translations by 2 commute with h.
"""
import numpy as np, itertools, sys

def lattice(d, L, m):
    sites = list(itertools.product(range(L), repeat=d)); idx = {s: i for i, s in enumerate(sites)}
    n = len(sites); h = np.zeros((n, n), complex)
    for x in sites:
        s = idx[x]
        for j in range(d):
            eta = (-1)**sum(x[:j])
            y = list(x); y[j] = (y[j]+1) % L; t = idx[tuple(y)]
            h[s, t] += 0.5j*eta; h[t, s] -= 0.5j*eta
        h[s, s] += m*(-1)**sum(x)
    def shift(mu):
        S = np.zeros((n, n), complex)
        for x in sites:
            y = list(x); y[mu] = (y[mu]+1) % L
            S[idx[x], idx[tuple(y)]] = (-1)**sum(x[mu+1:])
        return S
    def trans2(j):
        T = np.zeros((n, n), complex)
        for x in sites:
            y = list(x); y[j] = (y[j]+2) % L
            T[idx[x], idx[tuple(y)]] = 1
        return T
    return sites, h, [shift(mu) for mu in range(d)], [trans2(j) for j in range(d)]

def commutant_dim(mats):
    D = mats[0].shape[0]
    rows = [np.kron(np.eye(D), A) - np.kron(A.T, np.eye(D)) for A in mats]
    M = np.vstack(rows)
    sv = np.linalg.svd(M, compute_uv=False)
    return int(np.sum(sv < 1e-9*max(1, sv[0])))

for d, L in ((2, 8), (3, 4)):
    for m in (0.0, 0.5):
        sites, h, S, T = lattice(d, L, m)
        print(f"\n== d={d}, L={L}, m={m}")
        for mu in range(d):
            print(f"  ||[S_{mu+1}, h]|| = {np.linalg.norm(S[mu]@h - h@S[mu]):.1e};  ||S h S^+ - h(-m)|| = "
                  f"{np.linalg.norm(S[mu]@h@S[mu].conj().T - lattice(d, L, -m)[1]):.1e}")
        if m == 0:
            gens = S
        else:
            gens = [S[a]@S[b] for a in range(d) for b in range(a+1, d)]
            for g in gens: assert np.linalg.norm(g@h - h@g) < 1e-12
        # joint eigenspaces of translations by 2 (reduced momentum sectors)
        Tsum = sum((j+1)*np.pi*T[j] for j in range(d))  # commuting normal ops; diagonalize a generic combo
        Tc = sum(np.exp(0.37*(j+1))*T[j] for j in range(d))
        w, V = np.linalg.eig(Tc)
        # group eigenvectors by eigenvalue
        done = np.zeros(len(w), bool)
        res = []
        for i in range(len(w)):
            if done[i]: continue
            sel = np.where(np.abs(w - w[i]) < 1e-8)[0]; done[sel] = True
            Q, _ = np.linalg.qr(V[:, sel])
            hk = Q.conj().T @ h @ Q
            e, u = np.linalg.eigh(hk)
            if np.min(np.abs(e)) < 1e-6: continue   # skip k = 0 (degenerate cone point)
            Dp = u[:, e > 0]
            gk = [Dp.conj().T @ (Q.conj().T @ g @ Q) @ Dp for g in gens]
            # check closure: g restricted is unitary on D_+ (g commutes with h)
            res.append((len(sel), Dp.shape[1], commutant_dim(gk), np.round(np.linalg.eigvals(gk[0]), 3)))
        dims = {}
        for r in res: dims[(r[0], r[1], r[2])] = dims.get((r[0], r[1], r[2]), 0) + 1
        for key, c in sorted(dims.items()):
            print(f"  sectors with (orbit dim {key[0]}, dim D_+ {key[1]}): commutant dim of restricted symmetry group = {key[2]}  [{c} k-points]")
        sys.stdout.flush()

# multiplicity check for d=3, m=0.5: is the commutant of the restricted group commutative?
def commutant_basis(mats):
    D = mats[0].shape[0]
    M = np.vstack([np.kron(np.eye(D), A) - np.kron(A.T, np.eye(D)) for A in mats])
    u, sv, vh = np.linalg.svd(M)
    null = vh[sv.size - np.sum(sv < 1e-9*max(1, sv[0])):] if False else vh[np.sum(sv >= 1e-9*max(1, sv[0])):]
    return [v.reshape(D, D, order='F') for v in null.conj()]
print("\n== multiplicity check (is the commutant commutative?)")
for d, L, m in ((3, 4, 0.5), (3, 4, 0.0), (2, 8, 0.5)):
    sites, h, S, T = lattice(d, L, m)
    gens = S if m == 0 else [S[a]@S[b] for a in range(d) for b in range(a+1, d)]
    Tc = sum(np.exp(0.37*(j+1))*T[j] for j in range(d))
    w, V = np.linalg.eig(Tc)
    done = np.zeros(len(w), bool); out = []
    for i in range(len(w)):
        if done[i]: continue
        sel = np.where(np.abs(w - w[i]) < 1e-8)[0]; done[sel] = True
        Q, _ = np.linalg.qr(V[:, sel]); hk = Q.conj().T @ h @ Q
        e, u = np.linalg.eigh(hk)
        if np.min(np.abs(e)) < 1e-6: continue
        Dp = u[:, e > 0]
        gk = [Dp.conj().T @ (Q.conj().T @ g @ Q) @ Dp for g in gens]
        B = commutant_basis(gk)
        comm = max(np.linalg.norm(a@b - b@a) for a in B for b in B)
        out.append((len(B), comm))
    print(f"  d={d} m={m}: commutant dims {sorted(set(o[0] for o in out))}, max ||[X,Y]|| over commutant basis = {max(o[1] for o in out):.2e} "
          f"({'commutative => multiplicity-free' if max(o[1] for o in out) < 1e-8 else 'NON-commutative => multiplicity'})")
