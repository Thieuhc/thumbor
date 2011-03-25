#!/usr/bin/python
# -*- coding: utf-8 -*-

# thumbor imaging service
# https://github.com/globocom/thumbor/wiki

# Licensed under the MIT license: 
# http://www.opensource.org/licenses/mit-license
# Copyright (c) 2011 globo.com timehome@corp.globo.com

# the domains that can have their images resized
ALLOWED_SOURCES = ['s.glbimg.com', 'www.globo.com', 'ego.globo.com']

# the max width of the resized image
MAX_WIDTH = 1280

# the max height of the resized image
MAX_HEIGHT = 800

# the quality of the generated image
# this option can vary widely between
# imaging engines and works only on jpeg images
QUALITY = 80

# the way images are to be loaded
LOADER = 'thumbor.loaders.http_loader'

# how to store the original images
STORAGE = 'thumbor.storages.file_storage'

# imaging engine to use to process images
ENGINE = 'thumbor.engines.pil'

# in case imagemagick engine is used
# the path for the magickwand bindings
# this is not a required option since
# thumbor should be able to find magickwand
# on its own
#MAGICKWAND_PATH = []

# detectors to use to find Focal Points in the image
# more about detectors can be found in thumbor's docs
# at https://github.com/globocom/thumbor/wiki
DETECTORS = [
    'thumbor.filters.face_detector',
    'thumbor.filters.feature_detector'
]

# if you use face detection this is the file that
# OpenCV will use to find faces. The default should be
# fine, so change this at your own peril.
#FACE_DETECTOR_CASCADE_FILE = 'haarcascade_frontface_alt.xml'
