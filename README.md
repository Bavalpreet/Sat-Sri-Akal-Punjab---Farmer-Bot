# SSA Chatbot

## Project Description

The Farmer Assistance Bot is a technology-driven project aiming to enhance farmer support services in Punjab by addressing queries related to crop seed quality, diseases, and yield enhancement.

For example: They could ask <b>"What weedicide to apply for removing weeds from rice crop?"</b>

These type of questions are very general in nature and can be taken by the conversational AI very easily without need of any human in the loop that would save a lot of time for the farmer as well as employees working at Kisan Call Centers.

### crops included till now

| Sr. No. | Crop Name |
| :---: | :---: |
| 1. | Wheat |
| 2. | Rice |
| 3. | Pea |
| 4. | Garlic |
| 5. | Guava |
| 6. | Citrus |
| 7. | Chilli |

### Proposed Design of the Conversational AI Agent

<p style="text-align:center;"><img style="text-align:center;" src="Agribot Architecture.jpg" alt="Proposed Design" ></p>

<p style="text-align:center;">Proposed Design of the Conversational AI Agent</p>

The Idea is to divide the conversational agent into 9 agents each dealing with a specific type of crops.

<b>Process:</b>

1. User query will first pass the a script which would extract the crop name out of it. For example from the sentence `how to deal with weeds in rice` the script will extract rice.
2. After extracting the crop name the script would hit one of the nine bots and then send back the response of bot to the user.
3. If there is no crop name in the user query then the script would first ask user to provide with a crop name and then using that it would decide to hit one of the bots.

This process is propossed since there is huge amount of data for different crops and their are many queries which just differ in the crop name only this would make it hard for the bot to classifiy a query as the number of crops grow.

## How to Install and Run the Project

Firstly clone the repo locally or Download the source code.

After getting the source code you need to install python and rasa on to your system. Our recommendation is to download python using miniconda or Anaconda.

> Link for miniconda: https://docs.conda.io/en/latest/miniconda.html

> Link for Anaconda: https://www.anaconda.com/products/individual

After installing the python, it is recommended to create a seperate environment for RASA and install the required libraries into it.( Sometimes the libraries versions may differ for differnet packeges which might cause some dependency issues while using rasa )

Command to create a new Env.

> conda create -n \<Name of Environment> python=3.7

> conda create -n SSA python=3.7

Once the environment is created you can activate it using
> conda activte \<name of environment>

> conda activate rasa

After activating the environment you can install rasa by using
    
    > python -m pip install --upgrade pip  # to upgrade the pip version
    > pip install rasa == 3.0.6

To check that rasa is working or not you can run the below command
> rasa --version

** note if you get some error related to `sanic` you can run the below command to resolve it
> pip install sanic==21.9.3

## Workflow of making a bot

There are multiple important things to note in order to understand the workflow.

- The `data` directory in each bot directory contains the nlu data and these nlu files are divided into different batchs. Named as `nlu-faq-<agri/hort>-<crop name>-b<batch number>.yml` (Example `nlu-faq-agri-wheat-b0.yml or nlu-faq-hort-chilli-b0`) for each batch file there is a domain file too.
- The `domain-grp` directory in each bot directory contains domain batched files corresponding to the nlu files.
- When new data for nlu and domian is added to the above described directories we have to execute the `build-domain.py` script which will make sure that all the responses are being considered by rasa while training.

### Process followed
<p style="text-align:center;"><img src=pipeline.png alt="Logo"></p>

1. First using the s-bert transformer we narrow down the number of unique questions based on sentence similarity.
2. Using the unique sentences from above step we compare the new sentences with already added data to get questions which are not yet ingested in the model (Levenshtein Distance is used for the comparison here). `**Note:** use only in case there already is some data added for the crop in cosideration`
3. Use clustering to cluster similer questions together after doing the above to steps. It makes easier to select the good quality question and delete the ones which are not required.
4. With the help of T-5 transformer we get parapharse examples for each unique question
5. Generate NLU and DOMAIN files add them to the data and domain-grp directories respectivly.
6. Check the NLU file for parapharase questions quality and update those examples which are not good.
7. Fill up the domain file with answers from the dataset(Use the most recent answer by sorting based on the year)
8. Execute 'build-domain.py` scrip to make domain.yml from
9. Train model
10. Run and test it
