from scipy import misc
import matplotlib.pyplot as plt
from scipy import fftpack
import numpy as np
import pylab as py

def freqHighPass(img, r):
    """
    Applies an High Pass filter to img in the frequency domain.
    In:  img, image to filter
       r, percentage of spectrum to keep (in [0 1])
    Out: ifiltered, filtered version of the image
       P, filtered spectrum
    """
    I = fftpack.fftshift(fftpack.fft2(img)) # entering to frequency domain
    # fftshift moves zero-frequency component 
    # to the center of the array
    P = np.zeros(I.shape,dtype=complex)

    r = int((r*min(img.shape))/2);
    c1 = I.shape[0]/2 # spectrum center
    c2 = I.shape[1]/2

    for i in range(c1-r,c1+r):  # frequency cutting
        for j in range(c2-r,c2+r): # around the center
            P[i,j] = I[i,j]

    ifiltered = np.real(fftpack.ifft2(fftpack.ifftshift(P)))
    return ifiltered,P # back to the spatial domain

i = misc.imread('image2.png')
i = np.mean(i,2) # to get a 2-D array

ifiltered,P = freqHighPass(i,0.5) # 40% of spectrum preserved

plt.subplot(2,2,1)
plt.title('Original - Fourier Specturm')
plt.imshow(np.log(abs(fftpack.fftshift(fftpack.fft2(i))))**2)
plt.subplot(2,2,2)
plt.title('Filtered - Fourier Specturm')
plt.imshow(np.log(abs(P))**2)
plt.subplot(2,2,3)
plt.title('Original image')
plt.imshow(np.flipud(i))
plt.gray()
plt.subplot(2,2,4)
plt.title('Filtered image')
plt.imshow(np.flipud(ifiltered))
plt.show()

#F1 = fftpack.fft2(image)
#F2 = fftpack.fftshift( F1 )
#psf2D = np.log(np.abs( F2 ))**2
#
#py.figure(1)
#py.clf()
#py.imshow(  image , cmap=py.cm.Greys)
#
#py.figure(2)
#py.clf()
#py.imshow(  psf2D , cmap=py.cm.Greys)



#plt.imshow(im1)
#plt.show()
