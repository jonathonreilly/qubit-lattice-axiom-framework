"""Load PT measurement chunks and compute per-beta estimates with binned errors."""
import os, glob
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
D = os.path.join(HERE, "..", "data", "raw")


def load(tag):
    fs = sorted(glob.glob(os.path.join(D, tag + "_c*.npz")))
    if not fs:
        return None
    ms = []
    for f in fs:
        d = np.load(f)
        ms.append(d["m"])
        keys = list(d["keys"])
        betas = d["betas"]
        last = d
    m = np.concatenate(ms, axis=0)  # (nmeas, nbeta, nkeys)
    return {"m": m, "keys": keys, "betas": betas, "trips": int(last["trips"]), "swap": last["swap"],
            "stats": last["stats"], "nsw": int(last["nsw_end"])}


def derived(m, keys):
    k = {n: i for i, n in enumerate(keys)}
    W = m[..., [k["Wx"], k["Wy"], k["Wz"]]]
    out = {"E": m[..., k["E"]], "W2": (W ** 2).mean(-1), "P0": (W == 0).mean(-1),
           "P1": (np.abs(W) == 1).mean(-1), "Nc": m[..., k["Nc"]], "S1": m[..., k["S1"]],
           "nF": m[..., k["nF"]]}
    if "S2" in k:
        out["S2"] = m[..., k["S2"]]
    return out


def binerr(x, nb=20):
    """mean and binned standard error along axis 0 (nb equal bins)"""
    n = len(x) // nb
    if n < 1:
        return x.mean(0), np.nan * x.mean(0)
    b = x[: n * nb].reshape((nb, n) + x.shape[1:]).mean(1)
    return x.mean(0), b.std(0, ddof=1) / np.sqrt(nb)


def estimate(tags, discard_frac=0.0, nb=20):
    """per tag estimates, and combined (mean of tags, error = max(combined-binned, seed scatter/sqrt(n)))."""
    per = []
    for t in tags:
        d = load(t)
        if d is None:
            continue
        m = d["m"][int(discard_frac * len(d["m"])):]
        der = derived(m, d["keys"])
        per.append({"tag": t, "betas": d["betas"], "trips": d["trips"], "n": len(m), "swap": d["swap"],
                    "est": {q: binerr(v, nb) for q, v in der.items()}})
    if not per:
        return None
    comb = {}
    for q in per[0]["est"]:
        mus = np.array([p["est"][q][0] for p in per])
        ses = np.array([p["est"][q][1] for p in per])
        mu = mus.mean(0)
        se_b = np.sqrt((ses ** 2).sum(0)) / len(per)
        se_s = mus.std(0, ddof=1) / np.sqrt(len(per)) if len(per) > 1 else np.zeros_like(mu)
        comb[q] = (mu, np.maximum(se_b, se_s), se_b, se_s)
    return per, comb
