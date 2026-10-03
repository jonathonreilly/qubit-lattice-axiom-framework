"""A19: mover VELOCITY after mediated registration (dynamic two-excitation toy), by channel.
Velocity of band b at K: +v(K) for '+', -v(K) for '-'.  Branch registered: probe moving right (reflected).
Compares with the free mover and with a direct sharp site cut (Konno: mean (1-sin m) v0-weighted, broad)."""
import sys, numpy as np
from core1d import step, packet, vgroup, plus_band, PI

S = 1024; Mc = S // 2
def joint(mA, KA, mp, q, phi=0.6, T=400, wA=10.0, wp=30.0, cA=150, cp=300):
    aA, bA = packet(Mc, mA, KA, wA, cA); aB, bB = packet(Mc, mp, q, wp, cp)
    psiA = np.empty(S, complex); psiA[0::2] = aA; psiA[1::2] = bA
    psiB = np.empty(S, complex); psiB[0::2] = aB; psiB[1::2] = bB
    psi = np.outer(psiA, psiB); dg = np.arange(S); eph = np.exp(1j * phi)
    for t in range(T):
        pt = psi.T.copy(); a, b = step(pt[:, 0::2], pt[:, 1::2], mA); pt[:, 0::2] = a; pt[:, 1::2] = b; psi = pt.T.copy()
        a, b = step(psi[:, 0::2], psi[:, 1::2], mp); out = np.empty_like(psi); out[:, 0::2] = a; out[:, 1::2] = b; psi = out
        psi[dg, dg] *= eph
    return psi
for (mA, KA, mp, q) in ((1.2, 0.8, 0.1, -0.05), (0.6, 0.8, 0.1, -0.05), (0.3, 0.8, 0.1, -0.05)):
    psi = joint(mA, KA, mp, q)
    K = 2 * PI * np.arange(Mc) / Mc
    F = {(ca, cb): np.fft.fft2(psi[ca::2, cb::2]) / Mc for ca in (0, 1) for cb in (0, 1)}
    uAp = np.array(plus_band(K, mA)); uBp = np.array(plus_band(K, mp))
    uAm = np.array([-np.conj(uAp[1]), np.conj(uAp[0])]); uBm = np.array([-np.conj(uBp[1]), np.conj(uBp[0])])
    vA, vB = vgroup(K, mA), vgroup(K, mp)
    P = {}
    for sa, uA in (("+", uAp), ("-", uAm)):
        for sb, uB in (("+", uBp), ("-", uBm)):
            amp = sum(np.conj(uA[ca])[:, None] * np.conj(uB[cb])[None, :] * F[(ca, cb)] for ca in (0, 1) for cb in (0, 1))
            P[(sa, sb)] = np.abs(amp) ** 2
    def vel(s, v): return v if s == "+" else -v
    v0 = vgroup(KA, mA)
    for label, cond in (("probe reflected (right-moving)", lambda sb: vel(sb, vB) > 0), ("probe transmitted", lambda sb: vel(sb, vB) < 0)):
        w = 0.0; m1 = 0.0; m2 = 0.0; wum = 0.0
        for (sa, sb), p in P.items():
            sel = cond(sb)[None, :]
            pa = (p * sel).sum(1)                 # mover K distribution in this channel
            va = vel(sa, vA)
            w += pa.sum(); m1 += np.dot(pa, va); m2 += np.dot(pa, va ** 2)
            if sa == "-":
                wum += pa.sum()
        mean = m1 / w; sd = np.sqrt(max(m2 / w - mean ** 2, 0))
        print(f"m_A={mA} K_A={KA} (v0={v0:+.3f}), probe m={mp} q={q}: {label}: weight {w:.4f}; mover velocity mean {mean:+.4f}, "
              f"sd {sd:.4f}; share of time-umklapp (mover band flipped) {wum / w:.3f}")
    # direct sharp site cut of the free mover: velocity law from a single-site start, chirality-weighted
    pR = (1 + v0) / 2
    print(f"   direct sharp site cut instead: mean velocity (1-sin m) v0 = {(1 - np.sin(mA)) * v0:+.4f}, "
          f"sd ~ sqrt((1-sin m) - mean^2) = {np.sqrt((1 - np.sin(mA)) - ((1 - np.sin(mA)) * v0) ** 2):.4f}")
    sys.stdout.flush()
