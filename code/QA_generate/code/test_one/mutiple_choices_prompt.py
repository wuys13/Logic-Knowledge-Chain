import openai
import os

openai.api_key = "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"

text = f"""
Axitinib'EOL-1'inhibition'CTRPv2'1'waterfall
"""

prompt = f"""
This is a task of generating a multiple choice question and answer pair in a high-quality bio-medical qualification examination.\

You will be provided with single quote structured text, whose structure is as follows:\
entity1'entity2'relationship'dataset'number'methods\

It means that in the dataset, it has been proved that using the 'methods' we could get the 'relationship' between 'entity1' and 'entity2'. If the 'relatonship' is significant, the 'number' will be 1 and 0 otherwise. \

Suppose you are an expert in the clinical field of medicine, you will get the final multiple choice question and answer pair by following steps:
Firstly, both entity1 and entity2 are nouns with biochemical and medical significance. Based on your knowledge, understand their corresponding biological meanings, explain entity1 and entity2 separately within the scope of your learned knowledge, each in one sentence.\
Secondly, based on your understanding of entity1 and entity2 and your knowledge,summarize the single quote structured text delimited by triple backticks with one explanation sentence.\
Thirdly, judge whether your explanation sentence contains the information between entity1 and entity2 I provided.\
Then according to the explanation sentence you summarized, set up three alternative multiple choice question and answer pairs related to the 'relationship' between entity1 and entity2. And you should include some error messages as multiple choice wrong answers.\
Please note, all the three multiple choice question and answer pairs only focus on entity1 and entity2 and the true information supplemented based on your understanding, rather than other information such as 'dataset' and 'method' I provide you with.\
Nextly, judge whether all the three multiple choice question and answer pairs are consistent with the information you summarized before.\
And, judge whether the three question and answer pairs are consistent with the information between entity1 and entity2 I provided.\
If the three question and answer pairs are not consistent with the information you summarized before or not related with the 'relationship' between entity1 and entity2 I provided, please regenerate the unqualified question and answer pairs and repeat the above steps until all the three multiple choice question and answer pairs are qualified.\
Please note, the Question should contain no information about the 'dataset' and 'methods', which means the final multiple choice question focus on entity1 and entity2 and the true information supplemented based on your understanding, rather than other information such as 'dataset' and 'method' I provide you with.\
And then, based on your understanding of the field of biomedical clinical research, please determine which question and answer pair is the most appropriate.\

Generate the multiple choice question and answer pair based on the text delimited by triple backticks.\
```{text}```

Finally, provide me with the best question and answer pair in JSON format with the following keys: Question, Explanation, optionA, optionB, optionC, optionD, Answer.\
Question means the best question you choose.\
Explanation means the explanation sentence you summarized.\
Answer means the answer of the best question you choose.\
"""


def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=1,
    )
    return response.choices[0].message["content"]


response = get_completion(prompt)
print(response)
