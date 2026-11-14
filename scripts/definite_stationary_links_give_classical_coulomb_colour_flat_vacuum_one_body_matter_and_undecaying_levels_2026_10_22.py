AUDIT_INPUT_PATHS = ('docs/DEFINITE_STATIONARY_LINKS_GIVE_CLASSICAL_COULOMB_COLOUR_FLAT_VACUUM_ONE_BODY_MATTER_AND_UNDECAYING_LEVELS_BOUNDED_THEOREM_NOTE_2026-10-22.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
#!/usr/bin/env python3
"""definite-links: what a supplied Cartan / pure-gauge definite-link ansatz gives for colour
and light, with estimates against measurement; and what quantum links give instead.

Scope (narrowed 2026-11-14): the colour and vacuum statements are about the SUPPLIED ansatz
(spatial links pure gauge, A_0 in one Cartan, occupation-basis charges). They are not
statements about every definite stationary link configuration: A5 and C2 are explicit
witnesses that product unitarity does not give |tr W|/3 = 1 and that a sourceless stationary
point need not be flat. Estimates against measurement print as non-counted ESTIMATE lines.

Sections
 A  [T] supplied ansatz with a static quark pair: Cartan sources commute (control: a rotated
        source does not), exact lattice Gauss law, bounded static energy, every Wilson loop of a
        pure-gauge configuration has normalised trace 1; [W] witness U = diag(1, w, w^2).
 B  [D] contrast: fluctuating SU(2) links (3D Euclidean heat bath) give an area law.
 C  [T] the flat (pure-gauge) vacuum is a sourceless stationary point with F = 0;
    [W] a uniform Cartan flux is a sourceless stationary point with F != 0.
 D  [E] alpha_s running: matter loops only (c-number links) vs gluon + quark loops (not counted).
 E  [T] c-number links make every history's fermion update one-body: Slater stays Slater;
        no mediator entanglement for the supplied coupling vs a quantum link mode.
 F  [T] stationary odds -> fewest-change plan is the identity (control: unequal odds);
        classical g2 >= 1 (control: a one-photon Fock state); [E] decay estimates (not counted).
 G  [E] Lamb shift and a_e with and without the photon propagator (not counted).
"""
import os
import sys
os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
import time
import numpy as np
from scipy.linalg import expm
from scipy.optimize import linprog

AUDIT_TIMEOUT_SEC = 120
T0 = time.time()
NP = 0
NF = 0


def check(tag, ok, msg, extra=""):
    global NP, NF
    if ok:
        NP += 1
    else:
        NF += 1
    print(f"[{'PASS' if ok else 'FAIL'}] [{tag}] {msg}" + (f" | {extra}" if extra else ""))


def estimate(msg, extra=""):
    """A comparison with measurement from supplied constants: printed, not counted."""
    print(f"ESTIMATE (not counted): {msg}" + (f" | {extra}" if extra else ""))


rng = np.random.default_rng(20261022)

# ---------------------------------------------------------------- A
print("== A. supplied ansatz: spatial links pure gauge, A_0 in one Cartan, static quark pair")
wr = np.array([0.5, 0.5 / np.sqrt(3)])
wg = np.array([-0.5, 0.5 / np.sqrt(3)])
wb = np.array([0.0, -1 / np.sqrt(3)])
lam3 = np.diag([1, -1, 0]) / 2.0
lam8 = np.diag([1, 1, -2]) / (2 * np.sqrt(3))


def qmat(w):
    return w[0] * lam3 + w[1] * lam8


def comm_max(mats):
    return max(np.abs(a @ b - b @ a).max() for a in mats for b in mats)


# A_0(x) = sum_c Q_c G(x - x_c) on sample points; every commutator of A_0 values (and so of the
# Coulomb electric field E = -grad A_0) is a combination of [Q_c, Q_c'].
ra = np.random.default_rng(5)                 # own stream: the heat bath below keeps its seeded draws
Gs = ra.random((6, 2))                        # sample Green-function values at 6 points, 2 sources
srcs = [qmat(wr), -qmat(wr)]                   # quark colour r, antiquark anti-r
A0 = [Gs[i, 0] * srcs[0] + Gs[i, 1] * srcs[1] for i in range(6)]
c_cart = comm_max(A0)
Hm = ra.normal(size=(3, 3)) + 1j * ra.normal(size=(3, 3)); Hm = Hm + Hm.conj().T
g_rot = expm(1j * Hm)
A0r = [Gs[i, 0] * srcs[0] + Gs[i, 1] * (g_rot @ srcs[1] @ g_rot.conj().T) for i in range(6)]
c_rot = comm_max(A0r)
check("T", c_cart < 1e-14 and np.allclose(wr + wg + wb, 0) and c_rot > 1e-3,
      "A1 on the supplied ansatz (A_i pure gauge, A_0 in one Cartan) all commutators of A_0 values vanish: the "
      "Coulomb field is a stationary point (uniqueness NOT shown); control: a source rotated out of the Cartan",
      f"max |[A_0(x), A_0(y)]| Cartan {c_cart:.0e}, rotated source {c_rot:.2f}")
L = 48
k = 2 * np.pi * np.fft.fftfreq(L)
KX, KY, KZ = np.meshgrid(k, k, k, indexing="ij")
lap = 4 * (np.sin(KX / 2) ** 2 + np.sin(KY / 2) ** 2 + np.sin(KZ / 2) ** 2)
lap[0, 0, 0] = 1.0
Gk = 1.0 / lap
Gk[0, 0, 0] = 0.0
G = np.real(np.fft.ifftn(Gk))
q2 = wr @ wr
Rs = np.arange(1, 13)
V = np.array([q2 * (G[0, 0, 0] - G[R, 0, 0]) for R in Rs])
Vc = q2 * (G[0, 0, 0] - 1 / (4 * np.pi * Rs))
dev = np.max(np.abs(V[3:9] - Vc[3:9]) / np.abs(Vc[3:9]))
rho = np.zeros((L, L, L)); rho[0, 0, 0] = 1; rho[6, 0, 0] = -1
phi = np.real(np.fft.ifftn(np.fft.fftn(rho) * Gk))
E = [phi - np.roll(phi, -1, axis=a) for a in range(3)]
div = sum(E[a] - np.roll(E[a], 1, axis=a) for a in range(3))
gres = np.max(np.abs(div - rho))
check("T", gres < 1e-10, "A2 lattice Gauss law holds exactly for the Cartan Coulomb field of the ansatz",
      f"max residual {gres:.1e}")
X = np.vstack([np.ones(8), 1 / Rs[2:10], Rs[2:10]]).T
coef, *_ = np.linalg.lstsq(X, V[2:10], rcond=None)
check("T", V.max() < q2 * G[0, 0, 0] + 1e-12 and dev < 0.03,
      "A3 on the ansatz the static pair energy is bounded by the self-energy at every separation and is "
      "Coulomb, -g^2|w|^2/(4 pi R) = -alpha_s/(3R) (quantum one-gluon: -4 alpha_s/(3R)); zero string "
      "tension for this configuration",
      f"V/g^2 = {V[0]:.4f}..{V[-1]:.4f}, bound {q2*G[0,0,0]:.4f}, Coulomb dev {dev:.1%}, "
      f"fitted sigma a^2/g^2 = {coef[2]:.1e} (finite box)")


def rand_su3(r):
    h = r.normal(size=(3, 3)) + 1j * r.normal(size=(3, 3)); h = h + h.conj().T
    u = expm(1j * h)
    return u / np.linalg.det(u) ** (1 / 3)


def wilson_traces(Ux, Uy, Rr, Tt):
    """normalised traces of all Rr x Tt loops in the xy plane of a 2D periodic slice."""
    Lw = Ux.shape[0]
    out = []
    for x in range(Lw):
        for y in range(Lw):
            M = np.eye(3, dtype=complex)
            for i in range(Rr):
                M = M @ Ux[(x + i) % Lw, y]
            for j in range(Tt):
                M = M @ Uy[(x + Rr) % Lw, (y + j) % Lw]
            for i in range(Rr - 1, -1, -1):
                M = M @ Ux[(x + i) % Lw, (y + Tt) % Lw].conj().T
            for j in range(Tt - 1, -1, -1):
                M = M @ Uy[x, (y + j) % Lw].conj().T
            out.append(np.trace(M) / 3)
    return np.array(out)


Lw = 5
rg = np.random.default_rng(11)
gsite = [[rand_su3(rg) for _ in range(Lw)] for _ in range(Lw)]
Ux = np.array([[gsite[x][y] @ gsite[(x + 1) % Lw][y].conj().T for y in range(Lw)] for x in range(Lw)])
Uy = np.array([[gsite[x][y] @ gsite[x][(y + 1) % Lw].conj().T for y in range(Lw)] for x in range(Lw)])
Wpg = {key: wilson_traces(Ux, Uy, *key) for key in ((1, 1), (1, 2), (2, 2))}
dev_pg = max(np.abs(v - 1).max() for v in Wpg.values())
creutz_pg = -np.log(np.mean(Wpg[(2, 2)]).real * np.mean(Wpg[(1, 1)]).real / np.mean(Wpg[(1, 2)]).real ** 2)
check("T", dev_pg < 1e-12 and abs(creutz_pg) < 1e-12,
      "A4 every Wilson loop of a pure-gauge configuration (the ansatz's spatial links) has normalised "
      "trace exactly 1, so its Creutz ratio is exactly 0: no area law for this configuration",
      f"5^2 slice, random gauge: max |tr W/3 - 1| {dev_pg:.0e}, chi22 {creutz_pg:.0e}")
om = np.exp(2j * np.pi / 3)
Uw = np.diag([1, om, om ** 2])
Ux_w = Ux.copy(); Ux_w[0, 0] = Ux_w[0, 0] @ Uw
W11w = wilson_traces(Ux_w, Uy, 1, 1)
check("W", abs(np.linalg.det(Uw) - 1) < 1e-12 and np.abs(Uw.conj().T @ Uw - np.eye(3)).max() < 1e-12
      and abs(np.trace(Uw)) / 3 < 1e-12 and np.abs(W11w).min() < 1e-12,
      "A5 NEGATIVE RESULT kept: product unitarity does not give |W| = 1; U = diag(1, w, w^2) in SU(3) has "
      "tr U/3 = 0, and on one link of the pure-gauge slice it gives plaquettes of normalised trace 0",
      f"|det U - 1| {abs(np.linalg.det(Uw) - 1):.0e}, |tr U|/3 {abs(np.trace(Uw))/3:.0e}, "
      f"min |tr P/3| on the modified slice {np.abs(W11w).min():.0e}")

# ---------------------------------------------------------------- B
print("== B. contrast: fluctuating SU(2) links, 3D Euclidean heat bath (quantum links)")


def qmul(a, b):
    a0, av = a[..., 0], a[..., 1:]
    b0, bv = b[..., 0], b[..., 1:]
    out = np.empty(np.broadcast_shapes(a.shape, b.shape))
    out[..., 0] = a0 * b0 - np.sum(av * bv, -1)
    out[..., 1:] = a0[..., None] * bv + b0[..., None] * av - np.cross(av, bv)
    return out


def qdag(a):
    b = a.copy(); b[..., 1:] *= -1; return b


Ll = 8
U = np.zeros((3, Ll, Ll, Ll, 4)); U[..., 0] = 1.0
par = (np.indices((Ll, Ll, Ll)).sum(0) % 2)


def staple(U, mu):
    S = np.zeros(U.shape[1:])
    for nu in range(3):
        if nu == mu:
            continue
        a = np.roll(U[nu], -1, axis=mu)
        b = qdag(np.roll(U[mu], -1, axis=nu))
        c = qdag(U[nu])
        S += qmul(qmul(a, b), c)
        a = qdag(np.roll(np.roll(U[nu], -1, axis=mu), 1, axis=nu))
        b = qdag(np.roll(U[mu], 1, axis=nu))
        c = np.roll(U[nu], 1, axis=nu)
        S += qmul(qmul(a, b), c)
    return S


def heatbath(U, beta):
    for mu in range(3):
        for p in (0, 1):
            S = staple(U, mu)
            m = (par == p)
            Sm = S[m]
            kk = np.sqrt(np.sum(Sm ** 2, -1))
            Vh = Sm / kk[:, None]
            bk = beta * kk
            x0 = np.empty(len(bk)); todo = np.ones(len(bk), bool)
            while todo.any():
                u = rng.random(todo.sum())
                b = bk[todo]
                x = 1 + np.log(u + (1 - u) * np.exp(-2 * b)) / b
                acc = rng.random(todo.sum()) < np.sqrt(np.clip(1 - x * x, 0, 1))
                idx = np.where(todo)[0]
                x0[idx[acc]] = x[acc]
                todo[idx[acc]] = False
            nv = rng.normal(size=(len(bk), 3)); nv /= np.linalg.norm(nv, axis=1)[:, None]
            Xq = np.empty((len(bk), 4)); Xq[:, 0] = x0; Xq[:, 1:] = nv * np.sqrt(1 - x0 ** 2)[:, None]
            Um = U[mu]
            Um[m] = qmul(Xq, qdag(Vh))  # U S_hat = X, weight exp((beta/2) Tr U S)
    return U


def wloop(U, R, T):
    vals = []
    for mu in range(3):
        for nu in range(3):
            if mu == nu:
                continue
            A = U[mu].copy()
            for i in range(1, R):
                A = qmul(A, np.roll(U[mu], -i, axis=mu))
            B = U[nu].copy()
            for j in range(1, T):
                B = qmul(B, np.roll(U[nu], -j, axis=nu))
            A2 = np.roll(A, -T, axis=nu)
            B2 = np.roll(B, -R, axis=mu)
            W = qmul(qmul(A, B2), qmul(qdag(A2), qdag(B)))
            vals.append(W[..., 0].mean())
    return float(np.mean(vals))


betaB = 3.0
for _ in range(60):
    heatbath(U, betaB)
meas = {(1, 1): [], (1, 2): [], (2, 2): [], (2, 3): [], (3, 3): []}
for s in range(80):
    heatbath(U, betaB)
    if s % 4 == 0:
        for key in meas:
            meas[key].append(wloop(U, *key))
Wm = {key: np.mean(v) for key, v in meas.items()}
chi22 = -np.log(Wm[(2, 2)] * Wm[(1, 1)] / Wm[(1, 2)] ** 2)
chi33 = -np.log(Wm[(3, 3)] * Wm[(2, 2)] / Wm[(2, 3)] ** 2)
check("D", chi22 > 0.05 and chi33 > 0.0,
      "B1 fluctuating links (a path sum over link odds) give an area law, Creutz ratios > 0; the pure-gauge "
      "ansatz value is exactly 0 (A4)",
      f"SU(2) 3D 8^3 beta={betaB}: W11={Wm[(1,1)]:.3f} W22={Wm[(2,2)]:.3f} chi22={chi22:.3f} chi33={chi33:.3f}")

# ---------------------------------------------------------------- C
print("== C. sourceless stationary links: the flat one, and a non-flat witness")
# C1: the pure-gauge slice above has every plaquette = 1, so F = 0 and the Wilson-action force
# (traceless antihermitian part of U x staple) vanishes: a sourceless stationary point.
Pl = []
for x in range(Lw):
    for y in range(Lw):
        Pl.append(Ux[x, y] @ Uy[(x + 1) % Lw, y] @ Ux[x, (y + 1) % Lw].conj().T @ Uy[x, y].conj().T)
fdev = max(np.abs(P_ - np.eye(3)).max() for P_ in Pl)
check("T", fdev < 1e-12,
      "C1 the flat (pure-gauge) configuration has every plaquette = 1 (F = 0): a sourceless stationary point; "
      "that the definite vacuum is this one is a supplied selection (C2)", f"max |P - 1| {fdev:.0e}")
# C2: uniform abelian flux on a periodic L x L slice, embedded in the Cartan as diag(e^{ia}, e^{-ia}, 1)
Lf, nflux = 6, 1
thf = 2 * np.pi * nflux / Lf ** 2
axf = np.zeros((Lf, Lf)); ayf = np.zeros((Lf, Lf))
for x in range(Lf):
    ayf[x, :] = thf * x
axf[Lf - 1, :] = -thf * Lf * np.arange(Lf)
Pf = np.array([[axf[x, y] + ayf[(x + 1) % Lf, y] - axf[x, (y + 1) % Lf] - ayf[x, y]
                for y in range(Lf)] for x in range(Lf)])
Pf = (Pf + np.pi) % (2 * np.pi) - np.pi
# Wilson action S = sum_P (1 - cos theta_P) per Cartan component; dS/da_link = sum_P s sin(theta_P)
fx = np.array([[np.sin(Pf[x, y]) - np.sin(Pf[x, (y - 1) % Lf]) for y in range(Lf)] for x in range(Lf)])
fy = np.array([[-np.sin(Pf[x, y]) + np.sin(Pf[(x - 1) % Lf, y]) for y in range(Lf)] for x in range(Lf)])
force = max(np.abs(fx).max(), np.abs(fy).max())
check("W", force < 1e-12 and np.abs(Pf - thf).max() < 1e-12 and thf > 0.1,
      "C2 NEGATIVE RESULT kept: a sourceless stationary point need not be flat; a uniform Cartan flux on a "
      "periodic L x L slice has zero Wilson-action force, no source and F != 0",
      f"L = {Lf}: plaquette angle {thf:.4f} everywhere, max |force| {force:.0e}")
mpi, mK, meta, metap, fpi = 138.0, 495.6, 547.9, 957.8, 92.2
chi_need = fpi ** 2 * (metap ** 2 + meta ** 2 - 2 * mK ** 2) / (2 * 3)
estimate("Witten-Veneziano needs chi_top^(1/4) ~ 180 MeV (lattice 179); the flat ansatz gives 0, leaving "
         "m_eta' <= sqrt(3) m_pi = 239 MeV (Weinberg) against 957.8 measured",
         f"chi^(1/4) needed {chi_need**0.25:.0f} MeV (supplied PDG masses, f_pi)")

# ---------------------------------------------------------------- D
print("== D. alpha_s running: which loops definite links keep")


def run(a0, mu0, mu1, b0):
    return a0 / (1 + a0 * b0 / (2 * np.pi) * np.log(mu1 / mu0))


MZ, mb, mtau = 91.1876, 4.18, 1.777
aZ = 0.1180
aq = run(run(aZ, MZ, mb, 11 - 10 / 3), mb, mtau, 11 - 8 / 3)
ac = run(run(aZ, MZ, mb, -10 / 3), mb, mtau, -8 / 3)
estimate("gluon loops need link fluctuations; matter loops alone give b0 = -2nf/3: alpha_s falls toward low "
         "energy, no asymptotic freedom, no Lambda_QCD",
         f"alpha_s(m_tau): quantum 1-loop {aq:.3f}, matter loops only {ac:.3f}, measured 0.314(14)")
print("   QED differs: its one-loop beta is matter loops only, so the sea gives alpha's running in c-number")
print("   fields; photon lines enter at two loops (relative ~3 alpha/4pi)")

# ---------------------------------------------------------------- E
print("== E. one-body updates: no correlation, no mediated entanglement")


def ops(n):
    I2 = np.eye(2); Z = np.diag([1., -1.]); a = np.array([[0, 1], [0, 0.]])
    out = []
    for j in range(n):
        m = np.array([[1.]])
        for i in range(n):
            m = np.kron(m, Z if i < j else (a if i == j else I2))
        out.append(m)
    return out


n = 6
c = ops(n)
h = rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n)); h = h + h.conj().T
H1 = sum(h[i, j] * c[i].T @ c[j] for i in range(n) for j in range(n))
Hint = sum(c[i].T @ c[i] @ c[i + 1].T @ c[i + 1] for i in range(n - 1))
vac = np.zeros(2 ** n); vac[0] = 1
psi0 = c[0].T @ c[2].T @ c[4].T @ vac


def rdm_eigs(psi):
    rho1 = np.array([[psi.conj() @ (c[i].T @ c[j] @ psi) for j in range(n)] for i in range(n)])
    return np.sort(np.linalg.eigvalsh(rho1))


e1 = rdm_eigs(expm(-1j * 1.3 * H1) @ psi0)
e2 = rdm_eigs(expm(-1j * 1.3 * (H1 + 2.0 * Hint)) @ psi0)
idem1 = np.max(np.minimum(np.abs(e1), np.abs(1 - e1)))
idem2 = np.max(np.minimum(np.abs(e2), np.abs(1 - e2)))
check("T", idem1 < 1e-10 and idem2 > 1e-2,
      "E1 conditional lemma: if c-number links enter only through bilinear hop phases and potentials, each "
      "history's fermion update is one-body and a Slater determinant stays one (1-RDM idempotent); control: "
      "a link-mediated two-body term correlates",
      f"max non-idempotency: one-body {idem1:.1e}, with mediated n n term {idem2:.2f}")
nb = 30
a = np.diag(np.sqrt(np.arange(1, nb)), 1)
Z = np.diag([1., -1.]); I2 = np.eye(2)
Zs = np.kron(Z, I2) + np.kron(I2, Z)
gq = 0.4
Hq = np.kron(np.eye(4), a.T @ a) + gq * np.kron(Zs, a + a.T)
plus = np.ones(2) / np.sqrt(2)
psi = np.kron(np.kron(plus, plus), np.eye(nb)[0])
psi = expm(-1j * 2 * np.pi * Hq) @ psi


def concurrence(v4):
    v = v4.reshape(2, 2)
    return 2 * abs(np.linalg.det(v))


M = psi.reshape(4, nb)
w, s_, vh = np.linalg.svd(M)
v4 = w[:, 0] * s_[0]
Cq = concurrence(v4 / np.linalg.norm(v4))
purity_med = s_[0] ** 2
Cd = []
for z1 in (1, -1):
    for z2 in (1, -1):
        phic = -2 * gq * (z1 + z2)
        Ud = expm(-1j * 2 * np.pi * phic * gq * Zs)
        Cd.append(concurrence(Ud @ np.kron(plus, plus)))
check("T", Cq > 0.5 and max(Cd) < 1e-12,
      "E2 for the supplied coupling Zs = Z x 1 + 1 x Z, a quantised link mode entangles two charges (mediator "
      "back in its vacuum); a c-number link fixed by the actual configuration gives a product of one-body "
      "phases in every history: no entanglement",
      f"concurrence quantum {Cq:.3f} (mediator purity {purity_med:.3f}), c-number {max(Cd):.1e}")

# ---------------------------------------------------------------- F
print("== F. fewest-change transport, antibunching, and decay estimates")
nc = 5
p = rng.random(nc); p /= p.sum()
allowed = rng.random((nc, nc)) < 0.6; np.fill_diagonal(allowed, True)
idx = [(i, j) for i in range(nc) for j in range(nc) if allowed[i, j]]
cost = np.array([0.0 if i == j else 1.0 for i, j in idx])


def transport(p0, p1):
    Aeq = np.zeros((2 * nc, len(idx))); beq = np.concatenate([p0, p1])
    for kx, (i, j) in enumerate(idx):
        Aeq[i, kx] = 1; Aeq[nc + j, kx] = 1
    r = linprog(cost, A_eq=Aeq, b_eq=beq, bounds=(0, None), method="highs")
    plan = np.zeros((nc, nc))
    if r.status == 0:
        for kx, (i, j) in enumerate(idx):
            plan[i, j] = r.x[kx]
    return r, plan


res, plan = transport(p, p)
marg = max(np.abs(plan.sum(1) - p).max(), np.abs(plan.sum(0) - p).max())
check("T", res.status == 0 and res.fun < 1e-12 and np.abs(plan - np.diag(p)).max() < 1e-12 and marg < 1e-12
      and plan.min() > -1e-15,
      "F1 equal odds before and after: the fewest-change plan is the identity (plan = diag(p), marginals p, "
      "zero changes), so a stationary level's actual configuration and its c-number source stay",
      f"min changes {res.fun:.1e}, |plan - diag p| {np.abs(plan - np.diag(p)).max():.0e}, marginal err {marg:.0e}")
q = p.copy(); q[0] += 0.1; q[1] -= min(0.1, q[1] - 1e-3); q /= q.sum()
res_c, plan_c = transport(p, q)
tv = 0.5 * np.abs(q - p).sum()
check("T", res_c.status == 0 and res_c.fun > 1e-3 and res_c.fun >= tv - 1e-12,
      "F2 control: with unequal odds the same plan has changes at least the total-variation distance, so "
      "'stay' is specific to stationary odds",
      f"min changes {res_c.fun:.4f} >= TV {tv:.4f}")
alpha = 1 / 137.035999084
a0 = 0.529177210903e-10; c_ = 299792458.0
Ry_eV = 13.605693122994; hbar_eVs = 6.582119569e-16
mr = 1 / (1 + 1 / 1836.15267)
w21 = 0.75 * Ry_eV * mr / hbar_eVs
d = (128 * np.sqrt(2) / 243) * a0 / mr
A21 = 4 * alpha * w21 ** 3 * d ** 2 / (3 * c_ ** 2)
tau = 1 / A21
estimate("quantised links (vacuum link odds, Wigner-Weisskopf) give the hydrogen 2p lifetime; a stationary "
         "pure level under c-number links does not decay",
         f"tau(2p) = {tau*1e9:.4f} ns, measured 1.60 ns (supplied atomic constants)")
tt = np.linspace(0, 30, 3001); Pn = 1 / (1 + 1e-6 / (1 - 1e-6) * np.exp(tt))
t_half_n = tt[np.argmin(np.abs(Pn - 0.5))]
estimate("a c-number field's radiation reaction acting through the dipole coherence (dP/dt = -Gamma P(1-P), "
         "supplied classical model): from P_e = 1 - 1e-6 the half time is ~14 lifetimes, not ln 2",
         f"t_half {t_half_n:.1f}/Gamma vs exponential 0.69/Gamma")
g2min = 1e9
for _ in range(200):
    I = rng.exponential(size=50) ** rng.uniform(0.1, 3); wgt = rng.random(50); wgt /= wgt.sum()
    g2min = min(g2min, (wgt @ I ** 2) / (wgt @ I) ** 2)
nfock = 6
af = np.diag(np.sqrt(np.arange(1, nfock)), 1)
one = np.zeros(nfock); one[1] = 1
g2_fock = (one @ af.T @ af.T @ af @ af @ one) / (one @ af.T @ af @ one) ** 2
check("T", g2min >= 1 - 1e-12 and g2_fock < 1e-12,
      "F3 any classical (definite or mixed) intensity gives g2(0) = <I^2>/<I>^2 >= 1 (Cauchy-Schwarz); "
      "control: a one-photon Fock state has g2(0) = 0, so the bound is specific to classical fields",
      f"min g2 over 200 mixtures {g2min:.4f}; one-photon state {g2_fock:.0e}")

# ---------------------------------------------------------------- G
print("== G. Lamb shift and a_e")
me_eV = 0.51099895e6; h_eVs = 4.135667696e-15
pref = 4 * alpha ** 5 * me_eV / (3 * np.pi * 8) / h_eVs / 1e6
lnk2S, lnk2P = 2.811769893, -0.030016709
SE2S = pref * (np.log(alpha ** -2) - lnk2S + 5 / 6)
VP2S = pref * (-1 / 5)
SE2P = pref * (-lnk2P - 0.25)
lamb_q = SE2S + VP2S - SE2P
lamb_d = VP2S
estimate("Lamb shift: the self-energy (internal photon propagator) is most of it; c-number links keep only "
         "the sea's vacuum polarisation", f"leading-order quantised {lamb_q:.0f} MHz, c-number {lamb_d:.1f} MHz, "
         f"measured 1057.845 MHz")
ae_meas = 1.15965218059e-3
estimate("a_e: Schwinger's alpha/2pi needs an internal photon; c-number links leave a one-body Dirac electron, "
         "g = 2 plus lattice terms",
         f"alpha/2pi = {alpha/(2*np.pi):.6e}, measured {ae_meas:.6e}")
print("   kept as sea loops in c-number fields: alpha's 1-loop running, Uehling (-27 MHz), Euler-Heisenberg")
print("   light-by-light. Not carried by the flat ansatz: T = 0 Casimir zero-point force (estimate).")
print("   these estimates compare the SUPPLIED ansatz with measurement; they exclude no other definite-link")
print("   configuration and do not show that links must carry odds.")
print("checked: A1-A5, C1-C2, E1-E2, F1-F3 (A5, C2 are kept counterexamples); diagnostic: B1; estimates: not counted")
print(f"elapsed_seconds {time.time()-T0:.1f}")
print(f"TOTAL: PASS={NP} FAIL={NF}")
sys.exit(1 if NF else 0)
