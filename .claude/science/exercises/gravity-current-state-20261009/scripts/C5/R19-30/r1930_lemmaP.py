"""R19-30 (recheck of R19-26's Lemma P, independent of lib199): brute-force position-space operators on the 1D lattice (one translation cell).
For an operator O whose pieces sit at true positions y, T_true(q) = sum_y e^{-i q y} O_y (q any representative of the
transfer) and the 'site-label' kernel G(q) = sum_x e^{-i q x} O_{x+p} = e^{i q p} T_true(q).
Claim (Lemma P): G is a function on the torus (independent of the representative of q) and smooth iff O is local with
ALL pieces at p + Z;  T_true then flips by e^{-2 pi i p} when the representative of q jumps by 2 pi.
Tests (ring L, complex fermion psi_x, bilinear kernels K(k1, k2) = <k1| O(q) |k2>, k2 = k1 + q):
  (1) bond at its midpoint, psi^dag_x psi_{x+1} + h.c. at x + 1/2      (offset parity 1 -> sits at p = 1/2)
  (2) next-nearest bond psi^dag_x psi_{x+2} + h.c. at x + 1             (offset parity 0 -> sits at integers)
  (3) the MIXED midpoint operator (1) + (2), declared at p = 1/2         (the UD / E1-U situation)
  (4) (3) after the parity-resolved re-placement: the parity-0 piece moved to p = 1/2 by the 4-point stencil
      O'_{x+1/2} = sum_m a_m O_{x+1/2 - (m+1/2)}, a = (9/16, 9/16, -1/16, -1/16) at m = (0, -1, 1, -2)  [e^{-iq/2}F(q)]
For each, G is evaluated at the two representatives q and q - 2 pi of the same transfer: |G(q) - G(q - 2pi)| must vanish
for a local operator at p; and the Fourier coefficients of G(k1; q) along the full k1 circle at fixed k2 must decay."""
import numpy as np
L = 64
k = 2*np.pi*np.arange(L)/L
x = np.arange(L)

def kernel(pieces, q_rep, k1):
    """pieces: list of (position y (float), coefficient c, a, b) meaning c * psi^dag_{a} psi_{b} sits at y (a, b ints).
    returns T_true(q_rep; k1) = sum_pieces c e^{-i q y} <k1|psi^dag_a psi_b|k1 + q>, plane waves e^{i k x}/sqrt(L)."""
    out = 0.0
    k2 = k1 + q_rep
    for (y, c, a, b) in pieces:
        out = out + c*np.exp(-1j*q_rep*y)*np.exp(-1j*k1*a)*np.exp(1j*k2*b)
    return out

def op_pieces(kind):
    P = []
    for X in (0,):            # one translation cell: every cell gives the same symbol (k2 = k1 + q)
        if kind in ('nn', 'mixed', 'fixed'):
            P += [(X + 0.5, 1.0, X, X + 1), (X + 0.5, 1.0, X + 1, X)]
        if kind in ('nnn', 'mixed'):
            P += [(X + 1.0, 0.7, X, X + 2), (X + 1.0, 0.7, X + 2, X)]
        if kind == 'fixed':       # parity-0 piece re-placed to half-integers with the 4-point stencil
            for (m, a) in ((0, 9/16), (-1, 9/16), (1, -1/16), (-2, -1/16)):
                y = X + 1.0 + (m + 0.5)       # moved by +(m + 1/2): lands on a half-integer
                P += [(y, 0.7*a, X, X + 2), (y, 0.7*a, X + 2, X)]
    return P

def G(kind, p, q_rep, k1):
    """site-label kernel: e^{i q p} T_true; per piece only the phase matters, so evaluate one translation cell * L."""
    return np.exp(1j*q_rep*p)*kernel(op_pieces(kind), q_rep, k1)

print('R19-30 Lemma P recheck: explicit lattice operators, symbols on the infinite lattice (one translation cell)')
rng = np.random.default_rng(1930)
for kind, p in (('nn', 0.5), ('nnn', 0.0), ('nnn', 0.5), ('mixed', 0.5), ('mixed', 0.0), ('fixed', 0.5)):
    worst = 0.0; size = 0.0
    for t in range(40):
        k1 = rng.uniform(-np.pi, np.pi); q = rng.uniform(0.2, np.pi)
        g1 = G(kind, p, q, k1); g2 = G(kind, p, q - 2*np.pi, k1)
        worst = max(worst, abs(g1 - g2)); size = max(size, abs(g1))
    # Fourier coefficients of the TORUS function G(k1; q fixed) along the k1 circle, representative q in (-pi, pi]:
    # crossing of the cut happens in k2 = k1 + q, so scan k1 with k2 = k1 + q wrapped -> use q_rep = wrap(k2 - k1)
    N = 4096; kk = 2*np.pi*np.arange(N)/N - np.pi; k2 = 0.37
    qrep = -(((-(k2 - kk)) + np.pi) % (2*np.pi) - np.pi)
    g = np.array([G(kind, p, qq, kv) for qq, kv in zip(qrep, kk)])
    c = np.abs(np.fft.fft(g))/N; idx = np.minimum(np.arange(N), N - np.arange(N))
    band = lambda a, b: c[(idx >= a) & (idx < b)].max()
    print('  %-6s declared at p = %.1f : |G(q) - G(q - 2pi)| max %.2e (|G| ~ %.2f)  | Fourier |c_n| n in [64,128) %.1e  [512,1024) %.1e  [1024,2048) %.1e'
          % (kind, p, worst, size, band(64, 128), band(512, 1024), band(1024, 2048)))
print('expected: nn@1/2, nnn@0, fixed@1/2 representative-independent (local); nnn@1/2, mixed@1/2, mixed@0 not (1/n tails)')
