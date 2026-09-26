# Independent weak-field reconstruction, in progress

No new author weak-field source/output/seal/checkpoint/registry read. Only neutral target and pinned preceding large-spin packet are dependencies.

Core derivation: physical Gauss Hilbert on link-angle torus; additionally choose zero global electric flux. Quotient by all flat U(1) connections. Its Euclidean covering space T=range(C^T) has r=2(V-1), compact lattice Lambda=2pi P_T Z^E. Flat connections are vertex gauges plus three global holonomies, so this is an actual physical superselection sector, not gauge removal of physical harmonic modes. Lambda is discrete: C lambda is a nonzero 2pi integer vector for any nonzero lambda; norm(C)<=sqrt12 gives minimum length>=pi/sqrt3. Choose compact chart support radius R=pi/(4sqrt3), inner r0=R/2.

Weak parameter h=sqrt(K/J), omega0=sqrt(KJ), fixed omega0 while h->0: K=omega0 h,J=omega0/h. Shift rotor by 2J number_plaquettes. H_h=omega0[-h Delta_q+2/h sum(1-cos(Cq))]. q=sqrt(h)x gives H0=-Delta_x+x^T C^T C x. A C2 radial cutoff chi of a normalized Schwartz harmonic packet gives a legitimate compact wavefunction. Quintic smoothstep chi is one on ball r0 and zero beyond R. M1=15/[8(R-r0)], Laplacian bound Dchi=10/[sqrt3(R-r0)^2]+(r-1)M1/r0.

Residual: M4(T)=sup |||x|^4 psi(t)||, M31(T)=sup |||x|^3 grad psi(t)||, harmonic evolution exp(-i omega0 H0 t). Bound residual <= omega0[12 h M4 +2 h^2 M1 M31/r0^3 +h^3 Dchi M4/r0^4], using norm(C)<=sqrt12. Initial cutoff norm >=sqrt(1-h^4 M4(0)^2/r0^8). Duhamel error unnormalized <=T residual bound; normalized target/current <=2 T residual/n0. Fixed finite-volume positive B suffices; coherent or finite Hermite packets give finite uniform-in-time constants. No volume-uniform photon/phase theorem.

Transverse symbol in edge-centered Fourier: B(k)=|khat|^2I-khat khat^T, khat_i=2sin(k_i/2). Nonzero frequencies 2 omega0 |khat|, two polarizations; no harmonic modes in chosen sector. Later continuum finite-mode limit: a=L/N, omega0_N=c/(2a), first h->0 for each finite N, then N->infinity, fixed Fourier indices/times. Frequencies c|khat|/a -> c|2pi m/L|. Optional composition: spin S->infinity at fixed h,N first, then h->0, then finite-mode continuum. Initial compact packet has finite electric fourth moments and Fourier cutoff can be used at fixed h,N. No joint scaling imported silently.

Planned controls: independently assemble periodic cubic incidence matrices and exact modular ranks/symbol checks; a compact one-plaquette Fourier calculation with a cutoff (ground+first-Hermite) packet, compare actual rotor and harmonic at decreasing h, plus Fourier-cutoff/grid checks. All evidence stays here; retain failures. No author code import.


PRE COMPLETE 2026-09-22T22:30:33.343498+00:00.
REPORT.md SHA256 97e03699969206594235e727487ef55ab77d0cb201abff5870dc7ac52fe64a93.
PRE_COMPARISON_SEAL.json SHA256 d17725c9c6f2b1a973ea89791402c94b1ee87759164a9a551c38b7b499fcf0f6; all 25 bindings verified, plus prior 55 and 2 top-level identities.
All three scripts and complete results read; no failures. Exact compact quotient, radial-cutoff residual and normalized Duhamel bound established. Main state error O(h) for fixed omega0, finite box/time and prescribed Schwartz packet. Zero electric-flux sector is additional to Gauss. One-square fixed-K phase countercontrol retained. Ordered S then h then finite-mode continuum only; no uniform-volume or full-QFT implication.
No new author packet accessed. Await explicit author-comparison authorization, preserving REPORT/PRE and all bound files.


POST-COMPARISON COMPLETE 2026-09-22, after explicit authorization.
Full seven-artifact author packet read and authenticated; context dependency identities unchanged.
COMPARISON.md SHA256 4e0d398024ad892c8e5d878cf0e97bcd10b90a2c9e6135f3b5ede793680d3314.
FINAL_SEAL.json SHA256 381c1a07ff18dbca2019e51eaa086707ac0b11d4d7a1c642e5435b3aeaa0b610; all 41 listed bindings plus 2 top-level seals verified.
No substantive correction requested. Exact scale translation h=g^2 and omega0=c/(2a), Fourier-trace side-six coefficient 175.04506506168266, and one independently assembled loop evolution corroborate author. No full author rerun; full read and exact arithmetic coverage are recorded. All PRE files unchanged, no failures, other new author content/static/homogeneous/ramp/energy/transport packets and campaign checkpoint/registry remain unopened.
