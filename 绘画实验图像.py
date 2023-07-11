import matplotlib.pyplot as plt
import numpy as np
FPS = [87.590,88.460,88.568,89.666,88.840]
mAP1 = [97.32,97.75,97.94,97.87,98.23]
mAP2 = [75.10,75.79,76.04,76.57,76.78]
plt.figure(figsize=(9,4.5))

plt.subplot(211)
plt.plot(FPS,mAP1,"ro--",label="mAP:0.5")

plt.ylabel("mAP(%)")
# plt.xticks(np.arange(87,90,0.2))
# plt.yticks(np.arange(75,100,2))
plt.legend()
plt.grid()
plt.subplot(212)
plt.plot(FPS,mAP2,"c*:",label="mAP:0.75")

plt.xlabel("FPS")
plt.ylabel("mAP(%)")
plt.legend()
plt.grid()
plt.show()