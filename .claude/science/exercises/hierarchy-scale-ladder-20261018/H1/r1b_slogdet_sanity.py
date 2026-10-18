"""R1b: sanity of R1(iii) slogdet values (macOS Accelerate emits spurious FP warnings)."""
import warnings, numpy as np, importlib.util, sys
spec = importlib.util.spec_from_file_location("r1", "r1_species_invariants.py")
src = open("r1_species_invariants.py").read()
ns = {}
exec(src.split("# ---------------------------------------------------------------- (iii)")[1].split("for Ls, Lt in")[0], {"np": np, "itertools": __import__("itertools")}, ns)
stag_D = ns["stag_D"]
for Ls, Lt in ((2, 2), (2, 4), (4, 4)):
    D, N = stag_D(Ls, Lt, 1.0)
    with warnings.catch_warnings():
        warnings.simplefilter("error")
        try:
            s, l = np.linalg.slogdet(D)
            warned = False
        except Exception as e:
            warned = repr(e)
            s, l = None, None
    ev = np.linalg.eigvals(D)
    l_eig = np.sum(np.log(np.abs(ev)))
    print(Ls, Lt, N, "slogdet", s, l, "sum log|eig|", l_eig, "min|eig|", np.abs(ev).min(), "warning-as-error:", warned,
          "antisym", np.allclose(D, -D.T))
