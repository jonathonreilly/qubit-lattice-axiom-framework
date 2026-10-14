"""R2 check: can the one-handed tick be coupled to a U(1) field continuously and unitarily?

L x L torus in (x,y), Landau gauge A_y = phi*x (x = 0..L-1, seam between x=L-1 and x=0), phi = t*2pi/L.
t = 1: uniform field, N_phi = L flux quanta. k_y = 2pi m/L and k_z are good quantum numbers for every t.
Control: ordered strictly local tick S_x S_y S_z gauged factor by factor (unitary for every t).
Test: T4 range-2 truncation q_tr, Peierls-substituted hop by hop (y-move at the start x, then x-move),
unitarized U = Q (Q^dag Q)^{-1/2}; det-winding of U in k_z = det-winding of Q = net spectral flow
through any quasi-energy. Pre-registration: ../PREREG.md (Test R2). Memory: < 100 MB.
"""
import os
os.environ.setdefault("OMP_NUM_THREADS", "2")
import importlib.util
import numpy as np

here = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("r1", os.path.join(here, "r1_duality_check.py"))
r1 = importlib.util.module_from_spec(spec); spec.loader.exec_module(r1)

TAU = 2 * np.pi
sx = np.array([[0, 1], [1, 0]], complex); sy = np.array([[0, -1j], [1j, 0]]); sz = np.diag([1, -1]).astype(complex)
I2 = np.eye(2, dtype=complex)
COEF = {n: (c[0] * I2 - 1j * (c[1] * sx + c[2] * sy + c[3] * sz)) for n, c in r1.QTR.items()}
NZMAX = max(abs(n[2]) for n in COEF)


def Q_test(L, phi, ky, kz):
    """kz: array (M,). returns (M, 2L, 2L)."""
    M = len(kz)
    Q = np.zeros((M, 2 * L, 2 * L), complex)
    xs = np.arange(L)
    for (nx, ny, nz), C in COEF.items():
        ph = np.exp(1j * ny * (ky + phi * xs))            # Peierls phase of the y-move at the start x
        ez = np.exp(1j * nz * kz)                          # (M,)
        for x in xs:
            xp = (x + nx) % L
            Q[:, 2 * x:2 * x + 2, 2 * xp:2 * xp + 2] += ez[:, None, None] * (ph[x] * C)[None]
    return Q


def U_control(L, phi, ky, kz):
    M = len(kz)
    Pp = {j: (I2 + s) / 2 for j, s in ((0, sx), (1, sy), (2, sz))}
    Pm = {j: (I2 - s) / 2 for j, s in ((0, sx), (1, sy), (2, sz))}
    Sx = np.zeros((2 * L, 2 * L), complex); Sy = np.zeros((2 * L, 2 * L), complex)
    for x in range(L):
        # e^{-i kx sx}: P+ e^{-ikx} (n_x = -1) + P- e^{+ikx} (n_x = +1)
        Sx[2 * x:2 * x + 2, 2 * ((x - 1) % L):2 * ((x - 1) % L) + 2] += Pp[0]
        Sx[2 * x:2 * x + 2, 2 * ((x + 1) % L):2 * ((x + 1) % L) + 2] += Pm[0]
        a = ky + phi * x
        Sy[2 * x:2 * x + 2, 2 * x:2 * x + 2] = Pp[1] * np.exp(-1j * a) + Pm[1] * np.exp(1j * a)
    U = np.zeros((M, 2 * L, 2 * L), complex)
    for i, k in enumerate(kz):
        Sz = np.kron(np.eye(L), Pp[2] * np.exp(-1j * k) + Pm[2] * np.exp(1j * k))
        U[i] = Sx @ Sy @ Sz
    return U


def winding_from_dets(detfun, deg, Mfine=8192):
    """det(kz) is a Laurent polynomial in e^{ikz} of degree <= deg: sample exactly, zero-pad, unwrap."""
    Ms = 1
    while Ms < 2 * deg + 3:
        Ms *= 2
    Ms *= 2
    kz = TAU * np.arange(Ms) / Ms
    d = detfun(kz)
    c = np.fft.fft(d) / Ms                    # d(kz) = sum_m c[m] e^{-i m kz}? use ifft convention below
    # exact re-evaluation on a fine grid via zero-padding in the frequency domain
    cf = np.zeros(Mfine, complex)
    half = Ms // 2
    cf[:half] = c[:half]; cf[-half:] = c[-half:]
    dfine = np.fft.ifft(cf) * Mfine
    ph = np.unwrap(np.angle(dfine))
    w = (ph[-1] - ph[0] + (np.angle(dfine[0] / dfine[-1]))) / TAU
    return w, np.abs(dfine).min()


def run(L, tgrid):
    kys = TAU * np.arange(L) / L
    deg_test = NZMAX * 2 * L
    rows = []
    for t in tgrid:
        phi = t * TAU / L
        wt = 0.0; wc = 0.0; mindet = np.inf
        for ky in kys:
            w, md = winding_from_dets(lambda kz: np.linalg.det(Q_test(L, phi, ky, kz)), deg_test)
            wt += w; mindet = min(mindet, md)
            wcc, _ = winding_from_dets(lambda kz: np.linalg.det(U_control(L, phi, ky, kz)), 2 * L)
            wc += wcc
        rows.append((t, wt, wc, mindet))
    return rows


def sigma_min(L, t, ky_list=None, nk=512):
    phi = t * TAU / L
    kys = TAU * np.arange(L) / L if ky_list is None else ky_list
    kz = TAU * np.arange(nk) / nk
    smin = np.inf; arg = None
    for ky in kys:
        s = np.linalg.svd(Q_test(L, phi, ky, kz), compute_uv=False)[:, -1]
        i = int(np.argmin(s))
        if s[i] < smin:
            smin = s[i]; arg = (ky, kz[i])
    return smin, arg


def control_unitarity(L, t):
    phi = t * TAU / L
    kz = TAU * np.arange(16) / 16
    U = U_control(L, phi, 0.3, kz)
    return np.abs(np.einsum('mij,mkj->mik', U, U.conj()) - np.eye(2 * L)[None]).max()


def main():
    for L in (8, 12):
        tgrid = np.linspace(0, 1, 41)
        rows = run(L, tgrid)
        print(f"\n=== L = {L} (t = 1: N_phi = {L}, expected T22-type pump 4*N_phi = {4 * L}) ===")
        print("   t      winding(test)  winding(control)  min|det Q| over (ky,kz)")
        prev = None
        changes = []
        for (t, wt, wc, md) in rows:
            print(f"  {t:5.3f}   {wt:+9.3f}       {wc:+9.3f}          {md:.3e}")
            if prev is not None and abs(round(wt) - round(prev[1])) > 0:
                changes.append((prev[0], t, round(prev[1]), round(wt)))
            prev = (t, wt)
        print("control unitarity error at t = 0.5, 1:", control_unitarity(L, 0.5), control_unitarity(L, 1.0))
        print("winding changes of the gauged chiral tick (t_lo, t_hi, from, to):", changes)
        # locate each change by bisection on t, then sigma_min of Q at the bracket
        for (tlo, thi, w0, w1) in changes:
            def wind(t):
                phi = t * TAU / L
                return sum(winding_from_dets(lambda kz: np.linalg.det(Q_test(L, phi, ky, kz)), NZMAX * 2 * L)[0]
                           for ky in TAU * np.arange(L) / L)
            a, b = tlo, thi
            wa = round(wind(a))
            for _ in range(18):
                m = 0.5 * (a + b)
                if round(wind(m)) == wa:
                    a = m
                else:
                    b = m
            s_a, arg_a = sigma_min(L, a, nk=2048); s_b, arg_b = sigma_min(L, b, nk=2048)
            print(f"   change {w0:+d} -> {w1:+d} located in t in [{a:.6f}, {b:.6f}]: sigma_min(Q) = {s_a:.2e} / {s_b:.2e}"
                  f"  at (ky, kz) = ({arg_a[0]:.3f}, {arg_a[1]:.3f})")
        s_end, _ = sigma_min(L, 1.0)
        s_0, _ = sigma_min(L, 0.0)
        print(f"sigma_min(Q) at t=0: {s_0:.4f};  at t=1: {s_end:.4f}")


if __name__ == "__main__":
    main()
