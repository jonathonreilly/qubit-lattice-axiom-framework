exec(open('b18lib.py').read())
np.set_printoptions(linewidth=200)
for e,om in ((np.zeros(3),1),(np.zeros(3),-1),(EX[0],1),(EX[0],-1)):
    B,_=intertwiners(blli,shifted(blli,e,om),r=0)
    print("e",e,"omega",om,"dim",len(B))
    for b in B:
        M=b[(0,0,0)]; M=M/M.flat[np.argmax(np.abs(M))]
        print("  diagonal:",np.allclose(M,np.diag(np.diag(M))),np.round(np.diag(M).real,3) if np.allclose(M,np.diag(np.diag(M))) else np.round(M,2))
