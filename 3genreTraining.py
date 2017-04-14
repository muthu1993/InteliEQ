# coding: utf-8
from pyAudioAnalysis import audioTrainTest as aT
aT.featureAndTrain(['genres/classical/','genres/metal/'], 0.75, 0.5, aT.shortTermWindow, aT.shortTermStep, 'svm', 'svmclassmetl', True);
aT.fileClassification('genres/test/classical/classical_00089.wav', 'svmclassmetl','svm')
