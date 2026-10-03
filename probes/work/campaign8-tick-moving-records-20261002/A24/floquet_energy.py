#!/usr/bin/env python3
"""A24 S3 (supplied toy): energy budget of A19's mediated registration on the TICKED 1D Dirac round (A19 R2/R3).

Energy of one excitation over the aligned emptiness: the conserved band energy E = W(K), cos W = cos m cos K, on BOTH
velocity branches (they are parity partners).  In the cell basis E = W(K) x 1, so every single-site state has
<y|E|y> = mean_K W = pi/2 (band centre; band [m, pi - m]).  Hence a sharp one-site probe record injects exactly
   dE_lock = pi/2 - <W_B>   (probe's depth below its band centre); the mover's mean energy is untouched (P_y acts on B).
The unitary contact collision conserves quasi-energy only mod 2 pi: in the time-umklapp channel (-,-),
W_A + W_B -> 2 pi - (W_A + W_B) (A19 R3), a band-scale jump of the lifted energy that is NOT caused by any lock.
usage: floquet_energy.py mA:KA:mp:q[,...]
"""
import sys
import numpy as np
sys.path.insert(0, "/private/tmp/claude-501/-Users-jonreilly-Projects-Physics--claude-worktrees-focused-noyce-9a3983/"
                   "34c0b720-f781-4af0-9bb7-5d2e1b60d22e/scratchpad/c8/A19")
from core1d import step, packet, vgroup, plus_band, PI

S = 1024; Mc = S // 2
K = 2 * PI * np.arange(Mc) / Mc


def joint(mA, KA, mp, q, T, phi=0.6, wA=10.0, wp=30.0, cA=150, cp=300):
    aA, bA = packet(Mc, mA, KA, wA, cA); aB, bB = packet(Mc, mp, q, wp, cp)
    psiA = np.empty(S, complex); psiA[0::2] = aA; psiA[1::2] = bA
    psiB = np.empty(S, complex); psiB[0::2] = aB; psiB[1::2] = bB
    psi = np.outer(psiA, psiB); dg = np.arange(S); eph = np.exp(1j * phi)
    for t in range(T):
        pt = psi.T.copy(); a, b = step(pt[:, 0::2], pt[:, 1::2], mA); pt[:, 0::2] = a; pt[:, 1::2] = b; psi = pt.T.copy()
        a, b = step(psi[:, 0::2], psi[:, 1::2], mp); out = np.empty_like(psi); out[:, 0::2] = a; out[:, 1::2] = b; psi = out
        psi[dg, dg] *= eph
    return psi


def channels(psi, mA, mp):
    F = {(ca, cb): np.fft.fft2(psi[ca::2, cb::2]) / Mc for ca in (0, 1) for cb in (0, 1)}
    uAp = np.array(plus_band(K, mA)); uBp = np.array(plus_band(K, mp))
    uAm = np.array([-np.conj(uAp[1]), np.conj(uAp[0])]); uBm = np.array([-np.conj(uBp[1]), np.conj(uBp[0])])
    P = {}
    for sa, uA in (("+", uAp), ("-", uAm)):
        for sb, uB in (("+", uBp), ("-", uBm)):
            amp = sum(np.conj(uA[ca])[:, None] * np.conj(uB[cb])[None, :] * F[(ca, cb)] for ca in (0, 1) for cb in (0, 1))
            P[(sa, sb)] = np.abs(amp) ** 2
    return P


# check: every single-site state sits at the band centre pi/2 (exact by W(K + pi) = pi - W(K))
for m in (0.1, 0.6, 1.2):
    W = np.arccos(np.cos(m) * np.cos(K))
    print(f"m={m}: mean_K W = {W.mean():.15f} (pi/2 = {PI/2:.15f}); band [{W.min():.4f}, {W.max():.4f}]")

cases = [tuple(float(v) for v in c.split(":")) for c in sys.argv[1].split(",")] if len(sys.argv) > 1 else [(1.2, 0.8, 0.1, -0.05)]
for (mA, KA, mp, q) in cases:
    vA, vB = vgroup(KA, mA), abs(vgroup(q, mp))
    T = int(min(400, 150 / (vA + vB) + 100 / vB))
    WA = np.arccos(np.cos(mA) * np.cos(K)); WB = np.arccos(np.cos(mp) * np.cos(K))
    vAk, vBk = vgroup(K, mA), vgroup(K, mp)
    out = {}
    for tag, TT in (("start", 0), ("after", T)):
        psi = joint(mA, KA, mp, q, TT)
        P = channels(psi, mA, mp)
        tot = sum(p.sum() for p in P.values())
        EA = sum(np.sum(p * WA[:, None]) for p in P.values()) / tot
        EB = sum(np.sum(p * WB[None, :]) for p in P.values()) / tot
        refl = {}
        wR = 0.0; eAR = 0.0; eBR = 0.0
        for (sa, sb), p in P.items():
            sel = ((vBk if sb == "+" else -vBk) > 0)[None, :]
            wR += (p * sel).sum(); eAR += (p * sel * WA[:, None]).sum(); eBR += (p * sel * WB[None, :]).sum()
            w_ = (p * sel).sum()
            if w_ > 0:
                refl[(sa, sb)] = (w_ / tot, (p * sel * WA[:, None]).sum() / w_, (p * sel * WB[None, :]).sum() / w_)
        out[tag] = dict(tot=tot, EA=EA, EB=EB, wR=wR, EAR=eAR / max(wR, 1e-300), EBR=eBR / max(wR, 1e-300),
                        mm=P[("-", "-")].sum() / tot,
                        Emm=np.sum(P[("-", "-")] * (WA[:, None] + WB[None, :])) / max(P[("-", "-")].sum(), 1e-300),
                        Epp=np.sum(P[("+", "+")] * (WA[:, None] + WB[None, :])) / P[("+", "+")].sum(), refl=refl)
    s, a = out["start"], out["after"]
    Win = s["EA"] + s["EB"]
    print(f"\nmover m={mA} K={KA} (v={vA:+.3f}), probe m={mp} q={q} (|v|={vB:.3f}), T={T}: norm {a['tot']:.10f}")
    print(f"   lifted energy W_A+W_B: start {Win:.4f} (W_A {s['EA']:.4f}, W_B {s['EB']:.4f}); after collision {a['EA']+a['EB']:.4f} "
          f"(W_A {a['EA']:.4f}, W_B {a['EB']:.4f})")
    print(f"   channel (+,+): mean W_A+W_B {a['Epp']:.4f};  time-umklapp (-,-): weight {a['mm']:.4f}, mean W_A+W_B {a['Emm']:.4f} "
          f"(2 pi - start = {2*PI - Win:.4f}); umklapp share of the collision's lifted-energy change "
          f"{a['mm']*(a['Emm']-Win):+.4f} of {a['EA']+a['EB']-Win:+.4f}")
    print(f"   SHARP PROBE LOCK, all outcomes: dE = pi/2 - <W_B> = {PI/2 - a['EB']:+.4f} (probe half-band {(PI-2*mp)/2:.4f}); "
          f"mover share exactly 0")
    print(f"   per reflected-probe record (weight {a['wR']:.4f}): lock dE = {PI/2 - a['EBR']:+.4f}; mover's lifted energy change "
          f"from the collision {a['EAR'] - s['EA']:+.4f}")
    for ch, (w_, ea_, eb_) in sorted(a["refl"].items()):
        if w_ > 1e-4:
            print(f"      reflected-probe records in channel {ch}: weight {w_:.4f}; lock dE = pi/2 - W_B = {PI/2 - eb_:+.4f}; "
                  f"mover lifted-energy change {ea_ - s['EA']:+.4f}; pair change from the collision {ea_ + eb_ - Win:+.4f}")
    print(f"   direct sharp lock on the mover instead: pi/2 - W_A = {PI/2 - s['EA']:+.4f}")
    sys.stdout.flush()
