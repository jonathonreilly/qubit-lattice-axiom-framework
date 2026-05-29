# Handoff

This branch repairs the critical 3+1D Lorentz boost row by narrowing the
binding theorem to:

```text
supplied free-scalar Z^3 x R Hamiltonian-lattice continuum covariance
+ structural finite-a O(a^2 p^4) K4 anisotropy
```

It intentionally does not claim a Planck unit map, strict finite-`a` light
cone, experimental bound, or physical framework-substrate identification.

Verification:

```text
python3 -m py_compile scripts/frontier_lorentz_boost_3plus1d.py
python3 scripts/frontier_lorentz_boost_3plus1d.py
python3 scripts/precompute_audit_runners.py --runners scripts/frontier_lorentz_boost_3plus1d.py --force --push-mode none --allow-non-main --concurrency 1
bash docs/audit/scripts/run_pipeline.sh
```

Result: target row is `unaudited`, `ready: true`, with
`open_dependency_paths: []`.
