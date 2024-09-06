---
title: "Image Vectorization of Road Satellite Data Sets"
authors:
- admin
- P. Vateekul

- S. Lawawirojwong

date: "2016-09-01T00:00:00Z"
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
publishDate: "2016-04-01T00:00:00Z"

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ["2"]

# Publication name and optional abbreviated publication name.
publication: In *Journal of Remote Sensing and GIS Association of Thailand* **RESGAT**
publication_short: In *Journal of Remote Sensing and GIS Association of Thailand* **RESGAT**

abstract: Data extraction of geo-spatial objects from satellite images is a crucial step in facilitating analysis of geo-spatial or spatio-temporal data, typically involving line (road) and polygon (area) layers. This paper introduces a method for transforming satellite data (raster images) containing roads from pixel form into spatial objects comprising lines and polygons. Our algorithm consists of three primary steps. First, roads are isolated from other objects using k-means clustering. Second, line extraction is performed on the road areas by applying morphological operations to skeletonize the image, followed by enhancement using the Ramer-Douglas-Peucker algorithm. Finally, land-cover classification is applied to non-road objects to extract polygons. Experimental results demonstrate that both lines (road networks) and polygons (areas) can be accurately extracted from satellite imagery simultaneously.

# Summary. An optional shortened abstract.
summary: Data extraction of geo-spatial objects from satellite images is a crucial step in facilitating analysis of geo-spatial or spatio-temporal data, typically involving line (road) and polygon (area) layers. This paper introduces a method for transforming satellite data (raster images) containing roads from pixel form into spatial objects comprising lines and polygons. Our algorithm consists of three primary steps. First, roads are isolated from other objects using k-means clustering. Second, line extraction is performed on the road areas by applying morphological operations to skeletonize the image, followed by enhancement using the Ramer-Douglas-Peucker algorithm. Finally, land-cover classification is applied to non-road objects to extract polygons. Experimental results demonstrate that both lines (road networks) and polygons (areas) can be accurately extracted from satellite imagery simultaneously.

tags:
- Remote Sensing
- Road Segmentation
- Spatio-Temporal Data
- High-Resolution Imagery
- Aerial Imagery
- K-Means Clustering
- Ramer-Douglas-Peucker

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
url_pdf: https://learn.gistda.or.th/wp-content/uploads/2017/06/GISTDA-Research-Image-Understaning-2559-Image-Vectorization.pdf
url_code: https://github.com/kaopanboonyuen/
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