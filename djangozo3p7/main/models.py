#coding:utf-8
__author__ = "ila"
from django.db import models

from .model import BaseModel

from datetime import datetime



class yezhu(BaseModel):
    __doc__ = u'''yezhu'''
    __tablename__ = 'yezhu'

    __loginUser__='yezhuhao'


    __authTables__={}
    __authPeople__='是'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __loginUserColumn__='yezhuhao'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='否'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    yezhuhao=models.CharField ( max_length=255,null=False,unique=True, verbose_name='业主号' )
    mima=models.CharField ( max_length=255,null=False, unique=False, verbose_name='密码' )
    yezhuxingming=models.CharField ( max_length=255, null=True, unique=False, verbose_name='业主姓名' )
    xingbie=models.CharField ( max_length=255, null=True, unique=False, verbose_name='性别' )
    nianling=models.CharField ( max_length=255, null=True, unique=False, verbose_name='年龄' )
    touxiang=models.CharField ( max_length=255, null=True, unique=False, verbose_name='头像' )
    shouji=models.CharField ( max_length=255, null=True, unique=False, verbose_name='手机' )
    shenfenzheng=models.CharField ( max_length=255, null=True, unique=False, verbose_name='身份证' )
    loufanghao=models.CharField ( max_length=255, null=True, unique=False, verbose_name='楼房号' )
    menpaihao=models.CharField ( max_length=255, null=True, unique=False, verbose_name='门牌号' )
    dizhi=models.CharField ( max_length=255, null=True, unique=False, verbose_name='地址' )
    money=models.FloatField   (  null=True, unique=False,default='0', verbose_name='余额' )
    '''
    yezhuhao=VARCHAR
    mima=VARCHAR
    yezhuxingming=VARCHAR
    xingbie=VARCHAR
    nianling=VARCHAR
    touxiang=VARCHAR
    shouji=VARCHAR
    shenfenzheng=VARCHAR
    loufanghao=VARCHAR
    menpaihao=VARCHAR
    dizhi=VARCHAR
    money=Float
    '''
    class Meta:
        db_table = 'yezhu'
        verbose_name = verbose_name_plural = '业主'
class shangpinleixing(BaseModel):
    __doc__ = u'''shangpinleixing'''
    __tablename__ = 'shangpinleixing'



    __authTables__={}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='否'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    shangpinleixing=models.CharField ( max_length=255,null=False,unique=True, verbose_name='商品类型' )
    '''
    shangpinleixing=VARCHAR
    '''
    class Meta:
        db_table = 'shangpinleixing'
        verbose_name = verbose_name_plural = '商品类型'
class shangpinxinxi(BaseModel):
    __doc__ = u'''shangpinxinxi'''
    __tablename__ = 'shangpinxinxi'



    __authTables__={}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='是'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='前要登'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    shangpinbianhao=models.CharField ( max_length=255, null=True,unique=True, verbose_name='商品编号' )
    shangpinmingcheng=models.CharField ( max_length=255, null=True, unique=False, verbose_name='商品名称' )
    shangpinleixing=models.CharField ( max_length=255, null=True, unique=False, verbose_name='商品类型' )
    tupian=models.CharField ( max_length=255, null=True, unique=False, verbose_name='图片' )
    chandi=models.CharField ( max_length=255, null=True, unique=False, verbose_name='产地' )
    shengchanriqi=models.DateField   (  null=True, unique=False, verbose_name='生产日期' )
    baozhiqi=models.CharField ( max_length=255, null=True, unique=False, verbose_name='保质期' )
    shangpinxiangqing=models.TextField   (  null=True, unique=False, verbose_name='商品详情' )
    clicktime=models.DateTimeField  (  null=True, unique=False, verbose_name='最近点击时间' )
    price=models.FloatField   (  null=True, unique=False, verbose_name='价格' )
    '''
    shangpinbianhao=VARCHAR
    shangpinmingcheng=VARCHAR
    shangpinleixing=VARCHAR
    tupian=VARCHAR
    chandi=VARCHAR
    shengchanriqi=Date
    baozhiqi=VARCHAR
    shangpinxiangqing=Text
    clicktime=DateTime
    price=Float
    '''
    class Meta:
        db_table = 'shangpinxinxi'
        verbose_name = verbose_name_plural = '商品信息'
class jiaofeixinxi(BaseModel):
    __doc__ = u'''jiaofeixinxi'''
    __tablename__ = 'jiaofeixinxi'



    __authTables__={'yezhuhao':'yezhu',}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='是'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='前要登'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    yezhuhao=models.CharField ( max_length=255, null=True, unique=False, verbose_name='业主号' )
    yezhuxingming=models.CharField ( max_length=255, null=True, unique=False, verbose_name='业主姓名' )
    loufanghao=models.CharField ( max_length=255, null=True, unique=False, verbose_name='楼房号' )
    tupian=models.CharField ( max_length=255, null=True, unique=False, verbose_name='图片' )
    jiaofeibiaoti=models.CharField ( max_length=255, null=True, unique=False, verbose_name='缴费标题' )
    jiaofeileixing=models.CharField ( max_length=255, null=True, unique=False, verbose_name='缴费类型' )
    jiaofeijine=models.FloatField   (  null=True, unique=False, verbose_name='缴费金额' )
    dengjishijian=models.DateTimeField  (  null=True, unique=False, verbose_name='登记时间' )
    ispay=models.CharField ( max_length=255, null=True, unique=False,default='未支付', verbose_name='是否支付' )
    userid=models.BigIntegerField  (  null=True, unique=False, verbose_name='用户id' )
    '''
    yezhuhao=VARCHAR
    yezhuxingming=VARCHAR
    loufanghao=VARCHAR
    tupian=VARCHAR
    jiaofeibiaoti=VARCHAR
    jiaofeileixing=VARCHAR
    jiaofeijine=Float
    dengjishijian=DateTime
    ispay=VARCHAR
    userid=BigInteger
    '''
    class Meta:
        db_table = 'jiaofeixinxi'
        verbose_name = verbose_name_plural = '缴费信息'
class cheweixinxi(BaseModel):
    __doc__ = u'''cheweixinxi'''
    __tablename__ = 'cheweixinxi'



    __authTables__={}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='是'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='前要登'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    cheweibianhao=models.CharField ( max_length=255,null=False,unique=True, verbose_name='车位编号' )
    cheweimingcheng=models.CharField ( max_length=255, null=True, unique=False, verbose_name='车位名称' )
    cheweileixing=models.CharField ( max_length=255, null=True, unique=False, verbose_name='车位类型' )
    cheweitupian=models.CharField ( max_length=255, null=True, unique=False, verbose_name='车位图片' )
    dizhi=models.CharField ( max_length=255, null=True, unique=False, verbose_name='地址' )
    cheweiweizhi=models.CharField ( max_length=255, null=True, unique=False, verbose_name='车位位置' )
    shoufeibiaozhun=models.CharField ( max_length=255, null=True, unique=False, verbose_name='收费标准' )
    tingchejiage=models.FloatField   ( null=False, unique=False, verbose_name='停车价格' )
    cheweixiangqing=models.TextField   (  null=True, unique=False, verbose_name='车位详情' )
    zhuangtai=models.CharField ( max_length=255, null=True, unique=False, verbose_name='状态' )
    clicktime=models.DateTimeField  (  null=True, unique=False, verbose_name='最近点击时间' )
    '''
    cheweibianhao=VARCHAR
    cheweimingcheng=VARCHAR
    cheweileixing=VARCHAR
    cheweitupian=VARCHAR
    dizhi=VARCHAR
    cheweiweizhi=VARCHAR
    shoufeibiaozhun=VARCHAR
    tingchejiage=Float
    cheweixiangqing=Text
    zhuangtai=VARCHAR
    clicktime=DateTime
    '''
    class Meta:
        db_table = 'cheweixinxi'
        verbose_name = verbose_name_plural = '车位信息'
class yudingchewei(BaseModel):
    __doc__ = u'''yudingchewei'''
    __tablename__ = 'yudingchewei'



    __authTables__={'yezhuhao':'yezhu',}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='是'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='前要登'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    cheweibianhao=models.CharField ( max_length=255, null=True, unique=False, verbose_name='车位编号' )
    cheweimingcheng=models.CharField ( max_length=255, null=True, unique=False, verbose_name='车位名称' )
    cheweileixing=models.CharField ( max_length=255, null=True, unique=False, verbose_name='车位类型' )
    cheweitupian=models.CharField ( max_length=255, null=True, unique=False, verbose_name='车位图片' )
    cheweiweizhi=models.CharField ( max_length=255, null=True, unique=False, verbose_name='车位位置' )
    shoufeibiaozhun=models.CharField ( max_length=255, null=True, unique=False, verbose_name='收费标准' )
    tingchejiage=models.FloatField   (  null=True, unique=False, verbose_name='停车价格' )
    yuyueshijian=models.DateTimeField  (  null=True, unique=False, verbose_name='预约时间' )
    yezhuhao=models.CharField ( max_length=255, null=True, unique=False, verbose_name='业主号' )
    yezhuxingming=models.CharField ( max_length=255, null=True, unique=False, verbose_name='业主姓名' )
    shouji=models.CharField ( max_length=255, null=True, unique=False, verbose_name='手机' )
    xiadanshijian=models.DateTimeField  (  null=True, unique=False, verbose_name='下单时间' )
    userid=models.BigIntegerField  (  null=True, unique=False, verbose_name='用户id' )
    '''
    cheweibianhao=VARCHAR
    cheweimingcheng=VARCHAR
    cheweileixing=VARCHAR
    cheweitupian=VARCHAR
    cheweiweizhi=VARCHAR
    shoufeibiaozhun=VARCHAR
    tingchejiage=Float
    yuyueshijian=DateTime
    yezhuhao=VARCHAR
    yezhuxingming=VARCHAR
    shouji=VARCHAR
    xiadanshijian=DateTime
    userid=BigInteger
    '''
    class Meta:
        db_table = 'yudingchewei'
        verbose_name = verbose_name_plural = '预定车位'
class ruchangxinxi(BaseModel):
    __doc__ = u'''ruchangxinxi'''
    __tablename__ = 'ruchangxinxi'



    __authTables__={'yezhuhao':'yezhu',}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='是'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='前要登'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    cheweibianhao=models.CharField ( max_length=255, null=True, unique=False, verbose_name='车位编号' )
    cheweimingcheng=models.CharField ( max_length=255, null=True, unique=False, verbose_name='车位名称' )
    cheweileixing=models.CharField ( max_length=255, null=True, unique=False, verbose_name='车位类型' )
    cheweitupian=models.CharField ( max_length=255, null=True, unique=False, verbose_name='车位图片' )
    cheweiweizhi=models.CharField ( max_length=255, null=True, unique=False, verbose_name='车位位置' )
    shoufeibiaozhun=models.CharField ( max_length=255, null=True, unique=False, verbose_name='收费标准' )
    tingchejiage=models.FloatField   (  null=True, unique=False, verbose_name='停车价格' )
    ruchangshijian=models.DateTimeField  (  null=True, unique=False, verbose_name='入场时间' )
    yezhuxingming=models.CharField ( max_length=255, null=True, unique=False, verbose_name='业主姓名' )
    yezhuhao=models.CharField ( max_length=255, null=True, unique=False, verbose_name='业主号' )
    shouji=models.CharField ( max_length=255, null=True, unique=False, verbose_name='手机' )
    crossuserid=models.BigIntegerField  (  null=True, unique=False, verbose_name='跨表用户id' )
    crossrefid=models.BigIntegerField  (  null=True, unique=False, verbose_name='跨表主键id' )
    userid=models.BigIntegerField  (  null=True, unique=False, verbose_name='用户id' )
    '''
    cheweibianhao=VARCHAR
    cheweimingcheng=VARCHAR
    cheweileixing=VARCHAR
    cheweitupian=VARCHAR
    cheweiweizhi=VARCHAR
    shoufeibiaozhun=VARCHAR
    tingchejiage=Float
    ruchangshijian=DateTime
    yezhuxingming=VARCHAR
    yezhuhao=VARCHAR
    shouji=VARCHAR
    crossuserid=BigInteger
    crossrefid=BigInteger
    userid=BigInteger
    '''
    class Meta:
        db_table = 'ruchangxinxi'
        verbose_name = verbose_name_plural = '入场信息'
class chuchangxinxi(BaseModel):
    __doc__ = u'''chuchangxinxi'''
    __tablename__ = 'chuchangxinxi'



    __authTables__={'yezhuhao':'yezhu',}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='是'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='前要登'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    cheweibianhao=models.CharField ( max_length=255, null=True, unique=False, verbose_name='车位编号' )
    cheweimingcheng=models.CharField ( max_length=255, null=True, unique=False, verbose_name='车位名称' )
    cheweileixing=models.CharField ( max_length=255, null=True, unique=False, verbose_name='车位类型' )
    cheweitupian=models.CharField ( max_length=255, null=True, unique=False, verbose_name='车位图片' )
    cheweiweizhi=models.CharField ( max_length=255, null=True, unique=False, verbose_name='车位位置' )
    shoufeibiaozhun=models.CharField ( max_length=255, null=True, unique=False, verbose_name='收费标准' )
    tingchejiage=models.FloatField   (  null=True, unique=False, verbose_name='停车价格' )
    ruchangshijian=models.CharField ( max_length=255, null=True, unique=False, verbose_name='入场时间' )
    chuchangshijian=models.DateTimeField  (  null=True, unique=False, verbose_name='出场时间' )
    yezhuxingming=models.CharField ( max_length=255, null=True, unique=False, verbose_name='业主姓名' )
    yezhuhao=models.CharField ( max_length=255, null=True, unique=False, verbose_name='业主号' )
    shouji=models.CharField ( max_length=255, null=True, unique=False, verbose_name='手机' )
    crossuserid=models.BigIntegerField  (  null=True, unique=False, verbose_name='跨表用户id' )
    crossrefid=models.BigIntegerField  (  null=True, unique=False, verbose_name='跨表主键id' )
    userid=models.BigIntegerField  (  null=True, unique=False, verbose_name='用户id' )
    '''
    cheweibianhao=VARCHAR
    cheweimingcheng=VARCHAR
    cheweileixing=VARCHAR
    cheweitupian=VARCHAR
    cheweiweizhi=VARCHAR
    shoufeibiaozhun=VARCHAR
    tingchejiage=Float
    ruchangshijian=VARCHAR
    chuchangshijian=DateTime
    yezhuxingming=VARCHAR
    yezhuhao=VARCHAR
    shouji=VARCHAR
    crossuserid=BigInteger
    crossrefid=BigInteger
    userid=BigInteger
    '''
    class Meta:
        db_table = 'chuchangxinxi'
        verbose_name = verbose_name_plural = '出场信息'
class tingchefeiyong(BaseModel):
    __doc__ = u'''tingchefeiyong'''
    __tablename__ = 'tingchefeiyong'



    __authTables__={'yezhuhao':'yezhu',}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='是'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='前要登'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    cheweibianhao=models.CharField ( max_length=255, null=True, unique=False, verbose_name='车位编号' )
    cheweimingcheng=models.CharField ( max_length=255, null=True, unique=False, verbose_name='车位名称' )
    cheweileixing=models.CharField ( max_length=255, null=True, unique=False, verbose_name='车位类型' )
    cheweitupian=models.CharField ( max_length=255, null=True, unique=False, verbose_name='车位图片' )
    cheweiweizhi=models.CharField ( max_length=255, null=True, unique=False, verbose_name='车位位置' )
    shoufeibiaozhun=models.CharField ( max_length=255, null=True, unique=False, verbose_name='收费标准' )
    tingchejiage=models.FloatField   (  null=True, unique=False, verbose_name='停车价格' )
    ruchangshijian=models.CharField ( max_length=255, null=True, unique=False, verbose_name='入场时间' )
    chuchangshijian=models.CharField ( max_length=255, null=True, unique=False, verbose_name='出场时间' )
    tingcheshizhang=models.IntegerField  ( null=False, unique=False, verbose_name='停车时长' )
    zongfeiyong=models.FloatField   (  null=True, unique=False, verbose_name='总费用' )
    yezhuxingming=models.CharField ( max_length=255, null=True, unique=False, verbose_name='业主姓名' )
    yezhuhao=models.CharField ( max_length=255, null=True, unique=False, verbose_name='业主号' )
    shouji=models.CharField ( max_length=255, null=True, unique=False, verbose_name='手机' )
    crossuserid=models.BigIntegerField  (  null=True, unique=False, verbose_name='跨表用户id' )
    crossrefid=models.BigIntegerField  (  null=True, unique=False, verbose_name='跨表主键id' )
    ispay=models.CharField ( max_length=255, null=True, unique=False,default='未支付', verbose_name='是否支付' )
    userid=models.BigIntegerField  (  null=True, unique=False, verbose_name='用户id' )
    '''
    cheweibianhao=VARCHAR
    cheweimingcheng=VARCHAR
    cheweileixing=VARCHAR
    cheweitupian=VARCHAR
    cheweiweizhi=VARCHAR
    shoufeibiaozhun=VARCHAR
    tingchejiage=Float
    ruchangshijian=VARCHAR
    chuchangshijian=VARCHAR
    tingcheshizhang=Integer
    zongfeiyong=Float
    yezhuxingming=VARCHAR
    yezhuhao=VARCHAR
    shouji=VARCHAR
    crossuserid=BigInteger
    crossrefid=BigInteger
    ispay=VARCHAR
    userid=BigInteger
    '''
    class Meta:
        db_table = 'tingchefeiyong'
        verbose_name = verbose_name_plural = '停车费用'
class chat(BaseModel):
    __doc__ = u'''chat'''
    __tablename__ = 'chat'



    __authTables__={}
    __foreEndListAuth__='是'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    userid=models.BigIntegerField  ( null=False, unique=False, verbose_name='用户id' )
    adminid=models.BigIntegerField  (  null=True, unique=False, verbose_name='管理员id' )
    ask=models.TextField   (  null=True, unique=False, verbose_name='提问' )
    reply=models.TextField   (  null=True, unique=False, verbose_name='回复' )
    isreply=models.IntegerField  (  null=True, unique=False, verbose_name='是否回复' )
    '''
    userid=BigInteger
    adminid=BigInteger
    ask=Text
    reply=Text
    isreply=Integer
    '''
    class Meta:
        db_table = 'chat'
        verbose_name = verbose_name_plural = '在线咨询'
class cart(BaseModel):
    __doc__ = u'''cart'''
    __tablename__ = 'cart'



    __authTables__={}
    __authSeparate__='是'#后台列表权限
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    tablename=models.CharField ( max_length=255, null=True, unique=False,default='shangpinxinxi', verbose_name='商品表名' )
    userid=models.BigIntegerField  ( null=False, unique=False, verbose_name='用户id' )
    goodid=models.BigIntegerField  ( null=False, unique=False, verbose_name='商品id' )
    goodname=models.CharField ( max_length=255, null=True, unique=False, verbose_name='商品名称' )
    picture=models.CharField ( max_length=255, null=True, unique=False, verbose_name='图片' )
    buynumber=models.IntegerField  ( null=False, unique=False, verbose_name='购买数量' )
    price=models.FloatField   (  null=True, unique=False, verbose_name='单价' )
    discountprice=models.FloatField   (  null=True, unique=False, verbose_name='会员价' )
    '''
    tablename=VARCHAR
    userid=BigInteger
    goodid=BigInteger
    goodname=VARCHAR
    picture=VARCHAR
    buynumber=Integer
    price=Float
    discountprice=Float
    '''
    class Meta:
        db_table = 'cart'
        verbose_name = verbose_name_plural = '购物车表'
class orders(BaseModel):
    __doc__ = u'''orders'''
    __tablename__ = 'orders'



    __authTables__={}
    __authSeparate__='是'#后台列表权限
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    orderid=models.CharField ( max_length=255,null=False,unique=True, verbose_name='订单编号' )
    tablename=models.CharField ( max_length=255, null=True, unique=False,default='shangpinxinxi', verbose_name='商品表名' )
    userid=models.BigIntegerField  ( null=False, unique=False, verbose_name='用户id' )
    goodid=models.BigIntegerField  ( null=False, unique=False, verbose_name='商品id' )
    goodname=models.CharField ( max_length=255, null=True, unique=False, verbose_name='商品名称' )
    picture=models.CharField ( max_length=255, null=True, unique=False, verbose_name='商品图片' )
    buynumber=models.IntegerField  ( null=False, unique=False, verbose_name='购买数量' )
    price=models.FloatField   ( null=False, unique=False,default='0', verbose_name='价格/积分' )
    discountprice=models.FloatField   (  null=True, unique=False,default='0', verbose_name='折扣价格' )
    total=models.FloatField   ( null=False, unique=False,default='0', verbose_name='总价格/总积分' )
    discounttotal=models.FloatField   (  null=True, unique=False,default='0', verbose_name='折扣总价格' )
    type=models.IntegerField  (  null=True, unique=False,default='1', verbose_name='支付类型' )
    status=models.CharField ( max_length=255, null=True, unique=False, verbose_name='状态' )
    address=models.CharField ( max_length=255, null=True, unique=False, verbose_name='地址' )
    tel=models.CharField ( max_length=255, null=True, unique=False, verbose_name='电话' )
    consignee=models.CharField ( max_length=255, null=True, unique=False, verbose_name='收货人' )
    logistics=models.TextField   (  null=True, unique=False, verbose_name='物流' )
    '''
    orderid=VARCHAR
    tablename=VARCHAR
    userid=BigInteger
    goodid=BigInteger
    goodname=VARCHAR
    picture=VARCHAR
    buynumber=Integer
    price=Float
    discountprice=Float
    total=Float
    discounttotal=Float
    type=Integer
    status=VARCHAR
    address=VARCHAR
    tel=VARCHAR
    consignee=VARCHAR
    logistics=Text
    '''
    class Meta:
        db_table = 'orders'
        verbose_name = verbose_name_plural = '订单'
class address(BaseModel):
    __doc__ = u'''address'''
    __tablename__ = 'address'



    __authTables__={}
    __authSeparate__='是'#后台列表权限
    __foreEndListAuth__='是'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    userid=models.BigIntegerField  ( null=False, unique=False, verbose_name='用户id' )
    address=models.CharField ( max_length=255,null=False, unique=False, verbose_name='地址' )
    name=models.CharField ( max_length=255,null=False, unique=False, verbose_name='收货人' )
    phone=models.CharField ( max_length=255,null=False, unique=False, verbose_name='电话' )
    isdefault=models.CharField ( max_length=255,null=False, unique=False, verbose_name='是否默认地址[是/否]' )
    '''
    userid=BigInteger
    address=VARCHAR
    name=VARCHAR
    phone=VARCHAR
    isdefault=VARCHAR
    '''
    class Meta:
        db_table = 'address'
        verbose_name = verbose_name_plural = '地址'
class storeup(BaseModel):
    __doc__ = u'''storeup'''
    __tablename__ = 'storeup'



    __authTables__={}
    __authSeparate__='是'#后台列表权限
    __foreEndListAuth__='是'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    userid=models.BigIntegerField  ( null=False, unique=False, verbose_name='用户id' )
    refid=models.BigIntegerField  (  null=True, unique=False, verbose_name='收藏id' )
    tablename=models.CharField ( max_length=255, null=True, unique=False, verbose_name='表名' )
    name=models.CharField ( max_length=255,null=False, unique=False, verbose_name='收藏名称' )
    picture=models.CharField ( max_length=255,null=False, unique=False, verbose_name='收藏图片' )
    type=models.CharField ( max_length=255, null=True, unique=False,default='1', verbose_name='类型(1:收藏,21:赞,22:踩)' )
    inteltype=models.CharField ( max_length=255, null=True, unique=False, verbose_name='推荐类型' )
    '''
    userid=BigInteger
    refid=BigInteger
    tablename=VARCHAR
    name=VARCHAR
    picture=VARCHAR
    type=VARCHAR
    inteltype=VARCHAR
    '''
    class Meta:
        db_table = 'storeup'
        verbose_name = verbose_name_plural = '收藏表'
class news(BaseModel):
    __doc__ = u'''news'''
    __tablename__ = 'news'



    __authTables__={}
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    title=models.CharField ( max_length=255,null=False, unique=False, verbose_name='标题' )
    introduction=models.TextField   (  null=True, unique=False, verbose_name='简介' )
    picture=models.CharField ( max_length=255,null=False, unique=False, verbose_name='图片' )
    content=models.TextField   ( null=False, unique=False, verbose_name='内容' )
    '''
    title=VARCHAR
    introduction=Text
    picture=VARCHAR
    content=Text
    '''
    class Meta:
        db_table = 'news'
        verbose_name = verbose_name_plural = '社区资讯'
class messages(BaseModel):
    __doc__ = u'''messages'''
    __tablename__ = 'messages'



    __authTables__={}
    __hasMessage__='是'#表属性hasMessage为是，新增留言板表messages,字段content（内容），userid（用户id）
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    userid=models.BigIntegerField  ( null=False, unique=False, verbose_name='留言人id' )
    username=models.CharField ( max_length=255, null=True, unique=False, verbose_name='用户名' )
    content=models.TextField   ( null=False, unique=False, verbose_name='留言内容' )
    cpicture=models.CharField ( max_length=255, null=True, unique=False, verbose_name='留言图片' )
    reply=models.TextField   (  null=True, unique=False, verbose_name='回复内容' )
    rpicture=models.CharField ( max_length=255, null=True, unique=False, verbose_name='回复图片' )
    '''
    userid=BigInteger
    username=VARCHAR
    content=Text
    cpicture=VARCHAR
    reply=Text
    rpicture=VARCHAR
    '''
    class Meta:
        db_table = 'messages'
        verbose_name = verbose_name_plural = '投诉意见'
class discussshangpinxinxi(BaseModel):
    __doc__ = u'''discussshangpinxinxi'''
    __tablename__ = 'discussshangpinxinxi'



    __authTables__={}
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    refid=models.BigIntegerField  ( null=False, unique=False, verbose_name='关联表id' )
    userid=models.BigIntegerField  ( null=False, unique=False, verbose_name='用户id' )
    nickname=models.CharField ( max_length=255, null=True, unique=False, verbose_name='用户名' )
    content=models.TextField   ( null=False, unique=False, verbose_name='评论内容' )
    reply=models.TextField   (  null=True, unique=False, verbose_name='回复内容' )
    '''
    refid=BigInteger
    userid=BigInteger
    nickname=VARCHAR
    content=Text
    reply=Text
    '''
    class Meta:
        db_table = 'discussshangpinxinxi'
        verbose_name = verbose_name_plural = '商品信息评论表'
class discusscheweixinxi(BaseModel):
    __doc__ = u'''discusscheweixinxi'''
    __tablename__ = 'discusscheweixinxi'



    __authTables__={}
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    refid=models.BigIntegerField  ( null=False, unique=False, verbose_name='关联表id' )
    userid=models.BigIntegerField  ( null=False, unique=False, verbose_name='用户id' )
    nickname=models.CharField ( max_length=255, null=True, unique=False, verbose_name='用户名' )
    content=models.TextField   ( null=False, unique=False, verbose_name='评论内容' )
    reply=models.TextField   (  null=True, unique=False, verbose_name='回复内容' )
    '''
    refid=BigInteger
    userid=BigInteger
    nickname=VARCHAR
    content=Text
    reply=Text
    '''
    class Meta:
        db_table = 'discusscheweixinxi'
        verbose_name = verbose_name_plural = '车位信息评论表'
