store_dir='../result'
dataset='prism'
sample_num=5

nohup python -u QA.py --prompt_num 1  \
            --QA_num $sample_num  \
            --dataset $dataset \
            --output_dir $store_dir \
            1> ../records/log_sample.txt 2>&1 &