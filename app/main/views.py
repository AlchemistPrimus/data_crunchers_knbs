from flask import Blueprint, render_template
import sys
sys.path.insert(0,"/home/ado/Desktop/new_datacranchers/data_crunchers_knbs/app/main")



views=Blueprint('views',__name__)

@views.route('/',methods=['GET'])
def index():
    
    return render_template('index.html')

@views.route('/map')
def map_render():
    return render_template('my_map')