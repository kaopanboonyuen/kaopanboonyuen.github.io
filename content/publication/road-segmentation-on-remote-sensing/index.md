---
title: "Road segmentation of remotely-sensed images using deep convolutional neural networks with landscape metrics and conditional random fields"
authors:
- admin
- P. Vateekul

- S. Lawawirojwong

date: "2017-09-01T00:00:00Z"
doi: ""

author_notes:
- ""
- ""
- ""
- ""
- ""
- ""
- ""
- ""

# Schedule page publish date (NOT publication's date).
publishDate: "2017-09-01T00:00:00Z"

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ["2"]

# Publication name and optional abbreviated publication name.
publication: In *Remote Sensing* **Impact Factor 4.2**
publication_short: In *Remote Sensing* **Impact Factor 4.2**

abstract: Semantic segmentation of remotely-sensed aerial (or very-high resolution, VHS) images and satellite (or high-resolution, HR) images has numerous application domains, particularly in road extraction, where the segmented objects serve as essential layers in geospatial databases. Despite several efforts to use deep convolutional neural networks (DCNNs) for road extraction from remote sensing images, accuracy remains a challenge. This paper introduces an enhanced DCNN framework specifically designed for road extraction from remote sensing images by incorporating landscape metrics (LMs) and conditional random fields (CRFs). Our framework employs the exponential linear unit (ELU) activation function to improve the DCNN, leading to a higher quantity and more accurate road extraction. Additionally, to minimize false classifications of road objects, we propose a solution based on the integration of LMs. To further refine the extracted roads, a CRF method is incorporated into our framework. Experiments conducted on Massachusetts road aerial imagery and Thailand Earth Observation System (THEOS) satellite imagery datasets demonstrated that our proposed framework outperforms SegNet, a state-of-the-art object segmentation technique, in most cases regarding precision, recall, and F1 score across various types of remote sensing imagery.

# Summary. An optional shortened abstract.
summary: Semantic segmentation of remotely-sensed aerial (or very-high resolution, VHS) images and satellite (or high-resolution, HR) images has numerous application domains, particularly in road extraction, where the segmented objects serve as essential layers in geospatial databases. Despite several efforts to use deep convolutional neural networks (DCNNs) for road extraction from remote sensing images, accuracy remains a challenge. This paper introduces an enhanced DCNN framework specifically designed for road extraction from remote sensing images by incorporating landscape metrics (LMs) and conditional random fields (CRFs). Our framework employs the exponential linear unit (ELU) activation function to improve the DCNN, leading to a higher quantity and more accurate road extraction. Additionally, to minimize false classifications of road objects, we propose a solution based on the integration of LMs. To further refine the extracted roads, a CRF method is incorporated into our framework. Experiments conducted on Massachusetts road aerial imagery and Thailand Earth Observation System (THEOS) satellite imagery datasets demonstrated that our proposed framework outperforms SegNet, a state-of-the-art object segmentation technique, in most cases regarding precision, recall, and F1 score across various types of remote sensing imagery.

tags:
- Remote Sensing
- Road Segmentation
- Deep Learning
- Semantic Segmentation
- High-Resolution Imagery
- Aerial Imagery
- Convolutional Neural Networks
- Encoder-Decoder Networks
- Exponential Linear Unit
- Conditional Random Fields
- Landscape Metrics

featured: true

links:
# - name: Videos
#   url: https://www.youtube.com/channel/UCNzeAAPyZaX4EDr720q5msg
# - name: ICML talk
#   url: https://www.facebook.com/watch/live/?v=355035025132741&ref=watch_permalink
# - name: IEEE Spectrum article
#   url: https://spectrum.ieee.org/tech-talk/computing/software/deepmind-teaches-ai-teamwork
# - name: ICIAP 2017 Best Papers
#   url: https://link.springer.com/chapter/10.1007/978-3-319-60663-7_18
url_pdf: https://www.mdpi.com/2072-4292/9/7/680
url_code: https://github.com/kaopanboonyuen/
url_dataset: ''
url_poster: ''
url_project: ''
url_slides: https://kaopanboonyuen.github.io/files/panboonyuen_IC2IT2017_BestPaperAward.pdf
url_source: ''
url_video: ''

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder. 
image:
  caption: ''
  focal_point: Center
  preview_only: false

# Associated Projects (optional).
#   Associate this publication with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `internal-project` references `content/project/internal-project/index.md`.
#   Otherwise, set `projects: []`.
projects: []

# Slides (optional).
#   Associate this publication with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides: "example"` references `content/slides/example/index.md`.
#   Otherwise, set `slides: ""`.
slides: ""
---