# Goal

Obtain a consensus on what derivatives should be primarily for, offering a vision to drive BEPs. This in turn can be used as guideline into preparing the derivative BEP.  
  
Get ideas of the main roadblocks to address during the meeting.

# Method

For all attendees the following, we asked the following questions several weeks before the meeting:  
1. What is your vision for derivatives? (a vision is the non technical expression of what you want it to do, e.g. I can see output X being reused across labs for Y or output X can be easily reused by ML experts)  
2. There are two views on derivatives: A. it should store the outcome of a pipeline + share code B. it should document every steps, and thus store every step. --> what is your view? --> to help developing BEP derivatives, would it be useful to have a framework/guidelines considering the focus of derivatives i.e. re-usage?
3. Given your involvement in BIDS and derivatives, what is/are the current roadblocks to advance your project?
  
Answer were collected by email and compiled and assembled into broad categories using Cyrils' totally subjective judgement. 

# Results

## Vision
- provide upgraded raw data (from other people), using provenance tracking.
- provide well annotated, preprocessed data useful for direct use (by imaging people) or for mathematical modeling, machine learning, etc. (i.e. non imaging experts)
- standadized outcome format across pipelines/modalities (tsv and json, key-values for commonly used stuff, e.g. motion correction vs realignement, registration vs normalization, etc ... define *common vocabulary* as we did for raw)
- provenance (combinatorial complexity, no point trying to code it all)

## Derivative endpoints
- document and store every step (2.5/16)
- outcomes of a pipeline + share code (13.5/16)

Note: pipelines can have multiple outcomes: averages, effect size maps, connectivity matrces, etc ..  while sharing code seems recommended we know it will not always happen - Guiomar made also made the point that reading the code can be tedious, therefore a well documented json of each step taken is highly recommended. If we consider that non imaging experts should be able to re-use derivatives, this is also what they need (i.e. almost all will understand what a frequency filter is, but would not stop that in a code) -- we all agree on this anyway.

-> also have to think of the resources (too many steps saved, who will host that?)

*guidelines for preparing a BIDS derivative*
- different use cases to be adressed: minimal 1 outcome, then add intermediate steps
- common vocabulary for commonly used analyses (image and electrophy)s
   
*BIDS Validator*
- Derivatives may have many values associated with a given key, should the validator only focus on some keys and formats given the ‘infinity’ of possible transforms?
- Yarik [recently proposed](https://github.com/bids-standard/bids-validator/issues/1676#issuecomment-1563185929) to Provide summary of how many files analysed, have issues and ignored ; this came from a discussion with Scientific Data as the steering group is trying to get journals to have something to indicate data are in BIDS.
- In the same vein, Viviana mentioned that we could also provide a summary for derivatives, like number of outcomes and if the code is available (implies the json of an outcome refer to a code in the code folder)


## Roadblocks
- connectivity
- data formats (hd5, zarr?) --> https://github.com/bids-standard/bids-specification/issues/197
- adoption by software --> what can be done beyond containers for main software to adopt more widely BIDS, can sofware start implementing naming, json + provenance?
- producers vs. customers --> Should derivatives to stored as producers make them or formatted for future users (more hd5, tsv stuffs), can we even predict future users?
- identify which outcomes in a workflow are useful - making them derivatives endpoints
- provenance; resharing data
- derivative nesting can challenging to follow both in terms of metadata but also computationally
- surface objects not well supported
- clarify raw vs source for scanner obtained images --> T1w with gradient non linearity correction is raw, yet this is a post-hoc correction, same thing with the UNIT image from MP2RAGE, even the phasediff image is computed post-hoc and it is stored in raw. The common view being whatever comes out of the scanner is raw, and this should be formalized. FA, ADC, MD and CBF maps for instance, because somehow from time series tend to be seen as derivative.
- file system constrains producing too much derivatives


