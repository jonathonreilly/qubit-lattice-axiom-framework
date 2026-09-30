import sys, time, json, numpy as np
import su3mc as m

def main(Ls, Lt, beta, nth, nmeas, sep, seedv, out, do_wl=True, Rmax=4, Tmax=4, smear=(6, 14), w=0.25, n_or=2):
    dims = (Ls, Ls, Ls, Lt)
    up, dn, coords = m.make_tables(dims)
    V = up.shape[1]
    U = m.cold_start(V)
    m.seed(seedv)
    t0 = time.time()
    for i in range(nth):
        m.sweep(U, up, dn, beta, n_or)
    rec = dict(plaq=[], polyak=[], polyak_abs=[], Wu=[], Ws=[], O=[])
    for k in range(nmeas):
        for i in range(sep):
            m.sweep(U, up, dn, beta, n_or)
        rec['plaq'].append(m.plaquette_avg(U, up))
        P = m.polyakov(U, up, coords, Lt)
        rec['polyak'].append(P.mean())
        rec['polyak_abs'].append(np.abs(P).mean())
        if do_wl:
            Wu = np.zeros((Rmax + 1, Tmax + 1)); cnt = 0
            for mu in range(4):
                for nu in range(mu + 1, 4):
                    Wu += m.wloops(U, up, mu, nu, Rmax, Tmax); cnt += 1
            rec['Wu'].append(Wu / cnt)
            Uc = U; done = 0
            Wlist = []; Olist = []
            for lev in smear:
                Uc = m.ape_smear_spatial(Uc, up, dn, w, lev - done); done = lev
                Ws = np.zeros((Rmax + 1, Tmax + 1))
                for i in range(3):
                    Ws += m.wloops(Uc, up, i, 3, Rmax, Tmax)
                Wlist.append(Ws / 3)
                Olist.append(m.glue_op(Uc, up, Lt, coords))
            rec['Ws'].append(np.array(Wlist)); rec['O'].append(np.array(Olist))
        if (k + 1) % 20 == 0:
            print("meas %d/%d  plaq %.5f  elapsed %.0fs" % (k + 1, nmeas, np.mean(rec['plaq']), time.time() - t0), flush=True)
    np.savez(out, dims=np.array(dims), beta=beta, sep=sep, nth=nth,
             plaq=np.array(rec['plaq']), polyak=np.array(rec['polyak']), polyak_abs=np.array(rec['polyak_abs']),
             Wu=np.array(rec['Wu']), Ws=np.array(rec['Ws']), O=np.array(rec['O']), smear=np.array(smear))
    print("saved", out, "total %.0fs" % (time.time() - t0), flush=True)

if __name__ == "__main__":
    a = sys.argv
    Ls, Lt, beta, nth, nmeas, sep, seedv = int(a[1]), int(a[2]), float(a[3]), int(a[4]), int(a[5]), int(a[6]), int(a[7])
    out = a[8]; do_wl = bool(int(a[9])); Rmax = int(a[10]); Tmax = int(a[11])
    main(Ls, Lt, beta, nth, nmeas, sep, seedv, out, do_wl, Rmax, Tmax)
