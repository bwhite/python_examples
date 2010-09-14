import Image
import matplotlib.pyplot as mp
import numpy as np

filt = np.asfarray(Image.open('lena_eye.bmp').convert('L'))
filt = np.rot90(filt, 2)
lena = np.asfarray(Image.open('lena.bmp').convert('L'))
filt_fft = np.fft.fft2(filt, s=[512, 512])
lena_fft = np.fft.fft2(lena)
lena_conv0 = np.real(np.fft.ifft2(filt_fft * lena_fft))
mp.gray()
mp.imshow(lena_conv0)
mp.show()

