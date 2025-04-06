# demo02: reading the dimuon data with simple python and
# verify the enegy-momentum formula for 2 muons

fin = open('Dimuon_DoubleMu.csv')
data = fin.readlines()
event = data[1].split(',')

# 4-momentum of muon #1
px1 = float(event[4])
py1 = float(event[5])
pz1 = float(event[6])
E1 = (px1**2+py1**2+pz1**2+0.105658**2)**0.5

# 4-momentum of muon #2
px2 = float(event[13])
py2 = float(event[14])
pz2 = float(event[15])
E2 = (px2**2+py2**2+pz2**2+0.105658**2)**0.5

# 4-momentum of dimuon
px = px1 + px2
py = py1 + py2
pz = pz1 + pz2
E = E1 + E2

M = float(event[20]) # Dimuon invarant mass in GeV/c^2

print('4-momentum of muon #1: (%g,%g,%g,%g)' % (px1,py1,pz1,E1))
print('4-momentum of muon #2: (%g,%g,%g,%g)' % (px2,py2,pz2,E2))
print('4-momentum of dimuon: (%g,%g,%g,%g)' % (px,py,pz,E))
print('Dimuon invarant mass (from data file):',M)
print('Dimuon invarant mass (calculated):',(E**2 - px**2 - py**2 - pz**2)**0.5)
