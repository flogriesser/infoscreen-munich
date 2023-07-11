from flask import Flask, Response, render_template
import os
import time
import json
import datetime
import glob

app = Flask(__name__, template_folder='template')

#picture_path =  os.environ.get('picture_path')
picture_path =  "/var/infoscreen-munic/pictures"

restaurant_counter = 0
restaurants = [['Mensa Arcistraße', 'response_mensa-arcisstr.json'], ['Mensa Garching','response_mensa-garching.json'], ['Mensa Leopoldstraße', 'response_mensa-leopoldstr.json'], ['Mensa Lothstraße', 'response_mensa-lothstr.json']]
NOT_INTRESTING_FOOD = ["Reis", "Tagessuppe", "Täglich frische Dessertbar", "Täglich frische Salatbar", "Saisonale Beilagensalate"]

def get_mensa_data(number):
    dishes = []
    with open("./MENUs/" + restaurants[number][1], 'r') as f:
        data = json.load(f)
        weekday = datetime.datetime.now().weekday()
        print(weekday)
        for dish in data['days'][weekday]['dishes'][:][:][:]:
            dishes.append(dish['name'])

    # Remove stupid stuff
    dishes[:] = [item for item in dishes if item not in NOT_INTRESTING_FOOD]
    
    return dishes


def gen():
    i = 0

    while True:
        time.sleep(5)
        images = get_all_images()
        image_name = images[i]
        im = open(picture_path + image_name, 'rb').read()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + im + b'\r\n')
        i += 1
        if i >= len(images):
            i = 0


def get_all_images():
    images = [img for img in os.listdir(picture_path)
              if img.endswith(".jpg") or
              img.endswith(".jpeg") or
              img.endswith("png")]
    return images


@app.route('/slideshow')
def slideshow():
    return Response(gen(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/update_menu')
def update_menu():
    global restaurant_counter
    updated_list = get_mensa_data(restaurant_counter)
    print(update_menu)
    list_name = restaurants[restaurant_counter][0]
    if restaurant_counter < len(restaurants)-1:
        restaurant_counter = restaurant_counter +1
    else:
        restaurant_counter = 0
    return render_template('menus.html', list_name=list_name, items=updated_list)


#    dishes = get_mensa_data(0)
#    mensa_name = restaurants[0][0]

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
    