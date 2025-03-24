# Nordic PET-BIDS Onboarding and ezBIDS Workshop - 28-29 August 2025

We would like to invite you to attend a free 2-day onboarding workshop for PET researchers in the Nordics to learn about the Brain Imaging Data Standard (BIDS) for PET data, and how to make use of this new standard for storage, sharing and processing.

Here is a very brief summary of BIDS for PET and the benefits it offers

* BIDS is the *de facto* community-decided standard for sharing PET data [REF]
      * Hence, by adapting to this standard, it will be easier to share data, and to re-use shared data
      * Open-sharing of research data through OpenNeuro requires BIDS data, but this can be tricky with GDPR
      * The new public-nEUro platform streamlines GDPR-compliant agreement-based data sharing using BIDS
* BIDS organises neuroimaging data in a manner which is both human-readable and machine-readable
      * In this way, all PET information which is not stored in image headers is stored with the image data.
      * This improves data re-use within groups as data can be more easily handed to new researchers.
* BIDS data is machine-readable, which gives rise to a growing number of BIDS Apps, which are tools which can automatically read and process BIDS data.
      * BIDS apps are "containerised" meaning they can be run from any operating system, without even requiring installation.
      * BIDS apps are typically run using only a single command.
      * As new methods and tools are developed, they are converted into BIDS apps, and they can be re-used directly on new BIDS data.


The goals of the workshop are to train attendees in the following:

* What BIDS is and how it can be beneficial for research infrastructure an reproducible analysis.
* How BIDS can simplify sharing of resarch data using both open-access and closed-access.
* How to set up and use open-source tools, including ezBIDS and PET2BIDS, to facilitate data curation.
      * ezBIDS is a domain-general graphical user interface which provides a code-free interface to data curation.
* How to install and use several recent BIDS Apps for PET data processing and analysis.
* Establish a community of Nordic PET researchers at various PET centres who can collaborate with one another and assist one another in their BIDS transitions.


## Schedule

#### Thursday 28 August: BIDS Introduction and ezBIDS tutorial


### Friday 29 August: PET-BIDS apps and PET-specific considerations





----------------------------------------------------------------------------------------------------
   **REGISTER VIA THIS [FORM](https://forms.gle/orGjjeJSNXYpcHAK7)**

----------------------------------------------------------------------------------------------------    
Brainhack Nordic follows the [BrainHack code of conduct](https://github.com/openneuropet/outreach/blob/main/Brainhack-Nordic2021/code_of_conduct.md) - make sure you have a read.  

----------------------------------------------------------------------------------------------------  
## [Location](https://github.com/openneuropet/outreach/blob/main/Brainhack-Nordic2024/location.md)

## [Team and contact](https://github.com/openneuropet/outreach/blob/main/Brainhack-Nordic2024/team.md)

## [Attendees](https://github.com/openneuropet/outreach/blob/main/Brainhack-Nordic2024/attendees.md)

## [keep in touch using the BrainHack Mattermost channel](https://mattermost.brainhack.org/brainhack/channels/bhg21-openneuropet)  

## Schedule

All times are CEST (GMT+1:00)

08.30 Morning serving for hungry people
09.00 Unconference
12.00 Lunch
13.00 Hack-away
15.00 Afternoon serving
16.30 End of the day

### January 22th: BIDS Educational Day

This day is devoted to onboarding and training for researchers covering the basics of the BIDS standard, as well as more focused hands-on sessions in the afternoon. 

- **Morning Session: The BIDS Standard**
   - Terminology and Data Structure: source, raw, derivatives
   - Generic tools

- **Afternoon Session: Parallel tracks**
   - *PET-BIDS*: hands-on demonstrations of BIDS tooling for PET data
      - Data Curation: Tools for helping you more easily convert your data to BIDS.
      - BIDS Apps: How to get the most out of your BIDS datasets, with existing and upcoming tools.

   - *BIDS derivatives:* organizing and describing outputs of computations performed on brain imaging data
      - Electrophysiology derivatives
      - MRI derivatives


### January 23th - 24th

These days are devoted to projects, getting help with applying lessons learned during the BIDS educational day, or anything else you want, in total unconference style. 

- Public nEUro: sharing data in Europe, short presentation and discussion

- Unconference: project based hacking, see [Projects](#projects)

## Projects
- Head modelling and applications (extending FEM for MEG head models in [SimNIBS](https://simnibs.org), and integrating SimNIBS head models into [MNE-Python](https://mne.tools))
- Creating a preliminary BIDS App PET for kinetic modelling using both invasive and non-invasive models based on *kinfitr*
- BIDS Atlas PEB development, work on 23rd already and 24th from 2pm PM -- [jisti meeting](https://meet.jit.si/BIDS_connectivity_project_meeting) @PeerHerhol
