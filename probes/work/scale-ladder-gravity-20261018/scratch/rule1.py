import numpy as np
L = 96; c = L//2
k = 2*np.pi*np.fft.fftfreq(L); KX, KY, KZ = np.meshgrid(k, k, k, indexing='ij')
avg = (np.cos(KX) + np.cos(KY) + np.cos(KZ))/3                      # Fourier symbol of the 6-neighbour average
X, Y, Z = np.meshgrid(*[np.arange(L)]*3, indexing='ij'); stag = (-1.0)**(X + Y + Z)
for name, sign, keep in (('average', 1, 1.0), ('anti', -1, 1.0), ('leaky', 1, 0.97)):
    den = 1 - sign*keep*avg
    with np.errstate(divide='ignore'): G = np.where(np.abs(den) < 1e-12, 0.0, 1.0/den)   # drop the exact zero mode
    d = np.real(np.fft.ifftn(G*np.exp(-1j*(KX*c + KY*c + KZ*c))))                         # response to one record at the centre
    line = [d[c + r, c, c] for r in range(1, 17)]
    B = d.reshape(L//2, 2, L//2, 2, L//2, 2).mean(axis=(1, 3, 5)); Bs = (d*stag).reshape(L//2, 2, L//2, 2, L//2, 2).mean(axis=(1, 3, 5)); cb = c//2
    base = d[c + 24, c, c]
    print(f"{name:8s}: values r=1..6: " + " ".join(f"{v:+.4f}" for v in line[:6]))
    print(f"          r*(d - d_far) at r=4, 8, 12, 16: " + " ".join(f"{r*(line[r-1]-base):+.4f}" for r in (4, 8, 12, 16)))
    print(f"          zoom x2 plain block: R*(B - B_far) at R=2,4,6,8: " + " ".join(f"{2*R*(B[cb+R, cb, cb]-B[cb+12, cb, cb]):+.4f}" for R in (2, 4, 6, 8))
          + " | chessboard-read block: " + " ".join(f"{2*R*(Bs[cb+R, cb, cb]-Bs[cb+12, cb, cb]):+.4f}" for R in (2, 4, 6, 8)))
