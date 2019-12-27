from nuclide_data import *

hydrogen = 1
oganessum = 118

print("Z, N, A, t1/2, stable, decay_modes, weight")

for element in range(hydrogen, oganessum + 1):
    for isotope in isotopes[element]:
        nuclide = nuc(element, isotope)
        Z = element
        A = isotope
        N = A - Z
        t12 = nuclide['half-life']
        stable = nuclide['stable']
        decay_modes = ''
        weight = nuclide['weight'] if nuclide.has_key('weight') else "Unknown"
        for decay_mode in nuclide['decay modes'].keys():
            decay_modes = decay_modes + "None" if decay_mode is None else decay_mode + ";"
        print("{}, {}, {}, {}, {}, {}, {}".format(Z, N, A, t12, stable, decay_modes, weight))
