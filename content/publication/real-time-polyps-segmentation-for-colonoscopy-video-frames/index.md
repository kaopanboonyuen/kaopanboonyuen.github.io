---
title: "Real-Time Polyps Segmentation for Colonoscopy Video Frames Using Compressed Fully Convolutional Network"
authors:
- I. Wichakam
- admin
- C. Udomcharoenchaikit
- P. Vateekul

date: "2018-02-01T00:00:00Z"
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
publishDate: "2018-02-01T00:00:00Z"

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ["1"]

# Publication name and optional abbreviated publication name.
publication: In *International Conference on Multimedia Modeling* **MMM 2018**
publication_short: In *International Conference on Multimedia Modeling* **MMM 2018**

abstract: Colorectal cancer is one of the leading causes of cancer death worldwide. As of now, colonoscopy is the most effective screening tool for diagnosing colorectal cancer by searching for polyps which can develop into colon cancer. The drawback of manual colonoscopy process is its high polyp miss rate. Therefore, polyp detection is a crucial issue in the development of colonoscopy application. Despite having high evaluation scores, the recently published methods based on fully convolutional network (FCN) require a very long inferring (testing) time that cannot be applied in a real clinical process due to a large number of parameters in the network. In this paper, we proposed a compressed fully convolutional network by modifying the FCN-8s network, so our network is able to detect and segment polyp from video images within a real-time constraint in a practical screening routine. Furthermore, our customized loss function allows our network to be more robust when compared to the traditional cross-entropy loss function. The experiment was conducted on CVC-EndoSceneStill database which consists of 912 video frames from 36 patients. Our proposed framework has obtained state-of-the-art results while running more than 7 times faster and requiring fewer weight parameters by more than 9 times. The experimental results convey that our system has the potential to support clinicians during the analysis of colonoscopy video by automatically indicating the suspicious polyps locations.

# Summary. An optional shortened abstract.
summary: Colorectal cancer is one of the leading causes of cancer death worldwide. As of now, colonoscopy is the most effective screening tool for diagnosing colorectal cancer by searching for polyps which can develop into colon cancer. The drawback of manual colonoscopy process is its high polyp miss rate. Therefore, polyp detection is a crucial issue in the development of colonoscopy application. Despite having high evaluation scores, the recently published methods based on fully convolutional network (FCN) require a very long inferring (testing) time that cannot be applied in a real clinical process due to a large number of parameters in the network. In this paper, we proposed a compressed fully convolutional network by modifying the FCN-8s network, so our network is able to detect and segment polyp from video images within a real-time constraint in a practical screening routine. Furthermore, our customized loss function allows our network to be more robust when compared to the traditional cross-entropy loss function. The experiment was conducted on CVC-EndoSceneStill database which consists of 912 video frames from 36 patients. Our proposed framework has obtained state-of-the-art results while running more than 7 times faster and requiring fewer weight parameters by more than 9 times. The experimental results convey that our system has the potential to support clinicians during the analysis of colonoscopy video by automatically indicating the suspicious polyps locations.

tags:
- Colorectal Cancer
- Fully Convolutional Network
- CVC-EndoSceneStill
- Colonoscopy Video

featured: true

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
url_pdf: https://link.springer.com/chapter/10.1007/978-3-319-73603-7_32
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