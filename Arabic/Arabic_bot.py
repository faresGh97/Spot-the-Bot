#!/usr/bin/env python
# coding: utf-8



import torch
import numpy as np
import transformers
from tqdm import tqdm
from torch.utils.data import Dataset, DataLoader
from transformers import GPT2LMHeadModel, GPT2Tokenizer

def generate_Text_bot(input_file,output_file,tokenizer, model):
    model.cuda()
    model.eval()
    transformers.set_seed(1337)
    #output_file = './test_bot_corpus.txt'
    #tokenizer = GPT2Tokenizer.from_pretrained(bot_path)
    #model = TFGPT2LMHeadModel.from_pretrained(bot_path)
    file1 = open(input_file, 'r',encoding = 'utf-8')
    Lines = file1.readlines()
    for line in tqdm(Lines):
      generated_text = ''
      list_of_words  = line.split()
      #list_of_words = list_of_words[0:1000]
      #print(list_of_words)
      for i in range(0,len(list_of_words),100):
        start_token = ' '.join(list_of_words[i:i+15])
        #print(start_token)
        input_ids = tokenizer.encode(start_token, return_tensors="pt").cuda()
        out = model.generate(
            input_ids, 
            min_length=5,
            max_length=100,
            eos_token_id=5,
            pad_token_id=tokenizer.eos_token_id,
            do_sample=True,
            top_k=0,
            top_p=0.9,
            no_repeat_ngram_size=4)
        output_text = tokenizer.decode(out[0],skip_special_tokens = True)
        output_text = output_text.replace('\n', ' ')
        #fout.write(re.sub('\s+',' ',line))
        generated_text =generated_text +  " " + output_text
      with open(output_file, 'a',encoding='utf-8') as f:
        f.write(f"{generated_text}\n")

def main():
    model_name = "/home/fgazzavi/f_env/Bot"
    tokenizer = GPT2Tokenizer.from_pretrained(model_name)
    model = GPT2LMHeadModel.from_pretrained(model_name)

    train_on_gpu = torch.cuda.is_available()
    if(train_on_gpu):
        print('Training on GPU!')
    else: 
        print('No GPU available, training on CPU; consider making n_epochs very small.')

    print(torch.cuda.device_count())

    generate_Text_bot('/home/fgazzavi/f_env/Arabic/test_original_corpus_SVD_modified.txt','/home/fgazzavi/f_env/Arabic/test_bot_corpus_SVD.txt',tokenizer,model)

    generate_Text_bot('/home/fgazzavi/f_env/Arabic/test_original_corpus_CBOW_modified.txt','/home/fgazzavi/f_env/Arabic/test_bot_corpus_CBOW.txt',tokenizer,model)
   
if __name__ == "__main__":

    main()



