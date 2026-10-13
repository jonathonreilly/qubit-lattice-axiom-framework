"""R17-12 library: placement variants of the lattice Maxwell TT vertex (R17-9's conventions, rotated frame).

Pair matrix (both legs created, k1 + k2 = q, R17-9 photon.py:10-12):
  N = (1/2)[ sqrt(w1 w2) M_E + X1^T M_B X2 / sqrt(w1 w2) ],  X v = sigma x v,  sum_pol |amp|^2 = Re tr(P1 N P2 N^dagger).
Forward scattering (a^dagger_k a_k, legs (-k, k)) per polarization pair (derived in the report, sec. 3.1):
  S_ll' = (1/2)[ w eps_l^T M_E eps_l' + (sh x eps_l)^T M_B (sh x eps_l') w ],  sh = sigma/|sigma|.
  W1 at O(q) + symmetric T + int T^00 = H  =>  S_ll' = -(w/2) e:(v v) delta_ll',  v_i = sigma_i sigma_i'/w  (R17-9 sign, T = EE+BB-...).
Vertices (M_E, M_B as 3x3 in field-component space; c = d' per-leg averaging symbol; s = k1z + k2z with representatives):
  VU    : R17-9's registered vertex (E_j averaged along j; B_x along y,z; B_y along x,z), traceless e only.
  VMone : R17-9's VM (B product at z+1/2, phase exp(i s/2)); T2g: E_x along x, E_y along y, B_x along y, B_y along x; Eg: none.
  VMsym : VM with the B product placed symmetrically at z +- 1/2 (cos(s/2)); C2-covariant version.
  VW(n) : forward-correct ("index-placed") Maxwell stress T_ij = c_i c_j [E_iE_j + B_iB_j - delta_ij (E^2+B^2)/2],
          every half-integer-height product placed symmetrically at z +- (n+1/2): factor P = cos((n+1/2) s).
          T2g: = VMsym with offset n.  Eg: includes the delta part with weights (c_x^2 - c_y^2)/2 (E_z^2, B_z^2).
  VWa   : VW with the two-offset symmetric stencil P = (1-a) cos(s/2) + a cos(3s/2) (a = 0 is VW0), for the sensitivity.
"""
import numpy as np
from photon import kgrid, crossmat, EPOL, photonG, photonGw, photonNN, PhotonProfile

def _diag3(a, b, c):
    M = np.zeros(np.broadcast(a, b, c).shape + (3, 3), dtype=np.result_type(a, b, c, float))
    M[..., 0, 0] = a; M[..., 1, 1] = b; M[..., 2, 2] = c
    return M

def _offxy(a, b):
    """matrix with (x,y) = a, (y,x) = b."""
    M = np.zeros(np.broadcast(a, b).shape + (3, 3), dtype=np.result_type(a, b, float))
    M[..., 0, 1] = a; M[..., 1, 0] = b
    return M

def vertex(var, pol, c1, c2, s, lam=None):
    """c1, c2: (..., 3) per-leg averaging symbols c(k_i); s: k1z + k2z (representatives). returns M_E, M_B."""
    one = np.ones_like(c1[..., 0])
    if var == 'VU':
        ct1 = np.stack([c1[..., 1]*c1[..., 2], c1[..., 0]*c1[..., 2], c1[..., 0]*c1[..., 1]], -1)
        ct2 = np.stack([c2[..., 1]*c2[..., 2], c2[..., 0]*c2[..., 2], c2[..., 0]*c2[..., 1]], -1)
        e = EPOL[pol]
        ME = c1[..., :, None]*e*c2[..., None, :]
        MB = ct1[..., :, None]*e*ct2[..., None, :]
        return ME, MB
    if var in ('VMone', 'VMsym', 'VMn'):
        P = np.exp(0.5j*s) if var == 'VMone' else np.cos(0.5*s)
        if pol == 'T2g':
            ME = _offxy(c1[..., 0]*c2[..., 1], c1[..., 1]*c2[..., 0])
            MB = _offxy(c1[..., 1]*c2[..., 0], c1[..., 0]*c2[..., 1])*P[..., None, None]
        else:
            ME = _diag3(one, -one, 0*one); MB = ME*P[..., None, None]
        return ME, MB
    if var.startswith('VW'):
        if var == 'VWa':
            # two-offset symmetric stencil: weight (1-a) at z +- 1/2, a at z +- 3/2; antiperiodic in s (continuity);
            # P(0) = 1 (forward W1), O(s^2) coefficient -lam/2 with lam = 1/4 + 2a.
            P = (1.0 - lam)*np.cos(0.5*s) + lam*np.cos(1.5*s)
        else:
            n = int(var[2:]) if len(var) > 2 else 0
            P = np.cos((n + 0.5)*s)
        if pol == 'T2g':
            ME = _offxy(c1[..., 0]*c2[..., 1], c1[..., 1]*c2[..., 0])
            MB = _offxy(c1[..., 1]*c2[..., 0], c1[..., 0]*c2[..., 1])*P[..., None, None]
        else:
            cx2 = c1[..., 0]*c2[..., 0]; cy2 = c1[..., 1]*c2[..., 1]
            sp, sm = 0.5*(cx2 + cy2), 0.5*(cx2 - cy2)
            ME = _diag3(sp, -sp, -sm*P)                  # E_x^2, E_y^2 at integer z; E_z^2 at z+1/2 -> P
            MB = _diag3(sp*P, -sp*P, -sm)                # B_x^2, B_y^2 at z+1/2 -> P; B_z^2 at integer z
        return ME, MB
    raise ValueError(var)

def pair_W(law, N, n, pol, var, lam=None):
    """sum_pol |amp|^2 and E = w1 + w2 on the R17-9 grid, q = 2 pi n / N along z."""
    k = kgrid(N); s = law.sig(k); c = law.c(k)
    j = np.arange(N); j2 = (n - j - 1) % N; jm = (N - 1 - j)
    out_W = np.empty((N, N, N)); out_E = np.empty((N, N, N))
    Y, Z = np.meshgrid(j, j, indexing='ij')
    for ix in range(N):
        X_ = np.full_like(Y, ix)
        s1 = np.stack([s[X_], s[Y], s[Z]], -1); s2 = np.stack([s[jm[X_]], s[jm[Y]], s[j2[Z]]], -1)
        c1 = np.stack([c[X_], c[Y], c[Z]], -1); c2 = np.stack([c[jm[X_]], c[jm[Y]], c[j2[Z]]], -1)
        ssum = k[Z] + k[j2[Z]]
        ME, MB = vertex(var, pol, c1, c2, ssum, lam)
        w1 = np.sqrt((s1*s1).sum(-1)); w2 = np.sqrt((s2*s2).sum(-1)); rw = np.sqrt(w1*w2)
        Bp = np.einsum('...ji,...jk,...kl->...il', crossmat(s1), MB, crossmat(s2))/rw[..., None, None]
        Nm = 0.5*(rw[..., None, None]*ME + Bp)
        P1 = np.eye(3) - s1[..., :, None]*s1[..., None, :]/(w1*w1)[..., None, None]
        P2 = np.eye(3) - s2[..., :, None]*s2[..., None, :]/(w2*w2)[..., None, None]
        out_W[ix] = np.real(np.einsum('...ij,...jk,...kl,...il->...', P1, Nm, P2, np.conj(Nm)))
        out_E[ix] = w1 + w2
    return out_W, out_E

def xi(law, N, pol, var, shifts=(1, 2), lam=None):
    W0, E0 = pair_W(law, N, 0, pol, var, lam)
    beta = -np.mean(W0/E0**3); Pi0 = -np.mean(W0/E0)
    D = {}
    for n in shifts:
        W, E = pair_W(law, N, n, pol, var, lam); D[n] = -np.mean(W/E) - Pi0
    q1 = 2*np.pi*shifts[0]/N; r = shifts[1]/shifts[0]
    alpha = (r**4*D[shifts[0]] - D[shifts[1]])/((r**4 - r**2)*q1**2)
    return alpha + beta, alpha, beta

# ---------------- forward-scattering (W1 at O(q)) test ----------------
def pols(sig):
    sh = sig/np.linalg.norm(sig)
    a = np.cross(sh, [0.3, 0.7, 0.2]); a /= np.linalg.norm(a); b = np.cross(sh, a)
    return sh, [a, b]

def forward_S(law, kv, pol, var):
    """S_ll' at legs (-k, k) [scattering, q = 0] and the W1-required value -(w/2) e:(vv) delta."""
    kv = np.asarray(kv, float)
    sig = law.sig(kv); sp = law.dpr(kv); w = np.linalg.norm(sig)
    c1 = law.c(-kv); c2 = law.c(kv)                          # legs (-k, k): per-leg symbols (c even)
    ME, MB = vertex(var, pol, c1[None], c2[None], np.array([-kv[2] + kv[2]]))
    ME, MB = ME[0], MB[0]
    sh, ep = pols(sig)
    S = np.zeros((2, 2), complex)
    for a in range(2):
        for b in range(2):
            S[a, b] = 0.5*(w*ep[a] @ ME @ ep[b] + w*np.cross(sh, ep[a]) @ MB @ np.cross(sh, ep[b]))
    v = sig*sp/w
    e = EPOL[pol]
    Sreq = -(w/2)*(v @ e @ v)*np.eye(2)
    return S, Sreq
