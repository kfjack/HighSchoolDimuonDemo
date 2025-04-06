# demo03: generate the plot for the energy of muon #1
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
    
    if E1<100.: var.append(E1)

plt.hist(var, bins=100)
plt.xlabel('Energy of muons [GeV]')
plt.ylabel('Entries')
plt.show()
