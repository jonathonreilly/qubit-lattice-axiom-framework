"""TOR-1 T0: construction checks on the Lx x Lt torus (PREREG sections 2-3): momentum blocks, decomposition, toron data,
gauge invariance, reflection constant, factorisation, loop closure, timing.  usage: python3 tor1_t0.py Lx Lt [nfield]"""
import sys, time
import numpy as np
from tor1_lib import *

Lx, Lt = int(sys.argv[1]), int(sys.argv[2]); nf = int(sys.argv[3]) if len(sys.argv) > 3 else 6
NTOR = int(sys.argv[4]) if len(sys.argv) > 4 else 96; NLOOP = int(sys.argv[5]) if len(sys.argv) > 5 else 256
t0 = time.time(); S = Torus(Lx, Lt); rng = np.random.default_rng(7001)
print(f"# TOR-1 T0 Lx={Lx} Lt={Lt} N={S.N} nl={S.nl} ntor={NTOR} nloop={NLOOP}; build {time.time()-t0:.1f}s", flush=True)
print(f"momentum off-block max {S.offblock:.2e}")
# spectra check at a random toron
wx, wt = 1.3, -2.1; th = (wx * S.Ux + wt * S.Ut)[None]
ev_pos = np.sort(np.linalg.eigvalsh(S.H(th))[0]); ev_k = np.sort(np.linalg.eigvalsh(S.hk(np.array([wx]), np.array([wt]))[0]).ravel())
print(f"toron spectrum position vs momentum: max diff {np.abs(ev_pos - ev_k).max():.2e}")


def rand_field(P, s=0.12, dmax=0.55, toron=True):
    out = []
    while len(out) < P:
        th = rng.normal(0, s, S.nl)
        if toron: th = th + rng.uniform(0, 2 * np.pi) * S.Ux + rng.uniform(0, 2 * np.pi) * S.Ut
        F = th @ S.Pm.T; Fr = (F + np.pi) % (2 * np.pi) - np.pi
        if np.abs(Fr).max() < dmax and abs(np.round(Fr.sum() / (2 * np.pi))) == 0: out.append(th)
    return np.array(out)


A = rand_field(nf)
F, Q, AT, w = S.decompose(A)
Fr = (A @ S.Pm.T + np.pi) % (2 * np.pi) - np.pi
print(f"decompose: |P AT - F| {np.abs(AT @ S.Pm.T - F).max():.1e}; |div AT| {np.abs(S.div(AT)).max():.1e}; |mean AT| {np.abs(AT.mean(1)).max():.1e}")
Ac = S.canon(AT, w); Fc = (Ac @ S.Pm.T + np.pi) % (2 * np.pi) - np.pi
W1 = lambda B: np.stack([B @ S.Wx_ref, B @ S.Wt_ref], 1)
print(f"canonical rep: plaquettes {np.abs(np.angle(np.exp(1j*(Fc - Fr)))).max():.1e}; Wilson lines {np.abs(np.angle(np.exp(1j*(W1(Ac) - W1(A))))).max():.1e}")

for model in ('11112', 'L1'):
    t1 = time.time(); M = TorusMeasure(S, model, ntor=NTOR, nloop=NLOOP)
    print(f"[{model}] toron data: winding of Gam_t over wx-circle {M.wind:+.6f}; base holonomy phases h_t(0) {np.angle(np.exp(1j*M.gam[0])):+.3e}, "
          f"h_x(0) {np.angle(np.exp(1j*M.hx0)):+.3e}; Gam_t spread {np.ptp(M.gam - M.wind*M.ggrid):.4f} rad [{time.time()-t1:.1f}s]", flush=True)
    if model == 'L1':
        W = M.logrho(A)
        for nu in (0, 1):
            w2 = w.copy(); w2[:, nu] += 2 * np.pi; Wl = M.logrho(A, w_override=w2)
            dq = np.angle(np.exp(1j * (Wl.imag - W.imag)))
            print(f"   [L1] loop closure nu={'xt'[nu]}: arg Q_loop per field {np.array2string(dq, precision=4)}; expected -wind*wt (nu=x) = "
                  f"{np.array2string(np.angle(np.exp(-1j*M.wind*w[:,1])), precision=4)}", flush=True)
        continue
    t1 = time.time(); W, r = M.logrho(A, parts=True); dt = time.time() - t1
    print(f"[{model}] logrho on {nf} fields: {dt:.2f}s ({dt/nf*1e3:.0f} ms/field); gmin {r['gmin']:.3f}; idx {r['idx_ok']}; identity {r['idchk']:.1e}; "
          f"monopole {r['mono']:.1e}; div residual {r['resid']:.1e}; |kQ| {np.abs(r['kQ']).max():.1e}; toron Richardson {max(r['rich'].values()):.1e}", flush=True)
    print(f"   Re W {np.array2string(W.real, precision=6)}\n   Im W {np.array2string(W.imag, precision=6)}\n   S-phase {np.array2string(r['Sph'].imag, precision=6)}"
          f"\n   kbb phase {np.array2string((M.sk*np.sum(r['AT']*r['kbb'],1)), precision=3)}")
    # gauge invariance
    om = rng.uniform(-np.pi, np.pi, (nf, S.ns)); Wg = M.logrho(S.gauge(A, om))
    print(f"   gauge invariance: max |dW| {np.abs(np.angle(np.exp(1j*(Wg.imag - W.imag)))).max():.1e} (phase), {np.abs(Wg.real - W.real).max():.1e} (modulus)")
    # factorisation: Re W vs 2 Re logdet D(1) + 0.5 Re logdet D(2)
    l1, g1 = vec_logdet(S, A, 0.0, 1); l2, g2 = vec_logdet(S, A, 0.0, 2); mod = 2 * l1.real + 0.5 * l2.real
    d = W.real - mod; print(f"   factorisation: Re W - (2 Re ld D1 + 0.5 Re ld D2): mean {d.mean():+.10f} spread {np.ptp(d):.1e}")
    # reflection
    Wt_ = M.logrho(S.theta(A)); c = Wt_ - np.conj(W)
    cph = np.angle(np.exp(1j * (c.imag - c.imag[0])))
    print(f"   reflection: rho(theta U) = e^c conj rho(U): Re c spread {np.ptp(c.real):.1e}; Im c = {c.imag[0]:+.8f} spread {np.abs(cph).max():.1e}")
    # loop closure: continue torons by 2 pi at fixed AT
    for nu in (0, 1):
        w2 = w.copy(); w2[:, nu] += 2 * np.pi
        Wl = M.logrho(A, w_override=w2)
        dq = np.angle(np.exp(1j * (Wl.imag - W.imag)))
        print(f"   loop closure nu={'xt'[nu]}: max|arg Q_loop| {np.abs(dq).max():.2e}; max|ln|Q_loop|| {np.abs(Wl.real - W.real).max():.2e}", flush=True)
print(f"done [{time.time()-t0:.0f}s]")
