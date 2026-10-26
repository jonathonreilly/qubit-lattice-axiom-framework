#!/usr/bin/env python3
"""Conditional identities in explicitly supplied models, with separate finite illustrations.
The homogeneous two-derivative five-term tensor ansatz and self-adjointness are
supplied; normalize nonzero scale to one (zero operator is degenerate).
Static Fourier particular solution uses O=-T, |k|>0; no boundary-mode selection.
Six ray cases illustrate a leading weak-field coefficient, not exact deflection.
Markers use weighted distinguishability and a supplied visibility envelope.
Dirac result is P beta P=(m/E)P, not invariance under beta.
No physical field equation, coupling value or empirical identification follows.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 600
AUDIT_INPUT_PATHS = ('docs/RECORD_PROGRAM_THEOREMS_REDERIVED_BOUNDED_THEOREM_NOTE_2026-10-21.md', 'docs/CANDIDATE_LAWS.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')

import sys, os, signal, time
os.environ['OPENBLAS_NUM_THREADS'] = '1'
if not __debug__: raise RuntimeError('Optimized Python is unsupported')
sys.stdout.reconfigure(line_buffering=True)
_STARTED = time.monotonic()
def _timeout(*args):
    raise TimeoutError('Owning 600-second aggregate cap exceeded; streamed diagnostics retained')
signal.signal(signal.SIGALRM, _timeout)
signal.setitimer(signal.ITIMER_REAL, AUDIT_TIMEOUT_SEC - 2)
import numpy as np, sympy as sp
from scipy.integrate import solve_ivp

PASS = FAIL = 0


def check(name, ok, detail=''):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  {detail}" if detail else ''))


k = sp.symbols('k0:4'); a, b, c, d, e, mm = sp.symbols('a b c d e m')
eta = sp.diag(-1, 1, 1, 1); ku = [sum(eta[i, j] * k[j] for j in range(4)) for i in range(4)]; k2 = sum(k[i] * ku[i] for i in range(4))


def sym(name):
    s = sp.symbols(f'{name}0:10'); Hm = sp.zeros(4, 4); i_ = 0
    for i in range(4):
        for j in range(i, 4): Hm[i, j] = Hm[j, i] = s[i_]; i_ += 1
    return s, Hm


def Op(Hm, pars):
    a_, b_, c_, d_, e_ = pars
    tr = sum(eta[i, i] * Hm[i, i] for i in range(4)); kh = [sum(ku[p] * Hm[p, n] for p in range(4)) for n in range(4)]
    khk = sum(ku[p] * ku[q] * Hm[p, q] for p in range(4) for q in range(4))
    return sp.Matrix(4, 4, lambda m, n: a_ * k2 * Hm[m, n] + b_ * (k[m] * kh[n] + k[n] * kh[m]) + c_ * k[m] * k[n] * tr + d_ * eta[m, n] * khk + e_ * eta[m, n] * k2 * tr)


def main():
    hs, H = sym('h'); gs, Hp = sym('g')
    EIN = (1, -1, 1, 1, -1)
    # (1) divergence identity
    O = Op(H, (a, b, c, d, e))
    conds = set()
    for n in range(4):
        conds |= set(sp.Poly(sp.expand(sum(ku[m] * O[m, n] for m in range(4))), *hs, *k).coeffs())
    fam = sp.solve(list(conds), [b, c, d, e], dict=True)
    check('(1a) divergence vanishing for every field fixes b=-a, d=a, c=-e (one free parameter beyond scale)',
          fam == [{b: -a, c: -e, d: a}], str(fam))
    def pair(A, B):
        Bu = eta * B * eta; return sp.expand(sum(A[i, j] * Bu[i, j] for i in range(4) for j in range(4)))
    famp = (1, -1, -e, 1, e)
    asym = sp.expand(pair(Hp, Op(H, famp)) - pair(Op(Hp, famp), H))
    esol = sp.solve(list(set(sp.Poly(asym, *hs, *gs, *k).coeffs())), [e], dict=True)
    check('(1b) self-adjointness then fixes e=-1: the linearised Einstein operator', esol == [{e: -1}], str(esol))
    xi = sp.symbols('x0:4'); Hg = sp.Matrix(4, 4, lambda m, n: k[m] * xi[n] + k[n] * xi[m])
    check('(1c) pure-gauge fields k_m xi_n + k_n xi_m are annihilated', sp.simplify(Op(Hg, EIN)) == sp.zeros(4, 4))
    trH = sum(eta[i, i] * H[i, i] for i in range(4)); Om = Op(H, EIN) - mm ** 2 * (H - eta * trH)
    divm = [sp.expand(sum(ku[m] * Om[m, n] for m in range(4))) for n in range(4)]
    check('(1d) a Fierz-Pauli mass term makes the divergence nonzero for generic fields', any(dv != 0 for dv in divm))
    # (2) universality
    k1, k2_, J = sp.symbols('kappa1 kappa2 J')
    resid = sp.expand(k1 * J + k2_ * (-J))
    check('(2) coupled species: divergence of kappa1 T1 + kappa2 T2 is (kappa1 - kappa2) J, zero for J != 0 only if kappa1 = kappa2',
          sp.solve(resid, k1) == [k2_], f'divergence = {sp.factor(resid)}')
    # (3a) static source, harmonic gauge
    Mq = sp.symbols('M', positive=True); st = {k[0]: 0}; T = sp.zeros(4, 4); T[0, 0] = Mq
    Hb = H - eta * trH / 2; G = Op(H, EIN)
    eqs = [sp.expand(G[m, n].subs(st) + T[m, n]) for m in range(4) for n in range(m, 4)] + [sp.expand(sum(ku[m] * Hb[m, n] for m in range(4))).subs(st) for n in range(4)]
    sol = sp.solve(eqs, hs, dict=True)[0]; Hs = H.subs(sol)
    ok = all(sp.simplify(Hs[i, j] - (Hs[0, 0] if i == j else 0)) == 0 for i in range(1, 4) for j in range(1, 4)) and all(sp.simplify(Hs[0, j]) == 0 for j in range(1, 4))
    check('(3a) O=-T static Fourier particular solution at |k|>0: h_ij = h_00 delta_ij and h_0i = 0', ok, f'h_00 = {sp.simplify(Hs[0, 0])}')
    # (3b) rays
    def deflect(gam, v, Mb=1e-4, bb=1.0):
        E = 1.0
        def rhs(t, y):
            x, yy, px, py = y; r = np.hypot(x, yy); Phi = -Mb / r; dPhi = np.array([x, yy]) * Mb / r ** 3
            giu = 1 / (1 - 2 * gam * Phi); dg00u = (2 / (1 + 2 * Phi) ** 2) * dPhi; dgiu = (2 * gam / (1 - 2 * gam * Phi) ** 2) * dPhi
            p2 = px * px + py * py
            return [giu * px, giu * py, -0.5 * (dg00u[0] * E * E + dgiu[0] * p2), -0.5 * (dg00u[1] * E * E + dgiu[1] * p2)]
        Lr = 4000.0; s = solve_ivp(rhs, [0, 2 * Lr / v], [-Lr, bb, E * v, 0.0], rtol=1e-11, atol=1e-14)
        return -np.arctan2(s.y[3, -1], s.y[2, -1])
    rows = [(g_, v, deflect(g_, v), 2e-4 * (1 / v ** 2 + g_)) for g_ in (1.0, 0.0) for v in (1.0, 0.5, 0.2)]
    check('(3b) six supplied finite ray cases agree within 0.1% with leading weak-field coefficient (2M/b)(1/v^2 + gamma)',
          all(abs(r[2] / r[3] - 1) < 1e-3 for r in rows), '; '.join(f'gamma={r[0]:.0f} v={r[1]}: {r[2]:.4e} vs {r[3]:.4e}' for r in rows))
    # (4) Englert relation
    rng = np.random.default_rng(1); worst_pure = 0.0; worst_mixed = -1.0
    for _ in range(400):
        w1 = rng.random(); w2 = 1 - w1
        x1 = rng.normal(size=3) + 1j * rng.normal(size=3); x2 = rng.normal(size=3) + 1j * rng.normal(size=3); x1 /= np.linalg.norm(x1); x2 /= np.linalg.norm(x2)
        D = np.sum(abs(np.linalg.eigvalsh(w1 * np.outer(x1, x1.conj()) - w2 * np.outer(x2, x2.conj())))); V = 2 * np.sqrt(w1 * w2) * abs(np.vdot(x1, x2))
        worst_pure = max(worst_pure, abs(D * D + V * V - 1))
        A1 = rng.normal(size=(3, 3)) + 1j * rng.normal(size=(3, 3)); r1 = A1 @ A1.conj().T; r1 /= np.trace(r1)
        A2 = rng.normal(size=(3, 3)) + 1j * rng.normal(size=(3, 3)); r2 = A2 @ A2.conj().T; r2 /= np.trace(r2)
        Dm = np.sum(abs(np.linalg.eigvalsh(w1 * r1 - w2 * r2)))
        ev1, U1 = np.linalg.eigh(r1); s1 = U1 @ np.diag(np.sqrt(np.clip(ev1, 0, None))) @ U1.conj().T
        ev2, U2 = np.linalg.eigh(r2); s2 = U2 @ np.diag(np.sqrt(np.clip(ev2, 0, None))) @ U2.conj().T
        Vm = 2 * np.sqrt(w1 * w2) * np.sum(np.linalg.svd(s1 @ s2, compute_uv=False))
        worst_mixed = max(worst_mixed, Dm * Dm + Vm * Vm - 1)
    check('(4) 400 seeded marker cases: weighted D and supplied pure visibility/mixed fidelity envelope satisfy duality',
          worst_pure < 1e-12 and worst_mixed <= 1e-12, f'pure max |D^2+V^2-1| {worst_pure:.1e}; mixed max D^2+V^2-1 {worst_mixed:.3f}')
    # (5) Dirac scalar density
    p1, p2, p3, mq = sp.symbols('p1 p2 p3 mq', positive=True); Z = sp.zeros(2, 2); I2 = sp.eye(2)
    sx = sp.Matrix([[0, 1], [1, 0]]); sy = sp.Matrix([[0, -sp.I], [sp.I, 0]]); sz = sp.Matrix([[1, 0], [0, -1]])
    al = [sp.Matrix(sp.BlockMatrix([[s, Z], [Z, -s]])) for s in (sx, sy, sz)]; beta = sp.Matrix(sp.BlockMatrix([[Z, I2], [I2, Z]]))
    Hd = p1 * al[0] + p2 * al[1] + p3 * al[2] + mq * beta; E = sp.sqrt(p1 ** 2 + p2 ** 2 + p3 ** 2 + mq ** 2)
    P = (sp.eye(4) + Hd / E) / 2                                    # projector onto positive energy
    ok5 = sp.simplify((P * beta * P - (mq / E) * P)) == sp.zeros(4, 4)
    check('(5) compression P beta P=(m/E)P; fixed momentum, E>0, nonzero positive-energy spinor gives density ratio m/E', ok5)
    # Non-invariance countercontrol; no new physical identification.
    Pc = np.array(P.subs({p1: 2, p2: 0, p3: 0, mq: 1})).astype(complex)
    bc = np.array(beta).astype(complex)
    leakage = np.linalg.norm((np.eye(4) - Pc) @ bc @ Pc)
    compression = np.linalg.norm(Pc @ bc @ Pc - Pc / np.sqrt(5))
    check('(5-control) compression does not imply beta preserves positive energy',
          leakage > 1 and compression < 1e-12, f'leakage {leakage}; compression residual {compression}')
    identical = np.diag([1., 0., 0.])
    weighted = np.sum(abs(np.linalg.eigvalsh(.2 * identical - .8 * identical)))
    ordinary = .5 * np.sum(abs(np.linalg.eigvalsh(identical - identical)))
    check('(4-control) unequal-prior distinguishability differs from ordinary trace distance',
          abs(weighted - .6) < 1e-12 and ordinary == 0, f'weighted {weighted}; ordinary {ordinary}')
    # (6) chain rule and record entanglement
    Px = rng.random(40); Px /= Px.sum(); j = int(np.argmax(Px)); Hf = lambda q: float(-np.sum(q[q > 0] * np.log2(q[q > 0])))
    pr = np.array([Px[j], 1 - Px[j]]); rest = np.where(np.arange(40) == j, 0, Px) / (1 - Px[j])
    lhs = Hf(Px); rhs_ = pr[1] * Hf(rest) + Hf(pr)
    amp = np.sqrt(Px) * np.exp(1j * rng.random(40)); Aj = np.zeros((40, 2), complex); Aj[np.arange(40), (np.arange(40) == j).astype(int)] = amp
    ev = np.clip(np.linalg.eigvalsh(Aj.T @ Aj.conj()), 0, None)
    check('(6) H(X) = sum p(r) H(X|r) + H(R) for a record that is a function of X, and the record qubit carries H(R) as entanglement',
          abs(lhs - rhs_) < 1e-12 and abs(Hf(ev) - Hf(pr)) < 1e-12, f'H(X) {lhs:.6f} = {rhs_:.6f}; record entropy {Hf(ev):.6f}')
    print('per_site: the homogeneous two-derivative operator ansatz, self-adjointness, normalization, static particular solution, metric and marker preparation, ray setup and random seeds are supplied choices.')
    print('lattice_wide: no physical field equation, coupling value, extra-scalar exclusion or empirical identification is established.')
    print('elapsed_seconds', round(time.monotonic() - _STARTED, 1))
    print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
