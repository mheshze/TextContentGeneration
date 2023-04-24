import nltk
import re
from transformers import BartTokenizer, BartForConditionalGeneration
nltk.download('punkt')

bart_tokenizer = BartTokenizer.from_pretrained('facebook/bart-large-cnn')

device = 'mps'
bart_model = BartForConditionalGeneration.from_pretrained('facebook/bart-large-cnn')
bart_model.to(device)


def nest_sentences(document):
  nested = []
  sent = []
  length = 0
  for sentence in nltk.sent_tokenize(document):
    length += len(sentence)
    if length < 1024:
      sent.append(sentence)
    else:
      nested.append(sent)
      sent = []
      length = 0

  if sent:
    nested.append(sent)
  return nested

# generate summary on text with <= 1024 tokens
def generate_summary(nested_sentences):
  device = 'mps'
  summaries = []
  for nested in nested_sentences:
    input_tokenized = bart_tokenizer.encode(' '.join(nested), truncation=True, return_tensors='pt')
    input_tokenized = input_tokenized.to(device)
    summary_ids = bart_model.to(device).generate(input_tokenized,
                                      length_penalty=3.0,
                                      min_length=30,
                                      max_length=100)
    output = [bart_tokenizer.decode(g, skip_special_tokens=True, clean_up_tokenization_spaces=False) for g in summary_ids]
    summaries.append(output)
  summaries = [sentence for sublist in summaries for sentence in sublist]
  return summaries

# cont = [x + " " for x in re.sub(r"\x0f|\x15|\xa0"," ",transcript).splitlines() if x != "" ]
# cont = "".join(cont).strip()
# chunks = nest_sentences(cont)

def summarize_chunks(script):
    cont = [x + " " for x in re.sub(r"\x0f|\x15|\xa0"," ",script).splitlines() if x != "" ]
    cont = "".join(cont).strip()
    chunks = nest_sentences(cont)
    print(f"{len(chunks)} chunks created...\n")
    print("Summarizing Chunks...\n")
    summary = "".join(generate_summary(chunks))
    print("Summarization Completed!\n")
    return summary