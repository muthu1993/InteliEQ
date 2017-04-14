import audioBasicIO
import audioFeatureExtraction
import matplotlib.pyplot as plt

[Fs,x] = audioBasicIO.readAudioFile("doremi.wav");
F = audioFeatureExtraction.stFeatureExtraction(x,Fs,0.050*Fs,0.025*Fs);
plt.subplot(2,1,1); plt.plot(F[0,:]); plt.xlabel('Frame no'); plt.ylabel('ZCR');
plt.subplot(2,1,2); plt.plot(F[1,:]); plt.xlabel('Frame no'); plt.ylabel('Energ');plt.show()

