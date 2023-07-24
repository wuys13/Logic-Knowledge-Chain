import openai
import os

openai.api_key = "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"

text = f"""
Axitinib'EOL-1'inhibition'CTRPv2'1'waterfall'
"""

prompt = f"""
This is a task of generating question and answer pair.\

You will be provided with single quote-structured text, whose structure is as follows:\
'entity1'entity2'relationship'dataset'number'methods\

It means that in the dataset, it has been proved that using the 'methods' we could get the 'relationship' between 'entity1' and 'entity2'.\
If the 'relatonship' is significant, the 'number' will be 1 and 0 otherwise. \

Suppose you are an expert in the clinical field of medicine, you will get the final question and answer pair by following steps:\
Firstly, summarize the single quote-structured text delimited by triple backticks with 1 sentence.\
Secondly, judge whether your summary contains the information between entity1 and entity2 I provided.\
Then according to the sentence you summarized, set up three alternative question and answer pairs related to the entity1 and entity2, the questions format are decision, multiple choice, short answer respectively.\
Nextly, judge whether the three question and answer pairs are consistent with the information you summarized before.\
And, judge whether the three question and answer pairs are consistent with the information between entity1 and entity2 I provided.\
If the three question and answer pairs are not consistent with the information you summarized before or not related with the relationship between entity1 and entity2 I provided, please regenerate the unqualified question and answer pairs and repeat the judgement steps until all the three pairs are qualified.\
And then, based on your understanding of the field of biomedical clinical research, please determine which question and answer pair is the most appropriate.\
Finally, provide me with all the three question and answer pairs in JSON format with the following keys: Question, optionA, optionB, optionC, optionD,answer.\

Generate the question and answer pair based on the text delimited by triple backticks.\
```{text}```
"""


def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0,
    )
    return response.choices[0].message["content"]


response = get_completion(prompt)
print(response)
