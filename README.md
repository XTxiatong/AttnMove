# AttnMove
This is the code for submission #8692 in AAAI2020 


## Datasets

The geolife data to evaluate our model, which contains 40 users and ready for directly used. 

## Requirements

- Python 3.6
- TF-1.18

## Project Structure

- /data # preprocessed
  - pos.train.txt
  - pos.validate.txt
  - pos.test.txt
  - pos.vocab.txt
  - region_data
    - region_distance_no_less10.npy
    - region_beijing_grid2region_REID_no_less10.json
- /model # AttnMove
  - main.py
  - dataset_utils.py
  - Embedder.py
  - model_utils.py
  - self_attn_hyperaram_region.py
- /baseline #codes for baselines 
  - baseline.py
  - dataset_utils.py
  - Embedder.py
  - model_utils.py
  - self_attn_hyperaram_region.py
- /log #save dir
  - analyse_data # save attention map & location embedding

## Usage for AttnMove
```
python3 main.py --blank_num 10 --if_history 1 --hidden_dim 64 --bleu_interval 5 --nhead 1 --nlayer 2 --reg_lambda 1e-2 --gpu 4 --if_mask 1 --drop 0.3 --fb_drop 0.3
```

The codes contain four network model (AttnMove, AttnMove-H) and baseline model (LSTM, Bi-LSTM, DeepMove)
