---
title: "MARS: Mask Attention Refinement with Sequential Quadtree Nodes for Car Damage Instance Segmentation"
authors:
- admin
- N. Nithisopa
- P. Pienroj
- L. Jirachuphun
- C. Watthanasirikrit
- N. Pornwiriyakul

date: "2023-01-01T00:00:00Z"
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
publishDate: "2023-01-01T00:00:00Z"

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ["1"]

# Publication name and optional abbreviated publication name.
publication: In *Image Analysis and Processing* **ICIAP 2023**
publication_short: In *Image Analysis and Processing* **ICIAP 2023**

abstract: Evaluating car damages from misfortune is critical to the car insurance industry. However, the accuracy is still insufficient for real-world applications since the deep learning network is not designed for car damage images as inputs, and its segmented masks are still very coarse. This paper presents MARS (Mask Attention Refinement with Sequential quadtree nodes) for car damage instance segmentation. Our MARS represents self-attention mechanisms to draw global dependencies between the sequential quadtree nodes layer and quadtree transformer to recalibrate channel weights and predict highly accurate instance masks. Our extensive experiments demonstrate that MARS outperforms state-of-the-art (SOTA) instance segmentation methods on three popular benchmarks such as Mask R-CNN [9], PointRend [13], and Mask Transfiner [12], by a large margin of +1.3 maskAP-based R50-FPN backbone and +2.3 maskAP-based R101-FPN backbone on Thai car-damage dataset. Our demos are available at https://github.com/kaopanboonyuen/MARS

# Summary. An optional shortened abstract.
summary: Evaluating car damages is crucial for the car insurance industry, but current deep learning networks fall short in accuracy due to inadequacies in handling car damage images and producing fine segmentation masks. This paper introduces MARS (Mask Attention Refinement with Sequential quadtree nodes) for instance segmentation of car damages. MARS employs self-attention mechanisms to capture global dependencies within sequential quadtree nodes and a quadtree transformer to recalibrate channel weights, resulting in highly accurate instance masks. Extensive experiments show that MARS significantly outperforms state-of-the-art methods like Mask R-CNN, PointRend, and Mask Transfiner on three popular benchmarks, achieving a +1.3 maskAP improvement with the R50-FPN backbone and +2.3 maskAP with the R101-FPN backbone on the Thai car-damage dataset. Demos are available at https://github.com/kaopanboonyuen/MARS.

tags:
- Attention
- Self-Attention
- MARS
- Sequential Quadtree Nodes
- Mask R-CNN
- PointRend
- Mask Transfiner

featured: true

links:
# - name: Videos
#   url: https://www.youtube.com/channel/UCNzeAAPyZaX4EDr720q5msg
# - name: ICML talk
#   url: https://www.facebook.com/watch/live/?v=355035025132741&ref=watch_permalink
# - name: IEEE Spectrum article
#   url: https://spectrum.ieee.org/tech-talk/computing/software/deepmind-teaches-ai-teamwork
- name: ACM
  url: https://dl.acm.org/doi/10.1007/978-3-031-51023-6_3
- name: ArXiv
  url: https://arxiv.org/pdf/2305.04743
url_pdf: https://link.springer.com/chapter/10.1007/978-3-031-51023-6_3
url_code: https://github.com/kaopanboonyuen/MARS
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