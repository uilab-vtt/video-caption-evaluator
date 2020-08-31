import os 
import json
import time
import random
from collections import Counter
from flask import Flask, redirect, request, render_template

app = Flask(__name__)
data_path = './data'
output_path = './output'
secret_code = 'tube_corn_fossil_'
static_url = '/static'
video_path = 'vtt-demo-ex.mp4'
caption_path = '%s/caption.json' % data_path

def init_paths():
    paths = [
        '%s/response' % output_path,
        '%s/user_ids' % output_path,
    ]
    for path in paths:
        if not os.path.exists(path):
            os.makedirs(path)

def is_user_id(uid):
    file_path = '%s/user_ids/%s.json' % (output_path, uid)
    return os.path.exists(file_path)

def generate_user_id():
    while True:
        uid = ''.join(random.choice('abcedfghijklmnopqrstuvwxyz0123456789') for i in range(16))
        if not is_user_id(uid):
            break
    file_path = '%s/user_ids/%s.json' % (output_path, uid)
    with open(file_path, 'w') as f:
        f.write('!')
    return uid

def get_video_url():
    return '%s/%s' % (static_url, video_path)

def get_caption_data():
    with open(caption_path, 'r') as f:
        cont = f.read()
    return cont

def save_response(user_id, response):
    file_path = '%s/response/res__%s.json' % (output_path, user_id)
    with open(file_path, 'w') as f:
        f.write(json.dumps(response))

@app.route('/')
def index():
    return redirect('/experiment')

@app.route('/experiment')
def experiment_show():
    uid = generate_user_id()
    caption_data = get_caption_data()
    video_url = get_video_url()
    return render_template(
        'experiment.html', 
        uid=uid, 
        caption_data=caption_data,
        video_url=video_url)

@app.route('/submit', methods=['POST'])
def submit_data():
    data = json.loads(request.data)
    response = data['response']
    user_id = data['uid']
    save_response(user_id, response)

    return 'done:%s' % (secret_code + user_id)

@app.route('/done')
def done_show():
    code = request.args.get('code')
    return render_template('experiment_done.html', code=code)

# def get_all_context_ids():
#     context_filenames = os.listdir('%s/contexts' % data_path)
#     context_ids = []
#     for filename in context_filenames:
#         if filename.endswith('.json'):
#             filename_strip = filename[:-5]
#             context_ids.append(filename_strip)
#     return context_ids

# def get_context_response_count_dict():
#     context_ids = get_all_context_ids()
#     response_filenames = os.listdir('%s/response' % output_path)
#     counter = {cid: 0 for cid in context_ids}
#     for filename in response_filenames:
#         if '__res__' not in filename:
#             continue
#         split_filename = filename.split('__res__')
#         if len(split_filename) != 2 or not split_filename[1].endswith('.json'):
#             continue
#         context_id = split_filename[0]
#         counter[context_id] += 1
#     return counter

# def draw_context_ids():
#     count_dict = get_context_response_count_dict()
#     context_ids = []
#     while len(context_ids) < context_count_per_user:
#         # Draw a context that currently has minimum number of responses.
#         valid_counts = [count for cid, count in count_dict.items() if cid not in context_ids]
#         if not valid_counts:
#             break
#         min_count = min(valid_counts)
#         draw_box = [cid for cid, count in count_dict.items() if (count == min_count) and (cid not in context_ids)]
#         context_ids.append(random.choice(draw_box))
    
#     return context_ids

# def get_context_dict(context_id):
#     file_path = '%s/contexts/%s.json' % (data_path, context_id)
#     with open(file_path, 'r') as f:
#         context_dict = json.load(f)
#     if 'id' not in context_dict:
#         context_dict['id'] = context_id
#     return context_dict

# def get_questions():
#     with open('%s/questions.json' % data_path, 'r') as f:
#         questions = json.load(f)
#     return questions

# def get_validate_texts():
#     with open('%s/validate_texts.json' % data_path, 'r') as f:
#         validate_texts = json.load(f)
#     return validate_texts

# def draw_context_dicts():
#     context_ids = draw_context_ids()
#     return [get_context_dict(cid) for cid in context_ids]

# def is_user_id(uid):
#     file_path = '%s/user_ids/%s.json' % (output_path, uid)
#     return os.path.exists(file_path)

# def generate_user_id():
#     while True:
#         uid = ''.join(random.choice('abcedfghijklmnopqrstuvwxyz0123456789') for i in range(16))
#         if not is_user_id(uid):
#             break
#     file_path = '%s/user_ids/%s.json' % (output_path, uid)
#     with open(file_path, 'w') as f:
#         f.write('!')
#     return uid

# def save_response(context_id, user_id, response):
#     file_path = '%s/response/%s__res__%s.json' % (output_path, context_id, user_id)
#     with open(file_path, 'w') as f:
#         f.write(json.dumps(response))

# @app.route('/tasks')
# def task_index():
#     return render_template('task_index.html')

# @app.route('/tasks/draw')
# def task_draw():
#     uid = generate_user_id()
#     context_dicts = draw_context_dicts()
#     questions = get_questions()
#     validate_texts = get_validate_texts()
#     return render_template(
#         'task_draw.html', 
#         uid=uid, 
#         contexts=context_dicts,
#         questions=questions,
#         validate_texts=validate_texts)

# @app.route('/tasks/submit', methods=['POST'])
# def task_submit():
#     data = json.loads(request.data)
#     response = data['response']
#     user_id = data['uid']

#     for context_id, value in response.items():
#         save_response(context_id, user_id, value)

#     return 'done:%s' % (secret_code + user_id)

# @app.route('/tasks/done')
# def task_done():
#     code = request.args.get('code')
#     return render_template('task_done.html', code=code)

init_paths()
if __name__ == '__main__':
    app.run(debug=True)