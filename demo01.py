# demo01: reading the dimuon data with simple python and
# verify the enegy-momentum formula for 1 muon

fin = open('Dimuon_DoubleMu.csv')
data = fin.readlines()
event = data[1].split(',')

E1 = float(event[3])  # Energy in GeV
px1 = float(event[4]) # x-momentum in GeV/c
py1 = float(event[5]) # y-momentum in GeV/c
pz1 = float(event[6]) # z-momentum in GeV/c
M1 = 0.105658 # Mass in GeV/c^2

print('3-momentum of muon #1: (%g,%g,%g)' % (px1,py1,pz1))
print('energy of muon #1 (from data file):',E1)
print('energy of muon #1 (calculated):',(px1**2+py1**2+pz1**2 + M1**2)**0.5)
