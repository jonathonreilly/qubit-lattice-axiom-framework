#!/usr/bin/env python3
"""Charged-generator, square-root symbol, and missing-moment challenges.

Historical provenance: the charged ring basis was adapted from a prior
Gauss construction. Exact original source and provenance are archived under
docs/work_history/review_loop/pr8160; no prior executable is loaded.
New current matrices are differentiated from their literal flux increments.
"""
import hashlib
import json
import math
from pathlib import Path

import numpy as np
from scipy import sparse
from scipy.linalg import expm
from scipy.sparse.linalg import eigsh, expm_multiply

AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = ('docs/ROTOR_JOINT_REAL_TIME_GAUGE_TWO_POINT_LIMIT_BOUNDED_THEOREM_NOTE_2026-09-16.md', 'docs/ROTOR_UNIFORM_COMPACT_FIELD_SOFT_RESPONSE_BOUNDED_THEOREM_NOTE_2026-09-16.md', 'docs/ROTOR_JOINT_GROUND_ENERGY_OSCILLATOR_DEFECT_BOUNDED_THEOREM_NOTE_2026-09-16.md', 'docs/ROTOR_JOINT_LOCAL_GAUGE_CHARACTERISTIC_LIMIT_BOUNDED_THEOREM_NOTE_2026-09-16.md')
# Literal proof inputs are read below; the source self-hash is an integrity read.

_REPO = Path(__file__).resolve().parents[1]
for _input_path in AUDIT_INPUT_PATHS:
    _input_bytes = (_REPO / _input_path).read_bytes()
    if _input_path.endswith('.md'):
        assert ('claim_id: ' + Path(_input_path).stem.lower()).encode() in _input_bytes

assert '[calH,P(u)]=i Z(Su)-i g J(W_E^(1/2)u).' in (_REPO / AUDIT_INPUT_PATHS[0]).read_text()

TOL = 3e-8
checks = 0
report = {}


def demand(condition, label):
    global checks
    if not bool(condition):
        raise AssertionError(label)
    checks += 1


def car_hop(bits, create, annihilate):
    if not (bits>>annihilate)&1:
        return None
    sign = (-1)**((bits&((1<<annihilate)-1)).bit_count())
    after = bits^(1<<annihilate)
    if (after>>create)&1:
        return None
    sign *= (-1)**((after&((1<<create)-1)).bit_count())
    return after|(1<<create), sign


def charged_ring(g):
    # The original ceil(6/g) fixture at g=.6 left 4.98495e-16 in the
    # three outer flux layers, above the predeclared 1e-16 threshold.
    # Preserve that failure and enlarge the basis; keep the threshold.
    cutoff = math.ceil(8/g)
    matter = [bits for bits in range(256)
              if sum((bits>>(2*x))&1 for x in range(4))==2
              and sum((bits>>(2*x+1))&1 for x in range(4))==2]
    states = [(bits, n) for bits in matter for n in range(-cutoff, cutoff+1)]
    index = {s:j for j,s in enumerate(states)}
    dim = len(states)
    flux = []
    for bits,n in states:
        charges = np.array([((bits>>(2*x))&1)-((bits>>(2*x+1))&1) for x in range(4)])
        electric = n+np.cumsum(charges)
        demand(np.array_equal(electric-np.roll(electric, 1), charges), "literal ring Gauss law")
        flux.append(electric)
    flux = np.asarray(flux, float)
    shift_rows, shift_cols = [], []
    for col,(bits,n) in enumerate(states):
        if n<cutoff:
            shift_rows.append(index[(bits,n+1)])
            shift_cols.append(col)
    U = sparse.csr_matrix((np.ones(len(shift_rows)),(shift_rows,shift_cols)),shape=(dim,dim),dtype=complex)
    cosine, sine = (U+U.getH())/2, (U-U.getH())/(2j)
    e, b, hopping = np.array([1., 1.3, .8, 1.1]), .9, -.7
    onsite_potential = np.array([-.7,.2,.4,-.1])
    onsite = np.array([sum(onsite_potential[x]*(((bits>>(2*x))&1)+((bits>>(2*x+1))&1))
                              for x in range(4)) for bits,n in states])
    Hm = sparse.diags(onsite, format="csr", dtype=complex)
    currents = []
    for l in range(4):
        rows, cols, values, increments = [], [], [], []
        for col,(bits,n) in enumerate(states):
            for species,charge in [(0,1),(1,-1)]:
                moved = car_hop(bits,2*l+species,2*((l+1)%4)+species)
                if moved is None:
                    continue
                target,sign = moved
                nn = n+(charge if l==3 else 0)
                if abs(nn)>cutoff:
                    continue
                row = index[(target,nn)]
                increment = flux[row]-flux[col]
                expected = np.zeros(4)
                expected[l] = charge
                demand(np.array_equal(increment,expected), "charged CAR hop electric increment")
                rows.append(row); cols.append(col); values.append(hopping*sign)
                increments.append(increment[l])
        T = sparse.csr_matrix((values,(rows,cols)),shape=(dim,dim),dtype=complex)
        derivative_half = sparse.csr_matrix((1j*np.asarray(increments)*np.asarray(values),(rows,cols)),shape=(dim,dim))
        Hm += T+T.getH()
        currents.append(-(derivative_half+derivative_half.getH()))
    identity = sparse.eye(dim,format="csr",dtype=complex)
    H = sparse.diags(g*g/2*(flux*flux@e),format="csr")+b/g**2*(identity-cosine)+Hm
    S = np.sqrt(b)*np.sqrt(e)[None,:]
    frequency = float(np.linalg.norm(S))
    omega = S.T@S/frequency
    M = S.T/frequency
    Ps = [sparse.diags(g*np.sqrt(e[l])*flux[:,l],format="csr",dtype=complex) for l in range(4)]
    Z = math.sqrt(b)*sine/g
    Qs = [Ps[l]-1j*M[l,0]*Z for l in range(4)]
    u = np.array([.3,-.8,.4,1.2])
    P = sum(u[l]*Ps[l] for l in range(4))
    current = sum(np.sqrt(e[l])*u[l]*currents[l] for l in range(4))
    lhs = H@P-P@H
    rhs = 1j*float((S@u)[0])*Z-1j*g*current
    comm_error = float(sparse.linalg.norm(lhs-rhs))
    demand(comm_error<TOL, "exact charged electric equation")
    wrong_sign_error = float(sparse.linalg.norm(lhs-(1j*float((S@u)[0])*Z+1j*g*current)))
    demand(wrong_sign_error>1, "matter current sign discriminator")
    values,vectors = eigsh(H,k=1,which="SA",tol=2e-13,v0=np.ones(dim))
    energy,psi = float(values[0]),vectors[:,0]
    eigen_residual = float(np.linalg.norm(H@psi-energy*psi))
    demand(eigen_residual<TOL, "charged ground eigen residual")
    P_omega = sum((omega@u)[l]*Ps[l] for l in range(4))
    Q_omega = sum((omega@u)[l]*Qs[l] for l in range(4))
    residual = (H-energy*identity)@(P@psi)-P_omega@psi
    decomposition = -Q_omega@psi-1j*g*current@psi
    demand(np.linalg.norm(residual-decomposition)<TOL, "ground-vector norm residual decomposition")
    total_q_norm = float(sum(np.linalg.norm(Q@psi)**2 for Q in Qs))
    residual_upper = (frequency*math.sqrt(total_q_norm)
                        +g*2*abs(hopping)*math.sqrt(e.sum()))*np.linalg.norm(u)
    rows=[]
    G=H-energy*identity
    for t in [.7,1.4]:
        ut=expm(-1j*t*omega)@u
        comparator=sum(ut[l]*Ps[l] for l in range(4))@psi
        exact=expm_multiply(-1j*t*G,P@psi)
        error=float(np.linalg.norm(exact-comparator))
        demand(error<=abs(t)*residual_upper+TOL, "charged Duhamel norm estimate")
        rows.append(dict(t=t,error=error,upper=abs(t)*residual_upper))
    boundary=float(sum(abs(psi[j])**2 for j,(_,n) in enumerate(states) if abs(n)>=cutoff-2))
    demand(boundary<1e-16, "charged ground cutoff-tail check")
    return dict(g=g,cutoff=cutoff,dimension=dim,ground_energy=energy,
        eigen_residual=eigen_residual,electric_equation_error=comm_error,
        wrong_current_sign_error=wrong_sign_error,
        generator_residual=float(np.linalg.norm(residual)),
        residual_identity_error=float(np.linalg.norm(residual-decomposition)),
        total_annihilator_square=total_q_norm,boundary_mass=boundary,dynamics=rows)


def curl_symbol(k):
    d=np.exp(1j*np.asarray(k))-1
    return np.array([[-d[1],d[0],0],[-d[2],0,d[0]],[0,-d[2],d[1]]],complex),d


def symbol(k, formula=False):
    e,b=np.array([.7,1.1,1.8]),np.array([.9,1.4,1.2])
    C,d=curl_symbol(k)
    S=np.sqrt(b)[:,None]*C*np.sqrt(e)[None,:]
    A=S.conj().T@S
    if np.linalg.norm(d)<1e-13:
        return np.zeros((3,3),complex)
    if not formula:
        values,vectors=np.linalg.eigh(A)
        # The exact null vector removes spurious numerical sqrt(epsilon)
        # contributions from a roundoff eigenvalue of the rank-two matrix.
        values[0]=0
        return (vectors*np.sqrt(np.maximum(values,0)))@vectors.conj().T
    z=d/np.sqrt(e)
    Pi=np.eye(3)-np.outer(z,z.conj())/np.vdot(z,z)
    tau=np.trace(A).real
    p=(tau*tau-np.trace(A@A).real)/2
    return (A+math.sqrt(p)*Pi)/math.sqrt(tau+2*math.sqrt(p))


def symbol_checks():
    rng=np.random.default_rng(3420)
    errors=[]
    for _ in range(8):
        k=rng.uniform(-np.pi,np.pi,3)
        errors.append(float(np.linalg.norm(symbol(k)-symbol(k,True))))
    demand(max(errors)<TOL, "rank-two square-root formula")
    direction=np.array([1.,2.,-.7]);direction/=np.linalg.norm(direction)
    axis=np.array([0.,0.,1.])
    derivative_rows=[]
    for radius in [.1,.025,.00625]:
        k=radius*direction
        h=radius/64
        second=(symbol(k+h*axis,True)-2*symbol(k,True)+symbol(k-h*axis,True))/(h*h)
        derivative_rows.append(dict(radius=radius,scaled_second_derivative=float(radius*np.linalg.norm(second))))
    kernel_rows=[]
    for L in [5,8,12]:
        matrix=np.zeros((L,L,L,3,3),complex)
        for x in range(L):
            for y in range(L):
                for z in range(L):
                    matrix[x,y,z]=symbol(2*np.pi*np.array([x,y,z])/L,True)
        kernel=np.fft.ifftn(matrix,axes=(0,1,2))
        # Sum induced matrix l1 norms; this upper-bounds convolution l1 norm.
        l1=float(np.max(np.sum(np.abs(kernel),axis=3),axis=3).sum())
        kernel_rows.append(dict(L=L,l1_upper=l1))
    return dict(formula_errors=errors,scaled_second_derivatives=derivative_rows,
                finite_kernel_norms=kernel_rows,
                scope="Finite challenges only; the H2/summability proof is analytic.")


def first_moment_counterexample():
    c,t=.6,1.
    rows=[]
    for large in [10.,100.,1000.]:
        h=np.array([[1.,c*math.sqrt(large)],[c*math.sqrt(large),large]])
        eig=np.linalg.eigvalsh(h)
        observed=expm(-1j*t*h)[0,0]
        expected=np.exp(-1j*t*(1-c*c))
        demand(eig[0]>0 and h[0,0]==1, "positive quadratic toy with fixed first moment")
        demand(abs(observed-np.exp(-1j*t))>.2, "fixed first moment does not fix propagation")
        rows.append(dict(high_scale=large,low_eigenvalue=float(eig[0]),
            first_moment=float(h[0,0]),generator_norm_residual=float(np.linalg.norm((h-np.eye(2))@np.array([1.,0.]))),
            shifted_limit_error=float(abs(observed-expected)),naive_unit_frequency_error=float(abs(observed-np.exp(-1j*t)))))
    return rows


def main():
    report["charged_ring"]=[]
    for g in [.6,.4,.25]:
        row=charged_ring(g)
        report["charged_ring"].append(row)
        print(f"g={g:.2f}: charged generator residual={row['generator_residual']:.6g}, t=1.4 norm error={row['dynamics'][-1]['error']:.6g}",flush=True)
    report["weighted_square_root_symbol"]=symbol_checks()
    report["first_moment_counterexample"]=first_moment_counterexample()
    report["scope"]="Selective author checks, not a cubic thermodynamic phase computation."
    report["tolerance"]=TOL
    report["runner_sha256"]=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    report["checks"]=checks
    (_REPO / 'logs/runner-cache/rotor_joint_gauge_propagation_check_2026_09_16.json').write_text(json.dumps(report,indent=2)+"\n")
    print('per_element: executed — charged flux increments, current signs and residual identities')
    print('per_site: executed — four-site charged ring at g=0.6,0.4,0.25')
    print('per_mode: executed — weighted symbols on grids L=5,8,12 and three small radii; finite norms are diagnostic')
    print('per_block: executed — sparse charged Duhamel comparisons and hidden-oscillator witness')
    print('lattice_wide: checked and not executed — uniform bounds and joint-limit/time arguments are written proofs; finite fixtures do not execute an infinite lattice')
    print(f"TOTAL: PASS={checks} FAIL=0")


if __name__=="__main__":
    main()
