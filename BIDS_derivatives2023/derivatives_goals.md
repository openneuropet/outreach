# Goal

Obtain a consensus on what derivatives should be primarily for, offering a vision to drive BEPs. This in turn can be used as guideline into preparing the derivative BEP.  
  
Get ideas of the main roadblocks to address during the meeting.

# Method

For all attendees the following, we asked the following questions several weeks before the meeting:  
1. What is your vision for derivatives? (a vision is the non technical expression of what you want it to do, e.g. I can see output X being reused across labs for Y or output X can be easily reused by ML experts)  
2. There are two views on derivatives: A. it should store the outcome of a pipeline + share code B. it should document every steps, and thus store every step. --> what is your view? --> to help developing BEP derivatives, would it be useful to have a framework/guidelines considering the focus of derivatives i.e. re-usage?
3. Given your involvement in BIDS and derivatives, what is/are the current roadblocks to advance your project?
  
Answer were collected by email and compiled and assembled into broad categories.

# Results

## Vision
- provide upgraded raw data (from other people), using provenance tracking.
- provide well annotated, preprocessed data useful for direct use (by imaging people) or for mathematical modeling, machine learning, etc. (i.e. non imaging experts)
- standadized outcome format across pipelines/modalities (tsv and json, other) 

## Derivative endpoints
- document and store every step (2.5/13)
- outcomes of a pipeline + share code (10.5/13)
- guidelines for preparing a BIDS derivative dataset given common use cases

Note: pipelines can have multiple outcomes: averages, effect size maps, connectivity matrces, etc ..  while sharing code seems recommended we know it will not always happen - Guiomar made also made the point that reading the code can be tedious, therefore a well documented json of each step taken is highly recommended. If we consider that non imaging experts should be able to re-use derivatives, this is also what they need (i.e. almost all will understand what a frequency filter is, but would not stop that in a code)

*BIDS Validator*
- Yarik [recently proposed](https://github.com/bids-standard/bids-validator/issues/1676#issuecomment-1563185929) to Provide summary of how many files analyzed, have issues and ignored ; this strang discussion with Scientific Data as the streering group is trying to get journals to have something to indicate data are in BIDS.  
- In the same vein, Viviana mentioned that we could also provide a summary for derivatives, like numnber of outcomes and if the code available (implies the json of an outcome refer to a code in the code folder) - this also means that somehow pone would know the difference between an intermediate file (for QC) and an outcome file.
- Derivatives may have many values associated with a given key, should the validator only focus on keys and formats? 

## Roadblocks
- connectivity
- data formats (hd5, zarr?) --> https://github.com/bids-standard/bids-specification/issues/197
- adoption by software --> what can be done beyond containers for main software to adopt more widely BIDS
- producers vs. customers --> should derivatives to stored as producers make them or formated for future users (more hd5, tsv stuffs) 
- identify which outcomes in a workflow are useful - making them derivatives endpoints
- provenance; resharing data
- derivative nesting can challenging to follow both in term of metadata but also computationally
- surface objects not well surpported


