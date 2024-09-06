---
title: "Semantic Segmentation On Medium-Resolution Satellite Images Using Deep Convolutional Networks With Remote Sensing Derived Indices"
authors:
- S. Chantharaj
- K. Pornratthanapong
- P. Chitsinpchayakun
- admin

date: "2018-01-01T00:00:00Z"
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
publishDate: "2018-01-01T00:00:00Z"

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ["1"]

# Publication name and optional abbreviated publication name.
publication: In *15th International Joint Conference on Computer Science and Software Engineering * **JCSSE 2018**
publication_short: In *15th International Joint Conference on Computer Science and Software Engineering * **JCSSE 2018**

abstract: Semantic Segmentation is a fundamental task in computer vision and remote sensing imagery. Many applications, such as urban planning, change detection, and environmental monitoring, require the accurate segmentation; hence, most segmentation tasks are performed by humans. Currently, with the growth of Deep Convolutional Neural Network (DCNN), there are many works aiming to find the best network architecture fitting for this task. However, all of the studies are based on very-high resolution satellite images, and surprisingly; none of them are implemented on medium resolution satellite images. Moreover, no research has applied geoinformatics knowledge. Therefore, we purpose to compare the semantic segmentation models, which are FCN, SegNet, and GSN using medium resolution images from Landsat-8 satellite. In addition, we propose a modified SegNet model that can be used with remote sensing derived indices. The results show that the model that achieves the highest accuracy RGB bands of medium resolution aerial imagery is SegNet. The overall accuracy of the model increases when includes Near Infrared (NIR) and Short-Wave Infrared (SWIR) band. The results showed that our proposed method (our modified SegNet model, named RGB-IR-IDX-MSN method) outperforms all of the baselines in terms of mean F1 scores.

# Summary. An optional shortened abstract.
summary: Semantic Segmentation is a fundamental task in computer vision and remote sensing imagery. Many applications, such as urban planning, change detection, and environmental monitoring, require the accurate segmentation; hence, most segmentation tasks are performed by humans. Currently, with the growth of Deep Convolutional Neural Network (DCNN), there are many works aiming to find the best network architecture fitting for this task. However, all of the studies are based on very-high resolution satellite images, and surprisingly; none of them are implemented on medium resolution satellite images. Moreover, no research has applied geoinformatics knowledge. Therefore, we purpose to compare the semantic segmentation models, which are FCN, SegNet, and GSN using medium resolution images from Landsat-8 satellite. In addition, we propose a modified SegNet model that can be used with remote sensing derived indices. The results show that the model that achieves the highest accuracy RGB bands of medium resolution aerial imagery is SegNet. The overall accuracy of the model increases when includes Near Infrared (NIR) and Short-Wave Infrared (SWIR) band. The results showed that our proposed method (our modified SegNet model, named RGB-IR-IDX-MSN method) outperforms all of the baselines in terms of mean F1 scores.

tags:
- Convolutional Neural Networks
- Semantic Segmentation
- Near Infrared (NIR)
- Short-Wave Infrared (SWIR)
- Remote Sensing

featured: false

links:
# - name: Videos
#   url: https://www.youtube.com/channel/UCNzeAAPyZaX4EDr720q5msg
# - name: ICML talk
#   url: https://www.facebook.com/watch/live/?v=355035025132741&ref=watch_permalink
# - name: IEEE Spectrum article
#   url: https://spectrum.ieee.org/tech-talk/computing/software/deepmind-teaches-ai-teamwork
# - name: ICIAP 2017 Best Papers
#   url: https://link.springer.com/chapter/10.1007/978-3-319-60663-7_18
url_pdf: https://ieeexplore.ieee.org/document/8457378/
url_code: https://github.com/kaopanboonyuen/
url_dataset: https://www.isprs.org/education/benchmarks/UrbanSemLab/2d-sem-label-vaihingen.aspx
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