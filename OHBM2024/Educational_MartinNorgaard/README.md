# Molecular Imaging: A Hands-on Tutorial Based on Open Access Datasets (OHBM2024)

## Course Details
- **Submission Type:** Educational Course - Half Day (4 hours)  
- **Organizers:**
  - Arianna Sala, Université De Liège, Liege, Belgium
  - Igor Yakushev, Dept. of Nuclear Medicine, Technical University of Munich, Munich, Germany

## Presenters
- **Igor Yakushev**, Dept. of Nuclear Medicine, Technical University of Munich, Munich, Germany
- **Alessandra Bertoldo**, Padova Neuroscience Center, Padua, Italy
- **Arianna Sala**, Université De Liège, Liege, Belgium
- **Xin Di**, New Jersey Institute of Technology, Newark, USA
- **Martin Nørgaard, PhD**, University of Copenhagen, Copenhagen, Denmark
- **Granville Matheson**, Columbia University / Karolinska Institutet, USA / Sweden

## Overview
This half-day educational course introduces the essentials of molecular imaging, focusing on practical, hands-on experience using open-access datasets. The course is designed to expand participants' understanding of neuroimaging beyond traditional methods, emphasizing the integration of molecular features with connectomics.

## Detailed Session by Martin Nørgaard
- **Duration:** 40 minutes  
- **Topic:** PET Imaging of Neurotransmitter Systems: Access and Pre-processing (based on CIMBI or the OpenNeuro database)  
Martin Nørgaard will explore PET imaging of neurotransmitter systems, focusing on the COX-2 using the radiotracer [11C]MC1. This session will cover data acquisition from OpenNeuro, including essential preprocessing steps such as motion correction, registration, and segmentation. Participants will learn about the latest open-source tools like PETSurfer and PETPrep, empowering them to develop their own PET processing pipelines.

## Code
Using the [provided Jupyter notebook](./PET_preproc_tutorial_colab.ipynb) in this folder and [Google Colab](http://colab.research.google.com/), you will download a subset of a PET-BIDS dataset located on OpenNeuro (https://openneuro.org/datasets/ds004869/versions/1.0.1). Next, you will apply various PET preprocessing steps to the data using petprep_hmc for robust head motion correction and petprep_extract_tacs for co-registration, segmentation and extraction of time activity curves. 

## Educational Objectives
1. Understand the basic principles of brain molecular imaging.
2. Learn how to access and preprocess brain molecular imaging data.

## Target Audience
The course is designed for neuroimaging researchers at all levels of expertise who are keen to enhance their knowledge and skills in cutting-edge molecular imaging techniques.

## Interactive Components
Approximately 60% of the course time is dedicated to interactive elements, including live quizzes and hands-on sessions where participants engage in data preprocessing and quantification on their laptops.

## Diversity and Inclusion
The diverse panel of speakers and organizers from various stages of their careers and different international backgrounds ensures a rich, inclusive, and multi-perspective educational experience.

## Justification for Speaker Selection and Scientific Perspectives
The selection of speakers and the topics covered reflect OHBM’s commitment to diversity. The course utilizes a range of software tools and analytical perspectives, catering to a wide array of scientific interests and providing a comprehensive overview of the current landscape in molecular neuroimaging.
