"""F1 check C2: where a Golterman-Shamir 'bound-state' reduced model must put the extra light states
on the SPIN10 note's Wilson slab (SPIN10_..._2026-09-14.md:168-186).  See ../PREREG_C2.md."""
import numpy as np, itertools
sx = np.array([[0, 1], [1, 0]], complex); sy = np.array([[0, -1j], [1j, 0]]); sz = np.diag([1., -1]).astype(complex)
S3 = [sx, sy, sz]; I2 = np.eye(2)
out = []
def P(*a):
    s = " ".join(str(x) for x in a); print(s); out.append(s)

def slab(k, L):
    s = np.sin(k); b = np.sum(1 - np.cos(k))
    BL = b * np.eye(L) - np.diag(np.ones(L - 1), -1)          # (S_L)_{j+1,j}=1
    sd = sum(si * Si for si, Si in zip(s, S3))
    H = np.block([[np.kron(np.eye(L), sd), np.kron(BL, I2)],
                  [np.kron(BL.conj().T, I2), -np.kron(np.eye(L), sd)]])
    return H

def full(k, L, cls, Delta, r=1.0):
    Hs = slab(k, L); n = Hs.shape[0]
    s = np.sin(k); b = np.sum(1 - np.cos(k)); sd = sum(si * Si for si, Si in zip(s, S3))
    if cls == 'none': return Hs
    if cls == 'a': Hc = sd
    if cls == 'b': Hc = np.block([[sd, r * b * I2], [r * b * I2, -sd]])
    m = Hc.shape[0]
    H = np.zeros((n + m, n + m), complex); H[:n, :n] = Hs; H[n:, n:] = Hc
    iBL = slice(2 * L + 2 * (L - 1), 2 * L + 2 * L)              # B_L block
    H[iBL, n:n + 2] = Delta * I2; H[n:n + 2, iBL] = Delta * I2     # on-site B_L <-> chi
    return H

def chern_sphere(Hf, p0, eps=1e-3, nt=24, nph=48):
    th = np.linspace(1e-3, np.pi - 1e-3, nt); ph = np.linspace(0, 2 * np.pi, nph, endpoint=False)
    U = {}
    nocc = None
    for i, t in enumerate(th):
        for j, f in enumerate(ph):
            kk = p0 + eps * np.array([np.sin(t) * np.cos(f), np.sin(t) * np.sin(f), np.cos(t)])
            w, v = np.linalg.eigh(Hf(kk)); occ = v[:, w < 0]
            if nocc is None: nocc = occ.shape[1]
            assert occ.shape[1] == nocc and np.min(np.abs(w)) > 1e-9
            U[i, j] = occ
    def link(a, b):
        d = np.linalg.det(U[a].conj().T @ U[b]); return d / abs(d)
    C = 0.0
    for i in range(nt - 1):
        for j in range(nph):
            jp = (j + 1) % nph
            C += np.angle(link((i, j), (i, jp)) * link((i, jp), (i + 1, jp)) * link((i + 1, jp), (i + 1, j)) * link((i + 1, j), (i, j)))
    # caps (near poles) are tiny; the sphere is covered up to 1e-3 rad, residual flux negligible
    return C / (2 * np.pi)

Cref = chern_sphere(lambda kk: sum(ki * Si for ki, Si in zip(kk, S3)), np.zeros(3))
P(f"calibration: H=+sigma.k occupied-band Chern on sphere = {Cref:+.3f}  (define chirality R=+1 for H=+sigma.k)")
def chir(Hf, p0): return int(round(chern_sphere(Hf, p0) / Cref))

corners = [np.pi * np.array(c, float) for c in itertools.product((0, 1), repeat=3)]
def zero_scan(Hf, ngrid=16, tol=1e-6):
    ks = 2 * np.pi * np.arange(ngrid) / ngrid
    hits = []; mins = []
    for kk in itertools.product(ks, repeat=3):
        w = np.linalg.eigvalsh(Hf(np.array(kk))); m = np.min(np.abs(w)); mins.append(m)
        if m < tol: hits.append(tuple(np.round(np.array(kk) / np.pi, 3)))
    srt = np.sort(mins)
    return hits, srt[len(hits)] if len(hits) < len(srt) else None

def weights(H, n_slab, L):
    w, v = np.linalg.eigh(H); z = v[:, np.abs(w) < 1e-6]
    if z.shape[1] == 0: return None
    wt = np.sum(np.abs(z) ** 2, axis=1) / z.shape[1]
    lab = {}
    for j in range(L): lab[f"A{j+1}"] = wt[2*j:2*j+2].sum()
    for j in range(L): lab[f"B{j+1}"] = wt[2*L+2*j:2*L+2*j+2].sum()
    lab["chi"] = wt[n_slab:n_slab+2].sum() if len(wt) > n_slab else 0
    lab["chi'"] = wt[n_slab+2:n_slab+4].sum() if len(wt) > n_slab + 2 else 0
    return {k_: round(float(v_), 3) for k_, v_ in lab.items() if v_ > 1e-3}, z.shape[1]

for L in (2, 3):
    nsl = 4 * L
    for cls, Dl in [('none', 0.0)] + [(c, D) for c in ('a', 'b') for D in (0.3, 1.0, 3.0)]:
        Hf = lambda kk, cls=cls, Dl=Dl: full(kk, L, cls, Dl)
        hits, gapnext = zero_scan(Hf)
        nodes = []
        for p in hits:
            p0 = np.pi * np.array(p)
            H0 = Hf(p0); w = np.linalg.eigvalsh(H0); nz = int(np.sum(np.abs(w) < 1e-6))
            c = chir(Hf, p0); wt = weights(H0, nsl, L)
            nodes.append((p, nz // 2, c, wt[0] if wt else None))
        net = sum(nd[2] for nd in nodes)
        P(f"\nL={L} class={cls} Delta={Dl}: zero points on 16^3 grid = {len(hits)}; next-smallest |E| on grid = {gapnext:.3f}; NET chirality = {net:+d}")
        for nd in nodes:
            P(f"   p/pi={nd[0]}  #Weyl~{nd[1]}  chirality(sum)={nd[2]:+d}  zero-mode weights={nd[3]}")

open(__file__.replace('.py', '.out'), 'w').write("\n".join(out) + "\n")
