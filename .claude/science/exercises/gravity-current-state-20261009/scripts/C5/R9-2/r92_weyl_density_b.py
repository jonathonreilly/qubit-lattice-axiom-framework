"""C5 R9-2 (b), d = 1: the interaction's energy density T00_W, built on the lattice ring, and its moments.
T00_W(Q) (total-momentum transfer +Q, Q = 2 pi j / L) has the chart kernel
    <P+Q, q'| T00_W(Q) |P, q> = chi(Q) * c(Pbar) w(Pbar; q', q) sqrt(J' J) (2 pi/L),   Pbar = P + Q/2 (Weyl midpoint),
chi = 1 on |Q| <= 1, 0 on |Q| >= 2 (C^inf).  Real-space density T00_W(x) = (1/L) sum_Q e^{iQx} T00_W(Q)
(translation covariant by construction: T00_W(Q) changes lattice momentum by exactly Q).
Checks on smooth antisymmetric packets phi, psi (any total momenta):
  (0) zeroth moment:  T00_W(0) = W                                     (exact by construction; printed)
  (1) first moment:   d/dQ <phi|T00_W(Q)|psi> at Q = 0  ==  i <phi| (1/2){X_P, W} |psi>  =  i <phi|(K - K0) psi>
      (Richardson difference over j = +-1, +-2; K, K0 are R8-1's lattice operators)
  (2) hermiticity:    <phi|T00_W(Q) psi> = conj(<psi|T00_W(-Q) phi>)
  (3) tail of chi-hat (the density's profile around the pair's centre): |chi-hat(r)| for r up to 400.
"""
import numpy as np, sys, time
L = int(sys.argv[1]) if len(sys.argv) > 1 else 512
sys.argv = [sys.argv[0], str(L)]
exec(open('r92_fall_d1.py').read().split("T0 = time.time()")[0])
out2 = []
def pr2(*a):
    line = ' '.join(str(x) for x in a); print(line, flush=True); out2.append(line)
chi = lambda Q: sstep((2.0 - np.abs(Q))/(2.0 - 1.0))
MU_B = 0.85
lam, Kr, blocks = build(MU_B)
H, H0, Pp, K, K0 = ops(blocks)
# chart-region pair lists per lattice total momentum index
sel_by_nP = {}
for nP in range(L):
    P = wrap(2*np.pi*nP/L)
    if abs(P) >= PI2 + 1.1: continue
    k1 = k; n2 = (nP - n) % L; k2 = k[n2]
    ok = (np.abs(k1) < 2.0) & (np.abs(k2) < 2.0) & (np.abs(k1 + k2 - P) < 1e-9)
    q, J = chart(k1, k2); sel = ok & (np.abs(q) < KAP)
    if sel.any(): sel_by_nP[nP] = (n[sel], n2[sel], q[sel], J[sel], P)
def TW_apply(ph, j):
    """momentum-space action of T00_W(Q = 2 pi j/L) on F(psi) (ordered pairs)."""
    o = np.zeros_like(ph); Q = 2*np.pi*j/L
    for nP, (i1, i2, qs, Js, P) in sel_by_nP.items():
        nPp = (nP + j) % L
        if nPp not in sel_by_nP: continue
        o1, o2, qo, Jo, Pp_ = sel_by_nP[nPp]
        Pbar = P + Q/2
        if abs(Pbar) >= PI2: continue
        w = Kr.g1(qo)[:, None]*Kr.g1(qs)[None, :]*Kr.Omega(Pbar*Pbar, qo, qs)
        Tb = chi(Q)*(2*np.pi/L)*cP(Pbar)*w*np.sqrt(Jo[:, None]*Js[None, :])
        o[o1, o2] += Tb @ ph[i1, i2]
    return o
def me(a, b, j):   # <a| T00_W(Q_j) b>
    return np.vdot(a, IF(TW_apply(F(b), j)))
Wop = lambda p: H(p) - H0(p)
pr2('L = %d, M_b = %.2f; T00_W = chi(Q) x Weyl-midpoint kernel of W' % (L, MU_B))
def shift(p, x0):   # translate both particles by x0 sites (lattice translation)
    return np.roll(np.roll(p, x0, 0), x0, 1)
tests = [('bound P0=0 @x=7 / bound P0=0.03 @x=4', shift(packet(Kr, MU_B, 0.0, 0.06), 7), shift(packet(Kr, MU_B, 0.03, 0.06), 4)),
         ('bound P0=0.2 @x=-6 / mix P0=0.2 @x=-3', shift(packet(Kr, MU_B, 0.2, 0.05), -6), shift(packet(Kr, MU_B, 0.2, 0.05) + 0.7*packet(Kr, MU_B, 0.2, 0.05, 'scatt'), -3)),
         ('shell P0=0.85 @x=5 / mix P0=0.85 @x=9', shift(packet(Kr, MU_B, 0.85, 0.05), 5), shift(packet(Kr, MU_B, 0.85, 0.05) + 0.7*packet(Kr, MU_B, 0.85, 0.05, 'scatt'), 9))]
h = 2*np.pi/L
for lab, a, b in tests[:int(__import__("os").environ.get("NTEST","3"))]:
    Fb = F(b); mj = {j: np.vdot(a, IF(TW_apply(Fb, j))) for j in [-2, -1, 0, 1, 2]}
    m0 = mj[0]; w0 = np.vdot(a, Wop(b))
    d1 = (mj[1] - mj[-1])/(2*h); d2 = (mj[2] - mj[-2])/(4*h)
    dQ = (4*d1 - d2)/3
    target = 1j*np.vdot(a, K(b) - K0(b))
    herm = abs(mj[1] - np.conj(me(b, a, -1)))
    pr2('  %-30s zeroth: |<a|T(0)b> - <a|W b>| = %.1e (|<a|W b>| = %.3e) ; first: d/dQ<a|T(Q)b> = %+.6e%+.6ej , i<a|(K-K0)b> = %+.6e%+.6ej , rel.diff %.1e ; herm %.1e'
        % (lab, abs(m0 - w0), abs(w0), dQ.real, dQ.imag, target.real, target.imag, abs(dQ - target)/abs(target), herm))
# (3) chi-hat tail
NQ = 1 << 16; Qg = np.linspace(-np.pi, np.pi, NQ, endpoint=False)
ch = np.fft.fftshift(np.abs(np.fft.ifft(np.fft.ifftshift(chi(Qg)))))*NQ/(2*np.pi)*(2*np.pi/NQ)
r0 = NQ//2
pr2('  chi-hat(r) (density profile about the pair centre): ' + ', '.join('r=%d: %.1e' % (r, ch[r0 + r]) for r in [0, 5, 10, 20, 50, 100, 200, 400]))
with open('r92_weyl_density_L%d.out' % L, 'w') as fh: fh.write('\n'.join(out2) + '\n')
