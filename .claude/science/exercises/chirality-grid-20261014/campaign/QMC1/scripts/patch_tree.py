"""Apply the tree-product vertex_core (same product, fewer python calls) to afqmc.py; run after gate (iii)."""
s = open('afqmc.py').read()
old = s[s.index("    def vertex_core(self, l, phi):"):s.index("    # ------------------------------------------------------------------------------------------ one-body application")]
new = '''    def vertex_core(self, l, phi):
        """core = ordered product of the channel exponentials (first channel acts first); the order is reversed on
        odd slices. Returns (core, core^-1). Evaluated as a balanced tree of batched matmuls (same product)."""
        Xp = self.channel_exps(phi, +1)
        Xm = self.channel_exps(phi, -1)
        if l % 2 == 1:
            Xp, Xm = Xp[::-1], Xm[::-1]
        return self._chain(Xp), self._chain(Xm[::-1])

    def _chain(self, arr):
        """arr[-1] @ ... @ arr[1] @ arr[0]"""
        while len(arr) > 1:
            if len(arr) % 2:
                arr = np.concatenate([arr, np.eye(self.D, dtype=complex)[None]], axis=0)
            arr = np.matmul(arr[1::2], arr[0::2])
        return arr[0]

'''
s = s.replace(old, new)
open('afqmc.py', 'w').write(s)
print("patched")
