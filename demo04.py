# demo04: generate the plot for the invariant mass of dimuons
import matplotlib.pyplot as plt

fin = open('Dimuon_DoubleMu.csv')
data = fin.readlines()

var = []
for line in data[1:]:
    event = line.split(',')
    
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
    M = (E**2 - px**2 - py**2 - pz**2)**0.5
    
    if M<120.: var.append(M)

plt.hist(var, bins=240)
plt.xlabel('Invariant mass of dimuons [GeV/c^2]')
plt.ylabel('Entries')
plt.show()
