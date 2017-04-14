# coding: utf-8
from pyAudioAnalysis import audioTrainTest as aT
aT.featureAndTrain(['genres/classical/','genres/metal_w/'], 0.75, 0.5, aT.shortTermWindow, aT.shortTermStep, 'svm', 'svmclassdisc', True);
aT.fileClassification('genres/test/classical/classical_00089.wav', 'svmclassdisc','svm')
