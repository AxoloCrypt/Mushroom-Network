# Mushroom-Network
> A neural network for mushroom edibility classification

## About
**Mushroom-Network** is a neural network that classifies if a given mushroom
is edible (e/1) or is poisonous (p/0) base on the 
following attributes:
- Cap Shape
- Cap Surface
- Cap Color
- Bruises
- Odor
- Gill Attachment
- Gill Spacing
- Gill Size
- Gill Color
- Stalk Shape
- Stalk Root
- Stalk Surface Above and Below the Ring
- Stalk Colors
- Veil Type
- Ring Number
- Ring Type
- Spore Print Color
- Population
- Habitat

**Note:** There is no simple rule for determining the edibility of a mushroom.
This project was made for research purposes.

### Results After Training
- loss: 0.0455'
- binary_accuracy = 0.9793

### Used Libraries
- Pandas
- Numpy
- Tensorflow
- Matplotlib
- Seaborn

## Dataset
> Dataset taken from: https://www.kaggle.com/datasets/uciml/mushroom-classification

The dataset contains hypothetical samples of 23 species of gilled mushrooms in the Agaricus
and Lepiota Family Mushroom.
