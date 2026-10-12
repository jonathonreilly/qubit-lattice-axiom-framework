"""Lane RI, probe I3, script 3: coarse cells as genuine superlattices (multi-band), 1D and a 3D count.

A real scalar on the fine chain with an L-periodic dynamical matrix K (cells of L fine sites).
Bloch matrix K(q), q in the coarse zone [-pi, pi] (coarse units, ell = L a = 1 here).
Checks:
 (1) trace sum rule: sum_n int u_n'' dq = int d^2/dq^2 (1/2 Tr K(q)) dq = 0 for every L and coupling,
     so the band-diagonal C3 anomaly A_n = u_n'' - c^2 averages to exactly -c^2 per mode (equipartition measure);
 (2) vacuum-weighted, band by band (no crossings): int u_n'' omega_n = -int omega_n (omega_n')^2 <= 0;
 (3) the low (acoustic) band is itself a lattice at spacing ell: its own zone-mean anomaly is -1 (in its
     own IR speed units), i.e. coarse cells move the C3 anomaly from a to ell, they do not remove it;
 (4) the projector construction K = M^2 (1 - Pi) + Pi K_c Pi (Pi = uniform mode of each cell, range L):
     internal bands exactly flat at M (no group velocity), low band = coarse NN chain.
"""
import numpy as np


def bloch_block_chain(L, Jin, Jout, m2, q):
    """fine chain, springs Jin inside a cell, Jout between cells; K = m2 + graph Laplacian."""
    K = np.zeros((L, L), dtype=complex)
    for i in range(L):
        K[i, i] += m2
    for i in range(L - 1):
        K[i, i] += Jin; K[i + 1, i + 1] += Jin; K[i, i + 1] -= Jin; K[i + 1, i] -= Jin
    # bond from last site of cell to first site of next cell
    K[L - 1, L - 1] += Jout; K[0, 0] += Jout
    K[L - 1, 0] -= Jout * np.exp(1j * q); K[0, L - 1] -= Jout * np.exp(-1j * q)
    return K


def bloch_projector(L, M2, Kc_hop, m2c, q):
    """K = M^2 (1 - Pi) + Pi K_c Pi with Pi the cell-uniform mode; K_c = coarse NN chain on cell CMs."""
    one = np.ones((L, 1)) / np.sqrt(L)
    Pi = one @ one.T
    kc = m2c + Kc_hop * 2 * (1 - np.cos(q))
    return M2 * (np.eye(L) - Pi) + kc * Pi


def bands(Kfun, nq=4096):
    q = 2 * np.pi * (np.arange(nq) + 0.5) / nq - np.pi
    ev = np.array([np.linalg.eigvalsh(Kfun(qq)) for qq in q])  # sorted omega^2
    return q, ev


def deriv_periodic(f, dq, order):
    F = np.fft.fft(f, axis=0)
    k = np.fft.fftfreq(f.shape[0], d=dq) * 2 * np.pi
    return np.real(np.fft.ifft(((1j * k) ** order)[:, None] * F, axis=0))


def analyse(tag, Kfun, nq=4096):
    q, w2 = bands(Kfun, nq)
    dq = q[1] - q[0]
    u = 0.5 * w2
    om = np.sqrt(np.maximum(w2, 0))
    upp = deriv_periodic(u, dq, 2)
    omp = deriv_periodic(om, dq, 1) if np.all(w2.min(axis=0) > 1e-8) else np.gradient(om, dq, axis=0)
    trace_rule = np.mean(np.sum(upp, axis=1))
    per_band_mean = np.mean(upp, axis=0)
    vac_w = np.mean(upp * om, axis=0)
    vac_ibp = -np.mean(om * omp ** 2, axis=0)
    # low band: IR speed^2 c0^2 = u0''(0); its own zone-mean anomaly in units of c0^2
    i0 = np.argmin(np.abs(q))
    c02 = upp[i0, 0]
    A_low_rel = per_band_mean[0] / c02 - 1.0
    print(f"{tag}: trace rule sum_n <u_n''> = {trace_rule:+.2e}; per-band <u_n''> = {np.array2string(per_band_mean[:4], precision=3)}...;"
          f" low band c0^2 = {c02:.4f}, own zone-mean anomaly <u0''>/c0^2 - 1 = {A_low_rel:+.4f};"
          f" vacuum-weighted <u_n'' w_n> (first 3) = {np.array2string(vac_w[:3], precision=4)} vs IBP {np.array2string(vac_ibp[:3], precision=4)};"
          f" gap to band 2 = {np.sqrt(w2[:,1].min())-np.sqrt(w2[:,0].max()):.3f}")
    return per_band_mean


if __name__ == "__main__":
    print("== (1)-(3) block chains: cells of L fine sites, strong inside (Jin), weak between (Jout), m^2 = 0.2 ==")
    for L in (2, 4, 8, 16):
        for Jin, Jout in ((1.0, 1.0), (4.0, 0.25)):
            analyse(f"L={L:2d} Jin={Jin} Jout={Jout}", lambda qq, L=L, Jin=Jin, Jout=Jout: bloch_block_chain(L, Jin, Jout, 0.2, qq), nq=2048)
    print("   (Jin = Jout = 1 is the uniform fine chain folded L times: a relabelling, nothing is bought.)")
    print("\n== (4) projector construction: internal bands exactly flat at M^2 = 9 (above the low band max 4.2), low band = coarse NN chain ==")
    for L in (4, 16):
        analyse(f"projector L={L}", lambda qq, L=L: bloch_projector(L, 9.0, 1.0, 0.2, qq), nq=2048)
    print("   internal bands: <u''> = 0 exactly (flat): anomaly A = -1 per quantum, no stress, no momentum.")
    print("\n== count: what a 3D coarse cell of L^3 fine sites holds ==")
    for L in (2, 8, 64, 1024):
        print(f"L={L:5d}: modes per cell {L**3:.3e}; relativistic (low-band) modes per cell 1; fraction of modes that must be"
              f" stress-free (flat) for the L^-4 law: {1-1/L**3:.6f}")
