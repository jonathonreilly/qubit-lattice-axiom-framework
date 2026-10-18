"""B13 validation on the 2x2x2 torus (exact numbers from B6 ringlib exact diagonalisation).

Checks: lattice conventions equal ringlib; stoquasticity and J-sign gauge; DMC energies (vacuum and winding
sectors); DMC forward-walking magnetic-source curvatures vs exact Hessians (harmonic q=0 per orientation,
occupation-sign/staggered source, coexact q=(pi,0,0)); and the negative control that local pair-update
world-line (projector SSE) sampling does not reproduce the harmonic curvature.
Exploratory worker code; no claim.  Prints PASS/FAIL per check.
"""
import os
os.environ.setdefault("NUMBA_NUM_THREADS", "1")
import sys, time, json
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "B6_maxwell_winding"))
sys.path.insert(0, HERE)
import ringlib as R
import pqmclib as Q
import dmclib as D

NPASS = NFAIL = 0


def check(name, ok, detail=""):
    global NPASS, NFAIL
    NPASS += bool(ok)
    NFAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name} {detail}", flush=True)


def within(x, err, ref, nsig=3.0, floor=0.0):
    return abs(x - ref) <= nsig * err + floor


t0 = time.time()
T = R.Torus((2, 2, 2))
lat = Q.Lattice((2, 2, 2))
check("lattice: plaquette/link ordering identical to B6 ringlib", np.array_equal(T.plaq, lat.plaq) and lat.nl == T.nl)
codes = R.sector_states(T, (0, 0, 0))
inv, sizes, nf = R.split_components(T, codes)
vc = codes[inv == np.argmax(sizes)]
comp = R.Component(T, vc)
check("vacuum component has 864 states", comp.n == 864, f"n={comp.n}")

# ---------- stoquasticity ------------------------------------------------------------
A = comp.A.toarray()
check("stoquastic: every off-diagonal element of H is -J or 0 (J=1)", set(np.unique(-A)) <= {0.0, -1.0} and (A >= 0).all())
ok = True
for V in (0.0, 0.5, 1.0, -1.0):
    Hm = np.diag(V * comp.nf) - A
    Hp = np.diag(V * comp.nf) + A
    ok &= np.allclose(np.linalg.eigvalsh(Hm), np.linalg.eigvalsh(Hp), atol=1e-9)
check("sign of J is a diagonal gauge on 2^3: spec(V N_f - A) = spec(V N_f + A) for V in {0,.5,1,-1}", ok)
# explicit link-sign gauge s_x=(-1)^y, s_y=(-1)^z, s_z=(-1)^x on even tori: plaquette product -1
for dims in ((2, 2, 2), (4, 4, 4), (4, 6, 8)):
    L2 = Q.Lattice(dims)
    s = np.array([(-1) ** int(L2.coord[l][(L2.axis[l] + 1) % 3]) for l in range(L2.nl)])
    prod = np.prod(s[L2.plaq], axis=1)
    check(f"{dims}: link signs s_a(r)=(-1)^r_(a+1) give product -1 on every plaquette (J -> -J gauge)", (prod == -1).all())

# ---------- exact references -----------------------------------------------------------
eps = (-1.0) ** lat.proot.sum(1)
harm = [lat.fourier_dirs((0, 0, 0), o)[0] for o in range(3)]
stag = np.where(lat.pori == 0, eps, 0.0) / np.sqrt(8)
coex = lat.coexact_dirs((np.pi, 0.0, 0.0))
Csrc = np.array(harm + [stag] + coex)
labels = ["harm_o0", "harm_o1", "harm_o2", "stag_xy", "coex_pi00"]
check("coexact directions at q=(pi,0,0): exactly one", len(coex) == 1, f"n={len(coex)}")
exact = {}
for V in (1.0, 0.5, 0.0):
    E0, g, gap = comp.ground(V)
    Hs, info = comp.hessian(V, Csrc)
    exact[V] = dict(E0=E0, chi=np.diag(Hs).tolist(), Nf=float((g * g * comp.nf).sum()))
    print(f"  exact V={V}: E0={E0:.9f} chi={np.round(np.diag(Hs), 9).tolist()}")
check("exact V=1 harmonic chi = 0.285050028242 (source note)", abs(exact[1.0]["chi"][0] - 0.285050028242) < 1e-10)
check("exact V=1 staggered chi = 0.105121402155 (source note)", abs(exact[1.0]["chi"][3] - 0.105121402155) < 1e-10)

# ---------- DMC ------------------------------------------------------------------------
sig0 = T.sigma_of(int(vc[0]))
out = {"exact": {str(k): v for k, v in exact.items()}, "dmc": {}}
for V in (1.0, 0.5, 0.0):
    tv = time.time()
    res = D.run(lat, sig0, V, N=2000, dt=0.1, ntherm_t=20, nblocks=60, block_t=20, Csrc=Csrc, seed_=11)
    Em = D.binned(res["Emix"])
    ch = D.chi_fit(res)
    out["dmc"][str(V)] = dict(Emix=Em, chi=ch)
    print(f"  DMC V={V}: Emix={Em[0]:.5f}+-{Em[1]:.5f} chi={[(round(a, 4), round(b, 4)) for a, b in ch]} ({time.time()-tv:.0f}s)")
    check(f"DMC V={V}: mixed energy within 3 sigma + 2e-3 of exact {exact[V]['E0']:.6f}", within(Em[0], Em[1], exact[V]["E0"], floor=2e-3))
    for s, lab in enumerate(labels):
        ref = exact[V]["chi"][s]
        check(f"DMC V={V}: {lab} curvature within 3 sigma + 1% of exact {ref:.6f}", within(ch[s][0], ch[s][1], ref, floor=0.01 * abs(ref)),
              f"{ch[s][0]:.4f}+-{ch[s][1]:.4f}")

# ---------- winding sectors at V=0 ---------------------------------------------------------
for W, ref in (((2, 0, 0), -7.399111), ((4, 0, 0), -4 * np.sqrt(2))):
    cw = R.sector_states(T, W)
    inv2, sz2, _ = R.split_components(T, cw)
    s0 = T.sigma_of(int(cw[inv2 == np.argmax(sz2)][0]))
    res = D.run(lat, s0, 0.0, N=2000, dt=0.1, ntherm_t=20, nblocks=20, block_t=10, Csrc=Csrc[:1], seed_=5)
    Em = D.binned(res["Emix"])
    check(f"DMC V=0 sector W={W}: energy within 3 sigma + 2e-3 of {ref:.6f}", within(Em[0], Em[1], ref, floor=2e-3), f"{Em[0]:.5f}+-{Em[1]:.5f}")
    out["dmc"][f"W{W}"] = Em

# ---------- negative control: local pair-update projector SSE ------------------------------
res = Q.run(lat, sig0, 1.0, m=1800, nsweep=20000, ntherm=2000, Csrc=Csrc[:3], check_every=500, seed_=3)
check("projector SSE: operator strings stay consistent (0 violations)", res["bad"] == 0)
chs, _, _ = Q.chi_from_M(res, 0.0)
mx = max(abs(c[0]) for c in chs)
out["pqmc_local_chi_V1"] = chs
check("negative control: local pair-update SSE fails to reproduce harmonic chi (|chi|<0.1 vs exact 0.285)", mx < 0.1,
      f"{[round(c[0], 4) for c in chs]}")

json.dump(out, open(os.path.join(HERE, "b13_validate_2cubed_results.json"), "w"), indent=1, default=float)
print(f"PASS={NPASS} FAIL={NFAIL} ({time.time()-t0:.0f}s)")
