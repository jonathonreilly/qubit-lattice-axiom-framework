#!/usr/bin/env python3
"""GUIDE analysis (row 918): G(t) - (t/T) G(T) = int_0^beta [Nc_t P_t - (t/T) Nc_T P_T] db' from ti.py logs.
Usage: ana_ti.py prefix T shapes(comma, e.g. 4x4x4) times(comma) betas_out(comma)
Log files: out/<prefix>_<t>_<shape>.log  (periodic: prefix=ti and shape given as the side b, file ti_<t>_<b>.log)
Trapezoid on the grid with the point (0, 0) added. Errors: quadrature of independent per-point errors.
Also prints d_beta G(t) = Nc_t P_t - (t/T) Nc_T P_T at each output beta, split into temporal and spatial parts.
"""
import sys, json
import numpy as np

def load(fn):
    rows = [json.loads(l) for l in open(fn) if l.startswith('{')]
    return rows

def integ(bs, f, df, bout):
    bs = np.concatenate([[0.0], bs]); f = np.concatenate([[0.0], f]); df = np.concatenate([[0.0], df])
    k = int(np.nonzero(np.isclose(bs, bout))[0][0])
    h = np.diff(bs[:k+1])
    val = (0.5*h*(f[:k] + f[1:k+1])).sum()
    w = np.zeros(k+1); w[:k] += 0.5*h; w[1:k+1] += 0.5*h
    err = np.sqrt(((w*df[:k+1])**2).sum())
    return val, err

prefix, T = sys.argv[1], int(sys.argv[2])
shapes = sys.argv[3].split(','); times = [int(x) for x in sys.argv[4].split(',')]
bouts = [float(x) for x in sys.argv[5].split(',')]
res = {}
for sh in shapes:
    ref = load(f"out/{prefix}_{T}_{sh}.log")
    bs = np.array([r['beta'] for r in ref])
    for t in times:
        try: rows = load(f"out/{prefix}_{t}_{sh}.log")
        except FileNotFoundError: continue
        if len(rows) != len(ref): print('incomplete', sh, t); continue
        f = np.array([r['Nc']*r['P'] - (t/T)*q['Nc']*q['P'] for r, q in zip(rows, ref)])
        df = np.array([np.hypot(r['Nc']*r['dP'], (t/T)*q['Nc']*q['dP']) for r, q in zip(rows, ref)])
        ft = np.array([r['Nt']*r['Pt'] - (t/T)*q['Nt']*q['Pt'] for r, q in zip(rows, ref)])
        fs = np.array([r['Ns']*r['Ps'] - (t/T)*q['Ns']*q['Ps'] for r, q in zip(rows, ref)])
        dft = np.array([np.hypot(r['Nt']*r['dPt'], (t/T)*q['Nt']*q['dPt']) for r, q in zip(rows, ref)])
        dfs = np.array([np.hypot(r['Ns']*r['dPs'], (t/T)*q['Ns']*q['dPs']) for r, q in zip(rows, ref)])
        for bo in bouts:
            G, dG = integ(bs, f, df, bo)
            k = int(np.nonzero(np.isclose(bs, bo))[0][0])
            out = dict(shape=sh, t=t, T=T, beta=bo, G=round(G, 4), dG=round(dG, 4),
                       dbG=round(f[k], 3), ddbG=round(df[k], 3), dbG_t=round(ft[k], 3), dbG_s=round(fs[k], 3),
                       err_t=round(dft[k], 3), err_s=round(dfs[k], 3))
            print(json.dumps(out))
