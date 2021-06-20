# Open Science Room Discussion Topics
This is a brief outline of some of the subjects that we at OpenNeuroPet wish to highlight and discuss during an open science room
at this years OHBM meeting, that is if we are able to secure a room.

**PET BIDS Topic List**

- BEP 009
- The addition of PED data into Open Neuro ~> coming soon datasets from the NRU and NIMH
- Some brief overview of what makes PET data unique (meta data examples, ecat, dicom, etc)


## Bids Extension Proposal 009

### Meat and Potatoes
- As of April 7th 2021 PET data is now accepted/incorporated into the BIDS standard
- Special kudos to Melanie Ganz, Martin Norgaard, Cyril Pernet, Adam Thomas, and Robert Innis of Open Neuro PET and these many others shown here -> Granville J. Matheson, Hanne D. Hansen, Graham Searle, Gaia Rizzo, Mattia Veronese, Alessio Giacomel, Maqsood Yaqub, Matteo Tonietto, Thomas Funck, Ashley Gillman, Hugo Boniface, Alexandre Routier, Jelle R. Dalenberg, Tobey Betthauser, Franklin Feingold, Christopher J.6Markiewicz, Krzysztof J. Gorgolewski, Ross W. Blair, Stefan Appelhoff, Remi Gau,Taylor Salo, Guiomar Niso, Christophe Phillips, Robert Oostenveld, Jean-Dominique Gallezot, Richard E. Carson, Gitte M. Knudsen
- Additionally a preprint of the accompanying article has been released at `bioRxiv` [here](https://www.biorxiv.org/content/10.1101/2021.06.16.448390v1)

### Some pre-history/pre-BIDS

Previous work in the adoption of better standards and practices initially started in 2007 with the publishing of the following paper:  
- Innis, R. B.et al.Consensus nomenclature for in vivo imaging of reversibly binding radioligands.J. Cereb. Blood Flow &240Metab.27, 1533–1539 (2007)

## OpenNeuro PET

### On the database side

BIDSified PET data has existed on OpenNeuro for at least the past 3 years with an upload of some examples from the CIMBI dataset, additional datasets have slowly
been added. It is the current intent of OpenNeuro and researchers at the NIMH, NRU at the University of Copenhagen, and at Stanford to convert more datasets into
bids (now that it exists) and make those datasets publicly available on OpenNeuro. Emphasis on coming soon, special mention to Martin Norgaard as he has 300-400 
subjects converted.

### Concerning Tools, Methods, and other On Going Efforts

Stuff that works great for PET:
- [bids-validator](https://github.com/bids-standard/bids-validator)


At the present OpenNeuroPET is working to develop better support for PET BIDS in the form of:

- [BIDS Starter kit stuff](https://github.com/bids-standard/bids-starter-kit/)
    - [documentation on how to convert data sets to bids](https://github.com/bids-standard/bids-starter-kit/wiki/Creating-a-BIDS-compatible-PET-dataset)
    - [Buildng requered BIDS metadata text files from a PET dataset](https://github.com/CPernet/bids-starter-kit/tree/main/matlabCode)
- a matlab converter [here](https://github.com/CPernet/bids-starter-kit/tree/main/matlabCode)
- a python converter [here](https://github.com/bendhouseart/BespokeBIDSConverters/tree/nimh-dataset-1)

Additional work being done to better integrate PET bids PET into community:
- Better support for PET and BIDS PET in [Nibabel](), [Pybids]()
-  

