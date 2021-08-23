# The OpenNeuroPET Project

---
## Title

OpenNeuroPET: Campaign to Combat PET Data Entropy

## Body
At present there exists little standardization between/within PET neuroimaging data produced by researchers; analysis tools and methods are often as unique and inaccessible as the data they are used on. This can lead to irreproducibility and duplication of work within the community. Two notable efforts towards data standardization within the general neuroimaging community have been the development of the BIDS standard and, more specifically to PET, the publishing of the "Consensus Nomenclature for in 
vivo Imaging of Reversibly Binding Radioligands" by Innis et. al. [1]. 

OpenNeuroPET builds off of the aforementioned efforts and seeks to introduce a data standard for and a platform to share and distribute PET Neuroimaging data. The data standard utilized in OpenNeuroPET is built around the Brain Imaging Data Standard (BIDS) [2] and specifically customized for PET data [3]. The OpenNeuro platform [4] serves as insipration for the data sharing aspect. It aims at developing data sharing openly (CC0) with a united front-end and user friendly tools for the BIDS based data curation of data. OpenNeuroPET extends OpenNeuro's data sharing aspect to include curation of multimodal and specifically PET data as well as to add a secure data sharing feature (GDPR-DUA) in order to enable access to data that can not be shared openly.

OpenNeuroPET is currently introducing PET Preprocessing derivatives into the BIDS standard with BEP 023 [5]. Additionally, OpenNeuroPET has developed PET Neuroimaging and metadata conversion software from image and tabular formats such as DICOM, ECAT, csv, and xlsx into BIDS compliant formats with Matlab and Python [6].

OpenNeuroPET continues to work on improving OpenNeuro.org to better support PET, and is working with popular neuroimaging libraries, such as Nibabel and Freesurfer (via PetSurfer), to better support PET both within and outside of the PET BIDS standard. Simultaneously, OpenNeuroPET is seeking and solicating PET experts to educate and collaborate with in these efforts.

## References

[1] Innis RB, Cunningham VJ, Delforge J, Fujita M, Gjedde A, Gunn RN, Holden J, Houle S, Huang SC, Ichise M, Iida H. Consensus nomenclature for in vivo imaging of reversibly binding radioligands. Journal of Cerebral Blood Flow & Metabolism. 2007 Sep;27(9):1533-9.

[2] Gorgolewski KJ, Auer T, Calhoun VD, Craddock RC, Das S, Duff EP, Flandin G, Ghosh SS, Glatard T, Halchenko YO, Handwerker DA. The brain imaging data structure, a format for organizing and describing outputs of neuroimaging experiments. Scientific data. 2016 Jun 21;3(1):1-9.

[3] Norgaard M, Matheson GJ, Hansen HD, Thomas AG, Searle G, Rizzo G, Veronese M, Giacomel A, Yaqub M, Tonietto M, Funck T. PET-BIDS, an extension to the brain imaging data structure for positron emission tomography. bioRxiv. 2021 Jan 1.

[4] Gorgolewski K, Esteban O, Schaefer G, Wandell B, Poldrack R. OpenNeuro—a free online platform for sharing and analysis of neuroimaging data. Organization for human brain mapping. Vancouver, Canada. 2017 Jun;1677(2).

 [5] https://bids.neuroimaging.io/bep023
 
 [6] https://github.com/openneuropet/BIDS-converter 
