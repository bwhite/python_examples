import Image
import matplotlib.pyplot as mp
import numpy as np

filt = np.asfarray(Image.open('letter_a.bmp').convert('L'))
filt = np.rot90(filt, 2)
letters = np.asfarray(Image.open('letters.bmp').convert('L'))
filt_fft = np.fft.fft2(filt, s=[512, 512])
letters_fft = np.fft.fft2(letters)
letters_conv0 = np.real(np.fft.ifft2(filt_fft * letters_fft))
thresh = sorted(letters_conv0.ravel())[-3]
letters_conv0 = letters_conv0 >= thresh
mp.gray()
mp.imshow(letters_conv0)
mp.figure()
mp.imshow(letters)
mp.show()
