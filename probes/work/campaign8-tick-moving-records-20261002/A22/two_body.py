#!/usr/bin/env python3
"""A22 task 2 (supplied toy): energy-resolved doubled-channel weight D(k) in two-excitation collisions.
Relative coordinate at total momentum P = 2Kc; incoming A at Kc+k, B at Kc-k (band 'bin'), A starts left of B.
D(k) = weight of outgoing content whose momenta are both shifted by pi (the joint-staggering image), per incoming k,
normalised by the total outgoing weight at that k.  Exact maps (Lambda-exact rounds): transmitted q -> q, q+pi;
reflected (distinguishable) / other half (identical) q -> P-q, P-q+pi.

usage: two_body.py CASE   (cases defined below)
"""
import sys, time, numpy as np
from tb import Rel, bands, PI

CASES = {}
def case(name, **kw): CASES[name] = kw

phi = 0.8
for m in (0.15, 0.3, 0.6, 1.0):
    tag = f"m{m}"
    # ladder (distinguishable), A19 round, diagonal interactions between the chains
    case(f"ladder_contact_{tag}", geom="ladder", m=m, V=[(0, "all", phi)])
    case(f"ladder_nn_{tag}", geom="ladder", m=m, V=[(1, "all", phi), (-1, "all", phi)])
    case(f"ladder_nnodd_{tag}", geom="ladder", m=m, V=[(1, "odd", phi), (-1, "odd", phi)])
    case(f"ladder_nneven_{tag}", geom="ladder", m=m, V=[(1, "even", phi), (-1, "even", phi)])
    case(f"ladder_cbal_{tag}", geom="ladder", m=m, V=[(0, "all", phi), (2, "all", phi / 2), (-2, "all", phi / 2)])
    case(f"ladder_cunb_{tag}", geom="ladder", m=m, V=[(0, "all", phi), (2, "all", phi), (-2, "all", phi)])
    case(f"ladder_r2_{tag}", geom="ladder", m=m, V=[(2, "all", phi), (-2, "all", phi)])
    # chain (identical hard-core excitations): S1 gates (covariant), plus |11> phases on one or both bond types
    case(f"chain_S1_{tag}", geom="chain", m=m)
    case(f"chain_phio_{tag}", geom="chain", m=m, phi_o=phi)
    case(f"chain_phie_{tag}", geom="chain", m=m, phi_e=phi)
    case(f"chain_phieo_{tag}", geom="chain", m=m, phi_e=phi, phi_o=phi)


def run(geom, m, V=None, phi_e=0.0, phi_o=0.0, ks=(0.02, 0.04, 0.08, 0.16, 0.32, 0.64), M=16384, r0=-300, rcut=120,
        Kc=0.0, bin_=0, a_edge=0.03, k_s=0.5, Tmax=12000, label=""):
    te, to = PI / 2, PI / 2 - m
    P = 2 * Kc
    R = Rel(M, te, to, P, geom=geom, phi_e=phi_e, phi_o=phi_o, V=V)
    q = 2 * PI * np.fft.fftfreq(M)
    k = (q - Kc + PI) % (2 * PI) - PI
    g = np.where(k > 0, np.exp(-a_edge / np.maximum(k, 1e-12) - (k / k_s) ** 2), 0.0)
    EA, vA, uA = bands(q, te, to)[bin_]
    EB, vB, uB = bands(P - q, te, to)[bin_]
    chi = np.fft.ifft((g * np.exp(-1j * q * r0))[:, None, None] * uA[:, :, None] * uB[:, None, :], axis=0) * np.sqrt(M)
    if geom == "chain":
        rr = R.r
        ex = np.exp(1j * P * rr)[:, None, None] * np.transpose(chi[(-rr) % M], (0, 2, 1))
        chi = (chi + ex) / np.sqrt(2); chi[0, 0, 0] = 0; chi[0, 1, 1] = 0
    nrm0 = np.sum(np.abs(chi) ** 2); chi /= np.sqrt(nrm0)
    # time needed: slowest requested k must clear 2|r0| + 2 rcut
    vrel = np.abs(vA - vB)
    kmin = min(ks)
    i_kmin = np.argmin(np.abs(k - kmin))
    T = int(min(Tmax, (2 * abs(r0) + 2 * rcut + 200) / max(vrel[i_kmin], 1e-9)))
    for t in range(T):
        chi = R.tick(chi)
    norm = np.sum(np.abs(chi) ** 2)
    left = chi.copy(); left[R.r > -rcut] = 0
    right = chi.copy(); right[R.r < rcut] = 0
    mid = 1 - np.sum(np.abs(left) ** 2) - np.sum(np.abs(right) ** 2)
    qq, WL = R.project(left); _, WR = R.project(right)
    bdl = 1 - bin_
    idx = lambda kk: np.argmin(np.abs(((q - (Kc + kk)) + PI) % (2 * PI) - PI))
    half = M // 2
    print(f"[{label}] geom={geom} m={m} V={V} phi_e={phi_e} phi_o={phi_o}  M={M} T={T} norm={norm:.12f} unfinished(|r|<rcut)={mid:.2e}")
    tot = dict(To=0, Td=0, Ro=0, Rd=0, other=0)
    # totals over all k (band-resolved)
    for part, W, nm in ((right, WR, "T"), (left, WL, "R")):
        ordinary = W[bin_, bin_]; doubled = W[bdl, bdl]; mixed = W[bin_, bdl] + W[bdl, bin_]
        reg_ord = np.abs(((q - Kc) + PI) % (2 * PI) - PI) < PI / 2
        tot[nm + "o"] += ordinary[reg_ord].sum() + doubled[reg_ord].sum() * 0
        tot[nm + "d"] += doubled[~reg_ord].sum()
        tot["other"] += mixed.sum() + ordinary[~reg_ord].sum() + doubled[reg_ord].sum()
    print(f"   totals: transmitted ord {tot['To']:.4e} dbl {tot['Td']:.4e} | reflected ord {tot['Ro']:.4e} dbl {tot['Rd']:.4e} | "
          f"other band pairs/regions {tot['other']:.1e}")
    print(f"   {'k':>6s} {'v_rel':>7s} {'D(k)':>11s} {'R(k)':>10s} {'Dshare_of_refl':>14s} {'unitarity':>10s}")
    for kk in ks:
        i = idx(kk)
        ip = (i + half) % M                         # q + pi
        j = (-i + (2 * idx(0) if Kc != 0 else 0)) % M   # P - q  (P = 2Kc)
        jp = (j + half) % M
        To, Td = WR[bin_, bin_, i], WR[bdl, bdl, ip]
        Ro, Rd = WL[bin_, bin_, j], WL[bdl, bdl, jp]
        s = To + Td + Ro + Rd
        g2 = g[i] ** 2 / nrm0
        if geom == "chain":
            # identical: each half carries the full outgoing state at that k; use the left half only
            s = Ro + Rd
            D = Rd / s; Rk = float('nan'); share = float('nan'); g2 = g2 / 2
        else:
            D = (Td + Rd) / s; Rk = (Ro + Rd) / s; share = Rd / max(Ro + Rd, 1e-300)
        print(f"   {kk:6.3f} {vrel[i]:7.4f} {D:11.4e} {Rk:10.4e} {share:14.4f} {s/g2:10.6f}")
    sys.stdout.flush()


if __name__ == "__main__":
    names = sys.argv[1].split(",")
    kw_extra = {}
    for a in sys.argv[2:]:
        key, val = a.split("=")
        kw_extra[key] = eval(val)
    for nm in names:
        t0 = time.time()
        kw = dict(CASES[nm]); kw.update(kw_extra)
        run(label=nm, **kw)
        print(f"   ({time.time()-t0:.1f} s)")
