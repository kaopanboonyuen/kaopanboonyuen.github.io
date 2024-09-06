---
title: "A Performance Comparison between GIS-based and Neuron Network Methods for Flood Susceptibility Assessment in Ayutthaya Province"
authors:
- T. Vajeethaveesin
- admin

date: "2022-01-01T00:00:00Z"
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
publishDate: "2022-01-01T00:00:00Z"

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ["2"]

# Publication name and optional abbreviated publication name.
publication: In *Trends in Sciences (Trends Sci. or TiS)*
publication_short: In *Trends in Sciences (Trends Sci. or TiS)*

abstract: Flooding has been a long withstanding issue in Thailand. Due to its geographical setup, mitigation and management of floods are challenging and hard to execute. One of the tools used in managing the events is “flood susceptibility mapping,” in which an incident probability as well as a rescue path is estimated and planned. To create one, the traditional GIS method called FRAM (flood risk assessment model), combined with AHP (analytical hierarchy process), is used and implemented on ArcGIS software. In this method, we first created a comparison table to compute weights for each of the selected factors. Then the computed weights were used in the FRAM model in ArcGIS to create a flood susceptibility map for each region. Each region was then classified as very high, high, medium, low, and very low risk. On the other hand, in computer science, machine learning and AI are prevalent and being adopted to various domains, promising the effectiveness of the method, potentially beat the forementioned traditional method. Therefore, ANN (artificial neural network) is adopted in this work to create the flood susceptibility map. The ANN technique is developed by using causal factors. The ANN classifies areas as either flood areas or flood-free areas. The 2 methods from different disciplines (GIS and Computer Science) are applied and described in this paper with the intention to prove whether the machine learning is really efficient and can outperform the traditional GIS approach. Data on Thailand’s Ayutthaya Province is used in this work as a case study - in order to assess flood prone areas and compared for performance evaluation. Both of which use the 6 selected factors according to the literature, (i) flow accumulation, (ii) elevation, (iii) land use, (iv) rainfall intensity, (v) slope and (vi) soil types. The results from the 2 methods were verified with historical flood data and compared. The results showed that ANN (obtained via sensitivity analysis) outperformed the FRAM with precision of 79.90 %, recall of 79.04 %, F1-score of 79.08 % and accuracy of 79.31 %. In addition, we found that (according to our ANN experiments) the main causal factors related to flood susceptibility map only included 3 factors, flow accumulation, elevation, and soil types. Therefore, the proposed methodology for assessment of flood susceptibility areas using these 3 factors could be considered sufficient and applied to other regions in related applications, when needed.

# Summary. An optional shortened abstract.
summary: Flooding poses a significant challenge in Thailand due to its complex geography, traditionally addressed through GIS methods like the Flood Risk Assessment Model (FRAM) combined with the Analytical Hierarchy Process (AHP). This study assesses the efficacy of Artificial Neural Networks (ANN) in flood susceptibility mapping, using data from Ayutthaya Province and incorporating 5-fold cross-validation and Stochastic Gradient Descent (SGD) for training. ANN achieved superior performance with precision of 79.90%, recall of 79.04%, F1-score of 79.08%, and accuracy of 79.31%, outperforming the traditional FRAM approach. Notably, ANN identified that only three factors—flow accumulation, elevation, and soil types—were crucial for predicting flood-prone areas. This highlights the potential for ANN to simplify and enhance flood risk assessments. Moreover, the integration of advanced machine learning techniques underscores the evolving capability of AI in addressing complex environmental challenges.

tags:
- Remote Sensing
- Flood Susceptibility Assessment
- Machine Learning
- Artificial Neural Networks
- GIS

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
url_pdf: https://tis.wu.ac.th/index.php/tis/article/view/2038
url_code: https://github.com/kaopanboonyuen/rainfall-prediction-a-machine-learning-approach
url_dataset: ''
url_poster: ''
url_project: 'https://kaopanboonyuen.github.io/rainfall-prediction-a-machine-learning-approach'
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