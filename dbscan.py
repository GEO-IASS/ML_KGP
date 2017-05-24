import numpy as np
from sklearn.cluster import DBSCAN
from sklearn import metrics
from sklearn.datasets.samples_generator import make_blobs
from sklearn.preprocessing import StandardScaler
import image_helper as ih

def segment(pickle_file,cluster_number,output_file):
	data = ih.get_pickle_object_as_numpy(pickle_file)
	X = np.array([data[i][j] for i in xrange(data.shape[0]) for j in xrange(data.shape[1])])
	db = DBSCAN(eps=0.1, min_samples=10,n_jobs=8).fit(X)
	core_samples = db.core_sample_indices_
	labels = db.labels_
	n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
	L = [[0 for i in xrange(data.shape[1])] for j in xrange(data.shape[0])]
	col = 0
	for i in xrange(0,data.shape[0]):
		for j in xrange(0,data.shape[1]):
			L[i][j] = labels[i*data.shape[1]+j]
	ih.save_output(L,None,output_file+".pickle")
	ih.save_image(L,output_file+".jpeg")




