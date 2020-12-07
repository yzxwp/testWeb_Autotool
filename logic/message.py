# encoding:utf-8
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Member(db.Model):
    uid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(11), unique=True, nullable=False)
    tel = db.Column(db.String(11), unique=True, nullable=False)
    discount = db.Column(db.FLOAT, nullable=False, default=1)
    score = db.Column(db.Integer, nullable=False, default=0)
    active = db.Column(db.Integer, nullable=False, default=1)

    __tablename__ = 'members'

    #注册用户，根据手机号码
    @classmethod
    def add_user_by_tel(cls, tel):
        member = Member()
        member.tel = tel
        db.session.add(member)
        db.session.commit()
        ret_dic = cls.search_by_tel(tel)['members'][0]
        return ret_dic

    # 根据手机号查找会员列表
    @classmethod
    def search_by_tel(cls, tel):
        member_list = []
        type = tel.isdigit()
        member = Member.query.filter(Member.tel.endswith(tel)).first()
        if len(tel) == 11 and type == True and member != None:
            member_info = {'uid': member.uid, 'tel': member.tel, 'discount': member.discount, 'score': member.score,
                           'active': member.active}
            member_list.append(member_info)
            ret_dic = {
                'count': len(member_list),
                'members': member_list
            }
            return ret_dic
        elif len(tel) == 4 and type == True and member != None:
            db_query = Member.query.filter(Member.tel.endswith(tel))
            for member in db_query:
                member_info = {'uid': member.uid, 'tel': member.tel, 'discount': member.discount, 'score': member.score,
                               'active': member.active}
                member_list.append(member_info)
                ret_dic = {
                    'count': len(member_list),
                    'members': member_list
                }
            return ret_dic
        else:
            ret_dic = {
                'return_code': 400,
                'return_msg': 'Get Member by tel failed'
            }
            return ret_dic
