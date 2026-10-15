"""OBS-2 archive: symmetrised one-loop corner tensors I_ss'(c) (dv_a per y_s y_s') at N = 48, 64, 96 for every (m0, Delta, vertex),
the M2 flavon vectors, and the T2g check numbers, into obs2_archive.npz (reproduces sizes2*.out)."""
import sys, json, numpy as np
sys.argv = ['x']; exec(open('sizes2.py').read().split("if __name__")[0])
arr = {}
for N in (48, 64, 96):
    for m in ('0.1', '0.05', '0.025'):
        for D in ('0.0', '0.5'):
            for var in ('sym', 'int', 'ext'):
                I = loadI(N, m, D, var)
                for c in 'xyz':
                    for k, vv in I[c].items():
                        arr[f"I_N{N}_m{m}_D{D}_{var}_corner{c}_pair{k}"] = vv
            f = json.load(open(f"yuk_flav_N{N}_m{m}_D{D}_mH{m}.json"))
            for kk, vv in f.items():
                arr[f"flav_N{N}_m{m}_D{D}_{kk}"] = np.array(vv['dv'])
for fn in ('yuk_strain_N48_m0.1_D0.5_mH0.1.json', 'yuk_strain_N32_m0.1_D0.0_mH0.1.json'):
    s = json.load(open(fn))
    for q, vv in s.items():
        arr[f"strain_{fn[10:-5]}_{q}"] = np.array([vv['base']] + [vv['d'][l] for l in ('xx', 'yy', 'zz', 'xy', 'yz', 'zx')])
np.savez_compressed('obs2_archive.npz', **arr)
print(len(arr), 'arrays saved')
