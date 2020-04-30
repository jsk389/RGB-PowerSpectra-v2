# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np 

from sloscillations import frequencies, amplitudes, linewidths

def test_linewidths():

    frequency = np.arange(0.00787, 283., 0.00787)

    # Set up frequencies class
    freqs = frequencies.Frequencies(frequency=frequency,
                                          numax=103.2, 
                                          delta_nu=9.57, 
                                          radial_order_range=[-5, 5])
    # Eventually want this to read in from a configuration file
    params = {'calc_l0': True,
              'calc_l2': True,
              'calc_nom_l1': True,
              'calc_mixed': True,
              'calc_rot': False,
              'DPi1': 77.9,
              'coupling': 0.2,
              'eps_g': 0.0,
              'split_core': 0.5,
              'split_env': 0.0,
              'l': 1,
              'method': 'simple'}
    freqs(params)

    # Set up class
    amps = amplitudes.Amplitudes(freqs)

    amps(params)


    # Linewidths
    lwd = linewidths.Linewidths(amps)

    lwd(params)

    plt.plot(lwd.l0_freqs, lwd.l0_linewidths, 
             color='r', marker='D', linestyle='None', label='$\ell=0$')
    #plt.plot(amps.l2_freqs, amps.l2_amps, 
    #         color='g', marker='s', linestyle='None', label='$\ell=2$')
    #plt.plot(amps.l1_nom_freqs, amps.l1_nom_amps, 
    #         color='b', marker='o', linestyle='None', label='Nominal $\ell=1$')
    #plt.plot(amps.l1_mixed_freqs, amps.l1_mixed_amps, 
    #         color='c', marker='^', linestyle='None', label='Mixed $\ell=1$')
    #plt.plot(amps.frequency, amps.a0(frequency), '--')
    plt.xlim(lwd.l1_nom_freqs.min(), lwd.l1_nom_freqs.max())
    plt.xlabel(r'Frequency ($\mu$Hz)', fontsize=18)
    plt.ylabel(r'Linewidth ($\mu$Hz)', fontsize=18)
    plt.yscale('log')
    plt.legend(loc='best')
    plt.show()
    
if __name__=="__main__":

    test_linewidths()