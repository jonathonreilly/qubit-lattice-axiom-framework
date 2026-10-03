#!/usr/bin/env python3
"""A22 task 2 (supplied toy): doubled-channel weight D in two-excitation collisions, narrow packets.
Relative coordinate at total momentum P = 2Kc; incoming A at Kc+k0, B at Kc-k0 (band 'bin_'), Gaussian in k with
relative width sk; A starts left of B.  After the collision the relative wavefunction is split by sign(r):
right = A passed B ('transmitted'), left = 'reflected'.  Weights are projected on band pairs and momentum regions:
ordinary = both momenta within pi/2 of the incoming cone Kc, doubled = both near Kc+pi (the joint-staggering image).
For identical excitations (geom 'chain') only the totals O, D are meaningful.

usage: two_body.py CASE[,CASE...] k0[,k0...] [key=val ...]
"""
import sys, time, numpy as np
from tb import Rel, bands, PI

phi = 0.8
CASES = dict(
    contact=dict(geom="ladder", V=[(0, "all", phi)]),
    nn=dict(geom="ladder", V=[(1, "all", phi), (-1, "all", phi)]),
    nnodd=dict(geom="ladder", V=[(1, "odd", phi), (-1, "odd", phi)]),
    nneven=dict(geom="ladder", V=[(1, "even", phi), (-1, "even", phi)]),
    cbal=dict(geom="ladder", V=[(0, "all", phi), (2, "all", phi / 2), (-2, "all", phi / 2)]),
    cunb=dict(geom="ladder", V=[(0, "all", phi), (2, "all", phi), (-2, "all", phi)]),
    r2=dict(geom="ladder", V=[(2, "all", phi), (-2, "all", phi)]),
    S1=dict(geom="chain"),
    phio=dict(geom="chain", phi_o=phi),
    phie=dict(geom="chain", phi_e=phi),
    phieo=dict(geom="chain", phi_e=phi, phi_o=phi),
    S1nnn=dict(geom="chain", V=[(2, "all", phi), (-2, "all", phi)]),
)


def run(geom, k0, m=0.3, V=None, phi_e=0.0, phi_o=0.0, te=None, to=None, Kc=0.0, bin_=0, sk=0.15, M=None,
        label="", verbose=True):
    te = PI / 2 if te is None else te
    to = PI / 2 - m if to is None else to
    P = 2 * Kc
    w = 1.0 / (2 * sk * k0)                     # position width (cells) of the relative packet
    r0 = -(4 * w + 12)
    rcut = 3 * w + 8
    EA0, vA0, _ = bands(np.array([Kc + k0]), te, to)[bin_]
    EB0, vB0, _ = bands(np.array([P - Kc - k0]), te, to)[bin_]
    vrel = abs(vA0[0] - vB0[0])
    # spreading: relative-velocity spread dv = |d vrel/dk| * sk*k0 ; require transmitted part beyond rcut + 3 w + 3 dv T
    EAp, vAp, _ = bands(np.array([Kc + k0 * 1.01]), te, to)[bin_]
    EBp, vBp, _ = bands(np.array([P - Kc - k0 * 1.01]), te, to)[bin_]
    dv = abs(abs(vAp[0] - vBp[0]) - vrel) / (0.01 * k0) * sk * k0
    T = int((abs(r0) + rcut + 3 * w + 40) / max(vrel - 3 * dv, 0.3 * vrel)) + 50
    if M is None:
        need = 2 * (abs(r0) + vrel * T + 6 * w + 200)
        M = int(2 ** np.ceil(np.log2(need)))
    R = Rel(M, te, to, P, geom=geom, phi_e=phi_e, phi_o=phi_o, V=V)
    q = 2 * PI * np.fft.fftfreq(M)
    k = (q - Kc + PI) % (2 * PI) - PI
    g = np.exp(-(k - k0) ** 2 / (4 * (sk * k0) ** 2))
    g[k <= 0] = 0.0
    EA, vA, uA = bands(q, te, to)[bin_]
    EB, vB, uB = bands(P - q, te, to)[bin_]
    chi = np.fft.ifft((g * np.exp(-1j * q * r0))[:, None, None] * uA[:, :, None] * uB[:, None, :], axis=0) * np.sqrt(M)
    if geom == "chain":
        rr = R.r
        ex = np.exp(1j * P * rr)[:, None, None] * np.transpose(chi[(-rr) % M], (0, 2, 1))
        chi = (chi + ex) / np.sqrt(2); chi[0, 0, 0] = 0; chi[0, 1, 1] = 0
    chi /= np.sqrt(np.sum(np.abs(chi) ** 2))
    for t in range(T):
        chi = R.tick(chi)
    norm = np.sum(np.abs(chi) ** 2)
    left = chi.copy(); left[R.r > -rcut] = 0
    right = chi.copy(); right[R.r < rcut] = 0
    mid = norm - np.sum(np.abs(left) ** 2) - np.sum(np.abs(right) ** 2)
    _, WL = R.project(left); _, WR = R.project(right)
    regA = np.abs(((q - Kc) + PI) % (2 * PI) - PI) < PI / 2           # A near the incoming cone
    regB = np.abs(((P - q - Kc) + PI) % (2 * PI) - PI) < PI / 2       # B near the incoming cone
    res = {}
    for nm, W in (("T", WR), ("R", WL)):
        Wall = W.sum(axis=(0, 1))
        res[nm + "o"] = Wall[regA & regB].sum()
        res[nm + "d"] = Wall[~regA & ~regB].sum()
        res[nm + "x"] = Wall[regA ^ regB].sum()                       # one partner shifted only
        res[nm + "band_dd"] = W[1 - bin_, 1 - bin_][~regA & ~regB].sum()  # doubled in the Lambda-image bands
    D = res["Td"] + res["Rd"]
    out = dict(k0=k0, vrel=vrel, T=T, M=M, D=D, To=res["To"], Td=res["Td"], Ro=res["Ro"], Rd=res["Rd"],
               X=res["Tx"] + res["Rx"], mid=mid, norm=norm, img=(res["Tband_dd"] + res["Rband_dd"]) / max(D, 1e-300))
    if verbose:
        refl = out["Ro"] + out["Rd"]
        share = out["Rd"] / refl if refl > 0 else float("nan")
        print(f"  [{label}] m={m:.3f} k0={k0:.3f} vrel={vrel:.4f} T={T} M={M}: D={D:.4e} (fwd {out['Td']:.3e}, refl {out['Rd']:.3e}); "
              f"ord fwd {out['To']:.4f} refl {out['Ro']:.4e}; dbl share of refl {share:.4f}; one-shifted {out['X']:.1e}; "
              f"unfinished {mid:.1e}; doubled in image bands {out['img']:.4f}")
        sys.stdout.flush()
    return out


if __name__ == "__main__":
    names = sys.argv[1].split(",")
    k0s = [float(x) for x in sys.argv[2].split(",")]
    extra = {}
    for a in sys.argv[3:]:
        key, val = a.split("=")
        extra[key] = eval(val)
    t00 = time.time()
    for nm in names:
        for k0 in k0s:
            kw = dict(CASES[nm]); kw.update(extra)
            run(k0=k0, label=nm, **kw)
    print(f"  total {time.time()-t00:.1f} s")
