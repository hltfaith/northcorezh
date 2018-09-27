from django.shortcuts import render,redirect,HttpResponse
from asset.models import asset_db
from .tools import excel_export
from django.conf import settings

import os
import sys
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# sys.path.append(BASE_DIR)

# Create your views here.


# 获取资产列表信息
def get_server_asset_info(request):

    db_data = asset_db.objects.all()
    return render(request, 'asset_server_list.html', locals())


# excel文件格式导入数据库
def import_excel():

    # 将转换好的excel数据,写入到数据库
    data = excel_export.xslx_data()

    # 字典遍历出来,写入数据库
    for i in data:
        val = data[i].strip('[]')
        val = str(val).split(",")

        asset_db.objects.create(hostname=eval(val[0]), ip_addr=eval(val[1]), username=eval(val[2]),
                                password=eval(val[3]),
                                model=eval(val[4]), sn=eval(val[5]), local=eval(val[6]), resource_type=eval(val[7]),
                                port=eval(val[8]),
                                system_version=eval(val[9]), group=eval(val[10])
                                )

    return redirect("/asset/server_info/")

# excel文件上传到服务器目录
def excel_upload(request):
    if request.method == "POST":
        # 接收图片
        file = request.FILES['pic']

        # 保存图片
        file_name = os.path.join(settings.MEDIA_ROOT, file.name)  # 图片路径
        with open(file_name, 'wb') as pic:
            for b in file.chunks():
                pic.write(b)

        import_excel()
        return redirect("/asset/server_info/")

    else:
        return HttpResponse('Excel文件接收失败！')



# 资产管理新增设备
def idc_asset_manage(request):

    if request.method == "POST":
        hostname = request.POST.get("hostname")
        ip_addr = request.POST.get("ip_addr")
        username = request.POST.get("username")
        password = request.POST.get("password")

        model = request.POST.get("model")
        sn = request.POST.get("sn")
        local = request.POST.get("local")
        resource_type = request.POST.get("resource_type")

        port = request.POST.get("port")
        system_version = request.POST.get("system_version")
        group = request.POST.get("group")

        asset_obj = asset_db.objects.create(
            hostname=hostname, ip_addr=ip_addr, username=username, password=password,
            model=model, sn=sn, local=local, resource_type=resource_type, port=port,
            system_version=system_version, group=group
        )

        return redirect("/asset/server_info/")

    return render(request, 'asset_idc_manage.html')

# 资产管理删除设备
def idc_asset_delete(request, id):
    asset_db.objects.filter(id=id).delete()

    return redirect("/asset/server_info/")


# 资产管理编辑设备
def idc_asset_change(request, id):
    asset_obj = asset_db.objects.filter(id=id).first()

    if request.method == "POST":
        hostname = request.POST.get("hostname")
        ip_addr = request.POST.get("ip_addr")
        username = request.POST.get("username")
        password = request.POST.get("password")

        model = request.POST.get("model")
        sn = request.POST.get("sn")
        local = request.POST.get("local")
        resource_type = request.POST.get("resource_type")

        port = request.POST.get("port")
        system_version = request.POST.get("system_version")
        group = request.POST.get("group")

        asset_db.objects.filter(id=id).update(
            hostname=hostname, ip_addr=ip_addr, username=username, password=password,
            model=model, sn=sn, local=local, resource_type=resource_type, port=port,
            system_version=system_version, group=group
        )

        return redirect("/asset/server_info/")

    return render(request, 'asset_idc_change.html', {"asset_obj": asset_obj})






# 资产列表
def idc_asset_list(request):
    return render(request, 'asset_idc_list.html')

