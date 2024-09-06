---
title: "MeViT: A Medium-Resolution Vision Transformer for Semantic Segmentation on Landsat Satellite Imagery for Agriculture in Thailand"
authors:
- admin
- C. Charoenphon
- C. Satirapod

date: "2023-05-01T00:00:00Z"
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
publishDate: "2023-05-01T00:00:00Z"

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ["2"]

# Publication name and optional abbreviated publication name.
publication: In *Remote Sensing* **Impact Factor 4.2**
publication_short: In *Remote Sensing* **Impact Factor 4.2**

abstract: Semantic segmentation is a fundamental task in remote sensing image analysis that aims to classify each pixel in an image into different land use and land cover (LULC) segmentation tasks. In this paper, we propose MeViT (Medium-Resolution Vision Transformer) on Landsat satellite imagery for the main economic crops in Thailand as follows (i) para rubber, (ii) corn, and (iii) pineapple. Therefore, our proposed MeViT enhances vision transformers (ViTs), one of the modern deep learning on computer vision tasks, to learn semantically rich and spatially precise multi-scale representations by integrating medium-resolution multi-branch architectures with ViTs. We revised mixed-scale convolutional feedforward networks (MixCFN) by incorporating multiple depth-wise convolution paths to extract multi-scale local information to balance the model’s performance and efficiency. To evaluate the effectiveness of our proposed method, we conduct extensive experiments on the publicly available dataset of Thailand scenes and compare the results with several state-of-the-art deep learning methods. The experimental results demonstrate that our proposed MeViT outperforms existing methods and performs better in the semantic segmentation of Thailand scenes. The evaluation metrics used are precision, recall, F1 score, and mean intersection over union (IoU). Among the models compared, MeViT, our proposed model, achieves the best performance in all evaluation metrics. MeViT achieves a precision of 92.22%, a recall of 94.69%, an F1 score of 93.44%, and a mean IoU of 83.63%. These results demonstrate the effectiveness of our proposed approach in accurately segmenting Thai Landsat-8 data. The achieved F1 score overall, using our proposed MeViT, is 93.44%, which is a major significance of this work.

# Summary. An optional shortened abstract.
summary: In this paper, we present MeViT (Medium-Resolution Vision Transformer), designed for semantic segmentation of Landsat satellite imagery, focusing on key economic crops in Thailand para rubber, corn, and pineapple. MeViT enhances Vision Transformers (ViTs) by integrating medium-resolution multi-branch architectures and revising mixed-scale convolutional feedforward networks (MixCFN) to extract multi-scale local information. Extensive experiments on a public Thailand dataset demonstrate that MeViT outperforms state-of-the-art deep learning methods, achieving a precision of 92.22%, recall of 94.69%, F1 score of 93.44%, and mean IoU of 83.63%. These results highlight MeViT's effectiveness in accurately segmenting Thai Landsat-8 data.

tags:
- Remote Sensing
- Landsat-8
- Deep Learning
- Semantic Segmentation
- High-Resolution Imagery
- Convolutional Neural Networks
- Encoder-Decoder Networks
- Vision Transformers
- Transformer
- Multi-branch Architectures
- Mixed-scale Convolutional Feedforward Networks


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
url_pdf: https://www.mdpi.com/2072-4292/15/21/5124
url_code: https://github.com/kaopanboonyuen/MeVit
url_dataset: ''
url_poster: ''
url_project: 'https://kaopanboonyuen.github.io/MeViT/'
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