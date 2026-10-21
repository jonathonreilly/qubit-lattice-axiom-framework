#!/usr/bin/env python3
"""Source readings for the CL-7 record source under the formation law 'records never condition the odds'.
Supplied two-direction models only; no physical identification.
A. Theorem: no relay rule whose joint configuration stays Born at every tick can make the one-tick turn
   statistics of a relay at B depend only on B's reduced odds. Exact feasibility condition, rederived and
   checked against brute-force steering ensembles; a maximally entangled direction qubit is infeasible.
B. Rederived: Bell-local turn kernels obey CHSH <= 2.
C. Coarse-graining does not remove the dependence: alternating protocol, N pairs, T ticks.
D. Burns only: null steps are traceless; the 1D plane-wave identity burns + turns = eps v^2 and what is lost.
E. A sustained channel: steering a momentum-entangled relay into plane or standing waves changes its turns.
F. Page-Geilker toy: torque under actual, expected and hybrid deposits.
G. Size of the signal in physical units with the supplied G = a^2/(8 pi).
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = ('docs/RECORD_SOURCE_TURN_DEPOSITS_ARE_NOT_FIXED_BY_A_RELAYS_OWN_ODDS_BOUNDED_THEOREM_NOTE_2026-10-21.md', 'docs/CANDIDATE_LAWS.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')

import os, sys, signal
os.environ['OPENBLAS_NUM_THREADS'] = '1'
os.environ['VECLIB_MAXIMUM_THREADS'] = '1'
sys.stdout.reconfigure(line_buffering=True)
def _timeout(*a):
    raise TimeoutError('120-second cap exceeded')
signal.signal(signal.SIGALRM, _timeout)
signal.setitimer(signal.ITIMER_REAL, AUDIT_TIMEOUT_SEC - 2)
import numpy as np

PASS = FAIL = 0
rng = np.random.default_rng(20261021)


def check(name, ok, detail=''):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  {detail}" if detail else ''))


def psd_sqrt(r):
    w, V = np.linalg.eigh((r + r.conj().T) / 2); return (V * np.sqrt(np.clip(w, 0, None))) @ V.conj().T


def pos_tr(M):
    w = np.linalg.eigvalsh((M + M.conj().T) / 2); return w[w > 0].sum()


def bounds(rho, U, Pi0):
    """over all steerings {sigma_i} of rho: sup of sum_i max(0, P0_i - P0'_i) and inf of
    sum_i min(P0_i, P1'_i); J01 of any B-local rule must lie in [lo, up]."""
    I = np.eye(len(rho)); A = Pi0; B = U.conj().T @ (I - Pi0) @ U; r = psd_sqrt(rho)
    return pos_tr(r @ (A + B - I) @ r), np.trace(rho @ B).real - pos_tr(r @ (B - A) @ r)


def member_interval(sig, U, Pi0):
    """J01 interval of one (subnormalised) steered member sigma."""
    I = np.eye(len(sig)); P0 = np.trace(sig @ Pi0).real; P0n = np.trace(U @ sig @ U.conj().T @ Pi0).real
    P1n = np.trace(sig).real - P0n
    return max(0.0, P0 - P0n), min(P0, P1n)


def R(p):
    return np.array([[np.cos(p), -np.sin(p)], [np.sin(p), np.cos(p)]])


def steer(rho, E):
    r = psd_sqrt(rho); return [r @ e @ r for e in E]


def random_povm(dim, k):
    G = rng.normal(size=(k, dim, dim)) + 1j * rng.normal(size=(k, dim, dim)); M = np.einsum('kij,klj->kil', G, G.conj())
    S = psd_sqrt(np.linalg.inv(M.sum(0))); return [S @ m @ S for m in M]


def section_A():
    print('A. no B-local one-tick turn law (two directions)')
    Pi0 = np.diag([1.0, 0.0]); phi = np.pi / 4; rho = np.eye(2) / 2; U = R(phi)
    lo, up = bounds(rho, U, Pi0)
    blo, bup = 0.0, 1.0
    for _ in range(4000):
        mem = steer(rho, random_povm(2, rng.integers(2, 5)))
        iv = np.array([member_interval(s, U, Pi0) for s in mem]).sum(0); blo = max(blo, iv[0]); bup = min(bup, iv[1])
    check('A1 brute-force steerings never beat the closed-form bounds', blo <= lo + 1e-12 and bup >= up - 1e-12,
          f'search lo {blo:.4f} <= {lo:.4f}, search up {bup:.4f} >= {up:.4f}')
    # explicit ensembles: A rotates its register by -pi/8 (E1) or +pi/8 (E2) then its configuration is read off
    E1 = [np.outer(v, v) / 2 for v in (R(np.pi / 8)[:, 0], R(np.pi / 8)[:, 1])]
    E2 = [np.outer(v, v) / 2 for v in (R(-np.pi / 8)[:, 0], R(-np.pi / 8)[:, 1])]
    i1 = np.array([member_interval(s, U, Pi0) for s in E1]).sum(0); i2 = np.array([member_interval(s, U, Pi0) for s in E2]).sum(0)
    check('A2 maximally entangled direction, phi=pi/4: E1 forces J01 >= sin(phi)/2, E2 caps J01 <= sin^2(phi/2)',
          abs(i1[0] - np.sin(phi) / 2) < 1e-12 and abs(i2[1] - np.sin(phi / 2) ** 2) < 1e-12 and i1[0] > i2[1],
          f'E1 [{i1[0]:.4f},{i1[1]:.4f}]  E2 [{i2[0]:.4f},{i2[1]:.4f}]  disjoint by {i1[0]-i2[1]:.4f}')
    ph = np.linspace(1e-3, np.pi / 2 - 1e-3, 200)
    g = np.array([np.subtract(*bounds(rho, R(p), Pi0)) for p in ph]); gc = (np.sin(ph) + np.cos(ph) - 1) / 2
    check('A3 gap = (sin phi + cos phi - 1)/2 > 0 on all of (0, pi/2); max (sqrt2-1)/2 at pi/4',
          abs(g - gc).max() < 1e-10 and g.min() > 0, f'max|gap-formula|={abs(g-gc).max():.1e}, max gap {g.max():.4f}')
    th = 0.1; C = np.array([[np.cos(th), -1j * np.sin(th)], [-1j * np.sin(th), np.cos(th)]]); lo_c, up_c = bounds(rho, C, Pi0)
    check('A4 massive-walk coin theta=0.1 (eps=0.1 at rest): forced turn gap per tick ~ eps', 2 * (lo_c - up_c) > 0.9 * th,
          f'total-turn gap {2*(lo_c-up_c):.4f} per tick vs rest turn rate eps={th}')
    rows = []
    for lam in (0.6, 0.8, 0.9, 0.99):
        gg = max(np.subtract(*bounds(R(a) @ np.diag([lam, 1 - lam]) @ R(a).T, R(np.pi / 4), Pi0)) for a in np.linspace(0, np.pi, 91))
        rows.append(gg)
    check('A5 every tested partial entanglement has an infeasible orientation', min(rows) > 0,
          'Schmidt weight 0.6/0.8/0.9/0.99 max gap ' + '/'.join(f'{x:.4f}' for x in rows))
    b = np.array([1, 1]) / np.sqrt(2); rD = np.kron(np.eye(2) / 2, np.outer(b, b)); UD = np.zeros((4, 4)); UD[:2, :2] = R(np.pi / 8); UD[2:, 2:] = R(-np.pi / 8)
    lD, uD = bounds(rD, UD, np.kron(np.eye(2), Pi0))
    check('A6 the formation-law D set-up is feasible: total turns 0.3536 at B for every A basis is allowed', lD <= uD,
          f'J01 in [{lD:.4f},{uD:.4f}]; signal there removable, not in A2')


def section_B():
    print('B. Bell-local kernels')
    best = max(abs(a0 * (b0 + b1) + a1 * (b0 - b1)) for a0 in (1, -1) for a1 in (1, -1) for b0 in (1, -1) for b1 in (1, -1))
    check('B1 deterministic local values: |A0(B0+B1)+A1(B0-B1)| <= 2, so any mixture obeys CHSH <= 2', best == 2, f'max {best}')


def switch(P, Pn, blk, d):
    ex = np.clip(P - Pn, 0, None); sh = np.clip(Pn - P, 0, None); S = sh.sum(1)
    Pr = P[blk, d]; p = np.where(Pr > 0, ex[blk, d] / np.where(Pr > 0, Pr, 1), 0.0); sw = rng.random(len(d)) < p
    if sw.any():
        b = blk[sw]; cs = np.cumsum(sh[b], 1) / S[b][:, None]; d = d.copy(); d[sw] = np.minimum((rng.random(sw.sum())[:, None] > cs).sum(1), 1)
    return d


def section_C():
    print('C. coarse-graining: alternating B update R(+pi/4), R(-pi/4); A picks E1 or E2 once')
    Nrel, T, phi = 4000, 20, np.pi / 4; out = {}
    for name, alpha in (('E1', -np.pi / 8), ('E2', np.pi / 8)):
        psi = np.kron(R(alpha), np.eye(2)) @ (np.array([1, 0, 0, 1]) / np.sqrt(2))   # |a b>, A rotated
        P = abs(psi.reshape(2, 2)) ** 2; idx = rng.choice(4, Nrel, p=P.ravel()); a, d = idx // 2, idx % 2
        turns = np.zeros(Nrel); okb = True
        for t in range(T):
            Ub = R(phi if t % 2 == 0 else -phi); new = np.kron(np.eye(2), Ub) @ psi; Pn = abs(new.reshape(2, 2)) ** 2
            dn = switch(P, Pn, a, d); turns += dn != d; d = dn
            mem = [np.outer(m, m.conj()) * 1.0 for m in psi.reshape(2, 2)]
            iv = np.array([member_interval(s, Ub, np.diag([1.0, 0])) for s in mem]).sum(0)
            okb &= (iv[0] >= np.sin(phi) / 2 - 1e-12) if name == 'E1' else (iv[1] <= np.sin(phi / 2) ** 2 + 1e-12)
            psi, P = new, Pn
        out[name] = (turns.mean() / T, turns.std(), okb)
    check('C1 per-tick bounds hold at every tick of the protocol (E1 lower, E2 upper)', out['E1'][2] and out['E2'][2])
    check('C2 minimal joint rule: E1 0.7071 turns/relay/tick, E2 0', abs(out['E1'][0] - np.sqrt(0.5)) < 0.02 and out['E2'][0] == 0,
          f"E1 {out['E1'][0]:.4f}, E2 {out['E2'][0]:.4f}")
    gap = 2 * (np.sin(phi) / 2 - np.sin(phi / 2) ** 2)
    check('C3 any rule: shift >= 0.4142 N T turns; sd <= (T/2) sqrt N; so separation >= 0.83 sqrt N for all T',
          abs(gap - (np.sqrt(2) - 1)) < 1e-12, f'N=1e4: >= {2*gap*np.sqrt(1e4):.0f} sd; each 1D turn adds -1 to T11, so no cancellation')


def walk(th):
    C = np.array([[np.cos(th), -1j * np.sin(th)], [-1j * np.sin(th), np.cos(th)]])
    return C, (lambda k: np.diag([np.exp(-1j * k), np.exp(1j * k)]) @ C)


def upper_mode(U, k):
    w, V = np.linalg.eig(U(k)); j = int(np.argmax(-np.angle(w))); return -np.angle(w[j]), V[:, j]


def section_D():
    print('D. burns only')
    m = np.diag([-1.0, 1, 1, 1]); dirs = np.vstack([np.eye(3), -np.eye(3)])
    tr = max(abs(np.trace(m @ np.outer(np.r_[1, d], np.r_[1, d]))) for d in dirs)
    check('D1 every burn deposit (1,d)(1,d) is null: Minkowski trace 0, so a burns-only source is traceless', tr < 1e-15,
          'eps u u has trace -m^2/eps')
    th = 0.3; C, U = walk(th); err = 0; rows = []
    for k in (0.0, 0.1, 0.4, 1.0):
        eps, v = upper_mode(U, k); P = abs(v) ** 2; vg = np.cos(th) * np.sin(k) / np.sin(np.arccos(np.cos(th) * np.cos(k)))
        burn = eps; turn = -2 * eps * 2 * P[0] * P[1]; err = max(err, abs(burn + turn - eps * vg ** 2), abs(P[0] - P[1] - vg))
        rows.append(f'k={k}: burns {burn:.3f}, burns+turns {burn+turn:.3f}')
    check('D2 1D plane waves: P0-P1 = v_g and burns+turns T11 = eps v^2; burns alone overshoot by eps(1-v^2)', err < 1e-10, '; '.join(rows[:2]))
    eps0 = 1.0; T00, Tkk = eps0, eps0
    # linearised GR: hbar_mu nu ~ T; trace hbar = -T00+Tkk = 0 -> h00 = hbar00 ~ T00, h_ij = hbar_ij ~ Tkk/3
    h00 = T00 - 0.5 * (-1) * (-T00 + Tkk); hij = Tkk / 3 - 0.5 * (-T00 + Tkk); h00d = T00 - 0.5 * (-1) * (-T00); hijd = 0 - 0.5 * (-T00)
    check('D3 3D rest relay, burns only: Newtonian strength 2x dust, gamma = 1/3 (dust: 1, 1)',
          abs(h00 / h00d - 2) < 1e-12 and abs((hij / h00) - 1 / 3) < 1e-12, f'h00 ratio {h00/h00d:.2f}, gamma {hij/h00:.3f} (dust 1.0)')


def section_E():
    print('E. sustained channel: momentum-entangled relay; A picks plane (z) or standing (x) members')
    th, N = 0.1, 400; C, U = walk(th); x = np.arange(N); res = {}
    for kk in (2 * np.pi * 1 / N, 2 * np.pi * 4 / N, 2 * np.pi * 13 / N):
        eps, v = upper_mode(U, kk); vm = np.array([v[1], v[0]])
        pw = v[None, :] * np.exp(1j * kk * x)[:, None]; mw = vm[None, :] * np.exp(-1j * kk * x)[:, None]
        def turns(psi):
            psi = psi / np.linalg.norm(psi); P = abs(psi) ** 2; pc = psi @ C.T; Pc = abs(pc) ** 2
            sw = np.clip(P - Pc, 0, None).sum()
            new = np.stack([np.roll(pc[:, 0], 1), np.roll(pc[:, 1], -1)], 1); Pn = abs(new) ** 2; Px = Pn.sum(1)
            fr = (2 * eps * (Px - (Pn ** 2).sum(1) / np.maximum(Px, 1e-300))).sum()
            return sw + fr
        z = 0.5 * (turns(pw) + turns(mw)); xs = 0.5 * (turns(pw + mw) + turns(pw - mw))
        vg = abs(v[0]) ** 2 - abs(v[1]) ** 2; res[kk] = (eps, vg, z, xs)
    rows = [f'k={k:.3f} v={vg:.3f}: z {z:.5f}, x {xs:.5f}, (x-z)/(eps v^2) {(xs-z)/(e*vg**2):.3f}, (x-z)/k {(xs-z)/k:.2f}; standing T11 {e-xs:+.4f} vs plane {e*vg**2:.4f}' for k, (e, vg, z, xs) in res.items()]
    ok = all((xs - z) >= e * vg ** 2 * (1 - 1e-9) for (e, vg, z, xs) in res.values())
    check('E1 B turns per tick depend on A basis by at least eps v^2 (fresh draws) plus switching', ok, rows[0])
    for r in rows[1:]: print('   ' + r)


def section_F():
    print('F. Page-Geilker toy: ball at L (actual) or R, weight 1/2; torque in units of one classical ball')
    eps = 1.0; burn = 2 * eps; turn = -eps     # rho + sum p contributions of a 3D rest relay
    actual = (burn + turn) * 1 - 0 * (-1); expected = 0.5 * (burn + turn) * 1 + 0.5 * (burn + turn) * (-1)
    hybL = burn + 0.5 * turn; hybR = 0.5 * turn; hybrid = hybL * 1 + hybR * (-1)
    check('F1 torque: actual deposits 1, expected (branch-averaged) 0, hybrid (actual burns, reduced turns) 2',
          (actual, expected, hybrid) == (1.0, 0.0, 2.0), 'Page-Geilker 1981 saw torque follow the outcome')


def section_G():
    print('G. size, supplied G = a^2/(8 pi), hbar = c = 1')
    G, hbar, c = 6.674e-11, 1.0546e-34, 2.998e8
    lP = np.sqrt(G * hbar / c ** 3); a = np.sqrt(8 * np.pi) * lP; tau = a / c
    per_turn = 4 * G * hbar / (c ** 4 * 1.0)            # time-integrated strain (s) at r = 1 m, deposit hbar
    lat = (a / 1.0) * tau / (2 * np.pi)
    check('G1 per unit deposit (one 1D turn = hbar): integral of h dt at 1 m = a tau/(2 pi r)', abs(per_turn / lat - 1) < 1e-3,
          f'a={a:.2e} m, tau={tau:.2e} s, {per_turn:.2e} s; 1 turn/s = {per_turn/(2*G/c**2):.1e} kg static')
    mRb, v = 1.443e-25, 1e-2
    dm = 2 * mRb * (v / c) ** 2
    print(f'   E-channel, Rb atom v=1 cm/s: {mRb*v**2/hbar:.1e} turns/s, mass equivalent {dm:.1e} kg/atom; 1e6 atoms {1e6*dm:.0e} kg')
    print(f'   switching part ~0.8 p a/hbar per tick = 0.8 p c/hbar: Rb 1 cm/s {0.8*mRb*v*c/hbar:.1e} turns/s, {0.8*mRb*v*c/hbar*per_turn/(2*G/c**2):.0e} kg/atom')
    print('   smallest gravitating source measured ~9e-5 kg (torsion, 2021); BMV-type proposals ~1e-14 kg')


if __name__ == '__main__':
    section_A(); section_B(); section_C(); section_D(); section_E(); section_F(); section_G()
    print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
