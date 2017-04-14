# coding: utf-8
from pyAudioAnalysis import audioTrainTest as aT
aT.featureAndTrain(['genres/classical_w/','genres/blues_w/','genres/metal_w/','genres/disco_w/'], 1.0, 1.0, aT.shortTermWindow, aT.shortTermStep, 'svm', 'svmclasbluemetaldisc', True);
aT.fileClassification('genres/test/classical/classical_00089.wav', 'svmclasbluemetaldisc','svm')