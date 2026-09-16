"""Resolution diagnostic after the actual BLOCK07 radial-kernel failure."""
from hashlib import sha256
from pathlib import Path
import importlib.util
import json

from scipy.special import ive, i0e

p = Path(__file__).with_name("block07_positive_mixture_check.ATTEMPT1.py")
spec = importlib.util.spec_from_file_location("block07_attempt1", p)
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)
rows = []
for a in [1.0, 3.0, 12.0]:
    for resolution in [64, 128, 256, 512, 1024]:
        base, _ = m.radial_kernel(a, 0.0, resolution)
        for nu in [0.5, 1.0, 2.0]:
            value, modes = m.radial_kernel(a, nu, resolution)
            exact = float(ive(nu, a) / i0e(a))
            rows.append(dict(a=a, nu=nu, resolution=resolution,
                             ratio=value / base, bessel_ratio=exact,
                             signed_error=value / base - exact, modes=modes))
print(json.dumps({"diagnostic_source_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
                  "challenged_source_sha256": sha256(p.read_bytes()).hexdigest(),
                  "rows": rows}, indent=2))
