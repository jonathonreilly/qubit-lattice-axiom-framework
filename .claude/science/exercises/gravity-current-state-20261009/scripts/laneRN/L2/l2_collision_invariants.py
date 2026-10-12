"""L2 / lane RN: exact linear-algebra search for a conserved additive momentum
in interacting lattice matter, via the on-shell 2<->2 condition.

Criterion used (see report): a conserved P = sum_x P(x) with one-body symbol f(k)
(the part acting on one-particle states) must satisfy
    f_A(k1) + f_B(k2) = f_A(k3) + f_B(k4)
on every on-shell 2-particle scattering pair with T != 0
(k1+k2 = k3+k4 mod 2pi, eps_A(k1)+eps_B(k2) = eps_A(k3)+eps_B(k4)).
For contact interactions T is a nonzero constant on the shell, so the condition holds
on the whole resonance set.  Body order >= 3 parts of P and the range of the two-body
part of P never enter.  We search f in the span of sin(n.k), |n|_inf <= R (any range R),
plus cos(n.k) as a control.
"""
import numpy as np, sys, time
from scipy.optimize import brentq
rng = np.random.default_rng(12345)

def make_disp(kind, m):
    if kind == 'KG':      # lattice Klein-Gordon (onsite phi^4 boson)
        f = lambda k: np.sqrt(m**2 + np.sum(4*np.sin(k/2)**2, axis=-1))
    elif kind == 'TB':    # tight-binding fermion (Hubbard)
        f = lambda k: -2*np.sum(np.cos(k), axis=-1)
    return f

def sample_res(d, epsA, epsB, N, tmin=0.05):
    """sample nontrivial on-shell 2->2 resonances"""
    out = []
    tries = 0
    tgrid = np.linspace(tmin, 2*np.pi*np.sqrt(d), 400)
    while len(out) < N:
        tries += 1
        if tries > 200*N:
            print(f"  [sampler: only {len(out)} nontrivial resonances in {tries} tries]"); break
        k1 = rng.uniform(-np.pi, np.pi, d); k2 = rng.uniform(-np.pi, np.pi, d)
        K = k1 + k2; E = epsA(k1) + epsB(k2)
        u = rng.normal(size=d); u /= np.linalg.norm(u)
        k3s = k1[None, :] + tgrid[:, None]*u[None, :]
        g = epsA(k3s) + epsB(K[None, :] - k3s) - E
        idx = np.where(np.sign(g[:-1]) != np.sign(g[1:]))[0]
        if len(idx) == 0: continue
        i = idx[rng.integers(len(idx))]
        G = lambda t: epsA(k1 + t*u) + epsB(K - k1 - t*u) - E
        try:
            t = brentq(G, tgrid[i], tgrid[i+1], xtol=1e-14)
        except ValueError:
            continue
        k3 = k1 + t*u; k4 = K - k3
        # drop near-trivial (k3 ~ k1 or, for equal species, k3 ~ k2)
        w = lambda a: (a + np.pi) % (2*np.pi) - np.pi
        if np.linalg.norm(w(k3 - k1)) < 1e-3: continue
        out.append(np.concatenate([w(k1), w(k2), w(k3), w(k4)]))
    return np.array(out)

def nvecs(d, R, half=True):
    import itertools
    ns = [n for n in itertools.product(range(-R, R+1), repeat=d) if any(n)]
    if half:  # one of each +-n pair
        ns = [n for n in ns if tuple(n) > tuple(-np.array(n))]
    return np.array(ns, dtype=float)

def design(res, d, ns, trig, two_species):
    k = [res[:, i*d:(i+1)*d] for i in range(4)]
    s = [1, 1, -1, -1]
    if not two_species:
        A = sum(si*trig(k[i] @ ns.T) for i, si in enumerate(s))
        return A
    # independent f_A (on k1,k3) and f_B (on k2,k4)
    AA = trig(k[0] @ ns.T) - trig(k[2] @ ns.T)
    AB = trig(k[1] @ ns.T) - trig(k[3] @ ns.T)
    return np.hstack([AA, AB])

def umklapp_mask(res, d):
    k = [res[:, i*d:(i+1)*d] for i in range(4)]
    n = np.round((k[0] + k[1] - k[2] - k[3])/(2*np.pi))
    return np.any(n != 0, axis=1)

def nullity(A, tol=1e-9):
    sv = np.linalg.svd(A, compute_uv=False)
    return int(np.sum(sv < tol*sv[0])), sv

def best_defect(res, d, R, two_species, ball_w=1e3, kball=0.6):
    """min RMS(sum s f_x) with (a) f'(0)=1 only, (b) f_x = k_x on |k|<kball (weighted)."""
    ns = nvecs(d, R)
    A = design(res, d, ns, np.sin, two_species)
    nb = ns.shape[0]
    # derivative d f_x / d k_x at 0 = sum n_x c_n
    dcon = ns[:, 0].copy()
    if two_species: dcon = np.concatenate([dcon, dcon])  # both species normalised (universality)
    # (a): minimise |A c|^2 s.t. dcon.c = 1 (two species: each species separately normalised)
    M = A.T @ A / A.shape[0]
    if two_species:
        C = np.zeros((2, 2*nb)); C[0, :nb] = ns[:, 0]; C[1, nb:] = ns[:, 0]; b = np.ones(2)
    else:
        C = dcon[None, :]; b = np.ones(1)
    KKT = np.block([[2*M + 1e-12*np.eye(M.shape[0]), C.T], [C, np.zeros((C.shape[0], C.shape[0]))]])
    sol = np.linalg.solve(KKT, np.concatenate([np.zeros(M.shape[0]), b]))
    ca = sol[:M.shape[0]]
    Da = np.sqrt(np.mean((A @ ca)**2))
    # (b): IR-ball fidelity
    kb = rng.uniform(-kball, kball, (4000, d)); kb = kb[np.linalg.norm(kb, axis=1) < kball]
    B = np.sin(kb @ ns.T)
    if two_species:
        B = np.block([[B, np.zeros_like(B)], [np.zeros_like(B), B]]); tgt = np.concatenate([kb[:, 0], kb[:, 0]])
    else:
        tgt = kb[:, 0]
    Abig = np.vstack([A/np.sqrt(A.shape[0]), np.sqrt(ball_w)*B/np.sqrt(B.shape[0])])
    rhs = np.concatenate([np.zeros(A.shape[0]), np.sqrt(ball_w)*tgt/np.sqrt(B.shape[0])])
    cb, *_ = np.linalg.lstsq(Abig, rhs, rcond=None)
    Db = np.sqrt(np.mean((A @ cb)**2)); IRb = np.sqrt(np.mean((B @ cb - tgt)**2))
    um = umklapp_mask(res, d)
    Db_n = np.sqrt(np.mean((A[~um] @ cb)**2)) if (~um).any() else np.nan
    Db_u = np.sqrt(np.mean((A[um] @ cb)**2)) if um.any() else np.nan
    return Da, Db, IRb, Db_n, Db_u, um.mean()

if __name__ == '__main__':
    cases = [  # (label, d, kindA, mA, kindB, mB, two_species, N, Rlist)
        ('1D onsite phi^4 (KG m=1)', 1, 'KG', 1.0, 'KG', 1.0, False, 3000, [1, 2, 4, 8, 16, 32]),
        ('1D Hubbard (TB, up-down contact)', 1, 'TB', 0, 'TB', 0, False, 100, [1, 2, 4, 8, 16, 32]),
        ('2D onsite phi^4 (KG m=1)', 2, 'KG', 1.0, 'KG', 1.0, False, 6000, [1, 2, 4, 6, 8]),
        ('2D Hubbard (TB)', 2, 'TB', 0, 'TB', 0, False, 6000, [1, 2, 4, 6, 8]),
        ('3D onsite phi^4 (KG m=1)', 3, 'KG', 1.0, 'KG', 1.0, False, 8000, [1, 2, 3, 4]),
        ('3D onsite phi^4 (KG m=0.2)', 3, 'KG', 0.2, 'KG', 0.2, False, 8000, [1, 2, 3, 4]),
        ('3D Hubbard (TB)', 3, 'TB', 0, 'TB', 0, False, 8000, [1, 2, 3, 4]),
        ('3D two-species contact (KG mA=1, mB=0.5)', 3, 'KG', 1.0, 'KG', 0.5, True, 8000, [1, 2, 3, 4]),
    ]
    for lab, d, kA, mA, kB, mB, two, N, Rl in cases:
        t0 = time.time()
        eA = make_disp(kA, mA); eB = make_disp(kB, mB)
        res = sample_res(d, eA, eB, N)
        if len(res) < 50:
            print(f"\n== {lab}: no nontrivial 2->2 resonances found (found {len(res)}); every f passes the 2->2 test"); continue
        # check resonance residuals
        k = [res[:, i*d:(i+1)*d] for i in range(4)]
        err = np.max(np.abs(eA(k[0]) + eB(k[1]) - eA(k[2]) - eB(k[3])))
        print(f"\n== {lab}: {N} nontrivial resonances, max energy residual {err:.1e}, umklapp fraction {umklapp_mask(res,d).mean():.3f}")
        for R in Rl:
            ns = nvecs(d, R)
            A_odd = design(res, d, ns, np.sin, two)
            A_even = design(res, d, ns, np.cos, two)
            if A_odd.shape[1] > A_odd.shape[0]:
                print(f"  R={R}: basis {A_odd.shape[1]} > samples, skip"); continue
            n_odd, sv_o = nullity(A_odd); n_even, sv_e = nullity(A_even)
            Da, Db, IRb, Dn, Du, uf = best_defect(res, d, R, two)
            print(f"  R={R:2d} odd basis {A_odd.shape[1]:5d}: odd-nullity {n_odd:4d} (sv_min/sv_max {sv_o[-1]/sv_o[0]:.2e}); "
                  f"even-nullity {n_even} (+const not in basis) | min defect f'(0)=1: {Da:.3e} | IR-ball(|k|<0.6) fit: defect {Db:.3e} "
                  f"[normal {Dn:.3e}, umklapp {Du:.3e}], IR err {IRb:.1e}")
        print(f"  ({time.time()-t0:.1f}s)"); sys.stdout.flush()
