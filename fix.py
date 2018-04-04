import numpy as np

def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1
    
data =  np.genfromtxt("cepa_mon.dat", dtype= None)
corrections =  np.genfromtxt("../g32p745call_parametrs.dat", dtype= None)

out = list()
for i in range(0, len(corrections)):
    o = list()
    correction = corrections[i][1]
    o.append(data[i][0])
    for j in range(1, len(data[i])):
        o.append(data[i][j] * correction)
    out.append(o)
    
out = np.array(out)
np.savetxt("../cepa_mon_corrected.dat", dtype= None)

for k in range(0, len(out)):
    diviser = float(out[k][1])
    for l in range(1, len(data[k])):
        out[k][l] = float(out[k][l])/(diviser)
         
np.savetxt("cepa_mon_corrected_and_divided.dat", out)