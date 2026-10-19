#!/usr/bin/env python3
"""Resumable PT production chunk.  usage:
  run_pt.py TAG L SEED START BETAS(comma list or @file) WALL_MIN [THERM_SWEEPS] [MEAS_EVERY] [V]
Each call runs for at most WALL_MIN minutes, then checkpoints (data/ckpt/TAG.npz) and appends one
measurement chunk data/raw/TAG_cNNNN.npz (first THERM_SWEEPS sweeps of the whole run are not measured).
Re-run the same command to continue."""
import os, sys, time, json, glob
for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "NUMBA_NUM_THREADS"):
    os.environ.setdefault(_v, "1")
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from sim import PT
from ctqmc import nb_seed

KEYS = ["E", "nF", "Wx", "Wy", "Wz", "Nc", "S1", "S2", "Ib"]


def main():
    tag, L, seed, start, bs, wall = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), sys.argv[4], sys.argv[5], float(sys.argv[6])
    therm = int(sys.argv[7]) if len(sys.argv) > 7 else 1000
    every = int(sys.argv[8]) if len(sys.argv) > 8 else 1
    V = float(sys.argv[9]) if len(sys.argv) > 9 else 0.0
    if bs.startswith("@"):
        betas = [float(x) for x in open(bs[1:]).read().split()]
    else:
        betas = [float(x) for x in bs.split(",")]
    D = os.path.join(HERE, "..", "data")
    os.makedirs(os.path.join(D, "ckpt"), exist_ok=True)
    os.makedirs(os.path.join(D, "raw"), exist_ok=True)
    ck = os.path.join(D, "ckpt", tag + ".npz")
    pt = PT(L, betas, V=V, seed=seed, start=start)
    bmax = max(betas)
    FULL = set(int(np.argmin(np.abs(np.array(betas) - x))) for x in (L / 2, float(L), bmax, min(betas)))
    pt.noloop_sweeps = int(os.environ.get("NOLOOP_SWEEPS", "0"))
    if os.path.exists(ck):
        pt.load(ck)
        nb_seed(seed * 1000 + pt.nsw % 100000 + 7)  # fresh stream after resume
        pt.rng = np.random.default_rng(seed * 7919 + pt.nsw)
    chunks = sorted(glob.glob(os.path.join(D, "raw", tag + "_c*.npz")))
    ci = len(chunks)
    t0 = time.time()
    rows = []
    st0 = pt.stats.copy()
    n0 = pt.nsw
    tr0 = pt.trips
    while time.time() - t0 < wall * 60:
        pt.sweep_all()
        pt.swaps()
        if pt.nsw > therm and pt.nsw % every == 0:
            m = pt.measure(range(len(betas)), full=FULL)
            rows.append([[m[k].get(key, np.nan) for key in KEYS] for k in range(len(betas))])
    bad = pt.check()
    pt.save(ck)
    if rows:
        np.savez_compressed(os.path.join(D, "raw", f"{tag}_c{ci:04d}.npz"), m=np.array(rows, dtype=float),
                            keys=np.array(KEYS), betas=np.array(betas), nsw_end=pt.nsw,
                            stats=(pt.stats - st0) / max(1, pt.nsw - n0), trips=pt.trips,
                            swap=pt.swap_acc / np.maximum(1, pt.swap_try))
    info = {"tag": tag, "L": L, "seed": seed, "start": start, "nsw": pt.nsw, "sweeps_this_call": pt.nsw - n0,
            "trips_total": pt.trips, "trips_this_call": pt.trips - tr0, "check": int(bad),
            "nrows": len(rows), "secs": round(time.time() - t0, 1),
            "swap_min": float((pt.swap_acc / np.maximum(1, pt.swap_try)).min()) if len(betas) > 1 else None}
    print(json.dumps(info), flush=True)
    with open(os.path.join(HERE, "..", "logs", "prod_chunks.jsonl"), "a") as f:
        f.write(json.dumps(info) + "\n")


if __name__ == "__main__":
    main()
