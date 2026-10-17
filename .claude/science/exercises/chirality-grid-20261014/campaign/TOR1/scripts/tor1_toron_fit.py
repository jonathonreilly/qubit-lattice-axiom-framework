"""TOR-1 (b3): exponential fit of the toron-connection size (spread of Gam_t) vs L on square tori."""
import numpy as np
r = np.load('toron_scaling_4_6_8_10_12_4x8.npy')
for model, isL1 in (('11112', 0), ('L1', 1)):
    m = (r[:, 2] == isL1) & (r[:, 0] == r[:, 1])
    L = r[m, 0]; s = r[m, 7]
    A = np.vstack([L, np.ones_like(L)]).T; c, *_ = np.linalg.lstsq(A, np.log(s), rcond=None)
    res = np.log(s) - A @ c; s2 = res @ res / (len(L) - 2); se = np.sqrt(s2 * np.linalg.inv(A.T @ A)[0, 0])
    print(f"{model}: L {L.astype(int).tolist()} spread {np.array2string(s, precision=4)} -> rate {-c[0]:.4f} +- {se:.4f} per site ({-c[0]/se:.0f} sigma); "
          f"max |S_t| = spread/2pi at L=4: {s[0]/(2*np.pi):.3f}; windings {r[m,3].round(6).tolist()}")
