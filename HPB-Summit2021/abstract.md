# Open NeuroPET: enabling FAIR data sharing

*Cyril Pernet[^1], Melanie Ganz[^1], Martin Norgaard[^2], Russel Poldrack[^2], Douglas Greeve[^3], Paul Wighton[^3], Anthony Galassi[^4], Adam Thomas[^4], Robert Innis[^4], Gitte Moos Knudsen[^1]*

[^1] Neurobiology Research Unit, Rigshospitalet, Copenhagen, DK
[^2] Center for Reproducible Neuroscience, Stanford University, USA
[^3] Martinos Centre, Massachusetts General Hospital, USA
[^4] National Institure of Health, Bestesda, USA

## Goals

We aims primarily at developing brain PET data sharing openly (CC0) or securely (DUA-GDPR) with user friendly tools for PET [Brain Imaging Data Structure](https://bids.neuroimaging.io/) data curation [1]. Our secondary objective is to develop pipelines for automated QC and [molecular imaging template building](https://github.com/openneuropet/templates).  

## FAIR neuroPET data

**Find and Access data with nEurothenticate**: nEurothenticate is the future gateway for secured data sharing - also looking to serve EBRAINS infrastructure. User will be able to upload curated data along with a [Data User Agreement](https://open-brain-consent.readthedocs.io/en/stable/gdpr/data_user_agreement.html). Data are checked and pushed to EU restricted Cloud along the metadata using a jsonld file using [schema.org](https://schema.org/). Thanks to [DataLad](https://www.datalad.org/)[2], all metadata will be visible and platforms such as OpenNeuro or EBRAINS can list them, making them *Findable*  and *Accessible* worldwide. Because data are curated using BIDS, they are also *Interoperable* and *Reusable*. 

**GDPR governance**: Users have to register checking their IDs, which is the basis for accessing EU data. Having IDs, data can be accessed after signing the DUA and, if non-EU based, an additional [Standard Contractual Clauses Agreement](https://ec.europa.eu/info/law/law-topic/data-protection/international-dimension-data-protection/standard-contractual-clauses-scc_en). Users will be able to register institutions alowing to check the IT infrastructure is secured - see [Data Protection Impact Assessmement](https://gdpr.eu/data-protection-impact-assessment-template/), primarily to ensure data cannot be leaked. 

## PET BIDS converters

We have created Matlab(R) and Python converters available @https://github.com/openneuropet/BIDS-converter. Converters allow converting source ecat files to nifti+json. There are also tools to help converting metadata to json files. 

## References
[1] Norgaard M, Matheson GJ, Hansen HD, Thomas AG, Searle G, Rizzo G, Veronese M, Giacomel A, Yaqub M, Tonietto M, Funck T. PET-BIDS, an extension to the brain imaging data structure for positron emission tomography. bioRxiv. 2021 Jan 1.  
[2] Halchenko et al., (2021). DataLad: distributed system for joint management of code, data, and their relationship. Journal of Open Source Software, 6(63), 3262.  
