"""OBS-2: (1) N-convergence of the headline branch-B residuals (M1, primary combo, N = 48, 64, 96);
(2) comparator M2: off-diagonal corner entries carried by covariant flavon couplings (tau_x sigma_c, scalar light at Q_cc'),
coupling y_cc' = M_cc'/v (flavon vev set equal to v: a normalisation CHOICE), loop vectors from yuk_flav_N96_*.json."""
import sys, json, numpy as np
sys.argv = ['x']; exec(open('sizes2.py').read().split("if __name__")[0])
print("(1) N-convergence, branch B, trace and selective, low-scale couplings, m0 = 0.025, Delta = 0.5, sym:")
for split in ('trace', 'selective'):
    for N in (48, 64, 96):
        r = run(loadI(N, '0.025', '0.5', 'sym'), 'B', split, 1.0, 1.0)[0]
        print(f"   {split:9s} N={N}: d cTT {r['d']['cTT']:+.4e}  d aniso {max(r['d']['can'], r['d']['dan']):.4e}  u aniso {max(r['u']['can'], r['u']['dan']):.4e}  s cTT {r['s']['cTT']:+.4e}  e aniso {max(r['e']['can'], r['e']['dan']):.1e}")
print("(2) comparator M2 (covariant flavon couplings for off-diagonal entries):")
def flavvec(N, m, D):
    f = json.load(open(f"yuk_flav_N{N}_m{m}_D{D}_mH{m}.json"))
    dv = np.array(f['Qxy_sigma_c']['dv'])      # at corner x for pair (x,y): own axis x, partner axis y, third z
    return dv[0], dv[1], dv[2]
CI_ = {'x': 0, 'y': 1, 'z': 2}
def pair_T(M, own_par_third):
    own, partner, third = own_par_third
    T = {}
    for c in 'xyz':
        vec = np.zeros(3)
        for c2 in 'xyz':
            if c2 == c: continue
            y2 = abs(M[CI_[c], CI_[c2]] / v)**2
            t = [x for x in 'xyz' if x not in (c, c2)][0]
            w = np.zeros(3); w[CI_[c]] = own; w[CI_[c2]] = partner; w[CI_[t]] = third
            vec += y2 * w
        T[c] = vec
    return T
for (m, D) in (('0.025', '0.5'), ('0.1', '0.5'), ('0.025', '0.0')):
    opt = flavvec(96, m, D)
    for bname in ('B', 'A', "B'"):
        Uu, Ud, Ue, Un = branches[bname]
        Ms = {'u': Uu @ np.diag(mu_q) @ Uu.conj().T, 'd': Ud @ np.diag(md_q) @ Ud.conj().T, 'e': Ue @ np.diag(me_l) @ Ue.conj().T}
        Ts = {s: pair_T(Ms[s], opt) for s in Ms}
        fields = {'Q': {c: Ts['u'][c] + Ts['d'][c] for c in 'xyz'}, 'uc': {c: 2 * Ts['u'][c] for c in 'xyz'}, 'dc': {c: 2 * Ts['d'][c] for c in 'xyz'},
                  'L': Ts['e'], 'ec': {c: 2 * Ts['e'][c] for c in 'xyz'}}
        sp = {f: split_univ(fields[f]) for f in fields}
        line = []
        for sec, (Lf, Rf, U) in {'u': ('Q', 'uc', Uu), 'd': ('Q', 'dc', Ud), 'e': ('L', 'ec', Ue)}.items():
            dL = eig_dv(U, sp[Lf][2]); dR = eig_dv(U, sp[Rf][2])
            for i, nm in enumerate(NAMES[sec]):
                dvV = (dL[i] + dR[i]) / 2; dvA = (dL[i] - dR[i]) / 2
                line.append(f"{nm} cTT {-0.75*dvV.mean():+.1e} an {max(np.abs(dvV-dvV.mean()).max(), np.abs(dvA-dvA.mean()).max()):.1e}")
        print(f"   m0={m} D={D} branch {bname:2s}: " + "; ".join(line))
