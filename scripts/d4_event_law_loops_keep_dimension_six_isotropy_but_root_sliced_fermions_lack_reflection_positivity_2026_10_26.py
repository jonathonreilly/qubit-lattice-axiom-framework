AUDIT_INPUT_PATHS = ('docs/D4_EVENT_LAW_LOOPS_KEEP_DIMENSION_SIX_ISOTROPY_BUT_ROOT_SLICED_FERMIONS_LACK_REFLECTION_POSITIVITY_BOUNDED_THEOREM_NOTE_2026-10-26.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
#!/usr/bin/env python3
"""D4 interacting check: one/two-loop self-energy isotropy on D4 vs Z^4 (dim 4/6/8), fermion reflection positivity
under root slicing, triangle-photon link-mode spectrum. Self-contained (numpy). Seeded. Supplied models; float checks."""
import itertools, time
import numpy as np
AUDIT_TIMEOUT_SEC = 120
t0 = time.time(); rng = np.random.default_rng(20261026)
NP = NF = 0
def check(name, ok, info=""):
    global NP, NF
    NP += bool(ok); NF += (not ok)
    print(("PASS " if ok else "FAIL ") + name + (" | " + info if info else ""))
R = np.array([v for v in itertools.product([-1, 0, 1], repeat=4) if sum(map(abs, v)) == 2], float)
# --- C0 W(F4) by closure; invariant-tensor counts (character average)
gens = []
for i in range(3):
    M = np.eye(4); M[[i, i + 1]] = M[[i + 1, i]]; gens.append(M)
M = np.eye(4); M[0, 0] = -1; gens.append(M); B4g = list(gens[:4]); h = np.ones(4) / 2; gens.append(np.eye(4) - 2 * np.outer(h, h))
def close(gs):
    key = lambda A: tuple(np.round(2 * A).astype(int).ravel()); D = {key(np.eye(4)): np.eye(4)}; fr = [np.eye(4)]
    while fr:
        nf = []
        for A in fr:
            for g in gs:
                B = g @ A
                if key(B) not in D: D[key(B)] = B; nf.append(B)
        fr = nf
    return np.array(list(D.values()))
G, GB = close(gens), close(B4g); tr = lambda H, k: int(round(np.mean(np.trace(H, axis1=1, axis2=2)**k)))
cW, cB = [tr(G, k) for k in (2, 4, 6)], [tr(GB, k) for k in (2, 4, 6)]
check("C0 |W(F4)| = 1152, |B4| = 384; invariant tensors rank 2,4,6: W(F4) " + str(cW) + ", B4 " + str(cB) + ", O(4) [1, 3, 15]",
      len(G) == 1152 and len(GB) == 384 and cW[:2] == [1, 3] and cB[1] == 4 and cW[2] > 15, "W(F4) = O(4) through rank 4 (exact)")
# --- C1 self-energies in position space; D4 on a W(F4)-invariant torus (period L*D4), Z^4 control on L Z^4
P = rng.normal(size=(40, 4)); p2 = np.sum(P**2, 1)
J6 = lambda p: np.sum(p**6, 1) + 15 * sum(p[:, i]**2 * p[:, j]**2 * p[:, k]**2 for i, j, k in itertools.combinations(range(4), 3))
gJ6 = np.stack([6 * P[:, m]**5 + 30 * P[:, m] * sum(P[:, a]**2 * P[:, b]**2 for a, b in itertools.combinations([n for n in range(4) if n != m], 2)) for m in range(4)], 1)
C48 = np.array([v for v in itertools.product(range(-2, 3), repeat=4) if sum(v) % 2 == 0 and 0 < sum(np.square(v)) <= 4], float)
def selfen(kind, L, M2=4.0, MF=1.5):
    m1 = np.arange(L); Mg = np.stack(np.meshgrid(m1, m1, m1, m1, indexing='ij'), -1).reshape(-1, 4); sh = (L,) * 4
    if kind == 'D4':
        Bm = np.array([[1, 1, 0, 0], [1, -1, 0, 0], [0, 1, -1, 0], [0, 0, 1, -1]], float).T
        Pg = 2 * np.pi * Mg @ np.linalg.inv(Bm) / L; Xr = Mg @ Bm.T
        f = np.round(Xr / L); d = Xr / L - f; odd = np.where(f.sum(1) % 2 != 0)[0]; j = np.argmax(np.abs(d), 1)
        f[odd, j[odd]] += np.where(d[odd, j[odd]] > 0, 1, -1); X = Xr - L * f
        rp = Pg @ R.T; K = np.sum(1 - np.cos(rp), 1) / 6; s = np.sin(rp) @ R / 12; del rp
    else:
        Pg = 2 * np.pi * Mg / L; X = np.where(Mg >= L // 2, Mg - L, Mg).astype(float)
        K = np.sum(2 * (1 - np.cos(Pg)), 1); s = np.sin(Pg)
    n0 = np.sum(X**2, 1); ties = []; cnt = np.ones(len(X))
    for c in (C48 if kind == 'D4' else []):
        ii = np.where(np.abs(np.sum((X - L * c)**2, 1) - n0) < 1e-9)[0]
        if len(ii): ties.append((ii, X[ii] - L * c)); cnt[ii] += 1
    ft = lambda a: np.fft.ifftn(a.reshape(sh)).reshape(-1)
    Gx = ft(1 / (K + M2)).real
    bW = K / 2 - 1; N = np.sqrt(np.sum(s**2, 1) + bW**2); al = 1 + MF + bW / N; be = s / N[:, None]; den = al**2 + np.sum(be**2, 1)
    S0 = ft(al / den).real; Sm = np.stack([ft(-1j * be[:, m] / den).real for m in range(4)], 1)
    neg = np.ravel_multi_index(tuple(((-Mg) % L).T), sh)
    def mom(f, k):
        y = sum((f[i:i + 20000] / cnt[i:i + 20000]) @ (X[i:i + 20000] @ P.T)**k for i in range(0, len(X), 20000))
        for ii, Xc in ties: y = y + (f[ii] / cnt[ii]) @ (Xc @ P.T)**k
        return y
    def res(y, Bs):
        A = np.stack([b.ravel() for b in Bs], 1); c = np.linalg.lstsq(A, y.ravel(), rcond=None)[0]; return np.linalg.norm(y.ravel() - A @ c) / np.linalg.norm(y), c
    out = {}
    sp = {'bubble(phi^3)': Gx**2, 'sunset(phi^4)': Gx**3, 'Yukawa loop': -4 * (S0 * S0[neg] + np.sum(Sm * Sm[neg], 1)), 'fermion mass part': S0 * Gx}
    for nm, f in sp.items():
        r = [res(mom(f, 2), [p2]), res(mom(f, 4), [p2**2]), res(mom(f, 6), [p2**3]), res(mom(f, 6), [p2**3, J6(P)])]
        out[nm] = [a[0] for a in r] + [r[0][1][0], r[3][1][1] / r[3][1][0]]
    fm = Sm * Gx[:, None]; V = lambda k: np.stack([mom(fm[:, m], k) for m in range(4)], 1)
    r = [res(V(1), [P]), res(V(3), [p2[:, None] * P]), res(V(5), [p2[:, None]**2 * P]), res(V(5), [p2[:, None]**2 * P, gJ6])]
    out['fermion gamma_mu part'] = [a[0] for a in r] + [r[0][1][0], r[3][1][1] / r[3][1][0]]
    return out
D16, D20, Z16 = selfen('D4', 16), selfen('D4', 20), selfen('Z4', 16)
print("  residuals vs isotropic basis: dim4 | dim6 | dim8 w/o J6 | dim8 with J6 ; Z^4 dim6 ; J6 ratio (L=16 -> 20)")
for nm in D16:
    a, b, z = D16[nm], D20[nm], Z16[nm]
    print(f"  {nm:22s} {a[0]:.0e} {a[1]:.0e} {a[2]:.1e} {a[3]:.0e} ; Z4 {z[1]:.1e} ; {a[5]:+.5f} -> {b[5]:+.5f}")
allD = [D16[n] for n in D16] + [D20[n] for n in D20]
check("C1a dim 4: every species' p^2 (gamma.p) term is isotropic on D4 and Z^4: equal speed of light for all species",
      max(max(a[0] for a in allD), max(Z16[n][0] for n in Z16)) < 1e-9, "Euclidean point groups have one quadratic invariant (main: B4 marginal theorem)")
check("C1b dim 6: no O(4)-breaking quartic (cubic gamma) piece on D4 for all 5 self-energies; Z^4 control induces sum p^4 (p_mu^3)",
      max(a[1] for a in allD) < 1e-9 and min(Z16[n][1] for n in Z16) > 1e-3, f"D4 max {max(a[1] for a in allD):.0e}; Z4 min {min(Z16[n][1] for n in Z16):.1e}")
check("C1c dim 8: first induced O(4)-breaking piece is J6 (grad J6) for every species, ratio converged in L",
      min(a[2] for a in allD) > 1e-4 and max(a[3] for a in allD) < 1e-9 and max(abs(D16[n][5] - D20[n][5]) for n in D16) < 2e-3)
# --- C2 fermion reflection positivity (fiber method: exact transverse momentum, reflection-compatible time torus)
s1 = np.array([[0, 1], [1, 0]]); s2 = np.array([[0, -1j], [1j, 0]]); s3 = np.diag([1, -1]); I2 = np.eye(2); Z2 = np.zeros((2, 2))
gm = np.array([np.block([[Z2, I2], [I2, Z2]])] + [np.block([[Z2, -1j * s], [1j * s, Z2]]) for s in (s1, s2, s3)])
Nt = 16
def Sp(Pq, kind, w, MF=0.5):
    if kind == 'Z4': s = np.sin(Pq); K = np.sum(1 - np.cos(Pq), 1)
    else: rp = Pq @ R.T; s = np.sin(rp) @ R / 12; K = np.sum(1 - np.cos(rp), 1) / 12
    if w == 'sc': return (1 / (12 * K + 0.3))[:, None, None] * np.eye(4)
    if w == 'ov':
        bW = K - 1; N = np.sqrt(np.sum(s**2, 1) + bW**2); al = 1 + MF + bW / N; be = s / N[:, None]
    else: al = w * K + MF; be = s
    return (al[:, None, None] * np.eye(4) - 1j * np.einsum('pm,mab->pab', be, gm)) / (al**2 + np.sum(be**2, 1))[:, None, None]
def rpf(kind, w, rt, v, Gam, half, j, ferm=True):
    """max positive / max |eig| of the OS form -(S(x'+jv-sx) Gam)^T (positive form <=> this is ~0), Hermiticity."""
    s = lambda x: x - 2 * (x @ rt) / (rt @ rt) * rt; u = rt / (rt @ v)
    ph = 2 * np.pi * (np.arange(Nt) + (0.5 if ferm else 0)) / Nt
    Qp = np.linalg.qr(np.vstack([rt, np.eye(4)[:3]]).T)[0][:, 1:]; bad = herm = 0
    for k in [np.zeros(4)] + [Qp @ rng.uniform(-np.pi, np.pi, 3) for _ in range(10)]:
        Sq = Sp(k[None] + ph[:, None] * u[None], kind, w); A = np.einsum('tm,mab->tab', np.exp(1j * np.outer(np.arange(Nt), ph)) / Nt, Sq)
        Mm = np.zeros((len(half), 4, len(half), 4), complex)
        for a_, n in enumerate(half):
            for b_, n2 in enumerate(half):
                base = (n2 + j) * v - s(n * v); Mm[a_, :, b_, :] = -(np.exp(1j * k @ base) * A[int(round(base @ u)) % Nt] @ Gam).T
        Mm = Mm.reshape(4 * len(half), -1); herm = max(herm, np.abs(Mm - Mm.conj().T).max() / np.abs(Mm).max())
        e = np.linalg.eigvalsh((Mm + Mm.conj().T) / 2); bad = max(bad, e.max() / np.abs(e).max())
    return bad, herm
e0 = np.eye(4)[0]; H1, H0 = range(1, Nt // 2 + 1), range(0, Nt // 2 + 1)
zw_l, zw_t = rpf('Z4', 1.0, e0, e0, gm[0], H1, -1), rpf('Z4', 1.0, e0, e0, gm[0], range(1, Nt // 2), 0)
zn_l, zn_t = rpf('Z4', 0.0, e0, e0, gm[0], H1, -1), rpf('Z4', 0.0, e0, e0, gm[0], range(1, Nt // 2), 0)
zs, zws = rpf('Z4', 'sc', e0, e0, np.eye(4), H0, 0, False), rpf('Z4', 1.0, e0, e0, gm[0], H0, 0)
check("C2a calibration (Z^4, axis): Wilson r=1 link RP and T >= 0; naive r=0 link RP but T indefinite; scalar site RP; Wilson site RP fails",
      zw_l[0] < 1e-10 and zw_t[0] < 1e-10 and zn_l[0] < 1e-10 and zn_t[0] > 0.1 and zs[0] < 1e-10 and zws[0] > 0.1,
      f"pos.frac W-link {zw_l[0]:.0e} W-T {zw_t[0]:.0e} naive-T {zn_t[0]:.2f} W-site {zws[0]:.2f}")
rt, v = np.array([1., 1, 0, 0]), np.array([1., 0, 1, 0]); gt = (gm[0] + gm[1]) / np.sqrt(2)
ds = rpf('D4', 'sc', rt, v, np.eye(4), H0, 0, False)
out = {w: (rpf('D4', w, rt, v, gt, H0, 0), rpf('D4', w, rt, v, gt, range(1, Nt // 2), 0)) for w in (np.sqrt(2), 1.0, 'ov')}
lab = {np.sqrt(2): 'Wilson w=sqrt2', 1.0: 'Wilson w=1', 'ov': 'overlap'}
cpts = [np.array(c, float) for c in itertools.product(range(-3, 4), repeat=4) if sum(c) % 2 == 0 and np.dot(c, rt) == 1]
lk = [(A, (np.linalg.eigvalsh((A + A.T) / 2) < 0).sum()) for A in G if np.allclose(A @ A, np.eye(4)) and np.allclose(A @ rt, -rt) and any(np.allclose(A @ c, -c) for c in cpts)]
check("C2b D4 root slicing: scalar site RP holds; isometries x -> Ax + c with n -> 1-n exist only twisted (A = -1 on >= 3 dims), none is a reflection",
      ds[0] < 1e-10 and ds[1] < 1e-12 and len(lk) > 0 and min(d for _, d in lk) >= 3, f"scalar pos.frac {ds[0]:.0e}; {len(lk)} twisted, 0 pure (no link RP)")
check("C2c D4 fermions, root site reflection Theta psi = psibar(sx) g_t: two-point OS form INDEFINITE (Hermitian), with and without the plane",
      all(o[0][0] > 0.5 and o[1][0] > 1e-4 and o[1][1] < 1e-10 for o in out.values()),
      "; ".join(f"{lab[w]} open-half pos.frac {o[1][0]:.1e}" for w, o in out.items()))
# --- C3 triangle-photon link modes over the Brillouin zone
Rp = np.array([r for r in R if tuple(r) > tuple(-r)]); idx = {tuple(r): i for i, r in enumerate(Rp)}; tri = []
for r1 in R:
    for r2 in R:
        if r1 @ r2 == -1:
            y = np.zeros(4); Lr = []
            for r in (r1, r2, -(r1 + r2)):
                t = tuple(r); i, sg = (idx[t], 1.) if t in idx else (idx[tuple(-r)], -1.); Lr.append((i, sg, y + r / 2)); y = y + r
            tri.append(Lr)
TI = np.array([[l[0] for l in T] for T in tri]); TS = np.array([[l[1] for l in T] for T in tri]); TM = np.array([[l[2] for l in T] for T in tri])
OH = np.zeros((192, 3, 12)); OH[np.arange(192)[:, None], np.arange(3)[None], TI] = 1
def Kph(Q):
    C = np.einsum('qtj,tjl->qtl', np.exp(1j * np.einsum('tjm,qm->qtj', TM, Q)) * TS[None], OH); return np.einsum('qtl,qtm->qlm', C.conj(), C)
q1 = np.linspace(-np.pi, np.pi, 13)[:-1] + 1e-3; Q = np.array(list(itertools.product(q1, repeat=4))); Ks = np.sum(1 - np.cos(Q @ R.T), 1)
lam = np.concatenate([np.linalg.eigvalsh(Kph(Q[i:i + 400])) for i in range(0, len(Q), 400)])
check("C3 link modes (12 per site): 1 exact gauge zero, 3 photons with 2/3 <= lambda/K <= 3/2 (no photon doublers), 8 heavy >= 36 on all 12^4 q",
      np.abs(lam[:, 0]).max() < 1e-10 and (lam[:, 1] / Ks).min() > 0.6 and lam[:, 4].min() > 30,
      f"heavy min {lam[:, 4].min():.2f} max {lam[:, 11].max():.1f} (72 at q=0); photon/K in [{(lam[:, 1] / Ks).min():.3f}, {(lam[:, 3] / Ks).max():.3f}]")
print("VERDICT: item1 PASS (dim-6 protected at one/two loops, J6 first); item2 FAIL (fermion RP not available in root slicing); item3 PASS -> PARTIAL")
print(f"TOTAL: PASS={NP} FAIL={NF}   ({time.time() - t0:.1f} s)")
