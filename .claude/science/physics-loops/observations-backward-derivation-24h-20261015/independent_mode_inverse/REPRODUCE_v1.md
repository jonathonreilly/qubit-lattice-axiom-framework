# Reproduction

Run from this evidence directory after preserving existing outputs. The scientific programs print JSON to stdout and use no external observations. All required author runtime files are in author_snapshot.

    PYTHONDONTWRITEBYTECODE=1 python3 -B independent_controls_v1.py
    PYTHONDONTWRITEBYTECODE=1 python3 -B comparison_controls_v1.py
    PYTHONDONTWRITEBYTECODE=1 python3 -B author_snapshot/check_mode_inverse_v1.py
    PYTHONDONTWRITEBYTECODE=1 python3 -B author_snapshot/check_mode_inverse_jets_v1.py
    PYTHONDONTWRITEBYTECODE=1 python3 -B author_snapshot/check_mode_gain_v1.py
    PYTHONDONTWRITEBYTECODE=1 python3 -B author_snapshot/check_mode_gain_jets_v1.py

Use an external 120-second bound per program for a fresh reproduction. The recorded bounded wrappers provide the exact original argv, environment setting, timeout and byte captures. They deliberately refuse to overwrite existing attempt records. run_independent_bounded_v1.py accepts a fresh --attempt label; run_comparison_bounded_v1.py uses fixed immutable original labels.

The two scientific checker programs have no repository reads. Author paths resolve relative to their unchanged copied script locations. Thus those six programs are portable with this directory. capture_author_unit_v1.py is a provenance-capture tool requiring the original campaign pack argument; it is not needed to replay the mathematics and refuses to replace author_snapshot.

The six original runs used Python 3.12.8. Independent algebra used SymPy 1.14.0; author numerical dependency versions are in each retained result. Direct replays on another software environment need not be byte-identical. No independent-CAS claim is made.

