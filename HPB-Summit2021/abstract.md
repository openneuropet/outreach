# Open NeuroPET: enabling FAIR data sharing

*Cyril Pernet[^1], Melanie Ganz[^1], Martin Norgaard[^2], Russel Poldrack[^2], Douglas Greeve[^3], Paul Wighton[^3], Anthony Galassi[^4], Adam Thomas[^4], Robert Innis[^4], Gitte Moos Knudsen[^1]*

[^1] Neurobiology Research Unit, Rigshospitalet, Copenhagen, DK
[^2] Center for Reproducible Neuroscience, Stanford University, USA
[^3] Martinos Centre, Massachusetts General Hospital, USA
[^4] National Institute of Mental Health, NIH, DHHS, Bethesda, MD, USA

## Goals

Our aim is to develop methods to either openly (using a [CC0](https://creativecommons.org/share-your-work/public-domain/cc0/) license) or securely (using a General Data Protection Regulation (GDPR) compliant Data Use Agreement (DUA)) share positron emission tomography (PET) brain imaging data according to the [Brain Imaging Data Structure (BIDS)](https://bids.neuroimaging.io/) [1] accompanied by user friendly tools for curating BIDS datasets. Our secondary objective is to develop pipelines for automated quality control (QC) and [molecular imaging template building](https://github.com/openneuropet/templates).

## FAIR neuroPET data

**Find and Access data with nEurothenticate**: Our future nEurothenticate platform will be the gateway for secured data sharing. Its design is compatible with the already existing [EBRAINS infrastructure](https://ebrains.eu/). Users will be able to upload curated data along with a [Data Usage Agreement](https://open-brain-consent.readthedocs.io/en/stable/gdpr/data_user_agreement.html). Data are checked and pushed to a EU restricted cloud storage along with metadata in jsonld format using [schema.org](https://schema.org/). Thanks to [DataLad](https://www.datalad.org/)[2], all metadata will be visible on OpenNeuro (https://openneuro.org/) [3] and will be also visible to EBRAINS users, making them *Findable* and *Accessible* (FAIR) worldwide. Additionaly, since datasets are curated using BIDS, they are also *Interoperable* and *Reusable*. 

**GDPR governance**: Users must register and provide personal identification, which is the basis for accessing GDPR-protected data. Once identification is provided, data can be accessed after signing a DUA. For users who are not based in the European Union (EU), an additional [Standard Contractual Clause Agreement](https://ec.europa.eu/info/law/law-topic/data-protection/international-dimension-data-protection/standard-contractual-clauses-scc_en) needs to be provided. Users will be able to register their institution to determine if the user's IT infrastructure has been assessed as being secure. See the GDPR guidance on how to conduct a [Data Protection Impact Assessmement](https://gdpr.eu/data-protection-impact-assessment-template/) to minimize chance of unauthorized data access.

## Existing tools for PET data

We have created PET BIDS converters in Matlab(R) and Python that are publically available for download: @https://github.com/openneuropet/BIDS-converter. These tools allow ECAT files (a proprietary Siemens file format) to be converted to [NIfTI](https://nifti.nimh.nih.gov/) format with an additional JSON sidecar file containing necessary metadata. DICOM formatted files (used on other PET scanners such as the GE Advance) can be converted with the existing and widely-used (dcm2nixx)[https://github.com/rordenlab/dcm2niix] tool written by Mike Rorden. For these DICOM formatted source files, we have provided additional tools and templates to add additional necessary BIDS metadata to the JSON sidecar files. There are additional tools available in the [BIDS starter kit](https://github.com/bids-standard/bids-starter-kit/tree/main/matlabCode/pet) which help with converting PET metadata to JSON format.

## References
[1] Norgaard M, Matheson GJ, Hansen HD, Thomas AG, Searle G, Rizzo G, Veronese M, Giacomel A, Yaqub M, Tonietto M, Funck T. PET-BIDS, an extension to the brain imaging data structure for positron emission tomography. bioRxiv. 2021 Jan 1.
[2] Halchenko et al., (2021). DataLad: distributed system for joint management of code, data, and their relationship. Journal of Open Source Software, 6(63), 3262.
[3] Christopher J. Markiewicz, Krzysztof J. Gorgolewski, Franklin Feingold, Ross Blair, Yaroslav O. Halchenko, Eric Miller, Nell Hardcastle, Joe Wexler, Oscar Esteban, Mathias Goncalves, Anita Jwa, Russell A. Poldrack (2021). OpenNeuro: An open resource for sharing of neuroimaging data. bioRxiv 2021.06.28.450168.
