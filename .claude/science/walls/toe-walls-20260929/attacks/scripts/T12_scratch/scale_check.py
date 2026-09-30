import sys, json, time
import numpy as np
sys.argv = ["x"]
import interval_exponent as ie

def binned(res, factor=1.3):
    hs = sorted(res)
    bins = {}
    for h in hs:
        b = int(np.floor(np.log(h) / np.log(factor)))
        bins.setdefault(b, []).extend(res[h])
    xs, ys = [], []
    for b in sorted(bins):
        hh = [h for h in hs if int(np.floor(np.log(h)/np.log(factor))) == b]
        xs.append(np.exp(np.mean(np.log(hh)))); ys.append(max(bins[b]))
    return np.array(xs), np.array(ys)

def local_slopes(x, y):
    lx, ly = np.log(x), np.log(y)
    n = len(x)
    out = []
    for lo, hi in ((0, n//3), (n//3, 2*n//3), (2*n//3, n)):
        if hi - lo >= 3:
            out.append(float(np.polyfit(lx[lo:hi], ly[lo:hi], 1)[0]))
        else:
            out.append(None)
    return out, float(np.polyfit(lx, ly, 1)[0])

results = {}
def run(name, preds, site, L, nys):
    t0 = time.time()
    res = ie.run_turnover(preds, site, L, None, None, nys)
    x, y = binned(res)
    sl, allp = local_slopes(x, y)
    results[name] = dict(h_bins=[float(v) for v in x], maxN=[float(v) for v in y], slopes_thirds=sl, p_all=allp,
                         ratio_to_B3=[float(a/ie.B3(b)) for a, b in zip(y, x)])
    print(name, "slopes(thirds)=", [None if s is None else round(s,2) for s in sl], "p_all=", round(allp,2),
          "h range", round(x[0],1), round(x[-1],1), "ratio_B3 first/last", round(results[name]['ratio_to_B3'][0],4), round(results[name]['ratio_to_B3'][-1],4),
          "time", round(time.time()-t0,1), flush=True)

# E6 calibration at larger size
p, s = ie.sync_lightcone(48, 60); run("E6_sync_L48_T60", p, s, 48, 3)
# E4 async CA: two sizes to check wrap-around sensitivity
p, s = ie.sim_async_ca(44, 44**3*24, 11); run("E4_L44_T24", p, s, 44, 5)
p, s = ie.sim_async_ca(64, 64**3*24, 12); run("E4_L64_T24", p, s, 64, 4)
p, s = ie.sim_async_ca(56, 56**3*40, 13); run("E4_L56_T40", p, s, 56, 3)
# E5 SSEP
for rho, T in ((0.5, 150), (0.2, 300)):
    L = 56
    p, s = ie.sim_ssep(L, rho, int(rho*L**3*T), 7); run("E5_rho%.1f_L56_T%d" % (rho, T), p, s, L, 3)
json.dump(results, open("scale_check_results.json", "w"), indent=1)
