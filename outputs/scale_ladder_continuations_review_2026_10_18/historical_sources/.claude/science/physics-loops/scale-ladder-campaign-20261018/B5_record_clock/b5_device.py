"""B5 reduced one-excitation device (invariant one-head sector) and metrics.

Reduced model of the repo's certified autonomous-output devices
(STRUCTURED_SOURCE_TOLERANCE..., MEDIATED_* notes): in the one-head sector the
old qubits only contribute the literal factor exp(-itK)W, which is untouched by
head-coefficient errors, so it drops out of every metric below.  What remains
is a tight-binding chain:

  D1 (structured critical three-site source):
     s0 -a1- s1 -a2- s2 -kappa- p=lead[0] -g- lead[1] ... lead[M-1] (open end)
     a1 = lam/sqrt3, a2 = lam*sqrt(8/3), kappa = sqrt(3 g lam)   (repo's critical
     comparison coefficients with the background hopping j replaced by g).
  D2 (mediated emitter):  e -gam- [J_m,q,J_m,...,q,J_m] (2n heads) -gam- lead[0] ...
     effective coupling gam^2 r^(n-1)/J_m, r=q/J_m  (repo's bipartite mediator).

All centred onsite energies are 0 (the repo's common 2j carrier is a global
scalar and is removed).  The positive-block implementation P_w=w(I-X) adds the
full-space scalar C(w)=sum_new w_e; its effect is tracked analytically as a
global phase exp(-it C(w)).

Propagation: Chebyshev expansion of exp(-iHt) applied to the seed (exact to
~1e-12 here).  No fitted quantity enters any metric.
"""
import numpy as np
from scipy.special import jv


class Chain:
    """Tridiagonal Hermitian (real symmetric) one-excitation Hamiltonian."""

    def __init__(self, diag, off):
        self.d = np.asarray(diag, float)
        self.o = np.asarray(off, float)  # off[i] couples i,i+1 (sign included)

    def matvec(self, v):
        out = self.d * v
        out[:-1] += self.o * v[1:]
        out[1:] += self.o * v[:-1]
        return out

    def bound(self):
        a = np.abs(self.d).copy()
        a[:-1] += np.abs(self.o)
        a[1:] += np.abs(self.o)
        return a.max()

    def _step(self, psi0, t):
        a = 1.01 * self.bound()
        x = a * t
        K = int(x + 12 * max(x, 1.0) ** (1 / 3) + 60)
        ks = np.arange(K + 1)
        c = jv(ks, x) * (-1j) ** (ks % 4)
        c[1:] *= 2
        T0 = psi0.astype(complex)
        T1 = self.matvec(T0) / a
        acc = c[0] * T0 + c[1] * T1
        for k in range(2, K + 1):
            T2 = 2 * self.matvec(T1) / a - T0
            acc += c[k] * T2
            T0, T1 = T1, T2
        return acc

    def evolve(self, psi0, times):
        """exp(-iHt)psi0 for increasing times, propagated sequentially."""
        out, prev, tp = [], psi0, 0.0
        for t in times:
            prev = self._step(prev, t - tp) if t > tp else prev.astype(complex)
            tp = t
            out.append(prev)
        return out


def d1_chain(lam, M, g=1.0, eps_src=None, xi_src=None, eps_lead=None, xi_lead=None,
             xi_all=0.0):
    """D1 one-head chain.  Index 0..2 = s0,s1,s2 ; 3.. = lead (lead[0]=port p)."""
    n = 3 + M
    bonds = np.empty(n - 1)
    src = np.array([lam / np.sqrt(3), lam * np.sqrt(8 / 3), np.sqrt(3 * g * lam)])
    if eps_src is not None:
        src = src * (1 + eps_src)
    bonds[:3] = -src
    lead = np.full(M - 1, g)
    if eps_lead is not None:
        lead = lead * (1 + eps_lead)
    bonds[3:] = -lead
    diag = np.zeros(n) + xi_all
    if xi_src is not None:
        diag[:3] += xi_src
    if xi_lead is not None:
        diag[3:] += xi_lead
    seed = np.zeros(n); seed[0] = 1.0
    return Chain(diag, bonds), seed, src


def d2_chain(n_cells, gam, Jm, q, g, M, eps_med=None, xi_med=None, xi_e=0.0):
    """D2: emitter, 2n mediator heads, lead of M sites. Bonds: gam, Jm,q,...,Jm, gam, g..."""
    nm = 2 * n_cells
    inner = [Jm if i % 2 == 0 else q for i in range(nm - 1)]
    medb = np.array([gam] + inner + [gam])          # 2n+1 new bonds
    if eps_med is not None:
        medb = medb * (1 + eps_med)
    n = 1 + nm + M
    bonds = np.concatenate([-medb, -np.full(M - 1, g)])
    diag = np.zeros(n)
    diag[0] = xi_e
    if xi_med is not None:
        diag[1:1 + nm] += xi_med
    seed = np.zeros(n); seed[0] = 1.0
    return Chain(diag, bonds), seed, medb


# ---------------------------------------------------------------- metrics
def m_vec(psi, phi):
    """complete vector metric ||psi-phi|| (literal phase)."""
    return np.linalg.norm(psi - phi)


def m_pop(psi, phi):
    """probability-only: total-variation distance of site populations."""
    return 0.5 * np.abs(np.abs(psi) ** 2 - np.abs(phi) ** 2).sum()


def m_gp(psi, phi):
    """co-located phase reference: min over a global phase (computed without cancellation)."""
    ov = np.vdot(phi, psi)
    ph = ov / abs(ov) if abs(ov) > 0 else 1.0
    return np.linalg.norm(psi - ph * phi)
