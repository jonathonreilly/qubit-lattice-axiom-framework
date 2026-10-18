import pickle, numpy as np
class SafeU(pickle.Unpickler):
    OK = {('numpy', 'dtype'), ('numpy.core.multiarray', 'scalar'), ('numpy._core.multiarray', 'scalar'),
          ('numpy.core.multiarray', '_reconstruct'), ('numpy._core.multiarray', '_reconstruct'), ('numpy', 'ndarray'),
          ('builtins', 'set'), ('builtins', 'frozenset'), ('collections', 'Counter')}
    def find_class(self, mod, name):
        if (mod, name) in self.OK: return super().find_class(mod, name)
        raise pickle.UnpicklingError(f"blocked {mod}.{name}")
def load(path):
    with open(path, 'rb') as f: return SafeU(f).load()
