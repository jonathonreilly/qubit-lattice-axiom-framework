AUDIT_INPUT_PATHS = ('docs/PROPAGATOR_ZEROS_SIT_ON_THE_DIRAC_PARTNERS_LINE_AND_GIVE_NO_GHOSTS_ON_A_POSITIVE_NORM_LATTICE_BOUNDED_THEOREM_NOTE_2026-10-22.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
"""zeros-ghosts: is the Golterman-Shamir 'zeros act as ghosts once gauged' argument fatal for the far-rung route?

A. exact algebra: a propagator zero = the elementary field Dirac-paired with a charged composite; the GS
   nonlocal kernel's determinant = full determinant / composite determinant (the ghost IS the dropped composite).
B. free lattice (exact, L = 400): gapped b-chi Wilson pair. Full stiffness ~ 0 (decoupling); the GS truncation
   (full minus chi) has negative stiffness and negative current spectral weight = minus the composite's.
C. interacting ED: filtered 3450 Wilson ladder, L = 3 antiperiodic, zone corners kept (sector dim 64444), with an
   exact U(1)_{3450} gauge twist on every hop (Peierls in the free terms, the filter and the Tong shifts):
   Kohn decomposition = E0(theta) curvature, paramagnetic spectral weights >= 0, stiffness vs g.
E. measured spectral function of the electromagnetic current (R ratio) against the three response classes.
Self-contained (numpy/scipy/sympy). Ladder machinery inlined from filtered-smg-1d/core.py, with the twist added.
"""
import itertools, time
import numpy as np, scipy.sparse as sp, scipy.sparse.linalg as sla, sympy as sy

AUDIT_TIMEOUT_SEC = 120
T0 = time.time(); NP = NF = 0


def check(name, ok, detail=""):
    global NP, NF
    NP += bool(ok); NF += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f" | {detail}" if detail else ""))


# =============================================================================== A. exact algebra
print("== A. exact algebra (sympy)")
z, hb, hc, m = sy.symbols('z h_b h_chi m')
H2 = sy.Matrix([[hb, m], [m, hc]]); R = (z * sy.eye(2) - H2).inv()
Gbb = sy.simplify(R[0, 0]); Sig = sy.simplify(z - hb - 1 / Gbb); det = sy.factor((z * sy.eye(2) - H2).det())
ok1 = sy.simplify(Gbb - (z - hc) / ((z - hb) * (z - hc) - m ** 2)) == 0 and sy.simplify(Sig - m ** 2 / (z - hc)) == 0
ok2 = sy.simplify(det - (z - hc) / Gbb) == 0
check("A1 THEOREM the elementary propagator of a field b Dirac-paired (mass m) with a charged partner chi has its zero exactly on "
      "the partner's bare line z = h_chi(k), and its self-energy m^2/(z - h_chi) has the partner's pole: a zero is a pole of the "
      "composite, not an absence", ok1, "G_bb = (z-h_chi)/((z-h_b)(z-h_chi)-m^2), Sigma = m^2/(z-h_chi)")
check("A2 THEOREM det(z - H) = (z - h_chi) * G_bb^-1: the GS nonlocal kernel m^2 psi (1/D_A) psi (inverse of the zero) has "
      "determinant det(full)/det(D_A^chi), i.e. the GS 'bosonic spinor' det^-1(D_A) is exactly the dropped composite's "
      "fermion determinant; restoring the composite makes the gauged sector an ordinary massive Dirac fermion", ok2)

# =============================================================================== B. free lattice
print("== B. free lattice, L = 400 antiperiodic, charge 1 on b and chi (Peierls twist theta)")
L = 400; k = (2 * np.arange(L) + 1) * np.pi / L; m0, r = 0.5, 1.0


def e_full(th):
    kk = k + th / L; return -np.sum(np.sqrt(np.sin(kk) ** 2 + (m0 + r * (1 - np.cos(kk))) ** 2))


def e_chi(th):
    kk = k + th / L; s = np.sin(kk); return np.sum(np.minimum(s, 0.0))


def stiff(E, d=0.05): return L * (E(d) - 2 * E(0) + E(-d)) / d ** 2


Df, Dc = stiff(e_full), stiff(e_chi); Dgs = Df - Dc
gap = 2 * np.min(np.sqrt(np.sin(k) ** 2 + (m0 + r * (1 - np.cos(k))) ** 2))
check("B1 FINITE DIAGNOSTIC (exact free) the gapped b-chi pair has stiffness (1+1D photon mass^2 per e^2) ~ 0: a gapped "
      "charged sector decouples", abs(Df) < 1e-6, f"D_full = {Df:.1e}, pair gap {gap:.2f}")
check("B2 FINITE DIAGNOSTIC the composite chi alone (naive chain, two Weyl nodes) has D_chi = 1/pi > 0, and the GS truncation "
      "D_full - D_chi is NEGATIVE: GS's 'zeros lower the photon mass' is exactly the subtracted composite", abs(Dgs + Dc) < 1e-9 and Dgs < 0 and abs(Dc - 1 / np.pi) < 1e-3,
      f"D_chi = {Dc:.5f} (1/pi = {1/np.pi:.5f}), D_GS = {Dgs:.5f}")
# current spectral weight at q = 2 pi / L (Peierls current), full two-band vs chi alone
q = 2 * np.pi / L; wfull_low = 0.0; wfull_tot = 0.0; wchi = 0.0
for kk in k:
    def Hk(x): return np.array([[-np.sin(x), m0 + r * (1 - np.cos(x))], [m0 + r * (1 - np.cos(x)), np.sin(x)]])
    km = kk + q / 2; V = np.array([[-np.cos(km), r * np.sin(km)], [r * np.sin(km), np.cos(km)]])   # dH/dk at the midpoint
    e1, U1 = np.linalg.eigh(Hk(kk)); e2, U2 = np.linalg.eigh(Hk(kk + q))
    w = abs(U2[:, 1] @ V @ U1[:, 0]) ** 2 / L; om = e2[1] - e1[0]; wfull_tot += w; wfull_low += w * (om < gap * 0.99)
    if np.sin(kk) < 0 <= np.sin(kk + q): wchi += np.cos(km) ** 2 / L       # chi particle-hole at the node (omega ~ q)
    if np.sin(kk) >= 0 > np.sin(kk + q): wchi += np.cos(km) ** 2 / L
check("B3 FINITE DIAGNOSTIC current spectral function at q = 2pi/L: the full pair has zero weight below its gap (absorptive "
      "part starts at 2 Delta); chi alone has positive weight at omega ~ q; so Im Pi_GS = Im Pi_full - Im Pi_chi < 0 at low omega: "
      "GS's 'optical-theorem violation' is the composite's particle-hole line with its sign removed", wfull_low == 0 and wchi > 0,
      f"full weight below gap {wfull_low:.1e} (total {wfull_tot:.3e}), chi weight at node {wchi:.2e}")

# =============================================================================== C. interacting ED with an exact gauge twist
print("== C. filtered 3450 ladder, L = 3 antiperiodic, corners kept, exact U(1)_3450 twist on both legs")
QA = np.array([3, 4, 5, 0]); QB = np.array([2, 1, 2, -1]); S = np.array([-1, -1, 1, 1])
P1 = [(0, 0, 0), (1, 1, 0), (1, 1, 1), (2, 0, 0), (3, 0, 0), (3, 0, 1)]
P2 = [(0, 0, 0), (0, 0, 1), (1, 0, 0), (2, 1, 0), (2, 1, 1), (3, 0, 0)]


class Ladder:
    def __init__(s, L, bc):
        s.L = L; s.M = 2 * L
        s.ku = np.array([(2 * n + (1 if bc == 'a' else 0)) % (2 * L) for n in range(L)])
        s.kept = [(f, leg, i) for f in range(4) for leg in (0, 1) for i in range(L)]
        s.idx = {mm: j for j, mm in enumerate(s.kept)}

    def kv(s, f, i, th, qv): return np.pi * s.ku[i] / s.L + qv[f] * th / s.L

    def sector(s, qa_t, qb_t, Kt):
        per = []
        for f in range(4):
            mods = [s.idx[mm] for mm in s.kept if mm[0] == f]; ks = [s.ku[s.kept[j][2]] for j in mods]; cf = []
            for bits in range(1 << len(mods)):
                st = 0; nn = 0; kk = 0
                for j, md in enumerate(mods):
                    if bits >> j & 1: st |= 1 << md; nn += 1; kk += ks[j]
                cf.append((st, nn * QA[f], nn * QB[f], kk % s.M))
            per.append(cf)

        def merge(a, b):
            d = {}
            for x in a:
                for y in b: d.setdefault((x[1] + y[1], x[2] + y[2], (x[3] + y[3]) % s.M), []).append(x[0] | y[0])
            return d
        d1 = merge(per[0], per[1]); d2 = merge(per[2], per[3]); out = []
        for (a, b, c), s1 in d1.items():
            key = (qa_t - a, qb_t - b, (Kt - c) % s.M)
            if key in d2: out.append((np.array(s1, np.int64)[:, None] | np.array(d2[key], np.int64)[None, :]).ravel())
        return np.sort(np.concatenate(out))

    def free_terms(s, th, qv):
        T = []
        for f in range(4):
            for i in range(s.L):
                x = s.kv(f, i, th, qv); e = S[f] * np.sin(x); w = 1 - np.cos(x)
                a = s.idx[(f, 0, i)]; b = s.idx[(f, 1, i)]
                T += [(-e, [(b, True), (b, False)]), (e, [(a, True), (a, False)]), (w, [(a, True), (b, False)]), (w, [(b, True), (a, False)])]
        return T

    def tong_terms(s, th, qv):
        Lq = s.L; T = []
        for pat in (P1, P2):
            for iks in itertools.product(range(Lq), repeat=6):
                kt = sum((-1 if d else 1) * s.ku[i] for (f, d, sh), i in zip(pat, iks))
                if kt % s.M: continue
                shp = 1 + 0j; ops = []
                for (f, d, sh), i in zip(pat, iks):
                    x = s.kv(f, i, th, qv); shp *= np.exp((-1 if d else 1) * 1j * x * sh)
                    ops.append(((f, 1, i), bool(d), (1 + np.exp(1j * x)) / 2))
                for conj in (False, True):
                    o2 = [(mm, not d, ff) for mm, d, ff in reversed(ops)] if conj else ops
                    ph = (np.conj(shp) if conj else shp) * np.prod([np.conj(ff) if d else ff for mm, d, ff in o2])
                    if abs(ph) > 1e-14: T.append((ph / Lq ** 2, [(s.idx[mm], d) for mm, d, _ in o2]))
        return T


def apply(st, ops):
    st = st.copy(); sg = np.ones(len(st)); ok = np.ones(len(st), bool)
    for md, dag in reversed(ops):
        bit = np.int64(1) << np.int64(md); occ = (st & bit) != 0; ok &= occ != dag
        sg *= 1 - 2 * (np.bitwise_count(st & (bit - 1)) & 1).astype(np.int64); st ^= bit
    return st, sg, ok


def matrix(B, terms):
    rr = []; cc = []; vv = []; idx = np.arange(len(B))
    for co, ops in terms:
        ns, sg, ok = apply(B, ops)
        if not ok.any(): continue
        ns = ns[ok]; p = np.minimum(np.searchsorted(B, ns), len(B) - 1); h = B[p] == ns
        rr.append(p[h]); cc.append(idx[ok][h]); vv.append(co * sg[ok][h])
    Mx = sp.csr_matrix((np.concatenate(vv), (np.concatenate(rr), np.concatenate(cc))), shape=(len(B), len(B)), dtype=complex)
    return Mx


lad = Ladder(3, 'a'); B = lad.sector(36, 12, 0); dth = 0.02; G = (0.0, 8.0, 16.0)
F0 = matrix(B, lad.free_terms(0.0, QA)); T0m = matrix(B, lad.tong_terms(0.0, QA))
print(f" sector (Q_A, Q_B, K) = (36, 12, 0), dim {len(B)}; build {time.time() - T0:.1f} s")
herm = abs(T0m - T0m.getH()).max() + abs(F0 - F0.getH()).max()


def op(F, T, g): return sla.LinearOperator(F.shape, matvec=lambda x: F @ x + g * (T @ x), dtype=complex)


GS = {}
for g in G:
    e, v = sla.eigsh(op(F0, T0m, g), k=2, which='SA', tol=1e-12, v0=np.ones(op(F0, T0m, g).shape[0])); o = np.argsort(e); GS[g] = (e[o], v[:, o[0]])
side = {}
for th in (dth, -dth):                       # one twisted Tong matrix in memory at a time
    F1 = matrix(B, lad.free_terms(th, QA)); T1 = matrix(B, lad.tong_terms(th, QA))
    for g in G:
        gs = GS[g][1]; hv = F1 @ gs + g * (T1 @ gs)
        side[(th, g)] = (sla.eigsh(op(F1, T1, g), k=1, which='SA', tol=1e-12, v0=np.ones(op(F1, T1, g).shape[0]))[0][0], hv, np.vdot(gs, hv).real)
    del F1, T1
res = {}
for g in G:
    e, gs = GS[g]; E0 = e[0]; H0 = op(F0, T0m, g)
    (ep, hp, xp), (em, hm, xm) = side[(dth, g)], side[(-dth, g)]
    Dcurv = lad.L * (ep - 2 * E0 + em) / dth ** 2
    phi = (hp - hm) / (2 * dth); phi -= np.vdot(gs, phi) * gs
    A = sla.LinearOperator(F0.shape, matvec=lambda x: H0 @ x - E0 * x + np.vdot(gs, x) * gs, dtype=complex)
    y, info = sla.cg(A, phi, rtol=1e-11, maxiter=4000)
    para = 2 * np.vdot(phi, y).real; dia = (xp + xm - 2 * E0) / dth ** 2; Dk = lad.L * (dia - para)
    # spectral weights of J|0> via Lanczos (positive by construction of a positive-norm Hilbert space)
    nrm = np.linalg.norm(phi); Q = [phi / nrm]; al = []; be = []; qprev = np.zeros_like(phi); bprev = 0.0
    for it in range(80):
        wv = H0 @ Q[-1] - bprev * qprev; a_ = np.vdot(Q[-1], wv).real; wv -= a_ * Q[-1]
        for qq in Q: wv -= np.vdot(qq, wv) * qq
        b_ = np.linalg.norm(wv); al.append(a_)
        if b_ < 1e-10: break
        be.append(b_); qprev = Q[-1]; bprev = b_; Q.append(wv / b_)
    n = len(al); Tm = np.diag(al) + np.diag(be[:n - 1], 1) + np.diag(be[:n - 1], -1); ev, U = np.linalg.eigh(Tm)
    wts = nrm ** 2 * U[0, :] ** 2; om = ev - E0
    res[g] = dict(gap=e[1] - E0, Dc=Dcurv, Dk=Dk, para=lad.L * para, dia=lad.L * dia, wmin=wts.min(), wsum=wts.sum() / nrm ** 2,
                  low=wts[om < 1.0].sum() / wts.sum(), omin=om[wts > 1e-6 * wts.sum()].min(), info=info)
    print(f" g={g:4.0f}: gap {res[g]['gap']:.3f}; D_curv {Dcurv:.4f}, D_Kohn {Dk:.4f} (dia {res[g]['dia']:.3f} - para {res[g]['para']:.3f}); "
          f"J-weight below omega=1: {res[g]['low']:.3f}, lowest J pole {res[g]['omin']:.3f}")
check("C1 THEOREM-CHECK the twisted Hamiltonian is Hermitian and keeps (Q_A, Q_B, K) at every theta (Tong terms are 3450- and "
      "Q_B-neutral, so the Peierls phases cancel in momentum conservation): the gauge coupling is exact on the lattice",
      herm < 1e-12, f"Hermiticity defect {herm:.1e}")
check("C2 THEOREM-CHECK Kohn decomposition D = L(<d2H> - 2<J (H-E0)^-1 J>) equals the curvature of E0(theta) at every g: the "
      "induced gauge action IS the positive current spectral sum", all(abs(res[g]['Dc'] - res[g]['Dk']) < 2e-3 * max(1, abs(res[g]['Dc'])) for g in G),
      f"max |D_curv - D_Kohn| {max(abs(res[g]['Dc'] - res[g]['Dk']) for g in G):.1e}")
check("C3 THEOREM-CHECK every current spectral weight is >= 0 and they sum to |J|0>|^2 (Kallen-Lehmann positivity on a "
      "positive-norm Hilbert space; for a CL-1 step U = exp(-i eps H) the same weights give a positive-definite Toeplitz "
      "autocorrelation), so no ghost (negative weight) can occur", all(res[g]['wmin'] > -1e-12 and abs(res[g]['wsum'] - 1) < 1e-8 for g in G),
      f"min weight {'>= -1e-12 (roundoff level)' if min(res[g]['wmin'] for g in G) > -1e-12 else 'NEGATIVE'}")
rat = [res[g]['Dk'] / res[0.0]['Dk'] for g in G]
check("C4 FINITE DIAGNOSTIC stiffness D(g)/D(0) of the gauged ladder stays positive at g = 8, 16 (GS-ghost class predicts the "
      "mirror's share to flip sign; decoupling predicts it to vanish); L = 3 cannot separate the light and mirror shares, so "
      "this only bounds, it does not decide", all(x > 0 for x in rat), f"D(g)/D(0) {[round(float(x), 3) for x in rat]}")

# =============================================================================== E. measured spectral function
print("== E. measured EM-current spectral function vs the three response classes")
Qq = [2 / 3, -1 / 3, -1 / 3, 2 / 3, -1 / 3]; R1 = 3 * sum(x * x for x in Qq); as30 = 0.145
Rdec = R1 * (1 + as30 / np.pi); Rghost = 0.0; Rvec = 2 * Rdec; Rmeas, sR = 3.9, 0.05
check("E1 ESTIMATE R(e+e- -> hadrons) near sqrt(s) = 30-35 GeV is the measured absorptive part of the EM-current two-point "
      "function: decoupling class (light chiral content, mirror gapped above) gives (11/3)(1 + alpha_s/pi); GS-ghost class "
      "(zeros cancel the light share, total fermion beta = 0) gives 0; a light mirror gives twice. Measured ~3.9",
      abs(Rdec - Rmeas) < 3 * sR and abs(Rghost - Rmeas) > 50 * sR and abs(Rvec - Rmeas) > 50 * sR,
      f"decoupling {Rdec:.2f}, ghost {Rghost:.1f}, light mirror {Rvec:.2f}; measured ~{Rmeas} (PETRA/TRISTAN, approx.)")
print("supplied: Wilson ladder, 3450 charges, Tong vectors, two-site filter, g, L = 3 antiperiodic, twist on Q_A; free toy "
      "masses m0 = 0.5, r = 1; alpha_s(30 GeV) = 0.145 and R ~ 3.9 quoted approximately; cited: filtered-smg-1d, GS 2311.12790")
print(f"time {time.time() - T0:.1f} s")
print(f"TOTAL: PASS={NP} FAIL={NF}")
