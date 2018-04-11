from django.http import HttpResponseRedirect
from django.http import HttpResponse

from django.shortcuts import render, redirect

from django.core.paginator import Paginator

from . import models

from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
# def students(request):
#     stuList = models.Students.objects.all()
#     return render(request, 'stuManage/students.html', {"stuList":stuList})

# 判断用户是否已登录
def isLogin(request):
    user = request.session.get('user')
    if user:
        return user
    else:
        return None

# 登录界面
def login(request):
    return render(request, 'stuManage/login.html')

# 用户退出
from django.contrib.auth import logout
def uerLogout(request):
    logout(request)
    return redirect('/stuManage/login/')

# 验证验证码
def verifyvalidate(request):
    verifyCode = request.POST.get('verifycode')
    if verifyCode.upper() == request.session['verifycode']:
        return HttpResponse('true')
    else:
        return HttpResponse('false')

# 用户登录
from django.forms.models import model_to_dict
@csrf_exempt
def userLogin(request):
    if request.is_ajax():
        username = request.POST.get('username')
        password = request.POST.get('password')

        verifyCode = request.POST.get('verifycode')
        if verifyCode.upper() == request.session['verifycode']:
            admin = models.Admin.objects.all().filter(ad_number=username).filter(ad_password=password)[0:1]

            print(admin.count())
            if admin.count():
                request.session['user'] = model_to_dict(admin[0])
                request.session.set_expiry(20*60) # 设置session过期时间
                print('ren',username, password)
                print(request.session['user'])
                return HttpResponse('ok')
            else:
                print('render', username, password)
                return HttpResponse('false')
        else:
            return HttpResponse('验证码错误')

# 主页
def index(request):
    if not isLogin(request):
        return redirect('/stuManage/login/')
    else:
        user = request.session['user']
        return render(request, 'stuManage/index.html', {'user': user})

# 学生列表
def students(request, pageN):
    if not isLogin(request):
        return redirect('/stuManage/login/')
    else:
        return redirect('/stuManage/stuList/' + pageN)

# 学生列表
def stuList(request, pageN):
    if not isLogin(request):
        return redirect('/stuManage/login/')
    else:
        user = request.session['user']

        # kw = request.GET.get('kw')
        # print('kw' + kw)
        # if kw.strip:
        #     studentList = models.Students.objects.all().filter(s_name__contains=kw.strip)
        # else:
        # 所有学生
        studentList = models.Students.objects.all()

        paginator = Paginator(studentList, 10)
        pageStuList = paginator.page(int(pageN))
        print(studentList)
        # print(int(pageN), pageStuList.paginator.num_pages, 5)
        pageListHTML = getPageList(int(pageN), pageStuList.paginator.num_pages, '/stuManage/stuList')
        return render(request, 'stuManage/stu_list.html', {"pageStuList":pageStuList, 'user': user, 'pageListHTML':pageListHTML})

# 修改学生页面
def editstu(request, stu_id):
    if not isLogin(request):
        return redirect('/stuManage/login/')
    else:
        user = request.session['user']
        stu = ''
        if stu_id:
            stu = models.Students.objects.get(pk = int(stu_id))
        return render(request, 'stuManage/stu_addoredit.html', {'stu':stu, 'user': user})
# 新增学生页面
def addstu(request):
    if not isLogin(request):
        return redirect('/stuManage/login/')
    else:
        user = request.session['user']
        return render(request, 'stuManage/stu_addoredit.html', {'user': user})

# 执行新增或修改
def addOrEditStu(request):
    if not isLogin(request):
        return redirect('/stuManage/login/')
    else:
        stu_id = request.POST.get('stu_id')
        stu_num = request.POST.get('stu_num')
        stu_name = request.POST.get('stu_name')
        stu_gender = request.POST.get('stu_gender')
        stu_age = request.POST.get('stu_age')
        stu_intro = request.POST.get('stu_intro')
        stu_idnum = request.POST.get('stu_idnum')
        stu_addr = request.POST.get('stu_addr')
        stu_phone = request.POST.get('stu_phone')

        if not stu_id:
            # 新增
            try:
                stu = models.Students.createStudent(stu_num,stu_name,stu_gender,stu_age,stu_intro,stu_idnum,stu_addr,stu_phone)
                stu.save()
                return HttpResponse('ok')
            except:
                return HttpResponse('false')
        else:
            # 修改
            try:
                stu = models.Students.objects.get(pk = int(stu_id))
                stu.s_number = stu_num
                stu.s_name = stu_name
                stu.s_gender = stu_gender
                stu.s_age = stu_age
                stu.s_intro = stu_intro
                stu.s_idnumber = stu_idnum
                stu.s_address = stu_addr
                stu.s_phone = stu_phone
                stu.save()
                return HttpResponse('ok')
            except:
                return HttpResponse('false')

# 导入学生页面
def importstu(request):
    if not isLogin(request):
        return redirect('/stuManage/login/')
    else:
        user = request.session['user']
        return render(request, 'stuManage/stu_import.html', {'user': user})
# 执行导入学生
from stuManage.tools.excelTools import ExcelTools
def importStu(request):
    print('12345')
    if not isLogin(request):
        return redirect('/stuManage/login/')
    else:
        # if request.method == 'POST':
        try:
            stufile = request.FILES.get('stufile')
            # print(stufile)
            exceltool = ExcelTools()
            stuDict = exceltool.readExcelFile2(stufile)
            print(stuDict)

            # 遍历stuDict
            for sheet in stuDict:
                # print(stuDict[sheet])
                if len(stuDict[sheet]) > 0:
                    for line in range(1,len(stuDict[sheet])):
                        print(stuDict[sheet][line])
                        stu_num = stuDict[sheet][line][0]
                        stu_name = stuDict[sheet][line][1]
                        if stuDict[sheet][line][2] == '男':
                            stu_gender = 1
                        else:
                            stu_gender = 0

                        stu_age = stuDict[sheet][line][3]
                        stu_intro = stuDict[sheet][line][4]
                        stu_idnum = stuDict[sheet][line][5]
                        stu_addr = stuDict[sheet][line][6]
                        stu_phone = stuDict[sheet][line][7]
                        stu = models.Students.createStudent(stu_num, stu_name, stu_gender, stu_age, stu_intro,
                                                            stu_idnum, stu_addr, stu_phone)
                        stu.save()

            return HttpResponse('ok')
        except:
            return HttpResponse('false')


# 自定义分页
def getPageList(pageNow, pageCount, url):
    pageListHTML = ''

    if pageCount > 1:
        if pageNow != 1:
            pageListHTML += '<li><a href="%s/%d" aria-label="Previous"><span aria-hidden="true">&laquo;</span></a></li>' % (url, pageNow-1)

        if pageNow-2 <= 0:
            for index in range(1,pageCount+1):
                if pageNow == index:
                    pageListHTML += r'<li class="active"><a>%d</a></li>' % index
                else:
                    pageListHTML += r'<li><a href="%s/%d">%d</a></li>' % (url, index, index)

        elif pageNow+2 >= pageCount:
            for index in range(pageNow-2,pageCount+1):
                if pageNow == index:
                    pageListHTML += '<li class="active"><a>%d</a></li>' % index
                else:
                    pageListHTML += r'<li><a href="%s/%d">%d</a></li>' % (url, index, index)
        else:
            for index in range(pageNow-2,(pageNow+2)+1):
                if pageNow == index:
                    pageListHTML += '<li class="active"><a>%d</a></li>' % index
                else:
                    pageListHTML += r'<li><a href="%s/%d">%d</a></li>' % (url, index, index)

        if pageNow != pageCount:
            pageListHTML += r'<li><a href="%s/%d" aria-label="Next"><span aria-hidden="true">&raquo;</span></a></li>' % (url, pageNow+1)
    else:
        pageListHTML += '<li class="active"><a>1</a></li>'

    return pageListHTML

# 验证码
def showverify(request):
    #引入绘图模块
    from PIL import Image, ImageDraw, ImageFont
    #引入随机函数模块
    import random
    #定义变量，用于画面的背景色、宽、高
    bgcolor = (random.randrange(20, 100), random.randrange(
        20, 100), random.randrange(20, 100))
    width = 100
    height = 50
    #创建画面对象
    im = Image.new('RGB', (width, height), bgcolor)
    #创建画笔对象
    draw = ImageDraw.Draw(im)
    #调用画笔的point()函数绘制噪点
    for i in range(0, 100):
        xy = (random.randrange(0, width), random.randrange(0, height))
        fill = (random.randrange(0, 255), 255, random.randrange(0, 255))
        draw.point(xy, fill=fill)
    #定义验证码的备选值
    str = '1234567890QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm'
    #随机选取4个值作为验证码
    rand_str = ''
    for i in range(0, 4):
        rand_str += str[random.randrange(0, len(str))]
    #构造字体对象
    font = ImageFont.truetype(r'C:\Windows\Fonts\arialbd.ttf', 40)
    #构造字体颜色
    fontcolor1 = (255, random.randrange(0, 255), random.randrange(0, 255))
    fontcolor2 = (255, random.randrange(0, 255), random.randrange(0, 255))
    fontcolor3 = (255, random.randrange(0, 255), random.randrange(0, 255))
    fontcolor4 = (255, random.randrange(0, 255), random.randrange(0, 255))
    #绘制4个字
    draw.text((5, 2), rand_str[0], font=font, fill=fontcolor1)
    draw.text((25, 2), rand_str[1], font=font, fill=fontcolor2)
    draw.text((50, 2), rand_str[2], font=font, fill=fontcolor3)
    draw.text((75, 2), rand_str[3], font=font, fill=fontcolor4)
    #释放画笔
    del draw
    #存入session，用于做进一步验证
    request.session['verifycode'] = rand_str.upper()
    #内存文件操作
    import io
    buf = io.BytesIO()
    #将图片保存在内存中，文件类型为png
    im.save(buf, 'png')
    #将内存中的图片数据返回给客户端，MIME类型为图片png
    return HttpResponse(buf.getvalue(), 'image/png')




def testAJAX(request):
    return render(request, 'stuManage/text_ajax.html')
@csrf_exempt
def TestAJAX(request):
    if request.is_ajax():
        name = request.POST.get('name')
        pwd = request.POST.get('pass')
        print(name , pwd)
        return_json = {'name' : name + 're', 'pass' : pwd + 're'}
        print(return_json)
        return HttpResponse(json.dumps(return_json), content_type='application/json')
        # return HttpResponse('成功！')
    else:
        return HttpResponse('失败！')

def testValidate(request):
    return render(request, 'stuManage/text_validate.html')


