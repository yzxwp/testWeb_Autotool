# encoding:utf-8
from flask import Flask, render_template, request, jsonify
from logic import get_name as names
from logic import get_bank_card
from logic import get_car_vin
from logic import get_idcard
from logic import get_phone
from logic import get_zhongzhengma
from logic import get_scoure_card

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    # 姓名
    name = names.random_name()
    # 车架号
    vin = get_car_vin.random_vin()
    # 身份证号码
    id_card = get_idcard.ident_generator()
    # 电话
    phone = get_phone.phone_num()
    # 中征码
    zzm = get_zhongzhengma.ZZM()
    # 组织机构代码
    zhjgdm = get_scoure_card.create_organization()
    # 统一社会信用代码
    tyshzxm = get_scoure_card.create_social_credit()
    # 中行
    zhonghang = get_bank_card.gen_bank_card_zhongguo()
    # 建行
    jianhang = get_bank_card.gen_bank_card_jainshe()
    # 农行
    nonghang = get_bank_card.gen_bank_card_nonghang()
    # 交行
    jiaohang = get_bank_card.gen_bank_card_jiaotong()
    # 工行
    gonghang = get_bank_card.gen_bank_card_gonghang()
    data = {
        "name": name,
        "vin": vin,
        "id_card": id_card,
        "phone": phone,
        "zzm": zzm,
        "zhjgdm": zhjgdm,
        "tyshzxm": tyshzxm,
        "zhonghang": zhonghang,
        "jianhang": jianhang,
        "nonghang": nonghang,
        "jiaohang": jiaohang,
        "gonghang": gonghang

    }
    return render_template('index.html', **locals())


@app.route('/index1.html')
def index1():
    return render_template("index1.html")


@app.route('/test_all.html')
def index2():
    return render_template('test_all.html')


@app.route('/location.html')
def index3():
    return render_template('location.html')


@app.route('/webelements.html')
def index4():
    return render_template('webelements.html')


@app.route('/10seconds.html')
def index5():
    return render_template('10seconds.html')


@app.route('/frame.html')
def index6():
    return render_template('frame.html')


@app.route('/frame_func.html')
def index7():
    return render_template('frame_func.html')


@app.route('/frame_iframe.html')
def index8():
    return render_template('frame_iframe.html')


@app.route('/frame_content.html')
def index9():
    return render_template('frame_content.html')


@app.route('/monkey.html')
def index10():
    return render_template('monkey.html')


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=80)
