## Initial Concern
I want to understand the purpose of the competition. I understand the rule is to find the largest overlap between my answer and test set. However, I have a few concerns from a biology point of view. From my experience of manually counting cells/nuclei as a graduate student, I feel the current training label may not generate beneficial model for the academic research community. 

## It is most useful for a biologist to:
1. Count the number of nuclei
2. Find the area (average) of nuclei
3. Find the abnormal nuclei, which are usually not roundish shape. 

## The current label have these issues:
1. Overlapping cells were not counted as separate cells. This will underestimate the number of nuclei.
2. Partially cut-off nuclei on all 4 edges are counted. This will overestimate the number of nuclei and underestimate the average nucleus size. First talked about by Abercrombie (1946), counting/sampling this way make you double count 1/2 nuceli and introduce systematic errors. Counting smaller cells will obviously lower the average cell size. A better way is only count 2 edges systematically, e.g. only count top and right edge cells. Alternative approach is to not count edge cells for more accurate size estimation.
3. There are smaller polygons inside of larger polygons. Again, this will overestimate cell number and underestimate cell size (ONUS). For fluorescent images, smaller circles inside larger circles should be ignored. 
4. Multiple nuclei clumped together are counted as separate smaller nuclei. ONUS. The clumps are mostly likely one nuclei atropy/broke down into smaller pieces. They should be counted as one small nucleus. 

## Ending remark
I hope you could change the label for training or at least change the label for testing. Please let people know that if models are made using the current label, the model is not going to be useful to any biologist. We cannot expect an average biologist to be able to modify the code or re-train the model according to their liking. At the very least I hope you can give an prize incentive for people who train alternative models using the more researcher friendly label.
Thank you for your time. 

Former Biologist

## Preference:
Abercrombie, M., M. L. Johnson  1946  Quantitative histology of Wallerian degeneration I. Nuclear population in rabbit sciatic nerve. J. Anat. Lond. vol. 80, pp. 37-50.
