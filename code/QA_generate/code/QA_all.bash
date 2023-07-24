store_dir='../result'
dataset='prism'

nohup python -u QA.py --prompt_num 1  \
            --QA_num -1  \
            --dataset $dataset \
            --output_dir $store_dir \
            1> ../records/log_all.txt 2>&1 &