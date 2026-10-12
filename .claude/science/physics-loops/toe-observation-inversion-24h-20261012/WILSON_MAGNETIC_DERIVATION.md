# Conditional Wilson magnetic response and pair stability

Author derivation, 2026-10-12, before focused independent checker exposure. No physical identification or radiative closure. Domain: mu>0, w>0, a²>0; primary w=1 and a²=1−mu with 0<mu<1. Classical weak uniform field, fixed oscillator level, field sent to zero at fixed mass; spatial lattice/continuous time. Charge q is calibrated through minimal link phase. No Pauli improvement.

Let W(p)=sum_i(1−cos p_i), v_i=1−cos p_i. Free energy e²=a² sum sin² p_i+(mu+w W)². Corners with j components pi have masses mu+2wj. At mu=0 there is precisely one zero for w>0, since W=0 is necessary and sufficient together with sine zero. This is the free species statement, not anomaly-free chiral SM completion.

At w=1, a²=1−mu, subtract the common-Laplacian square mu²+2W:
 e²−mu²−2W = W²−sum v_i²+mu sum v_i²
 =2sum_(i<j)v_i v_j+mu sum v_i² >=0.
Hence e(p)+e(k−p)>=sqrt(4mu²+omega(k)²)>omega(k) using the chord-norm triangle. Full torus, positive mass, all pair partitions; no photon decay into this pair. The unretuned a=1 comparator has e²−mu²−2W=2mu W+2sum_(i<j)v_i v_j>=0 but low-momentum c_e²=1+mu.

Take pi=−i grad−q A, so [pi_x,pi_y]=i q B, and (sigma.pi)²=pi²−q sigma.B. The low-field expansion of the exact minimally gauged Wilson Hamiltonian is H=beta(mu+w pi²/2)+a alpha.pi plus higher spatial powers. At fixed mu the positive-band nonrelativistic reduction to linear order in B is
 H_+=mu+(a²+mu w)pi²/(2mu)−a² q sigma.B/(2mu)+O(B²),
for fixed Landau level and p_z=0. The odd cubic lattice correction first contributes beyond linear B; commutators of the even Wilson piece with the odd Dirac part likewise affect higher orders.

Thus cyclotron frequency Omega_c=|qB|(a²/mu+w), spin frequency Omega_s=|qB|a²/mu, and their measured ratio (g/2)_tree=Omega_s/Omega_c=a²/(a²+mu w). The speed-matched primary gives 1−mu w, hence an anomaly shift −w m/Lambda. The bare-a=1 ratio is 1/(1+mu w), not the same exact finite-mass expression. Defining the magnetic moment solely relative to the rest mass without checking the measured cyclotron frequency would confuse these cases.

Independent route to test the sign and factors: continuum oscillator blocks for fixed positive qB=B. With sigma.pi=sqrt(2B)[[0,b†],[b,0]] and beta Dirac form, H decomposes into blocks mixing upper spin-up |n> with lower spin-down |n−1> (and its companion). Even diagonal entries contain mu+w B(N+1/2). Exact 2x2 energies in this quadratic continuum truncation can be expanded at B=0; there is an unpaired n=0 branch. Compare actual spin and orbital gaps, not sorted eigenvalues without labels. A full finite-field link Hamiltonian will test lattice corrections independently.

Photon timing is still 1−v/c=A4 E²/(8Lambda²)+O(E⁴/Lambda⁴). Eliminating Lambda in the matched tree model gives timing coefficient A4(delta a_e)²/(8w²m²) and delta a_e<0 for positive w. With E_QG,2=sqrt12 Lambda/sqrtA4, |delta a_e|=sqrt12 w m/(sqrtA4 E_QG,2). Given A4 in[1/3,1], an externally applicable timing lower bound implies |delta a_e|<=6w m/E_QG,2. This is a conditional parameter relation, not a calibrated confidence bound until full propagation/field/loop identifications hold.

The positive Wilson Pauli term in Beane et al. 1210.1847v2 equations(3)–(6) belongs to their spacetime Euclidean Wilson action and on-shell field redefinition. Do not copy its sign into this spatial Hamiltonian. The target is to verify the difference directly, including the cyclotron calibration; no novelty claim is made for Wilson magnetic effects.
