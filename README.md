# Trello2Asana

This work is licensed under Creative Commons Attribution-ShareAlike 4.0 International. To view a copy of this license, visit https://creativecommons.org/licenses/by-sa/4.0/ or [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/legalcode.en) 


## What is this used for?

Let's say you have a Trello board and you want to move it to Asana. Currently, Asana is able to import only CSV files. Depending on your Trello plan, you won't be able to export CSV files, only JSON ones.

So this project helps you to convert the JSON file to a CSV one that will upload your board into Asana.


### How to use it?

Considering you have Python installed on your computer, rename your `.json` file to `trello_board.json` and then use your terminal to run the following command. You must have the `converter.py` in the same folder `trello_board.json` is. As a result, you'll get a `.csv` file, which is the one you should upload to Asana.

```python
python converter.py
```

