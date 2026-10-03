"""A28 c1: no-signalling of GATED formation inside the Option R package (supplied toy).

Sites (1D line): 0:a 1:y 2:x 3:w | distant 4:b 5:d.  Local bonds a-y, y-x, x-w.
Records are classical labels (site -> pure content); a recorded site's qubit is
always the content (cut to agree).  Per tick:
  Stage 1: every EMPTY site with >= 1 PRE-TICK recorded neighbour (gate open) applies
           one joint instrument: form+lock k (P_k sqrt F), claim record i
           (sqrt(c/z W_i)), or nothing (sqrt(1 - F - sum c/z W_i)).  Gate closed:
           identity (F = 0, no claims).
  Stage 2: a record claimed by several sites picks one uniformly (CL, A27).
  Stage 3: SWAP for winning claims (SW step, A27); new records added.
  Then smooth compressed change exp(-i Q H Q tau), H = J sum SWAP on local bonds.
Distant choice: d absent (b gated off), d=|0> (b forms, Z menu), d=|+> (b forms,
X menu).  b's outcome is unread locally.  b is entangled with the local sites.
Rule CUT  = the Option R instruments above (linear).
Rule UNCUT = claims happen with odds c/z <W> on the snapshot, but the claimant's
possibility is NOT cut (no sqrt W filter): a record place set without the cut.
Output: TV of the local record-history law across the three distant choices.
"""
import itertools, signal, sys
import numpy as np
from scipy.linalg import expm

signal.alarm(55)
N = 6
LOCAL = [0, 1, 2, 3]
BONDS = [(0, 1), (1, 2), (2, 3)]
NBR = {0: [1], 1: [0, 2], 2: [1, 3], 3: [2]}
Z1D = 2  # coordination number in 1D

SW2 = np.array([[1, 0, 0, 0], [0, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, 1]], dtype=complex)


def apply(op, sites, psi):
    """Apply a k-site operator (2^k x 2^k, sites in the given order) to state psi (shape (2,)*N)."""
    k = len(sites)
    opt = op.reshape((2,) * (2 * k))
    out = np.tensordot(opt, psi, axes=(list(range(k, 2 * k)), sites))
    return np.moveaxis(out, list(range(k)), sites)


def full_op(op, sites):
    """Dense N-qubit matrix of a k-site operator (for the change generator)."""
    dim = 2 ** N
    M = np.zeros((dim, dim), dtype=complex)
    for j in range(dim):
        e = np.zeros(dim, dtype=complex); e[j] = 1
        M[:, j] = apply(op, sites, e.reshape((2,) * N)).reshape(dim)
    return M


def psd_sqrt(A):
    w, v = np.linalg.eigh((A + A.conj().T) / 2)
    w = np.clip(w, 0, None)
    return (v * np.sqrt(w)) @ v.conj().T


def rand_psd(k, rng):
    X = rng.normal(size=(2 ** k, 2 ** k)) + 1j * rng.normal(size=(2 ** k, 2 ** k))
    G = X @ X.conj().T
    return G / np.linalg.eigvalsh(G).max()


def vr(r):
    """Unitary with V|0> = |r>, V|1> = |r_perp>."""
    rp = np.array([-np.conj(r[1]), np.conj(r[0])])
    return np.column_stack([r, rp])


H_full = sum(full_op(SW2, list(b)) for b in BONDS)


def change(psi, recs, tau, J=1.0):
    if tau == 0:
        return psi
    Q = np.array([[1.0 + 0j]])
    for s in range(N):
        P = np.outer(recs[s], recs[s].conj()) if s in recs else np.eye(2)
        Q = np.kron(Q, P)
    HR = Q @ (J * H_full) @ Q
    U = expm(-1j * tau * HR)
    return (U @ psi.reshape(-1)).reshape((2,) * N)


class Model:
    def __init__(self, rng, p=0.4, c=0.5, alpha=0.9, beta=0.2, tau=0.3):
        self.p, self.c, self.alpha, self.beta, self.tau = p, c, alpha, beta, tau
        self.G = {0: rand_psd(1, rng), 1: rand_psd(2, rng)}  # weight shapes, by # unrecorded nbrs

    def W(self, r):
        return self.beta * np.eye(2) + (self.alpha - self.beta) * np.outer(r, r.conj())

    def instrument(self, s, recs_pre):
        """Joint per-site instrument at empty site s given the pre-tick pattern.
        Returns list of (label, kraus, sites, claim_target) for the CUT rule."""
        rn = [i for i in NBR[s] if i in recs_pre]
        if not rn:  # gate closed: F = 0, nothing to claim -> identity
            return None
        un = [i for i in NBR[s] if i not in recs_pre and i in LOCAL]
        sites = [s] + un
        r0 = recs_pre[rn[0]]
        V = vr(r0)
        Vfull = V
        for _ in un:
            Vfull = np.kron(Vfull, V)
        F = self.p * Vfull @ self.G[len(un)] @ Vfull.conj().T
        sF = psd_sqrt(F)
        out = []
        for k in range(2):  # menu set by the recorded neighbour (Q7): {|r>, |r_perp>}
            m = V[:, k]
            Pk = np.outer(m, m.conj())
            for _ in un:
                Pk = np.kron(Pk, np.eye(2))
            out.append((('form', k), Pk @ sF, sites, None))
        Wsum = np.zeros_like(F)
        for i in rn:
            Wi = (self.c / Z1D) * self.W(recs_pre[i])
            Wi_full = Wi
            for _ in un:
                Wi_full = np.kron(Wi_full, np.eye(2))
            Wsum = Wsum + Wi_full
            out.append((('claim', i), psd_sqrt(Wi_full), sites, i))
        E0 = np.eye(2 ** len(sites)) - F - Wsum
        assert np.linalg.eigvalsh(E0).min() > -1e-12
        out.append((('none',), psd_sqrt(E0), sites, None))
        return out, F, Wsum, rn


def tick(branches, model, rule):
    """branches: list of (hist, psi, recs, weight). CUT: psi unnormalised, weight=1.
    UNCUT: psi normalised, weight = probability."""
    new = []
    for hist, psi, recs, wgt in branches:
        recs_pre = dict(recs)
        empties = [s for s in LOCAL if s not in recs_pre]
        # Stage 1, sequential over gated empty sites (fixed order)
        stage = [((), psi, wgt, [])]  # (outcomes, psi, weight, claims)
        for s in empties:
            inst = model.instrument(s, recs_pre)
            if inst is None:
                continue
            kr, F, Wsum, rn = inst
            nxt = []
            for outs, ph, wg, cl in stage:
                if rule == 'cut':
                    for lab, K, sites, tgt in kr:
                        ph2 = apply(K, sites, ph)
                        if np.vdot(ph2, ph2).real < 1e-30:
                            continue
                        nxt.append((outs + ((s,) + lab,), ph2, wg, cl + ([(tgt, s)] if tgt is not None else [])))
                else:  # UNCUT claims: odds on the snapshot, no cut of the claimant
                    nrm = np.sqrt(np.vdot(ph, ph).real)
                    phn = ph / nrm
                    tot = 0.0
                    for lab, K, sites, tgt in kr:
                        if lab[0] == 'form':
                            ph2 = apply(K, sites, phn)
                            pr = np.vdot(ph2, ph2).real
                            if pr < 1e-30:
                                continue
                            tot += pr
                            nxt.append((outs + ((s,) + lab,), ph2 / np.sqrt(pr), wg * pr, cl))
                        elif lab[0] == 'claim':
                            Wi = K.conj().T @ K
                            pr = np.vdot(phn, apply(Wi, sites, phn)).real
                            tot += pr
                            nxt.append((outs + ((s,) + lab,), phn, wg * pr, cl + [(tgt, s)]))
                    pnone = 1.0 - tot
                    K0 = psd_sqrt(np.eye(F.shape[0]) - F)
                    ph2 = apply(K0, [s] + [i for i in NBR[s] if i not in recs_pre and i in LOCAL], phn)
                    ph2 = ph2 / np.sqrt(np.vdot(ph2, ph2).real)
                    nxt.append((outs + ((s, 'none'),), ph2, wg * pnone, cl))
            stage = nxt
        # Stage 2 + 3: resolve claims (uniform pick), SWAP, update records
        for outs, ph, wg, cl in stage:
            targets = {}
            for tgt, s in cl:
                targets.setdefault(tgt, []).append(s)
            choices = [[(t, s) for s in ss] for t, ss in sorted(targets.items())]
            for combo in itertools.product(*choices) if choices else [()]:
                pw = 1.0
                for t, ss in sorted(targets.items()):
                    pw /= len(ss)
                rec2 = dict(recs_pre)
                ph2 = ph
                for t, s in combo:
                    ph2 = apply(SW2, [t, s], ph2)
                    rec2[s] = rec2.pop(t)
                for o in outs:
                    if o[1] == 'form':
                        V = vr(recs_pre[[i for i in NBR[o[0]] if i in recs_pre][0]])
                        rec2[o[0]] = V[:, o[2]]
                if rule == 'cut':
                    ph3 = change(ph2 * np.sqrt(pw), rec2, model.tau)
                    new.append((hist + (outs, combo), ph3, rec2, 1.0))
                else:
                    ph3 = change(ph2, rec2, model.tau)
                    new.append((hist + (outs, combo), ph3, rec2, wg * pw))
    return new


def local_law(model, psi0, recs0, cond, rule, nticks, rng_b):
    """Distant step at b (gated by d), then nticks local ticks. Returns dict hist->prob."""
    branches0 = []
    if cond == 'absent':
        branches0.append(((), psi0, dict(recs0), 1.0))
    else:
        menu = np.eye(2, dtype=complex) if cond == 'Z' else np.array([[1, 1], [1, -1]], dtype=complex) / np.sqrt(2)
        Fb = 0.8 * rng_b
        sFb = psd_sqrt(Fb)
        kb = [menu[:, [k]] @ menu[:, [k]].conj().T @ sFb for k in range(2)] + [psd_sqrt(np.eye(2) - Fb)]
        for K in kb:
            ph = apply(K, [4], psi0)
            pr = np.vdot(ph, ph).real
            if pr < 1e-30:
                continue
            if rule == 'cut':
                branches0.append(((), ph, dict(recs0), 1.0))
            else:
                branches0.append(((), ph / np.sqrt(pr), dict(recs0), pr))
    br = branches0
    for _ in range(nticks):
        br = tick(br, model, rule)
    law = {}
    for hist, ph, recs, wg in br:
        pr = np.vdot(ph, ph).real if rule == 'cut' else wg
        law[hist] = law.get(hist, 0.0) + pr
    return law


def tv(a, b):
    keys = set(a) | set(b)
    return 0.5 * sum(abs(a.get(k, 0.0) - b.get(k, 0.0)) for k in keys)


def ghz_example(cz=1.0, p=1.0):
    """Closed form: y,x,b in GHZ; record a moves to y (claim effect cz*|0><0|_y),
    then x forms with F = p|1><1|_x gated by the record now at y. No change."""
    def law(cond, cut):
        # GHZ on (y,x,b): (|000>+|111>)/sqrt2 ; branches by b's record
        if cond == 'none':
            branches = [(0.5, None)]  # snapshot is the GHZ state itself
        else:
            branches = [(0.5, 0), (0.5, 1)]  # Z record at b
        P = 0.0
        for wb, bval in branches:
            if bval is None:
                # rho_y = rho_x = I/2, joint (y,x) = (|00><00| + |11><11|)/2
                if cut:
                    P += 1.0 * cz * p * 0.0  # tr(|0><0|_y |1><1|_x rho) = 0
                else:
                    P += 1.0 * (cz * 0.5) * (p * 0.5)
            else:
                pm = cz * (1.0 if bval == 0 else 0.0)
                pf = p * (1.0 if bval == 1 else 0.0)  # x = bval after the cut
                P += wb * pm * pf
        return P
    out = {}
    for cut in (True, False):
        a, b = law('none', cut), law('Z', cut)
        out['cut' if cut else 'uncut'] = (a, b, abs(a - b))
    return out


if __name__ == '__main__':
    print('GHZ closed-form example (claim then gated formation), P(move & form):')
    for k, (a, b, d) in ghz_example().items():
        print(f'  {k:5s}: b no record {a:.4f}   b Z-record {b:.4f}   |diff| = {d:.4f}')
    nticks = 3
    worst = {'cut': 0.0, 'uncut': 0.0}
    smallest_uncut = 1.0
    for seed in range(6):
        rng = np.random.default_rng(1000 + seed)
        model = Model(rng)
        # random pure state on (a?,y,x,w,b): a recorded (pure content), d separate
        ra = rng.normal(size=2) + 1j * rng.normal(size=2); ra /= np.linalg.norm(ra)
        chi = rng.normal(size=(2,) * 4) + 1j * rng.normal(size=(2,) * 4)  # y,x,w,b
        chi /= np.linalg.norm(chi)
        d_state = np.array([1, 0], dtype=complex)
        psi0 = np.einsum('i,jklm,n->ijklmn', ra, chi, d_state)
        recs0 = {0: ra}
        Gb = rand_psd(1, rng)
        res = {}
        for rule in ('cut', 'uncut'):
            laws = {cond: local_law(model, psi0, recs0, cond, rule, nticks, Gb) for cond in ('absent', 'Z', 'X')}
            tot = {c: sum(l.values()) for c, l in laws.items()}
            t1, t2, t3 = tv(laws['absent'], laws['Z']), tv(laws['absent'], laws['X']), tv(laws['Z'], laws['X'])
            res[rule] = (t1, t2, t3, len(laws['absent']), tot)
            worst[rule] = max(worst[rule], t1, t2, t3)
            if rule == 'uncut':
                smallest_uncut = min(smallest_uncut, max(t1, t2, t3))
        c, u = res['cut'], res['uncut']
        print(f'seed {seed}: histories {c[3]:4d}  total prob {min(c[4].values()):.15f}  '
              f'CUT TV(abs,Z)={c[0]:.1e} TV(abs,X)={c[1]:.1e} TV(Z,X)={c[2]:.1e} | '
              f'UNCUT TV={u[0]:.2e} {u[1]:.2e} {u[2]:.2e}')
    print(f'worst CUT TV over seeds and pairs: {worst["cut"]:.2e}')
    print(f'UNCUT max TV over pairs: worst {worst["uncut"]:.3e}, smallest-per-seed {smallest_uncut:.3e}')
