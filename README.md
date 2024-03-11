# Warframe Wiki Helper
![](https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/1a8a75d4-a77e-484c-9bfe-6e25152f4f38/ddl7d2g-d1eadd9c-249b-47b0-bb48-7229ecf43842.png/v1/fill/w_1920,h_1048,q_80,strp/the_warframe_logo_by_leroyjenkins234_ddl7d2g-fullview.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MTA0OCIsInBhdGgiOiJcL2ZcLzFhOGE3NWQ0LWE3N2UtNDg0Yy05YmZlLTZlMjUxNTJmNGYzOFwvZGRsN2QyZy1kMWVhZGQ5Yy0yNDliLTQ3YjAtYmI0OC03MjI5ZWNmNDM4NDIucG5nIiwid2lkdGgiOiI8PTE5MjAifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6aW1hZ2Uub3BlcmF0aW9ucyJdfQ.I17VNV68G84VuidjkvF0RIVLOFtL3Z5YMy627zGBWOY)

Welcome!

## This project implements NLP techniques to:
- create a document database,
- retrieve relevant documents from it based on a question
- generate a text response, citing its sources

## Information
The techniques used here are based on a [video](https://youtu.be/inAY6M6UUkk?si=arSxHpOkYaLjHMzA) that leans heavily on Google's cloud service and API calls.

Since it's just a personal project, I've re-worked almost every step to be able to run the process **completely locally** and **without paying for web storage / API model inference**.

The embeddings model is [all-MiniLM-L6-v2](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2)

The generative model is Facebook's [Flan-T5-Large](https://huggingface.co/google/flan-t5-large)

Currently, the helper's responses are limited to a hard-coded list of warframes from the [Warframe Wiki](https://warframe.fandom.com/wiki/Warframes).

## Demo
```
Q: "What are all of Excalibur's abilities?"
A: Slash Dash, Radial Blind, Radial Javelin, Exalted Blade.

Passive: Excalibur deals 10% increased damage and attacks 10% faster when wielding swords.

Abilities: 1st Ability Slash Dash 2nd Ability Radial Blind 3rd Ability Radial Javelin 4th Ability Exalted Blade

...
```

# Usage
Definitely use venv to create a new virtual environment and install the ```requirements.txt```. There are some specific version dependencies. (Jupyter Notebooks lets you do this automagically at the top right!)

Open  ```./question-answering.ipynb```. Everything you need to run the process is inside ```WHOLE LOOP FOR DOCUMENT RETRIEVAL!```.

On the very first time you run the project, run all code inside ```First Time Ever```

Everytime you want to run the project after that, run all code inside ```Every Time -> Run Once``` Once, then ```Every Time -> Run Each Query``` each time you want to ask a question.
