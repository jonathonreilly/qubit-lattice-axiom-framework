"""R8-5 Lemma C illustration (1D, one mode per site, ring of L sites).
Attempted 'box charge' densities: m_x = |w_x><w_x| with w_x = chi^(1/2)(-i d) delta_x (smooth box chi in k),
so sum_x m_x = chi(k) (box-confined charge). Lemma C says no commuting quasi-local family can have a
non-constant charge symbol. Check: (i) sum_x m_x = chi; (ii) max_{x != y} ||[m_x, m_y]|| is O(1), not 0;
(iii) control: on-site m_x = |x><x| (chi = 1) commutes exactly; (iv) phase-dressed m_x = |phi_x><phi_x| with
|phi_hat| = 1 (a gauge-equivalent on-site density) commutes: charge symbol constant = 1.
"""
import numpy as np
L = 256
k = 2 * np.pi * np.fft.fftfreq(L)
def phi(t):
    t = np.clip(t, 0, 1)
    f0 = np.where(t > 0, np.exp(-1 / np.where(t > 0, t, 1)), 0.0)
    f1 = np.where(t < 1, np.exp(-1 / np.where(t < 1, 1 - t, 1)), 0.0)
    return f0 / (f0 + f1)
def run(chi_hat, label):
    w0 = np.fft.ifft(np.sqrt(chi_hat + 0j))              # w_0(x); |w_hat|^2 = chi/L
    W = np.array([np.roll(w0, x) for x in range(L)])      # rows: w_x
    M = [np.outer(W[x], W[x].conj()) for x in (0, 1, 2, 5)]
    S = sum(np.outer(W[x], W[x].conj()) for x in range(L))
    Sk = np.fft.fft(np.fft.ifft(S, axis=0), axis=1)       # momentum-space matrix of sum_x m_x
    diag = np.real(np.diag(Sk)); diag = diag / np.max(diag)  # charge symbol, normalised to max 1
    comm = max(np.linalg.norm(M[0] @ M[j] - M[j] @ M[0], 2) for j in (1, 2, 3)) / np.linalg.norm(M[0], 2) ** 2
    off = np.max(np.abs(Sk - np.diag(np.diag(Sk))))
    print(f"{label:40s} sum_x m_x diagonal in k: off-diag {off:.1e}; symbol range [{diag.min():.3f},{diag.max():.3f}]; "
          f"max ||[m_0,m_y]||/||m_0||^2 (y=1,2,5) = {comm:.3e}")
chi_box = 1 - phi((np.abs(k) - 1.0) / 1.0)                 # 1 on |k|<=1, 0 beyond 2
run(chi_box, "smooth box charge chi (b1=1,b2=2)")
run(np.ones(L), "on-site control (chi = 1)")
run(np.exp(2j * 0.7 * np.sin(k)), "phase-dressed |phi_hat|=1 (gauge-equivalent)")
