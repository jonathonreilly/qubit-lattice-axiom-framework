"""X1 test DI-Z8 (see ../PREREG.md, written before this script).

T1: Z8 gate for T-symmetric gapping of n T-odd Majoranas (n = 2..16).
T2: explicit T-symmetric, parity-even disentangler on one nu=8 Kitaev bond; non-Gaussianity.
T3: the cut reduces to an exactly solvable far-end term: no bilinear, unique gapped GS, forced
    Green's-function zero; T-breaking and pole controls.
"""
import itertools, sys
import numpy as np

rng = np.random.default_rng(20261014)
X = np.array([[0, 1], [1, 0]], dtype=complex)
Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
Z = np.array([[1, 0], [0, -1]], dtype=complex)
I2 = np.eye(2, dtype=complex)


def kron_list(ms):
    out = np.array([[1.0 + 0j]])
    for m in ms:
        out = np.kron(out, m)
    return out


def majoranas(m):
    """2m JW Majoranas on m modes: gamma_{2k} = Z..Z X_k (real), gamma_{2k+1} = Z..Z Y_k (imag)."""
    out = []
    for k in range(m):
        for P in (X, Y):
            out.append(kron_list([Z] * k + [P] + [I2] * (m - k - 1)))
    return out


def parity(m):
    return kron_list([Z] * m)


def antiunitary(majs, signs):
    """Return U with T = U K satisfying T M_i T^-1 = s_i M_i. U = product of a subset of Majoranas."""
    r = [1 if np.allclose(M.imag, 0) else -1 for M in majs]  # conj(M) = r M
    sig = [s * ri for s, ri in zip(signs, r)]                 # need U M U^-1 = sig M
    plus = [i for i, s in enumerate(sig) if s == 1]
    minus = [i for i, s in enumerate(sig) if s == -1]
    if len(minus) % 2 == 0:
        A = minus  # |A| even: i notin A -> +1, i in A -> -1
    else:
        A = plus   # |A| odd: i notin A -> -1, i in A -> +1
        assert len(A) % 2 == 1
    U = np.eye(majs[0].shape[0], dtype=complex)
    for i in A:
        U = U @ majs[i]
    # verify
    for M, s in zip(majs, signs):
        lhs = U @ M.conj() @ np.linalg.inv(U)
        assert np.allclose(lhs, s * M), "antiunitary construction failed"
    return U


def herm_monomial(majs, idx):
    G = np.eye(majs[0].shape[0], dtype=complex)
    for i in idx:
        G = G @ majs[i]
    d = len(idx)
    if (d * (d - 1) // 2) % 2 == 1:
        G = 1j * G
    assert np.allclose(G, G.conj().T)
    return G


def t_symmetrize(H, U):
    return 0.5 * (H + U @ H.conj() @ np.linalg.inv(U))


def random_even_H(majs, U, degrees=(2, 4, 6, 8), max_per_degree=120):
    n = len(majs)
    H = np.zeros_like(majs[0])
    for d in degrees:
        if d > n:
            continue
        combos = list(itertools.combinations(range(n), d))
        if len(combos) > max_per_degree:
            sel = rng.choice(len(combos), max_per_degree, replace=False)
            combos = [combos[i] for i in sel]
        for c in combos:
            H = H + rng.normal() * herm_monomial(majs, c)
    return t_symmetrize(H, U)


def gs_deg(H, tol=1e-9):
    w = np.linalg.eigvalsh(H)
    return int(np.sum(w < w[0] + tol)), w


out = []
def log(*a):
    s = " ".join(str(x) for x in a)
    print(s); out.append(s); sys.stdout.flush()

ok_all = True
# ---------------------------------------------------------------- T1
log("=== T1: Z8 gate, n T-odd Majoranas alone ===")
T1_ok = True
for n in range(2, 17, 2):
    m = n // 2
    majs = majoranas(m)
    U = antiunitary(majs, [-1] * n)
    P = parity(m)
    UP = U @ P @ np.linalg.inv(U)  # T P T^-1 (P real)
    if np.allclose(UP, P):
        pres = "preserves"
    elif np.allclose(UP, -P):
        pres = "SWAPS"
    else:
        pres = "??"
    T2op = U @ U.conj()
    sq = {}
    for sgn in (+1, -1):
        proj = 0.5 * (np.eye(2 ** m) + sgn * P)
        # T^2 commutes with all Majoranas -> scalar on each sector (or parity)
        vals = np.diag(T2op @ proj)[np.abs(np.diag(proj)) > 0.5]
        sq[sgn] = np.round(vals.real.mean(), 6) if np.allclose(vals, vals[0]) else "nonscalar"
    degs = []
    for _ in range(20):
        H = random_even_H(majs, U)
        # T-odd degree-2 parts removed? report norm of quadratic projection
        degs.append(gs_deg(H)[0])
    nuniq = sum(1 for d in degs if d == 1)
    mind = min(degs)
    if n % 8 == 0:
        good = pres == "preserves" and sq[1] == 1 and sq[-1] == 1 and nuniq >= 18
    elif n % 8 == 4:
        good = pres == "preserves" and sq[1] == -1 and sq[-1] == -1 and mind >= 2
    else:
        good = pres == "SWAPS" and mind >= 2
    T1_ok &= good
    log(f"n={n:2d}  T vs parity: {pres:9s}  T^2(even)={sq[1]}  T^2(odd)={sq[-1]}  "
        f"GS degeneracy over 20 draws: min={mind} unique={nuniq}/20  -> {'ok' if good else 'MISMATCH'}")
# check degree-2 terms are T-odd for one type: quadratic monomials anticommute-symmetrize to zero
majs8 = majoranas(4); U8 = antiunitary(majs8, [-1] * 8)
q = herm_monomial(majs8, (0, 1)); qs = t_symmetrize(q, U8)
log(f"check: T-symmetrized i g'_1 g'_2 has norm {np.linalg.norm(qs):.2e} (0 => bilinear T-forbidden)")
log("T1", "PASS" if T1_ok else "FAIL")
ok_all &= T1_ok

# ---------------------------------------------------------------- T2 / T3 setup (split basis)
log("\n=== T2: explicit disentangler on one nu=8 Kitaev bond ===")
mb = 8
M = majoranas(mb)            # 16 Majoranas on 8 modes
gp = M[:8]                   # gamma'_a (site j, T-odd): modes 1-4
g = M[8:]                    # gamma_a  (site j+1, T-even): modes 5-8
UT = antiunitary(M, [-1] * 8 + [+1] * 8)
Ptot = parity(mb)
gp_d = majoranas(4)          # gamma' as 16-dim operators (gp[i] == kron(gp_d[i], I16))
assert all(np.allclose(gp[i], np.kron(gp_d[i], np.eye(16))) for i in range(8))
g_e = majoranas(4)
Ud = antiunitary(gp_d, [-1] * 8)
Ue = antiunitary(g_e, [+1] * 8)

hB = sum(-1j * gp[a] @ g[a] for a in range(8))
assert np.allclose(hB, hB.conj().T)
assert np.allclose(t_symmetrize(hB, UT), hB), "h_B not T-symmetric"


def t_fix(v, U):
    """phase-fix a T-invariant nondegenerate vector so that U conj(v) = v"""
    w = U @ v.conj()
    ph = np.vdot(v, w)
    assert abs(abs(ph) - 1) < 1e-8, f"not T-invariant |<v|Tv>|={abs(ph)}"
    return v * np.sqrt(ph)


def ground(H):
    w, V = np.linalg.eigh(H)
    return w, V


def unique_end_state(majs4, U4, parity_target=None, tries=50):
    P4 = parity(4)
    for _ in range(tries):
        H = random_even_H(majs4, U4, degrees=(2, 4, 6, 8), max_per_degree=200)
        if parity_target is not None:
            # choose sector by adding a T-allowed parity term (octic monomial = +-parity)
            H = H - 3.0 * parity_target * P4
        w, V = ground(H)
        if w[1] - w[0] > 1e-3:
            v = V[:, 0]
            pv = np.real(np.vdot(v, P4 @ v))
            return H, t_fix(v, U4), w[1] - w[0], pv
    raise RuntimeError("no unique end state found")


T2_ok = True
T3_ok = True
w0, VB = ground(hB)
assert w0[1] - w0[0] > 1e-6
B = t_fix(VB[:, 0], UT)
pB = np.real(np.vdot(B, Ptot @ B))
log(f"|B>: h_B gap {w0[1]-w0[0]:.3f}, total parity {pB:+.0f}")

for draw in range(5):
    Hd, Ed, gapd, pd = unique_end_state(gp_d, Ud, parity_target=+1)
    He, Ee, gape, pe = unique_end_state(g_e, Ue, parity_target=pB)  # product parity = pd*pe = pB
    Pst = np.kron(Ed, Ee)
    Pst = t_fix(Pst, UT)
    pP = np.real(np.vdot(Pst, Ptot @ Pst))
    # Givens rotation B -> P
    c = np.vdot(B, Pst)
    Pt = Pst - c * B
    Pt = Pt / np.linalg.norm(Pt)
    Pt = t_fix(Pt, UT)
    th = np.arctan2(np.real(np.vdot(Pt, Pst)), np.real(np.vdot(B, Pst)))
    K = np.outer(Pt, B.conj()) - np.outer(B, Pt.conj())
    # exp(th K) on 2D subspace
    Pr = np.outer(B, B.conj()) + np.outer(Pt, Pt.conj())
    Ub = np.eye(256) + (np.cos(th) - 1) * Pr + np.sin(th) * K
    e_unit = np.linalg.norm(Ub.conj().T @ Ub - np.eye(256))
    e_T = np.linalg.norm(UT @ Ub.conj() @ np.linalg.inv(UT) - Ub)
    e_par = np.linalg.norm(Ub @ Ptot - Ptot @ Ub)
    fid = abs(np.vdot(Pst, Ub @ B))
    Mp = np.array([[np.real(np.vdot(Pst, 1j * gp[a] @ gp[b] @ Pst)) if a != b else 0.0
                    for b in range(8)] for a in range(8)])
    Mfull_cross = np.array([[np.real(np.vdot(Pst, 1j * gp[a] @ g[b] @ Pst)) for b in range(8)] for a in range(8)])
    okd = (e_unit < 1e-10 and e_T < 1e-10 and e_par < 1e-10 and fid > 1 - 1e-10
           and np.max(np.abs(Mp)) < 1e-10 and abs(pP - pB) < 1e-9)
    T2_ok &= okd
    log(f"draw {draw}: end gaps {gapd:.3f}/{gape:.3f}; parity B {pB:+.0f} P {pP:+.0f}; overlap <B|P>={abs(c):.3e}; "
        f"unitary {e_unit:.1e}; [U,T] {e_T:.1e}; [U,P] {e_par:.1e}; fidelity {fid:.12f}; "
        f"max|M'| {np.max(np.abs(Mp)):.1e}; max|<i g' g>| on |P> {np.max(np.abs(Mfull_cross)):.1e} -> {'ok' if okd else 'FAIL'}")

    # ------------------------------------------------------------ T3 for this draw
    O = Ub @ hB @ Ub.conj().T
    O4 = O.reshape(16, 16, 16, 16)  # [d, e, d', e']
    Hfar = np.einsum('aebf,e,f->ab', O4, Ee.conj(), Ee)
    herm = np.linalg.norm(Hfar - Hfar.conj().T)
    eTfar = np.linalg.norm(t_symmetrize(Hfar, Ud) - Hfar)
    P4 = parity(4)
    epar = np.linalg.norm(Hfar @ P4 - P4 @ Hfar)
    wf, Vf = ground(Hfar)
    gapf = wf[1] - wf[0]
    ovl = abs(np.vdot(Ed, Vf[:, 0]))
    # bilinear component: coefficients on i g'_a g'_b (normalised Hilbert-Schmidt)
    quad = 0.0
    for a, b in itertools.combinations(range(8), 2):
        mon = herm_monomial(gp_d, (a, b))
        quad += abs(np.trace(mon.conj().T @ Hfar) / 16) ** 2
    quad = np.sqrt(quad)

    def greens(H, majs, w):
        ev, V = np.linalg.eigh(H)
        gs = np.where(ev < ev[0] + 1e-9)[0]
        Gm = np.zeros((len(majs), len(majs)), dtype=complex)
        mats = [V.conj().T @ m @ V for m in majs]
        for gidx in gs:
            for a in range(len(majs)):
                for b in range(len(majs)):
                    A = mats[a][gidx, :] * mats[b][:, gidx]   # <g|a|n><n|b|g>
                    Bv = mats[b][gidx, :] * mats[a][:, gidx]  # <g|b|n><n|a|g>
                    D = ev - ev[0]
                    Gm[a, b] += np.sum(A / (1j * w - D) + Bv / (1j * w + D))
        return Gm / len(gs)

    zeros_ok = True
    gs_vals = []
    for w in (1e-2, 1e-4, 1e-6):
        Gw = greens(Hfar, gp_d, w)
        mx = np.max(np.abs(Gw))
        gs_vals.append((w, mx))
        zeros_ok &= mx < 10 * w
    ctrl = Hfar + 0.3 * herm_monomial(gp_d, (0, 1))
    Gc = greens(ctrl, gp_d, 1e-6)
    ctrl_ok = np.max(np.abs(Gc)) > 1e-2
    Gp = greens(np.zeros((16, 16), dtype=complex), g_e, 1e-4)
    pole_ok = np.max(np.abs(Gp)) > 1 / (10 * 1e-4)
    okt3 = (herm < 1e-10 and eTfar < 1e-10 and epar < 1e-10 and gapf > 1e-3 and ovl > 1 - 1e-10
            and quad < 1e-10 and zeros_ok and ctrl_ok and pole_ok)
    T3_ok &= okt3
    log(f"   T3: H_far herm {herm:.1e}, T-sym {eTfar:.1e}, parity {epar:.1e}, gap {gapf:.4f}, "
        f"<E'|GS> {ovl:.12f}, bilinear part {quad:.1e}; max|G_far(iw)|: "
        + ", ".join(f"w={w:.0e}:{mx:.2e}" for w, mx in gs_vals)
        + f"; T-break control |G(i1e-6)| {np.max(np.abs(Gc)):.2e}; near pole |G(i1e-4)| {np.max(np.abs(Gp)):.2e} -> {'ok' if okt3 else 'FAIL'}")

log("T2", "PASS" if T2_ok else "FAIL")
log("T3", "PASS" if T3_ok else "FAIL")
ok_all &= T2_ok and T3_ok
log("\nREADING:", "CHAIN-CONSISTENT (PASS)" if ok_all else "CHAIN-BROKEN or INSTRUMENT-FAIL (see lines)")
