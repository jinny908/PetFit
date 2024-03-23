import torch
from torch import nn
import torch.nn.functional as F

class Net(nn.Module):
    def __init__(self):
        super().__init__()
        self.lin1 = nn.Linear(5, 5)

    def forward(self, x):
        net = self.lin1(x)
        return net

# MPS가 사용 가능한지 확인
if torch.backends.mps.is_available():
    device = torch.device("mps")
    print("MPS 사용 가능")
else:
    device = torch.device("cpu")
    print("MPS 사용 불가능")

print(f"device: {device}")

# MPS 장치에 바로 tensor를 생성합니다.
x = torch.ones(5, device=device)

# GPU 상에서 연산 진행
y = x * 2

# 또는, 다른 장치와 마찬가지로 MPS로 이동할 수도 있습니다.
model = Net()
model.to(device) # MPS 장치로 이동합니다.

# 이제 모델과 텐서를 호출하면 MPS를 통해 GPU에서 연산이 이뤄집니다.
pred = model(x)
print(pred)
