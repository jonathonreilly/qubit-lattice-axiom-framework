"""Independent/adversarial checks for the K3a'' scratch calculation.

This file does not modify the worker's implementation.  It varies boundary
twists and the local interpolation used for off-diagonal photon constitutive
terms, and checks the constrained Maxwell oscillator and Coulomb kernel by
direct finite-dimensional linear algebra.
"""

import numpy as np
import scipy.linalg as sla

import k3a2_lib as lib


def photon_modes_variant(Q, G, averaging="product"):
    """Worker photon reduction with an explicitly selected local interpolation.

    For i != j the choices correspond to local placements of link-centered
    fields: product is the worker's site-centered four-link average;
    difference/sum use the two common-endpoint orientations; none collocates
    components algebraically.  All coincide in the continuum limit.
    """
    sig = 2 * np.sin(Q / 2)
    delta = 1j * sig
    n = len(Q)
    Mt = np.broadcast_to(G, (n, 3, 3)).copy()
    for i in range(3):
        for j in range(3):
            if i == j:
                continue
            if averaging == "product":
                fac = np.cos(Q[:, i] / 2) * np.cos(Q[:, j] / 2)
            elif averaging == "difference":
                fac = np.cos((Q[:, i] - Q[:, j]) / 2)
            elif averaging == "sum":
                fac = np.cos((Q[:, i] + Q[:, j]) / 2)
            elif averaging == "none":
                fac = np.ones(n)
            else:
                raise ValueError(averaging)
            Mt[:, i, j] *= fac
    Wt = Mt.copy()
    C = np.zeros((n, 3, 3), complex)
    C[:, 0, 1] = -delta[:, 2]
    C[:, 0, 2] = delta[:, 1]
    C[:, 1, 0] = delta[:, 2]
    C[:, 1, 2] = -delta[:, 0]
    C[:, 2, 0] = -delta[:, 1]
    C[:, 2, 1] = delta[:, 0]
    K = np.einsum("nba,nbc,ncd->nad", np.conj(C), Wt.astype(complex), C)
    Minv = np.linalg.inv(Mt)
    r = np.einsum("ni,nij->nj", delta, Minv)
    u = lib._nullspace_basis(delta)
    w = lib._nullspace_basis(r)
    overlap = np.einsum("nia,nib->nab", np.conj(u), w)
    w = np.einsum("nia,nab->nib", w, np.linalg.inv(overlap))
    MT = np.einsum("nia,nij,njb->nab", np.conj(u), Mt.astype(complex), u)
    KT = np.einsum("nia,nij,njb->nab", np.conj(w), K, w)
    ev, V = np.linalg.eigh(MT)
    S = np.einsum("nab,nb,ncb->nac", V, np.sqrt(ev), np.conj(V))
    Om2 = np.einsum("nab,nbc,ncd->nad", S, KT, S)
    Om2 = (Om2 + np.conj(np.swapaxes(Om2, 1, 2))) / 2
    o2, Vo = np.linalg.eigh(Om2)
    omega = np.sqrt(o2)
    Amode = np.einsum("nia,nab,nbk->nki", w, S, Vo)
    Amode /= np.sqrt(2 * omega)[:, :, None]
    Gc = 1 / np.einsum("ni,nij,nj->n", sig, Minv, sig)
    return omega, Amode, Gc, Mt, K


def e2_variant(L, e, G, twist=0.5, averaging="product", nfac=0.5):
    qa, Q = lib.q_grid(L)
    om, Am, Gc, _, _ = photon_modes_variant(Q[1:], G, averaging)
    omega = np.zeros((L**3, 2))
    Amode = np.zeros((L**3, 2, 3), complex)
    coul = np.zeros(L**3)
    omega[1:] = om
    Amode[1:] = Am
    coul[1:] = Gc

    pa = 2 * np.pi * (np.arange(L) + twist) / L
    s = np.sin(pa)
    S3 = np.stack(np.meshgrid(s, s, s, indexing="ij"), axis=-1)
    d = np.einsum("aj,xyzj->xyza", e, S3)
    dabs = np.linalg.norm(d, axis=-1)
    nh = d / dabs[..., None]
    ex = lib.exchange_sum(L, e, pa, qa, nh, dabs, omega, Amode)
    dia, _, _ = lib.dia_sum(L, e, pa, nh, Amode)
    co = lib.coulomb_sum(L, nh, coul)
    return {"exch": nfac * ex, "dia": nfac * dia, "coul": nfac * co,
            "tot": nfac * (ex + dia + co)}


def second_derivative(eval_at, h=0.08):
    """Even five-point/Richardson estimate of E''(0)."""
    z = eval_at(0.0)
    ans = {}
    for key in z:
        c_h = (eval_at(h)[key] + eval_at(-h)[key] - 2 * z[key]) / h**2
        c_2h = (eval_at(2 * h)[key] + eval_at(-2 * h)[key] - 2 * z[key]) / (2 * h)**2
        ans[key] = (4 * c_h - c_2h) / 3
    return ans


def constrained_photon_check():
    """Compare worker frequencies with symplectic eigenvalues in reduced phase space."""
    rng = np.random.default_rng(240513)
    errs_w = []
    errs_c = []
    errs_g = []
    for _ in range(12):
        q = rng.uniform(-2.7, 2.7, 3)
        X = rng.normal(size=(3, 3))
        G = X @ X.T + np.eye(3)
        om, A, Gc, Mstack, Kstack = photon_modes_variant(q[None], G)
        M = Mstack[0]
        K = Kstack[0]
        sig = 2 * np.sin(q / 2)
        delta = 1j * sig
        r = delta @ np.linalg.inv(M)

        # Coordinate basis obeys generalized Coulomb gauge; canonical momentum
        # obeys Gauss law.  Normalize the two bases to be symplectic duals.
        W = sla.null_space(r[None, :])
        U0 = sla.null_space(delta[None, :])
        U = U0 @ np.linalg.inv(W.conj().T @ U0)
        Kq = W.conj().T @ K @ W
        Mp = U.conj().T @ M @ U
        H = sla.block_diag(Kq, Mp)
        J = np.block([[np.zeros((2, 2)), np.eye(2)],
                      [-np.eye(2), np.zeros((2, 2))]])
        vals = np.linalg.eigvals(J @ H)
        wd = np.sort(np.abs(np.imag(vals)))[::2]
        errs_w.append(np.max(np.abs(wd - np.sort(om[0]))))

        # Direct constrained minimization of (1/2) p^T M p at unit charge.
        pinv = np.linalg.inv(M) @ sig
        pmin = pinv / (sig @ pinv)
        twice_energy = pmin @ M @ pmin
        errs_c.append(abs(twice_energy - Gc[0]))
        errs_g.append(np.max(np.abs(r @ A[0].T)))
    print("constrained photon: max frequency error", max(errs_w))
    print("Coulomb minimization: max kernel error", max(errs_c))
    print("generalized-Coulomb gauge: max residual", max(errs_g))


def response_checks(L=16):
    for averaging in ("product", "difference", "sum", "none"):
        def ev(t):
            e, G = lib.rule_matrices("exp", t, lib.EPS_FACE)
            return e2_variant(L, e, G, averaging=averaging)
        c = second_derivative(ev)
        print("face averaging", averaging, {k: float(v) for k, v in c.items()})

    for twist in (0.17, 0.31, 0.5):
        def ev(t):
            e, G = lib.rule_matrices("exp", t, lib.EPS_AXIS)
            return e2_variant(L, e, G, twist=twist)
        c = second_derivative(ev)
        print("axis fermion twist", twist, {k: float(v) for k, v in c.items()})

    # A common compact-KS Gauss-law convention uses the staggered static
    # background rho_bg(x)=(-1)^(x+y+z)/2 rather than a uniform half-filling
    # subtraction.  Its cross term with the massless vacuum vanishes, and its
    # Coulomb energy per cell is G(pi,pi,pi)/8.  This is absent from the worker
    # convention, so quote its separate shear curvature.
    qcorner = np.full((1, 3), np.pi)
    for name, eps in (("axis", lib.EPS_AXIS), ("face", lib.EPS_FACE)):
        def bg(t, eps=eps):
            _, G = lib.rule_matrices("exp", t, eps)
            Gc = photon_modes_variant(qcorner, G)[2][0]
            return {"background_coul": Gc / 8}
        print("staggered-background", name, second_derivative(bg))

    # The second-order metric completion shifts both normalized TT channels by
    # the same density response; the channel splitting is therefore invariant.
    for kf, kg in ((0, 0), (1, 1), (-1, 2), (3, -2)):
        vals = {}
        for name, eps in (("axis", lib.EPS_AXIS), ("face", lib.EPS_FACE)):
            def ev(t, eps=eps):
                return lib.E2_parts(L, *lib.rule_matrices("fam", t, eps, kf, kg))
            vals[name] = second_derivative(ev)["tot"]
        print("family", kf, kg, vals, "face-axis", vals["face"] - vals["axis"])


if __name__ == "__main__":
    constrained_photon_check()
    response_checks()
