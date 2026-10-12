"""R3-1 check 5b: raw lattice sums of kernels spread over proper time (all lattice points with
-48 <= d^2 <= -1, future sheet), S_f(u,kappa) = sum_d f(d^2) exp(-kappa w(u,d)), for
 (i) sharp f = 1 on [-48,-1];  (ii) smooth f(N) = exp(-((|N|-24)/8)^2);  (iii) single shell N=-3 (reference).
Relative LV = std_u(S_f)/mean_u(S_f), 48 directions with rapidity <= 0.7.  Poisson/Bragg-gap argument
(suggested): smooth f on a scale l_k suppresses the tube LV super-polynomially in l_k*sqrt(c)."""
import numpy as np, importlib.util
spec = importlib.util.spec_from_file_location("s", "r31_lv_scaling_lib.py")
lib = importlib.util.module_from_spec(spec); spec.loader.exec_module(lib)
rng = np.random.default_rng(5)
us = np.array([lib.boost(0.7 * rng.uniform() ** (1/3), rng.normal(size=3)) for _ in range(48)])
kaps = [0.4, 0.2, 0.1, 0.07, 0.05]
n0max = 520
Ns = list(range(-1, -49, -1))
raw = {k: {} for k in kaps}
for N in Ns:
    X = lib.shell(N, n0max)
    if len(X[0]) == 0: continue
    W = np.outer(us[:, 0], X[0]) if False else None
    for k in kaps:
        raw[k][N] = np.array([np.exp(-k * (u[0] * X[0] - u[1] * X[1] - u[2] * X[2] - u[3] * X[3])).sum() for u in us])
print("shells used:", len(raw[kaps[0]]), " margin at kappa=0.05:", round(0.05 * np.exp(-0.7) * np.sqrt(7) * n0max, 1))
fs = {"sharp [-48,-1]": lambda N: 1.0, "smooth gauss(|N|-24, 8)": lambda N: np.exp(-((abs(N) - 24) / 8.0) ** 2),
      "smooth gauss(|N|-24, 12)": lambda N: np.exp(-((abs(N) - 24) / 12.0) ** 2), "single N=-3": lambda N: 1.0 if N == -3 else 0.0}
for name, f in fs.items():
    out = []
    for k in kaps:
        S = sum(f(N) * v for N, v in raw[k].items())
        out.append(S.std() / S.mean())
    sl = np.polyfit(np.log(kaps), np.log(out), 1)[0]
    print(f"{name:26s}: rel LV at kappa {kaps} = {[f'{x:.2e}' for x in out]}  (log-slope {sl:.2f})")
