# R3 (events) pre-registration — written before any numerics
Stamp: see `date -u` line appended below.

Checks (none is verdict-bearing alone; verdict per TESTS.md Lane R fixed readings):
N-a  Bilayer (height<=2) sum for ANY interval-count action (BD local/smeared, link action):
     on a bilayer every relation is a link, so S = phi_n*n + phi_l*R. Claim (exact):
     |Z_bil| ~ |1+e^{i phi_l}|^{n^2/4}; suppressed below manifold-like e^{O(n ln n)} iff
     phi_l mod 2pi in (2pi/3, 4pi/3). Real weights e^{-S}: never suppressed (>= e^{c n^2}).
     Check: brute-force interval counts on random bilayers (N1=N2=N3=0, N0=R) and the closed form.
N-b  Orbit-volume lemma: any nonzero Lorentz-invariant pair kernel K(tau^2) (support tau^2 in [1,2])
     has int int_{DxD} K^2 ~ T^6 in a 4D diamond of height T (2D: ~ T^2 log T);
     a non-invariant kernel (Euclidean 4-distance in [1,2]) gives ~ T^4.
     PASS(lemma check): fitted exponents 6+-0.4 (4D inv), 4+-0.3 (4D non-inv).
N-d  Locality of a point move: displacing ONE point by delta in a 4D diamond of height T
     flips a number of relations ~ rho*delta*T^3 (null-shell reach), partners spread to the boundary.
     Check: exponent of T at fixed delta, 3+-0.5.
Dilemma arithmetic (suggested): with phi_l in the bilayer window, R = (h^2/8)Var/S_kin
     >= 7.9e-4*phi_l*(L/l_k)^4 using G-A's refereed second-chaos coefficient 0.0191 L^6,
     the smeared scaling eps^{5/2}, N1's (I0^{1/2}-1) ~ h^2/8, and S_kin = h^2 w^2 V/(64 pi G).
Sat Oct 10 10:38:46 UTC 2026
