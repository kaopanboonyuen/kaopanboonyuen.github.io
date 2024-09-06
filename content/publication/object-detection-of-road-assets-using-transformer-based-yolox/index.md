---
title: "Object Detection of Road Assets Using Transformer-Based YOLOX with Feature Pyramid Decoder on Thai Highway Panorama"
authors:
- admin
- S. Thongbai
- W. Wongweeranimit
- P. Santitamnont
- K. Suphan
- C. Charoenphon

date: "2022-09-01T00:00:00Z"
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
publishDate: "2022-09-01T00:00:00Z"

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ["2"]

# Publication name and optional abbreviated publication name.
publication: In *Information*
publication_short: In *Information*

abstract: Detecting objects of varying sizes, like kilometer stones, remains a significant challenge and directly affects the accuracy of object counts. Transformers have shown remarkable success in natural language processing (NLP) and image processing due to their ability to model long-range dependencies. This paper proposes an enhanced YOLO (You Only Look Once) series with two key contributions, (i) We employ a pre-training objective to obtain original visual tokens from image patches of road assets, using a pre-trained Vision Transformer (ViT) backbone, which is then fine-tuned on downstream tasks with additional task layers. (ii) We incorporate Feature Pyramid Network (FPN) decoder designs into our deep learning network to learn the significance of different input features, avoiding issues like feature mismatch and performance degradation that arise from simple summation or concatenation. Our proposed method, Transformer-Based YOLOX with FPN, effectively learns general representations of objects and significantly outperforms state-of-the-art detectors, including YOLOv5S, YOLOv5M, and YOLOv5L. It achieves a 61.5% AP on the Thailand highway corpus, surpassing the current best practice (YOLOv5L) by 2.56% AP on the test-dev dataset.

# Summary. An optional shortened abstract.
summary: Detecting objects of varying sizes, like kilometer stones, remains a significant challenge and directly affects the accuracy of object counts. Transformers have shown remarkable success in natural language processing (NLP) and image processing due to their ability to model long-range dependencies. This paper proposes an enhanced YOLO (You Only Look Once) series with two key contributions, (i) We employ a pre-training objective to obtain original visual tokens from image patches of road assets, using a pre-trained Vision Transformer (ViT) backbone, which is then fine-tuned on downstream tasks with additional task layers. (ii) We incorporate Feature Pyramid Network (FPN) decoder designs into our deep learning network to learn the significance of different input features, avoiding issues like feature mismatch and performance degradation that arise from simple summation or concatenation. Our proposed method, Transformer-Based YOLOX with FPN, effectively learns general representations of objects and significantly outperforms state-of-the-art detectors, including YOLOv5S, YOLOv5M, and YOLOv5L. It achieves a 61.5% AP on the Thailand highway corpus, surpassing the current best practice (YOLOv5L) by 2.56% AP on the test-dev dataset.

tags:
- Attention
- Self-Attention
- MARS
- Sequential Quadtree Nodes
- Mask R-CNN
- PointRend
- Mask Transfiner

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
url_pdf: https://www.mdpi.com/2078-2489/13/1/5
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