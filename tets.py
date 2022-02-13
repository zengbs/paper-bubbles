from parrot import Parrot
import torch
import warnings
warnings.filterwarnings("ignore")

'''
uncomment to get reproducable paraphrase generations
def random_state(seed):
  torch.manual_seed(seed)
  if torch.cuda.is_available():
    torch.cuda.manual_seed_all(seed)

random_state(1234)
'''

#Init models (make sure you init ONLY once if you integrate this to your code)
parrot = Parrot(model_tag="prithivida/parrot_paraphraser_on_T5")

phrases = [
"To this end, this work introduces a thin disk of dense interstellar medium around the jet source to deflect and decelerate the tilted jet in an attempt to resolve the galactic bubble's symmetry."
]

for phrase in phrases:
  print("-"*100)
  print("Input_phrase: ", phrase)
  print("-"*100)
  para_phrases = parrot.augment(input_phrase=phrase, use_gpu=False)
  for para_phrase in para_phrases:
   print(para_phrase)
