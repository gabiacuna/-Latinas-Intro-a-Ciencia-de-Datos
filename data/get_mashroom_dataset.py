#!/bin/bash
# curl -L -o ~/Downloads/mushroom-classification.zip\
#   https://www.kaggle.com/api/v1/datasets/download/uciml/mushroom-classification

import requests

response = requests.get("https://www.kaggle.com/api/v1/datasets/download/uciml/mushroom-classification")

print(response)

with open("./mushroom-classification.zip", "wb") as f:
    f.write(response.content)
