"""K2: how surprising is the GJ r_d/delta_d match? Rank of (3,1/3,1) among alphabet triples, several tolerances,
distinct (k2/k1,k3/k2) classes, and a broader/narrower alphabet. Same data as the attack (S4)."""
from common import *
import itertools
g = load_runner(); PARS, _RG = g["PARS"], g["_RG"]
R = _RG(PARS['aS'], PARS['mc'], PARS['mb'], PARS['mt'])
dn = np.array([PARS['md']*R.factor(2.0,162.5), PARS['ms']*R.factor(2.0,162.5), PARS['mb']*R.factor(PARS['mb'],162.5)])
r_d, del_d = rf(dn), delta_lep_convention(dn)
sig_r, sig_d = 0.0075, 0.0045
lep = M_LEP_POLE
def analyse(alph, label):
    rows=[]
    for k in itertools.product(alph, repeat=3):
        m=np.array(k)*lep; rows.append((k, abs(rf(m)-r_d), abs(delta_lep_convention(m)-del_d)))
    n=len(rows)
    gj=[x for x in rows if all(abs(a-b)<1e-9 for a,b in zip(x[0],(3.0,1/3,1.0)))][0]
    # chi2-like joint distance in sigma units
    chi=lambda x: np.hypot(x[1]/sig_r, x[2]/sig_d)
    rank_r=1+sum(1 for x in rows if x[1]<gj[1]-1e-12)
    rank_j=1+sum(1 for x in rows if chi(x)<chi(gj)-1e-12)
    # distinct ratio classes
    cls={}
    for k,dr,dd in rows:
        key=(round(k[1]/k[0],4), round(k[2]/k[1],4)); cls.setdefault(key,(dr,dd))
    ncls=len(cls)
    rank_r_c=1+sum(1 for v in cls.values() if v[0]<gj[1]-1e-12)
    rank_j_c=1+sum(1 for v in cls.values() if np.hypot(v[0]/sig_r,v[1]/sig_d)<chi(gj)-1e-12)
    print("%s: %d triples, %d distinct ratio classes" % (label, n, ncls))
    print("   GJ (3,1/3,1): dr=%.4f (%.2f sigma), ddelta=%.4f (%.2f sigma), joint chi=%.2f" % (gj[1], gj[1]/sig_r, gj[2], gj[2]/sig_d, chi(gj)))
    print("   rank by r-distance: %d of %d triples (%.1f%%) ; %d of %d classes (%.1f%%)" % (rank_r,n,100*rank_r/n,rank_r_c,ncls,100*rank_r_c/ncls))
    print("   rank by joint (r,delta) distance: %d of %d triples (%.1f%%) ; %d of %d classes (%.1f%%)" % (rank_j,n,100*rank_j/n,rank_j_c,ncls,100*rank_j_c/ncls))
    for tol in (0.0075, 0.015, 0.02):
        h=sum(1 for x in rows if x[1]<=tol); hc=sum(1 for v in cls.values() if v[0]<=tol)
        print("   r-hits within %.4f: %d triples (%.1f%%), %d classes (%.1f%%)" % (tol,h,100*h/n,hc,100*hc/ncls))
analyse([1/3,1/2,2/3,1,3/2,2,3], "attack alphabet (7 values)")
analyse([1/3,1,3], "GJ-only alphabet {1/3,1,3}")
analyse([1/9,1/6,1/3,1/2,2/3,1,3/2,2,3,6,9], "wider alphabet (11 values)")
# GUT-scale (SM one-loop) comparison omitted from the attack report
G=np.load('../../attacks/T37_scratch/gut_masses.npy')
print("\nGUT-scale (SM 1-loop, from attack s2): data r_d=%.4f  GJ(GUT leptons) r_d=%.4f  diff=%.4f = %.1f sigma; literal GJ ratios m_b/m_tau=%.3f m_s/m_mu=%.3f m_d/m_e=%.3f (GJ: 1, 0.333, 3)" %
      (rf(G[1]), rf(np.array([3,1/3,1])*G[2]), rf(np.array([3,1/3,1])*G[2])-rf(G[1]), (rf(np.array([3,1/3,1])*G[2])-rf(G[1]))/sig_r, G[1,2]/G[2,2], G[1,1]/G[2,1], G[1,0]/G[2,0]))
