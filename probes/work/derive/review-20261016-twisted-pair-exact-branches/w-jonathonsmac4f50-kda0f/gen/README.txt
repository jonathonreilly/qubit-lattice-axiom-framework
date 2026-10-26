Scratch generators (not needed by check.py). Order: build_cache.py (needs setup.py) -> reduce.py (branches.py) ->
labels.py -> layered.py <m-vector> for each of the 9 branches (tracked.py, poly.py) -> b4levels.py -> export.py -> export2.py.
They write pickles/JSON into the working directory; data.b64 is what was pasted into check.py as DATA_B64.
