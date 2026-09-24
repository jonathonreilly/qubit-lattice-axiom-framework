"""Compare root high-flux paths with an older independently built instrument."""
import hashlib
import importlib.util
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
MODEL = HERE.parent / "local_compensation_independent" / "model.py"
assert hashlib.sha256(MODEL.read_bytes()).hexdigest() == (
    "686529f4cd3dd5d73e3373f2604e56615c83228b5813a3848f2a194db00ae128")
spec = importlib.util.spec_from_file_location("older_independent_paths", MODEL)
model = importlib.util.module_from_spec(spec)
spec.loader.exec_module(model)
spec2 = importlib.util.spec_from_file_location("high_flux_author", HERE / "cube_high_flux_birth.py")
root = importlib.util.module_from_spec(spec2)
spec2.loader.exec_module(root)

rows = []
for n in (0, 1, 2, 3, 7, 19, 100):
    q, f = root.initial(n)
    got = model.effective_birth((tuple(q), tuple(f)), 0, 1,
                                model.CUBE_A, model.CUBE_EDGES)
    expected = {}
    for target in (2, 4):
        qq, ff = root.move(q, f, 0, target)
        qq, ff = root.birth(qq, ff)
        expected[tuple(qq), tuple(ff)] = 1.0
    assert got == expected
    assert all(model.gauss(qq, ff, model.CUBE_A, model.CUBE_EDGES)
               for qq, ff in got)
    coherent = model.effective_birth((tuple(q), tuple(f)), 0, None,
                                     model.CUBE_A, model.CUBE_EDGES)
    assert len(coherent) == 4 and all(a == 1.0 for a in coherent.values())
    rows.append({"n": n, "resolved_path_count": len(got),
                 "resolved_norm_squared": sum(abs(a) ** 2 for a in got.values()),
                 "coherent_path_count": len(coherent),
                 "coherent_norm_squared": sum(abs(a) ** 2 for a in coherent.values())})

print(json.dumps({"older_independent_model_sha256": hashlib.sha256(MODEL.read_bytes()).hexdigest(),
                  "rows": rows}, indent=2))
