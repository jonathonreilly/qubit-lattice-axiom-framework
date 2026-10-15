"""Independent OBS-2 checks for the referee record.

This deliberately does not import the worker's integration/assembly code.  It
builds the 4x4 spectral-projector self energy and differentiates the resulting
matrix in external frequency and momentum.
"""
import json
import math
import sys

import numpy as np


s0 = np.eye(2, dtype=complex)
sx = np.array([[0, 1], [1, 0]], dtype=complex)
sy = np.array([[0, -1j], [1j, 0]], dtype=complex)
sz = np.diag([1.0, -1.0]).astype(complex)
sig = (sx, sy, sz)
tx = np.kron(sx, s0)
tzsig = tuple(np.kron(sz, s) for s in sig)
i4 = np.eye(4, dtype=complex)
corners = (
    np.array([math.pi, 0.0, 0.0]),
    np.array([0.0, math.pi, 0.0]),
    np.array([0.0, 0.0, math.pi]),
)


def rot(t12, t23, t13, delta):
    s12, c12 = math.sin(t12), math.cos(t12)
    s23, c23 = math.sin(t23), math.cos(t23)
    s13, c13 = math.sin(t13), math.cos(t13)
    phase = np.exp(1j * delta)
    return np.array([
        [c12*c13, s12*c13, s13/phase],
        [-s12*c23-c12*s23*s13*phase,
         c12*c23-s12*s23*s13*phase, s23*c13],
        [s12*s23-c12*c23*s13*phase,
         -c12*s23-s12*c23*s13*phase, c23*c13],
    ])


def grid(n):
    u = -math.pi + (np.arange(n) + 0.5) * 2*math.pi/n
    return u*np.abs(u)/math.pi, 2*np.abs(u)/math.pi


def symbols(k):
    return np.stack((np.ones_like(k[0]),) + tuple((1-np.cos(x))/2 for x in k))


def self_energy(p, y, n, m0, delta, mh, omega):
    """Retarded old-fashioned one-loop Sigma, built from P_+ and P_- matrices."""
    qg, jac = grid(n)
    q1, q2 = np.meshgrid(qg, qg, indexing="ij")
    q1, q2 = q1.ravel(), q2.ravel()
    j12 = np.outer(jac, jac).ravel()
    gp = symbols(tuple(np.array(p[a]) for a in range(3)))[:, ...]
    gp = np.array([float(x) for x in gp])
    total = np.zeros((4, 4), dtype=complex)
    for ix in range(n):
        q = (np.full_like(q1, qg[ix]), q1, q2)
        weight = jac[ix]*j12/n**3
        k = tuple(p[a]-q[a] for a in range(3))
        sk = tuple(np.sin(x) for x in k)
        mass = m0 + delta*(1-sum(np.cos(x) for x in k))/2
        energy = np.sqrt(sum(x*x for x in sk) + mass*mass)
        om = np.sqrt(sum(4*np.sin(x/2)**2 for x in q) + mh*mh)
        h = mass[:, None, None]*tx
        for a in range(3):
            h = h + sk[a][:, None, None]*tzsig[a]
        hn = h/energy[:, None, None]
        pplus = (i4 + hn)/2
        pminus = (i4 - hn)/2
        ypk = y @ ((symbols(k) + gp[:, None])/2)
        pref = weight*ypk*ypk/(2*om)
        integrand = (
            (tx @ pplus @ tx)/(omega-energy-om)[:, None, None]
            + (tx @ pminus @ tx)/(omega+energy+om)[:, None, None]
        )
        total += np.einsum("p,pij->ij", pref, integrand)
    return total


def velocity_tensor(y, n, m0, delta, mh, dp=1e-3, dw=1e-4):
    tensors = []
    zlist = []
    for e in corners:
        center_p = self_energy(e, y, n, m0, delta, mh, dw)
        center_m = self_energy(e, y, n, m0, delta, mh, -dw)
        ds_dw = (center_p-center_m)/(2*dw)
        z = np.trace(ds_dw[:2, :2]).real/2
        dv = np.empty(3)
        for a in range(3):
            shift = np.zeros(3)
            shift[a] = dp
            sp = self_energy(e+shift, y, n, m0, delta, mh, 0.0)
            sm = self_energy(e-shift, y, n, m0, delta, mh, 0.0)
            deriv = (sp-sm)/(2*dp)
            bprime = np.trace(sig[a] @ deriv[:2, :2]).real/2
            dv[a] = bprime/math.cos(e[a]) + z
        tensors.append(dv)
        zlist.append(z)
    return np.array(tensors), np.array(zlist)


def ypattern(u, masses, split, vev=174.1):
    matrix = u @ np.diag(masses) @ u.conj().T
    y0 = np.trace(matrix).real/(3*vev) if split == "trace" else 0.0
    return np.r_[y0, np.diag(matrix).real/vev-y0]


def split_universal(tensor):
    iso = tensor.mean()
    tet = np.mean([tensor[c, c] - np.mean(np.delete(tensor[c], c)) for c in range(3)])
    universal = np.empty((3, 3))
    for c in range(3):
        universal[c] = iso + tet*(np.eye(3)[c]-1/3)
    return iso, tet, tensor-universal


def branch_b(n, m0, delta, split):
    deg = math.pi/180
    ckm = rot(13.04*deg, 2.38*deg, 0.201*deg, 1.20)
    root = np.exp(2j*math.pi/3)
    fourier = np.array([[root**(c*j) for j in range(3)] for c in range(3)])/math.sqrt(3)
    upmass = np.array([2.16e-3, 1.27, 172.69])
    downmass = np.array([4.67e-3, 0.0934, 4.18])
    uu, ud = fourier, fourier @ ckm
    yu = ypattern(uu, upmass, split)
    yd = ypattern(ud, downmass, split)
    tu, zu = velocity_tensor(yu, n, m0, delta, m0)
    td, zd = velocity_tensor(yd, n, m0, delta, m0)
    q = tu+td
    dr = 2*td
    iq, tq, rq = split_universal(q)
    ir, tr, rr = split_universal(dr)
    weights = np.abs(ud)**2
    dl = np.array([sum(weights[c, i]*rq[c] for c in range(3)) for i in range(3)])
    drmass = np.array([sum(weights[c, i]*rr[c] for c in range(3)) for i in range(3)])
    vec = (dl+drmass)/2
    axial = (dl-drmass)/2
    ctt = -0.75*vec.mean(axis=1)
    dtt = -0.75*axial.mean(axis=1)
    return {
        "N": n, "m0": m0, "Delta": delta, "split": split,
        "yu": yu.tolist(), "yd": yd.tolist(),
        "z_up": zu.tolist(), "z_down": zd.tolist(),
        "universal_Q": [iq, tq], "universal_dc": [ir, tr],
        "d_cTT": ctt.tolist(), "d_dTT": dtt.tolist(),
        "d_cvec": (-(vec-vec.mean(axis=1, keepdims=True))).tolist(),
        "d_dvec": (-(axial-axial.mean(axis=1, keepdims=True))).tolist(),
    }


def lv3_small_q():
    rho0 = np.eye(2)
    rhox = sx
    qvecs = {"x": np.array([1.0, 0, 0]), "z": np.array([0.0, 0, 1.0])}
    m, b = 0.01, 0.004
    def h(k):
        return sum(np.sin(k[a])*np.kron(sz, sig[a]) for a in range(3)) + m*tx
    def block(q, g):
        ex = np.array([math.pi, 0.0, 0.0])
        big_b = b*np.kron(sx, g)
        return np.block([[h(ex+q), big_b], [big_b.conj().T, h(ex+q+np.array([math.pi, math.pi, 0]))]])
    result = {}
    for name, g in (("blind", s0), ("sigma_z", sz)):
        e0 = np.linalg.eigvalsh(block(np.zeros(3), g))[4:]
        result[name] = {}
        for qmag in (1e-3, 2e-4, 5e-5):
            result[name][str(qmag)] = {}
            for dn, direction in qvecs.items():
                e = np.linalg.eigvalsh(block(qmag*direction, g))[4:]
                ratio = (e*e-e0*e0-qmag*qmag)/(qmag*qmag)
                result[name][str(qmag)][dn] = ratio.tolist()
    return result


if __name__ == "__main__":
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 24
    checks = [branch_b(n, 0.1, 0.0, "trace"), branch_b(n, 0.1, 0.5, "trace")]
    print(json.dumps({"loop_checks": checks, "lv3": lv3_small_q()}, indent=2))
