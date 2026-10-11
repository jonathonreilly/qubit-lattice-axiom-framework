"""Lane RI / probe I2 (b): general and optimized N-band networks.  Units a = 1, target beta = c^2 = 1.

Sum rules (proved in I2_report.md; checked here):
  (S1) Hessian sum rule: for any N x N periodic C^2 dynamical matrix W(k), with u_n = lambda_n(W)/2,
       sum_n int_BZ u_n'' dk = int_BZ (tr W/2)'' dk = 0   (distributionally, crossings included)
       => band-summed, zone-averaged C3 boost anomaly  <sum_n (u_n'' - beta)> = -beta per mode, every N.
  (S2) face sum rule: sum_n f_n(k), f_n = u_n', is continuous and periodic, while the N lowest tower members
       have sum_n K_n(k) = N k (N odd) jumping by 2 pi N at the face  =>  sum_n |f_n - K_n| >= pi beta N at a face.

Checks:
 (A) random N-band finite-range networks: sum_n [f_n(pi-) - f_n(-pi+)] = 0 and sum_n <u_n''> = 0 (band-sorted
     eigenvalues, crossings included).
 (B) C1's face-touching two-band network = a fine chain of spacing a/2 folded: its 2 bands are eps(k), eps(k+2pi)
     of ONE smooth 4pi-periodic function eps(K) = D0(K) - 2 cos(K/2) alpha(K); partner residual at K = 2 pi.
 (C) optimized N-band networks ('C1 face touching generalized to N bands' = folded fine chain whose fine
     dispersion is exact sqrt(m^2+K^2) for |K| <= pi(N - 1) - gap, glued C-infinity to an even periodic cap at the
     fine face, then Fourier-truncated to fine range R): low-band errors super-algebraic in R, while the top band
     carries the whole -N anomaly and the pi N face floor.
"""
import numpy as np
out = []
def P(s=""):
    print(s, flush=True); out.append(s)
rng = np.random.default_rng(20261011)
m = 1.0

# ------------------------------------------------------------------ (A)
P("=== (A) sum rules on random N-band finite-range networks (W = B(k)^dag B(k) + m^2, range 2) ===")
def rand_net(N, rng):
    B = [rng.normal(size=(N, N)) + 1j * rng.normal(size=(N, N)) for _ in range(3)]
    def W(k):
        Bk = B[0] + B[1] * np.exp(1j * k) + B[2] * np.exp(2j * k)
        return Bk.conj().T @ Bk + m**2 * np.eye(N)
    return W
for N in (2, 3, 5, 8, 16):
    W = rand_net(N, rng)
    G = 2048
    ks = -np.pi + 2 * np.pi * np.arange(G) / G                     # periodic grid
    lam = np.array([np.linalg.eigvalsh(W(k)) for k in ks])        # band-sorted (crossings -> kinks)
    u = lam / 2; h = ks[1] - ks[0]
    upp = (np.roll(u, -1, 0) - 2 * u + np.roll(u, 1, 0)) / h**2   # distributional u_n'' incl. kink deltas
    tot = np.mean(np.sum(upp, axis=1))
    # Hellmann-Feynman slopes at the face from both sides (W periodic => equal multisets)
    def slopes(k):
        w, v = np.linalg.eigh(W(k)); dk = 1e-6
        dW = (W(k + dk) - W(k - dk)) / (2 * dk)
        return np.real(np.einsum('in,ij,jn->n', v.conj(), dW, v)) / 2
    jumpHF = np.sum(slopes(np.pi)) - np.sum(slopes(-np.pi))
    smooth_max = np.max(np.abs(np.mean(upp, axis=0)))
    P(f"N={N:2d}: <sum_n u_n''>_BZ = {tot:+.1e};  sum_n [f_n(pi) - f_n(-pi)] (Hellmann-Feynman) = {jumpHF:+.1e};"
      f"  max_n |<u_n''>_BZ| = {smooth_max:.1e}  (scale max u'' = {np.max(np.abs(upp)):.0f})")
P("-> the band-summed zone average of the Hessian is 0 for every finite N (telescoping / periodic tr W):")
P("   the zone-averaged boost anomaly sum_n <u_n'' - beta> = -beta N, i.e. -beta per mode, whatever the network.")
P("   (For band-sorted labels each band's distributional average is already 0; a tower-like band with u'' = beta")
P("    inside must pay with kink deltas at touchings, as SLAC pays with its face delta.)")

# ------------------------------------------------------------------ (B)
P("\n=== (B) C1's face-touching two-band network is a folded fine chain of spacing a/2 ===")
c = 1.0
Nf = 2**14
K2 = 4 * np.pi * np.arange(Nf) / Nf - 2 * np.pi            # extended zone (-2pi, 2pi]
def Gh(x): return np.sqrt(m**2 + c**2 * (np.pi - x)**2)
def alpha_loc(dl):
    s = np.sin(dl / 2); o = np.empty_like(dl); sm = np.abs(dl) < 1e-6
    o[~sm] = -(Gh(dl[~sm]) - Gh(-dl[~sm])) / 2 / (2 * s[~sm]); o[sm] = c**2 * np.pi / np.sqrt(m**2 + c**2 * np.pi**2)
    return o
def smoothstep(x):
    fz = lambda t: np.where(t > 0, np.exp(-1 / np.maximum(t, 1e-300)), 0.0)
    return fz(x) / (fz(x) + fz(1 - x))
def c1_fields(k):     # C1 construction, 2pi-periodic in k
    kk = (k + np.pi) % (2 * np.pi) - np.pi
    delta = np.where(kk >= 0, kk - np.pi, kk + np.pi)
    w = 1 - smoothstep((np.abs(delta) - 1.0) / 1.6)
    aL = alpha_loc(delta)
    a0 = alpha_loc(np.array([1.0]))[0]
    alpha = w * aL + (1 - w) * a0
    D0 = np.sqrt(m**2 + c**2 * kk**2) + 2 * np.abs(np.cos(kk / 2)) * alpha
    return D0, alpha
D0, al = c1_fields(K2)
eps = D0 - 2 * np.cos(K2 / 2) * al                        # one function on the extended zone
D0b, alb = c1_fields(K2 + 2 * np.pi)
lower = D0 - 2 * np.abs(np.cos(K2 / 2)) * al; upper = D0 + 2 * np.abs(np.cos(K2 / 2)) * al
# folding check: {eps(k), eps(k + 2pi)} == {lower(k), upper(k)} for k in (-pi, pi]
sel = np.abs(K2) <= np.pi
epsb = D0b - 2 * np.cos((K2 + 2 * np.pi) / 2) * alb
pair = np.sort(np.stack([eps[sel], epsb[sel]]), axis=0)
ref = np.sort(np.stack([lower[sel], upper[sel]]), axis=0)
P(f"max |{{eps(k), eps(k+2pi)}} - {{E_-(k), E_+(k)}}| = {np.max(np.abs(pair - ref)):.1e}")
F = np.fft.fft(eps) / Nf
P(f"smoothness of eps(K) on the 4pi-periodic extended zone: |Fourier coeff| at 200, 400, 800: "
  f"{abs(F[200]):.1e} {abs(F[400]):.1e} {abs(F[800]):.1e}  (super-algebraic decay: one smooth fine band)")
u = eps**2 / 2
dK = K2[1] - K2[0]
fE = np.gradient(u, dK)
ext = np.sqrt(m**2 + K2**2)
inner = np.abs(K2) <= np.pi
P(f"closure residual |f - K|: lowest band (|K|<=pi) max {np.max(np.abs(fE - K2)[inner]):.2e};"
  f" partner at the fine face K -> +-2pi: |f - K| = {np.abs(fE - K2)[np.argmin(np.abs(K2 - 2 * np.pi + 1e-9))]:.4f}"
  f" (= pi N with N = 2: {2 * np.pi:.4f})")
upp = np.gradient(fE, dK)
P(f"zone-averaged boost anomaly over both bands <u''-1> = {np.mean(upp) - 1:+.4f}; on the partner band "
  f"(|K|>pi) <u''-1> = {np.mean(upp[~inner]) - 1:+.3f}; lowest band <u''-1> = {np.mean(upp[inner]) - 1:+.2e}")
P("-> the C1 two-band construction IS a fine lattice of spacing a/2 (one smooth fine band, folded); its face")
P("   touching is the folding, and the 'partner-band' problem is the fine lattice's own face floor (pi N, A ~ -N).")

# ------------------------------------------------------------------ (C)
P("\n=== (C) optimized N-band networks: exact tower on the lowest N-1 bands, smooth even cap at the fine face ===")
def opt_eps(N, R, G=2**15):
    K = 2 * np.pi * N * np.arange(G) / G - np.pi * N              # fine zone (-pi N, pi N]
    # target u = (m^2 + K^2)/2 for |K| <= pi N - L1; smooth even periodic cap near |K| = pi N
    L1 = 2 * np.pi * 0.9                                          # cap width (less than one band)
    s = smoothstep((np.abs(K) - (np.pi * N - L1)) / (0.8 * L1))
    Kc = np.pi * N
    ucap = 0.5 * (m**2 + Kc**2) - 0.5 * (np.abs(K) - Kc)**2 * 0.0 + 0.0 * K   # flat cap at the fine-face value
    # build u'' : 1 in the tower region, compensating negative bump in the cap, so that u is even, periodic, smooth
    u = (1 - s) * 0.5 * (m**2 + K**2) + s * ucap
    # Fourier-truncate u to fine range R (coarse hopping range ~ R/N)
    U = np.fft.fft(u); fr = np.fft.fftfreq(G, 1 / G)
    U[np.abs(fr) > R] = 0
    uR = np.fft.ifft(U).real
    return K, u, uR
P("   N    R(fine)   sup|E-E_tower| band0   sup|f-K| band0   sup|f-K| band N-2   top-band <A>   top-band min A   |f-K| at edge")
for N in (3, 5, 9, 17):
    for R in (4 * N, 16 * N, 64 * N):
        K, u, uR = opt_eps(N, R)
        dK = K[1] - K[0]
        fR = np.gradient(uR, dK); uppR = np.gradient(fR, dK)
        E = np.sqrt(2 * np.maximum(uR, 1e-30))
        b0 = np.abs(K) <= np.pi
        nN2 = (N - 1) // 2 - 1
        bh = np.abs(np.abs(K) - 2 * np.pi * nN2) <= np.pi
        top = np.abs(K) > np.pi * (N - 2)
        e0 = np.max(np.abs(E - np.sqrt(m**2 + K**2))[b0])
        r0 = np.max(np.abs(fR - K)[b0]); rh = np.max(np.abs(fR - K)[bh])
        At = np.mean(uppR[top] - 1); Amin = np.min(uppR[top] - 1)
        edge = np.abs(fR - K)[np.argmax(np.abs(K))]
        P(f"  {N:3d}  {R:6d}     {e0:.2e}              {r0:.2e}         {rh:.2e}          {At:+8.2f}     {Amin:+9.1f}      {edge:.2f} (pi N = {np.pi * N:.2f})")
P("-> low bands converge super-algebraically in the hopping range; the top two bands (n = +-(N-1)/2) carry the")
P("   whole zone anomaly -N (mean -N/2 each), and the edge closure residual is pi N: relative 1.")
open('i2_sumrule.out', 'w').write('\n'.join(out) + '\n')
