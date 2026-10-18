"""F5-T2: lossy far wall on a Qi-Wu-Zhang strip (2+1D -> 1+1D analogue). Pre-registered in PREREG_T1.md."""
import numpy as np

sx = np.array([[0, 1], [1, 0]], complex); sy = np.array([[0, -1j], [1j, 0]], complex)
sz = np.array([[1, 0], [0, -1]], complex)


def strip_h(kx, Ly, m):
    onsite = np.sin(kx) * sx + (m + np.cos(kx)) * sz
    hop = 0.5 * sz - 0.5j * sy          # hopping y -> y+1 from cos ky sz + sin ky sy
    H = np.zeros((2 * Ly, 2 * Ly), complex)
    for y in range(Ly):
        H[2*y:2*y+2, 2*y:2*y+2] = onsite
        if y + 1 < Ly:
            H[2*(y+1):2*(y+1)+2, 2*y:2*y+2] = hop
            H[2*y:2*y+2, 2*(y+1):2*(y+1)+2] = hop.conj().T
    return H


def scan(Ly, m, Gam, nk=241, egap=0.4):
    P = np.zeros((2 * Ly, 2 * Ly)); P[-2:, -2:] = np.eye(2)
    worst_light, n_light_max, min_heavy, far_light_k = 0.0, 0, np.inf, []
    near_decays = []
    for kx in np.linspace(-np.pi, np.pi, nk, endpoint=False):
        He = strip_h(kx, Ly, m) - 0.5j * Gam * P
        E, V = np.linalg.eig(He)
        sel = np.abs(E.real) < egap
        dec = -2 * E.imag[sel]
        Vs = V[:, sel]
        w_far = (np.abs(Vs[Ly:, :]) ** 2).sum(0) / (np.abs(Vs) ** 2).sum(0)  # weight on far half (rows Ly/2..)
        w_far = (np.abs(Vs[2*(Ly//2):, :]) ** 2).sum(0) / (np.abs(Vs) ** 2).sum(0)
        light = dec < 1e-2
        n_light_max = max(n_light_max, int(light.sum()))
        if light.any():
            for d, wf in zip(dec[light], w_far[light]):
                if wf < 0.5:
                    near_decays.append(d)
                else:
                    far_light_k.append((kx, d, wf))
        if (~light).any():
            min_heavy = min(min_heavy, dec[~light].min())
    return n_light_max, (max(near_decays) if near_decays else None), min_heavy, far_light_k


def main():
    m = -1.0
    for Ly in (12, 20, 30):
        print(f"=== Ly = {Ly} ===")
        for Gam in (0.0, 0.1, 0.3, 1.0, 3.0, 10.0, 30.0, 100.0):
            nl, near, heavy, farl = scan(Ly, m, Gam)
            fl = (f"{len(farl)} far-localised light states, max decay {max(d for _, d, _ in farl):.2e}"
                  if farl else "no far-localised light state")
            print(f"  Gamma={Gam:6.1f}: max #light(in-gap, decay<1e-2) per kx = {nl}; near-edge max decay = "
                  f"{near if near is None else f'{near:.2e}'}; min decay of other in-gap states = {heavy:.3e}; {fl}")


if __name__ == "__main__":
    main()
