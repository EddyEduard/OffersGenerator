# OffersGenerator

OffersGenerator is a offers generator for IT&C projects. The generator can provide details of the technologies used to develop the application, project structure and financial information.

**Backend**
   - Python
   - Ollama

## Run & Build commands

The application is developed using the python.

Before executing any command, we must make sure that the packages are installed, otherwise we must install them using this command:
```
pip install -r requirements.txt
```

To run the application in the development mode use this command:
```
python3 test.py
```

## Training the model

For creating the AI model has been used the LLM (Large Language Model) Llama 3. 
\
The model was trained using instructions that can be found in the file [generator.py](https://github.com/EddyEduard/OffersGenerator/tree/main/generator.py)
\
After executing the [test.py](https://github.com/EddyEduard/OffersGenerator/tree/main/test.py) file it is prompted to enter requests for projects and then the AI model will generate a new offer.
\
When the AI model has finished generating the offer, a **TXT** and **WORD** file are generated in the project folder that contines the offer output.

## License
Distributed under the MIT License. See [MIT](https://github.com/EddyEduard/OffersGenerator/blob/master/LICENSE) for more information.

## Contact
EddyEduard - [eduard_nicolae@yahoo.com](mailTo:eduard_nicolae@yahoo.com)
\
Project link - [https://github.com/EddyEduard/OffersGenerator](https://github.com/EddyEduard/OffersGenerator.git)
