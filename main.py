import torch

torch.__version__

assert not torch.cuda.is_available()
assert torch.backends.mps.is_available()
