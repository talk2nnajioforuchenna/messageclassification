import os
import openai

openai.api_key = os.environ['OPENAI_API_KEY']
print(os.environ['OPENAI_API_KEY'])

prompt = 'Is there an option for express or expedited shipping?'

response = openai.Completion.create(model='ada:ft-100-percent-fragrance-2023-03-06-20-01-57',
                                    prompt=prompt + ' /n/nIntent/n/n',
                                    temperature=0.0,
                                    max_tokens=100,
                                    top_p=1,
                                    frequency_penalty=0.0,
                                    presence_penalty=0.0,
                                    stop=[' END'])
print(response['choices'][0]['text'])
