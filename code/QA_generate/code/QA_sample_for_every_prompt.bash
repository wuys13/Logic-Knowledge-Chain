# bash QA_sample_for_every_prompt.sh 
store_dir='../result'
dataset='prism'
sample_num=5

for i in {1..3}; 
    do 
    nohup python -u QA.py --prompt_num $i  \
                --QA_num $sample_num  \
                --dataset $dataset \
                --output_dir $store_dir \
                1> ../records/${dataset}_${i}.txt 2>&1 &
    done