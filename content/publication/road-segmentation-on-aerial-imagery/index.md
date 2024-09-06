---
title: "An enhanced deep convolutional encoder-decoder network for road segmentation on aerial imagery"
authors:
- admin
- P. Vateekul

- S. Lawawirojwong

date: "2017-01-01T00:00:00Z"
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
publishDate: "2017-01-01T00:00:00Z"

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ["1"]

# Publication name and optional abbreviated publication name.
publication: In *International Conference on Computing and Information Technology (IC2IT)* **Best Student Paper Honourable Mention (top 0.26\% of submissions)**
publication_short: In *International Conference on Computing and Information Technology (IC2IT)* **Best Student Paper Honourable Mention (top 0.26\% of submissions)**

abstract: Object classification from images is among the many practical examples where deep learning algorithms have successfully been applied. In this paper, we present an improved deep convolutional encoder-decoder network (DCED) for segmenting road objects from aerial images. Several aspects of the proposed method are enhanced, incl. incorporation of ELU (exponential linear unit)—as opposed to ReLU (rectified linear unit) that typically outperforms ELU in most object classification cases; amplification of datasets by adding incrementally-rotated images with eight different angles in the training corpus (this eliminates the limitation that the number of training aerial images is usually limited), thus the number of training datasets is increased by eight times; and lastly, adoption of landscape metrics to further improve the overall quality of results by removing false road objects. The most recent DCED approach for object segmentation, namely SegNet, is used as one of the benchmarks in evaluating our method. The experiments were conducted on a well-known aerial imagery, Massachusetts roads dataset (Mass. Roads), which is publicly available. The results showed that our method outperforms all of the baselines in terms of precision, recall, and F1 scores.

# Summary. An optional shortened abstract.
summary: In this paper, we introduce an improved deep convolutional encoder-decoder network (DCED) for segmenting road objects from aerial images. Enhancements include the use of ELU (exponential linear unit) instead of ReLU, dataset augmentation with incrementally-rotated images to increase training data by eight times, and the use of landscape metrics to remove false road objects. Tested on the Massachusetts Roads dataset, our method outperformed the SegNet benchmark and other baselines in precision, recall, and F1 scores.

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

featured: true

links:
# - name: Videos
#   url: https://www.youtube.com/channel/UCNzeAAPyZaX4EDr720q5msg
# - name: ICML talk
#   url: https://www.facebook.com/watch/live/?v=355035025132741&ref=watch_permalink
# - name: IEEE Spectrum article
#   url: https://spectrum.ieee.org/tech-talk/computing/software/deepmind-teaches-ai-teamwork
- name: ICIAP 2017 Best Paper Award
  url: https://link.springer.com/chapter/10.1007/978-3-319-60663-7_18
url_pdf: https://link.springer.com/chapter/10.1007/978-3-319-60663-7_18
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