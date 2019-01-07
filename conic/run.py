from scipy.io import mmread
from glob import glob

s = glob("*.mtx")

print s
parts = [""

H = mmread("h.mtx")
A = mmread("a.mtx")
G = mmread("g.mtx")
lba = mmread("lba.mtx")
uba = mmread("lba.mtx")
lbx = mmread("lbx.mtx")
ubx = mmread("lbx.mtx")
x0 = mmread("x0.mtx")
lam_x0 = mmread("lam_x0.mtx")
lam_a0 = mmread("lam_a0.mtx")

solver = conic("conic","qrqp",{a:})
