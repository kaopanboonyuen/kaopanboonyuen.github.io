---
title: "Semantic Segmentation on Remotely Sensed Images Using Deep Convolutional Encoder-Decoder Neural Network"
authors:
- admin

date: "2020-01-01T00:00:00Z"
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
publishDate: "2020-01-01T00:00:00Z"

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ["7"]

# Publication name and optional abbreviated publication name.
publication: In *Chulalongkorn University* **Thesis Evaluation - Very Good Score (Outstanding Achievement)**
publication_short: In *Chulalongkorn University* **Thesis Evaluation - Very Good Score (Outstanding Achievement)**

abstract: One of the fundamental tasks in remote sensing is the semantic segmentation of the aerial and satellite images. It plays a vital role in applications, such as agriculture planning, map updates, route optimization, and navigation. The state-of-the-art model is the Deep Convolutional Encoder-Decoder (DCED). However, the accuracy is still limited since the architecture is not designed for recovering low-level features, e.g., river, low vegetation on remotely sensed images, and the training data in this domain are deficient. In this dissertation, we aim to propose the semantic segmentation architecture in five aspects, designed explicitly for the remotely sensed field. First, we propose applying a modern Convolutional Neural Network (CNN) called a Global Convolutional Network (GCN). Second, “channel attention” is presented to select the most discriminative filters (features). Third, “domain-specific transfer learning” is introduced to alleviate the scarcity issue. Fourth, “Feature Fusion (FF)” is added to our network to capture low-level features. Finally, “Depthwise Atrous Convolution (DA)” is introduced to refine the extracted features. The experiment was conducted on three data sets, two private corpora from Landsat-8 satellite and one public benchmark from the “ISPRS Vaihingen” challenge. The results showed that our proposed architectures outperformed the baseline model on any remote sensing imagery.

# Summary. An optional shortened abstract.
summary: My PhD thesis focuses on improving semantic segmentation of aerial and satellite images, a crucial task for applications like agriculture planning, map updates, route optimization, and navigation. Current models like the Deep Convolutional Encoder-Decoder (DCED) have limitations in accuracy due to their inability to recover low-level features and the scarcity of training data. To address these issues, I propose a new architecture with five key enhancements, a Global Convolutional Network (GCN) for improved feature extraction, channel attention for selecting discriminative features, domain-specific transfer learning to address data scarcity, Feature Fusion (FF) for capturing low-level details, and Depthwise Atrous Convolution (DA) for refining features. Experiments on Landsat-8 datasets and the ISPRS Vaihingen benchmark showed that my proposed architecture significantly outperforms the baseline models in remote sensing imagery.

tags:
- Convolutional Neural Networks
- Landsat-8
- Deep Learning
- Semantic Segmentation
- High-Resolution Imagery
- Aerial Imagery
- Global Convolutional Network
- Encoder-Decoder Networks
- ISPRS Vaihingen
- Transfer Learning
- Domain Adaptation
- Channel Attention
- Depthwise Atrous Convolution
- Feature Fusion
- Remote Sensing

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
url_pdf: https://digital.car.chula.ac.th/chulaetd/8534/
url_code: https://github.com/kaopanboonyuen/FusionNetGeoLabel
url_dataset: https://www.isprs.org/education/benchmarks/UrbanSemLab/2d-sem-label-vaihingen.aspx
url_poster: ''
url_project: https://kaopanboonyuen.github.io/FusionNetGeoLabel/
url_slides: https://kaopanboonyuen.github.io/files/panboonyuen_phd_defense_2020.pdf
url_source: https://kaopanboonyuen.github.io/files/picture/phd_defense_day.jpg
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