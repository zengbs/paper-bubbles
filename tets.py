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
"The same leptotonic CRe can simultaneously account for the Fermi bubbles and haze emission suggested that the magnetic fields within the bubbles are close to the exponentially distributed Galactic magnetic field. Moreover, the fact that the bubbles are symmetric across the Galactic plane and also centered on the GC endorsing the assumption that the bubbles, and the associated gamma-ray emissions, have their origin at the GC."
]

for phrase in phrases:
  print("-"*100)
  print("Input_phrase: ", phrase)
  print("-"*100)
  para_phrases = parrot.augment(input_phrase=phrase, use_gpu=False)
  for para_phrase in para_phrases:
   print(para_phrase)
