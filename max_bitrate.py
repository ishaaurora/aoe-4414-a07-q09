#max_bitrate.py
#
# Usage: max_bitrate.py tx_w tx_gain_db freq_hz dist_km rx_gain_db n0_j bw_hz
#
# Input:
#  tx_w: Transmitting power
#  tx_gain: Transmitting antenna gain
#  freq_hz: communication frequency
#  dist_km: communication distance 
#  rx_gain_db: Receiving antenna gain
#  n0_j: Noise spectral density
#  bw_hz: Communication bandwidth
# Output:
#  Print time and voltage at a set time of a capacitor based power system
#
# Written by Isha Aurora
# Other contributors: None

# import modules
import sys
import math

#CONSTS
c = 299792458
L_l = math.pow(10,-1/10)
L_a = math.pow(10,0/10)


if len(sys.argv)==8:
    tx_w = float(sys.argv[1])
    tx_gain_db = float(sys.argv[2])
    freq_hz = float(sys.argv[3])
    dist_km = float(sys.argv[4])
    rx_gain_db = float(sys.argv[5])
    n0_j = float(sys.argv[6])
    bw_hz = float(sys.argv[7])
else:
    print(\
     'Usage: '\
     'max_bitrate.py tx_w tx_gain_db freq_hz dist_km rx_gain_db n0_j bw_hz'\
    )
    exit()


#CALC

wavelength = c/freq_hz

tx_gain = math.pow(10,tx_gain_db/10)
rx_gain = math.pow(10,rx_gain_db/10)

C = tx_w*L_l*tx_gain*L_a*rx_gain*math.pow(wavelength/(4*math.pi*dist_km),2)
N = n0_j*bw_hz

r_max = bw_hz*math.log((1+C/N),2)

print(math.floor(r_max))