from django.shortcuts import render
from app.models import *

# Create your views here.
def equi(request):
    EMPOBJECTS=Emp.objects.select_related('deptno').all()
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(hiredate__year=1981)
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(hiredate__year=1981,sal__gte=2500)
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(deptno__dname='Accounting')
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(deptno__dloc='Dallas')
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(mgr__isnull=True,)
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(comm__isnull=True,)
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(comm__isnull=False)



    d={'EMPOBJECTS':EMPOBJECTS}

    return render(request,'equi.html',d)


def selfjoin(request):
    EMPMGROBJECTS=Emp.objects.select_related('mgr').all()
    EMPMGROBJECTS=Emp.objects.select_related('mgr').filter(mgr__ename='King')
    EMPMGROBJECTS=Emp.objects.select_related('mgr').filter(sal__gte=2000)
    EMPMGROBJECTS=Emp.objects.select_related('mgr').filter(sal__lte=2000)
    EMPMGROBJECTS=Emp.objects.select_related('mgr').filter(mgr__isnull=True)
    EMPMGROBJECTS=Emp.objects.select_related('mgr').filter(mgr__isnull=False)
    EMPMGROBJECTS=Emp.objects.select_related('mgr').filter(mgr__ename='Scott')
    EMPMGROBJECTS=Emp.objects.select_related('mgr').filter(sal__gte=1000)
    EMPMGROBJECTS=Emp.objects.select_related('mgr').filter(sal__lte=1000)
    EMPMGROBJECTS=Emp.objects.select_related('mgr').filter(mgr__ename='King',sal__gte=2000)
    EMPMGROBJECTS=Emp.objects.select_related('mgr').filter(sal__gte=2500)
    EMPMGROBJECTS=Emp.objects.select_related('mgr').filter(ename='Jones')
    EMPMGROBJECTS=Emp.objects.select_related('mgr').filter(sal__gte=2000,ename='Jones')
    EMPMGROBJECTS=Emp.objects.select_related('mgr').filter(sal__gte=2200,ename='king')
    EMPMGROBJECTS=Emp.objects.select_related('mgr').filter(sal__gte=3000)

    d={'EMPMGROBJECTS':EMPMGROBJECTS}
    return render(request,'selfjoin.html',d)

def emp_mgr_deptno(request):
   EMD =Emp.objects.select_related('deptno','mgr').all()
   EMD =Emp.objects.select_related('deptno','mgr').filter(ename='Martin')
   EMD =Emp.objects.select_related('deptno','mgr').filter(deptno__dname='Research')
   EMD =Emp.objects.select_related('deptno','mgr').filter(deptno__dname='Accounting')
   EMD =Emp.objects.select_related('deptno','mgr').filter(deptno__dname='Research',sal__gte=2500)
   EMD =Emp.objects.select_related('deptno','mgr').filter(ename='Smith',deptno__dname='Research')
   EMD =Emp.objects.select_related('deptno','mgr').filter(ename='Smith')
   EMD =Emp.objects.select_related('deptno','mgr').filter(ename='Smith',sal__lte=2000)
   EMD =Emp.objects.select_related('deptno','mgr').filter(deptno__dname='Accounting',sal__gte=3000)
   EMD =Emp.objects.select_related('deptno','mgr').filter(ename='Allen',deptno__dname='Sles')
   EMD =Emp.objects.select_related('deptno','mgr').filter(sal__gte=300)
   EMD =Emp.objects.select_related('deptno','mgr').filter(sal__lte=5000)
   EMD =Emp.objects.select_related('deptno','mgr').filter(mgr__ename='Blake')
   EMD =Emp.objects.select_related('deptno','mgr').filter(mgr__ename='Blake',sal__gte=1000)
   EMD =Emp.objects.select_related('deptno','mgr').filter(mgr__ename='Blake',deptno__dname='Research')
   EMD =Emp.objects.select_related('deptno','mgr').filter(mgr__ename='Blake',sal__gte=2000)
   EMD =Emp.objects.select_related('deptno','mgr').filter(ename='Allen')
   EMD =Emp.objects.select_related('deptno','mgr').filter(deptno__dname='Operations')
   EMD =Emp.objects.select_related('deptno','mgr').filter(hiredate__year=1981)
   EMD =Emp.objects.select_related('deptno','mgr').filter(hiredate__day=20)
   EMD =Emp.objects.select_related('deptno','mgr').filter(hiredate__day=2)
   EMD =Emp.objects.select_related('deptno','mgr').filter(ename='Scott')
   EMD =Emp.objects.select_related('deptno','mgr').filter(ename='King')
   EMD =Emp.objects.select_related('deptno','mgr').filter(ename='Allen',deptno__dname='Research')
   EMD =Emp.objects.select_related('deptno','mgr').filter(ename='Allen',sal__lte=2000)
   EMD =Emp.objects.select_related('deptno','mgr').filter(deptno__dloc='Accounting',sal__lte=3000)
   EMD =Emp.objects.select_related('deptno','mgr').filter(ename='Smith',sal__lte=3000)
   EMD =Emp.objects.select_related('deptno','mgr').filter(hiredate__day=17)
   EMD =Emp.objects.select_related('deptno','mgr').filter(deptno__dname='Research',hiredate__year=1980)
   EMD =Emp.objects.select_related('deptno','mgr').filter(hiredate__month=4)
   EMD =Emp.objects.select_related('deptno','mgr').filter(hiredate__month=2)
   EMD =Emp.objects.select_related('deptno','mgr').filter(mgr__ename__isnull=True)
   EMD =Emp.objects.select_related('deptno','mgr').filter(mgr__ename__isnull=False)
   EMD =Emp.objects.select_related('deptno','mgr').filter(hiredate__year__lte=1990)
   EMD =Emp.objects.select_related('deptno','mgr').filter(hiredate__day__lte=18)
   
   
   










   d={'EMD':EMD}
   return render(request,'emp_mgr_deptno.html',d)