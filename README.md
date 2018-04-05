# Multimodal Knowledge Graphs

![alt text](https://github.com/nle-ml/mmkb/blob/master/media/KB.png)

We provide several data sets for knowledge bases. 

(1) Numerical data for the entities in the FB15k knowledge graph. FB15k is a commonly used knowledge graph in the KB completion literature. Both FB15k and FB15k-237 can be used with the numerical data. The data set and one method for integrating numerical data into a joint machine learning model are described in the following paper.

https://arxiv.org/abs/1709.04676

[Download the numerical data for FB15k entities.](numTriples_FB15k.txt)

(2) The second data set consists of a set of images associated with each of the entities in the FB15k knowledge graph. For now, we provide a list of URLs that can be downloaded with a [script](download-images.py) which also scales the images (thanks to https://github.com/jrieke). We also provide the links of the Freebase IDs to their image URLs.  The paper describing the data set, possible visual queries, and a method for answering these queries are introduced in the following paper.

https://arxiv.org/abs/1709.02314

[Download the image URLs for FB15k entities.](https://www.dropbox.com/s/thct96phmypkaon/image-graph_urls.tar.gz)
NB: The Freebase ID is written m.xyz instead of /m/xyz

If you want to try out the crawler we used to retrieve the image URLs/data, you can download it [here](https://github.com/robegs/imageDownloader).

Feel free to use the data sets but please cite the respective paper(s). 



