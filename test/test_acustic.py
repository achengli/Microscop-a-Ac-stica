import sys
sys.path.append('../lib/')

from acustic import Acustic
import numpy as np

print(Acustic.refl_coef(300,200))
print(Acustic.refl_coef([400,500,600],[300,400,800]))
print(Acustic.refl_coef(np.array([400,500,600]),np.array([300,400,800])))

print(Acustic._spheric_coord_from_epicentre(23,3,45))
