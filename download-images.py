"""
Download and preprocess images for the ImageGraph dataset.

Before running this script, please download the URL lists from
https://github.com/nle-ml/mmkb and unpack. Images will (by defaul) be stored as
`image-graph_images/{freebase-id}/{provider}_{index}.jpg`. All images will be
converted to jpg and rescaled to a maximum size of 500 while preserving the
aspect ratio. Uses multiprocessing to download and process the images in
parallel. Skips images that were already downloaded.


usage: download-images.py [-h] [--url-dir URL_DIR] [--images-dir IMAGES_DIR]
                          [--provider {all,google,bing,yahoo}]
                          [--num-images NUM_IMAGES] [--workers WORKERS]

optional arguments:
  -h, --help            show this help message and exit
  --url-dir URL_DIR     the directory where the url files are stored (default:
                        image-graph_urls)
  --images-dir IMAGES_DIR
                        the directory where the processed images will be
                        stored (default: image-graph_images)
  --provider {all,google,bing,yahoo}
                        download only images from this provider (default: all)
  --num-images NUM_IMAGES
                        the number of images to download per provider
                        (default: 25)
  --workers WORKERS     the number of workers (should be much higher than your
                        number of cores because many workers will get stuck
                        waiting for server responses) (default: 100)
"""


from __future__ import absolute_import, division, print_function, unicode_literals
import pandas as pd
import urllib
import urlparse
from PIL import Image, ImageFile
from tqdm import tqdm
import os
import errno
from ssl import CertificateError
from httplib import HTTPException
from multiprocessing import Pool
import sys
import argparse
import socket

ImageFile.LOAD_TRUNCATED_IMAGES = True  # prevent PIL from raising an error if a file is truncated
socket.setdefaulttimeout(30)  # set timeout for downloads so processes do not get completely stuck

parser = argparse.ArgumentParser(description='Download images for ImageGraph.', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('--url-dir', default='image-graph_urls', help='the directory where the url files are stored')
parser.add_argument('--images-dir', default='image-graph_images', help='the directory where the processed images will be stored')
parser.add_argument('--provider', choices=['all', 'google', 'bing', 'yahoo'], default='all', help='download only images from this provider')
parser.add_argument('--num-images', type=int, default=25, help='the number of images to download per provider')
parser.add_argument('--workers', type=int, default=100, help='the number of workers (should be much higher than your number of cores because many workers will get stuck waiting for server responses)')
args = parser.parse_args()

if args.provider == 'all':
    providers = ['google', 'bing', 'yahoo']
else:
    providers = [args.provider]


for provider in providers:

    print('Downloading images for:', provider)
    urls = pd.read_csv(os.path.join(args.url_dir, 'URLS_{}.txt'.format(provider)), sep='\t', names=['url', 'id'])

    def download_image(i):

        row = urls.iloc[i]
        url = row['url']
        freebase_id, index = row['id'].split('/')
        index = int(index)

        # Create dir for entity if it doesn't exist.
        target_dir = os.path.join(args.images_dir, freebase_id)
        try:
            os.makedirs(target_dir)
        except OSError as e:  # multiprocessing-safe way to handle existing dir
            if e.errno != errno.EEXIST:
                raise

        # TODO: Maybe use more images if some cannot be downloaded.
        if index < args.num_images:  # only use first 25 images (as in the paper)
            target_filename = '{}_{}.jpg'.format(provider, index)

            # Skip images that were already downloaded.
            if os.path.exists(os.path.join(target_dir, target_filename)):
                pass
            else:
                try:
                    # Download and open image.
                    # TODO: Store temporary files in a separate folder (e.g. image-graph_temp),
                    #       so they are not hidden in the system folders.
                    temp_filename = ''
                    temp_filename, _ = urllib.urlretrieve(row['url'])
                    im = Image.open(temp_filename)
                except (IOError, CertificateError, HTTPException):
                    pass
                except Exception as e:
                    print('Got unusual error during downloading/opening of image:', e)
                    print('Please make sure that this error is just caused by a corrupted file.')
                else:
                    # Resize and convert to jpg.
                    im.thumbnail((500, 500), Image.ANTIALIAS)
                    im = im.convert('RGB')

                    # Save.
                    im.save(os.path.join(target_dir, target_filename))
                finally:
                    # Remove temporary file.
                    try:
                        os.remove(temp_filename)
                    except OSError:
                        pass


    pool = Pool(args.workers)  # use many processes here because some of them will get stuck waiting for server responses

    with tqdm(total=len(urls)) as pbar:
        for _ in pool.imap_unordered(download_image, urls.index, 100):
            pbar.update()

    pool.close()
    pool.join()

    print()
    print('Finished:', provider)
    print()
