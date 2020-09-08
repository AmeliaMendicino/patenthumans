# Patent Humans

Tools to automate the process of finding patents with funny images for [patenthumans.com](https://www.patenthumans.com/).

Based on Youness Mansar's [Fast_Image_Classification](https://github.com/CVxTz/FastImageClassification)

# Installation

Make sure you have `python`, `pip`, and `pipenv` installed.

To setup packages and environment for dev environment:

`pipenv install --dev`

To run a file in the virtual environment without having to activate it:

`pipenv run python filename.py`

To activate your pipenv environment (good for when you need to pipe):

`pipenv shell`

To deactivate the environment use `exit`

# Image Labels

Used [VGG Image Annotator (VIA)](http://www.robots.ox.ac.uk/~vgg/software/via/) for labeling all of the figure URLs for model training.
Can take the output from the `get_figure_urls.py` and load it directly into VIA with the `Project > Add url or path from text file` menu option.

Using the File Attributes, can add labels to all of the images by setting the attribute type to checkbox with an arbitrary id name.

Run the util `pipenv run python utils/via_csv_to_data_csv.py --file via_project.csv --labels w,x,y,z` to convert the csv output of VIA into the format we need for [Fast_Image_Classification](https://github.com/CVxTz/FastImageClassification).