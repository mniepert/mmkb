# Multimodal Knowledge Graphs

![alt text](https://github.com/nle-ml/mmkb/blob/master/media/KB.png)

[![DOI](https://zenodo.org/badge/122334067.svg)](https://zenodo.org/badge/latestdoi/122334067)

### License
MMKG is released under the BSD-3-Clause License (refer to the LICENSE file for details).

### Citing MMKG

If you find MMKG useful in your research, please consider citing:

```
@misc{ye_liu_2018_1244118,
    author       = {Ye Liu and
                    Hui Li and
                    Alberto Garcia-Duran and
                    Mathias Niepert and
                    Daniel Onoro-Rubio and
                    David Rosenblum},
    title        = {MMKG: Multi-Modal Knowledge Graphs},
    month        = may,
    year         = 2018,
    doi          = {10.5281/zenodo.1244118},
    url          = {https://doi.org/10.5281/zenodo.1244118}
}
```

### Numerical Data for FB15k, YAGO15k, and DBpedia15k

Numerical data for the entities in the FB15k, DBpedia15k, and Yago15k knowledge graphs. FB15k is a commonly used knowledge graph in the KB completion literature. Both FB15k and FB15k-237 can be used with the numerical data. The data set and one method for integrating numerical data into a joint machine learning model are described in the following paper.

https://arxiv.org/abs/1709.04676

[Download the numerical data for FB15k entities.](FB15K/numTriples_FB15k.txt)

We have created the Yago and DBpedia equivalents of FB15k and extracted numerical data for these data sets. You can find those files in the folders DB15K and YAGO15K.

### Visual Data for FB15k, YAGO15k, and DBpedia15k

The second data set consists of a set of images associated with each of the entities in the FB15k, DBpedia15k, and Yago15k knowledge graphs. For now, we provide a list of URLs that can be downloaded with a [script](download-images.py) which also scales the images (thanks to https://github.com/jrieke). We also provide the links of the Freebase IDs to their image URLs.  The paper describing the data set, possible visual queries, and a method for answering these queries are introduced in the following paper.

https://arxiv.org/abs/1709.02314

[Download the image URLs for FB15k entities.](https://www.dropbox.com/s/thct96phmypkaon/image-graph_urls.tar.gz)
NB: The Freebase ID is written m.xyz instead of /m/xyz

If you want to try out the crawler we used to retrieve the image URLs/data, you can download it [here](https://github.com/robegs/imageDownloader).

If you want to obtain the embeddings learned from a trained VGG16, you can download them [here](). For example, the embedding for the DB15k entity <http://dbpedia.org/resource/Bright_Star_(film)>, indexed by the identifier DBIMG00039, can be accessed: 

```python
import h5py
import numpy as np
filename = 'DB15K_ImageData.h5'
f = h5py.File(filename, 'r')
vgg_feats = f["DBIMG00039"] 
```

### sameAs Links between FB15k, YAGO15k, and DBpedia15k

We have sameAs links between [FB15k and DBpedia15k](https://github.com/nle-ml/mmkb/blob/master/DB15K/DB15K_SameAsLink.txt) as well as between [FB15k and YAGO15k](https://github.com/nle-ml/mmkb/blob/master/YAGO15K/YAGO15K_SameAsLink.txt).



