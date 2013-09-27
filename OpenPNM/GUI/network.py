from __future__ import absolute_import
import numpy as np
from .. import Generators

def Cubic(divisions=[10,10,10], lattice_spacing=.0005, loglevel=20, btype=[0,0,0], C=0.9, D=2.09e-9):
  gn = Generators.Cubic(divisions=divisions, lattice_spacing=lattice_spacing, loglevel=loglevel, btype=btype)
  pn = gn.generate()
  setattr(pn,"Total_Conc",C)
  setattr(pn,"Diff_Coefficient",D)
  setattr(pn,"divisions",divisions)
  setattr(pn,"lattice_spacing",lattice_spacing)
  pn.throat_properties['Pc_entry'] = -4*0.072*np.cos(np.radians(105))/pn.throat_properties['diameter']
  # Add dummy values for inlets and outlets
#  pn.declare_pore_property(name='inlets',dtype=np.int8)
#  pn.set_pore_property(name='inlets',ndarray=np.zeros((pn.get_num_pores(),),dtype=np.int8))
  pn.pore_properties['inlets']=np.zeros((pn.get_num_pores(),),dtype=np.int8)
  pn.pore_properties['inlets'][0]=1
#  pn.declare_pore_property(name='outlets',dtype=np.int8)
#  pn.set_pore_property(name='outlets',ndarray=np.zeros((pn.get_num_pores(),),dtype=np.int8))
  pn.pore_properties['outlets']=np.zeros((pn.get_num_pores(),),dtype=np.int8)
  pn.pore_properties['outlets'][0]=1
  return {'network': pn}