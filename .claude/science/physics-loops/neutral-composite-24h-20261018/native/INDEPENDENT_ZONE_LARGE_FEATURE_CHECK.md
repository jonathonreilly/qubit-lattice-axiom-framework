# Conditional threshold feature size and readout check

The recurrence, normalization, moment formula and threshold asymptotics check for the supplied infinite crossover operator. I independently evaluated the threshold derivatives at50-digit precision, without importing the root probe. No native source files were edited.

## Decaying solution and boundary equations

For an upper bound level E>2kappa, write x1=cosh beta>1, r1=exp(-beta), x2=-2kappa-x1<-1 and r2=x2+sqrt(x2²-1). Then both |r1| and |r2| are less than1, and E=x1²+2kappa*x1-1. The second root uses the plus square-root sign because x2 is negative; the other choice would grow.

The host solution psi_n=A(r1^n+b r2^n) obeys the bulk fourth-order recurrence. Eliminating d gives d=-sqrt(2)psi1/(E+2). The endpoint equations are a(r1)+b a(r2)=0 and B(r1)+b B(r2)=0, where a(r)=kappa/r+1/(4r²)-1 and B(r)=1/(4r)-[2/(E+2)]r. Thus b=-a(r1)/a(r2) and the probe determinant is correct.

## Exact norm and first moment

For the real parameters on this upper branch, the exact total norm divided by A² is

N=1/(1-r1²)+2b/(1-r1 r2)+b²/(1-r2²)
  +2(r1+b r2)²/(E+2)².

The last term is the side-state probability and must be present. A²=1/N and endpoint residue Z=A²(1+b)² therefore agree with the code. If parameters were complex, the formula would need conjugates; this real bound branch requires none.

The displayed mean_host_index is the TOTAL-state expectation of host index, with index zero assigned to the side component for this particular statistic:

A²[r1²/(1-r1²)²+2b r1r2/(1-r1r2)²+b²r2²/(1-r2²)²].

It is not the mean conditioned on being in the host, which would divide by host probability. The distinction is finite and does not affect the divergent leading term. For physical interval length ell=n+1 on the host and ell=2 on d, the mean is mean_host_index+P_host+2P_d. The d probability is O(beta), so these changes do not affect the asymptotic product claimed below.

## Independent threshold values

For the second/last disappearance threshold:

kappa_c=1.0452143582559712883698971029153159748,
b_c=-.1679933767871520105931996786800833950.

For delta=kappa_c-kappa>0, implicit differentiation of the determinant gives beta=(F_kappa/F_beta)delta+O(delta²), with

beta/delta→.4812808304108057054215722854396359487.

The sign in this derivative is correct because kappa=kappa_c-delta. Expanding the dispersion gives E-2kappa=(1+kappa)beta²+O(beta^4), hence

(E-2kappa)/delta²→.4737355332074169325039959311607200469.

The norm's only divergent term is1/(1-r1²)~1/(2beta); the short-root, cross and side pieces stay finite. Thus A²~2beta, Z~2beta(1+b_c)² and mean_host_index~1/(2beta). Consequently

Z*mean_host_index→(1+b_c)²
                =.6922350210700460028026876837479148161.

These numbers match the root expressions. The large feature follows from loss of normalizability at a tuned upper-band threshold; the local endpoint readout tends to zero rather than remaining fixed as its extent grows.

## Physical interpretation limits

Z is the residue for the normalized endpoint source in this crossover model. If the original observable retains the earlier leading source -2lambda E1, its physical leading weight is4lambda² Z, not Z alone. Higher source dressing and additional channels must still be controlled before a native readout claim.

The argument takes an infinite half-line and then approaches its threshold. A finite chain needs size much larger than1/beta to approximate this tail. In the original momentum construction q=pi-lambda*kappa, allowed finite-size momenta and the simultaneous lambda/volume/threshold limits must be compatible. Diverging feature size makes a merely fixed-size effective remainder inadequate; tiny native corrections can shift the threshold by more than delta or alter the near-threshold binding.

No interaction was added to this conditional operator, but approaching kappa_c is still a specified momentum/parameter limit. It is not a parameter-free mechanism that dynamically selects a large feature. It does not establish bulk native stability, a cosmological scalar, or an empirical detector coupling.

Operational note: the tensor virtual environment lacked mpmath; the independent numerical evaluation was successfully performed with system python3. This tool-path issue has no scientific implication.
