import numpy as np, glob, json, math, sys, os
here = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, here)
from ana import load, stat

LIC = 0.5934
groups = {}
for fn in sorted(glob.glob(here + '/runs/*.txt')):
    b = os.path.basename(fn)
    P, W, hdr = load(fn)
    if len(P) < 200: continue
    mode = 'met' if b.startswith('met') else 'hb'
    L = int(b.split('_L')[1].split('_')[0].split('.')[0])
    # drop first 100 sweeps of production as extra thermalization for the short-therm runs
    cut = 100 if L >= 12 else 0
    m, e, t = stat(P[cut:])
    groups.setdefault((mode, L), []).append((b, m, e, t, len(P) - cut))

out = {}
print('%-6s %-3s %-16s %10s %9s %6s %7s' % ('algo', 'L', 'file', 'P', 'err', 'tau', 'n'))
for key in sorted(groups):
    ch = groups[key]
    for b, m, e, t, n in ch:
        print('%-6s %-3d %-16s %10.6f %9.6f %6.2f %7d' % (key[0], key[1], b, m, e, t, n))
    w = np.array([1 / c[2] ** 2 for c in ch]); mm = np.array([c[1] for c in ch])
    mean = (w * mm).sum() / w.sum(); err = 1 / math.sqrt(w.sum()); chi2 = float((w * (mm - mean) ** 2).sum())
    print('   -> combined %s L=%d: P = %.6f +/- %.6f   chi2/dof = %.2f/%d' % (key[0], key[1], mean, err, chi2, len(ch) - 1))
    out['%s_L%d' % key] = dict(P=mean, err=err, chi2=chi2, nchain=len(ch))

# gates
def diff(a, b):
    return (a['P'] - b['P']), math.hypot(a['err'], b['err'])
if 'hb_L4' in out or True:
    pass
res = {}
if 'hb_L6' in out and 'met_L6' in out:
    d, s = diff(out['hb_L6'], out['met_L6']); res['G1_L6_HB_minus_Met'] = (d, s, abs(d) / s)
if 'hb_L4' in out and 'met_L4' in out:
    d, s = diff(out['hb_L4'], out['met_L4']); res['G1_L4_HB_minus_Met'] = (d, s, abs(d) / s)
# L=8 cold vs hot
c8 = [c for c in groups.get(('hb', 8), [])]
if len(c8) == 2:
    d = c8[0][1] - c8[1][1]; s = math.hypot(c8[0][2], c8[1][2]); res['G2_L8_cold_minus_hot'] = (d, s, abs(d) / s)
# L=4 vs earlier codes
if 'hb_L4' in out:
    for name, val, er in (('repo smoke L4 0.59601(78)', 0.59601, 0.00078), ('probe T31 L4 0.5970(4)', 0.5970, 0.0004)):
        d = out['hb_L4']['P'] - val; s = math.hypot(out['hb_L4']['err'], er); res['G3_' + name] = (d, s, abs(d) / s)
print('\nGates (diff, sigma, |diff|/sigma):')
for k, v in res.items(): print('  %-40s %+.2e  %.2e  %.2f' % ((k,) + v))

# large-volume estimate
big = [(k, out[k]) for k in ('hb_L12', 'hb_L16') if k in out]
repo = json.load(open(here + '/repo_ensembles_result.json'))
print('\nP by volume (HB+OR):', {k: (round(v['P'], 6), round(v['err'], 6)) for k, v in out.items() if k.startswith('hb')})
if len(big) == 2:
    w = np.array([1 / v['err'] ** 2 for k, v in big]); mm = np.array([v['P'] for k, v in big])
    mean = (w * mm).sum() / w.sum(); err = 1 / math.sqrt(w.sum())
    fv = abs(big[0][1]['P'] - big[1][1]['P'])
    print('combined L=12,16: %.6f +/- %.6f (stat)  |P12-P16| = %.2e' % (mean, err, fv))
    # combine with repo's independent 3 ensembles
    w2 = np.array([1 / err ** 2, 1 / repo['err'] ** 2]); m2 = np.array([mean, repo['mean']])
    mean2 = (w2 * m2).sum() / w2.sum(); err2 = 1 / math.sqrt(w2.sum())
    print('combined with repo 2026-04-30 ensembles (%.6f +/- %.6f): %.6f +/- %.6f' % (repo['mean'], repo['err'], mean2, err2))
    Pinf, sig_stat = mean, err
    sig_tot = math.sqrt(sig_stat ** 2 + (fv / 2) ** 2)
    d = Pinf - LIC
    print('P_inf(mine, L=12,16) = %.6f, sigma_tot(stat+FV/2) = %.6f, d = %.2e = %.1f sigma_tot' % (Pinf, sig_tot, d, d / sig_tot))
    band = 'A' if abs(d) <= 5e-5 else ('C' if abs(d) <= 1e-4 else 'D')
    print('repo band (point estimate):', band, '; decisive at 2 sigma:', abs(d) - 2 * sig_tot > 1e-4)
    abare = 1 / (4 * math.pi); Mpl = 1.2209e19
    v = lambda P: Mpl * (7 / 8) ** 0.25 * (abare / P ** 0.25) ** 16
    print('v_cand(0.5934)=%.3f  v_cand(P_inf)=%.3f  shift %.3f%%; observed 246.22 -> licensed residual %.3f%%, corrected residual %.3f%%' % (
        v(LIC), v(Pinf), 100 * (v(Pinf) / v(LIC) - 1), 100 * (v(LIC) / 246.2197 - 1), 100 * (v(Pinf) / 246.2197 - 1)))
    print('alpha_s(v)= %.6f -> %.6f ; u0 %.6f -> %.6f' % (abare / LIC ** 0.5, abare / Pinf ** 0.5, LIC ** 0.25, Pinf ** 0.25))
    out['summary'] = dict(P_inf=Pinf, sig_stat=sig_stat, fv=fv, sig_tot=sig_tot, d=d, band=band, gates=res, repo=repo)
json.dump(out, open(here + '/final_result.json', 'w'), indent=1, default=float)

# protocol step 6: P_L = P_inf + c L^-4 (weighted LSQ) over available HB volumes L>=6
Ls = [L for L in (6, 8, 12, 16) if 'hb_L%d' % L in out]
if len(Ls) >= 3:
    for pw in (4, 2):
        x = np.array([L ** (-float(pw)) for L in Ls]); y = np.array([out['hb_L%d' % L]['P'] for L in Ls]); s = np.array([out['hb_L%d' % L]['err'] for L in Ls])
        A = np.vstack([np.ones_like(x), x]).T / s[:, None]; b = y / s
        coef, *_ = np.linalg.lstsq(A, b, rcond=None); cov = np.linalg.inv(A.T @ A)
        chi2 = float(np.sum((A @ coef - b) ** 2))
        print('fit P_L = P_inf + c L^-%d over L=%s: P_inf = %.6f +/- %.6f, c=%.3f, chi2/dof = %.1f/%d' % (pw, Ls, coef[0], math.sqrt(cov[0, 0]), coef[1], chi2, len(Ls) - 2))
