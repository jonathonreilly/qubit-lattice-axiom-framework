#!/usr/bin/env python3
"""Exact local gauge commutators and Z2 physical-sector completion controls."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,itertools
import sympy as s
from sympy.polys.domains import QQ_I

HERE=Path(__file__).resolve().parent


def spin_half_u1():
    # Tensor order is left matter, link electric flux, right matter.
    I3=s.eye(3);I2=s.eye(2);basis=s.eye(3)
    Q=s.diag(0,1,-1);N=s.diag(0,1,1);E=s.diag(-s.Rational(1,2),s.Rational(1,2))
    U=s.Matrix([[0,0],[1,0]])
    creators=[basis[:,a]*basis[:,0].T for a in (1,2)]
    tensor=s.kronecker_product
    Gleft=tensor(I3,E,I3)-tensor(Q,I2,I3)
    Gright=-tensor(I3,E,I3)-tensor(I3,I2,Q)
    totalN=tensor(N,I2,I3)+tensor(I3,I2,N)
    counts=[tensor(basis[:,a]*basis[:,a].T,I2,I3)+tensor(I3,I2,basis[:,a]*basis[:,a].T) for a in (1,2)]
    hopplus=tensor(creators[0].T,U.T,creators[0])
    hopminus=tensor(creators[1].T,U,creators[1])
    H=hopplus+hopplus.T+hopminus+hopminus.T
    births=[tensor(creators[0],U,creators[1]),tensor(creators[1],U.T,creators[0])]
    for op in [H,*births,tensor(N,I2,I3),tensor(I3,I2,N)]:
        assert Gleft*op==op*Gleft and Gright*op==op*Gright
    for count in counts:assert H*count==count*H
    for birth in births:
        assert totalN*birth-birth*totalN==2*birth
        for count in counts:assert count*birth-birth*count==birth
    pairvac=tensor(basis[:,0]*basis[:,0].T,I2,basis[:,0]*basis[:,0].T)
    assert sum((J.T*J for J in births),s.zeros(18))==pairvac
    assert U.T*U!=I2 and U*U.T!=I2
    return dict(local_dimension=18,Gauss_commutators_exact_zero=True,
                hopping_preserves_each_charge_count=True,birth_adds_one_each_charge=True,
                two_birth_channels_total_loss_is_vacant_pair_projector=True,
                link_shift_not_unitary=True)


def z2_cycle():
    edges=[(0,1),(1,2),(2,3),(0,3)];V=4
    # In zero Gauss sector, site record occupancy is fixed by incident link parity.
    configurations=[]
    for bits in range(16):
        n=0
        for site in range(V):
            parity=sum((bits>>e)&1 for e,pair in enumerate(edges) if site in pair)%2
            n|=parity<<site
        configurations.append((bits,n))
    dim=len(configurations);I=s.eye(dim);where={z[0]:i for i,z in enumerate(configurations)}
    Hhop=s.zeros(dim);jumps=[];full=[]
    for i,(bits,n) in enumerate(configurations):
        if n==15:full.append(i)
        for e,(a,b) in enumerate(edges):
            na,nb=(n>>a)&1,(n>>b)&1
            target=where[bits^(1<<e)]
            n2=configurations[target][1]
            assert n2==n^(1<<a)^(1<<b)
            if na!=nb:Hhop[target,i]=1
    for e,(a,b) in enumerate(edges):
        J=s.zeros(dim)
        for i,(bits,n) in enumerate(configurations):
            if not ((n>>a)&1) and not ((n>>b)&1):J[where[bits^(1<<e)],i]=1
        jumps.append(J)
    assert Hhop==Hhop.T
    # One gauge loop and an electric term, both preserving occupation blocks.
    ring=s.zeros(dim)
    for i,(bits,n) in enumerate(configurations):
        ring[where[bits^15],i]=1
        assert configurations[where[bits^15]][1]==n
    electric=s.diag(*(sum(1-2*((bits>>e)&1) for e in range(4)) for bits,n in configurations))
    H=Hhop+s.Rational(2,3)*ring+s.Rational(1,7)*electric
    N=s.diag(*(n.bit_count() for bits,n in configurations))
    assert H*N==N*H
    for J in jumps:assert N*J-J*N==2*J
    transient=[i for i in range(dim) if i not in full];nt=len(transient);It=s.eye(nt)
    # Analyze the transient trace-decreasing generator directly; its invertibility
    # excludes every transient zero eigenmode in this exact finite control.
    Ht=H.extract(transient,transient)
    L=-s.I*(s.kronecker_product(It,Ht)-s.kronecker_product(Ht.T,It))
    for J in jumps:
        Jt=J.extract(transient,transient)
        K=(J.T*J).extract(transient,transient)
        L+=s.kronecker_product(Jt,Jt)-(s.kronecker_product(It,K)+s.kronecker_product(K.T,It))/2
    for site in range(4):
        n=s.diag(*((word>>site)&1 for bits,word in configurations)).extract(transient,transient)
        L+=s.kronecker_product(n,n)-(s.kronecker_product(It,n)+s.kronecker_product(n,It))/2
    rank=L.to_DM().convert_to(QQ_I).rank()
    assert rank==nt*nt
    # The physical occupation block dimension is two for every even pattern.
    multiplicities={str(n):sum(m==n for bits,m in configurations) for n in range(16) if n.bit_count()%2==0}
    assert set(multiplicities.values())=={2}
    return dict(physical_Hilbert_dimension=dim,full_occupation_dimension=len(full),
                transient_Hilbert_dimension=nt,transient_Liouvillian_dimension=nt*nt,
                exact_transient_Liouvillian_rank=rank,occupation_pattern_dimensions=multiplicities,
                gauge_magnetic_ring_coefficient='2/3',gauge_electric_coefficient='1/7',
                hopping_birth_monitoring_rates='1',no_stationary_transient_mode=True)


def main():
    result=dict(created_utc=datetime.now(timezone.utc).isoformat(),
                script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                U1_local=spin_half_u1(),Z2_cycle=z2_cycle(),
                scope='Supplied finite gauge models; exact gauge identities and one finite Z2 transient control. General completion proof is separate; no emergent U1 photon or native TOE claim.')
    encoded=json.dumps(result,indent=2)+'\n';(HERE/'GAUGE_RECORD_LOCAL_ALGEBRA_RESULTS.json').write_text(encoded);print(encoded,end='')


if __name__=='__main__':main()
