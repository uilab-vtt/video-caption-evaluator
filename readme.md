# Video Caption Evaluator

This is a web application for evaluating natural language sentences with a video data.
Use this application with Amazon Mechanical Turk to evaluate context-dependent video captions.

## How to setup

Make sure to have Python 3 installed, and run commands below to set up.

```bash
$ python -m venv ./env
$ source ./env/bin/activate
(env)$ pip install -r requirements.txt
```

## How to develop

To run development server, run the command below.

```bash
(env)$ FLASK_ENV=development python main.py
```

## How to run in production mode

To run this web app in production mode, run the command below.
```bash
(env)$ sh run.sh
```

Try http://localhost:5000 on a web browser.

## Caption data

This is an example of caption data in JSON format.

```json
{
    "timestamps": {
        "0.1": { "id": "c0", "type": "show" },
        "2.1": { "id": "c0", "type": "hide" },
        "2.4": { "id": "c1", "type": "show" },
        "5.4": { "id": "c1", "type": "hide" },
        "2.5": { "id": "c2", "type": "show" },
        "5.3": { "id": "c2", "type": "hide" },
        "3.8": { "id": "c3", "type": "show" },
        "5.6": { "id": "c3", "type": "hide" },
        "6": { "id": "c4", "type": "show" },
        "6.4": { "id": "c4", "type": "hide" },
        "6.1": { "id": "c5", "type": "show" },
        "6.3": { "id": "c5", "type": "hide" },
        "6.5": { "id": "c6", "type": "show" },
        "6.8": { "id": "c6", "type": "hide" }
    },
    "captions": {
        "c0": "Two people are walking in the video.",
        "c1": "A man is wearing a cap.",
        "c2": "A cup is on a table.",
        "c3": "There are people around a table.",
        "c4": "There are two people.",
        "c5": "A woman is talking.",
        "c6": "A watch is around a wrist."
    }
}
```

## Results

Participants who submitted the answer will get a code that looks like: 

`tube_corn_fossil_{user_id_with_16_digits_and_letters}`

The results are saved in `./output/response/res__{user_id}.json`. 
