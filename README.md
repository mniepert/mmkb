# Multimodal Knowledge Graphs

![alt text](https://github.com/nle-ml/mmkb/blob/master/media/KB.png)

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.1245698.svg)](https://doi.org/10.5281/zenodo.1245698)


### License
MMKG is released under the BSD-3-Clause License (please read the LICENSE file for more details).

### Numerical Data for FB15k, YAGO15k, and DBpedia15k

Numerical data for the entities in the FB15k, DBpedia15k, and Yago15k knowledge graphs. FB15k is a commonly used knowledge graph in the KB completion literature. Both FB15k and FB15k-237 can be used with the numerical data. The data set and one method for integrating numerical data into a joint machine learning model are described in the following paper (to be presented at UAI 2018).

https://arxiv.org/abs/1709.04676

```bibtex
@inproceedings{Garcia-DuranN18,
  author    = {Alberto Garc{\'{\i}}a{-}Dur{\'{a}}n and
               Mathias Niepert},
  title     = {KBlrn: End-to-End Learning of Knowledge Base Representations with
               Latent, Relational, and Numerical Features},
  booktitle = {Proceedings of the Thirty-Fourth Conference on Uncertainty in Artificial
               Intelligence, {UAI}},
  pages     = {372--381},
  publisher = {{AUAI} Press},
  year      = {2018}
}
```

[Download the numerical data for FB15k entities.](FB15K/FB15K_NumericalTriples.txt)

We have created the Yago and DBpedia equivalents of FB15k and extracted numerical data for these data sets. You can find those files in the folders DB15K and YAGO15K.

### Visual Data for FB15k, YAGO15k, and DBpedia15k

The second data set consists of a set of images associated with each of the entities in the FB15k, DBpedia15k, and Yago15k knowledge graphs. For now, we provide a list of URLs that can be downloaded with a [script](download-images.py) which also scales the images (thanks to https://github.com/jrieke). We also provide the links of the Freebase IDs to their image URLs.  The paper describing the data set, possible visual queries, and a method for answering these queries are introduced in the following paper.

https://arxiv.org/abs/1709.02314

```bibtex
@inproceedings{OoroRubio2019AnsweringVQ,
  title={Answering Visual-Relational Queries in Web-Extracted Knowledge Graphs},
  author={Daniel O{\~n}oro-Rubio and Mathias Niepert and Alberto Garc{\'i}a-Dur{\'a}n
  and Roberto Gonzalez-Sanchez and Roberto Javier L{\'o}pez-Sastre},
  booktitle={AKBC},
  year={2019}
}
```

[Download the image URLs for FB15k entities.](https://www.dropbox.com/s/thct96phmypkaon/image-graph_urls.tar.gz)
NB: The Freebase ID is written m.xyz instead of /m/xyz

If you want to try out the crawler we used to retrieve the image URLs/data, you can download it [here](https://github.com/robegs/imageDownloader).

If you want to obtain the embeddings learned from a trained VGG16, you can download them [FB15K](https://www.dropbox.com/s/acsaog6qxy1kgpu/FB15K_ImageData.h5?dl=0), [DB15K](https://www.dropbox.com/s/rfl27sqpet7wyb3/DB15K_ImageData.h5?dl=0), [YAGO15K](https://www.dropbox.com/s/8062amzsspx2d6b/YAGO15K_ImageData.h5?dl=0 ). For example, the embedding for the DB15k entity <http://dbpedia.org/resource/Bright_Star_(film)>, indexed by the identifier DBIMG00039, can be accessed: 

```python
import h5py
import numpy as np
filename = 'DB15K_ImageData.h5'
f = h5py.File(filename, 'r')
vgg_feats = f["DBIMG00039"] 
```

### Temporal Information for Yago15k, Wikidata, ICEWS14 and ICEWS05-15

Facts in Yago15k, Wikidata, ICEWS14 and ICEWS05-15 are enriched with temporal information. The data sets and a methodology for performing link prediction in temporal KGs with standard scoring functions are described in the following paper (to be presented at EMNLP 2018).

Learning Sequence Encoders for Temporal Knowledge Graph Completion.

https://arxiv.org/abs/1809.03202

```bibtex
@inproceedings{GarcaDurn2018LearningSE,
  title={Learning Sequence Encoders for Temporal Knowledge Graph Completion},
  author={Alberto Garc{\'i}a-Dur{\'a}n and Sebastijan Dumancic and Mathias Niepert},
  booktitle={EMNLP},
  year={2018}
}
```

[Download the knowledge graphs with time information.](TemporalKGs/)


### sameAs Links between FB15k, YAGO15k, and DBpedia15k

We have sameAs links between [FB15k and DBpedia15k](https://github.com/nle-ml/mmkb/blob/master/DB15K/DB15K_SameAsLink.txt) as well as between [FB15k and YAGO15k](https://github.com/nle-ml/mmkb/blob/master/YAGO15K/YAGO15K_SameAsLink.txt).

MMKG: Multi-Modal Knowledge Graphs
https://arxiv.org/abs/1903.05485

```bibtex
@inproceedings{liu2019mmkg,
  title={MMKG: multi-modal knowledge graphs},
  author={Liu, Ye and Li, Hui and Garcia-Duran, Alberto and Niepert, 
  Mathias and Onoro-Rubio, Daniel and Rosenblum, David S},
  booktitle={European Semantic Web Conference},
  pages={459--474},
  year={2019},
  organization={Springer}
}
```

### Citing MMKB

If you use MMKB in your work, please cite one of the above papers. Thanks!
