<div align="center">
    <h1>Integration of ChatGPT to an Python Application</h1>
    <p>Source code of <a href="https://www.youtube.com/watch?v=hr97D41UrAA" target="_blank"><u>ChatGPT at your service</u></a> on <a href="https://www.youtube.com/watch?v=hr97D41UrAA&list=PLpBtWRenhW_S0YjxqE1fhbtTuK8SSZHNW&index=2" target="_blank"><u>ImagineAndMake</u></a> serie</p>
    <div style="display: flex;align-items: center;justify-content: center;gap: 30px">
        <a href="https://discord.com/invite/dev-community" target="_blank">
            <img src="./documentation/discord_logo.png" alt="Official Discord logo" width="30"/>
        </a>
        <a href="https://www.youtube.com/channel/UCmH1td7f73IEyYNNg5XDT9g" target="_blank">
            <img src="./documentation/youtube_logo.png" alt="Official Youtube logo" width="30"/>
        </a>
    </div>
</div>

## Summary

The aim of this source code is to bring __ChatGPT's response capability right to your fingertips__. We integrate the OpenAI API into a Python application, and then add functions that might be considered indispensable in a developer's life. We've also added Speech To Text to initiate the ability to speak and get an immediate response.


## Demonstration

<video width="1020" height="540" controls autoplay muted>
    <source src="./documentation/demonstration.mp4" type="video/mp4">
</video>

## Requirements
- Python 3.10+ (Maybe you can use an older version of Python)

## Installation

Download this source code
```
git clone [URL]
```

Create a python environment and activate it
```
python3 -m venv environment
source environment/bin/activate
```

Install the require packages
```
cd IntegrateGPTonApp
pip install -r requirements.txt
```

You must define your main language for the Speech To Text system on line 63 of the `index.py` file in the format (for example: fr-FR or en-US)
```
input = recognizer.recognize_google(voice_input, language='fr-FR')
```

After installing the packages, you need to enter your OpenAI keys on line 76 of the `index.py` file in place of "OPENAI KEY".
```
openai.api_key = "OPENAI KEY"
```