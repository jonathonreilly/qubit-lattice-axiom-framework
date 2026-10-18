"""OS positivity for massive Gaussian k-form fields on the D4 cone (Whitney): Q = d^dag M_{k+1} d + m2 * diag(M_k).
Reflection Theta: t -> 2 t0 - t acts on cells by pullback with orientation signs. + algebra: cells whose
vertices all have t >= t0 (within half a torus)."""
import sys, pickle, numpy as np
sys.path.insert(0, '.')
import whitney as WF

def build(F, k, m2):
    def Q(q):
        q = np.asarray(q, complex)
        K = F.d(k, -q).T @ F.M(k + 1, q) @ F.d(k, q) if k < 4 else 0
        return K + m2 * np.diag(np.real(np.diag(F.M(k, np.zeros(4)))))
    return Q

def cells(F, k):
    """list of (class index, list of (offset vector, type)) for the canonical representative at anchor 0."""
    out = []
    for key, ci in F.cls[k].items():
        out.append((ci, [(np.array(b, float), t) for t, b in key]))
    return sorted(out)

def reflect_vertex(C, b, t, t0):
    p = np.array(b, float) + C.OFF[t]; pr = p.copy(); pr[3] = 2 * t0 - p[3]
    br = pr - C.OFF[t]; assert np.allclose(br, np.round(br)); return tuple(int(x) for x in np.round(br)), t

def rp_forms(F, k, m2, ks, Nt, t0):
    C = F.C; Qf = build(F, k, m2)
    kts = 2 * np.pi * np.arange(Nt) / Nt
    inv = [np.linalg.inv(Qf(np.array([*ks, kt]))) for kt in kts]
    G = lambda dbt: sum(Ki * np.exp(1j * kt * dbt) for Ki, kt in zip(inv, kts)) / Nt
    reps = cells(F, k)
    half = []                                  # (bt, class, vertex list absolute)
    for bt in range(-2, Nt // 2 + 2):
        for ci, verts in reps:
            ts = [bt + v[0][3] + C.OFF[v[1]][3] for v in verts]
            if min(ts) >= t0 - 1e-9 and max(ts) <= t0 + Nt / 2 + 1e-9:
                half.append((bt, ci, [(tuple(int(x) for x in v[0] + np.array([0, 0, 0, bt])), v[1]) for v in verts]))
    # image of each + cell under Theta: canonical class, its anchor time, sign
    img = []
    for bt, ci, verts in half:
        rv = [reflect_vertex(C, b, t, t0) for b, t in verts]
        key, anc, srt = WF.canon(rv)
        perm = [srt.index(v) for v in rv]; sg = WF.Forms._perm_sign(perm)
        img.append((F.cls[k][key], anc, sg))
    n = len(half); R = np.zeros((n, n), complex)
    for a, (bt1, c1, v1) in enumerate(half):
        for b, (c2i, anc2, sg2) in enumerate(img):
            # spatial anchor of the image differs from the + cell's by an integer spatial shift: Bloch phase
            d_sp = np.array(anc2[:3], float) - np.array(half[b][2][0][0][:3], float) * 0  # anchors measured in cells
            R[a, b] = sg2 * G(bt1 - anc2[3])[c1, c2i] * np.exp(-1j * np.array(ks) @ np.array(anc2[:3], float))
    return R
