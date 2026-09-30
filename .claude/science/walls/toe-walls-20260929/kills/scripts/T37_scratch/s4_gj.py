"""S4: Georgi-Jarlskog-type integer Clebsch link between the lepton and down-type triples."""
from common import *
import itertools
g = load_runner(); PARS, _RG, _sector_dials = g["PARS"], g["_RG"], g["_sector_dials"]
R = _RG(PARS['aS'], PARS['mc'], PARS['mb'], PARS['mt'])
dn = np.array([PARS['md']*R.factor(2.0,162.5), PARS['ms']*R.factor(2.0,162.5), PARS['mb']*R.factor(PARS['mb'],162.5)])
up = np.array([PARS['mu']*R.factor(2.0,162.5), PARS['mc']*R.factor(PARS['mc'],162.5), PARS['mt']*R.factor(PARS['mt'],162.5)])
r_d, r_u = rf(dn), rf(up); del_d, del_u = delta_lep_convention(dn), delta_lep_convention(up)
print("DATA (common scale): r_d=%.4f delta_d=%.4f | r_u=%.4f delta_u=%.4f" % (r_d, del_d, r_u, del_u))
lep = M_LEP_POLE
gj = np.array([3.0, 1/3, 1.0])*lep      # m_d = 3 m_e, m_s = m_mu/3, m_b = m_tau (common scale free)
print("GJ from lepton POLE masses: down triple ratios m_b/m_s=%.2f (data %.2f), m_s/m_d=%.2f (data %.2f)" % (gj[2]/gj[1], dn[2]/dn[1], gj[1]/gj[0], dn[1]/dn[0]))
print("   r_d^GJ=%.4f (data %.4f, diff %+.4f)  delta_d^GJ=%.4f (data %.4f, diff %+.4f)" % (rf(gj), r_d, rf(gj)-r_d, delta_lep_convention(gj), del_d, delta_lep_convention(gj)-del_d))
# error bar on data r_d is 0.0075 (propagated inputs); delta_d propagated error via MC
rng = np.random.default_rng(5)
PERR = dict(aS=0.0009, mu=0.38e-3, md=0.33e-3, ms=6.0e-3, mc=0.02, mb=0.025, mt=1.8)
rs=[]; ds=[]
for _ in range(4000):
    p = {k: rng.normal(PARS[k], PERR[k]) for k in PERR}
    if min(p.values())<=0: continue
    Rr = _RG(p['aS'], p['mc'], p['mb'], p['mt'])
    d = np.array([p['md']*Rr.factor(2.0,162.5), p['ms']*Rr.factor(2.0,162.5), p['mb']*Rr.factor(p['mb'],162.5)])
    rs.append(rf(d)); ds.append(delta_lep_convention(d))
print("MC data errors: r_d = %.4f +- %.4f ; delta_d = %.4f +- %.4f" % (np.mean(rs), np.std(rs), np.mean(ds), np.std(ds)))
print("   r_d^GJ - r_d = %+.1f sigma ; delta_d^GJ - delta_d = %+.1f sigma" % ((rf(gj)-r_d)/np.std(rs), (delta_lep_convention(gj)-del_d)/np.std(ds)))
# with SM-run six masses at 2e16 GeV (from s2)
G = np.load("gut_masses.npy")    # rows: up, down, lep at 2e16 (GeV)
print("SM one-loop masses at 2e16 GeV:  m_b/m_tau=%.3f (GJ 1), m_s/m_mu=%.3f (GJ 1/3), m_d/m_e=%.3f (GJ 3)" % (G[1,2]/G[2,2], G[1,1]/G[2,1], G[1,0]/G[2,0]))
gj_gut = np.array([3.0, 1/3, 1.0])*G[2]
print("   GUT-scale r_d(data run up)=%.4f delta_d=%.4f ; r_d^GJ(GUT leptons)=%.4f delta=%.4f" % (rf(G[1]), delta_lep_convention(G[1]), rf(gj_gut), delta_lep_convention(gj_gut)))
# look-elsewhere: 343 triples
alph = [1/3, 1/2, 2/3, 1, 3/2, 2, 3]
hits=[]; hits2=[]
for k in itertools.product(alph, repeat=3):
    m = np.array(k)*lep
    rr = rf(m)
    if abs(rr - r_d) <= 0.02:
        hits.append(k)
        if abs(delta_lep_convention(m)-del_d) <= 0.05: hits2.append(k)
print("look-elsewhere over %d triples: %d within 0.02 in r_d (%.1f%%); %d also within 0.05 rad in delta_d (%.1f%%)" % (len(alph)**3, len(hits), 100*len(hits)/343, len(hits2), 100*len(hits2)/343))
print("   r_d hits:", [tuple(round(x,3) for x in h) for h in hits][:40])
print("   r_d & delta_d hits:", [tuple(round(x,3) for x in h) for h in hits2])
# distinct ratio classes: r depends on (k2/k1, k3/k2) only
cls=set()
for h in hits2: cls.add((round(h[1]/h[0],3), round(h[2]/h[1],3)))
print("   distinct (k2/k1, k3/k2) classes among joint hits:", sorted(cls))
# the same alphabet applied to the UP sector with lepton triple as partner (no physical motivation; trial-factor control)
ups=[k for k in itertools.product(alph, repeat=3) if abs(rf(np.array(k)*lep)-r_u) <= 0.02]
print("control: triples within 0.02 of r_u: %d (max r reachable over alphabet = %.3f)" % (len(ups), max(rf(np.array(k)*lep) for k in itertools.product(alph, repeat=3))))
# cheap null: how often does a random log-uniform Clebsch triple in [1/3,3]^3 land within 0.02 of r_d?
kk = np.exp(rng.uniform(np.log(1/3), np.log(3), size=(200000,3))); mm = kk*lep[None,:]
Q = mm.sum(1)/np.sqrt(mm).sum(1)**2; rr = (3*Q-1)/2
print("null (log-uniform k in [1/3,3]^3): P(|r-r_d|<=0.02) = %.3f ; P(|r-r_u|<=0.02) = %.4f" % (np.mean(abs(rr-r_d)<=0.02), np.mean(abs(rr-r_u)<=0.02)))
