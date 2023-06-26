<div align="center">
    <h2>Integration of ChatGPT to an Python Application</h2>
    <p>Source code of <a href="https://www.youtube.com/watch?v=hr97D41UrAA" target="_blank"><u>ChatGPT at your service</u></a> video on <a href="https://www.youtube.com/watch?v=hr97D41UrAA&list=PLpBtWRenhW_S0YjxqE1fhbtTuK8SSZHNW&index=2" target="_blank"><u>ImagineAndMake</u></a> serie</p>
</div>

## Summary

The aim of this source code is to bring __ChatGPT's response capability right to your fingertips__. We integrate the OpenAI API into a Python application, and then add functions that might be considered indispensable in a developer's life. We've also added Speech To Text to initiate the ability to speak and get an immediate response.
You can find us on [Discord](http://discord.com/invite/dev-community) and on [Youtube](https://www.youtube.com/channel/UCmH1td7f73IEyYNNg5XDT9g).

## Demonstration

https://github.com/development-community/Integrate-GPT-on-App/assets/60803887/95efd13d-f9ee-48ae-a5ab-4e2b91b7468f

If the video doesn't work, you can watch on [Youtube](https://youtu.be/LlF1ojpID_c)

## Requirements
- Python 3.10+ (Maybe you can use an older version of Python)

## Installation

Download this source code
```
git clone https://github.com/development-community/Integrate-GPT-on-App.git
```

Create a python environment and activate it
```
python3 -m venv environment
source environment/bin/activate
```

Install the require packages
```
cd ./IntegrateGPTonApp
pip install -r requirements.txt
```

You must define your main language for the Speech To Text system on line 63 of the `index.py` file in the format (for example: fr-FR or en-US) because SpeechRecognition didn't manage multi-language in same time.
```
input = recognizer.recognize_google(voice_input, language='fr-FR')
```

After installing the packages, you need to enter your OpenAI keys on line 76 of the `index.py` file in place of "OPENAI KEY".
```
openai.api_key = "OPENAI KEY"
```
