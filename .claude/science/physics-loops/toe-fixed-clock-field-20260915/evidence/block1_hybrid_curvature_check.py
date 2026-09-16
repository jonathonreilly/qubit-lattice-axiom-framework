"""Actual free-four-cube Gamma2 diagnostic for the hybrid generator.

The direct generator calculation uses jets realized by smooth bump functions.
A separate scalar reduction checks its normalization. Negative curvature
rejects this pointwise sufficient criterion, not an integrated gap estimate.
"""
import itertools
import json
import math
from pathlib import Path

import numpy as np


def four_cube():
    vertices = list(itertools.product(range(2), repeat=4))
    edges = [(x, i) for x in vertices for i in range(4) if x[i] == 0]
    faces = [(x, (i, j)) for x in vertices for i in range(4)
             for j in range(i+1, 4) if x[i] == x[j] == 0]
    ei = {e: n for n, e in enumerate(edges)}
    D = np.zeros((len(faces), len(edges)))
    for p, (x, (i, j)) in enumerate(faces):
        xi, xj = list(x), list(x)
        xi[i] += 1
        xj[j] += 1
        for e, sign in [((x, i), 1), ((tuple(xi), j), 1),
                        ((tuple(xj), i), -1), ((x, j), -1)]:
            D[p, ei[e]] += sign
    P = D @ np.linalg.pinv(D)
    H = D @ D.T
    assert D.shape == (24, 32)
    assert np.linalg.matrix_rank(D) == 17
    assert np.max(abs(P@P-P)) < 2e-14
    assert np.max(abs(np.diag(P)-17/24)) < 2e-14
    assert np.all(np.diag(H) == 4)
    assert np.all(np.diag(H@H) == 24)
    return D, P


def check(beta):
    D, P = four_cube()
    tau = 1/64
    A = np.eye(24)+tau*D@D.T
    p = 0
    ep = np.eye(24)[p]
    h = 2*math.pi*math.sqrt(beta)
    q = h*h*A[p,p]
    mu = math.exp(q/4)
    a0 = h*mu/2
    z0 = h*ep
    moves = [s*h*np.eye(24)[i] for i in range(24) for s in [-1, 1]]

    def jets(z):
        n = round(float(z[p]/h))
        assert abs(z[p]/h-n) < 1e-10
        # Value and first/second/third derivative at the five relevant points.
        value = {-1:2., 0:1., 1:0., 2:0., 3:0.}[n]
        first = a0 if n in [0, 1, 2] else 0.
        return value, first*ep, np.zeros((24,24)), 0.

    def rate(z, v):
        c = math.exp(-float(v@A@z)/2-float(v@A@v)/4)
        g = -(A@v)*c/2
        Hc = np.outer(A@v, A@v)*c/4
        return c, g, Hc

    def Lf(z):
        f, g, Hf, third = jets(z)
        val = float(np.sum(P*Hf)-(P@A@z)@g)
        grad = -(A@P@g)-Hf@P@A@z+P[p,p]*third*ep
        for v in moves:
            fv, gv, _, _ = jets(z+v)
            c, gc, _ = rate(z, v)
            val += c*(fv-f)
            grad += gc*(fv-f)+c*(gv-g)
        return val, grad

    def Gamma(z, derivatives=False, split=False):
        f, g, Hf, third = jets(z)
        val_cont = float(g@P@g)
        val_jump = 0.
        grad = 2*Hf@P@g
        Hess = 2*Hf@P@Hf + 2*third*float(ep@P@g)*np.outer(ep,ep)
        for v in moves:
            fv, gv, Hv, _ = jets(z+v)
            c, gc, Hc = rate(z, v)
            d, dg, dH = fv-f, gv-g, Hv-Hf
            val_jump += c*d*d/2
            grad += (gc*d*d+2*c*d*dg)/2
            Hess += (Hc*d*d+2*d*(np.outer(gc,dg)+np.outer(dg,gc))
                     +2*c*np.outer(dg,dg)+2*c*d*dH)/2
        if split:
            return val_cont, val_jump
        val = val_cont+val_jump
        return (val, grad, Hess) if derivatives else val

    gam, ggam, Hgam = Gamma(z0, True)
    gam_cont, gam_jump = Gamma(z0, split=True)
    Lgam = float(np.sum(P*Hgam)-(P@A@z0)@ggam)
    for v in moves:
        c, _, _ = rate(z0,v)
        # Subtract the two form components separately: their magnitudes differ
        # exponentially here. Combining them first loses the smaller jump part.
        shifted_cont, shifted_jump = Gamma(z0+v, split=True)
        Lgam += c*((shifted_cont-gam_cont)+(shifted_jump-gam_jump))
    f, gf, _, _ = jets(z0)
    lf, glf = Lf(z0)
    mixed = float(gf@P@glf)
    for v in moves:
        c, _, _ = rate(z0,v)
        fv, _, _, _ = jets(z0+v)
        mixed += c*(fv-f)*(Lf(z0+v)[0]-lf)/2
    direct = Lgam/2-mixed

    r = math.exp(-q/2)
    pd, d, e = 17/24, 37/48, 1289/1536
    scalar = (mu*mu*(1-r-d*h*h)/4+(3-r)/4
              -e*h*h*mu/16+4*(1-math.cosh(tau*h*h/2)))
    scalar_gamma = pd*h*h*mu*mu/4+mu/2
    relative = abs(direct-scalar)/max(1,abs(scalar))
    assert relative < 4e-12
    assert abs(gam-scalar_gamma)/gam < 4e-13
    assert direct < 0

    # Actual electric correction: main's uniform Hessian bound, not a replacement
    # of the clock law by the Gaussian reference. All these points are periods,
    # so its first derivatives vanish; Gamma2 changes by at most delta*Gamma_cont.
    N = math.ceil(256*math.sqrt(beta))
    g2 = N*N/beta
    delta_e = 3*g2*58_320_000_000*math.exp(-g2/1024)
    correction = delta_e*pd*a0*a0
    assert g2/256 >= 256
    assert d*h*h-delta_e*pd*h*h >= 4
    assert scalar+correction < 0
    return dict(beta=beta, N=N, q=q, mean_reference_not_used=True,
                gamma=gam, direct_gamma2=direct, scalar_gamma2=scalar,
                relative_error=relative, curvature_ratio=direct/gam,
                electric_hessian_bound=delta_e,
                electric_correction_upper=correction,
                actual_clock_gamma2_upper=scalar+correction)


def main():
    rows = [check(beta) for beta in [1., 2., 4.]]
    out = dict(status='negative_pointwise_curvature_witness_checked', rows=rows,
               scope='Finite free four-cube; fixed-clock correction uses the cited '
                     'uniform electric-extension theorem. No gap, phase, or axiom no-go.')
    Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))


if __name__ == '__main__':
    main()
