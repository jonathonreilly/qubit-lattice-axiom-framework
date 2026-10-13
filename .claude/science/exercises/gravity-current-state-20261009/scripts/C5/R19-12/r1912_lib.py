"""R19-12 library: the charge block on the gravity root's edges.
Imports R16-10's Theorem-L split evaluator and law adapters, R16-2's photon moments (R10-1 Theorem D / T'),
and R18-5's photon profile, all UNMODIFIED from ../arch/ (copies of P/scripts/C5/{R16-10,R16-2,R18-5}).
Units: F, G printed per e^2 x 16 pi^2 (physical shift = u * value, u = e^2/16pi^2 = alpha/4pi = 5.807e-4)."""
import os, sys, numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)); A = os.path.join(HERE, '..', 'arch')
sys.path.insert(0, os.path.join(A, 'R16-10')); sys.path.insert(1, os.path.join(A, 'R16-10', 'arch', 'R16-2'))
from r1610_eval import lattice_part, K, U
from r1610_laws import photon, scalar_G, dirac_D1
_cwd = os.getcwd(); os.chdir(os.path.join(A, 'R16-10', 'arch', 'R16-2'))
import r162_scalar, r162_laws
from r101_dirac_moment_copy import moment
os.chdir(_cwd)
sys.path.insert(0, os.path.join(A, 'R18-5'))
import photon as ph185
from sublum import sstep

u_phys = 1/137.035999/(4*np.pi)          # alpha/4pi (RECALLED alpha), = 5.807e-4

# Gravity-root edges (R18-9 refined root, vR18-9:11; stored in arch/R18-13/root_refR18-9.npy)
ROOT = dict(bs=2.526103698477, bf=0.909103707957, r=0.555604225797, a=-0.176095005436, bg=2.9435, fw=1.0)

def photon_Gw(b, w):
    """gamma G_w(b, w) as an odd d(q) callable (R18-5 photon.py PhotonProfile, unmodified)."""
    pr = ph185.photonGw(b, w)
    return lambda q: pr.sig(np.asarray(q, float)), pr

def radii(box, choice=0):
    if choice == 0:
        r1 = min(0.75*box, 0.9); r0 = 0.35*r1          # R16-10 scan's rule (r1610_scan.py)
    else:
        r1 = min(0.55*box, 0.6); r0 = 0.25*r1          # alternative radii (split-independence check)
    return r0, r1

def F_dirac(bf, r, d, cbox, N, m=1e-6, lam=0.0, choice=0, h=0.02):
    r0, r1 = radii(min(bf, cbox), choice)
    lp, tp = lattice_part(0.5, N, m, lam, dirac_D1(bf, r), d, r0, r1, h=h)
    return K[0.5] + lp, tp

def F_scalar(bs, d, cbox, N, m=0.0, lam=0.0, choice=0, h=0.02):
    r0, r1 = radii(min(bs, cbox), choice)
    lp, tp = lattice_part(0, N, m, lam, scalar_G(bs), d, r0, r1, h=h)
    return K[0] + lp, tp

def G_dirac(bf, r, m, N):
    return moment(r162_laws.D1Law(bf, r, 1.0, 2.0, m), N)['tot']      # photon symbol irrelevant (Lemma Q)

def G_scalar(bs, m, N):
    return r162_scalar.photon_moment(r162_laws.GScal(bs, 1.0, 2.0, m), N)
