# Neural Network implementation in Python
My first NN implementation will be in Python, and will recognize handwritten digits. It will contain an ecosystem in order to train it as well.

## The `byteimg` Image Format
As a learning exercise, I will create my own image format which the neural network and the dataset will use. A `byteimg` file is just a list of 1024 bytes, each byte representing a black-and-white pixel's value. If the byte is 255, the pixel is white, if it is 0, the pixel is black, if it is 127, the pixel is gray, etc. After these 1024 bytes, there can be an optional identifier byte with a value from 0 to 9, which determines what the number in the image represents. This byte can be used so that the neural network can learn.

## File Structure
- `dataset` will house `byteimg` images for the dataset to learn with. As long as the final identifier byte is included, the filenames can be anything.
- `byteimg` will house various utilities for conversion, reading, and writing of a byteimg.
- `imgdraw` will house a web application which can draw `byteimg` numbers to the `dataset`.