"""Targeted check: in variant A, P(excitation never recorded) = |<uniform|psi0>|^2 (exact claim)."""
import os, sys
for v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "VECLIB_MAXIMUM_THREADS", "MKL_NUM_THREADS"):
    os.environ[v] = "1"
src = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "magnon_toy.py")).read()
exec(src.split("# exact checks")[0])
import numpy as np
rng.bit_generator.state = np.random.default_rng(99).bit_generator.state
NT = int(sys.argv[1]) if len(sys.argv) > 1 else 900
x0 = N // 2
uni = np.ones(N) / np.sqrt(N)
for k, sig in ((0.3, 3.0), (0.0, 6.0)):
    v = np.exp(1j * k * np.arange(N) - (np.arange(N) - x0) ** 2 / (2 * sig ** 2)); psi0 = v / np.linalg.norm(v)
    dark = abs(np.vdot(uni, psi0)) ** 2
    never = sum(run(psi0, "A")[5] for _ in range(NT))
    sd = np.sqrt(NT * dark * (1 - dark))
    print(f"packet k={k} width={sig}: never recorded {never}/{NT}; predicted {dark*NT:.1f} +- {sd:.1f} "
          f"(z = {(never - dark*NT)/sd:+.2f})")
