---
title: "Enhanced Feature Pyramid Vision Transformer for Semantic Segmentation on Thailand Landsat-8 Corpus"
authors:
- admin
- P. Rakwatin
- K. Intarat

date: "2020-03-01T00:00:00Z"
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
publishDate: "2020-03-01T00:00:00Z"

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ["2"]

# Publication name and optional abbreviated publication name.
publication: In *Information*
publication_short: In *Information*

abstract: Semantic segmentation on Landsat-8 data is crucial in the integration of diverse data, allowing researchers to achieve more productivity and lower expenses. This research aimed to improve the versatile backbone for dense prediction without convolutions—namely, using the pyramid vision transformer (PRM-VS-TM) to incorporate attention mechanisms across various feature maps. Furthermore, the PRM-VS-TM constructs an end-to-end object detection system without convolutions and uses handcrafted components, such as dense anchors and non-maximum suspension (NMS). The present study was conducted on a private dataset, i.e., the Thailand Landsat-8 challenge. There are three baselines, DeepLab, Swin Transformer (Swin TF), and PRM-VS-TM. Results indicate that the proposed model significantly outperforms all current baselines on the Thailand Landsat-8 corpus, providing F1-scores greater than 80% in almost all categories. Finally, we demonstrate that our model, without utilizing pre-trained settings or any further post-processing, can outperform current state-of-the-art (SOTA) methods for both agriculture and forest classes.

# Summary. An optional shortened abstract.
summary: Semantic segmentation on Landsat-8 data is crucial in the integration of diverse data, allowing researchers to achieve more productivity and lower expenses. This research aimed to improve the versatile backbone for dense prediction without convolutions—namely, using the pyramid vision transformer (PRM-VS-TM) to incorporate attention mechanisms across various feature maps. Furthermore, the PRM-VS-TM constructs an end-to-end object detection system without convolutions and uses handcrafted components, such as dense anchors and non-maximum suspension (NMS). The present study was conducted on a private dataset, i.e., the Thailand Landsat-8 challenge. There are three baselines, DeepLab, Swin Transformer (Swin TF), and PRM-VS-TM. Results indicate that the proposed model significantly outperforms all current baselines on the Thailand Landsat-8 corpus, providing F1-scores greater than 80% in almost all categories. Finally, we demonstrate that our model, without utilizing pre-trained settings or any further post-processing, can outperform current state-of-the-art (SOTA) methods for both agriculture and forest classes.

tags:
- Mon-Maximum Suspension
- Transfer Learning
- Vision Transformer
- Remote Sensing
- Landsat-8
- Transformer

featured: false

links:
# - name: Videos
#   url: https://www.youtube.com/channel/UCNzeAAPyZaX4EDr720q5msg
# - name: ICML talk
#   url: https://www.facebook.com/watch/live/?v=355035025132741&ref=watch_permalink
# - name: IEEE Spectrum article
#   url: https://spectrum.ieee.org/tech-talk/computing/software/deepmind-teaches-ai-teamwork
# - name: ACM
#   url: https://dl.acm.org/doi/10.1007/978-3-031-51023-6_3
# - name: ArXiv
#   url: https://arxiv.org/pdf/2305.04743
url_pdf: https://www.mdpi.com/2078-2489/13/5/259
url_code: https://github.com/kaopanboonyuen
url_dataset: ''
url_poster: ''
url_project: ''
url_slides: ''
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