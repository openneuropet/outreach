# The OpenNeuroPET project: enabling FAIR data sharing for Positron Emission Tomography

*Cyril Pernet[^1], Melanie Ganz[^1], Martin Norgaard[^2], Russel Poldrack[^2], Douglas Greeve[^3], Paul Wighton[^3], Anthony Galassi[^4], Adam Thomas[^4], Robert Innis[^4], Gitte Moos Knudsen[^1]*

[^1] Neurobiology Research Unit, Rigshospitalet, Copenhagen, DK  
[^2] Center for Reproducible Neuroscience, Stanford University, USA  
[^3] Martinos Centre, Massachusetts General Hospital, USA  
[^4] National Institute of Mental Health, NIH, DHHS, Bethesda, MD, USA  

*Keywords*: positron emission tomography, data sharing, Brain Imaging Data Structure, data curation tools, molecular imaging templates

*HBP/EBRAINS*: Data and Knowledge, Atlases

## Goals

The [OpenNeuroPET](https://openneuropet.github.io/) project primary aim is to share and promote sharing of positron emission tomography (PET) brain imaging data according to the [Brain Imaging Data Structure (BIDS)](https://bids.neuroimaging.io/) [1] either openly (using a [CC0](https://creativecommons.org/share-your-work/public-domain/cc0/) license) or securely (following General Data Protection Regulation (GDPR) rules). To do so, we are developing a new informatic platform and user friendly tools for curating datasets. Our secondary objective is to develop pipelines for automated quality control (QC) and for [molecular imaging template building](https://github.com/openneuropet/templates).

## FAIR neuroPET data

**Find and Access data with nEurothenticate**: Our future nEurothenticate platform is the gateway for secured data sharing and its design is compatible with the [EBRAINS infrastructure](https://ebrains.eu/). User will be able to upload curated data along with a [Data Usage Agreement](https://open-brain-consent.readthedocs.io/en/stable/gdpr/data_user_agreement.html). Data are checked and pushed to a EU restricted cloud storage along with the metadata in jsonld format using [schema.org](https://schema.org/). Thanks to [DataLad](https://www.datalad.org/)[2], all metadata will be visible on [OpenNeuro](https://openneuro.org/) [3] but will be also visible for EBRAINS users, making them _**F**indable_  and _**A**ccessible_ worldwide. Because data are curated using BIDS, they are also _**I**nteroperable_ and _**R**eusable_ (FAIR [4]). 

**General Data Protection Regulation (GDPR) governance**: Users must register and provide personal identification, which is the basis for accessing GDPR-protected data. Once identification is provided, data can be accessed after signing a DUA. For users who are not based in the European Union (EU), an additional [Standard Contractual Clause Agreement](https://ec.europa.eu/info/law/law-topic/data-protection/international-dimension-data-protection/standard-contractual-clauses-scc_en) needs to be provided. Users will be able to register their institution to determine if the user's IT infrastructure is secured following the GDPR [Data Protection Impact Assessmement](https://gdpr.eu/data-protection-impact-assessment-template/).

## New tools for PET data curation

We have created PET BIDS converters in Matlab(R) and Python that are openly available for download at https://github.com/openneuropet/BIDS-converter. These tools allow ECAT files (a proprietary Siemens file format) to be converted to [NIfTI](https://nifti.nimh.nih.gov/) format with an additional JSON sidecar file containing necessary metadata. DICOM formatted files (used on other PET scanners such as the GE Advance) can be converted with any existing tools - for instance the widely-used [dcm2nixx](https://github.com/rordenlab/dcm2niix) tool written by Chris Rorden. For these DICOM formatted source files, we have provided additional tools to complement automatically the JSON sidecar files with the necessary BIDS metadata. We also made tools available in the [BIDS starter kit](https://github.com/bids-standard/bids-starter-kit/tree/main/matlabCode/pet) to help with converting PET metadata to JSON format.

## Available Atlases

Serotonin system (5-HTT, 5-HT1A, 5-HT1B, 5-HT2A, 5-HT4 [5][6]) and gamma-Aminobutyric acid system (BZR [7]) templates in MNI space are freely at https://github.com/openneuropet/templates. 

## References
[1] Norgaard M, et al. (2021). PET-BIDS, an extension to the brain imaging data structure for positron emission tomography. bioRxiv 2021.06.16.448390. 
[2] Halchenko et al., (2021). DataLad: distributed system for joint management of code, data, and their relationship. Journal of Open Source Software, 6(63), 3262.
[3] Markiewicz, C.J. et al. (2021). OpenNeuro: An open resource for sharing of neuroimaging data. bioRxiv 2021.06.28.450168.
[4] Wilkinson, M. et al. (2016). The FAIR Guiding Principles for scientific data management and stewardship. Sci Data 3, 160018.
[5] Beliveau, V. et al. (2017). A high-resolution in vivo atlas of the human brain's serotonin system. J Neurosci. 37, 120 - 128.
[6] Beliveau, V. et al. (2020). The Structure of the Serotonin System: a PET Imaging Study. NeuroImage, 205, 116240.
[7] Nørgaard, et al. (2021). A high-resolution in vivo atlas of the human brain's benzodiazepine binding site of GABAA receptors. NeuroImage, 232, 117878.
