Considering the privacy issue, we cannot publish our Tencent dataset. Here we give the codes for data preprocessing. To re-implement the experiments, you can download Geolife dataset from https://www.microsoft.com/en-us/download/details.aspx?id=52367. 

Geolife dataset:
  - pos.train.txt
  - pos.validate.txt
  - pos.test.txt
  - pos.vocab.txt
  - region_data
    - region_distance_no_less10.npy
    - region_beijing_grid2region_REID_no_less10.json


Each line the the processed trajectory consists of UID, Time, and 6 traces:
- UID: 0	
- Time: 20090611	
- H1: 9 26 9 9 26 1177 26 9 9 * 9 9 9 9 9 9 9 26 9 9 9 26 2315 9 4237 9 9 26 26 9 26 26 26 26 26 26 26 26 26 26 * * 26 * 26 * 26 26  
- H2: 9 26 9 9 26 1177 26 9 9 * 9 9 9 9 9 9 9 26 9 9 9 26 2315 9 4237 9 9 26 26 9 26 26 26 26 26 26 26 26 26 26 * * 26 * 26 * 26 26  
- H3:9 26 9 9 26 1177 26 9 9 * 9 9 9 9 9 9 9 26 9 9 9 26 2315 9 4237 9 9 26 26 9 26 26 26 26 26 26 26 26 26 26 * * 26 * 26 * 26 26  
- D1: * * 9 9 * 9 871 6248 * * * * 6248 641 3802 3562 4573 9 * * * * * * * * * * 871 116 116 * * * * * * * * * * * * * 9 26 * *  
- D2: * * 9 9 * 9 871 6248 * * * * 6248 641 3802 3562 4573 9 * * * * * * * * * * 871 116 116 * * * * * * * * * * * * * 9 26 * *  
- Mask: * * 9 \<m> * 9 \<m> \<m> * * * * 6248 \<m> 3802 \<m> \<m> 9 * * * * * * * * * * 871 \<m> \<m> * * * * * * * * * * * * * \<m> \<m> * * 
  
Each trace is one day's trajectory: a sequence of 48 locations (one point per half hour), with * denoting the records are missing from raw data. 
  
H1, H2 and H3 are max pooling histories (they are repeated).
  
D1 and D2 are the trajectory of the target day (they are repeated).
  
Mask with <m> presents the location to be recovered. 
  
