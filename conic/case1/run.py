from scipy.io import mmread
from glob import glob
from casadi import *

s = glob("*.mtx")

qp_args = {}

for e in s:
  qp_args[e[:-4]] = DM(mmread(e))

opts = {"verbose":True, "max_iter":10}
solver = conic("conic","qrqp",{'a':qp_args["a"].sparsity(), 'h': qp_args["h"].sparsity()},opts)
solver(**qp_args)
