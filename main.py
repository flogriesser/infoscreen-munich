from flask import Flask, Response, render_template
import os
import time

app = Flask(__name__, template_folder='template')

picture_path =  os.environ.get('picture_path')



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
    #image_folder = '/home/flo/Nextcloud/Projects/GitHub/OWN/infoscreen-munich/TestPictures/wallpapers-master/'
    images = [img for img in os.listdir(picture_path)
              if img.endswith(".jpg") or
              img.endswith(".jpeg") or
              img.endswith("png")]
    return images


@app.route('/slideshow')
def slideshow():
    return Response(gen(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


#@app.route('/')
#def index():
#    return "<html><head></head><body><img src='/slideshow' style='width: 100%; height: 100%;'/></body></html>"

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
    