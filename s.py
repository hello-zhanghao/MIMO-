# 20200909

# 20200831
import numpy as np
import matplotlib.pyplot as plt
test_type = 'BER'
modOrder = 4
Nt = 4
Nr = 4
results = {}

results['SNR'] = np.arange(0, 23, 2)
results['ZF'] =  [0.381658375, 0.3502575, 0.30742712499999997, 0.260166875, 0.210769, 0.161568, 0.12085987499999999, 0.084516875, 0.057020625, 0.038428250000000004, 0.024409999999999998, 0.015804250000000002]
# results['SVD'] = 
results['MMSE'] =  [0.27805050000000003, 0.23526875, 0.19194225, 0.15009662499999998, 0.11289437499999999, 0.081051125, 0.05687225, 0.038660625000000004, 0.025491874999999997, 0.016624375, 0.010855875, 0.006942750000000001]
# results['Autoencoder-origin'] = 
# results['Autoencoder-TN64RN256'] = 
results['Autoencoder-TN256RN2048']= [0.24541249999999998, 0.197405, 0.1504675, 0.10499499999999999, 0.06437000000000001, 0.03227624999999999, 0.013854999999999998, 0.00526875, 0.00197875, 0.0009662500000000001, 0.0006712500000000001, 0.0004849999999999999]
for key, value in results.items():
    if key == 'SNR':
        pass
    else:
        print(key+' =', value)
        plt.plot(results['SNR'], value, label=key)
        
plt.grid(b=True, which='both', axis='both', color='k', linestyle='--', linewidth=0.3)
plt.yscale('log')
plt.xlabel('SNR(dB)')
plt.ylabel(test_type)

plt.title('M%dNr%dNt%d' % (modOrder, Nr, Nt))
plt.legend()
plt.show()
