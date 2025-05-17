# from flask import Flask, request, jsonify
# import logging
#
# app = Flask(__name__)
# logging.basicConfig(level=logging.INFO)
#
# sessionStorage = {}
#
#
# @app.route('/post', methods=['POST'])
# def main():
#     logging.info(f'Request: {request.json!r}')
#
#     response = {
#         'session': request.json['session'],
#         'version': request.json['version'],
#         'response': {
#             'end_session': False
#         }
#     }
#
#     handle_dialog(request.json, response)
#
#     logging.info(f'Response:  {response!r}')
#     return jsonify(response)
#
#
# def handle_dialog(req, res):
#     user_id = req['session']['user_id']
#
#     if req['session']['new']:
#         sessionStorage[user_id] = {
#             'suggests': [
#                 "Не хочу.",
#                 "Не буду.",
#                 "Отстань!",
#             ],
#             'elephants': 0
#         }
#         res['response']['text'] = 'Привет! Купи слона!'
#         res['response']['buttons'] = get_suggests(user_id)
#         return
#
#     if req['request']['original_utterance'].lower() in [
#         'ладно', 'куплю', 'покупаю', 'хорошо', 'ок', 'да'
#     ]:
#         res['response']['text'] = 'Слона можно найти на Яндекс.Маркете!'
#         res['response']['end_session'] = True
#         return
#
#     sessionStorage[user_id]['elephants'] += 1
#     count = sessionStorage[user_id]['elephants']
#
#     if count == 1:
#         res['response']['text'] = f"Все говорят '{req['request']['original_utterance']}', а ты купи слона!"
#     elif count == 2:
#         res['response']['text'] = f"Ну пожалуйста! Купи слона!"
#     elif count == 3:
#         res['response']['text'] = "Ты же знаешь, как я хочу слона! Купи его!"
#     else:
#         res['response']['text'] = "Я сдаюсь... Но ты всё равно купишь слона!"
#
#     res['response']['buttons'] = get_suggests(user_id)
#
#
# def get_suggests(user_id):
#     session = sessionStorage[user_id]
#
#     suggests = [
#         {'title': suggest, 'hide': True}
#         for suggest in session['suggests'][:2]
#     ]
#
#     session['suggests'] = session['suggests'][1:]
#     sessionStorage[user_id] = session
#
#     if len(suggests) < 2:
#         suggests.append({
#             "title": "Ладно",
#             "url": "https://market.yandex.ru/search?text=слон",
#             "hide": True
#         })
#
#     return suggests
#
#
# if __name__ == '__main__':
#     app.run(port=8080, debug=True)







# from flask import Flask, request, jsonify
# import logging
# import re
#
#
# app = Flask(__name__)
# logging.basicConfig(level=logging.INFO)
#
# sessionStorage = {}
#
#
# @app.route('/post', methods=['POST'])
# def main():
#     logging.info(f'Request: {request.json!r}')
#
#     response = {
#         'session': request.json['session'],
#         'version': request.json['version'],
#         'response': {
#             'end_session': False
#         }
#     }
#
#     handle_dialog(request.json, response)
#
#     logging.info(f'Response:  {response!r}')
#     return jsonify(response)
#
# def is_agreement(utterance):
#     utterance = utterance.lower()
#     return bool(re.search(r'\b(ладно|куплю|покупаю|хорошо|ок|да|соглас[енна]|уговорил[иа])\b', utterance))
#
# def handle_dialog(req, res):
#     user_id = req['session']['user_id']
#
#     if req['session']['new']:
#         sessionStorage[user_id] = {
#             'suggests': [
#                 "Не хочу.",
#                 "Не буду.",
#                 "Отстань!",
#             ],
#             'elephants': 0
#         }
#         res['response']['text'] = 'Привет! Купи слона!'
#         res['response']['buttons'] = get_suggests(user_id)
#         return
#
#     if is_agreement(req['request']['original_utterance']):
#         res['response']['text'] = 'Слона можно найти на Яндекс.Маркете!'
#         res['response']['end_session'] = True
#         return
#
#     sessionStorage[user_id]['elephants'] += 1
#     count = sessionStorage[user_id]['elephants']
#
#     if count == 1:
#         res['response']['text'] = f"Все говорят '{req['request']['original_utterance']}', а ты купи слона!"
#     elif count == 2:
#         res['response']['text'] = f"Ну пожалуйста! Купи слона!"
#     elif count == 3:
#         res['response']['text'] = "Ты же знаешь, как я хочу слона! Купи его!"
#     else:
#         res['response']['text'] = "Я сдаюсь... Но ты всё равно купишь слона!"
#
#     res['response']['buttons'] = get_suggests(user_id)
#
# def get_suggests(user_id):
#     session = sessionStorage[user_id]
#
#     suggests = [
#         {'title': suggest, 'hide': True}
#         for suggest in session['suggests'][:2]
#     ]
#
#     session['suggests'] = session['suggests'][1:]
#     sessionStorage[user_id] = session
#
#     if len(suggests) < 2:
#         suggests.append({
#             "title": "Ладно",
#             "url": "https://market.yandex.ru/search?text=слон",
#             "hide": True
#         })
#
#     return suggests
#
#
# if __name__ == '__main__':
#     app.run(port=8080, debug=True)









from flask import Flask, request, jsonify
import logging
import re

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

sessionStorage = {}

@app.route('/post', methods=['POST'])
def main():
    logging.info(f'Request: {request.json!r}')

    response = {
        'session': request.json['session'],
        'version': request.json['version'],
        'response': {
            'end_session': False
        }
    }

    handle_dialog(request.json, response)

    logging.info(f'Response:  {response!r}')
    return jsonify(response)

def is_agreement(utterance):
    utterance = utterance.lower()
    return bool(re.search(r'\b(ладно|куплю|покупаю|хорошо|ок|да|соглас[енна]|уговорил[иа])\b', utterance))

def handle_dialog(req, res):
    user_id = req['session']['user_id']

    if req['session']['new']:
        sessionStorage[user_id] = {
            'suggests': ["Не хочу.", "Не буду.", "Отстань!"],
            'elephants': 0,
            'rabbits': 0,
            'current_animal': 'слона'
        }
        res['response']['text'] = 'Привет! Купи слона!'
        res['response']['buttons'] = get_suggests(user_id)
        return

    if is_agreement(req['request']['original_utterance']):
        if sessionStorage[user_id]['current_animal'] == 'слона':
            sessionStorage[user_id]['current_animal'] = 'кролика'
            sessionStorage[user_id]['elephants'] = 0
            res['response']['text'] = 'Отлично! Слона можно найти на Яндекс.Маркете! А теперь купи кролика!'
            res['response']['buttons'] = get_suggests(user_id)
            return
        else:
            res['response']['text'] = 'Кролика можно найти на Яндекс.Маркете! Спасибо за покупки!'
            res['response']['end_session'] = True
            return

    animal = sessionStorage[user_id]['current_animal']
    sessionStorage[user_id]['elephants'] += 1
    count = sessionStorage[user_id]['elephants']

    if count == 1:
        res['response']['text'] = f"Все говорят '{req['request']['original_utterance']}', а ты купи {animal}!"
    elif count == 2:
        res['response']['text'] = f"Ну пожалуйста! Купи {animal}!"
    elif count == 3:
        res['response']['text'] = f"Ты же знаешь, как я хочу {animal}! Купи его!"
    else:
        res['response']['text'] = f"Я сдаюсь... Но ты всё равно купишь {animal}!"

    res['response']['buttons'] = get_suggests(user_id)

def get_suggests(user_id):
    session = sessionStorage[user_id]

    suggests = [
        {'title': suggest, 'hide': True}
        for suggest in session['suggests'][:2]
    ]

    session['suggests'] = session['suggests'][1:]
    sessionStorage[user_id] = session

    if len(suggests) < 2:
        suggests.append({
            "title": "Ладно",
            "url": f"https://market.yandex.ru/search?text={session['current_animal']}",
            "hide": True
        })

    return suggests

if __name__ == '__main__':
    app.run(port=8080, debug=True)