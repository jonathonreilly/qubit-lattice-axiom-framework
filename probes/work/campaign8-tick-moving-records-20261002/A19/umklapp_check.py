"""A19: time-umklapp in mover-probe contact scattering on the ticked lattice (supplied toy).
Two-body Floquet operator per tick: contact phase e^{i phi} on x_A = x_B after both Dirac-round steps.
Band '+' eigenvalue -e^{-iW}, band '-' eigenvalue -e^{+iW} (cos W = cos m cos K).  A joint flip (+,+) -> (-,-)
conserves the two-body quasi-energy only if W_A' + W_B' = 2 pi - (W_A + W_B)  (mod 2 pi): a time-umklapp channel.
Reports the weight-averaged quasi-energy bookkeeping and momenta per channel, for several mover/probe masses."""
import sys, numpy as np
from core1d import step, packet, vgroup, plus_band, PI

def run(mA, KA, mp, q, phi=0.6, S=1024, T=400, wA=10.0, wp=30.0, cA=150, cp=300):
    Mc = S // 2
    aA, bA = packet(Mc, mA, KA, wA, cA); aB, bB = packet(Mc, mp, q, wp, cp)
    psiA = np.empty(S, complex); psiA[0::2] = aA; psiA[1::2] = bA
    psiB = np.empty(S, complex); psiB[0::2] = aB; psiB[1::2] = bB
    psi = np.outer(psiA, psiB); dg = np.arange(S); eph = np.exp(1j * phi)
    for t in range(T):
        pt = psi.T.copy(); a, b = step(pt[:, 0::2], pt[:, 1::2], mA); pt[:, 0::2] = a; pt[:, 1::2] = b; psi = pt.T.copy()
        a, b = step(psi[:, 0::2], psi[:, 1::2], mp); out = np.empty_like(psi); out[:, 0::2] = a; out[:, 1::2] = b; psi = out
        psi[dg, dg] *= eph
    K = 2 * PI * np.arange(Mc) / Mc
    F = {(ca, cb): np.fft.fft2(psi[ca::2, cb::2]) / Mc for ca in (0, 1) for cb in (0, 1)}
    uAp = np.array(plus_band(K, mA)); uBp = np.array(plus_band(K, mp))
    uAm = np.array([-np.conj(uAp[1]), np.conj(uAp[0])]); uBm = np.array([-np.conj(uBp[1]), np.conj(uBp[0])])
    def P(uA, uB):
        amp = sum(np.conj(uA[ca])[:, None] * np.conj(uB[cb])[None, :] * F[(ca, cb)] for ca in (0, 1) for cb in (0, 1))
        return np.abs(amp) ** 2
    WA = np.arccos(np.cos(mA) * np.cos(K)); WB = np.arccos(np.cos(mp) * np.cos(K))
    W0 = np.arccos(np.cos(mA) * np.cos(KA)) + np.arccos(np.cos(mp) * np.cos(q))
    def wrap(x): return (x + PI) % (2 * PI) - PI
    pp, mm = P(uAp, uBp), P(uAm, uBm)
    pm, mp_ = P(uAp, uBm), P(uAm, uBp)
    Wsum = WA[:, None] + WB[None, :]
    # gentle channel: mover stays in band, momentum change small
    dKA = np.abs(wrap(K - KA))
    gentle = (pp * (dKA[:, None] < 0.3)).sum()
    out = dict(pp=pp.sum(), mm=mm.sum(), pm=pm.sum(), mpw=mp_.sum(), gentle_pp=gentle)
    out["E_pp"] = np.sum(pp * Wsum) / pp.sum()
    out["E_mm"] = np.sum(mm * Wsum) / max(mm.sum(), 1e-300)
    out["W0"] = W0
    out["KA_mm"] = np.angle(np.sum(mm.sum(1) * np.exp(1j * K))) if mm.sum() > 0 else np.nan
    out["KB_mm"] = np.angle(np.sum(mm.sum(0) * np.exp(1j * K))) if mm.sum() > 0 else np.nan
    # probe reversed (right-moving) and mover momentum change, in the band-preserving channel
    vB = vgroup(K, mp)
    rev_pp = (pp * (vB[None, :] > 0)).sum()
    out["rev_pp"] = rev_pp
    if rev_pp > 0:
        pk = (pp * (vB[None, :] > 0)).sum(1); pk /= pk.sum()
        out["dKA_rev_pp"] = np.dot(pk, wrap(K - KA))
    return out

if __name__ == "__main__":
    cases = [tuple(float(v) for v in c.split(":")) for c in sys.argv[1].split(",")] if len(sys.argv) > 1 else [(1.2, 0.8, 0.1, -0.05)]
    for (mA, KA, mp, q) in cases:
        o = run(mA, KA, mp, q)
        print(f"mover m={mA} K={KA}, probe m={mp} q={q}: channels (+,+) {o['pp']:.4f}  (-,-) {o['mm']:.4f}  (+,-) {o['pm']:.1e}  (-,+) {o['mpw']:.1e}")
        print(f"   quasi-energy W_A+W_B: in {o['W0']:.4f};  out (+,+) {o['E_pp']:.4f};  out (-,-) {o['E_mm']:.4f}  "
              f"[time-umklapp prediction 2pi - in = {2*PI - o['W0']:.4f}]")
        print(f"   (-,-) channel mean momenta K_A' {o['KA_mm']:+.3f}, K_B' {o['KB_mm']:+.3f}  (in: {KA:+.3f}, {q:+.3f});  "
              f"band-preserving probe reversal weight {o['rev_pp']:.4f}, mover momentum change there {o.get('dKA_rev_pp', float('nan')):+.4f} (2q = {2*q:+.3f})")
        sys.stdout.flush()
