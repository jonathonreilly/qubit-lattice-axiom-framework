"""A53 t2_cubeparton: delta = 0 end of the block-modulated parton family, EXACT: the projected pi-flux parton of one
isolated block (dual-frame hops of A51's _parton_h restricted to the block's internal bonds), its overlap with the
block's restricted-rule singlet ground state, and the product energy per site under the rules (inter-block terms
vanish for these tilings; see t2_prod n_inter_terms).  Usage: t2_cubeparton.py L KEY blocks"""
import sys, signal, time, numpy as np
signal.alarm(200)
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from a53lib import *
from a51lib import _parton_h
from t2_prod import lowest_singlets
t0 = time.time(); L, key = int(sys.argv[1]), sys.argv[2]; blocks = [tuple(int(c) for c in b) for b in sys.argv[3].split(",")]
cl = cube(L); h = _parton_h(cl); ks, J, c4 = load_rule(L, key)
for B in blocks:
    loc = [np.array(o) for o in itertools.product(*[range(b) for b in B])]; n = len(loc)
    gi = [cl.idx[tuple(o)] for o in loc]; fo = open_index(loc)
    hb = np.zeros((2 * n, 2 * n), complex)
    for a in range(n):
        for b in range(n):
            if a != b and np.abs(loc[a] - loc[b]).sum() == 1:
                hb[2 * a:2 * a + 2, 2 * b:2 * b + 2] = h[2 * gi[a]:2 * gi[a] + 2, 2 * gi[b]:2 * gi[b] + 2]
    ev, W = np.linalg.eigh(hb); Phi = W[:, :n]; gap = ev[n] - ev[n - 1]
    Sn = Sector(n, flip=False); bits = ((Sn.confs[:, None] >> np.arange(n)[None, :]) & 1)
    amp = np.linalg.det(Phi[2 * np.arange(n)[None, :] + bits]); amp *= np.exp(-1j * np.angle(amp[np.argmax(np.abs(amp))]))
    x = amp.real / np.linalg.norm(amp.real)
    pairs = bilinear_pairs(loc, fo, ks, J); fours = four_sets(loc, fo, c4)
    mv = make_mv_gen(GenHam(pairs, fours, n), Sn); E = x @ mv(x)
    sing, Sr, mvr = lowest_singlets(pairs, fours, n)
    E0, g, _ = sing[0]; gf = np.zeros(1 << n); gf[Sr.confs] = g
    if Sr.flip: gf[(~Sr.confs) & Sr.full] = g
    gf /= np.linalg.norm(gf); ov = (gf[Sn.confs] @ x) ** 2
    C = paircorr(x, Sn)
    print(f"block {B}: block-parton MF gap {gap:.4f}, max|Im| {np.abs(amp.imag).max():.1e}, S check {C.sum()/4:.1e}; "
          f"product E/N {E/n:+.5f} (block GS product {E0/n:+.5f}); |<block GS|block parton>|^2 {ov:.4f}  [{time.time()-t0:.1f}s]")
