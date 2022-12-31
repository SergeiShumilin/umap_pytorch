Parametric UMAP port for pytorch using pytorch lightning for the training loop.

## Install
```bash
pip install -r requirements.txt
```

## Usage

```py
import umap_pytorch.main.PUMAP as PUMAP
import umap_pytorch.model.conv as conv

encoder = conv(n_components=2)
PUMAP = PUMAP(encoder, n_neighbors=10, min_dist=0.1, epochs=5)
data = torch.randn((50000, 512))
PUMAP.fit(data)
embedding = PUMAP.transform(data) # (50000, 2)
```