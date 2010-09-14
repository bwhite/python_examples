import Image
import matplotlib.pyplot as mp
import numpy as np

filt = np.asfarray(np.array([[-1,0,1]]))
lena = np.asfarray(Image.open('lena.bmp').convert('L'))
filt_fft = np.fft.fft2(filt, s=[512, 512])
lena_fft = np.fft.fft2(lena)
lena_conv0 = np.real(np.fft.ifft2(filt_fft * lena_fft))
lena_conv1 = np.array(lena)
for i in range(1, lena.shape[0] - 1):
    for j in range(1, lena.shape[1] - 1):
        lena_conv1[i, j] = lena[i, j+1] - lena[i, j-1]
mp.gray()
mp.imshow(lena_conv0)
mp.figure()
mp.imshow(lena_conv1)
mp.show()

