import sys
sys.path.insert(0, '.')
from f5_t2_lossy_far_wall import scan
for m in (-1.5, -0.5):
    for Ly in (8, 12, 16):
        print(f"=== m = {m}, Ly = {Ly} ===")
        for Gam in (0.1, 1.0, 10.0, 100.0):
            nl, near, heavy, farl = scan(Ly, m, Gam, nk=181)
            fl = (f"{len(farl)} far-localised light, max decay {max(d for _, d, _ in farl):.2e}" if farl else "no far-localised light")
            print(f"  Gamma={Gam:6.1f}: #light/kx<= {nl}; near-edge max decay={near if near is None else f'{near:.2e}'}; "
                  f"min decay other in-gap={heavy:.3e}; {fl}")
